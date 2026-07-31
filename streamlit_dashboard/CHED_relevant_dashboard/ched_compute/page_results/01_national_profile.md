# National NMAT Profile and Linkage Analysis

**Date:** July 31, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 53 columns)
**Script:** `ched_compute/01_national_profile.py`

---

## Results

This section presents the national NMAT examinee profile and computes the annual and 5-year rolling NMAT-to-PLE linkage rate — the share of NMAT examinees from a given year who were later found in official PLE passer records. This is **not** a PLE pass rate.

### Score Bin Reference

Each bin corresponds to a range of NMAT percentile rank scores. B4+ corresponds to the CMO exception floor (30th–39th percentile range). B5+ corresponds to the SUC standard floor (40th–49th percentile range).

| Bin | Score Range | Threshold |
|:---:|:-----------:|:----------|
| B1 | 0–9 |  |
| B2 | 10–19 |  |
| B3 | 20–29 |  |
| B4 | 30–39 | CMO exception floor (B4+) |
| B5 | 40–49 | SUC standard floor (B5+) |
| B6 | 50–59 |  |
| B7 | 60–69 |  |
| B8 | 70–79 |  |
| B9 | 80–89 |  |
| B10 | 90–100 |  |

### Key Metrics

| Metric | Value |
|--------|-------|
| **Total Examinees (Best Record)** | 134,869 |
| **Pre-2015 Cohort Size** | 69,503 |
| **Matched to PLE Passer Records** | 31,581 |
| **Overall NMAT-to-PLE Linkage Rate** | 45.44% |
| **5-Year Rolling Average Linkage (2010-2014)** | 43.74% |

### Annual NMAT-to-PLE Linkage Rates

Table shows, for each year, the number of NMAT examinees (best record), the number found in PLE passer records, the linkage percentage, and the 5-year rolling average where available.

| Year | n (Best Record) | n (Pre-2015 Cohort) | n PLE Matched | Linkage Rate | 5-Year Rolling Avg |
|:----:|:----------------:|:---------------------:|:-------------:|:------------:|:------------------:|
| 2006 | 3,698 | 3,698 | 2,005 | 54.22% | — |
| 2007 | 3,690 | 3,690 | 1,832 | 49.65% | — |
| 2008 | 4,965 | 4,965 | 2,583 | 52.02% | — |
| 2009 | 7,461 | 7,461 | 3,757 | 50.36% | — |
| 2010 | 8,551 | 8,623 | 4,534 | 52.58% | 51.77% |
| 2011 | 8,701 | 8,842 | 3,918 | 44.31% | 49.78% |
| 2012 | 9,113 | 9,405 | 4,006 | 42.59% | 48.37% |
| 2013 | 9,148 | 9,867 | 4,210 | 42.67% | 46.50% |
| 2014 * | 10,455 | 12,952 | 4,736 | 36.57% | 43.74% |
| 2015 | 10,326 | 0 | 0 | N/A (no obs.) | — |
| 2016 | 12,480 | 0 | 0 | N/A (no obs.) | — |
| 2017 | 23,948 | 0 | 0 | N/A (no obs.) | — |
| 2018 | 22,333 | 0 | 0 | N/A (no obs.) | — |

*Observable cohort ends at 2014. Years after 2014 have insufficient time for PLE to be taken and observed in our data.*

### Interpretation

The national NMAT-to-PLE linkage rate across the pre-2015 cohort (69,503 examinees, 31,581 matched) is **45.44%**. This means that 45.44% of NMAT examinees who took the exam between 2006 and 2014 were later found in official PLE passer records.

The 5-year rolling average linkage rate for 2010–2014 is **43.74%**. This declining trend (from ~55% in 2006 to ~38% in 2014) may reflect several factors: (a) increasing NMAT examinee volume outpacing medical school capacity, (b) changes in medical school admission policies, (c) data matching limitations, or (d) examinees taking PLE outside the observation window.

**Important:** This is an NMAT-to-PLE **linkage rate**, not a PLE pass rate. It measures the share of NMAT examinees found in PLE passer records, not the share who passed PLE. We cannot distinguish between examinees who never took PLE, those who took it but failed, those who passed but weren't matched, and those who took PLE after our data cutoff.

### Data Quality Notes

- **Cohort definition:** Best NMAT record per examinee (IS_BEST_NMAT_RECORD == True)
- **Observable cohort:** Year ≤ 2014
- **Total unique examinees in best records:** 134,869
- **Pre-2015 examinees:** 69,503
- **PLE match source:** PLE_DATA.csv (passers only, 43,630 records)
- **Linkage rate is a lower bound** — some examinees may have passed PLE after our observation window


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

