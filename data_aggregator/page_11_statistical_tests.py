"""
Page 11: Statistical Tests
Replicates ALL computations from dashboard.py tab11 (lines 2560-2802).
Extracts unfiltered data and saves to page_results/11_statistical_tests.md.

Produces complete raw output:
- Kruskal-Wallis tests (Year x scores, UNI_TYPE/CourseGroup/UNI_LOCATION x NMS_PER_num)
- Mann-Whitney U tests (PLE_STATUS_LABEL x scores, SEX_CLEAN x NMS_PER_num)
- Chi-square tests (UNI_TYPE x PercentileBin, CourseGroup x PercentileBin)
- Dunn post-hoc pairwise comparisons (UNI_TYPE, CourseGroup)
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "data_aggregator"))

import numpy as np
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 300)
pd.set_option("display.max_colwidth", 60)

from config import BIN_ORDER, RESULTS_DIR
from helpers import load_data

HAS_POSTHOCS = False
try:
    import scikit_posthocs as sp
    HAS_POSTHOCS = True
except ImportError:
    pass


# ─────────────────────────────────────────────
# Helper: Kruskal-Wallis with eta-squared
# ─────────────────────────────────────────────
def kruskal_table_full(df, group_col, score_cols):
    """
    Compute Kruskal-Wallis tests for multiple score columns.
    Returns full table with H-stat, p-value, eta-squared, effect label.
    """
    from scipy import stats as sp_stats

    results = []
    groups = df[group_col].dropna().unique()
    valid_groups = [g for g in groups if len(df[df[group_col] == g]) >= 5]

    for score_name, score_col in score_cols.items():
        if score_col not in df.columns:
            continue
        data = {}
        for g in valid_groups:
            vals = df[df[group_col] == g][score_col].dropna().values
            if len(vals) >= 5:
                data[g] = vals

        if len(data) < 2:
            continue

        h_stat, p_val = sp_stats.kruskal(*data.values())

        n_total = sum(len(v) for v in data.values())
        k = len(data)
        eta2 = (h_stat - k + 1) / (n_total - k) if n_total > k else 0
        eta2 = max(0, eta2)

        if eta2 < 0.01:
            effect = "Negligible"
        elif eta2 < 0.06:
            effect = "Small"
        elif eta2 < 0.14:
            effect = "Medium"
        else:
            effect = "Large"

        results.append({
            "Score Variable": score_name,
            "Groups (k)": k,
            "Total N": n_total,
            "H-statistic": round(h_stat, 4),
            "p-value": p_val,
            "Eta-squared": round(eta2, 4),
            "Effect Size": effect,
        })

    return pd.DataFrame(results)


# ─────────────────────────────────────────────
# Helper: Mann-Whitney U with effect size r
# ─────────────────────────────────────────────
def mannwhitney_table_full(df, group_col, score_cols):
    """
    Compute Mann-Whitney U tests for a binary group column.
    Returns median both groups, U-stat, p-value, effect size r, N1, N2.
    """
    from scipy import stats as sp_stats

    results = []
    groups = sorted(df[group_col].dropna().unique())
    if len(groups) != 2:
        # Try to find the two most common
        top2 = df[group_col].value_counts().head(2).index.tolist()
        if len(top2) < 2:
            return pd.DataFrame()
        groups = top2

    g1, g2 = groups

    for score_name, score_col in score_cols.items():
        if score_col not in df.columns:
            continue
        s1 = df[df[group_col] == g1][score_col].dropna()
        s2 = df[df[group_col] == g2][score_col].dropna()

        if len(s1) < 2 or len(s2) < 2:
            continue

        u_stat, p_val = sp_stats.mannwhitneyu(s1, s2, alternative="two-sided")

        n1, n2 = len(s1), len(s2)
        r = 1 - (2 * u_stat) / (n1 * n2)

        results.append({
            "Score Variable": score_name,
            f"Median ({g1})": round(s1.median(), 2),
            f"Median ({g2})": round(s2.median(), 2),
            "U-statistic": round(u_stat, 2),
            "p-value": p_val,
            "Effect size (r)": round(r, 4),
            "N1": n1,
            "N2": n2,
        })

    return pd.DataFrame(results)


# ─────────────────────────────────────────────
# Helper: Chi-square with Cramer's V
# ─────────────────────────────────────────────
def chi_square_table_full(df, row_col, col_col):
    """
    Compute Chi-square test of independence.
    Returns observed, expected, and summary (chi2, p, Cramer's V).
    """
    from scipy import stats as sp_stats

    contingency = pd.crosstab(df[row_col], df[col_col])
    chi2, p_val, dof, expected = sp_stats.chi2_contingency(contingency)

    n = contingency.sum().sum()
    min_dim = min(contingency.shape) - 1
    cramer_v = np.sqrt(chi2 / (n * min_dim)) if min_dim > 0 else 0

    expected_df = pd.DataFrame(
        expected,
        index=contingency.index,
        columns=contingency.columns,
    )

    return contingency, expected_df, {
        "chi2": round(chi2, 4),
        "p_value": p_val,
        "dof": dof,
        "Cramer's V": round(cramer_v, 4),
        "n": int(n),
    }


# ─────────────────────────────────────────────
# Helper: Add significance stars
# ─────────────────────────────────────────────
def sig_stars(p):
    if p < 0.001:
        return "***"
    elif p < 0.01:
        return "**"
    elif p < 0.05:
        return "*"
    else:
        return "ns"


def run() -> str:
    df, subsets = load_data()

    # Core subsets matching dashboard
    besttrend = subsets["besttrend"].copy()
    bestobservable = subsets["bestobservable"].copy()
    uni = subsets["uni"].copy()

    lines = []

    # ── Header ──
    lines.append("# Page 11: Statistical Tests")
    lines.append("")
    lines.append(f"**Generated:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("**Data source:** NMAT_Exodus_Lite.parquet (Pipeline 4)")
    lines.append("")
    lines.append("**Filters:** None (full unfiltered dataset)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ================================================================
    # SECTION 1: Kruskal-Wallis Tests
    # ================================================================
    lines.append("## Section 1: Kruskal-Wallis Tests")
    lines.append("")
    lines.append("Non-parametric alternative to one-way ANOVA. Tests whether samples originate from the same distribution. Eta-squared (effect size): Negligible (<0.01), Small (0.01-0.06), Medium (0.06-0.14), Large (>=0.14).")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- 1a. Year x Score variables ---
    lines.append("### 1a. Year × Score Distributions")
    lines.append("")
    lines.append("Testing whether score distributions differ across NMAT years (2006-2018).")
    lines.append("")

    score_map = {
        "Total Raw Score": "TotalRawScoreTRUE",
        "Part I Raw Score": "PartIRawScoreTRUE",
        "Part II Raw Score": "PartIIRawScoreTRUE",
        "Percentile Rank": "NMS_PER_num",
        "GPS Standard Score": "NMS_GPS",
    }
    kw_year = kruskal_table_full(besttrend, "Year", score_map)
    if not kw_year.empty:
        lines.append("**Table 43. Kruskal-Wallis tests for score distributions across NMAT years**")
        lines.append("")
        kw_year_disp = kw_year.copy()
        kw_year_disp["Sig."] = kw_year_disp["p-value"].apply(sig_stars)
        lines.append(kw_year_disp.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")
    else:
        lines.append("Not enough year-group data for Kruskal-Wallis tests.")
        lines.append("")

    # --- 1b. UNI_TYPE x NMS_PER_num ---
    lines.append("### 1b. University Type × Percentile Rank")
    lines.append("")
    lines.append("Testing whether percentile rank distributions differ by university type (Public, Private, Foreign).")
    lines.append("")

    kw_uni = kruskal_table_full(uni, "UNI_TYPE", {"Percentile Rank": "NMS_PER_num"})
    if not kw_uni.empty:
        lines.append("**Kruskal-Wallis: UNI_TYPE × NMS_PER_num**")
        lines.append("")
        kw_uni_disp = kw_uni.copy()
        kw_uni_disp["Sig."] = kw_uni_disp["p-value"].apply(sig_stars)
        lines.append(kw_uni_disp.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")
    else:
        lines.append("Not enough UNI_TYPE groups for Kruskal-Wallis.")
        lines.append("")

    # --- 1c. CourseGroup x NMS_PER_num ---
    lines.append("### 1c. Course Group × Percentile Rank")
    lines.append("")
    lines.append("Testing whether percentile rank distributions differ by CourseGroup.")
    lines.append("")

    kw_course = kruskal_table_full(besttrend, "CourseGroup", {"Percentile Rank": "NMS_PER_num"})
    if not kw_course.empty:
        lines.append("**Kruskal-Wallis: CourseGroup × NMS_PER_num**")
        lines.append("")
        kw_course_disp = kw_course.copy()
        kw_course_disp["Sig."] = kw_course_disp["p-value"].apply(sig_stars)
        lines.append(kw_course_disp.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")
    else:
        lines.append("Not enough CourseGroup data for Kruskal-Wallis.")
        lines.append("")

    # --- 1d. UNI_LOCATION x NMS_PER_num ---
    lines.append("### 1d. University Location × Percentile Rank")
    lines.append("")
    lines.append("Testing whether percentile rank distributions differ by university location (NCR vs Provincial).")
    lines.append("")

    kw_loc = kruskal_table_full(besttrend, "UNI_LOCATION", {"Percentile Rank": "NMS_PER_num"})
    if not kw_loc.empty:
        lines.append("**Kruskal-Wallis: UNI_LOCATION × NMS_PER_num**")
        lines.append("")
        kw_loc_disp = kw_loc.copy()
        kw_loc_disp["Sig."] = kw_loc_disp["p-value"].apply(sig_stars)
        lines.append(kw_loc_disp.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")
    else:
        lines.append("Not enough UNI_LOCATION groups for Kruskal-Wallis.")
        lines.append("")

    # ================================================================
    # SECTION 2: Mann-Whitney U Tests
    # ================================================================
    lines.append("---")
    lines.append("## Section 2: Mann-Whitney U Tests")
    lines.append("")
    lines.append("Two-sample non-parametric test for differences between independent groups. Effect size r (rank-biserial correlation): |r| ~ 0.1 small, ~0.3 medium, ~0.5 large.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- 2a. PLE_STATUS_LABEL x scores ---
    lines.append("### 2a. PLE Status × Score Variables")
    lines.append("")
    lines.append("Comparing confirmed PLE passers vs no confirmed PLE match across score variables. Uses observable best-record cohort (Year <= 2014).")
    lines.append("")

    ple_score_map = {
        "Total Raw Score": "TotalRawScoreTRUE",
        "Percentile Rank": "NMS_PER_num",
        "GPS Standard Score": "NMS_GPS",
        "Part I Raw Score": "PartIRawScoreTRUE",
        "Part II Raw Score": "PartIIRawScoreTRUE",
    }
    mw_ple = mannwhitney_table_full(bestobservable, "PLE_STATUS_LABEL", ple_score_map)
    if not mw_ple.empty:
        lines.append("**Table 44. Mann-Whitney comparisons by PLE status (observable cohort)**")
        lines.append("")
        mw_ple_disp = mw_ple.copy()
        mw_ple_disp["Sig."] = mw_ple_disp["p-value"].apply(sig_stars)
        lines.append(mw_ple_disp.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")
    else:
        lines.append("Not enough PLE status data for Mann-Whitney tests.")
        lines.append("")

    # --- 2b. SEX_CLEAN x NMS_PER_num ---
    lines.append("### 2b. Sex × Percentile Rank")
    lines.append("")
    lines.append("Comparing percentile rank distributions by sex.")
    lines.append("")

    # Check if SEX_CLEAN exists and has at least 2 groups
    if "SEX_CLEAN" in besttrend.columns:
        sex_groups = besttrend["SEX_CLEAN"].dropna().unique()
        if len(sex_groups) >= 2:
            mw_sex = mannwhitney_table_full(besttrend, "SEX_CLEAN", {"Percentile Rank": "NMS_PER_num"})
            if not mw_sex.empty:
                lines.append("**Mann-Whitney: SEX_CLEAN × NMS_PER_num**")
                lines.append("")
                mw_sex_disp = mw_sex.copy()
                mw_sex_disp["Sig."] = mw_sex_disp["p-value"].apply(sig_stars)
                lines.append(mw_sex_disp.to_markdown(index=False, tablefmt="pipe", numalign="right"))
                lines.append("")
            else:
                lines.append("Insufficient data for sex-based Mann-Whitney test.")
                lines.append("")
        else:
            lines.append("SEX_CLEAN column found but has fewer than 2 groups.")
            lines.append("")
    else:
        lines.append("SEX_CLEAN column not available in dataset.")
        lines.append("")

    # ================================================================
    # SECTION 3: Chi-Square Tests
    # ================================================================
    lines.append("---")
    lines.append("## Section 3: Chi-Square Tests of Independence")
    lines.append("")
    lines.append("Tests whether two categorical variables are independent. Cramer's V measures association strength (0-1).")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- 3a. UNI_TYPE x PercentileBin ---
    lines.append("### 3a. University Type × Percentile Bin")
    lines.append("")
    lines.append("Testing independence between university type and percentile bin classification. H0: UNI_TYPE and PercentileBin are independent.")
    lines.append("")

    if not uni.empty and "PercentileBin" in uni.columns:
        chi_uni_obs, chi_uni_exp, chi_uni_summary = chi_square_table_full(uni, "UNI_TYPE", "PercentileBin")

        lines.append("**Table 45. Observed counts — University type × Percentile bin**")
        lines.append("")
        lines.append(chi_uni_obs.to_markdown(tablefmt="pipe", numalign="right"))
        lines.append("")

        lines.append("**Table 46. Chi-square summary — University type × Percentile bin**")
        lines.append("")
        chi_summary_df = pd.DataFrame([chi_uni_summary])
        chi_summary_df["Sig."] = chi_summary_df["p_value"].apply(sig_stars)
        lines.append(chi_summary_df.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")

        lines.append("**Table 47. Expected counts (under independence)**")
        lines.append("")
        lines.append(chi_uni_exp.to_markdown(tablefmt="pipe", numalign="right"))
        lines.append("")

        # Row percentages
        row_pct = chi_uni_obs.div(chi_uni_obs.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(2)
        lines.append("**Row percentages (university type × bin)**")
        lines.append("")
        lines.append(row_pct.to_markdown(tablefmt="pipe", numalign="right"))
        lines.append("")
    else:
        lines.append("No university-type records or PercentileBin column available for chi-square testing.")
        lines.append("")

    # --- 3b. CourseGroup x PercentileBin ---
    lines.append("### 3b. Course Group × Percentile Bin")
    lines.append("")
    lines.append("Testing independence between course group and percentile bin classification.")
    lines.append("")

    if "PercentileBin" in besttrend.columns:
        chi_course_obs, chi_course_exp, chi_course_summary = chi_square_table_full(besttrend, "CourseGroup", "PercentileBin")

        lines.append("**Observed counts — CourseGroup × Percentile bin**")
        lines.append("")
        lines.append(chi_course_obs.to_markdown(tablefmt="pipe", numalign="right"))
        lines.append("")

        lines.append("**Chi-square summary — CourseGroup × Percentile bin**")
        lines.append("")
        chi_cs_df = pd.DataFrame([chi_course_summary])
        chi_cs_df["Sig."] = chi_cs_df["p_value"].apply(sig_stars)
        lines.append(chi_cs_df.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")

        lines.append("**Expected counts (under independence) — CourseGroup × Percentile bin**")
        lines.append("")
        lines.append(chi_course_exp.to_markdown(tablefmt="pipe", numalign="right"))
        lines.append("")

        # Row percentages
        row_pct_cg = chi_course_obs.div(chi_course_obs.sum(axis=1).replace(0, np.nan), axis=0).mul(100).round(2)
        lines.append("**Row percentages (CourseGroup × bin)**")
        lines.append("")
        lines.append(row_pct_cg.to_markdown(tablefmt="pipe", numalign="right"))
        lines.append("")
    else:
        lines.append("PercentileBin column not available.")
        lines.append("")

    # ================================================================
    # SECTION 4: Dunn Post-Hoc Tests
    # ================================================================
    lines.append("---")
    lines.append("## Section 4: Dunn Post-Hoc Pairwise Comparisons")
    lines.append("")
    lines.append("Bonferroni-adjusted pairwise comparisons following significant Kruskal-Wallis results.")
    lines.append("")
    lines.append("---")

    if not HAS_POSTHOCS:
        lines.append("")
        lines.append("*scikit-posthocs is not installed. Dunn post-hoc output requires `pip install scikit-posthocs`.*")
        lines.append("")
    else:
        # --- 4a. UNI_TYPE pairwise ---
        lines.append("### 4a. University Type — Pairwise (Dunn + Bonferroni)")
        lines.append("")
        lines.append("Pairwise comparisons of percentile rank across university types.")
        lines.append("")

        ph_uni = uni.dropna(subset=["UNI_TYPE", "NMS_PER_num"]).copy()
        if ph_uni["UNI_TYPE"].nunique() >= 3:
            dunn_uni = sp.posthoc_dunn(
                ph_uni, val_col="NMS_PER_num", group_col="UNI_TYPE",
                p_adjust="bonferroni",
            )
            dunn_uni.index = dunn_uni.index.astype(str)
            dunn_uni.columns = dunn_uni.columns.astype(str)

            lines.append("**Dunn post-hoc adjusted p-value matrix (Bonferroni) — UNI_TYPE × NMS_PER_num**")
            lines.append("")
            lines.append(dunn_uni.to_markdown(tablefmt="pipe", numalign="right"))
            lines.append("")

            # Also produce a long-format table
            pairs_uni = []
            for i, r1 in enumerate(dunn_uni.index):
                for j, c1 in enumerate(dunn_uni.columns):
                    if i < j:
                        if r1 in dunn_uni.columns and c1 in dunn_uni.index:
                            val = dunn_uni.loc[r1, c1]
                        else:
                            val = np.nan
                        pairs_uni.append({
                            "Group 1": r1,
                            "Group 2": c1,
                            "Adjusted p-value": val,
                            "Significant": val < 0.05 if pd.notna(val) else False,
                        })
            if pairs_uni:
                pairs_uni_df = pd.DataFrame(pairs_uni)
                lines.append("**Table 48. Dunn post-hoc pairwise summary — UNI_TYPE**")
                lines.append("")
                lines.append(pairs_uni_df.to_markdown(index=False, tablefmt="pipe", numalign="right"))
                lines.append("")
        else:
            lines.append("Insufficient UNI_TYPE groups for post-hoc testing.")
            lines.append("")

        # --- 4b. CourseGroup pairwise ---
        lines.append("### 4b. Course Group — Pairwise (Dunn + Bonferroni)")
        lines.append("")
        lines.append("Pairwise comparisons of percentile rank across course groups.")
        lines.append("")

        ph_course = besttrend.dropna(subset=["CourseGroup", "NMS_PER_num"]).copy()
        if ph_course["CourseGroup"].nunique() >= 3:
            dunn_course = sp.posthoc_dunn(
                ph_course, val_col="NMS_PER_num", group_col="CourseGroup",
                p_adjust="bonferroni",
            )
            dunn_course.index = dunn_course.index.astype(str)
            dunn_course.columns = dunn_course.columns.astype(str)

            lines.append("**Dunn post-hoc adjusted p-value matrix (Bonferroni) — CourseGroup × NMS_PER_num**")
            lines.append("")
            lines.append(dunn_course.to_markdown(tablefmt="pipe", numalign="right"))
            lines.append("")

            # Long-format table
            pairs_cg = []
            for i, r1 in enumerate(dunn_course.index):
                for j, c1 in enumerate(dunn_course.columns):
                    if i < j:
                        if r1 in dunn_course.columns and c1 in dunn_course.index:
                            val = dunn_course.loc[r1, c1]
                        else:
                            val = np.nan
                        pairs_cg.append({
                            "Group 1": r1,
                            "Group 2": c1,
                            "Adjusted p-value": val,
                            "Significant": val < 0.05 if pd.notna(val) else False,
                        })
            if pairs_cg:
                pairs_cg_df = pd.DataFrame(pairs_cg)
                lines.append("**Dunn post-hoc pairwise summary — CourseGroup**")
                lines.append("")
                lines.append(pairs_cg_df.to_markdown(index=False, tablefmt="pipe", numalign="right"))
                lines.append("")
        else:
            lines.append("Insufficient CourseGroup groups for post-hoc testing.")
            lines.append("")

        # --- 4c. Year pairwise (original dashboard behavior) ---
        lines.append("### 4c. Year — Pairwise (Dunn + Bonferroni)")
        lines.append("")
        lines.append("Pairwise comparisons of percentile rank across NMAT years (2006-2018).")
        lines.append("")

        ph_year = besttrend.dropna(subset=["Year", "NMS_PER_num"]).copy()
        if ph_year["Year"].nunique() >= 3:
            dunn_year = sp.posthoc_dunn(
                ph_year, val_col="NMS_PER_num", group_col="Year",
                p_adjust="bonferroni",
            )
            dunn_year.index = dunn_year.index.astype(str)
            dunn_year.columns = dunn_year.columns.astype(str)

            lines.append("**Dunn post-hoc adjusted p-value matrix (Bonferroni) — Year × NMS_PER_num**")
            lines.append("")
            lines.append(dunn_year.to_markdown(tablefmt="pipe", numalign="right"))
            lines.append("")
        else:
            lines.append("Insufficient Year groups for post-hoc testing.")
            lines.append("")

    # ── Footer ──
    lines.append("---")
    lines.append("")
    lines.append("*Significance codes: *** p<0.001, ** p<0.01, * p<0.05, ns not significant*")
    lines.append("")

    return "\n".join(lines)


def save():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = RESULTS_DIR / "11_statistical_tests.md"
    content = run()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved: {out_path.resolve()}")


if __name__ == "__main__":
    save()
