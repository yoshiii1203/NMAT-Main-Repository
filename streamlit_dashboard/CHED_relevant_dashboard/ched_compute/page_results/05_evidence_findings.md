# Key Evidence for Policy Review

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/05_evidence_findings.py`

---

**Date:** July 28, 2026

The following findings synthesise the evidence from all preceding tabs.
They are descriptive observations based on historical NMAT data (2006-2018).

## Finding 1: National Threshold Context

The historical NMAT examinee pool ranges from approximately 70% meeting a B4+ threshold to 60% meeting a B5+ threshold (best-record examinees, 2006-2018). The marginal group between the two thresholds — B4 only — accounts for roughly 10 percentage points of the examinee population.

## Finding 2: Institutional Performance Patterns
Public institution examinees show a higher median bin rank (57) than Private institution examinees (49). This pattern is consistent across all NMAT years.

## Finding 3: NMAT-to-PLE-Passer Linkage Gradient
NMAT-to-PLE-passer linkage increases with score bin, from 8% in the lowest bin (B1) to 76% in the highest bin (B10). This historical gradient provides context for evaluating the relationship between NMAT scores and licensure outcomes, but is not a PLE pass rate.

## Finding 4: Historical Linkage Trends
The observable NMAT-to-PLE-passer linkage rate declined from 55.6% in 2006 to 37.8% in 2014 across the observable cohort.
The 5-year rolling average was 43.5% as of 2014.

## Finding 5: Public School Threshold Attainment
Public school examinees already meet the B5+ threshold at a high rate: 64.9% (17,482 out of 26,937) score at Bin 5 or above. Only 8.3% fall in the B4-only band that the CMO exception addresses.

## Finding 6: PLE Matching Robustness
Using the strictest defensible PLE matching criteria (single best-record, clean deterministic match, >=5 year gap, Filipino nationals only), the analysis yields 23,357 B5+ matched passers representing 36.2% of the observable cohort. The distribution by university type and year mirrors the broader analysis.

## Finding 7: Foreign Examinee Presence
Foreign nationals represent approximately 18.2% of all NMAT records (32,501 verified foreign records out of 178,927 total). India accounts for the largest share. These are NMAT examinee counts, not enrolled medical students.

---
*These findings are limited to the NMAT examinee population. Key data gaps include PLE failure rates, GIDA/IP status, medical school enrollment, and institutional admission criteria.*

> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

