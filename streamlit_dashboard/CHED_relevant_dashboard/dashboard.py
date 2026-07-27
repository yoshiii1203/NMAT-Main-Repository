"""
CHED Compliance Dashboard — CMO No. __, s. 2026
Streamlit dashboard providing data-driven evidence for NMAT cut-off policy decisions.

Target audience: CHED policymakers, HEI administrators, and education researchers.
Data source: NMAT_Exodus.parquet (Pipeline 4, 178,927 rows x 54 columns).

Usage:
    streamlit run dashboard.py
"""

import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

warnings.filterwarnings("ignore")

# ── Page Configuration ──

st.set_page_config(
    page_title="CHED Compliance Dashboard — CMO No. __, s. 2026",
    page_icon="\U0001f4ca",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Constants ──

BIN_ORDER = [f"B{i}" for i in range(1, 11)]

PAL_UNI = {
    "Public": "#1f77b4",
    "Private": "#ff7f0e",
    "Foreign": "#9467bd",
    "Not Specified": "#7f7f7f",
}

PAL_BIN = {
    "B1": "#8B0000",
    "B2": "#B22222",
    "B3": "#D9534F",
    "B4": "#F0AD4E",
    "B5": "#FFD166",
    "B6": "#A0D468",
    "B7": "#66C2A5",
    "B8": "#41B6C4",
    "B9": "#2C7FB8",
    "B10": "#253494",
}

PAL_COURSE = {
    "Medical & Allied": "#1f77b4",
    "Natural Sciences": "#2ca02c",
    "Social & Behavioral Sciences": "#ff7f0e",
    "Education": "#d62728",
    "Engineering & Technology": "#9467bd",
    "Other": "#7f7f7f",
}

PAL_SEX = {"Female": "#e377c2", "Male": "#1f77b4"}

YEAR_RANGE = (2006, 2018)


# ── Helper Functions ──


def bin_at_or_above(b: str, threshold_b: str) -> bool:
    """Check if bin b is at or above threshold_b in BIN_ORDER."""
    if pd.isna(b):
        return False
    try:
        return BIN_ORDER.index(b) >= BIN_ORDER.index(threshold_b)
    except (ValueError, IndexError):
        return False


def find_data_path() -> Path:
    """Locate NMAT_Exodus.parquet. Checks current dir first, then dataset/."""
    candidates = [
        Path("NMAT_Exodus.parquet"),
        Path("dataset/NMAT_Exodus.parquet"),
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError(
        "Could not find NMAT_Exodus.parquet. "
        "Place it in the app root or in ./dataset/."
    )


# ── Data Loading ──


@st.cache_data
def load_data():
    """Load NMAT_Exodus.parquet and return pre-computed subsets."""
    path = find_data_path()
    df = pd.read_parquet(path)

    # Ensure Year is integer
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")

    # Best NMAT record per examinee
    best = df[df["IS_BEST_NMAT_RECORD"] == True].copy()

    # Best records within trend window (2006–2018)
    besttrend = best[best["Year"].between(YEAR_RANGE[0], YEAR_RANGE[1], inclusive="both")].copy()

    # Best records observable for PLE (Year <= 2014, allowing 4-year licensure window)
    bestobs = besttrend[besttrend["Year"] <= 2014].copy()

    return df, best, besttrend, bestobs


# ── Main App ──


def main():
    # Title area
    st.title("CHED Compliance Dashboard — CMO No. __, s. 2026")
    st.caption(
        "Data-Driven Evidence for NMAT Cut-Off Policy. "
        "This dashboard supports CHED, HEI administrators, and education researchers "
        "in understanding the empirical basis for the amended NMAT cut-off score policy. "
        "All figures are computed from NMAT_Exodus.parquet (Pipeline 4, 178,927 best records, 2006\u20132018)."
    )

    # Load data
    with st.spinner("Loading NMAT data..."):
        df, best, besttrend, bestobs = load_data()

    # Pre-compute commonly used flags
    best["IS_B4_OR_ABOVE"] = best["PercentileBin"].apply(lambda b: bin_at_or_above(b, "B4"))
    best["IS_B5_OR_ABOVE"] = best["PercentileBin"].apply(lambda b: bin_at_or_above(b, "B5"))
    besttrend["IS_B4_OR_ABOVE"] = besttrend["PercentileBin"].apply(lambda b: bin_at_or_above(b, "B4"))
    besttrend["IS_B5_OR_ABOVE"] = besttrend["PercentileBin"].apply(lambda b: bin_at_or_above(b, "B5"))

    st.divider()

    # ── Navigation Tabs ──

    tab_names = [
        "Overview",
        "National Benchmark",
        "Cut-Off Scenarios",
        "Per-HEI Analysis",
        "Foreign Students",
        "Demographics",
        "PLE Alignment",
        "Trends",
        "Data Appendix",
    ]
    tabs = st.tabs(tab_names)

    # ════════════════════════════════════════════════════════════════
    # TAB 1: OVERVIEW
    # ════════════════════════════════════════════════════════════════
    with tabs[0]:
        st.header("Overview")
        st.subheader("Policy Context")
        st.markdown(
            "CMO No. __, s. 2026 amends the NMAT cut-off policy to provide flexibility for "
            "Philippine Higher Education Institutions (PHEIs) based on their PLE performance. "
            "Institutions with PLE performance above the national 5-year rolling average may set "
            "their NMAT cut-off at the **30th percentile**; those below must maintain the "
            "**40th percentile**. Additionally, State Universities and Colleges (SUCs) are subject "
            "to a 10-slot cap on foreign student enrollment per incoming freshmen class."
        )

        # Key metrics row
        n_total = len(best)
        n_years = int(best["Year"].nunique())
        linkage_rate = round(bestobs["IS_PLE_ANALYSIS_SAFE"].sum() / len(bestobs) * 100, 2)
        n_foreign = len(best[best["FOREIGNER_STATUS"] != "Filipino"])

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Examinees (best records)", f"{n_total:,}")
        m2.metric("Years Covered", f"{n_years} ({YEAR_RANGE[0]}\u2013{YEAR_RANGE[1]})")
        m3.metric("NMAT\u2013PLE Linkage Rate", f"{linkage_rate:.2f}%",
                  help="Share of NMAT examinees (observable cohort) found in PLE passer data. NOT a PLE pass rate.")
        m4.metric("Foreign Examinees", f"{n_foreign:,}",
                  help="Examinees classified as Verified Foreigner or Likely Foreigner on best record.")

        st.divider()

        # Data limitations
        st.info(
            "\ud83d\udcdd **Critical Data Limitation:** We cannot compute PLE pass rates. "
            "The PLE data contains passers only (43,630 rows, no fail records). "
            "What we report is the **NMAT-to-PLE linkage rate** \u2014 the share of NMAT examinees "
            "who are found in the PLE passer dataset. This is an evidence-based indicator of "
            "the relationship between NMAT scores and eventual PLE passage, but it is **not** "
            "the same as an official PLE pass rate.\n\n"
            "**Foreign student data:** Counts reflect NMAT examinees, not enrolled students. "
            "The 10-slot cap applies to enrollment, which we cannot verify.\n\n"
            "**Temporal limitation:** NMAT data covers 2006\u20132018 only. The CMO takes effect "
            "AY 2026\u20132027. This is historical analysis, not current monitoring."
        )

        st.subheader("How to Use This Dashboard")
        st.markdown(
            "Navigate through the tabs above to explore different aspects of the data:\n\n"
            "- **National Benchmark** \u2014 NMAT\u2013PLE linkage rates with 5-year rolling averages.\n"
            "- **Cut-Off Scenarios** \u2014 Comparison of 30th vs 40th percentile thresholds.\n"
            "- **Per-HEI Analysis** \u2014 Score distributions for individual institutions.\n"
            "- **Foreign Students** \u2014 Profile of foreign examinees and SUC slot analysis.\n"
            "- **Demographics** \u2014 Breakdowns by sex and course group.\n"
            "- **PLE Alignment** \u2014 Linkage rates by percentile bin and institution type.\n"
            "- **Trends** \u2014 Historical score and volume trends (2006\u20132018).\n"
            "- **Data Appendix** \u2014 Methodology, data dictionary, and limitations."
        )

    # ════════════════════════════════════════════════════════════════
    # TAB 2: NATIONAL BENCHMARK
    # ════════════════════════════════════════════════════════════════
    with tabs[1]:
        st.header("National NMAT\u2013PLE Linkage Benchmark")
        st.markdown(
            "Annual linkage rates between NMAT examinees and PLE passers, with 5-year rolling average. "
            "The CHED amendment uses the 5-year rolling average as the national benchmark: PHEIs above "
            "this benchmark may set cut-off at the 30th percentile; those below must maintain 40th."
        )

        # Compute annual linkage rates
        if bestobs.empty:
            st.info("No observable best-record rows available. Try adjusting filters.")
        else:
            annual_linkage = (
                bestobs.groupby("Year", observed=True)
                .agg(
                    n_examinees=("IS_PLE_ANALYSIS_SAFE", "size"),
                    n_confirmed_ple=("IS_PLE_ANALYSIS_SAFE", "sum"),
                )
                .reset_index()
            )
            annual_linkage["Linkage Rate (%)"] = (
                annual_linkage["n_confirmed_ple"] / annual_linkage["n_examinees"] * 100
            ).round(2)
            annual_linkage["5yr Rolling Avg (%)"] = (
                annual_linkage["Linkage Rate (%)"].rolling(window=5, min_periods=3).mean().round(2)
            )

            # Metric cards
            overall_rate = round(bestobs["IS_PLE_ANALYSIS_SAFE"].sum() / len(bestobs) * 100, 2)
            latest_5yr = annual_linkage[annual_linkage["5yr Rolling Avg (%)"].notna()].iloc[-1]
            observable_cohort_size = len(bestobs)

            m1, m2, m3 = st.columns(3)
            m1.metric(
                "Overall Linkage Rate",
                f"{overall_rate:.2f}%",
                help="Total confirmed PLE passers / total observable best examinees.",
            )
            m2.metric(
                "Latest 5yr National Avg (Benchmark)",
                f"{latest_5yr['5yr Rolling Avg (%)']:.2f}%",
                delta=None,
                help="The benchmark PHEIs must beat to qualify for 30th percentile cut-off.",
            )
            m3.metric(
                "Observable Cohort Size",
                f"{observable_cohort_size:,}",
                help="Best records with Year <= 2014 (allowing 4-year PLE licensure window).",
            )

            # Line chart: annual linkage + 5yr rolling avg
            fig_natl = go.Figure()
            fig_natl.add_trace(go.Scatter(
                x=annual_linkage["Year"].astype(str),
                y=annual_linkage["Linkage Rate (%)"],
                mode="lines+markers",
                name="Annual linkage rate",
                line=dict(color="#1f77b4", width=2),
                hovertemplate="Year: %{x}<br>Linkage: %{y:.1f}%<extra></extra>",
            ))
            fig_natl.add_trace(go.Scatter(
                x=annual_linkage["Year"].astype(str),
                y=annual_linkage["5yr Rolling Avg (%)"],
                mode="lines+markers",
                name="5-year rolling avg",
                line=dict(color="#d62728", width=2, dash="dash"),
                hovertemplate="Year: %{x}<br>5yr avg: %{y:.1f}%<extra></extra>",
            ))
            fig_natl.update_layout(
                title="Annual NMAT\u2013PLE Linkage Rate with 5-Year Rolling Average",
                xaxis_title="NMAT Year",
                yaxis_title="Linkage Rate (%)",
                height=420,
                hovermode="x unified",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            )
            st.plotly_chart(fig_natl, use_container_width=True, key="fig_t2_natl_benchmark")

            # Year-by-year table
            display_cols = {
                "Year": "NMAT Year",
                "n_examinees": "Examinees (observable)",
                "n_confirmed_ple": "Confirmed PLE Passers",
                "Linkage Rate (%)": "Linkage Rate (%)",
                "5yr Rolling Avg (%)": "5yr Rolling Avg (%)",
            }
            tbl_annual = annual_linkage.rename(columns=display_cols)[list(display_cols.values())]
            st.subheader("Year-by-Year Breakdown")
            st.dataframe(tbl_annual, use_container_width=True, hide_index=True)

            col_dl1, _ = st.columns([1, 3])
            with col_dl1:
                st.download_button(
                    "Download CSV",
                    data=annual_linkage.to_csv(index=False).encode("utf-8"),
                    file_name="ched_national_benchmark.csv",
                    mime="text/csv",
                )

            st.caption(
                "NMAT-to-PLE linkage rate = share of NMAT examinees found in PLE passer data. "
                "This is NOT a PLE pass rate. The 5-year rolling average is computed with a minimum "
                "of 3 years of data."
            )

    # ════════════════════════════════════════════════════════════════
    # TAB 3: CUT-OFF SCENARIOS
    # ════════════════════════════════════════════════════════════════
    with tabs[2]:
        st.header("30th vs 40th Percentile Cut-Off Analysis")
        st.markdown(
            "Comparison of examinee counts and PLE outcomes under the proposed 30th percentile (B4+) "
            "and 40th percentile (B5+) cut-off thresholds, broken down by university type."
        )

        if besttrend.empty:
            st.info("No data available for cut-off scenario analysis.")
        else:
            # Build scenario comparison
            scenario_rows = []
            for uni_type in ["All", "Public", "Private", "Foreign"]:
                sub = besttrend if uni_type == "All" else besttrend[besttrend["UNI_TYPE"] == uni_type]
                sub_obs = bestobs if uni_type == "All" else bestobs[bestobs["UNI_TYPE"] == uni_type]

                for label, threshold_bin, col_label in [
                    ("30th percentile (B4+)", "B4", "B4+"),
                    ("40th percentile (B5+)", "B5", "B5+"),
                ]:
                    admitted = sub[sub["PercentileBin"].apply(lambda b: bin_at_or_above(b, threshold_bin))]
                    ple_cohort = sub_obs[sub_obs["PercentileBin"].apply(lambda b: bin_at_or_above(b, threshold_bin))]
                    scenario_rows.append({
                        "University Type": uni_type,
                        "Cut-Off": col_label,
                        "Threshold": label,
                        "Admitted (best records)": len(admitted),
                        "PLE Passers (observable)": int(ple_cohort["IS_PLE_ANALYSIS_SAFE"].sum())
                        if len(ple_cohort) > 0 else 0,
                        "PLE Linkage Rate (%)": round(
                            ple_cohort["IS_PLE_ANALYSIS_SAFE"].mean() * 100, 2
                        ) if len(ple_cohort) > 0 else 0.0,
                        "Median Percentile": round(admitted["NMS_PER_num"].median(), 1)
                        if len(admitted) > 0 else 0.0,
                    })

            scenario_df = pd.DataFrame(scenario_rows)

            # Metrics
            total_b4 = int(scenario_df.loc[
                (scenario_df["University Type"] == "All") & (scenario_df["Cut-Off"] == "B4+"),
                "Admitted (best records)"
            ].sum())
            total_b5 = int(scenario_df.loc[
                (scenario_df["University Type"] == "All") & (scenario_df["Cut-Off"] == "B5+"),
                "Admitted (best records)"
            ].sum())
            diff = total_b4 - total_b5

            m1, m2, m3 = st.columns(3)
            m1.metric("Total at B4+ (30th percentile)", f"{total_b4:,}",
                      help="Examinees scoring at or above 30th percentile.")
            m2.metric("Total at B5+ (40th percentile)", f"{total_b5:,}",
                      help="Examinees scoring at or above 40th percentile.")
            m3.metric("Difference (B4+ \u2212 B5+)", f"{diff:,}",
                      delta=f"{-diff:,}" if diff > 0 else f"{diff:,}",
                      help="Additional examinees admitted at 30th vs 40th percentile cut-off.")

            # Grouped bar chart by UNI_TYPE
            chart_df = scenario_df[scenario_df["University Type"] != "All"].copy()
            fig_scenario = px.bar(
                chart_df,
                x="University Type",
                y="Admitted (best records)",
                color="Cut-Off",
                barmode="group",
                color_discrete_map={"B4+": "#F0AD4E", "B5+": "#2C7FB8"},
                title="Admitted Examinees by Cut-Off Threshold and University Type",
                text_auto=",",
            )
            fig_scenario.update_layout(height=400, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
            st.plotly_chart(fig_scenario, use_container_width=True, key="fig_t3_scenario_bar")

            # Scenario comparison table by year
            st.subheader("Scenario Comparison by Year")
            yearly_scenario_rows = []
            for year in sorted(besttrend["Year"].unique()):
                sub_yr = besttrend[besttrend["Year"] == year]
                sub_yr_obs = bestobs[bestobs["Year"] == year]
                for col_label, threshold_bin in [("B4+ (30th)", "B4"), ("B5+ (40th)", "B5")]:
                    admitted = sub_yr[sub_yr["PercentileBin"].apply(lambda b: bin_at_or_above(b, threshold_bin))]
                    ple_cohort = sub_yr_obs[sub_yr_obs["PercentileBin"].apply(lambda b: bin_at_or_above(b, threshold_bin))]
                    yearly_scenario_rows.append({
                        "Year": int(year),
                        "Cut-Off": col_label,
                        "Admitted": len(admitted),
                        "Median Percentile": round(admitted["NMS_PER_num"].median(), 1)
                        if len(admitted) > 0 else None,
                    })

            yr_scenario_df = pd.DataFrame(yearly_scenario_rows)
            pivot_yr = yr_scenario_df.pivot_table(
                index="Year", columns="Cut-Off", values=["Admitted", "Median Percentile"],
                aggfunc="first",
            )
            # Flatten columns
            pivot_yr.columns = [f"{col[0]} - {col[1]}" for col in pivot_yr.columns]
            pivot_yr = pivot_yr.reset_index()
            st.dataframe(pivot_yr, use_container_width=True, hide_index=True)

            col_dl2, _ = st.columns([1, 3])
            with col_dl2:
                st.download_button(
                    "Download Scenario CSV",
                    data=scenario_df.to_csv(index=False).encode("utf-8"),
                    file_name="ched_cutoff_scenarios.csv",
                    mime="text/csv",
                )

            st.caption(
                "Methodology: 'Admitted' counts best NMAT records at or above the stated percentile threshold. "
                "PLE-linked metrics use the observable cohort (Year <= 2014) to avoid misclassifying later "
                "cohorts as non-passers before their licensure window closes."
            )

    # ════════════════════════════════════════════════════════════════
    # TAB 4: PER-HEI ANALYSIS
    # ════════════════════════════════════════════════════════════════
    with tabs[3]:
        st.header("Per-Institution NMAT Score Distribution")
        st.markdown(
            "Summary statistics and percentile bin distributions for each institution. "
            "Only institutions with at least 5 best-record examinees are included."
        )

        if besttrend.empty:
            st.info("No data available.")
        else:
            # Compute per-HEI stats
            hei_stats_list = []
            for hei in sorted(besttrend["UNIVERSITY"].dropna().unique()):
                hei_data = besttrend[besttrend["UNIVERSITY"] == hei]
                hei_obs = bestobs[bestobs["UNIVERSITY"] == hei] if not bestobs.empty else pd.DataFrame()

                if len(hei_data) < 5:
                    continue

                bin_dist = hei_data["PercentileBin"].value_counts().reindex(BIN_ORDER).fillna(0)
                total = bin_dist.sum()
                b4_pct = round(
                    bin_dist.loc[bin_dist.index.isin(["B4", "B5", "B6", "B7", "B8", "B9", "B10"])].sum()
                    / total * 100, 1
                ) if total > 0 else 0.0
                b5_pct = round(
                    bin_dist.loc[bin_dist.index.isin(["B5", "B6", "B7", "B8", "B9", "B10"])].sum()
                    / total * 100, 1
                ) if total > 0 else 0.0

                bin_dist_str = ", ".join(
                    [f"{b}: {int(bin_dist[b])}" for b in BIN_ORDER if bin_dist[b] > 0]
                )

                hei_stats_list.append({
                    "HEI": hei,
                    "Type": hei_data["UNI_TYPE"].mode().iloc[0] if not hei_data["UNI_TYPE"].mode().empty else "Unknown",
                    "N": len(hei_data),
                    "Median %ile": round(hei_data["NMS_PER_num"].median(), 1),
                    "Mean %ile": round(hei_data["NMS_PER_num"].mean(), 1),
                    "B4+ %": b4_pct,
                    "B5+ %": b5_pct,
                    "Bin Distribution": bin_dist_str,
                    "PLE Linkage Rate (%)": round(
                        hei_obs["IS_PLE_ANALYSIS_SAFE"].mean() * 100, 1
                    ) if not hei_obs.empty and len(hei_obs) >= 5 else None,
                })

            hei_stats_df = pd.DataFrame(hei_stats_list)
            if hei_stats_df.empty:
                st.info("No institutions with >=5 examinees found.")
            else:
                hei_stats_df = hei_stats_df.sort_values("N", ascending=False).reset_index(drop=True)

                # Search box
                search_query = st.text_input(
                    "Filter by institution name",
                    placeholder="Type an HEI name to filter...",
                    key="hei_search",
                )
                if search_query:
                    mask = hei_stats_df["HEI"].str.contains(search_query, case=False, na=False)
                    filtered_df = hei_stats_df[mask]
                else:
                    filtered_df = hei_stats_df

                st.markdown(f"**Showing {len(filtered_df):,} of {len(hei_stats_df):,} institutions**")
                st.dataframe(
                    filtered_df,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "Median %ile": st.column_config.NumberColumn(format="%.1f"),
                        "Mean %ile": st.column_config.NumberColumn(format="%.1f"),
                        "B4+ %": st.column_config.NumberColumn(format="%.1f%%"),
                        "B5+ %": st.column_config.NumberColumn(format="%.1f%%"),
                        "PLE Linkage Rate (%)": st.column_config.NumberColumn(format="%.1f%%"),
                    },
                )

                col_dl3, _ = st.columns([1, 3])
                with col_dl3:
                    st.download_button(
                        "Download HEI Data CSV",
                        data=hei_stats_df.to_csv(index=False).encode("utf-8"),
                        file_name="ched_per_hei_stats.csv",
                        mime="text/csv",
                    )

                st.caption(
                    "Minimum 5 examinees required for reporting. Bin Distribution shows counts per bin (B1\u2013B10). "
                    "PLE Linkage Rate requires >=5 observable examinees (Year <= 2014)."
                )

    # ════════════════════════════════════════════════════════════════
    # TAB 5: FOREIGN STUDENTS
    # ════════════════════════════════════════════════════════════════
    with tabs[4]:
        st.header("Foreign Examinee Profile")
        st.markdown(
            "Profile of foreign NMAT examinees in the dataset. "
            "The CHED amendment caps foreign student enrollment at 10 per incoming freshmen class at SUCs. "
            "Note that we count NMAT examinees, not actual enrollees."
        )

        foreign = besttrend[besttrend["FOREIGNER_STATUS"] != "Filipino"].copy()

        if foreign.empty:
            st.info("No foreign examinee records found.")
        else:
            # Metrics
            n_foreign_total = len(foreign)
            n_foreign_suc = len(foreign[foreign["UNI_TYPE"] == "Public"])
            top_nat = foreign["CITIZENSHIP_FINAL"].value_counts().index[0] if not foreign.empty else "N/A"
            median_pct = round(foreign["NMS_PER_num"].median(), 1)

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Total Foreign Examinees", f"{n_foreign_total:,}")
            m2.metric("Foreign at SUCs", f"{n_foreign_suc:,}")
            m3.metric("Top Nationality", top_nat)
            m4.metric("Median Percentile", median_pct)

            # Top 15 nationalities bar chart
            top_nats = foreign["CITIZENSHIP_FINAL"].value_counts().head(15).reset_index()
            top_nats.columns = ["Nationality", "Count"]

            fig_nat = px.bar(
                top_nats,
                x="Count",
                y="Nationality",
                orientation="h",
                title="Top 15 Nationalities Among Foreign NMAT Examinees",
                color="Count",
                color_continuous_scale="Blues",
                text_auto=",",
            )
            fig_nat.update_layout(height=450, yaxis=dict(categoryorder="total ascending"))
            st.plotly_chart(fig_nat, use_container_width=True, key="fig_t5_top_nats")

            # Per-SUC foreign examinee counts
            st.subheader("Foreign Examinee Counts by SUC and Year")
            suc_foreign = foreign[foreign["UNI_TYPE"] == "Public"]
            if not suc_foreign.empty:
                suc_yr = (
                    suc_foreign.groupby(["UNIVERSITY", "Year"], observed=True)
                    .size()
                    .reset_index(name="Foreign Count")
                )
                suc_yr["Over 10-Slot Cap"] = suc_yr["Foreign Count"] > 10
                suc_yr["Year"] = suc_yr["Year"].astype(str)

                st.dataframe(
                    suc_yr.sort_values(["Year", "Foreign Count"], ascending=[True, False]),
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "Foreign Count": st.column_config.NumberColumn(format="%d"),
                        "Over 10-Slot Cap": st.column_config.CheckboxColumn(),
                    },
                )

                # Summary: SUCs with most foreign examinees
                st.subheader("Top SUCs by Foreign Examinee Volume")
                suc_summary = (
                    suc_yr.groupby("UNIVERSITY")
                    .agg(
                        Max_Foreign=("Foreign Count", "max"),
                        Total_Foreign=("Foreign Count", "sum"),
                        Years_Over_Cap=("Over 10-Slot Cap", "sum"),
                    )
                    .reset_index()
                    .sort_values("Max_Foreign", ascending=False)
                    .head(20)
                )
                suc_summary.columns = ["University", "Max Foreign (1 yr)", "Total Foreign", "Years Over Cap"]
                st.dataframe(suc_summary, use_container_width=True, hide_index=True)

                col_dl4, _ = st.columns([1, 3])
                with col_dl4:
                    st.download_button(
                        "Download SUC Foreign Data CSV",
                        data=suc_yr.to_csv(index=False).encode("utf-8"),
                        file_name="ched_suc_foreign.csv",
                        mime="text/csv",
                    )
            else:
                st.info("No foreign examinees recorded at SUCs under current filters.")

            st.warning(
                "Counts reflect NMAT examinees, not enrolled students. The 10-slot cap applies to "
                "enrollment, which requires data from HEIs that is not available in this dataset."
            )

    # ════════════════════════════════════════════════════════════════
    # TAB 6: DEMOGRAPHICS
    # ════════════════════════════════════════════════════════════════
    with tabs[5]:
        st.header("Demographic Profiles")
        st.markdown(
            "Distribution of NMAT examinees by sex and course group, "
            "with corresponding score percentiles."
        )

        col_dem1, col_dem2 = st.columns(2)

        # ── By Sex ──
        with col_dem1:
            st.subheader("By Sex")
            sex_data = besttrend.dropna(subset=["SEX"]).copy()
            if not sex_data.empty:
                sex_summary = (
                    sex_data.groupby("SEX", observed=True)
                    .agg(
                        Count=("SEX", "size"),
                        Median_Percentile=("NMS_PER_num", "median"),
                        Mean_Percentile=("NMS_PER_num", "mean"),
                    )
                    .reset_index()
                )
                sex_summary["Count"] = sex_summary["Count"].astype(int)
                sex_summary["Median_Percentile"] = sex_summary["Median_Percentile"].round(1)
                sex_summary["Mean_Percentile"] = sex_summary["Mean_Percentile"].round(1)

                st.dataframe(
                    sex_summary.rename(columns={
                        "SEX": "Sex",
                        "Count": "N",
                        "Median_Percentile": "Median %ile",
                        "Mean_Percentile": "Mean %ile",
                    }),
                    use_container_width=True,
                    hide_index=True,
                )

                fig_sex = px.bar(
                    sex_summary,
                    x="SEX",
                    y="Count",
                    color="SEX",
                    color_discrete_map=PAL_SEX,
                    title="Examinee Count by Sex",
                    text_auto=",",
                )
                fig_sex.update_layout(height=350, showlegend=False)
                st.plotly_chart(fig_sex, use_container_width=True, key="fig_t6_sex_bar")
            else:
                st.info("No sex data available.")

        # ── By Course Group ──
        with col_dem2:
            st.subheader("By Course Group")
            course_data = besttrend.dropna(subset=["CourseGroup"]).copy()
            if not course_data.empty:
                course_summary = (
                    course_data.groupby("CourseGroup", observed=True)
                    .agg(
                        Count=("CourseGroup", "size"),
                        Median_Percentile=("NMS_PER_num", "median"),
                        Mean_Percentile=("NMS_PER_num", "mean"),
                    )
                    .reset_index()
                )
                course_summary["Count"] = course_summary["Count"].astype(int)
                course_summary["Median_Percentile"] = course_summary["Median_Percentile"].round(1)
                course_summary["Mean_Percentile"] = course_summary["Mean_Percentile"].round(1)

                st.dataframe(
                    course_summary.rename(columns={
                        "CourseGroup": "Course Group",
                        "Count": "N",
                        "Median_Percentile": "Median %ile",
                        "Mean_Percentile": "Mean %ile",
                    }),
                    use_container_width=True,
                    hide_index=True,
                )

                fig_course = px.bar(
                    course_summary,
                    x="CourseGroup",
                    y="Count",
                    color="CourseGroup",
                    color_discrete_map=PAL_COURSE,
                    title="Examinee Count by Course Group",
                    text_auto=",",
                )
                fig_course.update_layout(height=350, showlegend=False, xaxis_tickangle=-30)
                st.plotly_chart(fig_course, use_container_width=True, key="fig_t6_course_bar")
            else:
                st.info("No course group data available.")

        # Combined: Percentile distribution by course group
        st.subheader("Percentile Distribution by Course Group")
        if not course_data.empty:
            course_bin = (
                course_data.groupby(["CourseGroup", "PercentileBin"], observed=True)
                .size()
                .reset_index(name="Count")
            )
            fig_course_bin = px.bar(
                course_bin,
                x="PercentileBin",
                y="Count",
                color="CourseGroup",
                barmode="group",
                color_discrete_map=PAL_COURSE,
                title="Percentile Bin Distribution by Course Group",
                category_orders={"PercentileBin": BIN_ORDER},
            )
            fig_course_bin.update_layout(height=400, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
            st.plotly_chart(fig_course_bin, use_container_width=True, key="fig_t6_course_bin")

        st.caption("All demographic figures use best-record NMAT data from 2006\u20132018.")

    # ════════════════════════════════════════════════════════════════
    # TAB 7: PLE ALIGNMENT
    # ════════════════════════════════════════════════════════════════
    with tabs[6]:
        st.header("NMAT\u2013PLE Alignment Analysis")
        st.markdown(
            "How NMAT percentile bins and university types relate to PLE linkage. "
            "This analysis uses the observable cohort (Year <= 2014) to ensure a valid "
            "licensure observation window."
        )

        if bestobs.empty:
            st.info("No observable cohort data available.")
        else:
            # Linkage rate by percentile bin
            bin_linkage = (
                bestobs.dropna(subset=["PercentileBin"])
                .groupby("PercentileBin", observed=True)
                .agg(
                    N=("IS_PLE_ANALYSIS_SAFE", "size"),
                    Confirmed_PLE=("IS_PLE_ANALYSIS_SAFE", "sum"),
                )
                .reset_index()
            )
            bin_linkage["Linkage Rate (%)"] = (
                bin_linkage["Confirmed_PLE"] / bin_linkage["N"] * 100
            ).round(2)

            # Metric cards for each bin tier
            st.subheader("Linkage Rate by Percentile Bin Tier")
            bin_tiers = {
                "Bottom (B1\u2013B3)": ["B1", "B2", "B3"],
                "Middle (B4\u2013B7)": ["B4", "B5", "B6", "B7"],
                "Top (B8\u2013B10)": ["B8", "B9", "B10"],
            }
            tier_cols = st.columns(3)
            for i, (tier_name, bins) in enumerate(bin_tiers.items()):
                tier_data = bin_linkage[bin_linkage["PercentileBin"].isin(bins)]
                if not tier_data.empty:
                    tier_rate = round(
                        tier_data["Confirmed_PLE"].sum() / tier_data["N"].sum() * 100, 2
                    )
                    tier_n = int(tier_data["N"].sum())
                    tier_cols[i].metric(tier_name, f"{tier_rate:.2f}%", help=f"N = {tier_n:,}")
                else:
                    tier_cols[i].metric(tier_name, "N/A")

            # Line chart: linkage rate by bin
            fig_bin_link = px.line(
                bin_linkage,
                x="PercentileBin",
                y="Linkage Rate (%)",
                markers=True,
                category_orders={"PercentileBin": BIN_ORDER},
                title="NMAT\u2013PLE Linkage Rate by Percentile Bin",
                text="Linkage Rate (%)",
            )
            fig_bin_link.update_traces(
                texttemplate="%{text:.1f}%",
                textposition="top center",
                line=dict(color="#1f77b4", width=3),
                marker=dict(size=10, color="#1f77b4"),
            )
            fig_bin_link.update_layout(height=400, xaxis_title="Percentile Bin", yaxis_title="Linkage Rate (%)")
            st.plotly_chart(fig_bin_link, use_container_width=True, key="fig_t7_bin_link")

            # Heatmap: bin x uni_type
            st.subheader("Linkage Rate Heatmap: Percentile Bin \u00d7 University Type")
            heatmap_data = (
                bestobs.dropna(subset=["PercentileBin", "UNI_TYPE"])
                .groupby(["PercentileBin", "UNI_TYPE"], observed=True)
                .agg(
                    N=("IS_PLE_ANALYSIS_SAFE", "size"),
                    Confirmed_PLE=("IS_PLE_ANALYSIS_SAFE", "sum"),
                )
                .reset_index()
            )
            heatmap_data["Linkage Rate (%)"] = (
                heatmap_data["Confirmed_PLE"] / heatmap_data["N"] * 100
            ).round(2)

            pivot_heat = heatmap_data.pivot_table(
                index="PercentileBin",
                columns="UNI_TYPE",
                values="Linkage Rate (%)",
                aggfunc="first",
            )
            pivot_heat = pivot_heat.reindex(index=BIN_ORDER)
            uni_types_order = [t for t in ["Public", "Private", "Foreign", "Not Specified"] if t in pivot_heat.columns]
            pivot_heat = pivot_heat[uni_types_order]

            fig_heat = px.imshow(
                pivot_heat,
                text_auto=".1f",
                aspect="auto",
                color_continuous_scale="RdYlBu",
                title="Linkage Rate (%) by Bin and University Type",
                labels=dict(x="University Type", y="Percentile Bin", color="Linkage Rate (%)"),
            )
            fig_heat.update_layout(height=450)
            st.plotly_chart(fig_heat, use_container_width=True, key="fig_t7_heatmap")

            # Full breakdown table
            st.subheader("Full Breakdown: Bin \u00d7 University Type")
            full_table = heatmap_data.pivot_table(
                index="PercentileBin",
                columns="UNI_TYPE",
                values=["N", "Confirmed_PLE", "Linkage Rate (%)"],
                aggfunc="first",
            )
            # Flatten columns
            full_table.columns = [f"{col[1]} - {col[0]}" for col in full_table.columns]
            full_table = full_table.reindex(index=BIN_ORDER).reset_index()
            full_table = full_table.rename(columns={"PercentileBin": "Bin"})
            st.dataframe(full_table, use_container_width=True, hide_index=True)

            col_dl5, _ = st.columns([1, 3])
            with col_dl5:
                st.download_button(
                    "Download PLE Alignment CSV",
                    data=heatmap_data.to_csv(index=False).encode("utf-8"),
                    file_name="ched_ple_alignment.csv",
                    mime="text/csv",
                )

            st.caption(
                "Linkage rate = share of NMAT examinees in each bin/type group who are found in PLE passer data. "
                "This is NOT a PLE pass rate."
            )

    # ════════════════════════════════════════════════════════════════
    # TAB 8: TRENDS
    # ════════════════════════════════════════════════════════════════
    with tabs[7]:
        st.header("Historical Trends (2006\u20132018)")
        st.markdown(
            "Year-over-year trends in NMAT scores, examinee volume, and percentile distribution."
        )

        if besttrend.empty:
            st.info("No trend data available.")
        else:
            # Yearly summary
            yearly = (
                besttrend.groupby("Year", observed=True)
                .agg(
                    Total_Examinees=("Year", "size"),
                    Median_Percentile=("NMS_PER_num", "median"),
                    Mean_Percentile=("NMS_PER_num", "mean"),
                    Pct_Female=("SEX", lambda x: (x == "Female").mean() * 100),
                )
                .reset_index()
            )
            yearly["Total_Examinees"] = yearly["Total_Examinees"].astype(int)
            yearly["Median_Percentile"] = yearly["Median_Percentile"].round(1)
            yearly["Mean_Percentile"] = yearly["Mean_Percentile"].round(1)
            yearly["Pct_Female"] = yearly["Pct_Female"].round(1)
            yearly["Year"] = yearly["Year"].astype(str)

            # Score trend line chart
            fig_score = go.Figure()
            fig_score.add_trace(go.Scatter(
                x=yearly["Year"],
                y=yearly["Median_Percentile"],
                mode="lines+markers",
                name="Median Percentile",
                line=dict(color="#1f77b4", width=2),
                hovertemplate="Year: %{x}<br>Median: %{y:.1f}<extra></extra>",
            ))
            fig_score.add_trace(go.Scatter(
                x=yearly["Year"],
                y=yearly["Mean_Percentile"],
                mode="lines+markers",
                name="Mean Percentile",
                line=dict(color="#d62728", width=2, dash="dash"),
                hovertemplate="Year: %{x}<br>Mean: %{y:.1f}<extra></extra>",
            ))
            fig_score.update_layout(
                title="NMAT Percentile Score Trends (2006\u20132018)",
                xaxis_title="NMAT Year",
                yaxis_title="Percentile Score",
                height=400,
                hovermode="x unified",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            )
            st.plotly_chart(fig_score, use_container_width=True, key="fig_t8_score_trend")

            # Volume trend bar chart
            fig_vol = px.bar(
                yearly,
                x="Year",
                y="Total_Examinees",
                title="Annual Examinee Volume (2006\u20132018)",
                color="Total_Examinees",
                color_continuous_scale="Blues",
                text_auto=",",
            )
            fig_vol.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_vol, use_container_width=True, key="fig_t8_vol_trend")

            # Yearly summary table
            st.subheader("Yearly Summary")
            st.dataframe(
                yearly.rename(columns={
                    "Year": "NMAT Year",
                    "Total_Examinees": "Total Examinees",
                    "Median_Percentile": "Median %ile",
                    "Mean_Percentile": "Mean %ile",
                    "Pct_Female": "Female (%)",
                }),
                use_container_width=True,
                hide_index=True,
            )

            col_dl6, _ = st.columns([1, 3])
            with col_dl6:
                st.download_button(
                    "Download Yearly Trends CSV",
                    data=yearly.to_csv(index=False).encode("utf-8"),
                    file_name="ched_yearly_trends.csv",
                    mime="text/csv",
                )

            st.caption("All figures use best-record NMAT data. Percentile scores are NMS_PER_num.")

    # ════════════════════════════════════════════════════════════════
    # TAB 9: DATA APPENDIX
    # ════════════════════════════════════════════════════════════════
    with tabs[8]:
        st.header("Methodology & Data Sources")
        st.markdown(
            "This appendix documents the data pipeline, key terms, and limitations "
            "for transparency and reproducibility."
        )

        st.subheader("Data Source")
        st.markdown(
            "**NMAT_Exodus.parquet** \u2014 the final enriched dataset from Pipeline 4, containing "
            "178,927 rows \u00d7 54 columns. This dataset integrates:\n\n"
            "- Raw NMAT scores and percentile bins (B1\u2013B10) for each examinee\n"
            "- Demographic data (sex, course group, institution, university type)\n"
            "- PLE match status (IS_PLE_ANALYSIS_SAFE, IS_PLE_PASSER)\n"
            "- Citizenship classification (CITIZENSHIP_FINAL, FOREIGNER_STATUS)\n"
            "- Best-record flag (IS_BEST_NMAT_RECORD) ensuring one record per examinee\n\n"
            "The original data sources are:\n"
            "- **NMAT historical database** (2006\u20132018) from CEM\n"
            "- **PLE_DATA.csv** (43,630 rows, 1 column: PLE_YEAR_PASSED) from PRC\n"
            "- **REAL_FOREIGNERS.csv** for citizenship verification"
        )

        st.subheader("Data Pipeline Overview")
        st.markdown(
            "The data flows through four pipelines:\n\n"
            "1. **Pipeline 1:** Raw score extraction and standardization\n"
            "2. **Pipeline 2:** NMAT\u2013PLE linkage via fuzzy matching on name and birth year\n"
            "3. **Pipeline 3:** Score sanity checks, deduplication, best-record selection\n"
            "4. **Pipeline 4:** Citizenship classification using name-based assessment and "
            "REAL_FOREIGNERS.csv\n\n"
            "The output is NMAT_Exodus.parquet, which feeds both the main NMAT Performance Dashboard "
            "and this CHED Compliance Dashboard."
        )

        st.subheader("Key Terms and Definitions")

        terms_df = pd.DataFrame({
            "Term": [
                "Best Record (IS_BEST_NMAT_RECORD)",
                "Observable Cohort",
                "Linkage Rate",
                "PLE Pass Rate",
                "B1\u2013B10 Bins",
                "B4+ (30th Percentile)",
                "B5+ (40th Percentile)",
                "FOREIGNER_STATUS",
                "CITIZENSHIP_FINAL",
                "SUC",
                "PHEI",
                "5-Year Rolling Average",
            ],
            "Definition": [
                "The highest-scoring NMAT attempt per examinee. Used to avoid double-counting.",
                "Best records with Year <= 2014, allowing a 4-year window for PLE licensure.",
                "Share of NMAT examinees found in PLE passer data. NOT a pass rate.",
                "Cannot be computed. Requires PLE taker data with pass/fail outcomes.",
                "Percentile rank bins: B1 (0\u20139.9) through B10 (90\u201399.9).",
                "Examinees at or above the 30th percentile (bins B4\u2013B10).",
                "Examinees at or above the 40th percentile (bins B5\u2013B10).",
                "Classification: Filipino, Verified Foreigner, or Likely Foreigner.",
                "Nationality as determined by Pipeline 4 citizenship integration.",
                "State University or College.",
                "Philippine Higher Education Institution.",
                "Average linkage rate over the most recent 5 years (min 3 years required).",
            ],
        })
        st.dataframe(terms_df, use_container_width=True, hide_index=True)

        st.subheader("Data Limitations")
        st.warning(
            "1. **No PLE pass rates.** PLE_DATA contains passers only (43,630 rows, no fail records). "
            "What we report is the NMAT-to-PLE linkage rate, which is an evidence-based indicator "
            "but different from the official PLE pass rate.\n\n"
            "2. **Foreign student data counts examinees, not enrollees.** The 10-slot cap in the CMO "
            "applies to enrolled foreign students. Our data shows who took the NMAT, not who enrolled.\n\n"
            "3. **Temporal gap.** NMAT data covers 2006\u20132018. The CMO takes effect AY 2026\u20132027. "
            "This is historical analysis, not current monitoring.\n\n"
            "4. **Per-HEI PLE performance cannot determine compliance with Section IV-B-1b/c.** "
            "The CMO requires per-HEI 'PLE performance at a rate above the average national passing "
            "percentage.' Without PLE pass rates, we cannot definitively determine compliance.\n\n"
            "5. **Province-level geography was removed** during column slimming (118 \u2192 54 columns). "
            "Province-level analysis is not currently possible."
        )

        st.subheader("How the Data Was Produced")
        st.markdown(
            "All computations in this dashboard are performed directly from NMAT_Exodus.parquet "
            "using the following approach:\n\n"
            "- `best` subset = IS_BEST_NMAT_RECORD == True\n"
            "- `besttrend` subset = best filtered to 2006\u20132018\n"
            "- `bestobs` subset = besttrend filtered to Year <= 2014 (observable PLE cohort)\n\n"
            "Aggregations use groupby operations on these subsets. All charts use Plotly Express "
            "or Plotly Graph Objects. Tables are rendered via Streamlit's st.dataframe with "
            "built-in sorting, search, and download capabilities.\n\n"
            "The dashboard is designed for reproducibility: the same NMAT_Exodus.parquet file "
            "will produce identical results regardless of environment."
        )

        st.subheader("Glossary of Column Names in NMAT_Exodus.parquet")
        col_df = pd.DataFrame({
            "Column": [
                "APPNO_CLEAN", "PERSON_KEY", "Year", "NMS_PER_num", "PercentileBin",
                "UNIVERSITY", "NMA_College", "UNI_TYPE", "UNI_LOCATION",
                "SEX", "CourseGroup", "CITIZENSHIP_FINAL", "FOREIGNER_STATUS",
                "IS_BEST_NMAT_RECORD", "IS_PLE_ANALYSIS_SAFE", "IS_PLE_PASSER",
                "TotalRawScoreTRUE", "NMS_GPS", "NMS_APT", "NMS_SA",
            ],
            "Description": [
                "Anonymized application number",
                "Deduplicated person identifier",
                "NMAT examination year",
                "NMAT percentile rank score",
                "Percentile bin classification (B1\u2013B10)",
                "University name (aggregated, deduplicated)",
                "College/institution name within university",
                "University type: Public, Private, Foreign, Not Specified",
                "University location (region/province)",
                "Sex: Female or Male",
                "Course group classification (6 categories)",
                "Final citizenship classification",
                "Foreigner status: Filipino, Verified Foreigner, Likely Foreigner",
                "Flag: best NMAT record per examinee",
                "Flag: confirmed PLE passer (observable)",
                "Flag: IS_PLE_PASSER (derived)",
                "True total raw score (sum of verified Part I and Part II)",
                "General Potential Standard Score",
                "Academic Potential Test score",
                "Spiritual Aptitude score",
            ],
        })
        st.dataframe(col_df, use_container_width=True, hide_index=True)

        st.subheader("References")
        st.markdown(
            "- CMO No. __, s. 2026: Amendment to NMAT Cut-Off Scores\n"
            "- NMAT_Exodus.parquet: Pipeline 4 output (Pipeline 1\u20134 documentation available in the "
            "repository)\n"
            "- Main NMAT Performance Dashboard: `streamlit_dashboard/main_dashboard/dashboard.py`\n"
            "- CHED Implementation Plan: `streamlit_dashboard/CHED_relevant_dashboard/IMPLEMENTATION_PLAN.md`"
        )


if __name__ == "__main__":
    main()
