"""
page_08_repeat_takers.py — Repeat-Taker Patterns and Score Change (Pages 7-8)

Produces: page_results/08_repeat_takers.md

Attempt count distribution, repeat-taker summary, first-vs-last score improvement,
attempt counts by year, and detailed repeat-taker records.

Uses the full trend cohort (2006-2018, unfiltered).
"""
import sys
import os
import numpy as np
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import RESULTS_DIR
from helpers import load_data, write_header, write_dataframe


def run():
    """Execute all analyses and return a dict of results DataFrames."""
    dfall, subsets = load_data()

    # Full trend cohort for repeat-taker analysis (matches dashboard tab8)
    df = subsets["trend"].copy()

    results = {}

    # ----------------------------------------------------------------
    # 6. NMA_AppNo Deterministic Match Histories (P8-03)
    # Attempt histories exclusively for records matched deterministically via
    # application number, rather than exact name — dashboard.py tab8.
    # ----------------------------------------------------------------
    appno_matches = dfall[
        dfall["PLE_MATCH_METHOD"].isin(["MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"])
    ].copy()
    appno_cols = ["PERSON_KEY", "APPNO_CLEAN", "Year", "TotalRawScoreTRUE", "NMS_PER_num", "PLE_STATUS_LABEL"]
    appno_cols = [c for c in appno_cols if c in appno_matches.columns]
    if not appno_matches.empty:
        appno_matches = appno_matches[appno_cols].sort_values(["PERSON_KEY", "Year"]).reset_index(drop=True)
    results["appno_match_histories"] = appno_matches

    # ----------------------------------------------------------------
    # 1. Attempt count distribution
    # ----------------------------------------------------------------
    attempt_ct = (
        df.groupby("PERSON_KEY", observed=True)["APPNO_CLEAN"]
        .nunique()
        .reset_index(name="attempt_count")
    )
    attempt_summary = (
        attempt_ct["attempt_count"]
        .value_counts()
        .sort_index()
        .rename_axis("Attempts")
        .reset_index(name="Count")
    )
    attempt_summary["Percent"] = (
        attempt_summary["Count"] / attempt_summary["Count"].sum() * 100
    ).round(2)
    attempt_summary["CumulativePercent"] = (
        attempt_summary["Percent"].cumsum().round(2)
    )
    results["attempt_distribution"] = attempt_summary

    total_persons = len(attempt_ct)
    repeat_persons = attempt_ct[attempt_ct["attempt_count"] > 1]
    n_repeaters = len(repeat_persons)
    repeat_rate = round(n_repeaters / total_persons * 100, 2) if total_persons > 0 else 0.0

    results["total_persons"] = total_persons
    results["n_repeaters"] = n_repeaters
    results["repeat_rate"] = repeat_rate

    # ----------------------------------------------------------------
    # 2. Repeat-taker summary table
    # ----------------------------------------------------------------
    summary_rows = [
        {"Indicator": "Unique persons (PERSON_KEY)", "Value": total_persons},
        {"Indicator": "Repeat takers (>1 attempt)", "Value": n_repeaters},
        {"Indicator": "Repeat rate (%)", "Value": repeat_rate},
        {"Indicator": "Max attempts observed", "Value": int(attempt_ct["attempt_count"].max())},
        {"Indicator": "Mean attempts (all persons)", "Value": round(attempt_ct["attempt_count"].mean(), 2)},
        {"Indicator": "Median attempts (all persons)", "Value": int(attempt_ct["attempt_count"].median())},
    ]
    results["repeat_summary"] = pd.DataFrame(summary_rows)

    # ----------------------------------------------------------------
    # 3. Score improvement: first vs last attempt
    # ----------------------------------------------------------------
    repeat_person_keys = repeat_persons["PERSON_KEY"]
    repeat_df = df[df["PERSON_KEY"].isin(repeat_person_keys)].copy()

    if not repeat_df.empty:
        # Ensure sort stability
        sort_col = "YEAR_INT" if "YEAR_INT" in repeat_df.columns else "Year"
        repeat_df = repeat_df.sort_values(["PERSON_KEY", sort_col, "APPNO_CLEAN"])

        first_last = (
            repeat_df.groupby("PERSON_KEY", observed=True)
            .agg(
                first_year=(sort_col, "first"),
                last_year=(sort_col, "last"),
                first_pct=("NMS_PER_num", "first"),
                last_pct=("NMS_PER_num", "last"),
                first_raw=("TotalRawScoreTRUE", "first"),
                last_raw=("TotalRawScoreTRUE", "last"),
                first_gps=("NMS_GPS", "first"),
                last_gps=("NMS_GPS", "last"),
                n_attempts=("APPNO_CLEAN", "count"),
            )
            .reset_index()
        )

        # Drop rows missing key scores
        first_last = first_last.dropna(subset=["first_pct", "last_pct"]).copy()

        if not first_last.empty:
            first_last["pct_improvement"] = (
                first_last["last_pct"] - first_last["first_pct"]
            ).round(2)
            first_last["raw_improvement"] = (
                first_last["last_raw"] - first_last["first_raw"]
            ).round(2)
            first_last["gps_improvement"] = (
                first_last["last_gps"] - first_last["first_gps"]
            ).round(2)

            improvement_summary = pd.DataFrame({
                "Indicator": [
                    "Repeat-taker persons (analytic)",
                    "Improved percentile rank (%)",
                    "Improved raw score (%)",
                    "Improved GPS (%)",
                    "Median percentile change",
                    "Median raw score change",
                    "Median GPS change",
                    "Mean percentile change",
                    "Mean raw score change",
                    "Mean GPS change",
                    "Q25 percentile change",
                    "Q75 percentile change",
                    "Q25 raw score change",
                    "Q75 raw score change",
                ],
                "Value": [
                    int(len(first_last)),
                    round((first_last["pct_improvement"] > 0).mean() * 100, 2),
                    round((first_last["raw_improvement"] > 0).mean() * 100, 2),
                    round((first_last["gps_improvement"] > 0).mean() * 100, 2),
                    round(first_last["pct_improvement"].median(), 2),
                    round(first_last["raw_improvement"].median(), 2),
                    round(first_last["gps_improvement"].median(), 2),
                    round(first_last["pct_improvement"].mean(), 2),
                    round(first_last["raw_improvement"].mean(), 2),
                    round(first_last["gps_improvement"].mean(), 2),
                    round(first_last["pct_improvement"].quantile(0.25), 2),
                    round(first_last["pct_improvement"].quantile(0.75), 2),
                    round(first_last["raw_improvement"].quantile(0.25), 2),
                    round(first_last["raw_improvement"].quantile(0.75), 2),
                ],
            })
            results["improvement_summary"] = improvement_summary
            results["first_last"] = first_last
        else:
            results["improvement_summary"] = pd.DataFrame()
            results["first_last"] = pd.DataFrame()
    else:
        results["improvement_summary"] = pd.DataFrame()
        results["first_last"] = pd.DataFrame()

    # ----------------------------------------------------------------
    # 4. Distribution of attempt counts by year
    # ----------------------------------------------------------------
    attempt_by_year = (
        df.groupby(["PERSON_KEY", "Year"], observed=True)["APPNO_CLEAN"]
        .nunique()
        .reset_index(name="attempts_that_year")
    )
    attempt_year_dist = (
        attempt_by_year.groupby(["Year", "attempts_that_year"], observed=True)
        .size()
        .reset_index(name="person_count")
        .sort_values(["Year", "attempts_that_year"])
    )
    # Pivot for a cleaner table: years as rows, attempt-counts as columns
    attempt_year_pivot = attempt_year_dist.pivot_table(
        index="Year", columns="attempts_that_year", values="person_count",
        fill_value=0, aggfunc="sum"
    )
    attempt_year_pivot.columns = [f"{int(c)} attempt(s)" for c in attempt_year_pivot.columns]
    attempt_year_pivot["total_persons"] = attempt_year_pivot.sum(axis=1)
    attempt_year_pivot.index.name = "Year"
    attempt_year_pivot = attempt_year_pivot.reset_index()
    results["attempt_by_year"] = attempt_year_pivot

    # ----------------------------------------------------------------
    # 5. Detail: repeat takers with their scores (all attempts)
    # ----------------------------------------------------------------
    detail_cols = [
        "PERSON_KEY", "APPNO_CLEAN", "Year", "TotalRawScoreTRUE",
        "NMS_PER_num", "NMS_GPS", "PartIRawScoreTRUE", "PartIIRawScoreTRUE",
        "PercentileBin", "PLE_STATUS_LABEL", "UNDERGRAD_UNI_TYPE", "UNDERGRAD_COURSE_GROUP",
    ]
    detail_cols = [c for c in detail_cols if c in df.columns]

    if not repeat_df.empty:
        detail = repeat_df.sort_values(["PERSON_KEY", "Year", "APPNO_CLEAN"])[detail_cols].reset_index(drop=True)
        results["repeat_detail"] = detail
    else:
        results["repeat_detail"] = pd.DataFrame()

    return results


def save(results):
    """Write all results to page_results/08_repeat_takers.md."""
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = RESULTS_DIR / "08_repeat_takers.md"

    with open(path, "w", encoding="utf-8") as f:
        write_header(f, "Repeat-Taker Patterns and Score Change", "trend (2006-2018, unfiltered)", 8)

        # --- 1. Attempt count distribution ---
        f.write("## 1. Attempt Count Distribution\n\n")
        f.write("Number of unique NMAT applications per PERSON_KEY in the trend cohort.\n\n")
        write_dataframe(f, results["attempt_distribution"],
                        "Table 31. Attempt-count distribution")
        f.write("\nFigure data: each row shows the number of persons with that many "
                "recorded NMAT attempts.\n\n")
        f.write("\n---\n\n")

        # --- 2. Repeat-taker summary ---
        f.write("## 2. Repeat-Taker Summary\n\n")
        write_dataframe(f, results["repeat_summary"],
                        "Repeat-taker overview")
        f.write("\n---\n\n")

        # --- 3. Score improvement ---
        f.write("## 3. Score Improvement: First vs Last Attempt\n\n")
        f.write("Among repeat takers with score data on both first and last attempt.\n\n")
        if not results["improvement_summary"].empty:
            write_dataframe(f, results["improvement_summary"],
                            "Table 32. Repeat-taker trajectory summary")

            f.write("\n\n### First-Last Detail (per person)\n\n")
            fl_cols = [
                "PERSON_KEY", "n_attempts",
                "first_year", "last_year",
                "first_pct", "last_pct", "pct_improvement",
                "first_raw", "last_raw", "raw_improvement",
                "first_gps", "last_gps", "gps_improvement",
            ]
            fl_cols = [c for c in fl_cols if c in results["first_last"].columns]
            fl_display = results["first_last"][fl_cols].sort_values(
                ["pct_improvement", "raw_improvement"], ascending=False
            )
            # P8-01: this used to dump all ~33.7k person-rows inline (8.7 MB file).
            # Cap the inline preview and offload the full table to CSV, mirroring the
            # pattern Section 5 already uses below.
            fl_preview = fl_display.head(100)
            f.write(f"**Preview: first 100 of {len(fl_display):,} rows "
                    f"(population: repeat takers with score data on both first and "
                    f"last attempt, n={len(fl_display):,})**\n\n")
            f.write(fl_preview.to_markdown(index=False, tablefmt="pipe", numalign="right"))
            f.write("\n\n")
            fl_csv_path = RESULTS_DIR / "08_first_last_detail.csv"
            fl_display.to_csv(fl_csv_path, index=False)
            f.write(f"> Full detail: [{fl_csv_path.name}]({fl_csv_path.name}) "
                    f"({len(fl_display):,} rows, {len(fl_display.columns)} cols)\n\n")
        else:
            f.write("*No repeat-taker data available for first-last comparison.*\n")
        f.write("\n---\n\n")

        # --- 4. Attempt counts by year ---
        f.write("## 4. Distribution of Attempt Counts by Year\n\n")
        f.write("For each test year, the number of persons with 1, 2, 3, ... attempts "
                "in that year.\n\n")
        write_dataframe(f, results["attempt_by_year"],
                        "Attempt counts per year")
        f.write("\n---\n\n")

        # --- 5. Repeat-taker detail ---
        f.write("## 5. Repeat-Taker Detail (All Attempts)\n\n")
        f.write("All recorded attempts for persons with more than one NMAT application.\n\n")
        if not results["repeat_detail"].empty:
            preview = results["repeat_detail"].head(100)
            f.write("**Preview: first 100 rows**\n\n")
            f.write(preview.to_markdown(index=False, tablefmt="pipe", numalign="right"))
            f.write("\n\n")
            csv_path = RESULTS_DIR / "08_repeat_takers_detail.csv"
            results["repeat_detail"].to_csv(csv_path, index=False)
            f.write(f"> Full detail: [{csv_path.name}]({csv_path.name}) "
                    f"({len(results['repeat_detail']):,} rows, {len(results['repeat_detail'].columns)} cols)\n\n")
        else:
            f.write("*No repeat-taker records found.*\n")
        f.write("\n---\n\n")

        # --- 6. NMA_AppNo deterministic match histories (P8-03) ---
        f.write("## 6. NMA_AppNo Deterministic Match Histories\n\n")
        f.write("Attempt histories exclusively for records matched deterministically via "
                "application number (PLE_MATCH_METHOD in MANUAL_APPNO_MATCH, "
                "DETERMINISTIC_APPNO), rather than by exact name.\n\n")
        appno_df = results["appno_match_histories"]
        if not appno_df.empty:
            f.write(f"**population: all NMAT rows | n={len(appno_df):,}**\n\n")
            appno_preview = appno_df.head(100)
            f.write(appno_preview.to_markdown(index=False, tablefmt="pipe", numalign="right"))
            f.write("\n\n")
            if len(appno_df) > 100:
                appno_csv_path = RESULTS_DIR / "08_appno_match_histories.csv"
                appno_df.to_csv(appno_csv_path, index=False)
                f.write(f"> Full detail: [{appno_csv_path.name}]({appno_csv_path.name}) "
                        f"({len(appno_df):,} rows)\n\n")
        else:
            f.write("*No records matched exclusively via NMA_AppNo.*\n\n")

    print(f"[page_08] Written {path}")
    return path


if __name__ == "__main__":
    res = run()
    save(res)
