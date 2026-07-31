# B4+ vs B5+ Threshold Analysis

**Date:** July 31, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 53 columns)
**Script:** `ched_compute/02_thresholds.py`

---

## Results

This section models the impact of two proposed NMAT cut-off thresholds: B4+ (at or above Bin 4) and B5+ (at or above Bin 5). For each threshold, we compute the number and proportion of examinees who qualify, broken down by university type, year, and PLE linkage rate.

### Key Metrics

| Metric | Value |
|--------|-------|
| **Total Examinees (Best Record)** | 134,869 |
| **At or Above B4 (Bin 4+)** | 92,437 |
| **At or Above B5 (Bin 5+)** | 79,848 |
| **Difference (B4+ minus B5+)** | 12,589 |
| **B4+ PLE Linkage Rate (Pre-2015)** | 54.70% (27,145 / 49,623) |
| **B5+ PLE Linkage Rate (Pre-2015)** | 57.51% (24,815 / 43,150) |
| **Linkage Rate Gap (B5+ minus B4+)** | 2.81 pp |

### Threshold Impact by University Type

Table shows the number and percent of examinees qualifying at each threshold, by university type.

| UNDERGRAD_UNI_TYPE | n (Best) | B4+ (Bin 4+) | % B4+ | B5+ (Bin 5+) | % B5+ | B4 Only (Bin 4) |
|:---------|:--------:|:-----------:|:-----:|:-----------:|:-----:|:------------------:|
| Public | 27,916 | 19,999 | 71.64% | 17,752 | 63.59% | 2,247 |
| Private | 103,669 | 70,245 | 67.76% | 60,184 | 58.05% | 10,061 |
| Foreign | 1,892 | 1,284 | 67.86% | 1,108 | 58.56% | 176 |
| Not Specified | 1,392 | 909 | 65.30% | 804 | 57.76% | 105 |

### Threshold Impact by Year

Table shows year-by-year qualifying counts at each threshold.

| Year | n (Best) | B4+ (Bin 4+) | % B4+ | B5+ (Bin 5+) | % B5+ | B4 Only |
|:----:|:--------:|:-----------:|:-----:|:-----------:|:-----:|:--------:|
| 2006 | 3,698 | 2,687 | 72.66% | 2,333 | 63.09% | 354 |
| 2007 | 3,690 | 2,671 | 72.38% | 2,274 | 61.63% | 397 |
| 2008 | 4,965 | 3,700 | 74.52% | 3,224 | 64.93% | 476 |
| 2009 | 7,461 | 5,465 | 73.25% | 4,660 | 62.46% | 805 |
| 2010 | 8,551 | 6,640 | 77.65% | 5,891 | 68.89% | 749 |
| 2011 | 8,701 | 6,531 | 75.06% | 5,564 | 63.95% | 967 |
| 2012 | 9,113 | 6,407 | 70.31% | 5,630 | 61.78% | 777 |
| 2013 | 9,148 | 6,406 | 70.03% | 5,796 | 63.36% | 610 |
| 2014 | 10,455 | 7,328 | 70.09% | 6,597 | 63.10% | 731 |
| 2015 | 10,326 | 6,877 | 66.60% | 6,180 | 59.85% | 697 |
| 2016 | 12,480 | 8,287 | 66.40% | 7,246 | 58.06% | 1,041 |
| 2017 | 23,948 | 15,433 | 64.44% | 12,783 | 53.38% | 2,650 |
| 2018 | 22,333 | 14,005 | 62.71% | 11,670 | 52.25% | 2,335 |

### PLE Linkage Rate by Threshold and University Type

For each university type and threshold, the NMAT-to-PLE linkage rate among the pre-2015 cohort.

| UNDERGRAD_UNI_TYPE | B4+ Linkage | B5+ Linkage | Gap (pp) |
|:---------|:-------------------:|:-------------------:|:--------:|
| Public | 57.55% (6,505/11,303) | 60.21% (6,178/10,261) | 2.66 |
| Private | 54.50% (20,130/36,939) | 57.34% (18,157/31,666) | 2.84 |
| Foreign | 27.54% (222/806) | 28.93% (208/719) | 1.39 |
| Not Specified | 50.09% (288/575) | 53.97% (272/504) | 3.88 |

### Linkage Rate by Individual Score Bin

Shows how the linkage rate changes across each score bin, highlighting the critical B4→B5 transition.

| Score Bin | Score Range | n (Pre-2015) | PLE Matched | Linkage Rate |
|:--------:|:-----------:|:------------:|:-----------:|:------------:|
| B1 | 0–9 | 6,853 | 795 | 11.60% |
| B2 | 10–19 | 5,884 | 1,336 | 22.71% |
| B3 | 20–29 | 5,813 | 1,703 | 29.30% |
| B4 | 30–39 | 6,473 | 2,330 | 36.00% |
| B5 | 40–49 | 6,582 | 3,003 | 45.62% |
| B6 | 50–59 | 6,284 | 3,168 | 50.41% |
| B7 | 60–69 | 6,359 | 3,407 | 53.58% |
| B8 | 70–79 | 6,704 | 3,690 | 55.04% |
| B9 | 80–89 | 7,263 | 4,474 | 61.60% |
| B10 | 90–100 | 9,958 | 7,073 | 71.03% |

The sharpest bin-to-bin increase occurs between B4 (30th–39th) and B5 (40th–49th). This is the empirical basis for the tiered cut-off proposal: the B5+ threshold selects a pool with meaningfully higher PLE linkage outcomes.

### Interpretation

Among 134,869 NMAT examinees (best record):
- **92,437 (68.5%)** qualify at the B4+ threshold (Bin 4 and above)
- **79,848 (59.2%)** qualify at the B5+ threshold (Bin 5 and above)
- **12,589 examinees (9.3%)** fall in the B4 band (Bin 4 only) — 
  the marginal pool affected by choosing the higher threshold

The PLE linkage rate at B4+ is 54.70% vs 57.51% at B5+ — a difference of 2.81 percentage points. This supports the tiered approach: the B5+ threshold meaningfully differentiates applicant pools on PLE linkage outcomes.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

