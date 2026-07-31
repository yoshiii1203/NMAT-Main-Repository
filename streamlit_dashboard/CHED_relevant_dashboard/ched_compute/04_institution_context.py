"""
04_foreign_analysis.py — Foreign examinee analysis.

Computes:
  - Foreign examinee counts by UNDERGRAD_UNI_TYPE, Year, nationality
  - Foreign count per SUC per year
  - Nationality distribution (top 20)
  - NMAT performance by nationality (median score)

CRITICAL: All counts are labeled as "examinee counts" NOT "enrollment".
Every foreign count specifies best-record vs all-records denominator.
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

SCRIPT = "04_institution_context"
TITLE = "Foreign Examinee Analysis"

def compute():
    df = load_data()
    subsets = create_subsets(df)
    best = subsets["best"]       # person-level (one record per examinee)
    full = subsets["full"]        # all records (includes repeat takers)

    lines = []
    lines.append("## Results\n")
    lines.append(
        "This section analyzes foreign NMAT examinees using CITIZENSHIP_FINAL and "
        "FOREIGNER_STATUS columns. "
        "**Important:** All figures represent NMAT examinee counts, not enrolled students. "
        "The 10-slot SUC cap applies to enrollment, which we cannot verify from this data."
    )
    lines.append("")

    # ── All-records context ──────────────────────────────────────────────
    lines.append("### Foreign Counts: Best-Record vs All-Records\n")
    lines.append(
        "Two perspectives are provided: **best-record** (one record per examinee, primary) and "
        "**all-records** (includes repeat takers, for volume context). "
        "Always check which denominator is used.\n"
    )

    foreign_statuses = ["Verified Foreigner", "Likely Foreigner"]
    best["IS_FOREIGN"] = best["FOREIGNER_STATUS"].isin(foreign_statuses)
    full["IS_FOREIGN"] = full["FOREIGNER_STATUS"].isin(foreign_statuses)

    foreign = best[best["IS_FOREIGN"]].copy()
    local = best[~best["IS_FOREIGN"]].copy()

    # All-records foreign count
    full_foreign = full[full["IS_FOREIGN"]].copy()
    full_foreign_count = len(full_foreign)

    # Best-record metrics
    total_foreign = len(foreign)
    total_local = len(local)
    verified_foreign = int((best["FOREIGNER_STATUS"] == "Verified Foreigner").sum())
    likely_foreign = int((best["FOREIGNER_STATUS"] == "Likely Foreigner").sum())
    pct_foreign = (total_foreign / len(best) * 100)
    pct_foreign_full = (full_foreign_count / len(full) * 100)

    # ── Metric cards ────────────────────────────────────────────────────
    metrics = [
        ("Total Examinees (Best Record)", fmt(len(best))),
        ("Total Records (All Attempts)", fmt(len(full))),
        ("", ""),
        ("Foreign Examinees (Best Record) — PRIMARY", fmt(total_foreign)),
        ("Foreign Records (All Attempts, includes repeat takers)", fmt(full_foreign_count)),
        ("", ""),
        ("Verified Foreigners (Best Record)", fmt(verified_foreign)),
        ("Likely Foreigners (Best Record)", fmt(likely_foreign)),
        ("Filipino Examinees (Best Record)", fmt(total_local)),
        ("Foreign as % of Total (Best Record)", f"{pct_foreign:.2f}%"),
        ("Foreign as % of Total (All Records)", f"{pct_foreign_full:.2f}%"),
    ]
    lines.append("### Summary Metrics\n")
    lines.append(make_metric_table(metrics))
    lines.append("")

    # ── By UNDERGRAD_UNI_TYPE ─────────────────────────────────────────────────────
    lines.append("### Foreign Examinees by University Type\n")
    lines.append(
        "Distribution of foreign examinees across university types "
        "(best-record basis).\n"
    )

    ut_header = "| UNDERGRAD_UNI_TYPE | Foreign n (Best Record) | % of Foreign | % of UNDERGRAD_UNI_TYPE Total |"
    ut_sep = "|:---------|:-----------------------:|:------------:|:-------------------:|"
    lines.append(ut_header)
    lines.append(ut_sep)

    for ut in UNI_TYPE_ORDER:
        foreign_ut = int((foreign["UNDERGRAD_UNI_TYPE"] == ut).sum())
        total_ut = int((best["UNDERGRAD_UNI_TYPE"] == ut).sum())
        if foreign_ut == 0:
            continue
        lines.append(
            f"| {ut} | {foreign_ut:,} | {foreign_ut/total_foreign*100:.2f}% | "
            f"{foreign_ut/total_ut*100:.2f}% |"
        )

    lines.append("")

    # ── By Year ─────────────────────────────────────────────────────────
    lines.append("### Foreign Examinees by Year\n")
    lines.append("Yearly foreign examinee counts and trends (best-record basis).\n")

    yr_header = "| Year | Foreign n (Best Record) | % of Year Total | Total Examinees |"
    yr_sep = "|:----:|:-----------------------:|:---------------:|:---------------:|"
    lines.append(yr_header)
    lines.append(yr_sep)

    for y in sorted(best["Year"].unique()):
        foreign_y = int((foreign["Year"] == y).sum())
        total_y = int((best["Year"] == y).sum())
        lines.append(
            f"| {y} | {foreign_y:,} | {foreign_y/total_y*100:.2f}% | {total_y:,} |"
        )

    lines.append("")

    # ── Per SUC per year ────────────────────────────────────────────────
    lines.append("### Foreign Examinees at SUCs (by Year)\n")
    lines.append(
        "This table shows foreign examinee counts at Public (SUC) institutions by year. "
        "**Note:** These are examinee counts (best-record), not enrollment. Actual enrollment figures "
        "may differ.\n"
    )

    suc_foreign = foreign[foreign["UNDERGRAD_UNI_TYPE"] == "Public"]
    suc_years = sorted(suc_foreign["Year"].unique())
    suc_totals = suc_foreign.groupby("UNDERGRAD_UNIVERSITY").size().sort_values(ascending=False)

    suc_header = "| SUC | " + " | ".join(str(y) for y in suc_years) + " | Total |"
    suc_sep = "|------|" + "|".join([":---:"] * (len(suc_years) + 1)) + "|"
    lines.append(suc_header)
    lines.append(suc_sep)

    for suc in suc_totals.head(30).index:
        row_vals = []
        total_suc = 0
        for y in suc_years:
            mask = (suc_foreign["UNDERGRAD_UNIVERSITY"] == suc) & (suc_foreign["Year"] == y)
            cnt = int(mask.sum())
            row_vals.append(str(cnt))
            total_suc += cnt
        suc_name = suc if len(suc) <= 40 else suc[:37] + "..."
        lines.append(f"| {suc_name} | {' | '.join(row_vals)} | {total_suc:,} |")

    lines.append("")
    lines.append("*Only top 30 SUCs by total foreign examinees shown.*")
    lines.append("")

    # ── Nationality distribution ────────────────────────────────────────
    lines.append("### Foreign Examinees by Nationality\n")
    lines.append("Distribution of foreign examinees by citizenship (all-records basis, includes repeat takers).\n")

    nat_counts = full_foreign["CITIZENSHIP_FINAL"].value_counts().head(20)

    nat_header = "| Rank | Nationality | n (All Records) | % of Foreign | Median |"
    nat_sep = "|:----:|:------------|:---------------:|:------------:|:-----------------:|"
    lines.append(nat_header)
    lines.append(nat_sep)

    for i, (nat, n) in enumerate(nat_counts.items(), 1):
        nat_median = full_foreign.loc[full_foreign["CITIZENSHIP_FINAL"] == nat, "NMS_PER_num"].median()
        med_str = f"{nat_median:.1f}" if not pd.isna(nat_median) else "N/A"
        lines.append(
            f"| {i} | {nat} | {n:,} | {n/total_foreign*100:.2f}% | {med_str} |"
        )

    lines.append("")

    # ── Performance by nationality ──────────────────────────────────────
    lines.append("### NMAT Performance by Nationality\n")
    lines.append(
        "Median NMAT score for top nationalities, showing score distribution "
        "(all-records basis).\n"
    )

    perf_header = "| Nationality | n (All Records) | Median | Q1 | Q3 | % Below B4+ |"
    perf_sep = "|:------------|:---------------:|:----------:|:-------:|:-------:|:-----------------:|"
    lines.append(perf_header)
    lines.append(perf_sep)

    for nat, n in nat_counts.items():
        sub = full_foreign[full_foreign["CITIZENSHIP_FINAL"] == nat]
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

    # ── Foreign vs Filipino PLE linkage ─────────────────────────────────
    lines.append("### Foreign vs Filipino: NMAT-to-PLE Linkage\n")
    lines.append(
        "NMAT-to-PLE linkage rates for foreign vs Filipino examinees (pre-2015 cohort, "
        "best-record basis).\n"
    )

    obs = subsets["best_pre2015"].copy()
    obs["IS_FOREIGN"] = obs["FOREIGNER_STATUS"].isin(foreign_statuses)

    ple_header = "| Group | n (Pre-2015, Best Record) | PLE Matched | NMAT-to-PLE Linkage Rate |"
    ple_sep = "|:------|:------------------------:|:-----------:|:------------------------:|"
    lines.append(ple_header)
    lines.append(ple_sep)

    for grp_name, grp_mask in [("Filipino", False), ("Foreign", True)]:
        sub = obs[obs["IS_FOREIGN"] == grp_mask]
        n_obs = len(sub)
        n_ple = int(sub["IS_PLE_PASSER"].sum())
        lr = (n_ple / n_obs * 100) if n_obs > 0 else 0
        lines.append(f"| {grp_name} | {n_obs:,} | {n_ple:,} | {lr:.2f}% |")

    lines.append("")

    # ── Key insight ─────────────────────────────────────────────────────
    lines.append("### Key Insight\n")
    india_count = int(nat_counts.get("India", 0))
    lines.append(
        f"Of {len(best):,} NMAT examinees (best-record), {total_foreign:,} ({pct_foreign:.1f}%) "
        "are foreign nationals based on CITIZENSHIP_FINAL. "
        f"Across all records (including repeat takers), there are {full_foreign_count:,} "
        "foreign test records."
    )
    lines.append("")
    lines.append(
        f"The largest nationality group is from India ({india_count:,}, "
        f"{india_count/total_foreign*100:.1f}% of foreign examinees, best-record basis)."
    )
    lines.append("")

    india_sub = full_foreign[full_foreign["CITIZENSHIP_FINAL"] == "India"]
    india_median = india_sub["NMS_PER_num"].median()
    india_below_b4 = int((
        india_sub["PercentileBin"].apply(
            lambda b: BIN_ORDER.index(b) < BIN_ORDER.index("B4") if b in BIN_ORDER else True
        )
    ).sum())
    india_pct_below = india_below_b4 / len(india_sub) * 100 if len(india_sub) > 0 else 0

    lines.append(
        f"Indian-origin examinees have a median score of {india_median:.1f} (B2 range), "
        f"and {india_pct_below:.1f}% fall below the B4+ threshold. "
        "This has significant implications for the proposed B4+/B5+ cut-off policy."
    )
    lines.append("")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)

    # ── Console summary ─────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"  {TITLE}")
    print(f"{'='*70}")
    print(f"  Total foreign examinees (best-record):  {total_foreign:>7,}")
    print(f"  Total foreign records (all attempts):   {full_foreign_count:>7,}")
    print(f"  Verified Foreigners (best-record):       {verified_foreign:>7,}")
    print(f"  Likely Foreigners (best-record):         {likely_foreign:>7,}")
    print(f"  Filipino examinees (best-record):        {total_local:>7,}")
    print(f"  Top nationality:                         India ({india_count:,})")
    print(f"  Top nationality median score:            {india_median:.1f}")
    print(f"  Output: {path}")
    print(f"{'='*70}\n")

    return {
        "total_foreign": total_foreign,
        "full_foreign_count": full_foreign_count,
        "verified_foreign": verified_foreign,
        "likely_foreign": likely_foreign,
    }

if __name__ == "__main__":
    compute()
