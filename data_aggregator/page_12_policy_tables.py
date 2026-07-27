"""
Page 12: Policy Tables
Replicates ALL computations from dashboard.py tab12 (lines ~2700-2900).
Extracts unfiltered data and saves to page_results/12_policy_tables.md.

Produces:
- PLE alignment by year (observable cohort)
- PLE alignment by CourseGroup (+ median_percentile_rank)
- PLE alignment by UNI_TYPE (+ median_percentile_rank)
- Survival to top bins (B8-B10) by CourseGroup
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "data_aggregator"))

import numpy as np
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 300)
pd.set_option("display.max_colwidth", 60)

from config import BIN_ORDER, RESULTS_DIR
from helpers import load_data


def run() -> str:
    df, subsets = load_data()

    # Core subsets matching dashboard tab12
    bestobservable = subsets["bestobservable"].copy()
    besttrend = subsets["besttrend"].copy()

    lines = []

    # ── Header ──
    lines.append("# Page 12: Policy Tables")
    lines.append("")
    lines.append(f"**Generated:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("**Data source:** NMAT_Exodus.parquet (Pipeline 4)")
    lines.append("")
    lines.append("**Data subsets:** `bestobservable` (PLE-linked analyses, Year <= 2014) and `besttrend` (survival analysis, 2006-2018)")
    lines.append("")
    lines.append("**Filters:** None (full unfiltered dataset)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Ensure PLE_STATUS_LABEL exists
    if "PLE_STATUS_LABEL" not in bestobservable.columns:
        bestobservable["PLE_STATUS_LABEL"] = np.where(
            bestobservable["IS_PLE_ANALYSIS_SAFE"] == True,
            "Confirmed PLE passer",
            "No confirmed PLE match"
        )

    # ================================================================
    # 1. PLE Alignment by Year
    # ================================================================
    lines.append("## 1. PLE Alignment by Year")
    lines.append("")
    lines.append("PLE status distribution across NMAT years for the observable best-record cohort (Year <= 2014).")
    lines.append("")

    t_year = (
        bestobservable
        .groupby("Year", observed=True)
        .apply(lambda x: pd.Series({
            "n_observable_best_records": len(x),
            "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
            "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
            "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
        }))
        .reset_index()
        .sort_values("Year")
    )

    lines.append("**Table: PLE alignment by NMAT year**")
    lines.append("")
    lines.append(t_year.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # ================================================================
    # 2. PLE Alignment by CourseGroup
    # ================================================================
    lines.append("---")
    lines.append("## 2. PLE Alignment by Course Group")
    lines.append("")
    lines.append("PLE status and median percentile rank by course group (observable best-record cohort).")
    lines.append("")

    t_course = (
        bestobservable
        .groupby("CourseGroup", observed=True)
        .apply(lambda x: pd.Series({
            "n_observable_best_records": len(x),
            "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
            "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
            "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
            "median_percentile_rank": round(x["NMS_PER_num"].median(), 2),
        }))
        .reset_index()
        .sort_values("confirmed_ple_share_pct", ascending=False)
    )

    lines.append("**Table: PLE alignment by CourseGroup**")
    lines.append("")
    lines.append(t_course.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # ================================================================
    # 3. PLE Alignment by UNI_TYPE
    # ================================================================
    lines.append("---")
    lines.append("## 3. PLE Alignment by University Type")
    lines.append("")
    lines.append("PLE status and median percentile rank by university type (Public, Private, Foreign). Observable best-record cohort.")
    lines.append("")

    t_uni = (
        bestobservable[bestobservable["UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
        .groupby("UNI_TYPE", observed=True)
        .apply(lambda x: pd.Series({
            "n_observable_best_records": len(x),
            "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
            "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
            "confirmed_ple_share_pct": round((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2),
            "median_percentile_rank": round(x["NMS_PER_num"].median(), 2),
        }))
        .reset_index()
    )

    lines.append("**Table: PLE alignment by UNI_TYPE**")
    lines.append("")
    lines.append(t_uni.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # ================================================================
    # 4. Survival to Top Bins (B8-B10) by CourseGroup
    # ================================================================
    lines.append("---")
    lines.append("## 4. Survival to Top Decile Bins (B8-B10) by Course Group")
    lines.append("")
    lines.append("Proportion of examinees in each course group whose best-record percentile rank falls in the top three bins (B8 = 70th-79th, B9 = 80th-89th, B10 = 90th-99th).")
    lines.append("")

    survival_base = (
        besttrend
        .dropna(subset=["CourseGroup", "PercentileBin"])
        .copy()
    )
    survival_base["IS_TOP_BIN"] = survival_base["PercentileBin"].isin(["B8", "B9", "B10"])

    survival = (
        survival_base
        .groupby("CourseGroup", observed=True)
        .agg(
            total_examinees=("IS_TOP_BIN", "size"),
            top_decile_n=("IS_TOP_BIN", "sum"),
        )
        .reset_index()
    )
    survival["top_decile_n"] = survival["top_decile_n"].astype(int)
    survival["survival_rate_pct"] = (
        survival["top_decile_n"] / survival["total_examinees"] * 100
    ).round(2)
    survival = survival.sort_values(
        ["survival_rate_pct", "top_decile_n"],
        ascending=[False, False],
    ).reset_index(drop=True)

    lines.append("**Table: Survival to top bins (B8-B10) by CourseGroup**")
    lines.append("")
    lines.append(survival.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # ── Footer ──
    lines.append("---")
    lines.append("")
    lines.append("*All PLE-linked analyses use the observable best-record cohort (Year <= 2014) to avoid misclassifying later cohorts as non-passers before their licensure window closes.*")
    lines.append("")

    return "\n".join(lines)


def save():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = RESULTS_DIR / "12_policy_tables.md"
    content = run()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved: {out_path.resolve()}")


if __name__ == "__main__":
    save()
