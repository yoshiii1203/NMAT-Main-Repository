"""
Page 2: Data Integrity and Cohort Definition Checks
Replicates ALL computations from dashboard.py tab2 (lines 830-970).
Extracts unfiltered data and saves to page_results/02_data_integrity.md.
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "data_aggregator"))

import numpy as np
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
pd.set_option("display.max_colwidth", 80)

from config import BIN_ORDER, PLE_ORDER, RESULTS_DIR
from helpers import load_data, write_header, write_dataframe


def count_true_flags(series: pd.Series) -> int:
    """Replicates dashboard.py count_true_flags.
    Handles StringDtype (str), object, float, and boolean dtypes.
    """
    if series is None:
        return 0
    dtype_str = str(series.dtype)
    # StringDtype variants: 'str', 'string', 'object'
    if dtype_str in ("str", "string", "object"):
        mapping = {
            "TRUE": True, "1": True, "1.0": True, "YES": True, "Y": True,
            "FALSE": False, "0": False, "0.0": False, "NO": False, "N": False,
        }
        s_norm = series.astype(str).str.strip().str.upper()
        out = s_norm.map(mapping)
        return int((out == True).sum())
    # For float with NaN (StoredVsDerivedMismatch)
    if pd.api.types.is_float_dtype(series):
        return int((series == 1.0).sum())
    return int((series == True).sum())


def run() -> str:
    df, subsets = load_data()

    # Pull all subsets needed for the cohort definition table
    dfall = subsets["all"]
    best = subsets["best"]
    besttrend = subsets["besttrend"]
    bestobservable = subsets["bestobservable"]
    plesafe = subsets["plesafe"]
    plebest = subsets["plebest"]

    lines = []

    # ========== HEADER ==========
    lines.append("# Page 2: Data Integrity and Cohort Definition Checks")
    lines.append("")
    lines.append(f"**Generated:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("**Data source:** NMAT_Exodus.parquet (Pipeline 4)")
    lines.append("")
    lines.append("**Data subset:** `all` (full unfiltered dataset) and derived analytic subsets")
    lines.append("")
    lines.append("**Filters:** None (full unfiltered dataset)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ========== 4 METRIC CARDS ==========
    lines.append("## Metric Cards")
    lines.append("")

    # Count TRUE raw score rows (handles StringDtype with str values "True"/"False")
    true_raw_count = int(
        df["HasTRUErawScores"].astype(str).str.strip().str.upper().isin(["TRUE", "1", "1.0", "YES"]).sum()
    )

    lines.append("| Metric | Value |")
    lines.append("|--------|------:|")
    lines.append(f"| All NMAT rows | {len(dfall):,} |")
    lines.append(f"| Best-record rows | {len(best):,} |")
    lines.append(f"| Rows with TRUE raw scores | {true_raw_count:,} |")
    lines.append(f"| Observable best-record rows | {len(bestobservable):,} |")
    lines.append("")

    lines.append("---")
    lines.append("")

    # ========== COHORT DEFINITION TABLE (Table 2) ==========
    lines.append("## Table 2: Analysis Cohorts Used in the Dashboard")
    lines.append("")
    lines.append("Each row defines one analytic subset used in later pages. Counts are rows, not necessarily unique persons.")
    lines.append("")

    cohort_tbl = pd.DataFrame({
        "Analytic subset": [
            "All cleaned NMAT rows",
            "One best NMAT record per person",
            "Best-record rows within 2006-2018",
            "Best-record rows in the observable PLE window",
            "Confirmed PLE-matched NMAT rows",
            "Confirmed PLE-matched best-record persons",
        ],
        "Row count": [
            len(dfall),
            len(best),
            len(besttrend),
            len(bestobservable),
            len(plesafe),
            len(plebest),
        ],
        "Interpretation": [
            "All cleaned NMAT rows",
            "One best NMAT record per person",
            "Best-record rows within 2006-2018",
            "Best-record rows in the observable PLE window",
            "Confirmed PLE-matched NMAT rows",
            "Confirmed PLE-matched best-record persons",
        ],
    })
    # Add column showing fraction of all rows
    total = len(dfall)
    cohort_tbl["Share of all (%)"] = (cohort_tbl["Row count"] / total * 100).round(2)

    lines.append(cohort_tbl.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    lines.append("---")
    lines.append("")

    # ========== RAW SCORE VALIDATION TABLE (Table 3) ==========
    lines.append("## Table 3: TRUE Raw-Score Validation Checks")
    lines.append("")
    lines.append("These checks confirm whether TRUE total raw score is internally consistent with its Part I and Part II components.")
    lines.append("")

    # Rows with complete Total + Part I + Part II
    eq_mask = df[["TotalRawScoreTRUE", "PartIRawScoreTRUE", "PartIIRawScoreTRUE"]].notna().all(axis=1)
    # Formula mismatches: Total != Part I + Part II
    mismatch = (df.loc[eq_mask, "TotalRawScoreTRUE"] - df.loc[eq_mask, "PartIRawScoreTRUE"] - df.loc[eq_mask, "PartIIRawScoreTRUE"]).round(6) != 0

    # StoredVsDerivedMismatch flag count
    if "StoredVsDerivedMismatch" in df.columns:
        stored_mismatch_count = count_true_flags(df["StoredVsDerivedMismatch"])
    else:
        stored_mismatch_count = 0

    # CalcVsDerivedMismatch flag count
    if "CalcVsDerivedMismatch" in df.columns:
        calc_mismatch_count = count_true_flags(df["CalcVsDerivedMismatch"])
    else:
        calc_mismatch_count = 0

    raw_tbl = pd.DataFrame({
        "Validation check": [
            "Rows with complete Total + Part I + Part II",
            "Formula mismatches: Total != Part I + Part II",
            "Stored-vs-derived mismatch flag count",
            "Calc-vs-derived mismatch flag count",
        ],
        "Count of rows": [
            int(eq_mask.sum()),
            int(mismatch.sum()),
            stored_mismatch_count,
            calc_mismatch_count,
        ],
    })
    # Add share of all rows
    raw_tbl["Share of total rows (%)"] = (raw_tbl["Count of rows"] / total * 100).round(4)

    lines.append(raw_tbl.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # Detailed flag value counts
    lines.append("### StoredVsDerivedMismatch detailed distribution")
    lines.append("")
    if "StoredVsDerivedMismatch" in df.columns:
        svd_vc = df["StoredVsDerivedMismatch"].value_counts(dropna=False).rename_axis("Value").reset_index(name="Count")
        lines.append(svd_vc.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    else:
        lines.append("Column not present.")
    lines.append("")

    lines.append("### CalcVsDerivedMismatch detailed distribution")
    lines.append("")
    if "CalcVsDerivedMismatch" in df.columns:
        cvd_vc = df["CalcVsDerivedMismatch"].value_counts(dropna=False).rename_axis("Value").reset_index(name="Count")
        lines.append(cvd_vc.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    else:
        lines.append("Column not present.")
    lines.append("")

    lines.append("---")
    lines.append("")

    # ========== COLLEGE-TYPE CONSISTENCY TABLE (Table 4) ==========
    lines.append("## Table 4: Post-Cleaning UNI_TYPE Consistency by Source College")
    lines.append("")
    lines.append("Each row summarizes how one normalized source college name maps to the cleaned UNI_TYPE field. Any college with more than one mapped type should be reviewed.")
    lines.append("")

    if "NMA_College" in df.columns:
        integrity_base = df[["NMA_College", "UNI_TYPE"]].copy()
        integrity_base["NMA_College_norm"] = (
            integrity_base["NMA_College"]
            .astype("string")
            .str.strip()
            .str.upper()
        )

        college_check = (
            integrity_base.dropna(subset=["NMA_College_norm"])
            .groupby("NMA_College_norm", observed=True)
            .agg(
                records=("UNI_TYPE", "size"),
                n_types=("UNI_TYPE", "nunique"),
                mapped_types=("UNI_TYPE", lambda s: " | ".join(sorted(set(str(x) for x in s if pd.notna(x)))))
            )
            .reset_index()
            .sort_values(["n_types", "records"], ascending=[False, False])
        )
        inconsistent = college_check[college_check["n_types"] > 1]

        lines.append(f"**Colleges checked:** {college_check.shape[0]:,}")
        lines.append("")
        lines.append(f"**Colleges with >1 UNI_TYPE:** {inconsistent.shape[0]:,}")
        lines.append("")
        lines.append("### All inconsistent colleges")
        lines.append("")
        lines.append(inconsistent.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")

        # Also show the consistent colleges summary
        consistent = college_check[college_check["n_types"] == 1]
        lines.append(f"**Colleges with exactly 1 UNI_TYPE:** {consistent.shape[0]:,}")
        lines.append("")
    else:
        lines.append("NMA_College column not available in the dataset.")
        lines.append("")

    lines.append("---")
    lines.append("")

    # ========== UNIVERSITY PAIRING CONFLICTS TABLE (Table 5) ==========
    lines.append("## Table 5: UNIVERSITY to UNI_TYPE and UNI_LOCATION Pairing Audit")
    lines.append("")
    lines.append("This table checks whether each standardized university name maps consistently to one university type and one location.")
    lines.append("")

    if "UNIVERSITY" in df.columns:
        university_pairing = (
            df[["UNIVERSITY", "UNI_TYPE", "UNI_LOCATION"]]
            .dropna(subset=["UNIVERSITY"])
            .groupby("UNIVERSITY", observed=True)
            .agg(
                records=("UNI_TYPE", "size"),
                n_uni_types=("UNI_TYPE", "nunique"),
                n_locations=("UNI_LOCATION", "nunique"),
                uni_types=("UNI_TYPE", lambda s: " | ".join(sorted(set(str(x) for x in s if pd.notna(x))))),
                locations=("UNI_LOCATION", lambda s: " | ".join(sorted(set(str(x) for x in s if pd.notna(x)))))
            )
            .reset_index()
            .sort_values(["n_uni_types", "n_locations", "records"], ascending=[False, False, False])
        )
        pairing_conflicts = university_pairing[
            (university_pairing["n_uni_types"] > 1) | (university_pairing["n_locations"] > 1)
        ]

        lines.append(f"**Universities checked:** {university_pairing.shape[0]:,}")
        lines.append("")
        lines.append(f"**University pairing conflicts:** {pairing_conflicts.shape[0]:,}")
        lines.append("")

        if not pairing_conflicts.empty:
            lines.append("### Pairing conflicts (showing all)")
            lines.append("")
            lines.append(pairing_conflicts.to_markdown(index=False, tablefmt="pipe", numalign="right"))
            lines.append("")

        # University type distribution breakdown
        lines.append("### University type distribution across all universities")
        lines.append("")
        uni_type_dist = university_pairing["n_uni_types"].value_counts().sort_index().rename_axis("Num UNI_TYPEs").reset_index(name="Universities")
        lines.append(uni_type_dist.to_markdown(index=False, tablefmt="pipe", numalign="right"))
        lines.append("")
    else:
        lines.append("UNIVERSITY column not available in the dataset.")
        lines.append("")

    lines.append("---")
    lines.append("")

    # ========== DISTRIBUTION TABLES (Tables 6-8) ==========
    lines.append("## Core Distributions (Tables 6-8)")
    lines.append("")
    lines.append("Values are row counts under the current filters (full unfiltered dataset).")
    lines.append("")

    # Table 6: UNI_TYPE distribution
    lines.append("### Table 6: Distribution of University Type (all rows)")
    lines.append("")
    uni_type_dist = df["UNI_TYPE"].value_counts(dropna=False).rename_axis("UNI_TYPE").reset_index(name="Count")
    uni_type_dist["Share (%)"] = (uni_type_dist["Count"] / total * 100).round(2)
    lines.append(uni_type_dist.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # Table 7: CourseGroup distribution
    lines.append("### Table 7: Distribution of Course Group (all rows)")
    lines.append("")
    course_dist = df["CourseGroup"].value_counts(dropna=False).rename_axis("CourseGroup").reset_index(name="Count")
    course_dist["Share (%)"] = (course_dist["Count"] / total * 100).round(2)
    lines.append(course_dist.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # Table 8: PLE_STATUS_LABEL distribution
    lines.append("### Table 8: Distribution of PLE Status Label (all rows)")
    lines.append("")
    # Derive PLE_STATUS_LABEL if not present (matching helpers.py logic)
    if "PLE_STATUS_LABEL" not in df.columns:
        ple_label = np.where(
            df["IS_PLE_ANALYSIS_SAFE"] == True,
            "Confirmed PLE passer", "No confirmed PLE match"
        )
        ple_vc = pd.Series(ple_label).value_counts(dropna=False).rename_axis("PLE_STATUS_LABEL").reset_index(name="Count")
    else:
        ple_vc = df["PLE_STATUS_LABEL"].value_counts(dropna=False).rename_axis("PLE_STATUS_LABEL").reset_index(name="Count")
    ple_vc["Share (%)"] = (ple_vc["Count"] / total * 100).round(2)
    lines.append(ple_vc.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    lines.append("---")
    lines.append("")

    # ========== ADDITIONAL INTEGRITY CHECKS ==========
    lines.append("## Additional Integrity Checks")
    lines.append("")

    # Year distribution
    lines.append("### Year Distribution (all rows)")
    lines.append("")
    year_dist = df["Year"].value_counts().sort_index().rename_axis("Year").reset_index(name="Count")
    year_dist["Share (%)"] = (year_dist["Count"] / total * 100).round(2)
    lines.append(year_dist.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # HasTRUErawScores flag distribution (handles StringDtype)
    lines.append("### HasTRUErawScores Flag Distribution")
    lines.append("")
    flag_vals = df["HasTRUErawScores"].astype(str).str.strip().str.upper()
    flag_vc = flag_vals.value_counts(dropna=False).rename_axis("HasTRUErawScores").reset_index(name="Count")
    lines.append(flag_vc.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    # PERSON_KEY duplicates check
    lines.append("### Person-Level Duplicate Check")
    lines.append("")
    person_counts = df.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique()
    lines.append(f"- Total unique PERSON_KEYs: {df['PERSON_KEY'].nunique():,}")
    lines.append(f"- Persons with 1 record: {(person_counts == 1).sum():,}")
    lines.append(f"- Persons with 2 records: {(person_counts == 2).sum():,}")
    lines.append(f"- Persons with 3+ records: {(person_counts >= 3).sum():,}")
    lines.append(f"- Max records for one person: {person_counts.max()}")
    lines.append("")

    # IS_PLE_ANALYSIS_SAFE distribution
    lines.append("### IS_PLE_ANALYSIS_SAFE Distribution")
    lines.append("")
    ple_safe_vc = df["IS_PLE_ANALYSIS_SAFE"].value_counts(dropna=False).rename_axis("IS_PLE_ANALYSIS_SAFE").reset_index(name="Count")
    ple_safe_vc["Share (%)"] = (ple_safe_vc["Count"] / total * 100).round(2)
    lines.append(ple_safe_vc.to_markdown(index=False, tablefmt="pipe", numalign="right"))
    lines.append("")

    return "\n".join(lines)


def save():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = RESULTS_DIR / "02_data_integrity.md"
    content = run()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved: {out_path.resolve()}")


if __name__ == "__main__":
    save()
