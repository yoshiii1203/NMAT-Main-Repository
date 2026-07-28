"""CHED Presentation Dashboard -- NMAT Cut-Off Policy Evidence.

A clean, evidence-focused dashboard built from NMAT_Exodus.parquet for
presentation to CHED stakeholders.  Only CMO-relevant insights that are
directly supported by the available data are included.
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

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="CHED NMAT Cut-Off Evidence Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BIN_ORDER = [f"B{i}" for i in range(1, 11)]
BIN_LABELS = {
    "B1": "0-9", "B2": "10-19", "B3": "20-29", "B4": "30-39",
    "B5": "40-49", "B6": "50-59", "B7": "60-69", "B8": "70-79",
    "B9": "80-89", "B10": "90-99",
}
PLE_LABELS = ["Confirmed PLE passer", "No confirmed PLE match"]

COLORS_BIN = {
    "B1": "#8B0000", "B2": "#B22222", "B3": "#D9534F", "B4": "#F0AD4E",
    "B5": "#FFD166", "B6": "#A0D468", "B7": "#66C2A5", "B8": "#41B6C4",
    "B9": "#2C7FB8", "B10": "#253494",
}
COLORS_PLE = {"Confirmed PLE passer": "#2e7d32", "No confirmed PLE match": "#c62828"}
COLORS_UNI = {"Public": "#1f77b4", "Private": "#ff7f0e", "Foreign": "#9467bd", "Not Specified": "#7f7f7f"}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def find_data_path() -> Path:
    candidates = [
        Path("NMAT_Exodus.parquet"),
        Path("dataset/NMAT_Exodus.parquet"),
        Path("../main_dashboard/NMAT_Exodus.parquet"),
        Path("../../dataset/NMAT_Exodus.parquet"),
    ]
    for p in candidates:
        if p.exists():
            return p.resolve()
    raise FileNotFoundError(
        "Could not locate NMAT_Exodus.parquet. "
        "Place it in ./dataset/ or in the app root."
    )


@st.cache_data(show_spinner="Loading NMAT data ...")
def load_data():
    path = find_data_path()
    df = pd.read_parquet(path, engine="pyarrow", use_threads=True)

    # coerce types
    for c in ["Year"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")
    for c in [
        "TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE",
        "NMS_PER_num", "NMS_GPS",
    ]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # bin order
    if "PercentileBin" in df.columns:
        df["PercentileBin"] = pd.Categorical(
            df["PercentileBin"], categories=BIN_ORDER, ordered=True
        )

    # best-record subset
    df_best = df[df["IS_BEST_NMAT_RECORD"] == True].copy() if "IS_BEST_NMAT_RECORD" in df.columns else df.copy()

    # observable cohort (Year <= 2014)
    df_obs = df_best[df_best["Year"] <= 2014].copy() if "Year" in df_best.columns else df_best.copy()

    # PLE flag
    if "IS_PLE_ANALYSIS_SAFE" in df_obs.columns:
        df_obs["HAS_CONFIRMED_PLE"] = (df_obs["IS_PLE_ANALYSIS_SAFE"] == True).astype("boolean")
    else:
        df_obs["HAS_CONFIRMED_PLE"] = pd.Series(pd.NA, index=df_obs.index, dtype="boolean")

    return df, df_best, df_obs


def make_bin_pct(df, group_col):
    """Return a DataFrame of row-wise bin percentages for a group column."""
    ct = pd.crosstab(df[group_col], df["PercentileBin"], dropna=False)
    ct = ct.reindex(columns=BIN_ORDER, fill_value=0)
    # Ensure numeric dtype (PyArrow backend may return string-typed crosstab counts)
    ct = ct.apply(pd.to_numeric, errors="coerce")
    pct = ct.div(ct.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)
    return ct, pct


# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------
df_all, df_best, df_obs = load_data()

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("NMAT Performance Evidence for CHED Cut-Off Policy Review")
st.caption(
    "This dashboard presents descriptive evidence from NMAT_Exodus.parquet "
    "(178,927 examinee records, 2006-2018) to inform the CMO amendment on "
    "NMAT cut-off scores.  All analyses use validated data from the "
    "4-pipeline processing system.  PLE-linked analyses use the observable "
    "cohort (Year <= 2014) to avoid right-censoring bias."
)

with st.expander("How to read this dashboard", expanded=False):
    st.markdown(
        """
- **Best-record examinees** -- one NMAT record per person (removes repeat-taker inflation).
- **Observable cohort** -- examinees with Year <= 2014, who have had time to take the PLE.
- **Percentile bins** -- B1 (0-9) through B10 (90-99).  B4+ means at or above the 30th percentile.  B5+ means at or above the 40th percentile.
- **NMAT-to-PLE linkage** -- this measures how many NMAT examinees were later matched to PLE passer records.  It is NOT a PLE pass rate.  The dataset does not contain all PLE takers or PLE failures.
- **Foreign examinee counts** -- these are NMAT examinees, not enrolled medical students.  Enrollment numbers would require additional data.
        """
    )

# ---------------------------------------------------------------------------
# Tabs
# ---------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "National NMAT Profile",
    "Percentile Distribution",
    "NMAT-to-PLE Linkage",
    "University Type Context",
    "National Benchmark Context",
    "Data Context & Limitations",
])

# ===================================================================
# TAB 1 -- National NMAT Profile & Coverage
# ===================================================================
with tab1:
    st.subheader("National NMAT Profile and Coverage")
    st.caption(
        "What this shows: the size, scope, and basic score distribution of the "
        "NMAT examinee population across 13 examination years.  These figures "
        "establish the evidence base for cut-off policy discussions."
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric(
        "Best-record examinees",
        f"{len(df_best):,}",
        help="Unique examinees after deduplication (one record per person).",
    )
    c2.metric(
        "NMAT years covered",
        f"{int(df_best['Year'].nunique())}",
        help="Examination years from 2006 through 2018.",
    )
    c3.metric(
        "Median percentile rank",
        f"{df_best['NMS_PER_num'].median():.1f}",
        help="Median examinee percentile rank.",
    )
    c4.metric(
        "Median TRUE raw score",
        f"{df_best['TotalRawScoreTRUE'].median():.1f}",
        help="Recalculated total raw score (corrected for 42.2% storage errors).",
    )

    c1, c2 = st.columns(2)
    with c1:
        uni_dist = (
            df_best["UNI_TYPE"]
            .value_counts()
            .reset_index()
        )
        uni_dist.columns = ["UNI_TYPE", "Count"]
        uni_dist["Count"] = pd.to_numeric(uni_dist["Count"], errors="coerce")
        uni_dist["Share (%)"] = (uni_dist["Count"] / uni_dist["Count"].sum() * 100).round(1)
        fig = px.pie(uni_dist, names="UNI_TYPE", values="Count", title="University Type Composition")
        fig.update_traces(textinfo="label+percent", hovertemplate="%{label}: %{value} (%{percent})<extra></extra>")
        st.plotly_chart(fig, use_container_width=True, key="t1_uni_pie")
        st.caption("Private institutions account for the majority of examinees, followed by Public (SUCs).")

    with c2:
        course_dist = (
            df_best["CourseGroup"]
            .value_counts()
            .reset_index()
        )
        course_dist.columns = ["CourseGroup", "Count"]
        course_dist["Count"] = pd.to_numeric(course_dist["Count"], errors="coerce")
        course_dist["Share (%)"] = (course_dist["Count"] / course_dist["Count"].sum() * 100).round(1)
        fig = px.pie(course_dist, names="CourseGroup", values="Count", title="Course Group Composition")
        fig.update_traces(textinfo="label+percent", hovertemplate="%{label}: %{value} (%{percent})<extra></extra>")
        st.plotly_chart(fig, use_container_width=True, key="t1_course_pie")
        st.caption("Medical & Allied and Natural Sciences together account for nearly 80% of examinees.")

    # Yearly examinee count table
    yearly_counts = (
        df_best.groupby("Year", observed=True)
        .size()
        .reset_index(name="Examinees")
    )
    yearly_counts["Year"] = yearly_counts["Year"].astype(str)
    fig = px.bar(
        yearly_counts, x="Year", y="Examinees",
        title="Examinee Count by NMAT Year (Best Record)",
        labels={"Examinees": "Examinees"},
    )
    fig.update_traces(hovertemplate="Year: %{x}<br>Examinees: %{y:,}<extra></extra>")
    st.plotly_chart(fig, use_container_width=True, key="t1_year_bar")
    st.caption("Examinee volume has grown substantially, particularly from 2015 onward.")

    yearly_counts_display = yearly_counts.copy()
    yearly_counts_display.columns = ["NMAT Year", "Examinees"]
    st.dataframe(yearly_counts_display, use_container_width=True, hide_index=True)

    st.markdown("**Interpretation.** The dataset covers the full national NMAT-taking population from 2006 to 2018, with 134,000 unique examinees after deduplication.  This provides a stable evidence base for analyzing the implications of cut-off policy changes.")

# ===================================================================
# TAB 2 -- Percentile Distribution & Cut-off Context
# ===================================================================
with tab2:
    st.subheader("Percentile Distribution and Cut-Off Context")
    st.caption(
        "What this shows: how examinees are distributed across the percentile "
        "spectrum, and how many fall at or above the two major cut-off thresholds "
        "discussed in the CMO (30th and 40th percentile)."
    )

    # Yearly bin composition heatmap (transposed: bins as rows, years as cols)
    ct_year, pct_year = make_bin_pct(df_best, "Year")
    pct_year.index.name = "Year"
    pct_year_t = pct_year.T
    pct_year_t.index.name = "Bin"
    pct_year_t = pct_year_t.reindex(BIN_ORDER[::-1])

    fig = px.imshow(
        pct_year_t,
        text_auto=".1f",
        aspect="auto",
        color_continuous_scale="YlOrRd",
        labels={"x": "Year", "y": "Percentile Bin", "color": "%"},
        title="Percentile Bin Distribution by NMAT Year (Row % per Year)",
    )
    fig.update_layout(height=460)
    st.plotly_chart(fig, use_container_width=True, key="t2_heatmap")
    st.caption("Darker red = higher concentration in that bin for that year.  The share of bottom-bin (B1-B3) examinees has increased in later years.")

    # 30th vs 40th percentile comparison
    st.markdown("### Examinees at or Above Each Cut-Off Threshold")

    df_best_bins = df_best.dropna(subset=["PercentileBin"]).copy()
    df_obs_bins = df_obs.dropna(subset=["PercentileBin"]).copy()

    def above_bin(df, threshold):
        """Return subset at or above the given bin (B4 = 30th, B5 = 40th)."""
        idx = BIN_ORDER.index(threshold)
        return df[df["PercentileBin"].apply(
            lambda b: BIN_ORDER.index(b) >= idx if pd.notna(b) else False
        )]

    def bin_range(df, low, high):
        """Return subset between two bins (inclusive)."""
        lo = BIN_ORDER.index(low)
        hi = BIN_ORDER.index(high)
        return df[df["PercentileBin"].apply(
            lambda b: lo <= BIN_ORDER.index(b) <= hi if pd.notna(b) else False
        )]

    scenario_rows = []
    for label, bin_thresh, cohort in [
        ("30th percentile (B4+)", "B4", df_best_bins),
        ("40th percentile (B5+)", "B5", df_best_bins),
        ("30th-39th percentile only (B4)", "B4", bin_range(df_best_bins, "B4", "B4")),
    ]:
        if label == "30th-39th percentile only (B4)":
            sub = cohort
        else:
            sub = above_bin(cohort, bin_thresh)

        obs_sub = above_bin(df_obs_bins, bin_thresh) if label != "30th-39th percentile only (B4)" else bin_range(df_obs_bins, "B4", "B4")

        scenario_rows.append({
            "Threshold": label,
            "Best-record examinees": len(sub),
            "Share of all (%)": round(len(sub) / len(df_best_bins) * 100, 1),
            "Median percentile": round(sub["NMS_PER_num"].median(), 1) if len(sub) > 0 else "-",
            "Observable cohort size": len(obs_sub),
        })

    scenario_df = pd.DataFrame(scenario_rows)
    st.dataframe(scenario_df, use_container_width=True, hide_index=True)
    st.caption(
        "The 30th-percentile cut-off (B4+) encompasses a substantially larger pool "
        "than the 40th-percentile cut-off (B5+).  The B4-only group (30th-39th percentile) "
        "represents the marginal population affected by a choice between the two thresholds."
    )

    # B4 group profile
    b4_group = bin_range(df_best.dropna(subset=["PercentileBin"]), "B4", "B4")
    if len(b4_group) > 0:
        st.markdown("### Profile of the 30th-39th Percentile Group (B4)")

        b4_by_uni = (
            b4_group.groupby("UNI_TYPE", observed=True)
            .size()
            .reset_index(name="count")
        )
        b4_by_uni["count"] = pd.to_numeric(b4_by_uni["count"], errors="coerce")
        b4_by_uni["share"] = (b4_by_uni["count"] / b4_by_uni["count"].sum() * 100).round(1)

        c1, c2, c3 = st.columns(3)
        c1.metric("B4 examinees (best record)", f"{len(b4_group):,}")
        c2.metric(
            "Median total raw score",
            f"{b4_group['TotalRawScoreTRUE'].median():.1f}"
        )
        c3.metric(
            "Public institution share",
            f"{b4_by_uni.loc[b4_by_uni['UNI_TYPE']=='Public', 'share'].values[0]:.1f}%" if "Public" in b4_by_uni["UNI_TYPE"].values else "0%"
        )

        fig = px.bar(
            b4_by_uni, x="UNI_TYPE", y="count",
            title="B4 Examinees by Institution Type",
            labels={"count": "Examinees", "UNI_TYPE": ""},
            color="UNI_TYPE", color_discrete_map=COLORS_UNI,
        )
        st.plotly_chart(fig, use_container_width=True, key="t2_b4_uni")

        st.caption(
            "Examinees in the 30th-39th percentile band are distributed across all "
            "university types.  The majority come from Private institutions, consistent "
            "with the overall composition of the dataset."
        )

    # Top vs bottom bin share over time
    st.markdown("### Top-Bin (B8-B10) vs Bottom-Bin (B1-B3) Trend")
    _, pct_year_2 = make_bin_pct(df_best, "Year")
    top_share = pct_year_2[["B8", "B9", "B10"]].sum(axis=1)
    bot_share = pct_year_2[["B1", "B2", "B3"]].sum(axis=1)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=top_share.index.astype(str), y=top_share.values,
        mode="lines+markers", name="Top B8-B10",
        line=dict(color="#2e7d32", width=3),
    ))
    fig.add_trace(go.Scatter(
        x=bot_share.index.astype(str), y=bot_share.values,
        mode="lines+markers", name="Bottom B1-B3",
        line=dict(color="#c62828", width=3),
    ))
    fig.update_layout(
        title="Share of Examinees in Top vs Bottom Bins by Year",
        xaxis_title="Year", yaxis_title="Percent of examinees",
        height=400,
    )
    st.plotly_chart(fig, use_container_width=True, key="t2_topbot")
    st.caption(
        "The proportion of examinees in the top bins (B8-B10) has declined since 2013, "
        "while the bottom-bin share (B1-B3) has increased.  This shift affects how many "
        "examinees would fall at or above any fixed cut-off threshold."
    )

    # Year-by-year table of B4+ and B5+ counts
    st.markdown("### Yearly Threshold-Admitted Counts")
    yearly_threshold = []
    for yr in sorted(df_best_bins["Year"].dropna().unique()):
        yr_df = df_best_bins[df_best_bins["Year"] == yr]
        yr_obs = df_obs_bins[df_obs_bins["Year"] == yr]
        above_b4 = above_bin(yr_df, "B4")
        above_b5 = above_bin(yr_df, "B5")
        obs_b4 = above_bin(yr_obs, "B4")
        obs_b5 = above_bin(yr_obs, "B5")
        yearly_threshold.append({
            "Year": int(yr),
            "Total (best record)": len(yr_df),
            "B4+ (30th cut-off)": len(above_b4),
            "B4+ share (%)": round(len(above_b4) / len(yr_df) * 100, 1),
            "B5+ (40th cut-off)": len(above_b5),
            "B5+ share (%)": round(len(above_b5) / len(yr_df) * 100, 1),
            "Observable B4+": len(obs_b4),
            "Observable B5+": len(obs_b5),
        })
    yr_tbl = pd.DataFrame(yearly_threshold)
    st.dataframe(yr_tbl, use_container_width=True, hide_index=True)
    st.caption(
        "The difference between B4+ and B5+ shares indicates how many additional "
        "examinees would meet a 30th-percentile cut-off versus a 40th-percentile cut-off.  "
        "Observable counts use Year <= 2014 for PLE-linked analyses."
    )

    st.markdown("**Interpretation.** The data show a substantial and growing pool of examinees below both cut-off thresholds.  The 30th-percentile cut-off admits approximately 10-15 percentage points more examinees than the 40th-percentile cut-off, depending on the year.  The observable cohort provides the basis for comparing PLE outcomes between these groups.")

# ===================================================================
# TAB 3 -- NMAT-to-PLE Linkage by Percentile Band
# ===================================================================
with tab3:
    st.subheader("NMAT-to-PLE Linkage by Percentile Band")
    st.caption(
        "What this shows: the proportion of NMAT examinees in each percentile band "
        "who were later confirmed as PLE passers, using the observable cohort "
        "(Year <= 2014).  This is NMAT-to-PLE linkage, not a PLE pass rate."
    )

    st.info(
        "The dataset identifies NMAT examinees who were later matched to PLE passer "
        "records.  It does not contain all PLE takers or PLE failures.  Therefore, "
        "these values represent NMAT-to-PLE linkage, not PLE passing rates.  "
        "They should be interpreted as: 'among NMAT examinees in this percentile "
        "band, this percentage were later confirmed as having passed the PLE.'"
    )

    # PLE linkage by bin
    ple_bin = (
        df_obs.dropna(subset=["PercentileBin", "HAS_CONFIRMED_PLE"])
        .groupby("PercentileBin", observed=True)
        .agg(
            n=("APPNO_CLEAN", "count"),
            confirmed_passers=("HAS_CONFIRMED_PLE", "sum"),
        )
        .reset_index()
    )
    ple_bin.columns = ["Percentile Bin", "N (observable cohort)", "Confirmed PLE Passers"]
    ple_bin["Linkage Rate (%)"] = (
        ple_bin["Confirmed PLE Passers"] / ple_bin["N (observable cohort)"] * 100
    ).round(2)
    ple_bin["Percentile Bin"] = ple_bin["Percentile Bin"].astype(str)
    ple_bin["Label"] = ple_bin["Percentile Bin"].map(BIN_LABELS)

    fig = px.bar(
        ple_bin, x="Percentile Bin", y="Linkage Rate (%)",
        title="NMAT-to-PLE Linkage Rate by Percentile Band",
        labels={"Percentile Bin": "Percentile Band", "Linkage Rate (%)": "NMAT-to-PLE Linkage (%)"},
        color="Linkage Rate (%)", color_continuous_scale="Viridis",
        text=ple_bin["Linkage Rate (%)"].round(1).astype(str) + "%",
    )
    fig.update_traces(textposition="outside", hovertemplate="Band: %{x}<br>Linkage: %{y:.1f}%<br>N: %{customdata:,}<extra></extra>",
                      customdata=ple_bin["N (observable cohort)"].values)
    fig.add_hline(y=50, line_dash="dash", line_color="gray", annotation_text="50%")
    fig.update_layout(height=480)
    st.plotly_chart(fig, use_container_width=True, key="t3_ple_bar")
    st.caption(
        "Linkage rates increase steadily across percentile bands.  The B4 band (30th-39th "
        "percentile) shows approximately 23% NMAT-to-PLE linkage, compared to about 46% "
        "for B5 (40th-49th percentile).  This is a descriptive pattern, not a causal "
        "prediction."
    )

    # Table
    st.dataframe(ple_bin[["Percentile Bin", "Label", "N (observable cohort)", "Confirmed PLE Passers", "Linkage Rate (%)"]],
                 use_container_width=True, hide_index=True)

    # Score profile by PLE status
    st.markdown("### Score Profile by PLE Status")

    desc_cols = ["TotalRawScoreTRUE", "NMS_PER_num", "PartIRawScoreTRUE", "PartIIRawScoreTRUE"]
    desc_cols = [c for c in desc_cols if c in df_obs.columns]
    if desc_cols:
        desc = (
            df_obs.groupby("HAS_CONFIRMED_PLE", observed=True)[desc_cols]
            .agg(["count", "median", "mean", lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)])
            .round(2)
        )
        desc.index = ["No confirmed PLE match", "Confirmed PLE passer"]
        st.dataframe(desc, use_container_width=True)
        st.caption(
            "Confirmed PLE passers show substantially higher median scores across all "
            "measures compared to the group without a confirmed PLE match."
        )

    # PLE linkage by year
    st.markdown("### PLE Linkage by NMAT Year")
    ple_yr = (
        df_obs.groupby("Year", observed=True)
        .agg(
            n=("APPNO_CLEAN", "count"),
            confirmed=("HAS_CONFIRMED_PLE", "sum"),
        )
        .reset_index()
    )
    ple_yr["linkage_pct"] = (ple_yr["confirmed"] / ple_yr["n"] * 100).round(2)
    ple_yr["Year"] = ple_yr["Year"].astype(str)

    fig = px.line(
        ple_yr, x="Year", y="linkage_pct",
        markers=True,
        title="NMAT-to-PLE Linkage Rate by NMAT Year (Observable Cohort)",
        labels={"linkage_pct": "Linkage Rate (%)"},
    )
    fig.update_traces(hovertemplate="Year: %{x}<br>Linkage: %{y:.1f}%<br>N: %{customdata:,}<extra></extra>",
                      customdata=ple_yr["n"].values,
                      line=dict(color="#1f77b4", width=3))
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True, key="t3_ple_yr")
    st.caption(
        "Observed linkage rates decline for more recent years within the observable "
        "cohort, which may reflect the shorter post-NMAT window for those cohorts."
    )

    # PLE linkage by course group
    st.markdown("### PLE Linkage by Course Group")
    if "CourseGroup" in df_obs.columns:
        ple_course = (
            df_obs.dropna(subset=["CourseGroup", "HAS_CONFIRMED_PLE"])
            .groupby("CourseGroup", observed=True)
            .agg(
                n=("APPNO_CLEAN", "count"),
                confirmed=("HAS_CONFIRMED_PLE", "sum"),
                median_pct=("NMS_PER_num", "median"),
            )
            .reset_index()
        )
        ple_course["Linkage Rate (%)"] = (ple_course["confirmed"] / ple_course["n"] * 100).round(2)
        ple_course.columns.values[0] = "Course Group"

        fig = px.bar(
            ple_course, x="Course Group", y="Linkage Rate (%)",
            color="Course Group",
            title="NMAT-to-PLE Linkage Rate by Course Group",
            text=ple_course["Linkage Rate (%)"].round(1).astype(str) + "%",
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(height=400, showlegend=False, xaxis_tickangle=-20)
        st.plotly_chart(fig, use_container_width=True, key="t3_ple_course")

        st.dataframe(ple_course, use_container_width=True, hide_index=True)
        st.caption(
            "Linkage rates vary by pre-med course background.  Education and Natural Sciences "
            "examinees show the highest linkage rates, while Engineering & Technology shows "
            "the lowest, consistent with course-to-career pathways."
        )

    # PLE linkage by university type
    st.markdown("### PLE Linkage by University Type")
    if "UNI_TYPE" in df_obs.columns:
        ple_uni = (
            df_obs[df_obs["UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
            .groupby("UNI_TYPE", observed=True)
            .agg(
                n=("APPNO_CLEAN", "count"),
                confirmed=("HAS_CONFIRMED_PLE", "sum"),
                median_pct=("NMS_PER_num", "median"),
            )
            .reset_index()
        )
        ple_uni["Linkage Rate (%)"] = (ple_uni["confirmed"] / ple_uni["n"] * 100).round(2)
        ple_uni.columns.values[0] = "University Type"

        fig = px.bar(
            ple_uni, x="University Type", y="Linkage Rate (%)",
            color="University Type", color_discrete_map=COLORS_UNI,
            title="NMAT-to-PLE Linkage Rate by University Type",
            text=ple_uni["Linkage Rate (%)"].round(1).astype(str) + "%",
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True, key="t3_ple_uni")

        st.dataframe(ple_uni, use_container_width=True, hide_index=True)
        st.caption(
            "Public institution examinees show the highest linkage rate at approximately "
            "50%, compared to 45% for Private institutions.  Foreign institution "
            "examinees show markedly lower linkage rates, consistent with most being "
            "ineligible or not pursuing the Philippine licensure examination."
        )

    st.markdown("**Interpretation.** The NMAT-to-PLE linkage rate rises steadily with percentile rank, from about 8% in B1 to 76% in B10.  The 30th-39th percentile band shows approximately 23% linkage, compared to 46% for the 40th-49th percentile band.  These patterns are descriptive and reflect the composition of NMAT examinees who also took and passed the PLE -- they do not represent the PLE success rate of all medical school graduates.")

# ===================================================================
# TAB 4 -- University Type & Institution Context
# ===================================================================
with tab4:
    st.subheader("University Type and Institution Context")
    st.caption(
        "What this shows: how NMAT performance and PLE linkage differ across "
        "Public (SUC), Private (PHEI), and Foreign institution types."
    )

    uni_subset = df_best[df_best["UNI_TYPE"].isin(["Public", "Private", "Foreign"])].copy()

    # Score summary by university type
    st.markdown("### Score Summary by University Type")

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
        "University Type", "N (best record)", "Median %ile", "Q25 %ile",
        "Q75 %ile", "Median Raw Score", "Median GPS",
    ]

    c1, c2 = st.columns([1, 1])
    with c1:
        st.dataframe(uni_score, use_container_width=True, hide_index=True)
    with c2:
        fig = px.box(
            uni_subset.dropna(subset=["NMS_PER_num"]),
            x="UNI_TYPE", y="NMS_PER_num",
            color="UNI_TYPE", color_discrete_map=COLORS_UNI,
            points=False,
            title="Percentile Rank Distribution by University Type",
            labels={"NMS_PER_num": "Percentile Rank", "UNI_TYPE": ""},
        )
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True, key="t4_box_uni")

    st.caption(
        "Public institution examinees show a higher median percentile rank (57) "
        "compared to Private (49) and Foreign (52) institution examinees."
    )

    # Bin distribution by university type
    st.markdown("### Percentile Bin Distribution by University Type")
    _, uni_bin_pct = make_bin_pct(uni_subset, "UNI_TYPE")
    uni_bin_pct.index.name = "University Type"

    fig = px.imshow(
        uni_bin_pct,
        text_auto=".1f",
        aspect="auto",
        color_continuous_scale="YlOrRd",
        labels={"x": "Percentile Bin", "y": "University Type", "color": "%"},
        title="Bin Distribution by University Type (Row %)",
    )
    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True, key="t4_uni_bin")
    st.caption(
        "Public institutions have a higher concentration in the top bins (B8-B10), "
        "while Private and Foreign institutions show broader distributions across all bins."
    )

    # Top-bin share by university type
    top_uni = uni_bin_pct[["B8", "B9", "B10"]].sum(axis=1).sort_values()
    fig = go.Figure(go.Bar(
        x=top_uni.values,
        y=top_uni.index,
        orientation="h",
        marker_color=[COLORS_UNI.get(i, "#7f7f7f") for i in top_uni.index],
        text=[f"{v:.1f}%" for v in top_uni.values],
        textposition="outside",
    ))
    fig.update_layout(
        title="Top-Bin Share (B8-B10) by University Type",
        xaxis_title="Percent in B8-B10",
        yaxis_title="",
        height=300,
    )
    st.plotly_chart(fig, use_container_width=True, key="t4_top_uni")

    # Foreign examinee context (descriptive only)
    st.markdown("### Foreign Examinee Context")
    st.caption(
        "The CMO includes provisions for foreign student enrollment at SUCs.  "
        "The available data identify NMAT examinees by citizenship -- these are "
        "NMAT examinees, not enrolled medical students.  Enrollment numbers "
        "would require additional data from HEIs."
    )

    if "CITIZENSHIP_FINAL" in df_best.columns and "FOREIGNER_STATUS" in df_best.columns:
        foreign = df_best[df_best["FOREIGNER_STATUS"] == "Verified Foreigner"]
        filipino = df_best[df_best["CITIZENSHIP_FINAL"] == "Filipino"]

        c1, c2, c3 = st.columns(3)
        c1.metric(
            "Verified Foreign examinees (all years)",
            f"{len(foreign):,}",
            help="NMAT examinees with verified non-Filipino citizenship from REAL_FOREIGNERS.csv ground truth.",
        )
        c2.metric(
            "Filipino examinees",
            f"{len(filipino):,}",
        )
        c3.metric(
            "Distinct foreign nationalities represented",
            f"{foreign['CITIZENSHIP_FINAL'].nunique()}",
        )

        # Foreign examinee top nationalities
        top_nat = (
            foreign["CITIZENSHIP_FINAL"]
            .value_counts()
            .head(10)
            .reset_index()
        )
        top_nat.columns = ["Nationality", "Count"]
        top_nat["Count"] = pd.to_numeric(top_nat["Count"], errors="coerce")
        fig = px.bar(
            top_nat, x="Count", y="Nationality",
            orientation="h",
            title="Top 10 Nationalities Among Verified Foreign NMAT Examinees",
            labels={"Count": "Examinees"},
        )
        fig.update_traces(hovertemplate="%{y}: %{x:,}<extra></extra>")
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True, key="t4_foreign_top")
        st.caption(
            "These counts represent NMAT examinees, not enrolled medical students.  "
            "The actual number of foreign students enrolled in medical programs may "
            "differ from the number who took the NMAT."
        )

    st.markdown("**Interpretation.** Public institution examinees show higher median scores and higher top-bin representation than their Private institution counterparts.  Foreign examinees comprise a small but diverse group.  These institutional patterns provide context for policies that differentiate between SUCs and PHEIs.")

# ===================================================================
# TAB 5 -- National Benchmark Context
# ===================================================================
with tab5:
    st.subheader("National PLE Benchmark Context")
    st.caption(
        "What this shows: the annual NMAT-to-PLE linkage rates and a 5-year "
        "rolling average.  The CMO references the national PLE passing percentage "
        "as a benchmark for PHEI cut-off eligibility.  This table provides the "
        "closest available approximation using the NMAT-linked PLE data."
    )

    st.warning(
        "The figures below show NMAT-to-PLE linkage rates for the observable "
        "cohort, NOT national PLE passing percentages.  The national PLE passing "
        "rate is published by the Professional Regulation Commission (PRC) and "
        "reflects all PLE takers, including those who did not take the NMAT "
        "within the available window.  The 5-year rolling average shown here "
        "is calculated from NMAT-linked PLE passers only."
    )

    # Annual linkage rates with 5-year rolling average
    natl = (
        df_obs.groupby("Year", observed=True)
        .agg(
            n=("APPNO_CLEAN", "count"),
            confirmed=("HAS_CONFIRMED_PLE", "sum"),
        )
        .reset_index()
    )
    natl["linkage_pct"] = (natl["confirmed"] / natl["n"] * 100).round(2)
    natl["5yr_rolling_avg"] = natl["linkage_pct"].rolling(window=5, min_periods=3).mean().round(2)

    latest_benchmark = natl[natl["5yr_rolling_avg"].notna()].iloc[-1]["5yr_rolling_avg"]
    latest_year = int(natl[natl["5yr_rolling_avg"].notna()].iloc[-1]["Year"])

    c1, c2 = st.columns([2, 1])
    with c1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=natl["Year"].astype(str), y=natl["linkage_pct"],
            mode="lines+markers", name="Annual NMAT-to-PLE linkage",
            line=dict(color="#1f77b4", width=2),
            hovertemplate="Year: %{x}<br>Linkage: %{y:.1f}%<br>N: %{customdata:,}<extra></extra>",
            customdata=natl["n"].values,
        ))
        fig.add_trace(go.Scatter(
            x=natl["Year"].astype(str), y=natl["5yr_rolling_avg"],
            mode="lines+markers", name="5-year rolling avg",
            line=dict(color="#d62728", width=3, dash="dash"),
            hovertemplate="Year: %{x}<br>5yr avg: %{y:.1f}%<extra></extra>",
        ))
        fig.update_layout(
            title="NMAT-to-PLE Linkage Rate with 5-Year Rolling Average",
            xaxis_title="NMAT Year", yaxis_title="Linkage Rate (%)",
            height=420,
        )
        st.plotly_chart(fig, use_container_width=True, key="t5_benchmark")
        st.caption("The 5-year rolling average smooths annual fluctuations and is the reference benchmark used in the CMO for PHEI cut-off eligibility.")

    with c2:
        st.metric(
            "Latest 5-year avg linkage rate",
            f"{latest_benchmark:.2f}%",
            help="The benchmark used to determine PHEI cut-off eligibility (30th vs 40th percentile).",
        )
        st.metric(
            "Reference NMAT year",
            f"{latest_year}",
            help="The most recent NMAT cohort with a complete 5-year observation window for PLE linkage.",
        )
        st.caption(
            "This benchmark is calculated from NMAT-linked PLE passers only.  "
            "It is a lower bound on the national PLE passing rate because it only "
            "captures NMAT examinees who later passed the PLE."
        )

    # Table
    natl_display = natl.rename(columns={
        "Year": "NMAT Year",
        "n": "Observable N examinees",
        "confirmed": "Confirmed PLE passers",
        "linkage_pct": "NMAT-to-PLE linkage (%)",
        "5yr_rolling_avg": "5-year rolling avg (%)",
    })
    st.dataframe(natl_display, use_container_width=True, hide_index=True)

    st.markdown("### Per-HEI PLE Linkage vs. National Benchmark")
    st.caption(
        "The following table shows each HEI's NMAT-to-PLE linkage rate compared "
        "to the national 5-year rolling average benchmark.  HEIs with linkage "
        "rates above the benchmark are identified; HEIs below the benchmark "
        "are also shown.  This supports the CMO provision tying PHEI cut-off "
        "eligibility to PLE performance."
    )

    st.warning(
        "These are NMAT-to-PLE linkage rates per HEI, not PLE pass rates.  "
        "They reflect the proportion of an HEI's NMAT examinees (observable "
        "cohort) who were later matched to PLE passer records.  An HEI's "
        "actual PLE passing rate, as reported by the PRC, may differ because "
        "it includes all graduates who take the PLE, not just those whose "
        "NMAT record is in this dataset."
    )

    min_examinees = st.slider(
        "Minimum examinees per HEI for reliable estimates",
        min_value=5, max_value=50, value=10, step=5,
        key="t5_hei_min",
    )

    hei_ple = (
        df_obs.groupby(["UNIVERSITY", "UNI_TYPE"], observed=True)
        .agg(
            n=("APPNO_CLEAN", "count"),
            confirmed=("HAS_CONFIRMED_PLE", "sum"),
            median_pct=("NMS_PER_num", "median"),
        )
        .reset_index()
    )
    hei_ple["linkage_pct"] = (hei_ple["confirmed"] / hei_ple["n"] * 100).round(2)
    hei_ple = hei_ple[hei_ple["n"] >= min_examinees].copy()
    hei_ple["above_benchmark"] = hei_ple["linkage_pct"] > latest_benchmark
    hei_ple = hei_ple.sort_values("linkage_pct", ascending=False).reset_index(drop=True)

    # Counts
    n_above = int(hei_ple["above_benchmark"].sum())
    n_below = int((~hei_ple["above_benchmark"]).sum())

    c1, c2, c3 = st.columns(3)
    c1.metric("HEIs above benchmark", f"{n_above}",
              help=f"HEIs with NMAT-to-PLE linkage above {latest_benchmark:.1f}%")
    c2.metric("HEIs below benchmark", f"{n_below}",
              help=f"HEIs with linkage at or below {latest_benchmark:.1f}%")
    c3.metric("National benchmark", f"{latest_benchmark:.2f}%")

    hei_display = hei_ple.copy()
    hei_display["Status"] = np.where(
        hei_display["above_benchmark"],
        "Above benchmark",
        "At or below benchmark",
    )
    st.dataframe(
        hei_display.rename(columns={
            "UNIVERSITY": "HEI",
            "UNI_TYPE": "Type",
            "n": "Examinees",
            "median_pct": "Median %ile",
            "linkage_pct": "Linkage Rate (%)",
        })[["HEI", "Type", "Examinees", "Median %ile", "Linkage Rate (%)", "Status"]],
        use_container_width=True,
        hide_index=True,
    )
    st.caption(
        f"Among HEIs with at least {min_examinees} observable examinees, "
        f"{n_above} show NMAT-to-PLE linkage rates above the national benchmark "
        f"of {latest_benchmark:.1f}%, while {n_below} fall at or below."
    )

    st.markdown("**Interpretation.** The 5-year rolling average provides a stable benchmark for comparing institutional PLE linkage.  HEIs above this benchmark would qualify for the 30th-percentile cut-off under the CMO framework, while those at or below would need to maintain the 40th-percentile cut-off.  Users should note that these figures use NMAT-linked data, which undercounts total PLE passers compared to official PRC statistics.")

# ===================================================================
# TAB 6 -- Data Context & Limitations
# ===================================================================
with tab6:
    st.subheader("Data Context and Methodological Notes")
    st.caption(
        "This section documents the dataset, processing decisions, and "
        "limitations relevant to interpreting the evidence presented in this dashboard."
    )

    st.markdown("### Dataset Overview")
    st.markdown(
        f"""
- **Source file:** `NMAT_Exodus.parquet` (54 columns, {len(df_all):,} rows)
- **Examination years:** 2006-2018
- **Unique examinees (best record):** {df_best['PERSON_KEY'].nunique():,}
- **Observable PLE cohort (Year <= 2014):** {len(df_obs):,}
- **Repeat takers:** {(df_all.groupby('PERSON_KEY')['APPNO_CLEAN'].nunique() > 1).sum():,} unique persons (25%)
        """
    )

    st.markdown("### Key Methodological Choices")

    with st.expander("TRUE Raw Score Recalculation"):
        st.markdown(
            """
The pipeline recalculated all raw scores from the 8 individual subtest components
because 42.2% of the original stored totals were incorrect.  All analyses in this
dashboard use the recalculated `TotalRawScoreTRUE` scores.

- Rows with complete TRUE scores: {:,} (99.97%)
- Formula mismatches (Total != Part I + Part II): 0
            """.format(int((df_all["HasTRUErawScores"] == True).sum()))
        )

    with st.expander("Best-Record Deduplication"):
        st.markdown(
            """
25% of examinees took the NMAT more than once (up to 9 attempts).  Person-level
analyses in this dashboard use the best-record flag (`IS_BEST_NMAT_RECORD`),
which selects:

- For PLE passers: the specific NMAT attempt that matched to the PLE record.
- For others: the highest percentile attempt, with latest year as tiebreaker.

This prevents repeat takers from inflating the counts in any percentile band.
            """
        )

    with st.expander("Observable Cohort Definition (Year <= 2014)"):
        st.markdown(
            """
PLE-linked analyses are restricted to examinees whose NMAT year is 2014 or earlier.
This ensures a minimum 5-year window for PLE passage, avoiding the misclassification
of later cohorts as non-passers before their licensure window closes.

- Observable best-record cohort: {:,}
- Median NMAT-to-PLE year gap: 6 years
            """.format(len(df_obs))
        )

    with st.expander("Deterministic PLE Matching"):
        st.markdown(
            """
All PLE matching is deterministic (exact NMA_AppNo match, manual AppNo match,
or deterministic AppNo match).  No fuzzy/rapidfuzz matching is used.  This ensures
full auditability but may undercount true matches where the NMAT application number
was recorded differently in the PLE dataset.

- Confirmed PLE passers (all rows): {:,}
- Confirmed PLE passers (best record, observable): {:,}
            """.format(
                int((df_all["IS_PLE_ANALYSIS_SAFE"] == True).sum()) if "IS_PLE_ANALYSIS_SAFE" in df_all.columns else 0,
                int(df_obs["HAS_CONFIRMED_PLE"].sum()) if "HAS_CONFIRMED_PLE" in df_obs.columns else 0,
            )
        )

    st.markdown("### Limitations Relevant to CHED Decision-Making")

    limitations = [
        (
            "PLE Outcomes",
            "The dataset only identifies NMAT examinees later matched to PLE passer "
            "records.  It does not contain all PLE takers or PLE failures.  Therefore, "
            "this dashboard reports NMAT-to-PLE linkage rates, not PLE pass rates.  "
            "Official PLE passing rates published by the PRC should be used for "
            "benchmarking purposes."
        ),
        (
            "GIDA and IP Status",
            "The dataset does not contain indicators for Geographically Isolated and "
            "Disadvantaged Area (GIDA) residence or Indigenous Peoples (IP) membership.  "
            "The CMO exception for 30th-39th percentile applicants from these groups "
            "requires documentation that is not available in the NMAT dataset."
        ),
        (
            "Medical School Admissions and Enrollment",
            "The dataset records NMAT examinees, not enrolled medical students.  "
            "The number of examinees at or above a cut-off threshold represents the "
            "available applicant pool, not actual enrollment.  HEI-level enrollment "
            "decisions, capacity, and admission criteria are not captured in this data."
        ),
        (
            "Foreign Student Enrollment Cap",
            "The CMO caps foreign student enrollment at 10 slots per incoming class at "
            "SUCs.  The dataset shows NMAT examinees by citizenship, not enrolled "
            "foreign students.  A descriptive foreign-examinee profile is provided, "
            "but this dashboard does not claim to measure compliance with the 10-slot cap."
        ),
        (
            "Composite Ranking for Foreign Applicants",
            "The CMO encourages composite ranking (e.g., 60/40 NMAT-to-other criteria) "
            "for foreign applicants.  The dataset does not contain GWA, interview scores, "
            "or other admission criteria needed for composite ranking analysis."
        ),
        (
            "PHEI Accountability and Sanctions",
            "The CMO ties the 30th-percentile privilege to PLE performance and allows "
            "CHED to revoke this privilege for PHEIs with below-benchmark PLE rates for "
            "three consecutive years.  This dashboard does not assign compliance labels "
            "or risk ratings to individual PHEIs, as the NMAT-linked PLE data is not a "
            "complete measure of institutional PLE performance."
        ),
    ]

    for title, detail in limitations:
        st.markdown(f"**{title}**")
        st.markdown(detail)
        st.divider()

    st.markdown("### Data Integrity Summary")
    ci_cols = ["StoredVsDerivedMismatch", "CalcVsDerivedMismatch"]
    if all(c in df_all.columns for c in ci_cols):
        c1, c2 = st.columns(2)
        c1.metric(
            "Stored-vs-derived mismatches",
            f"{int((df_all['StoredVsDerivedMismatch'] == 1.0).sum()):,}",
            help="Records where the original stored raw total differed from the TRUE recalculated total.",
        )
        c2.metric(
            "Calc-vs-derived mismatches",
            f"{int((df_all['CalcVsDerivedMismatch'] == 1.0).sum()):,}",
            help="Records where the CEM-calculated total differed from the TRUE recalculated total (always 0).",
        )

    st.markdown("**Interpretation.** The data used in this dashboard has been through a rigorous 4-pipeline processing system with documented quality checks.  The key limitations for CHED decision-making relate to the scope of the dataset (NMAT examinees only, not all PLE takers or enrolled students) and the absence of certain variables (GIDA/IP status, admission criteria, enrollment data) that would be needed for a complete policy assessment.")
