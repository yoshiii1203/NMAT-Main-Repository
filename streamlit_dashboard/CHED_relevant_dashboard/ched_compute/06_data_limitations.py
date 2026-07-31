"""
06_data_limitations.py — Data, Methods, and Limitations (Tab 6).

Documents the dataset, methodology, and limitations relevant to CHED decision-making.

Previously this script loaded the parquet directly (bypassing
ched_common's dtype coercion) and compared string-typed columns with
`== True` / `== 1.0`, which silently returned False/0 for every row --
producing a self-contradicting "Rows with complete TRUE scores: 0
(99.97%)" in the committed output (audit 06, F2/F3). Now it goes through
helpers.load_data() -> ched_common.load_and_validate(), which coerces
these columns before any comparison, and reuses the same compute_*
functions dashboard.py uses for the mismatch/TRUE-score/matching stats.
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import ched_common as cc
from config import B5_PLUS
from helpers import load_data, create_subsets, create_clean_subset, write_output, today_str

SCRIPT = "06_data_limitations"
TITLE = "Data, Methods, and Limitations"


def compute():
    df = load_data()
    S = create_subsets(df)
    best = S["best"]
    obs = S["best_pre2015"]  # IS_BEST_OBSERVABLE_RECORD cohort

    kpi = cc.compute_tab1_kpis(best)
    rep = cc.compute_repeat_taker_stats(df, kpi["n_unique"])
    mismatch = cc.compute_stored_mismatch_stats(df)
    true_stats = cc.compute_true_raw_score_stats(df)
    match_stats = cc.compute_ple_matching_stats(df, obs)
    amb = cc.compute_ambiguous_person_stats(df)

    clean = create_clean_subset(obs)
    clean_b5 = clean[clean["PercentileBin"].isin(B5_PLUS)]
    avg_gap = obs.loc[obs["HAS_CONFIRMED_PLE"], "PLE_YEAR_GAP"].median()

    lines = []
    lines.append(f"**Date:** {today_str()}")
    lines.append("")
    lines.append("## Dataset Overview")
    lines.append("")
    lines.append(f"- **Source file:** `NMAT_Exodus.parquet` ({df.shape[1]} columns, {len(df):,} rows)")
    lines.append(f"- **Examination years:** 2006-2018")
    lines.append(f"- **Unique examinees (best record):** {kpi['n_unique']:,}")
    lines.append(f"- **Observable PLE cohort (best attempt, Year <= 2014):** {len(obs):,}")
    lines.append(f"- **Repeat takers:** {rep['n_repeat']:,} unique persons ({rep['pct']:.0f}%)")
    lines.append("")
    if amb["n_ambiguous_keys"] is not None:
        lines.append(f"**Data quality note:** {amb['n_ambiguous_keys']:,} PERSON_KEY identifiers have "
                      "contradictory SEX recorded across their rows (PERSON_KEY_AMBIGUOUS), indicating "
                      "a possible identity collision. Disclosed, not silently corrected.")
        lines.append("")

    lines.append("## Key Methodological Choices")
    lines.append("")

    lines.append("### TRUE Raw Score Recalculation")
    lines.append(f"Of the {mismatch['n_stored']:,} records that carry a stored total, "
                  f"{mismatch['n_mismatch']:,} ({mismatch['pct_of_stored']:.1f}%) disagreed with the sum "
                  f"of the 8 component subtest scores ({mismatch['pct_of_all']:.1f}% of all "
                  f"{len(df):,} records). Computed live from `StoredVsDerivedMismatch` -- never hardcoded.")
    lines.append(f"")
    lines.append(f"- Rows with complete TRUE scores: {true_stats['n_true']:,} ({true_stats['pct_true']:.2f}%)")
    lines.append(f"- Stored-total mismatches: {mismatch['n_mismatch']:,} of {mismatch['n_stored']:,} rows "
                  f"with a stored total ({mismatch['pct_of_stored']:.1f}%)")
    lines.append("")

    lines.append("### Best-Record Deduplication")
    lines.append(f"{rep['n_repeat']:,} examinees ({rep['pct']:.0f}%) took the NMAT more than once (up to "
                  "9 attempts). Person-level analyses use the best-record flag (`IS_BEST_NMAT_RECORD`), "
                  "which selects, for every person, the highest NMAT percentile, latest year as "
                  "tiebreaker, then lowest application number -- one uniform rule for passers and "
                  "non-passers alike.")
    lines.append("")

    lines.append("### Observable Cohort Definition")
    lines.append("PLE-linked analyses use `IS_BEST_OBSERVABLE_RECORD` (each person's best attempt among "
                  "rows with Year <= 2014) -- deliberately not the same as filtering the overall "
                  "best-record flag to Year<=2014, which would silently drop people whose overall-best "
                  "attempt fell after 2014 and inflate the observed linkage rate.")
    lines.append(f"- Observable cohort: {len(obs):,}")
    lines.append(f"- Median NMAT-to-PLE year gap: {avg_gap:.0f} years")
    lines.append("")

    lines.append("### Deterministic PLE Matching")
    outcome = match_stats["outcome_counts"]
    lines.append("All PLE matching is deterministic (exact NMA_AppNo match, manual AppNo match, or "
                  "deterministic AppNo match). No fuzzy/rapidfuzz matching is used.")
    lines.append("")
    lines.append("**Caveats:**")
    lines.append("- The NMAT application number (NMA_AppNo) is not a well-established, consistent "
                  "identifier across datasets. Matching depends on this number being recorded "
                  "identically in both datasets.")
    lines.append(f"- Match outcome breakdown (`PLE_MATCH_OUTCOME`, all rows): accepted "
                  f"{outcome.get('accepted', 0):,}, rejected_ambiguous_person "
                  f"{outcome.get('rejected_ambiguous_person', 0):,} (name-collision candidate found but "
                  f"rejected as genuinely ambiguous), no_match {outcome.get('no_match', 0):,}. "
                  f"`PLE_YEAR_UNCERTAIN` flags {match_stats['n_year_uncertain']:,} confirmed passers "
                  "whose PLE year is not determinable.")
    lines.append("- `PLE_YEAR_PASSED`, `PLE_MATCH_METHOD`, `PLE_YEAR_GAP` are diagnostic metadata, not "
                  "authoritative passer counts, and do not nest inside `IS_PLE_PASSER`: non-null for "
                  f"{match_stats['n_year_passed_notna']:,} / {match_stats['n_match_method_notna']:,} / "
                  f"{match_stats['n_year_gap_notna']:,} rows respectively.")
    lines.append("- **PLE-matching bias against below-40th-percentile examinees (disclosed).** The "
                  "name-collision disambiguator (`2_PLE_Matching_Pipeline.ipynb`, `disambiguate()` "
                  "Step 4) previously applied a hard filter -- not a tie-break -- discarding every "
                  "candidate scoring below the 40th NMAT percentile and rejecting the match outright if "
                  "no candidate scored at or above 40. That constant, 40, is exactly the CMO threshold "
                  "under review. Confined to name-collision groups, now corrected upstream, but present "
                  "in every below-B4/B5 linkage figure derived from this parquet snapshot.")
    lines.append("- The Stress-Test analysis (Tab 3) uses the strictest criteria (confirmed match, "
                  ">=5 year gap, Filipino nationals only) as a genuine, non-tautological sensitivity "
                  "check -- population is NOT pre-filtered on match status.")
    lines.append("")
    lines.append(f"- Confirmed PLE passers (all rows): {match_stats['n_all_ple']:,}")
    lines.append(f"- Confirmed PLE passers (best-attempt, observable cohort): {match_stats['n_obs_ple']:,}")
    lines.append(f"- Strict-criteria B5+ subset (Filipino, >=5yr gap): {len(clean_b5):,}")
    lines.append("")

    lines.append("## Limitations Relevant to CHED Decision-Making")
    lines.append("")

    limitations = [
        ("PLE Outcomes", "The dataset only identifies NMAT examinees later matched to PLE passer "
         "records. It does not contain all PLE takers or PLE failures. This dashboard reports "
         "NMAT-to-PLE-passer linkage rates, not PLE pass rates."),
        ("GIDA and IP Status", "The dataset does not contain indicators for Geographically Isolated "
         "and Disadvantaged Area (GIDA) residence or Indigenous Peoples (IP) membership. The CMO "
         "exception for B4-only applicants from these groups requires documentation not available in "
         "this dataset."),
        ("Medical School Admissions and Enrollment", "This dataset records NMAT examinees, not enrolled "
         "medical students. The number of examinees at or above a threshold represents the available "
         "applicant pool, not actual enrollment."),
        ("Foreign Student Enrollment Cap", "The CMO caps foreign student enrollment at 10 slots per "
         "incoming class at SUCs. The dataset shows NMAT examinees by citizenship, not enrolled foreign "
         "students."),
        ("Composite Ranking for Foreign Applicants", "The dataset does not contain GWA, interview "
         "scores, or other admission criteria needed for composite ranking analysis."),
        ("PHEI Accountability and Sanctions", "This dataset contains NO medical-school identifier of "
         "any kind. No PHEI, SUC, or any other institution-level PLE performance, compliance label, or "
         "risk rating can be computed from any column in this file. UNDERGRAD_UNI_TYPE describes the "
         "examinee's undergraduate school and must never be read as a stand-in for the medical school."),
    ]

    for title, detail in limitations:
        lines.append(f"### {title}")
        lines.append(detail)
        lines.append("")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)
    print(f"  Wrote {path}")
    return path


if __name__ == "__main__":
    compute()
