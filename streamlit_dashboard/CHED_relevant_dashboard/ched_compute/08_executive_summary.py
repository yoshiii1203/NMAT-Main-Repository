"""
08_executive_summary.py — Executive summary of key CHED dashboard indicators.

Computes:
  - Total best records, years covered, median total raw score, median percentile
  - Unique examinees, repeat takers, observable cohort size, PLE linkage rate
  - UNI_TYPE distribution, CourseGroup distribution
  - Pie chart data tables, summary table with all indicators
"""

import sys
import os
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from config import BIN_ORDER, UNI_TYPE_ORDER, LINKAGE_LABEL
from helpers import (
    load_data,
    create_subsets,
    today_str,
    write_md,
    pct,
    fmt,
    make_metric_table,
    compute_linkage_rate,
    write_output,
)

SCRIPT = "08_executive_summary"
TITLE = "Executive Summary of Key CHED Dashboard Indicators"

def compute():
    df = load_data()
    subsets = create_subsets(df)
    best = subsets["best"]               # person-level
    best_pre2015 = subsets["best_pre2015"]  # observable cohort

    lines = []
    lines.append("## Results\n")
    lines.append(
        "This executive summary provides a quick-reference overview of the key findings "
        "across all CHED dashboard analyses. "
        "**Important:** NMAT-to-PLE linkage rates measure the share of NMAT examinees later "
        "found in PLE passer records — NOT the PLE pass rate."
    )
    lines.append("")

    # ── Key Indicators ──────────────────────────────────────────────────
    total_best = len(best)
    yr_min = int(best["Year"].min())
    yr_max = int(best["Year"].max())
    med_raw = best["TotalRawScoreTRUE"].median()
    med_pctl = best["NMS_PER_num"].median()
    unique_examinees = best["PERSON_KEY"].nunique()

    # Repeat takers: persons with more than 1 attempt
    person_attempts = df.groupby("PERSON_KEY").size()
    repeat_takers = int((person_attempts > 1).sum())
    repeat_taker_rate = (repeat_takers / len(person_attempts)) * 100

    # Pre-2015 cohort
    obs_size = len(best_pre2015)
    ple_matched = int(best_pre2015["IS_PLE_PASSER"].sum())
    linkage_rate = (ple_matched / obs_size * 100) if obs_size > 0 else 0.0

    # ── Metric cards (2 rows of 4) ──────────────────────────────────────
    metric_cards = [
        ("Total Examinees (Best Record)", fmt(total_best)),
        ("Years Covered", f"{yr_min} -- {yr_max}"),
        ("Median Total Raw Score", f"{med_raw:.1f}"),
        ("Median Percentile", f"{med_pctl:.1f}"),
        ("Unique Examinees (PERSON_KEY)", fmt(unique_examinees)),
        ("Repeat Takers (>1 attempt)", f"{fmt(repeat_takers)} ({repeat_taker_rate:.1f}%)"),
        ("Observable Cohort (≤2014)", fmt(obs_size)),
        ("NMAT-to-PLE Linkage Rate (pre-2015)", f"{linkage_rate:.2f}%"),
    ]

    # Split into two rows of 4 for visual layout
    lines.append("### Key Indicators\n")
    lines.append("#### Row 1: Volume and Performance\n")
    lines.append(make_metric_table(metric_cards[:4]))
    lines.append("")
    lines.append("#### Row 2: Cohort and Linkage\n")
    lines.append(make_metric_table(metric_cards[4:]))
    lines.append("")

    # ── Pie chart data: UNI_TYPE composition ────────────────────────────
    lines.append("### UNI_TYPE Composition\n")
    lines.append(
        "Distribution of examinees by university type (best-record basis). "
        "This data can be used for a pie chart.\n"
    )

    uni_dist = best["UNI_TYPE"].value_counts()
    uni_header = "| UNI_TYPE | n (Best Record) | % of Total |"
    uni_sep = "|:---------|:---------------:|:----------:|"
    lines.append(uni_header)
    lines.append(uni_sep)
    for ut in UNI_TYPE_ORDER:
        n_ut = int(uni_dist.get(ut, 0))
        if n_ut > 0:
            lines.append(f"| {ut} | {n_ut:,} | {n_ut/total_best*100:.2f}% |")
    lines.append("")

    # ── Pie chart data: CourseGroup composition ─────────────────────────
    lines.append("### CourseGroup Composition\n")
    lines.append(
        "Distribution of examinees by course group (best-record basis). "
        "This data can be used for a pie chart.\n"
    )

    cg_dist = best["CourseGroup"].value_counts()
    cg_header = "| CourseGroup | n (Best Record) | % of Total |"
    cg_sep = "|:------------|:---------------:|:----------:|"
    lines.append(cg_header)
    lines.append(cg_sep)
    for cg in cg_dist.index:
        n_cg = int(cg_dist[cg])
        lines.append(f"| {cg} | {n_cg:,} | {n_cg/total_best*100:.2f}% |")
    lines.append("")

    # ── Summary table with all indicators ───────────────────────────────
    lines.append("### Comprehensive Indicator Table\n")
    lines.append(
        "All key figures in a single reference table.\n"
    )

    summary_header = "| Indicator | Value | Notes |"
    summary_sep = "|:----------|:-----:|:------|"
    lines.append(summary_header)
    lines.append(summary_sep)

    summary_rows = [
        ("Total NMAT Records (All Attempts)", fmt(len(df)), "Includes repeat takers"),
        ("Total Examinees (Best Record)", fmt(total_best), "One record per person"),
        ("Unique Persons (PERSON_KEY)", fmt(unique_examinees), "Deduplicated by PERSON_KEY"),
        ("Years Covered", f"{yr_min} -- {yr_max}", "NMAT data availability"),
        ("Median Total Raw Score", f"{med_raw:.1f}", "Best record basis"),
        ("Median Percentile", f"{med_pctl:.1f}", "Best record basis"),
        ("Repeat Takers (>1 attempt)", f"{fmt(repeat_takers)} ({repeat_taker_rate:.1f}%)",
         "Persons with multiple NMAT records"),
        ("Observable Cohort (Year <= 2014)", fmt(obs_size),
         "Best records with sufficient PLE observation window"),
        ("PLE Matched (Pre-2015)", fmt(ple_matched),
         "Pre-2015 examinees found in PLE passer records"),
        ("NMAT-to-PLE Linkage Rate (Pre-2015)", f"{linkage_rate:.2f}%",
         "NOT a PLE pass rate"),
        ("Female Examinees", fmt(int(best["SEX"].value_counts().get("Female", 0))),
         "Best record basis"),
        ("Male Examinees", fmt(int(best["SEX"].value_counts().get("Male", 0))),
         "Best record basis"),
        ("Foreign Examinees (Best Record)",
         fmt(int((best["FOREIGNER_STATUS"].isin(["Verified Foreigner", "Likely Foreigner"])).sum())),
         "Best record basis"),
        ("Filipino Examinees (Best Record)",
         fmt(int((best["FOREIGNER_STATUS"] == "Filipino").sum())),
         "Best record basis"),
    ]

    for indicator, value, notes in summary_rows:
        lines.append(f"| **{indicator}** | {value} | {notes} |")

    lines.append("")

    # ── Yearly snapshot ─────────────────────────────────────────────────
    lines.append("### Yearly Snapshot\n")
    lines.append("Per-year summary of key metrics (best-record basis).\n")

    yr_header2 = "| Year | n | Median Percentile | Median Raw Score | % Foreign |"
    yr_sep2 = "|:----:|:--:|:-----------------:|:----------------:|:---------:|"
    lines.append(yr_header2)
    lines.append(yr_sep2)

    for yr in sorted(best["Year"].unique()):
        y_sub = best[best["Year"] == yr]
        y_n = len(y_sub)
        y_med_pctl = y_sub["NMS_PER_num"].median()
        y_med_raw = y_sub["TotalRawScoreTRUE"].median()
        y_foreign = int((y_sub["FOREIGNER_STATUS"].isin(["Verified Foreigner", "Likely Foreigner"])).sum())
        y_pct_f = (y_foreign / y_n * 100) if y_n > 0 else 0
        lines.append(f"| {yr} | {y_n:,} | {y_med_pctl:.1f} | {y_med_raw:.1f} | {y_pct_f:.2f}% |")

    lines.append("")
    lines.append("*Year 2014 is the last year of the observable PLE cohort.*")
    lines.append("")

    # ── Key observations ────────────────────────────────────────────────
    lines.append("### Key Observations\n")
    lines.append("")
    lines.append(
        f"1. **Volume growth:** NMAT examinees grew from {int((best['Year']==yr_min).sum()):,} in {yr_min} "
        f"to {int((best['Year']==yr_max).sum()):,} in {yr_max}, a significant increase that "
        "has implications for medical school capacity."
    )
    lines.append("")
    lines.append(
        f"2. **PLE linkage:** The NMAT-to-PLE linkage rate for the pre-2015 cohort is "
        f"{linkage_rate:.1f}%, meaning {ple_matched:,} of {obs_size:,} examinees with "
        f"sufficient observation time were later found in PLE passer records."
    )
    lines.append("")
    lines.append(
        f"3. **Repeat takers:** {fmt(repeat_takers)} ({repeat_taker_rate:.1f}%) of "
        f"{fmt(len(person_attempts))} unique persons have taken the NMAT more than once, "
        "indicating significant retake behavior."
    )
    lines.append("")
    lines.append(
        "4. **Gender balance:** Female examinees constitute the majority of NMAT test-takers."
    )
    lines.append("")
    lines.append(
        "5. **Course dominance:** Medical & Allied and Natural Sciences account for the "
        "majority of examinees, reflecting the NMAT's focus on medical and science programs."
    )
    lines.append("")

    # Remove the caveat separator since write_output adds standard caveats
    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)

    # ── Console summary ─────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"  {TITLE}")
    print(f"{'='*70}")
    print(f"  Total examinees (best):        {total_best:>7,}")
    print(f"  Years:                         {yr_min} -- {yr_max}")
    print(f"  Median percentile:             {med_pctl:.1f}")
    print(f"  Median raw score:              {med_raw:.1f}")
    print(f"  Unique examinees:              {unique_examinees:>7,}")
    print(f"  Repeat takers:                 {repeat_takers:>7,} ({repeat_taker_rate:.1f}%)")
    print(f"  Pre-2015 cohort:               {obs_size:>7,}")
    print(f"  PLE linkage rate:              {linkage_rate:.2f}%")
    print(f"  Output: {path}")
    print(f"{'='*70}\n")

    return {
        "total_best": total_best,
        "unique_examinees": unique_examinees,
        "repeat_takers": repeat_takers,
        "repeat_taker_rate": repeat_taker_rate,
        "obs_size": obs_size,
        "ple_matched": ple_matched,
        "linkage_rate": linkage_rate,
    }

if __name__ == "__main__":
    compute()
