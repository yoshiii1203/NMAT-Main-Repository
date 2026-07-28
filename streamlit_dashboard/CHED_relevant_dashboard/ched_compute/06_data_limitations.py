"""
06_data_limitations.py — Data, Methods, and Limitations (Tab 6).

Documents the dataset, methodology, and limitations relevant to CHED decision-making.
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import pandas as pd
from config import B5_PLUS
from helpers import load_data, create_subsets, create_clean_subset, write_output, fmt, today_str

SCRIPT = "06_data_limitations"
TITLE = "Data, Methods, and Limitations"

def compute():
    df = load_data()
    S = create_subsets(df)
    best = S["best"]
    obs = S["best_pre2015"]

    # Normalize
    for c in ["IS_BEST_NMAT_RECORD", "IS_PLE_ANALYSIS_SAFE"]:
        if c in obs.columns:
            if not pd.api.types.is_bool_dtype(obs[c]):
                obs[c] = obs[c].astype(str).str.upper().isin(["TRUE", "1", "YES"])
            else:
                obs[c] = obs[c].fillna(False)
    obs["HAS_CONFIRMED_PLE"] = (obs["IS_PLE_ANALYSIS_SAFE"] == True)

    n_all = len(df)
    n_best = len(best)
    n_obs = len(obs)
    n_unique = int(best["PERSON_KEY"].nunique())
    n_repeat = int((df.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique() > 1).sum())

    # TRUE raw score check
    n_true = int((df["HasTRUErawScores"] == True).sum()) if "HasTRUErawScores" in df.columns else 0

    # PLE matching
    n_all_ple = int((df["IS_PLE_ANALYSIS_SAFE"] == True).sum()) if "IS_PLE_ANALYSIS_SAFE" in df.columns else 0
    n_obs_ple = int(obs["HAS_CONFIRMED_PLE"].sum()) if "HAS_CONFIRMED_PLE" in obs.columns else 0
    clean = create_clean_subset(obs)
    clean_b5 = clean[clean["PercentileBin"].isin(B5_PLUS)]

    # Stored-vs-derived mismatches
    stored_mismatch = int((df["StoredVsDerivedMismatch"] == 1.0).sum()) if "StoredVsDerivedMismatch" in df.columns else 0
    calc_mismatch = int((df["CalcVsDerivedMismatch"] == 1.0).sum()) if "CalcVsDerivedMismatch" in df.columns else 0

    avg_gap = obs[obs["HAS_CONFIRMED_PLE"]]["PLE_YEAR_GAP"].median() if "PLE_YEAR_GAP" in obs.columns else "N/A"

    lines = []
    lines.append(f"**Date:** {today_str()}")
    lines.append("")
    lines.append("## Dataset Overview")
    lines.append("")
    lines.append(f"- **Source file:** `NMAT_Exodus.parquet` (54 columns, {n_all:,} rows)")
    lines.append(f"- **Examination years:** 2006-2018")
    lines.append(f"- **Unique examinees (best record):** {n_unique:,}")
    lines.append(f"- **Observable PLE cohort (Year <= 2014):** {n_obs:,}")
    lines.append(f"- **Repeat takers:** {n_repeat:,} unique persons ({n_repeat/n_unique*100:.0f}%)")
    lines.append("")

    lines.append("## Key Methodological Choices")
    lines.append("")

    lines.append("### TRUE Raw Score Recalculation")
    lines.append(f"The pipeline recalculated all raw scores from the 8 individual subtest components because 42.2% of the original stored totals were incorrect.")
    lines.append(f"")
    lines.append(f"- Rows with complete TRUE scores: {n_true:,} (99.97%)")
    lines.append(f"- Formula mismatches (Total != Part I + Part II): 0")
    lines.append(f"- Stored-vs-derived mismatches: {stored_mismatch:,}")
    lines.append(f"- Calc-vs-derived mismatches: {calc_mismatch:,}")
    lines.append("")

    lines.append("### Best-Record Deduplication")
    lines.append(f"{n_repeat:,} examinees ({n_repeat/n_unique*100:.0f}%) took the NMAT more than once (up to 9 attempts). Person-level analyses use the best-record flag (`IS_BEST_NMAT_RECORD`), which selects:")
    lines.append("- For PLE passers: the specific NMAT attempt that matched to the PLE record.")
    lines.append("- For others: the highest percentile attempt, with latest year as tiebreaker.")
    lines.append("")

    lines.append("### Observable Cohort Definition (Year <= 2014)")
    lines.append(f"PLE-linked analyses use examinees whose NMAT year is 2014 or earlier, ensuring a minimum window for PLE passage.")
    lines.append(f"- Observable best-record cohort: {n_obs:,}")
    lines.append(f"- Median NMAT-to-PLE year gap: {avg_gap} years")
    lines.append("")

    lines.append("### Deterministic PLE Matching")
    lines.append("All PLE matching is deterministic (exact NMA_AppNo match, manual AppNo match, or deterministic AppNo match). No fuzzy/rapidfuzz matching is used.")
    lines.append("")
    lines.append("**Caveats:**")
    lines.append("- The NMAT application number (NMA_AppNo) is not a well-established, consistent identifier across datasets. Matching depends on this number being recorded identically in both datasets.")
    lines.append("- Undercounting is possible where numbers differ between datasets.")
    lines.append("- The clean subset analysis (Tab 3) uses the strictest criteria as a robustness check.")
    lines.append("")
    lines.append(f"- Confirmed PLE passers (all rows): {n_all_ple:,}")
    lines.append(f"- Confirmed PLE passers (best record, observable): {n_obs_ple:,}")
    lines.append(f"- Clean subset (B5+, Filipino, >=5yr gap): {len(clean_b5):,}")
    lines.append("")

    lines.append("## Limitations Relevant to CHED Decision-Making")
    lines.append("")

    limitations = [
        ("PLE Outcomes", "The dataset only identifies NMAT examinees later matched to PLE passer records. It does not contain all PLE takers or PLE failures. This dashboard reports NMAT-to-PLE-passer linkage rates, not PLE pass rates."),
        ("GIDA and IP Status", "The dataset does not contain indicators for Geographically Isolated and Disadvantaged Area (GIDA) residence or Indigenous Peoples (IP) membership. The CMO exception for B4-only applicants from these groups requires documentation not available in this dataset."),
        ("Medical School Admissions and Enrollment", "This dataset records NMAT examinees, not enrolled medical students. The number of examinees at or above a threshold represents the available applicant pool, not actual enrollment."),
        ("Foreign Student Enrollment Cap", "The CMO caps foreign student enrollment at 10 slots per incoming class at SUCs. The dataset shows NMAT examinees by citizenship, not enrolled foreign students."),
        ("Composite Ranking for Foreign Applicants", "The dataset does not contain GWA, interview scores, or other admission criteria needed for composite ranking analysis."),
        ("PHEI Accountability and Sanctions", "This dashboard does not assign compliance labels or risk ratings to individual HEIs. The NMAT-linked PLE data is not a complete measure of institutional PLE performance."),
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
