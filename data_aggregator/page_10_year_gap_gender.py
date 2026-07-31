"""
Page 10 — PLE Year Gap and Gender Patterns
=============================================
Output: page_results/10_year_gap_gender.md

Analyses:
  1. PLE year gap distribution: n, median gap, min, max, quartiles
  2. PLE year gap by UNDERGRAD_COURSE_GROUP (n, median, q25, q75, median percentile)
  3. Gender composition: Male/Female counts and % overall
  4. Gender by year: Male/Female counts and % per year
  5. Gender score comparison: median %ile, median raw for Male vs Female
  6. Mann-Whitney for Sex x NMS_PER_num
  7. Sex x PLE status: counts and linkage rates (observable cohort)
  8. PLE year gap by gender

Data subsets:
  - besttrend (gender composition, score comparison, MW)
  - bestobservable (PLE gap, PLE status, PLE gap by gender)
Filters: None (full unfiltered dataset)
"""
import sys
import os
sys.path.append("data_aggregator")

import numpy as np
import pandas as pd
from scipy import stats as sp_stats

from config import PLE_ORDER, EXODUS_PARQUET, RESULTS_DIR
from helpers import write_header, write_dataframe, pct_table

MD_PATH = RESULTS_DIR / "10_year_gap_gender.md"


def load_subsets():
    """Load besttrend and bestobservable subsets."""
    import pyarrow.parquet as pq
    table = pq.read_table(EXODUS_PARQUET)
    df = table.to_pandas()
    del table

    # Derived columns
    if "SEX_CLEAN" not in df.columns:
        sex_source = None
        for c in ["SEX", "NMASex"]:
            if c in df.columns:
                sex_source = c
                break
        if sex_source is not None:
            s = df[sex_source].astype(str).str.strip().str.title()
            s = s.replace({"1": "Male", "2": "Female"})
            s = s.where(s.isin(["Male", "Female"]), None)
            df["SEX_CLEAN"] = s
        else:
            df["SEX_CLEAN"] = None

    if "PLE_STATUS_LABEL" not in df.columns:
        df["PLE_STATUS_LABEL"] = np.where(
            df["IS_PLE_PASSER"] == True,
            "Confirmed PLE passer", "No confirmed PLE match"
        )
    if "IS_OBSERVABLE_COHORT" not in df.columns:
        df["IS_OBSERVABLE_COHORT"] = df["Year"] <= 2014

    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")

    # besttrend
    mask_besttrend = (
        (df.get("IS_BEST_NMAT_RECORD", pd.Series([True] * len(df))) == True)
        & (df["Year"].between(2006, 2018, inclusive="both"))
    )
    besttrend = df.loc[mask_besttrend].copy()

    # bestobservable: best attempt WITHIN Year<=2014 (IS_BEST_OBSERVABLE_RECORD), not
    # best-overall & Year<=2014 — that naive combination drops people whose
    # overall-best attempt landed after 2014 (see _TARGET_SCHEMA_CONTRACT.md §2a).
    bestobservable = df.loc[df["IS_BEST_OBSERVABLE_RECORD"] == True].copy()

    del df
    return besttrend, bestobservable


def write_section_gap_distribution(f, bestobservable):
    """1. PLE year gap distribution: n, median gap, min, max, quartiles."""
    f.write("## 1. PLE Year Gap Distribution\n\n")

    gap_df = bestobservable[
        (bestobservable["PLE_STATUS_LABEL"] == "Confirmed PLE passer")
        & (bestobservable["PLE_YEAR_GAP"].notna())
    ].copy()

    if gap_df.empty:
        f.write("*No confirmed observable PLE year-gap records available.*\n\n")
        return gap_df

    gaps = gap_df["PLE_YEAR_GAP"]

    f.write(f"- **Confirmed passers:** {len(gap_df):,}\n")
    f.write(f"- **Median year gap:** {gaps.median():.1f}\n")
    f.write(f"- **Mean year gap:** {gaps.mean():.2f}\n")
    f.write(f"- **Std year gap:** {gaps.std():.2f}\n")
    f.write(f"- **Min year gap:** {gaps.min():.1f}\n")
    f.write(f"- **Max year gap:** {gaps.max():.1f}\n")
    f.write(f"- **Q1 (25th pctile):** {gaps.quantile(0.25):.1f}\n")
    f.write(f"- **Q3 (75th pctile):** {gaps.quantile(0.75):.1f}\n")
    f.write(f"- **IQR:** {gaps.quantile(0.75) - gaps.quantile(0.25):.1f}\n\n")

    # Full distribution table by year gap value
    gap_counts = gap_df["PLE_YEAR_GAP"].value_counts().sort_index().reset_index()
    gap_counts.columns = ["PLE_YEAR_GAP", "Count"]
    f.write("**Table 41. Full PLE year gap distribution**\n\n")
    write_dataframe(f, gap_counts, None)
    f.write("---\n\n")

    return gap_df


def write_section_gap_by_course(f, bestobservable):
    """2. PLE year gap by UNDERGRAD_COURSE_GROUP."""
    f.write("## 2. PLE Year Gap by UNDERGRAD_COURSE_GROUP\n\n")

    gap_df = bestobservable[
        (bestobservable["PLE_STATUS_LABEL"] == "Confirmed PLE passer")
        & (bestobservable["PLE_YEAR_GAP"].notna())
        & (bestobservable["UNDERGRAD_COURSE_GROUP"].notna())
    ].copy()

    if gap_df.empty:
        f.write("*No data available.*\n\n")
        return

    gap_summary = (
        gap_df.groupby("UNDERGRAD_COURSE_GROUP", observed=True)
        .agg(
            confirmed_passers=("PERSON_KEY", "nunique"),
            median_year_gap=("PLE_YEAR_GAP", "median"),
            mean_year_gap=("PLE_YEAR_GAP", "mean"),
            std_year_gap=("PLE_YEAR_GAP", "std"),
            q25_year_gap=("PLE_YEAR_GAP", lambda x: x.quantile(0.25)),
            q75_year_gap=("PLE_YEAR_GAP", lambda x: x.quantile(0.75)),
            min_year_gap=("PLE_YEAR_GAP", "min"),
            max_year_gap=("PLE_YEAR_GAP", "max"),
            median_percentile=("NMS_PER_num", "median"),
        )
        .reset_index()
        .sort_values("median_year_gap")
        .round(2)
    )

    write_dataframe(f, gap_summary, "Table 42. Year-gap summary by course group")
    f.write("---\n\n")


def write_section_gender_composition(f, besttrend):
    """3. Gender composition: Male/Female counts and % overall."""
    f.write("## 3. Gender Composition (Overall)\n\n")

    sex_base = besttrend.dropna(subset=["SEX_CLEAN"]).copy()

    if sex_base.empty:
        f.write("*No sex-coded records available.*\n\n")
        return

    counts = sex_base["SEX_CLEAN"].value_counts()
    pcts = sex_base["SEX_CLEAN"].value_counts(normalize=True).mul(100).round(2)

    comp = pd.DataFrame({
        "Sex": counts.index,
        "Count": counts.values,
        "Percent": pcts.values,
    }).reset_index(drop=True)

    write_dataframe(f, comp, "Table 43. Gender composition (besttrend)")
    f.write("---\n\n")


def write_section_gender_by_year(f, besttrend):
    """4. Gender by year: Male/Female counts and % per year."""
    f.write("## 4. Gender by Year\n\n")

    sex_base = besttrend.dropna(subset=["SEX_CLEAN"]).copy()
    if sex_base.empty:
        f.write("*No sex-coded records available.*\n\n")
        return

    ct, pct = pct_table(sex_base, "Year", "SEX_CLEAN", ["Male", "Female"])

    f.write("**Table 44. Gender counts by NMAT year**\n\n")
    write_dataframe(f, ct.reset_index(), None)
    f.write("\n")

    f.write("**Table 45. Gender percentages by NMAT year**\n\n")
    write_dataframe(f, pct.reset_index(), None)
    f.write("---\n\n")


def write_section_gender_score_comparison(f, besttrend):
    """5. Gender score comparison: median %ile, median raw for Male vs Female."""
    f.write("## 5. Gender Score Comparison\n\n")

    sex_base = besttrend.dropna(subset=["SEX_CLEAN"]).copy()
    if sex_base.empty:
        f.write("*No sex-coded records available.*\n\n")
        return

    sex_perf = (
        sex_base.groupby("SEX_CLEAN", observed=True)
        .agg(
            n=("PERSON_KEY", "nunique"),
            median_raw=("TotalRawScoreTRUE", "median"),
            mean_raw=("TotalRawScoreTRUE", "mean"),
            std_raw=("TotalRawScoreTRUE", "std"),
            median_pct=("NMS_PER_num", "median"),
            mean_pct=("NMS_PER_num", "mean"),
            std_pct=("NMS_PER_num", "std"),
            median_gps=("NMS_GPS", "median"),
            median_apt=("NMS_APT", "median"),
            median_sa=("NMS_SA", "median"),
        )
        .reset_index()
        .round(2)
    )

    write_dataframe(f, sex_perf, "Table 46. Score summary by sex")
    f.write("---\n\n")


def write_section_mannwhitney(f, besttrend):
    """6. Mann-Whitney for Sex x NMS_PER_num (percentile) and other key scores."""
    f.write("## 6. Mann-Whitney U Tests: Sex x NMS_PER_num and Key Scores\n\n")

    sex_base = besttrend.dropna(subset=["SEX_CLEAN"]).copy()
    groups = sex_base["SEX_CLEAN"].dropna().unique()
    if len(groups) != 2:
        f.write("*Expected exactly 2 sex groups for Mann-Whitney test.*\n\n")
        return

    g1_label, g2_label = sorted(groups)  # consistent ordering

    score_cols = {
        "Percentile Rank (NMS_PER_num)": "NMS_PER_num",
        "Total Raw Score": "TotalRawScoreTRUE",
        "Part I Raw Score": "PartIRawScoreTRUE",
        "Part II Raw Score": "PartIIRawScoreTRUE",
        "GPS Standard Score": "NMS_GPS",
        "APT Standard Score": "NMS_APT",
        "SA Standard Score": "NMS_SA",
    }

    results = []
    g1 = sex_base[sex_base["SEX_CLEAN"] == g1_label]
    g2 = sex_base[sex_base["SEX_CLEAN"] == g2_label]

    for label, col in score_cols.items():
        if col not in sex_base.columns:
            continue
        a = g1[col].dropna()
        b = g2[col].dropna()
        if len(a) < 5 or len(b) < 5:
            continue

        u_stat, p_val = sp_stats.mannwhitneyu(a, b, alternative="two-sided")
        r = 1 - (2 * u_stat) / (len(a) * len(b))

        results.append({
            "Score Variable": label,
            f"Median ({g1_label})": round(float(a.median()), 2),
            f"Median ({g2_label})": round(float(b.median()), 2),
            "U-statistic": round(float(u_stat), 2),
            "p-value": "<0.001" if p_val < 0.001 else round(float(p_val), 4),
            "Effect size (r)": round(float(r), 4),
            "N1": len(a),
            "N2": len(b),
        })

    if not results:
        f.write("*Insufficient data for Mann-Whitney tests.*\n\n")
    else:
        mw_df = pd.DataFrame(results)
        write_dataframe(f, mw_df, "Table 47. Mann-Whitney U tests: Sex differences in key scores")
    f.write("---\n\n")


def write_section_sex_ple_status(f, bestobservable):
    """7. Sex x PLE status: counts and linkage rates (observable cohort)."""
    f.write("## 7. Sex x PLE Status (Observable Cohort)\n\n")

    obs_sex = bestobservable.dropna(subset=["SEX_CLEAN"]).copy()
    if obs_sex.empty:
        f.write("*No sex-coded observable records available.*\n\n")
        return

    ct, pct = pct_table(obs_sex, "SEX_CLEAN", "PLE_STATUS_LABEL", PLE_ORDER)

    f.write("**Table 48. PLE status counts by sex (observable cohort)**\n\n")
    write_dataframe(f, ct.reset_index(), None)
    f.write("\n")

    f.write("**Table 49. PLE status percentages by sex (observable cohort)**\n\n")
    write_dataframe(f, pct.reset_index(), None)

    # Linkage rate: % confirmed PLE passer within each sex
    f.write("\n")
    f.write("**Table 50. Confirmed PLE linkage rate by sex**\n\n")
    linkage_rate = (
        obs_sex.groupby("SEX_CLEAN", observed=True)
        .apply(
            lambda x: pd.Series({
                "total": len(x),
                "confirmed_passers": int(x["PLE_STATUS_LABEL"].eq("Confirmed PLE passer").sum()),
                "linkage_rate_pct": round(x["PLE_STATUS_LABEL"].eq("Confirmed PLE passer").mean() * 100, 2),
            })
        )
        .reset_index()
    )
    write_dataframe(f, linkage_rate, None)

    # Chi-square test: Sex x PLE status
    try:
        contingency = pd.crosstab(obs_sex["SEX_CLEAN"], obs_sex["PLE_STATUS_LABEL"])
        chi2, chi_p, chi_dof, expected = sp_stats.chi2_contingency(contingency)
        n = contingency.sum().sum()
        min_dim = min(contingency.shape) - 1
        cramer_v = np.sqrt(chi2 / (n * min_dim)) if min_dim > 0 else 0

        f.write("\n")
        f.write("**Table 51. Chi-square test: Sex x PLE status**\n\n")
        chi_df = pd.DataFrame([{
            "Chi-square": round(chi2, 4),
            "p-value": "<0.001" if chi_p < 0.001 else round(chi_p, 4),
            "df": int(chi_dof),
            "N": int(n),
            "Cramer's V": round(cramer_v, 4),
        }])
        write_dataframe(f, chi_df, None)
    except Exception as e:
        f.write(f"\n*Chi-square test could not be computed: {e}*\n\n")

    f.write("---\n\n")


def write_section_gap_by_gender(f, bestobservable):
    """8. PLE year gap by gender."""
    f.write("## 8. PLE Year Gap by Gender\n\n")

    gap_df = bestobservable[
        (bestobservable["PLE_STATUS_LABEL"] == "Confirmed PLE passer")
        & (bestobservable["PLE_YEAR_GAP"].notna())
        & (bestobservable["SEX_CLEAN"].notna())
    ].copy()

    if gap_df.empty:
        f.write("*No confirmed observable PLE year-gap records with sex coding available.*\n\n")
        return

    gap_by_sex = (
        gap_df.groupby("SEX_CLEAN", observed=True)
        .agg(
            n=("PERSON_KEY", "nunique"),
            median_gap=("PLE_YEAR_GAP", "median"),
            mean_gap=("PLE_YEAR_GAP", "mean"),
            std_gap=("PLE_YEAR_GAP", "std"),
            min_gap=("PLE_YEAR_GAP", "min"),
            max_gap=("PLE_YEAR_GAP", "max"),
            q25_gap=("PLE_YEAR_GAP", lambda x: x.quantile(0.25)),
            q75_gap=("PLE_YEAR_GAP", lambda x: x.quantile(0.75)),
        )
        .reset_index()
        .round(2)
    )

    write_dataframe(f, gap_by_sex, "Table 52. PLE year gap summary by sex")

    # Mann-Whitney test: Sex x PLE_YEAR_GAP
    groups = gap_df["SEX_CLEAN"].dropna().unique()
    if len(groups) == 2:
        g1_label, g2_label = sorted(groups)
        g1 = gap_df[gap_df["SEX_CLEAN"] == g1_label]["PLE_YEAR_GAP"]
        g2 = gap_df[gap_df["SEX_CLEAN"] == g2_label]["PLE_YEAR_GAP"]

        if len(g1) >= 5 and len(g2) >= 5:
            u_stat, p_val = sp_stats.mannwhitneyu(g1, g2, alternative="two-sided")
            r = 1 - (2 * u_stat) / (len(g1) * len(g2))

            f.write("\n")
            f.write("**Table 53. Mann-Whitney test: Sex differences in PLE year gap**\n\n")
            mw_df = pd.DataFrame([{
                "Group 1": g1_label,
                "Group 2": g2_label,
                f"Median ({g1_label})": round(float(g1.median()), 2),
                f"Median ({g2_label})": round(float(g2.median()), 2),
                "U-statistic": round(float(u_stat), 2),
                "p-value": "<0.001" if p_val < 0.001 else round(float(p_val), 4),
                "Effect size (r)": round(float(r), 4),
                "N1": len(g1),
                "N2": len(g2),
            }])
            write_dataframe(f, mw_df, None)

    f.write("---\n\n")


def run():
    """Run all analyses and write to markdown."""
    print("[Page 10] Loading data...")
    besttrend, bestobservable = load_subsets()
    print(f"  besttrend:       {len(besttrend):,} records")
    print(f"  bestobservable:  {len(bestobservable):,} records")

    print("[Page 10] Computing analyses...")
    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(MD_PATH, "w", encoding="utf-8") as f:
        write_header(f, "Page 10: PLE Year Gap and Gender Patterns",
                     "besttrend / bestobservable", 10)

        write_section_gap_distribution(f, bestobservable)
        write_section_gap_by_course(f, bestobservable)
        write_section_gender_composition(f, besttrend)
        write_section_gender_by_year(f, besttrend)
        write_section_gender_score_comparison(f, besttrend)
        write_section_mannwhitney(f, besttrend)
        write_section_sex_ple_status(f, bestobservable)
        write_section_gap_by_gender(f, bestobservable)

    print(f"[Page 10] Written to {MD_PATH}")


def save():
    """Alias for run()."""
    run()


if __name__ == "__main__":
    run()
