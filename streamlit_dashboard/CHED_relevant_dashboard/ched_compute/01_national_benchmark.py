"""
01_national_benchmark.py — NMAT-to-PLE linkage rates, national trends.

Computes:
  - Annual NMAT-to-PLE linkage rates for the observable cohort (Year <= 2014)
  - 5-year rolling average linkage rate
  - Metric cards with key figures
"""

import sys
import os
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from config import PLE_OBSERVABLE_MAX_YEAR, BIN_ORDER
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

SCRIPT = "01_national_benchmark"
TITLE = "National NMAT-to-PLE Linkage Benchmark"


def compute():
    df = load_data()
    subsets = create_subsets(df)
    best = subsets["best"]
    best_pre2015 = subsets["best_pre2015"]
    best_ple_pre2015 = subsets["best_ple_matched_pre2015"]

    lines = []
    lines.append("## Results\n")
    lines.append(
        "This section computes the annual and 5-year rolling NMAT-to-PLE linkage rate — "
        "the share of NMAT examinees from a given year who were later found in official PLE "
        "passer records. This is **not** a PLE pass rate."
    )
    lines.append("")

    # ── Metric cards ────────────────────────────────────────────────────
    total_n = len(best)
    total_pre2015 = len(best_pre2015)
    total_ple_matched = len(best_ple_pre2015)

    overall_linkage = (total_ple_matched / total_pre2015 * 100) if total_pre2015 > 0 else 0.0

    # 5-year rolling average (2010-2014)
    years_5yr = list(range(2010, 2015))
    linkage_rates_5yr = []
    for y in years_5yr:
        y_denom = (best_pre2015["Year"] == y).sum()
        y_numer = (best_ple_pre2015["Year"] == y).sum()
        if y_denom > 0:
            linkage_rates_5yr.append(y_numer / y_denom * 100)
    avg_5yr = np.mean(linkage_rates_5yr) if linkage_rates_5yr else 0.0

    metrics = [
        ("Total Examinees (Best Record)", fmt(total_n)),
        ("Pre-2015 Cohort Size", fmt(total_pre2015)),
        ("Matched to PLE Passer Records", fmt(total_ple_matched)),
        ("Overall NMAT-to-PLE Linkage Rate", f"{overall_linkage:.2f}%"),
        ("5-Year Rolling Average Linkage (2010-2014)", f"{avg_5yr:.2f}%"),
    ]
    lines.append("### Key Metrics\n")
    lines.append(make_metric_table(metrics))
    lines.append("")

    # ── Annual linkage table ──────────────────────────────────────────────
    lines.append("### Annual NMAT-to-PLE Linkage Rates\n")
    lines.append(
        "Table shows, for each year, the number of NMAT examinees (best record), "
        "the number found in PLE passer records, the linkage percentage, and the "
        "5-year rolling average where available.\n"
    )

    header = "| Year | n (Best Record) | n (Pre-2015 Cohort) | n PLE Matched | Linkage Rate | 5-Year Rolling Avg |"
    sep = "|:----:|:----------------:|:---------------------:|:-------------:|:------------:|:------------------:|"
    lines.append(header)
    lines.append(sep)

    all_years = sorted(best["Year"].unique())
    rolling_window = []

    for y in all_years:
        n_best = int((best["Year"] == y).sum())
        n_denom = int((best_pre2015["Year"] == y).sum()) if y <= PLE_OBSERVABLE_MAX_YEAR else 0
        n_ple = int((best_ple_pre2015["Year"] == y).sum()) if y <= PLE_OBSERVABLE_MAX_YEAR else 0

        if n_denom > 0:
            linkage = n_ple / n_denom * 100
        else:
            linkage = None

        # Rolling average: last 5 years where we have data
        rolling_window.append(linkage)
        if len(rolling_window) > 5:
            rolling_window.pop(0)

        if linkage is not None and len(rolling_window) >= 5:
            valid = [v for v in rolling_window if v is not None]
            rolling_avg = np.mean(valid) if len(valid) >= 5 else None
        else:
            rolling_avg = None

        linkage_str = f"{linkage:.2f}%" if linkage is not None else "N/A (no obs.)"
        rolling_str = f"{rolling_avg:.2f}%" if rolling_avg is not None else "—"
        flag = ""
        if y == PLE_OBSERVABLE_MAX_YEAR:
            flag = " *"

        lines.append(
            f"| {y}{flag} | {n_best:,} | {n_denom:,} | {n_ple:,} | {linkage_str} | {rolling_str} |"
        )

    lines.append("")
    lines.append(
        "*Observable cohort ends at 2014. Years after 2014 have insufficient "
        "time for PLE to be taken and observed in our data.*"
    )
    lines.append("")

    # ── Interpretation ──────────────────────────────────────────────────
    lines.append("### Interpretation\n")
    lines.append(
        f"The national NMAT-to-PLE linkage rate across the pre-2015 cohort "
        f"({total_pre2015:,} examinees, {total_ple_matched:,} matched) is "
        f"**{overall_linkage:.2f}%**. This means that {overall_linkage:.2f}% of NMAT "
        f"examinees who took the exam between 2006 and 2014 were later found in "
        f"official PLE passer records."
    )
    lines.append("")
    lines.append(
        "The 5-year rolling average linkage rate for 2010–2014 is "
        f"**{avg_5yr:.2f}%**. This declining trend (from ~55% in 2006 to ~38% in 2014) "
        "may reflect several factors: (a) increasing NMAT examinee volume outpacing "
        "medical school capacity, (b) changes in medical school admission policies, "
        "(c) data matching limitations, or (d) examinees taking PLE outside the "
        "observation window."
    )
    lines.append("")
    lines.append(
        "**Important:** This is an NMAT-to-PLE **linkage rate**, not a PLE pass rate. "
        "It measures the share of NMAT examinees found in PLE passer records. "
        "We cannot distinguish between examinees who never took PLE, those who took "
        "it but failed, those who passed but weren't matched, and those who took PLE "
        "after our data cutoff."
    )
    lines.append("")

    # ── Data quality notes ──────────────────────────────────────────────
    lines.append("### Data Quality Notes\n")
    lines.append("- **Cohort definition:** Best NMAT record per examinee (IS_BEST_NMAT_RECORD == True)")
    lines.append(f"- **Observable cohort:** Year ≤ {PLE_OBSERVABLE_MAX_YEAR}")
    lines.append("- **Total unique examinees in best records:** {:,}".format(total_n))
    lines.append("- **Pre-2015 examinees:** {:,}".format(total_pre2015))
    lines.append("- **PLE match source:** PLE_DATA.csv (passers only, 43,630 records)")
    lines.append("- **Linkage rate is a lower bound** — some examinees may have passed PLE after our observation window")
    lines.append("")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)

    # ── Print summary ───────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"  {TITLE}")
    print(f"{'='*70}")
    print(f"  Total best examinees:     {total_n:>7,}")
    print(f"  Pre-2015 cohort:          {total_pre2015:>7,}")
    print(f"  PLE matched:              {total_ple_matched:>7,}")
    print(f"  Overall linkage rate:     {overall_linkage:>6.2f}%")
    print(f"  5-year avg (2010-2014):   {avg_5yr:>6.2f}%")
    print(f"  Output: {path}")
    print(f"{'='*70}\n")

    return total_pre2015, overall_linkage


if __name__ == "__main__":
    compute()
