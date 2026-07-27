"""
Page 1: Executive Summary
Replicates ALL computations from dashboard.py tab1 (lines 754-828).
Extracts unfiltered data and saves to page_results/01_executive_summary.md.
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "data_aggregator"))

import numpy as np
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
pd.set_option("display.max_colwidth", 50)

from config import BIN_ORDER, PLE_ORDER, RESULTS_DIR
from helpers import load_data, write_header, write_dataframe, yearly_summary


def run() -> str:
    df, subsets = load_data()

    # Subsets matching dashboard tab1
    base = subsets["besttrend"]       # best-record rows within 2006-2018
    observable = subsets["bestobservable"]  # best-record rows with Year <= 2014
    trend = subsets["trend"]           # all rows within 2006-2018

    lines = []

    # ========== HEADER ==========
    lines.append("# Page 1: Executive Summary")
    lines.append("")
    lines.append(f"**Generated:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("**Data source:** NMAT_Exodus.parquet (Pipeline 4)")
    lines.append("")
    lines.append("**Data subset:** `besttrend` (best-record rows 2006-2018) and `bestobservable` (Year <= 2014)")
    lines.append("")
    lines.append("**Filters:** None (full unfiltered dataset)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ========== 8 METRIC CARDS ==========
    lines.append("## Metric Cards (Row 1)")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|------:|")
    lines.append(f"| Best-record examinees | {len(base):,} |")
    lines.append(f"| Years covered | {base['Year'].nunique():,} |")
    lines.append(f"| Median TRUE raw score | {base['TotalRawScoreTRUE'].median():.1f} |")
    lines.append(f"| Median percentile rank | {base['NMS_PER_num'].median():.1f} |")
    lines.append("")
    lines.append("## Metric Cards (Row 2)")
    lines.append("")
    # Repeat takers: trend (not besttrend) grouped by PERSON_KEY
    repeat_takers = int((trend.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique() > 1).sum())
    confirmed_ple_share = observable["HAS_CONFIRMED_PLE"].mean() * 100

    lines.append("| Metric | Value |")
    lines.append("|--------|------:|")
    lines.append(f"| Unique examinees | {base['PERSON_KEY'].nunique():,} |")
    lines.append(f"| Repeat takers | {repeat_takers:,} |")
    lines.append(f"| Observable cohort size | {len(observable):,} |")
    lines.append(f"| Confirmed PLE share (observable) | {confirmed_ple_share:.2f}% |")
    lines.append("")

    lines.append("---")
    lines.append("")

    # ========== COURSE GROUP DISTRIBUTION ==========
    lines.append("## Course Group Composition")
    lines.append("")
    course_dist = base["CourseGroup"].value_counts().rename_axis("CourseGroup").reset_index(name="Count")
    course_dist["Share (%)"] = (course_dist["Count"] / course_dist["Count"].sum() * 100).round(2)
    lines.append("**Figure 2 data — Course-group pie chart (best-record examinees)**")
    lines.append("")
    lines.append(course_dist.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # ========== UNIVERSITY TYPE COMPOSITION ==========
    lines.append("## University Type Composition")
    lines.append("")
    uni_dist = base["UNI_TYPE"].value_counts().rename_axis("UNI_TYPE").reset_index(name="Count")
    uni_dist["Share (%)"] = (uni_dist["Count"] / uni_dist["Count"].sum() * 100).round(2)
    lines.append("**Figure 3 data — University-type pie chart (best-record examinees)**")
    lines.append("")
    lines.append(uni_dist.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    lines.append("---")
    lines.append("")

    # ========== ANNUAL NMAT SCORE AND VOLUME PROFILE ==========
    lines.append("## Annual NMAT Score and Volume Profile (Figure 1)")
    lines.append("")
    lines.append("**Figure 1. Annual NMAT score and volume profile**")
    lines.append("")
    lines.append("Median TRUE raw score, Part I and Part II medians, median percentile rank, and examinee count by year.")
    lines.append("")

    summary = yearly_summary(base)
    lines.append("### Yearly Summary (besttrend cohort)")
    lines.append("")
    lines.append(summary.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # Additional columns per get_yearly_summary
    summary_detail = summary.copy()
    if not summary_detail.empty:
        summary_detail["IQR Raw"] = summary_detail["q75_raw"] - summary_detail["q25_raw"]
        summary_detail["Part I Share (%)"] = np.where(
            summary_detail["median_raw"] > 0,
            (summary_detail["median_raw"] / summary_detail["median_raw"]) * 100,
            np.nan
        )
        # Recalculate Part I and Part II share properly using PartIRawScoreTRUE medians
        # The dashboard computes these from yearly aggregates
        part1_by_year = base.groupby("Year", observed=True)["PartIRawScoreTRUE"].median().round(2)
        part2_by_year = base.groupby("Year", observed=True)["PartIIRawScoreTRUE"].median().round(2)
        raw_med_by_year = base.groupby("Year", observed=True)["TotalRawScoreTRUE"].median().round(2)

        share_df = pd.DataFrame({
            "Year": part1_by_year.index,
            "Median Part I": part1_by_year.values,
            "Median Part II": part2_by_year.values,
            "Median Total Raw": raw_med_by_year.values,
            "Part I Share (%)": np.where(raw_med_by_year.values > 0,
                                          (part1_by_year.values / raw_med_by_year.values * 100).round(2), np.nan),
            "Part II Share (%)": np.where(raw_med_by_year.values > 0,
                                           (part2_by_year.values / raw_med_by_year.values * 100).round(2), np.nan),
        })
        lines.append("### Yearly Part I / Part II Breakdown")
        lines.append("")
        lines.append(share_df.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")

    lines.append("---")
    lines.append("")

    # ========== TOP / BOTTOM BIN SHARE TREND ==========
    lines.append("## Top / Bottom Bin Share Trend")
    lines.append("")

    # Bin share by year for trend analysis
    bin_by_year = base.groupby("Year", observed=True)["PercentileBin"]
    bin_data = []
    for yr, grp in bin_by_year:
        n = len(grp)
        bin_data.append({
            "Year": yr,
            "N": n,
            "Top share % (B8-B10)": round((grp.isin(["B8", "B9", "B10"]).mean() * 100), 2),
            "Mid share % (B4-B7)": round((grp.isin(["B4", "B5", "B6", "B7"]).mean() * 100), 2),
            "Bottom share % (B1-B3)": round((grp.isin(["B1", "B2", "B3"]).mean() * 100), 2),
        })
    bin_df = pd.DataFrame(bin_data)

    lines.append("**Yearly bin share breakdown (besttrend cohort)**")
    lines.append("")
    lines.append(bin_df.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # Overall shares for the full besttrend cohort
    top_bin_share = base["PercentileBin"].isin(["B8", "B9", "B10"]).mean() * 100
    bottom_bin_share = base["PercentileBin"].isin(["B1", "B2", "B3"]).mean() * 100
    mid_bin_share = base["PercentileBin"].isin(["B4", "B5", "B6", "B7"]).mean() * 100

    lines.append("**Overall bin shares (full besttrend cohort)**")
    lines.append("")
    lines.append(f"- Top-bin share (B8-B10): {top_bin_share:.2f}%")
    lines.append(f"- Mid-bin share (B4-B7): {mid_bin_share:.2f}%")
    lines.append(f"- Bottom-bin share (B1-B3): {bottom_bin_share:.2f}%")
    lines.append("")

    lines.append("---")
    lines.append("")

    # ========== EXECUTIVE SUMMARY INDICATORS TABLE ==========
    lines.append("## Executive Summary Indicators (Table 1)")
    lines.append("")

    summary_tbl = pd.DataFrame({
        "Indicator": [
            "Median Total Raw Score",
            "Median Part I Raw Score",
            "Median Part II Raw Score",
            "Median Percentile Rank",
            "Top-bin share (B8-B10)",
            "Bottom-bin share (B1-B3)",
        ],
        "Value": [
            round(base["TotalRawScoreTRUE"].median(), 2),
            round(base["PartIRawScoreTRUE"].median(), 2),
            round(base["PartIIRawScoreTRUE"].median(), 2),
            round(base["NMS_PER_num"].median(), 2),
            round(top_bin_share, 2),
            round(bottom_bin_share, 2),
        ]
    })
    lines.append(summary_tbl.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    lines.append("---")
    lines.append("")

    # ========== SUPPLEMENTARY: ALL YEARS OVERVIEW ==========
    lines.append("## Supplementary: All-year overview (besttrend cohort)")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|------:|")
    lines.append(f"| Total rows (besttrend) | {len(base):,} |")
    lines.append(f"| Total unique examinees | {base['PERSON_KEY'].nunique():,} |")
    years_list = sorted(base['Year'].dropna().unique().tolist())
    years_str = ", ".join(str(y) for y in years_list)
    lines.append(f"| Years covered | {years_str} |")
    lines.append(f"| Median total raw score | {base['TotalRawScoreTRUE'].median():.2f} |")
    lines.append(f"| Mean total raw score | {base['TotalRawScoreTRUE'].mean():.2f} |")
    lines.append(f"| Std total raw score | {base['TotalRawScoreTRUE'].std():.2f} |")
    lines.append(f"| Median Part I raw score | {base['PartIRawScoreTRUE'].median():.2f} |")
    lines.append(f"| Median Part II raw score | {base['PartIIRawScoreTRUE'].median():.2f} |")
    lines.append(f"| Median percentile rank | {base['NMS_PER_num'].median():.2f} |")
    lines.append(f"| Mean percentile rank | {base['NMS_PER_num'].mean():.2f} |")
    lines.append(f"| Median GPS | {base['NMS_GPS'].median():.2f} |")
    lines.append(f"| Median APT | {base['NMS_APT'].median():.2f} |")
    lines.append(f"| Median SA | {base['NMS_SA'].median():.2f} |")
    lines.append("")

    # Gross by university type
    lines.append("### Score Summary by University Type (besttrend)")
    lines.append("")
    uni_score_summary = (
        base.groupby("UNI_TYPE", observed=True)[
            ["TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE",
             "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA"]
        ]
        .agg(["count", "median", "mean"])
        .round(2)
    )
    lines.append(uni_score_summary.to_markdown(tablefmt="pipe", numalign="right"))
    lines.append("")

    # Gross by course group
    lines.append("### Score Summary by Course Group (besttrend)")
    lines.append("")
    course_score_summary = (
        base.groupby("CourseGroup", observed=True)[
            ["TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE",
             "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA"]
        ]
        .agg(["count", "median", "mean"])
        .round(2)
    )
    lines.append(course_score_summary.to_markdown(tablefmt="pipe", numalign="right"))
    lines.append("")

    return "\n".join(lines)


def save():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = RESULTS_DIR / "01_executive_summary.md"
    content = run()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved: {out_path.resolve()}")


if __name__ == "__main__":
    save()
