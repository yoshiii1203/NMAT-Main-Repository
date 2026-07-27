"""
Page 09 — Subtest Profiles
=============================
Output: page_results/09_subtests.md

Analyses:
  1. Subtest standard score means by UNI_TYPE
  2. Subtest standard score means by CourseGroup
  3. Subtest raw score means by UNI_TYPE
  4. Subtest raw score means by CourseGroup
  5. Radar profile data (standard scores centered for comparison)
  6. Full descriptive statistics table (n, mean, median, std, min, max for each subtest)

Data subset: "uni" for UNI_TYPE analyses, "besttrend" for CourseGroup and descriptive stats
Filters: None (full unfiltered dataset)
"""
import sys
sys.path.append("data_aggregator")

import numpy as np
import pandas as pd

from config import SUBTEST_STD, SUBTEST_RAW
from helpers import write_header, write_dataframe

MD_PATH = "page_results/09_subtests.md"

# ── Column lists ──────────────────────────────────────────────────────────
STD_ORDER = [
    "Verbal", "Inductive", "Quantitative", "Perceptual",
    "Biology", "Physics", "Social", "Chemistry",
]
RAW_ORDER = STD_ORDER  # same ordering


def load_besttrend():
    """Load besttrend subset (best NMAT record, Year 2006-2018)."""
    import pyarrow.parquet as pq
    table = pq.read_table("dataset/NMAT_Exodus.parquet")
    df = table.to_pandas()
    del table

    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")

    mask = (
        (df.get("IS_BEST_NMAT_RECORD", pd.Series([True] * len(df))) == True)
        & (df["Year"].between(2006, 2018, inclusive="both"))
    )
    besttrend = df.loc[mask].copy()
    del df
    return besttrend


def load_uni_subset():
    """Load uni subset (besttrend with UNI_TYPE in Public/Private/Foreign)."""
    besttrend = load_besttrend()
    mask = besttrend["UNI_TYPE"].isin(["Public", "Private", "Foreign"])
    uni = besttrend.loc[mask].copy()
    # Keep besttrend for CourseGroup and descriptive analyses
    return uni, besttrend


def subtest_mean_table(df, group_col, std=True):
    """Replicate dashboard subtest_mean_table()."""
    cols = SUBTEST_STD if std else SUBTEST_RAW
    available = {k: v for k, v in cols.items() if v in df.columns}
    if not available:
        return pd.DataFrame()
    out = df.groupby(group_col, observed=True)[list(available.values())].mean().round(2)
    out.columns = list(available.keys())
    return out


def radar_centered_table(std_table):
    """Center standard scores by subtracting the overall mean per subtest for radar comparison."""
    if std_table.empty:
        return pd.DataFrame()
    centered = std_table.copy()
    for col in centered.columns:
        centered[col] = centered[col] - centered[col].mean()
    return centered.round(2)


def descriptive_stats_table(df):
    """Full descriptive stats (n, mean, median, std, min, max) for each subtest.

    Includes both standard and raw scores.
    """
    all_cols = {}
    all_cols.update(SUBTEST_STD)
    all_cols.update(SUBTEST_RAW)

    rows = []
    for label, col in all_cols.items():
        if col not in df.columns:
            continue
        vals = df[col].dropna()
        if len(vals) == 0:
            continue
        score_type = "Standard" if col in SUBTEST_STD.values() else "Raw"
        rows.append({
            "Subtest": label,
            "Type": score_type,
            "n": len(vals),
            "Mean": round(vals.mean(), 2),
            "Median": round(vals.median(), 2),
            "Std": round(vals.std(), 2),
            "Min": round(vals.min(), 2),
            "Max": round(vals.max(), 2),
        })

    return pd.DataFrame(rows)


def write_section_std_uni(f, uni_df):
    """1. Subtest standard score means by UNI_TYPE."""
    f.write("## 1. Subtest Standard Score Means by UNI_TYPE\n\n")
    tbl = subtest_mean_table(uni_df, "UNI_TYPE", std=True)
    if tbl.empty:
        f.write("*No standard score data available.*\n\n")
        return
    # Reorder rows
    row_order = [u for u in ["Public", "Private", "Foreign"] if u in tbl.index]
    if row_order:
        tbl = tbl.reindex(row_order)
    write_dataframe(f, tbl.reset_index(), "Table 34. Standardized subtest means by university type")
    f.write("---\n\n")


def write_section_raw_uni(f, uni_df):
    """3. Subtest raw score means by UNI_TYPE."""
    f.write("## 2. Subtest Raw Score Means by UNI_TYPE\n\n")
    tbl = subtest_mean_table(uni_df, "UNI_TYPE", std=False)
    if tbl.empty:
        f.write("*No raw score data available.*\n\n")
        return
    row_order = [u for u in ["Public", "Private", "Foreign"] if u in tbl.index]
    if row_order:
        tbl = tbl.reindex(row_order)
    write_dataframe(f, tbl.reset_index(), "Table 35. Raw-score subtest means by university type")
    f.write("---\n\n")


def write_section_std_course(f, df):
    """2. Subtest standard score means by CourseGroup."""
    f.write("## 3. Subtest Standard Score Means by CourseGroup\n\n")
    tbl = subtest_mean_table(df, "CourseGroup", std=True)
    if tbl.empty:
        f.write("*No standard score data available.*\n\n")
        return
    course_order = [
        "Medical & Allied", "Natural Sciences", "Social & Behavioral Sciences",
        "Education", "Engineering & Technology", "Other",
    ]
    course_order = [c for c in course_order if c in tbl.index]
    if course_order:
        tbl = tbl.reindex(course_order)
    write_dataframe(f, tbl.reset_index(), "Table 36. Standardized subtest means by course group")
    f.write("---\n\n")


def write_section_raw_course(f, df):
    """4. Subtest raw score means by CourseGroup."""
    f.write("## 4. Subtest Raw Score Means by CourseGroup\n\n")
    tbl = subtest_mean_table(df, "CourseGroup", std=False)
    if tbl.empty:
        f.write("*No raw score data available.*\n\n")
        return
    course_order = [
        "Medical & Allied", "Natural Sciences", "Social & Behavioral Sciences",
        "Education", "Engineering & Technology", "Other",
    ]
    course_order = [c for c in course_order if c in tbl.index]
    if course_order:
        tbl = tbl.reindex(course_order)
    write_dataframe(f, tbl.reset_index(), "Table 37. Raw-score subtest means by course group")
    f.write("---\n\n")


def write_section_radar(f, uni_df, df):
    """5. Radar profile data (standard scores centered for comparison)."""
    f.write("## 5. Radar Profile Data (Standard Scores Centered for Comparison)\n\n")

    # ── By UNI_TYPE ──
    f.write("### 5.1 By University Type\n\n")
    std_uni = subtest_mean_table(uni_df, "UNI_TYPE", std=True)
    if std_uni.empty:
        f.write("*No data available.*\n\n")
    else:
        row_order = [u for u in ["Public", "Private", "Foreign"] if u in std_uni.index]
        if row_order:
            std_uni = std_uni.reindex(row_order)
        centered_uni = radar_centered_table(std_uni)
        f.write("**Table 38. Radar-profile values (centered standard scores) by university type**\n\n")
        f.write("*Values are mean-centered within each subtest (overall mean subtracted). Negative values indicate below-average performance for that group on that subtest, positive values above-average.*\n\n")
        write_dataframe(f, centered_uni.reset_index(), None)
    f.write("\n")

    # ── By CourseGroup ──
    f.write("### 5.2 By Course Group\n\n")
    std_course = subtest_mean_table(df, "CourseGroup", std=True)
    if std_course.empty:
        f.write("*No data available.*\n\n")
    else:
        course_order = [
            "Medical & Allied", "Natural Sciences", "Social & Behavioral Sciences",
            "Education", "Engineering & Technology", "Other",
        ]
        course_order = [c for c in course_order if c in std_course.index]
        if course_order:
            std_course = std_course.reindex(course_order)
        centered_course = radar_centered_table(std_course)
        f.write("**Table 39. Radar-profile values (centered standard scores) by course group**\n\n")
        f.write("*Values are mean-centered within each subtest (overall mean subtracted). Negative values indicate below-average performance for that group on that subtest, positive values above-average.*\n\n")
        write_dataframe(f, centered_course.reset_index(), None)
    f.write("---\n\n")


def write_section_descriptive_stats(f, df):
    """6. Full descriptive statistics for each subtest."""
    f.write("## 6. Full Descriptive Statistics (n, Mean, Median, Std, Min, Max)\n\n")
    tbl = descriptive_stats_table(df)
    if tbl.empty:
        f.write("*No subtest score data available.*\n\n")
    else:
        write_dataframe(f, tbl, "Table 40. Descriptive statistics for each subtest (standard and raw scores)")
    f.write("---\n\n")


def run():
    """Run all analyses and write to markdown."""
    print("[Page 09] Loading data...")
    uni_df, besttrend_df = load_uni_subset()
    print(f"  uni subset:       {len(uni_df):,} records")
    print(f"  besttrend subset: {len(besttrend_df):,} records")

    print("[Page 09] Computing analyses...")
    with open(MD_PATH, "w", encoding="utf-8") as f:
        write_header(f, "Page 09: Subtest Profiles", "uni (UNI_TYPE) / besttrend (CourseGroup, desc)", 9)

        write_section_std_uni(f, uni_df)
        write_section_raw_uni(f, uni_df)
        write_section_std_course(f, besttrend_df)
        write_section_raw_course(f, besttrend_df)
        write_section_radar(f, uni_df, besttrend_df)
        write_section_descriptive_stats(f, besttrend_df)

    print(f"[Page 09] Written to {MD_PATH}")


def save():
    """Alias for run()."""
    run()


if __name__ == "__main__":
    run()
