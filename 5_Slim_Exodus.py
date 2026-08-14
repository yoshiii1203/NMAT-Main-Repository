"""
Pipeline 5: Slim Exodus  (NEW -- the previously-missing reproducible step)
============================================================================
dataset/NMAT_Exodus.parquet.bak (wide, output of 4_Citizenship_Integration.py)
    -> dataset/NMAT_Exodus.parquet (narrow, contract-shaped, shipped)
    -> byte-identical copies in both dashboard folders
    -> dataset/EXODUS_MANIFEST.json (row/col counts, md5, column list, timestamp)

Prior to this script, the shipped 54-column dataset/NMAT_Exodus.parquet had no
generating code at all (Audit-01 F2 / Audit-02 F9): someone hand-selected 54
columns from the 118-column pipeline-4 output and the selection existed only
as prose in docs/pipeline_architecture.md. This script makes that step
explicit, deterministic, and asserted.

Target schema: `.claude/audit/_TARGET_SCHEMA_CONTRACT.md` (binding).
Baseline (pre-fix, current shipped file): 178,927 rows x 54 cols.
Contract math (orchestrator-approved): 54 - 5 removed + 3 added = 52.
The 5th removal, `name_based_assessment`, is Task 1 item 2 of the P2 brief
(unused by the citizenship tier logic, disagrees with the final label in
23/871 profiled rows) -- orchestrator ruling folded it into the contract, so
this is no longer a documented deviation, it IS the contract.

--- Two-tier assertions (orchestrator ruling, see coordination log) --------
STRUCTURAL checks (`check_hard`) encode correctness that must hold no matter
what today's data says: shape, one-best-record-per-person, no tautologies,
dtype coercions, dropped columns absent, arithmetic identities, copy parity.
These raise SystemExit and block the chain.

REFERENCE checks (`check_soft`) encode *today's* data (e.g. "134,869 unique
people"). P1's disambiguator fix is expected to legitimately move some of
these numbers (its tie-break is moving off the circular NMS_PER_num). A
correct upstream improvement must not be blocked by a stale headline number,
so these only print a loud WARNING and get recorded in
EXODUS_MANIFEST.json's `reference_count_deltas` block for the orchestrator to
consciously accept or reject -- they never raise.

Author: Automated Pipeline 5
Date:   2026-07-31
"""

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

ROOT = Path("dataset")
SOURCE_BAK = ROOT / "NMAT_Exodus.parquet.bak"
TARGET_PARQUET = ROOT / "NMAT_Exodus.parquet"
MANIFEST_PATH = ROOT / "EXODUS_MANIFEST.json"

DASHBOARD_COPIES = [
    Path("streamlit_dashboard") / "main_dashboard" / "NMAT_Exodus.parquet",
    Path("streamlit_dashboard") / "CHED_relevant_dashboard" / "NMAT_Exodus.parquet",
]

EXPECTED_ROWS = 178_927  # structural -- row count must never change in a slim step

# Reference values (contract section 8) -- see check_soft tier above.
EXPECTED_UNIQUE_PERSONS = 134_869
EXPECTED_BEST_OBSERVABLE = 69_503
EXPECTED_AMBIGUOUS_KEYS = 6_148
# 2026-08 chain re-run after the Pipeline 2 double-crediting fix (get_ple_info()
# name fallback) and the Pipeline 1 -1-sentinel fix. Passer sittings 49,086 ->
# 47,485; observable linkage 45.44% -> 43.31%. The old 49_986 here was doubly
# stale: it predated even the RC-0 percentile-floor fix.
EXPECTED_PLE_PASSERS = 47_485
LINKAGE_RATE_BAND = (0.431, 0.435)

RAW_8 = [
    "Raw_Biology", "Raw_Chemistry", "Raw_InductiveReasoning", "Raw_PerceptualAcuity",
    "Raw_Physics", "Raw_Quantitative", "Raw_SocialScience", "Raw_Verbal",
]

# --- Columns explicitly REMOVED (contract section 1) -----------------------
EXPLICIT_DROP = [
    "IS_PLE_ANALYSIS_SAFE",   # duplicate of IS_PLE_PASSER; replaced by IS_OBSERVABLE_COHORT
    "NMA_College",            # redundant free-text duplicate of UNIVERSITY
    "AllRawComponentsPresent",  # constant, zero information
    "CalcVsDerivedMismatch",    # constant, zero information
    # Found by tests/test_data_invariants.py::test_no_duplicate_bool_columns, NOT by the
    # original audit: HasCEMMatch is byte-identical to HasTRUErawScores (both 178,882 True).
    # They encode one condition -- TRUE raw scores exist precisely when a CEM record matched.
    # Keeping HasTRUErawScores (32 references vs 13, and the clearer name for the data-
    # integrity narrative). Two identical columns is the RC-1 trap; collapse to one.
    "HasCEMMatch",
]
# 5th removal, folded into the contract by orchestrator ruling (Task 1 item 2):
# unused by the citizenship tier decision, disagrees with the final label in
# 23/871 profiled rows. Dropped upstream by 4_Citizenship_Integration.py already.
EXPLICIT_DROP_TASK1 = ["name_based_assessment"]

# --- Columns RENAMED (contract section 3) -----------------------------------
RENAME_MAP = {
    "UNIVERSITY": "UNDERGRAD_UNIVERSITY",
    "UNI_TYPE": "UNDERGRAD_UNI_TYPE",
    "UNI_LOCATION": "UNDERGRAD_UNI_LOCATION",
    "CourseGroup": "UNDERGRAD_COURSE_GROUP",
}

# --- Columns whose dtype must be coerced str -> bool (contract section 4) --
BOOL_COERCE = ["HasTRUErawScores", "StoredVsDerivedMismatch"]

# --- Columns P1 must land for this script to produce a contract-valid file -
P1_NEW_COLUMNS = ["IS_OBSERVABLE_COHORT", "PERSON_KEY_AMBIGUOUS", "IS_BEST_OBSERVABLE_RECORD"]

# Diagnostic provenance columns from P1's Pipeline 2. Carried through when present so the
# dashboards can state WHY a candidate match was not counted, instead of silently showing a
# smaller passer count. Optional: an older Ultima without them still slims cleanly.
#   PLE_MATCH_OUTCOME   -- accepted / rejected / rejected_ambiguous_person / no_match
#   PLE_YEAR_UNCERTAIN  -- accepted passer whose PLE *year* could not be disambiguated
P1_OPTIONAL_COLUMNS = ["PLE_MATCH_OUTCOME", "PLE_YEAR_UNCERTAIN"]

# --- The full pre-rename baseline column list (contract's "54"), taken from
# the currently-shipped dataset/NMAT_Exodus.parquet (Audit-02 appendix,
# confirmed against the live file). Kept columns = BASELINE_54 minus both
# drop lists; renamed/coerced in place afterwards.
BASELINE_54 = [
    "APPNO_CLEAN", "PERSON_KEY", "Year", "SEX", "NMA_College", "UNIVERSITY",
    "UNI_LOCATION", "UNI_TYPE", "CourseGroup", "PercentileBin", "NMS_PER_num",
    "NMS_GPS", "NMS_APT", "NMS_SA", "NMS_VCss", "NMS_IRss", "NMS_Qss", "NMS_PAss",
    "NMS_BIOss", "NMS_PHYss", "NMS_SSCss", "NMS_CHEMss", "TotalRawScoreTRUE",
    "PartIRawScoreTRUE", "PartIIRawScoreTRUE", "Raw_Verbal", "Raw_InductiveReasoning",
    "Raw_Quantitative", "Raw_PerceptualAcuity", "Raw_Biology", "Raw_Physics",
    "Raw_SocialScience", "Raw_Chemistry", "StoredRawTotal", "StoredVsDerivedMismatch",
    "CalculatedRawTotal_Source", "AllRawComponentsPresent", "CalcVsDerivedMismatch",
    "HasTRUErawScores", "HasCEMMatch", "APT_CEM", "SA_CEM", "GPS_CEM", "Percentile_CEM",
    "IS_BEST_NMAT_RECORD", "IS_PLE_PASSER", "IS_PLE_ANALYSIS_SAFE", "PLE_MATCH_METHOD",
    "PLE_MATCH_CONFIDENCE", "PLE_YEAR_PASSED", "PLE_YEAR_GAP", "CITIZENSHIP_FINAL",
    "FOREIGNER_STATUS", "name_based_assessment",
]
assert len(BASELINE_54) == 54, f"BASELINE_54 has {len(BASELINE_54)} entries, expected 54"


def _to_bool(series: pd.Series) -> pd.Series:
    """str-encoded booleans ('True'/'False'/'1.0'/'0.0'/NaN) -> pandas nullable 'boolean'.

    Plain numpy bool cannot hold NaN (StoredVsDerivedMismatch has 79,611 of them);
    the nullable extension dtype keeps missingness explicit instead of silently
    coercing NaN to True/False, and still satisfies pd.api.types.is_bool_dtype().
    """
    mapping = {"True": True, "False": False, "1.0": True, "0.0": False,
               "1": True, "0": False, True: True, False: False}
    return series.map(lambda v: mapping.get(v, pd.NA) if pd.notna(v) else pd.NA).astype("boolean")


def _md5(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build_target_columns(df: pd.DataFrame) -> list[str]:
    """The exact final column list (pre-rename source names), asserted present.

    name_based_assessment (EXPLICIT_DROP_TASK1) is expected to already be absent
    from the .bak -- 4_Citizenship_Integration.py drops it deliberately (Task 1
    item 2) before writing the .bak, so it is not required here.

    Likewise, columns in EXPLICIT_DROP are not *required* to be present: P1 now
    removes IS_PLE_ANALYSIS_SAFE at its source in Pipeline 2 (the correct place to
    kill it), so demanding it here only to drop it made the script fail on a
    correctly-fixed upstream. A drop target that is already gone is success, not
    an error.
    """
    required_baseline = [
        c for c in BASELINE_54
        if c not in EXPLICIT_DROP_TASK1 and c not in EXPLICIT_DROP
    ]
    missing_baseline = [c for c in required_baseline if c not in df.columns]
    if missing_baseline:
        raise SystemExit(
            f"FATAL: source .bak is missing {len(missing_baseline)} expected baseline "
            f"column(s): {missing_baseline}. Cannot build the target schema."
        )
    kept = [c for c in BASELINE_54
            if c not in EXPLICIT_DROP and c not in EXPLICIT_DROP_TASK1]
    missing_p1 = [c for c in P1_NEW_COLUMNS if c not in df.columns]
    if missing_p1:
        raise SystemExit(
            f"BLOCKED: P1 has not yet landed {missing_p1} in NMAT_Ultima.parquet. "
            f"5_Slim_Exodus.py refuses to fabricate a fallback for these columns -- "
            f"per the P2 brief, fail loudly rather than silently degrade. "
            f"Re-run this script after P1's pipeline lands."
        )
    present_optional = [c for c in P1_OPTIONAL_COLUMNS if c in df.columns]
    for c in P1_OPTIONAL_COLUMNS:
        if c not in df.columns:
            print(f"       NOTE: optional provenance column '{c}' absent upstream; skipping")
    return kept + P1_NEW_COLUMNS + present_optional


def main():
    print("=" * 60)
    print("  Pipeline 5: Slim Exodus")
    print("  NMAT_Exodus.parquet.bak -> NMAT_Exodus.parquet")
    print("=" * 60)

    print(f"\n[1/7] Loading {SOURCE_BAK}...")
    if not SOURCE_BAK.exists():
        raise SystemExit(
            f"FATAL: {SOURCE_BAK} not found. Run 4_Citizenship_Integration.py first."
        )
    df = pd.read_parquet(SOURCE_BAK)
    print(f"       Loaded {len(df):,} rows x {len(df.columns)} cols")

    print(f"\n[2/7] Selecting target columns...")
    target_cols = build_target_columns(df)
    print(f"       Target column count: {len(target_cols)} "
          f"({len(target_cols)} = 54 baseline - {len(EXPLICIT_DROP)} contract-removed "
          f"- {len(EXPLICIT_DROP_TASK1)} name_based_assessment + {len(P1_NEW_COLUMNS)} P1-added)")
    df = df[target_cols].copy()

    print(f"\n[3/7] Renaming columns (contract section 3)...")
    for old, new in RENAME_MAP.items():
        assert old in df.columns, f"FATAL: rename source '{old}' missing"
        print(f"       {old} -> {new}")
    df = df.rename(columns=RENAME_MAP)

    print(f"\n[4/7] Coercing str -> bool (contract section 4)...")
    for col in BOOL_COERCE:
        before_dtype = df[col].dtype
        df[col] = _to_bool(df[col])
        print(f"       {col}: {before_dtype} -> {df[col].dtype}")

    print(f"\n[5/7] Asserting invariants (structural = hard fail, reference = warn-only)...")

    def check_hard(label, cond):
        status = "OK" if cond else "FAIL"
        print(f"       [STRUCTURAL {status}] {label}")
        if not cond:
            raise SystemExit(f"CONTRACT VIOLATION (structural): {label}")

    reference_deltas = {}

    def check_soft(name, label, expected, actual, match):
        status = "OK" if match else "WARNING"
        print(f"       [REFERENCE {status}] {label} (expected {expected}, actual {actual})")
        reference_deltas[name] = {
            "expected": expected, "actual": actual, "match": bool(match),
        }
        if not match:
            print(f"       WARNING: '{name}' moved from the documented reference value. "
                  f"This is expected if upstream (P1) legitimately changed matching/dedup "
                  f"logic -- recorded in EXODUS_MANIFEST.json.reference_count_deltas for "
                  f"the orchestrator to accept or reject. NOT blocking the chain.")

    # --- Tier A: structural -------------------------------------------------
    check_hard(f"len(df) == {EXPECTED_ROWS:,}", len(df) == EXPECTED_ROWS)
    check_hard(f"len(df.columns) == {len(target_cols)} (post-rename width preserved)",
               len(df.columns) == len(target_cols))
    check_hard("groupby(PERSON_KEY).IS_BEST_NMAT_RECORD.sum() is 1 for every person",
               df.groupby("PERSON_KEY")["IS_BEST_NMAT_RECORD"].sum().eq(1).all())
    check_hard("IS_BEST_NMAT_RECORD.sum() == PERSON_KEY.nunique() (flag count matches distinct persons)",
               df["IS_BEST_NMAT_RECORD"].sum() == df["PERSON_KEY"].nunique())

    obs = df[df["Year"] <= 2014]
    check_hard("groupby(PERSON_KEY).IS_BEST_OBSERVABLE_RECORD.sum() is 1 for every person in Year<=2014",
               obs.groupby("PERSON_KEY")["IS_BEST_OBSERVABLE_RECORD"].sum().eq(1).all())
    naive = (df["IS_BEST_NMAT_RECORD"] & (df["Year"] <= 2014)).sum()
    check_hard(f"naive filter ({naive:,}) != IS_BEST_OBSERVABLE_RECORD.sum() "
               f"({df['IS_BEST_OBSERVABLE_RECORD'].sum():,}) -- guards the RC bug returning",
               naive != df["IS_BEST_OBSERVABLE_RECORD"].sum())

    check_hard("PERSON_KEY_AMBIGUOUS is constant within each PERSON_KEY",
               df.groupby("PERSON_KEY")["PERSON_KEY_AMBIGUOUS"].nunique().eq(1).all())

    check_hard("IS_OBSERVABLE_COHORT == (Year <= 2014) for all rows",
               (df["IS_OBSERVABLE_COHORT"] == (df["Year"] <= 2014)).all())
    check_hard("IS_OBSERVABLE_COHORT is not a tautological copy of IS_PLE_PASSER",
               not (df["IS_OBSERVABLE_COHORT"] == df["IS_PLE_PASSER"]).all())

    raw_sum = df[RAW_8].sum(axis=1)
    max_diff = (raw_sum - df["TotalRawScoreTRUE"]).abs().max()
    check_hard(f"max |sum(RAW_8) - TotalRawScoreTRUE| < 1e-6 (actual {max_diff:.2e})",
               max_diff < 1e-6)

    check_hard("'IS_PLE_ANALYSIS_SAFE' not in columns", "IS_PLE_ANALYSIS_SAFE" not in df.columns)
    check_hard("'NMA_College' not in columns", "NMA_College" not in df.columns)
    check_hard("'name_based_assessment' not in columns", "name_based_assessment" not in df.columns)

    for col in BOOL_COERCE:
        check_hard(f"{col} dtype is bool-like", pd.api.types.is_bool_dtype(df[col]))

    # --- Tier B: reference counts (today's data, not correctness) ----------
    n_unique = df["PERSON_KEY"].nunique()
    check_soft("unique_persons", "PERSON_KEY.nunique()",
               EXPECTED_UNIQUE_PERSONS, n_unique, n_unique == EXPECTED_UNIQUE_PERSONS)

    n_best_obs = int(df["IS_BEST_OBSERVABLE_RECORD"].sum())
    check_soft("best_observable_record_count", "IS_BEST_OBSERVABLE_RECORD.sum()",
               EXPECTED_BEST_OBSERVABLE, n_best_obs, n_best_obs == EXPECTED_BEST_OBSERVABLE)

    n_ambiguous = int(df.groupby("PERSON_KEY")["PERSON_KEY_AMBIGUOUS"].first().sum())
    check_soft("ambiguous_keys", "PERSON_KEY_AMBIGUOUS distinct-key count",
               EXPECTED_AMBIGUOUS_KEYS, n_ambiguous, n_ambiguous == EXPECTED_AMBIGUOUS_KEYS)

    n_passers = int(df["IS_PLE_PASSER"].sum())
    check_soft("ple_passers", "IS_PLE_PASSER.sum()",
               EXPECTED_PLE_PASSERS, n_passers, n_passers == EXPECTED_PLE_PASSERS)

    linkage_rate = float(df.loc[df["IS_BEST_OBSERVABLE_RECORD"], "IS_PLE_PASSER"].mean())
    lo, hi = LINKAGE_RATE_BAND
    check_soft("observable_linkage_rate", "observable linkage rate",
               f"[{lo*100:.1f}%, {hi*100:.1f}%]", f"{linkage_rate*100:.2f}%",
               lo <= linkage_rate <= hi)

    print(f"\n[6/7] Writing {TARGET_PARQUET} and dashboard copies...")
    df.to_parquet(TARGET_PARQUET, index=False)
    canonical_md5 = _md5(TARGET_PARQUET)
    print(f"       Canonical: {TARGET_PARQUET} ({len(df):,} rows x {len(df.columns)} cols, md5={canonical_md5})")

    copy_md5s = {}
    for dest in DASHBOARD_COPIES:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(TARGET_PARQUET, dest)
        copy_md5s[str(dest)] = _md5(dest)
        print(f"       Copy:      {dest} (md5={copy_md5s[str(dest)]})")

    all_md5s = {canonical_md5, *copy_md5s.values()}
    if len(all_md5s) != 1:
        raise SystemExit(f"CONTRACT VIOLATION (structural): parquet copies are not byte-identical: {all_md5s}")
    print(f"       [STRUCTURAL OK] All {1 + len(DASHBOARD_COPIES)} copies share one md5")

    print(f"\n[7/7] Writing manifest {MANIFEST_PATH}...")
    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "generator": "5_Slim_Exodus.py",
        "source": str(SOURCE_BAK),
        "rows": len(df),
        "columns": len(df.columns),
        "column_list": list(df.columns),
        "md5": canonical_md5,
        "copies": {str(TARGET_PARQUET): canonical_md5, **copy_md5s},
        "reference_count_deltas": reference_deltas,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
    print(f"       [OK] Manifest written ({MANIFEST_PATH})")

    print("\n" + "=" * 60)
    print("  Pipeline 5 complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
