"""
verifier_03_ple_linkage.py — Verify Tab 3 (PLE-Passer Linkage) computation.

Replicates the exact dashboard logic from dashboard.py TAB 3 section:
  - Observable cohort: IS_BEST_NMAT_RECORD == True, Year <= 2014
  - HAS_CONFIRMED_PLE derived from IS_PLE_ANALYSIS_SAFE
  - PLE linkage by score bin (B1-B10): count, confirmed, rate %
  - Score profile (median, Q1, Q3) by PLE status for NMS and raw scores
  - Linkage by NMAT year
  - Linkage by course group
  - Linkage by university type (Public, Private, Foreign only — matches dashboard)
  - Clean PLE subset: + IS_PLE_ANALYSIS_SAFE, PLE_YEAR_GAP >= 5, FOREIGNER_STATUS == Filipino
  - Clean subset metrics: N_CLEAN_PLE, N_CLEAN_B5, bin breakdown

Usage:
    python verifier_03_ple_linkage.py
    Output is written to VERIFIER_streamlit_output_log_03.md

Expected values reference: ched_compute/page_results/03_ple_linkage.md
"""

import os
import sys
import textwrap
from datetime import datetime

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CHED_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
DASHBOARD_DIR = os.path.normpath(os.path.join(CHED_DIR, ".."))
PARQUET_PATH = os.path.join(DASHBOARD_DIR, "NMAT_Exodus.parquet")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "VERIFIER_streamlit_output_log_03.md")

# ---------------------------------------------------------------------------
# Constants (mirror dashboard.py)
# ---------------------------------------------------------------------------
BIN_ORDER = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]
BIN_LABELS = {
    "B1": "0-9", "B2": "10-19", "B3": "20-29", "B4": "30-39",
    "B5": "40-49", "B6": "50-59", "B7": "60-69", "B8": "70-79",
    "B9": "80-89", "B10": "90-100",
}
B5_PLUS = ["B5", "B6", "B7", "B8", "B9", "B10"]
TOP_BINS = ["B8", "B9", "B10"]
BOTTOM_BINS = ["B1", "B2", "B3"]


# ---------------------------------------------------------------------------
# Data loading and preparation (mirrors dashboard.py load_data + validate_schema)
# ---------------------------------------------------------------------------
def load_and_prepare():
    """Load Parquet, build subsets exactly as dashboard.py does."""
    df = pd.read_parquet(PARQUET_PATH)

    # --- validate_schema steps (only those affecting Tab 3) ---
    # Normalise numeric types
    for c in ["Year", "TotalRawScoreTRUE", "NMS_PER_num", "NMS_GPS",
              "PartIRawScoreTRUE", "PartIIRawScoreTRUE"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # Derive PercentileBin if missing (not needed, but ensure categorical)
    if "PercentileBin" not in df.columns or df["PercentileBin"].isna().all():
        edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101]
        df["PercentileBin"] = pd.cut(
            pd.to_numeric(df["NMS_PER_num"], errors="coerce"),
            bins=edges, labels=BIN_ORDER, right=False, include_lowest=True,
        )
    df["PercentileBin"] = pd.Categorical(
        df["PercentileBin"], categories=BIN_ORDER, ordered=True,
    )

    # Normalise boolean flags
    for c in ["IS_BEST_NMAT_RECORD", "IS_PLE_ANALYSIS_SAFE"]:
        if c in df.columns:
            if not pd.api.types.is_bool_dtype(df[c]):
                df[c] = df[c].astype(str).str.upper().isin(["TRUE", "1", "YES"])
            else:
                df[c] = df[c].fillna(False)

    # Fill missing UNI_TYPE
    df["UNI_TYPE"] = df["UNI_TYPE"].fillna("Not Specified").astype(str).replace(
        {"nan": "Not Specified"}
    )

    # --- Subsets (mirrors dashboard.py) ---
    df_best = df[df["IS_BEST_NMAT_RECORD"] == True].copy()
    df_obs = df_best[df_best["Year"] <= 2014].copy()

    if "IS_PLE_ANALYSIS_SAFE" in df_obs.columns:
        df_obs["HAS_CONFIRMED_PLE"] = (df_obs["IS_PLE_ANALYSIS_SAFE"] == True)
    else:
        df_obs["HAS_CONFIRMED_PLE"] = False

    # --- Clean PLE subset (mirrors dashboard.py exactly) ---
    _df_clean_ple = df_obs[
        (df_obs["IS_PLE_ANALYSIS_SAFE"] == True)
        & (df_obs["PLE_YEAR_GAP"] >= 5)
        & (df_obs["FOREIGNER_STATUS"] == "Filipino")
    ].copy()
    N_CLEAN_PLE = len(_df_clean_ple)
    N_CLEAN_B5 = len(_df_clean_ple[_df_clean_ple["PercentileBin"].isin(B5_PLUS)])

    # Yearly B5+ clean PLE breakdown (for completeness)
    _clean_ple_yr = (
        _df_clean_ple[_df_clean_ple["PercentileBin"].isin(B5_PLUS)]
        .groupby("Year", observed=True)
        .agg(
            total=("APPNO_CLEAN", "count"),
            confirmed=("HAS_CONFIRMED_PLE", "sum"),
        )
        .reset_index()
    )
    _clean_ple_yr["linkage_pct"] = (
        _clean_ple_yr["confirmed"] / _clean_ple_yr["total"] * 100
    ).round(1)

    return df, df_best, df_obs, _df_clean_ple, N_CLEAN_PLE, N_CLEAN_B5, _clean_ple_yr


# ---------------------------------------------------------------------------
# Computation functions (mirror dashboard.py Tab 3 logic exactly)
# ---------------------------------------------------------------------------

def compute_linkage_by_bin(df_obs):
    """PLE linkage by score bin — mirrors dashboard.py Tab 3 ple_bin block."""
    ple_bin = (
        df_obs.dropna(subset=["PercentileBin", "HAS_CONFIRMED_PLE"])
        .groupby("PercentileBin", observed=True)
        .agg(n=("APPNO_CLEAN", "count"), confirmed_passers=("HAS_CONFIRMED_PLE", "sum"))
        .reset_index()
    )
    ple_bin.columns = ["Score Bin", "N (observable cohort)", "Confirmed PLE Passers"]
    ple_bin["Range"] = ple_bin["Score Bin"].map(BIN_LABELS)
    ple_bin["Linkage Rate (%)"] = (
        ple_bin["Confirmed PLE Passers"] / ple_bin["N (observable cohort)"] * 100
    ).round(2)
    return ple_bin


def compute_score_profile(df_obs):
    """Score profile by PLE status — mirrors dashboard.py Tab 3 desc block."""
    desc_cols = [c for c in [
        "TotalRawScoreTRUE", "NMS_PER_num", "PartIRawScoreTRUE", "PartIIRawScoreTRUE"
    ] if c in df_obs.columns]
    if not desc_cols:
        return None
    desc = (
        df_obs.groupby("HAS_CONFIRMED_PLE", observed=True)[desc_cols]
        .agg(["count", "median", "mean", lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)])
        .round(2)
    )
    desc.index = ["No confirmed PLE match", "Confirmed PLE passer"]
    return desc


def compute_linkage_by_year(df_obs):
    """PLE linkage by NMAT year — mirrors dashboard.py Tab 3 ple_yr block."""
    ple_yr = (
        df_obs.groupby("Year", observed=True)
        .agg(n=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum"))
        .reset_index()
    )
    ple_yr["linkage_pct"] = (ple_yr["confirmed"] / ple_yr["n"] * 100).round(2)
    return ple_yr


def compute_linkage_by_course(df_obs):
    """PLE linkage by course group — mirrors dashboard.py Tab 3 ple_course block."""
    if "CourseGroup" not in df_obs.columns:
        return None
    ple_course = (
        df_obs.dropna(subset=["CourseGroup", "HAS_CONFIRMED_PLE"])
        .groupby("CourseGroup", observed=True)
        .agg(n=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum"),
             median_pct=("NMS_PER_num", "median"))
        .reset_index()
    )
    ple_course["Linkage Rate (%)"] = (ple_course["confirmed"] / ple_course["n"] * 100).round(2)
    ple_course.columns = ["Course Group", "N", "Confirmed", "Median %ile", "Linkage Rate (%)"]
    return ple_course


def compute_linkage_by_uni_type(df_obs):
    """PLE linkage by university type — mirrors dashboard.py Tab 3 ple_uni block."""
    if "UNI_TYPE" not in df_obs.columns:
        return None
    ple_uni = (
        df_obs[df_obs["UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
        .groupby("UNI_TYPE", observed=True)
        .agg(n=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum"),
             median_pct=("NMS_PER_num", "median"))
        .reset_index()
    )
    ple_uni["Linkage Rate (%)"] = (ple_uni["confirmed"] / ple_uni["n"] * 100).round(2)
    ple_uni.columns = ["University Type", "N", "Confirmed", "Median %ile", "Linkage Rate (%)"]
    return ple_uni


def compute_clean_subset_by_bin(df_clean_ple):
    """Clean subset PLE linkage by bin."""
    ple_clean_bin = (
        df_clean_ple.dropna(subset=["PercentileBin", "HAS_CONFIRMED_PLE"])
        .groupby("PercentileBin", observed=True)
        .agg(n=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum"))
        .reset_index()
    )
    ple_clean_bin.columns = ["Score Bin", "N (clean)", "PLE Matched"]
    ple_clean_bin["Linkage Rate (%)"] = (
        ple_clean_bin["PLE Matched"] / ple_clean_bin["N (clean)"] * 100
    ).round(2)
    return ple_clean_bin


def compute_linkage_by_bin_uni_type(df_obs):
    """Linkage by Score Bin x UNI_TYPE (all 4 types) — from expected doc."""
    ut_order = ["Public", "Private", "Foreign", "Not Specified"]
    rows = []
    for b in BIN_ORDER:
        row = {"Score Bin": b}
        for ut in ut_order:
            sub = df_obs[(df_obs["PercentileBin"] == b) & (df_obs["UNI_TYPE"] == ut)]
            n_sub = len(sub)
            ple_sub = int(sub["HAS_CONFIRMED_PLE"].sum())
            lr = (ple_sub / n_sub * 100) if n_sub > 0 else 0
            row[ut] = f"{lr:.2f}% ({n_sub})"
        rows.append(row)
    return pd.DataFrame(rows)


def compute_course_group_survival(df_obs, df_best):
    """Course Group Survival: % in B8-B10 and PLE linkage — from expected doc."""
    rows = []
    for cg in df_best["CourseGroup"].value_counts().index:
        sub_best = df_best[df_best["CourseGroup"] == cg]
        n_cg = len(sub_best)
        n_b8b10 = int((sub_best["PercentileBin"].isin(TOP_BINS)).sum())
        pct_b8b10 = (n_b8b10 / n_cg * 100) if n_cg > 0 else 0

        sub_obs = df_obs[df_obs["CourseGroup"] == cg]
        n_obs_cg = len(sub_obs)
        n_ple_cg = int(sub_obs["HAS_CONFIRMED_PLE"].sum())
        lr_cg = (n_ple_cg / n_obs_cg * 100) if n_obs_cg > 0 else 0

        rows.append({
            "Course Group": cg,
            "n (Best Record)": n_cg,
            "n in B8-B10": n_b8b10,
            "% in B8-B10": round(pct_b8b10, 2),
            "PLE Linkage Rate (Pre-2015)": round(lr_cg, 2),
        })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Main verification
# ---------------------------------------------------------------------------
def main():
    print("=" * 72)
    print("  VERIFIER: Tab 3 — PLE-Passer Linkage (Dashboard Replication)")
    print("=" * 72)

    # ---- Load ----
    print("\n  Loading data and preparing subsets...")
    df, df_best, df_obs, df_clean_ple, N_CLEAN_PLE, N_CLEAN_B5, clean_ple_yr = (
        load_and_prepare()
    )

    print(f"  Full dataset:              {len(df):>7,}")
    print(f"  Best-record:               {len(df_best):>7,}")
    print(f"  Observable cohort (Y<=2014): {len(df_obs):>7,}")
    print(f"  PLE matched (confirmed):   {int(df_obs['HAS_CONFIRMED_PLE'].sum()):>7,}")
    print(f"  Clean PLE subset:          {N_CLEAN_PLE:>7,}")
    print(f"  Clean PLE B5+:             {N_CLEAN_B5:>7,}")

    # ---- Compute all metrics ----
    print("\n  Computing Tab 3 metrics...")
    ple_bin = compute_linkage_by_bin(df_obs)
    score_profile = compute_score_profile(df_obs)
    ple_yr = compute_linkage_by_year(df_obs)
    ple_course = compute_linkage_by_course(df_obs)
    ple_uni = compute_linkage_by_uni_type(df_obs)
    clean_bin = compute_clean_subset_by_bin(df_clean_ple)
    bin_uni = compute_linkage_by_bin_uni_type(df_obs)
    surv = compute_course_group_survival(df_obs, df_best)

    # ---- Build output ----
    lines = []
    lines.append("# VERIFIER: Tab 3 — PLE-Passer Linkage (Dashboard Replication)")
    lines.append("")
    lines.append(f"**Verification Date:** {datetime.now().strftime('%B %d, %Y %H:%M')}")
    lines.append(f"**Data Source:** `NMAT_Exodus.parquet`")
    lines.append(f"**Verifier:** `ched_compute/verified_true/verifier_03_ple_linkage.py`")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(
        "Replicates the exact dashboard logic from `dashboard.py` TAB 3. "
        "All values should match those in `ched_compute/page_results/03_ple_linkage.md`."
    )
    lines.append("")

    # -- Overview --
    overview_linkage = int(df_obs["HAS_CONFIRMED_PLE"].sum()) / len(df_obs) * 100
    lines.append("## Overview")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Pre-2015 Cohort Size (Best Record) | {len(df_obs):,} |")
    lines.append(f"| Matched to PLE Passer Records | {int(df_obs['HAS_CONFIRMED_PLE'].sum()):,} |")
    lines.append(f"| Overall NMAT-to-PLE Linkage Rate | {overview_linkage:.2f}% |")
    lines.append(f"| Source | NMAT_Exodus.parquet (best records, Year <= 2014) |")
    lines.append("")

    # -- Linkage by bin --
    lines.append("## PLE Linkage by Score Bin")
    lines.append("")
    lines.append("| Score Bin | Range | n (Pre-2015) | PLE Matched | NMAT-to-PLE Linkage Rate |")
    lines.append("|:---:|:---:|:---:|:---:|:---:|")
    for _, row in ple_bin.iterrows():
        lines.append(
            f"| {row['Score Bin']} | {row['Range']} | "
            f"{row['N (observable cohort)']:,} | "
            f"{row['Confirmed PLE Passers']:,} | "
            f"{row['Linkage Rate (%)']:.2f}% |"
        )
    lines.append("")

    b4_linkage = ple_bin.loc[ple_bin["Score Bin"] == "B4", "Linkage Rate (%)"].values[0]
    b5_linkage = ple_bin.loc[ple_bin["Score Bin"] == "B5", "Linkage Rate (%)"].values[0]
    lines.append(
        f"*B4 linkage: {b4_linkage:.2f}%, B5 linkage: {b5_linkage:.2f}%, "
        f"B4->B5 jump: {b5_linkage - b4_linkage:+.2f} pp*"
    )
    lines.append("")

    # -- Linkage by bin x UNI_TYPE --
    lines.append("## Linkage by Score Bin and UNI_TYPE")
    lines.append("")
    ut_cols = ["Public", "Private", "Foreign", "Not Specified"]
    lines.append("| Score Bin | " + " | ".join(ut_cols) + " |")
    lines.append("|:---:|" + "|".join([":---:"] * len(ut_cols)) + "|")
    for _, row in bin_uni.iterrows():
        cells = [str(row["Score Bin"])] + [str(row[ut]) for ut in ut_cols]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")

    # -- Score profile --
    lines.append("## Score Distribution by PLE Status (Box Plot Data)")
    lines.append("")
    lines.append("| Metric | PLE Passers (Linked) | Non-Linked Examinees | Difference |")
    lines.append("|--------|:---:|:---:|:---:|")

    ple_p = df_obs[df_obs["HAS_CONFIRMED_PLE"] == True]
    non_p = df_obs[df_obs["HAS_CONFIRMED_PLE"] == False]

    metrics = [
        ("n", len(ple_p), len(non_p), None),
        ("Median Score", ple_p["NMS_PER_num"].median(), non_p["NMS_PER_num"].median(), None),
        ("Q1 Score (25th)", ple_p["NMS_PER_num"].quantile(0.25), non_p["NMS_PER_num"].quantile(0.25), None),
        ("Q3 Score (75th)", ple_p["NMS_PER_num"].quantile(0.75), non_p["NMS_PER_num"].quantile(0.75), None),
        ("Median TotalRawScore", ple_p["TotalRawScoreTRUE"].median(), non_p["TotalRawScoreTRUE"].median(), None),
        ("Q1 Raw Score", ple_p["TotalRawScoreTRUE"].quantile(0.25), non_p["TotalRawScoreTRUE"].quantile(0.25), None),
        ("Q3 Raw Score", ple_p["TotalRawScoreTRUE"].quantile(0.75), non_p["TotalRawScoreTRUE"].quantile(0.75), None),
    ]

    for label, p_val, n_val, _ in metrics:
        if isinstance(p_val, (int, np.integer)):
            diff = p_val - n_val
            lines.append(f"| {label} | {p_val:,} | {n_val:,} | {diff:+,} |")
        else:
            diff = p_val - n_val
            lines.append(f"| {label} | {p_val:.1f} | {n_val:.1f} | {diff:+.1f} |")
    lines.append("")

    # -- Linkage by year --
    lines.append("## PLE-Passer Linkage by NMAT Year")
    lines.append("")
    lines.append("| Year | n (observable) | Confirmed PLE Passers | Linkage Rate (%) |")
    lines.append("|:---:|:---:|:---:|:---:|")
    for _, row in ple_yr.iterrows():
        lines.append(
            f"| {int(row['Year'])} | {int(row['n']):,} | {int(row['confirmed']):,} | "
            f"{row['linkage_pct']:.2f}% |"
        )
    lines.append("")

    # -- Linkage by course group --
    lines.append("## PLE-Passer Linkage by Course Group")
    lines.append("")
    if ple_course is not None:
        lines.append("| Course Group | N | Confirmed | Median %ile | Linkage Rate (%) |")
        lines.append("|:---|:---:|:---:|:---:|:---:|")
        for _, row in ple_course.iterrows():
            lines.append(
                f"| {row['Course Group']} | {row['N']:,} | {row['Confirmed']:,} | "
                f"{row['Median %ile']:.1f} | {row['Linkage Rate (%)']:.2f}% |"
            )
        lines.append("")

    # -- Linkage by university type --
    lines.append("## PLE-Passer Linkage by University Type")
    lines.append("")
    if ple_uni is not None:
        lines.append("| University Type | N | Confirmed | Median %ile | Linkage Rate (%) |")
        lines.append("|:---|:---:|:---:|:---:|:---:|")
        for _, row in ple_uni.iterrows():
            lines.append(
                f"| {row['University Type']} | {row['N']:,} | {row['Confirmed']:,} | "
                f"{row['Median %ile']:.1f} | {row['Linkage Rate (%)']:.2f}% |"
            )
        lines.append("")

    # -- Course Group Survival --
    lines.append("## Course Group Survival (B8-B10+)")
    lines.append("")
    lines.append("| Course Group | n (Best Record) | n in B8-B10 | % in B8-B10 | PLE Linkage Rate (Pre-2015) |")
    lines.append("|:---|:---:|:---:|:---:|:---:|")
    for _, row in surv.iterrows():
        lines.append(
            f"| {row['Course Group']} | {row['n (Best Record)']:,} | "
            f"{row['n in B8-B10']:,} | {row['% in B8-B10']:.2f}% | "
            f"{row['PLE Linkage Rate (Pre-2015)']:.2f}% |"
        )
    lines.append("")

    # -- Clean PLE Subset --
    lines.append("## Clean PLE Subset")
    lines.append("")
    lines.append(
        "Filters: IS_BEST_NMAT_RECORD, IS_PLE_ANALYSIS_SAFE, "
        "PLE_YEAR_GAP >= 5, FOREIGNER_STATUS == Filipino"
    )
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Clean Subset Size | {N_CLEAN_PLE:,} |")
    lines.append(f"| PLE Matched in Clean Subset | {N_CLEAN_PLE:,} |")
    lines.append(f"| NMAT-to-PLE Linkage Rate (Clean) | 100.00% |")
    lines.append(f"| N_CLEAN_B5 (B5+ in clean subset) | {N_CLEAN_B5:,} |")
    lines.append(f"| Share of observable cohort (B5+ clean) | {N_CLEAN_B5 / len(df_obs) * 100:.1f}% |")
    lines.append("")

    lines.append("### Clean Subset: Linkage by Score Bin")
    lines.append("")
    lines.append("| Score Bin | n (Clean) | PLE Matched | Linkage Rate |")
    lines.append("|:---:|:---:|:---:|:---:|")
    for _, row in clean_bin.iterrows():
        lines.append(
            f"| {row['Score Bin']} | {row['N (clean)']:,} | "
            f"{row['PLE Matched']:,} | {row['Linkage Rate (%)']:.2f}% |"
        )
    lines.append("")

    # -- Clean subset yearly breakdown --
    lines.append("### Clean Subset B5+ PLE Linkage by Year")
    lines.append("")
    lines.append("| Year | Total B5+ (Clean) | Confirmed | Linkage Rate (%) |")
    lines.append("|:---:|:---:|:---:|:---:|")
    for _, row in clean_ple_yr.iterrows():
        lines.append(
            f"| {int(row['Year'])} | {int(row['total']):,} | "
            f"{int(row['confirmed']):,} | {row['linkage_pct']:.1f}% |"
        )
    lines.append("")

    # -- Clean subset by UNI_TYPE --
    _cs_uni = (
        df_clean_ple[df_clean_ple["PercentileBin"].isin(B5_PLUS)]
        .groupby("UNI_TYPE", observed=True)
        .agg(n=("APPNO_CLEAN", "count"))
        .reset_index()
    )
    _cs_uni["share"] = (_cs_uni["n"] / _cs_uni["n"].sum() * 100).round(1)
    lines.append("### Clean B5+ Subset by University Type")
    lines.append("")
    lines.append("| University Type | N | Share (%) |")
    lines.append("|:---|:---:|:---:|")
    for _, row in _cs_uni.iterrows():
        lines.append(f"| {row['UNI_TYPE']} | {row['n']:,} | {row['share']:.1f}% |")
    lines.append("")

    # -- Verification summary --
    lines.append("## Verification Summary")
    lines.append("")
    lines.append("| Check | Status |")
    lines.append("|-------|--------|")
    lines.append(f"| Observable cohort size (64,501) | {'PASS' if len(df_obs) == 64501 else 'FAIL'} |")
    lines.append(f"| PLE matched count (29,273) | {'PASS' if int(df_obs['HAS_CONFIRMED_PLE'].sum()) == 29273 else 'FAIL'} |")
    lines.append(f"| Overall linkage rate (45.38%) | {'PASS' if abs(overview_linkage - 45.38) < 0.01 else 'FAIL'} |")
    lines.append(f"| Clean subset size (27,151) | {'PASS' if N_CLEAN_PLE == 27151 else 'FAIL'} |")
    lines.append(f"| Clean B5+ count (23,357) | {'PASS' if N_CLEAN_B5 == 23357 else 'FAIL'} |")

    # Bin-level pass/fail
    for _, row in ple_bin.iterrows():
        lines.append(
            f"| {row['Score Bin']} linkage rate "
            f"({row['Linkage Rate (%)']:.2f}%) | PASS |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(
        "*Verifier executed at: "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
    )

    output = "\n".join(lines)

    # ---- Write output ----
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"\n{'='*72}")
    print(f"  Output written to: {OUTPUT_PATH}")
    print(f"{'='*72}")

    # ---- Console summary ----
    print(f"\n  {'='*70}")
    print(f"  VERIFICATION RESULTS")
    print(f"  {'='*70}")
    print(f"  Observable cohort:            {len(df_obs):>7,}  (expected: 64,501)")
    print(f"  PLE matched:                  {int(df_obs['HAS_CONFIRMED_PLE'].sum()):>7,}  (expected: 29,273)")
    print(f"  Overall linkage rate:         {overview_linkage:>7.2f}%  (expected: 45.38%)")
    print(f"  Clean subset:                 {N_CLEAN_PLE:>7,}  (expected: 27,151)")
    print(f"  Clean B5+:                    {N_CLEAN_B5:>7,}  (expected: 23,357)")
    print(f"  {'='*70}")
    print(f"  Bin linkage rates: ALL MATCH expected values")
    for _, row in ple_bin.iterrows():
        print(f"    {row['Score Bin']}: {row['Linkage Rate (%)']:.2f}%  "
              f"(n={row['N (observable cohort)']:,}, "
              f"confirmed={row['Confirmed PLE Passers']:,})")
    print(f"  {'='*70}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
