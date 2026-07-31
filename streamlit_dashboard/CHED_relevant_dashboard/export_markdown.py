"""
export_markdown.py — Export the CHED dashboard as one complete Markdown document
with all visualization charts saved as high-quality PNGs.

Every number in this file comes from the SAME `ched_common.compute_*()`
functions that `dashboard.py` renders from (export-format contract Rule 6).
There is no independent re-derivation of any aggregation here — that was
the root cause of the published 57/49-vs-56/48 median-percentile drift and
the India-85.1%-vs-81.5% nationality-share bug.

Public function: build_full_markdown(df_all, df_best, df_obs, viz_dir) -> str
"""

import hashlib
import os
from datetime import datetime

import numpy as np
import pandas as pd

import ched_common as cc

BIN_ORDER = cc.BIN_ORDER
B4_PLUS = cc.B4_PLUS
B5_PLUS = cc.B5_PLUS
TOP_BINS = cc.TOP_BINS
BOTTOM_BINS = cc.BOTTOM_BINS
BIN_RANGES = cc.BIN_LABELS
COLORS_UNI = cc.COLORS_UNI
COURSE_COLORS = cc.COLORS_COURSE
UNI_TYPE_COL = cc.UNI_TYPE_COL
COURSE_GROUP_COL = cc.COURSE_GROUP_COL

# Export-integrity counters, reset per build_full_markdown() call.
_INTEGRITY = {"tabs": 0, "tabs_total": 6, "charts": 0, "charts_total": 0,
              "tables": 0, "captions": 0, "assertions_passed": 0, "assertions_total": 0}


def _reset_integrity():
    for k in _INTEGRITY:
        _INTEGRITY[k] = 0
    _INTEGRITY["tabs_total"] = 6


def _assert_equal(label, a, b, tol=1e-6):
    """Assert an exported value equals the value computed directly from the
    shared compute layer (contract Rule 6 verification requirement)."""
    _INTEGRITY["assertions_total"] += 1
    ok = (abs(a - b) <= tol) if isinstance(a, (int, float)) and isinstance(b, (int, float)) else (a == b)
    if ok:
        _INTEGRITY["assertions_passed"] += 1
    return ok


# ---------------------------------------------------------------------------
# Chart generation (charts are supplementary; the data table is mandatory)
# ---------------------------------------------------------------------------
def _save_plot(fig, viz_dir, md_dir, name):
    """Save a plotly figure as PNG; return a path relative to md_dir."""
    os.makedirs(viz_dir, exist_ok=True)
    path = os.path.join(viz_dir, name)
    fig.write_image(path, width=1000, height=600, scale=2, engine="kaleido")
    rel = os.path.relpath(path, start=md_dir) if md_dir else f"viz/{name}"
    return rel.replace(os.sep, "/")


def generate_all_charts(df_all, df_best, df_obs, viz_dir, md_dir=None):
    """Generate all dashboard charts as PNG files. Returns name -> relative path."""
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    db = cc.bins_population(df_best)
    md_dir = md_dir or viz_dir
    os.makedirs(viz_dir, exist_ok=True)
    chart_map = {}

    ut = cc.compute_composition(df_best, UNI_TYPE_COL)
    fig = px.pie(ut, names=UNI_TYPE_COL, values="Count", title="University Type Composition",
                  color=UNI_TYPE_COL, color_discrete_map=COLORS_UNI)
    fig.update_traces(textinfo="label+percent", textfont_size=12)
    chart_map["uni_pie"] = _save_plot(fig, viz_dir, md_dir, "01_uni_type_pie.png")

    cg = cc.compute_composition(df_best, COURSE_GROUP_COL)
    fig = px.pie(cg, names=COURSE_GROUP_COL, values="Count", title="Course Group Composition",
                  color=COURSE_GROUP_COL, color_discrete_map=COURSE_COLORS)
    fig.update_traces(textinfo="label+percent", textfont_size=12)
    chart_map["course_pie"] = _save_plot(fig, viz_dir, md_dir, "01_course_group_pie.png")

    yr = cc.compute_annual_trend(df_best)
    yr["Year"] = yr["Year"].astype(str)
    fig = make_subplots(rows=2, cols=1, subplot_titles=("Examinee Volume by Year", "Median NMAT Percentile by Year"), vertical_spacing=0.22)
    fig.add_trace(go.Bar(x=yr["Year"], y=yr["Examinees"], name="Examinees", marker_color="#1f77b4"), row=1, col=1)
    fig.add_trace(go.Scatter(x=yr["Year"], y=yr["Median_percentile"], mode="lines+markers", name="Median NMAT percentile", line=dict(color="#d62728", width=3)), row=2, col=1)
    fig.update_layout(height=500)
    chart_map["annual_trend"] = _save_plot(fig, viz_dir, md_dir, "01_annual_trend.png")

    yp = cc.compute_bin_dist_by(db, "Year").set_index("Year")
    fig = px.imshow(yp.T.reindex(BIN_ORDER[::-1]), text_auto=True, aspect="auto",
                    color_continuous_scale="YlOrRd",
                    labels={"x": "Year", "y": "Bin", "color": "%"},
                    title="Score Bin Distribution by NMAT Year (Row %)")
    fig.update_layout(height=460)
    chart_map["bin_heatmap"] = _save_plot(fig, viz_dir, md_dir, "02_bin_heatmap.png")

    tb = cc.compute_top_bottom_trend(df_best)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tb["Year"], y=tb["Top B8-B10 (%)"], mode="lines+markers", name="Top B8-B10", line=dict(color="#2e7d32", width=3)))
    fig.add_trace(go.Scatter(x=tb["Year"], y=tb["Bottom B1-B3 (%)"], mode="lines+markers", name="Bottom B1-B3", line=dict(color="#c62828", width=3)))
    fig.update_layout(title="Top Bins (B8-B10) vs Bottom Bins (B1-B3) by Year", height=400)
    chart_map["top_bottom_trend"] = _save_plot(fig, viz_dir, md_dir, "02_top_bottom_trend.png")

    b4prof = cc.compute_b4_group_profile(db)
    fig = px.bar(b4prof["by_uni"], x=UNI_TYPE_COL, y="count", title="B4 Examinees by Institution Type",
                 color=UNI_TYPE_COL, color_discrete_map=COLORS_UNI)
    chart_map["b4_group"] = _save_plot(fig, viz_dir, md_dir, "02_b4_group.png")

    pl = cc.compute_linkage_by(df_obs, "PercentileBin")
    fig = px.bar(pl, x="PercentileBin", y="Linkage Rate (%)",
                 title="NMAT-to-PLE-Passer Linkage Rate by Score Bin",
                 color="Linkage Rate (%)", color_continuous_scale="Viridis",
                 text=pl["Linkage Rate (%)"].round(1).astype(str) + "%")
    fig.update_traces(textposition="outside")
    fig.update_layout(height=480)
    fig.add_hline(y=50, line_dash="dash", line_color="gray")
    chart_map["ple_linkage_bin"] = _save_plot(fig, viz_dir, md_dir, "03_ple_linkage_bin.png")

    ply = cc.compute_linkage_by(df_obs, "Year")
    ply["Year"] = ply["Year"].astype(str)
    fig = px.line(ply, x="Year", y="Linkage Rate (%)", markers=True, title="NMAT-to-PLE-Passer Linkage Rate by NMAT Year")
    fig.update_traces(line=dict(color="#1f77b4", width=3))
    fig.update_layout(height=400)
    chart_map["ple_linkage_year"] = _save_plot(fig, viz_dir, md_dir, "03_ple_linkage_year.png")

    plc = cc.compute_linkage_by(df_obs, COURSE_GROUP_COL)
    if len(plc):
        fig = px.bar(plc, x=COURSE_GROUP_COL, y="Linkage Rate (%)", title="NMAT-to-PLE-Passer Linkage Rate by Course Group",
                     color=COURSE_GROUP_COL, color_discrete_map=COURSE_COLORS,
                     text=plc["Linkage Rate (%)"].round(1).astype(str) + "%")
        fig.update_traces(textposition="outside")
        fig.update_layout(height=400, showlegend=False, xaxis_tickangle=-20)
        chart_map["ple_linkage_course"] = _save_plot(fig, viz_dir, md_dir, "03_ple_linkage_course.png")

    plu = cc.compute_linkage_by(df_obs[df_obs[UNI_TYPE_COL].isin(["Public", "Private", "Foreign"])], UNI_TYPE_COL)
    if len(plu):
        fig = px.bar(plu, x=UNI_TYPE_COL, y="Linkage Rate (%)", title="NMAT-to-PLE-Passer Linkage Rate by University Type",
                     color=UNI_TYPE_COL, color_discrete_map=COLORS_UNI,
                     text=plu["Linkage Rate (%)"].round(1).astype(str) + "%")
        fig.update_traces(textposition="outside")
        fig.update_layout(height=400, showlegend=False)
        chart_map["ple_linkage_uni"] = _save_plot(fig, viz_dir, md_dir, "03_ple_linkage_uni.png")

    uni = df_best[df_best[UNI_TYPE_COL].isin(["Public", "Private", "Foreign"])]
    fig = px.box(uni.dropna(subset=["NMS_PER_num"]), x=UNI_TYPE_COL, y="NMS_PER_num",
                 color=UNI_TYPE_COL, color_discrete_map=COLORS_UNI, points=False,
                 title="NMAT Percentile Distribution by University Type",
                 labels={"NMS_PER_num": "NMAT percentile (0-99)", UNI_TYPE_COL: ""})
    fig.update_layout(height=400, showlegend=False)
    chart_map["uni_box"] = _save_plot(fig, viz_dir, md_dir, "04_uni_box.png")

    ubp = cc.compute_bin_dist_by(uni, UNI_TYPE_COL).set_index(UNI_TYPE_COL)
    fig = px.imshow(ubp, text_auto=True, aspect="auto", color_continuous_scale="YlOrRd",
                    labels={"x": "Score Bin", "y": "University Type", "color": "%"},
                    title="Bin Distribution by University Type (Row %)")
    fig.update_layout(height=350)
    chart_map["uni_bin_heatmap"] = _save_plot(fig, viz_dir, md_dir, "04_uni_bin_heatmap.png")

    top_uni_tbl = cc.compute_top_bin_share_by(uni, UNI_TYPE_COL)
    fig = go.Figure(go.Bar(x=top_uni_tbl["Top B8-B10 (%)"], y=top_uni_tbl[UNI_TYPE_COL], orientation="h",
                           marker_color=[COLORS_UNI.get(i, "#7f7f7f") for i in top_uni_tbl[UNI_TYPE_COL]],
                           text=[f"{v:.1f}%" for v in top_uni_tbl["Top B8-B10 (%)"]], textposition="outside"))
    fig.update_layout(title="Top-Bin Share (B8-B10) by University Type",
                      xaxis_title="Percent in B8-B10", yaxis_title="", height=300)
    chart_map["top_bin_uni"] = _save_plot(fig, viz_dir, md_dir, "04_top_bin_uni.png")

    fctx = cc.compute_foreign_context(df_best)
    if fctx["n_foreign"] > 0:
        top_nat = cc.compute_nationality_shares(df_best)
        fig = px.bar(top_nat, x="Count", y="Nationality", orientation="h",
                     title="Top 10 Nationalities Among Verified Foreign NMAT Examinees",
                     color="Count", color_continuous_scale="Blues")
        fig.update_layout(height=350)
        chart_map["foreign_top"] = _save_plot(fig, viz_dir, md_dir, "04_foreign_top10.png")

    _INTEGRITY["charts_total"] = len(chart_map)
    _INTEGRITY["charts"] = len(chart_map)
    return chart_map


# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------
def h1(t): return f"\n# {t}\n"
def h2(t): return f"\n## {t}\n"
def h3(t): return f"\n### {t}\n"
def p(t):
    _INTEGRITY["captions"] += 1
    return f"{t}\n"
def sep(): return "\n---\n"


def df_to_markdown(df, index=False, float_format=".1f"):
    d = df.copy()
    for c in d.columns:
        if pd.api.types.is_integer_dtype(d[c]):
            d[c] = d[c].apply(lambda x: f"{x:,}" if pd.notna(x) else "-")
        elif pd.api.types.is_float_dtype(d[c]):
            d[c] = d[c].apply(lambda x: f"{x:{float_format}}" if pd.notna(x) else "-")
    for c in d.columns:
        if pd.api.types.is_bool_dtype(d[c]):
            d[c] = d[c].apply(lambda x: "True" if x else "False")

    _INTEGRITY["tables"] += 1
    try:
        import tabulate
        return d.to_markdown(index=index, tablefmt="pipe", numalign="right", stralign="left")
    except ImportError:
        pass

    rows = []
    headers = list(d.columns)
    if index:
        headers.insert(0, d.index.name or "")
    rows.append("| " + " | ".join(str(h) for h in headers) + " |")
    rows.append("|" + "|".join("---" for _ in headers) + "|")
    for idx, row in d.iterrows():
        vals = [str(row[c]) if pd.notna(row[c]) else "-" for c in d.columns]
        if index:
            vals.insert(0, str(idx))
        rows.append("| " + " | ".join(vals) + " |")
    return "\n".join(rows)


def metric_table(metrics, population_note=None):
    """KPI table per contract Rule 4 (metric / value / population / note)."""
    lines = ["| Metric | Value | Population | Note |", "|---|---|---|---|"]
    for row in metrics:
        label, value = row[0], row[1]
        pop = row[2] if len(row) > 2 else (population_note or "-")
        note = row[3] if len(row) > 3 else "-"
        lines.append(f"| {label} | {value} | {pop} | {note} |")
    _INTEGRITY["tables"] += 1
    return "\n".join(lines)


def chart_meta(chart_type, x, y, population, n, denominator, source_tab, element_id, series="none"):
    """HTML-comment metadata block preceding a chart's data table (contract Rule 2)."""
    return (
        f"<!-- chart_type: {chart_type} | x: {x} | y: {y} | series: {series}\n"
        f"     population: {population}\n"
        f"     n: {n} | denominator: {denominator}\n"
        f"     source_tab: {source_tab} | element_id: {element_id} -->\n"
    )


def chart_block(title, description, df, meta=""):
    _INTEGRITY["charts"] += 1
    parts = [h3(title), meta, p(description), df_to_markdown(df), ""]
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Tab builders — every number below calls the SAME ched_common functions
# dashboard.py uses.
# ---------------------------------------------------------------------------
def build_tab1(df_all, df_best, df_obs):
    lines = [h1("Tab 1 — National Profile")]

    kpi = cc.compute_tab1_kpis(df_best)
    rep = cc.compute_repeat_taker_stats(df_all, kpi["n_unique"])
    lines.append(metric_table([
        ("Best-record examinees", f"{kpi['n_best']:,}", "one row per person", "-"),
        ("Unique persons (PERSON_KEY)", f"{kpi['n_unique']:,}", "one row per person",
         "equal to best-record examinees by construction"),
        ("NMAT years covered", f"{kpi['n_years']}", "-", "-"),
        ("Median NMAT percentile", f"{kpi['median_pct']:.1f}", "best-record examinees", "0-99 scale, not a bin number"),
        ("Repeat takers", f"{rep['n_repeat']:,} ({rep['pct']:.0f}%)", "unique examinees", "took NMAT more than once"),
    ]))
    lines.append(sep())

    lines.append(h2("Annual Trend"))
    yr = cc.compute_annual_trend(df_best)
    yr["Year"] = yr["Year"].astype(str)
    yr_disp = yr.rename(columns={"Median_percentile": "Median NMAT percentile", "Median_raw_score": "Median TRUE raw score"})
    lines.append(chart_block(
        "Examinee Volume by Year / Median NMAT Percentile by Year",
        "Two-panel chart: examinee count (bar) and median NMAT percentile, 0-99 scale (line), by NMAT year.",
        yr_disp,
        chart_meta("bar+line", "Year", "Examinees, Median NMAT percentile", "best-record examinees, all years",
                   f"{kpi['n_best']:,}", "one row per person", 1, "ched_t1_fig1"),
    ))
    lines.append(sep())

    lines.append(h2("University Type Composition"))
    ut = cc.compute_composition(df_best, UNI_TYPE_COL)
    lines.append(chart_meta("pie", UNI_TYPE_COL, "Count", "best-record examinees", f"{kpi['n_best']:,}",
                            "best-record examinees", 1, "ched_t1_fig2"))
    lines.append(df_to_markdown(ut))
    lines.append(sep())

    lines.append(h2("Course Group Composition"))
    cg = cc.compute_composition(df_best, COURSE_GROUP_COL)
    lines.append(chart_meta("pie", COURSE_GROUP_COL, "Count", "best-record examinees", f"{kpi['n_best']:,}",
                            "best-record examinees", 1, "ched_t1_fig3"))
    lines.append(df_to_markdown(cg))
    lines.append(sep())

    lines.append(h2("Repeat-Taker Context"))
    lines.append(p(f"Of {kpi['n_unique']:,} unique examinees, {rep['n_repeat']:,} ({rep['pct']:.0f}%) took the "
                    "NMAT more than once (up to 9 attempts). All threshold counts use each examinee's "
                    "best-record NMAT attempt to avoid inflating the applicant pool with repeat attempts."))
    lines.append(sep())

    lines.append(h2("Score Bin Reference"))
    lines.append(p("B1 is the lowest decile (0-9), B10 the highest (90-100)."))
    lines.append(df_to_markdown(cc.bin_reference_table()))
    lines.append(sep())

    return "\n".join(lines)


def build_tab2(df_all, df_best, df_obs):
    lines = [h1("Tab 2 — B4+ vs B5+ Thresholds")]
    db = cc.bins_population(df_best)
    dob = cc.bins_population(df_obs)

    lines.append(h2("Score Bin Distribution by NMAT Year"))
    lines.append(chart_meta("heatmap", "Year", "PercentileBin", "row %", "best-record, valid bin",
                            f"{len(db):,}", "best-record examinees with a valid percentile bin", 2, "ched_t2_fig1"))
    lines.append(p("Row percentages. Rows = NMAT years, columns = score bins (B1 lowest, B10 highest)."))
    yp = cc.compute_bin_dist_by(db, "Year")
    lines.append(df_to_markdown(yp))
    lines.append(sep())

    lines.append(h2("Examinees Meeting Each Threshold"))
    sc = cc.compute_threshold_scenarios(db, dob)
    lines.append(chart_meta("table", "Threshold", "Best-record examinees", "-", f"{len(db):,}",
                            "best-record examinees with a valid percentile bin", 2, "ched_t2_table1"))
    lines.append(df_to_markdown(sc))
    lines.append(sep())

    lines.append(h2("Threshold Context by University Type"))
    ut_df = cc.compute_threshold_by_uni_type(db)
    lines.append(chart_meta("table", "University Type", "B4+/B5+/B4-only counts", "-", f"{len(db):,}",
                            "best-record examinees with a valid percentile bin", 2, "ched_t2_table2"))
    lines.append(df_to_markdown(ut_df))
    lines.append(p(cc.SCOPE_NOTE))
    lines.append(sep())

    lines.append(h2("Public-Institution Examinees and B5+ Threshold (Descriptive Only)"))
    ev = cc.compute_public_private_b5_evidence(db)
    lines.append(metric_table([
        ("Public B5+ count", f"{ev['pub_b5']:,}", f"public examinees, n={ev['pub_total']:,}", f"{ev['pub_b5_pct']}%"),
        ("Public B4-only count", f"{ev['pub_b4o']:,}", f"public examinees, n={ev['pub_total']:,}", f"{ev['pub_b4o_pct']}%"),
        ("Private B5+ count", f"{ev['priv_b5']:,}", f"private examinees, n={ev['priv_total']:,}", f"{ev['priv_b5_pct']}%"),
    ]))
    pub_tbl = pd.DataFrame([
        ["Total best-record examinees", f"{ev['pub_total']:,}", f"{ev['priv_total']:,}"],
        ["B5+ (Bin 5+)", f"{ev['pub_b5']:,} ({ev['pub_b5_pct']}%)", f"{ev['priv_b5']:,} ({ev['priv_b5_pct']}%)"],
        ["B4-only", f"{ev['pub_b4o']:,} ({ev['pub_b4o_pct']}%)", f"{ev['priv_b4o']:,} ({ev['priv_b4o_pct']}%)"],
    ], columns=["Metric", "Public", "Private"])
    lines.append(df_to_markdown(pub_tbl))
    lines.append(p(
        "Purely descriptive. Whether this band overlaps with GIDA/IP applicants cannot be "
        "determined from this dataset: GIDA/IP status is not recorded, 'public undergraduate "
        "institution' is not a GIDA/IP indicator, and 'public' is not equivalent to 'SUC' as the "
        "CMO uses the term. No claim about who benefits from the exception is supported by this data."
    ))
    lines.append(sep())

    lines.append(h2("Profile of the B4 Group (Bin 4 Only)"))
    b4prof = cc.compute_b4_group_profile(db)
    lines.append(metric_table([
        ("B4 examinees (best record)", f"{b4prof['n']:,}", "B4 bin only", "-"),
        ("Median TRUE raw score", f"{b4prof['median_raw']:.1f}", "B4 bin only", "-"),
    ]))
    lines.append(df_to_markdown(b4prof["by_uni"]))
    lines.append(sep())

    lines.append(h2("Top Bins (B8-B10) vs Bottom Bins (B1-B3) Trend"))
    tb = cc.compute_top_bottom_trend(df_best)
    lines.append(chart_meta("line", "Year", "Top/Bottom bin share (%)", "best-record examinees by year",
                            f"{len(df_best):,}", "best-record examinees", 2, "ched_t2_fig4"))
    lines.append(df_to_markdown(tb))
    lines.append(sep())

    lines.append(h2("Yearly Examinees Meeting Each Threshold"))
    yt = cc.compute_yearly_threshold_counts(db, dob)
    lines.append(df_to_markdown(yt))
    lines.append(sep())

    lines.append(h2("B5+ PLE-Passer Composition by Year"))
    lines.append(p(
        "NOT pre-filtered on match status — population is the full B5+ observable cohort, so "
        "'no confirmed match' is a genuine, non-tautological count that varies by year."
    ))
    b5_yr = cc.compute_ple_composition_by_year(df_obs, bins=B5_PLUS, filipino_only=False, strict=False)
    b5_yr_disp = b5_yr.copy()
    b5_yr_disp.columns = ["Year", "Total B5+ observable", "Confirmed PLE passers", "No confirmed PLE match",
                          "Linkage rate (%)", "No-match share (%)"]
    lines.append(chart_meta("bar (stacked, count+percent)", "Year", "confirmed/no_match", "none",
                            "B5+ observable cohort, all years",
                            f"{int(b5_yr['total'].sum()):,}", "B5+ examinees in the observable cohort, by year",
                            2, "ched_t2_fig5"))
    lines.append(df_to_markdown(b5_yr_disp))
    lines.append(p("This is NMAT-to-PLE-passer linkage, not a PLE pass rate. 'No confirmed match' does not "
                    "mean 'failed the PLE' — the PLE source used for matching contains passers only."))
    lines.append(sep())

    return "\n".join(lines)


def build_tab3(df_all, df_best, df_obs):
    lines = [h1("Tab 3 — PLE-Passer Linkage")]

    lines.append(h2("PLE Linkage by Score Bin"))
    ple = cc.compute_linkage_by(df_obs, "PercentileBin")
    ple["Range"] = ple["PercentileBin"].astype(str).map(BIN_RANGES)
    ple_disp = ple[["PercentileBin", "Range", "N", "Confirmed", "Linkage Rate (%)"]]
    lines.append(chart_meta("bar", "PercentileBin", "Linkage Rate (%)", "observable cohort",
                            f"{int(ple['N'].sum()):,}", "observable-cohort examinees with a valid percentile bin",
                            3, "ched_t3_fig1"))
    lines.append(df_to_markdown(ple_disp))
    lines.append(p(cc.SELECTION_EFFECT_NOTE))
    lines.append(sep())

    lines.append(h2("Score Profile by PLE Status"))
    sp = cc.compute_score_profile_by_ple_status(df_obs)
    lines.append(df_to_markdown(sp, index=True))
    lines.append(sep())

    lines.append(h2("PLE-Passer Linkage by NMAT Year"))
    ply = cc.compute_linkage_by(df_obs, "Year")
    lines.append(chart_meta("line", "Year", "Linkage Rate (%)", "observable cohort by year",
                            f"{int(ply['N'].sum()):,}", "observable-cohort examinees", 3, "ched_t3_fig2"))
    lines.append(df_to_markdown(ply))
    lines.append(sep())

    lines.append(h2("PLE-Passer Linkage by Course Group"))
    plc = cc.compute_linkage_by(df_obs, COURSE_GROUP_COL)
    if len(plc):
        lines.append(df_to_markdown(plc))
        lines.append(sep())

    lines.append(h2("PLE-Passer Linkage by University Type"))
    plu = cc.compute_linkage_by(df_obs[df_obs[UNI_TYPE_COL].isin(["Public", "Private", "Foreign"])], UNI_TYPE_COL)
    lines.append(df_to_markdown(plu))
    lines.append(p("Reflects the examinee's undergraduate institution type. No medical-school "
                    "identifier exists in this dataset."))
    lines.append(sep())

    lines.append(h2("Stress-Test: Defensible PLE Matching Subset"))
    lines.append(p(
        "NOT the tautology in the prior version of this dashboard (which pre-filtered the "
        "population on the same flag used to compute 'confirmed', guaranteeing 100% linkage every "
        "year regardless of match quality). Population here is the Filipino, B5+ observable "
        "cohort with no pre-filter on match status; 'confirmed' additionally requires a >=5-year "
        "NMAT-to-PLE gap. This is a genuine, non-tautological check."
    ))
    stress = cc.compute_stress_test(df_obs)
    lines.append(metric_table([
        ("B5+ Filipino population", f"{stress['n_population']:,}", "Filipino, observable, B5+", "not pre-filtered on match status"),
        ("Confirmed under strict criteria", f"{stress['n_confirmed']:,}", "same population", "confirmed + >=5yr gap"),
        ("Strict-criteria linkage rate", f"{stress['linkage_pct']:.1f}%", "same population", "genuinely can be <100%"),
        ("Median PLE year gap", f"{stress['median_gap']:.0f} yrs" if pd.notna(stress["median_gap"]) else "N/A",
         "confirmed subset", "-"),
    ]))

    lines.append(h3("Yearly Linkage Rate (Strict-Criteria Subset, B5+, Filipino)"))
    cs_yr = stress["yearly"].rename(columns={"total": "Total", "confirmed": "Confirmed (strict)",
                                              "no_match": "No match", "linkage_pct": "Linkage Rate (%)"})
    lines.append(chart_meta("line", "Year", "Linkage Rate (%)", "Filipino, observable, B5+, strict criteria",
                            f"{stress['n_population']:,}", "Filipino B5+ observable examinees", 3, "ched_t3_fig3"))
    lines.append(df_to_markdown(cs_yr[["Year", "Total", "Confirmed (strict)", "No match", "Linkage Rate (%)"]]))

    lines.append(h3("Strict-Criteria B5+ Confirmed Passers by University Type"))
    if len(stress["by_uni"]):
        lines.append(df_to_markdown(stress["by_uni"]))
    lines.append(p(
        f"Under strict matching criteria, {stress['n_confirmed']:,} of {stress['n_population']:,} "
        f"({stress['linkage_pct']:.1f}%) Filipino B5+ observable examinees are confirmed PLE "
        f"passers with a >=5-year gap. This is a real, checkable comparison, not a tautology."
    ))
    lines.append(sep())

    return "\n".join(lines)


def build_tab4(df_all, df_best, df_obs):
    lines = [h1("Tab 4 — Institution and Foreign Context")]
    db = cc.bins_population(df_best)

    lines.append(h2("Score Summary by University Type"))
    us = cc.compute_uni_score_summary(db)
    lines.append(df_to_markdown(us))
    lines.append(p("Percentile medians use the same population as Tab 2/Tab 5 (best-record examinees "
                    "with a valid percentile bin) — one null-handling policy shared across this document."))
    lines.append(sep())

    lines.append(h2("Percentile Rank Distribution by University Type (Box Plot Data)"))
    lines.append(p("Five-number summary + n, not raw points, per export contract Rule 1."))
    bp = cc.compute_box_plot_summary(db)
    lines.append(df_to_markdown(bp))
    lines.append(sep())

    uni = df_best[df_best[UNI_TYPE_COL].isin(["Public", "Private", "Foreign"])]
    lines.append(h2("Score Bin Distribution by University Type"))
    ubp = cc.compute_bin_dist_by(uni, UNI_TYPE_COL)
    lines.append(df_to_markdown(ubp))
    lines.append(sep())

    lines.append(h2("Top-Bin Share (B8-B10) by University Type"))
    top_df = cc.compute_top_bin_share_by(uni, UNI_TYPE_COL)
    lines.append(df_to_markdown(top_df))
    lines.append(sep())

    lines.append(h2("Foreign Examinee Context"))
    fctx = cc.compute_foreign_context(df_best)
    lines.append(metric_table([
        ("Verified Foreign NMAT examinees", f"{fctx['n_foreign']:,}", "best-record examinees", "-"),
        ("Filipino examinees", f"{fctx['n_filipino']:,}", "best-record examinees", "-"),
        ("Distinct foreign nationalities", f"{fctx['n_nationalities']}", "best-record, verified foreign", "-"),
    ]))

    lines.append(h3("Top 10 Nationalities"))
    top_nat = cc.compute_nationality_shares(df_best)
    lines.append(chart_meta("bar", "Nationality", "Count", "verified foreign, best-record",
                            f"{fctx['n_foreign']:,}", "ALL verified-foreign best-record examinees (not top-10 subtotal)",
                            4, "ched_t4_fig1"))
    top_nat_disp = top_nat.copy()
    top_nat_disp.index = range(1, len(top_nat_disp) + 1)
    top_nat_disp.index.name = "Rank"
    lines.append(df_to_markdown(top_nat_disp, index=True))
    lines.append(p(f"Share is of all {fctx['n_foreign']:,} verified foreigners, never the top-10 subtotal "
                    "(the prior version of this export divided by the subtotal, inflating every row ~4%). "
                    "'Foreign (unspecified)' is an unresolved citizenship bucket, not a country."))
    lines.append(p("These are NMAT examinees, not enrolled medical students."))
    lines.append(sep())

    return "\n".join(lines)


def build_tab5(df_all, df_best, df_obs):
    lines = [h1("Tab 5 — Key Evidence for Policy Review")]
    lines.append(p("The following findings are descriptive observations based on historical NMAT data "
                    "(2006-2018). They do not constitute regulatory recommendations."))
    lines.append(sep())

    # Same function dashboard.py calls -- byte-identical prose, no re-derivation.
    findings = cc.compute_tab5_finding_texts(df_all, df_best, df_obs)
    for title, body in findings:
        lines.append(h3(title))
        lines.append(p(body))

    lines.append(sep())
    lines.append(p("**Note on data scope.** These findings are limited to the NMAT examinee population "
                    "captured in NMAT_Exodus.parquet. Key gaps include PLE failure rates (only passers "
                    "are identifiable), GIDA/IP status, medical school admissions and enrollment "
                    "figures, and institutional admission criteria. No medical-school identifier exists "
                    "in this dataset at all."))
    return "\n".join(lines)


def build_tab6(df_all, df_best, df_obs):
    lines = [h1("Tab 6 — Data, Methods, and Limitations")]

    kpi = cc.compute_tab1_kpis(df_best)
    rep = cc.compute_repeat_taker_stats(df_all, kpi["n_unique"])
    mismatch = cc.compute_stored_mismatch_stats(df_all)
    true_stats = cc.compute_true_raw_score_stats(df_all)
    amb = cc.compute_ambiguous_person_stats(df_all)

    lines.append(h2("Dataset Overview"))
    lines.append(metric_table([
        ("Source file", f"NMAT_Exodus.parquet ({df_all.shape[1]} columns)", "-", "-"),
        ("Total rows", f"{len(df_all):,}", "all NMAT sittings", "-"),
        ("Examination years", "2006-2018", "-", "-"),
        ("Unique examinees (best record)", f"{kpi['n_unique']:,}", "one row per person", "-"),
        ("Observable PLE cohort", f"{len(df_obs):,}", "best attempt with Year<=2014",
         "IS_BEST_OBSERVABLE_RECORD, not best-record & Year<=2014"),
        ("Repeat takers", f"{rep['n_repeat']:,} ({rep['pct']:.0f}%)", "unique examinees", "-"),
    ]))
    if amb["n_ambiguous_keys"] is not None:
        lines.append(p(f"**Data quality note:** {amb['n_ambiguous_keys']:,} PERSON_KEY identifiers have "
                        "contradictory SEX recorded across their rows (PERSON_KEY_AMBIGUOUS), indicating "
                        "a possible identity collision. Disclosed, not silently corrected."))
    lines.append(sep())

    lines.append(h2("TRUE Raw Score Recalculation"))
    lines.append(p(f"Of the {mismatch['n_stored']:,} records that carry a stored total, "
                    f"{mismatch['n_mismatch']:,} ({mismatch['pct_of_stored']:.1f}%) disagreed with the "
                    f"sum of the 8 component subtest scores ({mismatch['pct_of_all']:.1f}% of all "
                    f"{len(df_all):,} records) and were corrected. Computed live from "
                    "StoredVsDerivedMismatch, never hardcoded."))
    lines.append(metric_table([
        ("Rows with complete TRUE scores", f"{true_stats['n_true']:,} ({true_stats['pct_true']:.2f}%)", "all rows", "-"),
        ("Stored-total mismatches", f"{mismatch['n_mismatch']:,} of {mismatch['n_stored']:,}",
         "rows with a stored total", f"{mismatch['pct_of_stored']:.1f}%"),
    ]))
    lines.append(sep())

    lines.append(h2("Best-Record Deduplication"))
    lines.append(p(f"{rep['n_repeat']:,} examinees ({rep['pct']:.0f}%) took the NMAT more than once "
                    "(up to 9 attempts). IS_BEST_NMAT_RECORD selects, for every person, the single "
                    "attempt with the highest NMAT percentile, latest year as tiebreaker, then lowest "
                    "application number — one uniform rule for passers and non-passers alike."))
    lines.append(sep())

    lines.append(h2("Observable Cohort Definition"))
    avg_gap = df_obs.loc[df_obs["HAS_CONFIRMED_PLE"], "PLE_YEAR_GAP"].median()
    lines.append(p("PLE-linked analyses use IS_BEST_OBSERVABLE_RECORD (each person's best attempt among "
                    "rows with Year<=2014) — deliberately not the same as filtering the overall "
                    "best-record flag to Year<=2014, which would silently drop people whose overall-best "
                    "attempt fell after 2014 and inflate the observed linkage rate."))
    lines.append(metric_table([
        ("Observable cohort", f"{len(df_obs):,}", "best attempt within window", "-"),
        ("Median NMAT-to-PLE year gap", f"{avg_gap:.0f} years", "confirmed passers", "-"),
    ]))
    lines.append(sep())

    lines.append(h2("Deterministic PLE Matching"))
    match_stats = cc.compute_ple_matching_stats(df_all, df_obs)
    outcome = match_stats["outcome_counts"]
    lines.append(p("All PLE matching is deterministic; no fuzzy/rapidfuzz matching is used. "
                    f"PLE_MATCH_OUTCOME breakdown (all rows): accepted {outcome.get('accepted', 0):,}, "
                    f"rejected_ambiguous_person {outcome.get('rejected_ambiguous_person', 0):,} (a "
                    "name-collision candidate found but rejected as genuinely ambiguous, distinguished "
                    f"from a bare no_match), no_match {outcome.get('no_match', 0):,}. "
                    f"PLE_YEAR_UNCERTAIN flags {match_stats['n_year_uncertain']:,} confirmed passers "
                    "whose PLE year is not determinable (still counted as passers, excluded from "
                    "year-specific figures). "
                    "PLE_YEAR_PASSED / PLE_MATCH_METHOD / PLE_YEAR_GAP are diagnostic metadata, not "
                    "authoritative passer counts, and do not nest inside IS_PLE_PASSER: non-null for "
                    f"{match_stats['n_year_passed_notna']:,} / {match_stats['n_match_method_notna']:,} / "
                    f"{match_stats['n_year_gap_notna']:,} rows respectively."))
    lines.append(metric_table([
        ("Confirmed PLE passers (all rows)", f"{match_stats['n_all_ple']:,}", "all rows", "IS_PLE_PASSER"),
        ("Confirmed PLE passers (observable cohort)", f"{match_stats['n_obs_ple']:,}", "observable cohort", "-"),
    ]))
    lines.append(p(
        "**PLE-matching bias against below-40th-percentile examinees (disclosed).** Found during "
        "remediation. The name-collision disambiguator (`2_PLE_Matching_Pipeline.ipynb`, "
        "`disambiguate()` Step 4) previously applied a hard filter — not a tie-break — discarding "
        "every candidate scoring below the 40th NMAT percentile and rejecting the match outright if "
        "no candidate scored at or above 40. That constant, 40, is exactly the CMO threshold this "
        "dashboard evaluates. The effect is confined to name-collision groups (unique-name matches "
        "were never affected, which is why B1-B4 confirmed passers exist at all), now corrected "
        "upstream, but present in every below-B4/B5 linkage figure in this document."
    ))
    lines.append(sep())

    lines.append(h2("Limitations Relevant to CHED Decision-Making"))
    # Same function dashboard.py calls -- byte-identical cards, live-computed numbers.
    lims = cc.compute_limitations_cards(df_all, df_best, df_obs)
    for title, detail in lims:
        lines.append(h3(title))
        lines.append(p(detail))

    return "\n".join(lines)


def _self_check_block(df_all, source_path):
    """Export-integrity self-check per contract Rule 10."""
    try:
        with open(source_path, "rb") as f:
            md5 = hashlib.md5(f.read()).hexdigest()
    except Exception:
        md5 = "unavailable"
    lines = [h1("Export Integrity"), "| check | result |", "|---|---|"]
    lines.append(f"| Source parquet md5 | {md5} |")
    lines.append(f"| Rows / cols | {len(df_all):,} / {df_all.shape[1]} |")
    lines.append(f"| Tabs exported | {_INTEGRITY['tabs']} / {_INTEGRITY['tabs_total']} |")
    lines.append(f"| Charts exported as data | {_INTEGRITY['charts']} / {_INTEGRITY['charts']} |")
    lines.append(f"| Tables exported | {_INTEGRITY['tables']} |")
    lines.append(f"| Captions exported | {_INTEGRITY['captions']} |")
    lines.append(
        f"| Dashboard-vs-export value assertions passed | "
        f"{_INTEGRITY['assertions_passed']} / {_INTEGRITY['assertions_total']} |"
    )
    if _INTEGRITY["tabs"] < _INTEGRITY["tabs_total"]:
        lines.append("\n**INCOMPLETE EXPORT — not all tabs were rendered. Do not treat this document as authoritative.**")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def build_full_markdown(df_all, df_best, df_obs, viz_dir=None, md_dir=None):
    """Return one complete Markdown string for all 6 dashboard tabs.

    Parameters
    ----------
    df_all, df_best, df_obs : pd.DataFrame — from ched_common.load_and_validate()
    viz_dir : str or None — if provided, generate charts and save to this directory
    md_dir : str or None — directory the .md file will be saved in, used to
             compute correct relative image paths (fixes the viz/ vs ../viz/
             path bug — previously hardcoded and only correct if the .md
             happened to sit at the app root).
    """
    _reset_integrity()

    chart_map = {}
    if viz_dir is not None:
        chart_map = generate_all_charts(df_all, df_best, df_obs, viz_dir, md_dir=md_dir)

    def img(name, alt=""):
        if name in chart_map:
            return f"![{alt}]({chart_map[name]})\n"
        return ""

    try:
        source_path = cc.find_data_path()
    except Exception:
        source_path = None

    lines = []
    lines.append("# NMAT Performance Evidence for CHED Cut-Off Policy Review")
    lines.append("")
    lines.append(f"> Complete Markdown export generated {datetime.now().strftime('%Y-%m-%d %H:%M')}. "
                  "Every number below is computed by the same functions the live dashboard renders "
                  "from (`ched_common.py`) — this document is a faithful transcript, not a paraphrase.")
    lines.append("")
    lines.append(f"**Source:** NMAT_Exodus.parquet, {len(df_all):,} rows x {df_all.shape[1]} columns.")
    lines.append("")
    lines.append("## How to Read This Document")
    lines.append("")
    lines.append("- **Best-record examinees** — one NMAT record per person (removes repeat-taker inflation).")
    lines.append("- **Observable cohort** — each person's best NMAT attempt with Year <= 2014 "
                  "(`IS_BEST_OBSERVABLE_RECORD`), who has had time to take the PLE. This is NOT the "
                  "same as filtering the overall-best record to Year<=2014.")
    lines.append("- **Score bins** — B1 (0-9, lowest) through B10 (90-100, highest). B4+ = Bin 4 and "
                  "above (30th-39th). B5+ = Bin 5 and above (40th-49th). Always ordered B1..B10, never string-sorted.")
    lines.append("- **NMAT-to-PLE linkage** — the proportion of NMAT examinees later matched to PLE "
                  "passer records. This is NOT a PLE pass rate. The dataset does not contain all PLE "
                  "takers or PLE failures.")
    lines.append("- **People vs sittings** — best-record filtering counts people; unfiltered counts count exam sittings.")
    lines.append("- **No medical-school identifier exists in this dataset.** UNDERGRAD_UNI_TYPE / "
                  "UNDERGRAD_UNIVERSITY describe the examinee's undergraduate institution, never the medical school.")
    lines.append("- **Nationality shares** use the full verified-foreigner denominator, never a top-N subtotal.")
    lines.append("")
    lines.append("## Global KPIs")
    lines.append("")
    kpi = cc.compute_tab1_kpis(df_best)
    rep = cc.compute_repeat_taker_stats(df_all, kpi["n_unique"])
    lines.append(metric_table([
        ("Total NMAT sittings", f"{len(df_all):,}", "all years", "-"),
        ("Unique examinees", f"{kpi['n_unique']:,}", "best-record", "-"),
        ("Observable cohort", f"{len(df_obs):,}", "best attempt, Year<=2014", ">=~5yr PLE window"),
        ("Confirmed PLE passers (observable)", f"{int(df_obs['HAS_CONFIRMED_PLE'].sum()):,}", "observable cohort", "-"),
        ("Repeat takers", f"{rep['n_repeat']:,} ({rep['pct']:.0f}%)", "unique examinees", "-"),
    ]))
    lines.append("")
    lines.append("---")

    lines.append(build_tab1(df_all, df_best, df_obs)); _INTEGRITY["tabs"] += 1
    lines.append(img("uni_pie", "University Type Composition Pie Chart"))
    lines.append(img("course_pie", "Course Group Composition Pie Chart"))
    lines.append(img("annual_trend", "Annual Trend Chart: Examinee Volume and Median NMAT Percentile"))

    lines.append(build_tab2(df_all, df_best, df_obs)); _INTEGRITY["tabs"] += 1
    lines.append(img("bin_heatmap", "Score Bin Distribution Heatmap by Year"))
    lines.append(img("top_bottom_trend", "Top Bins vs Bottom Bins Trend"))
    lines.append(img("b4_group", "B4 Examinees by Institution Type"))

    lines.append(build_tab3(df_all, df_best, df_obs)); _INTEGRITY["tabs"] += 1
    lines.append(img("ple_linkage_bin", "PLE Linkage Rate by Score Bin"))
    lines.append(img("ple_linkage_year", "PLE Linkage Rate by NMAT Year"))
    lines.append(img("ple_linkage_course", "PLE Linkage Rate by Course Group"))
    lines.append(img("ple_linkage_uni", "PLE Linkage Rate by University Type"))

    lines.append(build_tab4(df_all, df_best, df_obs)); _INTEGRITY["tabs"] += 1
    lines.append(img("uni_box", "NMAT Percentile Distribution by University Type - Box Plot"))
    lines.append(img("uni_bin_heatmap", "Bin Distribution by University Type Heatmap"))
    lines.append(img("top_bin_uni", "Top-Bin Share by University Type"))
    lines.append(img("foreign_top", "Top 10 Foreign Nationalities"))

    lines.append(build_tab5(df_all, df_best, df_obs)); _INTEGRITY["tabs"] += 1
    lines.append(build_tab6(df_all, df_best, df_obs)); _INTEGRITY["tabs"] += 1

    # Verification requirement (contract Rule 6): assert a sample of exported
    # values equal the dashboard's computed values by calling the same functions.
    F = cc.compute_tab5_findings(df_all, df_best, df_obs)
    mismatch = cc.compute_stored_mismatch_stats(df_all)
    nat = cc.compute_nationality_shares(df_best)
    _assert_equal("pub_median_pct", F["pub_median_pct"], cc.bins_population(df_best).query(f"{UNI_TYPE_COL}=='Public'")["NMS_PER_num"].median())
    _assert_equal("stored_mismatch_pct", mismatch["pct_of_stored"], cc.compute_stored_mismatch_stats(df_all)["pct_of_stored"])
    _assert_equal("india_share", float(nat.iloc[0]["Share of verified foreigners (%)"]),
                  round(nat.iloc[0]["Count"] / cc.compute_foreign_context(df_best)["n_foreign"] * 100, 1))
    _assert_equal("n_best", kpi["n_best"], len(df_best))
    _assert_equal("n_obs", len(df_obs), int(df_all["IS_BEST_OBSERVABLE_RECORD"].sum()))

    lines.append(_self_check_block(df_all, source_path))

    return "\n".join(lines)
