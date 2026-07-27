#!/usr/bin/env python3
"""
Extract ALL data from dashboard.py Page 3 (Trends & Stability).
Replicates: tab3 (Performance Trends and Year-to-Year Stability)
Output: page_results/03_trends_stability.md
"""
import sys
sys.path.append("data_aggregator")

from pathlib import Path
from datetime import datetime
import numpy as np
import pandas as pd

from helpers import load_data, yearly_summary, kruskal_table


def fmt_df(df, caption=None):
    """Return markdown string of a DataFrame."""
    lines_out = []
    if caption:
        lines_out.append(f"**{caption}**\n")
    lines_out.append(
        df.to_markdown(index=False, tablefmt="pipe", numalign="right")
    )
    lines_out.append("")
    return "\n".join(lines_out)


def box_stats(df, year_col, value_col, label):
    """Compute yearly distribution stats for one score variable."""
    stats = (
        df.dropna(subset=[year_col, value_col])
        .groupby(year_col, observed=True)[value_col]
        .agg(
            n="count",
            mean="mean",
            std="std",
            min="min",
            q25=lambda x: x.quantile(0.25),
            median="median",
            q75=lambda x: x.quantile(0.75),
            max="max",
        )
        .round(2)
        .reset_index()
    )
    stats.columns = [
        year_col, "n", "mean", "std", "min",
        "q25", "median", "q75", "max"
    ]
    return stats


def run():
    """Compute all Page 3 metrics and return as markdown string."""
    df, F = load_data()
    df = F["besttrend"]

    lines = []

    # -- Header --
    lines.append("# Page 3: Trends & Stability")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("**Data source:** NMAT_Exodus.parquet (Pipeline 4)")
    lines.append("")
    lines.append("**Data subset:** `besttrend` (IS_BEST_NMAT_RECORD & Year 2006-2018)")
    lines.append("")
    lines.append("**Filters:** None (full unfiltered dataset)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # -- 1. Annual Score Trends --
    lines.append("## 1. Annual Score Trends")
    lines.append("")
    lines.append(
        "Yearly summary with n, median_raw, q25_raw, q75_raw, "
        "median_pct, q25_pct, q75_pct, median_gps, median_apt, median_sa."
    )
    lines.append("")
    summary = yearly_summary(df)
    lines.append(fmt_df(summary, "Table: Annual Score Trends (yearly_summary)"))
    lines.append("")

    # -- 2. Box Plot Data --
    lines.append("## 2. Box Plot Data (Yearly Distribution Stats)")
    lines.append("")

    box_vars = [
        ("TotalRawScoreTRUE", "Total Raw Score"),
        ("NMS_PER_num", "Percentile Rank"),
        ("PartIRawScoreTRUE", "Part I Raw Score"),
        ("PartIIRawScoreTRUE", "Part II Raw Score"),
    ]
    for col, label in box_vars:
        sdf = box_stats(df, "Year", col, label)
        lines.append(fmt_df(sdf, f"Box plot data: {label} ({col}) by Year"))
        lines.append("")

    # -- 3. Kruskal-Wallis Table --
    lines.append("## 3. Kruskal-Wallis Tests for Year-to-Year Score Differences")
    lines.append("")
    lines.append(
        "Tests whether score distributions differ significantly across NMAT years. "
        "Eta-squared included as effect-size indicator."
    )
    lines.append("")
    # helpers.py kruskal_table expects {display_name: column_name} convention
    ktable = kruskal_table(
        df,
        "Year",
        {
            "Total Raw Score": "TotalRawScoreTRUE",
            "Part I Raw Score": "PartIRawScoreTRUE",
            "Part II Raw Score": "PartIIRawScoreTRUE",
            "Percentile Rank": "NMS_PER_num",
            "GPS Standard Score": "NMS_GPS",
        },
    )
    if not ktable.empty:
        lines.append(fmt_df(ktable, "Table: Kruskal-Wallis Tests"))
    else:
        lines.append("*(No valid Kruskal-Wallis results — insufficient groups with n >= 5.)*")
    lines.append("")

    # -- 4. IQR Ranges by Year --
    lines.append("## 4. IQR Ranges by Year")
    lines.append("")
    iqr_df = (
        df.groupby("Year", observed=True)
        .agg(
            n=("TotalRawScoreTRUE", "size"),
            median_raw=("TotalRawScoreTRUE", "median"),
            q25_raw=("TotalRawScoreTRUE", lambda x: x.quantile(0.25)),
            q75_raw=("TotalRawScoreTRUE", lambda x: x.quantile(0.75)),
            iqr_raw=("TotalRawScoreTRUE", lambda x: x.quantile(0.75) - x.quantile(0.25)),
            median_pct=("NMS_PER_num", "median"),
            q25_pct=("NMS_PER_num", lambda x: x.quantile(0.25)),
            q75_pct=("NMS_PER_num", lambda x: x.quantile(0.75)),
            iqr_pct=("NMS_PER_num", lambda x: x.quantile(0.75) - x.quantile(0.25)),
        )
        .reset_index()
        .round(2)
    )
    lines.append(
        fmt_df(iqr_df, "Table: IQR Ranges by Year (raw score and percentile rank)")
    )
    lines.append("")

    return "\n".join(lines)


def save(md):
    out_dir = Path("page_results")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "03_trends_stability.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    md = run()
    save(md)
    print(f"Output length: {len(md)} chars")
    # Print first 300 chars as preview
    print("--- PREVIEW (first 300 chars) ---")
    print(md[:300])
