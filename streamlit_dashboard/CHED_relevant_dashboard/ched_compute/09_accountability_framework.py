"""
09_accountability_framework.py — Accountability Framework & Monitoring (Tab 8).

Covers CMO Section IV-B-2 (accountability), Section VI (monitoring),
and the Transitory Provision.

Computes:
  - PHEI-level risk flags: linkage rate vs national benchmark (43.46%)
  - Risk classification: Monitor / High for persistently underperforming PHEIs
  - Monitoring framework template (policy design)
  - Transition timeline for AY 2026-2027 implementation
  - Data gap recommendations with priority and effort estimates
"""

import sys
import os
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from config import BIN_ORDER, UNI_TYPE_ORDER, PLE_OBSERVABLE_MAX_YEAR
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

SCRIPT = "09_accountability_framework"
TITLE = "Accountability Framework & Monitoring (CMO Section IV-B-2, VI, Transitory)"

# National benchmark linkage rate for PHEIs (from dashboard analysis)
NATIONAL_BENCHMARK = 43.46  # %

# Minimum examinees for an HEI to be included in risk assessment
MIN_EXAMINEES = 5


def compute():
    df = load_data()
    subsets = create_subsets(df)
    best = subsets["best"]
    best_pre2015 = subsets["best_pre2015"]

    lines = []
    lines.append("\n")
    lines.append(
        "This section operationalises CMO No. __, s. 2026 provisions on institutional "
        "accountability (Section IV-B-2), CHED monitoring (Section VI), and the "
        "transitory provision. It identifies private HEIs (PHEIs) whose NMAT-to-PLE "
        "linkage rates fall below the national benchmark and provides a monitoring "
        "framework and transition timeline for full CMO compliance."
    )
    lines.append("")

    # ─────────────────────────────────────────────────────────────────
    # Metric cards: summary counts
    # ─────────────────────────────────────────────────────────────────
    phei = best[best["UNI_TYPE"] == "Private"].copy()
    phei_pre2015 = best_pre2015[best_pre2015["UNI_TYPE"] == "Private"].copy()

    total_phei = phei["NMA_College"].nunique()

    # PHEIs with >=5 examinees in observable cohort
    phei_grouped = phei_pre2015.groupby("NMA_College").agg(
        n=("IS_PLE_PASSER", "count"),
        ple_count=("IS_PLE_PASSER", "sum"),
    )
    phei_grouped = phei_grouped[phei_grouped["n"] >= MIN_EXAMINEES].copy()
    phei_grouped["linkage_rate"] = (
        phei_grouped["ple_count"] / phei_grouped["n"] * 100
    )

    above_benchmark = int((phei_grouped["linkage_rate"] >= NATIONAL_BENCHMARK).sum())
    below_benchmark = int((phei_grouped["linkage_rate"] < NATIONAL_BENCHMARK).sum())

    metrics = [
        ("Total PHEIs in Dataset", fmt(total_phei)),
        ("PHEIs with ≥5 Observable Examinees", fmt(len(phei_grouped))),
        ("Above National Benchmark (≥43.46%)", fmt(above_benchmark)),
        ("Below National Benchmark (<43.46%)", fmt(below_benchmark)),
        ("National PHEI Linkage Benchmark", f"{NATIONAL_BENCHMARK:.2f}%"),
        ("Observable Cohort Period", f"2006 – {PLE_OBSERVABLE_MAX_YEAR}"),
    ]
    lines.append("## Overview")
    lines.append("")
    lines.append(make_metric_table(metrics))
    lines.append("")

    # ─────────────────────────────────────────────────────────────────
    # Section A: PHEI Risk Flags (multi-year detail)
    # ─────────────────────────────────────────────────────────────────
    lines.append("## Section A: PHEI Risk Flags")
    lines.append("")
    lines.append(
        "Each PHEI with ≥5 examinees in the observable cohort (Year ≤ 2014) is assessed "
        "against the national NMAT-to-PLE linkage benchmark of **43.46%**. "
        "The linkage rate measures the share of NMAT examinees from that HEI who were "
        "later found in official PLE passer records — **not** the PLE pass rate. "
        "PHEIs below the benchmark are flagged for monitoring; those below the benchmark "
        "for every available year are classified as **High Risk**."
    )
    lines.append("")

    # Build detailed per-PHEI data with yearly breakdown
    risk_rows = []
    for hei in phei_grouped.index.sort_values():
        row = phei_grouped.loc[hei]
        n = int(row["n"])
        ple_count = int(row["ple_count"])
        linkage_rate = row["linkage_rate"]
        status = "Above Benchmark" if linkage_rate >= NATIONAL_BENCHMARK else "Below Benchmark"

        # Determine risk level
        if linkage_rate >= NATIONAL_BENCHMARK:
            risk_level = "Low"
        else:
            # Check every year this PHEI had examinees
            hei_years = phei_pre2015[phei_pre2015["NMA_College"] == hei]
            yr_grouped = hei_years.groupby("Year").agg(
                yr_n=("IS_PLE_PASSER", "count"),
                yr_ple=("IS_PLE_PASSER", "sum"),
            )
            yr_grouped["yr_rate"] = yr_grouped["yr_ple"] / yr_grouped["yr_n"] * 100
            # Only consider years with >= MIN_EXAMINEES examinees for classification
            yr_valid = yr_grouped[yr_grouped["yr_n"] >= MIN_EXAMINEES]
            if len(yr_valid) > 0 and (yr_valid["yr_rate"] < NATIONAL_BENCHMARK).all():
                risk_level = "High"
            elif linkage_rate == 0.0:
                risk_level = "High"
            else:
                risk_level = "Monitor"

        uni_type_row = phei_pre2015[phei_pre2015["NMA_College"] == hei]["UNI_TYPE"].mode().iloc[0]

        risk_rows.append({
            "HEI": hei,
            "UNI_TYPE": str(uni_type_row),
            "n": n,
            "ple_count": ple_count,
            "linkage_rate": linkage_rate,
            "status": status,
            "risk_level": risk_level,
        })
        if len(risk_rows) >= 500:
            break

    risk_df = pd.DataFrame(risk_rows)
    risk_df = risk_df.sort_values("linkage_rate", ascending=True)

    # ── Risk Flag Table ──────────────────────────────────────────────
    lines.append("### Risk Flag Table (Sorted by Linkage Rate, Worst First)")
    lines.append("")
    lines.append(
        f"| HEI | Type | n (Obs.) | PLE Linked | Linkage Rate | Benchmark ({NATIONAL_BENCHMARK:.2f}%) | Status | Risk Level |"
    )
    lines.append(
        "|-----|:----:|:--------:|:----------:|:------------:|:-----------------------------------:|:------:|:----------:|"
    )

    for _, r in risk_df.iterrows():
        hei_short = r["HEI"][:55] if len(str(r["HEI"])) > 55 else r["HEI"]
        lines.append(
            f"| {hei_short} | {r['UNI_TYPE']} | {fmt(r['n'])} | {fmt(r['ple_count'])} | "
            f"{r['linkage_rate']:.2f}% | {NATIONAL_BENCHMARK:.2f}% | {r['status']} | {r['risk_level']} |"
        )

    lines.append("")
    lines.append(
        f"_Table shows {len(risk_df)} PHEIs with ≥{MIN_EXAMINEES} examinees in the "
        f"observable cohort, ranked by linkage rate (lowest first). "
        f"{int((risk_df['risk_level'] == 'High').sum())} High-risk and "
        f"{int((risk_df['risk_level'] == 'Monitor').sum())} Monitor-level PHEIs identified._"
    )
    lines.append("")

    # ── Summary of Risk Distribution ─────────────────────────────────
    lines.append("### Risk Distribution Summary")
    lines.append("")
    risk_counts = risk_df["risk_level"].value_counts()
    lines.append("| Risk Level | PHEIs | % of Total |")
    lines.append("|:----------:|:----:|:----------:|")
    for rl in ["High", "Monitor", "Low"]:
        cnt = int(risk_counts.get(rl, 0))
        pct_val = cnt / len(risk_df) * 100 if len(risk_df) > 0 else 0
        lines.append(f"| {rl} | {fmt(cnt)} | {pct_val:.1f}% |")
    lines.append("")

    # ── Top 20 Worst Performers Detail ───────────────────────────────
    top20 = risk_df.head(20).copy()
    lines.append("### Bottom 20 PHEIs — Detail")
    lines.append("")
    lines.append(
        "The following PHEIs have the lowest NMAT-to-PLE linkage rates in the "
        "observable cohort. These institutions warrant priority attention.\n"
    )
    lines.append(
        "| Rank | HEI | n (Obs.) | Linkage Rate | Risk Level |"
    )
    lines.append(
        "|:----:|------|:--------:|:------------:|:----------:|"
    )
    for rank, (_, r) in enumerate(top20.iterrows(), 1):
        hei_short = str(r["HEI"])[:60]
        lines.append(
            f"| {rank} | {hei_short} | {fmt(r['n'])} | {r['linkage_rate']:.2f}% | {r['risk_level']} |"
        )
    lines.append("")

    # ── Multi-Year Trend Notes ───────────────────────────────────────
    lines.append("### Multi-Year Trend Flagging")
    lines.append("")
    lines.append(
        "For each HEI classified as **High Risk**, we examined whether the linkage rate "
        "fell below benchmark in **every available year** with ≥5 examinees. "
        "This approximates the CMO's intent to track persistent underperformance. "
        "Note that the available data covers only 2006–2014 for the observable cohort "
        "(9 years), and many HEIs have data for only a subset of those years.\n"
    )
    lines.append("")
    high_risk_heis = risk_df[risk_df["risk_level"] == "High"]
    lines.append(
        f"- **{len(high_risk_heis)} PHEI(s)** classified as High Risk "
        f"(below benchmark in all available years)\n"
    )
    lines.append(
        f"- **{int((risk_df['risk_level'] == 'Monitor').sum())} PHEI(s)** classified as Monitor "
        f"(below benchmark overall but above in at least one year)\n"
    )
    lines.append(
        "> **Policy Note:** Full 3-year consecutive tracking (as specified in the draft CMO) "
        "cannot be computed from this dataset because NMAT data ends in 2018 and the "
        "observable PLE cohort ends in 2014. CHED must collect prospective data starting "
        "AY 2026-2027 to enable proper multi-year consecutive monitoring."
    )
    lines.append("")

    # ─────────────────────────────────────────────────────────────────
    # Section B: Monitoring Framework Template
    # ─────────────────────────────────────────────────────────────────
    lines.append("## Section B: Monitoring Framework Template")
    lines.append("")
    lines.append(
        "The following template outlines the data CHED should collect annually from each "
        "HEI to operationalise CMO Section VI monitoring requirements. This is a **policy "
        "design instrument** — the data to populate it does not yet exist in this dataset."
    )
    lines.append("")

    mon_header = (
        "| # | Metric | Definition | Collection Frequency | Responsible Party |"
    )
    mon_sep = "|:-:|--------|------------|:-------------------:|:-----------------:|"
    lines.append(mon_header)
    lines.append(mon_sep)

    monitoring_rows = [
        (
            "1",
            "NMAT Cut-Off Implemented",
            "Whether the HEI has set and published an NMAT cut-off score ≥30th "
            "percentile (B4+).",
            "Annual (start of AY)",
            "HEI Registrar / Admissions",
        ),
        (
            "2",
            "Cut-Off Score Value",
            "The specific NMAT percentile ranking adopted as minimum requirement.",
            "Annual (start of AY)",
            "HEI Registrar / Admissions",
        ),
        (
            "3",
            "Composite Ranking System",
            "Whether the HEI uses a holistic ranking (≥60% NMAT + ≤40% GWA or other "
            "academic criteria) for admission.",
            "Annual (start of AY)",
            "HEI Academic Council",
        ),
        (
            "4",
            "GWA Collection Rate",
            "Share of applicants with complete GWA records submitted alongside NMAT.",
            "Per admission cycle",
            "HEI Registrar",
        ),
        (
            "5",
            "Foreign Student Slots Used",
            "Number of foreign nationals enrolled, with cap compliance "
            "(≤10 per SUC, ≤ per-program limits).",
            "Annual (end of AY)",
            "HEI Office of Student Affairs",
        ),
        (
            "6",
            "NMAT Examinee Volume",
            "Total number of NMAT examinees from the HEI (best-record basis).",
            "Annual (after NMAT release)",
            "CEM / CHED",
        ),
        (
            "7",
            "NMAT-to-PLE Linkage Rate",
            "Share of NMAT examinees from 5+ years prior found in PLE passer records. "
            "Proxy for program quality.",
            "Every 3 years (rolling)",
            "CHED / PRC data sharing",
        ),
        (
            "8",
            "PLE Pass Rate (when available)",
            "First-time PLE takers' pass rate for the HEI's medical program.",
            "Annual (after PLE results)",
            "PRC / CHED",
        ),
        (
            "9",
            "Student-Teacher Ratio",
            "Ratio of enrolled medical students to qualified faculty.",
            "Annual",
            "HEI",
        ),
        (
            "10",
            "Program Compliance Status",
            "Overall compliance rating: Compliant, Partially Compliant, Non-Compliant.",
            "Annual",
            "CHED Regional Office",
        ),
    ]

    for row in monitoring_rows:
        lines.append(f"| {' | '.join(row)} |")
    lines.append("")

    lines.append(
        "> **Note:** Metrics 1–5 rely on HEI self-reporting. Metrics 6–8 require "
        "data-sharing agreements between CEM, PRC, and CHED. Metric 9 requires HEI "
        "faculty records. The PHEI Risk Flags from Section A above serve as a "
        "retrospective proxy for Metric 7 until prospective data collection begins."
    )
    lines.append("")

    # ─────────────────────────────────────────────────────────────────
    # Section C: Transition Timeline
    # ─────────────────────────────────────────────────────────────────
    lines.append("## Section C: Transition Timeline (CMO Transitory Provision)")
    lines.append("")
    lines.append(
        "The draft CMO No. __, s. 2026 takes effect at the start of **AY 2026-2027**. "
        "The following timeline outlines key milestones and actions required of HEIs "
        "to achieve full compliance. This is a **policy design document**, not data-driven."
    )
    lines.append("")

    timeline_header = (
        "| Phase | Period | Action | Responsible | Verification |"
    )
    timeline_sep = "|:-----:|:------:|--------|:-----------:|:------------:|"
    lines.append(timeline_header)
    lines.append(timeline_sep)

    timeline_rows = [
        (
            "Pre-1",
            "Q1–Q2 2026",
            "CHED publishes IRR and compliance guidelines; disseminate to all HEIs.",
            "CHED Central Office",
            "IRR published, memo sent to HEIs",
        ),
        (
            "Pre-2",
            "Q2–Q3 2026",
            "HEIs review current NMAT cut-off policies; identify gaps.",
            "HEI Administration",
            "Self-assessment report",
        ),
        (
            "Pre-3",
            "Q3 2026",
            "HEIs set or adjust NMAT cut-off to ≥30th percentile (B4+); "
            "publish in admission materials.",
            "HEI Academic Council",
            "Published cut-off, board resolution",
        ),
        (
            "Pre-4",
            "Q3 2026",
            "HEIs design composite ranking system: ≥60% NMAT + ≤40% GWA.",
            "HEI Admissions Office",
            "Approved ranking formula",
        ),
        (
            "1",
            "AY 2026-2027 Start",
            "New admission cycle begins with CMO-compliant cut-off and ranking.",
            "HEI Registrar",
            "Admission records",
        ),
        (
            "2",
            "AY 2026-2027 Mid",
            "First annual compliance report due to CHED.",
            "HEI Compliance Officer",
            "Compliance report submitted",
        ),
        (
            "3",
            "AY 2026-2027 End",
            "CHED conducts first annual monitoring visit or desk audit.",
            "CHED Regional Office",
            "Monitoring report",
        ),
        (
            "4",
            "AY 2027-2028",
            "First foreign slot cap verification; review of cut-off compliance.",
            "CHED + HEIs",
            "Slot utilization report",
        ),
        (
            "5",
            "AY 2028-2029",
            "First NMAT-to-PLE linkage rate review (observable 5-year cohort from start) "
            "— earliest point for accountability trigger.",
            "CHED + PRC",
            "Linkage rate analysis",
        ),
        (
            "6",
            "AY 2029-2030",
            "First round of potential sanctions for persistently non-compliant HEIs.",
            "CHED",
            "Show-cause order/remedial plan",
        ),
    ]

    for row in timeline_rows:
        lines.append(f"| {' | '.join(row)} |")
    lines.append("")

    lines.append(
        "> **Important:** The accountability trigger (consecutive years below benchmark) "
        "cannot be evaluated before AY 2028-2029 at the earliest, because it requires "
        "at least 3 years of prospective linkage data (from AY 2026-2027 intake) plus "
        "5 years for those students to reach PLE."
    )
    lines.append("")

    # ─────────────────────────────────────────────────────────────────
    # Section D: Data Gap Recommendations
    # ─────────────────────────────────────────────────────────────────
    lines.append("## Section D: Data Gap Recommendations")
    lines.append("")
    lines.append(
        "Full implementation of the CMO accountability framework requires data that does "
        "not currently exist in the NMAT_Exodus dataset. The following recommendations "
        "are ordered by priority and estimated effort."
    )
    lines.append("")

    gap_header = (
        "| Priority | Data Requirement | Purpose | Current Gap | Effort | Timeline |"
    )
    gap_sep = "|:-------:|------------------|---------|:-----------:|:-----:|:--------:|"
    lines.append(gap_header)
    lines.append(gap_sep)

    gap_rows = [
        (
            "P1",
            "HEI-submitted NMAT cut-off values per program per AY",
            "Verify cut-off ≥30th percentile compliance",
            "Not collected; no baseline",
            "High",
            "AY 2026-2027",
        ),
        (
            "P1",
            "GWA records per examinee (linked to NMAT score)",
            "Enable composite ranking monitoring",
            "Not in dataset; CHED must mandate submission",
            "High",
            "AY 2026-2027",
        ),
        (
            "P2",
            "Annual enrollment counts by citizenship",
            "Verify foreign slot cap (≤10 per SUC)",
            "Dataset has examinee counts only, not enrollment",
            "Medium",
            "AY 2027-2028",
        ),
        (
            "P2",
            "PLE pass/fail records per HEI per year",
            "Compute actual PLE pass rate (not just linkage rate)",
            "PRC PLE data not linked to NMAT person-level data",
            "Medium",
            "AY 2027-2028",
        ),
        (
            "P2",
            "HEI compliance self-report submissions",
            "Populate monitoring template",
            "No reporting mechanism exists yet",
            "Medium",
            "AY 2026-2027",
        ),
        (
            "P3",
            "Faculty-to-student ratios per medical program",
            "Program quality indicator",
            "Not collected in this dataset",
            "Low",
            "AY 2027-2028",
        ),
        (
            "P3",
            "Program accreditation status (e.g., PAASCU, AACCUP)",
            "Context for compliance evaluation",
            "Not linked to NMAT data",
            "Low",
            "AY 2028-2029",
        ),
        (
            "P3",
            "Continuous NMAT data feed from CEM",
            "Enable year-over-year trend monitoring beyond 2018",
            "CEM data ends at 2018; no agreement for ongoing feed",
            "Low",
            "Ongoing",
        ),
    ]

    for row in gap_rows:
        lines.append(f"| {' | '.join(row)} |")
    lines.append("")

    lines.append(
        "**Priority Definitions:** "
        "P1 = Required for baseline CMO compliance verification. "
        "P2 = Required for full monitoring framework. "
        "P3 = Desirable for comprehensive evaluation.\n"
    )
    lines.append(
        "**Effort Estimates:** "
        "High = New MOA/data-sharing agreement or legislative mandate required. "
        "Medium = Extension of existing data-sharing arrangement. "
        "Low = Automated or existing collection mechanism.\n"
    )
    lines.append(
        "> **Recommendation:** CHED should prioritise P1 items before AY 2026-2027 to "
        "establish baseline compliance when the CMO takes effect. The NMAT-to-PLE linkage "
        "rate (from this dataset) serves as an interim, retrospective accountability "
        "tool until prospective P1 data collection begins."
    )
    lines.append("")

    # ─────────────────────────────────────────────────────────────────
    # Caveats specific to accountability framework
    # ─────────────────────────────────────────────────────────────────
    lines.append("## Limitations")
    lines.append("")
    lines.append(
        "1. **Data recency:** NMAT data covers 2006–2018 only. The 8-year gap to "
        "AY 2026-2027 means risk flags are historical, not current.\n\n"
        "2. **PLE linkage ≠ PLE pass rate:** Our dataset contains PLE passers only. "
        "We cannot distinguish between 'did not take PLE' and 'took PLE and failed.'\n\n"
        "3. **HEI name disambiguation:** Some HEIs may appear under slightly different "
        "names in different years. We used NMA_College as-is.\n\n"
        "4. **Observable cohort limit:** Full accountability can only be assessed 5+ years "
        "after CMO implementation (earliest: AY 2031-2032).\n\n"
        "5. **No GWA data:** The composite ranking formula (≥60% NMAT + ≤40% GWA) cannot be "
        "verified from this dataset.\n\n"
        "6. **Foreign slot monitoring:** Our counts are examinee-level, not enrollment-level. "
        "Enforcement requires enrollment data from HEIs."
    )
    lines.append("")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)

    # Return metadata for orchestration
    return {
        "script": SCRIPT,
        "title": TITLE,
        "output_path": path,
        "total_phei": total_phei,
        "analyzed_phei": len(risk_df),
        "above_benchmark": above_benchmark,
        "below_benchmark": below_benchmark,
        "high_risk": int((risk_df["risk_level"] == "High").sum()),
        "monitor": int((risk_df["risk_level"] == "Monitor").sum()),
    }


if __name__ == "__main__":
    result = compute()
    print(f"\nAccountability Framework complete.")
    print(f"  PHEIs analyzed: {result['analyzed_phei']}")
    print(f"  Above benchmark: {result['above_benchmark']}")
    print(f"  Below benchmark: {result['below_benchmark']}")
    print(f"  High risk: {result['high_risk']}")
    print(f"  Monitor: {result['monitor']}")
    print(f"  Output: {result['output_path']}")
