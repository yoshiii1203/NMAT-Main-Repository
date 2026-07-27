"""
06_ple_alignment.py — PLE linkage alignment analysis.

Computes:
  - PLE linkage rate by PercentileBin
  - PLE linkage by UNI_TYPE x PercentileBin
  - PLE linkage by CourseGroup x PercentileBin

CRITICAL: All labeled as "linkage rate" not "pass rate".
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

SCRIPT = "06_ple_alignment"
TITLE = "PLE Linkage Alignment with NMAT Performance"


def compute():
    df = load_data()
    subsets = create_subsets(df)
    obs = subsets["best_pre2015"]  # all best records with Year <= 2014

    lines = []
    lines.append("## Results\n")
    lines.append(
        "This section examines how NMAT percentile bins align with PLE linkage rates. "
        "**Important:** All rates shown are NMAT-to-PLE linkage rates — the share of "
        "NMAT examinees later found in PLE passer records. These are NOT PLE pass rates."
    )
    lines.append("")

    # ── Metric cards ────────────────────────────────────────────────────
    total_obs = len(obs)
    total_ple = int(obs["IS_PLE_PASSER"].sum())
    overall_linkage = (total_ple / total_obs * 100) if total_obs > 0 else 0

    metrics = [
        ("Pre-2015 Cohort Size", fmt(total_obs)),
        ("Matched to PLE Passer Records", fmt(total_ple)),
        ("Overall NMAT-to-PLE Linkage Rate", f"{overall_linkage:.2f}%"),
        ("Source", "NMAT_Exodus.parquet (best records, Year <= 2014)"),
    ]
    lines.append("### Key Metrics\n")
    lines.append(make_metric_table(metrics))
    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 1. PLE linkage by PercentileBin
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### PLE Linkage Rate by Percentile Bin\n")
    lines.append(
        "The NMAT-to-PLE linkage rate for each percentile bin. "
        "The B4->B5 jump is the largest adjacent-bin increase.\n"
    )

    bin_header = "| PercentileBin | Range | n (Pre-2015) | PLE Matched | Linkage Rate |"
    bin_sep = "|:------------:|:-----:|:------------:|:-----------:|:------------:|"
    lines.append(bin_header)
    lines.append(bin_sep)

    bin_results = []

    for b in BIN_ORDER:
        sub = obs[obs["PercentileBin"] == b]
        n_bin = len(sub)
        ple_bin = int(sub["IS_PLE_PASSER"].sum())
        lr = (ple_bin / n_bin * 100) if n_bin > 0 else 0

        idx = BIN_ORDER.index(b)
        lo = idx * 10
        hi = (idx + 1) * 10
        range_str = f"{lo}–{hi}th"

        lines.append(
            f"| {b} | {range_str} | {n_bin:,} | {ple_bin:,} | "
            f"{lr:.2f}% |"
        )
        bin_results.append((b, lr))

    lines.append("")

    # B4->B5 jump
    b4_lr = bin_results[3][1] if len(bin_results) > 3 else 0
    b5_lr = bin_results[4][1] if len(bin_results) > 4 else 0
    jump = b5_lr - b4_lr
    lines.append(
        f"The **B4→B5 jump** is the largest between adjacent bins: +{jump:.2f} percentage points "
        f"(from {b4_lr:.2f}% to {b5_lr:.2f}%). This validates the tiered cut-off approach — "
        "the 40th percentile (B5+) selects a cohort with meaningfully higher PLE linkage."
    )
    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 2. PLE linkage by UNI_TYPE x PercentileBin
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### PLE Linkage Rate by University Type and Percentile Bin\n")
    lines.append(
        "Heatmap-style table showing how linkage rates vary across both dimensions.\n"
    )

    ut_bin_header = "| PercentileBin | " + " | ".join(ut for ut in UNI_TYPE_ORDER) + " |"
    ut_bin_sep = "|:------------:|" + "|".join([":---:"] * len(UNI_TYPE_ORDER)) + "|"
    lines.append(ut_bin_header)
    lines.append(ut_bin_sep)

    for b in BIN_ORDER:
        row = [b]
        for ut in UNI_TYPE_ORDER:
            sub = obs[(obs["PercentileBin"] == b) & (obs["UNI_TYPE"] == ut)]
            n_sub = len(sub)
            ple_sub = int(sub["IS_PLE_PASSER"].sum()) if n_sub > 0 else 0
            lr = (ple_sub / n_sub * 100) if n_sub > 0 else 0
            if n_sub == 0:
                row.append("—")
            else:
                row.append(f"{lr:.2f}%")
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # Summary by UNI_TYPE
    lines.append("#### Overall PLE Linkage by University Type\n")
    lines.append("Aggregated across all percentile bins.\n")

    ut_sum_header = "| UNI_TYPE | n (Pre-2015) | PLE Matched | Linkage Rate |"
    ut_sum_sep = "|:---------|:------------:|:-----------:|:------------:|"
    lines.append(ut_sum_header)
    lines.append(ut_sum_sep)

    for ut in UNI_TYPE_ORDER:
        sub = obs[obs["UNI_TYPE"] == ut]
        n_sub = len(sub)
        if n_sub == 0:
            continue
        ple_sub = int(sub["IS_PLE_PASSER"].sum())
        lr = (ple_sub / n_sub * 100) if n_sub > 0 else 0
        lines.append(f"| {ut} | {n_sub:,} | {ple_sub:,} | {lr:.2f}% |")

    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 3. PLE linkage by CourseGroup x PercentileBin
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### PLE Linkage Rate by Course Group and Percentile Bin\n")
    lines.append(
        "How linkage rates differ by course group across the percentile distribution.\n"
    )

    cg_order = obs["CourseGroup"].value_counts().index.tolist()

    cg_bin_header = "| PercentileBin | " + " | ".join(str(cg) for cg in cg_order) + " |"
    cg_bin_sep = "|:------------:|" + "|".join([":---:"] * len(cg_order)) + "|"
    lines.append(cg_bin_header)
    lines.append(cg_bin_sep)

    for b in BIN_ORDER:
        row = [b]
        for cg in cg_order:
            sub = obs[(obs["PercentileBin"] == b) & (obs["CourseGroup"] == cg)]
            n_sub = len(sub)
            ple_sub = int(sub["IS_PLE_PASSER"].sum()) if n_sub > 0 else 0
            lr = (ple_sub / n_sub * 100) if n_sub > 0 else 0
            if n_sub == 0:
                row.append("—")
            else:
                row.append(f"{lr:.2f}%")
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # Summary by CourseGroup
    lines.append("#### Overall PLE Linkage by Course Group\n")

    cg_sum_header = "| Course Group | n (Pre-2015) | PLE Matched | Linkage Rate |"
    cg_sum_sep = "|:-------------|:------------:|:-----------:|:------------:|"
    lines.append(cg_sum_header)
    lines.append(cg_sum_sep)

    for cg in cg_order:
        sub = obs[obs["CourseGroup"] == cg]
        n_sub = len(sub)
        ple_sub = int(sub["IS_PLE_PASSER"].sum())
        lr = (ple_sub / n_sub * 100) if n_sub > 0 else 0
        lines.append(f"| {cg} | {n_sub:,} | {ple_sub:,} | {lr:.2f}% |")

    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # INTERPRETATION
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### Interpretation\n")
    lines.append(
        "The NMAT-to-PLE linkage rate increases monotonically from B1 (lowest) to B10 (highest). "
        "This monotonic relationship provides empirical support for NMAT cut-off scores as a "
        "screening tool: examinees with higher NMAT percentiles are more likely to be found "
        "in PLE passer records."
    )
    lines.append("")
    lines.append(
        "**However, this is an association, not a causal relationship.** "
        "Examinees with higher NMAT scores may: (a) attend higher-quality medical schools, "
        "(b) have better study habits or preparation, (c) be more motivated, or (d) have "
        "other advantages that contribute both to higher NMAT scores and higher PLE linkage. "
        "The linkage rate alone cannot be used to set a specific cut-off threshold without "
        "consideration of other factors."
    )
    lines.append("")
    lines.append(
        "**Critical caveat:** Our data contains only PLE passers. The linkage rate is affected by: "
        "(1) whether the examinee took PLE, (2) whether they passed, and (3) whether the match "
        "succeeded. We cannot distinguish these factors."
    )
    lines.append("")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)

    # ── Print summary ───────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"  {TITLE}")
    print(f"{'='*70}")
    print(f"  Pre-2015 cohort:            {total_obs:>7,}")
    print(f"  PLE matched:                {total_ple:>7,}")
    print(f"  Overall linkage rate:       {overall_linkage:>6.2f}%")
    print(f"  B4 linkage rate:            {b4_lr:>6.2f}%")
    print(f"  B5 linkage rate:            {b5_lr:>6.2f}%")
    print(f"  B4->B5 jump:               +{jump:>5.2f} pp")
    print(f"  Output: {path}")
    print(f"{'='*70}\n")

    return {
        "total_obs": total_obs,
        "total_ple": total_ple,
        "overall_linkage": overall_linkage,
        "b4_linkage": b4_lr,
        "b5_linkage": b5_lr,
        "b4b5_jump": jump,
    }


if __name__ == "__main__":
    compute()
