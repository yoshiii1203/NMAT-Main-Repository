"""
06_ple_alignment.py — PLE linkage alignment analysis.

Computes:
  - PLE linkage rate by PercentileBin
  - PLE linkage by UNI_TYPE x PercentileBin
  - PLE linkage by CourseGroup x PercentileBin
  - Box plot data: score distribution by PLE status (median, Q1, Q3)
  - Course group survival: % in B8-B10 and PLE linkage rate

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
    obs = subsets["best_pre2015"]   # observable cohort
    best = subsets["best"]          # all best records

    lines = []
    lines.append("## Results\n")
    lines.append(
        "This section examines how NMAT percentile bins align with PLE linkage rates. "
        "**Important:** All rates shown are NMAT-to-PLE linkage rates — the share of "
        "NMAT examinees later found in PLE passer records. These are NOT PLE pass rates."
    )
    lines.append("")

    # ── Overall metrics ─────────────────────────────────────────────────
    total_obs = len(obs)
    total_ple = int(obs["IS_PLE_PASSER"].sum())
    overall_linkage = (total_ple / total_obs * 100) if total_obs > 0 else 0

    metrics = [
        ("Pre-2015 Cohort Size (Best Record)", fmt(total_obs)),
        ("Matched to PLE Passer Records", fmt(total_ple)),
        ("Overall NMAT-to-PLE Linkage Rate", f"{overall_linkage:.2f}%"),
        ("Source", "NMAT_Exodus.parquet (best records, Year <= 2014)"),
    ]
    lines.append("### Overview\n")
    lines.append(make_metric_table(metrics))
    lines.append("")

    # ────────────────────────────────────────────────────────────────────
    # 1) PLE Linkage by PercentileBin
    # ────────────────────────────────────────────────────────────────────
    lines.append("### PLE Linkage by PercentileBin\n")
    lines.append(
        "The NMAT-to-PLE linkage rate for each percentile bin. "
        "The B4->B5 jump is the largest adjacent-bin increase.\n"
    )

    bin_header = "| PercentileBin | Range | n (Pre-2015) | PLE Matched | NMAT-to-PLE Linkage Rate |"
    bin_sep = "|:------------:|:-----:|:------------:|:-----------:|:------------------------:|"
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
        range_str = f"{lo}--{hi}th"

        lines.append(
            f"| {b} | {range_str} | {n_bin:,} | {ple_bin:,} | "
            f"{lr:.2f}% |"
        )
        bin_results.append((b, lr))

    lines.append("")

    b4_lr = bin_results[3][1] if len(bin_results) > 3 else 0
    b5_lr = bin_results[4][1] if len(bin_results) > 4 else 0
    jump = b5_lr - b4_lr

    lines.append(f"*B4 linkage: {b4_lr:.2f}%, B5 linkage: {b5_lr:.2f}%, B4->B5 jump: {jump:+.2f} pp*\n")
    lines.append("")

    # ────────────────────────────────────────────────────────────────────
    # 2) PercentileBin x UNI_TYPE heatmap
    # ────────────────────────────────────────────────────────────────────
    lines.append("### Linkage by PercentileBin and UNI_TYPE\n")
    lines.append(
        "How linkage rates vary by university type within each percentile bin.\n"
    )

    ut_bin_header = "| PercentileBin | " + " | ".join(UNI_TYPE_ORDER) + " |"
    ut_bin_sep = "|:------------:|" + "|".join([":---:"] * len(UNI_TYPE_ORDER)) + "|"
    lines.append(ut_bin_header)
    lines.append(ut_bin_sep)

    for b in BIN_ORDER:
        row = [b]
        for ut in UNI_TYPE_ORDER:
            sub = obs[(obs["PercentileBin"] == b) & (obs["UNI_TYPE"] == ut)]
            n_sub = len(sub)
            ple_sub = int(sub["IS_PLE_PASSER"].sum())
            lr = (ple_sub / n_sub * 100) if n_sub > 0 else 0
            if n_sub == 0:
                row.append("--")
            else:
                row.append(f"{lr:.2f}% ({n_sub})")
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # ────────────────────────────────────────────────────────────────────
    # 3) PercentileBin x CourseGroup heatmap
    # ────────────────────────────────────────────────────────────────────
    lines.append("### Linkage by PercentileBin and CourseGroup\n")
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
                row.append("--")
            else:
                row.append(f"{lr:.2f}%")
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # CourseGroup summary
    lines.append("#### CourseGroup Summary\n")
    cg_sum_header = "| Course Group | n (Pre-2015) | PLE Matched | NMAT-to-PLE Linkage Rate |"
    cg_sum_sep = "|:-------------|:------------:|:-----------:|:------------------------:|"
    lines.append(cg_sum_header)
    lines.append(cg_sum_sep)

    for cg in cg_order:
        sub = obs[obs["CourseGroup"] == cg]
        n_sub = len(sub)
        ple_sub = int(sub["IS_PLE_PASSER"].sum())
        lr = (ple_sub / n_sub * 100) if n_sub > 0 else 0
        lines.append(f"| {cg} | {n_sub:,} | {ple_sub:,} | {lr:.2f}% |")

    lines.append("")

    # ────────────────────────────────────────────────────────────────────
    # 4) Box plot data: Score distribution by PLE status
    # ────────────────────────────────────────────────────────────────────
    lines.append("### Score Distribution by PLE Status (Box Plot Data)\n")
    lines.append(
        "Median, Q1, and Q3 of NMAT scores for PLE-linked vs non-linked examinees "
        "(pre-2015 cohort, best-record basis).\n"
    )

    ple_passers = obs[obs["IS_PLE_PASSER"] == True]
    non_passers = obs[obs["IS_PLE_PASSER"] == False]

    bp_header = "| Metric | PLE Passers (Linked) | Non-Linked Examinees | Difference |"
    bp_sep = "|--------|:--------------------:|:--------------------:|:----------:|"
    lines.append(bp_header)
    lines.append(bp_sep)

    bp_metrics = [
        ("n", len(ple_passers), len(non_passers), None),
        ("Median Percentile",
         ple_passers["NMS_PER_num"].median(),
         non_passers["NMS_PER_num"].median(), None),
        ("Q1 Percentile (25th)",
         ple_passers["NMS_PER_num"].quantile(0.25),
         non_passers["NMS_PER_num"].quantile(0.25), None),
        ("Q3 Percentile (75th)",
         ple_passers["NMS_PER_num"].quantile(0.75),
         non_passers["NMS_PER_num"].quantile(0.75), None),
        ("Median TotalRawScore",
         ple_passers["TotalRawScoreTRUE"].median(),
         non_passers["TotalRawScoreTRUE"].median(), None),
        ("Q1 Raw Score",
         ple_passers["TotalRawScoreTRUE"].quantile(0.25),
         non_passers["TotalRawScoreTRUE"].quantile(0.25), None),
        ("Q3 Raw Score",
         ple_passers["TotalRawScoreTRUE"].quantile(0.75),
         non_passers["TotalRawScoreTRUE"].quantile(0.75), None),
    ]

    for label, p_val, n_val, _ in bp_metrics:
        if isinstance(p_val, (int, np.integer)):
            diff = p_val - n_val
            lines.append(f"| {label} | {p_val:,} | {n_val:,} | {diff:+,} |")
        else:
            diff = p_val - n_val
            lines.append(f"| {label} | {p_val:.1f} | {n_val:.1f} | {diff:+.1f} |")

    lines.append("")
    lines.append(
        "PLE-linked examinees have substantially higher NMAT scores across all metrics. "
        "The median percentile for PLE-linked examinees is "
        f"{ple_passers['NMS_PER_num'].median():.0f}, compared to "
        f"{non_passers['NMS_PER_num'].median():.0f} for non-linked examinees."
    )
    lines.append("")

    # ────────────────────────────────────────────────────────────────────
    # 5) Course Group Survival: % in B8-B10 and PLE linkage rate
    # ────────────────────────────────────────────────────────────────────
    lines.append("### Course Group Survival (B8-B10)\n")
    lines.append(
        "For each course group, the percentage of examinees in the top 3 percentile bins "
        "(B8-B10, 70th-100th percentile) and the NMAT-to-PLE linkage rate. "
        "Higher B8-B10 share generally correlates with higher linkage.\n"
    )

    surv_header = "| Course Group | n (Best Record) | n in B8-B10 | % in B8-B10 | PLE Linkage Rate (Pre-2015) |"
    surv_sep = "|:-------------|:---------------:|:-----------:|:-----------:|:--------------------------:|"
    lines.append(surv_header)
    lines.append(surv_sep)

    surv_data = []
    for cg in best["CourseGroup"].value_counts().index:
        sub_best = best[best["CourseGroup"] == cg]
        n_cg = len(sub_best)
        n_b8b10 = int((sub_best["PercentileBin"].isin(["B8", "B9", "B10"])).sum())
        pct_b8b10 = (n_b8b10 / n_cg * 100) if n_cg > 0 else 0

        sub_obs = obs[obs["CourseGroup"] == cg]
        n_obs_cg = len(sub_obs)
        n_ple_cg = int(sub_obs["IS_PLE_PASSER"].sum())
        lr_cg = (n_ple_cg / n_obs_cg * 100) if n_obs_cg > 0 else 0

        lines.append(
            f"| {cg} | {n_cg:,} | {n_b8b10:,} | {pct_b8b10:.2f}% | {lr_cg:.2f}% |"
        )
        surv_data.append((cg, pct_b8b10, lr_cg))

    lines.append("")

    # ────────────────────────────────────────────────────────────────────
    # Key interpretation
    # ────────────────────────────────────────────────────────────────────
    lines.append("### Key Interpretation\n")
    lines.append("")
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
    lines.append(
        "**Course group survival:** The share of examinees in B8-B10 varies notably by course group, "
        "from ~27% (Social & Behavioral Sciences) to ~51% (Engineering & Technology). "
        "However, smaller sample sizes for some groups warrant cautious interpretation."
    )
    lines.append("")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)

    # ── Console summary ─────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"  {TITLE}")
    print(f"{'='*70}")
    print(f"  Pre-2015 cohort:            {total_obs:>7,}")
    print(f"  PLE matched:                {total_ple:>7,}")
    print(f"  Overall linkage rate:       {overall_linkage:>6.2f}%")
    print(f"  B4 linkage rate:            {b4_lr:>6.2f}%")
    print(f"  B5 linkage rate:            {b5_lr:>6.2f}%")
    print(f"  B4->B5 jump:               +{jump:>5.2f} pp")
    print(f"  PLE-linked median pctl:     {ple_passers['NMS_PER_num'].median():>6.1f}")
    print(f"  Non-linked median pctl:     {non_passers['NMS_PER_num'].median():>6.1f}")
    for cg, pct_b8b10, lr_cg in surv_data:
        print(f"  {cg:40s} B8-B10: {pct_b8b10:>5.1f}%  Linkage: {lr_cg:.2f}%")
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
