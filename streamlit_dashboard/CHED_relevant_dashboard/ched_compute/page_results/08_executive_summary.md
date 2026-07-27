# Executive Summary of Key CHED Dashboard Indicators

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/08_executive_summary.py`

---

## Results

This executive summary provides a quick-reference overview of the key findings across all CHED dashboard analyses. **Important:** NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate.

### Key Indicators

#### Row 1: Volume and Performance

| Metric | Value |
|--------|-------|
| **Total Examinees (Best Record)** | 133,804 |
| **Years Covered** | 2006 -- 2018 |
| **Median Total Raw Score** | 122.0 |
| **Median Percentile** | 50.0 |

#### Row 2: Cohort and Linkage

| Metric | Value |
|--------|-------|
| **Unique Examinees (PERSON_KEY)** | 133,558 |
| **Repeat Takers (>1 attempt)** | 33,714 (25.0%) |
| **Observable Cohort (≤2014)** | 64,501 |
| **NMAT-to-PLE Linkage Rate (pre-2015)** | 45.38% |

### UNI_TYPE Composition

Distribution of examinees by university type (best-record basis). This data can be used for a pie chart.

| UNI_TYPE | n (Best Record) | % of Total |
|:---------|:---------------:|:----------:|
| Public | 27,627 | 20.65% |
| Private | 102,888 | 76.89% |
| Foreign | 1,894 | 1.42% |
| Not Specified | 1,395 | 1.04% |

### CourseGroup Composition

Distribution of examinees by course group (best-record basis). This data can be used for a pie chart.

| CourseGroup | n (Best Record) | % of Total |
|:------------|:---------------:|:----------:|
| Medical & Allied | 63,900 | 47.76% |
| Natural Sciences | 41,430 | 30.96% |
| Social & Behavioral Sciences | 16,462 | 12.30% |
| Other | 7,983 | 5.97% |
| Education | 3,279 | 2.45% |
| Engineering & Technology | 750 | 0.56% |

### Comprehensive Indicator Table

All key figures in a single reference table.

| Indicator | Value | Notes |
|:----------|:-----:|:------|
| **Total NMAT Records (All Attempts)** | 178,927 | Includes repeat takers |
| **Total Examinees (Best Record)** | 133,804 | One record per person |
| **Unique Persons (PERSON_KEY)** | 133,558 | Deduplicated by PERSON_KEY |
| **Years Covered** | 2006 -- 2018 | NMAT data availability |
| **Median Total Raw Score** | 122.0 | Best record basis |
| **Median Percentile** | 50.0 | Best record basis |
| **Repeat Takers (>1 attempt)** | 33,714 (25.0%) | Persons with multiple NMAT records |
| **Observable Cohort (Year <= 2014)** | 64,501 | Best records with sufficient PLE observation window |
| **PLE Matched (Pre-2015)** | 29,273 | Pre-2015 examinees found in PLE passer records |
| **NMAT-to-PLE Linkage Rate (Pre-2015)** | 45.38% | NOT a PLE pass rate |
| **Female Examinees** | 74,153 | Best record basis |
| **Male Examinees** | 59,613 | Best record basis |
| **Foreign Examinees (Best Record)** | 24,079 | Best record basis |
| **Filipino Examinees (Best Record)** | 109,725 | Best record basis |

### Yearly Snapshot

Per-year summary of key metrics (best-record basis).

| Year | n | Median Percentile | Median Raw Score | % Foreign |
|:----:|:--:|:-----------------:|:----------------:|:---------:|
| 2006 | 3,665 | 53.0 | 131.0 | 3.87% |
| 2007 | 3,660 | 52.0 | 130.0 | 8.74% |
| 2008 | 4,849 | 54.0 | 129.0 | 6.99% |
| 2009 | 6,881 | 52.0 | 129.0 | 6.57% |
| 2010 | 8,008 | 57.0 | 135.0 | 5.14% |
| 2011 | 8,731 | 52.0 | 129.0 | 5.36% |
| 2012 | 9,145 | 53.0 | 121.0 | 6.16% |
| 2013 | 9,121 | 59.0 | 128.0 | 7.65% |
| 2014 | 10,441 | 57.0 | 120.0 | 15.90% |
| 2015 | 10,402 | 52.0 | 118.0 | 29.23% |
| 2016 | 12,609 | 48.0 | 123.0 | 29.80% |
| 2017 | 23,955 | 44.0 | 118.0 | 29.30% |
| 2018 | 22,337 | 43.0 | 111.0 | 23.32% |

*Year 2014 is the last year of the observable PLE cohort.*

### Key Observations


1. **Volume growth:** NMAT examinees grew from 3,665 in 2006 to 22,337 in 2018, a significant increase that has implications for medical school capacity.

2. **PLE linkage:** The NMAT-to-PLE linkage rate for the pre-2015 cohort is 45.4%, meaning 29,273 of 64,501 examinees with sufficient observation time were later found in PLE passer records.

3. **Repeat takers:** 33,714 (25.0%) of 134,869 unique persons have taken the NMAT more than once, indicating significant retake behavior.

4. **Gender balance:** Female examinees constitute the majority of NMAT test-takers.

5. **Course dominance:** Medical & Allied and Natural Sciences account for the majority of examinees, reflecting the NMAT's focus on medical and science programs.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

