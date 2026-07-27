"""
Page 13: CHED Compliance
Replicates ALL computations from dashboard.py tab13 (lines ~2900-3300).
Extracts unfiltered data and saves to page_results/13_ched_compliance.md.

Produces:
- Section A: National PLE benchmark (annual rates, 5-year rolling avg, latest benchmark)
- Section B: Per-HEI PLE performance (each HEI with >=5 records, rate vs benchmark, above/below)
- Section C: Cut-off scenarios (30th B4+ vs 40th B5+ by UNI_TYPE)
- Section D: Foreign student SUC slot analysis (foreign count per SUC per year, over_cap flag)
- Section E: Per-HEI score distribution (NMS_PER_num stats, PercentileBin distribution)
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "data_aggregator"))

import numpy as np
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 300)
pd.set_option("display.max_colwidth", 60)

from config import BIN_ORDER, RESULTS_DIR
from helpers import load_data


def bin_at_or_above(b, threshold_b):
    """Check if bin b is at or above threshold bin in BIN_ORDER."""
    if pd.isna(b):
        return False
    try:
        return BIN_ORDER.index(b) >= BIN_ORDER.index(threshold_b)
    except (ValueError, IndexError):
        return False


def run() -> str:
    df, subsets = load_data()

    df_obs = subsets["bestobservable"].copy()
    df_trend = subsets["besttrend"].copy()

    lines = []

    # ── Header ──
    lines.append("# Page 13: CHED Compliance — CMO No. __, s. 2026")
    lines.append("")
    lines.append(f"**Generated:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("**Data source:** NMAT_Exodus.parquet (Pipeline 4)")
    lines.append("")
    lines.append("**Data subsets:**")
    lines.append("- `bestobservable` (Year <= 2014) — PLE-linked summaries")
    lines.append("- `besttrend` (2006-2018) — score distributions and cut-off scenarios")
    lines.append("")
    lines.append("**Filters:** None (full unfiltered dataset)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ================================================================
    # SECTION A: National PLE Benchmark
    # ================================================================
    lines.append("## Section A: National PLE Benchmark")
    lines.append("")
    lines.append("Annual national PLE passing rates and 5-year rolling average. The CHED amendment uses the 5-year rolling average as the benchmark: PHEIs above this benchmark may set cut-off at 30th percentile; those below must maintain 40th percentile.")
    lines.append("")

    if df_obs.empty:
        lines.append("*No observable best-record rows available.*")
        lines.append("")
    else:
        _annual = (
            df_obs.groupby("Year", observed=True)
            .agg(
                n_examinees=("IS_PLE_ANALYSIS_SAFE", "size"),
                n_confirmed_ple=("IS_PLE_ANALYSIS_SAFE", "sum"),
            )
            .reset_index()
        )
        _annual["ple_rate_pct"] = (_annual["n_confirmed_ple"] / _annual["n_examinees"] * 100).round(2)
        _annual["5yr_rolling_avg_pct"] = _annual["ple_rate_pct"].rolling(window=5, min_periods=3).mean().round(2)

        lines.append("**Table A1. Annual national PLE passing rates with 5-year rolling average**")
        lines.append("")
        lines.append(_annual.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")

        # Latest benchmark
        _latest_5yr = _annual[_annual["5yr_rolling_avg_pct"].notna()].iloc[-1] if len(_annual[_annual["5yr_rolling_avg_pct"].notna()]) > 0 else None
        if _latest_5yr is not None:
            _benchmark_val = _latest_5yr["5yr_rolling_avg_pct"]
            lines.append("**Latest 5-year national average (benchmark):**")
            lines.append("")
            lines.append(f"| Metric | Value |")
            lines.append(f"|--------|------:|")
            lines.append(f"| Latest 5-year national avg | {_benchmark_val:.2f}% |")
            lines.append(f"| Reference year | {int(_latest_5yr['Year'])} |")
            lines.append("")
        else:
            _benchmark_val = None
            lines.append("*Insufficient data for 5-year rolling average.*")
            lines.append("")

    # ================================================================
    # SECTION B: Per-HEI PLE Performance
    # ================================================================
    lines.append("---")
    lines.append("## Section B: Per-HEI PLE Performance vs National Benchmark")
    lines.append("")
    lines.append("Each HEI's PLE passing rate compared to the national 5-year rolling average. Only HEIs with at least 5 observable best-record examinees are shown. Green = above benchmark (30th percentile eligible), Red = below benchmark (40th percentile required).")
    lines.append("")

    if df_obs.empty or _benchmark_val is None:
        lines.append("*Insufficient data for per-HEI analysis.*")
        lines.append("")
    else:
        _hei_ple = (
            df_obs.groupby(["UNIVERSITY", "UNI_TYPE"], observed=True)
            .agg(
                n_examinees=("IS_PLE_ANALYSIS_SAFE", "size"),
                n_confirmed_ple=("IS_PLE_ANALYSIS_SAFE", "sum"),
                median_percentile=("NMS_PER_num", "median"),
            )
            .reset_index()
        )
        _hei_ple["ple_rate_pct"] = (_hei_ple["n_confirmed_ple"] / _hei_ple["n_examinees"] * 100).round(2)
        _hei_ple = _hei_ple[_hei_ple["n_examinees"] >= 5].copy()
        _hei_ple["above_benchmark"] = _hei_ple["ple_rate_pct"] > _benchmark_val

        _hei_display = _hei_ple.sort_values("ple_rate_pct", ascending=False).reset_index(drop=True)
        _hei_display["status"] = np.where(
            _hei_display["above_benchmark"],
            "Above benchmark (30th eligible)",
            "Below benchmark (40th required)",
        )

        _c_pass = int(_hei_display["above_benchmark"].sum())
        _c_fail = int((~_hei_display["above_benchmark"]).sum())

        lines.append("**Summary:**")
        lines.append("")
        lines.append(f"| Metric | Value |")
        lines.append(f"|--------|------:|")
        lines.append(f"| HEIs above benchmark | {_c_pass} |")
        lines.append(f"| HEIs below benchmark | {_c_fail} |")
        lines.append(f"| National benchmark | {_benchmark_val:.2f}% |")
        lines.append("")

        lines.append("**Table B1. Per-HEI PLE performance vs benchmark**")
        lines.append(f"*(Minimum examinees: 5, sorted by PLE rate descending)*")
        lines.append("")
        lines.append(_hei_display[[
            "UNIVERSITY", "UNI_TYPE", "n_examinees", "median_percentile",
            "ple_rate_pct", "status",
        ]].to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")

    # ================================================================
    # SECTION C: Cut-off Scenarios
    # ================================================================
    lines.append("---")
    lines.append("## Section C: Cut-off Scenarios — 30th Percentile (B4+) vs 40th Percentile (B5+)")
    lines.append("")
    lines.append("Comparison of examinee counts and PLE outcomes under the 30th percentile (B4+) vs 40th percentile (B5+) cut-off thresholds, broken down by university type.")
    lines.append("")

    if df_obs.empty or df_trend.empty:
        lines.append("*Insufficient data for cut-off scenario analysis.*")
        lines.append("")
    else:
        _scenario_rows = []
        for _uni_type in ["All", "Public", "Private", "Foreign"]:
            _sub = df_trend if _uni_type == "All" else df_trend[df_trend["UNI_TYPE"] == _uni_type]
            _sub_obs = df_obs if _uni_type == "All" else df_obs[df_obs["UNI_TYPE"] == _uni_type]

            for _label, _bin in [("30th percentile (B4+)", "B4"), ("40th percentile (B5+)", "B5")]:
                _admitted = _sub[_sub["PercentileBin"].apply(lambda x: bin_at_or_above(x, _bin))]
                _ple_cohort = _sub_obs[_sub_obs["PercentileBin"].apply(lambda x: bin_at_or_above(x, _bin))]
                _scenario_rows.append({
                    "University Type": _uni_type,
                    "Cut-off": _label,
                    "Admitted (best records)": len(_admitted),
                    "PLE passers (observable)": int(_ple_cohort["IS_PLE_ANALYSIS_SAFE"].sum()) if len(_ple_cohort) > 0 else 0,
                    "PLE pass rate (%)": round(_ple_cohort["IS_PLE_ANALYSIS_SAFE"].mean() * 100, 2) if len(_ple_cohort) > 0 else 0,
                    "Median percentile": round(_admitted["NMS_PER_num"].median(), 1) if len(_admitted) > 0 else 0,
                })

        _scenario_df = pd.DataFrame(_scenario_rows)

        lines.append("**Table C1. Cut-off scenario comparison by university type**")
        lines.append("")
        lines.append(_scenario_df.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")

    # ================================================================
    # SECTION D: Foreign Student SUC Slot Analysis
    # ================================================================
    lines.append("---")
    lines.append("## Section D: Foreign Student Enrollment at SUCs — 10-Slot Cap Analysis")
    lines.append("")
    lines.append("The CHED amendment caps foreign student enrollment at 10 per incoming freshmen class at SUCs. This section shows foreign student counts per SUC per year based on CITIZENSHIP_FINAL from Pipeline 4.")
    lines.append("")

    if "CITIZENSHIP_FINAL" in df_trend.columns:
        _suc_foreign = df_trend[
            (df_trend["UNI_TYPE"] == "Public")
            & (df_trend["FOREIGNER_STATUS"] != "Filipino")
            & (df_trend["IS_BEST_NMAT_RECORD"] == True)
        ]

        if not _suc_foreign.empty:
            _suc_yr = (
                _suc_foreign.groupby(["UNIVERSITY", "Year"], observed=True)
                .size()
                .reset_index(name="foreign_count")
            )
            _suc_yr["over_cap"] = _suc_yr["foreign_count"] > 10

            _over_cap = _suc_yr[_suc_yr["over_cap"]]

            lines.append("**Summary metrics:**")
            lines.append("")
            lines.append(f"| Metric | Value |")
            lines.append(f"|--------|------:|")
            lines.append(f"| SUC-Year combos exceeding 10-slot cap | {len(_over_cap)} |")
            lines.append(f"| Total foreign students at SUCs | {len(_suc_foreign):,} |")
            lines.append("")

            # Per-SUC summary (top 20 by max foreign)
            _suc_summary = (
                _suc_yr.groupby("UNIVERSITY")
                .agg(
                    max_foreign=("foreign_count", "max"),
                    total_foreign=("foreign_count", "sum"),
                    years_over_cap=("over_cap", "sum"),
                )
                .reset_index()
                .sort_values("max_foreign", ascending=False)
                .head(20)
            )

            lines.append("**Table D1. Top 20 SUCs by max foreign enrollment in a single year**")
            lines.append("")
            lines.append(_suc_summary.to_markdown(index=False, tablefmt="pipe", numalign="right"))
            lines.append("")

            # Full SUC-Year detail
            lines.append("**Table D2. Full foreign enrollment detail by SUC and year**")
            lines.append("*(Sorted by year ascending, foreign count descending within year)*")
            lines.append("")
            _suc_detail = _suc_yr.sort_values(
                ["Year", "foreign_count"], ascending=[True, False]
            ).reset_index(drop=True)
            lines.append(_suc_detail.to_markdown(index=False, tablefmt="pipe", numalign="right"))
            lines.append("")
        else:
            lines.append("*No foreign student records at SUCs under the current filters.*")
            lines.append("")
    else:
        lines.append("*Citizenship columns not available. Run Pipeline 4 to generate NMAT_Exodus.parquet with CITIZENSHIP_FINAL.*")
        lines.append("")

    # ================================================================
    # SECTION E: Per-HEI Score Distribution
    # ================================================================
    lines.append("---")
    lines.append("## Section E: Per-HEI Score Distribution")
    lines.append("")
    lines.append("For every institution (with at least 5 best-record examinees): NMS_PER_num statistics, percentile bin distribution, and cut-off eligibility metrics.")
    lines.append("")

    if df_trend.empty:
        lines.append("*No trend data available.*")
        lines.append("")
    else:
        _hei_list = sorted(df_trend["UNIVERSITY"].dropna().unique())
        lines.append(f"**Total institutions with data: {len(_hei_list):,}**")
        lines.append("")

        # Compute per-HEI stats for all HEIs
        hei_stats_rows = []
        for hei in _hei_list:
            hei_data = df_trend[df_trend["UNIVERSITY"] == hei]
            hei_obs = df_obs[df_obs["UNIVERSITY"] == hei] if not df_obs.empty else pd.DataFrame()

            if len(hei_data) < 5:
                continue

            bin_dist = hei_data["PercentileBin"].value_counts().reindex(BIN_ORDER).fillna(0)
            total = bin_dist.sum()
            hei_stats_rows.append({
                "UNIVERSITY": hei,
                "UNI_TYPE": hei_data["UNI_TYPE"].mode().iloc[0] if not hei_data["UNI_TYPE"].mode().empty else "Unknown",
                "Total Examinees": len(hei_data),
                "Median %ile": round(hei_data["NMS_PER_num"].median(), 1),
                "Mean %ile": round(hei_data["NMS_PER_num"].mean(), 1),
                "Q25 %ile": round(hei_data["NMS_PER_num"].quantile(0.25), 1),
                "Q75 %ile": round(hei_data["NMS_PER_num"].quantile(0.75), 1),
                "B4+ %": round(bin_dist.loc[bin_dist.index.isin(["B4","B5","B6","B7","B8","B9","B10"])].sum() / total * 100, 1) if total > 0 else 0,
                "B5+ %": round(bin_dist.loc[bin_dist.index.isin(["B5","B6","B7","B8","B9","B10"])].sum() / total * 100, 1) if total > 0 else 0,
                "Health Sci %": round(hei_data["CourseGroup"].value_counts().get("Medical & Allied", 0) / len(hei_data) * 100, 1) if len(hei_data) > 0 else 0,
                "PLE pass rate %": round(hei_obs["IS_PLE_ANALYSIS_SAFE"].mean() * 100, 1) if not hei_obs.empty else None,
            })

        hei_stats_df = pd.DataFrame(hei_stats_rows)
        if not hei_stats_df.empty:
            hei_stats_df = hei_stats_df.sort_values("Total Examinees", ascending=False).reset_index(drop=True)

            lines.append("**Table E1. Per-HEI summary statistics**")
            lines.append("*(Sorted by total examinees descending; minimum 5 examinees)*")
            lines.append("")
            lines.append(hei_stats_df.to_markdown(index=False, tablefmt="pipe", numalign="right"))
            lines.append("")

            # Also produce the detailed bin distribution for all HEIs
            lines.append("**Table E2. Per-HEI percentile bin distribution (full)**")
            lines.append("")

            # Build a multi-HEI bin distribution table
            bin_hei_rows = []
            for hei in _hei_list:
                hei_data = df_trend[df_trend["UNIVERSITY"] == hei]
                if len(hei_data) < 5:
                    continue
                bin_dist = hei_data["PercentileBin"].value_counts().reindex(BIN_ORDER).fillna(0).astype(int)
                hei_type = hei_data["UNI_TYPE"].mode().iloc[0] if not hei_data["UNI_TYPE"].mode().empty else "Unknown"
                bin_hei_rows.append(pd.Series(
                    data=[hei, hei_type, len(hei_data)] + [bin_dist[b] for b in BIN_ORDER],
                    index=["UNIVERSITY", "UNI_TYPE", "N"] + BIN_ORDER
                ))
            if bin_hei_rows:
                bin_hei_df = pd.DataFrame(bin_hei_rows).sort_values("N", ascending=False).reset_index(drop=True)
                lines.append(bin_hei_df.to_markdown(index=False, tablefmt="pipe", numalign="right"))
                lines.append("")
        else:
            lines.append("*No HEI data with >=5 examinees.*")
            lines.append("")

    # ── Footer ──
    lines.append("---")
    lines.append("")
    lines.append("*Source: NMAT_Exodus.parquet (Pipeline 4). Observable best-record cohort (Year <= 2014) used for all PLE-linked summaries to avoid misclassifying later cohorts as non-passers before their licensure window closes.*")
    lines.append("")

    return "\n".join(lines)


def save():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = RESULTS_DIR / "13_ched_compliance.md"
    content = run()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved: {out_path.resolve()}")


if __name__ == "__main__":
    save()
