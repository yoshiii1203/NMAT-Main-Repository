"""
Page 05 — University Type Analysis
====================================
Output: page_results/05_university_type.md

Analyses:
  1. UNI_TYPE distribution by UNI_LOCATION (matrix and counts)
  2. Bin distribution by UNI_TYPE (counts and percentages)
  3. Top bin share (B8-B10) by UNI_TYPE
  4. Foreign examinee summary (by FOREIGNER_STATUS and UNI_TYPE)
  5. Descriptive statistics by UNI_TYPE (n, median %ile, median raw, etc.)
  6. Kruskal-Wallis test: UNI_TYPE x NMS_PER_num

Data subset: "uni" (besttrend with UNI_TYPE in [Public, Private, Foreign])
Filters: None (full unfiltered dataset)
"""
import sys
sys.path.append("data_aggregator")

import numpy as np
import pandas as pd
from scipy import stats as sp_stats
from itertools import combinations

from config import BIN_ORDER, SUBTEST_STD, SUBTEST_RAW
from helpers import write_header, write_dataframe, pct_table

MD_PATH = "page_results/05_university_type.md"


def load_uni_data():
    """Load only the 'uni' subset directly (avoids load_data memory overhead)."""
    import pyarrow.parquet as pq
    table = pq.read_table("dataset/NMAT_Exodus.parquet")
    df = table.to_pandas()
    # Free table
    del table

    # Compute derived columns
    if "Year" in df.columns:
        df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")

    # Filter: IS_BEST_NMAT_RECORD == True, Year 2006-2018, UNI_TYPE in Public/Private/Foreign
    mask = (
        (df.get("IS_BEST_NMAT_RECORD", pd.Series([True] * len(df))) == True)
        & (df["Year"].between(2006, 2018, inclusive="both"))
        & (df["UNI_TYPE"].isin(["Public", "Private", "Foreign"]))
    )
    uni = df.loc[mask].copy()
    # Drop full dataframe
    del df

    return uni


def descriptive_stats(uni_base):
    """Descriptive statistics by UNI_TYPE."""
    stats_list = []
    # Each entry: (label, column, agg_func)
    score_cols = [
        ("Median Percentile", "NMS_PER_num", "median"),
        ("Mean Percentile", "NMS_PER_num", "mean"),
        ("Std Percentile", "NMS_PER_num", "std"),
        ("Median Raw Total", "TotalRawScoreTRUE", "median"),
        ("Mean Raw Total", "TotalRawScoreTRUE", "mean"),
        ("Std Raw Total", "TotalRawScoreTRUE", "std"),
        ("Median GPS", "NMS_GPS", "median"),
        ("Median APT", "NMS_APT", "median"),
        ("Median SA", "NMS_SA", "median"),
        ("Q25 Percentile", "NMS_PER_num", lambda x: x.quantile(0.25)),
        ("Q75 Percentile", "NMS_PER_num", lambda x: x.quantile(0.75)),
        ("Q25 Raw Total", "TotalRawScoreTRUE", lambda x: x.quantile(0.25)),
        ("Q75 Raw Total", "TotalRawScoreTRUE", lambda x: x.quantile(0.75)),
    ]

    for uni_type in ["Public", "Private", "Foreign"]:
        subset = uni_base[uni_base["UNI_TYPE"] == uni_type]
        row = {"UNI_TYPE": uni_type, "N": len(subset)}
        for label, col, agg_fn in score_cols:
            vals = subset[col].dropna()
            if len(vals) == 0:
                row[label] = np.nan
            else:
                if callable(agg_fn):
                    row[label] = round(agg_fn(vals), 2)
                else:
                    row[label] = round(getattr(vals, agg_fn)(), 2)
        stats_list.append(row)

    return pd.DataFrame(stats_list)


def kruskal_uni_type(uni_base):
    """Kruskal-Wallis test: UNI_TYPE x NMS_PER_num."""
    groups = [g for g in ["Public", "Private", "Foreign"] if g in uni_base["UNI_TYPE"].unique()]
    data = {g: uni_base[uni_base["UNI_TYPE"] == g]["NMS_PER_num"].dropna().values for g in groups}
    valid = {k: v for k, v in data.items() if len(v) >= 5}

    results = {}
    if len(valid) >= 2:
        h_stat, p_val = sp_stats.kruskal(*valid.values())
        n_total = sum(len(v) for v in valid.values())
        k = len(valid)
        eta2 = (h_stat - k + 1) / (n_total - k) if n_total > k else 0

        if eta2 < 0.01:
            effect = "Negligible"
        elif eta2 < 0.06:
            effect = "Small"
        elif eta2 < 0.14:
            effect = "Medium"
        else:
            effect = "Large"

        posthoc = []
        for g1, g2 in combinations(valid.keys(), 2):
            u_stat, p = sp_stats.mannwhitneyu(valid[g1], valid[g2], alternative="two-sided")
            n1, n2 = len(valid[g1]), len(valid[g2])
            r = 1 - (2 * u_stat) / (n1 * n2)
            posthoc.append({
                "Group 1": g1,
                "Group 2": g2,
                "U-statistic": round(u_stat, 2),
                "p-value": p,
                "Effect size (r)": round(r, 4),
                "N1": n1,
                "N2": n2,
            })

        results = {
            "test": {
                "Score Variable": "NMS_PER_num (Percentile Rank)",
                "H-statistic": round(h_stat, 4),
                "p-value": p_val,
                "Eta-squared": round(max(0, eta2), 4),
                "Effect Size": effect,
                "Groups compared": len(valid),
                "Total N": n_total,
            },
            "posthoc": pd.DataFrame(posthoc),
        }

    return results


def foreign_summary(uni_base):
    """Foreign examinee summary by FOREIGNER_STATUS and UNI_TYPE."""
    foreign = uni_base[uni_base["UNI_TYPE"] == "Foreign"].copy()

    f_status = (
        foreign.groupby("FOREIGNER_STATUS", observed=True)
        .agg(
            N=("APPNO_CLEAN", "count"),
            Median_Percentile=("NMS_PER_num", "median"),
            Median_Raw=("TotalRawScoreTRUE", "median"),
            Top_Bin_Rate=("PercentileBin", lambda x: x.isin(["B8", "B9", "B10"]).mean()),
        )
        .reset_index()
    )
    f_status.columns = ["FOREIGNER_STATUS", "N", "Median Percentile", "Median Raw Total",
                         "Top Bin (B8-B10) Rate"]
    f_status["Top Bin (B8-B10) Rate"] = (f_status["Top Bin (B8-B10) Rate"] * 100).round(2)

    f_status_all = (
        uni_base.groupby(["UNI_TYPE", "FOREIGNER_STATUS"], observed=True)
        .agg(
            N=("APPNO_CLEAN", "count"),
            Median_Percentile=("NMS_PER_num", "median"),
            Median_Raw=("TotalRawScoreTRUE", "median"),
        )
        .reset_index()
    )
    f_status_all.columns = ["UNI_TYPE", "FOREIGNER_STATUS", "N", "Median Percentile",
                            "Median Raw Total"]
    f_status_all["Median Percentile"] = f_status_all["Median Percentile"].round(1)
    f_status_all["Median Raw Total"] = f_status_all["Median Raw Total"].round(1)

    return f_status, f_status_all


def kruskal_subtests(uni_base):
    """Kruskal-Wallis tests for each standard subtest by UNI_TYPE."""
    results = []
    for label, col in SUBTEST_STD.items():
        groups = {}
        for ut in ["Public", "Private", "Foreign"]:
            vals = uni_base[uni_base["UNI_TYPE"] == ut][col].dropna().values
            if len(vals) >= 5:
                groups[ut] = vals
        if len(groups) >= 2:
            h, p = sp_stats.kruskal(*groups.values())
            n_total = sum(len(v) for v in groups.values())
            k = len(groups)
            eta2 = (h - k + 1) / (n_total - k) if n_total > k else 0
            results.append({
                "Subtest": label,
                "H-statistic": round(h, 4),
                "p-value": p,
                "Eta-squared": round(max(0, eta2), 4),
                "Groups": k,
                "Total N": n_total,
            })
    return pd.DataFrame(results)


def run():
    print("Loading uni data...")
    uni_base = load_uni_data()
    uni_base = uni_base.dropna(subset=["UNI_TYPE", "UNI_LOCATION", "PercentileBin"]).copy()
    print(f"  Records: {len(uni_base):,}")

    with open(MD_PATH, "w", encoding="utf-8") as f:
        write_header(f, "University Type Analysis (Page 05)", "uni", 5)
        f.write("**Subset:** besttrend filtered to UNI_TYPE in [Public, Private, Foreign]\n\n")
        f.write(f"**Total records:** {len(uni_base):,}\n\n")
        f.write("---\n\n")

        # ── 1. UNI_TYPE distribution by UNI_LOCATION ──
        f.write("## 1. UNI_TYPE Distribution by UNI_LOCATION\n\n")

        f.write("### 1a. Institution type by location mix\n\n")
        type_loc = (
            uni_base.groupby(["UNI_TYPE", "UNI_LOCATION"], observed=True)
            .size()
            .reset_index(name="Count")
        )
        type_loc["Percent of Total"] = (type_loc["Count"] / type_loc["Count"].sum() * 100).round(2)
        type_loc = type_loc.sort_values(["UNI_TYPE", "UNI_LOCATION"]).reset_index(drop=True)
        write_dataframe(f, type_loc, "Table 05-1. Institution type by location mix")

        f.write("### 1b. Count matrix with margins\n\n")
        inst_count = pd.crosstab(uni_base["UNI_TYPE"], uni_base["UNI_LOCATION"], margins=True)
        write_dataframe(
            f, inst_count.reset_index(),
            "Table 05-2. UNI_TYPE x UNI_LOCATION count matrix (with totals)"
        )

        f.write("### 1c. Row percentages (within UNI_TYPE)\n\n")
        inst_pct_row = (pd.crosstab(uni_base["UNI_TYPE"], uni_base["UNI_LOCATION"],
                                    normalize="index") * 100).round(2)
        write_dataframe(
            f, inst_pct_row.reset_index(),
            "Table 05-3. Row percentages: within UNI_TYPE"
        )

        f.write("### 1d. Column percentages (within UNI_LOCATION)\n\n")
        inst_pct_col = (pd.crosstab(uni_base["UNI_TYPE"], uni_base["UNI_LOCATION"],
                                    normalize="columns") * 100).round(2)
        write_dataframe(
            f, inst_pct_col.reset_index(),
            "Table 05-4. Column percentages: within UNI_LOCATION"
        )

        f.write("---\n\n")

        # ── 2. Bin distribution by UNI_TYPE ──
        f.write("## 2. Bin Distribution by UNI_TYPE\n\n")

        uni_decile_count, uni_decile_pct = pct_table(uni_base, "UNI_TYPE", "PercentileBin",
                                                     BIN_ORDER)

        f.write("### 2a. Bin counts by UNI_TYPE\n\n")
        summary = uni_decile_count.copy()
        summary["Total"] = summary.sum(axis=1)
        write_dataframe(
            f, summary.reset_index(),
            "Table 05-5. Bin counts by university type"
        )

        f.write("### 2b. Bin percentages by UNI_TYPE\n\n")
        write_dataframe(
            f, uni_decile_pct.reset_index(),
            "Table 05-6. Row percentages (within UNI_TYPE) across percentile bins"
        )

        f.write("---\n\n")

        # ── 3. Top bin share (B8-B10) by UNI_TYPE ──
        f.write("## 3. Top Bin Share (B8-B10) by UNI_TYPE\n\n")

        top_share = (
            uni_base.groupby("UNI_TYPE", observed=True)
            .apply(
                lambda g: pd.Series({
                    "Total N": len(g),
                    "Top Bin (B8-B10) Count": g["PercentileBin"].isin(["B8", "B9", "B10"]).sum(),
                    "Top Bin Share (%)": round(
                        g["PercentileBin"].isin(["B8", "B9", "B10"]).mean() * 100, 2
                    ),
                }),
                include_groups=False,
            )
            .reset_index()
        )
        write_dataframe(f, top_share, "Table 05-7. Top bin (B8-B10) share by university type")

        f.write("### 3b. Top bin share by UNI_TYPE x UNI_LOCATION\n\n")
        inst_top = (
            uni_base.groupby(["UNI_TYPE", "UNI_LOCATION"], observed=True)
            .apply(
                lambda g: pd.Series({
                    "Total N": len(g),
                    "Top Bin Count": g["PercentileBin"].isin(["B8", "B9", "B10"]).sum(),
                    "Top Bin Share (%)": round(
                        g["PercentileBin"].isin(["B8", "B9", "B10"]).mean() * 100, 2
                    ),
                }),
                include_groups=False,
            )
            .reset_index()
        )
        write_dataframe(
            f, inst_top,
            "Table 05-8. Top bin (B8-B10) share by institution type x location"
        )

        f.write("---\n\n")

        # ── 4. Foreign examinee summary ──
        f.write("## 4. Foreign Examinee Summary\n\n")

        f.write("### 4a. Foreign examinee overview (UNI_TYPE = Foreign)\n\n")
        foreign = uni_base[uni_base["UNI_TYPE"].eq("Foreign")].copy()
        f.write(f"- **Foreign examinees (besttrend):** {len(foreign):,}\n")
        f.write(f"- **Percent of total (uni subset):** "
                f"{(len(foreign) / max(len(uni_base), 1) * 100):.2f}%\n")
        f.write(f"- **Median percentile:** "
                f"{foreign['NMS_PER_num'].median():.1f}\n")
        f.write(f"- **Top bin share (B8-B10):** "
                f"{(foreign['PercentileBin'].isin(['B8','B9','B10']).mean() * 100):.2f}%\n\n")

        f.write("### 4b. Foreign examinees by FOREIGNER_STATUS\n\n")
        f_status, f_status_all = foreign_summary(uni_base)
        write_dataframe(
            f, f_status,
            "Table 05-9. Foreign examinee summary by FOREIGNER_STATUS"
        )

        f.write("### 4c. FOREIGNER_STATUS x UNI_TYPE cross-tabulation\n\n")
        write_dataframe(
            f, f_status_all,
            "Table 05-10. FOREIGNER_STATUS by UNI_TYPE (all types)"
        )

        foreign_decile_count, foreign_decile_pct = pct_table(
            foreign, "FOREIGNER_STATUS", "PercentileBin", BIN_ORDER
        )
        write_dataframe(
            f, foreign_decile_pct.reset_index(),
            "Table 05-11. Bin distribution among foreign examinees by FOREIGNER_STATUS"
        )

        f.write("---\n\n")

        # ── 5. Descriptive stats by UNI_TYPE ──
        f.write("## 5. Descriptive Statistics by UNI_TYPE\n\n")

        stats_df = descriptive_stats(uni_base)
        write_dataframe(
            f, stats_df,
            "Table 05-12. Descriptive statistics by university type"
        )

        # Subtest standard scores by UNI_TYPE
        f.write("### 5b. Median standard subtest scores by UNI_TYPE\n\n")
        subtest_rows = []
        for label, col in SUBTEST_STD.items():
            row = {"Subtest": label}
            for ut in ["Public", "Private", "Foreign"]:
                vals = uni_base[uni_base["UNI_TYPE"] == ut][col].dropna()
                row[f"{ut} (n={len(vals):,})"] = round(vals.median(), 2) if len(vals) > 0 else np.nan
            subtest_rows.append(row)
        subtest_df = pd.DataFrame(subtest_rows)
        write_dataframe(
            f, subtest_df,
            "Table 05-13. Median standard subtest scores by university type"
        )

        f.write("### 5c. Median raw subtest scores by UNI_TYPE\n\n")
        raw_rows = []
        for label, col in SUBTEST_RAW.items():
            row = {"Subtest": label}
            for ut in ["Public", "Private", "Foreign"]:
                vals = uni_base[uni_base["UNI_TYPE"] == ut][col].dropna()
                row[f"{ut} (n={len(vals):,})"] = round(vals.median(), 2) if len(vals) > 0 else np.nan
            raw_rows.append(row)
        raw_df = pd.DataFrame(raw_rows)
        write_dataframe(
            f, raw_df,
            "Table 05-14. Median raw subtest scores by university type"
        )

        f.write("---\n\n")

        # ── 6. Kruskal-Wallis: UNI_TYPE x NMS_PER_num ──
        f.write("## 6. Kruskal-Wallis Test: UNI_TYPE x NMS_PER_num\n\n")

        kw_result = kruskal_uni_type(uni_base)
        if kw_result:
            test_row = kw_result["test"]
            f.write("### 6a. Omnibus test\n\n")
            kw_df = pd.DataFrame([test_row])
            write_dataframe(f, kw_df, "Table 05-15. Kruskal-Wallis test result")

            f.write("### 6b. Post-hoc pairwise comparisons (Mann-Whitney U)\n\n")
            if not kw_result["posthoc"].empty:
                write_dataframe(
                    f, kw_result["posthoc"],
                    "Table 05-16. Post-hoc Mann-Whitney U pairwise comparisons"
                )
        else:
            f.write("*Insufficient data for Kruskal-Wallis test.*\n\n")

        # Additional KW tests for subtest scores
        f.write("### 6c. Kruskal-Wallis by subtest (standard scores)\n\n")
        kw_subtests_df = kruskal_subtests(uni_base)
        if not kw_subtests_df.empty:
            write_dataframe(
                f, kw_subtests_df,
                "Table 05-17. Kruskal-Wallis tests by subtest (standard scores)"
            )

        f.write("\n---\n")
        f.write("*Analysis complete. Generated by page_05_university_type.py*\n")

    print(f"[OK] Page 05 written to {MD_PATH}")


def save():
    """Alias for run()."""
    run()


if __name__ == "__main__":
    run()
