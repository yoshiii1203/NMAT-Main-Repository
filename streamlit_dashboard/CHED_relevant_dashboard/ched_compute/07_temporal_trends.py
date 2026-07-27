"""
07_temporal_trends.py — Temporal trend analysis (2006-2018).

Computes:
  - Yearly median scores, IQR, examinee counts
  - Yearly bin distribution
  - Yearly foreign examinee counts
"""

import sys
import os
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from config import BIN_ORDER
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

SCRIPT = "07_temporal_trends"
TITLE = "Temporal Trends in NMAT Performance (2006–2018)"


def compute():
    df = load_data()
    subsets = create_subsets(df)
    best = subsets["best"]

    lines = []
    lines.append("## Results\n")
    lines.append(
        "This section analyzes year-over-year trends in NMAT examinee volume, "
        "score distribution, and composition across the 13 years of data (2006–2018)."
    )
    lines.append("")

    all_years = sorted(best["Year"].unique())

    # ── Metric cards ────────────────────────────────────────────────────
    first_year = all_years[0]
    last_year = all_years[-1]
    first_n = int((best["Year"] == first_year).sum())
    last_n = int((best["Year"] == last_year).sum())
    growth = ((last_n - first_n) / first_n * 100) if first_n > 0 else 0
    total_best = len(best)

    metrics = [
        ("Data Range", f"{first_year}–{last_year} ({len(all_years)} years)"),
        ("Total Examinees (Best Record)", fmt(total_best)),
        (f"Examinees in {first_year} (first year)", fmt(first_n)),
        (f"Examinees in {last_year} (last year)", fmt(last_n)),
        ("Volume Growth", f"+{growth:.0f}%"),
    ]
    lines.append("### Key Metrics\n")
    lines.append(make_metric_table(metrics))
    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 1. Yearly summary statistics
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### Yearly NMAT Score Summary\n")
    lines.append(
        "Median, Q1, Q3 of NMS_PER_num (percentile) and TotalRawScoreTRUE by year.\n"
    )

    yr_header = "| Year | n | Median Pctl | Q1 Pctl | Q3 Pctl | IQR | Median Raw | Q1 Raw | Q3 Raw |"
    yr_sep = "|:----:|:-:|:----------:|:-------:|:-------:|:---:|:----------:|:------:|:------:|"
    lines.append(yr_header)
    lines.append(yr_sep)

    yearly_stats = []
    for y in all_years:
        sub = best[best["Year"] == y]
        n = len(sub)
        med_p = sub["NMS_PER_num"].median()
        q1_p = sub["NMS_PER_num"].quantile(0.25)
        q3_p = sub["NMS_PER_num"].quantile(0.75)
        med_r = sub["TotalRawScoreTRUE"].median()
        q1_r = sub["TotalRawScoreTRUE"].quantile(0.25)
        q3_r = sub["TotalRawScoreTRUE"].quantile(0.75)
        iqr = q3_p - q1_p

        lines.append(
            f"| {y} | {n:,} | {med_p:.1f} | {q1_p:.1f} | {q3_p:.1f} | {iqr:.1f} | "
            f"{med_r:.0f} | {q1_r:.0f} | {q3_r:.0f} |"
        )
        yearly_stats.append({
            "year": y,
            "n": n,
            "median_pctl": med_p,
            "q1_pctl": q1_p,
            "q3_pctl": q3_p,
            "median_raw": med_r,
        })

    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 2. Yearly bin distribution
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### Yearly Percentile Bin Distribution\n")
    lines.append("Number of examinees in each percentile bin, by year.\n")

    bin_yr_header = "| Year | " + " | ".join(BIN_ORDER) + " | Total |"
    bin_yr_sep = "|:----:|" + "|".join([":---:"] * len(BIN_ORDER)) + "|:----:|"
    lines.append(bin_yr_header)
    lines.append(bin_yr_sep)

    for y in all_years:
        sub = best[best["Year"] == y]
        row = [str(y)]
        bin_sum = 0
        for b in BIN_ORDER:
            cnt = int((sub["PercentileBin"] == b).sum())
            row.append(str(cnt))
            bin_sum += cnt
        row.append(str(bin_sum))
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # Yearly bin distribution as percentages
    lines.append("#### Yearly Percentile Bin Distribution (%)\n")
    lines.append("Percentage of each year's examinees in each percentile bin.\n")

    pct_header = "| Year | " + " | ".join(BIN_ORDER) + " |"
    pct_sep = "|:----:|" + "|".join([":---:"] * len(BIN_ORDER)) + "|"
    lines.append(pct_header)
    lines.append(pct_sep)

    for y in all_years:
        sub = best[best["Year"] == y]
        n = len(sub)
        row = [str(y)]
        for b in BIN_ORDER:
            pct_val = (sub["PercentileBin"] == b).sum() / n * 100
            row.append(f"{pct_val:.1f}%")
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 3. Yearly foreign examinee counts
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### Yearly Foreign Examinee Counts\n")
    lines.append(
        "Foreign examinee counts and percentage of total by year.\n"
    )

    foreign_statuses = ["Verified Foreigner", "Likely Foreigner"]
    best["IS_FOREIGN"] = best["FOREIGNER_STATUS"].isin(foreign_statuses)

    fgn_header = "| Year | Total | Foreign n | % Foreign | Filipino n | % Filipino |"
    fgn_sep = "|:----:|:----:|:---------:|:---------:|:----------:|:----------:|"
    lines.append(fgn_header)
    lines.append(fgn_sep)

    for y in all_years:
        sub = best[best["Year"] == y]
        n = len(sub)
        fgn = int(sub["IS_FOREIGN"].sum())
        fil = n - fgn
        lines.append(
            f"| {y} | {n:,} | {fgn:,} | {fgn/n*100:.1f}% | "
            f"{fil:,} | {fil/n*100:.1f}% |"
        )

    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 4. Yearly PLE linkage trends
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### Yearly PLE Linkage Trend\n")
    lines.append(
        "NMAT-to-PLE linkage rates by year for the observable cohort (Year <= 2014). "
        "After 2014, PLE linkage is incomplete as examinees may not have had time to take PLE.\n"
    )

    obs = subsets["best_pre2015"]

    ple_yr_header = "| Year | n (Obs) | PLE Matched | Linkage Rate |"
    ple_yr_sep = "|:----:|:-------:|:-----------:|:------------:|"
    lines.append(ple_yr_header)
    lines.append(ple_yr_sep)

    for y in sorted(obs["Year"].unique()):
        sub = obs[obs["Year"] == y]
        n_sub = len(sub)
        ple_sub = int(sub["IS_PLE_PASSER"].sum())
        lr = (ple_sub / n_sub * 100) if n_sub > 0 else 0
        lines.append(f"| {y} | {n_sub:,} | {int(ple_sub):,} | {lr:.2f}% |")

    lines.append("")
    lines.append(
        "*Note: PLE linkage declines over time. This may reflect: (a) increasing "
        "NMAT examinee volume without proportional increase in medical school capacity, "
        "(b) changes in admission policies, or (c) data matching limitations.*"
    )
    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # INTERPRETATION
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### Interpretation\n")
    lines.append(
        "NMAT examinee volume has grown substantially over the 13-year period, "
        f"from {first_n:,} in {first_year} to {last_n:,} in {last_year} "
        f"(+{growth:.0f}% increase)."
    )
    lines.append("")

    # Overall trend in median scores
    first_med = yearly_stats[0]["median_pctl"]
    last_med = yearly_stats[-1]["median_pctl"]
    lines.append(
        f"The median NMAT percentile has {'increased' if last_med > first_med else 'decreased'} "
        f"from {first_med:.1f} in {first_year} to {last_med:.1f} in {last_year}."
    )
    lines.append("")

    # Foreign trend
    first_fgn_pct = best[best["Year"] == first_year]["IS_FOREIGN"].mean() * 100
    last_fgn_pct = best[best["Year"] == last_year]["IS_FOREIGN"].mean() * 100
    lines.append(
        f"Foreign examinees as a share of total have "
        f"{'increased' if last_fgn_pct > first_fgn_pct else 'decreased'} "
        f"from {first_fgn_pct:.1f}% in {first_year} to {last_fgn_pct:.1f}% in {last_year}."
    )
    lines.append("")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)

    # ── Print summary ───────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"  {TITLE}")
    print(f"{'='*70}")
    print(f"  Year range:                 {first_year}–{last_year}")
    print(f"  First year n:               {first_n:,}")
    print(f"  Last year n:                {last_n:,}")
    print(f"  Growth:                     +{growth:.0f}%")
    print(f"  Median pctl {first_year}:   {first_med:.1f}")
    print(f"  Median pctl {last_year}:    {last_med:.1f}")
    print(f"  Foreign % {first_year}:     {first_fgn_pct:.1f}%")
    print(f"  Foreign % {last_year}:      {last_fgn_pct:.1f}%")
    print(f"  Output: {path}")
    print(f"{'='*70}\n")

    return {
        "first_year": first_year,
        "last_year": last_year,
        "growth_pct": growth,
    }


if __name__ == "__main__":
    compute()
