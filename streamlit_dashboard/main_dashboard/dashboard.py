import os
import sys
from pathlib import Path
import warnings
import concurrent.futures

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import cudf.pandas
    cudf.pandas.install()
    print("cuDF Pandas acceleration activated.")
except Exception:
    pass

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import duckdb
import streamlit as st
from scipy import stats

import main_common as mc
from export_markdown import build_full_markdown

warnings.filterwarnings("ignore")

try:
    import scikit_posthocs as sp
    HAS_POSTHOCS = mc.HAS_POSTHOCS
except Exception:
    HAS_POSTHOCS = False


# -----------------------------------------------------------------------------
# CONFIG
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="NMAT Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Constants below are the SAME objects main_common.py uses -- aliased here
# (not redefined) so dashboard.py and export_markdown.py can never drift.
BIN_ORDER = mc.BIN_ORDER
PLE_ORDER = mc.PLE_ORDER
TOP_BINS = mc.TOP_BINS
BOTTOM_BINS = mc.BOTTOM_BINS
PALETTE_UNI = mc.PALETTE_UNI
PALETTE_COURSE = mc.PALETTE_COURSE
PALETTE_PLE = mc.PALETTE_PLE
BIN_COLORS = mc.BIN_COLORS
NUMERIC_COLS = mc.NUMERIC_COLS
BOOL_COLS = mc.BOOL_COLS
REQUIRED_PIPELINE_COLS = mc.REQUIRED_PIPELINE_COLS

# Pure-compute helpers (find_data_path, to_bool_series, classify_course,
# count_true_flags, ensure_required_columns, load_data_and_subsets,
# filter_df, pct_table, make_flow, kruskal_table, mc.mann_whitney_ple,
# chi_square_unitype_bin, get_yearly_summary, mc.subtest_mean_table,
# radar_for_group) all live in main_common.py now -- call as mc.<name>.
# Only chart-DRAWING functions (figure out, no new aggregation) stay below.


# -----------------------------------------------------------------------------
# CHART-DRAWING HELPERS (data comes from main_common; these only plot it)
# -----------------------------------------------------------------------------
def make_heatmap(table: pd.DataFrame, title: str, xlab: str, ylab: str, color_scale="Blues"):
    fig = px.imshow(
        table,
        text_auto=".1f",
        aspect="auto",
        color_continuous_scale=color_scale,
        labels={"x": xlab, "y": ylab, "color": "Percent"},
        title=title,
    )
    fig.update_traces(
        hovertemplate=f"{ylab}: %{{y}}<br>{xlab}: %{{x}}<br>Percent: %{{z:.2f}}<extra></extra>"
    )
    fig.update_layout(height=450)
    return fig


def make_stacked_pct_bar(pct_df: pd.DataFrame, title: str, xlab: str, ylab: str, color_map=None):
    plot_df = pct_df.reset_index().melt(id_vars=pct_df.index.name or "index", var_name="Category", value_name="Percent")
    idx_name = pct_df.index.name or "index"
    fig = px.bar(
        plot_df,
        x=idx_name,
        y="Percent",
        color="Category",
        title=title,
        labels={idx_name: xlab, "Percent": ylab},
        color_discrete_map=color_map,
    )
    fig.update_traces(
        hovertemplate=f"{xlab}: %{{x}}<br>Category: %{{fullData.name}}<br>{ylab}: %{{y:.2f}}%<extra></extra>"
    )
    fig.update_layout(barmode="stack", height=450, legend_title_text="")
    return fig


def make_top_share_bar(series: pd.Series, title: str, xlab: str, ylab: str, color_map=None):
    s = series.sort_values()
    colors = [color_map.get(i, "#7f7f7f") if color_map else "#1f77b4" for i in s.index]
    fig = go.Figure(
        go.Bar(
            x=s.values,
            y=s.index.astype(str),
            orientation="h",
            marker_color=colors,
            text=[f"{v:.1f}%" for v in s.values],
            textposition="outside",
            hovertemplate=f"{ylab}: %{{y}}<br>{xlab}: %{{x:.2f}}%<extra></extra>",
        )
    )
    fig.update_layout(title=title, xaxis_title=xlab, yaxis_title=ylab, height=450)
    return fig


def make_sankey(flow: pd.DataFrame, source_col: str, target_col: str, title: str, source_colors=None, target_colors=None):
    source_nodes = flow[source_col].astype(str).drop_duplicates().tolist()
    target_nodes = flow[target_col].astype(str).drop_duplicates().tolist()
    labels = source_nodes + target_nodes
    node_map = {label: i for i, label in enumerate(labels)}

    sources = flow[source_col].astype(str).map(node_map).tolist()
    targets = flow[target_col].astype(str).map(node_map).tolist()
    values = flow["count"].tolist()

    use_custom_colors = bool(source_colors or target_colors)

    node_dict = dict(
        pad=18,
        thickness=18,
        line=dict(color="black", width=0.4),
        label=labels,
    )
    link_dict = dict(
        source=sources,
        target=targets,
        value=values,
    )

    if use_custom_colors:
        node_colors = []
        for lab in labels:
            if source_colors and lab in source_colors:
                node_colors.append(source_colors[lab])
            elif target_colors and lab in target_colors:
                node_colors.append(target_colors[lab])
            else:
                node_colors.append("#bdbdbd")

        link_colors = []
        for _, r in flow.iterrows():
            tgt = str(r[target_col])
            src = str(r[source_col])
            if target_colors and tgt in target_colors:
                link_colors.append(target_colors[tgt])
            elif source_colors and src in source_colors:
                link_colors.append(source_colors[src])
            else:
                link_colors.append("rgba(160,160,160,0.45)")

        node_dict["color"] = node_colors
        link_dict["color"] = link_colors

    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="snap",
                node=node_dict,
                link=link_dict,
            )
        ]
    )
    fig.update_traces(
        node_hovertemplate="%{label}<extra></extra>",
        link_hovertemplate=f"{source_col}: %{{source.label}}<br>{target_col}: %{{target.label}}<br>Count: %{{value}}<extra></extra>",
    )
    fig.update_layout(title=title, height=560)
    return fig


def make_trends_figure(summary: pd.DataFrame, sittings_by_year: pd.Series = None):
    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Median TRUE Raw Score (with IQR)",
            "Median Part I vs Part II Raw Score",
            "Median Percentile Rank (with IQR)",
            "Examinees (best-record) vs. Total Sittings by Year",
        ),
    )

    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["raw_q75"], mode="lines", line=dict(color="lightblue"), showlegend=False), 1, 1)
    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["raw_q25"], mode="lines", fill="tonexty", fillcolor="rgba(31,119,180,0.25)", line=dict(color="lightblue"), name="Raw IQR"), 1, 1)
    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["raw_median"], mode="lines+markers", name="Median raw", line=dict(color="#1f77b4", width=3)), 1, 1)

    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["part1_median"], mode="lines+markers", name="Part I", line=dict(color="#2ca02c", width=3)), 1, 2)
    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["part2_median"], mode="lines+markers", name="Part II", line=dict(color="#ff7f0e", width=3)), 1, 2)

    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["per_q75"], mode="lines", line=dict(color="lightsalmon"), showlegend=False), 2, 1)
    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["per_q25"], mode="lines", fill="tonexty", fillcolor="rgba(255,127,14,0.22)", line=dict(color="lightsalmon"), name="Percentile IQR"), 2, 1)
    fig.add_trace(go.Scatter(x=summary["Year"], y=summary["per_median"], mode="lines+markers", name="Median percentile", line=dict(color="#d62728", width=3)), 2, 1)

    fig.add_trace(go.Bar(x=summary["Year"], y=summary["n"], name="Examinees (best-record)"), 2, 2)
    if sittings_by_year is not None:
        fig.add_trace(
            go.Bar(x=sittings_by_year.index, y=sittings_by_year.values, name="Total sittings (all attempts)"),
            2, 2,
        )
        fig.update_layout(barmode="group")

    fig.update_layout(height=760, hovermode="x unified")
    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="Score", row=1, col=1)
    fig.update_yaxes(title_text="Score", row=1, col=2)
    fig.update_yaxes(title_text="Percentile", row=2, col=1)
    fig.update_yaxes(title_text="Count", row=2, col=2)
    return fig


def make_box_by_year(df: pd.DataFrame, value_col: str, title: str):
    tmp = df.dropna(subset=["Year", value_col]).copy()
    fig = px.box(tmp, x="Year", y=value_col, points=False, title=title)
    fig.update_traces(hovertemplate="Year: %{x}<br>Value: %{y:.2f}<extra></extra>")
    fig.update_layout(height=420)
    return fig



# -----------------------------------------------------------------------------
# LOAD
# -----------------------------------------------------------------------------
@st.cache_data(show_spinner="Loading NMAT data ...")
def load_data_and_subsets():
    return mc.load_data_and_subsets()


df_raw, subsets, data_path = load_data_and_subsets()

# Schema-drift sanity check: the pipeline regenerates this parquet in place, so a silent shape
# change (upstream bug, wrong file picked up, partial write) would otherwise show up only as
# subtly wrong numbers deep in a tab. Make it loud instead.
EXPECTED_ROWS = 178_927
EXPECTED_COLS = 53
if len(df_raw) != EXPECTED_ROWS or len(df_raw.columns) != EXPECTED_COLS:
    st.warning(
        f"Schema drift detected: loaded {len(df_raw):,} rows x {len(df_raw.columns)} columns from "
        f"`{data_path}`, expected {EXPECTED_ROWS:,} rows x {EXPECTED_COLS} columns. Figures on this "
        "page may not match prior documentation until this is investigated."
    )

dfbesttrend = subsets["besttrend"]
dfbestobservable = subsets["bestobservable"]

# --- Citizenship profile lookup ---
# Citizenship columns (CITIZENSHIP_FINAL, FOREIGNER_STATUS) are now baked into NMAT_Exodus.parquet by Pipeline 4
_PC_LOOKUP_AVAILABLE = True

# -----------------------------------------------------------------------------
# SIDEBAR  (filters only -- navigation is now handled by st.tabs)
# -----------------------------------------------------------------------------
st.sidebar.subheader("Global filters")

year_options = sorted([int(x) for x in dfbesttrend["Year"].dropna().unique()])
unitype_options = sorted(dfbesttrend["UNDERGRAD_UNI_TYPE"].dropna().astype(str).unique().tolist())
course_options = sorted(dfbesttrend["UNDERGRAD_COURSE_GROUP"].dropna().astype(str).unique().tolist())
sex_options = sorted([x for x in dfbesttrend["SEX_CLEAN"].dropna().astype(str).unique().tolist() if x])

selected_years = st.sidebar.multiselect("Year", year_options, default=year_options)
selected_unitypes = st.sidebar.multiselect("University type", unitype_options, default=unitype_options)
selected_courses = st.sidebar.multiselect("Course group", course_options, default=course_options)
selected_sexes = st.sidebar.multiselect("Sex", sex_options, default=sex_options)

apply_ple_status_filter = st.sidebar.checkbox("Filter PLE pages by status", value=False)
selected_ple_status = PLE_ORDER if apply_ple_status_filter else None
if apply_ple_status_filter:
    selected_ple_status = st.sidebar.multiselect("PLE status", PLE_ORDER, default=PLE_ORDER)

st.sidebar.divider()
st.sidebar.caption(f"Source file: {data_path}")

# common filtered subsets
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_name = {
        executor.submit(
            mc.filter_df,
            df,
            years=selected_years,
            unitypes=selected_unitypes,
            courses=selected_courses,
            sexes=selected_sexes,
            ple_status=selected_ple_status if name in ["bestobservable", "uniobservable"] else None,
        ): name
        for name, df in subsets.items()
    }
    F = {}
    for future in concurrent.futures.as_completed(future_to_name):
        name = future_to_name[future]
        F[name] = future.result()

# Merge citizenship lookup into the observable university subset
_uniobs_pc = F["uniobservable"].copy()
# CITIZENSHIP_FINAL and FOREIGNER_STATUS are already available in the parquet from Pipeline 4

# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------
st.title("NMAT Performance Dashboard, 2006-2018")
st.caption("Descriptive, trend-based, and policy-oriented summaries based on the cleaned NMAT_Exodus pipeline. Person-level views use one best NMAT record per examinee; PLE-linked person-level pages use the observable cohort (Year <= 2014).")

with st.expander("Read this first: how to interpret the dashboard", expanded=True):
    st.markdown(
        """
**People vs. sittings.** Every applicant can sit the NMAT more than once (25% do). "Best-record" pages
collapse this to one row per person (`IS_BEST_NMAT_RECORD`, the person's highest-percentile / latest-year /
lowest-appno-tiebreak attempt) — use these for "how many examinees" questions. Pages that instead need every
attempt (e.g. Repeat Takers) use the full, non-deduplicated rows — this is stated in each page's caption.

**The observable cohort.** The PLE source list can only contain people who have *already* passed by the time
the data was collected. Examinees from Year > 2014 have not had enough time to plausibly appear in it, so
comparing them to earlier years as if they "failed" is a recency artifact, not a real outcome. `IS_OBSERVABLE_COHORT`
(Year <= 2014) restricts a page to years old enough to be fairly judged. For **person-level** PLE-linked pages
the correct cohort is `IS_BEST_OBSERVABLE_RECORD` — a person's best attempt *within* that window — which is
**not** the same as "this person's overall best attempt happens to fall before 2015" (that narrower, incorrect
filter silently drops people whose single best sitting came later even though they also sat, and could have
linked, within the observable window).

**Linkage rate, not pass rate.** The PLE source used to build `IS_PLE_PASSER` contains **passers only** — there
is no fail list anywhere in this pipeline. So "No confirmed PLE match" means *not found in the passer list*,
which can mean they failed, haven't sat the boards yet, sat after this data's coverage window, or were missed
by the deterministic matcher — never only "failed." Every percentage built from `IS_PLE_PASSER` in this
dashboard is therefore a **linkage rate**, not a licensure pass rate, and is labeled that way throughout.

**Percentile bins.** `B1` is the **lowest** decile (percentile 0-9); `B10` is the **highest** (90-99). Bins are
always ordered B1 -> B10 on every chart and table in this app.

**Undergraduate institution, not medical school.** `UNDERGRAD_UNIVERSITY` / `UNDERGRAD_UNI_TYPE` /
`UNDERGRAD_UNI_LOCATION` record where the examinee earned their **bachelor's degree**, sat *before* the NMAT.
No column in this dataset identifies the medical school the examinee later attended, so nothing here can be
read as a statement about any medical school's teaching quality or licensure-exam performance.
        """
    )

with st.expander("Export Complete Dashboard", expanded=False):
    st.caption(
        "Download a complete Markdown copy of all 13 tabs, charts, tables, and notes as data. "
        "This export always uses the FULL, UNFILTERED dataset (not the sidebar filters currently "
        "applied above) so the document is a complete, reproducible picture of the pipeline output."
    )

    if st.button("Generate & Download", use_container_width=True, key="btn_generate_export"):
        with st.spinner("Generating markdown export..."):
            _md = build_full_markdown(df_raw, subsets)
            st.session_state["_md_export"] = _md
        st.success("Export generated. Click below to download.")

    if "_md_export" in st.session_state:
        st.download_button(
            label="Download Complete Dashboard (Markdown)",
            data=st.session_state["_md_export"],
            file_name="NMAT_Main_Dashboard_Complete.md",
            mime="text/markdown",
            use_container_width=True,
        )

(
    tab1, tab2, tab3, tab4, tab5, tab6,
    tab7, tab8, tab9, tab10, tab11, tab12, tab13,
) = st.tabs([
    "🏠 Executive Summary",
    "🧪 Data Integrity",
    "📈 Trends & Stability",
    "📊 Score Bins & Background",
    "🏫 University Type Analysis",
    "🔄 Flow & Pathways",
    "🎯 PLE Alignment",
    "🔁 Repeat Takers",
    "🧠 Subtests & Profiles",
    "⏰ Year Gap & Gender",
    "📐 Statistical Tests",
    "📋 Policy Tables & Export",
    "⚖️ CHED Compliance",
])

# -----------------------------------------------------------------------------
# TAB 1
# -----------------------------------------------------------------------------
with tab1:
    base = F["besttrend"]
    observable = F["bestobservable"]

    st.subheader("Executive Summary")
    st.caption("High-level summary of examinee volume, score levels, composition, and observable PLE alignment using the filtered best-record cohort.")

    # Exactly one examinee-count KPI: IS_BEST_NMAT_RECORD is one row per PERSON_KEY system-wide,
    # so len(base) == base['PERSON_KEY'].nunique() by construction -- do not show both as if they
    # could disagree (that was the old F10 defect; the old two-KPI framing implied they might not).
    _t1_kpis = mc.compute_tab1_kpis(base, observable, F["trend"])
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Examinees (best-record)", f"{_t1_kpis['n_best']:,}", help="One row per unique PERSON_KEY: the person's single best NMAT attempt under the current filters.")
    col2.metric("Years covered", f"{_t1_kpis['n_years']:,}", help="Distinct NMAT years represented after filters are applied.")
    col3.metric("Median TRUE raw score", f"{_t1_kpis['median_raw']:.1f}", help="Median of TotalRawScoreTRUE in the filtered best-record trend cohort.")
    col4.metric("Median percentile rank", f"{_t1_kpis['median_pct']:.1f}", help="Median of NMS_PER_num in the filtered best-record trend cohort.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Repeat takers", f"{_t1_kpis['n_repeat']:,}", help="People with more than one distinct NMAT application (APPNO_CLEAN) linked to the same PERSON_KEY, counted over all sittings, not the best-record cohort.")
    col2.metric("Repeat-taker share", f"{_t1_kpis['repeat_share_pct']:.1f}%" if _t1_kpis['repeat_share_pct'] is not None else "N/A", help="Repeat takers as a share of examinees in this KPI row's cohort.")
    col3.metric("Observable cohort (IS_BEST_OBSERVABLE_RECORD)", f"{_t1_kpis['n_observable']:,}", help="One row per person: their best attempt among sittings with Year <= 2014. Used for all person-level PLE-linked pages.")
    col4.metric("PLE linkage rate, observable cohort", f"{_t1_kpis['ple_linkage_pct']:.2f}%" if _t1_kpis['ple_linkage_pct'] is not None else "N/A", help="Share of the observable cohort found in the PLE passer source list (IS_PLE_PASSER). This is a LINKAGE rate, not a pass rate -- see 'Read this first' above.")

    st.markdown("""
    📚 **Course Group Distribution**

    Course groups are sourced directly from the cleaned pipeline output (`UNDERGRAD_COURSE_GROUP`):

    - **Medical & Allied**: Medical, Nursing, Pharmacy, Health-related
    - **Natural Sciences**: Biology, Physics, Chemistry, Natural Sciences
    - **Social & Behavioral Sciences**: Psychology, Economics, Social Sciences
    - **Engineering & Technology**: Engineering, Technology fields
    - **Education**: Teacher training, Education programs
    - **Other**: All remaining courses
    """)

    exec_tab1, exec_tab2, exec_tab3 = st.tabs(["📊 Overview", "📈 Composition", "📋 Quick Tables"])

    with exec_tab1:
        st.markdown("**Figure 1. Annual NMAT score and volume profile**")
        st.caption(
            "Score panels (raw, Part I/II, percentile) use the best-record cohort: one attempt per person. "
            "The volume panel shows best-record examinees alongside total sittings (all attempts, undeduped) "
            "because a repeat taker's earlier attempts are otherwise invisible in the year they occurred."
        )
        summary = mc.get_yearly_summary(base)
        _sittings_by_year = mc.compute_sittings_by_year(F["trend"])
        st.plotly_chart(make_trends_figure(summary, _sittings_by_year), use_container_width=True, key="fig_t1_trends")

    with exec_tab2:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Figure 2. Course-group composition of best-record examinees**")
            st.caption("Values are counts of filtered best-record examinees by category.")
            course_dist = mc.compute_composition(base, "UNDERGRAD_COURSE_GROUP")
            fig = px.pie(course_dist, names="UNDERGRAD_COURSE_GROUP", values="Count")
            st.plotly_chart(fig, use_container_width=True, key="fig_t1_course_pie")
        with c2:
            st.markdown("**Figure 3. University-type composition of best-record examinees**")
            st.caption("Percent shares refer to the current filtered cohort only.")
            uni_dist = mc.compute_composition(base, "UNDERGRAD_UNI_TYPE")
            fig = px.pie(uni_dist, names="UNDERGRAD_UNI_TYPE", values="Count")
            st.plotly_chart(fig, use_container_width=True, key="fig_t1_uni_pie")

    with exec_tab3:
        st.markdown("**Table 1. Executive summary indicators**")
        st.caption("This table reports central score levels and the shares of examinees in the upper and lower bins. Top-bin share refers to B8-B10, while bottom-bin share refers to B1-B3.")
        summary_tbl = mc.compute_tab1_summary_table(base)
        st.dataframe(summary_tbl, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 2
# -----------------------------------------------------------------------------
with tab2:
    st.subheader("Data Integrity and Cohort Definition Checks")
    st.caption("This page verifies whether the dashboard inputs remain aligned with the cleaned NMAT_Exodus pipeline (enriched by Pipeline 4), including cohort construction, raw-score consistency, and institutional classification fields.")
    df = F["all"]
    best_filtered = F["best"]
    best_observable_filtered = F["bestobservable"]
    plepasser_filtered = F["plepasser"]
    plepasserbest_filtered = F["plepasserbest"]

    _t2_kpis = mc.compute_tab2_kpis(df, best_filtered, best_observable_filtered)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("All NMAT rows", f"{_t2_kpis['n_all']:,}", help="All cleaned NMAT_Exodus rows that are loaded into the app.")
    col2.metric("Best-record rows", f"{_t2_kpis['n_best']:,}", help="Number of best-record rows in the pipeline (one per examinee after best-record flag applied).")
    col3.metric("Rows with TRUE raw scores", f"{_t2_kpis['n_true_raw']:,}", help="Rows where HasTRUErawScores == True.")
    col4.metric("Observable best-record rows (IS_BEST_OBSERVABLE_RECORD)", f"{_t2_kpis['n_best_observable']:,}", help="One row per person: their best NMAT attempt among sittings with Year <= 2014. This is the only correct person-level PLE-linked cohort -- it is NOT the same as 'best-record & Year<=2014' (see caption below).")

    st.subheader("Table 2. Analysis cohorts used in the dashboard")
    st.caption(
        "Each row defines one analytic subset used in later pages. Counts should be interpreted as rows, "
        "not necessarily unique persons, unless explicitly stated otherwise. 'Best-record rows in the "
        "observable PLE window' uses IS_BEST_OBSERVABLE_RECORD (the person's best attempt *within* "
        "Year<=2014), not the person's overall best attempt filtered to Year<=2014 -- the latter drops "
        "people whose single best NMAT sitting happened after 2014 even though they also sat, and could "
        "have been linked, within the observable window."
    )
    cohort_tbl = mc.compute_cohort_table(F)
    st.dataframe(cohort_tbl, use_container_width=True)

    st.subheader("Table 3. TRUE raw-score validation checks")
    st.caption("These checks confirm whether TRUE total raw score is internally consistent with its Part I and Part II components, and whether the stored-vs-derived mismatch flag remains zero.")
    _rv = mc.compute_raw_validation_checks(df)
    raw_tbl = pd.DataFrame({
        "Validation check": [
            "Rows with complete Total + Part I + Part II",
            "Formula mismatches: Total != Part I + Part II",
            "Rows with a stored raw total (StoredRawTotal notna)",
            "Stored-vs-derived mismatch flag count (of rows with a stored total)",
        ],
        "Count of rows": [
            _rv["eq_mask_n"],
            _rv["mismatch_n"],
            _rv["stored_nonnull_n"],
            _rv["mismatch_flag_n"],
        ],
    })
    st.dataframe(raw_tbl, use_container_width=True)
    _mismatch_rate_pct = _rv["mismatch_rate_pct"]
    st.metric("Stored-vs-derived mismatch rate (of rows with a stored total)", f"{_mismatch_rate_pct:.2f}%" if pd.notna(_mismatch_rate_pct) else "N/A")
    st.caption("Reference: 56,065 of the 99,316 rows carrying a stored total disagree with the recalculated TotalRawScoreTRUE (56.45% of that denominator, 31.33% of all rows) in the unfiltered dataset. Never state this as \"42.2%\" -- that figure divided the mismatch count by the wrong (unique-examinee) denominator.")

    st.subheader("Table 4. UNDERGRAD_UNIVERSITY to UNDERGRAD_UNI_TYPE / UNDERGRAD_UNI_LOCATION pairing audit")
    st.caption("Checks whether each standardized undergraduate-university name maps consistently to one university type and one location in the cleaned pipeline. This describes the examinee's undergraduate (pre-NMAT) institution, not a medical school.")
    university_pairing, pairing_conflicts = mc.compute_university_pairing_audit(df)
    if university_pairing is not None:
        c3, c4 = st.columns(2)
        c3.metric("Universities checked", f"{university_pairing.shape[0]:,}")
        c4.metric("University pairing conflicts", f"{pairing_conflicts.shape[0]:,}")
        with st.expander("University-level pairing conflicts (detail)", expanded=False):
            st.caption("This table checks whether each standardized university name maps consistently to one university type and one location in the cleaned pipeline.")
            st.dataframe(pairing_conflicts.head(200), use_container_width=True)
    else:
        st.info("UNDERGRAD_UNIVERSITY is not available in the dataset.")

    st.subheader("Core distributions")
    st.caption("Values are row counts under the current filters.")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Table 6. Distribution of university type in the filtered rows**")
        st.dataframe(mc.compute_composition(df, "UNDERGRAD_UNI_TYPE", dropna=False), use_container_width=True)
    with c2:
        st.markdown("**Table 7. Distribution of course group in the filtered rows**")
        st.dataframe(mc.compute_composition(df, "UNDERGRAD_COURSE_GROUP", dropna=False), use_container_width=True)
    with c3:
        st.markdown("**Table 8. Distribution of PLE status label, observable cohort only**")
        st.caption(
            "Restricted to IS_OBSERVABLE_COHORT (Year <= 2014). Rows from later years are structurally "
            "too recent to have a confirmed PLE outcome yet, so including them here would inflate the "
            "apparent 'no match' share as a recency artifact rather than a real linkage gap."
        )
        _status_counts, _non_obs_n, _non_obs_pct = mc.compute_ple_status_observable(df)
        st.dataframe(_status_counts, use_container_width=True)
        st.caption(f"{_non_obs_n:,} of {len(df):,} filtered rows ({_non_obs_pct:.1f}%) are Year > 2014 and excluded from this table for that reason.")

    _outcome_tbl, _yr_uncertain_n = mc.compute_ple_match_outcome(df)
    if _outcome_tbl is not None:
        st.subheader("Table 9. PLE match-outcome breakdown")
        st.caption(
            "IS_PLE_PASSER (the sole authoritative passer flag) is True only for PLE_MATCH_OUTCOME == "
            "'accepted'. This table shows why the rest were not counted, instead of silently collapsing "
            "them into one 'no match' figure: 'no_match' means no name/appno candidate was found at all; "
            "'rejected_ambiguous_person' means a candidate was found but the person-key match could not "
            "be disambiguated with confidence; a small residual 'rejected' bucket covers other rejections."
        )
        st.dataframe(_outcome_tbl, use_container_width=True, hide_index=True)
        if _yr_uncertain_n is not None:
            st.caption(f"Additionally, {_yr_uncertain_n:,} confirmed passers have PLE_YEAR_UNCERTAIN == True: they are counted in IS_PLE_PASSER, but the specific year they passed could not be disambiguated (affects PLE_YEAR_GAP-based analyses, not the passer count itself).")

# -----------------------------------------------------------------------------
# TAB 3
# -----------------------------------------------------------------------------
with tab3:
    st.subheader("Performance Trends and Year-to-Year Stability")
    st.caption("This page summarizes how NMAT score levels and score distributions changed across test years using the filtered best-record trend cohort.")
    df = F["besttrend"]
    summary = mc.get_yearly_summary(df)

    st.markdown("**Figure 4. Annual score trends and examinee volume**")
    st.caption(
        "Score panels use the best-record cohort (one attempt per person). The volume panel shows both "
        "best-record examinees and total sittings (all attempts) side by side, since best-record volume "
        "alone under-represents mid-decade years (60-69% of true sittings) and over-represents 2017 "
        "(92.6%) -- a non-uniform pattern that can misread as a volume dip/surge if shown alone. "
        "The score/boxplot panels below inherit the same best-record-per-year composition caveat."
    )
    _sittings_by_year_t3 = mc.compute_sittings_by_year(F["trend"])
    st.plotly_chart(make_trends_figure(summary, _sittings_by_year_t3), use_container_width=True, key="fig_t3_trends")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**This boxplot shows the yearly spread, median, and upper/lower quartiles for TRUE raw scores**")
        st.plotly_chart(make_box_by_year(df, "TotalRawScoreTRUE", "Total Raw Score by Year"), use_container_width=True, key="fig_t3_box_raw")
    with c2:
        st.markdown("**This boxplot shows the yearly spread of percentile rank**")
        st.plotly_chart(make_box_by_year(df, "NMS_PER_num", "Percentile Rank by Year"), use_container_width=True, key="fig_t3_box_pct")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**This boxplot shows the yearly spread of Part I raw score**")
        st.plotly_chart(make_box_by_year(df, "PartIRawScoreTRUE", "Part I Raw Score by Year"), use_container_width=True, key="fig_t3_box_p1")
    with c2:
        st.markdown("**This boxplot shows the yearly spread of Part II raw score**")
        st.plotly_chart(make_box_by_year(df, "PartIIRawScoreTRUE", "Part II Raw Score by Year"), use_container_width=True, key="fig_t3_box_p2")

    st.markdown("**Table 9. Kruskal-Wallis tests for year-to-year score differences**")
    st.caption("This table tests whether score distributions differ significantly across NMAT years. Eta-squared is included as an effect-size indicator, so statistical significance is not mistaken for practical importance.")
    ktable = mc.kruskal_table(
        df,
        "Year",
        {
            "TotalRawScoreTRUE": "Total Raw Score",
            "PartIRawScoreTRUE": "Part I Raw Score",
            "PartIIRawScoreTRUE": "Part II Raw Score",
            "NMS_PER_num": "Percentile Rank",
            "NMS_GPS": "GPS Standard Score",
        },
    )
    st.dataframe(ktable, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 4
# -----------------------------------------------------------------------------
with tab4:
    st.subheader("Bin Distribution by Year and Examinee Background")
    st.caption("This page shows how score bins are distributed across NMAT years, university type, and pre-med course background in the best-record trend cohort.")
    df = F["besttrend"]
    dfuni = F["uni"]

    dec_tab1, dec_tab2, dec_tab3 = st.tabs(["By year", "University type", "Course group"])

    with dec_tab1:
        st.caption("Use this tab to see whether later cohorts became more concentrated in higher bins, lower bins, or the middle of the distribution.")
        count, pct = mc.pct_table(df, "Year", "PercentileBin", BIN_ORDER)
        pct.index.name = "Year"
        # Transpose for deciles on y-axis, years on x-axis
        pct_transposed = pct.T
        pct_transposed.index.name = "Bin"
        # Reverse decile order for D10-D1 descending
        decile_order_desc = BIN_ORDER[::-1]
        pct_transposed = pct_transposed.reindex(decile_order_desc)
        st.markdown("**Figure 5. Percentile-bin heatmap by NMAT year**")
        st.caption("Heatmap values are within-year percentages; B8-B10 represents the upper segment and B1-B3 represents the lower segment.")
        st.plotly_chart(make_heatmap(pct_transposed, "Bin Distribution by Year", "Bin", "Year", "YlOrRd"), use_container_width=True, key="fig_t4_heatmap_year")

        # Add deciles distribution table by counts with D10 to D1 rows and Year columns
        st.markdown("**Table 10. Count of examinees in each bin by NMAT year**")
        st.caption("Counts are rows in the filtered best-record trend cohort. Rows show bins (B10->B1) and columns show years.")
        count_transposed = count.T.reindex(BIN_ORDER[::-1])
        count_transposed.index.name = "PercentileBin"
        st.dataframe(count_transposed.reset_index(), use_container_width=True)

        st.markdown("**Figure 6. Bin composition within each NMAT year**")
        st.caption("This figure shows within-year percentile-bin composition (percent). B8-B10 is the upper segment and B1-B3 the lower segment.")
        st.plotly_chart(make_stacked_pct_bar(pct, "Bin Composition by Year", "Year", "Percent", BIN_COLORS), use_container_width=True, key="fig_t4_stacked_year")

        _topbot_year = mc.compute_top_bottom_by(pct)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=_topbot_year["Year"], y=_topbot_year["Top B8-B10 (%)"], mode="lines+markers", name="Top B8-B10", line=dict(color="#2e7d32", width=3)))
        fig.add_trace(go.Scatter(x=_topbot_year["Year"], y=_topbot_year["Bottom B1-B3 (%)"], mode="lines+markers", name="Bottom B1-B3", line=dict(color="#c62828", width=3)))
        fig.update_layout(title="Top vs Bottom Bin Share by Year", xaxis_title="Year", yaxis_title="Percent", height=420)
        st.markdown("**Figure 7. Top-bin versus bottom-bin share by NMAT year**")
        st.caption("This chart compares combined B8-B10 (top) versus B1-B3 (bottom) shares by year.")
        st.plotly_chart(fig, use_container_width=True, key="fig_t4_topbot")

    with dec_tab2:
        st.caption("Insight: Compare which university types are overrepresented in higher bins.")
        _, uni_pct = mc.pct_table(dfuni, "UNDERGRAD_UNI_TYPE", "PercentileBin", BIN_ORDER)
        uni_pct.index.name = "UNDERGRAD_UNI_TYPE"
        st.markdown("**Figure 8. Percentile-bin distribution by university type**")
        st.caption("Heatmap values are within-type percentages.")
        st.plotly_chart(make_heatmap(uni_pct, "Bin Distribution by University Type", "Bin", "University type"), use_container_width=True, key="fig_t4_heatmap_uni")

        top_uni = uni_pct[["B8", "B9", "B10"]].sum(axis=1)
        st.markdown("**Figure 9. Share of examinees in B8-B10 by university type**")
        st.caption("The bar chart highlights representation in the top three bins (B8-B10) by university type.")
        st.plotly_chart(make_top_share_bar(top_uni, "Top Bin Share by University Type", "Percent in B8-B10", "University type", PALETTE_UNI), use_container_width=True, key="fig_t4_top_uni")

        contingency, expected, chi_summary = mc.chi_square_unitype_bin(dfuni.dropna(subset=["UNDERGRAD_UNI_TYPE", "PercentileBin"]))
        st.markdown("**Table 11. Chi-square test for association between university type and percentile bin**")
        st.caption("The chi-square table tests whether bin composition differs by university type beyond random variation.")
        st.dataframe(chi_summary, use_container_width=True)

        st.divider()
        st.subheader("Bin distribution per year by university type")
        st.caption("Each facet shows one university type. Bars are stacked by percentile bin so you can see how Foreign, Public, and Private examinees are distributed each year.")

        _yr_uni_dec = mc.compute_bin_by_year_and_unitype(dfuni)

        if _yr_uni_dec.empty:
            st.info("No data available for this chart under the current filters.")
        else:
            _yr_uni_dec = _yr_uni_dec.copy()
            _yr_uni_dec["Year"] = _yr_uni_dec["Year"].astype(str)

            _fig_yr_uni = px.bar(
                _yr_uni_dec,
                x="Year",
                y="n",
                color="PercentileBin",
                facet_col="UNDERGRAD_UNI_TYPE",
                barmode="stack",
                title="Examinees per bin by year and university type",
                labels={"n": "Examinees", "Year": "Year", "PercentileBin": "Bin"},
                color_discrete_map=BIN_COLORS,
                category_orders={"PercentileBin": BIN_ORDER},
            )
            _fig_yr_uni.update_layout(height=520)
            _fig_yr_uni.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
            st.markdown("**Figure: Bin composition per year -- Foreign vs Public vs Private**")
            st.caption("Counts are filtered best-record trend examinees. Use this chart to compare year-to-year shifts within each university type.")
            st.plotly_chart(_fig_yr_uni, use_container_width=True, key="fig_t4_yr_uni_bin_facet")

        st.divider()
        st.subheader("Record-level listings by university type")
        st.caption("Browse all examinees under each university type. Sorted by year (newest first) then percentile rank (highest first).")

        _rec_tab_foreign, _rec_tab_public, _rec_tab_private = st.tabs(
            ["🌐 Foreign", "🏛️ Public", "🏫 Private"]
        )
        _rec_display_cols = [
            c for c in [
                "PERSON_KEY", "APPNO_CLEAN", "UNDERGRAD_UNIVERSITY", "UNDERGRAD_UNI_LOCATION",
                "Year", "UNDERGRAD_COURSE_GROUP", "PercentileBin", "NMS_PER_num", "TotalRawScoreTRUE",
            ]
            if c in dfuni.columns
        ]
        _rec_col_sql = ", ".join([f'"{c}"' for c in _rec_display_cols])
        _rec_con = duckdb.connect()
        _rec_con.register("_rec_src", dfuni)

        for _rtab, _utype in [
            (_rec_tab_foreign, "Foreign"),
            (_rec_tab_public, "Public"),
            (_rec_tab_private, "Private"),
        ]:
            with _rtab:
                _recs = _rec_con.execute(f"""
                    SELECT {_rec_col_sql}
                    FROM _rec_src
                    WHERE UNDERGRAD_UNI_TYPE = '{_utype}'
                    ORDER BY CAST(Year AS INTEGER) DESC NULLS LAST,
                             NMS_PER_num DESC NULLS LAST
                """).df()
                if _recs.empty:
                    st.info(f"No {_utype} university examinees found under the current filters.")
                else:
                    st.caption(
                        f"{len(_recs):,} {_utype} examinee records. "
                        "Sorted by year (newest first) and percentile rank (highest first)."
                    )
                    st.dataframe(_recs, use_container_width=True, hide_index=True)

        _rec_con.close()

        st.divider()
        st.subheader("No PLE match -- record listings by university type")
        st.caption(
            "Records shown here belong to the observable best-record cohort (Year <= 2014) "
            "and have **no confirmed PLE match** (IS_PLE_PASSER != True). "
            "The observable cohort is used because examinees from later years have not had enough "
            "time to plausibly appear in the PLE passer source list. Absence from that list is not "
            "evidence of failure -- it can also mean the exam hasn't been sat, or the match was missed."
        )

        _nople_df = F["uniobservable"]

        _nople_tab_foreign, _nople_tab_public, _nople_tab_private = st.tabs(
            ["🌐 Foreign", "🏛️ Public", "🏫 Private"]
        )
        _nople_display_cols = [
            c for c in [
                "PERSON_KEY", "APPNO_CLEAN", "UNDERGRAD_UNIVERSITY", "UNDERGRAD_UNI_LOCATION",
                "Year", "UNDERGRAD_COURSE_GROUP", "PercentileBin", "NMS_PER_num",
                "TotalRawScoreTRUE", "PLE_STATUS_LABEL",
            ]
            if c in _nople_df.columns
        ]
        _nople_col_sql = ", ".join([f'"{c}"' for c in _nople_display_cols])
        _nople_con = duckdb.connect()
        _nople_con.register("_nople_src", _nople_df)

        for _ntab, _utype in [
            (_nople_tab_foreign, "Foreign"),
            (_nople_tab_public, "Public"),
            (_nople_tab_private, "Private"),
        ]:
            with _ntab:
                _nople_recs = _nople_con.execute(f"""
                    SELECT {_nople_col_sql}
                    FROM _nople_src
                    WHERE UNDERGRAD_UNI_TYPE = '{_utype}'
                      AND PLE_STATUS_LABEL = 'No confirmed PLE match'
                    ORDER BY CAST(Year AS INTEGER) DESC NULLS LAST,
                             NMS_PER_num DESC NULLS LAST
                """).df()
                if _nople_recs.empty:
                    st.info(
                        f"No {_utype} university examinees without a PLE match found "
                        "under the current filters and observable cohort window."
                    )
                else:
                    st.caption(
                        f"{len(_nople_recs):,} {_utype} examinee records with no confirmed PLE match. "
                        "Sorted by year (newest first) and percentile rank (highest first)."
                    )
                    st.dataframe(_nople_recs, use_container_width=True, hide_index=True)

        _nople_con.close()

        # -- Citizenship profile -------------------------------------
        st.divider()
        st.subheader("Citizenship profile for no-PLE-match examinees")
        st.caption(
            "Citizenship labels (CITIZENSHIP_FINAL, FOREIGNER_STATUS) are baked into "
            "NMAT_Exodus.parquet by Pipeline 4 using a 3-tier hierarchy: "
            "REAL_FOREIGNERS.csv ground truth -> pseudo-citizenship inference -> Filipino default."
        )

        if "CITIZENSHIP_FINAL" not in _uniobs_pc.columns:
            st.error(
                "CITIZENSHIP_FINAL column not found. "
                "The dashboard may be loading from NMAT_Ultima.parquet instead of NMAT_Exodus.parquet. "
                "Run Pipeline 4 (4_Citizenship_Integration.py) or clear the Streamlit cache "
                "(Settings > Clear Cache) and reload."
            )
        else:
            _cp = mc.compute_citizenship_profile(_uniobs_pc)

            if _cp.get("empty"):
                st.info("No profiled no-PLE-match records match the current filters.")
            else:
                _pc_base = _cp["records"]
                _pc_foreigners = _cp["kpis"]["n_foreigners"]
                _pc_filipinos = _cp["kpis"]["n_filipinos"]
                _pc_distinct = _cp["kpis"]["n_distinct"]

                _pm1, _pm2, _pm3, _pm4 = st.columns(4)
                _pm1.metric("Profiled no-PLE-match records", f"{_cp['kpis']['n_profiled']:,}")
                _pm2.metric("Foreigners", f"{_pc_foreigners:,}")
                _pm3.metric("Filipinos", f"{_pc_filipinos:,}")
                _pm4.metric("Distinct citizenship labels", f"{_pc_distinct:,}")

                # -- citizenship counts (reused in multiple charts) ----------
                _pc_counts = _cp["counts"]

                # Pie charts side-by-side -------------------------------------
                _pp1, _pp2 = st.columns(2)

                with _pp1:
                    st.markdown("**Citizenship composition**")
                    _fig_pc_pie = px.pie(
                        _pc_counts,
                        names="CITIZENSHIP_FINAL",
                        values="n",
                        title="Citizenship composition",
                    )
                    st.plotly_chart(_fig_pc_pie, use_container_width=True, key="fig_pc_pie_comp")

                with _pp2:
                    st.markdown("**Foreigners vs Filipinos**")
                    _pc_fvf_counts = pd.DataFrame({
                        "group": ["Foreigner", "Filipino"],
                        "n": [_pc_foreigners, _pc_filipinos],
                    })
                    _fig_pc_fvf = px.pie(
                        _pc_fvf_counts,
                        names="group",
                        values="n",
                        title="Foreigners vs Filipinos in profiled no-PLE-match set",
                        color_discrete_map={
                            "Foreigner": PALETTE_UNI.get("Foreign", "#9467bd"),
                            "Filipino": PALETTE_UNI.get("Public", "#1f77b4"),
                        },
                    )
                    st.plotly_chart(_fig_pc_fvf, use_container_width=True, key="fig_pc_pie_fvf")

                # Top-15 horizontal bar ---------------------------------------
                st.markdown("**Top citizenship groups by count**")
                _top15 = _pc_counts.head(15).sort_values("n")
                _fig_pc_top15 = go.Figure(go.Bar(
                    x=_top15["n"],
                    y=_top15["CITIZENSHIP_FINAL"],
                    orientation="h",
                    text=_top15["n"].astype(str),
                    textposition="outside",
                    marker_color=PALETTE_UNI.get("Foreign", "#9467bd"),
                    hovertemplate="Citizenship: %{y}<br>Count: %{x}<extra></extra>",
                ))
                _fig_pc_top15.update_layout(
                    title="Top 15 citizenship groups",
                    xaxis_title="Examinees",
                    yaxis_title="",
                    height=max(380, len(_top15) * 30),
                )
                st.plotly_chart(_fig_pc_top15, use_container_width=True, key="fig_pc_top15_bar")

                # Stacked % bar: decile composition by citizenship ------------
                st.markdown("**Bin composition by citizenship (top 15 groups)**")
                _pc_top_grps = _cp["top15"]
                _pc_dec_pct = _cp["bin_dist_top15"]
                if _pc_dec_pct is not None:
                    _fig_pc_dec = make_stacked_pct_bar(
                        _pc_dec_pct,
                        "Bin composition by citizenship",
                        "Citizenship",
                        "Percent",
                        BIN_COLORS,
                    )
                    _fig_pc_dec.update_layout(height=520)
                    st.plotly_chart(_fig_pc_dec, use_container_width=True, key="fig_pc_bin_stacked")

                    st.markdown("**Full percentile-bin heatmap by citizenship (all bins B1-B10)**")
                    st.caption(
                        "Each row is one citizenship group; each column is one percentile bin. "
                        "Values are row percentages -- read across a row to see where that group clusters "
                        "across the full score distribution, from the bottom (B1) to the top (B10). "
                        "Red tones flag higher concentration in that bin."
                    )
                    _fig_pc_hm_all = make_heatmap(
                        _pc_dec_pct,
                        "Full bin profile by citizenship (row %)",
                        "Percentile bin",
                        "Citizenship",
                        "YlOrRd",
                    )
                    _fig_pc_hm_all.update_layout(height=max(450, len(_pc_top_grps) * 32 + 120))
                    st.plotly_chart(_fig_pc_hm_all, use_container_width=True, key="fig_pc_bin_heatmap_all")

                # Top-decile share bar  +  percentile box plot ----------------
                _pb1, _pb2 = st.columns(2)

                with _pb1:
                    st.markdown("**Top-bin share (B8-B10) by citizenship**")
                    if "PercentileBin" in _pc_base.columns:
                        _pc_top_dec = _cp["topbin_share"]
                        if _pc_top_dec is not None and not _pc_top_dec.empty:
                            _fig_pc_topdec = go.Figure(go.Bar(
                                x=_pc_top_dec["top_dec_pct"],
                                y=_pc_top_dec["CITIZENSHIP_FINAL"],
                                orientation="h",
                                text=[f"{v:.1f}%" for v in _pc_top_dec["top_dec_pct"]],
                                textposition="outside",
                                marker_color=BIN_COLORS["B10"],
                                hovertemplate="Citizenship: %{y}<br>B8-B10 share: %{x:.1f}%<extra></extra>",
                            ))
                            _fig_pc_topdec.update_layout(
                                title="Top-bin share (B8-B10)",
                                xaxis_title="% in B8-B10",
                                yaxis_title="",
                                height=max(360, len(_pc_top_dec) * 30),
                            )
                            st.plotly_chart(_fig_pc_topdec, use_container_width=True, key="fig_pc_topbin_bar")

                with _pb2:
                    st.markdown("**Percentile rank by citizenship (n >= 5)**")
                    if "NMS_PER_num" in _pc_base.columns:
                        _pc_big = _pc_base.groupby("CITIZENSHIP_FINAL", observed=True).filter(
                            lambda x: len(x) >= 5
                        )
                        if not _pc_big.empty:
                            _fig_pc_box_pct = px.box(
                                _pc_big,
                                x="CITIZENSHIP_FINAL",
                                y="NMS_PER_num",
                                points=False,
                                title="Percentile rank by citizenship (n >= 5)",
                                labels={"NMS_PER_num": "Percentile rank", "CITIZENSHIP_FINAL": ""},
                            )
                            _fig_pc_box_pct.update_layout(height=430)
                            st.plotly_chart(_fig_pc_box_pct, use_container_width=True, key="fig_pc_box_pct")

                # TRUE raw score box plot --------------------------------------
                st.markdown("**TRUE raw score by citizenship (n >= 5)**")
                if "TotalRawScoreTRUE" in _pc_base.columns:
                    _pc_big_raw = _pc_base.groupby("CITIZENSHIP_FINAL", observed=True).filter(
                        lambda x: len(x) >= 5
                    )
                    if not _pc_big_raw.empty:
                        _fig_pc_box_raw = px.box(
                            _pc_big_raw,
                            x="CITIZENSHIP_FINAL",
                            y="TotalRawScoreTRUE",
                            points=False,
                            title="TRUE raw score by citizenship (n >= 5)",
                            labels={"TotalRawScoreTRUE": "Total raw score", "CITIZENSHIP_FINAL": ""},
                        )
                        _fig_pc_box_raw.update_layout(height=430)
                        st.plotly_chart(_fig_pc_box_raw, use_container_width=True, key="fig_pc_box_raw")

                # -- Summary tables --------------------------------------------
                st.markdown("**Summary by citizenship**")
                st.dataframe(_cp["summary"], use_container_width=True, hide_index=True)

                _pt1, _pt2 = st.columns(2)
                with _pt1:
                    st.markdown("**Summary by citizenship and university type**")
                    if _cp["by_unitype"] is not None:
                        st.dataframe(_cp["by_unitype"], use_container_width=True, hide_index=True)

                with _pt2:
                    st.markdown("**Summary by citizenship and course group**")
                    if _cp["by_course"] is not None:
                        st.dataframe(_cp["by_course"], use_container_width=True, hide_index=True)

                st.markdown("**Year distribution by citizenship**")
                if _cp["by_year"] is not None:
                    st.dataframe(_cp["by_year"], use_container_width=True, hide_index=True)

                st.markdown("**Matched no-PLE-match records with citizenship**")
                _pc_rec_cols = [c for c in [
                    "CITIZENSHIP_FINAL", "FOREIGNER_STATUS",
                    "PERSON_KEY", "APPNO_CLEAN", "UNDERGRAD_UNIVERSITY", "UNDERGRAD_UNI_LOCATION", "UNDERGRAD_UNI_TYPE",
                    "Year", "UNDERGRAD_COURSE_GROUP", "PercentileBin", "NMS_PER_num",
                    "TotalRawScoreTRUE", "PLE_STATUS_LABEL",
                ] if c in _pc_base.columns]
                _pc_rec_df = (
                    _pc_base[_pc_rec_cols]
                    .sort_values(
                        ["CITIZENSHIP_FINAL", "Year", "NMS_PER_num"],
                        ascending=[True, False, False],
                    )
                )
                st.caption(
                    f"{len(_pc_rec_df):,} matched records. "
                    "Sorted by citizenship (A->Z), year (newest first), "
                    "percentile rank (highest first)."
                )
                st.dataframe(_pc_rec_df, use_container_width=True, hide_index=True)

                # -- Comparative analysis: foreigners vs Filipino students ------
                st.divider()
                st.subheader("Comparative analysis: foreigners vs Filipino students")
                st.caption(
                    "Compares (1) actual foreigners (non-Filipino, identified via the profiling CSV), "
                    "(2) Filipinos whose undergraduate degree was from a foreign/international school, "
                    "(3) all students whose undergraduate degree was from a public school, and "
                    "(4) all students whose undergraduate degree was from a private school. "
                    "Groups 1 and 2 come from the profiling-matched observable university subset. "
                    "Groups 3 and 4 use all observable best-record examinees at those institution types. "
                    "All groups reflect the current sidebar filters. "
                    "**UNDERGRAD_UNI_TYPE / UNDERGRAD_UNIVERSITY record the examinee's undergraduate "
                    "(pre-NMAT) school, not the medical school they later attended between the NMAT and "
                    "the licensure exam** -- no medical-school identifier exists in this dataset, so the "
                    "linkage-rate differences below cannot be attributed to medical-school quality."
                )

                _cmp = mc.compute_comparative_groups(_uniobs_pc, F["bestobservable"])

                if _cmp is None:
                    st.info("No comparative data available under the current filters. Ensure Public and/or Private university types are included.")
                else:
                    _cmp_df = _cmp["cmp_df"]

                    # Summary table -------------------------------------------
                    st.markdown("**Summary: key score indicators by comparison group**")
                    st.caption(
                        "\"PLE linkage rate %\" is the share of each group found in the PLE passer source "
                        "list (IS_PLE_PASSER) -- it is a LINKAGE rate, not a licensure pass rate, since the "
                        "source contains passers only and absence does not mean failure. "
                        "Verified-foreigner linkage in the observable cohort is low (~2.5%) but not "
                        "exactly 0%, mainly because foreign nationals rarely sit Philippine licensure exams."
                    )
                    _cmp_agg = _cmp["agg"]
                    st.dataframe(_cmp_agg, use_container_width=True, hide_index=True)

                    # Boxplots -------------------------------------------------
                    _bcol1, _bcol2 = st.columns(2)
                    with _bcol1:
                        st.markdown("**Percentile rank distribution by group**")
                        _cmp_pct_plot = _cmp_df.dropna(subset=["NMS_PER_num"]).copy()
                        if not _cmp_pct_plot.empty:
                            _fig_cmp_pct = px.box(
                                _cmp_pct_plot,
                                x="_cmp_group",
                                y="NMS_PER_num",
                                color="_cmp_group",
                                points=False,
                                title="Percentile rank: foreigners vs Filipinos",
                                labels={"NMS_PER_num": "Percentile rank", "_cmp_group": ""},
                            )
                            _fig_cmp_pct.update_layout(height=460, showlegend=False, xaxis_tickangle=-20)
                            st.plotly_chart(_fig_cmp_pct, use_container_width=True, key="fig_cmp_pct_box")

                    with _bcol2:
                        st.markdown("**TRUE raw score distribution by group**")
                        _cmp_raw_plot = _cmp_df.dropna(subset=["TotalRawScoreTRUE"]).copy()
                        if not _cmp_raw_plot.empty:
                            _fig_cmp_raw = px.box(
                                _cmp_raw_plot,
                                x="_cmp_group",
                                y="TotalRawScoreTRUE",
                                color="_cmp_group",
                                points=False,
                                title="TRUE raw score: foreigners vs Filipinos",
                                labels={"TotalRawScoreTRUE": "Total raw score", "_cmp_group": ""},
                            )
                            _fig_cmp_raw.update_layout(height=460, showlegend=False, xaxis_tickangle=-20)
                            st.plotly_chart(_fig_cmp_raw, use_container_width=True, key="fig_cmp_raw_box")

                    # Full bin heatmap -----------------------------------------
                    _cmp_bin_pct = _cmp["bin_pct"]
                    if _cmp_bin_pct is not None:
                        st.markdown("**Full bin heatmap: foreigners vs Filipino groups (all bins B1-B10)**")
                        st.caption(
                            "Row percentages show the full distribution of each group across all ten "
                            "percentile bins. Compare rows to see which groups skew high (B8-B10) "
                            "or low (B1-B3). This is a magnitude (0-100%), not a value judgment, so a "
                            "sequential (dark = more) scale is used rather than a red-green diverging one."
                        )
                        _fig_cmp_hm = make_heatmap(
                            _cmp_bin_pct,
                            "Bin distribution by comparison group (row %)",
                            "Percentile bin",
                            "Group",
                            "YlOrRd",
                        )
                        _fig_cmp_hm.update_layout(height=400)
                        st.plotly_chart(_fig_cmp_hm, use_container_width=True, key="fig_cmp_all_bins_hm")

                        # Stacked bar
                        st.markdown("**Bin composition by group (stacked %)**")
                        _cmp_bin_pct_labeled = _cmp_bin_pct.copy()
                        _cmp_bin_pct_labeled.index.name = "Group"
                        _fig_cmp_stk = make_stacked_pct_bar(
                            _cmp_bin_pct_labeled,
                            "Bin composition: foreigners vs Filipinos",
                            "Group",
                            "Percent",
                            BIN_COLORS,
                        )
                        _fig_cmp_stk.update_layout(height=480)
                        st.plotly_chart(_fig_cmp_stk, use_container_width=True, key="fig_cmp_stk_bar")

                        # Top vs bottom grouped bar
                        st.markdown("**Top-bin (B8-B10) vs bottom-bin (B1-B3) share by group**")
                        _cmp_topbot = _cmp["topbot"]
                        _cmp_topbot_long = _cmp_topbot.melt(
                            id_vars="Group", var_name="Segment", value_name="Percent"
                        )
                        _fig_cmp_topbot = px.bar(
                            _cmp_topbot_long,
                            x="Group",
                            y="Percent",
                            color="Segment",
                            barmode="group",
                            title="Top vs bottom bin share by group",
                            color_discrete_map={
                                "Top B8-B10 (%)": "#2e7d32",
                                "Bottom B1-B3 (%)": "#c62828",
                            },
                            labels={"Group": "", "Percent": "Percent", "Segment": ""},
                        )
                        _fig_cmp_topbot.update_layout(height=420, xaxis_tickangle=-15)
                        st.plotly_chart(_fig_cmp_topbot, use_container_width=True, key="fig_cmp_topbot_grouped")

                        st.markdown("**Bin distribution table: all groups (row %)**")
                        st.dataframe(
                            _cmp_bin_pct.reset_index().rename(columns={"_cmp_group": "Group"}),
                            use_container_width=True,
                            hide_index=True,
                        )

    with dec_tab3:
        st.caption("Insight: Compare bin profiles across pre-med backgrounds.")
        _, course_pct = mc.pct_table(df, "UNDERGRAD_COURSE_GROUP", "PercentileBin", BIN_ORDER)
        course_pct.index.name = "UNDERGRAD_COURSE_GROUP"
        st.markdown("**Figure 10. Percentile-bin distribution by course group**")
        st.caption("Heatmap values are within-course-group percentages.")
        st.plotly_chart(make_heatmap(course_pct, "Bin Distribution by Course Group", "Bin", "Course group", "OrRd"), use_container_width=True, key="fig_t4_heatmap_course")

        top_course = course_pct[["B8", "B9", "B10"]].sum(axis=1)
        st.markdown("**Figure 11. Share of examinees in B8-B10 by course group**")
        st.caption("The bar chart highlights representation in the top three bins by course group.")
        st.plotly_chart(make_top_share_bar(top_course, "Top Bin Share by Course Group", "Percent in B8-B10", "Course group", PALETTE_COURSE), use_container_width=True, key="fig_t4_top_course")

        course_desc = mc.compute_percentile_summary_by(df, "UNDERGRAD_COURSE_GROUP")
        st.markdown("**Table 12. Percentile summary by course group**")
        st.caption("Values show sample size, median percentile rank, and interquartile range for each course group.")
        st.dataframe(course_desc, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 5
# -----------------------------------------------------------------------------
with tab5:
    st.subheader("Institutional Profile: Undergraduate University Type and Location")
    st.caption("This page profiles examinees by their undergraduate (pre-NMAT) institution -- Public, Private, and Foreign university types, with location shown as Local or International where available. No medical-school identifier exists in this dataset; nothing on this page should be read as a statement about medical-school quality.")

    base = F["uni"].copy()
    # Two bases: uni_type_base only requires undergrad type/location (used by elements that don't
    # touch PercentileBin); uni_base additionally requires a non-null PercentileBin (used only by
    # bin-dependent charts/tables). Splitting these avoids silently dropping ~2.3% of applicants
    # from tables (e.g. university listings) that have nothing to do with percentile bins.
    uni_type_base = base.dropna(subset=["UNDERGRAD_UNI_TYPE", "UNDERGRAD_UNI_LOCATION"]).copy()
    uni_base = uni_type_base.dropna(subset=["PercentileBin"]).copy()

    if uni_type_base.empty:
        st.info("No university-type records are available under the current filters.")
    else:
        st.caption("Insight: This page follows the institutional comparison subset (Public, Private, Foreign) from the analysis pipeline. This describes the examinee's undergraduate (pre-NMAT) institution, not a medical school.")
        type_loc = mc.compute_unitype_location_mix(uni_type_base)
        st.markdown("**Table 13. Institution type by location mix**")
        st.caption(f"Values show counts and percentages of {len(uni_type_base):,} examinees within each institutional classification (does not require a percentile bin).")
        st.dataframe(type_loc, use_container_width=True)

        st.markdown("**Table 14. Institution type by location matrix**")
        st.caption("Row percentages describe the location mix within each university type. Column percentages show composition within each location.")
        inst_count, inst_pct_row, inst_pct_col = mc.compute_unitype_location_crosstab(uni_type_base)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Counts (with totals)**")
            st.dataframe(inst_count, use_container_width=True)
            st.markdown("**Row percentages: within UNDERGRAD_UNI_TYPE**")
            st.dataframe(inst_pct_row, use_container_width=True)
        with c2:
            st.markdown("**Column percentages: within UNDERGRAD_UNI_LOCATION**")
            st.dataframe(inst_pct_col, use_container_width=True)

        inst_decile_pct = mc.compute_unitype_location_bin_dist(uni_base)
        if not inst_decile_pct.empty:
            st.markdown("**Figure 12. Percentile-bin distribution by institution type and location**")
            st.caption("Each row in the heatmap is one institution type-location combination.")
            st.plotly_chart(
                make_heatmap(
                    inst_decile_pct,
                    "Bin Distribution by Institution Type x Location",
                    "Percentile Bin",
                    "Institution classification",
                    "Blues",
                ),
                use_container_width=True,
                key="fig_t5_heatmap_instloc",
            )

            top_by_inst = inst_decile_pct[["B8", "B9", "B10"]].sum(axis=1).sort_values()
            st.markdown("**Figure 13. Top-bin representation by institution type and location**")
            st.caption("Top-bin representation refers to the combined share in B8-B10.")
            st.plotly_chart(
                make_top_share_bar(
                    top_by_inst,
                    "Top Bin Representation by Institution Type x Location",
                    "Percent in B8-B10",
                    "Institution classification",
                    None,
                ),
                use_container_width=True,
                key="fig_t5_top_instloc",
            )

        st.markdown("**Figure 14. Bin composition by university type**")
        st.caption("Stacked percentages sum to 100% within each university type.")
        uni_decile_pct, uni_decile_summary = mc.compute_uni_bin_summary(uni_base)
        st.plotly_chart(
            make_stacked_pct_bar(
                uni_decile_pct,
                "Bin Composition by University Type",
                "University type",
                "Percent",
                PALETTE_UNI,
            ),
            use_container_width=True,
            key="fig_t5_stacked_uni",
        )

        st.markdown("**Table 15. Bin counts by university type**")
        st.caption("Values show counts of examinees by bin within each university type.")
        st.dataframe(uni_decile_summary, use_container_width=True)

        st.markdown("**Table 16. Foreign examinee summary**")
        st.caption("Foreign examinees are shown separately because they are a small but policy-relevant subgroup.")
        _fsum = mc.compute_foreign_summary(uni_base)
        foreign = _fsum["foreign_df"]
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Foreign examinees", f"{_fsum['n_foreign']:,}")
        c2.metric("% of total", f"{_fsum['pct_of_total']:.2f}%")
        c3.metric("Median percentile", f"{_fsum['median_pct']:.1f}" if _fsum['median_pct'] is not None else "n/a")
        c4.metric(
            "Top bin %",
            f"{_fsum['topbin_pct']:.2f}%" if _fsum['topbin_pct'] is not None else "n/a",
        )

        if not foreign.empty:
            _, foreign_pct = mc.pct_table(foreign, "UNDERGRAD_UNI_TYPE", "PercentileBin", BIN_ORDER)
            foreign_pct.index.name = "UNDERGRAD_UNI_TYPE"
            st.markdown("**Figure 15. Bin distribution among foreign examinees**")
            st.caption("Values show counts and percentages for foreign examinees under the current filters.")
            st.plotly_chart(
                make_stacked_pct_bar(
                    foreign_pct,
                    "Foreign Examinees Bin Distribution",
                    "University type",
                    "Percent",
                    {"Foreign": PALETTE_UNI.get("Foreign", "#9467bd")},
                ),
                use_container_width=True,
                key="fig_t5_foreign_bin",
            )

        st.markdown("**Figure 16. Medical and allied versus other courses by university type**")
        st.caption(f"Stacked percentages sum to 100% within each university type. Uses {len(uni_type_base):,} examinees (does not require a percentile bin).")
        med_pct = mc.compute_course_bucket_by_unitype(uni_type_base)
        st.plotly_chart(
            make_stacked_pct_bar(
                med_pct,
                "Medical & Allied vs Other Courses by University Type",
                "University type",
                "Percent",
                {"Medical & Allied": "#d62728", "Other Courses": "#7f7f7f"},
            ),
            use_container_width=True,
            key="fig_t5_med_course",
        )
        st.dataframe(med_pct.reset_index(), use_container_width=True)

        st.markdown("**Table 17. University listings by university type**")
        st.caption(f"Each university listing shows the standardized university name, cleaned location, and applicant count, over {len(uni_type_base):,} examinees (does not require a percentile bin, so this includes applicants dropped from the bin-dependent charts above).")
        for uni_type in ["Public", "Private", "Foreign"]:
            table = mc.compute_university_listing(uni_type_base, uni_type)
            with st.expander(f"{uni_type} Universities", expanded=False):
                st.dataframe(table, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 6
# -----------------------------------------------------------------------------
with tab6:
    st.subheader("Pathways from Background to NMAT Outcome")
    st.caption("Flow widths represent examinee counts moving from one background category to one score or outcome category under the current filters.")
    best = F["besttrend"]
    uni = F["uni"]
    observable = F["bestobservable"]

    flow_tab1, flow_tab2, flow_tab3, flow_tab4 = st.tabs(["University -> Bin", "Course -> Bin", "Bin -> PLE", "Top pathways"])

    with flow_tab1:
        st.caption("Insight: Compare how Public, Private, and Foreign flows distribute across bins.")
        st.markdown("**Figure 17. Flow from university type to percentile bin**")
        st.caption("Each flow width represents the count of examinees moving from university type to percentile bin.")
        flow = mc.make_flow(uni, "UNDERGRAD_UNI_TYPE", "PercentileBin", ["Public", "Private", "Foreign"], BIN_ORDER)
        st.plotly_chart(
            make_sankey(flow, "UNDERGRAD_UNI_TYPE", "PercentileBin", "University Type to Bin", None, None),
            use_container_width=True,
            key="fig_t6_sankey_uni",
        )
        st.markdown("**Table 18. University-type to bin flow counts**")
        st.caption("Each row in the flow table is one source-to-target pathway with its count.")
        st.dataframe(flow, use_container_width=True)

    with flow_tab2:
        st.caption("Insight: Compare which course groups feed higher versus lower bins.")
        st.markdown("**Figure 18. Flow from course group to percentile bin**")
        st.caption("Each flow width represents the count of examinees moving from course group to percentile bin.")
        order = [
            c
            for c in ["Medical & Allied", "Natural Sciences", "Social & Behavioral Sciences", "Education", "Engineering & Technology", "Other"]
            if c in best["UNDERGRAD_COURSE_GROUP"].unique()
        ]
        flow = mc.make_flow(best, "UNDERGRAD_COURSE_GROUP", "PercentileBin", order, BIN_ORDER)
        st.plotly_chart(
            make_sankey(flow, "UNDERGRAD_COURSE_GROUP", "PercentileBin", "Course Group to Bin", None, None),
            use_container_width=True,
            key="fig_t6_sankey_course",
        )
        st.markdown("**Table 19. Course-group to bin flow counts**")
        st.caption("Each row in the flow table is one source-to-target pathway with its count.")
        st.dataframe(flow, use_container_width=True)

    with flow_tab3:
        st.caption(
            "Insight: In the observable cohort, this shows how bins map to confirmed-PLE-passer versus "
            "no-confirmed-match status. This is a LINKAGE breakdown, not a pass/fail breakdown -- "
            "'No confirmed PLE match' can include people who never sat the boards, not only people "
            "who failed."
        )
        st.markdown("**Figure 19. Flow from percentile bin to PLE status in the observable cohort**")
        st.caption("Bin-to-PLE flow uses only the observable best-record cohort (IS_BEST_OBSERVABLE_RECORD).")
        flow = mc.make_flow(observable, "PercentileBin", "PLE_STATUS_LABEL", BIN_ORDER, PLE_ORDER)
        st.plotly_chart(
            make_sankey(flow, "PercentileBin", "PLE_STATUS_LABEL", "Bin to PLE Status (Observable Cohort)", None, None),
            use_container_width=True,
            key="fig_t6_sankey_ple",
        )
        row_pct = mc.compute_flow_pct(flow, "PercentileBin", "PLE_STATUS_LABEL", BIN_ORDER, PLE_ORDER)
        st.markdown("**Table 20. PLE status composition within each bin**")
        st.caption("Bin-to-PLE flow uses only the observable best-record cohort; values are percent within each bin.")
        st.dataframe(row_pct.reset_index(), use_container_width=True)

    with flow_tab4:
        st.caption("Insight: These are the largest pathways into top bins (B8-B10).")
        st.markdown("**Table 21. Largest university-type pathways into B8-B10**")
        top_uni = mc.compute_top_pathways(uni, "UNDERGRAD_UNI_TYPE")
        top_course = mc.compute_top_pathways(best, "UNDERGRAD_COURSE_GROUP")
        c1, c2 = st.columns(2)
        with c1:
            st.dataframe(top_uni, use_container_width=True)
        with c2:
            st.markdown("**Table 22. Largest course-group pathways into B8-B10**")
            st.caption("Top pathways highlight where high-bin representation is most concentrated by count, not by rate.")
            st.dataframe(top_course, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 7
# -----------------------------------------------------------------------------
with tab7:
    st.subheader("PLE Alignment of NMAT Performance")
    st.caption("This page examines how NMAT performance and background characteristics relate to confirmed PLE outcomes within the observable best-record cohort only.")
    df = F["bestobservable"]
    dfuni = F["uniobservable"]

    st.info("This page is restricted to the observable best-record cohort so later NMAT cohorts are not misclassified as non-passers before the licensure window is observable.")

    ple_tab1, ple_tab2, ple_tab3, ple_tab4 = st.tabs(["Status profile", "Bin profile", "Background links", "Policy tables"])

    with ple_tab1:
        st.markdown("**Table 23. Score profile by PLE status**")
        st.caption("Table 23 reports count, median, mean, and interquartile range for each score measure by PLE status.")
        desc_cols = ["TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE", "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA"]
        desc = mc.compute_score_desc_by(df, "PLE_STATUS_LABEL", desc_cols)
        st.dataframe(desc, use_container_width=True)

        st.markdown("**Figure 20. TRUE raw score distribution by PLE status**")
        st.caption("The boxplot compares TRUE raw score distributions across confirmed and no-confirmed-match groups.")
        plot_df = df.dropna(subset=["PLE_STATUS_LABEL", "TotalRawScoreTRUE"]).copy()
        fig = px.box(plot_df, x="PLE_STATUS_LABEL", y="TotalRawScoreTRUE", color="PLE_STATUS_LABEL",
                     color_discrete_map=PALETTE_PLE, points=False, title="Total Raw Score by PLE Status")
        fig.update_layout(height=430, showlegend=False)
        st.plotly_chart(fig, use_container_width=True, key="fig_t7_box_raw_ple")

        st.markdown("**Table 24. Mann-Whitney comparison of confirmed passers versus no confirmed match**")
        st.caption("Table 24 compares only confirmed passers with the no-confirmed-match group and includes effect size.")
        mw = mc.mann_whitney_ple(
            df,
            {
                "TotalRawScoreTRUE": "Total Raw Score",
                "PartIRawScoreTRUE": "Part I",
                "PartIIRawScoreTRUE": "Part II",
                "NMS_PER_num": "Percentile Rank",
                "NMS_GPS": "GPS Standard Score",
            },
        )
        st.dataframe(mw, use_container_width=True)

    with ple_tab2:
        st.markdown("**Figure 21. Bin distribution by PLE status**")
        _n_null_bin = int(df["PercentileBin"].isna().sum())
        st.caption(f"This chart reads within PLE status: how bins are distributed across each PLE-status group. {_n_null_bin:,} of {len(df):,} observable-cohort rows lack a percentile bin and are excluded from this figure and Figure 22/Table 25.")
        ple_dist_count, ple_dist_pct = mc.pct_table(df, "PLE_STATUS_LABEL", "PercentileBin", BIN_ORDER)
        ple_dist_pct = ple_dist_pct.reindex(PLE_ORDER)
        ple_dist_pct.index.name = "PLE_STATUS_LABEL"
        st.plotly_chart(make_stacked_pct_bar(ple_dist_pct, "Bin Distribution by PLE Status", "PLE Status", "Percent", BIN_COLORS), use_container_width=True, key="fig_t7_bin_ple")

        st.markdown("**Figure 22. PLE status composition within each percentile bin**")
        st.caption("This chart reads within bin: how PLE statuses are distributed within each percentile bin.")
        decile_status_pct = mc.compute_ple_status_by_bin(df)
        st.plotly_chart(make_stacked_pct_bar(decile_status_pct, "PLE Status Composition within Each Bin", "Bin", "Percent within bin", PALETTE_PLE), use_container_width=True, key="fig_t7_ple_bin")
        st.markdown("**Table 25. Percent distribution of PLE status within each bin**")
        st.caption("Values show percent distribution of PLE status within each percentile bin.")
        st.dataframe(decile_status_pct.reset_index(), use_container_width=True)

    with ple_tab3:
        st.markdown("**Table 26. Course-group representation in the top bins**")
        st.caption("Top-bin survival here means the share of examinees in B8-B10, not a time-to-event survival model.")
        survival = mc.compute_top_bin_share_by(F["besttrend"], "UNDERGRAD_COURSE_GROUP")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Figure 23. Share of examinees in B8-B10 by course group**")
            st.caption("Top-bin survival here means the share of examinees in B8-B10, not a time-to-event survival model.")
            st.dataframe(survival, use_container_width=True)
        with c2:
            st.plotly_chart(
                make_top_share_bar(
                    survival.set_index("UNDERGRAD_COURSE_GROUP")["survival_rate_pct"],
                    "Survival to Top Bins by Course Group",
                    "Percent in B8-B10",
                    "Course group",
                    PALETTE_COURSE,
                ),
                use_container_width=True,
                key="fig_t7_course_top_bin",
            )

        st.markdown("**Table 27. Confirmed PLE alignment by university type in the observable cohort**")
        st.caption("University-type policy table reports observable best records, confirmed passers, no confirmed match, and confirmed PLE share.")
        plelink_uni = mc.compute_ple_alignment_by(dfuni, "UNDERGRAD_UNI_TYPE")
        st.dataframe(plelink_uni, use_container_width=True)

    with ple_tab4:
        policybase = df.copy()

        t_year = mc.compute_ple_alignment_by(policybase, "Year")
        t_course = mc.compute_ple_alignment_by(policybase, "UNDERGRAD_COURSE_GROUP", include_median=True)
        t_uni = mc.compute_ple_alignment_by(policybase, "UNDERGRAD_UNI_TYPE", include_median=True)

        st.markdown("**Table 28. Confirmed PLE alignment by NMAT year**")
        st.caption("These policy tables are designed for direct inclusion in narrative reporting and use only the observable best-record cohort.")
        st.dataframe(t_year, use_container_width=True)
        st.markdown("**Table 29. Confirmed PLE alignment by pre-med background**")
        st.dataframe(t_course, use_container_width=True)
        st.markdown("**Table 30. Confirmed PLE alignment by university type**")
        st.dataframe(t_uni, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 8
# -----------------------------------------------------------------------------
with tab8:
    st.subheader("Repeat-Taker Patterns and Score Change")
    st.caption(
        "This page examines how often examinees retake the NMAT and whether their last recorded attempt "
        "differs from their first recorded attempt. Caveat: PERSON_KEY is a name + partial-birthdate key; "
        "an estimated third or more of 'repeat takers' may be distinct people who share a name rather than "
        "one person's genuine repeat attempts (see PERSON_KEY_AMBIGUOUS in the source data)."
    )
    df = F["trend"]

    attempt_ct, attempt_summary = mc.compute_attempt_distribution(df)

    st.markdown("**Figure 24. Distribution of NMAT attempt counts per examinee**")
    st.caption("Each examinee is grouped by the number of unique NMAT applications linked to the same PERSON_KEY.")
    fig = px.bar(attempt_summary, x="Attempts", y="Count", text="Percent", title="NMAT Attempt Count Distribution")
    fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
    fig.update_layout(height=420)
    st.plotly_chart(fig, use_container_width=True, key="fig_t8_attempts")

    st.markdown("**Table 31. Attempt-count distribution**")
    st.caption("Each examinee is grouped by the number of unique NMAT applications linked to the same PERSON_KEY.")
    st.dataframe(attempt_summary, use_container_width=True)

    first_last, _traj = mc.compute_repeat_trajectories(df)
    if first_last is not None:
        summary = pd.DataFrame({
            "Indicator": [
                "Repeat-taker persons",
                "Analytic repeat takers",
                "Improved percentile rank (%)",
                "Improved raw score (%)",
                "Median percentile change",
                "Median raw score change",
            ],
            "Value": [
                _traj["n_repeat_persons"],
                _traj["n_analytic_repeat_takers"],
                _traj["pct_improved_percentile"],
                _traj["pct_improved_raw"],
                _traj["median_pct_change"],
                _traj["median_raw_change"],
            ],
        })

        st.markdown("**Table 32. Repeat-taker trajectory summary**")
        st.caption("This table summarizes repeat-taker counts and median changes from first to last attempt. Positive values indicate improvement.")
        c1, c2 = st.columns([1, 2])

        with c1:
            st.dataframe(summary, use_container_width=True)

        with c2:
            long_change = first_last.melt(
                id_vars=["PERSON_KEY", "n_attempts"],
                value_vars=["pct_improvement", "raw_improvement"],
                var_name="Measure",
                value_name="Change",
            )
            long_change["Measure"] = long_change["Measure"].replace({
                "pct_improvement": "Percentile change",
                "raw_improvement": "Raw score change",
            })

            fig = px.box(
                long_change,
                x="Measure",
                y="Change",
                color="Measure",
                points=False,
                title="Change from first to last attempt among repeat takers",
                color_discrete_map={
                    "Percentile change": "#1f77b4",
                    "Raw score change": "#d62728",
                },
            )
            fig.add_hline(y=0, line_dash="dash", line_color="red")
            fig.update_layout(height=420, showlegend=False)
            st.plotly_chart(fig, use_container_width=True, key="fig_t8_box_change")

        scatter_df = first_last.dropna(subset=["first_pct", "last_pct"]).copy()
        if not scatter_df.empty:
            fig = px.scatter(
                scatter_df,
                x="first_pct",
                y="last_pct",
                color="n_attempts",
                size="n_attempts",
                title="First vs last percentile among repeat takers",
                labels={
                    "first_pct": "First-attempt percentile",
                    "last_pct": "Last-attempt percentile",
                    "n_attempts": "Attempts",
                },
                color_continuous_scale="Viridis",
            )
            lo = float(min(scatter_df["first_pct"].min(), scatter_df["last_pct"].min()))
            hi = float(max(scatter_df["first_pct"].max(), scatter_df["last_pct"].max()))
            fig.add_trace(
                go.Scatter(
                    x=[lo, hi],
                    y=[lo, hi],
                    mode="lines",
                    name="No change",
                    line=dict(color="red", dash="dash"),
                )
            )
            fig.update_layout(height=460)
            st.plotly_chart(fig, use_container_width=True, key="fig_t8_scatter_repeat")

        st.subheader("Repeat-taker detail table")
        st.caption(
            "PERSON_KEY is a name + partial-birthdate key, not a verified individual identifier -- "
            "about 4.6% of repeat-taker keys are known collisions (contradictory SEX across rows of the "
            "same key), and the true collision rate is plausibly higher. A meaningful minority of the "
            "'repeats' below may be two different people sharing a name, not one person retaking."
        )
        display_cols = [
            "PERSON_KEY",
            "n_attempts",
            "first_year",
            "last_year",
            "first_pct",
            "last_pct",
            "pct_improvement",
            "first_raw",
            "last_raw",
            "raw_improvement",
        ]
        _rt_sorted = first_last[display_cols].sort_values(
            ["pct_improvement", "raw_improvement"], ascending=False
        )
        _rt_max = st.slider("Rows to display", min_value=50, max_value=max(50, len(_rt_sorted)), value=min(500, len(_rt_sorted)), step=50, key="rt_detail_rows")
        st.caption(f"Showing {min(_rt_max, len(_rt_sorted)):,} of {len(_rt_sorted):,} repeat-taker persons.")
        st.dataframe(_rt_sorted.head(_rt_max), use_container_width=True)
        st.download_button(
            "Download full repeat-taker detail table (CSV)",
            _rt_sorted.to_csv(index=False).encode("utf-8"),
            file_name="repeat_taker_detail_full.csv",
            mime="text/csv",
        )
    else:
        st.info("No repeat takers are available under the current filters.")

    st.divider()
    st.subheader("NMA_AppNo Deterministic Match Histories")
    st.caption("Attempt histories exclusively for records matched deterministically via NMA_AppNo.")

    # Isolate deterministic matches
    appno_matches = mc.compute_appno_deterministic_matches(df)

    if not appno_matches.empty:
        display_cols = ["PERSON_KEY", "APPNO_CLEAN", "Year", "TotalRawScoreTRUE", "NMS_PER_num", "PLE_STATUS_LABEL"]
        _am_sorted = appno_matches[display_cols].sort_values(["PERSON_KEY", "Year"])
        _am_max = st.slider("Rows to display", min_value=50, max_value=max(50, len(_am_sorted)), value=min(500, len(_am_sorted)), step=50, key="appno_match_rows")
        st.caption(f"Showing {min(_am_max, len(_am_sorted)):,} of {len(_am_sorted):,} rows.")
        st.dataframe(_am_sorted.head(_am_max), use_container_width=True)
        st.download_button(
            "Download full NMA_AppNo match-history table (CSV)",
            _am_sorted.to_csv(index=False).encode("utf-8"),
            file_name="appno_match_history_full.csv",
            mime="text/csv",
        )
    else:
        st.info("No records matched exclusively via NMA_AppNo under the current filters.")

# -----------------------------------------------------------------------------
# TAB 9
# -----------------------------------------------------------------------------
with tab9:
    st.subheader("Subtest Profiles by Institution and Course Background")
    st.caption("This page compares standardized NMAT subtest profiles across university type and course group, with optional raw-score tables for reference.")

    uni_base = F["uni"]
    course_base = F["besttrend"]

    sub_tab1, sub_tab2, sub_tab3 = st.tabs(["University type", "Course group", "Radar profiles"])

    with sub_tab1:
        uni_table = mc.subtest_mean_table(uni_base, "UNDERGRAD_UNI_TYPE", std=True)
        uni_order = [u for u in ["Public", "Private", "Foreign"] if u in uni_table.index]
        if uni_order:
            uni_table = uni_table.reindex(uni_order)

        if uni_table.empty:
            st.info("No standardized subtest scores are available for the selected filters.")
        else:
            st.markdown("**Figure 27. Mean standardized subtest scores by university type**")
            st.caption("Higher values indicate stronger average standardized performance in that subtest dimension.")
            fig = px.imshow(
                uni_table,
                text_auto=".1f",
                aspect="auto",
                color_continuous_scale="RdBu_r",
                title="Mean standardized subtest scores by university type",
                labels={"x": "Subtest", "y": "University type", "color": "Mean score"},
            )
            fig.update_layout(height=450)
            st.plotly_chart(fig, use_container_width=True, key="fig_t9_heatmap_uni")
            st.markdown("**Table 34. Standardized subtest means by university type**")
            st.caption("Higher values indicate stronger average standardized performance in that subtest dimension.")
            st.dataframe(uni_table.reset_index(), use_container_width=True)

            raw_uni_table = mc.subtest_mean_table(uni_base, "UNDERGRAD_UNI_TYPE", std=False)
            if not raw_uni_table.empty:
                with st.expander("Table 35. Raw-score subtest means by university type", expanded=False):
                    st.caption("Raw-score subtest means for reference; these are not standardized scores.")
                    st.dataframe(raw_uni_table.reset_index(), use_container_width=True)

    with sub_tab2:
        course_table = mc.subtest_mean_table(course_base, "UNDERGRAD_COURSE_GROUP", std=True)
        course_order = [c for c in PALETTE_COURSE.keys() if c in course_table.index]
        if course_order:
            course_table = course_table.reindex(course_order)

        if course_table.empty:
            st.info("No course-level standardized subtest scores are available for the selected filters.")
        else:
            fig = px.imshow(
                course_table,
                text_auto=".1f",
                aspect="auto",
                color_continuous_scale="RdBu_r",
                title="Mean standardized subtest scores by course group",
                labels={"x": "Subtest", "y": "Course group", "color": "Mean score"},
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True, key="fig_t9_heatmap_course")
            st.markdown("**Figure 28. Mean standardized subtest scores by course group**")
            st.caption("Higher values indicate stronger average standardized performance in that subtest dimension.")
            st.dataframe(course_table.reset_index(), use_container_width=True)

            raw_course_table = mc.subtest_mean_table(course_base, "UNDERGRAD_COURSE_GROUP", std=False)
            if not raw_course_table.empty:
                with st.expander("Table 37. Raw-score subtest means by course group", expanded=False):
                    st.caption("Raw-score subtest means for reference; these are not standardized scores.")
                    st.dataframe(raw_course_table.reset_index(), use_container_width=True)

    with sub_tab3:
        c1, c2 = st.columns(2)

        with c1:
            if uni_base.empty:
                st.info("No university-type data available for radar plotting.")
            else:
                st.markdown("**Figure 29. Standardized subtest radar profile by university type**")
                st.caption("Radar shapes are descriptive profiles and should be read together with the mean-value tables.")
                fig_uni, tbl_uni = mc.radar_for_group(uni_base[uni_base["UNDERGRAD_UNI_TYPE"].isin(["Public", "Private", "Foreign"])], "UNDERGRAD_UNI_TYPE")
                st.plotly_chart(fig_uni, use_container_width=True, key="fig_t9_radar_uni")
                st.markdown("**Table 38. Radar-profile values by university type**")
                st.dataframe(tbl_uni.reset_index(), use_container_width=True)

        with c2:
            if course_base.empty:
                st.info("No course-group data available for radar plotting.")
            else:
                st.markdown("**Figure 30. Standardized subtest radar profile by course group**")
                st.caption("Radar shapes are descriptive profiles and should be read together with the mean-value tables.")
                fig_course, tbl_course = mc.radar_for_group(course_base, "UNDERGRAD_COURSE_GROUP")
                st.plotly_chart(fig_course, use_container_width=True, key="fig_t9_radar_course")
                st.markdown("**Table 39. Radar-profile values by course group**")
                st.dataframe(tbl_course.reset_index(), use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 10
# -----------------------------------------------------------------------------
with tab10:
    st.subheader("PLE Year Gap and Gender Patterns")
    st.caption("This page summarizes the time between NMAT and confirmed PLE passage, and compares sex-coded performance patterns in the filtered cohorts.")

    gap_tab1, gap_tab2 = st.tabs(["PLE year gap", "Gender patterns"])

    with gap_tab1:
        gap_df, _gap_kpis = mc.compute_year_gap_kpis(F["bestobservable"])

        if gap_df.empty:
            st.info("No confirmed observable PLE year-gap records are available under the current filters.")
        else:
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Confirmed passers", f"{_gap_kpis['n']:,}")
            col2.metric("Median year gap", f"{_gap_kpis['median']:.1f}", help="Median of PLE_YEAR_GAP among confirmed observable passers.")
            col3.metric("Q1 year gap", f"{_gap_kpis['q25']:.1f}", help="25th percentile of PLE_YEAR_GAP among confirmed observable passers.")
            col4.metric("Q3 year gap", f"{_gap_kpis['q75']:.1f}", help="75th percentile of PLE_YEAR_GAP among confirmed observable passers.")

            c1, c2 = st.columns(2)

            with c1:
                st.markdown("**Figure 31. Distribution of NMAT-to-PLE year gap**")
                st.caption("Only confirmed observable PLE passers with non-missing PLE_YEAR_GAP are included.")
                fig = px.histogram(
                    gap_df,
                    x="PLE_YEAR_GAP",
                    nbins=25,
                    title="Distribution of NMAT-to-PLE year gap",
                    labels={"PLE_YEAR_GAP": "PLE year gap"},
                    color_discrete_sequence=["#1f77b4"],
                )
                fig.update_layout(height=420)
                st.plotly_chart(fig, use_container_width=True, key="fig_t10_gap_hist")

            with c2:
                st.markdown("**Figure 32. PLE year gap by course group**")
                st.caption("Only confirmed observable PLE passers with non-missing PLE_YEAR_GAP are included.")
                box_base = gap_df.dropna(subset=["UNDERGRAD_COURSE_GROUP", "PLE_YEAR_GAP"]).copy()
                fig = px.box(
                    box_base,
                    x="UNDERGRAD_COURSE_GROUP",
                    y="PLE_YEAR_GAP",
                    color="UNDERGRAD_COURSE_GROUP",
                    title="PLE year gap by course group",
                    color_discrete_map=PALETTE_COURSE,
                )
                fig.update_layout(height=420, xaxis_title="", yaxis_title="PLE year gap")
                st.plotly_chart(fig, use_container_width=True, key="fig_t10_gap_box")

            gap_summary = mc.compute_year_gap_by_course(gap_df)
            st.markdown("**Table 40. Year-gap summary by course group**")
            st.caption("Table 40 reports confirmed passers, median year gap, interquartile range, and median NMAT percentile rank by course group.")
            st.dataframe(gap_summary, use_container_width=True)

    with gap_tab2:
        sex_base = F["besttrend"].dropna(subset=["SEX_CLEAN"]).copy()
        observable_sex = F["bestobservable"].dropna(subset=["SEX_CLEAN"]).copy()

        if sex_base.empty:
            st.info("No sex-coded records are available under the current filters.")
        else:
            c1, c2 = st.columns(2)

            with c1:
                st.markdown("**Table 41. Score summary by sex**")
                st.caption("Sex summaries use records with valid SEX_CLEAN coding only.")
                sex_perf = mc.compute_score_by_sex(sex_base)
                st.dataframe(sex_perf, use_container_width=True)

            with c2:
                st.markdown("**Figure 33. Percentile-rank distribution by sex**")
                st.caption("The boxplot shows percentile-rank spread by sex.")
                fig = px.box(
                    sex_base,
                    x="SEX_CLEAN",
                    y="NMS_PER_num",
                    color="SEX_CLEAN",
                    title="Percentile rank by sex",
                    color_discrete_map={"Male": "#1f77b4", "Female": "#e377c2"},
                    points=False,
                )
                fig.update_layout(height=420, xaxis_title="", yaxis_title="Percentile rank")
                st.plotly_chart(fig, use_container_width=True, key="fig_t10_box_sex")

            _, sex_year_pct = mc.pct_table(sex_base, "Year", "SEX_CLEAN", ["Male", "Female"])
            st.markdown("**Figure 34. Sex composition by NMAT year**")
            st.caption("The stacked bar shows the within-year sex mix.")
            fig = make_stacked_pct_bar(
                sex_year_pct,
                "Sex composition by NMAT year",
                "Year",
                "Percent within year",
                {"Male": "#1f77b4", "Female": "#e377c2"},
            )
            st.plotly_chart(fig, use_container_width=True, key="fig_t10_sex_year")

            if not observable_sex.empty:
                _, sex_ple_pct = mc.pct_table(observable_sex, "SEX_CLEAN", "PLE_STATUS_LABEL", PLE_ORDER)
                fig = make_stacked_pct_bar(
                    sex_ple_pct,
                    "PLE status composition by sex (observable cohort)",
                    "Sex",
                    "Percent within sex",
                    PALETTE_PLE,
                )
                st.markdown("**Table 42. PLE status composition by sex in the observable cohort**")
                st.caption("The PLE-status table shows the percent distribution of confirmed and no-confirmed-match outcomes within each sex.")
                st.plotly_chart(fig, use_container_width=True, key="fig_t10_sex_ple")
                st.dataframe(sex_ple_pct.reset_index(), use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 11
# -----------------------------------------------------------------------------
with tab11:
    st.subheader("Statistical Test Results")
    st.caption("This page reports non-parametric tests used to assess whether observed descriptive differences across groups are statistically detectable in the filtered data.")

    stat_tab1, stat_tab2, stat_tab3, stat_tab4 = st.tabs(
        ["Kruskal-Wallis by year", "PLE status tests", "Chi-square tests", "Post hoc"]
    )

    with stat_tab1:
        test_df = F["besttrend"].copy()
        score_map = {
            "TotalRawScoreTRUE": "Total raw score",
            "PartIRawScoreTRUE": "Part I raw score",
            "PartIIRawScoreTRUE": "Part II raw score",
            "NMS_PER_num": "Percentile rank",
            "NMS_GPS": "GPS standard score",
        }
        kw_tbl = mc.kruskal_table(test_df, "Year", score_map)
        if kw_tbl.empty:
            st.info("Not enough data to run year-based Kruskal-Wallis tests.")
        else:
            st.markdown("**Table 43. Kruskal-Wallis tests for score distributions across NMAT years**")
            st.caption("Each row reports the Kruskal-Wallis H-statistic and p-value testing whether the score distribution differs across NMAT years.")
            st.dataframe(kw_tbl, use_container_width=True)

    with stat_tab2:
        ple_test_df = F["bestobservable"].copy()
        mw_tbl = mc.mann_whitney_ple(
            ple_test_df,
            {
                "TotalRawScoreTRUE": "Total raw score",
                "PartIRawScoreTRUE": "Part I raw score",
                "PartIIRawScoreTRUE": "Part II raw score",
                "NMS_PER_num": "Percentile rank",
                "NMS_GPS": "GPS standard score",
            },
        )
        if mw_tbl.empty:
            st.info("Not enough observable PLE-status data for Mann-Whitney tests.")
        else:
            st.markdown("**Table 44. Mann-Whitney comparisons by PLE status (observable cohort)**")
            st.caption("Tests compare confirmed passers vs no confirmed match (and other pairings where applicable). Reported values include U and p-value.")
            st.dataframe(mw_tbl, use_container_width=True)

    with stat_tab3:
        chi_base = F["uni"].copy()
        if chi_base.empty:
            st.info("No university-type records are available for chi-square testing.")
        else:
            observed_tbl, expected_tbl, chi_summary = mc.chi_square_unitype_bin(chi_base)

            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Table 45. Observed counts by university type and percentile bin**")
                st.caption("Cell counts of examinees by university type (rows) and percentile bin (columns).")
                st.dataframe(observed_tbl.reset_index(), use_container_width=True)
                st.markdown("**Table 46. Chi-square summary (university type × bin)**")
                st.caption("Chi-square statistic, degrees of freedom, and p-value testing independence between university type and bin.")
                st.dataframe(chi_summary, use_container_width=True)

            with c2:
                row_pct = observed_tbl.div(observed_tbl.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(2)
                st.markdown("**Figure 35. University type × bin row percentages**")
                st.caption("Heatmap shows row-wise percent distribution (percent of each university type located in each bin).")
                fig = px.imshow(
                    row_pct,
                    text_auto=".1f",
                    aspect="auto",
                    color_continuous_scale="YlGnBu",
                    title="University type × bin row percentages",
                    labels={"x": "Percentile bin", "y": "University type", "color": "Percent"},
                )
                fig.update_layout(height=450)
                st.plotly_chart(fig, use_container_width=True, key="fig_t11_heatmap_chi")

            with st.expander("Table 47. Expected counts", expanded=False):
                st.caption("Expected cell counts under the null hypothesis of independence between university type and bin.")
                st.dataframe(expected_tbl.reset_index(), use_container_width=True)

    with stat_tab4:
        if not HAS_POSTHOCS:
            st.info("scikit-posthocs is not installed, so Dunn post-hoc output is skipped.")
        else:
            dunn = mc.compute_dunn_posthoc(F["besttrend"])
            if dunn is None:
                st.info("Not enough year groups are available for post-hoc testing.")
            else:
                st.markdown("**Figure 36. Dunn post-hoc adjusted p-value matrix (percentile rank by year)**")
                st.caption("Bonferroni-adjusted p-values from pairwise Dunn tests; cells < 0.05 indicate significant pairwise differences.")
                fig = px.imshow(
                    dunn,
                    text_auto=".3f",
                    aspect="auto",
                    color_continuous_scale="Viridis_r",
                    title="Dunn post-hoc adjusted p-values for percentile rank by year",
                    labels={"x": "Year", "y": "Year", "color": "Adj. p-value"},
                )
                fig.update_layout(height=520)
                st.plotly_chart(fig, use_container_width=True, key="fig_t11_dunn")
                st.markdown("**Table 48. Dunn post-hoc adjusted p-values**")
                st.dataframe(dunn.reset_index(), use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 12
# -----------------------------------------------------------------------------
with tab12:
    st.subheader("Policy Tables and Downloads")
    st.caption(
        "These tables are formatted as policy-ready reference tables and use the observable best-record "
        "cohort (IS_BEST_OBSERVABLE_RECORD) for all PLE-linked summaries. \"confirmed_ple_share_pct\" is a "
        "LINKAGE rate (share found in the PLE passer source list), not a licensure pass rate -- the source "
        "contains passers only, so absence is not evidence of failure."
    )

    policybase = F["bestobservable"].copy()

    if policybase.empty:
        st.info("No observable best-record rows are available under the current filters.")
    else:
        t_year = mc.compute_ple_alignment_by(policybase, "Year")
        t_course = mc.compute_ple_alignment_by(policybase, "UNDERGRAD_COURSE_GROUP", include_median=True)
        t_uni = mc.compute_ple_alignment_by(policybase, "UNDERGRAD_UNI_TYPE", include_median=True)
        survival = mc.compute_top_bin_share_by(F["besttrend"], "UNDERGRAD_COURSE_GROUP")

        st.markdown("### Table 1. Confirmed PLE alignment by NMAT year")
        st.dataframe(t_year, use_container_width=True)

        st.markdown("### Table 2. Confirmed PLE alignment by pre-med background")
        st.dataframe(t_course, use_container_width=True)

        st.markdown("### Table 3. Confirmed PLE alignment by university type")
        st.dataframe(t_uni, use_container_width=True)

        st.markdown("### Table 4. Survival to top bins by course group")
        c1, c2 = st.columns([1, 1])
        with c1:
            st.dataframe(survival, use_container_width=True)
        with c2:
            st.plotly_chart(
                make_top_share_bar(
                    survival.set_index("UNDERGRAD_COURSE_GROUP")["survival_rate_pct"],
                    "Survival to Top Bins by Course Group",
                    "Percent in B8-B10",
                    "Course group",
                    PALETTE_COURSE,
                ),
                use_container_width=True,
                key="fig_t12_survival",
            )

        st.markdown("### Download policy tables as CSV")
        st.caption("Each download reflects the current filter settings applied in the dashboard.")
        d1, d2, d3, d4 = st.columns(4)
        with d1:
            st.download_button(
                "Download year table",
                data=t_year.to_csv(index=False).encode("utf-8"),
                file_name="policy_table_year.csv",
                mime="text/csv",
            )
        with d2:
            st.download_button(
                "Download course table",
                data=t_course.to_csv(index=False).encode("utf-8"),
                file_name="policy_table_course.csv",
                mime="text/csv",
            )
        with d3:
            st.download_button(
                "Download university table",
                data=t_uni.to_csv(index=False).encode("utf-8"),
                file_name="policy_table_university.csv",
                mime="text/csv",
            )
        with d4:
            st.download_button(
                "Download survival table",
                data=survival.to_csv(index=False).encode("utf-8"),
                file_name="policy_table_top_decile_survival.csv",
                mime="text/csv",
            )

# -----------------------------------------------------------------------------
# TAB 13 — CHED Compliance
# -----------------------------------------------------------------------------
with tab13:
    st.subheader("CHED Compliance — What This Dataset Can and Cannot Tell CHED")
    st.caption(
        "CMO No. __, s. 2026 conditions a PHEI's NMAT cut-off privilege (30th vs 40th percentile) on "
        "that PHEI's OWN PLE passing performance. This dataset cannot support that specific, "
        "per-institution determination -- see the panel below. What follows is restricted to claims "
        "the schema genuinely supports: applicant-pool distributions against the candidate thresholds, "
        "foreign-vs-Filipino composition, and the individual-level PLE-linkage gradient."
    )

    with st.expander("What this dataset CAN and CANNOT tell CHED (read first)", expanded=True):
        st.markdown(
            """
**Supportable, and shown below:**
- Applicant-pool percentile distributions against the 30th- and 40th-percentile candidate thresholds (Section A).
- Foreign-vs-Filipino composition of the applicant pool, by percentile bin (Section B).
- The individual-level PLE-linkage gradient by percentile bin -- a steady rise from bottom to top decile, with no sharp step at the 40th-percentile threshold (Section C).

**NOT supportable with this dataset, and not shown below:**
- **Per-institution PLE performance.** `UNDERGRAD_UNIVERSITY` records the examinee's undergraduate
  (pre-NMAT) school, not the medical school the CMO regulates -- e.g. UP Diliman appears in this data
  with over a thousand eventual PLE-linked examinees despite having no College of Medicine. No column
  in this schema identifies the medical school actually attended. A per-HEI "PLE passing rate"
  computed from this data would attribute licensure outcomes to the wrong institution.
- **The CMO's 5-year national PLE benchmark.** The benchmark the CMO means is the PRC's published
  national PLE passing percentage for the last 5 *administrations of the exam*. This dataset has no
  PRC pass-rate series and no fail records at all (the PLE source list contains passers only), so it
  cannot compute that benchmark -- only a same-cohort "linkage rate" that is a different statistic. The
  observable-cohort restriction (Year<=2014) also means any dataset-derived proxy would be permanently
  frozen 12+ years in the past relative to the CMO's 2026 effectivity.
- **GIDA/IP equity provisions.** No geographic-isolation, indigenous-peoples, or socioeconomic field
  exists anywhere in the schema.
- **Enrolment, and the 10-foreign-slot cap.** This dataset counts NMAT *test-takers*, not admitted or
  enrolled MD freshmen, and the cap is only effective AY2026-2027 -- applying it to 2006-2018
  test-taker counts would misrepresent historical testing volume as policy violations.
- **Composite 60/40 or 70/30 admission ranking.** No GWA, interview score, or other admission
  criterion exists in this dataset beyond the NMAT itself.

A prior version of this tab attempted per-HEI PLE pass/fail verdicts, a "5-year rolling national
benchmark," and a foreign-enrolment cap check against 2006-2018 data. All three were removed because
the data cannot support them, not because they were miscalculated -- fixing the arithmetic would not
fix the underlying category error (RC-4: `UNDERGRAD_UNIVERSITY` is the wrong institution for a PLE
performance claim).
            """
        )

    st.divider()

    df_obs = F["bestobservable"]
    df_trend = F["besttrend"]

    if df_obs.empty:
        st.info("No observable best-record rows are available under the current filters.")
    else:
        # -- Section A: Applicant-pool cut-off scenarios -----------------------
        st.markdown("### Section A: Applicant-Pool Cut-off Scenarios (30th vs 40th Percentile)")
        st.caption(
            "Compares the observable-cohort applicant pool at or above the 30th-percentile (B4+) and "
            "40th-percentile (B5+) candidate thresholds, by undergraduate institution type. "
            "\"PLE linkage rate\" is the share found in the PLE passer source list -- not a licensure "
            "pass rate, since the source contains passers only. Both columns below use the SAME "
            "observable-cohort window (Year<=2014) so they describe one consistent population; an "
            "earlier version of this table mixed a full-history 'admitted' count with an "
            "observable-only PLE count in the same row."
        )

        _scenario_df = mc.compute_cutoff_scenarios(df_obs)

        _c1, _c2 = st.columns([1, 1])
        with _c1:
            st.dataframe(_scenario_df, use_container_width=True, hide_index=True)
        with _c2:
            _fig_scenario = px.bar(
                _scenario_df,
                x="University Type", y="PLE linkage rate (%)",
                color="Cut-off", barmode="group",
                title="PLE Linkage Rate by Cut-off Scenario (observable cohort)",
                color_discrete_map={
                    "30th percentile (B4+)": "#2e7d32",
                    "40th percentile (B5+)": "#1565c0",
                },
            )
            _fig_scenario.update_layout(height=400)
            st.plotly_chart(_fig_scenario, use_container_width=True, key="fig_t13_scenario")

        st.info(
            "**Reading this table:** PLE linkage rises steadily from the lowest to the highest percentile "
            "bin, with no sharp step at the 30th or 40th percentile threshold -- see the bin-by-bin gradient "
            "in Section C. A notable data point: a nontrivial number of B1 (lowest-decile) examinees are "
            "confirmed PLE passers, which a strictly binding 40th-percentile admission floor would not "
            "predict. This table describes the applicant pool's outcomes at each threshold; it is not, by "
            "itself, a causal estimate of what would happen if a cut-off were changed."
        )

        st.download_button(
            "Download cut-off scenarios",
            data=_scenario_df.to_csv(index=False).encode("utf-8"),
            file_name="ched_cutoff_scenarios.csv",
            mime="text/csv",
        )

        st.divider()

        # -- Section B: Foreign vs Filipino applicant-pool composition ---------
        st.markdown("### Section B: Foreign vs. Filipino Applicant-Pool Composition")
        st.caption(
            "Percentile-bin composition of the observable applicant pool, split by citizenship status. "
            "This describes the applicant pool only -- it is not an institutional or enrolment metric, "
            "and it says nothing about the 10-foreign-slot enrolment cap (which this dataset cannot "
            "evaluate; see the panel above)."
        )

        _citz_n, _citz_pct = mc.compute_citizenship_group_bin_dist(F["uniobservable"])
        if _citz_pct is not None:
            _cb1, _cb2 = st.columns(2)
            with _cb1:
                st.plotly_chart(
                    make_stacked_pct_bar(_citz_pct, "Bin Composition: Foreigner vs Filipino", "Group", "Percent", BIN_COLORS),
                    use_container_width=True, key="fig_t13_citz_stacked",
                )
            with _cb2:
                st.dataframe(_citz_n, use_container_width=True, hide_index=True)
                st.dataframe(_citz_pct.reset_index(), use_container_width=True, hide_index=True)
        else:
            st.info("Citizenship columns not available. Run Pipeline 4 to generate NMAT_Exodus.parquet.")

        st.divider()

        # -- Section C: Individual-level PLE linkage gradient -------------------
        st.markdown("### Section C: Individual-Level PLE Linkage Gradient by Percentile Bin")
        st.caption(
            "The one individual-level relationship this dataset can speak to directly: how the PLE "
            "linkage rate rises with NMAT percentile bin, in the observable cohort."
        )

        _grad = mc.compute_linkage_gradient(df_obs)

        _gc1, _gc2 = st.columns([1, 1])
        with _gc1:
            st.dataframe(_grad, use_container_width=True, hide_index=True)
        with _gc2:
            _fig_grad = go.Figure(go.Bar(
                x=_grad["PercentileBin"], y=_grad["linkage_rate_pct"],
                marker_color=[BIN_COLORS.get(b, "#7f7f7f") for b in _grad["PercentileBin"]],
                text=[f"{v:.1f}%" if pd.notna(v) else "" for v in _grad["linkage_rate_pct"]],
                textposition="outside",
            ))
            _fig_grad.update_layout(
                title="PLE Linkage Rate by Percentile Bin (observable cohort)",
                xaxis_title="Percentile bin", yaxis_title="Linkage rate (%)", height=420,
            )
            st.plotly_chart(_fig_grad, use_container_width=True, key="fig_t13_gradient")

        _b1_row = _grad[_grad["PercentileBin"] == "B1"]
        _b1_passers = int(_b1_row["linked_n"].iloc[0]) if not _b1_row.empty and pd.notna(_b1_row["linked_n"].iloc[0]) else 0
        st.caption(
            f"The gradient rises steadily from the lowest to the highest bin, with no sharp step at the "
            f"30th (B4) or 40th (B5) percentile threshold. Notably, {_b1_passers:,} B1 (lowest-decile) "
            "examinees in the observable cohort are confirmed PLE passers -- a strictly binding "
            "40th-percentile admission floor would predict this group should barely exist."
        )

        st.download_button(
            "Download linkage-gradient table",
            data=_grad.to_csv(index=False).encode("utf-8"),
            file_name="ched_linkage_gradient_by_bin.csv",
            mime="text/csv",
        )
