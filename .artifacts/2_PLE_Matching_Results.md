# ============================================================
# CELL 1 — Install dependencies
# ============================================================
# !pip -q install -U pandas numpy pyarrow unidecode tqdm matplotlib seaborn
# ============================================================
# CELL 2 — Imports, paths, config
# ============================================================
from pathlib import Path
import re
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm.auto import tqdm
from unidecode import unidecode

warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", 200)
pd.set_option("display.max_rows", 100)

# -------------------------------------------------------------------
# PATHS — adjust ROOT if your folder differs
# -------------------------------------------------------------------
ROOT_CANDIDATES = [Path("/root/dataset"), Path("root/dataset"), Path("dataset")]
ROOT = next((p for p in ROOT_CANDIDATES if p.exists()), None)
assert ROOT is not None, "Dataset folder not found."

NMAT_FINAL_PATH    = ROOT / "NMAT_FINAL.csv"
PLE_DATA_PATH      = ROOT / "PLE_DATA.csv"
PLE_UNMATCHED_PATH = ROOT / "PLE_UNMATCHED.csv"
PLE_STILL_UNMATCHED_PATH = ROOT / "output" / "PLE_STILL_UNMATCHED.csv"

OUTDIR = ROOT / "output"
OUTDIR.mkdir(parents=True, exist_ok=True)

ULTIMA_PATH = ROOT / "NMAT_Ultima.csv"

assert NMAT_FINAL_PATH.exists(),    f"Missing: {NMAT_FINAL_PATH}"
assert PLE_DATA_PATH.exists(),      f"Missing: {PLE_DATA_PATH}"
assert PLE_UNMATCHED_PATH.exists(), f"Missing: {PLE_UNMATCHED_PATH}"
# Note: PLE_STILL_UNMATCHED_PATH might not exist until the file is placed, so we won't assert it strictly initially

# -------------------------------------------------------------------
# MATCHING CONFIG
# -------------------------------------------------------------------
YEAR_GAP_MIN          = 5    # PLE_YEAR - NMAT_YEAR >= 5 (medical school takes ≥4 yrs + boards)
PERCENTILE_FLOOR      = 40   # Percentile cutoff for disambiguation

print("ROOT:", ROOT)
print("NMAT_FINAL_PATH:", NMAT_FINAL_PATH)
print("PLE_DATA_PATH:", PLE_DATA_PATH)
print("PLE_UNMATCHED_PATH:", PLE_UNMATCHED_PATH)
print("YEAR_GAP_MIN:", YEAR_GAP_MIN)
print("PERCENTILE_FLOOR:", PERCENTILE_FLOOR)
ROOT: dataset
NMAT_FINAL_PATH: dataset\NMAT_FINAL.csv
PLE_DATA_PATH: dataset\PLE_DATA.csv
PLE_UNMATCHED_PATH: dataset\PLE_UNMATCHED.csv
YEAR_GAP_MIN: 5
PERCENTILE_FLOOR: 40
# ============================================================
# CELL 3 — Name normalization helpers
# ============================================================

def normalize_name(x) -> str:
    """
    Normalize a Filipino name for matching.
    1. Strip accents (Añes → Anes)
    2. Uppercase
    3. Remove punctuation except commas and spaces
    4. Collapse whitespace
    5. Strip leading/trailing
    Returns empty string if null/empty.
    """
    if pd.isna(x):
        return ""
    x = str(x)
    x = unidecode(x)          # strip diacritics
    x = x.upper()
    x = re.sub(r"[^A-Z0-9, ]+", " ", x)   # keep letters, digits, comma, space
    x = re.sub(r"\s+", " ", x).strip()
    return x


def clean_appno(x) -> str:
    """Strip non-digits from applicant number."""
    if pd.isna(x):
        return ""
    s = re.sub(r"\D", "", str(x))
    return s if s else ""


def clean_year(x):
    """Convert year to int; return NaN if not parseable."""
    try:
        v = int(float(str(x).strip()))
        return v if 1990 <= v <= 2030 else np.nan
    except Exception:
        return np.nan


# Quick sanity tests
assert normalize_name("Añes, Marvin") == "ANES, MARVIN"
assert normalize_name("ABANDO, ALEJANDRO LUIS ARELLANO") == "ABANDO, ALEJANDRO LUIS ARELLANO"
assert clean_appno("1070637") == "1070637"
assert clean_appno(None) == ""

print("Name normalization helpers OK.")
Name normalization helpers OK.
# ============================================================
# CELL 4 — Load all three source files
# ============================================================

# ── NMAT_FINAL ────────────────────────────────────────────
nmat = pd.read_csv(NMAT_FINAL_PATH, dtype=str, low_memory=False)

num_cols = [
    "Year", "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA",
    "NMS_VCss","NMS_IRss","NMS_Qss","NMS_PAss",
    "NMS_BIOss","NMS_PHYss","NMS_SSCss","NMS_CHEMss",
    "TotalRawScoreTRUE","PartIRawScoreTRUE","PartIIRawScoreTRUE",
    "Raw_Verbal","Raw_InductiveReasoning","Raw_Quantitative","Raw_PerceptualAcuity",
    "Raw_Biology","Raw_Physics","Raw_SocialScience","Raw_Chemistry",
    "StoredRawTotal","CalculatedRawTotal_Source",
    "APT_CEM","SA_CEM","GPS_CEM","Percentile_CEM"
]
for col in num_cols:
    if col in nmat.columns:
        nmat[col] = pd.to_numeric(nmat[col], errors="coerce")

# Normalize names and keys
nmat["NAME_NORM"]   = nmat["NMA_Name"].map(normalize_name)
nmat["APPNO_CLEAN"] = nmat["NMA_AppNo"].map(clean_appno)
nmat["YEAR_INT"]    = nmat["Year"].map(clean_year)

print(f"NMAT_FINAL loaded:     {len(nmat):,} rows  |  {nmat['APPNO_CLEAN'].nunique():,} unique AppNos")
print(f"  Name coverage:       {nmat['NAME_NORM'].ne('').sum():,} non-empty names")

# ── PLE_DATA ──────────────────────────────────────────────
ple = pd.read_csv(PLE_DATA_PATH, dtype=str)
ple.columns = [c.strip() for c in ple.columns]
ple["FULL_NAME"]       = ple["FULL_NAME"].str.strip()
ple["PLE_YEAR_PASSED"] = ple["PLE_YEAR_PASSED"].map(clean_year)
ple["NAME_NORM"]       = ple["FULL_NAME"].map(normalize_name)

print(f"\nPLE_DATA loaded:       {len(ple):,} rows")
print(f"  Year range:          {int(ple['PLE_YEAR_PASSED'].min())} – {int(ple['PLE_YEAR_PASSED'].max())}")
print(f"  Unique names:        {ple['NAME_NORM'].nunique():,}")

# ── PLE_UNMATCHED ─────────────────────────────────────────
unmatched = pd.read_csv(PLE_UNMATCHED_PATH, dtype=str)
unmatched.columns = [c.strip() for c in unmatched.columns]
unmatched["FULL_NAME"]  = unmatched["FULL_NAME"].str.strip()
unmatched["NMA_AppNo"]  = unmatched["NMA_AppNo"].fillna("").str.strip()
unmatched["NAME_NORM"]  = unmatched["FULL_NAME"].map(normalize_name)
unmatched["APPNO_CLEAN"]= unmatched["NMA_AppNo"].map(clean_appno)

has_appno = unmatched["APPNO_CLEAN"].ne("").sum()
print(f"\nPLE_UNMATCHED loaded:  {len(unmatched):,} rows")
print(f"  With AppNo filled:   {has_appno:,}")
print(f"  AppNo empty:         {len(unmatched) - has_appno:,}")

# ── PLE_STILL_UNMATCHED ───────────────────────────────────
ple_still_unmatched = pd.read_csv(PLE_STILL_UNMATCHED_PATH, dtype=str)
ple_still_unmatched.columns = [c.strip() for c in ple_still_unmatched.columns]
# Determine which AppNo column is present
appno_col = "NMA_AppNo" if "NMA_AppNo" in ple_still_unmatched.columns else "MATCHED_APPNO"
if appno_col in ple_still_unmatched.columns:
    ple_still_unmatched["NMA_AppNo"] = ple_still_unmatched[appno_col].fillna("").str.strip()
else:
    ple_still_unmatched["NMA_AppNo"] = ""
ple_still_unmatched["APPNO_CLEAN"] = ple_still_unmatched["NMA_AppNo"].map(clean_appno)
ple_still_unmatched["NAME_NORM"] = ple_still_unmatched["PLE_NAME_NORM"] # Usually it's PLE_NAME_NORM
print(f"\nPLE_STILL_UNMATCHED loaded:  {len(ple_still_unmatched):,} rows")
print(f"  With AppNo filled:         {ple_still_unmatched['APPNO_CLEAN'].ne('').sum():,}")
NMAT_FINAL loaded:     178,927 rows  |  178,926 unique AppNos
  Name coverage:       178,927 non-empty names

PLE_DATA loaded:       43,630 rows
  Year range:          2011 – 2022
  Unique names:        43,630

PLE_UNMATCHED loaded:  6,600 rows
  With AppNo filled:   2,332
  AppNo empty:         4,268
PLE_STILL_UNMATCHED loaded:  7,207 rows
  With AppNo filled:         321
# ============================================================
# CELL 4 — Load all three source files
# ============================================================

# ── NMAT_FINAL ────────────────────────────────────────────
nmat = pd.read_csv(NMAT_FINAL_PATH, dtype=str, low_memory=False)

num_cols = [
    "Year", "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA",
    "NMS_VCss","NMS_IRss","NMS_Qss","NMS_PAss",
    "NMS_BIOss","NMS_PHYss","NMS_SSCss","NMS_CHEMss",
    "TotalRawScoreTRUE","PartIRawScoreTRUE","PartIIRawScoreTRUE",
    "Raw_Verbal","Raw_InductiveReasoning","Raw_Quantitative","Raw_PerceptualAcuity",
    "Raw_Biology","Raw_Physics","Raw_SocialScience","Raw_Chemistry",
    "StoredRawTotal","CalculatedRawTotal_Source",
    "APT_CEM","SA_CEM","GPS_CEM","Percentile_CEM"
]
for col in num_cols:
    if col in nmat.columns:
        nmat[col] = pd.to_numeric(nmat[col], errors="coerce")

# Normalize names and keys
nmat["NAME_NORM"]   = nmat["NMA_Name"].map(normalize_name)
nmat["APPNO_CLEAN"] = nmat["NMA_AppNo"].map(clean_appno)
nmat["YEAR_INT"]    = nmat["Year"].map(clean_year)

print(f"NMAT_FINAL loaded:     {len(nmat):,} rows  |  {nmat['APPNO_CLEAN'].nunique():,} unique AppNos")
print(f"  Name coverage:       {nmat['NAME_NORM'].ne('').sum():,} non-empty names")

# ── PLE_DATA ──────────────────────────────────────────────
ple = pd.read_csv(PLE_DATA_PATH, dtype=str)
ple.columns = [c.strip() for c in ple.columns]
ple["FULL_NAME"]       = ple["FULL_NAME"].str.strip()
ple["PLE_YEAR_PASSED"] = ple["PLE_YEAR_PASSED"].map(clean_year)
ple["NAME_NORM"]       = ple["FULL_NAME"].map(normalize_name)

print(f"\nPLE_DATA loaded:       {len(ple):,} rows")
print(f"  Year range:          {int(ple['PLE_YEAR_PASSED'].min())} – {int(ple['PLE_YEAR_PASSED'].max())}")
print(f"  Unique names:        {ple['NAME_NORM'].nunique():,}")

# ── PLE_UNMATCHED ─────────────────────────────────────────
unmatched = pd.read_csv(PLE_UNMATCHED_PATH, dtype=str)
unmatched.columns = [c.strip() for c in unmatched.columns]
unmatched["FULL_NAME"]  = unmatched["FULL_NAME"].str.strip()
unmatched["NMA_AppNo"]  = unmatched["NMA_AppNo"].fillna("").str.strip()
unmatched["NAME_NORM"]  = unmatched["FULL_NAME"].map(normalize_name)
unmatched["APPNO_CLEAN"]= unmatched["NMA_AppNo"].map(clean_appno)

has_appno = unmatched["APPNO_CLEAN"].ne("").sum()
print(f"\nPLE_UNMATCHED loaded:  {len(unmatched):,} rows")
print(f"  With AppNo filled:   {has_appno:,}")
print(f"  AppNo empty:         {len(unmatched) - has_appno:,}")

# ── PLE_STILL_UNMATCHED ───────────────────────────────────
ple_still_unmatched = pd.read_csv(PLE_STILL_UNMATCHED_PATH, dtype=str)
ple_still_unmatched.columns = [c.strip() for c in ple_still_unmatched.columns]
# Determine which AppNo column is present
appno_col = "NMA_AppNo" if "NMA_AppNo" in ple_still_unmatched.columns else "MATCHED_APPNO"
if appno_col in ple_still_unmatched.columns:
    ple_still_unmatched["NMA_AppNo"] = ple_still_unmatched[appno_col].fillna("").str.strip()
else:
    ple_still_unmatched["NMA_AppNo"] = ""
ple_still_unmatched["APPNO_CLEAN"] = ple_still_unmatched["NMA_AppNo"].map(clean_appno)
ple_still_unmatched["NAME_NORM"] = ple_still_unmatched["PLE_NAME_NORM"] # Usually it's PLE_NAME_NORM
print(f"\nPLE_STILL_UNMATCHED loaded:  {len(ple_still_unmatched):,} rows")
print(f"  With AppNo filled:         {ple_still_unmatched['APPNO_CLEAN'].ne('').sum():,}")
NMAT_FINAL loaded:     178,927 rows  |  178,926 unique AppNos
  Name coverage:       178,927 non-empty names

PLE_DATA loaded:       43,630 rows
  Year range:          2011 – 2022
  Unique names:        43,630

PLE_UNMATCHED loaded:  6,600 rows
  With AppNo filled:   2,332
  AppNo empty:         4,268

PLE_STILL_UNMATCHED loaded:  7,207 rows
  With AppNo filled:         321
# ============================================================
# CELL 5 — Build NMAT lookup structures
# ============================================================

# Group all NMAT rows by normalized name
# Each group is a list of row dicts (representing all attempts by that person)
nmat_records = nmat.to_dict("records")

from collections import defaultdict
nmat_by_name = defaultdict(list)
nmat_by_appno = {}

for row in nmat_records:
    name = row["NAME_NORM"]
    appno = row["APPNO_CLEAN"]
    if name:
        nmat_by_name[name].append(row)
    if appno:
        nmat_by_appno[appno] = row

nmat_name_choices = sorted(nmat_by_name.keys())

print(f"Unique NMAT names indexed:   {len(nmat_name_choices):,}")
print(f"Unique NMAT AppNos indexed:  {len(nmat_by_appno):,}")

# Person-level dedup for reporting
# Two rows = same person if same NAME_NORM + same BDATE
nmat["BDATE_CLEAN"] = nmat["BDATE"].fillna("").str.strip()
person_id_cols = ["NAME_NORM", "BDATE_CLEAN"]
nmat["PERSON_KEY"] = nmat["NAME_NORM"] + "||" + nmat["BDATE_CLEAN"]
unique_persons = nmat["PERSON_KEY"].nunique()
attempt_counts = nmat.groupby("PERSON_KEY")["APPNO_CLEAN"].count()

print(f"\nUnique persons (name+BDATE):  {unique_persons:,}")
print(f"Took NMAT once:               {(attempt_counts == 1).sum():,}")
print(f"Took NMAT 2+ times:           {(attempt_counts > 1).sum():,}")
print(f"Max attempts by one person:   {attempt_counts.max()}")
Unique NMAT names indexed:   123,736
Unique NMAT AppNos indexed:  178,926

Unique persons (name+BDATE):  134,869
Took NMAT once:               101,155
Took NMAT 2+ times:           33,714
Max attempts by one person:   9
# ============================================================
# CELL 6 — Disambiguation helper
# ============================================================

def disambiguate(candidates: list, ple_year: int, ple_name_norm: str) -> dict:
    """
    Apply teacher's disambiguation rules to a list of NMAT candidate rows.
    Returns a result dict with keys:
        selected_row, status, reason, n_before_filter, n_after_filter
    
    Status values:
        FINAL_MATCH        — one clean winner
        AMBIGUOUS          — still multiple after all filters
        NO_VALID_MATCH     — zero remain after filters
    """
    n_before = len(candidates)

    # ── Step 1: Year gap filter ────────────────────────────────────
    # PLE_YEAR - NMAT_YEAR >= YEAR_GAP_MIN
    gap_pass = [
        r for r in candidates
        if (
            pd.notna(r.get("YEAR_INT"))
            and (ple_year - r["YEAR_INT"]) >= YEAR_GAP_MIN
        )
    ]

    if not gap_pass:
        return {
            "selected_row": None,
            "status": "NO_VALID_MATCH",
            "reason": f"All {n_before} candidates failed year gap filter (gap < {YEAR_GAP_MIN})",
            "n_before_filter": n_before,
            "n_after_filter": 0
        }

    # ── Step 2: Identity filter (DOB + Sex) ───────────────────────
    # Group by BDATE+SEX.  Keep records where DOB matches majority.
    # If DOB is missing for all → skip this step.
    has_dob = [r for r in gap_pass if r.get("BDATE_CLEAN", "") not in ("", "00/00/0000", "nan")]

    if has_dob:
        # If DOBs are present, prefer records that share the most common DOB
        from collections import Counter
        dob_counts = Counter(r.get("BDATE_CLEAN", "") for r in has_dob)
        modal_dob = dob_counts.most_common(1)[0][0]
        identity_pass = [r for r in gap_pass if r.get("BDATE_CLEAN", "") == modal_dob]
        if not identity_pass:
            identity_pass = gap_pass  # fall back if no DOB consensus
    else:
        identity_pass = gap_pass  # no DOB available → keep all

    # ── Step 3: Take latest NMAT year ──────────────────────────────
    max_year = max(
        r["YEAR_INT"] for r in identity_pass if pd.notna(r.get("YEAR_INT"))
    )
    latest_pass = [r for r in identity_pass if r.get("YEAR_INT") == max_year]

    # ── Step 4: Percentile rule ────────────────────────────────────
    pct_pass = [
        r for r in latest_pass
        if pd.notna(r.get("NMS_PER_num")) and r["NMS_PER_num"] >= PERCENTILE_FLOOR
    ]

    # If none pass percentile filter, check if all are missing percentile
    all_pct_missing = all(pd.isna(r.get("NMS_PER_num")) for r in latest_pass)
    if all_pct_missing:
        pct_pass = latest_pass  # can't apply rule, keep all

    if not pct_pass:
        return {
            "selected_row": None,
            "status": "NO_VALID_MATCH",
            "reason": f"Percentile < {PERCENTILE_FLOOR} for all latest-year candidates",
            "n_before_filter": n_before,
            "n_after_filter": 0
        }

    # ── Step 5: Final verdict ──────────────────────────────────────
    if len(pct_pass) == 1:
        return {
            "selected_row": pct_pass[0],
            "status": "FINAL_MATCH",
            "reason": f"1 candidate after all filters (gap≥{YEAR_GAP_MIN}, latest year, pct≥{PERCENTILE_FLOOR})",
            "n_before_filter": n_before,
            "n_after_filter": 1
        }

    # Still multiple — take highest percentile as tiebreak, else ambiguous
    top = max(
        pct_pass,
        key=lambda r: r.get("NMS_PER_num") if pd.notna(r.get("NMS_PER_num")) else -1
    )
    runners = [r for r in pct_pass if r is not top]
    # If top is clearly better (5+ percentile points) → accept
    top_pct = top.get("NMS_PER_num", np.nan)
    runner_pct = max(
        (r.get("NMS_PER_num", np.nan) for r in runners),
        default=np.nan
    )

    if pd.notna(top_pct) and pd.notna(runner_pct) and (top_pct - runner_pct) >= 5:
        return {
            "selected_row": top,
            "status": "FINAL_MATCH",
            "reason": f"Tiebreak: highest percentile ({top_pct:.0f} vs {runner_pct:.0f}) after all filters",
            "n_before_filter": n_before,
            "n_after_filter": len(pct_pass)
        }

    return {
        "selected_row": top,   # include best guess but flag as AMBIGUOUS
        "status": "AMBIGUOUS",
        "reason": f"{len(pct_pass)} candidates remain after all filters — manual review needed",
        "n_before_filter": n_before,
        "n_after_filter": len(pct_pass)
    }


print("Disambiguation helper defined.")
Disambiguation helper defined.
# ============================================================
# CELL 7 — Stage 0: PLE_UNMATCHED with pre-filled AppNo
# ============================================================

print("=" * 60)
print("STAGE 0: Manual AppNo matches from PLE_UNMATCHED.csv")
print("=" * 60)

unmatched_with_appno = unmatched[unmatched["APPNO_CLEAN"].ne("")].copy()
unmatched_no_appno   = unmatched[unmatched["APPNO_CLEAN"].eq("") ].copy()

print(f"PLE_UNMATCHED rows WITH AppNo:    {len(unmatched_with_appno):,}")
print(f"PLE_UNMATCHED rows WITHOUT AppNo: {len(unmatched_no_appno):,}")

# Join on AppNo to NMAT
stage0_results = []

for _, row in unmatched_with_appno.iterrows():
    appno = row["APPNO_CLEAN"]
    nmat_row = nmat_by_appno.get(appno)

    if nmat_row is not None:
        stage0_results.append({
            "PLE_FULL_NAME":       row["FULL_NAME"],
            "PLE_NAME_NORM":       row["NAME_NORM"],
            "PLE_YEAR_PASSED":     np.nan,      # not in PLE_UNMATCHED (no year column)
            "MATCHED_APPNO":       appno,
            "MATCHED_NMA_Name":    nmat_row.get("NMA_Name"),
            "MATCHED_YEAR_INT":    nmat_row.get("YEAR_INT"),
            "MATCHED_NMS_PER_num": nmat_row.get("NMS_PER_num"),
            "YEAR_GAP":            np.nan,
            "MATCH_METHOD":        "MANUAL_APPNO_MATCH",
            "MATCH_STATUS":        "FINAL_MATCH",
            "MATCH_CONFIDENCE":    100,
            "MATCH_REASON":        "Pre-filled AppNo from PLE_UNMATCHED.csv — direct join"
        })
    else:
        stage0_results.append({
            "PLE_FULL_NAME":       row["FULL_NAME"],
            "PLE_NAME_NORM":       row["NAME_NORM"],
            "PLE_YEAR_PASSED":     np.nan,
            "MATCHED_APPNO":       appno,
            "MATCHED_NMA_Name":    None,
            "MATCHED_YEAR_INT":    np.nan,
            "MATCHED_NMS_PER_num": np.nan,
            "YEAR_GAP":            np.nan,
            "MATCH_METHOD":        "MANUAL_APPNO_MATCH",
            "MATCH_STATUS":        "APPNO_NOT_IN_NMAT",   # AppNo given but not found in NMAT_FINAL
            "MATCH_CONFIDENCE":    0,
            "MATCH_REASON":        "AppNo from PLE_UNMATCHED not found in NMAT_FINAL"
        })

stage0_df = pd.DataFrame(stage0_results)
found_s0   = (stage0_df["MATCH_STATUS"] == "FINAL_MATCH").sum()
missing_s0 = (stage0_df["MATCH_STATUS"] != "FINAL_MATCH").sum()

print(f"\nStage 0 results:")
print(f"  Matched via AppNo:    {found_s0:,}")
print(f"  AppNo not in NMAT:    {missing_s0:,}")

# The remaining unmatched (no AppNo) go to Stage 3 name matching
ple_unmatched_to_name_match = unmatched_no_appno.copy()
print(f"\n  Proceeding to name matching: {len(ple_unmatched_to_name_match):,} records")
============================================================
STAGE 0: Manual AppNo matches from PLE_UNMATCHED.csv
============================================================
PLE_UNMATCHED rows WITH AppNo:    2,332
PLE_UNMATCHED rows WITHOUT AppNo: 4,268

Stage 0 results:
  Matched via AppNo:    2,331
  AppNo not in NMAT:    1

  Proceeding to name matching: 4,268 records
# ============================================================
# CELL 8 — Build master PLE list with source tags
# ============================================================

# PLE_DATA: all 43,630 passers
# PLE_UNMATCHED (no AppNo): additional 6,600 that failed prior match

ple_all = ple[["FULL_NAME", "PLE_YEAR_PASSED", "NAME_NORM"]].copy()
ple_all["SOURCE"] = "PLE_DATA"

# For PLE_UNMATCHED with no AppNo: they are a SUBSET of PLE_DATA
# We should not double-count them.
# The PLE_UNMATCHED file represents PLE_DATA records that failed prior exact match.
# We'll attempt to match all PLE_DATA records via our own algorithm,
# so PLE_UNMATCHED without AppNo is implicitly covered.
# Stage 0 already handled the ones WITH AppNo separately.

print(f"PLE_DATA records to match (all): {len(ple_all):,}")
print(f"Already resolved in Stage 0:     {found_s0:,}  (these will be excluded from name-match stages)")

# Names already resolved in Stage 0
stage0_resolved_names = set(
    stage0_df[stage0_df["MATCH_STATUS"] == "FINAL_MATCH"]["PLE_NAME_NORM"].tolist()
)

# For name matching we process all PLE_DATA; Stage 0 results take priority
print(f"Names pre-resolved by Stage 0:   {len(stage0_resolved_names):,}")
PLE_DATA records to match (all): 43,630
Already resolved in Stage 0:     2,331  (these will be excluded from name-match stages)
Names pre-resolved by Stage 0:   2,330
# ============================================================
# CELL 9 — Stage 1: Exact name match on all PLE_DATA
# ============================================================

print("=" * 60)
print("STAGE 1: Exact name match — PLE_DATA vs NMAT_FINAL")
print("=" * 60)

exact_match_results = []

for _, ple_row in tqdm(ple_all.iterrows(), total=len(ple_all), desc="Exact matching"):
    pname      = ple_row["NAME_NORM"]
    ple_year   = ple_row["PLE_YEAR_PASSED"]
    full_name  = ple_row["FULL_NAME"]

    # Skip if already resolved by Stage 0
    if pname in stage0_resolved_names:
        continue

    candidates = nmat_by_name.get(pname, [])

    if len(candidates) == 0:
        # No exact match → goes to Stage 2 (fuzzy)
        exact_match_results.append({
            "PLE_FULL_NAME":       full_name,
            "PLE_NAME_NORM":       pname,
            "PLE_YEAR_PASSED":     ple_year,
            "MATCHED_APPNO":       None,
            "MATCHED_NMA_Name":    None,
            "MATCHED_YEAR_INT":    np.nan,
            "MATCHED_NMS_PER_num": np.nan,
            "YEAR_GAP":            np.nan,
            "MATCH_METHOD":        "EXACT",
            "MATCH_STATUS":        "NEEDS_FUZZY",
            "MATCH_CONFIDENCE":    0,
            "MATCH_REASON":        "No exact name match found"
        })

    elif len(candidates) == 1:
        # Single exact match — still apply year gap check
        r = candidates[0]
        year_int = r.get("YEAR_INT")
        gap = (ple_year - year_int) if (pd.notna(ple_year) and pd.notna(year_int)) else np.nan

        if pd.notna(gap) and gap < YEAR_GAP_MIN:
            exact_match_results.append({
                "PLE_FULL_NAME":       full_name,
                "PLE_NAME_NORM":       pname,
                "PLE_YEAR_PASSED":     ple_year,
                "MATCHED_APPNO":       r.get("APPNO_CLEAN"),
                "MATCHED_NMA_Name":    r.get("NMA_Name"),
                "MATCHED_YEAR_INT":    year_int,
                "MATCHED_NMS_PER_num": r.get("NMS_PER_num"),
                "YEAR_GAP":            gap,
                "MATCH_METHOD":        "EXACT",
                "MATCH_STATUS":        "NO_VALID_MATCH",
                "MATCH_CONFIDENCE":    95,
                "MATCH_REASON":        f"Single exact match but year gap {gap:.0f} < {YEAR_GAP_MIN}"
            })
        else:
            exact_match_results.append({
                "PLE_FULL_NAME":       full_name,
                "PLE_NAME_NORM":       pname,
                "PLE_YEAR_PASSED":     ple_year,
                "MATCHED_APPNO":       r.get("APPNO_CLEAN"),
                "MATCHED_NMA_Name":    r.get("NMA_Name"),
                "MATCHED_YEAR_INT":    year_int,
                "MATCHED_NMS_PER_num": r.get("NMS_PER_num"),
                "YEAR_GAP":            gap,
                "MATCH_METHOD":        "EXACT",
                "MATCH_STATUS":        "FINAL_MATCH",
                "MATCH_CONFIDENCE":    100,
                "MATCH_REASON":        "Single exact name match, year gap OK"
            })

    else:
        # Multiple exact matches → disambiguate
        result = disambiguate(candidates, int(ple_year) if pd.notna(ple_year) else 9999, pname)
        sel    = result["selected_row"]
        status = result["status"]
        year_int = sel.get("YEAR_INT") if sel else np.nan
        gap = (ple_year - year_int) if (pd.notna(ple_year) and pd.notna(year_int)) else np.nan

        exact_match_results.append({
            "PLE_FULL_NAME":       full_name,
            "PLE_NAME_NORM":       pname,
            "PLE_YEAR_PASSED":     ple_year,
            "MATCHED_APPNO":       sel.get("APPNO_CLEAN") if sel else None,
            "MATCHED_NMA_Name":    sel.get("NMA_Name") if sel else None,
            "MATCHED_YEAR_INT":    year_int,
            "MATCHED_NMS_PER_num": sel.get("NMS_PER_num") if sel else np.nan,
            "YEAR_GAP":            gap,
            "MATCH_METHOD":        "EXACT",
            "MATCH_STATUS":        status,
            "MATCH_CONFIDENCE":    100 if status == "FINAL_MATCH" else 50,
            "MATCH_REASON":        result["reason"]
        })

exact_df = pd.DataFrame(exact_match_results)

print(f"\nExact match results:")
print(exact_df["MATCH_STATUS"].value_counts(dropna=False).to_string())
print(f"\nTotal processed: {len(exact_df):,}")
============================================================
STAGE 1: Exact name match — PLE_DATA vs NMAT_FINAL
============================================================
Exact matching: 100%
 43630/43630 [00:01<00:00, 36482.62it/s]
Exact match results:
MATCH_STATUS
FINAL_MATCH       33970
NEEDS_FUZZY        4208
NO_VALID_MATCH     2350
AMBIGUOUS           772

Total processed: 41,300
# ============================================================
# CELL 10 — Stage 2: Deterministic AppNo Match
# ============================================================

print("=" * 60)
print("STAGE 2: Deterministic AppNo Match")
print("=" * 60)

deterministic_results = []
has_appno_records = ple_still_unmatched[ple_still_unmatched["APPNO_CLEAN"].ne("")]
no_appno_records = ple_still_unmatched[ple_still_unmatched["APPNO_CLEAN"].eq("")]

print(f"Records with AppNo to match deterministically: {len(has_appno_records):,}")
print(f"Records missing AppNo:                       {len(no_appno_records):,}")

for _, row in has_appno_records.iterrows():
    appno = row["APPNO_CLEAN"]
    nmat_row = nmat_by_appno.get(appno)
    if nmat_row is not None:
        deterministic_results.append({
            "PLE_FULL_NAME":       row["PLE_FULL_NAME"],
            "PLE_NAME_NORM":       row["NAME_NORM"],
            "PLE_YEAR_PASSED":     float(row["PLE_YEAR_PASSED"]) if pd.notna(row["PLE_YEAR_PASSED"]) and str(row["PLE_YEAR_PASSED"]).strip() != '' else np.nan,
            "MATCHED_APPNO":       appno,
            "MATCHED_NMA_Name":    nmat_row.get("NMA_Name"),
            "MATCHED_YEAR_INT":    nmat_row.get("YEAR_INT"),
            "MATCHED_NMS_PER_num": nmat_row.get("NMS_PER_num"),
            "YEAR_GAP":            np.nan, # or calculate it if needed
            "MATCH_METHOD":        "DETERMINISTIC_APPNO",
            "MATCH_STATUS":        "FINAL_MATCH",
            "MATCH_CONFIDENCE":    100,
            "MATCH_REASON":        "Matched deterministically via provided NMA_AppNo"
        })
    else:
        deterministic_results.append({
            "PLE_FULL_NAME":       row["PLE_FULL_NAME"],
            "PLE_NAME_NORM":       row["NAME_NORM"],
            "PLE_YEAR_PASSED":     float(row["PLE_YEAR_PASSED"]) if pd.notna(row["PLE_YEAR_PASSED"]) and str(row["PLE_YEAR_PASSED"]).strip() != '' else np.nan,
            "MATCHED_APPNO":       appno,
            "MATCHED_NMA_Name":    None,
            "MATCHED_YEAR_INT":    np.nan,
            "MATCHED_NMS_PER_num": np.nan,
            "YEAR_GAP":            np.nan,
            "MATCH_METHOD":        "DETERMINISTIC_APPNO",
            "MATCH_STATUS":        "APPNO_NOT_IN_NMAT",
            "MATCH_CONFIDENCE":    0,
            "MATCH_REASON":        "Provided NMA_AppNo not found in NMAT_FINAL"
        })

for _, row in no_appno_records.iterrows():
    deterministic_results.append({
        "PLE_FULL_NAME":       row["PLE_FULL_NAME"],
        "PLE_NAME_NORM":       row["NAME_NORM"],
        "PLE_YEAR_PASSED":     float(row["PLE_YEAR_PASSED"]) if pd.notna(row["PLE_YEAR_PASSED"]) and str(row["PLE_YEAR_PASSED"]).strip() != '' else np.nan,
        "MATCHED_APPNO":       None,
        "MATCHED_NMA_Name":    None,
        "MATCHED_YEAR_INT":    np.nan,
        "MATCHED_NMS_PER_num": np.nan,
        "YEAR_GAP":            np.nan,
        "MATCH_METHOD":        "DETERMINISTIC_APPNO",
        "MATCH_STATUS":        "UNMATCHED_NO_APPNO",
        "MATCH_CONFIDENCE":    0,
        "MATCH_REASON":        "Empty NMA_AppNo and no determinable CEM data link"
    })

deterministic_df = pd.DataFrame(deterministic_results)
if len(deterministic_df) > 0:
    print(f"\nDeterministic match results:")
    print(deterministic_df["MATCH_STATUS"].value_counts(dropna=False).to_string())
else:
    print("\nNo deterministic match results.")
============================================================
STAGE 2: Deterministic AppNo Match
============================================================
Records with AppNo to match deterministically: 321
Records missing AppNo:                       6,886

Deterministic match results:
MATCH_STATUS
UNMATCHED_NO_APPNO    6886
FINAL_MATCH            321
# ============================================================
# CELL 11 — Combine all match results into master match table
# ============================================================

print("=" * 60)
print("Combining all match stages into master match table")
print("=" * 60)

# Stage 0 — manual AppNo matches
stage0_final = stage0_df.copy()
stage0_final["SOURCE_STAGE"] = "STAGE0_MANUAL_APPNO"

# Stage 1 — exact matches (exclude NEEDS_FUZZY rows, those went to fuzzy)
exact_final = exact_df[exact_df["MATCH_STATUS"] != "NEEDS_FUZZY"].copy()
exact_final["SOURCE_STAGE"] = "STAGE1_EXACT"

# Stage 2 — deterministic results
deterministic_final = deterministic_df.copy()
deterministic_final["SOURCE_STAGE"] = "STAGE2_DETERMINISTIC_APPNO"

# Standard columns across all stages
std_cols = [
    "PLE_FULL_NAME", "PLE_NAME_NORM", "PLE_YEAR_PASSED",
    "MATCHED_APPNO", "MATCHED_NMA_Name", "MATCHED_YEAR_INT",
    "MATCHED_NMS_PER_num", "YEAR_GAP",
    "MATCH_METHOD", "MATCH_STATUS", "MATCH_CONFIDENCE", "MATCH_REASON",
    "SOURCE_STAGE"
]

# Ensure all stages have all columns
for df in [stage0_final, exact_final, deterministic_final]:
    for col in std_cols:
        if col not in df.columns:
            df[col] = np.nan

master_match = pd.concat(
    [
        stage0_final[std_cols],
        exact_final[std_cols],
        deterministic_final[std_cols]
    ],
    ignore_index=True
)

# De-duplicate: if same PLE_NAME_NORM resolved by multiple stages,
# keep the highest confidence / best status result
# Priority: FINAL_MATCH > MANUAL_APPNO_MATCH > DETERMINISTIC_APPNO > AMBIGUOUS > ...
status_priority = {
    "FINAL_MATCH": 1,
    "MANUAL_APPNO_MATCH": 1,
    "DETERMINISTIC_APPNO": 1,
    "AMBIGUOUS": 3,
    "NO_VALID_MATCH": 5,
    "UNMATCHED_FINAL": 6,
    "APPNO_NOT_IN_NMAT": 6,
    "UNMATCHED_NO_APPNO": 6,
    "NEEDS_FUZZY": 99
}

master_match["STATUS_RANK"] = master_match["MATCH_STATUS"].map(
    lambda s: status_priority.get(str(s), 99)
)

master_match = (
    master_match
    .sort_values(["PLE_NAME_NORM", "STATUS_RANK", "MATCH_CONFIDENCE"],
                 ascending=[True, True, False])
    .drop_duplicates(subset=["PLE_NAME_NORM"], keep="first")
    .drop(columns=["STATUS_RANK"])
    .reset_index(drop=True)
)

master_match.to_csv(OUTDIR / "PLE_MATCH_MASTER.csv", index=False)

print(f"\nMaster match table: {len(master_match):,} PLE records")
print("\nFinal MATCH_STATUS breakdown:")
print(master_match["MATCH_STATUS"].value_counts(dropna=False).to_string())
print("\nBy METHOD:")
print(master_match["MATCH_METHOD"].value_counts(dropna=False).to_string())
============================================================
Combining all match stages into master match table
============================================================
Master match table: 43,601 PLE records

Final MATCH_STATUS breakdown:
MATCH_STATUS
FINAL_MATCH           36395
UNMATCHED_NO_APPNO     4135
NO_VALID_MATCH         2298
AMBIGUOUS               772
APPNO_NOT_IN_NMAT         1

By METHOD:
MATCH_METHOD
EXACT                  37040
DETERMINISTIC_APPNO     4230
MANUAL_APPNO_MATCH      2331
# ============================================================
# CELL 12 — Apply IS_PLE_PASSER flag to NMAT_FINAL
# ============================================================

print("=" * 60)
print("Applying PLE match flags to NMAT_FINAL → NMAT_Ultima")
print("=" * 60)

# Only accepted statuses contribute to IS_PLE_PASSER = True for clean analysis
accepted_statuses = {"FINAL_MATCH", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"}
analysis_safe      = {"FINAL_MATCH", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"}

# Build AppNo → PLE match info lookup
# Only rows with a valid MATCHED_APPNO
appno_to_ple = {}
for _, mrow in master_match.iterrows():
    appno = str(mrow.get("MATCHED_APPNO", "") or "").strip()
    if appno and appno != "nan":
        appno_to_ple[appno] = mrow.to_dict()

# Also build name-based lookup for records without AppNo match
# (handles cases where same name matched but no specific AppNo assigned)
name_to_ple = {}
for _, mrow in master_match.iterrows():
    name = str(mrow.get("PLE_NAME_NORM", "") or "").strip()
    if name:
        name_to_ple[name] = mrow.to_dict()

# Apply to NMAT_FINAL row by row
# An NMAT row is "PLE matched" if:
#   1. Its APPNO_CLEAN appears in appno_to_ple, OR
#   2. Its NAME_NORM appears in name_to_ple AND no specific AppNo was matched
#      (i.e., MATCHED_APPNO is null in match table — handles name-only matches)

def get_ple_info(nmat_row: dict) -> dict:
    appno = nmat_row.get("APPNO_CLEAN", "")
    name  = nmat_row.get("NAME_NORM", "")

    info = appno_to_ple.get(appno)
    if info is None:
        info = name_to_ple.get(name)

    if info is None:
        return {
            "PLE_MATCH_STATUS":     "NOT_IN_PLE",
            "PLE_MATCH_METHOD":     None,
            "PLE_YEAR_PASSED":      np.nan,
            "PLE_YEAR_GAP":         np.nan,
            "PLE_MATCH_CONFIDENCE": np.nan,
            "PLE_MATCH_REASON":     None,
            "IS_PLE_PASSER":        False,
            "IS_PLE_ANALYSIS_SAFE": False,
        }

    status = str(info.get("MATCH_STATUS", ""))
    return {
        "PLE_MATCH_STATUS":     status,
        "PLE_MATCH_METHOD":     info.get("MATCH_METHOD"),
        "PLE_YEAR_PASSED":      info.get("PLE_YEAR_PASSED"),
        "PLE_YEAR_GAP":         info.get("YEAR_GAP"),
        "PLE_MATCH_CONFIDENCE": info.get("MATCH_CONFIDENCE"),
        "PLE_MATCH_REASON":     info.get("MATCH_REASON"),
        "IS_PLE_PASSER":        status in accepted_statuses,
        "IS_PLE_ANALYSIS_SAFE": status in analysis_safe,
    }

# Apply to all rows
ple_flags = [get_ple_info(r) for r in tqdm(nmat.to_dict("records"), desc="Applying PLE flags")]
ple_flags_df = pd.DataFrame(ple_flags)

# Merge back
nmat_ultima = pd.concat(
    [nmat.reset_index(drop=True), ple_flags_df.reset_index(drop=True)],
    axis=1
)

print(f"\nNMAT_Ultima shape: {nmat_ultima.shape}")
print(f"\nIS_PLE_PASSER distribution:")
print(nmat_ultima["IS_PLE_PASSER"].value_counts(dropna=False).to_string())
print(f"\nPLE_MATCH_STATUS distribution:")
print(nmat_ultima["PLE_MATCH_STATUS"].value_counts(dropna=False).to_string())
============================================================
Applying PLE match flags to NMAT_FINAL → NMAT_Ultima
============================================================
Applying PLE flags: 100%
 178927/178927 [00:00<00:00, 879165.94it/s]
NMAT_Ultima shape: (178927, 114)

IS_PLE_PASSER distribution:
IS_PLE_PASSER
False    128941
True      49986

PLE_MATCH_STATUS distribution:
PLE_MATCH_STATUS
NOT_IN_PLE        121623
FINAL_MATCH        49986
NO_VALID_MATCH      5595
AMBIGUOUS           1723
# ============================================================
# CELL 13 — IS_BEST_NMAT_RECORD flag
# ============================================================
# Among all NMAT attempts by a PLE passer, exactly ONE row should be
# flagged as the "selected" record used in analysis.
# For matched records: the row whose APPNO_CLEAN == MATCHED_APPNO in match table.
# For unmatched persons: the row with highest percentile (latest year tiebreak).

print("=" * 60)
print("Flagging IS_BEST_NMAT_RECORD")
print("=" * 60)

nmat_ultima["IS_BEST_NMAT_RECORD"] = False

# For PLE-matched rows: the specifically matched AppNo row is the best record
matched_appnos = set(
    str(v) for v in master_match.loc[
        master_match["MATCH_STATUS"].isin(accepted_statuses), "MATCHED_APPNO"
    ].dropna().tolist()
)

nmat_ultima.loc[
    nmat_ultima["APPNO_CLEAN"].isin(matched_appnos),
    "IS_BEST_NMAT_RECORD"
] = True

# For unmatched persons (not PLE passers): flag best record per PERSON_KEY
# (highest percentile, then latest year) — useful for person-level analysis
unmatched_mask = ~nmat_ultima["IS_PLE_PASSER"]
unmatched_nmat = nmat_ultima[unmatched_mask].copy()

best_idx = (
    unmatched_nmat
    .sort_values(
        ["PERSON_KEY", "NMS_PER_num", "YEAR_INT"],
        ascending=[True, False, False],
        na_position="last"
    )
    .groupby("PERSON_KEY")
    .head(1)
    .index
)

nmat_ultima.loc[best_idx, "IS_BEST_NMAT_RECORD"] = True

best_records = nmat_ultima["IS_BEST_NMAT_RECORD"].sum()
print(f"IS_BEST_NMAT_RECORD = True:  {best_records:,}  rows")
print(f"  of which IS_PLE_PASSER:    {nmat_ultima[nmat_ultima['IS_BEST_NMAT_RECORD'] & nmat_ultima['IS_PLE_PASSER']].shape[0]:,}")
print(f"  of which NOT PLE passer:   {nmat_ultima[nmat_ultima['IS_BEST_NMAT_RECORD'] & ~nmat_ultima['IS_PLE_PASSER']].shape[0]:,}")
============================================================
Flagging IS_BEST_NMAT_RECORD
============================================================
IS_BEST_NMAT_RECORD = True:  133,804  rows
  of which IS_PLE_PASSER:    36,305
  of which NOT PLE passer:   97,499
# ============================================================
# CELL 14 — Save NMAT_Ultima.csv
# ============================================================

# Reorder: PLE columns come after university columns, before score columns
ple_new_cols = [
    "IS_PLE_PASSER",
    "IS_PLE_ANALYSIS_SAFE",
    "IS_BEST_NMAT_RECORD",
    "PLE_MATCH_STATUS",
    "PLE_MATCH_METHOD",
    "PLE_YEAR_PASSED",
    "PLE_YEAR_GAP",
    "PLE_MATCH_CONFIDENCE",
    "PLE_MATCH_REASON",
]

existing_cols = [c for c in nmat_ultima.columns if c not in ple_new_cols]

# Insert PLE cols after "evidence_summary" column if it exists
try:
    insert_after = existing_cols.index("evidence_summary") + 1
except ValueError:
    insert_after = 40  # fallback

final_col_order = (
    existing_cols[:insert_after]
    + ple_new_cols
    + existing_cols[insert_after:]
)

nmat_ultima = nmat_ultima[final_col_order]
nmat_ultima.to_csv(ULTIMA_PATH, index=False)
nmat_ultima.to_parquet(str(ULTIMA_PATH).replace(".csv", ".parquet"), index=False)

print(f"✅ NMAT_Ultima saved: {ULTIMA_PATH}")
print(f"   Shape: {nmat_ultima.shape}")
print(f"   Columns: {len(nmat_ultima.columns)}")
✅ NMAT_Ultima saved: dataset\NMAT_Ultima.csv
   Shape: (178927, 115)
   Columns: 115
# ============================================================
# CELL 15 — Comprehensive validation report
# ============================================================

print("=" * 70)
print("COMPREHENSIVE VALIDATION REPORT")
print("=" * 70)

total_ple     = len(ple)
total_nmat    = len(nmat_ultima)
total_persons = nmat_ultima["PERSON_KEY"].nunique()

# PLE matching summary
ms = master_match["MATCH_STATUS"].value_counts(dropna=False)

final_matched = ms.get("FINAL_MATCH", 0) + ms.get("MANUAL_APPNO_MATCH", 0) + ms.get("DETERMINISTIC_APPNO", 0)
ambiguous     = ms.get("AMBIGUOUS", 0)
no_valid      = ms.get("NO_VALID_MATCH", 0)
unmatched_fin = ms.get("UNMATCHED_FINAL", 0)
unmatched_no_appno = ms.get("UNMATCHED_NO_APPNO", 0)

print(f"\n{'─'*55}")
print(f"PLE PASSERS (2011–2022)")
print(f"{'─'*55}")
print(f"  Total PLE passers:                  {total_ple:>8,}")
print(f"  FINAL_MATCH (exact/manual/appno):   {final_matched:>8,}  ({final_matched/total_ple*100:.2f}%)")
print(f"  AMBIGUOUS (flagged, included):      {ambiguous:>8,}  ({ambiguous/total_ple*100:.2f}%)")
print(f"  NO_VALID_MATCH:                     {no_valid:>8,}  ({no_valid/total_ple*100:.2f}%)")
print(f"  UNMATCHED_FINAL:                    {unmatched_fin:>8,}  ({unmatched_fin/total_ple*100:.2f}%)")
print(f"  UNMATCHED_NO_APPNO:                 {unmatched_no_appno:>8,}  ({unmatched_no_appno/total_ple*100:.2f}%)")
total_accepted = final_matched
print(f"\n  Total accepted for analysis:        {total_accepted:>8,}  ({total_accepted/total_ple*100:.2f}%)")

print(f"\n{'─'*55}")
print(f"NMAT_FINAL (2006–2018)")
print(f"{'─'*55}")
print(f"  Total NMAT rows:                    {total_nmat:>8,}")
print(f"  Unique NMAT persons (name+DOB):     {total_persons:>8,}")

attempt_counts2 = nmat_ultima.groupby("PERSON_KEY")["APPNO_CLEAN"].count()
print(f"  Took NMAT once:                     {(attempt_counts2 == 1).sum():>8,}")
print(f"  Took NMAT 2+ times:                 {(attempt_counts2 > 1).sum():>8,}")
print(f"  Max attempts by one person:         {attempt_counts2.max():>8}")

print(f"\n{'─'*55}")
print(f"NMAT ROWS WITH PLE FLAG")
print(f"{'─'*55}")
print(f"  IS_PLE_PASSER = True:               {nmat_ultima['IS_PLE_PASSER'].sum():>8,}")
print(f"  IS_PLE_ANALYSIS_SAFE = True:        {nmat_ultima['IS_PLE_ANALYSIS_SAFE'].sum():>8,}")
print(f"  IS_BEST_NMAT_RECORD = True:         {nmat_ultima['IS_BEST_NMAT_RECORD'].sum():>8,}")

print(f"\n{'─'*55}")
print(f"YEAR GAP DISTRIBUTION (PLE – NMAT)")
print(f"{'─'*55}")
gap_stats = master_match[master_match["YEAR_GAP"].notna()]["YEAR_GAP"]
print(f"  Median gap:   {gap_stats.median():.1f} years")
print(f"  Mean gap:     {gap_stats.mean():.1f} years")
print(f"  Min gap:      {gap_stats.min():.0f} years")
print(f"  Max gap:      {gap_stats.max():.0f} years")
print(f"  Distribution:")
print(gap_stats.value_counts().sort_index().to_string())

print(f"\n{'─'*55}")
print(f"PLE_MATCH_STATUS IN NMAT_ULTIMA")
print(f"{'─'*55}")
print(nmat_ultima["PLE_MATCH_STATUS"].value_counts(dropna=False).to_string())
======================================================================
COMPREHENSIVE VALIDATION REPORT
======================================================================

───────────────────────────────────────────────────────
PLE PASSERS (2011–2022)
───────────────────────────────────────────────────────
  Total PLE passers:                    43,630
  FINAL_MATCH (exact/manual/appno):     36,395  (83.42%)
  AMBIGUOUS (flagged, included):           772  (1.77%)
  NO_VALID_MATCH:                        2,298  (5.27%)
  UNMATCHED_FINAL:                           0  (0.00%)
  UNMATCHED_NO_APPNO:                    4,135  (9.48%)

  Total accepted for analysis:          36,395  (83.42%)

───────────────────────────────────────────────────────
NMAT_FINAL (2006–2018)
───────────────────────────────────────────────────────
  Total NMAT rows:                     178,927
  Unique NMAT persons (name+DOB):      134,869
  Took NMAT once:                      101,155
  Took NMAT 2+ times:                   33,714
  Max attempts by one person:                9

───────────────────────────────────────────────────────
NMAT ROWS WITH PLE FLAG
───────────────────────────────────────────────────────
  IS_PLE_PASSER = True:                 49,986
  IS_PLE_ANALYSIS_SAFE = True:          49,986
  IS_BEST_NMAT_RECORD = True:          133,804

───────────────────────────────────────────────────────
YEAR GAP DISTRIBUTION (PLE – NMAT)
───────────────────────────────────────────────────────
  Median gap:   6.0 years
  Mean gap:     6.4 years
  Min gap:      5 years
  Max gap:      15 years
  Distribution:
YEAR_GAP
5.0      4424
6.0     18518
7.0      8246
8.0      2264
9.0       774
10.0      294
11.0      128
12.0       62
13.0       23
14.0        5
15.0        4

───────────────────────────────────────────────────────
PLE_MATCH_STATUS IN NMAT_ULTIMA
───────────────────────────────────────────────────────
PLE_MATCH_STATUS
NOT_IN_PLE        121623
FINAL_MATCH        49986
NO_VALID_MATCH      5595
AMBIGUOUS           1723
# ============================================================
# CELL 16 — Save all audit outputs
# ============================================================

master_match.to_csv(OUTDIR / "PLE_MATCH_MASTER.csv", index=False)

# Unmatched PLE passers for review
unmatched_output = master_match[
    master_match["MATCH_STATUS"].isin(["UNMATCHED_FINAL", "NO_VALID_MATCH", "UNMATCHED_NO_APPNO"])
].copy()
unmatched_output.to_csv(OUTDIR / "PLE_STILL_UNMATCHED_v2.csv", index=False) # Saving as v2 so we don't overwrite the input if they are in the same folder

# Ambiguous for manual review
ambiguous_output = master_match[master_match["MATCH_STATUS"] == "AMBIGUOUS"].copy()
ambiguous_output.to_csv(OUTDIR / "PLE_AMBIGUOUS_REVIEW.csv", index=False)

# PLE passers in NMAT (best record only)
ple_in_nmat = nmat_ultima[
    nmat_ultima["IS_PLE_PASSER"] & nmat_ultima["IS_BEST_NMAT_RECORD"]
].copy()
ple_in_nmat.to_csv(OUTDIR / "PLE_PASSERS_IN_NMAT.csv", index=False)

print("Saved audit outputs:")
print(f"  PLE_MATCH_MASTER.csv          → {len(master_match):,} rows")
print(f"  PLE_STILL_UNMATCHED_v2.csv    → {len(unmatched_output):,} rows")
print(f"  PLE_AMBIGUOUS_REVIEW.csv      → {len(ambiguous_output):,} rows")
print(f"  PLE_PASSERS_IN_NMAT.csv       → {len(ple_in_nmat):,} rows")
print(f"\n✅ NMAT_Ultima.csv is ready for all analyses.")
print(f"   Use IS_BEST_NMAT_RECORD=True for person-level analysis.")
print(f"   Use IS_PLE_ANALYSIS_SAFE=True for clean PLE survival analysis.")
print(f"   IS_PLE_PASSER=True includes AMBIGUOUS (flag these in PLE plots).")
Saved audit outputs:
  PLE_MATCH_MASTER.csv          → 43,601 rows
  PLE_STILL_UNMATCHED_v2.csv    → 6,433 rows
  PLE_AMBIGUOUS_REVIEW.csv      → 772 rows
  PLE_PASSERS_IN_NMAT.csv       → 36,305 rows

✅ NMAT_Ultima.csv is ready for all analyses.
   Use IS_BEST_NMAT_RECORD=True for person-level analysis.
   Use IS_PLE_ANALYSIS_SAFE=True for clean PLE survival analysis.
   IS_PLE_PASSER=True includes AMBIGUOUS (flag these in PLE plots).