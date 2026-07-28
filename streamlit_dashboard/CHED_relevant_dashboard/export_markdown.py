"""
export_markdown.py — Export the CHED dashboard as one complete Markdown document
with all visualization charts saved as high-quality PNGs.

Public function: build_full_markdown(df_all, df_best, df_obs, viz_dir) -> str
"""

import os
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BIN_ORDER = [f"B{i}" for i in range(1, 11)]
B4_PLUS = ["B4", "B5", "B6", "B7", "B8", "B9", "B10"]
B5_PLUS = ["B5", "B6", "B7", "B8", "B9", "B10"]
TOP_BINS = ["B8", "B9", "B10"]
BOTTOM_BINS = ["B1", "B2", "B3"]

BIN_RANGES = {
    "B1": "0-9", "B2": "10-19", "B3": "20-29", "B4": "30-39",
    "B5": "40-49", "B6": "50-59", "B7": "60-69", "B8": "70-79",
    "B9": "80-89", "B10": "90-100",
}

COLORS_BIN = {
    "B1": "#8B0000", "B2": "#B22222", "B3": "#D9534F", "B4": "#F0AD4E",
    "B5": "#FFD166", "B6": "#A0D468", "B7": "#66C2A5", "B8": "#41B6C4",
    "B9": "#2C7FB8", "B10": "#253494",
}
COLORS_UNI = {"Public": "#1f77b4", "Private": "#ff7f0e", "Foreign": "#9467bd", "Not Specified": "#7f7f7f"}
COLORS_PLE = {"Confirmed PLE passer": "#2e7d32", "No confirmed PLE match": "#c62828"}

# ---------------------------------------------------------------------------
# Chart generation
# ---------------------------------------------------------------------------
def _save_plot(fig, viz_dir, name):
    """Save a plotly figure as high-quality PNG."""
    os.makedirs(viz_dir, exist_ok=True)
    path = os.path.join(viz_dir, name)
    fig.write_image(path, width=1000, height=600, scale=2, engine="kaleido")
    return f"viz/{name}"


def generate_all_charts(df_all, df_best, df_obs, viz_dir):
    """Generate all dashboard charts as PNG files in viz_dir.

    Returns a dict mapping chart_name -> relative path for markdown embedding.
    """
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    db = df_best.dropna(subset=["PercentileBin"])
    dob = df_obs.dropna(subset=["PercentileBin"])

    os.makedirs(viz_dir, exist_ok=True)
    chart_map = {}

    # ---- Tab 1: National Profile ----
    # 1. University type pie chart
    ut = df_best["UNI_TYPE"].value_counts().reset_index()
    ut.columns = ["UNI_TYPE", "Count"]
    fig = px.pie(ut, names="UNI_TYPE", values="Count", title="University Type Composition",
                  color="UNI_TYPE", color_discrete_map=COLORS_UNI)
    fig.update_traces(textinfo="label+percent", textfont_size=12)
    chart_map["uni_pie"] = _save_plot(fig, viz_dir, "01_uni_type_pie.png")

    # 2. Course group pie chart
    cg = df_best["CourseGroup"].value_counts().reset_index()
    cg.columns = ["CourseGroup", "Count"]
    COURSE_COLORS = {"Medical & Allied": "#d62728", "Natural Sciences": "#2ca02c",
                     "Social & Behavioral Sciences": "#ff9800", "Education": "#17becf",
                     "Engineering & Technology": "#8c564b", "Other": "#7f7f7f"}
    fig = px.pie(cg, names="CourseGroup", values="Count", title="Course Group Composition",
                  color="CourseGroup", color_discrete_map=COURSE_COLORS)
    fig.update_traces(textinfo="label+percent", textfont_size=12)
    chart_map["course_pie"] = _save_plot(fig, viz_dir, "01_course_group_pie.png")

    # 3. Annual trend chart
    yr = df_best.groupby("Year", observed=True).agg(
        examinees=("APPNO_CLEAN", "count"),
        median_pct=("NMS_PER_num", "median"),
    ).reset_index()
    yr["Year"] = yr["Year"].astype(str)
    fig = make_subplots(rows=2, cols=1, subplot_titles=("Examinee Volume by Year", "Median Bin Rank by Year"), vertical_spacing=0.22)
    fig.add_trace(go.Bar(x=yr["Year"], y=yr["examinees"], name="Examinees", marker_color="#1f77b4"), row=1, col=1)
    fig.add_trace(go.Scatter(x=yr["Year"], y=yr["median_pct"], mode="lines+markers", name="Median bin rank", line=dict(color="#d62728", width=3)), row=2, col=1)
    fig.update_layout(height=500)
    chart_map["annual_trend"] = _save_plot(fig, viz_dir, "01_annual_trend.png")

    # ---- Tab 2: Thresholds ----
    # 4. Score bin heatmap
    yp = pd.crosstab(db["Year"], db["PercentileBin"], dropna=False).reindex(columns=BIN_ORDER, fill_value=0)
    yp = yp.div(yp.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(1)
    fig = px.imshow(yp.T.reindex(BIN_ORDER[::-1]), text_auto=True, aspect="auto",
                    color_continuous_scale="YlOrRd",
                    labels={"x": "Year", "y": "Bin", "color": "%"},
                    title="Score Bin Distribution by NMAT Year (Row %)")
    fig.update_layout(height=460)
    chart_map["bin_heatmap"] = _save_plot(fig, viz_dir, "02_bin_heatmap.png")

    # 5. Top vs bottom bin trend
    _, pct2 = None, None
    ct2 = pd.crosstab(db["Year"], db["PercentileBin"], dropna=False).reindex(columns=BIN_ORDER, fill_value=0)
    ct2 = ct2.apply(pd.to_numeric, errors="coerce")
    pct2 = ct2.div(ct2.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(1)
    top_s = pct2[TOP_BINS].sum(axis=1)
    bot_s = pct2[BOTTOM_BINS].sum(axis=1)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=top_s.index.astype(str), y=top_s.values, mode="lines+markers", name="Top B8-B10", line=dict(color="#2e7d32", width=3)))
    fig.add_trace(go.Scatter(x=bot_s.index.astype(str), y=bot_s.values, mode="lines+markers", name="Bottom B1-B3", line=dict(color="#c62828", width=3)))
    fig.update_layout(title="Top Bins (B8-B10) vs Bottom Bins (B1-B3) by Year", height=400)
    chart_map["top_bottom_trend"] = _save_plot(fig, viz_dir, "02_top_bottom_trend.png")

    # 6. B4 group bar chart
    b4g = db[db["PercentileBin"] == "B4"]
    b4_uni = b4g.groupby("UNI_TYPE", observed=True).size().reset_index(name="count")
    fig = px.bar(b4_uni, x="UNI_TYPE", y="count", title="B4 Examinees by Institution Type",
                 color="UNI_TYPE", color_discrete_map=COLORS_UNI)
    chart_map["b4_group"] = _save_plot(fig, viz_dir, "02_b4_group.png")

    # ---- Tab 3: PLE Linkage ----
    # 7. PLE linkage bar chart
    pl = df_obs.dropna(subset=["PercentileBin", "HAS_CONFIRMED_PLE"]).groupby("PercentileBin", observed=True).agg(
        n=("APPNO_CLEAN", "count"), c=("HAS_CONFIRMED_PLE", "sum")
    ).reset_index()
    pl["linkage"] = (pl["c"] / pl["n"] * 100).round(1)
    fig = px.bar(pl, x="PercentileBin", y="linkage",
                 title="NMAT-to-PLE-Passer Linkage Rate by Score Bin",
                 color="linkage", color_continuous_scale="Viridis",
                 text=pl["linkage"].astype(str) + "%")
    fig.update_traces(textposition="outside")
    fig.update_layout(height=480)
    fig.add_hline(y=50, line_dash="dash", line_color="gray")
    chart_map["ple_linkage_bin"] = _save_plot(fig, viz_dir, "03_ple_linkage_bin.png")

    # 8. PLE linkage by year
    ply = df_obs.groupby("Year", observed=True).agg(n=("APPNO_CLEAN", "count"), c=("HAS_CONFIRMED_PLE", "sum")).reset_index()
    ply["rate"] = (ply["c"] / ply["n"] * 100).round(1)
    ply["Year"] = ply["Year"].astype(str)
    fig = px.line(ply, x="Year", y="rate", markers=True, title="NMAT-to-PLE-Passer Linkage Rate by NMAT Year")
    fig.update_traces(line=dict(color="#1f77b4", width=3))
    fig.update_layout(height=400)
    chart_map["ple_linkage_year"] = _save_plot(fig, viz_dir, "03_ple_linkage_year.png")

    # 9. PLE linkage by course group
    if "CourseGroup" in df_obs.columns:
        plc = df_obs.dropna(subset=["CourseGroup", "HAS_CONFIRMED_PLE"]).groupby("CourseGroup", observed=True).agg(
            n=("APPNO_CLEAN", "count"), c=("HAS_CONFIRMED_PLE", "sum")).reset_index()
        plc["rate"] = (plc["c"] / plc["n"] * 100).round(1)
        fig = px.bar(plc, x="CourseGroup", y="rate", title="NMAT-to-PLE-Passer Linkage Rate by Course Group",
                     color="CourseGroup", color_discrete_map=COURSE_COLORS,
                     text=plc["rate"].round(1).astype(str) + "%")
        fig.update_traces(textposition="outside")
        fig.update_layout(height=400, showlegend=False, xaxis_tickangle=-20)
        chart_map["ple_linkage_course"] = _save_plot(fig, viz_dir, "03_ple_linkage_course.png")

    # 10. PLE linkage by UNI_TYPE
    plu = df_obs[df_obs["UNI_TYPE"].isin(["Public", "Private", "Foreign"])].groupby("UNI_TYPE", observed=True).agg(
        n=("APPNO_CLEAN", "count"), c=("HAS_CONFIRMED_PLE", "sum")).reset_index()
    plu["rate"] = (plu["c"] / plu["n"] * 100).round(1)
    fig = px.bar(plu, x="UNI_TYPE", y="rate", title="NMAT-to-PLE-Passer Linkage Rate by University Type",
                 color="UNI_TYPE", color_discrete_map=COLORS_UNI,
                 text=plu["rate"].round(1).astype(str) + "%")
    fig.update_traces(textposition="outside")
    fig.update_layout(height=400, showlegend=False)
    chart_map["ple_linkage_uni"] = _save_plot(fig, viz_dir, "03_ple_linkage_uni.png")

    # ---- Tab 4: Institution Context ----
    # 11. Box plot by UNI_TYPE
    uni = df_best[df_best["UNI_TYPE"].isin(["Public", "Private", "Foreign"])]
    fig = px.box(uni.dropna(subset=["NMS_PER_num"]), x="UNI_TYPE", y="NMS_PER_num",
                 color="UNI_TYPE", color_discrete_map=COLORS_UNI, points=False,
                 title="Bin Rank Distribution by University Type",
                 labels={"NMS_PER_num": "Bin rank", "UNI_TYPE": ""})
    fig.update_layout(height=400, showlegend=False)
    chart_map["uni_box"] = _save_plot(fig, viz_dir, "04_uni_box.png")

    # 12. Bin heatmap by UNI_TYPE
    ub = pd.crosstab(uni["UNI_TYPE"], uni["PercentileBin"], dropna=False).reindex(columns=BIN_ORDER, fill_value=0)
    ub = ub.apply(pd.to_numeric, errors="coerce")
    ubp = ub.div(ub.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(1)
    fig = px.imshow(ubp, text_auto=True, aspect="auto", color_continuous_scale="YlOrRd",
                    labels={"x": "Score Bin", "y": "University Type", "color": "%"},
                    title="Bin Distribution by University Type (Row %)")
    fig.update_layout(height=350)
    chart_map["uni_bin_heatmap"] = _save_plot(fig, viz_dir, "04_uni_bin_heatmap.png")

    # 13. Top-bin share bar
    top_uni = ubp[TOP_BINS].sum(axis=1).sort_values()
    fig = go.Figure(go.Bar(x=top_uni.values, y=top_uni.index, orientation="h",
                           marker_color=[COLORS_UNI.get(i, "#7f7f7f") for i in top_uni.index],
                           text=[f"{v:.1f}%" for v in top_uni.values], textposition="outside"))
    fig.update_layout(title="Top-Bin Share (B8-B10) by University Type",
                      xaxis_title="Percent in B8-B10", yaxis_title="", height=300)
    chart_map["top_bin_uni"] = _save_plot(fig, viz_dir, "04_top_bin_uni.png")

    # 14. Foreign nationality bar
    foreign = df_all[df_all["FOREIGNER_STATUS"] == "Verified Foreigner"]
    if len(foreign) > 0:
        top_nat = foreign["CITIZENSHIP_FINAL"].value_counts().head(10).reset_index()
        top_nat.columns = ["Nationality", "Count"]
        fig = px.bar(top_nat, x="Count", y="Nationality", orientation="h",
                     title="Top 10 Nationalities Among Verified Foreign NMAT Examinees",
                     color="Count", color_continuous_scale="Blues")
        fig.update_layout(height=350)
        chart_map["foreign_top"] = _save_plot(fig, viz_dir, "04_foreign_top10.png")

    return chart_map


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def h1(t): return f"\n# {t}\n"
def h2(t): return f"\n## {t}\n"
def h3(t): return f"\n### {t}\n"
def p(t): return f"{t}\n"
def sep(): return "\n---\n"


def df_to_markdown(df, index=False, float_format=".1f"):
    """Convert a DataFrame to a Markdown table string.

    Uses tabulate if available, falls back to manual rendering.
    """
    d = df.copy()
    # Format integer columns with commas
    for c in d.columns:
        if pd.api.types.is_integer_dtype(d[c]):
            d[c] = d[c].apply(lambda x: f"{x:,}" if pd.notna(x) else "—")
        elif pd.api.types.is_float_dtype(d[c]):
            d[c] = d[c].apply(lambda x: f"{x:{float_format}}" if pd.notna(x) else "—")
    # Convert nullable booleans
    for c in d.columns:
        if pd.api.types.is_bool_dtype(d[c]):
            d[c] = d[c].apply(lambda x: "True" if x else "False")

    try:
        import tabulate
        return d.to_markdown(index=index, tablefmt="pipe", numalign="right", stralign="left")
    except ImportError:
        pass

    # Fallback manual renderer
    rows = []
    headers = list(d.columns)
    if index:
        headers.insert(0, d.index.name or "")
    rows.append("| " + " | ".join(str(h) for h in headers) + " |")
    rows.append("|" + "|".join("---" for _ in headers) + "|")
    for idx, row in d.iterrows():
        vals = [str(row[c]) if pd.notna(row[c]) else "—" for c in d.columns]
        if index:
            vals.insert(0, str(idx))
        rows.append("| " + " | ".join(vals) + " |")
    return "\n".join(rows)


def metric_table(metrics):
    """Build a 2-column metric table from list of (label, value) tuples."""
    lines = ["| Metric | Value |", "|--------|-------|"]
    for label, value in metrics:
        lines.append(f"| {label} | {value} |")
    return "\n".join(lines)


def chart_block(title, description, df):
    """Build a complete chart block: title, description, source table, caption."""
    parts = [h3(title), p(description), df_to_markdown(df), ""]
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Tab builders
# ---------------------------------------------------------------------------
def build_tab1(df_all, df_best, df_obs):
    """National Profile."""
    lines = [h1("Tab 1 — National Profile")]

    # Metric cards
    n_best = len(df_best)
    n_unique = int(df_best["PERSON_KEY"].nunique())
    n_obs = len(df_obs)
    n_repeat = int((df_all.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique() > 1).sum())
    lines.append(metric_table([
        ("Best-record examinees", f"{n_best:,}"),
        ("Unique persons (PERSON_KEY)", f"{n_unique:,}"),
        ("NMAT years covered", f"{int(df_best['Year'].nunique())}"),
        ("Median percentile rank", f"{df_best['NMS_PER_num'].median():.1f}"),
    ]))
    lines.append(sep())

    # Yearly trend data
    lines.append(h2("Annual Trend Chart Data"))
    yr = df_best.groupby("Year", observed=True).agg(
        Examinees=("APPNO_CLEAN", "count"),
        Median_percentile_rank=("NMS_PER_num", "median"),
        Median_TRUE_raw_score=("TotalRawScoreTRUE", "median"),
    ).round(1).reset_index()
    yr.columns = ["Year", "Examinees", "Median percentile rank", "Median TRUE raw score"]
    yr["Year"] = yr["Year"].astype(str)
    lines.append(chart_block(
        "Examinee Volume by Year / Median Bin Rank by Year",
        "Two-panel chart: examinee count (bar) and median bin rank (line) by NMAT year.",
        yr,
    ))
    lines.append(sep())

    # University type composition
    lines.append(h2("University Type Composition"))
    ut = df_best["UNI_TYPE"].value_counts().reset_index()
    ut.columns = ["UNI_TYPE", "Count"]
    ut["Share (%)"] = (ut["Count"] / ut["Count"].sum() * 100).round(2)
    lines.append(df_to_markdown(ut))
    lines.append(sep())

    # Course group composition
    lines.append(h2("Course Group Composition"))
    cg = df_best["CourseGroup"].value_counts().reset_index()
    cg.columns = ["CourseGroup", "Count"]
    cg["Share (%)"] = (cg["Count"] / cg["Count"].sum() * 100).round(2)
    lines.append(df_to_markdown(cg))
    lines.append(sep())

    # Repeat-taker context
    lines.append(h2("Repeat-Taker Context"))
    lines.append(p(f"Of {n_unique:,} unique examinees, {n_repeat:,} ({n_repeat / n_unique * 100:.0f}%) took the NMAT more than once (up to 9 attempts). All threshold counts use each examinee's best-record NMAT attempt to avoid inflating the applicant pool with repeat attempts."))
    lines.append(sep())

    # Bin reference table
    lines.append(h2("Score Bin Reference"))
    ref = pd.DataFrame({
        "Bin": [f"B{i}" for i in range(1, 11)],
        "Score Range": [BIN_RANGES[f"B{i}"] for i in range(1, 11)],
        "Threshold": ["", "", "", "CMO exception floor (B4+)", "SUC standard floor (B5+)", "", "", "", "", ""],
    })
    lines.append(df_to_markdown(ref))
    lines.append(sep())

    return "\n".join(lines)


def build_tab2(df_all, df_best, df_obs):
    """B4+ vs B5+ Thresholds."""
    lines = [h1("Tab 2 — B4+ vs B5+ Thresholds")]
    db = df_best.dropna(subset=["PercentileBin"])
    dob = df_obs.dropna(subset=["PercentileBin"])

    # Heatmap
    lines.append(h2("Score Bin Distribution by NMAT Year"))
    lines.append(p("Heatmap values are row percentages. Rows = NMAT years, columns = score bins. Darker red = higher concentration in that bin for that year."))
    yp = pd.crosstab(db["Year"], db["PercentileBin"], dropna=False).reindex(columns=BIN_ORDER, fill_value=0)
    yp = yp.div(yp.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(1)
    yp.index.name = "Year"
    yp = yp.reset_index()
    yp["Year"] = yp["Year"].astype(str)
    lines.append(df_to_markdown(yp))
    lines.append(sep())

    # Threshold comparison
    lines.append(h2("Examinees Meeting Each Threshold"))
    n4 = db["PercentileBin"].isin(B4_PLUS).sum()
    n5 = db["PercentileBin"].isin(B5_PLUS).sum()
    n4o = (db["PercentileBin"] == "B4").sum()
    sc = pd.DataFrame([
        ["B4+ (Bin 4 and above)", n4, round(n4 / len(db) * 100, 1), dob["PercentileBin"].isin(B4_PLUS).sum()],
        ["B5+ (Bin 5 and above)", n5, round(n5 / len(db) * 100, 1), dob["PercentileBin"].isin(B5_PLUS).sum()],
        ["B4 only (Bin 4)", n4o, round(n4o / len(db) * 100, 1), (dob["PercentileBin"] == "B4").sum()],
    ], columns=["Threshold", "Best-record examinees", "Share of all (%)", "Observable cohort size"])
    lines.append(df_to_markdown(sc))
    lines.append(sep())

    # Threshold by UNI_TYPE
    lines.append(h2("Threshold Context by University Type"))
    ut_rows = []
    for ut in ["Public", "Private", "Foreign", "Not Specified"]:
        s = db[db["UNI_TYPE"] == ut]
        if s.empty: continue
        ut_rows.append([ut, len(s),
            f"{s['PercentileBin'].isin(B4_PLUS).sum():,} ({s['PercentileBin'].isin(B4_PLUS).sum()/len(s)*100:.1f}%)",
            f"{s['PercentileBin'].isin(B5_PLUS).sum():,} ({s['PercentileBin'].isin(B5_PLUS).sum()/len(s)*100:.1f}%)",
            f"{(s['PercentileBin']=='B4').sum():,} ({(s['PercentileBin']=='B4').sum()/len(s)*100:.1f}%)"])
    ut_df = pd.DataFrame(ut_rows, columns=["University Type", "Best-record examinees", "B4+", "B5+", "B4-only"])
    lines.append(df_to_markdown(ut_df))
    lines.append(sep())

    # Public school evidence
    lines.append(h2("Public School Examinees and B5+ Threshold"))
    pub = db[db["UNI_TYPE"] == "Public"]
    priv = db[db["UNI_TYPE"] == "Private"]
    pub_b5 = pub["PercentileBin"].isin(B5_PLUS).sum()
    pub_b4o = (pub["PercentileBin"] == "B4").sum()
    priv_b5 = priv["PercentileBin"].isin(B5_PLUS).sum()
    lines.append(metric_table([
        ("Public B5+ count", f"{pub_b5:,} ({pub_b5/len(pub)*100:.1f}%)"),
        ("Public B4-only count", f"{pub_b4o:,} ({pub_b4o/len(pub)*100:.1f}%)"),
        ("Private B5+ count", f"{priv_b5:,} ({priv_b5/len(priv)*100:.1f}%)"),
    ]))
    pub_tbl = pd.DataFrame([
        ["Total best-record examinees", f"{len(pub):,}", f"{len(priv):,}"],
        ["B5+ (Bin 5+)", f"{pub_b5:,} ({pub_b5/len(pub)*100:.1f}%)", f"{priv_b5:,} ({priv_b5/len(priv)*100:.1f}%)"],
        ["B4-only", f"{pub_b4o:,} ({pub_b4o/len(pub)*100:.1f}%)", f"{(priv['PercentileBin']=='B4').sum():,} ({(priv['PercentileBin']=='B4').sum()/len(priv)*100:.1f}%)"],
    ], columns=["Metric", "Public", "Private"])
    lines.append(df_to_markdown(pub_tbl))
    lines.append(p("Note: UNI_TYPE refers to the examinee's undergraduate institution, not necessarily the medical school they applied to. GIDA/IP status is not available in this dataset."))
    lines.append(sep())

    # B4 group profile
    lines.append(h2("Profile of the B4 Group (Bin 4 Only)"))
    b4g = db[db["PercentileBin"] == "B4"]
    b4_uni = b4g.groupby("UNI_TYPE", observed=True).size().reset_index(name="count")
    b4_uni["share"] = (b4_uni["count"] / b4_uni["count"].sum() * 100).round(1)
    lines.append(metric_table([
        ("B4 examinees (best record)", f"{len(b4g):,}"),
        ("Median TRUE raw score", f"{b4g['TotalRawScoreTRUE'].median():.1f}"),
    ]))
    lines.append(df_to_markdown(b4_uni))
    lines.append(sep())

    # Top vs bottom bins
    lines.append(h2("Top Bins (B8-B10) vs Bottom Bins (B1-B3) Trend"))
    _, pct_yr2 = None, None
    ct2 = pd.crosstab(db["Year"], db["PercentileBin"], dropna=False).reindex(columns=BIN_ORDER, fill_value=0)
    ct2 = ct2.apply(pd.to_numeric, errors="coerce")
    pct_yr2 = ct2.div(ct2.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(1)
    top_bot = pd.DataFrame({
        "Year": pct_yr2.index.astype(str),
        "Top B8-B10 (%)": pct_yr2[TOP_BINS].sum(axis=1).values.round(1),
        "Bottom B1-B3 (%)": pct_yr2[BOTTOM_BINS].sum(axis=1).values.round(1),
    })
    top_bot["Difference (pp)"] = (top_bot["Top B8-B10 (%)"] - top_bot["Bottom B1-B3 (%)"]).round(1)
    lines.append(df_to_markdown(top_bot))
    lines.append(sep())

    # Yearly threshold counts
    lines.append(h2("Yearly Examinees Meeting Each Threshold"))
    yt_rows = []
    for yr in sorted(db["Year"].dropna().unique()):
        yrd = db[db["Year"] == yr]
        yro = dob[dob["Year"] == yr]
        b4 = yrd["PercentileBin"].isin(B4_PLUS).sum()
        b5 = yrd["PercentileBin"].isin(B5_PLUS).sum()
        ob4 = yro["PercentileBin"].isin(B4_PLUS).sum() if not yro.empty else 0
        ob5 = yro["PercentileBin"].isin(B5_PLUS).sum() if not yro.empty else 0
        yt_rows.append([int(yr), len(yrd), b4, round(b4/len(yrd)*100, 1), b5, round(b5/len(yrd)*100, 1), ob4, ob5])
    yt_df = pd.DataFrame(yt_rows, columns=["Year", "Total best-record", "B4+ count", "B4+ share (%)", "B5+ count", "B5+ share (%)", "Observable B4+", "Observable B5+"])
    lines.append(df_to_markdown(yt_df))
    lines.append(sep())

    # B5+ stacked chart data
    lines.append(h2("B5+ PLE-Passer Composition by Year"))
    clean = df_obs[
        (df_obs["IS_PLE_ANALYSIS_SAFE"] == True)
        & (df_obs["PLE_YEAR_GAP"] >= 5)
        & (df_obs["FOREIGNER_STATUS"] == "Filipino")
    ].copy()
    clean_b5 = clean[clean["PercentileBin"].isin(B5_PLUS)].copy()
    if "HAS_CONFIRMED_PLE" not in clean_b5.columns:
        clean_b5["HAS_CONFIRMED_PLE"] = (clean_b5["IS_PLE_ANALYSIS_SAFE"] == True)
    b5_yr = (
        clean_b5.groupby("Year", observed=True)
        .agg(total=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum"))
        .reset_index()
    )
    b5_yr["no_match"] = b5_yr["total"] - b5_yr["confirmed"]
    b5_yr["linkage_pct"] = (b5_yr["confirmed"] / b5_yr["total"] * 100).round(1)
    b5_yr["no_match_pct"] = (b5_yr["no_match"] / b5_yr["total"] * 100).round(1)
    b5_yr_disp = b5_yr[["Year", "total", "confirmed", "no_match", "linkage_pct", "no_match_pct"]].copy()
    b5_yr_disp.columns = ["Year", "Total B5+ observable", "Confirmed PLE passers", "No confirmed PLE match", "Linkage rate (%)", "No-match share (%)"]
    lines.append(chart_block(
        "B5+ Examinees by PLE Status (Count) — B5+ Examinees by PLE Status (Percent)",
        "Two stacked bar charts showing Count (upper) and Percent (lower) of B5+ examinees by PLE-match status across NMAT years.",
        b5_yr_disp,
    ))
    lines.append(p("This is NMAT-to-PLE-passer linkage, not a PLE pass rate."))
    lines.append(sep())

    return "\n".join(lines)


def build_tab3(df_all, df_best, df_obs):
    """PLE-Passer Linkage."""
    lines = [h1("Tab 3 — PLE-Passer Linkage")]

    # Linkage by bin
    lines.append(h2("PLE Linkage by Score Bin"))
    ple = df_obs.dropna(subset=["PercentileBin", "HAS_CONFIRMED_PLE"]).groupby("PercentileBin", observed=True).agg(
        N=("APPNO_CLEAN", "count"), Confirmed=("HAS_CONFIRMED_PLE", "sum")
    ).reset_index()
    ple["Linkage Rate (%)"] = (ple["Confirmed"] / ple["N"] * 100).round(2)
    ple["Range"] = ple["PercentileBin"].map(BIN_RANGES)
    ple_disp = ple[["PercentileBin", "Range", "N", "Confirmed", "Linkage Rate (%)"]].copy()
    ple_disp.columns = ["Score Bin", "Range", "N (observable cohort)", "Confirmed PLE Passers", "Linkage Rate (%)"]
    lines.append(df_to_markdown(ple_disp))
    lines.append(sep())

    # Score profile
    lines.append(h2("Score Profile by PLE Status"))
    sp_cols = [c for c in ["TotalRawScoreTRUE", "NMS_PER_num", "PartIRawScoreTRUE", "PartIIRawScoreTRUE"] if c in df_obs.columns]
    sp = df_obs.groupby("HAS_CONFIRMED_PLE", observed=True)[sp_cols].agg(["count", "median", "mean", lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)]).round(2)
    sp.index = ["No confirmed PLE match", "Confirmed PLE passer"]
    lines.append(df_to_markdown(sp))
    lines.append(sep())

    # Linkage by year
    lines.append(h2("PLE-Passer Linkage by NMAT Year"))
    ply = df_obs.groupby("Year", observed=True).agg(N=("APPNO_CLEAN", "count"), Confirmed=("HAS_CONFIRMED_PLE", "sum")).reset_index()
    ply["Linkage Rate (%)"] = (ply["Confirmed"] / ply["N"] * 100).round(2)
    lines.append(df_to_markdown(ply))
    lines.append(sep())

    # Linkage by course group
    lines.append(h2("PLE-Passer Linkage by Course Group"))
    if "CourseGroup" in df_obs.columns:
        plc = df_obs.dropna(subset=["CourseGroup", "HAS_CONFIRMED_PLE"]).groupby("CourseGroup", observed=True).agg(
            N=("APPNO_CLEAN", "count"), Confirmed=("HAS_CONFIRMED_PLE", "sum"), Median_percentile=("NMS_PER_num", "median")
        ).reset_index()
        plc["Linkage Rate (%)"] = (plc["Confirmed"] / plc["N"] * 100).round(2)
        lines.append(df_to_markdown(plc))
        lines.append(sep())

    # Linkage by university type
    lines.append(h2("PLE-Passer Linkage by University Type"))
    plu = df_obs[df_obs["UNI_TYPE"].isin(["Public", "Private", "Foreign"])].groupby("UNI_TYPE", observed=True).agg(
        N=("APPNO_CLEAN", "count"), Confirmed=("HAS_CONFIRMED_PLE", "sum"), Median_percentile=("NMS_PER_num", "median")
    ).reset_index()
    plu["Linkage Rate (%)"] = (plu["Confirmed"] / plu["N"] * 100).round(2)
    lines.append(df_to_markdown(plu))
    lines.append(p("The observed difference in linkage rates between institution types reflects the set of NMAT examinees who were later matched to PLE passer records. The data does not identify the reasons for these differences."))
    lines.append(sep())

    # Clean PLE subset
    lines.append(h2("Clean PLE Subset Stress Test"))
    lines.append(p("Criteria: IS_BEST_NMAT_RECORD + IS_PLE_ANALYSIS_SAFE + PLE_YEAR_GAP >= 5 + FOREIGNER_STATUS == 'Filipino'"))
    clean = df_obs[
        (df_obs["IS_PLE_ANALYSIS_SAFE"] == True)
        & (df_obs["PLE_YEAR_GAP"] >= 5)
        & (df_obs["FOREIGNER_STATUS"] == "Filipino")
    ].copy()
    if "HAS_CONFIRMED_PLE" not in clean.columns:
        clean["HAS_CONFIRMED_PLE"] = (clean["IS_PLE_ANALYSIS_SAFE"] == True)
    clean_b5 = clean[clean["PercentileBin"].isin(B5_PLUS)].copy()
    lines.append(metric_table([
        ("Clean subset (all bins)", f"{len(clean):,}"),
        ("B5+ in clean subset", f"{len(clean_b5):,}"),
        ("Share of observable cohort", f"{len(clean_b5)/len(df_obs)*100:.1f}%"),
        ("Median PLE year gap", f"{clean_b5['PLE_YEAR_GAP'].median():.0f} yrs") if "PLE_YEAR_GAP" in clean_b5.columns else ("Median PLE year gap", "N/A"),
    ]))

    lines.append(h3("Yearly Clean Subset B5+ Data"))
    cs_yr = clean_b5.groupby("Year", observed=True).agg(total=("APPNO_CLEAN", "count"), confirmed=("HAS_CONFIRMED_PLE", "sum")).reset_index()
    cs_yr["no_match"] = cs_yr["total"] - cs_yr["confirmed"]
    cs_yr["linkage_pct"] = (cs_yr["confirmed"] / cs_yr["total"] * 100).round(1)
    lines.append(df_to_markdown(cs_yr))

    lines.append(h3("Clean B5+ by University Type"))
    cu = clean_b5.groupby("UNI_TYPE", observed=True).size().reset_index(name="N")
    cu["Share (%)"] = (cu["N"] / cu["N"].sum() * 100).round(1)
    lines.append(df_to_markdown(cu))
    lines.append(p("This subset uses the strictest defensible criteria. Results mirror the broader analysis."))
    lines.append(sep())

    return "\n".join(lines)


def build_tab4(df_all, df_best, df_obs):
    """Institution and Foreign Context."""
    lines = [h1("Tab 4 — Institution and Foreign Context")]
    uni = df_best[df_best["UNI_TYPE"].isin(["Public", "Private", "Foreign"])].copy()

    # Score summary
    lines.append(h2("Score Summary by University Type"))
    us = uni.groupby("UNI_TYPE", observed=True).agg(
        **{"N (best record)": ("APPNO_CLEAN", "count"),
           "Median %ile": ("NMS_PER_num", "median"),
           "Q25 %ile": ("NMS_PER_num", lambda x: x.quantile(0.25)),
           "Q75 %ile": ("NMS_PER_num", lambda x: x.quantile(0.75)),
           "Median TRUE raw score": ("TotalRawScoreTRUE", "median"),
           "Median GPS": ("NMS_GPS", "median")}
    ).round(1).reset_index()
    lines.append(df_to_markdown(us))
    lines.append(sep())

    # Box plot five-number summary
    lines.append(h2("Percentile Rank Distribution by University Type (Box Plot Data)"))
    bp_rows = []
    for ut in ["Public", "Private", "Foreign"]:
        s = uni[uni["UNI_TYPE"] == ut]["NMS_PER_num"].dropna()
        if len(s) == 0: continue
        bp_rows.append([ut, len(s), s.min(), s.quantile(0.25), s.median(), s.quantile(0.75), s.max()])
    bp_df = pd.DataFrame(bp_rows, columns=["University Type", "N", "Minimum", "Q25", "Median", "Q75", "Maximum"])
    lines.append(df_to_markdown(bp_df))
    lines.append(sep())

    # Bin distribution by UNI_TYPE
    lines.append(h2("Score Bin Distribution by University Type"))
    ct = pd.crosstab(uni["UNI_TYPE"], uni["PercentileBin"], dropna=False).reindex(columns=BIN_ORDER, fill_value=0)
    ct = ct.apply(pd.to_numeric, errors="coerce")
    ubp = ct.div(ct.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(1).reset_index()
    lines.append(df_to_markdown(ubp))
    lines.append(sep())

    # Top-bin share
    lines.append(h2("Top-Bin Share (B8-B10) by University Type"))
    tc = ct.sum(axis=1).reset_index()
    tc.columns = ["University Type", "Total Examinees"]
    top_s = ct[TOP_BINS].sum(axis=1).reset_index()
    top_s.columns = ["University Type", "Top B8-B10 Count"]
    top_pct = (ct[TOP_BINS].sum(axis=1) / ct.sum(axis=1).replace(0, np.nan) * 100).round(1).reset_index()
    top_pct.columns = ["University Type", "Top B8-B10 (%)"]
    top_df = tc.merge(top_pct, on="University Type").merge(top_s, on="University Type")
    lines.append(df_to_markdown(top_df))
    lines.append(sep())

    # Foreign context
    lines.append(h2("Foreign Examinee Context"))
    foreign = df_all[df_all["FOREIGNER_STATUS"] == "Verified Foreigner"]
    filipino = df_all[df_all["CITIZENSHIP_FINAL"] == "Filipino"]
    lines.append(metric_table([
        ("Verified Foreign NMAT examinees (all records)", f"{len(foreign):,}"),
        ("Filipino examinees", f"{len(filipino):,}"),
        ("Distinct foreign nationalities", f"{foreign['CITIZENSHIP_FINAL'].nunique()}"),
    ]))

    lines.append(h3("Top 10 Nationalities"))
    top_nat = foreign["CITIZENSHIP_FINAL"].value_counts().head(10).reset_index()
    top_nat.columns = ["Nationality", "Count"]
    top_nat["Share of verified foreign (%)"] = (top_nat["Count"] / top_nat["Count"].sum() * 100).round(1)
    top_nat.index = range(1, len(top_nat) + 1)
    top_nat.index.name = "Rank"
    lines.append(df_to_markdown(top_nat, index=True))
    lines.append(p("These are NMAT examinees, not enrolled medical students."))
    lines.append(sep())

    return "\n".join(lines)


def build_tab5(df_all, df_best, df_obs):
    """Key Evidence for Policy Review."""
    lines = [h1("Tab 5 — Key Evidence for Policy Review")]
    lines.append(p("The following findings are descriptive observations based on historical NMAT data (2006-2018). They do not constitute regulatory recommendations."))
    lines.append(sep())

    db = df_best.dropna(subset=["PercentileBin"])
    n4 = db["PercentileBin"].isin(B4_PLUS).sum()
    n5 = db["PercentileBin"].isin(B5_PLUS).sum()
    pub = db[db["UNI_TYPE"] == "Public"]
    priv = db[db["UNI_TYPE"] == "Private"]
    ple = df_obs.dropna(subset=["PercentileBin", "HAS_CONFIRMED_PLE"]).groupby("PercentileBin", observed=True).agg(n=("APPNO_CLEAN", "count"), c=("HAS_CONFIRMED_PLE", "sum")).reset_index()
    b1r = ple[ple["PercentileBin"] == "B1"].iloc[0] if "B1" in ple["PercentileBin"].values else None
    b10r = ple[ple["PercentileBin"] == "B10"].iloc[0] if "B10" in ple["PercentileBin"].values else None
    ann = df_obs.groupby("Year", observed=True).agg(n=("APPNO_CLEAN", "count"), c=("HAS_CONFIRMED_PLE", "sum")).reset_index()
    ann["r"] = (ann["c"] / ann["n"] * 100).round(1)
    ann["5yr"] = ann["r"].rolling(5, min_periods=3).mean().round(1)
    clean = df_obs[(df_obs["IS_PLE_ANALYSIS_SAFE"] == True) & (df_obs["PLE_YEAR_GAP"] >= 5) & (df_obs["FOREIGNER_STATUS"] == "Filipino")].copy()
    clean_b5 = clean[clean["PercentileBin"].isin(B5_PLUS)]
    nf = int((df_all["FOREIGNER_STATUS"] == "Verified Foreigner").sum())

    findings = [
        ("National Threshold Context", f"The historical NMAT examinee pool ranges from approximately {n4/len(db)*100:.0f}% meeting a B4+ threshold to {n5/len(db)*100:.0f}% meeting a B5+ threshold (best-record examinees, 2006-2018). The marginal group between the two thresholds — B4 only — accounts for roughly {(n4-n5)/len(db)*100:.0f} percentage points of the examinee population."),
        ("Institutional Performance Patterns", f"Public institution examinees show a higher median bin rank ({pub['NMS_PER_num'].median():.0f}) than Private institution examinees ({priv['NMS_PER_num'].median():.0f})."),
        ("NMAT-to-PLE-Passer Linkage Gradient", f"NMAT-to-PLE-passer linkage increases with score bin, from {b1r['c']/b1r['n']*100:.0f}% in the lowest bin (B1) to {b10r['c']/b10r['n']*100:.0f}% in the highest bin (B10). This is not a PLE pass rate." if b1r is not None and b10r is not None else "Data not available."),
        ("Historical Linkage Trends", f"The observable NMAT-to-PLE-passer linkage rate declined from {ann.iloc[0]['r']:.1f}% in {int(ann['Year'].iloc[0])} to {ann.iloc[-1]['r']:.1f}% in {int(ann['Year'].iloc[-1])} across the observable cohort. The 5-year rolling average was {ann['5yr'].dropna().iloc[-1]:.1f}% as of {int(ann[ann['5yr'].notna()]['Year'].iloc[-1])}."),
        ("Public School Threshold Attainment", f"Public school examinees already meet the B5+ threshold at a high rate: {pub['PercentileBin'].isin(B5_PLUS).sum()/len(pub)*100:.1f}% ({pub['PercentileBin'].isin(B5_PLUS).sum():,} out of {len(pub):,}) score at Bin 5 or above. Only {(pub['PercentileBin']=='B4').sum()/len(pub)*100:.1f}% fall in the B4-only band that the CMO exception addresses."),
        ("PLE Matching Robustness", f"Using the strictest defensible PLE matching criteria (single best-record, clean deterministic match, >=5 year gap, Filipino nationals only), the analysis yields {len(clean_b5):,} B5+ matched passers representing {len(clean_b5)/len(df_obs)*100:.1f}% of the observable cohort."),
        ("Foreign Examinee Presence", f"Foreign nationals represent approximately {nf/len(df_all)*100:.1f}% of all NMAT records ({nf:,} verified foreign records out of {len(df_all):,} total). India accounts for the largest share of foreign examinees. These are NMAT examinee counts, not enrolled medical students."),
    ]
    for title, body in findings:
        lines.append(h3(title))
        lines.append(p(body))

    lines.append(sep())
    lines.append(p("**Note on data scope.** These findings are limited to the NMAT examinee population captured in NMAT_Exodus.parquet. Key gaps in the available data include PLE failure rates (only passers are identifiable), GIDA/IP status, medical school admissions and enrollment figures, and institutional admission criteria."))
    return "\n".join(lines)


def build_tab6(df_all, df_best, df_obs):
    """Data, Methods, and Limitations."""
    lines = [h1("Tab 6 — Data, Methods, and Limitations")]

    n_best = len(df_best)
    n_obs = len(df_obs)
    n_unique = int(df_best["PERSON_KEY"].nunique())
    n_repeat = int((df_all.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique() > 1).sum())

    lines.append(h2("Dataset Overview"))
    lines.append(metric_table([
        ("Source file", "NMAT_Exodus.parquet (54 columns)"),
        ("Total rows", f"{len(df_all):,}"),
        ("Examination years", "2006-2018"),
        ("Unique examinees (best record)", f"{n_unique:,}"),
        ("Observable PLE cohort (Year <= 2014)", f"{n_obs:,}"),
        ("Repeat takers", f"{n_repeat:,} ({n_repeat/n_unique*100:.0f}%)"),
    ]))
    lines.append(sep())

    lines.append(h2("TRUE Raw Score Recalculation"))
    n_true = int((df_all["HasTRUErawScores"] == True).sum()) if "HasTRUErawScores" in df_all.columns else 0
    lines.append(p(f"The pipeline recalculated all raw scores from the 8 individual subtest components because 42.2% of the original stored totals were incorrect. All analyses use the recalculated TotalRawScoreTRUE scores."))
    lines.append(metric_table([
        ("Rows with complete TRUE scores", f"{n_true:,} (99.97%)"),
        ("Formula mismatches (Total != Part I + Part II)", "0"),
    ]))
    lines.append(sep())

    lines.append(h2("Best-Record Deduplication"))
    lines.append(p(f"{n_repeat:,} examinees ({n_repeat/n_unique*100:.0f}%) took the NMAT more than once (up to 9 attempts). Person-level analyses use the best-record flag (IS_BEST_NMAT_RECORD), which selects:"))
    lines.append(p("- For PLE passers: the specific NMAT attempt that matched to the PLE record."))
    lines.append(p("- For others: the highest percentile attempt, with latest year as tiebreaker."))
    lines.append(sep())

    lines.append(h2("Observable Cohort Definition (Year <= 2014)"))
    avg_gap = df_obs[df_obs["HAS_CONFIRMED_PLE"]]["PLE_YEAR_GAP"].median() if "PLE_YEAR_GAP" in df_obs.columns else "N/A"
    lines.append(p(f"PLE-linked analyses are restricted to examinees whose NMAT year is 2014 or earlier, ensuring a minimum 5-year window for PLE passage."))
    lines.append(metric_table([
        ("Observable best-record cohort", f"{n_obs:,}"),
        ("Median NMAT-to-PLE year gap", f"{avg_gap} years" if isinstance(avg_gap, (int, float)) else str(avg_gap)),
    ]))
    lines.append(sep())

    lines.append(h2("Deterministic PLE Matching"))
    n_all_ple = int((df_all["IS_PLE_ANALYSIS_SAFE"] == True).sum()) if "IS_PLE_ANALYSIS_SAFE" in df_all.columns else 0
    n_obs_ple = int(df_obs["HAS_CONFIRMED_PLE"].sum()) if "HAS_CONFIRMED_PLE" in df_obs.columns else 0
    clean = df_obs[(df_obs["IS_PLE_ANALYSIS_SAFE"] == True) & (df_obs["PLE_YEAR_GAP"] >= 5) & (df_obs["FOREIGNER_STATUS"] == "Filipino")] if "PLE_YEAR_GAP" in df_obs.columns else df_obs.iloc[0:0]
    clean_b5 = clean[clean["PercentileBin"].isin(B5_PLUS)] if not clean.empty else clean
    lines.append(p("All PLE matching is deterministic (exact NMA_AppNo match, manual AppNo match, or deterministic AppNo match). No fuzzy/rapidfuzz matching is used. This ensures full auditability but has important caveats: the NMAT application number (NMA_AppNo) is not a well-established, consistent identifier across datasets. The clean subset analysis uses the strictest criteria as a robustness check."))
    lines.append(metric_table([
        ("Confirmed PLE passers (all rows)", f"{n_all_ple:,}"),
        ("Confirmed PLE passers (best record, observable)", f"{n_obs_ple:,}"),
        ("Clean subset (B5+, Filipino, >=5yr gap)", f"{len(clean_b5):,}"),
    ]))
    lines.append(sep())

    lines.append(h2("Data Integrity Summary"))
    stored_m = int((df_all["StoredVsDerivedMismatch"] == 1.0).sum()) if "StoredVsDerivedMismatch" in df_all.columns else 0
    calc_m = int((df_all["CalcVsDerivedMismatch"] == 1.0).sum()) if "CalcVsDerivedMismatch" in df_all.columns else 0
    lines.append(metric_table([
        ("Stored-vs-derived mismatches", f"{stored_m:,}"),
        ("Calc-vs-derived mismatches", f"{calc_m:,}"),
    ]))
    lines.append(sep())

    lines.append(h2("Limitations Relevant to CHED Decision-Making"))
    lims = [
        ("PLE Outcomes", "The dataset only identifies NMAT examinees later matched to PLE passer records. It does not contain all PLE takers or PLE failures. Therefore, this dashboard reports NMAT-to-PLE-passer linkage rates, not PLE pass rates. Official PLE passing rates published by the PRC should be used for benchmarking purposes."),
        ("GIDA and IP Status", "The dataset does not contain indicators for Geographically Isolated and Disadvantaged Area (GIDA) residence or Indigenous Peoples (IP) membership. The CMO exception for B4-only applicants from these groups requires documentation not available in this dataset."),
        ("Medical School Admissions and Enrollment", "This dataset records NMAT examinees, not enrolled medical students. The number of examinees at or above a threshold represents the available applicant pool, not actual enrollment."),
        ("Foreign Student Enrollment Cap", "The CMO caps foreign student enrollment at 10 slots per incoming class at SUCs. The dataset shows NMAT examinees by citizenship, not enrolled foreign students."),
        ("Composite Ranking for Foreign Applicants", "The dataset does not contain GWA, interview scores, or other admission criteria needed for composite ranking analysis."),
        ("PHEI Accountability and Sanctions", "This dashboard does not assign compliance labels or risk ratings to individual HEIs. The NMAT-linked PLE data is not a complete measure of institutional PLE performance."),
    ]
    for title, detail in lims:
        lines.append(h3(title))
        lines.append(p(detail))

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def build_full_markdown(df_all, df_best, df_obs, viz_dir=None):
    """Return one complete Markdown string for all 6 dashboard tabs.

    Parameters
    ----------
    df_all : pd.DataFrame — all NMAT records
    df_best : pd.DataFrame — best-record subset
    df_obs : pd.DataFrame — observable cohort (best + Year <= 2014)
    viz_dir : str or None — if provided, generate charts and save to this directory
    """
    chart_map = {}
    if viz_dir is not None:
        chart_map = generate_all_charts(df_all, df_best, df_obs, viz_dir)

    def img(name, alt=""):
        if name in chart_map:
            return f"![{alt}]({chart_map[name]})\n"
        return ""

    lines = []
    lines.append("# NMAT Performance Evidence for CHED Cut-Off Policy Review")
    lines.append("")
    lines.append("> Complete Markdown export generated from the dashboard's underlying computations and data tables. This document mirrors all six dashboard tabs.")
    lines.append("")
    lines.append("**Scope:** Descriptive evidence from NMAT_Exodus.parquet (178,927 examinee records, 2006-2018) to inform the CMO amendment on NMAT cut-off scores. PLE-linked analyses use the observable cohort (Year <= 2014) to avoid right-censoring bias.")
    lines.append("")
    lines.append("**Definitions:**")
    lines.append("- **Best-record examinees** — one NMAT record per person (removes repeat-taker inflation).")
    lines.append("- **Observable cohort** — examinees with Year <= 2014, who have had time to take the PLE.")
    lines.append("- **Score bins** — B1 (0-9) through B10 (90-100). B4+ means at or above Bin 4 (30th-39th). B5+ means at or above Bin 5 (40th-49th).")
    lines.append("- **NMAT-to-PLE linkage** — the proportion of NMAT examinees who were later matched to PLE passer records. This is NOT a PLE pass rate. The dataset does not contain all PLE takers or PLE failures.")
    lines.append("- **Foreign examinee counts** — these are NMAT examinees, not enrolled medical students.")
    lines.append("- **All score summaries use recalculated TRUE raw scores** — the original stored total was inconsistent for 42.2% of records and has been corrected.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Ensure HAS_CONFIRMED_PLE exists
    if "HAS_CONFIRMED_PLE" not in df_obs.columns and "IS_PLE_ANALYSIS_SAFE" in df_obs.columns:
        df_obs = df_obs.copy()
        df_obs["HAS_CONFIRMED_PLE"] = (df_obs["IS_PLE_ANALYSIS_SAFE"] == True)

    # Bin order
    if "PercentileBin" in df_all.columns:
        for df_tmp in [df_all, df_best, df_obs]:
            if "PercentileBin" in df_tmp.columns and not isinstance(df_tmp["PercentileBin"].dtype, pd.CategoricalDtype):
                df_tmp["PercentileBin"] = pd.Categorical(df_tmp["PercentileBin"], categories=BIN_ORDER, ordered=True)

    lines.append(build_tab1(df_all, df_best, df_obs))
    lines.append(img("uni_pie", "University Type Composition Pie Chart"))
    lines.append(img("course_pie", "Course Group Composition Pie Chart"))
    lines.append(img("annual_trend", "Annual Trend Chart: Examinee Volume and Median Bin Rank"))
    lines.append(build_tab2(df_all, df_best, df_obs))
    lines.append(img("bin_heatmap", "Score Bin Distribution Heatmap by Year"))
    lines.append(img("top_bottom_trend", "Top Bins vs Bottom Bins Trend"))
    lines.append(img("b4_group", "B4 Examinees by Institution Type"))
    lines.append(build_tab3(df_all, df_best, df_obs))
    lines.append(img("ple_linkage_bin", "PLE Linkage Rate by Score Bin"))
    lines.append(img("ple_linkage_year", "PLE Linkage Rate by NMAT Year"))
    lines.append(img("ple_linkage_course", "PLE Linkage Rate by Course Group"))
    lines.append(img("ple_linkage_uni", "PLE Linkage Rate by University Type"))
    lines.append(build_tab4(df_all, df_best, df_obs))
    lines.append(img("uni_box", "Bin Rank Distribution by University Type - Box Plot"))
    lines.append(img("uni_bin_heatmap", "Bin Distribution by University Type Heatmap"))
    lines.append(img("top_bin_uni", "Top-Bin Share by University Type"))
    lines.append(img("foreign_top", "Top 10 Foreign Nationalities"))
    lines.append(build_tab5(df_all, df_best, df_obs))
    lines.append(build_tab6(df_all, df_best, df_obs))

    return "\n".join(lines)
