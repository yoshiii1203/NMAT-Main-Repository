"""
Data invariant tests for the shipped NMAT_Exodus.parquet.

This is the FIRST test suite in the repo. It exists to make every root cause
found by the schema audit (`.claude/audit/_TARGET_SCHEMA_CONTRACT.md`,
`.claude/audit/_ORCHESTRATOR_FINDINGS.md`) mechanically un-regressable: a
future change that reintroduces any of these bugs fails a test instead of
shipping silently to a policy dashboard.

Run: `.venv/Scripts/python.exe -m pytest tests/ -v`  (see tests/README.md)

Until Agent P1's corrected NMAT_Ultima.parquet has propagated through
4_Citizenship_Integration.py and 5_Slim_Exodus.py, most of these tests are
EXPECTED TO FAIL against the currently-shipped dataset/NMAT_Exodus.parquet --
that is the point: they define the target state, not the current one.
"""

import hashlib
import json
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
EXODUS_PATH = ROOT / "dataset" / "NMAT_Exodus.parquet"
MANIFEST_PATH = ROOT / "dataset" / "EXODUS_MANIFEST.json"
DASHBOARD_COPIES = [
    ROOT / "streamlit_dashboard" / "main_dashboard" / "NMAT_Exodus.parquet",
    ROOT / "streamlit_dashboard" / "CHED_relevant_dashboard" / "NMAT_Exodus.parquet",
]

# Contract reference values (.claude/audit/_TARGET_SCHEMA_CONTRACT.md section 8)
EXPECTED_ROWS = 178_927
EXPECTED_UNIQUE_PERSONS = 134_869
EXPECTED_BEST_OBSERVABLE = 69_503
EXPECTED_AMBIGUOUS_KEYS = 6_148
EXPECTED_PLE_PASSERS = 49_986
# 52 = 54 baseline - 5 removed (4 contract + name_based_assessment, Task 1
# item 2) + 3 added. Orchestrator-approved into the contract (was originally
# flagged as a deviation; see .claude/audit/logs/P2_pipelines_4_5_tests.md).
EXPECTED_COLUMNS = 52

RAW_8 = [
    "Raw_Biology", "Raw_Chemistry", "Raw_InductiveReasoning", "Raw_PerceptualAcuity",
    "Raw_Physics", "Raw_Quantitative", "Raw_SocialScience", "Raw_Verbal",
]
BIN_ORDER = [f"B{i}" for i in range(1, 11)]

REMOVED_COLUMNS = ["IS_PLE_ANALYSIS_SAFE", "NMA_College", "AllRawComponentsPresent",
                   "CalcVsDerivedMismatch", "name_based_assessment"]
RENAMED_COLUMNS = ["UNDERGRAD_UNIVERSITY", "UNDERGRAD_UNI_TYPE",
                   "UNDERGRAD_UNI_LOCATION", "UNDERGRAD_COURSE_GROUP"]
OLD_RENAMED_NAMES = ["UNIVERSITY", "UNI_TYPE", "UNI_LOCATION", "CourseGroup"]
COERCED_BOOL_COLUMNS = ["HasCEMMatch", "HasTRUErawScores", "StoredVsDerivedMismatch"]


def _md5(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


@pytest.fixture(scope="module")
def df():
    if not EXODUS_PATH.exists():
        pytest.skip(f"{EXODUS_PATH} not found -- run the pipeline chain first")
    return pd.read_parquet(EXODUS_PATH)


# --------------------------------------------------------------------------
# Row / column shape
# --------------------------------------------------------------------------

def test_row_count(df):
    assert len(df) == EXPECTED_ROWS


def test_column_count(df):
    assert len(df.columns) == EXPECTED_COLUMNS, (
        f"got {len(df.columns)} columns: {sorted(df.columns)}"
    )


def test_unique_person_count(df):
    assert df["PERSON_KEY"].nunique() == EXPECTED_UNIQUE_PERSONS


# --------------------------------------------------------------------------
# Removed / renamed / coerced columns (contract sections 1, 3, 4)
# --------------------------------------------------------------------------

@pytest.mark.parametrize("col", REMOVED_COLUMNS)
def test_removed_columns_absent(df, col):
    assert col not in df.columns


@pytest.mark.parametrize("col", RENAMED_COLUMNS)
def test_renamed_columns_present(df, col):
    assert col in df.columns


@pytest.mark.parametrize("old_name", OLD_RENAMED_NAMES)
def test_old_names_absent(df, old_name):
    assert old_name not in df.columns, (
        f"'{old_name}' should have been renamed; no compatibility alias per contract section 3"
    )


@pytest.mark.parametrize("col", COERCED_BOOL_COLUMNS)
def test_coerced_columns_are_real_bool(df, col):
    assert pd.api.types.is_bool_dtype(df[col]), (
        f"{col} has dtype {df[col].dtype}, not bool -- bool('False') is True "
        f"silently inverts truthiness tests on the old str dtype"
    )


# --------------------------------------------------------------------------
# IS_BEST_NMAT_RECORD -- exactly one True per person (contract section 5)
# --------------------------------------------------------------------------

def test_best_nmat_record_exactly_one_per_person(df):
    counts = df.groupby("PERSON_KEY")["IS_BEST_NMAT_RECORD"].sum()
    assert counts.eq(1).all(), (
        f"{(counts == 0).sum()} people have zero best records, "
        f"{(counts > 1).sum()} have more than one"
    )


def test_best_nmat_record_sum_matches_unique_persons(df):
    assert df["IS_BEST_NMAT_RECORD"].sum() == df["PERSON_KEY"].nunique() == EXPECTED_UNIQUE_PERSONS


# --------------------------------------------------------------------------
# IS_OBSERVABLE_COHORT / IS_BEST_OBSERVABLE_RECORD (contract sections 2, 2a)
# --------------------------------------------------------------------------

def test_observable_cohort_matches_year_filter(df):
    assert (df["IS_OBSERVABLE_COHORT"] == (df["Year"] <= 2014)).all()


def test_observable_cohort_is_not_tautological_with_ple_passer(df):
    """The RC-1 bug: IS_PLE_ANALYSIS_SAFE was byte-identical to IS_PLE_PASSER."""
    assert not (df["IS_OBSERVABLE_COHORT"] == df["IS_PLE_PASSER"]).all()


def test_best_observable_record_count(df):
    assert df["IS_BEST_OBSERVABLE_RECORD"].sum() == EXPECTED_BEST_OBSERVABLE


def test_best_observable_record_exactly_one_per_person_in_window(df):
    obs = df[df["Year"] <= 2014]
    counts = obs.groupby("PERSON_KEY")["IS_BEST_OBSERVABLE_RECORD"].sum()
    assert counts.eq(1).all()


def test_naive_best_and_year_filter_is_not_equivalent_to_best_observable(df):
    """Guards against the withdrawn 'IS_BEST_NMAT_RECORD & Year<=2014' shortcut
    (contract section 2a): it drops 3,721 people whose best attempt landed
    after 2014 and silently inflates the linkage rate to 46.69%."""
    naive = (df["IS_BEST_NMAT_RECORD"] & (df["Year"] <= 2014)).sum()
    assert naive != df["IS_BEST_OBSERVABLE_RECORD"].sum()


def test_observable_linkage_rate_in_documented_band(df):
    """45.4-45.8% per contract section 8. The naive-filter shortcut gives
    46.69%, safely outside this band, so this test catches its return."""
    rate = df.loc[df["IS_BEST_OBSERVABLE_RECORD"], "IS_PLE_PASSER"].mean()
    assert 0.454 <= rate <= 0.458, f"observable linkage rate {rate*100:.2f}% outside [45.4%, 45.8%]"


# --------------------------------------------------------------------------
# PERSON_KEY_AMBIGUOUS -- SEX-contradiction only (contract section 2b)
# --------------------------------------------------------------------------

def test_person_key_ambiguous_count(df):
    ambiguous_keys = df.groupby("PERSON_KEY")["PERSON_KEY_AMBIGUOUS"].first().sum()
    assert ambiguous_keys == EXPECTED_AMBIGUOUS_KEYS


def test_person_key_ambiguous_constant_within_key(df):
    """The flag is a per-person property; every row for one PERSON_KEY must agree."""
    nunique_per_key = df.groupby("PERSON_KEY")["PERSON_KEY_AMBIGUOUS"].nunique()
    assert nunique_per_key.eq(1).all()


# --------------------------------------------------------------------------
# No column is a perfect duplicate of another (RC-1 class of bug)
# --------------------------------------------------------------------------

def test_no_duplicate_bool_columns(df):
    bool_cols = [c for c in df.columns if pd.api.types.is_bool_dtype(df[c])]
    duplicates = []
    for i, a in enumerate(bool_cols):
        for b in bool_cols[i + 1:]:
            if df[a].equals(df[b]):
                duplicates.append((a, b))
    assert not duplicates, f"byte-identical bool column pairs found (RC-1 class): {duplicates}"


# --------------------------------------------------------------------------
# Raw score arithmetic
# --------------------------------------------------------------------------

def test_total_raw_score_equals_sum_of_components(df):
    sub = df.dropna(subset=RAW_8 + ["TotalRawScoreTRUE"])
    diff = (sub[RAW_8].sum(axis=1) - sub["TotalRawScoreTRUE"]).abs()
    assert diff.max() < 1e-6


def test_part_i_plus_part_ii_equals_total(df):
    sub = df.dropna(subset=["PartIRawScoreTRUE", "PartIIRawScoreTRUE", "TotalRawScoreTRUE"])
    diff = (sub["PartIRawScoreTRUE"] + sub["PartIIRawScoreTRUE"] - sub["TotalRawScoreTRUE"]).abs()
    assert diff.max() < 1e-6


# --------------------------------------------------------------------------
# Percentile bin orientation -- B1 is the LOWEST decile
# --------------------------------------------------------------------------

def test_b1_is_lowest_decile_monotonic_raw_score(df):
    means = df.groupby("PercentileBin")["TotalRawScoreTRUE"].mean().reindex(BIN_ORDER)
    assert means.notna().all(), f"missing bins: {means[means.isna()].index.tolist()}"
    diffs = means.diff().dropna()
    assert (diffs > 0).all(), (
        f"mean TotalRawScoreTRUE is not strictly increasing B1->B10: {means.to_dict()}"
    )


# --------------------------------------------------------------------------
# PLE passer counting (contract section 7)
# --------------------------------------------------------------------------

def test_is_ple_passer_authoritative_count(df):
    assert df["IS_PLE_PASSER"].sum() == EXPECTED_PLE_PASSERS


def test_ple_linkage_metadata_is_not_nested_with_passer_flag(df):
    """PLE_YEAR_PASSED / PLE_MATCH_METHOD / PLE_YEAR_GAP are diagnostic
    metadata, not passer indicators -- the sets deliberately do not nest
    inside IS_PLE_PASSER. If these counts have genuinely moved (e.g. P1
    changed the matching cascade), update the expected values here rather
    than deleting the assertion -- the point is that SOMEONE looks at the
    new numbers before they ship."""
    year_not_passer = ((df["PLE_YEAR_PASSED"].notna()) & (~df["IS_PLE_PASSER"])).sum()
    passer_no_year = ((df["IS_PLE_PASSER"]) & (df["PLE_YEAR_PASSED"].isna())).sum()
    assert year_not_passer > 0 and passer_no_year > 0, (
        "PLE_YEAR_PASSED now nests perfectly inside IS_PLE_PASSER -- either the "
        "matching pipeline changed for the better (update docs) or a regression "
        "silently made these two columns redundant (investigate)."
    )
    if (year_not_passer, passer_no_year) != (7_318, 2_776):
        pytest.fail(
            f"non-nested counts changed from documented (7318, 2776) to "
            f"({year_not_passer}, {passer_no_year}). This may be legitimate if "
            f"P1's matching cascade changed -- update EXPECTED and contract "
            f"section 7 together, don't just silence this test."
        )


# --------------------------------------------------------------------------
# File integrity -- three copies, one md5
# --------------------------------------------------------------------------

def test_dashboard_copies_are_byte_identical():
    if not EXODUS_PATH.exists():
        pytest.skip("canonical parquet not found")
    missing = [p for p in DASHBOARD_COPIES if not p.exists()]
    if missing:
        pytest.skip(f"dashboard copies not found: {missing}")
    canonical_md5 = _md5(EXODUS_PATH)
    for copy in DASHBOARD_COPIES:
        assert _md5(copy) == canonical_md5, f"{copy} diverges from {EXODUS_PATH}"


def test_manifest_md5_matches_canonical_file():
    if not MANIFEST_PATH.exists():
        pytest.skip(f"{MANIFEST_PATH} not found -- run 5_Slim_Exodus.py first")
    manifest = json.loads(MANIFEST_PATH.read_text())
    assert manifest["md5"] == _md5(EXODUS_PATH)
    assert manifest["rows"] == EXPECTED_ROWS
    assert manifest["columns"] == EXPECTED_COLUMNS
