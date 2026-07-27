"""
page_07_ple_alignment.py — PLE Alignment of NMAT Performance (Pages 7-8)

Produces: page_results/07_ple_alignment.md

Score profile by PLE status, box-plot data, Mann-Whitney U tests, bin pass rates,
stacked-bar composition, survival to top bins, alignment tables by year/course/uni,
and top-percentile record-level summary.

Uses the observable best-record cohort for PLE-linked analyses.
"""
import sys
import os
import numpy as np
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import BIN_ORDER, PLE_ORDER, RESULTS_DIR
from helpers import (
    load_data, write_header, write_dataframe, pct_table,
    mannwhitney_table,
)


def run():
    """Execute all analyses and return a dict of results DataFrames and strings."""
    _, subsets = load_data()

    # Observable best-record cohort for PLE analyses
    obs = subsets["bestobservable"].copy()
    # Full best-trend cohort for survival analysis (broader CourseGroup coverage)
    trend = subsets["besttrend"].copy()

    results = {}

    # ----------------------------------------------------------------
    # 1. Score profile by PLE status
    # ----------------------------------------------------------------
    desc_cols = [
        "TotalRawScoreTRUE", "NMS_PER_num", "NMS_GPS",
        "PartIRawScoreTRUE", "PartIIRawScoreTRUE",
    ]
    desc_cols = [c for c in desc_cols if c in obs.columns]

    def q25(x):
        return x.quantile(0.25)

    def q75(x):
        return x.quantile(0.75)

    profile = (
        obs.groupby("PLE_STATUS_LABEL", observed=True)[desc_cols]
        .agg(["count", "median", "mean", q25, q75])
        .round(2)
    )
    # Flatten MultiIndex columns for clean markdown output
    profile.columns = [f"{col[0]}_{col[1]}" for col in profile.columns]
    profile = profile.reset_index()
    results["score_profile"] = profile

    # ----------------------------------------------------------------
    # 2. Box-plot data (per-score quantiles by PLE status)
    # ----------------------------------------------------------------
    box_records = []
    for col in desc_cols:
        for label, grp in obs.groupby("PLE_STATUS_LABEL", observed=True):
            vals = grp[col].dropna()
            if len(vals) == 0:
                continue
            stats = vals.describe(percentiles=[0.05, 0.25, 0.50, 0.75, 0.95])
            box_records.append({
                "ScoreVariable": col,
                "PLE_STATUS_LABEL": label,
                "n": int(stats["count"]),
                "min": round(float(stats["min"]), 2),
                "q05": round(float(stats["5%"]), 2),
                "q25": round(float(stats["25%"]), 2),
                "median": round(float(stats["50%"]), 2),
                "mean": round(float(stats["mean"]), 2),
                "q75": round(float(stats["75%"]), 2),
                "q95": round(float(stats["95%"]), 2),
                "max": round(float(stats["max"]), 2),
                "std": round(float(stats["std"]), 2),
            })
    results["boxplot_data"] = pd.DataFrame(box_records)

    # ----------------------------------------------------------------
    # 3. Mann-Whitney U tests
    # ----------------------------------------------------------------
    mw_dict = {
        "Total Raw Score": "TotalRawScoreTRUE",
        "Percentile Rank": "NMS_PER_num",
        "GPS Standard Score": "NMS_GPS",
        "Part I Raw Score": "PartIRawScoreTRUE",
        "Part II Raw Score": "PartIIRawScoreTRUE",
    }
    mw_df = mannwhitney_table(obs, "PLE_STATUS_LABEL", mw_dict)
    results["mannwhitney"] = mw_df

    # ----------------------------------------------------------------
    # 4. PLE pass rate by PercentileBin
    # ----------------------------------------------------------------
    bin_ple = (
        obs.dropna(subset=["PercentileBin", "PLE_STATUS_LABEL"])
        .groupby("PercentileBin", observed=True)
        .agg(
            n=("PLE_STATUS_LABEL", "size"),
            confirmed_passers=("HAS_CONFIRMED_PLE", "sum"),
            pass_rate_pct=("HAS_CONFIRMED_PLE", lambda x: round(x.mean() * 100, 2)),
        )
        .reindex(BIN_ORDER)
        .reset_index()
    )
    bin_ple.columns = ["PercentileBin", "n", "confirmed_passers", "pass_rate_pct"]
    bin_ple["confirmed_passers"] = bin_ple["confirmed_passers"].astype(int)
    results["bin_pass_rate"] = bin_ple

    # ----------------------------------------------------------------
    # 5. Stacked bar data — bin composition by PLE status
    #    a) Within-bin: PLE status distribution per bin
    #    b) Within-PLE-status: bin distribution per PLE status
    # ----------------------------------------------------------------
    # 5a) Within-bin PLE composition (row-wise: each bin sums to 100%)
    comp = (
        obs.dropna(subset=["PercentileBin", "PLE_STATUS_LABEL"])
        .groupby(["PercentileBin", "PLE_STATUS_LABEL"], observed=True)
        .size()
        .unstack(fill_value=0)
        .reindex(index=BIN_ORDER, columns=PLE_ORDER, fill_value=0)
    )
    comp_pct = comp.div(comp.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)
    comp_pct.index.name = "PercentileBin"
    results["bin_composition_pct"] = comp_pct

    # 5b) Within-PLE-status bin distribution (column-wise: each PLE status sums to 100%)
    status_dist = (
        obs.dropna(subset=["PercentileBin", "PLE_STATUS_LABEL"])
        .groupby(["PLE_STATUS_LABEL", "PercentileBin"], observed=True)
        .size()
        .unstack(fill_value=0)
        .reindex(columns=BIN_ORDER, fill_value=0)
    )
    status_dist_pct = status_dist.div(status_dist.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)
    status_dist_pct.index.name = "PLE_STATUS_LABEL"
    results["status_distribution_pct"] = status_dist_pct

    # ----------------------------------------------------------------
    # 6. Survival rate to top bins (B8-B10) by CourseGroup
    # ----------------------------------------------------------------
    surv_base = trend.dropna(subset=["CourseGroup", "PercentileBin"]).copy()
    surv_base["IS_TOP_BIN"] = surv_base["PercentileBin"].isin(["B8", "B9", "B10"])
    survival = (
        surv_base.groupby("CourseGroup", observed=True)
        .agg(
            total_examinees=("IS_TOP_BIN", "size"),
            top_bin_n=("IS_TOP_BIN", "sum"),
        )
        .reset_index()
    )
    survival["top_bin_n"] = survival["top_bin_n"].astype(int)
    survival["survival_rate_pct"] = (
        survival["top_bin_n"] / survival["total_examinees"] * 100
    ).round(2)
    survival = survival.sort_values(
        ["survival_rate_pct", "top_bin_n"], ascending=[False, False]
    ).reset_index(drop=True)
    results["survival_by_course"] = survival

    # ----------------------------------------------------------------
    # 7. PLE alignment by year
    # ----------------------------------------------------------------
    pol_base = obs.copy()
    align_year = (
        pol_base.groupby("Year", observed=True)
        .apply(lambda x: pd.Series({
            "n_observable_best_records": len(x),
            "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
            "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
            "confirmed_ple_share_pct": round(
                (x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2
            ),
        }), include_groups=False)
        .reset_index()
        .sort_values("Year")
    )
    # Ensure Year is int for clean display
    align_year["Year"] = align_year["Year"].astype(int)
    results["align_year"] = align_year

    # ----------------------------------------------------------------
    # 8. PLE alignment by course group
    # ----------------------------------------------------------------
    align_course = (
        pol_base.groupby("CourseGroup", observed=True)
        .apply(lambda x: pd.Series({
            "n_observable_best_records": len(x),
            "confirmed_ple_passers": int((x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").sum()),
            "no_confirmed_ple_match": int((x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()),
            "confirmed_ple_share_pct": round(
                (x["PLE_STATUS_LABEL"] == "Confirmed PLE passer").mean() * 100, 2
            ),
            "median_percentile_rank": round(x["NMS_PER_num"].median(), 2),
        }), include_groups=False)
        .reset_index()
        .sort_values("confirmed_ple_share_pct", ascending=False)
    )
    results["align_course"] = align_course

    # ----------------------------------------------------------------
    # 9. PLE alignment by UNI_TYPE (Public, Private, Foreign only)
    # ----------------------------------------------------------------
    uni_sub = pol_base[pol_base["UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
    align_uni = (
        uni_sub.groupby("UNI_TYPE", observed=True)
        .apply(lambda x: pd.Series({
            "n_observable_best_records": len(x),
            "confirmed_ple_passers": int(x["HAS_CONFIRMED_PLE"].sum()),
            "no_confirmed_ple_match": int(
                (x["PLE_STATUS_LABEL"] == "No confirmed PLE match").sum()
            ),
            "confirmed_ple_share_pct": round(
                x["HAS_CONFIRMED_PLE"].mean() * 100, 2
            ),
        }), include_groups=False)
        .reset_index()
    )
    results["align_uni"] = align_uni

    # ----------------------------------------------------------------
    # 10. Record-level: top percentile scores per PLE status
    # ----------------------------------------------------------------
    record_cols = [
        "PERSON_KEY", "APPNO_CLEAN", "Year", "TotalRawScoreTRUE",
        "NMS_PER_num", "NMS_GPS", "PartIRawScoreTRUE", "PartIIRawScoreTRUE",
        "PercentileBin", "PLE_STATUS_LABEL", "UNI_TYPE", "CourseGroup",
    ]
    record_cols = [c for c in record_cols if c in obs.columns]

    # Top 20 percentile scores per PLE status (highest NMS_PER_num first)
    top_records = []
    for label in PLE_ORDER:
        sub = obs[obs["PLE_STATUS_LABEL"] == label].copy()
        if "NMS_PER_num" in sub.columns:
            sub = sub.sort_values("NMS_PER_num", ascending=False).head(20)
        elif "TotalRawScoreTRUE" in sub.columns:
            sub = sub.sort_values("TotalRawScoreTRUE", ascending=False).head(20)
        top_records.append(sub[record_cols])
    results["top_records"] = pd.concat(top_records, ignore_index=True) if top_records else pd.DataFrame()

    return results


def save(results):
    """Write all results to page_results/07_ple_alignment.md."""
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = RESULTS_DIR / "07_ple_alignment.md"

    with open(path, "w", encoding="utf-8") as f:
        write_header(f, "PLE Alignment of NMAT Performance", "bestobservable", 7)

        # --- 1. Score profile ---
        f.write("## 1. Score Profile by PLE Status\n\n")
        f.write("Count, median, mean, Q25, and Q75 for each score measure by PLE status.\n\n")
        write_dataframe(f, results["score_profile"], "Table 23. Score profile by PLE status")
        f.write("\n---\n\n")

        # --- 2. Box-plot data ---
        f.write("## 2. Box-Plot Data by Score and PLE Status\n\n")
        f.write("Quantile-based summary for each score variable, split by PLE status.\n\n")
        write_dataframe(f, results["boxplot_data"], "Box-plot summary statistics")
        f.write("\n---\n\n")

        # --- 3. Mann-Whitney U tests ---
        f.write("## 3. Mann-Whitney U Tests: Confirmed PLE Passer vs No Confirmed Match\n\n")
        if not results["mannwhitney"].empty:
            write_dataframe(f, results["mannwhitney"],
                            "Table 24. Mann-Whitney comparison")
        else:
            f.write("*No Mann-Whitney results available (requires exactly two PLE status groups).*\n\n")
        f.write("\n---\n\n")

        # --- 4. PLE pass rate by PercentileBin ---
        f.write("## 4. PLE Pass Rate by Percentile Bin\n\n")
        f.write("Within each percentile bin, the number of observable best records, "
                "confirmed PLE passers, and the pass rate (%).\n\n")
        write_dataframe(f, results["bin_pass_rate"],
                        "Figure 21. PLE confirmed share by percentile bin")
        f.write("\n---\n\n")

        # --- 5a. Bin composition by PLE status ---
        f.write("## 5a. Bin Composition by PLE Status (within-bin %)\n\n")
        f.write("Within each bin, the distribution of PLE statuses (row-wise percentages).\n\n")
        comp_display = results["bin_composition_pct"].reset_index()
        write_dataframe(f, comp_display,
                        "Percent distribution of PLE status within each bin")
        f.write("\n---\n\n")

        # --- 5b. PLE status distribution ---
        f.write("## 5b. PLE Status Distribution Across Bins (within-PLE-status %)\n\n")
        f.write("For each PLE status, the distribution across percentile bins (column-wise percentages).\n\n")
        stat_display = results["status_distribution_pct"].reset_index()
        write_dataframe(f, stat_display,
                        "Bin distribution by PLE status")
        f.write("\n---\n\n")

        # --- 6. Survival to top bins by course group ---
        f.write("## 6. Survival Rate to Top Bins (B8-B10) by Course Group\n\n")
        f.write("Share of examinees in each course group who scored in the top three percentile bins.\n\n")
        write_dataframe(f, results["survival_by_course"],
                        "Table 26. Course-group representation in top bins")
        f.write("\n---\n\n")

        # --- 7. PLE alignment by year ---
        f.write("## 7. Confirmed PLE Alignment by NMAT Year\n\n")
        f.write("Observable best records, confirmed passers, no match, and confirmed share by year.\n\n")
        write_dataframe(f, results["align_year"],
                        "Table 28. Confirmed PLE alignment by NMAT year")
        f.write("\n---\n\n")

        # --- 8. PLE alignment by course group ---
        f.write("## 8. Confirmed PLE Alignment by Pre-Med Background\n\n")
        f.write("Observable best records, confirmed passers, no match, confirmed share, "
                "and median percentile rank by course group.\n\n")
        write_dataframe(f, results["align_course"],
                        "Table 29. Confirmed PLE alignment by course group")
        f.write("\n---\n\n")

        # --- 9. PLE alignment by UNI_TYPE ---
        f.write("## 9. Confirmed PLE Alignment by University Type\n\n")
        f.write("Public, Private, and Foreign university types in the observable best-record cohort.\n\n")
        write_dataframe(f, results["align_uni"],
                        "Table 27. Confirmed PLE alignment by university type")
        f.write("\n---\n\n")

        # --- 10. Record-level summary ---
        f.write("## 10. Top Percentile Scores by PLE Status\n\n")
        f.write("Top 20 records per PLE status, sorted by highest percentile rank.\n\n")
        if not results["top_records"].empty:
            write_dataframe(f, results["top_records"],
                            "Record-level detail: highest percentile scores per PLE status")
        else:
            f.write("*No matching records.*\n")

    print(f"[page_07] Written {path}")
    return path


if __name__ == "__main__":
    res = run()
    save(res)
