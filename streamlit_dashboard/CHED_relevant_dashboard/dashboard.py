"""CHED Presentation Dashboard -- NMAT Cut-Off Policy Evidence.

A clean, evidence-focused dashboard built from NMAT_Exodus.parquet for
presentation to CHED stakeholders.  Only CMO-relevant insights that are
directly supported by the available data are included.  No compliance
labels, eligibility decisions, or regulatory assessments are assigned.

All aggregation logic lives in ched_common.py and is shared with
export_markdown.py so the dashboard and the exported document can never
silently disagree.
"""

import warnings

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

import ched_common as cc
from export_markdown import build_full_markdown

warnings.filterwarnings("ignore")

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="CHED NMAT Cut-Off Evidence Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BIN_ORDER = cc.BIN_ORDER
BIN_LABELS = cc.BIN_LABELS
B4_PLUS = cc.B4_PLUS
B5_PLUS = cc.B5_PLUS
TOP_BINS = cc.TOP_BINS
BOTTOM_BINS = cc.BOTTOM_BINS
COLORS_BIN = cc.COLORS_BIN
COLORS_UNI = cc.COLORS_UNI
UNI_TYPE_COL = cc.UNI_TYPE_COL
COURSE_GROUP_COL = cc.COURSE_GROUP_COL


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
@st.cache_data(show_spinner="Loading NMAT data ...")
def load_data():
    return cc.load_and_validate()


# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------
df_all, df_best, df_obs = load_data()

kpi1 = cc.compute_tab1_kpis(df_best)
N_BEST, N_UNIQUE = kpi1["n_best"], kpi1["n_unique"]
N_OBS = len(df_obs)
_rep = cc.compute_repeat_taker_stats(df_all, N_UNIQUE)
N_REPEAT, REPEAT_PCT = _rep["n_repeat"], _rep["pct"]
_mismatch = cc.compute_stored_mismatch_stats(df_all)
_true_stats = cc.compute_true_raw_score_stats(df_all)

_df_best_bins = cc.bins_population(df_best)
_df_obs_bins = cc.bins_population(df_obs)

_ple_bin_all = cc.compute_linkage_by(df_obs, "PercentileBin")
_b4_row = _ple_bin_all.loc[_ple_bin_all["PercentileBin"] == "B4"]
_b5_row = _ple_bin_all.loc[_ple_bin_all["PercentileBin"] == "B5"]
_B4_LINKAGE = float(_b4_row["Linkage Rate (%)"].values[0]) if len(_b4_row) else 0.0
_B5_LINKAGE = float(_b5_row["Linkage Rate (%)"].values[0]) if len(_b5_row) else 0.0

_PUB_PRIV_EV = cc.compute_public_private_b5_evidence(_df_best_bins)

SELECTION_EFFECT_NOTE = cc.SELECTION_EFFECT_NOTE
SCOPE_NOTE = cc.SCOPE_NOTE

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("NMAT Performance Evidence for CHED Cut-Off Policy Review")
st.caption(
    f"This dashboard presents descriptive evidence from NMAT_Exodus.parquet "
    f"({len(df_all):,} examinee records, 2006-2018) to inform the CMO amendment on "
    f"NMAT cut-off scores.  All analyses use validated data from the "
    f"4-pipeline processing system.  PLE-linked analyses use the observable "
    f"cohort -- each person's best attempt with Year <= 2014 "
    f"(`IS_BEST_OBSERVABLE_RECORD`) -- to avoid right-censoring bias."
)

with st.expander("How to read this dashboard", expanded=False):
    st.markdown(
        f"""
- **Best-record examinees** -- one NMAT record per person (removes repeat-taker inflation).
- **Observable cohort** -- each person's best NMAT attempt with Year <= 2014, who has had time to take the PLE. This is **not** the same as simply filtering the overall-best record to Year<=2014, which would silently drop people whose best attempt fell in a later year.
- **Score bins** -- B1 (0-9, lowest) through B10 (90-100, highest).  B4+ means at or above Bin 4 (30th-39th).  B5+ means at or above Bin 5 (40th-49th).
- **NMAT-to-PLE linkage** -- the proportion of NMAT examinees who were later matched to PLE passer records.  This is NOT a PLE pass rate.  The dataset does not contain all PLE takers or PLE failures.
- **Foreign examinee counts** -- these are NMAT examinees, not enrolled medical students.  Enrollment numbers would require additional data.
- **All score summaries use recalculated TRUE raw scores.**  Of the {_mismatch['n_stored']:,} records that carry a stored total, {_mismatch['n_mismatch']:,} ({_mismatch['pct_of_stored']:.1f}%) disagreed with the sum of the 8 component subtest scores and have been corrected using the recalculated total.
- {SCOPE_NOTE}
        """
    )

with st.expander("Export Complete Dashboard", expanded=False):
    st.caption(
        "Download a complete Markdown copy of all tabs, charts, "
        "tables, notes, and underlying chart data.  Charts are "
        "generated only when you click \"Generate & Download\"."
    )

    if st.button("Generate & Download (with Charts)", use_container_width=True):
        with st.spinner("Generating charts and markdown..."):
            _md = build_full_markdown(
                df_all=df_all,
                df_best=df_best,
                df_obs=df_obs,
                viz_dir="viz",
            )
            st.session_state["_md_export"] = _md
        st.success("Charts saved to viz/ folder. Click below to download.")

    if "_md_export" in st.session_state:
        st.download_button(
            label="Download Complete Dashboard (Markdown)",
            data=st.session_state["_md_export"],
            file_name="CHED_NMAT_Dashboard_Complete.md",
            mime="text/markdown",
            use_container_width=True,
        )

# ---------------------------------------------------------------------------
# Tabs
# ---------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "National Profile",
    "B4+ vs B5+ Thresholds",
    "PLE-Passer Linkage",
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
        f"What this shows: the size, scope, and basic score distribution of the "
        f"NMAT examinee population across 13 examination years.  All score "
        f"summaries use recalculated TRUE raw scores ({_mismatch['n_mismatch']:,} of "
        f"{_mismatch['n_stored']:,} records with a stored total, or "
        f"{_mismatch['pct_of_stored']:.1f}%, disagreed with the recalculated total and "
        f"were corrected)."
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Best-record examinees", f"{N_BEST:,}")
    c2.metric("Unique persons (PERSON_KEY)", f"{N_UNIQUE:,}",
              help="Distinct person identifiers in the best-record subset. Equal by construction to best-record examinees.")
    c3.metric("NMAT years covered", f"{kpi1['n_years']}")
    c4.metric("Median NMAT percentile", f"{kpi1['median_pct']:.1f}")

    yearly_summary = cc.compute_annual_trend(df_best)
    yearly_summary["Year"] = yearly_summary["Year"].astype(str)

    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=("Examinee Volume by Year", "Median NMAT Percentile by Year"),
        vertical_spacing=0.22,
    )
    fig.add_trace(go.Bar(x=yearly_summary["Year"], y=yearly_summary["Examinees"],
                         name="Examinees", marker_color="#1f77b4",
                         hovertemplate="Year: %{x}<br>Examinees: %{y:,}<extra></extra>"),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=yearly_summary["Year"], y=yearly_summary["Median_percentile"],
                             mode="lines+markers", name="Median NMAT percentile",
                             line=dict(color="#d62728", width=3),
                             hovertemplate="Year: %{x}<br>Median NMAT percentile: %{y:.1f}<extra></extra>"),
                  row=2, col=1)
    fig.update_layout(height=500, hovermode="x unified", showlegend=False)
    fig.update_yaxes(title_text="Examinees", row=1, col=1)
    fig.update_yaxes(title_text="Median NMAT percentile (0-99 scale)", row=2, col=1)
    st.plotly_chart(fig, use_container_width=True, key="t1_trend")
    _first_med = yearly_summary["Median_percentile"].iloc[0]
    _last_med = yearly_summary["Median_percentile"].iloc[-1]
    st.caption(
        f"Examinee volume has grown substantially since 2015.  Median NMAT percentile "
        f"(the raw 0-99 percentile score, not a bin number) moved from "
        f"{_first_med:.0f} in {yearly_summary['Year'].iloc[0]} to {_last_med:.0f} in "
        f"{yearly_summary['Year'].iloc[-1]}.  These historical trends provide context for "
        f"evaluating threshold impacts."
    )

    c1, c2 = st.columns(2)
    with c1:
        uni_dist = cc.compute_composition(df_best, UNI_TYPE_COL)
        fig = px.pie(uni_dist, names=UNI_TYPE_COL, values="Count",
                     title="University Type Composition")
        fig.update_traces(textinfo="label+percent",
                          hovertemplate="%{label}: %{value} (%{percent})<extra></extra>")
        st.plotly_chart(fig, use_container_width=True, key="t1_uni_pie")

    with c2:
        course_dist = cc.compute_composition(df_best, COURSE_GROUP_COL)
        fig = px.pie(course_dist, names=COURSE_GROUP_COL, values="Count",
                     title="Course Group Composition")
        fig.update_traces(textinfo="label+percent",
                          hovertemplate="%{label}: %{value} (%{percent})<extra></extra>")
        st.plotly_chart(fig, use_container_width=True, key="t1_course_pie")

    st.markdown("**Repeat-taker context.** "
                f"Of {N_UNIQUE:,} unique examinees, {N_REPEAT:,} "
                f"({REPEAT_PCT:.0f}%) took the NMAT more than once "
                "(up to 9 attempts).  All threshold counts in this dashboard use "
                "each examinee's best-record NMAT attempt to avoid inflating the "
                "applicant pool with repeat attempts.")

    st.markdown("### Score Bin Reference")
    st.caption("Each bin corresponds to a range of NMAT percentile rank scores.  B1 is the lowest decile, B10 the highest.  B4+ corresponds to the CMO exception floor (30th-39th percentile range).  B5+ corresponds to the SUC standard floor (40th-49th percentile range).")
    st.dataframe(cc.bin_reference_table(), use_container_width=True, hide_index=True)

# ===================================================================
# TAB 2 -- B4+ vs B5+ Thresholds
# ===================================================================
with tab2:
    st.subheader("Score Bin Distribution and Cut-Off Threshold Context")
    st.caption(
        "What this shows: how examinees are distributed across the score "
        "spectrum, and how many fall at or above the two major thresholds "
        "discussed in the CMO (B4+ and B5+).  These are NMAT "
        "examinee counts, not medical school admission numbers."
    )

    ct_year, pct_year = cc.make_bin_pct(df_best, "Year")
    pct_year_t = pct_year.T.reindex(BIN_ORDER[::-1])

    fig = px.imshow(
        pct_year_t, text_auto=True, aspect="auto",
        color_continuous_scale="YlOrRd",
        labels={"x": "Year", "y": "Bin", "color": "%"},
        title="Score Bin Distribution by NMAT Year (Row % per Year)",
    )
    fig.update_layout(height=460)
    st.plotly_chart(fig, use_container_width=True, key="t2_heatmap")
    st.caption("Darker red = higher concentration in that bin for that year.  B1 (lowest decile) at bottom, B10 (highest) at top.")

    _ht_tbl = pct_year.copy()
    _ht_tbl.index.name = "Year"
    _ht_tbl = _ht_tbl.reset_index()
    _ht_tbl["Year"] = _ht_tbl["Year"].astype(str)
    with st.expander("Bin distribution table (row %)", expanded=False):
        st.dataframe(_ht_tbl, use_container_width=True, hide_index=True)

    st.markdown("### Examinees Meeting Each NMAT Score Threshold")
    sc_df = cc.compute_threshold_scenarios(_df_best_bins, _df_obs_bins)
    st.dataframe(sc_df, use_container_width=True, hide_index=True)
    st.caption(
        "The B4+ threshold (Bin 4 and above) encompasses a substantially larger pool "
        "than the B5+ threshold (Bin 5 and above).  The B4-only group represents "
        "the marginal population affected by a choice between the two thresholds."
    )

    st.markdown("### Threshold Context by University Type")
    st.caption(
        "This table shows how many examinees from each reported undergraduate "
        "institution type would fall at or above each threshold.  These are NMAT "
        "score distributions, not medical school admissions.  " + SCOPE_NOTE
    )
    ut_df = cc.compute_threshold_by_uni_type(_df_best_bins)
    st.dataframe(ut_df, use_container_width=True, hide_index=True)

    st.markdown("### Public-Institution Examinees and the B5+ Threshold")
    st.caption(
        "Descriptive only.  The CMO's B4-only exception (30th-39th percentile) is intended for "
        "GIDA/IP-documented applicants; this dataset contains no GIDA/IP field and cannot "
        "determine whether public-undergraduate-institution examinees overlap with that "
        "population.  " + SCOPE_NOTE
    )

    ev = _PUB_PRIV_EV
    c1, c2, c3 = st.columns(3)
    c1.metric("Public examinees meeting B5+", f"{ev['pub_b5']:,} ({ev['pub_b5_pct']}%)",
              help="Public undergraduate-institution examinees who meet the B5+ threshold.")
    c2.metric("Public examinees in B4 only", f"{ev['pub_b4o']:,} ({ev['pub_b4o_pct']}%)",
              help="Public undergraduate-institution examinees in the CMO exception band (B4 only).")
    c3.metric("Private examinees meeting B5+", f"{ev['priv_b5']:,} ({ev['priv_b5_pct']}%)",
              help="Private undergraduate-institution examinees who meet the B5+ threshold.")

    _pub_ev_tbl = pd.DataFrame({
        "Metric": ["Total best-record examinees", "B5+ (Bin 5 and above)", "B5+ share (%)",
                   "B4 only (Bin 4 only)", "B4 only share (%)"],
        "Public": [f"{ev['pub_total']:,}", f"{ev['pub_b5']:,}", f"{ev['pub_b5_pct']}%",
                   f"{ev['pub_b4o']:,}", f"{ev['pub_b4o_pct']}%"],
        "Private": [f"{ev['priv_total']:,}", f"{ev['priv_b5']:,}", f"{ev['priv_b5_pct']}%",
                    f"{ev['priv_b4o']:,}", f"{ev['priv_b4o_pct']}%"],
    })
    st.dataframe(_pub_ev_tbl, use_container_width=True, hide_index=True)
    st.caption(
        f"{ev['pub_b5_pct']}% of public-undergraduate-institution examinees already score at or "
        f"above B5+.  {ev['pub_b4o_pct']}% fall in the B4-only band the CMO exception addresses.  "
        f"Whether this band overlaps with GIDA/IP applicants cannot be determined from this "
        f"dataset -- 'public undergraduate institution' is not a GIDA/IP indicator and "
        f"'public' is not equivalent to 'SUC' as the CMO uses the term."
    )

    b4prof = cc.compute_b4_group_profile(_df_best_bins)
    if b4prof["n"] > 0:
        st.markdown("### Profile of the B4 Group (Bin 4 only)")
        c1, c2, c3 = st.columns(3)
        c1.metric("B4 examinees (best record)", f"{b4prof['n']:,}")
        c2.metric("Median total raw score", f"{b4prof['median_raw']:.1f}")
        c3.metric("Public-institution share", f"{b4prof['pub_share']:.1f}%")

        fig = px.bar(b4prof["by_uni"], x=UNI_TYPE_COL, y="count",
                     title="B4 Examinees by Institution Type",
                     labels={"count": "Examinees", UNI_TYPE_COL: ""},
                     color=UNI_TYPE_COL, color_discrete_map=COLORS_UNI)
        st.plotly_chart(fig, use_container_width=True, key="t2_b4_uni")
        st.dataframe(b4prof["by_uni"], use_container_width=True, hide_index=True)

    st.markdown("### Top Bins (B8-B10) vs Bottom Bins (B1-B3) Trend")
    tb_tbl = cc.compute_top_bottom_trend(df_best)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tb_tbl["Year"], y=tb_tbl["Top B8-B10 (%)"],
                  mode="lines+markers", name="Top B8-B10",
                  line=dict(color="#2e7d32", width=3)))
    fig.add_trace(go.Scatter(x=tb_tbl["Year"], y=tb_tbl["Bottom B1-B3 (%)"],
                  mode="lines+markers", name="Bottom B1-B3",
                  line=dict(color="#c62828", width=3)))
    fig.update_layout(title="Share of Examinees in Top vs Bottom Bins by Year",
                      xaxis_title="Year", yaxis_title="Percent of examinees",
                      height=400)
    st.plotly_chart(fig, use_container_width=True, key="t2_topbot")
    with st.expander("Top vs bottom bin share table", expanded=False):
        st.dataframe(tb_tbl, use_container_width=True, hide_index=True)

    st.markdown("### Yearly Examinees Meeting Each Threshold")
    yt_df = cc.compute_yearly_threshold_counts(_df_best_bins, _df_obs_bins)
    st.dataframe(yt_df, use_container_width=True, hide_index=True)
    st.caption(
        "The difference between B4+ and B5+ shares indicates how many additional "
        "examinees would meet a B4 threshold versus a B5 "
        "threshold in each year."
    )

    st.markdown("### B5+ (Bin 5 and above) PLE-Passer Composition by Year")
    st.caption(
        "Among examinees who meet the B5+ threshold (Bin 5 and above, observable cohort), "
        "this chart shows the count and percentage who were later confirmed as PLE passers "
        "versus those with no confirmed PLE match in this dataset.  'No confirmed match' "
        "does NOT mean 'failed the PLE' -- the PLE source used for matching contains passers "
        "only, so a no-match examinee may have passed under an unmatched name/AppNo, not yet "
        "sat the boards, or genuinely not passed; this dataset cannot distinguish those cases."
    )

    _b5_yr = cc.compute_ple_composition_by_year(df_obs, bins=B5_PLUS, filipino_only=False, strict=False)
    _b5_yr_data = _b5_yr.copy()
    _b5_yr_data["Year"] = _b5_yr_data["Year"].astype(str)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=_b5_yr_data["Year"], y=_b5_yr_data["confirmed"],
        name="Confirmed PLE passer", marker_color="#2e7d32",
        text=_b5_yr_data["confirmed"].astype(str), textposition="inside",
        hovertemplate="Year: %{x}<br>Confirmed PLE passers: %{y:,}<extra></extra>"))
    fig.add_trace(go.Bar(x=_b5_yr_data["Year"], y=_b5_yr_data["no_match"],
        name="No confirmed PLE match", marker_color="#c62828",
        text=_b5_yr_data["no_match"].astype(str), textposition="inside",
        hovertemplate="Year: %{x}<br>No confirmed PLE match: %{y:,}<extra></extra>"))
    fig.update_layout(barmode="stack", title="B5+ Examinees by PLE Status (Count)",
        xaxis_title="Year", yaxis_title="Examinees", height=400)
    st.plotly_chart(fig, use_container_width=True, key="t2_b5_ple_count")

    fig = go.Figure()
    fig.add_trace(go.Bar(x=_b5_yr_data["Year"], y=_b5_yr_data["linkage_pct"],
        name="Confirmed PLE passer", marker_color="#2e7d32",
        text=_b5_yr_data["linkage_pct"].astype(str) + "%", textposition="inside",
        hovertemplate="Year: %{x}<br>Confirmed PLE passers: %{y:.1f}%<extra></extra>"))
    fig.add_trace(go.Bar(x=_b5_yr_data["Year"], y=_b5_yr_data["no_match_pct"],
        name="No confirmed PLE match", marker_color="#c62828",
        text=_b5_yr_data["no_match_pct"].astype(str) + "%", textposition="inside",
        hovertemplate="Year: %{x}<br>No confirmed PLE match: %{y:.1f}%<extra></extra>"))
    fig.update_layout(barmode="stack", title="B5+ Examinees by PLE Status (Percent)",
        xaxis_title="Year", yaxis_title="Percent of B5+ examinees", height=400)
    st.plotly_chart(fig, use_container_width=True, key="t2_b5_ple_pct")

    _b5_display = _b5_yr_data[["Year", "total", "confirmed", "no_match", "linkage_pct"]].copy()
    _b5_display.columns = ["Year", "Total B5+ (observable)", "Confirmed PLE Passers", "No Confirmed Match", "Linkage Rate (%)"]
    st.dataframe(_b5_display, use_container_width=True, hide_index=True)

# ===================================================================
# TAB 3 -- Historical PLE-Passer Linkage
# ===================================================================
with tab3:
    st.subheader("Historical NMAT-to-PLE-Passer Linkage by Score Bin")
    st.caption(
        "What this shows: the proportion of NMAT examinees in each score bin "
        "who were later confirmed as PLE passers, using the observable cohort "
        "(each person's best attempt with Year <= 2014).  This is an NMAT-to-PLE-passer "
        "linkage measure and is not comparable to an official PLE pass rate."
    )

    st.info(
        "The dataset identifies NMAT examinees who were later matched to PLE passer "
        "records.  It does not contain all PLE takers or PLE failures.  Therefore, "
        "these values represent NMAT-to-PLE-passer linkage, not PLE passing rates. "
        "The observable cohort permits a historical comparison of later confirmed "
        "PLE-passer linkage across NMAT score bands."
    )

    ple_bin = _ple_bin_all.copy()
    ple_bin["Score Bin"] = ple_bin["PercentileBin"].astype(str)
    ple_bin["Range"] = ple_bin["Score Bin"].map(BIN_LABELS)

    fig = px.bar(
        ple_bin, x="Score Bin", y="Linkage Rate (%)",
        title="NMAT-to-PLE-Passer Linkage Rate by Percentile Band",
        color="Linkage Rate (%)", color_continuous_scale="Viridis",
        text=ple_bin["Linkage Rate (%)"].round(1).astype(str) + "%",
    )
    fig.update_traces(textposition="outside",
                      hovertemplate="Band: %{x}<br>Linkage: %{y:.1f}%<br>N: %{customdata:,}<extra></extra>",
                      customdata=ple_bin["N"].values)
    fig.add_hline(y=50, line_dash="dash", line_color="gray", annotation_text="50%")
    fig.update_layout(height=480)
    st.plotly_chart(fig, use_container_width=True, key="t3_ple_bar")

    st.dataframe(ple_bin[["Score Bin", "Range", "N", "Confirmed", "Linkage Rate (%)"]]
                 .rename(columns={"N": "N (observable cohort)", "Confirmed": "Confirmed PLE Passers"}),
                 use_container_width=True, hide_index=True)

    st.markdown(
        f"The B4 bin (Bin 4) shows a linkage rate of "
        f"{_B4_LINKAGE:.1f}%, compared to {_B5_LINKAGE:.1f}% for B5 (Bin 5).  "
        f"These are historical descriptive patterns, not causal predictions."
    )
    st.warning(SELECTION_EFFECT_NOTE)

    st.markdown("### Score Profile by PLE Status")
    desc = cc.compute_score_profile_by_ple_status(df_obs)
    if len(desc):
        st.dataframe(desc, use_container_width=True)

    st.markdown("### PLE-Passer Linkage by NMAT Year")
    ple_yr = cc.compute_linkage_by(df_obs, "Year")
    ple_yr_disp = ple_yr.copy()
    ple_yr_disp["Year"] = ple_yr_disp["Year"].astype(str)
    fig = px.line(ple_yr_disp, x="Year", y="Linkage Rate (%)", markers=True,
                  title="NMAT-to-PLE-Passer Linkage Rate by NMAT Year (Observable Cohort)")
    fig.update_traces(hovertemplate="Year: %{x}<br>Linkage: %{y:.1f}%<br>N: %{customdata:,}<extra></extra>",
                      customdata=ple_yr_disp["N"].values, line=dict(color="#1f77b4", width=3))
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True, key="t3_ple_yr")

    st.markdown("### PLE-Passer Linkage by Course Group")
    ple_course = cc.compute_linkage_by(df_obs, COURSE_GROUP_COL)
    if len(ple_course):
        fig = px.bar(ple_course, x=COURSE_GROUP_COL, y="Linkage Rate (%)",
                     color=COURSE_GROUP_COL,
                     title="NMAT-to-PLE-Passer Linkage Rate by Course Group",
                     text=ple_course["Linkage Rate (%)"].round(1).astype(str) + "%")
        fig.update_traces(textposition="outside")
        fig.update_layout(height=400, showlegend=False, xaxis_tickangle=-20)
        st.plotly_chart(fig, use_container_width=True, key="t3_ple_course")
        st.dataframe(ple_course, use_container_width=True, hide_index=True)

    st.markdown("### PLE-Passer Linkage by University Type")
    ple_uni = cc.compute_linkage_by(df_obs[df_obs[UNI_TYPE_COL].isin(["Public", "Private", "Foreign"])], UNI_TYPE_COL)
    if len(ple_uni):
        fig = px.bar(ple_uni, x=UNI_TYPE_COL, y="Linkage Rate (%)",
                     color=UNI_TYPE_COL, color_discrete_map=COLORS_UNI,
                     title="NMAT-to-PLE-Passer Linkage Rate by University Type",
                     text=ple_uni["Linkage Rate (%)"].round(1).astype(str) + "%")
        fig.update_traces(textposition="outside")
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True, key="t3_ple_uni")
        st.dataframe(ple_uni, use_container_width=True, hide_index=True)
        st.caption(
            "The observed difference in linkage rates between undergraduate institution types "
            "reflects the set of NMAT examinees who were later matched to PLE "
            "passer records.  The data does not identify the reasons for these differences.  "
            + SCOPE_NOTE
        )

    st.markdown("### Stress-Test: Defensible PLE Matching Subset")
    st.caption(
        "This section repeats the B5+ PLE-passer linkage analysis using only the strictest "
        "defensible match: a confirmed PLE passer AND at least 5 years between the NMAT "
        "attempt and PLE passage, restricted to Filipino nationals in the B5+ band.  Unlike "
        "the broader B5+ chart above, the population here is NOT pre-filtered on match "
        "status, so this check can genuinely show a lower linkage rate if match quality is "
        "poor -- it is not guaranteed to show 100%."
    )

    st.info(
        "The PLE matching process uses deterministic linking via NMAT application numbers. "
        "While the DE-FUZZY refactor removed all fuzzy matching for full auditability, "
        "the match depends on the application number being recorded consistently across "
        "the NMAT and PLE datasets."
    )

    stress = cc.compute_stress_test(df_obs)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("B5+ Filipino population", f"{stress['n_population']:,}",
              help="Filipino, observable-cohort, B5+ examinees -- NOT pre-filtered on match status.")
    c2.metric("Confirmed under strict criteria", f"{stress['n_confirmed']:,}",
              help="Confirmed PLE passer AND PLE_YEAR_GAP >= 5 years.")
    c3.metric("Strict-criteria linkage rate", f"{stress['linkage_pct']:.1f}%",
              help="confirmed / population -- can genuinely be below 100%.")
    _gap_display = f"{stress['median_gap']:.0f} yrs" if pd.notna(stress["median_gap"]) else "N/A"
    c4.metric("Median PLE year gap", _gap_display)

    st.markdown("#### Yearly Linkage Rate (Strict-Criteria Subset, B5+, Filipino)")
    _cs_yr = stress["yearly"].copy()
    _cs_yr["Year"] = _cs_yr["Year"].astype(str)
    fig = px.line(_cs_yr, x="Year", y="linkage_pct", markers=True,
                  title="NMAT-to-PLE-Passer Linkage Rate (Strict-Criteria B5+ Subset)",
                  labels={"linkage_pct": "Linkage Rate (%)"})
    fig.update_traces(hovertemplate="Year: %{x}<br>Linkage: %{y:.1f}%<br>N: %{customdata:,}<extra></extra>",
                      customdata=_cs_yr["total"].values, line=dict(color="#1f77b4", width=3))
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True, key="t3_clean_ple_yr")
    st.dataframe(_cs_yr[["Year", "total", "confirmed", "no_match", "linkage_pct"]]
                 .rename(columns={"total": "Total", "confirmed": "Confirmed (strict)", "no_match": "No match", "linkage_pct": "Linkage Rate (%)"}),
                 use_container_width=True, hide_index=True)

    st.markdown("#### Strict-Criteria B5+ Confirmed Passers by University Type")
    if len(stress["by_uni"]):
        st.dataframe(stress["by_uni"], use_container_width=True, hide_index=True)

    st.caption(
        f"Under strict matching criteria, {stress['n_confirmed']:,} of {stress['n_population']:,} "
        f"({stress['linkage_pct']:.1f}%) Filipino B5+ observable examinees are confirmed PLE "
        f"passers with a >=5-year gap.  This is a genuine check, not a tautology: it can and "
        f"does show less than 100% linkage.  It indicates that a meaningful share of the "
        f"broader B5+ linkage figures reflect either looser matching criteria or examinees "
        f"who have not yet been confirmed -- not that the underlying data is unreliable."
    )

# ===================================================================
# TAB 4 -- Institution and Foreign Context
# ===================================================================
with tab4:
    st.subheader("University Type and Institution Context")
    st.caption(
        "What this shows: how NMAT performance varies across Public, Private, "
        "and Foreign undergraduate institution types.  " + SCOPE_NOTE
    )

    uni_subset = df_best[df_best[UNI_TYPE_COL].isin(["Public", "Private", "Foreign"])].copy()
    uni_subset_bins = cc.bins_population(uni_subset)

    st.markdown("### Score Summary by University Type")
    uni_score = cc.compute_uni_score_summary(_df_best_bins)
    c1, c2 = st.columns([1, 1])
    with c1:
        st.dataframe(uni_score, use_container_width=True, hide_index=True)
    with c2:
        fig = px.box(uni_subset.dropna(subset=["NMS_PER_num"]),
                     x=UNI_TYPE_COL, y="NMS_PER_num",
                     color=UNI_TYPE_COL, color_discrete_map=COLORS_UNI,
                     points=False,
                     title="NMAT Percentile Distribution by University Type",
                     labels={"NMS_PER_num": "NMAT percentile (0-99)", UNI_TYPE_COL: ""})
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True, key="t4_box_uni")

    st.markdown("### Score Bin Distribution by University Type")
    uni_bin_pct = cc.compute_bin_dist_by(uni_subset, UNI_TYPE_COL).set_index(UNI_TYPE_COL)
    fig = px.imshow(uni_bin_pct, text_auto=True, aspect="auto",
                    color_continuous_scale="YlOrRd",
                    labels={"x": "Score Bin", "y": "University Type", "color": "%"},
                    title="Bin Distribution by University Type (Row %)")
    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True, key="t4_uni_bin")
    with st.expander("Bin distribution table (row %)", expanded=False):
        st.dataframe(uni_bin_pct.reset_index(), use_container_width=True, hide_index=True)

    st.markdown("### Top-Bin Share (B8-B10) by University Type")
    top_uni_tbl = cc.compute_top_bin_share_by(uni_subset, UNI_TYPE_COL)
    fig = go.Figure(go.Bar(
        x=top_uni_tbl["Top B8-B10 (%)"], y=top_uni_tbl[UNI_TYPE_COL], orientation="h",
        marker_color=[COLORS_UNI.get(i, "#7f7f7f") for i in top_uni_tbl[UNI_TYPE_COL]],
        text=[f"{v:.1f}%" for v in top_uni_tbl["Top B8-B10 (%)"]], textposition="outside",
    ))
    fig.update_layout(title="Top-Bin Share (B8-B10) by University Type",
                      xaxis_title="Percent in B8-B10", yaxis_title="", height=300)
    st.plotly_chart(fig, use_container_width=True, key="t4_top_uni")
    with st.expander("Top-bin share table", expanded=False):
        st.dataframe(top_uni_tbl, use_container_width=True, hide_index=True)

    st.markdown("### Foreign Examinee Context")
    st.caption(
        "The available data identify NMAT examinees by citizenship.  These are "
        "best-record NMAT examinees (one per person), not enrolled medical students.  The CMO includes "
        "provisions for foreign students, but enrollment numbers would require "
        "separate data from HEIs.  'Foreign (unspecified)' is an unresolved citizenship "
        "bucket, not a country -- excluded from the nationality ranking below."
    )

    fctx = cc.compute_foreign_context(df_best)
    c1, c2, c3 = st.columns(3)
    c1.metric("Verified Foreign NMAT examinees (best record)", f"{fctx['n_foreign']:,}")
    c2.metric("Filipino examinees", f"{fctx['n_filipino']:,}")
    c3.metric("Distinct foreign nationalities", f"{fctx['n_nationalities']}")

    top_nat = cc.compute_nationality_shares(df_best)
    fig = px.bar(top_nat, x="Count", y="Nationality", orientation="h",
                 title="Top 10 Nationalities Among Verified Foreign NMAT Examinees (Best Record)",
                 labels={"Count": "Examinees"})
    fig.update_traces(hovertemplate="%{y}: %{x:,}<extra></extra>")
    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True, key="t4_foreign_top")
    st.dataframe(top_nat, use_container_width=True, hide_index=True)
    st.caption(
        "Share is of ALL verified-foreign best-record examinees "
        f"({fctx['n_foreign']:,}), not of the top-10 subtotal shown here."
    )

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

    findings = cc.compute_tab5_finding_texts(df_all, df_best, df_obs)

    for title, body in findings:
        st.markdown(f"**{title}**")
        st.markdown(body)
        st.divider()

    st.markdown(
        "**Note on data scope.**  These findings are limited to the NMAT "
        "examinee population captured in NMAT_Exodus.parquet.  Key gaps in "
        "the available data include PLE failure rates (only passers are "
        "identifiable), GIDA/IP status, medical school admissions and "
        "enrollment figures, and institutional admission criteria.  " + SCOPE_NOTE + "  See "
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
- **Source file:** `NMAT_Exodus.parquet` ({df_all.shape[1]} columns, {len(df_all):,} rows)
- **Examination years:** 2006-2018
- **Unique examinees (best record):** {N_UNIQUE:,}
- **Observable PLE cohort (best attempt, Year <= 2014):** {N_OBS:,}
- **Repeat takers:** {N_REPEAT:,} unique persons ({REPEAT_PCT:.0f}%)
        """
    )

    _amb = cc.compute_ambiguous_person_stats(df_all)
    if _amb["n_ambiguous_keys"] is not None:
        st.caption(
            f"**Data quality note:** {_amb['n_ambiguous_keys']:,} `PERSON_KEY` identifiers have "
            f"contradictory `SEX` recorded across their rows (`PERSON_KEY_AMBIGUOUS`), indicating "
            f"a possible identity collision. These records are still included in all counts above; "
            f"this is disclosed, not hidden or corrected silently."
        )

    st.markdown("### Key Methodological Choices")

    with st.expander("TRUE Raw Score Recalculation"):
        st.markdown(
            f"""
The pipeline recalculated all raw scores from the 8 individual subtest components.
Of the {_mismatch['n_stored']:,} records that carry a stored total, {_mismatch['n_mismatch']:,}
({_mismatch['pct_of_stored']:.1f}%) disagreed with the sum of the 8 component subtest scores
({_mismatch['pct_of_all']:.1f}% of all {len(df_all):,} records).  All analyses in this
dashboard use the recalculated `TotalRawScoreTRUE` scores.

- Rows with complete TRUE scores: {_true_stats['n_true']:,} ({_true_stats['pct_true']:.2f}%)
- Stored-total mismatches: {_mismatch['n_mismatch']:,} of {_mismatch['n_stored']:,} rows with a
  stored total ({_mismatch['pct_of_stored']:.1f}%)
        """
        )

    with st.expander("Best-Record Deduplication"):
        st.markdown(
            f"""
{N_REPEAT:,} examinees ({REPEAT_PCT:.0f}%) took the NMAT more than
once (up to 9 attempts).  Person-level analyses use the best-record flag
(`IS_BEST_NMAT_RECORD`), which selects, for every person, the single attempt with the
highest NMAT percentile, latest year as tiebreaker, then lowest application number --
one uniform rule applied identically to passers and non-passers alike.

- Best-record examinees: {N_BEST:,}
- Unique persons: {N_UNIQUE:,} (equal by construction -- exactly one best record per person)

This prevents repeat takers from inflating counts in any percentile band.
        """
        )

    with st.expander("Observable Cohort Definition (Year <= 2014)"):
        avg_gap = df_obs.loc[df_obs["HAS_CONFIRMED_PLE"], "PLE_YEAR_GAP"].median()
        st.markdown(
            f"""
PLE-linked analyses use each person's best NMAT attempt among rows with Year <= 2014
(`IS_BEST_OBSERVABLE_RECORD`).  This is deliberately **not** the same as filtering the
overall best-record flag to Year<=2014, which would silently drop people whose
overall-best attempt fell after 2014 and inflate the observed linkage rate.

- Observable cohort (best attempt within window): {N_OBS:,}
- Median NMAT-to-PLE year gap among confirmed passers: {avg_gap:.0f} years
        """
        )

    with st.expander("Deterministic PLE Matching"):
        match_stats = cc.compute_ple_matching_stats(df_all, df_obs)
        outcome = match_stats["outcome_counts"]
        st.markdown(
            f"""
All PLE matching is deterministic (exact NMA_AppNo match, manual AppNo match,
or deterministic AppNo match).  No fuzzy/rapidfuzz matching is used.  This ensures
full auditability but has important caveats:

- The NMAT application number (NMA_AppNo) is not a well-established, consistent
  identifier across datasets.  The matching process depends on this number being
  recorded identically in both the NMAT and PLE datasets, which is not always the
  case.  Undercounting is possible where numbers differ.
- Match outcome breakdown (`PLE_MATCH_OUTCOME`, all rows): **accepted** {outcome.get('accepted', 0):,},
  **rejected_ambiguous_person** {outcome.get('rejected_ambiguous_person', 0):,} (a name-collision
  candidate was found but rejected as genuinely ambiguous by the disambiguator -- distinguished from
  a bare "no match" so a reader can see where borderline candidates went), **no_match**
  {outcome.get('no_match', 0):,}.  `PLE_YEAR_UNCERTAIN` additionally flags
  {match_stats['n_year_uncertain']:,} confirmed passers whose PLE year is not determinable; they
  remain counted as passers but are excluded from any year-specific figure.
- Three other columns carry PLE-related metadata but are **not** authoritative passer counts and
  do not nest inside `IS_PLE_PASSER`: `PLE_YEAR_PASSED` is non-null for
  {match_stats['n_year_passed_notna']:,} rows, `PLE_MATCH_METHOD` for
  {match_stats['n_match_method_notna']:,} rows, `PLE_YEAR_GAP` for
  {match_stats['n_year_gap_notna']:,} rows.  Only `IS_PLE_PASSER` should be used as the passer flag.
- The "Stress-Test" analysis in Tab 3 uses the strictest criteria (confirmed match, >=5 year gap,
  Filipino nationals only) as a genuine, non-tautological sensitivity check -- see Tab 3 for the
  result, which is below 100% linkage.
- Confirmed PLE passers (all rows): {match_stats['n_all_ple']:,}
- Confirmed PLE passers (best-attempt, observable cohort): {match_stats['n_obs_ple']:,}
        """
        )

    with st.expander("Data Integrity Summary"):
        st.metric("Stored-vs-derived mismatches",
                  f"{_mismatch['n_mismatch']:,} of {_mismatch['n_stored']:,} rows with a stored total "
                  f"({_mismatch['pct_of_stored']:.1f}%)")

    st.markdown("### Limitations Relevant to CHED Decision-Making")

    limitations_text = cc.compute_limitations_cards(df_all, df_best, df_obs)

    for title, detail in limitations_text:
        st.markdown(f"**{title}**")
        st.markdown(detail)
        st.divider()
