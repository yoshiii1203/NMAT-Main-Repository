# Key Evidence for Policy Review

**Date:** July 31, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 53 columns)
**Script:** `ched_compute/05_evidence_findings.py`

---

**Date:** July 31, 2026

The following findings synthesise the evidence from all preceding tabs.
They are descriptive observations based on historical NMAT data (2006-2018) and do not constitute regulatory recommendations.

## Finding 1: National Threshold Context

The historical NMAT examinee pool ranges from approximately 70% meeting a B4+ threshold to 61% meeting a B5+ threshold (best-record examinees with a valid percentile bin, 2006-2018).  The marginal group between the two thresholds -- B4 only -- accounts for roughly 9 percentage points of the examinee population.

## Finding 2: Institutional Performance Patterns

Public-undergraduate-institution examinees show a higher median NMAT percentile (57) than private-undergraduate-institution examinees (49).  This pattern is consistent across all NMAT years and may reflect differences in pre-medical preparation, admission selectivity, or other institutional factors not captured in this dataset.  'Institution' here means the undergraduate school, not the medical school. **No medical-school identifier exists in this dataset.** `UNDERGRAD_UNI_TYPE` records the examinee's *undergraduate* institution, not the medical school they attended, and cannot serve as a proxy for CMO §IV.B's SUC-vs-PHEI distinction or for GIDA/IP disadvantage status. No PHEI-level, SUC-vs-PHEI, or per-institution PLE-performance claim can be made from any column in this file.

## Finding 3: NMAT-to-PLE-Passer Linkage Gradient

NMAT-to-PLE-passer linkage rises roughly continuously with score bin, from 12% in the lowest bin (B1) to 71% in the highest bin (B10).  This historical gradient provides context for evaluating the relationship between NMAT scores and licensure outcomes, but is not a PLE pass rate. **Two caveats apply to this gradient, not one.** (1) *Admission selection:* examinees scoring lower on the NMAT were, on average, less likely to be admitted anywhere under the historical, non-uniform cutoffs individual schools actually applied, so lower linkage at the low end reflects **non-admission for at least part of the population, not solely lower ability or a lower chance of passing PLE had they been admitted.** (2) *Matching artefact, now corrected:* the PLE-matching pipeline's name-collision disambiguator previously applied a hard 40th-percentile floor when choosing among multiple same-name candidates, discarding candidates below percentile 40 and rejecting the match outright if none scored at or above 40 -- confined to name-collision groups (unique-name matches were never affected). This has been corrected upstream; every figure below reflects the corrected matcher. Note that the gradient does **not** show a sharp, isolated break at the 40th-percentile boundary -- the B4->B5 step is comparable in size to the B1->B2 and B9->B10 steps, i.e. the increase is roughly continuous across bins, not concentrated at one threshold. Neither this gradient nor any single step in it should be read as evidence about what a *new* cutoff would produce.

## Finding 4: The 40th-Percentile Floor Was Not Uniformly Binding

**The 40th-percentile floor was not uniformly binding historically.** Under a strictly enforced 40th-percentile rule, confirmed PLE passers scoring below that floor (bins B1-B3) should barely exist. They do not: 11.6% of B1 (lowest-decile) examinees and 36.0% of B4 examinees in the observable cohort are confirmed PLE passers (795 confirmed passers in B1 alone). This implies the existing rule -- and by extension any single hard percentile floor -- was not uniformly applied or uniformly binding across the schools examinees actually attended between 2006 and 2014, which bears directly on CMO §IV.B.1's proposal to condition a PHEI's cut-off privilege on a single threshold.

## Finding 5: Historical Linkage Trends

The observable NMAT-to-PLE-passer linkage rate went from 54.2% in 2006 to 36.6% in 2014 across the observable cohort.  The 5-year rolling average was 43.7% as of 2014.  This measure reflects NMAT examinees later matched to PLE passer records and is not directly comparable to official PLE passing rates.  Later years have a shorter observed window for a match to appear even within the observable cohort, which can mechanically lower recent-year rates.

## Finding 6: Public-Institution Threshold Attainment (Descriptive Only)

65.2% of public-undergraduate-institution examinees (17,752 of 27,234) score at Bin 5 or above; only 8.3% fall in the B4-only band the CMO exception addresses.  This is purely descriptive.  Whether this band overlaps with GIDA/IP applicants cannot be determined from this dataset -- GIDA/IP status is not recorded, and 'public undergraduate institution' is neither a GIDA/IP indicator nor equivalent to 'SUC' as the CMO uses the term.  No claim about who benefits from the exception can be supported by this data.

## Finding 7: PLE Matching Sensitivity Check

Restricting to the strictest defensible PLE match (confirmed passer, >=5-year gap, Filipino nationals, B5+ band) yields a linkage rate of 56.0% (23,128 of 41,289) -- genuinely lower than the broader B5+ linkage figures, because this population is not pre-filtered on match status.  This is a real, checkable comparison, not a tautology: it shows that loosening match criteria measurably raises the apparent linkage rate, which should be kept in mind when reading the less-strict figures elsewhere in this dashboard.

## Finding 8: Foreign Examinee Presence

Foreign nationals represent approximately 18.2% of all NMAT records (32,501 verified foreign records out of 178,927 total).  India accounts for the largest share of foreign examinees.  These are NMAT examinee counts, not enrolled medical students.

---
*These findings are limited to the NMAT examinee population. Key data gaps include PLE failure rates, GIDA/IP status, medical school enrollment, and institutional admission criteria. No medical-school identifier exists in this dataset at all.*

> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

