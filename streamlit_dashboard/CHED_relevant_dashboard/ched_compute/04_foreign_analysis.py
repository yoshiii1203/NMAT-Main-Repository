"""
04_foreign_analysis.py — Foreign examinee analysis.

Computes:
  - Foreign examinee counts by UNI_TYPE, Year, nationality
  - Foreign count per SUC per year
  - Nationality distribution (top 20)
  - NMAT performance by nationality (median percentile)

CRITICAL: All counts are labeled as "examinee counts" NOT "enrollment".
"""

import sys
import os
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from config import BIN_ORDER, UNI_TYPE_ORDER
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

SCRIPT = "04_foreign_analysis"
TITLE = "Foreign Examinee Analysis"


def compute():
    df = load_data()
    subsets = create_subsets(df)
    best = subsets["best"]

    lines = []
    lines.append("## Results\n")
    lines.append(
        "This section analyzes foreign NMAT examinees using CITIZENSHIP_FINAL and "
        "FOREIGNER_STATUS columns. "
        "**Important:** All figures represent NMAT examinee counts, not enrolled students. "
        "The 10-slot SUC cap applies to enrollment, which we cannot verify from this data."
    )
    lines.append("")

    # ── Identify foreign examinees ──────────────────────────────────────
    foreign_statuses = ["Verified Foreigner", "Likely Foreigner"]
    best["IS_FOREIGN"] = best["FOREIGNER_STATUS"].isin(foreign_statuses)

    foreign = best[best["IS_FOREIGN"]].copy()
    local = best[~best["IS_FOREIGN"]].copy()

    # ── Metric cards ────────────────────────────────────────────────────
    total_foreign = len(foreign)
    total_local = len(local)
    verified_foreign = int((best["FOREIGNER_STATUS"] == "Verified Foreigner").sum())
    likely_foreign = int((best["FOREIGNER_STATUS"] == "Likely Foreigner").sum())
    pct_foreign = (total_foreign / len(best) * 100)

    metrics = [
        ("Total Examinees (Best Record)", fmt(len(best))),
        ("Verified Foreigners", fmt(verified_foreign)),
        ("Likely Foreigners", fmt(likely_foreign)),
        ("Total Foreign Examinees", fmt(total_foreign)),
        ("Filipino Examinees", fmt(total_local)),
        ("Foreign as % of Total", f"{pct_foreign:.2f}%"),
    ]
    lines.append("### Key Metrics\n")
    lines.append(make_metric_table(metrics))
    lines.append("")

    # ── Foreign examinees by UNI_TYPE ───────────────────────────────────
    lines.append("### Foreign Examinees by University Type\n")
    lines.append("Distribution of foreign examinees across university types.\n")

    ut_header = "| UNI_TYPE | Foreign n | % of Foreign | % of UNI_TYPE Total |"
    ut_sep = "|:---------|:---------:|:------------:|:-------------------:|"
    lines.append(ut_header)
    lines.append(ut_sep)

    for ut in UNI_TYPE_ORDER:
        foreign_ut = int((foreign["UNI_TYPE"] == ut).sum())
        total_ut = int((best["UNI_TYPE"] == ut).sum())
        if foreign_ut == 0:
            continue
        lines.append(
            f"| {ut} | {foreign_ut:,} | {foreign_ut/total_foreign*100:.2f}% | "
            f"{foreign_ut/total_ut*100:.2f}% |"
        )

    lines.append("")

    # ── Foreign by Year ─────────────────────────────────────────────────
    lines.append("### Foreign Examinees by Year\n")
    lines.append("Yearly foreign examinee counts and trends.\n")

    yr_header = "| Year | Foreign n | % of Year Total | Total Examinees |"
    yr_sep = "|:----:|:---------:|:---------------:|:---------------:|"
    lines.append(yr_header)
    lines.append(yr_sep)

    for y in sorted(best["Year"].unique()):
        foreign_y = int((foreign["Year"] == y).sum())
        total_y = int((best["Year"] == y).sum())
        lines.append(
            f"| {y} | {foreign_y:,} | {foreign_y/total_y*100:.2f}% | {total_y:,} |"
        )

    lines.append("")

    # ── Foreign per SUC per year (for 10-slot cap analysis) ─────────────
    lines.append("### Foreign Examinee Counts per SUC per Year\n")
    lines.append(
        "This table shows foreign examinee counts at Public (SUC) institutions by year. "
        "**Note:** These are examinee counts, not enrollment. Actual enrollment figures "
        "may differ.\n"
    )

    suc_foreign = foreign[foreign["UNI_TYPE"] == "Public"]
    suc_years = sorted(suc_foreign["Year"].unique())
    suc_totals = suc_foreign.groupby("NMA_College").size().sort_values(ascending=False)

    suc_header = "| SUC | " + " | ".join(str(y) for y in suc_years) + " | Total |"
    suc_sep = "|------|" + "|".join([":---:"] * (len(suc_years) + 1)) + "|"
    lines.append(suc_header)
    lines.append(suc_sep)

    for suc in suc_totals.head(30).index:
        row_vals = []
        total_suc = 0
        for y in suc_years:
            mask = (suc_foreign["NMA_College"] == suc) & (suc_foreign["Year"] == y)
            cnt = int(mask.sum())
            row_vals.append(str(cnt))
            total_suc += cnt
        suc_name = suc if len(suc) <= 40 else suc[:37] + "..."
        lines.append(f"| {suc_name} | {' | '.join(row_vals)} | {total_suc:,} |")

    lines.append("")
    lines.append("*Only top 30 SUCs by total foreign examinees shown.*")
    lines.append("")

    # ── Nationality distribution (top 20) ───────────────────────────────
    lines.append("### Top 20 Nationalities Among Foreign Examinees\n")
    lines.append("Distribution of foreign examinees by citizenship.\n")

    nat_counts = foreign["CITIZENSHIP_FINAL"].value_counts().head(20)

    nat_header = "| Rank | Nationality | n | % of Foreign | Median Percentile |"
    nat_sep = "|:----:|:------------|:--:|:------------:|:-----------------:|"
    lines.append(nat_header)
    lines.append(nat_sep)

    for i, (nat, n) in enumerate(nat_counts.items(), 1):
        nat_median = foreign.loc[foreign["CITIZENSHIP_FINAL"] == nat, "NMS_PER_num"].median()
        med_str = f"{nat_median:.1f}" if not pd.isna(nat_median) else "N/A"
        lines.append(
            f"| {i} | {nat} | {n:,} | {n/total_foreign*100:.2f}% | {med_str} |"
        )

    lines.append("")

    # ── NMAT performance by nationality ─────────────────────────────────
    lines.append("### NMAT Performance by Nationality\n")
    lines.append(
        "Median NMAT percentile for top nationalities, showing score distribution.\n"
    )

    perf_header = "| Nationality | n | Median Pctl | Q1 Pctl | Q3 Pctl | % Below B4 (30th) |"
    perf_sep = "|:------------|:--:|:----------:|:-------:|:-------:|:-----------------:|"
    lines.append(perf_header)
    lines.append(perf_sep)

    for nat, n in nat_counts.items():
        sub = foreign[foreign["CITIZENSHIP_FINAL"] == nat]
        med = sub["NMS_PER_num"].median()
        q1 = sub["NMS_PER_num"].quantile(0.25)
        q3 = sub["NMS_PER_num"].quantile(0.75)
        below_b4 = int((
            sub["PercentileBin"].apply(
                lambda b: BIN_ORDER.index(b) < BIN_ORDER.index("B4") if b in BIN_ORDER else True
            )
        ).sum())
        pct_below = below_b4 / n * 100
        lines.append(
            f"| {nat} | {n:,} | {med:.1f} | {q1:.1f} | {q3:.1f} | {pct_below:.2f}% |"
        )

    lines.append("")

    # ── Foreign PLE linkage ─────────────────────────────────────────────
    lines.append("### Foreign Examinee PLE Linkage\n")
    lines.append(
        "NMAT-to-PLE linkage rates for foreign vs Filipino examinees (pre-2015 cohort).\n"
    )

    obs = subsets["best_pre2015"].copy()
    obs["IS_FOREIGN"] = obs["FOREIGNER_STATUS"].isin(foreign_statuses)

    ple_header = "| Group | n (Pre-2015) | PLE Matched | Linkage Rate |"
    ple_sep = "|:------|:------------:|:-----------:|:------------:|"
    lines.append(ple_header)
    lines.append(ple_sep)

    for grp_name, grp_mask in [("Filipino", False), ("Foreign", True)]:
        sub = obs[obs["IS_FOREIGN"] == grp_mask]
        n_obs = len(sub)
        n_ple = int(sub["IS_PLE_PASSER"].sum())
        lr = (n_ple / n_obs * 100) if n_obs > 0 else 0
        lines.append(f"| {grp_name} | {n_obs:,} | {n_ple:,} | {lr:.2f}% |")

    lines.append("")

    # ── Interpretation ──────────────────────────────────────────────────
    lines.append("### Interpretation\n")
    india_count = int(nat_counts.get("India", 0))
    lines.append(
        f"Of {len(best):,} NMAT examinees, {total_foreign:,} ({pct_foreign:.1f}%) "
        "are foreign nationals based on CITIZENSHIP_FINAL. "
        f"The largest group is from India ({india_count:,}, "
        f"{india_count/total_foreign*100:.1f}% of foreign examinees)."
    )
    lines.append("")

    india_sub = foreign[foreign["CITIZENSHIP_FINAL"] == "India"]
    india_median = india_sub["NMS_PER_num"].median()
    india_below_b4 = int((
        india_sub["PercentileBin"].apply(
            lambda b: BIN_ORDER.index(b) < BIN_ORDER.index("B4") if b in BIN_ORDER else True
        )
    ).sum())
    india_pct_below = india_below_b4 / len(india_sub) * 100 if len(india_sub) > 0 else 0

    lines.append(
        f"Indian-origin examinees have a median percentile of {india_median:.1f} (B2 range), "
        f"and {india_pct_below:.1f}% fall below the 30th percentile threshold (B4). "
        "This has significant implications for the proposed 30th/40th cut-off policy."
    )
    lines.append("")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)

    # ── Print summary ───────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"  {TITLE}")
    print(f"{'='*70}")
    print(f"  Total foreign examinees:         {total_foreign:>7,}")
    print(f"  Verified Foreigners:             {verified_foreign:>7,}")
    print(f"  Likely Foreigners:               {likely_foreign:>7,}")
    print(f"  Filipino examinees:              {total_local:>7,}")
    print(f"  Top nationality:                 India ({india_count:,})")
    print(f"  Top nationality median pctl:     {india_median:.1f}")
    print(f"  Output: {path}")
    print(f"{'='*70}\n")

    return {
        "total_foreign": total_foreign,
        "verified_foreign": verified_foreign,
        "likely_foreign": likely_foreign,
    }


if __name__ == "__main__":
    compute()
