"""
verifier_01_national_profile.py — Verifies Tab 1 (National Profile) computations
against actual NMAT_Exodus.parquet data and expected page_results values.

Replicates the EXACT subset logic and aggregation from dashboard.py.
"""
import sys
import os
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PARQUET_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "NMAT_Exodus.parquet"
)
PAGE_RESULTS_PATH = os.path.join(
    os.path.dirname(__file__), "..", "page_results", "01_national_profile.md"
)

# ---------------------------------------------------------------------------
# Load data (exact same subset logic as dashboard.py load_data / validate_schema)
# ---------------------------------------------------------------------------
df = pd.read_parquet(PARQUET_PATH, engine="pyarrow")
df_best = df[df["IS_BEST_NMAT_RECORD"] == True].copy()
df_obs = df_best[df_best["Year"] <= 2014].copy()

# ---------------------------------------------------------------------------
# Dashboard Tab 1 Metrics (replicated exactly)
# ---------------------------------------------------------------------------
N_BEST = len(df_best)
N_UNIQUE = int(df_best["PERSON_KEY"].nunique())
NMAT_YEARS = int(df_best["Year"].nunique())
MEDIAN_PCT_RANK = df_best["NMS_PER_num"].median()

# Yearly summary (examinee volume + median percentile + median raw)
yearly_summary = (
    df_best.groupby("Year", observed=True)
    .agg(
        examinees=("APPNO_CLEAN", "count"),
        median_pct=("NMS_PER_num", "median"),
        median_raw=("TotalRawScoreTRUE", "median"),
    )
    .reset_index()
)

# UNI_TYPE composition
uni_dist = df_best["UNI_TYPE"].value_counts().reset_index()
uni_dist.columns = ["UNI_TYPE", "Count"]

# CourseGroup composition
course_dist = df_best["CourseGroup"].value_counts().reset_index()
course_dist.columns = ["CourseGroup", "Count"]

# Repeat takers (across ALL data, same as dashboard)
N_REPEAT = int((df.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique() > 1).sum())

# ---------------------------------------------------------------------------
# PLE linkage metrics (from dashboard's pre-computed values + page_results)
# ---------------------------------------------------------------------------
N_OBS = len(df_obs)
if "IS_PLE_ANALYSIS_SAFE" in df_obs.columns:
    ple_matched = df_obs[df_obs["IS_PLE_ANALYSIS_SAFE"] == True]
else:
    ple_matched = df_obs[df_obs["IS_PLE_PASSER"] == True]
N_PLE_MATCHED = len(ple_matched)

OVERALL_LINKAGE = (N_PLE_MATCHED / N_OBS * 100) if N_OBS > 0 else 0.0

# 5-year rolling average (2010-2014)
linkage_rates_5yr = []
for y in range(2010, 2015):
    y_denom = int((df_obs["Year"] == y).sum())
    y_numer = int((ple_matched["Year"] == y).sum())
    if y_denom > 0:
        linkage_rates_5yr.append(y_numer / y_denom * 100)
AVG_5YR = np.mean(linkage_rates_5yr) if linkage_rates_5yr else 0.0

# Annual linkage table
annual_linkage = []
for y in sorted(df_best["Year"].unique()):
    n_best = int((df_best["Year"] == y).sum())
    if y <= 2014:
        n_denom = int((df_obs["Year"] == y).sum())
        n_ple = int((ple_matched["Year"] == y).sum())
        linkage = n_ple / n_denom * 100 if n_denom > 0 else None
        annual_linkage.append({
            "Year": y, "n_best": n_best, "n_denom": n_denom,
            "n_ple": n_ple, "linkage": linkage
        })

# Also compute 5-yr rolling for alignment with page_results
rolling_window = []
annual_with_rolling = []
for y in sorted(df_best["Year"].unique()):
    n_best = int((df_best["Year"] == y).sum())
    if y <= 2014:
        n_denom = int((df_obs["Year"] == y).sum())
        n_ple = int((ple_matched["Year"] == y).sum())
        linkage = n_ple / n_denom * 100 if n_denom > 0 else None
    else:
        n_denom = 0
        n_ple = 0
        linkage = None
    
    rolling_window.append(linkage)
    if len(rolling_window) > 5:
        rolling_window.pop(0)
    
    if linkage is not None and len(rolling_window) >= 5:
        valid = [v for v in rolling_window if v is not None]
        rolling_avg = np.mean(valid) if len(valid) >= 5 else None
    else:
        rolling_avg = None
    
    annual_with_rolling.append({
        "Year": y, "n_best": n_best, "n_denom": n_denom,
        "n_ple": n_ple, "linkage": linkage, "rolling_avg": rolling_avg
    })

# ---------------------------------------------------------------------------
# Expected values from page_results
# ---------------------------------------------------------------------------
expected = {
    "Best-record examinees": 133804,
    "Pre-2015 Cohort Size": 64501,
    "Matched to PLE Passer Records": 29273,
    "Overall NMAT-to-PLE Linkage Rate": 45.38,
    "5-Year Rolling Average Linkage (2010-2014)": 43.46,
}

expected_annual = {
    2006: {"n_best": 3665, "n_denom": 3665, "n_ple": 2038, "linkage": 55.61},
    2007: {"n_best": 3660, "n_denom": 3660, "n_ple": 1868, "linkage": 51.04},
    2008: {"n_best": 4849, "n_denom": 4849, "n_ple": 2514, "linkage": 51.85},
    2009: {"n_best": 6881, "n_denom": 6881, "n_ple": 3226, "linkage": 46.88},
    2010: {"n_best": 8008, "n_denom": 8008, "n_ple": 3808, "linkage": 47.55, "rolling": 50.59},
    2011: {"n_best": 8731, "n_denom": 8731, "n_ple": 3853, "linkage": 44.13, "rolling": 48.29},
    2012: {"n_best": 9145, "n_denom": 9145, "n_ple": 4066, "linkage": 44.46, "rolling": 46.97},
    2013: {"n_best": 9121, "n_denom": 9121, "n_ple": 3951, "linkage": 43.32, "rolling": 45.27},
    2014: {"n_best": 10441, "n_denom": 10441, "n_ple": 3949, "linkage": 37.82, "rolling": 43.46},
}

# ---------------------------------------------------------------------------
# Comparison helpers
# ---------------------------------------------------------------------------
MISMATCH_THRESHOLD_PCT = 0.5  # 0.5% relative difference

def pct_diff(computed, expected_val):
    """Return relative percentage difference."""
    if expected_val == 0:
        return 0.0 if computed == 0 else 100.0
    return abs(computed - expected_val) / abs(expected_val) * 100

def flag_if_mismatch(label, computed, expected_val, is_pct=False):
    """Flag if relative difference > MISMATCH_THRESHOLD_PCT."""
    if is_pct:
        # Compare the percentage values directly
        diff = abs(computed - expected_val)
        if diff > MISMATCH_THRESHOLD_PCT:
            return f" **MISMATCH** (diff={diff:.2f}pp)"
        return ""
    else:
        if expected_val == 0:
            if computed != 0:
                return f" **MISMATCH** (computed={computed}, expected={expected_val})"
            return ""
        rel_diff = pct_diff(computed, expected_val)
        if rel_diff > MISMATCH_THRESHOLD_PCT:
            return f" **MISMATCH** (rel_diff={rel_diff:.2f}%)"
        return ""

# ---------------------------------------------------------------------------
# Results collector
# ---------------------------------------------------------------------------
results = []
mismatches = []

def add_result(label, computed, expected_val=None, is_pct=False, fmt_spec=None):
    """Add a comparison row."""
    if fmt_spec == "int":
        computed_str = f"{computed:,}" if computed is not None else "N/A"
        exp_str = f"{expected_val:,}" if expected_val is not None else "N/A"
    elif fmt_spec == "pct":
        computed_str = f"{computed:.2f}%" if computed is not None else "N/A"
        exp_str = f"{expected_val:.2f}%" if expected_val is not None else "N/A"
    elif fmt_spec == "float1":
        computed_str = f"{computed:.1f}" if computed is not None else "N/A"
        exp_str = f"{expected_val:.1f}" if expected_val is not None else "N/A"
    else:
        computed_str = str(computed) if computed is not None else "N/A"
        exp_str = str(expected_val) if expected_val is not None else "N/A"
    
    flag = ""
    if expected_val is not None:
        flag = flag_if_mismatch(label, computed, expected_val, is_pct)
        if flag:
            mismatches.append(f"{label}: computed={computed_str}, expected={exp_str}{flag}")
    
    results.append({
        "Metric": label,
        "Computed (from parquet)": computed_str,
        "Expected (page_results)": exp_str if expected_val is not None else "—",
        "Status": "PASS" if not flag else "MISMATCH"
    })

# ── Key Metrics ──
add_result("Best-record examinees (N_BEST)", N_BEST, expected["Best-record examinees"], fmt_spec="int")
add_result("Unique persons (PERSON_KEY) in best", N_UNIQUE, None, fmt_spec="int")
add_result("NMAT years covered", NMAT_YEARS, None, fmt_spec="int")
add_result("Median percentile rank", MEDIAN_PCT_RANK, None, fmt_spec="float1")
add_result("Pre-2015 Cohort Size (N_OBS)", N_OBS, expected["Pre-2015 Cohort Size"], fmt_spec="int")
add_result("Matched to PLE Passer Records", N_PLE_MATCHED, expected["Matched to PLE Passer Records"], fmt_spec="int")
add_result("Overall NMAT-to-PLE Linkage Rate", OVERALL_LINKAGE, expected["Overall NMAT-to-PLE Linkage Rate"], is_pct=True, fmt_spec="pct")
add_result("5-Year Rolling Avg Linkage (2010-2014)", AVG_5YR, expected["5-Year Rolling Average Linkage (2010-2014)"], is_pct=True, fmt_spec="pct")

# ── Repeat takers ──
repeat_pct = N_REPEAT / N_UNIQUE * 100 if N_UNIQUE > 0 else 0
add_result("Repeat takers (all data, >1 attempt)", N_REPEAT, None, fmt_spec="int")
add_result("Repeat taker share of unique persons", repeat_pct, None, is_pct=True, fmt_spec="pct")

# ── UNI_TYPE composition ──
for _, row in uni_dist.iterrows():
    ut = row["UNI_TYPE"]
    cnt = int(row["Count"])
    share = cnt / N_BEST * 100
    add_result(f"UNI_TYPE: {ut}", f"{cnt:,} ({share:.1f}%)", None)

# ── CourseGroup composition ──
cg_total = course_dist["Count"].sum()
for _, row in course_dist.iterrows():
    cg = row["CourseGroup"]
    cnt = int(row["Count"])
    share = cnt / cg_total * 100
    add_result(f"CourseGroup: {cg}", f"{cnt:,} ({share:.1f}%)", None)

# ── Annual NMAT-to-PLE Linkage Rates ──
for entry in annual_with_rolling:
    y = entry["Year"]
    if y in expected_annual:
        exp = expected_annual[y]
        add_result(f"Annual: {y} n (Best Record)", entry["n_best"], exp["n_best"], fmt_spec="int")
        add_result(f"Annual: {y} n (Pre-2015 Cohort)", entry["n_denom"], exp["n_denom"], fmt_spec="int")
        add_result(f"Annual: {y} n PLE Matched", entry["n_ple"], exp["n_ple"], fmt_spec="int")
        add_result(f"Annual: {y} Linkage Rate", entry["linkage"], exp["linkage"], is_pct=True, fmt_spec="pct")
        if "rolling" in exp:
            r = entry["rolling_avg"]
            add_result(f"Annual: {y} 5-Yr Rolling Avg", r if r is not None else None, exp["rolling"], is_pct=True, fmt_spec="pct")

# ── Extra: Verify PersonKey uniqueness in best ──
person_best_counts = df[df["IS_BEST_NMAT_RECORD"] == True].groupby("PERSON_KEY").size()
max_best_per_person = person_best_counts.max()
dup_best_persons = int((person_best_counts > 1).sum())
add_result("Max best records per person", max_best_per_person, 1, fmt_spec="int")
add_result("Persons with >1 best record", dup_best_persons, 0, fmt_spec="int")

# ---------------------------------------------------------------------------
# Print output (Markdown)
# ---------------------------------------------------------------------------
def print_table(rows, title):
    """Print a markdown table from a list of dicts."""
    print(f"\n### {title}")
    print()
    print("| Metric | Computed (from parquet) | Expected (page_results) | Status |")
    print("|--------|------------------------|-------------------------|--------|")
    for r in rows:
        print(f"| {r['Metric']} | {r['Computed (from parquet)']} | {r['Expected (page_results)']} | {r['Status']} |")

# ── Overall Summary ──
print("# Verifier 01: National Profile (Tab 1)")
print()
print(f"**Data source:** `NMAT_Exodus.parquet`")
print(f"**Best-record examinees:** {N_BEST:,}")
print(f"**Pre-2015 observable cohort:** {N_OBS:,}")
print(f"**PLE matched (pre-2015):** {N_PLE_MATCHED:,}")
print()

total_checks = len(results)
pass_count = sum(1 for r in results if r["Status"] == "PASS")
fail_count = sum(1 for r in results if r["Status"] == "MISMATCH")
print(f"**Checks:** {total_checks} total, {pass_count} passed, {fail_count} failed")
print()

if mismatches:
    print("### MISMATCHES DETECTED")
    for m in mismatches:
        print(f"- {m}")
    print()
else:
    print("**All checks passed.** No discrepancies found (>0.5% threshold).")
    print()

# ── Key Metrics ──
print("## Key Metrics Comparison")
print()
print("| Metric | Computed (from parquet) | Expected (page_results) | Status |")
print("|--------|------------------------|-------------------------|--------|")
key_metrics = [r for r in results if not r["Metric"].startswith("Annual:") and not r["Metric"].startswith("UNI_TYPE:") and not r["Metric"].startswith("CourseGroup:")]
for r in key_metrics:
    print(f"| {r['Metric']} | {r['Computed (from parquet)']} | {r['Expected (page_results)']} | {r['Status']} |")

# ── UNI_TYPE Composition ──
print()
print("## UNI_TYPE Composition")
print()
print("| Metric | Computed (from parquet) | Expected (page_results) | Status |")
print("|--------|------------------------|-------------------------|--------|")
uni_rows = [r for r in results if r["Metric"].startswith("UNI_TYPE:")]
for r in uni_rows:
    print(f"| {r['Metric']} | {r['Computed (from parquet)']} | {r['Expected (page_results)']} | {r['Status']} |")

# ── CourseGroup Composition ──
print()
print("## CourseGroup Composition")
print()
print("| Metric | Computed (from parquet) | Expected (page_results) | Status |")
print("|--------|------------------------|-------------------------|--------|")
cg_rows = [r for r in results if r["Metric"].startswith("CourseGroup:")]
for r in cg_rows:
    print(f"| {r['Metric']} | {r['Computed (from parquet)']} | {r['Expected (page_results)']} | {r['Status']} |")

# ── Yearly Summary (Dashboard-specific) ──
print()
print("## Yearly Summary (Dashboard Tab 1)")
print()
print("| Year | Examinees | Median Percentile Rank | Median Raw Score |")
print("|:----:|:---------:|:---------------------:|:----------------:|")
for _, row in yearly_summary.iterrows():
    y = int(row["Year"])
    print(f"| {y} | {row['examinees']:,} | {row['median_pct']:.1f} | {row['median_raw']:.1f} |")

# ── Annual NMAT-to-PLE Linkage ──
print()
print("## Annual NMAT-to-PLE Linkage Rates")
print()
print("| Year | n (Best Record) | n (Pre-2015 Cohort) | n PLE Matched | Linkage Rate | 5-Year Rolling Avg | Status |")
print("|:----:|:----------------:|:---------------------:|:-------------:|:------------:|:------------------:|:------:|")
for entry in annual_with_rolling:
    y = entry["Year"]
    n_best = entry["n_best"]
    n_denom = entry["n_denom"]
    n_ple = entry["n_ple"]
    linkage = entry["linkage"]
    rolling = entry["rolling_avg"]
    
    if y in expected_annual:
        exp = expected_annual[y]
        # Check all sub-metrics
        flags = []
        if n_best != exp["n_best"]:
            flags.append("n_best")
        if n_denom != exp["n_denom"]:
            flags.append("n_denom")
        if n_ple != exp["n_ple"]:
            flags.append("n_ple")
        if linkage is not None and abs(linkage - exp["linkage"]) > MISMATCH_THRESHOLD_PCT:
            flags.append("linkage")
        if "rolling" in exp and rolling is not None and abs(rolling - exp["rolling"]) > MISMATCH_THRESHOLD_PCT:
            flags.append("rolling")
        status = "PASS" if not flags else f"MISMATCH ({', '.join(flags)})"
    else:
        status = "—"
    
    linkage_str = f"{linkage:.2f}%" if linkage is not None else "N/A"
    rolling_str = f"{rolling:.2f}%" if rolling is not None else "—"
    
    asterisk = " *" if y == 2014 else ""
    print(f"| {y}{asterisk} | {n_best:,} | {n_denom:,} | {n_ple:,} | {linkage_str} | {rolling_str} | {status} |")

print()
print("*Observable cohort ends at 2014. Years after 2014 have insufficient time for PLE to be taken and observed in our data.*")
print()

# ── Repeat taker detail ──
print("## Repeat Taker Context")
print()
print(f"Of {N_UNIQUE:,} unique examinees (best-record PERSON_KEY count),")
print(f"{N_REPEAT:,} ({repeat_pct:.0f}%) took the NMAT more than once.")
print()

if mismatches:
    print("## Mismatch Details")
    print()
    for m in mismatches:
        print(f"- {m}")
    print()

print("---")
print("*Verifier replicates dashboard.py Tab 1 exact subset logic (IS_BEST_NMAT_RECORD==True, Year<=2014).*")
print(f"*Threshold for flagging mismatch: >{MISMATCH_THRESHOLD_PCT}% relative difference (or >{MISMATCH_THRESHOLD_PCT}pp for percentage values).*")
