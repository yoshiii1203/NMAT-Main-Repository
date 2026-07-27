"""
05_demographic_profiles.py — Demographic, gender, course, and temporal trends.

Computes (renamed mentally to 05_gender_course_trends):
  - By SEX: NMAT performance, PLE linkage
  - By CourseGroup: NMAT performance, PLE linkage
  - Repeat taker rate (% of examinees with >1 attempt)
  - Course group performance table (n, median percentile, PLE linkage)
  - PLE year gap distribution (median gap, min, max, distribution)
  - Yearly trend summary (n, median percentile, median raw score)
  - Metric cards + comparison tables
"""

import sys
import os
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from config import BIN_ORDER, UNI_TYPE_ORDER
from helpers import (
    load_data,
    create_subsets,
    today_str,
    write_md,
    pct,
    fmt,
    make_metric_table,
    compute_linkage_rate,
    write_output,
)

SCRIPT = "05_demographic_profiles"
TITLE = "Demographic Profiles: NMAT Performance and PLE Linkage"

def compute():
    df = load_data()
    subsets = create_subsets(df)
    best = subsets["best"]
    obs = subsets["best_pre2015"]

    lines = []
    lines.append("## Results\n")
    lines.append(
        "This section examines NMAT performance and PLE linkage across demographic "
        "dimensions: sex, course group, repeat taker status, and PLE year gap."
    )
    lines.append("")

    # ────────────────────────────────────────────────────────────────────
    # 1) SEX (Gender) Analysis
    # ────────────────────────────────────────────────────────────────────
    lines.append("### Sex-Based Analysis\n")
    sex_counts = best["SEX"].value_counts(dropna=False)
    total_known_sex = sex_counts.get("Female", 0) + sex_counts.get("Male", 0)
    sex_unknown = sex_counts.get(np.nan, 0)

    sex_metrics = [
        ("Female Examinees", fmt(int(sex_counts.get("Female", 0)))),
        ("Male Examinees", fmt(int(sex_counts.get("Male", 0)))),
        ("Sex Not Specified", fmt(int(sex_unknown))),
    ]

    for sex_label in ["Female", "Male"]:
        sub = best[best["SEX"] == sex_label]
        med = sub["NMS_PER_num"].median()
        q1 = sub["NMS_PER_num"].quantile(0.25)
        q3 = sub["NMS_PER_num"].quantile(0.75)
        mean = sub["NMS_PER_num"].mean()
        sex_metrics.append(
            (f"{sex_label} Median Percentile", f"{med:.1f} (Q1: {q1:.1f}, Q3: {q3:.1f})")
        )

    lines.append(make_metric_table(sex_metrics))
    lines.append("")

    lines.append("#### Sex Comparison Table\n")
    sex_perf_header = "| Metric | Female | Male | Difference |"
    sex_perf_sep = "|--------|:-----:|:----:|:----------:|"
    lines.append(sex_perf_header)
    lines.append(sex_perf_sep)

    f_sub = best[best["SEX"] == "Female"]
    m_sub = best[best["SEX"] == "Male"]

    metrics_list = [
        ("n", len(f_sub), len(m_sub), None),
        ("Median Percentile", f_sub["NMS_PER_num"].median(), m_sub["NMS_PER_num"].median(), None),
        ("Mean Percentile", f_sub["NMS_PER_num"].mean(), m_sub["NMS_PER_num"].mean(), None),
        ("Median TotalRawScore", f_sub["TotalRawScoreTRUE"].median(), m_sub["TotalRawScoreTRUE"].median(), None),
    ]

    for label, f_val, m_val, _ in metrics_list:
        if isinstance(f_val, (int, np.integer)):
            diff = f_val - m_val
            lines.append(f"| {label} | {f_val:,} | {m_val:,} | {diff:+,} |")
        else:
            diff = f_val - m_val
            lines.append(f"| {label} | {f_val:.2f} | {m_val:.2f} | {diff:+.2f} |")

    lines.append("")

    # PLE linkage by sex
    lines.append("#### PLE Linkage by Sex\n")
    lines.append("NMAT-to-PLE linkage rates by sex (pre-2015 cohort, best-record basis).\n")

    ple_sex_header = "| Sex | n (Pre-2015) | PLE Matched | NMAT-to-PLE Linkage Rate |"
    ple_sex_sep = "|:----|:------------:|:-----------:|:------------------------:|"
    lines.append(ple_sex_header)
    lines.append(ple_sex_sep)

    for sex_label in ["Female", "Male"]:
        sub_obs = obs[obs["SEX"] == sex_label]
        n_obs = len(sub_obs)
        n_ple = int(sub_obs["IS_PLE_PASSER"].sum())
        lr = (n_ple / n_obs * 100) if n_obs > 0 else 0
        lines.append(f"| {sex_label} | {n_obs:,} | {n_ple:,} | {lr:.2f}% |")

    lines.append("")

    # ────────────────────────────────────────────────────────────────────
    # 2) Repeat Taker Rate
    # ────────────────────────────────────────────────────────────────────
    lines.append("### Repeat Taker Analysis\n")
    lines.append(
        "Repeat takers are persons with more than one NMAT attempt. "
        "The repeat taker rate quantifies how many unique examinees retake the exam.\n"
    )

    person_attempts = df.groupby("PERSON_KEY").size()
    repeat_takers = int((person_attempts > 1).sum())
    total_persons = len(person_attempts)
    repeat_rate = (repeat_takers / total_persons * 100) if total_persons > 0 else 0

    # Distribution of attempt counts
    attempt_dist = person_attempts.value_counts().sort_index()

    repeat_metrics = [
        ("Total Unique Persons (PERSON_KEY)", fmt(total_persons)),
        ("Repeat Takers (>1 attempt)", fmt(repeat_takers)),
        ("Repeat Taker Rate", f"{repeat_rate:.2f}%"),
        ("Single Attempt Only", fmt(total_persons - repeat_takers)),
    ]
    lines.append(make_metric_table(repeat_metrics))
    lines.append("")

    lines.append("#### Attempt Count Distribution\n")
    att_header = "| Attempts | Persons | % of Total |"
    att_sep = "|:--------:|:-------:|:----------:|"
    lines.append(att_header)
    lines.append(att_sep)
    for n_att, n_persons in attempt_dist.head(10).items():
        lines.append(f"| {int(n_att)} | {n_persons:,} | {n_persons/total_persons*100:.2f}% |")
    lines.append("")

    # ────────────────────────────────────────────────────────────────────
    # 3) Course Group Performance
    # ────────────────────────────────────────────────────────────────────
    lines.append("### Course Group Performance\n")
    lines.append(
        "NMAT performance and PLE linkage by course group "
        "(best-record basis).\n"
    )

    cg_counts = best["CourseGroup"].value_counts()
    total_cg = len(best)

    cg_perf_header = "| Course Group | n | % of Total | Median Pctl | Q1 Pctl | Q3 Pctl | Median Raw |"
    cg_perf_sep = "|:-------------|:--:|:----------:|:-----------:|:-------:|:-------:|:----------:|"
    lines.append(cg_perf_header)
    lines.append(cg_perf_sep)

    for cg in cg_counts.index:
        sub = best[best["CourseGroup"] == cg]
        n = len(sub)
        med = sub["NMS_PER_num"].median()
        q1 = sub["NMS_PER_num"].quantile(0.25)
        q3 = sub["NMS_PER_num"].quantile(0.75)
        med_raw = sub["TotalRawScoreTRUE"].median()
        lines.append(
            f"| {cg} | {n:,} | {n/total_cg*100:.1f}% | {med:.1f} | "
            f"{q1:.1f} | {q3:.1f} | {med_raw:.0f} |"
        )

    lines.append("")

    # Course group x PercentileBin heatmap
    lines.append("#### Course Group x PercentileBin Distribution\n")
    lines.append("Percentage of each course group's examinees in each percentile bin.\n")

    cg_bin_header = "| PercentileBin | " + " | ".join(str(cg) for cg in cg_counts.index) + " |"
    cg_bin_sep = "|:------------:|" + "|".join([":---:"] * len(cg_counts)) + "|"
    lines.append(cg_bin_header)
    lines.append(cg_bin_sep)

    for b in BIN_ORDER:
        row = [b]
        for cg in cg_counts.index:
            sub = best[best["CourseGroup"] == cg]
            n_bin = int((sub["PercentileBin"] == b).sum())
            pct_bin = n_bin / len(sub) * 100 if len(sub) > 0 else 0
            row.append(f"{pct_bin:.2f}%")
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # Course group PLE linkage
    lines.append("#### NMAT-to-PLE Linkage by Course Group\n")
    lines.append(
        "NMAT-to-PLE linkage rates by course group (observable cohort, Year <= 2014, "
        "best-record basis).\n"
    )

    ple_cg_header = "| Course Group | n (Observable) | PLE Matched | NMAT-to-PLE Linkage Rate |"
    ple_cg_sep = "|:-------------|:--------------:|:-----------:|:------------------------:|"
    lines.append(ple_cg_header)
    lines.append(ple_cg_sep)

    for cg in obs["CourseGroup"].value_counts().index:
        sub_obs = obs[obs["CourseGroup"] == cg]
        n_obs = len(sub_obs)
        n_ple = int(sub_obs["IS_PLE_PASSER"].sum())
        lr = (n_ple / n_obs * 100) if n_obs > 0 else 0
        lines.append(f"| {cg} | {n_obs:,} | {int(n_ple):,} | {lr:.2f}% |")

    lines.append("")

    # ────────────────────────────────────────────────────────────────────
    # 4) PLE Year Gap Distribution
    # ────────────────────────────────────────────────────────────────────
    lines.append("### PLE Year Gap Distribution\n")
    lines.append(
        "For examinees matched to PLE passer records, the gap (in years) between NMAT "
        "and PLE. This indicates how long after NMAT examinees typically pass PLE.\n"
    )

    ple_gap = obs["PLE_YEAR_GAP"].dropna()
    if len(ple_gap) > 0:
        gap_median = ple_gap.median()
        gap_min = ple_gap.min()
        gap_max = ple_gap.max()
        gap_mean = ple_gap.mean()

        gap_metrics = [
            ("Matched Examinees with Gap Data", fmt(len(ple_gap))),
            ("Median NMAT-to-PLE Gap", f"{gap_median:.0f} years"),
            ("Mean NMAT-to-PLE Gap", f"{gap_mean:.1f} years"),
            ("Minimum Gap", f"{gap_min:.0f} years"),
            ("Maximum Gap", f"{gap_max:.0f} years"),
        ]
        lines.append(make_metric_table(gap_metrics))
        lines.append("")

        # Distribution table
        lines.append("#### Gap Distribution\n")
        gap_header = "| Gap (Years) | n | % of Matched |"
        gap_sep = "|:-----------:|:--:|:------------:|"
        lines.append(gap_header)
        lines.append(gap_sep)

        gap_dist = ple_gap.value_counts().sort_index()
        for gap_val, n_gap in gap_dist.items():
            lines.append(f"| {int(gap_val)} | {n_gap:,} | {n_gap/len(ple_gap)*100:.2f}% |")

        lines.append("")
        lines.append(
            f"The typical gap is {gap_median:.0f} years (mean {gap_mean:.1f}), consistent "
            "with a standard 4-year undergraduate degree followed by immediate PLE."
        )
    else:
        lines.append("No PLE year gap data available.\n")

    lines.append("")

    # ────────────────────────────────────────────────────────────────────
    # 5) Yearly Trend Summary
    # ────────────────────────────────────────────────────────────────────
    lines.append("### Yearly Trend Summary\n")
    lines.append(
        "Per-year NMAT performance metrics (best-record basis). "
        "This shows how examinee volume and scores have evolved over time.\n"
    )

    yr_header = "| Year | n | Median Percentile | Median Raw Score | % Foreign | Female % |"
    yr_sep = "|:----:|:--:|:-----------------:|:----------------:|:---------:|:--------:|"
    lines.append(yr_header)
    lines.append(yr_sep)

    for yr in sorted(best["Year"].unique()):
        y_sub = best[best["Year"] == yr]
        y_n = len(y_sub)
        y_med_pctl = y_sub["NMS_PER_num"].median()
        y_med_raw = y_sub["TotalRawScoreTRUE"].median()
        y_foreign = int((y_sub["FOREIGNER_STATUS"].isin(["Verified Foreigner", "Likely Foreigner"])).sum())
        y_pct_f = (y_foreign / y_n * 100) if y_n > 0 else 0
        y_female = int((y_sub["SEX"] == "Female").sum())
        y_pct_female = (y_female / y_n * 100) if y_n > 0 else 0
        lines.append(
            f"| {yr} | {y_n:,} | {y_med_pctl:.1f} | {y_med_raw:.1f} | "
            f"{y_pct_f:.2f}% | {y_pct_female:.2f}% |"
        )

    lines.append("")

    # ── Key insight ─────────────────────────────────────────────────────
    lines.append("### Key Insights\n")
    f_med = best[best["SEX"] == "Female"]["NMS_PER_num"].median()
    m_med = best[best["SEX"] == "Male"]["NMS_PER_num"].median()
    lines.append(
        f"- **Sex:** Female examinees have a median NMAT percentile of {f_med:.1f} "
        f"vs {m_med:.1f} for males (difference: {f_med - m_med:+.1f} points). "
        "Females represent the majority of NMAT examinees."
    )
    lines.append("")
    lines.append(
        f"- **Repeat taking:** {fmt(repeat_takers)} ({repeat_rate:.1f}%) of "
        f"{fmt(total_persons)} unique examinees have taken the NMAT more than once."
    )
    lines.append("")

    best_cg = cg_counts.index[0]
    best_cg_n = cg_counts.iloc[0]
    lines.append(
        f"- **Course Group:** {best_cg} is the largest course group "
        f"({best_cg_n:,} examinees, {best_cg_n/len(best)*100:.1f}%). "
        "Medical & Allied courses dominate the NMAT-taking population."
    )
    lines.append("")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)

    # ── Console summary ─────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"  {TITLE}")
    print(f"{'='*70}")
    print(f"  Female examinees:          {int(sex_counts.get('Female', 0)):>7,}")
    print(f"  Male examinees:            {int(sex_counts.get('Male', 0)):>7,}")
    print(f"  Female median pctl:        {f_med:.1f}")
    print(f"  Male median pctl:          {m_med:.1f}")
    print(f"  Repeat takers:             {repeat_takers:>7,} ({repeat_rate:.1f}%)")
    print(f"  Median PLE gap:            {ple_gap.median():.0f} years" if len(ple_gap) > 0 else "  PLE gap: N/A")
    for cg in cg_counts.index:
        sub = best[best["CourseGroup"] == cg]
        print(f"  {cg:40s} {len(sub):>7,}  (med pctl: {sub['NMS_PER_num'].median():.1f})")
    print(f"  Output: {path}")
    print(f"{'='*70}\n")

    return {
        "female_n": int(sex_counts.get("Female", 0)),
        "male_n": int(sex_counts.get("Male", 0)),
        "female_median_pctl": f_med,
        "male_median_pctl": m_med,
        "repeat_takers": repeat_takers,
        "repeat_rate": repeat_rate,
    }

if __name__ == "__main__":
    compute()
