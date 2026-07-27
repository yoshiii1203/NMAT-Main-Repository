#!/usr/bin/env python3
"""
Extract ALL data from dashboard.py Page 4 (Score Bins + Citizenship).
Replicates: tab4 (Bin Distribution by Year and Examinee Background)
  + Citizenship section (ALL records, not just no-PLE-match)
Output: page_results/04_score_bins.md
"""
import sys
sys.path.append("data_aggregator")

from pathlib import Path
from datetime import datetime
import numpy as np
import pandas as pd

from helpers import load_data, pct_table, chi_square_table
from config import BIN_ORDER


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


def run():
    """Compute all Page 4 metrics and return as markdown string."""
    df_all, F = load_data()
    df = F["besttrend"]       # main bin data (besttrend)
    dfuni = F["uni"]           # university subset (besttrend & Public/Private/Foreign)

    lines = []

    # -- Header --
    lines.append("# Page 4: Score Bins + Citizenship")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("**Data source:** NMAT_Exodus.parquet (Pipeline 4)")
    lines.append("")
    lines.append("**Data subset:** `besttrend`/`uni` for bins; ALL records for citizenship")
    lines.append("")
    lines.append("**Filters:** None (full unfiltered dataset)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ========================================================================
    # SUB-TAB 1: BY YEAR
    # ========================================================================
    lines.append("## Sub-tab 1: By Year")
    lines.append("")
    lines.append(
        "Use this tab to see whether later cohorts became more concentrated "
        "in higher bins, lower bins, or the middle of the distribution."
    )
    lines.append("")

    count, pct = pct_table(df, "Year", "PercentileBin", BIN_ORDER)
    pct.index.name = "Year"

    # -- Count table --
    count_t = count.T.reindex(index=BIN_ORDER[::-1])
    count_t.index.name = "PercentileBin"
    count_out = count_t.reset_index()
    lines.append(fmt_df(count_out, "Table 10: Count of examinees in each bin by NMAT year"))
    lines.append("")

    # -- Percentage table --
    pct_out = pct.reset_index()
    lines.append(fmt_df(pct_out, "Percentage of examinees in each bin by NMAT year (row %)"))
    lines.append("")

    # -- Heatmap data (bin x year row percentages, transposed for heatmap) --
    pct_transposed = pct.T
    pct_transposed.index.name = "Bin"
    pct_transposed = pct_transposed.reindex(index=BIN_ORDER[::-1])
    lines.append("**Heatmap data: Bin Distribution by Year (row %, bins as rows, years as columns)**")
    lines.append("")
    lines.append(pct_transposed.to_markdown(tablefmt="pipe", numalign="right"))
    lines.append("")
    lines.append("")

    # -- Top (B8-B10) vs Bottom (B1-B3) bin share by year --
    top_share = pct[["B8", "B9", "B10"]].sum(axis=1).reset_index()
    top_share.columns = ["Year", "Top_B8_B10_pct"]
    bottom_share = pct[["B1", "B2", "B3"]].sum(axis=1).reset_index()
    bottom_share.columns = ["Year", "Bottom_B1_B3_pct"]
    tb = top_share.merge(bottom_share, on="Year")
    lines.append(fmt_df(tb, "Figure 7: Top-bin (B8-B10) vs Bottom-bin (B1-B3) share by Year"))
    lines.append("")

    # ========================================================================
    # SUB-TAB 2: UNIVERSITY TYPE
    # ========================================================================
    lines.append("---")
    lines.append("## Sub-tab 2: University Type")
    lines.append("")
    lines.append(
        "Insight: Compare which university types are overrepresented in higher bins."
    )
    lines.append("")

    _, uni_pct = pct_table(dfuni, "UNI_TYPE", "PercentileBin", BIN_ORDER)
    uni_pct.index.name = "UNI_TYPE"

    # -- Bin distribution percentages --
    uni_pct_out = uni_pct.reset_index()
    lines.append(fmt_df(uni_pct_out, "Figure 8: Percentile-bin distribution by university type (row %)"))
    lines.append("")

    # -- Top bin share (B8-B10) by UNI_TYPE --
    top_uni = uni_pct[["B8", "B9", "B10"]].sum(axis=1).reset_index()
    top_uni.columns = ["UNI_TYPE", "Top_B8_B10_pct"]
    lines.append(fmt_df(top_uni, "Figure 9: Share of examinees in B8-B10 by university type"))
    lines.append("")

    # -- Chi-square test: UNI_TYPE x PercentileBin --
    chi_uni = chi_square_table(
        dfuni.dropna(subset=["UNI_TYPE", "PercentileBin"]),
        "UNI_TYPE",
        "PercentileBin",
    )
    chi_summary_uni = pd.DataFrame([{
        "chi2": chi_uni["chi2"],
        "p_value": "<0.001" if chi_uni["p_value"] < 0.001 else round(chi_uni["p_value"], 4),
        "degrees_of_freedom": chi_uni["dof"],
        "n_observations": chi_uni["n"],
        "cramers_v": chi_uni["cramer_v"],
    }])
    lines.append(fmt_df(chi_summary_uni, "Table 11: Chi-square test — UNI_TYPE x PercentileBin"))
    lines.append("")

    # Observed contingency table
    obs_uni = chi_uni["observed"].reset_index()
    lines.append(fmt_df(obs_uni, "Observed contingency: UNI_TYPE x PercentileBin"))
    lines.append("")

    # Expected frequencies
    exp_uni = chi_uni["expected"].reset_index()
    lines.append(fmt_df(exp_uni, "Expected frequencies: UNI_TYPE x PercentileBin"))
    lines.append("")

    # ========================================================================
    # SUB-TAB 3: COURSE GROUP
    # ========================================================================
    lines.append("---")
    lines.append("## Sub-tab 3: Course Group")
    lines.append("")
    lines.append("Insight: Compare bin profiles across pre-med backgrounds.")
    lines.append("")

    _, course_pct = pct_table(df, "CourseGroup", "PercentileBin", BIN_ORDER)
    course_pct.index.name = "CourseGroup"

    # -- Bin distribution percentages --
    course_pct_out = course_pct.reset_index()
    lines.append(fmt_df(course_pct_out, "Figure 10: Percentile-bin distribution by Course Group (row %)"))
    lines.append("")

    # -- Top bin share (B8-B10) by CourseGroup --
    top_course = course_pct[["B8", "B9", "B10"]].sum(axis=1).reset_index()
    top_course.columns = ["CourseGroup", "Top_B8_B10_pct"]
    lines.append(fmt_df(top_course, "Figure 11: Share of examinees in B8-B10 by Course Group"))
    lines.append("")

    # -- Chi-square test: CourseGroup x PercentileBin --
    chi_course = chi_square_table(
        df.dropna(subset=["CourseGroup", "PercentileBin"]),
        "CourseGroup",
        "PercentileBin",
    )
    chi_summary_course = pd.DataFrame([{
        "chi2": chi_course["chi2"],
        "p_value": "<0.001" if chi_course["p_value"] < 0.001 else round(chi_course["p_value"], 4),
        "degrees_of_freedom": chi_course["dof"],
        "n_observations": chi_course["n"],
        "cramers_v": chi_course["cramer_v"],
    }])
    lines.append(fmt_df(chi_summary_course, "Chi-square test — CourseGroup x PercentileBin"))
    lines.append("")

    # Observed contingency table
    obs_course = chi_course["observed"].reset_index()
    lines.append(fmt_df(obs_course, "Observed contingency: CourseGroup x PercentileBin"))
    lines.append("")

    # Expected frequencies
    exp_course = chi_course["expected"].reset_index()
    lines.append(fmt_df(exp_course, "Expected frequencies: CourseGroup x PercentileBin"))
    lines.append("")

    # -- Percentile summary by CourseGroup --
    course_desc = (
        df.groupby("CourseGroup", observed=True)["NMS_PER_num"]
        .agg(n="count", median="median", q25=lambda x: x.quantile(0.25),
             q75=lambda x: x.quantile(0.75))
        .round(2)
        .reset_index()
    )
    lines.append(fmt_df(course_desc, "Table 12: Percentile summary by Course Group"))
    lines.append("")

    # ========================================================================
    # CITIZENSHIP SECTION (ALL records, not just no-PLE-match)
    # ========================================================================
    lines.append("---")
    lines.append("## Citizenship Section (ALL records)")
    lines.append("")
    lines.append(
        "Citizenship labels (CITIZENSHIP_FINAL, FOREIGNER_STATUS) are baked into "
        "NMAT_Exodus.parquet by Pipeline 4 using a 3-tier hierarchy: "
        "REAL_FOREIGNERS.csv ground truth -> pseudo-citizenship inference -> Filipino default."
    )
    lines.append("")
    lines.append(
        "**NOTE:** Unlike the dashboard (which filters to no-PLE-match records only), "
        "this section uses ALL records with a valid CITIZENSHIP_FINAL."
    )
    lines.append("")

    # Base: ALL records with CITIZENSHIP_FINAL not null
    _pc_base = df_all[df_all["CITIZENSHIP_FINAL"].notna()].copy()

    if _pc_base.empty:
        lines.append("*No CITIZENSHIP_FINAL data found in the dataset.*")
    else:
        _pc_foreigners = int((_pc_base["FOREIGNER_STATUS"] == "Verified Foreigner").sum())
        _pc_filipinos = int((_pc_base["CITIZENSHIP_FINAL"] == "Filipino").sum())
        _pc_distinct = int(_pc_base["CITIZENSHIP_FINAL"].nunique())

        # -- Summary metrics --
        lines.append("### Citizenship Profile — Summary Metrics")
        lines.append("")
        metrics_df = pd.DataFrame([
            ("Total records with citizenship", len(_pc_base)),
            ("Verified Foreigners", _pc_foreigners),
            ("Filipinos", _pc_filipinos),
            ("Distinct citizenship labels", _pc_distinct),
        ], columns=["Metric", "Value"])
        lines.append(fmt_df(metrics_df, "Citizenship profile metrics"))
        lines.append("")

        # -- CITIZENSHIP_FINAL distribution (counts, %) --
        lines.append("### CITIZENSHIP_FINAL Distribution")
        lines.append("")
        _pc_counts = (
            _pc_base["CITIZENSHIP_FINAL"]
            .value_counts()
            .reset_index()
        )
        _pc_counts.columns = ["CITIZENSHIP_FINAL", "n"]
        _pc_counts["percent"] = (
            _pc_counts["n"] / _pc_counts["n"].sum() * 100
        ).round(2)
        lines.append(fmt_df(_pc_counts, "CITIZENSHIP_FINAL — counts and percentages"))
        lines.append("")

        # -- FOREIGNER_STATUS distribution --
        lines.append("### FOREIGNER_STATUS Distribution")
        lines.append("")
        _pc_fs = (
            _pc_base["FOREIGNER_STATUS"]
            .value_counts(dropna=False)
            .reset_index()
        )
        _pc_fs.columns = ["FOREIGNER_STATUS", "n"]
        _pc_fs["percent"] = (
            _pc_fs["n"] / _pc_fs["n"].sum() * 100
        ).round(2)
        lines.append(fmt_df(_pc_fs, "FOREIGNER_STATUS — counts and percentages"))
        lines.append("")

        # -- Foreigners vs Filipinos comparison --
        lines.append("### Foreigners vs Filipinos Comparison")
        lines.append("")
        _pc_fvf = pd.DataFrame({
            "group": ["Foreigner", "Filipino"],
            "n": [_pc_foreigners, _pc_filipinos],
        })
        _pc_fvf["percent"] = (
            _pc_fvf["n"] / _pc_fvf["n"].sum() * 100
        ).round(2)
        lines.append(fmt_df(_pc_fvf, "Foreigners vs Filipinos"))
        lines.append("")

        # -- Top 15 citizenship groups by count --
        lines.append("### Top 15 Citizenship Groups by Count")
        lines.append("")
        _top15 = _pc_counts.head(15).copy()
        _top15_sorted = _top15.sort_values("n")
        lines.append(fmt_df(_top15_sorted, "Top 15 citizenship groups"))
        lines.append("")

        # -- Bin composition by citizenship (top 15 groups) --
        lines.append("### Bin Composition by Citizenship (Top 15 Groups)")
        lines.append("")
        _pc_top_grps = _top15["CITIZENSHIP_FINAL"].tolist()
        _pc_dec_base = _pc_base[_pc_base["CITIZENSHIP_FINAL"].isin(_pc_top_grps)].copy()
        if not _pc_dec_base.empty and "PercentileBin" in _pc_dec_base.columns:
            _, _pc_dec_pct = pct_table(
                _pc_dec_base, "CITIZENSHIP_FINAL", "PercentileBin", BIN_ORDER
            )
            _pc_dec_pct.index.name = "CITIZENSHIP_FINAL"
            _pc_dec_pct_out = _pc_dec_pct.reset_index()
            lines.append(fmt_df(_pc_dec_pct_out, "Bin composition by citizenship (row %)"))
            lines.append("")

            # -- Full percentile-bin heatmap by citizenship --
            lines.append("### Full Percentile-Bin Heatmap by Citizenship (All Bins B1-B10)")
            lines.append("")
            lines.append(
                "Each row is one citizenship group; each column is one percentile bin. "
                "Values are row percentages."
            )
            lines.append("")
            _pc_hm = _pc_dec_pct.T
            _pc_hm.index.name = "Bin"
            _pc_hm = _pc_hm.reindex(index=BIN_ORDER[::-1])
            lines.append(_pc_hm.to_markdown(tablefmt="pipe", numalign="right"))
            lines.append("")
            lines.append("")

        # -- Top-bin share (B8-B10) by citizenship --
        lines.append("### Top-Bin Share (B8-B10) by Citizenship")
        lines.append("")
        if "PercentileBin" in _pc_base.columns:
            _pc_top_dec = (
                _pc_base
                .assign(_is_top=_pc_base["PercentileBin"].isin(["B8", "B9", "B10"]))
                .groupby("CITIZENSHIP_FINAL", observed=True)
                .agg(n=("_is_top", "size"), top_n=("_is_top", "sum"))
                .reset_index()
            )
            _pc_top_dec["top_dec_pct"] = (
                _pc_top_dec["top_n"] / _pc_top_dec["n"].replace(0, np.nan) * 100
            ).fillna(0).round(1)
            _pc_top_dec = _pc_top_dec[_pc_top_dec["n"] >= 3].sort_values("top_dec_pct", ascending=False)
            lines.append(fmt_df(_pc_top_dec, "Top-bin (B8-B10) share by citizenship (n >= 3)"))
            lines.append("")

        # -- Percentile rank by citizenship (n >= 5) --
        lines.append("### Percentile Rank by Citizenship (n >= 5)")
        lines.append("")
        if "NMS_PER_num" in _pc_base.columns:
            _pc_big = _pc_base.groupby("CITIZENSHIP_FINAL", observed=True).filter(
                lambda x: len(x) >= 5
            )
            if not _pc_big.empty:
                _pc_pct_stats = (
                    _pc_big
                    .groupby("CITIZENSHIP_FINAL", observed=True)["NMS_PER_num"]
                    .agg(n="count", mean="mean", std="std", min="min",
                         q25=lambda x: x.quantile(0.25), median="median",
                         q75=lambda x: x.quantile(0.75), max="max")
                    .round(2)
                    .reset_index()
                )
                lines.append(fmt_df(_pc_pct_stats, "Percentile rank statistics by citizenship (n >= 5)"))
                lines.append("")

        # -- TRUE raw score by citizenship (n >= 5) --
        lines.append("### TRUE Raw Score by Citizenship (n >= 5)")
        lines.append("")
        if "TotalRawScoreTRUE" in _pc_base.columns:
            _pc_big_raw = _pc_base.groupby("CITIZENSHIP_FINAL", observed=True).filter(
                lambda x: len(x) >= 5
            )
            if not _pc_big_raw.empty:
                _pc_raw_stats = (
                    _pc_big_raw
                    .groupby("CITIZENSHIP_FINAL", observed=True)["TotalRawScoreTRUE"]
                    .agg(n="count", mean="mean", std="std", min="min",
                         q25=lambda x: x.quantile(0.25), median="median",
                         q75=lambda x: x.quantile(0.75), max="max")
                    .round(2)
                    .reset_index()
                )
                lines.append(fmt_df(_pc_raw_stats, "TRUE raw score statistics by citizenship (n >= 5)"))
                lines.append("")

        # -- Summary by citizenship --
        lines.append("### Summary by Citizenship")
        lines.append("")
        _pc_base["_is_top_d"] = (
            _pc_base["PercentileBin"].isin(["B8", "B9", "B10"])
            if "PercentileBin" in _pc_base.columns else False
        )
        _pc_base["_is_bot_d"] = (
            _pc_base["PercentileBin"].isin(["B1", "B2", "B3"])
            if "PercentileBin" in _pc_base.columns else False
        )
        _pc_summary = (
            _pc_base
            .groupby("CITIZENSHIP_FINAL", observed=True)
            .agg(
                n_examinees=("APPNO_CLEAN", "count"),
                median_percentile_rank=("NMS_PER_num", "median"),
                median_true_raw_score=("TotalRawScoreTRUE", "median"),
                top_decile_n=("_is_top_d", "sum"),
                bottom_decile_n=("_is_bot_d", "sum"),
            )
            .round(2)
            .reset_index()
        )
        _pc_summary["top_decile_pct"] = (
            _pc_summary["top_decile_n"] / _pc_summary["n_examinees"].replace(0, np.nan) * 100
        ).fillna(0).round(2)
        _pc_summary["bottom_decile_pct"] = (
            _pc_summary["bottom_decile_n"] / _pc_summary["n_examinees"].replace(0, np.nan) * 100
        ).fillna(0).round(2)
        _pc_summary["top_decile_n"] = _pc_summary["top_decile_n"].astype(int)
        _pc_summary["bottom_decile_n"] = _pc_summary["bottom_decile_n"].astype(int)
        _pc_summary = _pc_summary[
            ["CITIZENSHIP_FINAL", "n_examinees", "median_percentile_rank",
             "median_true_raw_score", "top_decile_n", "top_decile_pct",
             "bottom_decile_n", "bottom_decile_pct"]
        ].sort_values(["n_examinees", "median_percentile_rank"], ascending=[False, False])
        lines.append(fmt_df(_pc_summary, "Summary statistics by citizenship"))
        lines.append("")

        # -- By citizenship and UNI_TYPE --
        lines.append("### Summary by Citizenship and University Type")
        lines.append("")
        if "UNI_TYPE" in _pc_base.columns:
            _pc_uni_sum = (
                _pc_base
                .groupby(["CITIZENSHIP_FINAL", "UNI_TYPE"], observed=True)
                .agg(
                    n=("APPNO_CLEAN", "count"),
                    median_percentile_rank=("NMS_PER_num", "median"),
                    median_true_raw_score=("TotalRawScoreTRUE", "median"),
                )
                .round(2)
                .reset_index()
            )
            lines.append(fmt_df(_pc_uni_sum, "By citizenship and university type"))
            lines.append("")

        # -- By citizenship and CourseGroup --
        lines.append("### Summary by Citizenship and Course Group")
        lines.append("")
        if "CourseGroup" in _pc_base.columns:
            _pc_course_sum = (
                _pc_base
                .groupby(["CITIZENSHIP_FINAL", "CourseGroup"], observed=True)
                .agg(
                    n=("APPNO_CLEAN", "count"),
                    median_percentile_rank=("NMS_PER_num", "median"),
                    median_true_raw_score=("TotalRawScoreTRUE", "median"),
                )
                .round(2)
                .reset_index()
            )
            lines.append(fmt_df(_pc_course_sum, "By citizenship and course group"))
            lines.append("")

        # -- Year distribution by citizenship --
        lines.append("### Year Distribution by Citizenship")
        lines.append("")
        if "Year" in _pc_base.columns:
            _pc_year_tbl = (
                _pc_base
                .groupby(["CITIZENSHIP_FINAL", "Year"], observed=True)
                .size()
                .unstack(fill_value=0)
            )
            _pc_year_tbl.index.name = "CITIZENSHIP_FINAL"
            _pc_year_tbl_out = _pc_year_tbl.reset_index()
            lines.append(fmt_df(_pc_year_tbl_out, "Year distribution by citizenship (counts)"))
            lines.append("")

    return "\n".join(lines)


def save(md):
    out_dir = Path("page_results")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "04_score_bins.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    md = run()
    save(md)
    print(f"Output length: {len(md)} chars")
    # Print first 300 chars as preview
    print("--- PREVIEW (first 300 chars) ---")
    print(md[:300])
