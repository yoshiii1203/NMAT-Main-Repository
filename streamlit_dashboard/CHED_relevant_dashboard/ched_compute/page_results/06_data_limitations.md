# Data, Methods, and Limitations

**Date:** July 31, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 53 columns)
**Script:** `ched_compute/06_data_limitations.py`

---

**Date:** July 31, 2026

## Dataset Overview

- **Source file:** `NMAT_Exodus.parquet` (53 columns, 178,927 rows)
- **Examination years:** 2006-2018
- **Unique examinees (best record):** 134,869
- **Observable PLE cohort (best attempt, Year <= 2014):** 69,503
- **Repeat takers:** 33,713 unique persons (25%)

**Data quality note:** 6,148 PERSON_KEY identifiers have contradictory SEX recorded across their rows (PERSON_KEY_AMBIGUOUS), indicating a possible identity collision. Disclosed, not silently corrected.

## Key Methodological Choices

### TRUE Raw Score Recalculation
Of the 99,316 records that carry a stored total, 56,065 (56.5%) disagreed with the sum of the 8 component subtest scores (31.3% of all 178,927 records). Computed live from `StoredVsDerivedMismatch` -- never hardcoded.

- Rows with complete TRUE scores: 178,882 (99.97%)
- Stored-total mismatches: 56,065 of 99,316 rows with a stored total (56.5%)

### Best-Record Deduplication
33,713 examinees (25%) took the NMAT more than once (up to 9 attempts). Person-level analyses use the best-record flag (`IS_BEST_NMAT_RECORD`), which selects, for every person, the highest NMAT percentile, latest year as tiebreaker, then lowest application number -- one uniform rule for passers and non-passers alike.

### Observable Cohort Definition
PLE-linked analyses use `IS_BEST_OBSERVABLE_RECORD` (each person's best attempt among rows with Year <= 2014) -- deliberately not the same as filtering the overall best-record flag to Year<=2014, which would silently drop people whose overall-best attempt fell after 2014 and inflate the observed linkage rate.
- Observable cohort: 69,503
- Median NMAT-to-PLE year gap: 6 years

### Deterministic PLE Matching
All PLE matching is deterministic (exact NMA_AppNo match, manual AppNo match, or deterministic AppNo match). No fuzzy/rapidfuzz matching is used.

**Caveats:**
- The NMAT application number (NMA_AppNo) is not a well-established, consistent identifier across datasets. Matching depends on this number being recorded identically in both datasets.
- Match outcome breakdown (`PLE_MATCH_OUTCOME`, all rows): accepted 49,086, rejected_ambiguous_person 8,216 (name-collision candidate found but rejected as genuinely ambiguous), no_match 121,623. `PLE_YEAR_UNCERTAIN` flags 110 confirmed passers whose PLE year is not determinable.
- `PLE_YEAR_PASSED`, `PLE_MATCH_METHOD`, `PLE_YEAR_GAP` are diagnostic metadata, not authoritative passer counts, and do not nest inside `IS_PLE_PASSER`: non-null for 54,529 / 57,304 / 46,219 rows respectively.
- **PLE-matching bias against below-40th-percentile examinees (disclosed).** The name-collision disambiguator (`2_PLE_Matching_Pipeline.ipynb`, `disambiguate()` Step 4) previously applied a hard filter -- not a tie-break -- discarding every candidate scoring below the 40th NMAT percentile and rejecting the match outright if no candidate scored at or above 40. That constant, 40, is exactly the CMO threshold under review. Confined to name-collision groups, now corrected upstream, but present in every below-B4/B5 linkage figure derived from this parquet snapshot.
- The Stress-Test analysis (Tab 3) uses the strictest criteria (confirmed match, >=5 year gap, Filipino nationals only) as a genuine, non-tautological sensitivity check -- population is NOT pre-filtered on match status.

- Confirmed PLE passers (all rows): 49,086
- Confirmed PLE passers (best-attempt, observable cohort): 31,581
- Strict-criteria B5+ subset (Filipino, >=5yr gap): 23,128

## Limitations Relevant to CHED Decision-Making

### PLE Outcomes
The dataset only identifies NMAT examinees later matched to PLE passer records. It does not contain all PLE takers or PLE failures. This dashboard reports NMAT-to-PLE-passer linkage rates, not PLE pass rates.

### GIDA and IP Status
The dataset does not contain indicators for Geographically Isolated and Disadvantaged Area (GIDA) residence or Indigenous Peoples (IP) membership. The CMO exception for B4-only applicants from these groups requires documentation not available in this dataset.

### Medical School Admissions and Enrollment
This dataset records NMAT examinees, not enrolled medical students. The number of examinees at or above a threshold represents the available applicant pool, not actual enrollment.

### Foreign Student Enrollment Cap
The CMO caps foreign student enrollment at 10 slots per incoming class at SUCs. The dataset shows NMAT examinees by citizenship, not enrolled foreign students.

### Composite Ranking for Foreign Applicants
The dataset does not contain GWA, interview scores, or other admission criteria needed for composite ranking analysis.

### PHEI Accountability and Sanctions
This dataset contains NO medical-school identifier of any kind. No PHEI, SUC, or any other institution-level PLE performance, compliance label, or risk rating can be computed from any column in this file. UNDERGRAD_UNI_TYPE describes the examinee's undergraduate school and must never be read as a stand-in for the medical school.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

