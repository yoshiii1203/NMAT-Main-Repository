"""
03_per_hei_distribution.py — Per-HEI NMAT score distribution analysis.

Computes:
  - Full bin distribution (B1-B10) per HEI with >=5 examinees
  - HEI ranking by median percentile
  - HEI type classification (SUC/PHEI)
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

SCRIPT = "03_per_hei_distribution"
TITLE = "Per-HEI NMAT Score Distribution Analysis"


def compute():
    df = load_data()
    subsets = create_subsets(df)
    best = subsets["best"]

    lines = []
    lines.append("## Results\n")
    lines.append(
        "This section examines the NMAT score distribution at the institution (HEI) level. "
        "Only HEIs with 5 or more examinees are included in the detailed analysis. "
        "HEIs with fewer than 5 examinees are flagged as having insufficient data."
    )
    lines.append("")

    # ── Prepare per-HEI data ────────────────────────────────────────────
    hei_col = "NMA_College"

    # Group by HEI
    hei_groups = best.groupby(hei_col)

    hei_stats = []
    for hei, grp in hei_groups:
        n = len(grp)
        uni_type = grp["UNI_TYPE"].mode().iloc[0] if len(grp) > 0 else "Unknown"

        if n < 5:
            hei_stats.append({
                "HEI": hei,
                "UNI_TYPE": uni_type,
                "n": n,
                "median_pct": None,
                "insufficient": True,
            })
            continue

        median_pct = grp["NMS_PER_num"].median()
        total_bins = len(grp)
        bin_dist = {}
        for b in BIN_ORDER:
            bin_dist[b] = int((grp["PercentileBin"] == b).sum())

        hei_stats.append({
            "HEI": hei,
            "UNI_TYPE": uni_type,
            "n": n,
            "median_pct": median_pct,
            "insufficient": False,
            **bin_dist,
        })

    hei_df = pd.DataFrame(hei_stats)
    sufficient = hei_df[hei_df["insufficient"] == False].copy()
    insufficient = hei_df[hei_df["insufficient"] == True].copy()

    # ── Metric cards ────────────────────────────────────────────────────
    total_heis = len(hei_df)
    sufficient_heis = len(sufficient)
    insufficient_heis = len(insufficient)

    # Top 10 by median percentile
    top_heis = sufficient.nlargest(10, "median_pct")["HEI"].tolist()
    bottom_heis = sufficient.nsmallest(10, "median_pct")["HEI"].tolist()

    metrics = [
        ("Total HEIs Represented", fmt(total_heis)),
        ("HEIs with >=5 Examinees (Analyzed)", fmt(sufficient_heis)),
        ("HEIs with <5 Examinees (Insufficient Data)", fmt(insufficient_heis)),
        ("Total Examinees in Analyzed HEIs", fmt(int(sufficient["n"].sum()))),
        ("Total Examinees in Insufficient-Data HEIs", fmt(int(insufficient["n"].sum()))),
        ("Top HEI by Median Percentile", top_heis[0] if top_heis else "N/A"),
        ("Bottom HEI by Median Percentile", bottom_heis[0] if bottom_heis else "N/A"),
    ]
    lines.append("### Key Metrics\n")
    lines.append(make_metric_table(metrics))
    lines.append("")

    # ── Top 25 HEIs by median percentile ────────────────────────────────
    lines.append("### Top 25 HEIs by Median NMAT Percentile\n")
    lines.append(
        "HEIs with >=5 examinees, ranked by median NMS_PER_num (percentile).\n"
    )

    top25 = sufficient.nlargest(25, "median_pct")

    bin_header = " | ".join([""] + BIN_ORDER)
    header = f"| Rank | HEI | UNI_TYPE | n | Median Pctl | {bin_header} |"
    sep_vals = ["|:----:|------|:--------:|:--:|:----------:|"] + [":---:"] * len(BIN_ORDER)
    sep = " ".join(sep_vals)
    lines.append(header)
    lines.append(sep)

    for i, (_, row) in enumerate(top25.iterrows(), 1):
        bin_strs = [str(int(row[b])) for b in BIN_ORDER]
        hei_name = row["HEI"]
        if len(hei_name) > 40:
            hei_name = hei_name[:37] + "..."
        lines.append(
            f"| {i} | {hei_name} | {row['UNI_TYPE']} | {int(row['n']):,} | "
            f"{row['median_pct']:.1f} | {' | '.join(bin_strs)} |"
        )

    lines.append("")

    # ── Bottom 25 HEIs by median percentile ─────────────────────────────
    lines.append("### Bottom 25 HEIs by Median NMAT Percentile\n")
    lines.append(
        "HEIs with >=5 examinees, ranked by lowest median NMS_PER_num.\n"
    )

    bot25 = sufficient.nsmallest(25, "median_pct")

    lines.append(header)
    lines.append(sep)

    for i, (_, row) in enumerate(bot25.iterrows(), 1):
        bin_strs = [str(int(row[b])) for b in BIN_ORDER]
        hei_name = row["HEI"]
        if len(hei_name) > 40:
            hei_name = hei_name[:37] + "..."
        lines.append(
            f"| {i} | {hei_name} | {row['UNI_TYPE']} | {int(row['n']):,} | "
            f"{row['median_pct']:.1f} | {' | '.join(bin_strs)} |"
        )

    lines.append("")

    # ── Distribution by UNI_TYPE ────────────────────────────────────────
    lines.append("### Summary by University Type\n")
    lines.append("Aggregated HEI-level statistics by UNI_TYPE.\n")

    ut_header = "| UNI_TYPE | HEIs (>=5) | Total Examinees | Median Pctl (Median of HEI Medians) | Avg HEI Size |"
    ut_sep = "|:---------|:----------:|:---------------:|:-----------------------------------:|:------------:|"
    lines.append(ut_header)
    lines.append(ut_sep)

    for ut in UNI_TYPE_ORDER:
        sub = sufficient[sufficient["UNI_TYPE"] == ut]
        if len(sub) == 0:
            continue
        median_of_medians = sub["median_pct"].median()
        avg_size = sub["n"].mean()
        lines.append(
            f"| {ut} | {len(sub):,} | {int(sub['n'].sum()):,} | "
            f"{median_of_medians:.1f} | {avg_size:.0f} |"
        )

    lines.append("")

    # ── HEIs with insufficient data ─────────────────────────────────────
    lines.append("### HEIs with Insufficient Data (<5 Examinees)\n")
    lines.append(
        f"There are {insufficient_heis} HEIs with fewer than 5 examinees "
        f"(totaling {int(insufficient['n'].sum())} examinees). These are "
        "excluded from ranking analysis but listed below.\n"
    )

    insuf_header = "| HEI | UNI_TYPE | n |"
    insuf_sep = "|-----|:--------:|:-:|"
    lines.append(insuf_header)
    lines.append(insuf_sep)

    for _, row in insufficient.iterrows():
        hei_name = row["HEI"]
        if len(hei_name) > 50:
            hei_name = hei_name[:47] + "..."
        lines.append(f"| {hei_name} | {row['UNI_TYPE']} | {int(row['n'])} |")

    lines.append("")

    # ── HEIs with 0 examinees (should not exist) ────────────────────────
    lines.append("### Data Quality Notes\n")
    lines.append(f"- **HEI column used:** `{hei_col}`")
    lines.append(f"- **Examinee count:** best record per person (IS_BEST_NMAT_RECORD == True)")
    lines.append(f"- **Total unique HEIs:** {total_heis}")
    lines.append(f"- **HEIs with >=5 examinees:** {sufficient_heis}")
    lines.append(f"- **HEIs with <5 examinees (flagged):** {insufficient_heis}")
    lines.append("- HEI names are as recorded in `NMA_College`. Name variations across years are not normalized.")
    lines.append("")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)

    # ── Print summary ───────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"  {TITLE}")
    print(f"{'='*70}")
    print(f"  Total HEIs:                  {total_heis:>5,}")
    print(f"  HEIs with >=5 examinees:     {sufficient_heis:>5,}")
    print(f"  HEIs with <5 examinees:      {insufficient_heis:>5,}")
    print(f"  Total examinees (analyzed):  {int(sufficient['n'].sum()):>7,}")
    print(f"  Top HEI:                     {top_heis[0] if top_heis else 'N/A'}")
    print(f"  Bottom HEI:                  {bottom_heis[0] if bottom_heis else 'N/A'}")
    print(f"  Output: {path}")
    print(f"{'='*70}\n")

    return {
        "total_heis": total_heis,
        "sufficient_heis": sufficient_heis,
        "insufficient_heis": insufficient_heis,
    }


if __name__ == "__main__":
    compute()
