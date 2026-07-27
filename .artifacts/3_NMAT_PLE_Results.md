# ============================================================
# ANALYSIS CELL 1 — Install dependencies
# ============================================================
# !pip -q install -U pandas numpy pyarrow matplotlib seaborn scipy scikit-posthocs plotly kaleido
# ============================================================
# ANALYSIS CELL 2 — Imports and global config
# ============================================================
from pathlib import Path
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from scipy import stats
import scikit_posthocs as sp

warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", 120)
pd.set_option("display.float_format", "{:.2f}".format)

# ── Paths ────────────────────────────────────────────────────────────
ROOT_CANDIDATES = [Path("/root/dataset"), Path("root/dataset"), Path("dataset")]
ROOT  = next((p for p in ROOT_CANDIDATES if p.exists()), None)
assert ROOT is not None, "Dataset folder not found."

ULTIMA_PATH = ROOT / "NMAT_Ultima.parquet"
OUTDIR      = ROOT / "analysis_output"
OUTDIR.mkdir(parents=True, exist_ok=True)

assert ULTIMA_PATH.exists(), f"Missing: {ULTIMA_PATH}"

# ── Global plot style ────────────────────────────────────────────────
PALETTE_YEAR   = "tab20"
PALETTE_UNI    = {
    "Public": "#2196F3",
    "Private": "#FF9800",
    "Foreign": "#9C27B0",
    "Not Specified": "#9E9E9E"
}
PALETTE_COURSE = {
    "Medical & Allied": "#E53935",
    "Natural Sciences": "#43A047",
    "Social & Behavioral Sciences": "#FB8C00",
    "Education": "#1E88E5",
    "Engineering & Technology": "#8E24AA",
    "Other": "#757575"
}
PALETTE_PLE = {
    "Confirmed PLE passer": "#2E7D32",
    "No confirmed PLE match": "#C62828"
}
DECILE_ORDER = [f"D{i}" for i in range(1, 11)]
DPI = 180

sns.set_theme(style="whitegrid", context="notebook", font_scale=1.1)
plt.rcParams.update({
    "figure.dpi": DPI,
    "savefig.dpi": DPI,
    "figure.facecolor": "white",
    "axes.facecolor": "white"
})

def savefig(name: str):
    path = OUTDIR / f"{name}.png"
    plt.savefig(path, bbox_inches="tight", dpi=DPI)
    plt.show()
    print(f"  ✓ Saved: {path.name}")

def print_section(title: str):
    bar = "=" * 70
    print(f"\n{bar}\n{title}\n{bar}")

def df_to_md(df: pd.DataFrame, title: str = "") -> None:
    if title:
        print(f"\n── {title} ──")
    print(df.to_string(index=False))
    print()

print("✅ Analysis environment ready.")
print(f"   Output folder: {OUTDIR}")
✅ Analysis environment ready.
   Output folder: dataset\analysis_output
# ============================================================
# ANALYSIS CELL 3 — Load and cast NMAT_Ultima
# ============================================================
print_section("LOADING NMAT_Ultima.parquet")

df_raw = pd.read_parquet(ULTIMA_PATH)
print(f"Loaded: {df_raw.shape[0]:,} rows × {df_raw.shape[1]} columns")

# ── Cast numerics ─────────────────────────────────────────────────────
num_cols = [
    "Year", "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA",
    "NMS_VCss","NMS_IRss","NMS_Qss","NMS_PAss",
    "NMS_BIOss","NMS_PHYss","NMS_SSCss","NMS_CHEMss",
    "TotalRawScoreTRUE","PartIRawScoreTRUE","PartIIRawScoreTRUE",
    "Raw_Verbal","Raw_InductiveReasoning","Raw_Quantitative","Raw_PerceptualAcuity",
    "Raw_Biology","Raw_Physics","Raw_SocialScience","Raw_Chemistry",
    "StoredRawTotal","CalculatedRawTotal_Source",
    "APT_CEM","SA_CEM","GPS_CEM","Percentile_CEM",
    "PLE_YEAR_PASSED","PLE_YEAR_GAP","PLE_MATCH_CONFIDENCE"
]

for col in num_cols:
    if col in df_raw.columns:
        df_raw[col] = pd.to_numeric(df_raw[col], errors="coerce")

# ── Boolean flags ─────────────────────────────────────────────────────
for flag in [
    "IS_PLE_PASSER","IS_PLE_ANALYSIS_SAFE","IS_BEST_NMAT_RECORD",
    "HasCEMMatch","HasTRUErawScores","AllRawComponentsPresent"
]:
    if flag in df_raw.columns:
        df_raw[flag] = df_raw[flag].map(
            lambda x: True if str(x).strip().upper() in ("TRUE", "1", "YES") else
                      False if str(x).strip().upper() in ("FALSE", "0", "NO") else pd.NA
        ).astype("boolean")

# ── Ordered categorical decile ────────────────────────────────────────
df_raw["PercentileDecile"] = pd.Categorical(
    df_raw["PercentileDecile"], categories=DECILE_ORDER, ordered=True
)

# ── Year fields ───────────────────────────────────────────────────────
df_raw["Year"] = pd.to_numeric(df_raw["Year"], errors="coerce").astype("Int64")
df_raw["Year_int"] = df_raw["Year"].astype("Int64")
df_raw["YEAR_INT"] = df_raw["Year"].astype("Int64")   # downstream alias for compatibility

# ── Board observability flag for PLE-linked descriptive work ──────────
df_raw["IS_BOARD_OBSERVABLE_COHORT"] = df_raw["Year"].le(2014).astype("boolean")

# ── Clean sex field ───────────────────────────────────────────────────
if "SEX" in df_raw.columns:
    df_raw["SEX_CLEAN"] = df_raw["SEX"].astype(str).str.strip().str.title()
    df_raw.loc[~df_raw["SEX_CLEAN"].isin(["Male", "Female"]), "SEX_CLEAN"] = pd.NA
else:
    df_raw["SEX_CLEAN"] = pd.NA

# ── Confirmed PLE flag ────────────────────────────────────────────────
df_raw["HAS_CONFIRMED_PLE"] = (df_raw["IS_PLE_ANALYSIS_SAFE"] == True).astype("boolean")

# ── PLE status label for plots and tables ─────────────────────────────
def ple_label(row):
    if row.get("IS_PLE_ANALYSIS_SAFE") == True:
        return "Confirmed PLE passer"
    else:
        return "No confirmed PLE match"

df_raw["PLE_STATUS_LABEL"] = df_raw.apply(ple_label, axis=1)

print(f"\nYear range: {int(df_raw['Year'].min())} – {int(df_raw['Year'].max())}")
print(f"Total rows: {len(df_raw):,}")

print(f"\nColumn count by category:")
print(f"  Score columns available: {sum(1 for c in df_raw.columns if any(s in c for s in ['Raw_','NMS_','GPS','APT','SA_CEM']))}")
print(f"  PLE flag columns:        {sum(1 for c in df_raw.columns if 'PLE' in c)}")

print(f"\nPLE_STATUS_LABEL:")
print(df_raw["PLE_STATUS_LABEL"].value_counts(dropna=False).to_string())

print(f"\nIS_BOARD_OBSERVABLE_COHORT:")
print(df_raw["IS_BOARD_OBSERVABLE_COHORT"].value_counts(dropna=False).to_string())

print(f"\nSEX_CLEAN distribution:")
print(df_raw["SEX_CLEAN"].value_counts(dropna=False).to_string())
======================================================================
LOADING NMAT_Ultima.parquet
======================================================================
Loaded: 178,927 rows × 115 columns
Year range: 2006 – 2018
Total rows: 178,927

Column count by category:
  Score columns available: 24
  PLE flag columns:        10

PLE_STATUS_LABEL:
PLE_STATUS_LABEL
No confirmed PLE match    128941
Confirmed PLE passer       49986

IS_BOARD_OBSERVABLE_COHORT:
IS_BOARD_OBSERVABLE_COHORT
False    90783
True     88144

SEX_CLEAN distribution:
SEX_CLEAN
Female    101240
Male       77642
NaN           45
# ============================================================
# ANALYSIS CELL 4 — Define analysis subsets
# ============================================================

# ── All rows ─────────────────────────────────────────────────────────
df_all = df_raw.copy()

# ── Best record per person (person-level analysis basis) ─────────────
df_best = df_raw[df_raw["IS_BEST_NMAT_RECORD"] == True].copy()

# ── PLE-safe subset (confirmed matches only) ──────────────────────────
df_ple_safe = df_raw[df_raw["IS_PLE_ANALYSIS_SAFE"] == True].copy()
df_ple_best = df_ple_safe[df_ple_safe["IS_BEST_NMAT_RECORD"] == True].copy()

# ── Year filter 2006–2018 ────────────────────────────────────────────
df_trend      = df_all[df_all["Year"].between(2006, 2018)].copy()
df_best_trend = df_best[df_best["Year"].between(2006, 2018)].copy()

# ── Observable cohort for PLE-linked descriptive work ────────────────
df_best_observable = df_best_trend[df_best_trend["IS_BOARD_OBSERVABLE_COHORT"] == True].copy()

# ── UNI_TYPE filter for institutional comparisons ────────────────────
df_uni = df_best_trend[df_best_trend["UNI_TYPE"].isin(["Public", "Private", "Foreign"])].copy()
df_uni_observable = df_best_observable[df_best_observable["UNI_TYPE"].isin(["Public", "Private", "Foreign"])].copy()

print_section("ANALYSIS SUBSETS")
print(f"All rows (df_all):                       {len(df_all):,}")
print(f"Best record per person (df_best):       {len(df_best):,}")
print(f"Trend subset 2006–2018:                 {len(df_trend):,}")
print(f"Best trend subset:                      {len(df_best_trend):,}")
print(f"Observable best-record cohort:          {len(df_best_observable):,}")
print(f"PLE-safe matched rows:                  {len(df_ple_safe):,}  ← NMAT rows, not unique persons")
print(f"PLE-safe matched best-record persons:   {len(df_ple_best):,}  ← one row per confirmed matched passer")

print(f"\nCourseGroup distribution (best records):")
print(df_best_trend["CourseGroup"].value_counts(dropna=False).to_string())

print(f"\nUNI_TYPE distribution (best records):")
print(df_best_trend["UNI_TYPE"].value_counts(dropna=False).to_string())

print(f"\nPLE_STATUS_LABEL distribution (observable best-record cohort):")
print(df_best_observable["PLE_STATUS_LABEL"].value_counts(dropna=False).to_string())
======================================================================
ANALYSIS SUBSETS
======================================================================
All rows (df_all):                       178,927
Best record per person (df_best):       133,804
Trend subset 2006–2018:                 178,927
Best trend subset:                      133,804
Observable best-record cohort:          64,501
PLE-safe matched rows:                  49,986  ← NMAT rows, not unique persons
PLE-safe matched best-record persons:   36,305  ← one row per confirmed matched passer

CourseGroup distribution (best records):
CourseGroup
Medical & Allied                63900
Natural Sciences                41430
Social & Behavioral Sciences    16462
Other                            7983
Education                        3279
Engineering & Technology          750

UNI_TYPE distribution (best records):
UNI_TYPE
Private          101342
Public            27797
Foreign            3270
Not Specified      1395

PLE_STATUS_LABEL distribution (observable best-record cohort):
PLE_STATUS_LABEL
No confirmed PLE match    35228
Confirmed PLE passer      29273
# ============================================================
# ANALYSIS CELL 4A — Data Integrity: Post-Cleaning University Classification
# ============================================================
print_section("SECTION 0A: DATA INTEGRITY — UNI_TYPE CONSISTENCY (POST-CLEANING)")

# ── DESIGN NOTE ──────────────────────────────────────────────────────
# The UNIVERSITY, UNI_TYPE, and UNI_LOCATION columns are the AUTHORITATIVE
# post-cleaning institutional fields, derived from UNIVS.csv matching
# in the data cleaning pipeline (verified_dim, drop_duplicates on NMA_College).
#
# School Type_rec2_FINAL is the RAW pre-cleaning field from NMAT source data.
# That field has a KNOWN data quality issue: the same college name can appear
# with different school types across rows (e.g. UST mapped to all four types),
# because different NMAT records encoded it inconsistently.
# This was the exact problem the UNIVS.csv pipeline was built to resolve.
# Checking School Type_rec2_FINAL for integrity would report the pre-cleaning
# problem, not the post-cleaning state — which would be misleading.
#
# CORRECT CHECK: UNI_TYPE per NMA_College (verified, one-to-one after cleaning).
# REFERENCE ONLY: School Type_rec2_FINAL (pre-cleaning, documented for audit).
# ─────────────────────────────────────────────────────────────────────

print("\n[Source of Truth — Post-Cleaning Institutional Classification]")
print("  Column: UNIVERSITY   → Standardized institution name (from UNIVS.csv)")
print("  Column: UNI_TYPE     → Foreign | Private | Public | Not Specified")
print("  Column: UNI_LOCATION → International | Local | Unknown")
print("  Each NMA_College maps to exactly ONE UNI_TYPE after UNIVS.csv matching.")

# ── A: Post-cleaning integrity check: UNI_TYPE per NMA_College ──────
integrity_base = df_all[["NMA_College", "UNI_TYPE"]].copy()
integrity_base["NMA_College_norm"] = (
    integrity_base["NMA_College"].astype(str).str.strip().str.upper()
)

college_type_summary = (
    integrity_base
    .groupby("NMA_College_norm")
    .agg(
        records=("UNI_TYPE", "size"),
        n_unique_types=("UNI_TYPE", "nunique"),
        mapped_types=("UNI_TYPE", lambda s: " | ".join(sorted(set(x for x in s if pd.notna(x)))))
    )
    .reset_index()
    .sort_values(["n_unique_types", "records"], ascending=[False, False])
)

multi_type_colleges = college_type_summary[college_type_summary["n_unique_types"] > 1].copy()
college_type_summary.to_csv(OUTDIR / "00E_college_uni_type_post_cleaning.csv", index=False)
if not multi_type_colleges.empty:
    multi_type_colleges.to_csv(OUTDIR / "00E_college_uni_type_conflicts.csv", index=False)

n_colleges_checked  = college_type_summary.shape[0]
n_single_type       = int((college_type_summary["n_unique_types"] == 1).sum())
n_multi_type        = int((college_type_summary["n_unique_types"] > 1).sum())

print(f"\n[Post-Cleaning UNI_TYPE Consistency]")
print(f"  Unique NMA_College values checked:   {n_colleges_checked:,}")
print(f"  Colleges with exactly 1 UNI_TYPE:    {n_single_type:,}")
print(f"  Colleges with >1 UNI_TYPE (conflict): {n_multi_type:,}")

if n_multi_type == 0:
    print("\n  ✅ PASS — Every college maps to exactly one UNI_TYPE.")
    print("     The UNIVS.csv cleaning pipeline successfully resolved all")
    print("     School Type_rec2_FINAL inconsistencies in the source data.")
else:
    print(f"\n  ⚠️  {n_multi_type:,} colleges still have multiple UNI_TYPE values.")
    print("     These may require investigation in the UNIVS.csv lookup.")
    print(multi_type_colleges.to_string(index=False))

# ── B: UNI_TYPE × UNI_LOCATION pairing check ─────────────────────────
loc_check = (
    df_all[["UNIVERSITY", "UNI_TYPE", "UNI_LOCATION"]].dropna(subset=["UNIVERSITY"])
    .groupby("UNIVERSITY")
    .agg(
        records=("UNIVERSITY", "size"),
        n_uni_types=("UNI_TYPE", "nunique"),
        n_locations=("UNI_LOCATION", "nunique"),
        uni_types=("UNI_TYPE", lambda s: " | ".join(sorted(set(str(x) for x in s if pd.notna(x))))),
        locations=("UNI_LOCATION", lambda s: " | ".join(sorted(set(str(x) for x in s if pd.notna(x)))))
    )
    .reset_index()
    .sort_values(["n_uni_types", "n_locations", "records"], ascending=[False, False, False])
)

loc_conflicts = loc_check[(loc_check["n_uni_types"] > 1) | (loc_check["n_locations"] > 1)]
loc_check.to_csv(OUTDIR / "00E_university_type_location_summary.csv", index=False)
if not loc_conflicts.empty:
    loc_conflicts.to_csv(OUTDIR / "00E_university_type_location_conflicts.csv", index=False)

print(f"\n[UNIVERSITY → UNI_TYPE / UNI_LOCATION Pairing]")
print(f"  Unique UNIVERSITY names checked:               {loc_check.shape[0]:,}")
print(f"  With consistent UNI_TYPE:                      {(loc_check['n_uni_types']==1).sum():,}")
print(f"  With consistent UNI_LOCATION:                  {(loc_check['n_locations']==1).sum():,}")
if loc_conflicts.empty:
    print("  ✅ All universities have consistent type and location mappings.")
else:
    print(f"  ⚠️  {loc_conflicts.shape[0]:,} universities have inconsistent mappings:")
    print(loc_conflicts.head(10).to_string(index=False))

# ── C: Pre-cleaning reference (audit only, NOT a finding) ────────────
pre_clean_check = (
    df_all[["NMA_College", "School Type_rec2_FINAL"]]
    .dropna(subset=["NMA_College"])
    .groupby("NMA_College")["School Type_rec2_FINAL"]
    .nunique()
)
n_pre_conflicts = int((pre_clean_check > 1).sum())
print(f"\n[Pre-Cleaning Reference — School Type_rec2_FINAL]")
print(f"  Colleges with >1 School Type_rec2_FINAL: {n_pre_conflicts:,}")
print(f"  ⚠️  This is a KNOWN raw data quality issue in the original NMAT source.")
print(f"     It is documented here for audit transparency only.")
print(f"     The UNIVS.csv pipeline resolved this; UNI_TYPE is the authoritative field.")

# ── D: Visualization ─────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 4))

post_clean_counts = pd.DataFrame({
    "Status": ["Single UNI_TYPE\n(Post-Cleaning ✅)", "Multiple UNI_TYPE\n(Post-Cleaning)"],
    "Count":  [n_single_type, n_multi_type]
})
axes[0].bar(post_clean_counts["Status"], post_clean_counts["Count"],
            color=["#43A047", "#E53935"], alpha=0.85)
axes[0].set_ylabel("Number of Colleges")
axes[0].set_title("Post-Cleaning: UNI_TYPE Integrity\n(Authoritative — from UNIVS.csv)")
axes[0].grid(True, axis="y", linestyle="--", alpha=0.4)
for i, v in enumerate(post_clean_counts["Count"]):
    axes[0].text(i, v + 2, f"{v:,}", ha="center", va="bottom", fontsize=10)

pre_clean_counts = pd.DataFrame({
    "Status": ["Single type\n(Pre-Cleaning)", "Multiple types\n(Pre-Cleaning ⚠️)"],
    "Count":  [int((pre_clean_check == 1).sum()), n_pre_conflicts]
})
axes[1].bar(pre_clean_counts["Status"], pre_clean_counts["Count"],
            color=["#90CAF9", "#FFA726"], alpha=0.85)
axes[1].set_ylabel("Number of Colleges")
axes[1].set_title("Pre-Cleaning: School Type_rec2_FINAL\n(Reference Only — Known Raw Data Issue)")
axes[1].grid(True, axis="y", linestyle="--", alpha=0.4)
for i, v in enumerate(pre_clean_counts["Count"]):
    axes[1].text(i, v + 2, f"{v:,}", ha="center", va="bottom", fontsize=10)

plt.suptitle(
    "Section 0A: University Classification Integrity\n"
    "Left = post-cleaning (authoritative) | Right = pre-cleaning (reference only)",
    fontsize=12, fontweight="bold"
)
plt.tight_layout()
savefig("00E_university_type_integrity")
======================================================================
SECTION 0A: DATA INTEGRITY — UNI_TYPE CONSISTENCY (POST-CLEANING)
======================================================================

[Source of Truth — Post-Cleaning Institutional Classification]
  Column: UNIVERSITY   → Standardized institution name (from UNIVS.csv)
  Column: UNI_TYPE     → Foreign | Private | Public | Not Specified
  Column: UNI_LOCATION → International | Local | Unknown
  Each NMA_College maps to exactly ONE UNI_TYPE after UNIVS.csv matching.
[Post-Cleaning UNI_TYPE Consistency]
  Unique NMA_College values checked:   3,213
  Colleges with exactly 1 UNI_TYPE:    3,213
  Colleges with >1 UNI_TYPE (conflict): 0

  ✅ PASS — Every college maps to exactly one UNI_TYPE.
     The UNIVS.csv cleaning pipeline successfully resolved all
     School Type_rec2_FINAL inconsistencies in the source data.
[UNIVERSITY → UNI_TYPE / UNI_LOCATION Pairing]
  Unique UNIVERSITY names checked:               2,399
  With consistent UNI_TYPE:                      2,397
  With consistent UNI_LOCATION:                  2,397
  ⚠️  2 universities have inconsistent mappings:
         UNIVERSITY  records  n_uni_types  n_locations         uni_types             locations
      VELEZ COLLEGE     2971            2            2 Foreign | Private International | Local
NEW YORK UNIVERSITY       11            2            2 Foreign | Private International | Local

[Pre-Cleaning Reference — School Type_rec2_FINAL]
  Colleges with >1 School Type_rec2_FINAL: 760
  ⚠️  This is a KNOWN raw data quality issue in the original NMAT source.
     It is documented here for audit transparency only.
     The UNIVS.csv pipeline resolved this; UNI_TYPE is the authoritative field.
No description has been provided for this image
  ✓ Saved: 00E_university_type_integrity.png
# ============================================================
# ANALYSIS CELL 5 — Section 0: Data Validation Report
# (raw score mismatches, missing data, CEM coverage)
# ============================================================
print_section("SECTION 0: DATA VALIDATION REPORT")

# ── 0A: CEM match coverage ────────────────────────────────────────────
cem_matched = df_all["HasCEMMatch"].sum()
cem_total   = len(df_all)
print(f"[CEM Coverage]")
print(f"  Rows with CEM match:         {int(cem_matched):,} / {cem_total:,}  ({cem_matched/cem_total*100:.2f}%)")
print(f"  Rows with TRUE raw scores:   {int(df_all['HasTRUErawScores'].sum()):,}")

# ── 0B: Raw score mismatch ────────────────────────────────────────────
mismatch_stored = df_all["StoredVsDerivedMismatch"]
mismatch_calc   = df_all["CalcVsDerivedMismatch"]

n_stored_available = df_all["StoredRawTotal"].notna().sum()
n_stored_mismatch  = (mismatch_stored == True).sum()
n_calc_mismatch    = (mismatch_calc   == True).sum()

print(f"\n[Raw Score Validation]")
print(f"  Stored total available:              {n_stored_available:,}")
print(f"  StoredTotal ≠ DerivedTotal:          {n_stored_mismatch:,}  ({n_stored_mismatch/n_stored_available*100:.2f}% of available)")
print(f"  CalcTotal ≠ DerivedTotal:            {int(n_calc_mismatch):,}")
print(f"  Records using TotalRawScoreTRUE:     {df_all['TotalRawScoreTRUE'].notna().sum():,}")

# ── 0C: Missing values in key analysis columns ────────────────────────
key_cols = ["NMS_GPS","NMS_PER_num","TotalRawScoreTRUE","PartIRawScoreTRUE",
            "PartIIRawScoreTRUE","UNI_TYPE","CourseGroup","PercentileDecile"]
missing_report = pd.DataFrame({
    "column": key_cols,
    "missing_n": [df_best_trend[c].isna().sum() for c in key_cols],
    "missing_pct": [df_best_trend[c].isna().mean()*100 for c in key_cols]
})
missing_report["missing_pct"] = missing_report["missing_pct"].round(2)
df_to_md(missing_report, "Missing Values in Key Analysis Columns (best-record subset)")
missing_report.to_csv(OUTDIR / "00_data_validation_missing.csv", index=False)

# ── 0D: Validation summary table ──────────────────────────────────────
val_summary = pd.DataFrame([
    {"Metric": "Total NMAT rows",              "Value": f"{len(df_all):,}"},
    {"Metric": "Rows 2006–2018",               "Value": f"{len(df_trend):,}"},
    {"Metric": "Unique persons (name+DOB)",    "Value": f"{df_all['PERSON_KEY'].nunique():,}"},
    {"Metric": "CEM-matched rows",             "Value": f"{int(cem_matched):,}"},
    {"Metric": "StoredTotal ≠ DerivedTotal",   "Value": f"{n_stored_mismatch:,}"},
    {"Metric": "CalcTotal ≠ DerivedTotal",     "Value": f"{int(n_calc_mismatch):,}"},
    {"Metric": "PLE safe-matched (best rec.)", "Value": f"{len(df_ple_best):,}"},
    {"Metric": "PLE AMBIGUOUS (flagged)",      "Value": f"{(df_all['PLE_MATCH_STATUS']=='AMBIGUOUS').sum():,}"},
    {"Metric": "PLE UNMATCHED_FINAL",          "Value": f"{(df_all['PLE_MATCH_STATUS']=='UNMATCHED_FINAL').sum():,}"},
])
df_to_md(val_summary, "Data Validation Summary")
val_summary.to_csv(OUTDIR / "00_data_validation_summary.csv", index=False)

# ── 0E: Mismatch visualization ────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 4))

mismatch_counts = pd.DataFrame({
    "Type": ["Stored vs Derived\n(Available subset)", "Calc vs Derived\n(All rows)"],
    "Mismatch": [n_stored_mismatch, int(n_calc_mismatch)],
    "Total":    [n_stored_available, cem_total]
})
mismatch_counts["Match"] = mismatch_counts["Total"] - mismatch_counts["Mismatch"]

axes[0].bar(mismatch_counts["Type"], mismatch_counts["Mismatch"], color="#E53935", label="Mismatch")
axes[0].bar(mismatch_counts["Type"], mismatch_counts["Match"],
            bottom=mismatch_counts["Mismatch"], color="#43A047", label="Match")
axes[0].set_title("Raw Score Consistency Check")
axes[0].set_ylabel("Record Count")
axes[0].legend()

missing_report_plot = missing_report.sort_values("missing_pct", ascending=True)
axes[1].barh(missing_report_plot["column"], missing_report_plot["missing_pct"], color="#1E88E5")
axes[1].set_title("Missing % — Key Analysis Columns\n(Best-record subset)")
axes[1].set_xlabel("Missing %")
axes[1].axvline(5, color="red", linestyle="--", linewidth=0.8, label="5% threshold")
axes[1].legend()

plt.suptitle("Section 0: Data Validation", fontsize=13, fontweight="bold")
plt.tight_layout()
savefig("00_data_validation")
======================================================================
SECTION 0: DATA VALIDATION REPORT
======================================================================
[CEM Coverage]
  Rows with CEM match:         178,882 / 178,927  (99.97%)
  Rows with TRUE raw scores:   178,882

[Raw Score Validation]
  Stored total available:              99,316
  StoredTotal ≠ DerivedTotal:          0  (0.00% of available)
  CalcTotal ≠ DerivedTotal:            0
  Records using TotalRawScoreTRUE:     178,882

── Missing Values in Key Analysis Columns (best-record subset) ──
            column  missing_n  missing_pct
           NMS_GPS          0         0.00
       NMS_PER_num       1222         0.91
 TotalRawScoreTRUE         38         0.03
 PartIRawScoreTRUE         38         0.03
PartIIRawScoreTRUE         38         0.03
          UNI_TYPE          0         0.00
       CourseGroup          0         0.00
  PercentileDecile       3069         2.29


── Data Validation Summary ──
                      Metric   Value
             Total NMAT rows 178,927
              Rows 2006–2018 178,927
   Unique persons (name+DOB) 134,869
            CEM-matched rows 178,882
  StoredTotal ≠ DerivedTotal       0
    CalcTotal ≠ DerivedTotal       0
PLE safe-matched (best rec.)  36,305
     PLE AMBIGUOUS (flagged)   1,723
         PLE UNMATCHED_FINAL       0

No description has been provided for this image
  ✓ Saved: 00_data_validation.png
# ============================================================
# ANALYSIS CELL 6 — Section 1: Overall Performance Trends
# Yearly summaries of raw scores and percentile ranks
# ============================================================
print_section("SECTION 1A: OVERALL PERFORMANCE TRENDS — YEARLY SUMMARIES")

# Use best-record subset across 2006–2018
score_trend = (
    df_best_trend
    .groupby("Year")[["TotalRawScoreTRUE","PartIRawScoreTRUE","PartIIRawScoreTRUE","NMS_PER_num","NMS_GPS"]]
    .agg(["median","mean",
          lambda x: x.quantile(0.25),
          lambda x: x.quantile(0.75),
          "count"])
    .round(2)
)

# Flatten for export
flat = df_best_trend.groupby("Year").agg(
    n=("TotalRawScoreTRUE","count"),
    raw_median=("TotalRawScoreTRUE","median"),
    raw_q25=("TotalRawScoreTRUE", lambda x: x.quantile(0.25)),
    raw_q75=("TotalRawScoreTRUE", lambda x: x.quantile(0.75)),
    pct_median=("NMS_PER_num","median"),
    pct_q25=("NMS_PER_num", lambda x: x.quantile(0.25)),
    pct_q75=("NMS_PER_num", lambda x: x.quantile(0.75)),
    gps_median=("NMS_GPS","median"),
).reset_index().round(2)

df_to_md(flat, "Yearly Summary: Total Raw Score and Percentile Rank (Best Records)")
flat.to_csv(OUTDIR / "01A_yearly_summary.csv", index=False)

# ── Plot: Median raw score and IQR over years ──────────────────────────
fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

years = flat["Year"].astype(int)

# Panel A: Total Raw Score
axes[0].plot(years, flat["raw_median"], "o-", color="#1565C0", linewidth=2, label="Median")
axes[0].fill_between(years, flat["raw_q25"], flat["raw_q75"], alpha=0.25, color="#1565C0", label="IQR (25–75%)")
axes[0].set_ylabel("Total Raw Score (Derived)")
axes[0].set_title("A. Total Raw Score Trend (2006–2018)")
axes[0].legend()
axes[0].grid(True, axis="y", linestyle="--", alpha=0.5)

# Panel B: Percentile Rank
axes[1].plot(years, flat["pct_median"], "s-", color="#E65100", linewidth=2, label="Median")
axes[1].fill_between(years, flat["pct_q25"], flat["pct_q75"], alpha=0.25, color="#E65100", label="IQR (25–75%)")
axes[1].set_ylabel("Percentile Rank")
axes[1].set_title("B. Percentile Rank Trend (2006–2018)")
axes[1].set_xlabel("NMAT Year")
axes[1].legend()
axes[1].grid(True, axis="y", linestyle="--", alpha=0.5)
axes[1].xaxis.set_major_locator(mticker.MultipleLocator(1))

plt.suptitle("Section 1: Overall NMAT Performance Trends", fontsize=13, fontweight="bold")
plt.tight_layout()
savefig("01A_overall_trend_raw_and_percentile")

# ── Textual summary ────────────────────────────────────────────────────
print("\n[Interpretation]")
print(f"  Overall median raw score range: {flat['raw_median'].min():.1f} – {flat['raw_median'].max():.1f}")
print(f"  Year with highest median raw:   {int(flat.loc[flat['raw_median'].idxmax(),'Year'])}")
print(f"  Year with lowest median raw:    {int(flat.loc[flat['raw_median'].idxmin(),'Year'])}")
print(f"  IQR width range:                {(flat['raw_q75']-flat['raw_q25']).min():.1f} – {(flat['raw_q75']-flat['raw_q25']).max():.1f}")
print(f"  Overall median percentile:      {flat['pct_median'].median():.1f}")
======================================================================
SECTION 1A: OVERALL PERFORMANCE TRENDS — YEARLY SUMMARIES
======================================================================

── Yearly Summary: Total Raw Score and Percentile Rank (Best Records) ──
 Year     n  raw_median  raw_q25  raw_q75  pct_median  pct_q25  pct_q75  gps_median
 2006  3665      131.00   108.00   154.00       53.00    27.00    77.00      508.00
 2007  3660      130.00   107.00   155.00       52.00    27.00    77.00      504.00
 2008  4849      129.00   107.00   153.00       54.00    28.00    80.00      511.00
 2009  6864      129.00   108.00   152.00       52.00    26.00    77.00      504.00
 2010  8006      135.00   113.00   159.00       57.00    31.00    81.00      517.00
 2011  8725      129.00   109.00   151.00       52.00    30.00    76.00      504.00
 2012  9135      121.00   101.00   145.00       53.00    26.00    81.00      510.00
 2013  9118      128.00   103.00   154.00       59.00    24.00    86.00      525.00
 2014 10441      120.00    98.00   142.00       57.00    24.00    83.00      518.00
 2015 10402      118.00    93.00   142.00       52.00    20.00    78.00      506.00
 2016 12609      123.00    98.00   147.00       48.00    19.00    73.00      495.00
 2017 23955      118.00    93.00   143.00       44.00    19.00    70.00      485.00
 2018 22337      111.00    91.00   132.00       43.00    17.00    70.00      481.00

No description has been provided for this image
  ✓ Saved: 01A_overall_trend_raw_and_percentile.png

[Interpretation]
  Overall median raw score range: 111.0 – 135.0
  Year with highest median raw:   2010
  Year with lowest median raw:    2018
  IQR width range:                41.0 – 51.0
  Overall median percentile:      52.0
# ============================================================
# ANALYSIS CELL 7 — Section 1B: Faceted Boxplots by Year
# ============================================================
print_section("SECTION 1B: FACETED BOXPLOTS — RAW SCORES BY YEAR")

fig, axes = plt.subplots(3, 1, figsize=(18, 16))

score_vars = [
    ("TotalRawScoreTRUE", "Total Raw Score (All 8 Subtests)", "#1565C0"),
    ("PartIRawScoreTRUE", "Part I Raw Score (Aptitude: Verbal, IR, Quant, PA)", "#2E7D32"),
    ("PartIIRawScoreTRUE","Part II Raw Score (Science: Bio, Phys, SS, Chem)", "#6A1B9A"),
]

for ax, (col, title, color) in zip(axes, score_vars):
    plot_data = df_best_trend[["Year", col]].dropna()
    year_order = sorted(plot_data["Year"].unique())
    bp = ax.boxplot(
        [plot_data[plot_data["Year"]==y][col].values for y in year_order],
        positions=year_order,
        widths=0.6,
        patch_artist=True,
        medianprops=dict(color="white", linewidth=2),
        boxprops=dict(facecolor=color, alpha=0.7),
        whiskerprops=dict(color=color),
        capprops=dict(color=color),
        flierprops=dict(marker=".", color=color, alpha=0.2, markersize=2)
    )
    ax.set_title(title, fontsize=11)
    ax.set_ylabel("Score")
    ax.set_xlabel("NMAT Year")
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(1))

plt.suptitle("Section 1B: Score Distributions by Year", fontsize=13, fontweight="bold")
plt.tight_layout()
savefig("01B_boxplots_by_year")

# ── Per-subtest trends table ──────────────────────────────────────────
subtest_trend = df_best_trend.groupby("Year")[
    ["Raw_Verbal","Raw_InductiveReasoning","Raw_Quantitative","Raw_PerceptualAcuity",
     "Raw_Biology","Raw_Physics","Raw_SocialScience","Raw_Chemistry"]
].median().round(2)
subtest_trend.to_csv(OUTDIR / "01B_subtest_median_by_year.csv")
print("\nMedian subtest raw scores by year:")
print(subtest_trend.to_string())
======================================================================
SECTION 1B: FACETED BOXPLOTS — RAW SCORES BY YEAR
======================================================================
No description has been provided for this image
  ✓ Saved: 01B_boxplots_by_year.png

Median subtest raw scores by year:
      Raw_Verbal  Raw_InductiveReasoning  Raw_Quantitative  Raw_PerceptualAcuity  Raw_Biology  Raw_Physics  Raw_SocialScience  Raw_Chemistry
Year                                                                                                                                        
2006       17.00                   19.00             15.00                 17.00        17.00        15.00              16.00          15.00
2007       17.00                   19.00             14.00                 16.00        17.00        16.00              18.00          15.00
2008       17.00                   19.00             16.00                 15.00        16.00        15.00              16.00          14.00
2009       17.00                   18.00             15.00                 17.00        16.00        15.00              17.00          14.00
2010       18.00                   20.00             15.00                 18.00        16.00        15.00              18.00          15.00
2011       17.00                   20.00             15.00                 17.00        16.00        15.00              17.00          13.00
2012       16.00                   20.00             14.00                 17.00        13.00        13.00              16.00          13.00
2013       16.00                   20.00             15.00                 19.00        13.00        14.00              17.00          13.00
2014       16.00                   18.00             14.00                 17.00        14.00        12.00              16.00          13.00
2015       15.00                   16.00             13.00                 16.00        14.00        14.00              14.00          14.00
2016       15.00                   18.00             13.00                 20.00        16.00        13.00              15.00          13.00
2017       14.00                   16.00             13.00                 19.00        15.00        13.00              13.00          13.00
2018       15.00                   16.00             12.00                 16.00        13.00        12.00              13.00          13.00
# ============================================================
# ANALYSIS CELL 7A — Section 1C: Part I vs Part II Trend Insights
# ============================================================
print_section("SECTION 1C: PART I (APTITUDE) VS PART II (SCIENCE) TRENDS")

part_trend = (
    df_best_trend
    .groupby("Year")[["PartIRawScoreTRUE", "PartIIRawScoreTRUE", "TotalRawScoreTRUE"]]
    .median()
    .reset_index()
    .round(2)
)

part_trend["PartI_share_pct"] = (
    part_trend["PartIRawScoreTRUE"] / part_trend["TotalRawScoreTRUE"] * 100
).round(2)
part_trend["PartII_share_pct"] = (
    part_trend["PartIIRawScoreTRUE"] / part_trend["TotalRawScoreTRUE"] * 100
).round(2)
part_trend["PartI_minus_PartII"] = (
    part_trend["PartIRawScoreTRUE"] - part_trend["PartIIRawScoreTRUE"]
).round(2)

# TRUE Raw Score rule check: TotalRawScoreTRUE = Part I + Part II
eq_mask = df_best_trend[["TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE"]].notna().all(axis=1)
eq_delta = (
    df_best_trend.loc[eq_mask, "TotalRawScoreTRUE"]
    - (df_best_trend.loc[eq_mask, "PartIRawScoreTRUE"] + df_best_trend.loc[eq_mask, "PartIIRawScoreTRUE"])
).round(6)
n_formula_mismatch = int((eq_delta != 0).sum())

df_to_md(part_trend, "Yearly Median Trend: Part I vs Part II vs TRUE Total")
part_trend.to_csv(OUTDIR / "01C_parti_partii_trend.csv", index=False)

fig, axes = plt.subplots(2, 1, figsize=(14, 9), sharex=True)
years = part_trend["Year"].astype(int)

axes[0].plot(years, part_trend["PartIRawScoreTRUE"], "o-", color="#1E88E5", linewidth=2, label="Part I (Aptitude)")
axes[0].plot(years, part_trend["PartIIRawScoreTRUE"], "s-", color="#FB8C00", linewidth=2, label="Part II (Science)")
axes[0].plot(years, part_trend["TotalRawScoreTRUE"], "^-", color="#2E7D32", linewidth=2, label="TRUE Raw Total")
axes[0].set_ylabel("Median Raw Score")
axes[0].set_title("Section 1C-A: Median Raw Trends by Test Component")
axes[0].legend()
axes[0].grid(True, axis="y", linestyle="--", alpha=0.5)

axes[1].plot(years, part_trend["PartI_share_pct"], "o-", color="#1565C0", linewidth=2, label="Part I share (%)")
axes[1].plot(years, part_trend["PartII_share_pct"], "s-", color="#EF6C00", linewidth=2, label="Part II share (%)")
axes[1].axhline(50, color="gray", linestyle="--", linewidth=1, label="50% parity")
axes[1].set_ylabel("Share of TRUE Raw Score (%)")
axes[1].set_xlabel("NMAT Year")
axes[1].set_title("Section 1C-B: Contribution Share to TRUE Raw Score")
axes[1].legend()
axes[1].grid(True, axis="y", linestyle="--", alpha=0.5)
axes[1].xaxis.set_major_locator(mticker.MultipleLocator(1))

plt.tight_layout()
savefig("01C_parti_partii_trend")

print("\n[Insights]")
print("  Part I captures cognitive aptitude (Verbal, Inductive Reasoning, Quantitative, Perceptual Acuity).")
print("  Part II captures science knowledge (Biology, Physics, Social Science, Chemistry).")
print(f"  Median Part I share range:  {part_trend['PartI_share_pct'].min():.2f}% to {part_trend['PartI_share_pct'].max():.2f}%")
print(f"  Median Part II share range: {part_trend['PartII_share_pct'].min():.2f}% to {part_trend['PartII_share_pct'].max():.2f}%")
print(f"  Years where Part I median > Part II median: {(part_trend['PartI_minus_PartII'] > 0).sum()} / {len(part_trend)}")
print(f"  TRUE Raw formula mismatches (in complete records): {n_formula_mismatch:,}")
======================================================================
SECTION 1C: PART I (APTITUDE) VS PART II (SCIENCE) TRENDS
======================================================================

── Yearly Median Trend: Part I vs Part II vs TRUE Total ──
 Year  PartIRawScoreTRUE  PartIIRawScoreTRUE  TotalRawScoreTRUE  PartI_share_pct  PartII_share_pct  PartI_minus_PartII
 2006              67.00               63.00             131.00            51.15             48.09                4.00
 2007              65.50               65.00             130.00            50.38             50.00                0.50
 2008              67.00               61.00             129.00            51.94             47.29                6.00
 2009              68.00               62.00             129.00            52.71             48.06                6.00
 2010              71.00               64.00             135.00            52.59             47.41                7.00
 2011              69.00               60.00             129.00            53.49             46.51                9.00
 2012              67.00               54.00             121.00            55.37             44.63               13.00
 2013              70.00               57.00             128.00            54.69             44.53               13.00
 2014              65.00               54.00             120.00            54.17             45.00               11.00
 2015              61.00               57.00             118.00            51.69             48.31                4.00
 2016              66.00               57.00             123.00            53.66             46.34                9.00
 2017              63.00               54.00             118.00            53.39             45.76                9.00
 2018              59.00               51.00             111.00            53.15             45.95                8.00

No description has been provided for this image
  ✓ Saved: 01C_parti_partii_trend.png

[Insights]
  Part I captures cognitive aptitude (Verbal, Inductive Reasoning, Quantitative, Perceptual Acuity).
  Part II captures science knowledge (Biology, Physics, Social Science, Chemistry).
  Median Part I share range:  50.38% to 55.37%
  Median Part II share range: 44.53% to 50.00%
  Years where Part I median > Part II median: 13 / 13
  TRUE Raw formula mismatches (in complete records): 0
# ============================================================
# ANALYSIS CELL 8 — Section 2: Stability Analysis (Kruskal-Wallis)
# ============================================================
print_section("SECTION 2: STABILITY ANALYSIS — KRUSKAL-WALLIS BY YEAR")

from scipy.stats import kruskal

score_targets = [
    ("TotalRawScoreTRUE", "Total Raw Score"),
    ("PartIRawScoreTRUE",  "Part I Raw Score"),
    ("PartIIRawScoreTRUE", "Part II Raw Score"),
    ("NMS_PER_num",        "Percentile Rank"),
    ("NMS_GPS",            "GPS (Standard Score)"),
]

kw_results = []

for col, label in score_targets:
    groups = [
        g[col].dropna().values
        for _, g in df_best_trend.groupby("Year")
        if g[col].dropna().shape[0] > 5
    ]
    if len(groups) < 2:
        continue

    stat, pval = kruskal(*groups)

    # Effect size: eta-squared approximation
    n_total = sum(len(g) for g in groups)
    k = len(groups)
    eta2 = (stat - k + 1) / (n_total - k)
    eta2 = max(0.0, eta2)

    magnitude = (
        "Large (η²≥0.14)" if eta2 >= 0.14 else
        "Medium (η²≥0.06)" if eta2 >= 0.06 else
        "Small (η²≥0.01)" if eta2 >= 0.01 else
        "Negligible"
    )

    kw_results.append({
        "Score": label, "H-stat": round(stat, 3),
        "p-value": f"{'<0.001' if pval<0.001 else round(pval,4)}",
        "η²": round(eta2, 4), "Effect Size": magnitude,
        "Significant": "Yes" if pval < 0.05 else "No"
    })

kw_df = pd.DataFrame(kw_results)
df_to_md(kw_df, "Kruskal-Wallis Tests: Score Distributions Across Years")
kw_df.to_csv(OUTDIR / "02_kruskal_wallis_by_year.csv", index=False)

# ── IQR stability table ────────────────────────────────────────────────
iqr_stability = df_best_trend.groupby("Year")["TotalRawScoreTRUE"].agg(
    IQR=lambda x: x.quantile(0.75) - x.quantile(0.25)
).reset_index().round(2)
iqr_stability.to_csv(OUTDIR / "02_iqr_by_year.csv", index=False)

fig, ax = plt.subplots(figsize=(13, 4))
ax.bar(iqr_stability["Year"].astype(int), iqr_stability["IQR"], color="#0288D1", alpha=0.8)
ax.axhline(iqr_stability["IQR"].mean(), color="red", linestyle="--",
           label=f"Mean IQR = {iqr_stability['IQR'].mean():.1f}")
ax.set_xlabel("NMAT Year")
ax.set_ylabel("IQR (Total Raw Score)")
ax.set_title("Section 2: Score IQR by Year — Stability Proxy")
ax.legend()
plt.tight_layout()
savefig("02_iqr_stability_by_year")

print(f"\n[Interpretation]")
print(f"  IQR range: {iqr_stability['IQR'].min():.1f} – {iqr_stability['IQR'].max():.1f}")
print(f"  Narrow IQR range indicates distributional stability across years.")
print(f"  Significant Kruskal-Wallis does NOT mean difficulty changed —")
print(f"  it reflects distributional shifts, potentially driven by cohort composition.")
======================================================================
SECTION 2: STABILITY ANALYSIS — KRUSKAL-WALLIS BY YEAR
======================================================================

── Kruskal-Wallis Tests: Score Distributions Across Years ──
               Score  H-stat p-value   η²     Effect Size Significant
     Total Raw Score 5598.20  <0.001 0.04 Small (η²≥0.01)         Yes
    Part I Raw Score 5453.44  <0.001 0.04 Small (η²≥0.01)         Yes
   Part II Raw Score 5515.99  <0.001 0.04 Small (η²≥0.01)         Yes
     Percentile Rank 2226.02  <0.001 0.02 Small (η²≥0.01)         Yes
GPS (Standard Score) 2411.01  <0.001 0.02 Small (η²≥0.01)         Yes

No description has been provided for this image
  ✓ Saved: 02_iqr_stability_by_year.png

[Interpretation]
  IQR range: 41.0 – 51.0
  Narrow IQR range indicates distributional stability across years.
  Significant Kruskal-Wallis does NOT mean difficulty changed —
  it reflects distributional shifts, potentially driven by cohort composition.
# ============================================================
# ANALYSIS CELL 9 — Section 3: Decile-Based Distribution Analysis
# Heatmap and stacked bar: Year × Decile
# ============================================================
print_section("SECTION 3: DECILE-BASED DISTRIBUTION ANALYSIS")

# ── 3A: Count of examinees per decile per year ─────────────────────────
decile_year = (
    df_best_trend
    .dropna(subset=["PercentileDecile"])
    .groupby(["Year", "PercentileDecile"], observed=True)
    .size()
    .unstack(fill_value=0)
    .reindex(columns=DECILE_ORDER, fill_value=0)
)

decile_year_pct = decile_year.div(decile_year.sum(axis=1), axis=0) * 100

# Export
decile_year.to_csv(OUTDIR / "03A_decile_by_year_count.csv")
decile_year_pct.round(2).to_csv(OUTDIR / "03A_decile_by_year_pct.csv")

# ── Heatmap ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 7))
sns.heatmap(
    decile_year_pct,
    annot=True, fmt=".1f", cmap="YlOrRd",
    linewidths=0.4, cbar_kws={"label": "% of Examinees"},
    ax=ax
)
ax.set_title("Section 3A: Decile Distribution by Year (% of Examinees per Year)", fontsize=12)
ax.set_xlabel("Percentile Decile")
ax.set_ylabel("NMAT Year")
plt.tight_layout()
savefig("03A_heatmap_decile_by_year")

# ── Stacked bar chart ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(16, 6))
cmap_dec = plt.get_cmap("RdYlGn", 10)
colors_dec = [cmap_dec(i) for i in range(10)]

bottom = np.zeros(len(decile_year_pct))
for i, decile in enumerate(DECILE_ORDER):
    vals = decile_year_pct[decile].values
    ax.bar(decile_year_pct.index.astype(int), vals, bottom=bottom,
           color=colors_dec[i], label=decile, width=0.85)
    bottom += vals

ax.set_xlabel("NMAT Year")
ax.set_ylabel("% of Examinees")
ax.set_title("Section 3B: Decile Composition by Year (Stacked)")
ax.legend(title="Decile", bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=9)
plt.tight_layout()
savefig("03B_stacked_bar_decile_by_year")

# ── Top vs Bottom decile trend ─────────────────────────────────────────
top_decile_pct    = decile_year_pct[["D8","D9","D10"]].sum(axis=1)
bottom_decile_pct = decile_year_pct[["D1","D2","D3"]].sum(axis=1)

fig, ax = plt.subplots(figsize=(13, 4))
ax.plot(top_decile_pct.index.astype(int), top_decile_pct.values, "o-",
        color="#2E7D32", linewidth=2, label="Top (D8–D10)")
ax.plot(bottom_decile_pct.index.astype(int), bottom_decile_pct.values, "s-",
        color="#C62828", linewidth=2, label="Bottom (D1–D3)")
ax.set_xlabel("NMAT Year")
ax.set_ylabel("% of Examinees")
ax.set_title("Section 3C: Top vs Bottom Decile Share by Year")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
savefig("03C_top_bottom_decile_trend")

print(f"\n[Interpretation]")
print(f"  Mean % in top deciles (D8–D10): {top_decile_pct.mean():.1f}%")
print(f"  Mean % in bottom deciles (D1–D3): {bottom_decile_pct.mean():.1f}%")
top_shift = top_decile_pct.iloc[-1] - top_decile_pct.iloc[0]
print(f"  Change in top decile share (first→last year): {top_shift:+.1f} pp")
======================================================================
SECTION 3: DECILE-BASED DISTRIBUTION ANALYSIS
======================================================================
No description has been provided for this image
  ✓ Saved: 03A_heatmap_decile_by_year.png
No description has been provided for this image
  ✓ Saved: 03B_stacked_bar_decile_by_year.png
No description has been provided for this image
  ✓ Saved: 03C_top_bottom_decile_trend.png

[Interpretation]
  Mean % in top deciles (D8–D10): 32.4%
  Mean % in bottom deciles (D1–D3): 29.2%
  Change in top decile share (first→last year): -7.7 pp
# ============================================================
# ANALYSIS CELL 10 — Section 4: University Type × Deciles
# ============================================================
print_section("SECTION 4A: UNIVERSITY TYPE → DECILE DISTRIBUTION")

uni_decile = (
    df_uni
    .dropna(subset=["PercentileDecile"])
    .groupby(["UNI_TYPE", "PercentileDecile"], observed=True)
    .size()
    .unstack(fill_value=0)
    .reindex(columns=DECILE_ORDER, fill_value=0)
)

uni_decile_pct = uni_decile.div(uni_decile.sum(axis=1), axis=0) * 100
uni_decile.to_csv(OUTDIR / "04A_uni_type_decile_count.csv")
uni_decile_pct.round(2).to_csv(OUTDIR / "04A_uni_type_decile_pct.csv")

df_to_md(uni_decile_pct.round(1), "UNI_TYPE × Decile (%)")

# ── Heatmap ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 4))
sns.heatmap(uni_decile_pct, annot=True, fmt=".1f", cmap="Blues",
            linewidths=0.4, cbar_kws={"label":"% within UNI_TYPE"}, ax=ax)
ax.set_title("Section 4A: Decile Distribution by University Type (%)")
plt.tight_layout()
savefig("04A_heatmap_uni_type_decile")

# ── Grouped bar: top decile share by UNI_TYPE ─────────────────────────
top_by_uni = uni_decile_pct[["D8","D9","D10"]].sum(axis=1).reset_index()
top_by_uni.columns = ["UNI_TYPE","Top_Decile_Pct"]

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(top_by_uni["UNI_TYPE"], top_by_uni["Top_Decile_Pct"],
              color=[PALETTE_UNI.get(u,"#9E9E9E") for u in top_by_uni["UNI_TYPE"]])
for bar, val in zip(bars, top_by_uni["Top_Decile_Pct"]):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f"{val:.1f}%", ha="center", va="bottom", fontsize=10)
ax.set_ylabel("% in Top Deciles (D8–D10)")
ax.set_title("Section 4A: Top Decile Representation by University Type")
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
savefig("04A_top_decile_by_uni_type")

# ── Kruskal-Wallis: UNI_TYPE × percentile ─────────────────────────────
uni_groups = {u: g["NMS_PER_num"].dropna().values
              for u, g in df_uni.groupby("UNI_TYPE")}
if len(uni_groups) >= 2:
    stat, pval = kruskal(*uni_groups.values())
    n_tot = sum(len(v) for v in uni_groups.values())
    eta2  = max(0, (stat - len(uni_groups) + 1) / (n_tot - len(uni_groups)))
    print(f"\n[Kruskal-Wallis: UNI_TYPE × Percentile Rank]")
    print(f"  H = {stat:.3f}, p {'< 0.001' if pval < 0.001 else f'= {pval:.4f}'}, η² = {eta2:.4f}")

    # Descriptive per group
    uni_desc = df_uni.groupby("UNI_TYPE")["NMS_PER_num"].agg(
        n="count", median="median", q25=lambda x: x.quantile(.25),
        q75=lambda x: x.quantile(.75)
    ).round(2).reset_index()
    df_to_md(uni_desc, "Descriptive: Percentile Rank by University Type")
    uni_desc.to_csv(OUTDIR / "04A_kw_uni_type_descriptive.csv", index=False)
======================================================================
SECTION 4A: UNIVERSITY TYPE → DECILE DISTRIBUTION
======================================================================

── UNI_TYPE × Decile (%) ──
   D1   D2   D3    D4   D5    D6   D7   D8    D9   D10
12.70 8.80 8.90 10.50 9.20 10.20 9.50 9.50 10.40 10.40
13.00 9.90 8.90  9.90 9.90 10.20 9.30 9.50  9.60  9.80
11.90 8.50 7.60  8.40 8.60  9.20 8.80 9.50 11.00 16.50

No description has been provided for this image
  ✓ Saved: 04A_heatmap_uni_type_decile.png
No description has been provided for this image
  ✓ Saved: 04A_top_decile_by_uni_type.png
[Kruskal-Wallis: UNI_TYPE × Percentile Rank]
  H = 614.156, p < 0.001, η² = 0.0047

── Descriptive: Percentile Rank by University Type ──
UNI_TYPE      n  median   q25   q75
 Foreign   3249   50.00 24.00 76.00
 Private 100493   48.00 21.00 74.00
  Public  27459   55.00 26.00 82.00

# ============================================================
# ANALYSIS CELL 10A — Section 4A-Extended: UNI_TYPE × UNI_LOCATION Matrix
# Comprehensive institutional classification analysis
# ============================================================
print_section("SECTION 4A-EXTENDED: INSTITUTION TYPE × LOCATION CLASSIFICATION MATRIX")

print("\n[Source of Truth: Three-Dimensional Institution Classification]")
print("  ├─ UNIVERSITY: Standardized institution name")
print("  ├─ UNI_TYPE: Foreign | Private | Public")
print("  └─ UNI_LOCATION: International | Local")
print("\n  Key Insight: Understanding how Public/Private/Foreign differs when")
print("  considering their geographic scope (International vs Local) provides")
print("  nuanced policy insights on institution-type stratification.")

# ── Prepare base data: filter to Public/Private/Foreign, drop unknowns ──
df_inst = df_best_trend[df_best_trend["UNI_TYPE"].isin(["Public","Private","Foreign"])].dropna(subset=["UNI_LOCATION"]).copy()

if df_inst.empty:
    print("\n⚠️ No rows with both UNI_TYPE and UNI_LOCATION data. Skipping Section 4A-Extended.")
else:
    # ── 4A-1: Cross-tabulation (count and percentage) ──────────────────
    print("\n[4A-1: Institution Count Matrix]")
    
    inst_count = pd.crosstab(df_inst["UNI_TYPE"], df_inst["UNI_LOCATION"], margins=True)
    inst_pct_row = pd.crosstab(df_inst["UNI_TYPE"], df_inst["UNI_LOCATION"], normalize="index") * 100
    inst_pct_col = pd.crosstab(df_inst["UNI_TYPE"], df_inst["UNI_LOCATION"], normalize="columns") * 100
    
    df_to_md(inst_count, "Institution Count: UNI_TYPE × UNI_LOCATION")
    df_to_md(inst_pct_row.round(2), "Row %: Distribution of Location within each Type")
    df_to_md(inst_pct_col.round(2), "Column %: Distribution of Type within each Location")
    
    inst_count.to_csv(OUTDIR / "04A_ext_inst_type_location_count.csv")
    inst_pct_row.round(2).to_csv(OUTDIR / "04A_ext_inst_type_location_row_pct.csv")
    inst_pct_col.round(2).to_csv(OUTDIR / "04A_ext_inst_type_location_col_pct.csv")

    # ── 4A-2: Heatmap visualization ────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 4))
    
    sns.heatmap(inst_pct_row.iloc[:-1, :], annot=True, fmt=".1f", cmap="Blues",
                cbar_kws={"label": "% within UNI_TYPE"}, ax=axes[0])
    axes[0].set_title("Distribution of UNI_LOCATION within each UNI_TYPE (%)")
    axes[0].set_xlabel("University Location")
    axes[0].set_ylabel("University Type")
    
    sns.heatmap(inst_pct_col.iloc[:, :-1], annot=True, fmt=".1f", cmap="Oranges",
                cbar_kws={"label": "% within UNI_LOCATION"}, ax=axes[1])
    axes[1].set_title("Distribution of UNI_TYPE within each UNI_LOCATION (%)")
    axes[1].set_xlabel("University Location")
    axes[1].set_ylabel("University Type")
    
    plt.suptitle("Section 4A-Extended: Institution Type × Location Matrix", fontsize=13, fontweight="bold")
    plt.tight_layout()
    savefig("04A_ext_inst_matrix_heatmap")

    # ── 4A-3: Decile distribution by institution classification ────────
    print("\n[4A-2: Decile Distribution by Institution Classification]")
    
    inst_decile = (
        df_inst.dropna(subset=["PercentileDecile"])
        .groupby(["UNI_TYPE", "UNI_LOCATION", "PercentileDecile"], observed=True)
        .size()
        .unstack(fill_value=0)
        .reindex(columns=DECILE_ORDER, fill_value=0)
    )
    
    if not inst_decile.empty:
        inst_decile_pct = inst_decile.div(inst_decile.sum(axis=1), axis=0) * 100
        inst_decile_pct.round(2).to_csv(OUTDIR / "04A_ext_inst_decile_pct.csv")
        df_to_md(inst_decile_pct.round(1), "Decile Distribution (%) by Institution Type × Location")
        
        # Top deciles visualization
        top_by_inst = inst_decile_pct[[c for c in DECILE_ORDER if c in ["D8","D9","D10"]]].sum(axis=1).reset_index(name="Top_Decile_Pct")
        top_by_inst["Label"] = top_by_inst["UNI_TYPE"] + " (" + top_by_inst["UNI_LOCATION"] + ")"
        top_by_inst = top_by_inst.sort_values("Top_Decile_Pct", ascending=True)
        
        fig, ax = plt.subplots(figsize=(10, 5))
        colors_inst = ["#2196F3" if "Public" in x else "#FF9800" if "Private" in x else "#9C27B0" 
                       for x in top_by_inst["Label"]]
        bars = ax.barh(top_by_inst["Label"], top_by_inst["Top_Decile_Pct"], color=colors_inst, alpha=0.85)
        for bar, val in zip(bars, top_by_inst["Top_Decile_Pct"]):
            ax.text(val + 0.5, bar.get_y() + bar.get_height()/2, f"{val:.1f}%", va="center", fontsize=9)
        ax.set_xlabel("% in Top Deciles (D8–D10)")
        ax.set_title("Section 4A-Extended: Top Decile Representation by Institution Type × Location")
        ax.grid(True, axis="x", linestyle="--", alpha=0.5)
        plt.tight_layout()
        savefig("04A_ext_inst_top_decile")

    # ── 4A-4: Descriptive statistics by institution classification ─────
    print("\n[4A-3: Performance Metrics by Institution Classification]")
    
    inst_desc = (
        df_inst.groupby(["UNI_TYPE", "UNI_LOCATION"])
        .agg(
            n=("NMS_PER_num", "count"),
            median_pct=("NMS_PER_num", "median"),
            q25_pct=("NMS_PER_num", lambda x: x.quantile(0.25)),
            q75_pct=("NMS_PER_num", lambda x: x.quantile(0.75)),
            mean_raw=("TotalRawScoreTRUE", "mean"),
            median_raw=("TotalRawScoreTRUE", "median"),
        )
        .reset_index()
        .round(2)
    )
    
    inst_desc["inst_label"] = inst_desc["UNI_TYPE"] + " (" + inst_desc["UNI_LOCATION"] + ")"
    inst_desc = inst_desc[["inst_label", "n", "median_pct", "q25_pct", "q75_pct", "mean_raw", "median_raw"]]
    inst_desc.columns = ["Institution", "Count", "Median %ile", "Q25 %ile", "Q75 %ile", "Mean Raw", "Median Raw"]
    
    df_to_md(inst_desc, "Descriptive Statistics: Institution Type × Location")
    inst_desc.to_csv(OUTDIR / "04A_ext_inst_descriptive.csv", index=False)

    # ── 4A-5: Statistical tests ────────────────────────────────────────
    print("\n[4A-4: Statistical Tests]")
    
    # Test 1: UNI_TYPE effect on percentile
    uni_type_groups = {
        ut: g["NMS_PER_num"].dropna().values
        for ut, g in df_inst.groupby("UNI_TYPE")
        if g["NMS_PER_num"].dropna().shape[0] > 5
    }
    if len(uni_type_groups) >= 2:
        h_type, p_type = kruskal(*uni_type_groups.values())
        n_tot_type = sum(len(v) for v in uni_type_groups.values())
        eta2_type = max(0, (h_type - len(uni_type_groups) + 1) / (n_tot_type - len(uni_type_groups)))
        magnitude_type = (
            "Large (η²≥0.14)" if eta2_type >= 0.14 else
            "Medium (η²≥0.06)" if eta2_type >= 0.06 else
            "Small (η²≥0.01)" if eta2_type >= 0.01 else "Negligible"
        )
        print(f"\n  Kruskal-Wallis: UNI_TYPE × Percentile Rank")
        print(f"    H = {h_type:.3f}, p {'<0.001' if p_type < 0.001 else f'= {p_type:.4f}'}, η² = {eta2_type:.4f} ({magnitude_type})")
    
    # Test 2: UNI_LOCATION effect on percentile
    location_groups = {
        loc: g["NMS_PER_num"].dropna().values
        for loc, g in df_inst.groupby("UNI_LOCATION")
        if g["NMS_PER_num"].dropna().shape[0] > 5
    }
    if len(location_groups) >= 2:
        h_loc, p_loc = kruskal(*location_groups.values())
        n_tot_loc = sum(len(v) for v in location_groups.values())
        eta2_loc = max(0, (h_loc - len(location_groups) + 1) / (n_tot_loc - len(location_groups)))
        magnitude_loc = (
            "Large (η²≥0.14)" if eta2_loc >= 0.14 else
            "Medium (η²≥0.06)" if eta2_loc >= 0.06 else
            "Small (η²≥0.01)" if eta2_loc >= 0.01 else "Negligible"
        )
        print(f"\n  Kruskal-Wallis: UNI_LOCATION × Percentile Rank")
        print(f"    H = {h_loc:.3f}, p {'<0.001' if p_loc < 0.001 else f'= {p_loc:.4f}'}, η² = {eta2_loc:.4f} ({magnitude_loc})")
    
    # Test 3: Chi-square for independence
    chi_data = df_inst.dropna(subset=["UNI_TYPE", "UNI_LOCATION", "PercentileDecile"])
    chi_ct = pd.crosstab(
        [chi_data["UNI_TYPE"], chi_data["UNI_LOCATION"]], 
        chi_data["PercentileDecile"]
    ).reindex(columns=DECILE_ORDER, fill_value=0)
    
    if chi_ct.values.sum() > 0:
        chi2_val, p_chi, dof, expected = stats.chi2_contingency(chi_ct.values)
        n_chi = chi_ct.values.sum()
        r_chi, c_chi = chi_ct.shape
        cv_chi = float(np.sqrt(chi2_val / (n_chi * (min(r_chi - 1, c_chi - 1)))) if min(r_chi-1, c_chi-1) > 0 else 0)
        
        print(f"\n  Chi-Square: (UNI_TYPE × UNI_LOCATION) × Percentile Decile Independence")
        print(f"    χ² = {chi2_val:.1f}, p {'<0.001' if p_chi < 0.001 else f'= {p_chi:.4f}'}, df = {dof}")
        print(f"    Cramér's V = {cv_chi:.4f}")

    # ── 4A-6: Violin plots for visual comparison ───────────────────────
    fig, ax = plt.subplots(figsize=(12, 5))
    
    df_inst_plot = df_inst.copy()
    df_inst_plot["Institution"] = df_inst_plot["UNI_TYPE"] + "\n(" + df_inst_plot["UNI_LOCATION"] + ")"
    
    color_map = {
        "Public\n(International)": "#2196F3",
        "Public\n(Local)": "#64B5F6",
        "Private\n(International)": "#FF9800",
        "Private\n(Local)": "#FFB74D",
        "Foreign\n(International)": "#9C27B0",
        "Foreign\n(Local)": "#BA68C8",
    }
    
    inst_order = sorted(df_inst_plot["Institution"].unique())
    plot_data = df_inst_plot.dropna(subset=["NMS_PER_num", "Institution"])
    sns.violinplot(data=plot_data, x="Institution", y="NMS_PER_num",
                   order=inst_order, palette=color_map, ax=ax)
    ax.set_title("Section 4A-Extended: Percentile Rank Distribution\nby Institution Type × Location")
    ax.set_ylabel("Percentile Rank")
    ax.set_xlabel("Institution Classification")
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    savefig("04A_ext_inst_violin")

    # ── 4A-7: Summary insights ─────────────────────────────────────────
    print("\n[KEY INSIGHTS]")
    
    if not inst_pct_row.empty:
        for uni_type in ["Public", "Private", "Foreign"]:
            if uni_type in inst_pct_row.index:
                row_data = inst_pct_row.loc[uni_type].iloc[:-1]
                if len(row_data) > 0:
                    most_common_loc = row_data.idxmax()
                    most_common_pct = row_data.max()
                    print(f"  • {uni_type:8} institutions: {most_common_pct:.0f}% are {most_common_loc}")
    
    print(f"\n  • Total examinees analyzed: {len(df_inst):,}")
    print(f"  • Unique institution classifications: {len(inst_desc):,}")
    
    inst_perf = inst_desc[inst_desc["Institution"] != "Total"].copy()
    if not inst_perf.empty:
        best_inst = inst_perf.loc[inst_perf["Median %ile"].idxmax()]
        worst_inst = inst_perf.loc[inst_perf["Median %ile"].idxmin()]
        print(f"\n  • Highest median percentile: {best_inst['Institution']} ({best_inst['Median %ile']:.1f})")
        print(f"  • Lowest median percentile:  {worst_inst['Institution']} ({worst_inst['Median %ile']:.1f})")
        print(f"  • Percentile gap: {best_inst['Median %ile'] - worst_inst['Median %ile']:.1f} points")

print("\n✅ Section 4A-Extended analysis complete.")
======================================================================
SECTION 4A-EXTENDED: INSTITUTION TYPE × LOCATION CLASSIFICATION MATRIX
======================================================================

[Source of Truth: Three-Dimensional Institution Classification]
  ├─ UNIVERSITY: Standardized institution name
  ├─ UNI_TYPE: Foreign | Private | Public
  └─ UNI_LOCATION: International | Local

  Key Insight: Understanding how Public/Private/Foreign differs when
  considering their geographic scope (International vs Local) provides
  nuanced policy insights on institution-type stratification.
[4A-1: Institution Count Matrix]
── Institution Count: UNI_TYPE × UNI_LOCATION ──
 International  Local    All
          3270      0   3270
             0 101342 101342
           334  27463  27797
          3604 128805 132409


── Row %: Distribution of Location within each Type ──
 International  Local
        100.00   0.00
          0.00 100.00
          1.20  98.80


── Column %: Distribution of Type within each Location ──
 International  Local
         90.73   0.00
          0.00  78.68
          9.27  21.32

No description has been provided for this image
  ✓ Saved: 04A_ext_inst_matrix_heatmap.png

[4A-2: Decile Distribution by Institution Classification]

── Decile Distribution (%) by Institution Type × Location ──
   D1   D2    D3    D4    D5    D6   D7   D8    D9   D10
12.70 8.80  8.90 10.50  9.20 10.20 9.50 9.50 10.40 10.40
13.00 9.90  8.90  9.90  9.90 10.20 9.30 9.50  9.60  9.80
20.60 9.20 10.70  8.90 11.30  8.30 6.40 7.10  7.70  9.80
11.80 8.50  7.60  8.40  8.60  9.20 8.90 9.60 11.00 16.50

No description has been provided for this image
  ✓ Saved: 04A_ext_inst_top_decile.png

[4A-3: Performance Metrics by Institution Classification]

── Descriptive Statistics: Institution Type × Location ──
            Institution  Count  Median %ile  Q25 %ile  Q75 %ile  Mean Raw  Median Raw
Foreign (International)   3249        50.00     24.00     76.00    124.71      124.00
        Private (Local) 100493        48.00     21.00     74.00    121.50      120.00
 Public (International)    331        40.00     14.00     69.00    115.77      114.00
         Public (Local)  27128        55.00     26.00     83.00    128.37      126.00


[4A-4: Statistical Tests]

  Kruskal-Wallis: UNI_TYPE × Percentile Rank
    H = 614.156, p <0.001, η² = 0.0047 (Negligible)
  Kruskal-Wallis: UNI_LOCATION × Percentile Rank
    H = 0.690, p = 0.4061, η² = 0.0000 (Negligible)

  Chi-Square: (UNI_TYPE × UNI_LOCATION) × Percentile Decile Independence
    χ² = 1138.7, p <0.001, df = 27
    Cramér's V = 0.0542
No description has been provided for this image
  ✓ Saved: 04A_ext_inst_violin.png

[KEY INSIGHTS]
  • Public   institutions: 1% are International
  • Private  institutions: 0% are International
  • Foreign  institutions: 100% are International

  • Total examinees analyzed: 132,409
  • Unique institution classifications: 4

  • Highest median percentile: Public (Local) (55.0)
  • Lowest median percentile:  Public (International) (40.0)
  • Percentile gap: 15.0 points

✅ Section 4A-Extended analysis complete.
# ============================================================
# ANALYSIS CELL 11 — Section 4B: CourseGroup × Deciles
# ============================================================
print_section("SECTION 4B: PRE-MED BACKGROUND → DECILE DISTRIBUTION")

course_decile = (
    df_best_trend
    .dropna(subset=["PercentileDecile","CourseGroup"])
    .groupby(["CourseGroup","PercentileDecile"], observed=True)
    .size()
    .unstack(fill_value=0)
    .reindex(columns=DECILE_ORDER, fill_value=0)
)

course_decile_pct = course_decile.div(course_decile.sum(axis=1), axis=0) * 100
course_decile.to_csv(OUTDIR / "04B_course_decile_count.csv")
course_decile_pct.round(2).to_csv(OUTDIR / "04B_course_decile_pct.csv")
df_to_md(course_decile_pct.round(1), "CourseGroup × Decile (%)")

# ── Heatmap ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 5))
sns.heatmap(course_decile_pct, annot=True, fmt=".1f", cmap="Oranges",
            linewidths=0.4, cbar_kws={"label":"% within CourseGroup"}, ax=ax)
ax.set_title("Section 4B: Decile Distribution by Pre-Med Background (%)")
plt.tight_layout()
savefig("04B_heatmap_course_decile")

# ── Top decile share by course ─────────────────────────────────────────
top_by_course = course_decile_pct[["D8","D9","D10"]].sum(axis=1).reset_index()
top_by_course.columns = ["CourseGroup","Top_Decile_Pct"]
top_by_course = top_by_course.sort_values("Top_Decile_Pct", ascending=True)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(top_by_course["CourseGroup"], top_by_course["Top_Decile_Pct"],
               color=[PALETTE_COURSE.get(c,"#9E9E9E") for c in top_by_course["CourseGroup"]])
for bar, val in zip(bars, top_by_course["Top_Decile_Pct"]):
    ax.text(val + 0.2, bar.get_y() + bar.get_height()/2,
            f"{val:.1f}%", va="center", fontsize=9)
ax.set_xlabel("% in Top Deciles (D8–D10)")
ax.set_title("Section 4B: Top Decile Representation by Pre-Med Background")
ax.grid(True, axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
savefig("04B_top_decile_by_course")

# ── Kruskal-Wallis ─────────────────────────────────────────────────────
course_groups = {c: g["NMS_PER_num"].dropna().values
                 for c, g in df_best_trend.groupby("CourseGroup")}
stat, pval = kruskal(*course_groups.values())
n_tot = sum(len(v) for v in course_groups.values())
eta2  = max(0, (stat - len(course_groups) + 1) / (n_tot - len(course_groups)))
print(f"\n[Kruskal-Wallis: CourseGroup × Percentile Rank]")
print(f"  H = {stat:.3f}, p {'< 0.001' if pval < 0.001 else f'= {pval:.4f}'}, η² = {eta2:.4f}")

course_desc = df_best_trend.groupby("CourseGroup")["NMS_PER_num"].agg(
    n="count", median="median",
    q25=lambda x: x.quantile(.25), q75=lambda x: x.quantile(.75)
).round(2).reset_index()
df_to_md(course_desc, "Descriptive: Percentile Rank by Course Group")
course_desc.to_csv(OUTDIR / "04B_kw_course_descriptive.csv", index=False)
======================================================================
SECTION 4B: PRE-MED BACKGROUND → DECILE DISTRIBUTION
======================================================================

── CourseGroup × Decile (%) ──
   D1    D2   D3    D4    D5    D6   D7    D8    D9   D10
10.80  9.10 9.60  9.80 10.30  8.80 9.30  9.10 10.20 13.00
 6.20  5.60 6.30  5.90  8.10  9.10 7.30 10.30 15.10 26.20
10.90 10.00 9.40 10.60 10.90 11.00 9.60  9.60  9.10  8.90
13.10  8.70 7.40  8.40  8.30  9.20 9.30  9.90 11.10 14.50
11.00  8.60 8.60  9.60  9.50  9.30 9.20 10.20 12.00 12.00
21.00 11.00 8.50  8.20  7.80  8.70 7.30  7.80  8.90 10.80

No description has been provided for this image
  ✓ Saved: 04B_heatmap_course_decile.png
No description has been provided for this image
  ✓ Saved: 04B_top_decile_by_course.png
[Kruskal-Wallis: CourseGroup × Percentile Rank]
  H = 1279.831, p < 0.001, η² = 0.0096

── Descriptive: Percentile Rank by Course Group ──
                 CourseGroup     n  median   q25   q75
                   Education  3260   51.00 26.00 78.00
    Engineering & Technology   730   72.00 41.00 91.00
            Medical & Allied 63432   49.00 25.00 73.00
            Natural Sciences 40851   54.00 23.00 81.00
                       Other  7943   53.00 26.00 79.00
Social & Behavioral Sciences 16366   39.00 11.00 73.00

# ============================================================
# ANALYSIS CELL 11A — Section 4C/4D: Additional Group Diagnostics
# ============================================================
print_section("SECTION 4C: COLLEGE-LEVEL DECILES, CHI-SQUARE, AND COURSE PIE")

# ── 4C-1: Course group composition pie chart ───────────────────────────
course_dist = (
    df_best_trend["CourseGroup"]
    .fillna("Unknown")
    .value_counts()
    .rename_axis("CourseGroup")
    .reset_index(name="count")
)
course_dist["pct"] = (course_dist["count"] / course_dist["count"].sum() * 100).round(2)
course_dist.to_csv(OUTDIR / "04C_course_group_distribution.csv", index=False)

fig, ax = plt.subplots(figsize=(8, 8))
colors = [PALETTE_COURSE.get(c, "#9E9E9E") for c in course_dist["CourseGroup"]]
wedges, texts, autotexts = ax.pie(
    course_dist["count"],
    labels=course_dist["CourseGroup"],
    autopct="%1.1f%%",
    startangle=140,
    colors=colors,
    wedgeprops={"edgecolor": "white", "linewidth": 1}
 )
for t in autotexts:
    t.set_fontsize(9)
ax.set_title("Section 4C-1: Course Group Distribution (% of Examinees)")
plt.tight_layout()
savefig("04C_course_group_pie")

# ── 4C-2: College-level decile table per university type ───────────────
college_decile_base = df_best_trend.dropna(subset=["UNI_TYPE", "NMA_College", "PercentileDecile"]).copy()
college_sizes = (
    college_decile_base.groupby(["UNI_TYPE", "NMA_College"], observed=True)
    .size()
    .rename("n_examinees")
    .reset_index()
)
eligible_colleges = college_sizes[college_sizes["n_examinees"] >= 10].copy()

college_decile = (
    college_decile_base
    .merge(eligible_colleges[["UNI_TYPE", "NMA_College"]], on=["UNI_TYPE", "NMA_College"], how="inner")
    .groupby(["UNI_TYPE", "NMA_College", "PercentileDecile"], observed=True)
    .size()
    .unstack(fill_value=0)
    .reindex(columns=DECILE_ORDER, fill_value=0)
)

college_decile_pct = (
    college_decile
    .div(college_decile.sum(axis=1), axis=0)
    .mul(100)
    .reset_index()
)
college_decile_pct = college_decile_pct.merge(eligible_colleges, on=["UNI_TYPE", "NMA_College"], how="left")
college_decile_pct["D10_pct_highlight"] = college_decile_pct["D10"].round(2)

ordered_cols = ["UNI_TYPE", "NMA_College", "n_examinees"] + DECILE_ORDER + ["D10_pct_highlight"]
college_decile_pct = college_decile_pct[ordered_cols].sort_values(["UNI_TYPE", "D10_pct_highlight", "n_examinees"], ascending=[True, False, False])

college_decile_pct.round(2).to_csv(OUTDIR / "04C_college_decile_by_uni_type_pct.csv", index=False)

top10_d10_by_uni = (
    college_decile_pct
    .groupby("UNI_TYPE", group_keys=False)
    .head(10)
    .copy()
)
top10_d10_by_uni.round(2).to_csv(OUTDIR / "04C_college_top10_d10_by_uni_type.csv", index=False)

print("\nCollege-level decile table created for colleges with at least 10 examinees.")
print(f"Eligible college rows: {college_decile_pct.shape[0]:,}")
print("\nTop D10% colleges per UNI_TYPE (preview):")
print(top10_d10_by_uni[["UNI_TYPE", "NMA_College", "n_examinees", "D10_pct_highlight"]].to_string(index=False))

# ── 4D: Chi-square test of independence (UNI_TYPE × Decile) ────────────
chi_data = df_best_trend.dropna(subset=["UNI_TYPE", "PercentileDecile"]).copy()
contingency = (
    pd.crosstab(chi_data["UNI_TYPE"], chi_data["PercentileDecile"])
    .reindex(columns=DECILE_ORDER, fill_value=0)
)

chi2, pval, dof, expected = stats.chi2_contingency(contingency.values)
n_obs = contingency.values.sum()
r, c = contingency.shape
cramers_v = np.sqrt(chi2 / (n_obs * (min(r - 1, c - 1)))) if min(r - 1, c - 1) > 0 else np.nan

chi_summary = pd.DataFrame([
    {
        "chi2_statistic": round(chi2, 4),
        "p_value": pval,
        "degrees_of_freedom": int(dof),
        "n_observations": int(n_obs),
        "cramers_v": round(float(cramers_v), 4) if not np.isnan(cramers_v) else np.nan,
        "significant_at_0_05": "Yes" if pval < 0.05 else "No",
        "interpretation": (
            "Reject H0: University type and percentile decile are associated."
            if pval < 0.05
            else "Fail to reject H0: No evidence of association."
        ),
    }
])

chi_summary.to_csv(OUTDIR / "04D_chi_square_uni_type_vs_decile.csv", index=False)
contingency.to_csv(OUTDIR / "04D_uni_type_decile_observed.csv")
pd.DataFrame(expected, index=contingency.index, columns=contingency.columns).round(2).to_csv(
    OUTDIR / "04D_uni_type_decile_expected.csv"
 )

df_to_md(chi_summary, "Chi-square Test: University Type × Percentile Decile")
======================================================================
SECTION 4C: COLLEGE-LEVEL DECILES, CHI-SQUARE, AND COURSE PIE
======================================================================
No description has been provided for this image
  ✓ Saved: 04C_course_group_pie.png
College-level decile table created for colleges with at least 10 examinees.
Eligible college rows: 492

Top D10% colleges per UNI_TYPE (preview):
     UNI_TYPE                                                       NMA_College  n_examinees  D10_pct_highlight
      Foreign                                          University Of Washington           15              40.00
      Foreign                                University Of California, Berkeley           13              38.46
      Foreign                             University Of California, Los Angeles           23              30.43
      Foreign                                             University Of Toronto           17              29.41
      Foreign                      University Of California, Riverside, Ca, Usa           25              28.00
      Foreign                                                Rutgers University           11              27.27
      Foreign                                   University Of California, Davis           34              26.47
      Foreign                                  University Of California, Irvine           34              23.53
      Foreign                               University Of California, San Diego           18              22.22
      Foreign                                    Rutgers University, New Jersey           11              18.18
Not Specified                                                            13207A           21              23.81
Not Specified                                           Others (Please Specify)           23              21.74
Not Specified                                University For Development Studies           13              15.38
Not Specified                                                            13100A           13               7.69
Not Specified Mariano Marcos State University - College Of Fisheries - Currimao          104               5.77
Not Specified                    Remedios Trinidad Romualdez Medical Foundation           30               3.33
      Private                                       Ateneo De Manila University          714              44.26
      Private                              Polytechnic College Of Davao Del Sur           10              40.00
      Private                                        Northern Christian College           11              36.36
      Private                                                Lipa City Colleges           15              33.33
      Private                              College Of The Holy Spirit Of Tarlac           14              28.57
      Private                                   Brokenshire College Socsksargen           11              27.27
      Private                                         University of Santo Tomas           26              26.92
      Private                                              University Of Iloilo           12              25.00
      Private               University Of Perpetual Help System Dalta - Calamba           30              23.33
      Private                                                    Gordon College           14              21.43
       Public                            University Of The Philippines - Manila         3406              36.38
       Public                           University Of The Philippines - Diliman         3054              34.64
       Public                University Of The Philippines In The Visayas, Cebu           34              26.47
       Public                 University Of The Philippines - Los Banos, Laguna          447              25.28
       Public    Northern Negros State College Of Science And Technology - Main           10              20.00
       Public                          Camarines Sur Polytechnic College - Main           46              19.57
       Public                   University Of The Philippines - Visayas, Iloilo          179              19.55
       Public                          University Of The Philippines - Mindanao          346              18.21
       Public                              Cebu Technological University - Main           18              16.67
       Public                                       Bicol University - Polangui           12              16.67

── Chi-square Test: University Type × Percentile Decile ──
 chi2_statistic  p_value  degrees_of_freedom  n_observations  cramers_v significant_at_0_05                                                   interpretation
        1110.22     0.00                  27          130735       0.05                 Yes Reject H0: University type and percentile decile are associated.

# ============================================================
# ANALYSIS CELL 11B — Section 5A: Alluvial / Sankey helpers
# ============================================================
import plotly.graph_objects as go

def make_flow_table(
    df, source_col, target_col,
    source_order=None, target_order=None,
    source_label=None, target_label=None,
    min_count=1
):
    tmp = df[[source_col, target_col]].copy().dropna()

    if source_order is not None:
        tmp = tmp[tmp[source_col].isin(source_order)].copy()
    if target_order is not None:
        tmp = tmp[tmp[target_col].isin(target_order)].copy()

    flow = (
        tmp.groupby([source_col, target_col], observed=True)
           .size()
           .reset_index(name="count")
    )

    flow = flow[flow["count"] >= min_count].copy()

    if source_order is not None:
        flow[source_col] = pd.Categorical(flow[source_col], categories=source_order, ordered=True)
    if target_order is not None:
        flow[target_col] = pd.Categorical(flow[target_col], categories=target_order, ordered=True)

    flow = flow.sort_values([source_col, target_col]).reset_index(drop=True)

    total_source = flow.groupby(source_col, observed=True)["count"].sum().rename("source_total")
    flow = flow.merge(total_source, on=source_col, how="left")
    flow["source_pct"] = (flow["count"] / flow["source_total"] * 100).round(2)

    if source_label:
        flow = flow.rename(columns={source_col: source_label})
        source_col = source_label
    if target_label:
        flow = flow.rename(columns={target_col: target_label})
        target_col = target_label

    return flow, source_col, target_col

def sankey_from_flow(
    flow, source_col, target_col, value_col="count",
    title="Sankey", source_colors=None, target_colors=None,
    outfile_stem="sankey"
):
    source_nodes = flow[source_col].astype(str).drop_duplicates().tolist()
    target_nodes = flow[target_col].astype(str).drop_duplicates().tolist()

    labels = source_nodes + target_nodes
    node_map = {lab: i for i, lab in enumerate(labels)}

    sources = flow[source_col].astype(str).map(node_map).tolist()
    targets = flow[target_col].astype(str).map(node_map).tolist()
    values  = flow[value_col].tolist()

    node_colors = []
    for lab in labels:
        if source_colors and lab in source_colors:
            node_colors.append(source_colors[lab])
        elif target_colors and lab in target_colors:
            node_colors.append(target_colors[lab])
        else:
            node_colors.append("#BDBDBD")

    link_colors = []
    for _, r in flow.iterrows():
        tgt = str(r[target_col])
        src = str(r[source_col])
        if target_colors and tgt in target_colors:
            link_colors.append(target_colors[tgt])
        elif source_colors and src in source_colors:
            link_colors.append(source_colors[src])
        else:
            link_colors.append("rgba(160,160,160,0.45)")

    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="snap",
                node=dict(
                    pad=18,
                    thickness=18,
                    line=dict(color="black", width=0.4),
                    label=labels,
                    color=node_colors
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values,
                    color=link_colors,
                    hovertemplate="%{source.label} → %{target.label}<br>n=%{value}<extra></extra>"
                )
            )
        ]
    )

    fig.update_layout(
        title=title,
        font=dict(size=12),
        width=1100,
        height=650,
        margin=dict(l=20, r=20, t=60, b=20)
    )

    html_path = OUTDIR / f"{outfile_stem}.html"
    png_path  = OUTDIR / f"{outfile_stem}.png"

    fig.write_html(html_path)
    try:
        fig.write_image(png_path, scale=2)
        print(f"  ✓ Saved: {png_path.name}")
    except Exception as e:
        print(f"  ⚠ PNG export skipped: {e}")

    print(f"  ✓ Saved: {html_path.name}")
    return fig
# ============================================================
# ANALYSIS CELL 11C — Section 5B: University/Course -> Decile flows
# ============================================================
print_section("SECTION 5B: FLOW VISUALS — BACKGROUND TO DECILE")

DECILE_COLORS = {
    "D1": "#8B0000", "D2": "#B22222", "D3": "#D9534F", "D4": "#F0AD4E", "D5": "#FFD166",
    "D6": "#A0D468", "D7": "#66C2A5", "D8": "#41B6C4", "D9": "#2C7FB8", "D10": "#253494"
}

COURSE_COLORS = {
    "Medical & Allied": "#E53935",
    "Natural Sciences": "#43A047",
    "Social & Behavioral Sciences": "#FB8C00",
    "Education": "#1E88E5",
    "Engineering & Technology": "#8E24AA",
    "Other": "#757575"
}

# ── Flow 1: University type -> decile ─────────────────────────────────
flow_uni, src_uni, tgt_uni = make_flow_table(
    df=df_uni.copy(),
    source_col="UNI_TYPE",
    target_col="PercentileDecile",
    source_order=["Public", "Private", "Foreign"],
    target_order=DECILE_ORDER,
    source_label="UNI_TYPE",
    target_label="PercentileDecile"
)
flow_uni.to_csv(OUTDIR / "05A_flow_uni_type_to_decile.csv", index=False)

fig_uni = sankey_from_flow(
    flow_uni,
    source_col=src_uni,
    target_col=tgt_uni,
    title="Section 5A: University Type → Percentile Decile (Best Record per Person)",
    source_colors=PALETTE_UNI,
    target_colors=DECILE_COLORS,
    outfile_stem="05A_sankey_uni_type_to_decile"
)
fig_uni.show()

# ── Flow 2: Course group -> decile ────────────────────────────────────
course_order = [c for c in [
    "Medical & Allied",
    "Natural Sciences",
    "Social & Behavioral Sciences",
    "Education",
    "Engineering & Technology",
    "Other"
] if c in df_best_trend["CourseGroup"].dropna().unique()]

flow_course, src_course, tgt_course = make_flow_table(
    df=df_best_trend.copy(),
    source_col="CourseGroup",
    target_col="PercentileDecile",
    source_order=course_order,
    target_order=DECILE_ORDER,
    source_label="CourseGroup",
    target_label="PercentileDecile"
)
flow_course.to_csv(OUTDIR / "05B_flow_course_group_to_decile.csv", index=False)

fig_course = sankey_from_flow(
    flow_course,
    source_col=src_course,
    target_col=tgt_course,
    title="Section 5B: Pre-Med Background → Percentile Decile (Best Record per Person)",
    source_colors=COURSE_COLORS,
    target_colors=DECILE_COLORS,
    outfile_stem="05B_sankey_course_group_to_decile"
)
fig_course.show()
======================================================================
SECTION 5B: FLOW VISUALS — BACKGROUND TO DECILE
======================================================================
Wait expired, Browser is being closed by watchdog.
  ⚠ PNG export skipped: ('The browser seemed to close immediately after starting.', 'You can set the `logging.Logger` level lower to see more output.', 'You may try installing a known working copy of Chrome by running ', '`$ choreo_get_chrome`.It may be your browser auto-updated and will now work upon restart. The browser we tried to start is located at C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe.')
  ✓ Saved: 05A_sankey_uni_type_to_decile.html
Wait expired, Browser is being closed by watchdog.
  ⚠ PNG export skipped: ('The browser seemed to close immediately after starting.', 'You can set the `logging.Logger` level lower to see more output.', 'You may try installing a known working copy of Chrome by running ', '`$ choreo_get_chrome`.It may be your browser auto-updated and will now work upon restart. The browser we tried to start is located at C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe.')
  ✓ Saved: 05B_sankey_course_group_to_decile.html
# ============================================================
# ANALYSIS CELL 11D — Section 5C: Decile -> PLE status flow
# ============================================================
print_section("SECTION 5C: FLOW VISUAL — DECILE TO PLE STATUS")

PLE_FLOW_ORDER = [
    "Confirmed PLE passer",
    "No confirmed PLE match"
]

PLE_FLOW_COLORS = {
    "Confirmed PLE passer": "#2E7D32",
    "No confirmed PLE match": "#C62828"
}

flow_ple, src_ple, tgt_ple = make_flow_table(
    df=df_best_observable.copy(),
    source_col="PercentileDecile",
    target_col="PLE_STATUS_LABEL",
    source_order=DECILE_ORDER,
    target_order=PLE_FLOW_ORDER,
    source_label="PercentileDecile",
    target_label="PLE_STATUS_LABEL"
)
flow_ple.to_csv(OUTDIR / "05C_flow_decile_to_ple_status_observable.csv", index=False)

fig_ple = sankey_from_flow(
    flow_ple,
    source_col=src_ple,
    target_col=tgt_ple,
    title="Section 5C: Percentile Decile → PLE Status (Observable Best-Record Cohorts Only)",
    source_colors=DECILE_COLORS,
    target_colors=PLE_FLOW_COLORS,
    outfile_stem="05C_sankey_decile_to_ple_status_observable"
)
fig_ple.show()

ple_row_pct = (
    flow_ple.pivot(index="PercentileDecile", columns="PLE_STATUS_LABEL", values="source_pct")
            .reindex(index=DECILE_ORDER, columns=PLE_FLOW_ORDER)
            .fillna(0)
            .round(2)
)
ple_row_pct.to_csv(OUTDIR / "05C_decile_to_ple_status_row_pct_observable.csv")
df_to_md(ple_row_pct.reset_index(), "Row % within Decile: PLE Status (observable cohorts)")
Wait expired, Browser is being closed by watchdog.
======================================================================
SECTION 5C: FLOW VISUAL — DECILE TO PLE STATUS
======================================================================
  ⚠ PNG export skipped: ('The browser seemed to close immediately after starting.', 'You can set the `logging.Logger` level lower to see more output.', 'You may try installing a known working copy of Chrome by running ', '`$ choreo_get_chrome`.It may be your browser auto-updated and will now work upon restart. The browser we tried to start is located at C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe.')
  ✓ Saved: 05C_sankey_decile_to_ple_status_observable.html
── Row % within Decile: PLE Status (observable cohorts) ──
PercentileDecile  Confirmed PLE passer  No confirmed PLE match
              D1                  8.77                   91.23
              D2                 16.07                   83.93
              D3                 19.20                   80.80
              D4                 25.66                   74.34
              D5                 46.30                   53.70
              D6                 51.81                   48.19
              D7                 57.62                   42.38
              D8                 60.44                   39.56
              D9                 67.82                   32.18
             D10                 76.25                   23.75

# ============================================================
# ANALYSIS CELL 11E — Section 5D: Flow interpretation tables
# ============================================================
print_section("SECTION 5D: FLOW INTERPRETATION TABLES")

top_deciles = ["D8", "D9", "D10"]

uni_top = (
    df_uni[df_uni["PercentileDecile"].isin(top_deciles)]
    .groupby("UNI_TYPE", observed=True)
    .size()
    .reset_index(name="n_top_decile")
)
uni_top["pct_of_top_decile"] = (uni_top["n_top_decile"] / uni_top["n_top_decile"].sum() * 100).round(2)
uni_top.to_csv(OUTDIR / "05D_uni_type_composition_top_deciles.csv", index=False)
df_to_md(uni_top, "University Type Composition within D8–D10")

course_top = (
    df_best_trend[df_best_trend["PercentileDecile"].isin(top_deciles)]
    .groupby("CourseGroup", observed=True)
    .size()
    .reset_index(name="n_top_decile")
    .sort_values("n_top_decile", ascending=False)
)
course_top["pct_of_top_decile"] = (course_top["n_top_decile"] / course_top["n_top_decile"].sum() * 100).round(2)
course_top.to_csv(OUTDIR / "05E_course_group_composition_top_deciles.csv", index=False)
df_to_md(course_top, "Course Group Composition within D8–D10")
======================================================================
SECTION 5D: FLOW INTERPRETATION TABLES
======================================================================

── University Type Composition within D8–D10 ──
UNI_TYPE  n_top_decile  pct_of_top_decile
 Foreign           976               2.46
 Private         28742              72.33
  Public         10021              25.22


── Course Group Composition within D8–D10 ──
                 CourseGroup  n_top_decile  pct_of_top_decile
            Medical & Allied         17453              43.47
            Natural Sciences         14244              35.48
Social & Behavioral Sciences          4327              10.78
                       Other          2695               6.71
                   Education          1050               2.62
    Engineering & Technology           376               0.94

# ============================================================
# ANALYSIS CELL 12A — Section 5D/5E: Top 10 Pathways to D8-D10
# ============================================================
print_section("SECTION 5D/5E: TOP 10 PATHWAYS TO TOP DECILES (D8-D10)")

top_deciles = ["D8", "D9", "D10"]

# ── UNI_TYPE → top deciles ─────────────────────────────────────────────
path_uni = (
    df_uni.dropna(subset=["UNI_TYPE", "PercentileDecile"])
    .query("PercentileDecile in @top_deciles")
    .groupby(["UNI_TYPE", "PercentileDecile"], observed=True)
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
    .head(10)
)
path_uni.to_csv(OUTDIR / "05D_top10_pathways_uni_to_top_deciles.csv", index=False)

# ── CourseGroup → top deciles ───────────────────────────────────────────
path_course = (
    df_best_trend.dropna(subset=["CourseGroup", "PercentileDecile"])
    .query("PercentileDecile in @top_deciles")
    .groupby(["CourseGroup", "PercentileDecile"], observed=True)
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
    .head(10)
)
path_course.to_csv(OUTDIR / "05E_top10_pathways_course_to_top_deciles.csv", index=False)

print("Top 10 UNI_TYPE → Decile pathways:")
print(path_uni.to_string(index=False))
print("\nTop 10 CourseGroup → Decile pathways:")
print(path_course.to_string(index=False))

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

if not path_uni.empty:
    labels_uni = path_uni.apply(lambda r: f"{r['UNI_TYPE']} → {r['PercentileDecile']}", axis=1)
    axes[0].barh(labels_uni[::-1], path_uni["count"].values[::-1], color="#1E88E5", alpha=0.85)
    axes[0].set_title("Section 5D: Top 10 UNI_TYPE → D8-D10 Pathways")
    axes[0].set_xlabel("Count")
    axes[0].grid(True, axis="x", linestyle="--", alpha=0.4)

if not path_course.empty:
    labels_course = path_course.apply(lambda r: f"{r['CourseGroup']} → {r['PercentileDecile']}", axis=1)
    axes[1].barh(labels_course[::-1], path_course["count"].values[::-1], color="#FB8C00", alpha=0.85)
    axes[1].set_title("Section 5E: Top 10 CourseGroup → D8-D10 Pathways")
    axes[1].set_xlabel("Count")
    axes[1].grid(True, axis="x", linestyle="--", alpha=0.4)

plt.tight_layout()
savefig("05DE_top10_pathways_to_top_deciles")
======================================================================
SECTION 5D/5E: TOP 10 PATHWAYS TO TOP DECILES (D8-D10)
======================================================================
Top 10 UNI_TYPE → Decile pathways:
UNI_TYPE PercentileDecile  count
 Private              D10   9747
 Private               D9   9550
 Private               D8   9445
  Public              D10   4463
  Public               D9   2973
  Public               D8   2585
 Foreign               D9    335
 Foreign              D10    335
 Foreign               D8    306

Top 10 CourseGroup → Decile pathways:
                 CourseGroup PercentileDecile  count
            Medical & Allied               D8   6083
            Natural Sciences              D10   5816
            Medical & Allied               D9   5751
            Medical & Allied              D10   5619
            Natural Sciences               D9   4457
            Natural Sciences               D8   3971
Social & Behavioral Sciences              D10   1701
Social & Behavioral Sciences               D9   1396
Social & Behavioral Sciences               D8   1230
                       Other              D10    949
No description has been provided for this image
  ✓ Saved: 05DE_top10_pathways_to_top_deciles.png
# ============================================================
# ANALYSIS CELL 13 — Section 6: PLE Status Performance Profile
# ============================================================
print_section("SECTION 6: PLE STATUS PERFORMANCE PROFILE")

# Use observable best-record cohort only for PLE-linked descriptive work
ple_comp = (
    df_best_observable
    .dropna(subset=["PLE_STATUS_LABEL"])
    .copy()
)

plot_order = ["Confirmed PLE passer", "No confirmed PLE match"]

# ── 6A: Descriptive comparison ────────────────────────────────────────
score_vars_ple = [
    "TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE",
    "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA"
]

ple_desc = (
    ple_comp
    .groupby("PLE_STATUS_LABEL")[score_vars_ple]
    .agg([
        "count", "median", "mean",
        lambda x: x.quantile(0.25),
        lambda x: x.quantile(0.75)
    ])
    .round(2)
)

ple_desc = ple_desc.reindex(plot_order)
ple_desc.to_csv(OUTDIR / "06A_ple_status_descriptive_observable.csv")
print("PLE Status — Score Descriptives (Observable Best-Record Cohorts Only):")
print(ple_desc.to_string())

# ── 6B: Boxplot comparison ────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
compare_vars = [
    ("TotalRawScoreTRUE", "Total Raw Score"),
    ("NMS_PER_num", "Percentile Rank"),
    ("NMS_GPS", "GPS (Standard Score)")
]

available_groups = [
    g for g in plot_order
    if g in ple_comp["PLE_STATUS_LABEL"].dropna().unique()
]

for ax, (col, label) in zip(axes, compare_vars):
    groups = [
        ple_comp.loc[ple_comp["PLE_STATUS_LABEL"] == g, col].dropna()
        for g in available_groups
    ]

    bp = ax.boxplot(
        groups,
        labels=available_groups,
        patch_artist=True,
        medianprops=dict(color="white", linewidth=2)
    )

    for patch, g in zip(bp["boxes"], available_groups):
        patch.set_facecolor(PALETTE_PLE[g])
        patch.set_alpha(0.80)

    ax.set_title(label)
    ax.set_ylabel("Score")
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)
    ax.tick_params(axis="x", rotation=15)

plt.suptitle(
    "Section 6B: Score Comparison by PLE Status\n(Observable Best-Record Cohorts Only)",
    fontsize=12,
    fontweight="bold"
)
plt.tight_layout()
savefig("06B_ple_status_boxplot_observable")

# ── 6C: Mann-Whitney U tests (confirmed vs no confirmed match) ───────
print("\n[Mann-Whitney U Tests: Confirmed PLE passer vs No confirmed PLE match]")

mw_results = []
g1_label = "Confirmed PLE passer"
g2_label = "No confirmed PLE match"

if all(g in ple_comp["PLE_STATUS_LABEL"].unique() for g in [g1_label, g2_label]):
    for col, label in compare_vars + [
        ("PartIRawScoreTRUE", "Part I"),
        ("PartIIRawScoreTRUE", "Part II")
    ]:
        g1 = ple_comp.loc[ple_comp["PLE_STATUS_LABEL"] == g1_label, col].dropna()
        g2 = ple_comp.loc[ple_comp["PLE_STATUS_LABEL"] == g2_label, col].dropna()

        if len(g1) > 0 and len(g2) > 0:
            stat, pval = stats.mannwhitneyu(g1, g2, alternative="two-sided")
            r = 1 - (2 * stat / (len(g1) * len(g2)))

            mw_results.append({
                "Score": label,
                "U-stat": round(stat, 1),
                "p": "<0.001" if pval < 0.001 else round(pval, 4),
                "r (effect)": round(r, 4),
                "Confirmed Median": round(g1.median(), 2),
                "NoMatch Median": round(g2.median(), 2)
            })

mw_df = pd.DataFrame(mw_results)
df_to_md(mw_df, "Mann-Whitney U: Confirmed PLE passer vs No confirmed PLE match")
mw_df.to_csv(OUTDIR / "06C_mannwhitney_ple_status_observable.csv", index=False)

# ── 6D: Decile distribution by PLE status ────────────────────────────
ple_decile_dist = (
    ple_comp
    .dropna(subset=["PercentileDecile"])
    .groupby(["PLE_STATUS_LABEL", "PercentileDecile"], observed=True)
    .size()
    .unstack(fill_value=0)
    .reindex(index=plot_order, fill_value=0)
    .reindex(columns=DECILE_ORDER, fill_value=0)
)

row_totals = ple_decile_dist.sum(axis=1).replace(0, np.nan)
ple_decile_pct = (
    ple_decile_dist
    .div(row_totals, axis=0)
    .mul(100)
    .fillna(0)
    .round(2)
)

fig, ax = plt.subplots(figsize=(14, 5))
x = np.arange(len(DECILE_ORDER))
width = 0.25

for i, group in enumerate(plot_order):
    if group in ple_decile_pct.index:
        ax.bar(
            x + i * width,
            ple_decile_pct.loc[group].values,
            width,
            label=group,
            color=PALETTE_PLE[group],
            alpha=0.85
        )

ax.set_xticks(x + width)
ax.set_xticklabels(DECILE_ORDER)
ax.set_ylabel("% of Group")
ax.set_xlabel("Percentile Decile")
ax.set_title(
    "Section 6D: Decile Distribution by PLE Status\n"
    "(Observable Best-Record Cohorts Only)"
)
ax.legend()
ax.grid(True, axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
savefig("06D_ple_status_decile_distribution_observable")

ple_decile_pct.to_csv(OUTDIR / "06D_ple_status_decile_pct_observable.csv")

print("\n[Textual Summary]")
if "Confirmed PLE passer" in ple_decile_pct.index and "No confirmed PLE match" in ple_decile_pct.index:
    confirmed_top = ple_decile_pct.loc["Confirmed PLE passer", ["D8", "D9", "D10"]].sum()
    no_match_top  = ple_decile_pct.loc["No confirmed PLE match", ["D8", "D9", "D10"]].sum()
    print(f"  Confirmed PLE passers in D8–D10:     {confirmed_top:.1f}%")
    print(f"  No confirmed PLE match in D8–D10:    {no_match_top:.1f}%")
    print(f"  Difference:                          {confirmed_top - no_match_top:+.1f} percentage points")
======================================================================
SECTION 6: PLE STATUS PERFORMANCE PROFILE
======================================================================
PLE Status — Score Descriptives (Observable Best-Record Cohorts Only):
                       TotalRawScoreTRUE                                     PartIRawScoreTRUE                                    PartIIRawScoreTRUE                                    NMS_PER_num                                    NMS_GPS                                     NMS_APT                                     NMS_SA                                    
                                   count median   mean <lambda_0> <lambda_1>             count median  mean <lambda_0> <lambda_1>              count median  mean <lambda_0> <lambda_1>       count median  mean <lambda_0> <lambda_1>   count median   mean <lambda_0> <lambda_1>   count median   mean <lambda_0> <lambda_1>  count median   mean <lambda_0> <lambda_1>
PLE_STATUS_LABEL                                                                                                                                                                                                                                                                                                                                                         
Confirmed PLE passer               29269 143.00 144.76     125.00     164.00             29269  76.00 75.75      66.00      86.00              29269  68.00 69.02      57.00      80.00       28646  73.00 68.64      52.00      90.00   29273 564.00 569.18     506.00     632.00   29273 563.00 563.95     504.00     623.00  29273 554.00 556.91     497.00     618.00
No confirmed PLE match             35194 112.00 115.01      94.00     134.00             35194  61.00 61.31      51.00      72.00              35194  51.00 53.69      42.00      64.00       35075  36.00 40.28      15.00      63.00   35228 464.00 466.41     398.00     533.00   35228 474.00 475.34     410.00     539.00  35228 464.00 469.29     406.00     530.00
No description has been provided for this image
  ✓ Saved: 06B_ple_status_boxplot_observable.png

[Mann-Whitney U Tests: Confirmed PLE passer vs No confirmed PLE match]

── Mann-Whitney U: Confirmed PLE passer vs No confirmed PLE match ──
               Score       U-stat      p  r (effect)  Confirmed Median  NoMatch Median
     Total Raw Score 794198092.00 <0.001       -0.54            143.00          112.00
     Percentile Rank 773255790.00 <0.001       -0.54             73.00           36.00
GPS (Standard Score) 795288060.00 <0.001       -0.54            564.00          464.00
              Part I 774202494.00 <0.001       -0.50             76.00           61.00
             Part II 776289550.00 <0.001       -0.51             68.00           51.00

No description has been provided for this image
  ✓ Saved: 06D_ple_status_decile_distribution_observable.png

[Textual Summary]
  Confirmed PLE passers in D8–D10:     53.5%
  No confirmed PLE match in D8–D10:    19.8%
  Difference:                          +33.7 percentage points
# ============================================================
# ANALYSIS CELL 13A — Section 6E/6F: Survival and PLE Status by Decile
# ============================================================
print_section("SECTION 6E/6F: TOP DECILE SURVIVAL AND PLE STATUS PROFILE")

# ── 6E: Survival rate to top deciles (D8-D10) by CourseGroup ─────────
survival_base = (
    df_best_trend
    .dropna(subset=["CourseGroup", "PercentileDecile"])
    .copy()
)

survival_base["IS_TOP_DECILE"] = survival_base["PercentileDecile"].isin(["D8", "D9", "D10"])

survival_course = (
    survival_base
    .groupby("CourseGroup", observed=True)
    .agg(
        total_examinees=("IS_TOP_DECILE", "size"),
        top_decile_n=("IS_TOP_DECILE", "sum")
    )
    .reset_index()
)

survival_course["top_decile_n"] = survival_course["top_decile_n"].astype(int)
survival_course["survival_rate_pct"] = (
    survival_course["top_decile_n"] / survival_course["total_examinees"] * 100
).round(2)

survival_course = survival_course.sort_values(
    ["survival_rate_pct", "top_decile_n"],
    ascending=[False, False]
).reset_index(drop=True)

survival_course.to_csv(OUTDIR / "06E_survival_top_decile_by_course.csv", index=False)

df_to_md(
    survival_course,
    "Survival to Top Deciles (D8-D10) by Course Group"
)

fig, ax = plt.subplots(figsize=(10, 5))
plot_df = survival_course.iloc[::-1].copy()

ax.barh(
    plot_df["CourseGroup"],
    plot_df["survival_rate_pct"],
    color=[PALETTE_COURSE.get(c, "#9E9E9E") for c in plot_df["CourseGroup"]],
    alpha=0.85
)

for i, (_, row) in enumerate(plot_df.iterrows()):
    ax.text(
        row["survival_rate_pct"] + 0.3,
        i,
        f"{row['survival_rate_pct']:.1f}%",
        va="center",
        fontsize=9
    )

ax.set_xlabel("Survival Rate to D8-D10 (%)")
ax.set_ylabel("Course Group")
ax.set_title("Section 6E: Survival Rate to Top Deciles by Course Group")
ax.grid(True, axis="x", linestyle="--", alpha=0.4)
plt.tight_layout()
savefig("06E_survival_top_decile_by_course")

# ── 6F: PLE status profile by decile (observable cohorts only) ───────
ple_status_base = (
    df_best_observable
    .dropna(subset=["PercentileDecile", "PLE_STATUS_LABEL"])
    .copy()
)

plot_order = ["Confirmed PLE passer", "No confirmed PLE match"]

ple_status_decile = (
    ple_status_base
    .groupby(["PercentileDecile", "PLE_STATUS_LABEL"], observed=True)
    .size()
    .unstack(fill_value=0)
    .reindex(index=DECILE_ORDER, fill_value=0)
    .reindex(columns=plot_order, fill_value=0)
)

ple_status_decile.to_csv(OUTDIR / "06F_ple_status_by_decile_observable_count.csv")

row_totals = ple_status_decile.sum(axis=1).replace(0, np.nan)

ple_status_decile_pct = (
    ple_status_decile
    .div(row_totals, axis=0)
    .mul(100)
    .fillna(0)
    .round(2)
)

ple_status_decile_pct.to_csv(OUTDIR / "06F_ple_status_by_decile_observable_pct.csv")

df_to_md(
    ple_status_decile_pct.reset_index(),
    "PLE Status Composition by Decile (Observable Best-Record Cohorts Only)"
)

fig, ax = plt.subplots(figsize=(12, 5))

bottom = np.zeros(len(ple_status_decile_pct))

for status in plot_order:
    vals = ple_status_decile_pct[status].values
    ax.bar(
        ple_status_decile_pct.index.astype(str),
        vals,
        bottom=bottom,
        label=status,
        color=PALETTE_PLE[status],
        alpha=0.9
    )
    bottom += vals

ax.set_xlabel("Percentile Decile")
ax.set_ylabel("Percent within decile")
ax.set_ylim(0, 100)
ax.set_title(
    "Section 6F: PLE Status Composition by Decile\n"
    "(Observable best-record cohorts only)"
)
ax.legend()
ax.grid(True, axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
savefig("06F_ple_status_by_decile_observable")
======================================================================
SECTION 6E/6F: TOP DECILE SURVIVAL AND PLE STATUS PROFILE
======================================================================

── Survival to Top Deciles (D8-D10) by Course Group ──
                 CourseGroup  total_examinees  top_decile_n  survival_rate_pct
    Engineering & Technology              729           376              51.58
            Natural Sciences            40086         14244              35.53
                       Other             7885          2695              34.18
                   Education             3244          1050              32.37
            Medical & Allied            63067         17453              27.67
Social & Behavioral Sciences            15724          4327              27.52

No description has been provided for this image
  ✓ Saved: 06E_survival_top_decile_by_course.png

── PLE Status Composition by Decile (Observable Best-Record Cohorts Only) ──
PercentileDecile  Confirmed PLE passer  No confirmed PLE match
              D1                  8.77                   91.23
              D2                 16.07                   83.93
              D3                 19.20                   80.80
              D4                 25.66                   74.34
              D5                 46.30                   53.70
              D6                 51.81                   48.19
              D7                 57.62                   42.38
              D8                 60.44                   39.56
              D9                 67.82                   32.18
             D10                 76.25                   23.75

No description has been provided for this image
  ✓ Saved: 06F_ple_status_by_decile_observable.png
# ============================================================
# ANALYSIS CELL 14 — Section 7: Repeated NMAT Takers Analysis
# ============================================================
print_section("SECTION 7: REPEATED NMAT TAKERS — TRAJECTORY ANALYSIS")

# ── Attempt count per person ──────────────────────────────────────────
attempt_ct = df_trend.groupby("PERSON_KEY")["APPNO_CLEAN"].count().reset_index()
attempt_ct.columns = ["PERSON_KEY", "attempt_count"]

attempt_summary = attempt_ct["attempt_count"].value_counts().sort_index().reset_index()
attempt_summary.columns = ["Attempts", "Count"]
attempt_summary["Pct"] = (attempt_summary["Count"] / len(attempt_ct) * 100).round(2)

df_to_md(attempt_summary, "NMAT Attempt Count Distribution (All Persons)")
attempt_summary.to_csv(OUTDIR / "07_attempt_count_dist.csv", index=False)

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(attempt_summary["Attempts"].astype(str), attempt_summary["Count"], color="#1565C0", alpha=0.85)
ax.set_xlabel("Number of NMAT Attempts")
ax.set_ylabel("Number of Persons")
ax.set_title("Section 7A: NMAT Attempt Count Distribution")
for x, (_, row) in zip(ax.patches, attempt_summary.iterrows()):
    ax.text(
        x.get_x() + x.get_width()/2,
        x.get_height() + 100,
        f"{row['Pct']:.1f}%",
        ha="center", va="bottom", fontsize=9
    )
plt.tight_layout()
savefig("07A_attempt_count_distribution")

# ── Score change for repeat takers ────────────────────────────────────
repeat_persons = attempt_ct.loc[attempt_ct["attempt_count"] > 1, "PERSON_KEY"]
repeat_df = df_trend[df_trend["PERSON_KEY"].isin(repeat_persons)].copy()

first_last = (
    repeat_df
    .sort_values(["PERSON_KEY", "YEAR_INT", "APPNO_CLEAN"])
    .groupby("PERSON_KEY")
    .agg(
        first_year=("YEAR_INT", "first"),
        last_year=("YEAR_INT", "last"),
        first_pct=("NMS_PER_num", "first"),
        last_pct=("NMS_PER_num", "last"),
        first_raw=("TotalRawScoreTRUE", "first"),
        last_raw=("TotalRawScoreTRUE", "last"),
        n_attempts=("APPNO_CLEAN", "count")
    )
    .dropna(subset=["first_pct", "last_pct", "first_raw", "last_raw"])
    .reset_index()
)

first_last["pct_improvement"] = first_last["last_pct"] - first_last["first_pct"]
first_last["raw_improvement"] = first_last["last_raw"] - first_last["first_raw"]

trajectory_summary = pd.DataFrame([{
    "repeat_taker_persons": len(repeat_persons),
    "analytic_repeat_takers": len(first_last),
    "pct_improved_percentile": round((first_last["pct_improvement"] > 0).mean() * 100, 2),
    "pct_improved_raw": round((first_last["raw_improvement"] > 0).mean() * 100, 2),
    "median_percentile_change": round(first_last["pct_improvement"].median(), 2),
    "median_raw_change": round(first_last["raw_improvement"].median(), 2)
}])

df_to_md(trajectory_summary, "Repeat Taker Trajectory Summary")
trajectory_summary.to_csv(OUTDIR / "07B_repeat_taker_summary.csv", index=False)
first_last.to_csv(OUTDIR / "07B_repeat_taker_improvement.csv", index=False)

# ── Boxplots instead of histograms ────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 4))

plot_specs = [
    ("pct_improvement", "Percentile Rank Change", "#0288D1"),
    ("raw_improvement", "Total Raw Score Change", "#E65100")
]

for ax, (col, label, color) in zip(axes, plot_specs):
    vals = first_last[col].dropna()
    bp = ax.boxplot(
        vals,
        vert=True,
        patch_artist=True,
        medianprops=dict(color="white", linewidth=2),
        boxprops=dict(facecolor=color, alpha=0.8),
        whiskerprops=dict(color=color),
        capprops=dict(color=color)
    )
    ax.axhline(0, color="red", linestyle="--", linewidth=1.2, label="No change")
    ax.set_title(label)
    ax.set_ylabel("Last attempt – First attempt")
    ax.set_xticks([1])
    ax.set_xticklabels(["Repeat takers"])
    ax.legend(fontsize=9)
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)

plt.suptitle("Section 7B: Score Change Among Repeat NMAT Takers", fontsize=12, fontweight="bold")
plt.tight_layout()
savefig("07B_repeat_taker_change_boxplots")
======================================================================
SECTION 7: REPEATED NMAT TAKERS — TRAJECTORY ANALYSIS
======================================================================

── NMAT Attempt Count Distribution (All Persons) ──
 Attempts  Count   Pct
        1 101155 75.00
        2  25813 19.14
        3   6046  4.48
        4   1411  1.05
        5    332  0.25
        6     88  0.07
        7     17  0.01
        8      6  0.00
        9      1  0.00

No description has been provided for this image
  ✓ Saved: 07A_attempt_count_distribution.png
── Repeat Taker Trajectory Summary ──
 repeat_taker_persons  analytic_repeat_takers  pct_improved_percentile  pct_improved_raw  median_percentile_change  median_raw_change
                33714                   33703                    77.65             73.58                     11.00              12.00

No description has been provided for this image
  ✓ Saved: 07B_repeat_taker_change_boxplots.png
# ============================================================
# ANALYSIS CELL 15 — Section 8: Subtest Profile Analysis
# Radar / spider chart + heatmap of mean scores
# ============================================================
print_section("SECTION 8: SUBTEST PROFILE — APTITUDE vs SCIENCE BY GROUP")

std_subtests = {
    "Verbal": "NMS_VCss",
    "Inductive\nReasoning": "NMS_IRss",
    "Quantitative": "NMS_Qss",
    "Perceptual\nAcuity": "NMS_PAss",
    "Biology": "NMS_BIOss",
    "Physics": "NMS_PHYss",
    "Social\nScience": "NMS_SSCss",
    "Chemistry": "NMS_CHEMss"
}

# ── Mean subtest scores by UNI_TYPE ───────────────────────────────────
subtest_uni = df_uni.groupby("UNI_TYPE")[list(std_subtests.values())].mean()
subtest_uni.columns = list(std_subtests.keys())
subtest_uni.round(1).to_csv(OUTDIR / "08_subtest_by_uni_type.csv")

# ── Mean subtest scores by CourseGroup ────────────────────────────────
subtest_course = df_best_trend.groupby("CourseGroup")[list(std_subtests.values())].mean()
subtest_course.columns = list(std_subtests.keys())
subtest_course.round(1).to_csv(OUTDIR / "08_subtest_by_course.csv")

# ── Heatmap: UNI_TYPE × Subtest ───────────────────────────────────────
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

sns.heatmap(subtest_uni, annot=True, fmt=".1f", cmap="coolwarm",
            center=500, cbar_kws={"label":"Mean Standard Score"}, ax=axes[0])
axes[0].set_title("Section 8A: Mean Subtest Scores by University Type")

sns.heatmap(subtest_course, annot=True, fmt=".1f", cmap="coolwarm",
            center=500, cbar_kws={"label":"Mean Standard Score"}, ax=axes[1])
axes[1].set_title("Section 8B: Mean Subtest Scores by Pre-Med Background")

plt.tight_layout()
savefig("08_subtest_heatmap")

# ── Radar chart: UNI_TYPE ─────────────────────────────────────────────
labels  = list(std_subtests.keys())
n_labs  = len(labels)
angles  = [n / float(n_labs) * 2 * np.pi for n in range(n_labs)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
for uni_type, color in [("Public","#2196F3"),("Private","#FF9800"),("Foreign","#9C27B0")]:
    if uni_type not in subtest_uni.index:
        continue
    vals = subtest_uni.loc[uni_type].tolist() + [subtest_uni.loc[uni_type].tolist()[0]]
    ax.plot(angles, vals, "o-", linewidth=2, label=uni_type, color=color)
    ax.fill(angles, vals, alpha=0.08, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)
ax.set_title("Section 8C: Subtest Profile by University Type (Radar)", fontsize=11, pad=20)
ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
plt.tight_layout()
savefig("08C_radar_subtest_uni_type")

df_to_md(subtest_uni.round(1), "Mean Subtest Scores by University Type")
df_to_md(subtest_course.round(1), "Mean Subtest Scores by Course Group")
======================================================================
SECTION 8: SUBTEST PROFILE — APTITUDE vs SCIENCE BY GROUP
======================================================================
No description has been provided for this image
  ✓ Saved: 08_subtest_heatmap.png
No description has been provided for this image
  ✓ Saved: 08C_radar_subtest_uni_type.png

── Mean Subtest Scores by University Type ──
 Verbal  Inductive\nReasoning  Quantitative  Perceptual\nAcuity  Biology  Physics  Social\nScience  Chemistry
 486.60                511.10        506.50              493.00   494.50   506.60           490.50     493.30
 484.50                499.90        498.80              499.40   489.70   497.90           490.10     491.50
 494.40                512.00        516.30              507.20   510.00   517.30           501.20     512.40


── Mean Subtest Scores by Course Group ──
 Verbal  Inductive\nReasoning  Quantitative  Perceptual\nAcuity  Biology  Physics  Social\nScience  Chemistry
 499.90                516.60        509.00              501.00   489.30   508.90           505.90     508.70
 525.10                540.70        575.50              519.30   501.10   570.90           507.60     547.10
 498.30                510.60        497.30              505.70   483.90   493.80           506.00     483.30
 476.50                499.70        512.30              503.40   520.40   516.00           470.70     518.20
 505.10                512.10        511.60              495.60   496.30   512.40           511.40     492.00
 453.30                469.90        490.60              476.50   466.90   490.40           481.20     485.70

# ============================================================
# ANALYSIS CELL 16 — Section 9C: Confirmed PLE linkage by university type
# Observable cohorts only
# ============================================================
print_section("SECTION 9C: CONFIRMED PLE LINKAGE BY UNIVERSITY TYPE")

ple_link_uni = (
    df_uni_observable
    .groupby("UNI_TYPE", observed=True)
    .apply(lambda x: pd.Series({
        "n_observable_best_records": len(x),
        "confirmed_ple_passers": int((x["HAS_CONFIRMED_PLE"] == True).sum()),
        "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
        "confirmed_ple_share_pct": round((x["HAS_CONFIRMED_PLE"] == True).mean() * 100, 2)
    }))
    .reset_index()
)

df_to_md(ple_link_uni, "Confirmed PLE linkage by University Type (observable cohorts)")
ple_link_uni.to_csv(OUTDIR / "09C_confirmed_ple_linkage_by_uni_type.csv", index=False)

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(
    ple_link_uni["UNI_TYPE"],
    ple_link_uni["confirmed_ple_share_pct"],
    color=[PALETTE_UNI.get(u, "#9E9E9E") for u in ple_link_uni["UNI_TYPE"]]
)
for bar, val in zip(bars, ple_link_uni["confirmed_ple_share_pct"]):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
            f"{val:.1f}%", ha="center", va="bottom", fontsize=10)

ax.set_ylabel("Confirmed PLE passer share (%)")
ax.set_title("Section 9C: Confirmed PLE Passer Share by University Type\n(Observable best-record cohorts only)")
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
savefig("09C_confirmed_ple_linkage_by_uni_type")
======================================================================
SECTION 9C: CONFIRMED PLE LINKAGE BY UNIVERSITY TYPE
======================================================================

── Confirmed PLE linkage by University Type (observable cohorts) ──
UNI_TYPE  n_observable_best_records  confirmed_ple_passers  no_confirmed_ple_match  confirmed_ple_share_pct
 Foreign                    2122.00                 786.00                 1336.00                    37.04
 Private                   47916.00               21402.00                26514.00                    44.67
  Public                   13632.00                6755.00                 6877.00                    49.55

No description has been provided for this image
  ✓ Saved: 09C_confirmed_ple_linkage_by_uni_type.png
# ============================================================
# ANALYSIS CELL 17 — Section 10: PLE Year Gap Analysis
# ============================================================
print_section("SECTION 10: PLE YEAR GAP — NMAT TO PLE PASSAGE")

gap_data = df_ple_best.dropna(subset=["PLE_YEAR_GAP"]).copy()
gap_data["PLE_YEAR_GAP"] = gap_data["PLE_YEAR_GAP"].astype(int)

print(f"PLE-matched best records with year gap: {len(gap_data):,}")

gap_desc = gap_data["PLE_YEAR_GAP"].describe()
print("\nYear Gap Summary:")
print(gap_desc.to_string())

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Distribution
gap_counts = gap_data["PLE_YEAR_GAP"].value_counts().sort_index()
axes[0].bar(gap_counts.index, gap_counts.values, color="#1565C0", alpha=0.85)
axes[0].axvline(gap_data["PLE_YEAR_GAP"].median(), color="red", linestyle="--",
                label=f"Median: {gap_data['PLE_YEAR_GAP'].median():.0f} yrs")
axes[0].set_xlabel("Year Gap (PLE Year − NMAT Year)")
axes[0].set_ylabel("Count")
axes[0].set_title("Section 10A: Distribution of Year Gap")
axes[0].legend()

# Gap by decile
gap_by_decile = gap_data.groupby("PercentileDecile", observed=True)["PLE_YEAR_GAP"].median()
axes[1].bar(gap_by_decile.index.astype(str), gap_by_decile.values,
            color=[plt.get_cmap("RdYlGn",10)(i) for i in range(10)])
axes[1].set_xlabel("Percentile Decile")
axes[1].set_ylabel("Median Year Gap")
axes[1].set_title("Section 10B: Median Year Gap by NMAT Decile")
axes[1].grid(True, axis="y", linestyle="--", alpha=0.4)

plt.suptitle("Section 10: NMAT-to-PLE Year Gap Analysis", fontsize=12, fontweight="bold")
plt.tight_layout()
savefig("10_ple_year_gap")

gap_by_decile.reset_index().rename(columns={"PLE_YEAR_GAP":"median_gap"}).to_csv(
    OUTDIR / "10_gap_by_decile.csv", index=False
)

print(f"\n[Textual Interpretation]")
print(f"  Median time from NMAT to PLE: {gap_data['PLE_YEAR_GAP'].median():.0f} years")
print(f"  Most common gap:              {gap_counts.idxmax()} years ({gap_counts.max():,} records)")
print(f"  Short gap (<5 yrs, flagged):  {(gap_data['PLE_YEAR_GAP'] < 5).sum():,} records")
======================================================================
SECTION 10: PLE YEAR GAP — NMAT TO PLE PASSAGE
======================================================================
PLE-matched best records with year gap: 33,929

Year Gap Summary:
count   33929.00
mean        6.38
std         1.02
min         5.00
25%         6.00
50%         6.00
75%         7.00
max        15.00
No description has been provided for this image
  ✓ Saved: 10_ple_year_gap.png

[Textual Interpretation]
  Median time from NMAT to PLE: 6 years
  Most common gap:              6 years (17,911 records)
  Short gap (<5 yrs, flagged):  0 records
# ============================================================
# ANALYSIS CELL 18 — Section 11: Gender Analysis
# ============================================================
print_section("SECTION 11: GENDER DISAGGREGATION")

# SEX_CLEAN is pre-computed in Cell 3 on df_raw, so all subsets
# (df_best_trend, df_uni, etc.) already carry it. No re-assignment needed here.
# Source: CEM SEX field (text: "Male" / "Female"), joined in the cleaning pipeline.
# Note:   NMA_Sex (coded 1=Male / 2=Female) is the NMAT-native field;
#         SEX from CEM is the preferred text representation used here.

gender_valid = df_best_trend[df_best_trend["SEX_CLEAN"].isin(["Male","Female"])].copy()

print(f"Records with gender info: {len(gender_valid):,}")
print(gender_valid["SEX_CLEAN"].value_counts().to_string())

# ── Decile by gender ──────────────────────────────────────────────────
gender_decile = (
    gender_valid.dropna(subset=["PercentileDecile"])
    .groupby(["SEX_CLEAN","PercentileDecile"], observed=True).size()
    .unstack(fill_value=0)
    .reindex(columns=DECILE_ORDER, fill_value=0)
)
gender_decile_pct = gender_decile.div(gender_decile.sum(axis=1), axis=0) * 100
gender_decile_pct.round(2).to_csv(OUTDIR / "11_gender_decile_pct.csv")

fig, ax = plt.subplots(figsize=(13, 5))
x = np.arange(len(DECILE_ORDER))
for i, (gender, color) in enumerate([("Female","#E91E63"),("Male","#1565C0")]):
    if gender in gender_decile_pct.index:
        ax.bar(x + i*0.35, gender_decile_pct.loc[gender], width=0.35,
               label=gender, color=color, alpha=0.85)
ax.set_xticks(x + 0.175)
ax.set_xticklabels(DECILE_ORDER)
ax.set_ylabel("% within Gender")
ax.set_title("Section 11: Decile Distribution by Gender")
ax.legend()
ax.grid(True, axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
savefig("11_gender_decile")

# ── Gender PLE pass rate and descriptive summary ──────────────────────
gender_ple = (
    gender_valid.groupby("SEX_CLEAN")
    .apply(lambda x: pd.Series({
        "n": len(x),
        "ple_passers": (x["IS_PLE_ANALYSIS_SAFE"]==True).sum(),
        "ple_pct": (x["IS_PLE_ANALYSIS_SAFE"]==True).mean()*100,
        "median_pct_rank": x["NMS_PER_num"].median()
    }))
    .round(2)
    .reset_index()
)
df_to_md(gender_ple, "Gender: PLE Pass Rate and Median Percentile")
gender_ple.to_csv(OUTDIR / "11_gender_ple_summary.csv", index=False)

# ── Mann-Whitney U: gender × percentile rank ──────────────────────────
f_pct = gender_valid[gender_valid["SEX_CLEAN"]=="Female"]["NMS_PER_num"].dropna()
m_pct = gender_valid[gender_valid["SEX_CLEAN"]=="Male"]["NMS_PER_num"].dropna()
if len(f_pct) > 5 and len(m_pct) > 5:
    u_stat, p_val = stats.mannwhitneyu(f_pct, m_pct, alternative="two-sided")
    r_eff = 1 - (2*u_stat / (len(f_pct)*len(m_pct)))
    print(f"\n[Mann-Whitney U: Female vs Male — Percentile Rank]")
    print(f"  U = {u_stat:.0f}, p = {'<0.001' if p_val<0.001 else round(p_val,4)}, "
          f"r = {r_eff:.4f}")
    print(f"  Female median: {f_pct.median():.1f}  |  Male median: {m_pct.median():.1f}")
======================================================================
SECTION 11: GENDER DISAGGREGATION
======================================================================
Records with gender info: 133,766
SEX_CLEAN
Female    74153
Male      59613
No description has been provided for this image
  ✓ Saved: 11_gender_decile.png

── Gender: PLE Pass Rate and Median Percentile ──
SEX_CLEAN        n  ple_passers  ple_pct  median_pct_rank
   Female 74153.00     21656.00    29.20            50.00
     Male 59613.00     14645.00    24.57            49.00

[Mann-Whitney U: Female vs Male — Percentile Rank]
  U = 2180681937, p = 0.0958, r = -0.0053
  Female median: 50.0  |  Male median: 49.0
# ============================================================
# ANALYSIS CELL 19 — Section 12: Dunn Post-Hoc Tests
# ============================================================
print_section("SECTION 12: DUNN POST-HOC TESTS (ADJUSTED)")

def run_dunn(data, group_col, value_col, label):
    groups = data.dropna(subset=[group_col, value_col])
    group_list = groups[group_col].unique().tolist()
    if len(group_list) < 2:
        return

    dunn_result = sp.posthoc_dunn(
        groups, val_col=value_col, group_col=group_col, p_adjust="bonferroni"
    )

    print(f"\n[Dunn Post-Hoc: {label}] (Bonferroni-adjusted p-values)")
    print(dunn_result.round(4).to_string())

    fname = f"12_dunn_{label.lower().replace(' ','_').replace('→','_')}"
    dunn_result.round(4).to_csv(OUTDIR / f"{fname}.csv")

    fig, ax = plt.subplots(figsize=(max(6, len(group_list)), max(4, len(group_list)-1)))
    sns.heatmap(dunn_result, annot=True, fmt=".3f", cmap="RdYlGn_r",
                vmin=0, vmax=0.1, linewidths=0.4, ax=ax)
    ax.set_title(f"Dunn Post-Hoc p-values: {label}\n(Red = significant difference, Green = no significant difference)")
    plt.tight_layout()
    savefig(fname)

# UNI_TYPE
run_dunn(df_uni, "UNI_TYPE", "NMS_PER_num", "UNI_TYPE vs Percentile")

# CourseGroup
run_dunn(df_best_trend, "CourseGroup", "NMS_PER_num", "CourseGroup vs Percentile")

# Year (sample to avoid memory issues with many groups)
run_dunn(df_best_trend.sample(min(20000, len(df_best_trend)), random_state=42),
         "Year", "TotalRawScoreTRUE", "Year vs Raw Score (sample)")
======================================================================
SECTION 12: DUNN POST-HOC TESTS (ADJUSTED)
======================================================================
[Dunn Post-Hoc: UNI_TYPE vs Percentile] (Bonferroni-adjusted p-values)
         Foreign  Private  Public
Foreign     1.00     0.05    0.00
Private     0.05     1.00    0.00
Public      0.00     0.00    1.00
No description has been provided for this image
  ✓ Saved: 12_dunn_uni_type_vs_percentile.png
[Dunn Post-Hoc: CourseGroup vs Percentile] (Bonferroni-adjusted p-values)
                              Education  Engineering & Technology  Medical & Allied  Natural Sciences  Other  Social & Behavioral Sciences
Education                          1.00                      0.00              0.00              1.00   1.00                          0.00
Engineering & Technology           0.00                      1.00              0.00              0.00   0.00                          0.00
Medical & Allied                   0.00                      0.00              1.00              0.00   0.00                          0.00
Natural Sciences                   1.00                      0.00              0.00              1.00   1.00                          0.00
Other                              1.00                      0.00              0.00              1.00   1.00                          0.00
Social & Behavioral Sciences       0.00                      0.00              0.00              0.00   0.00                          1.00
No description has been provided for this image
  ✓ Saved: 12_dunn_coursegroup_vs_percentile.png

[Dunn Post-Hoc: Year vs Raw Score (sample)] (Bonferroni-adjusted p-values)
      2006  2007  2008  2009  2010  2011  2012  2013  2014  2015  2016  2017  2018
2006  1.00  1.00  0.17  1.00  1.00  1.00  0.00  0.02  0.00  0.00  0.00  0.00  0.00
2007  1.00  1.00  1.00  1.00  1.00  1.00  0.00  0.53  0.00  0.00  0.00  0.00  0.00
2008  0.17  1.00  1.00  1.00  0.00  1.00  0.17  1.00  0.00  0.00  1.00  0.00  0.00
2009  1.00  1.00  1.00  1.00  0.12  1.00  0.00  1.00  0.00  0.00  0.00  0.00  0.00
2010  1.00  1.00  0.00  0.12  1.00  0.29  0.00  0.00  0.00  0.00  0.00  0.00  0.00
2011  1.00  1.00  1.00  1.00  0.29  1.00  0.00  0.16  0.00  0.00  0.00  0.00  0.00
2012  0.00  0.00  0.17  0.00  0.00  0.00  1.00  0.06  1.00  0.62  1.00  0.11  0.00
2013  0.02  0.53  1.00  1.00  0.00  0.16  0.06  1.00  0.00  0.00  0.81  0.00  0.00
2014  0.00  0.00  0.00  0.00  0.00  0.00  1.00  0.00  1.00  1.00  0.02  1.00  0.00
2015  0.00  0.00  0.00  0.00  0.00  0.00  0.62  0.00  1.00  1.00  0.01  1.00  0.00
2016  0.00  0.00  1.00  0.00  0.00  0.00  1.00  0.81  0.02  0.01  1.00  0.00  0.00
2017  0.00  0.00  0.00  0.00  0.00  0.00  0.11  0.00  1.00  1.00  0.00  1.00  0.00
2018  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  1.00
No description has been provided for this image
  ✓ Saved: 12_dunn_year_vs_raw_score_(sample).png
# ============================================================
# ANALYSIS CELL 20 — Section 13: Policy-relevant PLE alignment tables
# Observable cohorts only
# ============================================================
print_section("SECTION 13: POLICY-RELEVANT PLE ALIGNMENT TABLES")

policy_base = df_best_observable.copy()

# ── Table 1: By year ──────────────────────────────────────────────────
table_year = (
    policy_base.groupby("Year", observed=True)
    .apply(lambda x: pd.Series({
        "n_observable_best_records": len(x),
        "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
        "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
        "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2)
    }))
    .reset_index()
    .sort_values("Year")
)
df_to_md(table_year, "Table 1. Confirmed PLE alignment by NMAT year (observable cohorts only)")
table_year.to_csv(OUTDIR / "13T1_confirmed_ple_by_year_observable.csv", index=False)

# ── Table 2: By course group ──────────────────────────────────────────
table_course = (
    policy_base.groupby("CourseGroup", observed=True)
    .apply(lambda x: pd.Series({
        "n_observable_best_records": len(x),
        "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
        "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
        "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
        "median_percentile_rank": round(x["NMS_PER_num"].median(), 2)
    }))
    .reset_index()
    .sort_values("confirmed_ple_share_pct", ascending=False)
)
df_to_md(table_course, "Table 2. Confirmed PLE alignment by pre-med background (observable cohorts only)")
table_course.to_csv(OUTDIR / "13T2_confirmed_ple_by_course_observable.csv", index=False)

# ── Table 3: By university type ───────────────────────────────────────
table_uni = (
    policy_base[policy_base["UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
    .groupby("UNI_TYPE", observed=True)
    .apply(lambda x: pd.Series({
        "n_observable_best_records": len(x),
        "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
        "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
        "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
        "median_percentile_rank": round(x["NMS_PER_num"].median(), 2)
    }))
    .reset_index()
)
df_to_md(table_uni, "Table 3. Confirmed PLE alignment by university type (observable cohorts only)")
table_uni.to_csv(OUTDIR / "13T3_confirmed_ple_by_uni_type_observable.csv", index=False)
======================================================================
SECTION 13: POLICY-RELEVANT PLE ALIGNMENT TABLES
======================================================================

── Table 1. Confirmed PLE alignment by NMAT year (observable cohorts only) ──
 Year  n_observable_best_records  confirmed_ple_passers  no_confirmed_ple_match  confirmed_ple_share_pct
 2006                    3665.00                2038.00                 1627.00                    55.61
 2007                    3660.00                1868.00                 1792.00                    51.04
 2008                    4849.00                2514.00                 2335.00                    51.85
 2009                    6881.00                3226.00                 3655.00                    46.88
 2010                    8008.00                3808.00                 4200.00                    47.55
 2011                    8731.00                3853.00                 4878.00                    44.13
 2012                    9145.00                4066.00                 5079.00                    44.46
 2013                    9121.00                3951.00                 5170.00                    43.32
 2014                   10441.00                3949.00                 6492.00                    37.82


── Table 2. Confirmed PLE alignment by pre-med background (observable cohorts only) ──
                 CourseGroup  n_observable_best_records  confirmed_ple_passers  no_confirmed_ple_match  confirmed_ple_share_pct  median_percentile_rank
                   Education                    2973.00                1541.00                 1432.00                    51.83                   52.00
                       Other                    6189.00                2853.00                 3336.00                    46.10                   55.00
            Natural Sciences                   15219.00                6921.00                 8298.00                    45.48                   66.00
            Medical & Allied                   35433.00               16061.00                19372.00                    45.33                   49.00
Social & Behavioral Sciences                    4385.00                1783.00                 2602.00                    40.66                   64.00
    Engineering & Technology                     302.00                 114.00                  188.00                    37.75                   71.00

── Table 3. Confirmed PLE alignment by university type (observable cohorts only) ──
UNI_TYPE  n_observable_best_records  confirmed_ple_passers  no_confirmed_ple_match  confirmed_ple_share_pct  median_percentile_rank
 Foreign                    2122.00                 786.00                 1336.00                    37.04                   52.00
 Private                   47916.00               21402.00                26514.00                    44.67                   52.00
  Public                   13632.00                6755.00                 6877.00                    49.55                   67.00

# ============================================================
# ANALYSIS CELL 21 — Section 14: Executive Summary Print
# ============================================================
print_section("SECTION 14: EXECUTIVE SUMMARY")

n_all  = len(df_all)
n_best = len(df_best)
yr_min = int(df_all["Year"].min())
yr_max = int(df_all["Year"].max())
overall_med_pct = df_best_trend["NMS_PER_num"].median()
overall_med_raw = df_best_trend["TotalRawScoreTRUE"].median()

# ── Attempt counts — defined here (Issue 2 fix) ───────────────────────
# Cell 14 uses attempt_ct (local variable); this cell needs its own
# computation using df_all so it covers the full dataset.
attempt_counts = df_all.groupby("PERSON_KEY")["APPNO_CLEAN"].count()
repeat_pct     = (attempt_counts > 1).sum() / attempt_counts.shape[0] * 100

# ── PLE person counts — clarified (Issue 6 fix) ───────────────────────
# df_ple_safe : all NMAT rows where IS_PLE_ANALYSIS_SAFE == True
#               (includes every attempt by a matched PLE passer)
# df_ple_best : one row per matched PLE passer (IS_BEST_NMAT_RECORD == True)
n_ple_rows    = len(df_ple_safe)   # NMAT rows, not unique persons
n_ple_persons = len(df_ple_best)   # unique matched PLE passers (best record)
n_ambig       = (df_all["PLE_MATCH_STATUS"]=="AMBIGUOUS").sum()
n_unmatched   = (df_all["PLE_MATCH_STATUS"]=="UNMATCHED_FINAL").sum()

print("""
╔══════════════════════════════════════════════════════════════════════╗
║          NMAT PERFORMANCE ANALYSIS — EXECUTIVE SUMMARY             ║
╚══════════════════════════════════════════════════════════════════════╝
""")

print(f"  Study Period:             {yr_min}–{yr_max}")
print(f"  Total NMAT Records:       {n_all:,}")
print(f"  Unique Persons:           {df_all['PERSON_KEY'].nunique():,}  "
      f"(deduped by normalized name + BDATE where available)")
print(f"  Repeat NMAT Takers:       {repeat_pct:.1f}% of persons took NMAT 2+ times")
print(f"  Max Attempts (1 person):  {attempt_counts.max()}")
print()
print(f"  Overall Median Raw Score (TotalRawScoreTRUE):  {overall_med_raw:.1f}")
print(f"  Overall Median Percentile Rank:                {overall_med_pct:.1f}")
print()
print(f"  ── PLE Matching ───────────────────────────────────────────────")
print(f"  PLE passers in source file (PLE_DATA 2011–2022):  43,630")
print(f"  NMAT rows with IS_PLE_ANALYSIS_SAFE = True:       {n_ple_rows:,}")
print(f"    (all NMAT attempts by a matched PLE passer)")
print(f"  Unique matched PLE passers (best record only):    {n_ple_persons:,}")
print(f"    (one row per person — used in PLE comparative analyses)")
print(f"  AMBIGUOUS — flagged, included with caution:       {n_ambig:,}")
print(f"  UNMATCHED_FINAL — excluded from analysis:         {n_unmatched:,}")
print()
print(f"  ⚠️  PLE match rates decline sharply after 2014 due to PLE data")
print(f"     coverage ending at 2022 — NOT indicative of lower pass rates.")
print(f"     NMAT 2018 cohort's earliest board eligibility is 2023 (outside data).")
print()
print(f"  ── University Type Coverage (best records) ─────────────────────")
for ut, n in df_best_trend["UNI_TYPE"].value_counts().items():
    print(f"    {ut:<20} {n:>7,}  ({n/len(df_best_trend)*100:.1f}%)")
print()
print(f"  ── Course Group Coverage (best records) ────────────────────────")
for cg, n in df_best_trend["CourseGroup"].value_counts().items():
    print(f"    {cg:<35} {n:>7,}  ({n/len(df_best_trend)*100:.1f}%)")
print()
print(f"  ── Data Quality ────────────────────────────────────────────────")
print(f"    StoredTotal ≠ DerivedTotal: {n_stored_mismatch:,} records")
print(f"    CalcTotal   ≠ DerivedTotal: {int(n_calc_mismatch):,} records")
print(f"    Analysis uses TotalRawScoreTRUE (re-derived from 8 components).")
print()
print(f"  ── Methodological Notes ────────────────────────────────────────")
print(f"    PERSON_KEY = NAME_NORM + BDATE_CLEAN.")
print(f"    When BDATE is available it improves deduplication accuracy;")
print(f"    records without a valid BDATE rely on name alone.")
print(f"    IS_BEST_NMAT_RECORD for PLE passers = the specifically matched")
print(f"    attempt (not necessarily peak score). See methodology note.")
print()
print(f"  Output folder: {OUTDIR}")
print(f"  Files saved:   {len(list(OUTDIR.glob('*.csv'))) + len(list(OUTDIR.glob('*.png')))} files")

# ── Final output inventory ─────────────────────────────────────────────
print("\n[Output File Inventory]")
for f in sorted(OUTDIR.glob("*.csv")) + sorted(OUTDIR.glob("*.png")):
    print(f"  {f.name}")
======================================================================
SECTION 14: EXECUTIVE SUMMARY
======================================================================

╔══════════════════════════════════════════════════════════════════════╗
║          NMAT PERFORMANCE ANALYSIS — EXECUTIVE SUMMARY             ║
╚══════════════════════════════════════════════════════════════════════╝

  Study Period:             2006–2018
  Total NMAT Records:       178,927
  Unique Persons:           134,869  (deduped by normalized name + BDATE where available)
  Repeat NMAT Takers:       25.0% of persons took NMAT 2+ times
  Max Attempts (1 person):  9

  Overall Median Raw Score (TotalRawScoreTRUE):  122.0
  Overall Median Percentile Rank:                50.0

  ── PLE Matching ───────────────────────────────────────────────
  PLE passers in source file (PLE_DATA 2011–2022):  43,630
  NMAT rows with IS_PLE_ANALYSIS_SAFE = True:       49,986
    (all NMAT attempts by a matched PLE passer)
  Unique matched PLE passers (best record only):    36,305
    (one row per person — used in PLE comparative analyses)
  AMBIGUOUS — flagged, included with caution:       1,723
  UNMATCHED_FINAL — excluded from analysis:         0

  ⚠️  PLE match rates decline sharply after 2014 due to PLE data
     coverage ending at 2022 — NOT indicative of lower pass rates.
     NMAT 2018 cohort's earliest board eligibility is 2023 (outside data).

  ── University Type Coverage (best records) ─────────────────────
    Private              101,342  (75.7%)
    Public                27,797  (20.8%)
    Foreign                3,270  (2.4%)
    Not Specified          1,395  (1.0%)

  ── Course Group Coverage (best records) ────────────────────────
    Medical & Allied                     63,900  (47.8%)
    Natural Sciences                     41,430  (31.0%)
    Social & Behavioral Sciences         16,462  (12.3%)
    Other                                 7,983  (6.0%)
    Education                             3,279  (2.5%)
    Engineering & Technology                750  (0.6%)

  ── Data Quality ────────────────────────────────────────────────
    StoredTotal ≠ DerivedTotal: 0 records
    CalcTotal   ≠ DerivedTotal: 0 records
    Analysis uses TotalRawScoreTRUE (re-derived from 8 components).

  ── Methodological Notes ────────────────────────────────────────
    PERSON_KEY = NAME_NORM + BDATE_CLEAN.
    When BDATE is available it improves deduplication accuracy;
    records without a valid BDATE rely on name alone.
    IS_BEST_NMAT_RECORD for PLE passers = the specifically matched
    attempt (not necessarily peak score). See methodology note.

  Output folder: dataset\analysis_output
  Files saved:   95 files

[Output File Inventory]
  00_data_validation_missing.csv
  00_data_validation_summary.csv
  00E_college_uni_type_post_cleaning.csv
  00E_university_type_location_conflicts.csv
  00E_university_type_location_summary.csv
  01A_yearly_summary.csv
  01B_subtest_median_by_year.csv
  01C_parti_partii_trend.csv
  02_iqr_by_year.csv
  02_kruskal_wallis_by_year.csv
  03A_decile_by_year_count.csv
  03A_decile_by_year_pct.csv
  04A_ext_inst_decile_pct.csv
  04A_ext_inst_descriptive.csv
  04A_ext_inst_type_location_col_pct.csv
  04A_ext_inst_type_location_count.csv
  04A_ext_inst_type_location_row_pct.csv
  04A_kw_uni_type_descriptive.csv
  04A_uni_type_decile_count.csv
  04A_uni_type_decile_pct.csv
  04B_course_decile_count.csv
  04B_course_decile_pct.csv
  04B_kw_course_descriptive.csv
  04C_college_decile_by_uni_type_pct.csv
  04C_college_top10_d10_by_uni_type.csv
  04C_course_group_distribution.csv
  04D_chi_square_uni_type_vs_decile.csv
  04D_uni_type_decile_expected.csv
  04D_uni_type_decile_observed.csv
  05A_flow_uni_type_to_decile.csv
  05B_flow_course_group_to_decile.csv
  05C_decile_to_ple_status_row_pct_observable.csv
  05C_flow_decile_to_ple_status_observable.csv
  05D_top10_pathways_uni_to_top_deciles.csv
  05D_uni_type_composition_top_deciles.csv
  05E_course_group_composition_top_deciles.csv
  05E_top10_pathways_course_to_top_deciles.csv
  06A_ple_status_descriptive_observable.csv
  06C_mannwhitney_ple_status_observable.csv
  06D_ple_status_decile_pct_observable.csv
  06E_survival_top_decile_by_course.csv
  06F_ple_status_by_decile_observable_count.csv
  06F_ple_status_by_decile_observable_pct.csv
  07_attempt_count_dist.csv
  07B_repeat_taker_improvement.csv
  07B_repeat_taker_summary.csv
  08_subtest_by_course.csv
  08_subtest_by_uni_type.csv
  09C_confirmed_ple_linkage_by_uni_type.csv
  10_gap_by_decile.csv
  11_gender_decile_pct.csv
  11_gender_ple_summary.csv
  12_dunn_coursegroup_vs_percentile.csv
  12_dunn_uni_type_vs_percentile.csv
  12_dunn_year_vs_raw_score_(sample).csv
  13T1_confirmed_ple_by_year_observable.csv
  13T2_confirmed_ple_by_course_observable.csv
  13T3_confirmed_ple_by_uni_type_observable.csv
  XX_examinee_count_by_year.csv
  00_data_validation.png
  00E_university_type_integrity.png
  01A_overall_trend_raw_and_percentile.png
  01B_boxplots_by_year.png
  01C_parti_partii_trend.png
  02_iqr_stability_by_year.png
  03A_heatmap_decile_by_year.png
  03B_stacked_bar_decile_by_year.png
  03C_top_bottom_decile_trend.png
  04A_ext_inst_matrix_heatmap.png
  04A_ext_inst_top_decile.png
  04A_ext_inst_violin.png
  04A_heatmap_uni_type_decile.png
  04A_top_decile_by_uni_type.png
  04B_heatmap_course_decile.png
  04B_top_decile_by_course.png
  04C_course_group_pie.png
  05A_sankey_uni_type_to_decile.png
  05B_sankey_course_group_to_decile.png
  05C_sankey_decile_to_ple_status_observable.png
  05DE_top10_pathways_to_top_deciles.png
  06B_ple_status_boxplot_observable.png
  06D_ple_status_decile_distribution_observable.png
  06E_survival_top_decile_by_course.png
  06F_ple_status_by_decile_observable.png
  07A_attempt_count_distribution.png
  07B_repeat_taker_change_boxplots.png
  08_subtest_heatmap.png
  08C_radar_subtest_uni_type.png
  09C_confirmed_ple_linkage_by_uni_type.png
  10_ple_year_gap.png
  11_gender_decile.png
  12_dunn_coursegroup_vs_percentile.png
  12_dunn_uni_type_vs_percentile.png
  12_dunn_year_vs_raw_score_(sample).png
  XX_examinee_count_by_year.png
# ============================================================
# ANALYSIS CELL X — Examinee Count by Year
# ============================================================
print_section("SECTION X: EXAMINEE COUNT BY YEAR")

# Use best-record trend subset (one row per person, 2006–2018)
year_counts = (
    df_best_trend
    .groupby("Year")
    .size()
    .reset_index(name="ExamineeCount")
    .sort_values("Year")
)

df_to_md(year_counts, "Examinee Count by Year (Best-Record Subset)")
year_counts.to_csv(OUTDIR / "XX_examinee_count_by_year.csv", index=False)

fig, ax = plt.subplots(figsize=(14, 5))

bars = ax.bar(
    year_counts["Year"].astype(int),
    year_counts["ExamineeCount"],
    color="#1565C0",
    alpha=0.9
)

for bar, val in zip(bars, year_counts["ExamineeCount"]):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 120,
        f"{val:,}",
        ha="center",
        va="bottom",
        fontsize=9
    )

ax.set_title("Examinee Count by Year (2006–2018)", fontsize=12, fontweight="bold")
ax.set_xlabel("NMAT Year")
ax.set_ylabel("Number of Examinees")
ax.xaxis.set_major_locator(mticker.MultipleLocator(1))
ax.grid(True, axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
savefig("XX_examinee_count_by_year")

print("\n[Summary]")
print(f"  Total best-record examinees shown: {year_counts['ExamineeCount'].sum():,}")
print(f"  Highest year count: {year_counts.loc[year_counts['ExamineeCount'].idxmax(), 'Year']} "
      f"({year_counts['ExamineeCount'].max():,})")
print(f"  Lowest year count:  {year_counts.loc[year_counts['ExamineeCount'].idxmin(), 'Year']} "
      f"({year_counts['ExamineeCount'].min():,})")
======================================================================
SECTION X: EXAMINEE COUNT BY YEAR
======================================================================

── Examinee Count by Year (Best-Record Subset) ──
 Year  ExamineeCount
 2006           3665
 2007           3660
 2008           4849
 2009           6881
 2010           8008
 2011           8731
 2012           9145
 2013           9121
 2014          10441
 2015          10402
 2016          12609
 2017          23955
 2018          22337

No description has been provided for this image
  ✓ Saved: XX_examinee_count_by_year.png

[Summary]
  Total best-record examinees shown: 133,804
  Highest year count: 2017 (23,955)
  Lowest year count:  2007 (3,660)