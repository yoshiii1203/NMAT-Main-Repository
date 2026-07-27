# National NMAT-to-PLE Linkage Benchmark

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/01_national_benchmark.py`

---

## Results

This section computes the annual and 5-year rolling NMAT-to-PLE linkage rate — the share of NMAT examinees from a given year who were later found in official PLE passer records. This is **not** a PLE pass rate.

### Key Metrics

| Metric | Value |
|--------|-------|
| **Total Examinees (Best Record)** | 133,804 |
| **Pre-2015 Cohort Size** | 64,501 |
| **Matched to PLE Passer Records** | 29,273 |
| **Overall NMAT-to-PLE Linkage Rate** | 45.38% |
| **5-Year Rolling Average Linkage (2010-2014)** | 43.46% |

### Annual NMAT-to-PLE Linkage Rates

Table shows, for each year, the number of NMAT examinees (best record), the number found in PLE passer records, the linkage percentage, and the 5-year rolling average where available.

| Year | n (Best Record) | n (Pre-2015 Cohort) | n PLE Matched | Linkage Rate | 5-Year Rolling Avg |
|:----:|:----------------:|:---------------------:|:-------------:|:------------:|:------------------:|
| 2006 | 3,665 | 3,665 | 2,038 | 55.61% | — |
| 2007 | 3,660 | 3,660 | 1,868 | 51.04% | — |
| 2008 | 4,849 | 4,849 | 2,514 | 51.85% | — |
| 2009 | 6,881 | 6,881 | 3,226 | 46.88% | — |
| 2010 | 8,008 | 8,008 | 3,808 | 47.55% | 50.59% |
| 2011 | 8,731 | 8,731 | 3,853 | 44.13% | 48.29% |
| 2012 | 9,145 | 9,145 | 4,066 | 44.46% | 46.97% |
| 2013 | 9,121 | 9,121 | 3,951 | 43.32% | 45.27% |
| 2014 * | 10,441 | 10,441 | 3,949 | 37.82% | 43.46% |
| 2015 | 10,402 | 0 | 0 | N/A (no obs.) | — |
| 2016 | 12,609 | 0 | 0 | N/A (no obs.) | — |
| 2017 | 23,955 | 0 | 0 | N/A (no obs.) | — |
| 2018 | 22,337 | 0 | 0 | N/A (no obs.) | — |

*Observable cohort ends at 2014. Years after 2014 have insufficient time for PLE to be taken and observed in our data.*

### Interpretation

The national NMAT-to-PLE linkage rate across the pre-2015 cohort (64,501 examinees, 29,273 matched) is **45.38%**. This means that 45.38% of NMAT examinees who took the exam between 2006 and 2014 were later found in official PLE passer records.

The 5-year rolling average linkage rate for 2010–2014 is **43.46%**. This declining trend (from ~55% in 2006 to ~38% in 2014) may reflect several factors: (a) increasing NMAT examinee volume outpacing medical school capacity, (b) changes in medical school admission policies, (c) data matching limitations, or (d) examinees taking PLE outside the observation window.

**Important:** This is an NMAT-to-PLE **linkage rate**, not a PLE pass rate. It measures the share of NMAT examinees found in PLE passer records. We cannot distinguish between examinees who never took PLE, those who took it but failed, those who passed but weren't matched, and those who took PLE after our data cutoff.

### Data Quality Notes

- **Cohort definition:** Best NMAT record per examinee (IS_BEST_NMAT_RECORD == True)
- **Observable cohort:** Year ≤ 2014
- **Total unique examinees in best records:** 133,804
- **Pre-2015 examinees:** 64,501
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

