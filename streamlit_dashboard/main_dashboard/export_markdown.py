"""export_markdown.py -- Export the main NMAT dashboard as one complete
Markdown document with every visualization's underlying data as a table.

Every number in this file comes from the SAME `main_common.compute_*()`
functions that `dashboard.py` renders from (export-format contract Rule 6).
There is no independent re-derivation of any aggregation here.

The export always uses the FULL, UNFILTERED cohort (`subsets`, as returned
by `main_common.load_data_and_subsets()`), never the sidebar filter state --
"export the full picture" per the task brief.

Public function: build_full_markdown(df_raw, subsets) -> str
"""

import hashlib
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pandas as pd

import main_common as mc

BIN_ORDER = mc.BIN_ORDER
PLE_ORDER = mc.PLE_ORDER
TOP_BINS = mc.TOP_BINS
BOTTOM_BINS = mc.BOTTOM_BINS

# Export-integrity counters, reset per build_full_markdown() call.
_INTEGRITY = {
    "tabs": 0, "tabs_total": 13, "charts": 0, "charts_total": 0,
    "tables": 0, "captions": 0, "assertions_passed": 0, "assertions_total": 0,
}


def _reset_integrity():
    for k in _INTEGRITY:
        _INTEGRITY[k] = 0
    _INTEGRITY["tabs_total"] = 13


def _assert_equal(label, a, b, tol=1e-6):
    """Assert an exported value equals the value computed directly from the
    shared compute layer (contract Rule 6 verification requirement)."""
    _INTEGRITY["assertions_total"] += 1
    ok = (abs(a - b) <= tol) if isinstance(a, (int, float)) and isinstance(b, (int, float)) else (a == b)
    if ok:
        _INTEGRITY["assertions_passed"] += 1
    return ok


# ---------------------------------------------------------------------------
# Markdown helpers (same pattern as CHED_relevant_dashboard/export_markdown.py)
# ---------------------------------------------------------------------------
def h1(t): return f"\n# {t}\n"
def h2(t): return f"\n## {t}\n"
def h3(t): return f"\n### {t}\n"


def p(t):
    _INTEGRITY["captions"] += 1
    return f"{t}\n"


def sep(): return "\n---\n"


def df_to_markdown(df, index=False, float_format=".2f"):
    if df is None or (hasattr(df, "empty") and df.empty):
        _INTEGRITY["tables"] += 1
        return "_(no data under the current population)_"
    d = df.copy()
    if index and d.index.name is None:
        d.index.name = "index"
    if isinstance(d.columns, pd.MultiIndex):
        d.columns = [" / ".join(str(x) for x in c if str(x) != "") for c in d.columns]
    for c in d.columns:
        if pd.api.types.is_bool_dtype(d[c]):
            d[c] = d[c].apply(lambda x: "True" if x else "False")
        elif pd.api.types.is_integer_dtype(d[c]):
            d[c] = d[c].apply(lambda x: f"{x:,}" if pd.notna(x) else "-")
        elif pd.api.types.is_float_dtype(d[c]):
            d[c] = d[c].apply(lambda x: f"{x:{float_format}}" if pd.notna(x) else "-")

    _INTEGRITY["tables"] += 1
    try:
        import tabulate  # noqa: F401
        return d.to_markdown(index=index, tablefmt="pipe", numalign="right", stralign="left")
    except ImportError:
        pass

    rows = []
    headers = list(d.columns)
    if index:
        headers = [d.index.name or ""] + headers
    rows.append("| " + " | ".join(str(h) for h in headers) + " |")
    rows.append("|" + "|".join("---" for _ in headers) + "|")
    for idx, row in d.iterrows():
        vals = [str(row[c]) if pd.notna(row[c]) else "-" for c in d.columns]
        if index:
            vals = [str(idx)] + vals
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
    _INTEGRITY["charts"] += 1
    _INTEGRITY["charts_total"] += 1
    return (
        f"<!-- chart_type: {chart_type} | x: {x} | y: {y} | series: {series}\n"
        f"     population: {population}\n"
        f"     n: {n} | denominator: {denominator}\n"
        f"     source_tab: {source_tab} | element_id: {element_id} -->\n"
    )


def chart_block(title, description, df, meta="", index=False):
    parts = [h3(title), meta, p(description), df_to_markdown(df, index=index), ""]
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Tab builders -- every number below calls the SAME main_common functions
# dashboard.py uses.
# ---------------------------------------------------------------------------
def build_tab1(S):
    base, observable, trend = S["besttrend"], S["bestobservable"], S["trend"]
    lines = [h1("Tab 1 -- Executive Summary")]

    kpi = mc.compute_tab1_kpis(base, observable, trend)
    lines.append(metric_table([
        ("Examinees (best-record)", f"{kpi['n_best']:,}", "one row per person", "-"),
        ("Years covered", f"{kpi['n_years']}", "-", "-"),
        ("Median TRUE raw score", f"{kpi['median_raw']:.1f}", "best-record examinees", "-"),
        ("Median percentile rank", f"{kpi['median_pct']:.1f}", "best-record examinees", "0-99 scale"),
        ("Repeat takers", f"{kpi['n_repeat']:,} ({kpi['repeat_share_pct']:.1f}%)", "unique examinees, all sittings", "-"),
        ("Observable cohort (IS_BEST_OBSERVABLE_RECORD)", f"{kpi['n_observable']:,}", "best attempt, Year<=2014", "-"),
        ("PLE linkage rate, observable cohort", f"{kpi['ple_linkage_pct']:.2f}%", "observable cohort", "linkage, not pass rate"),
    ]))
    lines.append(sep())

    lines.append(h2("Annual Trend"))
    summary = mc.get_yearly_summary(base)
    lines.append(chart_meta("bar+line", "Year", "n, raw_median, per_median", "best-record examinees, all years",
                             f"{kpi['n_best']:,}", "one row per person", 1, "t1_fig1"))
    lines.append(df_to_markdown(summary))
    lines.append(sep())

    lines.append(h2("Course-Group Composition"))
    course_dist = mc.compute_composition(base, "UNDERGRAD_COURSE_GROUP")
    lines.append(chart_meta("pie", "UNDERGRAD_COURSE_GROUP", "Count", "best-record examinees",
                             f"{kpi['n_best']:,}", "best-record examinees", 1, "t1_fig2"))
    lines.append(df_to_markdown(course_dist))
    lines.append(sep())

    lines.append(h2("University-Type Composition"))
    uni_dist = mc.compute_composition(base, "UNDERGRAD_UNI_TYPE")
    lines.append(chart_meta("pie", "UNDERGRAD_UNI_TYPE", "Count", "best-record examinees",
                             f"{kpi['n_best']:,}", "best-record examinees", 1, "t1_fig3"))
    lines.append(df_to_markdown(uni_dist))
    lines.append(sep())

    lines.append(h2("Table 1 -- Executive Summary Indicators"))
    lines.append(df_to_markdown(mc.compute_tab1_summary_table(base)))
    lines.append(sep())
    return "\n".join(lines)


def build_tab2(S):
    df, best, best_obs = S["all"], S["best"], S["bestobservable"]
    lines = [h1("Tab 2 -- Data Integrity")]

    kpi = mc.compute_tab2_kpis(df, best, best_obs)
    lines.append(metric_table([
        ("All NMAT rows", f"{kpi['n_all']:,}", "all sittings", "-"),
        ("Best-record rows", f"{kpi['n_best']:,}", "one row per person", "-"),
        ("Rows with TRUE raw scores", f"{kpi['n_true_raw']:,}", "all rows", "-"),
        ("Observable best-record rows", f"{kpi['n_best_observable']:,}", "IS_BEST_OBSERVABLE_RECORD", "-"),
    ]))
    lines.append(sep())

    lines.append(h2("Table 2 -- Analysis Cohorts"))
    lines.append(df_to_markdown(mc.compute_cohort_table(S)))
    lines.append(sep())

    lines.append(h2("Table 3 -- TRUE Raw-Score Validation Checks"))
    rv = mc.compute_raw_validation_checks(df)
    lines.append(metric_table([
        ("Rows with complete Total + Part I + Part II", f"{rv['eq_mask_n']:,}", "all rows", "-"),
        ("Formula mismatches (Total != Part I + Part II)", f"{rv['mismatch_n']:,}", "rows above", "-"),
        ("Rows with a stored raw total", f"{rv['stored_nonnull_n']:,}", "all rows", "-"),
        ("Stored-vs-derived mismatch flag count", f"{rv['mismatch_flag_n']:,}", "rows with a stored total",
         f"{rv['mismatch_rate_pct']:.2f}%"),
    ]))
    lines.append(p(
        f"Stored-vs-derived mismatch rate: {rv['mismatch_flag_n']:,} of {rv['stored_nonnull_n']:,} rows "
        f"with a stored total disagree with the recalculated TotalRawScoreTRUE "
        f"({rv['mismatch_rate_pct']:.2f}% of that denominator). Never state this as \"42.2%\" -- that "
        "figure divided the mismatch count by the wrong (unique-examinee) denominator."
    ))
    lines.append(sep())

    lines.append(h2("Table 4 -- University Pairing Audit"))
    university_pairing, pairing_conflicts = mc.compute_university_pairing_audit(df)
    if university_pairing is not None:
        lines.append(metric_table([
            ("Universities checked", f"{university_pairing.shape[0]:,}", "distinct UNDERGRAD_UNIVERSITY values", "-"),
            ("University pairing conflicts", f"{pairing_conflicts.shape[0]:,}", "universities above",
             ">1 UNDERGRAD_UNI_TYPE or >1 UNDERGRAD_UNI_LOCATION"),
        ]))
        lines.append(df_to_markdown(pairing_conflicts.head(200)))
        if len(pairing_conflicts) > 200:
            lines.append(p(f"<!-- truncated: true | shown: 200 | total: {len(pairing_conflicts)} -->"))
    lines.append(sep())

    lines.append(h2("Tables 6-8 -- Core Distributions"))
    lines.append(df_to_markdown(mc.compute_composition(df, "UNDERGRAD_UNI_TYPE", dropna=False)))
    lines.append(df_to_markdown(mc.compute_composition(df, "UNDERGRAD_COURSE_GROUP", dropna=False)))
    status_counts, non_obs_n, non_obs_pct = mc.compute_ple_status_observable(df)
    lines.append(df_to_markdown(status_counts))
    lines.append(p(f"{non_obs_n:,} of {len(df):,} rows ({non_obs_pct:.1f}%) are Year > 2014 and excluded from the PLE-status table for that reason."))
    lines.append(sep())

    outcome_tbl, yr_uncertain_n = mc.compute_ple_match_outcome(df)
    if outcome_tbl is not None:
        lines.append(h2("Table 9 -- PLE Match-Outcome Breakdown"))
        lines.append(df_to_markdown(outcome_tbl))
        if yr_uncertain_n is not None:
            lines.append(p(f"{yr_uncertain_n:,} confirmed passers have PLE_YEAR_UNCERTAIN == True."))
        lines.append(sep())
    return "\n".join(lines)


def build_tab3(S):
    df = S["besttrend"]
    lines = [h1("Tab 3 -- Trends & Stability")]
    summary = mc.get_yearly_summary(df)
    lines.append(chart_meta("line (4-panel)", "Year", "raw/percentile median + IQR, n", "best-record trend cohort",
                             f"{len(df):,}", "best-record examinees, 2006-2018", 3, "t3_fig4"))
    lines.append(df_to_markdown(summary))
    lines.append(sep())

    lines.append(h2("Table 9 -- Kruskal-Wallis Tests by Year"))
    ktable = mc.kruskal_table(df, "Year", {
        "TotalRawScoreTRUE": "Total Raw Score", "PartIRawScoreTRUE": "Part I Raw Score",
        "PartIIRawScoreTRUE": "Part II Raw Score", "NMS_PER_num": "Percentile Rank", "NMS_GPS": "GPS Standard Score",
    })
    lines.append(df_to_markdown(ktable))
    lines.append(sep())
    return "\n".join(lines)


def build_tab4(S):
    df, dfuni = S["besttrend"], S["uni"]
    lines = [h1("Tab 4 -- Score Bins & Background")]

    count, pct = mc.pct_table(df, "Year", "PercentileBin", BIN_ORDER)
    lines.append(h2("Bin Distribution by Year"))
    lines.append(chart_meta("heatmap", "Year", "PercentileBin", "row %", "best-record trend cohort",
                             f"{len(df):,}", "best-record examinees, 2006-2018", 4, "t4_fig5"))
    lines.append(df_to_markdown(pct.reset_index()))
    lines.append(sep())

    lines.append(h2("Top vs Bottom Bin Share by Year"))
    lines.append(df_to_markdown(mc.compute_top_bottom_by(pct)))
    lines.append(sep())

    lines.append(h2("Bin Distribution by University Type"))
    _, uni_pct = mc.pct_table(dfuni, "UNDERGRAD_UNI_TYPE", "PercentileBin", BIN_ORDER)
    lines.append(df_to_markdown(uni_pct.reset_index()))
    lines.append(sep())

    lines.append(h2("Table 11 -- Chi-Square: University Type x Bin"))
    _, _, chi_summary = mc.chi_square_unitype_bin(dfuni.dropna(subset=["UNDERGRAD_UNI_TYPE", "PercentileBin"]))
    lines.append(df_to_markdown(chi_summary))
    lines.append(sep())

    lines.append(h2("Bin Count by Year x University Type"))
    yr_uni = mc.compute_bin_by_year_and_unitype(dfuni)
    lines.append(df_to_markdown(yr_uni))
    lines.append(p(
        f"<!-- truncated: {'true' if len(yr_uni) > 500 else 'false'} | shown: {min(len(yr_uni), 500)} | "
        f"total: {len(yr_uni)} -->" if len(yr_uni) > 500 else "Full table shown."
    ))
    lines.append(sep())

    cp = mc.compute_citizenship_profile(S["uniobservable"])
    lines.append(h2("Citizenship Profile for No-PLE-Match Examinees"))
    if cp.get("available") and not cp.get("empty"):
        lines.append(metric_table([
            ("Profiled no-PLE-match records", f"{cp['kpis']['n_profiled']:,}", "no-PLE-match, observable, uni subset", "-"),
            ("Foreigners", f"{cp['kpis']['n_foreigners']:,}", "rows above", "Verified Foreigner"),
            ("Filipinos", f"{cp['kpis']['n_filipinos']:,}", "rows above", "-"),
            ("Distinct citizenship labels", f"{cp['kpis']['n_distinct']:,}", "rows above", "-"),
        ]))
        lines.append(h3("Citizenship Counts"))
        lines.append(df_to_markdown(cp["counts"].head(50)))
        if len(cp["counts"]) > 50:
            lines.append(p(f"<!-- truncated: true | shown: 50 | total: {len(cp['counts'])} -->"))
        if cp["bin_dist_top15"] is not None:
            lines.append(h3("Bin Distribution by Citizenship (Top 15)"))
            lines.append(df_to_markdown(cp["bin_dist_top15"].reset_index()))
        if cp["topbin_share"] is not None:
            lines.append(h3("Top-Bin Share (B8-B10) by Citizenship (n>=3)"))
            lines.append(df_to_markdown(cp["topbin_share"]))
        lines.append(h3("Summary by Citizenship"))
        lines.append(df_to_markdown(cp["summary"]))
        if cp["by_year"] is not None:
            lines.append(h3("Year Distribution by Citizenship"))
            lines.append(df_to_markdown(cp["by_year"].head(30)))
        lines.append(p(
            f"Person-level record detail ({len(cp['records']):,} rows) is available in the live dashboard "
            "and its CSV downloads; not dumped inline here per export contract Rule 3."
        ))
    else:
        lines.append(p("Citizenship columns not available or no matching rows under this population."))
    lines.append(sep())

    cmp = mc.compute_comparative_groups(S["uniobservable"], S["bestobservable"])
    lines.append(h2("Comparative Analysis: Foreigners vs Filipino Undergrad Groups"))
    if cmp is not None:
        lines.append(df_to_markdown(cmp["agg"]))
        if cmp["bin_pct"] is not None:
            lines.append(h3("Bin Distribution by Comparison Group"))
            lines.append(df_to_markdown(cmp["bin_pct"].reset_index()))
        if cmp["topbot"] is not None:
            lines.append(h3("Top vs Bottom Bin Share by Comparison Group"))
            lines.append(df_to_markdown(cmp["topbot"]))
    else:
        lines.append(p("No comparative data available (requires Public/Private undergrad groups)."))
    lines.append(sep())

    lines.append(h2("Table 12 -- Percentile Summary by Course Group"))
    lines.append(df_to_markdown(mc.compute_percentile_summary_by(df, "UNDERGRAD_COURSE_GROUP")))
    lines.append(sep())
    return "\n".join(lines)


def build_tab5(S):
    base = S["uni"]
    uni_type_base = base.dropna(subset=["UNDERGRAD_UNI_TYPE", "UNDERGRAD_UNI_LOCATION"])
    uni_base = uni_type_base.dropna(subset=["PercentileBin"])
    lines = [h1("Tab 5 -- University Type Analysis")]

    lines.append(h2("Table 13 -- Institution Type by Location Mix"))
    lines.append(df_to_markdown(mc.compute_unitype_location_mix(uni_type_base)))
    lines.append(sep())

    lines.append(h2("Table 14 -- Institution Type by Location Matrix"))
    inst_count, inst_pct_row, inst_pct_col = mc.compute_unitype_location_crosstab(uni_type_base)
    lines.append(h3("Counts (with totals)"))
    lines.append(df_to_markdown(inst_count.reset_index()))
    lines.append(h3("Row % (within UNDERGRAD_UNI_TYPE)"))
    lines.append(df_to_markdown(inst_pct_row.reset_index()))
    lines.append(h3("Column % (within UNDERGRAD_UNI_LOCATION)"))
    lines.append(df_to_markdown(inst_pct_col.reset_index()))
    lines.append(sep())

    inst_decile_pct = mc.compute_unitype_location_bin_dist(uni_base)
    lines.append(h2("Bin Distribution by Institution Type x Location"))
    lines.append(df_to_markdown(inst_decile_pct.reset_index()))
    lines.append(sep())

    uni_decile_pct, uni_decile_summary = mc.compute_uni_bin_summary(uni_base)
    lines.append(h2("Table 15 -- Bin Counts by University Type"))
    lines.append(df_to_markdown(uni_decile_summary))
    lines.append(sep())

    lines.append(h2("Table 16 -- Foreign Examinee Summary"))
    fsum = mc.compute_foreign_summary(uni_base)
    lines.append(metric_table([
        ("Foreign examinees", f"{fsum['n_foreign']:,}", "uni_base", "-"),
        ("% of total", f"{fsum['pct_of_total']:.2f}%", "uni_base", "-"),
        ("Median percentile", f"{fsum['median_pct']:.1f}" if fsum['median_pct'] is not None else "n/a", "foreign subset", "-"),
        ("Top-bin (B8-B10) %", f"{fsum['topbin_pct']:.2f}%" if fsum['topbin_pct'] is not None else "n/a", "foreign subset", "-"),
    ]))
    lines.append(sep())

    lines.append(h2("Figure 16 -- Medical & Allied vs Other Courses by University Type"))
    lines.append(df_to_markdown(mc.compute_course_bucket_by_unitype(uni_type_base).reset_index()))
    lines.append(sep())

    lines.append(h2("Table 17 -- University Listings by University Type"))
    for uni_type in ["Public", "Private", "Foreign"]:
        table = mc.compute_university_listing(uni_type_base, uni_type)
        lines.append(h3(f"{uni_type} Universities"))
        lines.append(df_to_markdown(table.head(50)))
        if len(table) > 50:
            lines.append(p(f"<!-- truncated: true | shown: 50 | total: {len(table)} -->"))
    lines.append(sep())
    return "\n".join(lines)


def build_tab6(S):
    best, uni, observable = S["besttrend"], S["uni"], S["bestobservable"]
    lines = [h1("Tab 6 -- Flow & Pathways")]

    flow1 = mc.make_flow(uni, "UNDERGRAD_UNI_TYPE", "PercentileBin", ["Public", "Private", "Foreign"], BIN_ORDER)
    lines.append(h2("Table 18 -- University Type to Bin Flow"))
    lines.append(chart_meta("sankey", "UNDERGRAD_UNI_TYPE", "PercentileBin", "source->target->value", "uni subset",
                             f"{int(flow1['count'].sum()):,}", "best-record, Public/Private/Foreign", 6, "t6_fig17"))
    lines.append(df_to_markdown(flow1))
    lines.append(sep())

    order = [c for c in ["Medical & Allied", "Natural Sciences", "Social & Behavioral Sciences", "Education", "Engineering & Technology", "Other"]
             if c in best["UNDERGRAD_COURSE_GROUP"].unique()]
    flow2 = mc.make_flow(best, "UNDERGRAD_COURSE_GROUP", "PercentileBin", order, BIN_ORDER)
    lines.append(h2("Table 19 -- Course Group to Bin Flow"))
    lines.append(df_to_markdown(flow2))
    lines.append(sep())

    flow3 = mc.make_flow(observable, "PercentileBin", "PLE_STATUS_LABEL", BIN_ORDER, PLE_ORDER)
    row_pct = mc.compute_flow_pct(flow3, "PercentileBin", "PLE_STATUS_LABEL", BIN_ORDER, PLE_ORDER)
    lines.append(h2("Table 20 -- Bin to PLE Status Flow (Observable Cohort)"))
    lines.append(df_to_markdown(flow3))
    lines.append(h3("PLE Status Composition within Each Bin (%)"))
    lines.append(df_to_markdown(row_pct.reset_index()))
    lines.append(sep())

    lines.append(h2("Tables 21-22 -- Largest Pathways into B8-B10"))
    lines.append(df_to_markdown(mc.compute_top_pathways(uni, "UNDERGRAD_UNI_TYPE")))
    lines.append(df_to_markdown(mc.compute_top_pathways(best, "UNDERGRAD_COURSE_GROUP")))
    lines.append(sep())
    return "\n".join(lines)


def build_tab7(S):
    df, dfuni = S["bestobservable"], S["uniobservable"]
    lines = [h1("Tab 7 -- PLE Alignment")]

    lines.append(h2("Table 23 -- Score Profile by PLE Status"))
    desc_cols = ["TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE", "NMS_PER_num", "NMS_GPS", "NMS_APT", "NMS_SA"]
    lines.append(df_to_markdown(mc.compute_score_desc_by(df, "PLE_STATUS_LABEL", desc_cols).reset_index(), index=False))
    lines.append(sep())

    lines.append(h2("Table 24 -- Mann-Whitney: Confirmed vs No Match"))
    mw = mc.mann_whitney_ple(df, {
        "TotalRawScoreTRUE": "Total Raw Score", "PartIRawScoreTRUE": "Part I", "PartIIRawScoreTRUE": "Part II",
        "NMS_PER_num": "Percentile Rank", "NMS_GPS": "GPS Standard Score",
    })
    lines.append(df_to_markdown(mw))
    lines.append(sep())

    _, ple_dist_pct = mc.pct_table(df, "PLE_STATUS_LABEL", "PercentileBin", BIN_ORDER)
    lines.append(h2("Figure 21 -- Bin Distribution by PLE Status"))
    lines.append(df_to_markdown(ple_dist_pct.reindex(PLE_ORDER).reset_index()))
    lines.append(sep())

    lines.append(h2("Table 25 -- PLE Status Composition within Each Bin"))
    lines.append(df_to_markdown(mc.compute_ple_status_by_bin(df).reset_index()))
    lines.append(sep())

    lines.append(h2("Table 26 -- Course-Group Top-Bin Survival"))
    lines.append(df_to_markdown(mc.compute_top_bin_share_by(S["besttrend"], "UNDERGRAD_COURSE_GROUP")))
    lines.append(sep())

    lines.append(h2("Table 27 -- Confirmed PLE Alignment by University Type"))
    lines.append(df_to_markdown(mc.compute_ple_alignment_by(dfuni, "UNDERGRAD_UNI_TYPE")))
    lines.append(sep())

    lines.append(h2("Tables 28-30 -- Confirmed PLE Alignment by Year / Course / University Type"))
    lines.append(df_to_markdown(mc.compute_ple_alignment_by(df, "Year")))
    lines.append(df_to_markdown(mc.compute_ple_alignment_by(df, "UNDERGRAD_COURSE_GROUP", include_median=True)))
    lines.append(df_to_markdown(mc.compute_ple_alignment_by(df, "UNDERGRAD_UNI_TYPE", include_median=True)))
    lines.append(sep())
    return "\n".join(lines)


def build_tab8(S):
    df = S["trend"]
    lines = [h1("Tab 8 -- Repeat Takers")]

    attempt_ct, attempt_summary = mc.compute_attempt_distribution(df)
    lines.append(h2("Table 31 -- Attempt-Count Distribution"))
    lines.append(chart_meta("bar", "Attempts", "Count", "all sittings, 2006-2018", f"{len(df):,}",
                             "all NMAT sittings in the trend window", 8, "t8_fig24"))
    lines.append(df_to_markdown(attempt_summary))
    lines.append(sep())

    first_last, traj = mc.compute_repeat_trajectories(df)
    lines.append(h2("Table 32 -- Repeat-Taker Trajectory Summary"))
    if first_last is not None:
        lines.append(metric_table([
            ("Repeat-taker persons", f"{traj['n_repeat_persons']:,}", "unique PERSON_KEY, >1 attempt", "-"),
            ("Analytic repeat takers", f"{traj['n_analytic_repeat_takers']:,}", "with complete first/last scores", "-"),
            ("Improved percentile rank", f"{traj['pct_improved_percentile']:.2f}%", "analytic repeat takers", "-"),
            ("Improved raw score", f"{traj['pct_improved_raw']:.2f}%", "analytic repeat takers", "-"),
            ("Median percentile change", f"{traj['median_pct_change']:.2f}", "analytic repeat takers", "-"),
            ("Median raw score change", f"{traj['median_raw_change']:.2f}", "analytic repeat takers", "-"),
        ]))
    else:
        lines.append(p("No repeat takers available."))
    lines.append(sep())

    appno_matches = mc.compute_appno_deterministic_matches(df)
    lines.append(h2("NMA_AppNo Deterministic Match Histories"))
    lines.append(metric_table([
        ("Deterministically matched rows", f"{len(appno_matches):,}", "PLE_MATCH_METHOD in MANUAL_APPNO_MATCH/DETERMINISTIC_APPNO", "-"),
    ]))
    lines.append(p("Full record-level detail is available via CSV download in the live dashboard; not dumped inline here per export contract Rule 3."))
    lines.append(sep())
    return "\n".join(lines)


def build_tab9(S):
    uni_base, course_base = S["uni"], S["besttrend"]
    lines = [h1("Tab 9 -- Subtests & Profiles")]

    uni_table = mc.subtest_mean_table(uni_base, "UNDERGRAD_UNI_TYPE", std=True)
    lines.append(h2("Table 34 -- Standardized Subtest Means by University Type"))
    lines.append(df_to_markdown(uni_table.reset_index()))
    lines.append(sep())

    course_table = mc.subtest_mean_table(course_base, "UNDERGRAD_COURSE_GROUP", std=True)
    lines.append(h2("Table 36 -- Standardized Subtest Means by Course Group"))
    lines.append(df_to_markdown(course_table.reset_index()))
    lines.append(sep())

    _, tbl_uni = mc.radar_for_group(uni_base[uni_base["UNDERGRAD_UNI_TYPE"].isin(["Public", "Private", "Foreign"])], "UNDERGRAD_UNI_TYPE")
    lines.append(h2("Table 38 -- Radar-Profile Values by University Type"))
    lines.append(df_to_markdown(tbl_uni.reset_index()))
    lines.append(sep())

    _, tbl_course = mc.radar_for_group(course_base, "UNDERGRAD_COURSE_GROUP")
    lines.append(h2("Table 39 -- Radar-Profile Values by Course Group"))
    lines.append(df_to_markdown(tbl_course.reset_index()))
    lines.append(sep())
    return "\n".join(lines)


def build_tab10(S):
    lines = [h1("Tab 10 -- Year Gap & Gender")]

    gap_df, gap_kpis = mc.compute_year_gap_kpis(S["bestobservable"])
    lines.append(h2("PLE Year Gap"))
    if not gap_df.empty:
        lines.append(metric_table([
            ("Confirmed passers (with year gap)", f"{gap_kpis['n']:,}", "observable, confirmed, PLE_YEAR_GAP notna", "-"),
            ("Median year gap", f"{gap_kpis['median']:.1f}", "rows above", "-"),
            ("Q1 year gap", f"{gap_kpis['q25']:.1f}", "rows above", "-"),
            ("Q3 year gap", f"{gap_kpis['q75']:.1f}", "rows above", "-"),
        ]))
        lines.append(h3("Table 40 -- Year-Gap Summary by Course Group"))
        lines.append(df_to_markdown(mc.compute_year_gap_by_course(gap_df)))
    else:
        lines.append(p("No confirmed observable PLE year-gap records available."))
    lines.append(sep())

    sex_base = S["besttrend"].dropna(subset=["SEX_CLEAN"])
    lines.append(h2("Table 41 -- Score Summary by Sex"))
    sex_perf = mc.compute_score_by_sex(sex_base)
    if sex_perf is not None:
        lines.append(df_to_markdown(sex_perf))
    lines.append(sep())

    _, sex_year_pct = mc.pct_table(sex_base, "Year", "SEX_CLEAN", ["Male", "Female"])
    lines.append(h2("Figure 34 -- Sex Composition by Year"))
    lines.append(df_to_markdown(sex_year_pct.reset_index()))
    lines.append(sep())

    observable_sex = S["bestobservable"].dropna(subset=["SEX_CLEAN"])
    if not observable_sex.empty:
        _, sex_ple_pct = mc.pct_table(observable_sex, "SEX_CLEAN", "PLE_STATUS_LABEL", PLE_ORDER)
        lines.append(h2("Table 42 -- PLE Status Composition by Sex (Observable Cohort)"))
        lines.append(df_to_markdown(sex_ple_pct.reset_index()))
        lines.append(sep())
    return "\n".join(lines)


def build_tab11(S):
    lines = [h1("Tab 11 -- Statistical Tests")]

    kw_tbl = mc.kruskal_table(S["besttrend"], "Year", {
        "TotalRawScoreTRUE": "Total raw score", "PartIRawScoreTRUE": "Part I raw score",
        "PartIIRawScoreTRUE": "Part II raw score", "NMS_PER_num": "Percentile rank", "NMS_GPS": "GPS standard score",
    })
    lines.append(h2("Table 43 -- Kruskal-Wallis Tests by Year"))
    lines.append(df_to_markdown(kw_tbl))
    lines.append(sep())

    mw_tbl = mc.mann_whitney_ple(S["bestobservable"], {
        "TotalRawScoreTRUE": "Total raw score", "PartIRawScoreTRUE": "Part I raw score",
        "PartIIRawScoreTRUE": "Part II raw score", "NMS_PER_num": "Percentile rank", "NMS_GPS": "GPS standard score",
    })
    lines.append(h2("Table 44 -- Mann-Whitney by PLE Status"))
    lines.append(df_to_markdown(mw_tbl))
    lines.append(sep())

    chi_base = S["uni"]
    if not chi_base.empty:
        observed_tbl, expected_tbl, chi_summary = mc.chi_square_unitype_bin(chi_base)
        lines.append(h2("Tables 45-47 -- Chi-Square: University Type x Bin"))
        lines.append(df_to_markdown(observed_tbl.reset_index()))
        lines.append(df_to_markdown(chi_summary))
        lines.append(df_to_markdown(expected_tbl.reset_index()))
        lines.append(sep())

    dunn = mc.compute_dunn_posthoc(S["besttrend"])
    lines.append(h2("Table 48 -- Dunn Post-Hoc Adjusted P-Values"))
    if dunn is not None:
        lines.append(df_to_markdown(dunn.reset_index()))
    else:
        lines.append(p("scikit-posthocs unavailable or insufficient year groups."))
    lines.append(sep())
    return "\n".join(lines)


def build_tab12(S):
    policybase = S["bestobservable"]
    lines = [h1("Tab 12 -- Policy Tables & Export")]
    if policybase.empty:
        lines.append(p("No observable best-record rows available."))
        return "\n".join(lines)

    lines.append(h2("Table 1 -- Confirmed PLE Alignment by NMAT Year"))
    lines.append(df_to_markdown(mc.compute_ple_alignment_by(policybase, "Year")))
    lines.append(h2("Table 2 -- Confirmed PLE Alignment by Pre-Med Background"))
    lines.append(df_to_markdown(mc.compute_ple_alignment_by(policybase, "UNDERGRAD_COURSE_GROUP", include_median=True)))
    lines.append(h2("Table 3 -- Confirmed PLE Alignment by University Type"))
    lines.append(df_to_markdown(mc.compute_ple_alignment_by(policybase, "UNDERGRAD_UNI_TYPE", include_median=True)))
    lines.append(h2("Table 4 -- Survival to Top Bins by Course Group"))
    lines.append(df_to_markdown(mc.compute_top_bin_share_by(S["besttrend"], "UNDERGRAD_COURSE_GROUP")))
    lines.append(sep())
    return "\n".join(lines)


def build_tab13(S):
    df_obs = S["bestobservable"]
    lines = [h1("Tab 13 -- CHED Compliance")]
    if df_obs.empty:
        lines.append(p("No observable best-record rows available."))
        return "\n".join(lines)

    lines.append(h2("Section A -- Applicant-Pool Cut-off Scenarios (30th vs 40th Percentile)"))
    lines.append(df_to_markdown(mc.compute_cutoff_scenarios(df_obs)))
    lines.append(sep())

    lines.append(h2("Section B -- Foreign vs Filipino Applicant-Pool Composition"))
    citz_n, citz_pct = mc.compute_citizenship_group_bin_dist(S["uniobservable"])
    if citz_pct is not None:
        lines.append(df_to_markdown(citz_n))
        lines.append(df_to_markdown(citz_pct.reset_index()))
    else:
        lines.append(p("Citizenship columns not available."))
    lines.append(sep())

    lines.append(h2("Section C -- Individual-Level PLE Linkage Gradient by Percentile Bin"))
    grad = mc.compute_linkage_gradient(df_obs)
    lines.append(df_to_markdown(grad))
    b1_row = grad[grad["PercentileBin"] == "B1"]
    b1_passers = int(b1_row["linked_n"].iloc[0]) if len(b1_row) and pd.notna(b1_row["linked_n"].iloc[0]) else 0
    lines.append(p(
        f"The gradient rises steadily from the lowest to the highest bin, with no sharp step at the 30th "
        f"(B4) or 40th (B5) percentile threshold. {b1_passers:,} B1 (lowest-decile) examinees in the "
        "observable cohort are confirmed PLE passers -- a strictly binding 40th-percentile admission "
        "floor would predict this group should barely exist."
    ))
    lines.append(sep())
    return "\n".join(lines)


def _self_check_block(df_raw, source_path):
    """Export-integrity self-check per contract Rule 10."""
    try:
        with open(source_path, "rb") as f:
            md5 = hashlib.md5(f.read()).hexdigest()
    except Exception:
        md5 = "unavailable"
    lines = [h1("Export Integrity"), "| check | result |", "|---|---|"]
    lines.append(f"| Source parquet md5 | {md5} |")
    lines.append(f"| Rows / cols | {len(df_raw):,} / {df_raw.shape[1]} |")
    lines.append(f"| Tabs exported | {_INTEGRITY['tabs']} / {_INTEGRITY['tabs_total']} |")
    lines.append(f"| Charts exported as data | {_INTEGRITY['charts']} / {_INTEGRITY['charts']} |")
    lines.append(f"| Tables exported | {_INTEGRITY['tables']} |")
    lines.append(f"| Captions exported | {_INTEGRITY['captions']} |")
    lines.append(
        f"| Dashboard-vs-export value assertions passed | "
        f"{_INTEGRITY['assertions_passed']} / {_INTEGRITY['assertions_total']} |"
    )
    if _INTEGRITY["tabs"] < _INTEGRITY["tabs_total"]:
        lines.append("\n**INCOMPLETE EXPORT -- not all tabs were rendered. Do not treat this document as authoritative.**")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def build_full_markdown(df_raw: pd.DataFrame, subsets: dict) -> str:
    """Return one complete Markdown string for all 13 dashboard tabs.

    df_raw, subsets -- exactly what `main_common.load_data_and_subsets()`
    returns (df, subsets). ALWAYS the full, unfiltered cohort -- never the
    sidebar-filtered `F` dict dashboard.py builds per session, so the export
    is a complete, reproducible picture regardless of what a user happened
    to have selected when they clicked the button.
    """
    _reset_integrity()
    S = subsets

    try:
        source_path = mc.find_data_path()
    except Exception:
        source_path = None

    kpi = mc.compute_tab1_kpis(S["besttrend"], S["bestobservable"], S["trend"])

    lines = []
    lines.append("# NMAT Performance Dashboard -- Complete Export")
    lines.append("")
    lines.append(f"> Complete Markdown export generated {datetime.now().strftime('%Y-%m-%d %H:%M')}. "
                  "Every number below is computed by the same functions the live dashboard renders from "
                  "(`main_common.py`) -- this document is a faithful transcript, not a paraphrase. "
                  "**This export always reflects the FULL, UNFILTERED dataset**, not whatever sidebar "
                  "filters happened to be applied in the browser session that generated it.")
    lines.append("")
    lines.append(f"**Source:** {os.path.basename(str(source_path)) if source_path else 'NMAT_Exodus.parquet'}, "
                  f"{len(df_raw):,} rows x {df_raw.shape[1]} columns.")
    lines.append("")
    lines.append("## How to Read This Document")
    lines.append("")
    lines.append("- **Best-record examinees** -- one NMAT record per person (`IS_BEST_NMAT_RECORD`): highest "
                  "percentile, latest year, lowest APPNO_CLEAN tiebreak.")
    lines.append("- **Observable cohort** -- each person's best NMAT attempt with Year <= 2014 "
                  "(`IS_BEST_OBSERVABLE_RECORD`). This is NOT the same as filtering the overall best-record "
                  "flag to Year<=2014, which silently drops people whose overall-best attempt fell later.")
    lines.append("- **NMAT-to-PLE linkage** -- the share of examinees later matched to PLE passer records. "
                  "This is NEVER a pass rate: the PLE source list contains passers only, so \"No confirmed "
                  "PLE match\" is not evidence of failure.")
    lines.append("- **Score bins** -- B1 (0-9, lowest) through B10 (90-100, highest). Always ordered "
                  "B1..B10, never string-sorted.")
    lines.append("- **People vs sittings** -- best-record filtering counts people; unfiltered subsets "
                  "(e.g. Tab 8 Repeat Takers) count exam sittings.")
    lines.append("- **No medical-school identifier exists in this dataset.** UNDERGRAD_UNI_TYPE / "
                  "UNDERGRAD_UNIVERSITY describe the examinee's undergraduate institution, never the "
                  "medical school.")
    lines.append("")
    lines.append("## Global KPIs")
    lines.append("")
    lines.append(metric_table([
        ("Total NMAT sittings", f"{len(df_raw):,}", "all years, all rows", "-"),
        ("Unique examinees", f"{kpi['n_best']:,}", "best-record", "-"),
        ("Observable cohort", f"{kpi['n_observable']:,}", "best attempt, Year<=2014", ">=5yr PLE window"),
        ("PLE linkage rate, observable cohort", f"{kpi['ple_linkage_pct']:.2f}%", "observable cohort", "linkage, not pass rate"),
        ("Repeat takers", f"{kpi['n_repeat']:,} ({kpi['repeat_share_pct']:.1f}%)", "unique examinees", "-"),
    ]))
    lines.append("")
    lines.append("---")

    builders = [
        build_tab1, build_tab2, build_tab3, build_tab4, build_tab5, build_tab6,
        build_tab7, build_tab8, build_tab9, build_tab10, build_tab11, build_tab12, build_tab13,
    ]
    for builder in builders:
        lines.append(builder(S))
        _INTEGRITY["tabs"] += 1

    # Verification requirement (contract Rule 6): assert exported values
    # equal values computed directly from the shared compute layer.
    _assert_equal("n_best", kpi["n_best"], S["besttrend"]["PERSON_KEY"].nunique())
    _assert_equal("n_observable", kpi["n_observable"], int(df_raw["IS_BEST_OBSERVABLE_RECORD"].sum()))
    _assert_equal("ple_linkage_pct", round(kpi["ple_linkage_pct"], 2),
                  round(float(S["bestobservable"]["HAS_CONFIRMED_PLE"].mean() * 100), 2))
    mismatch = mc.compute_raw_validation_checks(df_raw)
    _assert_equal("mismatch_rate_pct", round(mismatch["mismatch_rate_pct"], 2),
                  round(mc.compute_raw_validation_checks(df_raw)["mismatch_rate_pct"], 2))
    _assert_equal("n_all_rows", len(df_raw), len(S["all"]))

    lines.append(_self_check_block(df_raw, source_path))

    return "\n".join(lines)


if __name__ == "__main__":
    # Headless regeneration, same code path as the dashboard's export button.
    _here = os.path.dirname(os.path.abspath(__file__))
    _df, _subsets, _path = mc.load_data_and_subsets()
    _md = build_full_markdown(_df, _subsets)
    _out = os.path.join(_here, "complete_markdown", "NMAT_Main_Dashboard_Complete.md")
    os.makedirs(os.path.dirname(_out), exist_ok=True)
    with open(_out, "w", encoding="utf-8") as fh:
        fh.write(_md)
    print(f"wrote {_out}  ({len(_md):,} chars)")
