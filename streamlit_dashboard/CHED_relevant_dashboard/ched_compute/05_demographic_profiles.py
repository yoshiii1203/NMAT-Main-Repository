"""
05_demographic_profiles.py — Demographic profile analysis.

Computes:
  - By SEX: NMAT performance, PLE linkage
  - By CourseGroup: NMAT performance, PLE linkage
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
        "dimensions: sex and course group."
    )
    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SEX ANALYSIS
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### Performance by Sex\n")

    # Metric cards
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

    # Detailed sex comparison
    lines.append("#### NMAT Performance by Sex\n")

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

    # Bin distribution by sex
    lines.append("#### Percentile Bin Distribution by Sex\n")

    bin_sex_header = "| PercentileBin | Female n | Female % | Male n | Male % |"
    bin_sex_sep = "|:------------:|:--------:|:--------:|:------:|:------:|"
    lines.append(bin_sex_header)
    lines.append(bin_sex_sep)

    for b in BIN_ORDER:
        f_n = int((f_sub["PercentileBin"] == b).sum())
        m_n = int((m_sub["PercentileBin"] == b).sum())
        f_pct = f_n / len(f_sub) * 100 if len(f_sub) > 0 else 0
        m_pct = m_n / len(m_sub) * 100 if len(m_sub) > 0 else 0
        lines.append(f"| {b} | {f_n:,} | {f_pct:.2f}% | {m_n:,} | {m_pct:.2f}% |")

    lines.append("")

    # PLE linkage by sex
    lines.append("#### PLE Linkage Rate by Sex\n")
    lines.append("NMAT-to-PLE linkage rates for the observable cohort by sex.\n")

    ple_sex_header = "| Sex | n (Observable) | PLE Matched | Linkage Rate |"
    ple_sex_sep = "|:---:|:--------------:|:-----------:|:------------:|"
    lines.append(ple_sex_header)
    lines.append(ple_sex_sep)

    for sex_label in ["Female", "Male"]:
        sub_obs = obs[obs["SEX"] == sex_label]
        n_obs = len(sub_obs)
        n_ple = int(sub_obs["IS_PLE_PASSER"].sum())
        lr = (n_ple / n_obs * 100) if n_obs > 0 else 0
        lines.append(f"| {sex_label} | {n_obs:,} | {int(n_ple):,} | {lr:.2f}% |")

    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # COURSE GROUP ANALYSIS
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### Performance by Course Group\n")

    # Course group distribution
    cg_counts = best["CourseGroup"].value_counts()
    total_cg = len(best)

    cg_metrics = []
    for cg in cg_counts.index:
        sub = best[best["CourseGroup"] == cg]
        med = sub["NMS_PER_num"].median()
        cg_metrics.append((f"{cg}", f"{len(sub):,} ({len(sub)/total_cg*100:.1f}%), Median Pctl: {med:.1f}"))

    lines.append(make_metric_table(cg_metrics))
    lines.append("")

    # Course group detailed comparison
    lines.append("#### NMAT Performance by Course Group\n")

    cg_perf_header = "| Course Group | n | % of Total | Median Pctl | Q1 | Q3 | Median TotalRaw |"
    cg_perf_sep = "|:-------------|:--:|:----------:|:----------:|:--:|:--:|:---------------:|"
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

    # Bin distribution by course group
    lines.append("#### Percentile Bin Distribution by Course Group\n")
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

    # PLE linkage by course group
    lines.append("#### PLE Linkage Rate by Course Group\n")
    lines.append("NMAT-to-PLE linkage rates by course group (observable cohort, Year <= 2014).\n")

    ple_cg_header = "| Course Group | n (Observable) | PLE Matched | Linkage Rate |"
    ple_cg_sep = "|:-------------|:--------------:|:-----------:|:------------:|"
    lines.append(ple_cg_header)
    lines.append(ple_cg_sep)

    for cg in obs["CourseGroup"].value_counts().index:
        sub_obs = obs[obs["CourseGroup"] == cg]
        n_obs = len(sub_obs)
        n_ple = int(sub_obs["IS_PLE_PASSER"].sum())
        lr = (n_ple / n_obs * 100) if n_obs > 0 else 0
        lines.append(f"| {cg} | {n_obs:,} | {int(n_ple):,} | {lr:.2f}% |")

    lines.append("")

    # ══════════════════════════════════════════════════════════════════════
    # INTERPRETATION
    # ══════════════════════════════════════════════════════════════════════
    lines.append("### Interpretation\n")

    f_med = f_sub["NMS_PER_num"].median()
    m_med = m_sub["NMS_PER_num"].median()
    lines.append(
        f"- **Sex:** Female examinees have a median NMAT percentile of {f_med:.1f} "
        f"vs {m_med:.1f} for males (difference: {f_med - m_med:+.1f} points). "
        "Females represent the majority of NMAT examinees."
    )
    lines.append("")

    best_cg = cg_counts.index[0]
    best_cg_n = cg_counts.iloc[0]
    lines.append(
        f"- **Course Group:** {best_cg} is the largest course group "
        f"({best_cg_n:,} examinees, {best_cg_n/len(best)*100:.1f}%). "
        f"Medical & Allied courses dominate the NMAT-taking population."
    )
    lines.append("")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)

    # ── Print summary ───────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"  {TITLE}")
    print(f"{'='*70}")
    print(f"  Female examinees:          {int(sex_counts.get('Female', 0)):>7,}")
    print(f"  Male examinees:            {int(sex_counts.get('Male', 0)):>7,}")
    print(f"  Female median pctl:        {f_med:.1f}")
    print(f"  Male median pctl:          {m_med:.1f}")
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
    }


if __name__ == "__main__":
    compute()
