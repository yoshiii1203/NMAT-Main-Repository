"""CHED Presentation Dashboard -- NMAT Cut-Off Policy Evidence.

A clean, evidence-focused dashboard built from NMAT_Exodus.parquet for
presentation to CHED stakeholders.  Only CMO-relevant insights that are
directly supported by the available data are included.  No compliance
labels, eligibility decisions, or regulatory assessments are assigned.
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
    "B9": "80-89", "B10": "90-100",
}
B4_PLUS = ["B4", "B5", "B6", "B7", "B8", "B9", "B10"]
B5_PLUS = ["B5", "B6", "B7", "B8", "B9", "B10"]
TOP_BINS = ["B8", "B9", "B10"]
BOTTOM_BINS = ["B1", "B2", "B3"]

COLORS_BIN = {
    "B1": "#8B0000", "B2": "#B22222", "B3": "#D9534F", "B4": "#F0AD4E",
    "B5": "#FFD166", "B6": "#A0D468", "B7": "#66C2A5", "B8": "#41B6C4",
    "B9": "#2C7FB8", "B10": "#253494",
}
COLORS_UNI = {"Public": "#1f77b4", "Private": "#ff7f0e", "Foreign": "#9467bd", "Not Specified": "#7f7f7f"}

REQUIRED_COLS = [
    "APPNO_CLEAN", "PERSON_KEY", "Year", "UNI_TYPE", "UNIVERSITY",
    "CourseGroup", "IS_BEST_NMAT_RECORD", "IS_PLE_ANALYSIS_SAFE",
    "TotalRawScoreTRUE", "NMS_PER_num", "PercentileBin",
]

# ---------------------------------------------------------------------------
# Schema validation (lightweight)
# ---------------------------------------------------------------------------
def validate_schema(df: pd.DataFrame) -> pd.DataFrame:
    """Check required columns, normalize types, derive missing fields."""
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(
            "NMAT_Exodus.parquet is missing required columns: "
            + ", ".join(missing)
        )

    df = df.copy()

    # Normalize numeric types
    for c in ["Year", "TotalRawScoreTRUE", "NMS_PER_num", "NMS_GPS",
              "PartIRawScoreTRUE", "PartIIRawScoreTRUE"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # Derive PercentileBin if absent (left-closed [0,10)...[90,100])
    if "PercentileBin" not in df.columns or df["PercentileBin"].isna().all():
        edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101]
        df["PercentileBin"] = pd.cut(
            pd.to_numeric(df["NMS_PER_num"], errors="coerce"),
            bins=edges, labels=BIN_ORDER, right=False, include_lowest=True,
        )
    df["PercentileBin"] = pd.Categorical(
        df["PercentileBin"], categories=BIN_ORDER, ordered=True
    )

    # Normalise boolean flags safely (may be nullable booleans or strings)
    for c in ["IS_BEST_NMAT_RECORD", "IS_PLE_ANALYSIS_SAFE"]:
        if c in df.columns:
            if not pd.api.types.is_bool_dtype(df[c]):
                df[c] = df[c].astype(str).str.upper().isin(["TRUE", "1", "YES"])
            else:
                df[c] = df[c].fillna(False)

    # Fill missing UNI_TYPE
    df["UNI_TYPE"] = df["UNI_TYPE"].fillna("Not Specified").astype(str).replace({"nan": "Not Specified"})

    return df


# ---------------------------------------------------------------------------
# Data loading
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
    df = validate_schema(df)

    # Subsets
    df_best = df[df["IS_BEST_NMAT_RECORD"] == True].copy()
    df_obs = df_best[df_best["Year"] <= 2014].copy()

    if "IS_PLE_ANALYSIS_SAFE" in df_obs.columns:
        df_obs["HAS_CONFIRMED_PLE"] = (df_obs["IS_PLE_ANALYSIS_SAFE"] == True)
    else:
        df_obs["HAS_CONFIRMED_PLE"] = False

    return df, df_best, df_obs


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def make_bin_pct(df, group_col):
    """Return (count_df, pct_df) of row-wise bin percentages."""
    ct = pd.crosstab(df[group_col], df["PercentileBin"], dropna=False)
    ct = ct.reindex(columns=BIN_ORDER, fill_value=0)
    ct = ct.apply(pd.to_numeric, errors="coerce")
    pct = ct.div(ct.sum(axis=1).replace(0, np.nan), axis=0).mul(100).fillna(0).round(2)
    return ct, pct


def n_in_bins(df, bins):
    """Return count of rows whose PercentileBin is in the given list."""
    return df["PercentileBin"].isin(bins).sum()


# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------
df_all, df_best, df_obs = load_data()

N_BEST = len(df_best)
N_OBS = len(df_obs)
N_UNIQUE = int(df_best["PERSON_KEY"].nunique())
N_REPEAT = int((df_all.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique() > 1).sum())
N_FOREIGN_ALL = int((df_all["FOREIGNER_STATUS"] == "Verified Foreigner").sum()) if "FOREIGNER_STATUS" in df_all.columns else 0
N_FILIPINO_ALL = int((df_all["CITIZENSHIP_FINAL"] == "Filipino").sum()) if "CITIZENSHIP_FINAL" in df_all.columns else 0

# Pre-compute key values for dynamic captions
_PLE_BIN_ALL = (
    df_obs.dropna(subset=["PercentileBin", "HAS_CONFIRMED_PLE"])
    .groupby("PercentileBin", observed=True)
    .agg(n=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum"))
    .reset_index()
)
_PLE_BIN_ALL.columns = ["Bin", "n", "confirmed"]
_PLE_BIN_ALL["linkage"] = (_PLE_BIN_ALL["confirmed"] / _PLE_BIN_ALL["n"].replace(0, np.nan) * 100).round(2)
_B4_LINKAGE = _PLE_BIN_ALL.loc[_PLE_BIN_ALL["Bin"] == "B4", "linkage"].values[0] if "B4" in _PLE_BIN_ALL["Bin"].values else 0
_B5_LINKAGE = _PLE_BIN_ALL.loc[_PLE_BIN_ALL["Bin"] == "B5", "linkage"].values[0] if "B5" in _PLE_BIN_ALL["Bin"].values else 0

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
- **Percentile bins** -- B1 (0-9) through B10 (90-100).  B4+ means at or above the 30th percentile.  B5+ means at or above the 40th percentile.
- **NMAT-to-PLE linkage** -- the proportion of NMAT examinees who were later matched to PLE passer records.  This is NOT a PLE pass rate.  The dataset does not contain all PLE takers or PLE failures.
- **Foreign examinee counts** -- these are NMAT examinees, not enrolled medical students.  Enrollment numbers would require additional data.
- **All score summaries use recalculated TRUE raw scores** -- the original stored total was inconsistent for 42.2% of records and has been corrected.
        """
    )

# ---------------------------------------------------------------------------
# Tabs
# ---------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "National Profile",
    "30th vs 40th Thresholds",
    "Historical PLE-Passer Linkage",
    "Institution and Foreign Context",
    "Key Evidence for Policy Review",
    "Data, Methods, and Limitations",
])

# ===================================================================
# TAB 1 -- National Profile
# ===================================================================
with tab1:
    st.subheader("National NMAT Profile and Coverage")
    st.caption(
        "What this shows: the size, scope, and basic score distribution of the "
        "NMAT examinee population across 13 examination years.  All score "
        "summaries use recalculated TRUE raw scores (the original stored total "
        "was inconsistent for 42.2% of records and has been corrected)."
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Best-record examinees", f"{N_BEST:,}")
    c2.metric("Unique persons (PERSON_KEY)", f"{N_UNIQUE:,}",
              help="Distinct person identifiers in the best-record subset.")
    c3.metric("NMAT years covered", f"{int(df_best['Year'].nunique())}")
    c4.metric("Median percentile rank", f"{df_best['NMS_PER_num'].median():.1f}")

    # Simplified annual trend (examinee volume + median percentile)
    yearly_summary = (
        df_best.groupby("Year", observed=True)
        .agg(
            examinees=("APPNO_CLEAN", "count"),
            median_pct=("NMS_PER_num", "median"),
            median_raw=("TotalRawScoreTRUE", "median"),
        )
        .reset_index()
    )
    yearly_summary["Year"] = yearly_summary["Year"].astype(str)

    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=("Examinee Volume by Year", "Median Percentile Rank by Year"),
        vertical_spacing=0.12,
    )
    fig.add_trace(go.Bar(x=yearly_summary["Year"], y=yearly_summary["examinees"],
                         name="Examinees", marker_color="#1f77b4",
                         hovertemplate="Year: %{x}<br>Examinees: %{y:,}<extra></extra>"),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=yearly_summary["Year"], y=yearly_summary["median_pct"],
                             mode="lines+markers", name="Median percentile",
                             line=dict(color="#d62728", width=3),
                             hovertemplate="Year: %{x}<br>Median %ile: %{y:.1f}<extra></extra>"),
                  row=2, col=1)
    fig.update_layout(height=500, hovermode="x unified", showlegend=False)
    fig.update_yaxes(title_text="Examinees", row=1, col=1)
    fig.update_yaxes(title_text="Median percentile", row=2, col=1)
    st.plotly_chart(fig, use_container_width=True, key="t1_trend")
    st.caption(
        "Examinee volume has grown substantially since 2015.  Median percentile "
        "has declined from 53-57 in earlier years to 43-48 in 2016-2018.  These "
        "historical trends provide context for evaluating threshold impacts."
    )

    # Composition
    c1, c2 = st.columns(2)
    with c1:
        uni_dist = df_best["UNI_TYPE"].value_counts().reset_index()
        uni_dist.columns = ["UNI_TYPE", "Count"]
        uni_dist["Count"] = pd.to_numeric(uni_dist["Count"], errors="coerce")
        fig = px.pie(uni_dist, names="UNI_TYPE", values="Count",
                     title="University Type Composition")
        fig.update_traces(textinfo="label+percent",
                          hovertemplate="%{label}: %{value} (%{percent})<extra></extra>")
        st.plotly_chart(fig, use_container_width=True, key="t1_uni_pie")

    with c2:
        course_dist = df_best["CourseGroup"].value_counts().reset_index()
        course_dist.columns = ["CourseGroup", "Count"]
        course_dist["Count"] = pd.to_numeric(course_dist["Count"], errors="coerce")
        fig = px.pie(course_dist, names="CourseGroup", values="Count",
                     title="Course Group Composition")
        fig.update_traces(textinfo="label+percent",
                          hovertemplate="%{label}: %{value} (%{percent})<extra></extra>")
        st.plotly_chart(fig, use_container_width=True, key="t1_course_pie")

    # Repeat-taker context
    st.markdown("**Repeat-taker context.** "
                f"Of {N_UNIQUE:,} unique examinees, {N_REPEAT:,} "
                f"({N_REPEAT / N_UNIQUE * 100:.0f}%) took the NMAT more than once "
                "(up to 9 attempts).  All threshold counts in this dashboard use "
                "each examinee's best-record NMAT attempt to avoid inflating the "
                "applicant pool with repeat attempts.")

# ===================================================================
# TAB 2 -- 30th vs 40th Thresholds
# ===================================================================
with tab2:
    st.subheader("Percentile Distribution and Cut-Off Threshold Context")
    st.caption(
        "What this shows: how examinees are distributed across the percentile "
        "spectrum, and how many fall at or above the two major score thresholds "
        "discussed in the CMO (30th and 40th percentile).  These are NMAT "
        "examinee counts, not medical school admission numbers."
    )

    # ---- Heatmap ----
    ct_year, pct_year = make_bin_pct(df_best, "Year")
    pct_year_t = pct_year.T.reindex(BIN_ORDER[::-1])

    fig = px.imshow(
        pct_year_t, text_auto=".1f", aspect="auto",
        color_continuous_scale="YlOrRd",
        labels={"x": "Year", "y": "Percentile Bin", "color": "%"},
        title="Percentile Bin Distribution by NMAT Year (Row % per Year)",
    )
    fig.update_layout(height=460)
    st.plotly_chart(fig, use_container_width=True, key="t2_heatmap")
    st.caption("Darker red = higher concentration in that bin for that year.")

    # Table for heatmap
    _ht_tbl = pct_year.copy()
    _ht_tbl.index.name = "Year"
    _ht_tbl = _ht_tbl.reset_index()
    _ht_tbl["Year"] = _ht_tbl["Year"].astype(str)
    with st.expander("Bin distribution table (row %)", expanded=False):
        st.dataframe(_ht_tbl, use_container_width=True, hide_index=True)

    # ---- 30th vs 40th comparison ----
    st.markdown("### Examinees Meeting Each NMAT Score Threshold")
    df_best_bins = df_best.dropna(subset=["PercentileBin"]).copy()
    df_obs_bins = df_obs.dropna(subset=["PercentileBin"]).copy()

    n_b4plus = n_in_bins(df_best_bins, B4_PLUS)
    n_b5plus = n_in_bins(df_best_bins, B5_PLUS)
    n_b4only = n_in_bins(df_best_bins, ["B4"])

    scenario_rows = [
        {"Threshold": "30th percentile (B4+)", "Best-record examinees": n_b4plus,
         "Share of all (%)": round(n_b4plus / len(df_best_bins) * 100, 1),
         "Observable cohort size": n_in_bins(df_obs_bins, B4_PLUS)},
        {"Threshold": "40th percentile (B5+)", "Best-record examinees": n_b5plus,
         "Share of all (%)": round(n_b5plus / len(df_best_bins) * 100, 1),
         "Observable cohort size": n_in_bins(df_obs_bins, B5_PLUS)},
        {"Threshold": "30th-39th percentile only (B4)", "Best-record examinees": n_b4only,
         "Share of all (%)": round(n_b4only / len(df_best_bins) * 100, 1),
         "Observable cohort size": n_in_bins(df_obs_bins, ["B4"])},
    ]
    st.dataframe(pd.DataFrame(scenario_rows), use_container_width=True, hide_index=True)
    st.caption(
        "The 30th-percentile cut-off (B4+) encompasses a substantially larger pool "
        "than the 40th-percentile cut-off (B5+).  The B4-only group represents "
        "the marginal population affected by a choice between the two thresholds."
    )

    # ---- B4+ vs B5+ by institution type ----
    st.markdown("### Threshold Context by University Type")
    st.caption(
        "This table shows how many examinees from each reported undergraduate "
        "institution type would fall at or above each threshold.  These are NMAT "
        "score distributions, not medical school admissions."
    )

    uni_threshold_rows = []
    for ut in ["Public", "Private", "Foreign", "Not Specified"]:
        sub = df_best_bins[df_best_bins["UNI_TYPE"] == ut]
        if sub.empty:
            continue
        n_ut = len(sub)
        n_ut_b4 = n_in_bins(sub, B4_PLUS)
        n_ut_b5 = n_in_bins(sub, B5_PLUS)
        n_ut_b4o = n_in_bins(sub, ["B4"])
        uni_threshold_rows.append({
            "University Type": ut,
            "Best-record examinees": n_ut,
            "B4+ (30th cut-off)": f"{n_ut_b4} ({round(n_ut_b4 / n_ut * 100, 1)}%)",
            "B5+ (40th cut-off)": f"{n_ut_b5} ({round(n_ut_b5 / n_ut * 100, 1)}%)",
            "B4-only (30th-39th)": f"{n_ut_b4o} ({round(n_ut_b4o / n_ut * 100, 1)}%)",
        })
    uni_threshold_df = pd.DataFrame(uni_threshold_rows)
    st.dataframe(uni_threshold_df, use_container_width=True, hide_index=True)

    # ---- B4 group profile ----
    b4_group = df_best_bins[df_best_bins["PercentileBin"] == "B4"]
    if len(b4_group) > 0:
        st.markdown("### Profile of the 30th-39th Percentile Group (B4)")

        b4_by_uni = b4_group.groupby("UNI_TYPE", observed=True).size().reset_index(name="count")
        b4_by_uni["count"] = pd.to_numeric(b4_by_uni["count"], errors="coerce")
        b4_by_uni["share"] = (b4_by_uni["count"] / b4_by_uni["count"].sum() * 100).round(1)

        c1, c2, c3 = st.columns(3)
        c1.metric("B4 examinees (best record)", f"{len(b4_group):,}")
        c2.metric("Median total raw score",
                  f"{b4_group['TotalRawScoreTRUE'].median():.1f}")
        pub_share = b4_by_uni.loc[b4_by_uni["UNI_TYPE"] == "Public", "share"].values
        c3.metric("Public institution share",
                  f"{pub_share[0]:.1f}%" if len(pub_share) > 0 else "0%")

        fig = px.bar(b4_by_uni, x="UNI_TYPE", y="count",
                     title="B4 Examinees by Institution Type",
                     labels={"count": "Examinees", "UNI_TYPE": ""},
                     color="UNI_TYPE", color_discrete_map=COLORS_UNI)
        st.plotly_chart(fig, use_container_width=True, key="t2_b4_uni")

        # Table for B4 chart
        st.dataframe(b4_by_uni, use_container_width=True, hide_index=True)

    # ---- Top vs bottom bin trend ----
    st.markdown("### Top-Bin (B8-B10) vs Bottom-Bin (B1-B3) Trend")
    _, pct_year2 = make_bin_pct(df_best, "Year")
    top_share = pct_year2[TOP_BINS].sum(axis=1)
    bot_share = pct_year2[BOTTOM_BINS].sum(axis=1)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=top_share.index.astype(str), y=top_share.values,
                  mode="lines+markers", name="Top B8-B10",
                  line=dict(color="#2e7d32", width=3)))
    fig.add_trace(go.Scatter(x=bot_share.index.astype(str), y=bot_share.values,
                  mode="lines+markers", name="Bottom B1-B3",
                  line=dict(color="#c62828", width=3)))
    fig.update_layout(title="Share of Examinees in Top vs Bottom Bins by Year",
                      xaxis_title="Year", yaxis_title="Percent of examinees",
                      height=400)
    st.plotly_chart(fig, use_container_width=True, key="t2_topbot")

    # Table for top/bottom trend
    _tb_tbl = pd.DataFrame({
        "Year": top_share.index.astype(str),
        "Top B8-B10 (%)": top_share.values.round(1),
        "Bottom B1-B3 (%)": bot_share.values.round(1),
        "Difference (pp)": (top_share.values - bot_share.values).round(1),
    }).reset_index(drop=True)
    with st.expander("Top vs bottom bin share table", expanded=False):
        st.dataframe(_tb_tbl, use_container_width=True, hide_index=True)

    # ---- Yearly threshold counts ----
    st.markdown("### Yearly Examinees Meeting Each Threshold")
    yearly_threshold = []
    for yr in sorted(df_best_bins["Year"].dropna().unique()):
        yr_df = df_best_bins[df_best_bins["Year"] == yr]
        yr_obs = df_obs_bins[df_obs_bins["Year"] == yr]
        _b4 = n_in_bins(yr_df, B4_PLUS)
        _b5 = n_in_bins(yr_df, B5_PLUS)
        _ob4 = n_in_bins(yr_obs, B4_PLUS) if not yr_obs.empty else 0
        _ob5 = n_in_bins(yr_obs, B5_PLUS) if not yr_obs.empty else 0
        yearly_threshold.append({
            "Year": int(yr), "Total (best record)": len(yr_df),
            "B4+ (30th cut-off)": _b4,
            "B4+ share (%)": round(_b4 / len(yr_df) * 100, 1),
            "B5+ (40th cut-off)": _b5,
            "B5+ share (%)": round(_b5 / len(yr_df) * 100, 1),
            "Observable B4+": _ob4, "Observable B5+": _ob5,
        })
    st.dataframe(pd.DataFrame(yearly_threshold), use_container_width=True, hide_index=True)
    st.caption(
        "The difference between B4+ and B5+ shares indicates how many additional "
        "examinees would meet a 30th-percentile threshold versus a 40th-percentile "
        "threshold in each year."
    )

# ===================================================================
# TAB 3 -- Historical PLE-Passer Linkage
# ===================================================================
with tab3:
    st.subheader("Historical NMAT-to-PLE-Passer Linkage by Percentile Band")
    st.caption(
        "What this shows: the proportion of NMAT examinees in each percentile band "
        "who were later confirmed as PLE passers, using the observable cohort "
        "(Year <= 2014).  This is an NMAT-to-PLE-passer linkage measure and is "
        "not comparable to an official PLE pass rate."
    )

    st.info(
        "The dataset identifies NMAT examinees who were later matched to PLE passer "
        "records.  It does not contain all PLE takers or PLE failures.  Therefore, "
        "these values represent NMAT-to-PLE-passer linkage, not PLE passing rates. "
        "The observable cohort permits a historical comparison of later confirmed "
        "PLE-passer linkage across NMAT score bands."
    )

    # ---- Linkage by bin ----
    ple_bin = (
        df_obs.dropna(subset=["PercentileBin", "HAS_CONFIRMED_PLE"])
        .groupby("PercentileBin", observed=True)
        .agg(n=("APPNO_CLEAN", "count"), confirmed_passers=("HAS_CONFIRMED_PLE", "sum"))
        .reset_index()
    )
    ple_bin.columns = ["Percentile Bin", "N (observable cohort)", "Confirmed PLE Passers"]
    ple_bin["Linkage Rate (%)"] = (
        ple_bin["Confirmed PLE Passers"] / ple_bin["N (observable cohort)"] * 100
    ).round(2)
    ple_bin["Percentile Bin"] = ple_bin["Percentile Bin"].astype(str)
    ple_bin["Range"] = ple_bin["Percentile Bin"].map(BIN_LABELS)

    fig = px.bar(
        ple_bin, x="Percentile Bin", y="Linkage Rate (%)",
        title="NMAT-to-PLE-Passer Linkage Rate by Percentile Band",
        color="Linkage Rate (%)", color_continuous_scale="Viridis",
        text=ple_bin["Linkage Rate (%)"].round(1).astype(str) + "%",
    )
    fig.update_traces(textposition="outside",
                      hovertemplate="Band: %{x}<br>Linkage: %{y:.1f}%<br>N: %{customdata:,}<extra></extra>",
                      customdata=ple_bin["N (observable cohort)"].values)
    fig.add_hline(y=50, line_dash="dash", line_color="gray", annotation_text="50%")
    fig.update_layout(height=480)
    st.plotly_chart(fig, use_container_width=True, key="t3_ple_bar")

    st.dataframe(ple_bin[["Percentile Bin", "Range", "N (observable cohort)", "Confirmed PLE Passers", "Linkage Rate (%)"]],
                 use_container_width=True, hide_index=True)

    st.markdown(
        f"The B4 band (30th-39th percentile) shows a linkage rate of "
        f"{_B4_LINKAGE:.1f}%, compared to {_B5_LINKAGE:.1f}% for B5 (40th-49th "
        f"percentile).  These are historical descriptive patterns, not causal "
        f"predictions."
    )

    # ---- Score profile by PLE status ----
    st.markdown("### Score Profile by PLE Status")
    desc_cols = [c for c in ["TotalRawScoreTRUE", "NMS_PER_num", "PartIRawScoreTRUE", "PartIIRawScoreTRUE"]
                 if c in df_obs.columns]
    if desc_cols:
        desc = (
            df_obs.groupby("HAS_CONFIRMED_PLE", observed=True)[desc_cols]
            .agg(["count", "median", "mean", lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)])
            .round(2)
        )
        desc.index = ["No confirmed PLE match", "Confirmed PLE passer"]
        st.dataframe(desc, use_container_width=True)

    # ---- Linkage by year ----
    st.markdown("### PLE-Passer Linkage by NMAT Year")
    ple_yr = (
        df_obs.groupby("Year", observed=True)
        .agg(n=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum"))
        .reset_index()
    )
    ple_yr["linkage_pct"] = (ple_yr["confirmed"] / ple_yr["n"] * 100).round(2)
    ple_yr["Year"] = ple_yr["Year"].astype(str)

    fig = px.line(ple_yr, x="Year", y="linkage_pct", markers=True,
                  title="NMAT-to-PLE-Passer Linkage Rate by NMAT Year (Observable Cohort)",
                  labels={"linkage_pct": "Linkage Rate (%)"})
    fig.update_traces(hovertemplate="Year: %{x}<br>Linkage: %{y:.1f}%<br>N: %{customdata:,}<extra></extra>",
                      customdata=ple_yr["n"].values, line=dict(color="#1f77b4", width=3))
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True, key="t3_ple_yr")

    # ---- Linkage by course group ----
    st.markdown("### PLE-Passer Linkage by Course Group")
    if "CourseGroup" in df_obs.columns:
        ple_course = (
            df_obs.dropna(subset=["CourseGroup", "HAS_CONFIRMED_PLE"])
            .groupby("CourseGroup", observed=True)
            .agg(n=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum"),
                 median_pct=("NMS_PER_num", "median"))
            .reset_index()
        )
        ple_course["Linkage Rate (%)"] = (ple_course["confirmed"] / ple_course["n"] * 100).round(2)
        ple_course.columns = [ple_course.columns[0], "N", "Confirmed", "Median %ile", "Linkage Rate (%)"]

        _cg_col = ple_course.columns[0]
        fig = px.bar(ple_course, x=_cg_col, y="Linkage Rate (%)",
                     color=_cg_col,
                     title="NMAT-to-PLE-Passer Linkage Rate by Course Group",
                     text=ple_course["Linkage Rate (%)"].round(1).astype(str) + "%")
        fig.update_traces(textposition="outside")
        fig.update_layout(height=400, showlegend=False, xaxis_tickangle=-20)
        st.plotly_chart(fig, use_container_width=True, key="t3_ple_course")
        st.dataframe(ple_course, use_container_width=True, hide_index=True)

    # ---- Linkage by university type ----
    st.markdown("### PLE-Passer Linkage by University Type")
    if "UNI_TYPE" in df_obs.columns:
        ple_uni = (
            df_obs[df_obs["UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
            .groupby("UNI_TYPE", observed=True)
            .agg(n=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum"),
                 median_pct=("NMS_PER_num", "median"))
            .reset_index()
        )
        ple_uni["Linkage Rate (%)"] = (ple_uni["confirmed"] / ple_uni["n"] * 100).round(2)
        ple_uni.columns = ["University Type", "N", "Confirmed", "Median %ile", "Linkage Rate (%)"]

        fig = px.bar(ple_uni, x="University Type", y="Linkage Rate (%)",
                     color="University Type", color_discrete_map=COLORS_UNI,
                     title="NMAT-to-PLE-Passer Linkage Rate by University Type",
                     text=ple_uni["Linkage Rate (%)"].round(1).astype(str) + "%")
        fig.update_traces(textposition="outside")
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True, key="t3_ple_uni")
        st.dataframe(ple_uni, use_container_width=True, hide_index=True)
        st.caption(
            "The observed difference in linkage rates between institution types "
            "reflects the set of NMAT examinees who were later matched to PLE "
            "passer records.  The data does not identify the reasons for these differences."
        )

# ===================================================================
# TAB 4 -- Institution and Foreign Context
# ===================================================================
with tab4:
    st.subheader("University Type and Institution Context")
    st.caption(
        "What this shows: how NMAT performance varies across Public, Private, "
        "and Foreign institution types.  These classifications refer to the "
        "examinee's recorded undergraduate institution, not necessarily the "
        "medical school they applied to or attended."
    )

    uni_subset = df_best[df_best["UNI_TYPE"].isin(["Public", "Private", "Foreign"])].copy()

    # ---- Score summary ----
    st.markdown("### Score Summary by University Type")
    uni_score = (
        uni_subset.groupby("UNI_TYPE", observed=True)
        .agg(n=("APPNO_CLEAN", "count"),
             median_percentile=("NMS_PER_num", "median"),
             q25_percentile=("NMS_PER_num", lambda x: x.quantile(0.25)),
             q75_percentile=("NMS_PER_num", lambda x: x.quantile(0.75)),
             median_raw=("TotalRawScoreTRUE", "median"),
             median_gps=("NMS_GPS", "median"))
        .round(2).reset_index()
    )
    uni_score.columns = ["University Type", "N (best record)", "Median %ile",
                         "Q25 %ile", "Q75 %ile", "Median Raw Score", "Median GPS"]

    c1, c2 = st.columns([1, 1])
    with c1:
        st.dataframe(uni_score, use_container_width=True, hide_index=True)
    with c2:
        fig = px.box(uni_subset.dropna(subset=["NMS_PER_num"]),
                     x="UNI_TYPE", y="NMS_PER_num",
                     color="UNI_TYPE", color_discrete_map=COLORS_UNI,
                     points=False,
                     title="Percentile Rank Distribution by University Type",
                     labels={"NMS_PER_num": "Percentile Rank", "UNI_TYPE": ""})
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True, key="t4_box_uni")

    # ---- Bin by UNI_TYPE heatmap ----
    st.markdown("### Percentile Bin Distribution by University Type")
    _, uni_bin_pct = make_bin_pct(uni_subset, "UNI_TYPE")
    uni_bin_pct.index.name = "University Type"

    fig = px.imshow(uni_bin_pct, text_auto=".1f", aspect="auto",
                    color_continuous_scale="YlOrRd",
                    labels={"x": "Percentile Bin", "y": "University Type", "color": "%"},
                    title="Bin Distribution by University Type (Row %)")
    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True, key="t4_uni_bin")

    # Table for bin heatmap
    _ub_tbl = uni_bin_pct.reset_index()
    with st.expander("Bin distribution table (row %)", expanded=False):
        st.dataframe(_ub_tbl, use_container_width=True, hide_index=True)

    # ---- Top-bin share ----
    st.markdown("### Top-Bin Share (B8-B10) by University Type")
    top_uni = uni_bin_pct[TOP_BINS].sum(axis=1).sort_values()
    fig = go.Figure(go.Bar(
        x=top_uni.values, y=top_uni.index, orientation="h",
        marker_color=[COLORS_UNI.get(i, "#7f7f7f") for i in top_uni.index],
        text=[f"{v:.1f}%" for v in top_uni.values], textposition="outside",
    ))
    fig.update_layout(title="Top-Bin Share (B8-B10) by University Type",
                      xaxis_title="Percent in B8-B10", yaxis_title="", height=300)
    st.plotly_chart(fig, use_container_width=True, key="t4_top_uni")

    # Table for top-bin share
    _tbuni_tbl = top_uni.reset_index()
    _tbuni_tbl.columns = ["University Type", "Top B8-B10 (%)"]
    with st.expander("Top-bin share table", expanded=False):
        st.dataframe(_tbuni_tbl, use_container_width=True, hide_index=True)

    # ---- Foreign examinee context (descriptive only) ----
    st.markdown("### Foreign Examinee Context")
    st.caption(
        "The available data identify NMAT examinees by citizenship.  These are "
        "NMAT examinees, not enrolled medical students.  The CMO includes "
        "provisions for foreign students, but enrollment numbers would require "
        "separate data from HEIs."
    )

    # Use ALL records for citizenship context (consistent with data-aggregator page 04)
    if "CITIZENSHIP_FINAL" in df_all.columns and "FOREIGNER_STATUS" in df_all.columns:
        foreign_all = df_all[df_all["FOREIGNER_STATUS"] == "Verified Foreigner"]
        filipino_all = df_all[df_all["CITIZENSHIP_FINAL"] == "Filipino"]

        c1, c2, c3 = st.columns(3)
        c1.metric("Verified Foreign NMAT examinees (all records)", f"{len(foreign_all):,}")
        c2.metric("Filipino examinees",
                  f"{len(filipino_all):,}")
        c3.metric("Distinct foreign nationalities",
                  f"{foreign_all['CITIZENSHIP_FINAL'].nunique()}")

        top_nat = foreign_all["CITIZENSHIP_FINAL"].value_counts().head(10).reset_index()
        top_nat.columns = ["Nationality", "Count"]
        top_nat["Count"] = pd.to_numeric(top_nat["Count"], errors="coerce")

        fig = px.bar(top_nat, x="Count", y="Nationality", orientation="h",
                     title="Top 10 Nationalities Among Verified Foreign NMAT Examinees",
                     labels={"Count": "Examinees"})
        fig.update_traces(hovertemplate="%{y}: %{x:,}<extra></extra>")
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True, key="t4_foreign_top")

        # Table for foreign chart
        st.dataframe(top_nat, use_container_width=True, hide_index=True)

# ===================================================================
# TAB 5 -- Key Evidence for Policy Review
# ===================================================================
with tab5:
    st.subheader("Key Evidence for Policy Review")
    st.caption(
        "The following findings synthesise the evidence presented in the "
        "preceding tabs.  They are descriptive observations based on "
        "historical NMAT data (2006-2018) and do not constitute regulatory "
        "recommendations."
    )

    # Pre-compute values for dynamic findings
    _uni_best = df_best.dropna(subset=["PercentileBin"])
    _n_all = len(_uni_best)
    _30th_share = n_in_bins(_uni_best, B4_PLUS) / _n_all * 100
    _40th_share = n_in_bins(_uni_best, B5_PLUS) / _n_all * 100
    _pub_med_pct = df_best[df_best["UNI_TYPE"] == "Public"]["NMS_PER_num"].median()
    _priv_med_pct = df_best[df_best["UNI_TYPE"] == "Private"]["NMS_PER_num"].median()

    _ple_b10 = _PLE_BIN_ALL.loc[_PLE_BIN_ALL["Bin"] == "B10", "linkage"].values
    _ple_b1 = _PLE_BIN_ALL.loc[_PLE_BIN_ALL["Bin"] == "B1", "linkage"].values
    _b10_link = _ple_b10[0] if len(_ple_b10) > 0 else 0
    _b1_link = _ple_b1[0] if len(_ple_b1) > 0 else 0

    # Annual linkage data for 5-year context
    _ann_link = (
        df_obs.groupby("Year", observed=True)
        .agg(n=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum"))
        .reset_index()
    )
    _ann_link["rate"] = (_ann_link["confirmed"] / _ann_link["n"] * 100).round(2)
    _ann_link["5yr"] = _ann_link["rate"].rolling(window=5, min_periods=3).mean().round(2)
    _valid_5yr = _ann_link[_ann_link["5yr"].notna()]
    if not _valid_5yr.empty:
        _latest_5yr = _valid_5yr.iloc[-1]
        _5yr_val = _latest_5yr["5yr"]
        _5yr_yr = int(_latest_5yr["Year"])
    else:
        _5yr_val = None
        _5yr_yr = None

    finding1 = (
        f"The historical NMAT examinee pool ranges from approximately "
        f"{_30th_share:.0f}% meeting a 30th-percentile threshold to "
        f"{_40th_share:.0f}% meeting a 40th-percentile threshold "
        f"(best-record examinees, 2006-2018).  The marginal group between "
        f"the two thresholds -- the 30th-39th percentile band -- accounts "
        f"for roughly {_30th_share - _40th_share:.0f} percentage points "
        f"of the examinee population."
    )

    finding2 = (
        f"Public institution examinees show a higher median percentile rank "
        f"({_pub_med_pct:.0f}) than Private institution examinees "
        f"({_priv_med_pct:.0f}).  This pattern is consistent across all "
        f"NMAT years and may reflect differences in pre-medical preparation, "
        f"admission selectivity, or other institutional factors not captured "
        f"in this dataset."
    )

    finding3 = (
        f"NMAT-to-PLE-passer linkage increases with percentile rank, from "
        f"{_b1_link:.0f}% in the lowest band (B1) to {_b10_link:.0f}% in the "
        f"highest band (B10).  This historical gradient provides context for "
        f"evaluating the relationship between NMAT scores and licensure "
        f"outcomes, but is not a PLE pass rate."
    )

    _yr_trend = _ann_link.copy()
    _first_pct = _yr_trend["rate"].iloc[0] if len(_yr_trend) > 0 else 0
    _last_pct = _yr_trend["rate"].iloc[-1] if len(_yr_trend) > 0 else 0
    finding4 = (
        f"The observable NMAT-to-PLE-passer linkage rate declined from "
        f"{_first_pct:.1f}% in {int(_yr_trend['Year'].iloc[0])} to "
        f"{_last_pct:.1f}% in {int(_yr_trend['Year'].iloc[-1])} across the "
        f"observable cohort.  The 5-year rolling average, which smooths "
        f"annual fluctuations, "
    )
    if _5yr_val is not None:
        finding4 += f"was {_5yr_val:.1f}% as of {_5yr_yr}.  "
    else:
        finding4 += "is shown in the yearly data.  "
    finding4 += (
        "This measure reflects NMAT examinees later matched to PLE passer "
        "records and is not directly comparable to official PLE passing rates."
    )

    finding5 = (
        f"Foreign nationals represent approximately "
        f"{N_FOREIGN_ALL / len(df_all) * 100:.1f}% of all NMAT records "
        f"({N_FOREIGN_ALL:,} verified foreign records out of {len(df_all):,} total).  India accounts for "
        f"the largest share of foreign examinees.  These are NMAT examinee "
        f"counts, not enrolled medical students."
    )

    findings = [
        ("National Threshold Context", finding1),
        ("Institutional Performance Patterns", finding2),
        ("NMAT-to-PLE-Passer Linkage Gradient", finding3),
        ("Historical Linkage Trends", finding4),
        ("Foreign Examinee Presence", finding5),
    ]

    for title, body in findings:
        st.markdown(f"**{title}**")
        st.markdown(body)
        st.divider()

    st.markdown(
        "**Note on data scope.**  These findings are limited to the NMAT "
        "examinee population captured in NMAT_Exodus.parquet.  Key gaps in "
        "the available data include PLE failure rates (only passers are "
        "identifiable), GIDA/IP status, medical school admissions and "
        "enrollment figures, and institutional admission criteria.  See "
        "the Data, Methods, and Limitations tab for full documentation."
    )

# ===================================================================
# TAB 6 -- Data, Methods, and Limitations
# ===================================================================
with tab6:
    st.subheader("Data Context and Methodological Notes")
    st.caption(
        "This section documents the dataset, processing decisions, and "
        "limitations relevant to interpreting the evidence presented."
    )

    st.markdown("### Dataset Overview")
    st.markdown(
        f"""
- **Source file:** `NMAT_Exodus.parquet` (54 columns, {len(df_all):,} rows)
- **Examination years:** 2006-2018
- **Unique examinees (best record):** {N_UNIQUE:,}
- **Observable PLE cohort (Year <= 2014):** {N_OBS:,}
- **Repeat takers:** {N_REPEAT:,} unique persons ({N_REPEAT / N_UNIQUE * 100:.0f}%)
        """
    )

    st.markdown("### Key Methodological Choices")

    with st.expander("TRUE Raw Score Recalculation"):
        n_true = int((df_all["HasTRUErawScores"] == True).sum()) if "HasTRUErawScores" in df_all.columns else 0
        st.markdown(
            f"""
The pipeline recalculated all raw scores from the 8 individual subtest components
because 42.2% of the original stored totals were incorrect.  All analyses in this
dashboard use the recalculated `TotalRawScoreTRUE` scores.

- Rows with complete TRUE scores: {n_true:,} (99.97%)
- Formula mismatches (Total != Part I + Part II): 0
        """
        )

    with st.expander("Best-Record Deduplication"):
        st.markdown(
            f"""
{N_REPEAT:,} examinees ({N_REPEAT / N_UNIQUE * 100:.0f}%) took the NMAT more than
once (up to 9 attempts).  Person-level analyses use the best-record flag
(`IS_BEST_NMAT_RECORD`), which selects:

- For PLE passers: the specific NMAT attempt that matched to the PLE record.
- For others: the highest percentile attempt, with latest year as tiebreaker.

This prevents repeat takers from inflating counts in any percentile band.
        """
        )

    with st.expander("Observable Cohort Definition (Year <= 2014)"):
        avg_gap = df_obs[df_obs["HAS_CONFIRMED_PLE"]]["PLE_YEAR_GAP"].median() if "PLE_YEAR_GAP" in df_obs.columns else "N/A"
        st.markdown(
            f"""
PLE-linked analyses are restricted to examinees whose NMAT year is 2014 or earlier.
This ensures a minimum 5-year window for PLE passage, avoiding the misclassification
of later cohorts as non-passers before their licensure window closes.

- Observable best-record cohort: {N_OBS:,}
- Median NMAT-to-PLE year gap: {avg_gap} years
        """
        )

    with st.expander("Deterministic PLE Matching"):
        n_all_ple = int((df_all["IS_PLE_ANALYSIS_SAFE"] == True).sum()) if "IS_PLE_ANALYSIS_SAFE" in df_all.columns else 0
        n_obs_ple = int(df_obs["HAS_CONFIRMED_PLE"].sum()) if "HAS_CONFIRMED_PLE" in df_obs.columns else 0
        st.markdown(
            f"""
All PLE matching is deterministic (exact NMA_AppNo match, manual AppNo match,
or deterministic AppNo match).  No fuzzy/rapidfuzz matching is used.  This ensures
full auditability but may undercount true matches where the NMAT application number
was recorded differently in the PLE dataset.

- Confirmed PLE passers (all rows): {n_all_ple:,}
- Confirmed PLE passers (best record, observable): {n_obs_ple:,}
        """
        )

    with st.expander("Data Integrity Summary"):
        ci_cols = ["StoredVsDerivedMismatch", "CalcVsDerivedMismatch"]
        if all(c in df_all.columns for c in ci_cols):
            c1, c2 = st.columns(2)
            c1.metric("Stored-vs-derived mismatches",
                      f"{int((df_all['StoredVsDerivedMismatch'] == 1.0).sum()):,}")
            c2.metric("Calc-vs-derived mismatches",
                      f"{int((df_all['CalcVsDerivedMismatch'] == 1.0).sum()):,}")

    st.markdown("### Limitations Relevant to CHED Decision-Making")

    limitations_text = [
        ("PLE Outcomes",
         "The dataset only identifies NMAT examinees later matched to PLE passer "
         "records.  It does not contain all PLE takers or PLE failures.  Therefore, "
         "this dashboard reports NMAT-to-PLE-passer linkage rates, not PLE pass "
         "rates.  Official PLE passing rates published by the PRC should be used "
         "for benchmarking purposes."),
        ("GIDA and IP Status",
         "The dataset does not contain indicators for Geographically Isolated and "
         "Disadvantaged Area (GIDA) residence or Indigenous Peoples (IP) membership.  "
         "The CMO exception for 30th-39th percentile applicants from these groups "
         "requires documentation not available in this dataset."),
        ("Medical School Admissions and Enrollment",
         "This dataset records NMAT examinees, not enrolled medical students.  "
         "The number of examinees at or above a threshold represents the available "
         "applicant pool, not actual enrollment.  HEI-level admissions decisions, "
         "capacity constraints, and selection criteria are not captured."),
        ("Foreign Student Enrollment Cap",
         "The CMO caps foreign student enrollment at 10 slots per incoming class at "
         "SUCs.  The dataset shows NMAT examinees by citizenship, not enrolled "
         "foreign students.  A descriptive foreign-examinee profile is provided, "
         "but this dashboard does not assess compliance with the 10-slot cap."),
        ("Composite Ranking for Foreign Applicants",
         "The CMO encourages composite ranking for foreign applicants.  The dataset "
         "does not contain GWA, interview scores, or other admission criteria "
         "needed for such analysis."),
        ("PHEI Accountability and Sanctions",
         "The CMO ties cut-off privileges to PLE performance and provides for "
         "revocation after three consecutive years below benchmark.  This dashboard "
         "does not assign compliance labels or risk ratings to individual HEIs.  "
         "The NMAT-linked PLE data is not a complete measure of institutional "
         "PLE performance, as it only captures NMAT examinees who later passed "
         "the PLE."),
    ]

    for title, detail in limitations_text:
        st.markdown(f"**{title}**")
        st.markdown(detail)
        st.divider()
