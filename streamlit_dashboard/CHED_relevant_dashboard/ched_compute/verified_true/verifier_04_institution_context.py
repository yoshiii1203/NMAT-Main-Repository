"""
verifier_04_institution_context.py — Verify Tab 4 (Institution and Foreign Context).

Replicates dashboard.py TAB 4 computation logic:
  1. Score summary by UNI_TYPE (median, Q25, Q75) on best-record subset
  2. Bin distribution (row %) by UNI_TYPE via cross-tab PercentileBin
  3. Top-bin share (B8+B9+B10) by UNI_TYPE
  4. Foreign examinee counts using ALL records (not best-record) for citizenship
  5. Top 10 nationalities among verified foreign examinees
  6. Additional cross-checks against expected values in 04_institution_context.md

Usage:
    python streamlit_dashboard/CHED_relevant_dashboard/ched_compute/verified_true/verifier_04_institution_context.py

Output:
    VERIFIER_streamlit_output_log_04.md
"""

import pandas as pd
import numpy as np
import os
import datetime

# ── Paths ──────────────────────────────────────────────────────────────────
PARQUET_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "NMAT_Exodus.parquet"
))
OUTPUT_DIR = os.path.dirname(__file__)
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "VERIFIER_streamlit_output_log_04.md")

# ── Constants (mirroring dashboard.py / config.py) ─────────────────────────
BIN_ORDER = [f"B{i}" for i in range(1, 11)]
TOP_BINS = ["B8", "B9", "B10"]
UNI_TYPE_ORDER = ["Public", "Private", "Foreign", "Not Specified"]
COLORS_UNI = {"Public": "#1f77b4", "Private": "#ff7f0e",
              "Foreign": "#9467bd", "Not Specified": "#7f7f7f"}
FOREIGN_STATUSES_FULL = ["Verified Foreigner", "Likely Foreigner"]


def fmt(val, decimals=2):
    """Format a number for display."""
    if isinstance(val, (int, np.integer)):
        return f"{val:,}"
    elif isinstance(val, (float, np.floating)):
        if pd.isna(val):
            return "N/A"
        return f"{val:,.{decimals}f}"
    return str(val)


def pct(val, decimals=2):
    """Format as percentage string."""
    return f"{val:.{decimals}f}%"


def write_line(lines, content=""):
    lines.append(content)


def main():
    # ── Load data ──────────────────────────────────────────────────────────
    print(f"Loading parquet from {PARQUET_PATH} ...")
    df_all = pd.read_parquet(PARQUET_PATH)
    df_best = df_all[df_all["IS_BEST_NMAT_RECORD"] == True].copy()

    print(f"  df_all:  {len(df_all):,} records")
    print(f"  df_best: {len(df_best):,} records")
    print()

    out = []
    write_line(out, "# Verifier: Tab 4 — Institution and Foreign Context")
    write_line(out)
    write_line(out, f"**Date:** {datetime.datetime.now().strftime('%B %d, %Y')}")
    write_line(out, f"**Data:** `NMAT_Exodus.parquet` ({len(df_all):,} rows, {len(df_all.columns)} cols)")
    write_line(out, f"**Best-record examinees:** {len(df_best):,}")
    write_line(out)
    write_line(out, "---")
    write_line(out)

    # ═══════════════════════════════════════════════════════════════════════
    #  1. SCORE SUMMARY BY UNI_TYPE (dashboard lines 844–860)
    # ═══════════════════════════════════════════════════════════════════════
    write_line(out, "## 1. Score Summary by University Type")
    write_line(out)
    write_line(out, "Dashboard logic: best-record subset, UNI_TYPE in [Public, Private, Foreign].")
    write_line(out, "Groups by UNI_TYPE; median, Q25, Q75 on NMS_PER_num; median raw + GPS.")
    write_line(out)

    uni_subset = df_best[df_best["UNI_TYPE"].isin(["Public", "Private", "Foreign"])].copy()
    write_line(out, f"uni_subset n: {len(uni_subset):,}")
    write_line(out)

    uni_score = (
        uni_subset.groupby("UNI_TYPE", observed=True)
        .agg(
            n=("APPNO_CLEAN", "count"),
            median_percentile=("NMS_PER_num", "median"),
            q25_percentile=("NMS_PER_num", lambda x: x.quantile(0.25)),
            q75_percentile=("NMS_PER_num", lambda x: x.quantile(0.75)),
            median_raw=("TotalRawScoreTRUE", "median"),
            median_gps=("NMS_GPS", "median"),
        )
        .round(2)
        .reset_index()
    )
    uni_score.columns = [
        "UNI_TYPE", "N (best)", "Median %ile",
        "Q25 %ile", "Q75 %ile", "Median Raw", "Median GPS"
    ]

    write_line(out, "| UNI_TYPE | N (best) | Median %ile | Q25 %ile | Q75 %ile | Median Raw | Median GPS |")
    write_line(out, "|:---------|:--------:|:-----------:|:--------:|:--------:|:----------:|:----------:|")
    for _, row in uni_score.iterrows():
        write_line(out,
            f"| {row['UNI_TYPE']} | {fmt(row['N (best)'], 0)} | "
            f"{row['Median %ile']:.1f} | {row['Q25 %ile']:.1f} | "
            f"{row['Q75 %ile']:.1f} | {row['Median Raw']:.1f} | "
            f"{row['Median GPS']:.1f} |"
        )
    write_line(out)

    # ── Cross-check note ─────────────────────────────────────────────────
    write_line(out, "> **Cross-check note:** Expected values doc shows bin-rank medians for all "
                "UNI_TYPE values. Dashboard uses uni_subset (Public/Private/Foreign only, "
                "excluding Not Specified).")
    write_line(out)

    # ═══════════════════════════════════════════════════════════════════════
    #  2. BIN DISTRIBUTION BY UNI_TYPE (row %)
    # ═══════════════════════════════════════════════════════════════════════
    write_line(out, "## 2. Bin Distribution by UNI_TYPE (Row %)")
    write_line(out)
    write_line(out, "Dashboard uses `make_bin_pct(uni_subset, 'UNI_TYPE')`: cross-tab UNI_TYPE vs PercentileBin, "
                "reindexed to B1–B10, row-wise percentages.")
    write_line(out)

    # Replicate make_bin_pct
    ct = pd.crosstab(uni_subset["UNI_TYPE"], uni_subset["PercentileBin"], dropna=False)
    ct = ct.reindex(columns=BIN_ORDER, fill_value=0)
    ct = ct.apply(pd.to_numeric, errors="coerce")
    pct_df = ct.div(ct.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)

    write_line(out, "**Row % (each UNI_TYPE row sums to ~100%):**")
    write_line(out)
    header_cols = " | ".join(BIN_ORDER)
    write_line(out, f"| UNI_TYPE | {header_cols} |")
    write_line(out, "|:---------|" + "|".join([":---:"] * len(BIN_ORDER)) + "|")
    for ut in pct_df.index:
        vals = [f"{pct_df.loc[ut, b]:.1f}" for b in BIN_ORDER]
        write_line(out, f"| {ut} | {' | '.join(vals)} |")
    write_line(out)

    # Raw counts
    write_line(out, "**Raw counts:**")
    write_line(out)
    header_cols = " | ".join(BIN_ORDER)
    write_line(out, f"| UNI_TYPE | {header_cols} |")
    write_line(out, "|:---------|" + "|".join([":---:"] * len(BIN_ORDER)) + "|")
    for ut in ct.index:
        vals = [f"{int(ct.loc[ut, b]):,}" for b in BIN_ORDER]
        write_line(out, f"| {ut} | {' | '.join(vals)} |")
    write_line(out)

    # ═══════════════════════════════════════════════════════════════════════
    #  3. TOP-BIN SHARE (B8–B10) BY UNI_TYPE
    # ═══════════════════════════════════════════════════════════════════════
    write_line(out, "## 3. Top-Bin Share (B8–B10) by UNI_TYPE")
    write_line(out)
    write_line(out, "Dashboard sums B8+B9+B10 row% from bin distribution, sorts ascending.")
    write_line(out)

    top_uni = pct_df[TOP_BINS].sum(axis=1).sort_values()

    write_line(out, "| UNI_TYPE | B8 % | B9 % | B10 % | B8–B10 Total % |")
    write_line(out, "|:---------|:----:|:----:|:-----:|:--------------:|")
    for ut in top_uni.index:
        b8 = pct_df.loc[ut, "B8"]
        b9 = pct_df.loc[ut, "B9"]
        b10 = pct_df.loc[ut, "B10"]
        tot = top_uni.loc[ut]
        write_line(out, f"| {ut} | {b8:.1f} | {b9:.1f} | {b10:.1f} | {tot:.1f} |")
    write_line(out)

    # Counts for top-bin table (dashboard also shows total examinees)
    write_line(out, "**With examinee counts (matching dashboard table):**")
    write_line(out)
    write_line(out, "| UNI_TYPE | Total examinees | B8–B10 % |")
    write_line(out, "|:---------|:---------------:|:--------:|")
    for ut in top_uni.index:
        n_ut = len(uni_subset[uni_subset["UNI_TYPE"] == ut])
        write_line(out, f"| {ut} | {n_ut:,} | {top_uni.loc[ut]:.1f} |")
    write_line(out)

    # ═══════════════════════════════════════════════════════════════════════
    #  4. FOREIGN EXAMINEE COUNTS (ALL records — consistent with dashboard)
    # ═══════════════════════════════════════════════════════════════════════
    write_line(out, "## 4. Foreign Examinee Counts (df_all — all records)")
    write_line(out)
    write_line(out, "Dashboard uses **all records (df_all)** for citizenship context. "
                "FOREIGNER_STATUS == 'Verified Foreigner' defines foreign.")
    write_line(out, "")
    write_line(out, "> **Note:** The expected values doc (04_institution_context.md) uses FOREIGNER_STATUS in "
                "['Verified Foreigner', 'Likely Foreigner'] for the nationality distribution "
                "table (26,491 India, 32,514 total foreign records), while the dashboard TAB 4 "
                "uses only FOREIGNER_STATUS == 'Verified Foreigner' (26,490 India, 32,501 total "
                "foreign records). This means the '% of Foreign' columns will differ between "
                "the two. The 13 'Likely Foreigner' records are dropped from dashboard TAB 4's "
                "nationality chart.")
    write_line(out)
    write_line(out)

    foreign_all = df_all[df_all["FOREIGNER_STATUS"] == "Verified Foreigner"]
    filipino_all = df_all[df_all["CITIZENSHIP_FINAL"] == "Filipino"]
    likely_all = df_all[df_all["FOREIGNER_STATUS"] == "Likely Foreigner"]

    write_line(out, "### Summary Metrics (All Records)")
    write_line(out)
    write_line(out, "| Metric | Value |")
    write_line(out, "|--------|-------|")
    write_line(out, f"| Verified Foreign examinees (all records) | {len(foreign_all):,} |")
    write_line(out, f"| Likely Foreign examinees (all records) | {len(likely_all):,} |")
    write_line(out, f"| Filipino examinees (all records) | {len(filipino_all):,} |")
    write_line(out, f"| Distinct foreign nationalities | {foreign_all['CITIZENSHIP_FINAL'].nunique():,} |")
    write_line(out)

    # ── Best-record foreign counts (for cross-check with expected doc) ──
    write_line(out, "### Cross-Check: Best-Record Foreign Counts")
    write_line(out)
    write_line(out, "Expected values doc (04_institution_context.md) uses best-record for primary counts, "
                "combining Verified + Likely Foreigner.")
    write_line(out)

    best_foreign_full = df_best[df_best["FOREIGNER_STATUS"].isin(FOREIGN_STATUSES_FULL)]
    best_verified = df_best[df_best["FOREIGNER_STATUS"] == "Verified Foreigner"]
    best_likely = df_best[df_best["FOREIGNER_STATUS"] == "Likely Foreigner"]
    best_filipino = df_best[df_best["CITIZENSHIP_FINAL"] == "Filipino"]

    write_line(out, "| Metric | Value |")
    write_line(out, "|--------|-------|")
    write_line(out, f"| Total examinees (best record) | {len(df_best):,} |")
    write_line(out, f"| Foreign examinees (best, Verified+Likely) | {len(best_foreign_full):,} |")
    write_line(out, f"|   Verified Foreigners (best) | {len(best_verified):,} |")
    write_line(out, f"|   Likely Foreigners (best) | {len(best_likely):,} |")
    write_line(out, f"| Filipino examinees (best) | {len(best_filipino):,} |")
    write_line(out, f"| Foreign as % of Total (best) | {pct(len(best_foreign_full) / len(df_best) * 100)} |")
    write_line(out)

    # ── Foreign by UNI_TYPE (best-record) ────────────────────────────────
    write_line(out, "### Foreign Examinees by UNI_TYPE (Best Record)")
    write_line(out)

    write_line(out, "| UNI_TYPE | Foreign n (Best) | % of Foreign | % of UNI_TYPE Total |")
    write_line(out, "|:---------|:----------------:|:------------:|:-------------------:|")
    for ut in UNI_TYPE_ORDER:
        foreign_ut = int((best_foreign_full["UNI_TYPE"] == ut).sum())
        total_ut = int((df_best["UNI_TYPE"] == ut).sum())
        if total_ut == 0:
            continue
        write_line(out,
            f"| {ut} | {foreign_ut:,} | "
            f"{foreign_ut/len(best_foreign_full)*100:.2f}% | "
            f"{foreign_ut/total_ut*100:.2f}% |"
        )
    write_line(out)

    # ═══════════════════════════════════════════════════════════════════════
    #  5. TOP 10 NATIONALITIES (all records, dashboard logic)
    # ═══════════════════════════════════════════════════════════════════════
    write_line(out, "## 5. Top 10 Nationalities (All Records, Verified Foreign)")
    write_line(out)
    write_line(out, "Dashboard: `foreign_all['CITIZENSHIP_FINAL'].value_counts().head(10)`")
    write_line(out)

    top_nat = foreign_all["CITIZENSHIP_FINAL"].value_counts().head(10).reset_index()
    top_nat.columns = ["Nationality", "Count"]

    write_line(out, "| Rank | Nationality | Count | % of Foreign |")
    write_line(out, "|:----:|:------------|:-----:|:------------:|")
    for i, (_, row) in enumerate(top_nat.iterrows(), 1):
        write_line(out,
            f"| {i} | {row['Nationality']} | {row['Count']:,} | "
            f"{row['Count'] / len(foreign_all) * 100:.2f}% |"
        )
    write_line(out)

    # ── Extended: Top 20 with median (04_institution_context.md style) ───
    write_line(out, "### Extended: Top 20 Nationalities with Median NMS (All Records)")
    write_line(out)

    top20 = foreign_all["CITIZENSHIP_FINAL"].value_counts().head(20)

    write_line(out, "| Rank | Nationality | n (All Records) | % of Foreign | Median | Q1 | Q3 | % Below B4+ |")
    write_line(out, "|:----:|:------------|:---------------:|:------------:|:-----:|:--:|:--:|:-----------:|")
    for i, (nat, n) in enumerate(top20.items(), 1):
        sub = foreign_all[foreign_all["CITIZENSHIP_FINAL"] == nat]
        med = sub["NMS_PER_num"].median()
        q1 = sub["NMS_PER_num"].quantile(0.25)
        q3 = sub["NMS_PER_num"].quantile(0.75)
        below_b4 = int(
            sub["PercentileBin"]
            .apply(lambda b: BIN_ORDER.index(b) < BIN_ORDER.index("B4") if b in BIN_ORDER else True)
            .sum()
        )
        pct_below = below_b4 / n * 100 if n > 0 else 0
        write_line(out,
            f"| {i} | {nat} | {n:,} | {n/len(foreign_all)*100:.2f}% | "
            f"{med:.1f} | {q1:.1f} | {q3:.1f} | {pct_below:.2f}% |"
        )
    write_line(out)

    # ═══════════════════════════════════════════════════════════════════════
    #  6. FOREIGN EXAMINEES BY YEAR (best-record, cross-check)
    # ═══════════════════════════════════════════════════════════════════════
    write_line(out, "## 6. Foreign Examinees by Year (Best Record)")
    write_line(out)

    write_line(out, "| Year | Foreign n | % of Year | Total Examinees |")
    write_line(out, "|:----:|:---------:|:---------:|:---------------:|")
    for yr in sorted(df_best["Year"].unique()):
        foreign_yr = int((best_foreign_full["Year"] == yr).sum())
        total_yr = int((df_best["Year"] == yr).sum())
        if total_yr == 0:
            continue
        write_line(out, f"| {yr} | {foreign_yr:,} | {foreign_yr/total_yr*100:.2f}% | {total_yr:,} |")
    write_line(out)

    # ═══════════════════════════════════════════════════════════════════════
    #  7. FOREIGN vs FILIPINO NMAT-to-PLE LINKAGE
    # ═══════════════════════════════════════════════════════════════════════
    write_line(out, "## 7. Foreign vs Filipino: NMAT-to-PLE Linkage (Best Record, Pre-2015)")
    write_line(out)

    obs = df_best[df_best["Year"] <= 2014].copy()
    obs["IS_FOREIGN"] = obs["FOREIGNER_STATUS"].isin(FOREIGN_STATUSES_FULL)

    write_line(out, "| Group | n (Pre-2015, Best Record) | PLE Matched | NMAT-to-PLE Linkage Rate |")
    write_line(out, "|:------|:------------------------:|:-----------:|:------------------------:|")
    for grp_name, grp_mask in [("Filipino", False), ("Foreign", True)]:
        sub = obs[obs["IS_FOREIGN"] == grp_mask]
        n_obs = len(sub)
        n_ple = int(sub["IS_PLE_PASSER"].sum())
        lr = (n_ple / n_obs * 100) if n_obs > 0 else 0
        write_line(out, f"| {grp_name} | {n_obs:,} | {n_ple:,} | {lr:.2f}% |")
    write_line(out)

    # ═══════════════════════════════════════════════════════════════════════
    #  8. KEY INSIGHT CROSS-CHECK
    # ═══════════════════════════════════════════════════════════════════════
    write_line(out, "## 8. Key Insight Cross-Check")
    write_line(out)

    india_all = foreign_all[foreign_all["CITIZENSHIP_FINAL"] == "India"]
    india_best = best_foreign_full[best_foreign_full["CITIZENSHIP_FINAL"] == "India"]

    write_line(out, f"- India examinees (all records): {len(india_all):,}")
    write_line(out, f"- India examinees (best record): {len(india_best):,}")
    write_line(out, f"- India % of foreign (best): {len(india_best)/len(best_foreign_full)*100:.1f}%")
    write_line(out, f"- India median NMS (all records): {india_all['NMS_PER_num'].median():.1f}")
    write_line(out, f"- India median NMS (best record): {india_best['NMS_PER_num'].median():.1f}")

    india_below = int(
        india_all["PercentileBin"]
        .apply(lambda b: BIN_ORDER.index(b) < BIN_ORDER.index("B4") if b in BIN_ORDER else True)
        .sum()
    )
    india_pct_below = india_below / len(india_all) * 100 if len(india_all) > 0 else 0
    write_line(out, f"- India % below B4+ (all records): {india_pct_below:.1f}%")
    write_line(out)

    # ═══════════════════════════════════════════════════════════════════════
    #  9. VERIFICATION SUMMARY
    # ═══════════════════════════════════════════════════════════════════════
    write_line(out, "## 9. Verification Summary")
    write_line(out)

    # Cross-check key expected values
    expected = {
        "total_examinees_best": 133804,
        "total_records_all": 178927,
        "foreign_best_combined": 24079,
        "foreign_all_records": 32514,
        "verified_foreigners_best": 24066,
        "likely_foreigners_best": 13,
        "filipinos_best": 109725,
        "pct_foreign_best": 18.00,
        "pct_foreign_all": 18.17,
    }

    actual = {
        "total_examinees_best": len(df_best),
        "total_records_all": len(df_all),
        "foreign_best_combined": len(best_foreign_full),
        "foreign_all_records": len(df_all[df_all["FOREIGNER_STATUS"].isin(FOREIGN_STATUSES_FULL)]),
        "verified_foreigners_best": len(best_verified),
        "likely_foreigners_best": len(best_likely),
        "filipinos_best": len(best_filipino),
        "pct_foreign_best": len(best_foreign_full) / len(df_best) * 100,
        "pct_foreign_all": len(df_all[df_all["FOREIGNER_STATUS"].isin(FOREIGN_STATUSES_FULL)]) / len(df_all) * 100,
    }

    write_line(out, "### Key Metrics vs Expected")
    write_line(out)
    write_line(out, "| Metric | Expected | Actual | Match |")
    write_line(out, "|--------|:--------:|:------:|:-----:|")

    all_match = True
    for key, exp_val in expected.items():
        act_val = actual[key]
        if isinstance(exp_val, float):
            match = abs(act_val - exp_val) < 0.02
            act_str = f"{act_val:.2f}"
            exp_str = f"{exp_val:.2f}"
        else:
            match = act_val == exp_val
            act_str = f"{act_val:,}"
            exp_str = f"{exp_val:,}"
        if not match:
            all_match = False
        write_line(out, f"| {key} | {exp_str} | {act_str} | {'PASS' if match else 'FAIL'} |")

    write_line(out)
    write_line(out, f"**Overall: {'ALL METRICS MATCH' if all_match else 'DISCREPANCIES FOUND' }**")
    write_line(out)
    write_line(out, "---")
    write_line(out)

    # ── Write output ───────────────────────────────────────────────────────
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"Verification output written to: {OUTPUT_PATH}")
    print(f"Overall: {'ALL METRICS MATCH' if all_match else 'DISCREPANCIES FOUND'}")

    return all_match


if __name__ == "__main__":
    main()
