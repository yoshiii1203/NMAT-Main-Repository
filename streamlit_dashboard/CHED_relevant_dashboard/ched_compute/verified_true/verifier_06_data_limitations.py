"""
verifier_06_data_limitations.py — Verifies Tab 6 (Data, Methods, and Limitations)
computations against actual NMAT_Exodus.parquet data.

Replicates the EXACT subset logic and aggregation from dashboard.py TAB 6.
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
    os.path.dirname(__file__), "..", "page_results", "06_data_limitations.md"
)

# ---------------------------------------------------------------------------
# Load data — same subset logic as dashboard.py load_data + validate_schema
# ---------------------------------------------------------------------------
df_all = pd.read_parquet(PARQUET_PATH, engine="pyarrow")

# Normalize boolean flags like dashboard.validate_schema
for c in ["IS_BEST_NMAT_RECORD", "IS_PLE_ANALYSIS_SAFE"]:
    if c in df_all.columns:
        if not pd.api.types.is_bool_dtype(df_all[c]):
            df_all[c] = df_all[c].astype(str).str.upper().isin(["TRUE", "1", "YES"])
        else:
            df_all[c] = df_all[c].fillna(False)

# Normalize HasTRUErawScores (str column) — dashboard does NOT cast this, so
# comparisons to Python bool/float will behave as string comparisons.
# We replicate the EXACT dashboard behaviour for comparison purposes,
# then also compute the semantically correct value.

# Subsets (same as dashboard)
df_best = df_all[df_all["IS_BEST_NMAT_RECORD"] == True].copy()
df_obs = df_best[df_best["Year"] <= 2014].copy()

# HAS_CONFIRMED_PLE (same as dashboard)
if "IS_PLE_ANALYSIS_SAFE" in df_obs.columns:
    df_obs["HAS_CONFIRMED_PLE"] = (df_obs["IS_PLE_ANALYSIS_SAFE"] == True)
else:
    df_obs["HAS_CONFIRMED_PLE"] = False

# B5_PLUS bins
B5_PLUS = ["B5", "B6", "B7", "B8", "B9", "B10"]

# ---------------------------------------------------------------------------
# Replicate every metric from dashboard.py TAB 6
# ---------------------------------------------------------------------------

# 1. Total rows
total_rows = len(df_all)

# 2. Best-record count (N_BEST)
best_count = len(df_best)

# 3. Unique examinees (best record)
n_unique = int(df_best["PERSON_KEY"].nunique())

# 4. Observable cohort
n_obs = len(df_obs)

# 5. Repeat takers
n_repeat = int((df_all.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique() > 1).sum())

# 6. TRUE raw score count — dashboard uses == True on a str column, which yields 0
n_true_dashboard = int((df_all["HasTRUErawScores"] == True).sum())
# Semantically correct (for reference):
n_true_actual = int((df_all["HasTRUErawScores"] == "True").sum())

# 7. Formula mismatches — hardcoded as 0 in dashboard
n_formula_mismatch = 0

# 8. Stored-vs-derived mismatches — dashboard uses == 1.0 on str column, which yields 0
stored_mismatch_dashboard = int((df_all["StoredVsDerivedMismatch"] == 1.0).sum())
stored_mismatch_actual = int((df_all["StoredVsDerivedMismatch"] == "1.0").sum())

# 9. Calc-vs-derived mismatches
calc_mismatch_dashboard = int((df_all["CalcVsDerivedMismatch"] == 1.0).sum())
calc_mismatch_actual = int((df_all["CalcVsDerivedMismatch"] == "1.0").sum())

# 10. PLE passers (all rows)
n_all_ple = int((df_all["IS_PLE_ANALYSIS_SAFE"] == True).sum())

# 11. PLE passers (best record, observable)
n_obs_ple = int(df_obs["HAS_CONFIRMED_PLE"].sum())

# 12. Clean subset (B5+, Filipino, >=5yr gap) — exact same logic as dashboard
_clean = df_obs[
    (df_obs["IS_PLE_ANALYSIS_SAFE"] == True)
    & (df_obs["PLE_YEAR_GAP"] >= 5)
    & (df_obs["FOREIGNER_STATUS"] == "Filipino")
].copy()
n_clean_ple = len(_clean)
n_clean_b5 = len(_clean[_clean["PercentileBin"].isin(B5_PLUS)])

# 13. Median PLE year gap
avg_gap = df_obs[df_obs["HAS_CONFIRMED_PLE"]]["PLE_YEAR_GAP"].median()

# ---------------------------------------------------------------------------
# Expected values from page_results/06_data_limitations.md
# ---------------------------------------------------------------------------
expected = {
    "total_rows": 178927,
    "best_count": 133804,  # N_BEST from dashboard (not shown in page_results but computed)
    "n_unique": 133558,
    "n_obs": 64501,
    "n_repeat": 33713,
    "n_true_dashboard": 0,  # dashboard computes 0 due to str-vs-bool
    "stored_mismatch_dashboard": 0,  # dashboard computes 0 due to str-vs-float
    "calc_mismatch_dashboard": 0,
    "n_all_ple": 49986,
    "n_obs_ple": 29273,
    "n_clean_ple": 27151,
    "n_clean_b5": 23357,
    "avg_gap": 6.0,
}

# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------
checks = [
    ("Total rows", total_rows, expected["total_rows"]),
    ("Best-record count (N_BEST)", best_count, expected["best_count"]),
    ("Unique examinees (best record)", n_unique, expected["n_unique"]),
    ("Observable cohort size", n_obs, expected["n_obs"]),
    ("Repeat takers", n_repeat, expected["n_repeat"]),
    ("Repeat taker share (%)", round(n_repeat / n_unique * 100, 2),
     round(expected["n_repeat"] / expected["n_unique"] * 100, 2)),
    ("TRUE raw score count (dashboard logic)", n_true_dashboard, expected["n_true_dashboard"]),
    ("TRUE raw score count (actual)", n_true_actual, None),
    ("Formula mismatches", n_formula_mismatch, 0),
    ("Stored-vs-derived mismatches (dashboard logic)", stored_mismatch_dashboard, expected["stored_mismatch_dashboard"]),
    ("Stored-vs-derived mismatches (actual)", stored_mismatch_actual, None),
    ("Calc-vs-derived mismatches (dashboard logic)", calc_mismatch_dashboard, expected["calc_mismatch_dashboard"]),
    ("Calc-vs-derived mismatches (actual)", calc_mismatch_actual, None),
    ("PLE passers (all rows)", n_all_ple, expected["n_all_ple"]),
    ("PLE passers (best record, observable)", n_obs_ple, expected["n_obs_ple"]),
    ("Clean subset total", n_clean_ple, expected["n_clean_ple"]),
    ("Clean subset B5+", n_clean_b5, expected["n_clean_b5"]),
    ("Median PLE year gap", avg_gap, expected["avg_gap"]),
]

pass_count = 0
fail_count = 0
results = []

results.append("# Verifier 06: Data, Methods, and Limitations (Tab 6)")
results.append("")
results.append("**Data source:** `NMAT_Exodus.parquet`")
results.append("**Dashboard logic replicated:** yes (bug-for-bug for dtype-sensitive comparisons)")
results.append("")

# Overview table
results.append("## Overview")
results.append("")
results.append("| Metric | Value |")
results.append("|--------|-------|")
results.append(f"| Total rows | {total_rows:,} |")
results.append(f"| Best-record examinees | {best_count:,} |")
results.append(f"| Unique examinees (PERSON_KEY) | {n_unique:,} |")
results.append(f"| Pre-2015 observable cohort | {n_obs:,} |")
results.append(f"| Repeat takers | {n_repeat:,} ({n_repeat/n_unique*100:.0f}%) |")
results.append(f"| PLE passers (all rows) | {n_all_ple:,} |")
results.append(f"| PLE passers (best, observable) | {n_obs_ple:,} |")
results.append(f"| Clean subset (Filipino, >=5yr gap) | {n_clean_ple:,} |")
results.append(f"| Clean subset B5+ | {n_clean_b5:,} |")
results.append(f"| Median PLE year gap | {avg_gap} |")
results.append("")

# Detailed comparison
results.append("## Metrics Comparison")
results.append("")
results.append("| Metric | Computed (from parquet) | Expected (page_results) | Status |")
results.append("|--------|----------------------|------------------------|--------|")

for label, computed, exp in checks:
    if exp is None:
        # Informational only (actual correct value, not in page_results)
        status = "INFO"
        exp_str = "(not in page_results)"
        results.append(f"| {label} | {computed:,} | {exp_str} | {status} |")
        continue

    # Round floats for comparison
    if isinstance(computed, float) and isinstance(exp, float):
        match = abs(computed - exp) < 0.01
    else:
        match = computed == exp

    if match:
        status = "PASS"
        pass_count += 1
    else:
        status = "**MISMATCH**"
        fail_count += 1

    if isinstance(computed, float):
        results.append(f"| {label} | {computed} | {exp} | {status} |")
    else:
        results.append(f"| {label} | {computed:,} | {exp:,} | {status} |")

results.append("")
results.append(f"**Checks:** {pass_count + fail_count} total, {pass_count} passed, {fail_count} failed")
results.append("")

# Data integrity notes
results.append("## Column Type Notes")
results.append("")
results.append("Several columns in the parquet file are stored as **string** dtype, which causes")
results.append("the dashboard's numeric/bool comparisons (`== True`, `== 1.0`) to always return")
results.append("`False`.  The verifier replicates this bug-for-bug to match the dashboard display,")
results.append("while also showing the semantically correct values for reference.")
results.append("")
results.append("| Column | Actual dtype | Dashboard comparison | Dashboard result | Actual count |")
results.append("|--------|-------------|---------------------|-----------------|-------------|")
results.append(f"| `HasTRUErawScores` | str | `== True` | {n_true_dashboard:,} | {n_true_actual:,} |")
results.append(f"| `StoredVsDerivedMismatch` | str | `== 1.0` | {stored_mismatch_dashboard:,} | {stored_mismatch_actual:,} |")
results.append(f"| `CalcVsDerivedMismatch` | str | `== 1.0` | {calc_mismatch_dashboard:,} | {calc_mismatch_actual:,} |")
results.append("")
results.append("*Note: `IS_BEST_NMAT_RECORD` and `IS_PLE_ANALYSIS_SAFE` are properly normalized")
results.append("to bool dtype by `validate_schema()`, so their comparisons work correctly.*")
results.append("")

output = "\n".join(results)
print(output)

# ---------------------------------------------------------------------------
# Save output log
# ---------------------------------------------------------------------------
LOG_PATH = os.path.join(
    os.path.dirname(__file__), "VERIFIER_streamlit_output_log_06.md"
)
with open(LOG_PATH, "w", encoding="utf-8") as f:
    f.write(output)

print(f"\nLog saved to {LOG_PATH}")
