# Data, Methods, and Limitations

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/06_data_limitations.py`

---

**Date:** July 28, 2026

## Dataset Overview

- **Source file:** `NMAT_Exodus.parquet` (54 columns, 178,927 rows)
- **Examination years:** 2006-2018
- **Unique examinees (best record):** 133,558
- **Observable PLE cohort (Year <= 2014):** 64,501
- **Repeat takers:** 33,713 unique persons (25%)

## Key Methodological Choices

### TRUE Raw Score Recalculation
The pipeline recalculated all raw scores from the 8 individual subtest components because 42.2% of the original stored totals were incorrect.

- Rows with complete TRUE scores: 0 (99.97%)
- Formula mismatches (Total != Part I + Part II): 0
- Stored-vs-derived mismatches: 0
- Calc-vs-derived mismatches: 0

### Best-Record Deduplication
33,713 examinees (25%) took the NMAT more than once (up to 9 attempts). Person-level analyses use the best-record flag (`IS_BEST_NMAT_RECORD`), which selects:
- For PLE passers: the specific NMAT attempt that matched to the PLE record.
- For others: the highest percentile attempt, with latest year as tiebreaker.

### Observable Cohort Definition (Year <= 2014)
PLE-linked analyses use examinees whose NMAT year is 2014 or earlier, ensuring a minimum window for PLE passage.
- Observable best-record cohort: 64,501
- Median NMAT-to-PLE year gap: 6.0 years

### Deterministic PLE Matching
All PLE matching is deterministic (exact NMA_AppNo match, manual AppNo match, or deterministic AppNo match). No fuzzy/rapidfuzz matching is used.

**Caveats:**
- The NMAT application number (NMA_AppNo) is not a well-established, consistent identifier across datasets. Matching depends on this number being recorded identically in both datasets.
- Undercounting is possible where numbers differ between datasets.
- The clean subset analysis (Tab 3) uses the strictest criteria as a robustness check.

- Confirmed PLE passers (all rows): 49,986
- Confirmed PLE passers (best record, observable): 29,273
- Clean subset (B5+, Filipino, >=5yr gap): 23,357

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
This dashboard does not assign compliance labels or risk ratings to individual HEIs. The NMAT-linked PLE data is not a complete measure of institutional PLE performance.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

