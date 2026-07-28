# Demographic Profiles: NMAT Performance and PLE Linkage

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/05_demographic_profiles.py`

---

## Results

This section examines NMAT performance and PLE linkage across demographic dimensions: sex, course group, repeat taker status, and PLE year gap.

### Sex-Based Analysis

| Metric | Value |
|--------|-------|
| **Female Examinees** | 74,153 |
| **Male Examinees** | 59,613 |
| **Sex Not Specified** | 38 |
| **Female Median Percentile** | 50.0 (Q1: 23.0, Q3: 76.0) |
| **Male Median Percentile** | 49.0 (Q1: 22.0, Q3: 76.0) |

#### Sex Comparison Table

| Metric | Female | Male | Difference |
|--------|:-----:|:----:|:----------:|
| n | 74,153 | 59,613 | +14,540 |
| Median Percentile | 50.00 | 49.00 | +1.00 |
| Mean Percentile | 49.44 | 49.16 | +0.28 |
| Median TotalRawScore | 122.00 | 121.00 | +1.00 |

#### PLE Linkage by Sex

NMAT-to-PLE linkage rates by sex (pre-2015 cohort, best-record basis).

| Sex | n (Pre-2015) | PLE Matched | NMAT-to-PLE Linkage Rate |
|:----|:------------:|:-----------:|:------------------------:|
| Female | 38,215 | 17,144 | 44.86% |
| Male | 26,248 | 12,125 | 46.19% |

### Repeat Taker Analysis

Repeat takers are persons with more than one NMAT attempt. The repeat taker rate quantifies how many unique examinees retake the exam.

| Metric | Value |
|--------|-------|
| **Total Unique Persons (PERSON_KEY)** | 134,869 |
| **Repeat Takers (>1 attempt)** | 33,714 |
| **Repeat Taker Rate** | 25.00% |
| **Single Attempt Only** | 101,155 |

#### Attempt Count Distribution

| Attempts | Persons | % of Total |
|:--------:|:-------:|:----------:|
| 1 | 101,155 | 75.00% |
| 2 | 25,813 | 19.14% |
| 3 | 6,046 | 4.48% |
| 4 | 1,411 | 1.05% |
| 5 | 332 | 0.25% |
| 6 | 88 | 0.07% |
| 7 | 17 | 0.01% |
| 8 | 6 | 0.00% |
| 9 | 1 | 0.00% |

### Course Group Performance

NMAT performance and PLE linkage by course group (best-record basis).

| Course Group | n | % of Total | Median Pctl | Q1 Pctl | Q3 Pctl | Median Raw |
|:-------------|:--:|:----------:|:-----------:|:-------:|:-------:|:----------:|
| Medical & Allied | 63,900 | 47.8% | 49.0 | 25.0 | 73.0 | 121 |
| Natural Sciences | 41,430 | 31.0% | 54.0 | 23.0 | 81.0 | 124 |
| Social & Behavioral Sciences | 16,462 | 12.3% | 39.0 | 11.0 | 73.0 | 112 |
| Other | 7,983 | 6.0% | 53.0 | 26.0 | 79.0 | 130 |
| Education | 3,279 | 2.5% | 51.0 | 26.0 | 78.0 | 130 |
| Engineering & Technology | 750 | 0.6% | 72.0 | 41.0 | 91.0 | 140 |

#### Course Group x PercentileBin Distribution

Percentage of each course group's examinees in each percentile bin.

| PercentileBin | Medical & Allied | Natural Sciences | Social & Behavioral Sciences | Other | Education | Engineering & Technology |
|:------------:|:---:|:---:|:---:|:---:|:---:|:---:|
| B1 | 9.94% | 11.94% | 19.06% | 10.05% | 9.52% | 5.07% |
| B2 | 9.67% | 8.28% | 10.55% | 8.56% | 9.15% | 5.73% |
| B3 | 9.33% | 7.29% | 8.27% | 8.41% | 9.45% | 5.73% |
| B4 | 10.51% | 8.07% | 8.01% | 9.19% | 9.55% | 5.47% |
| B5 | 10.77% | 8.14% | 7.50% | 9.42% | 10.34% | 8.40% |
| B6 | 10.48% | 8.50% | 7.93% | 9.32% | 8.72% | 8.53% |
| B7 | 9.62% | 9.14% | 7.13% | 9.03% | 9.09% | 7.33% |
| B8 | 9.64% | 9.64% | 7.55% | 10.32% | 9.33% | 9.73% |
| B9 | 9.18% | 10.63% | 8.47% | 11.36% | 10.03% | 14.27% |
| B10 | 9.57% | 15.12% | 11.04% | 13.12% | 13.75% | 26.93% |

#### NMAT-to-PLE Linkage by Course Group

NMAT-to-PLE linkage rates by course group (observable cohort, Year <= 2014, best-record basis).

| Course Group | n (Observable) | PLE Matched | NMAT-to-PLE Linkage Rate |
|:-------------|:--------------:|:-----------:|:------------------------:|
| Medical & Allied | 35,433 | 16,061 | 45.33% |
| Natural Sciences | 15,219 | 6,921 | 45.48% |
| Other | 6,189 | 2,853 | 46.10% |
| Social & Behavioral Sciences | 4,385 | 1,783 | 40.66% |
| Education | 2,973 | 1,541 | 51.83% |
| Engineering & Technology | 302 | 114 | 37.75% |

### PLE Year Gap Distribution

For examinees matched to PLE passer records, the gap (in years) between NMAT and PLE. This indicates how long after NMAT examinees typically pass PLE.

| Metric | Value |
|--------|-------|
| **Matched Examinees with Gap Data** | 27,901 |
| **Median NMAT-to-PLE Gap** | 6 years |
| **Mean NMAT-to-PLE Gap** | 6.5 years |
| **Minimum Gap** | 5 years |
| **Maximum Gap** | 15 years |

#### Gap Distribution

| Gap (Years) | n | % of Matched |
|:-----------:|:--:|:------------:|
| 5 | 2,308 | 8.27% |
| 6 | 14,759 | 52.90% |
| 7 | 7,283 | 26.10% |
| 8 | 2,260 | 8.10% |
| 9 | 775 | 2.78% |
| 10 | 294 | 1.05% |
| 11 | 128 | 0.46% |
| 12 | 62 | 0.22% |
| 13 | 23 | 0.08% |
| 14 | 5 | 0.02% |
| 15 | 4 | 0.01% |

The typical gap is 6 years (mean 6.5), consistent with a standard 4-year undergraduate degree followed by immediate PLE.

### Yearly Trend Summary

Per-year NMAT performance metrics (best-record basis). This shows how examinee volume and scores have evolved over time.

| Year | n | Median Percentile | Median Raw Score | % Foreign | Female % |
|:----:|:--:|:-----------------:|:----------------:|:---------:|:--------:|
| 2006 | 3,665 | 53.0 | 131.0 | 3.87% | 66.44% |
| 2007 | 3,660 | 52.0 | 130.0 | 8.74% | 63.11% |
| 2008 | 4,849 | 54.0 | 129.0 | 6.99% | 61.08% |
| 2009 | 6,881 | 52.0 | 129.0 | 6.57% | 61.34% |
| 2010 | 8,008 | 57.0 | 135.0 | 5.14% | 47.15% |
| 2011 | 8,731 | 52.0 | 129.0 | 5.36% | 55.07% |
| 2012 | 9,145 | 53.0 | 121.0 | 6.16% | 61.33% |
| 2013 | 9,121 | 59.0 | 128.0 | 7.65% | 62.33% |
| 2014 | 10,441 | 57.0 | 120.0 | 15.90% | 61.38% |
| 2015 | 10,402 | 52.0 | 118.0 | 29.23% | 57.91% |
| 2016 | 12,609 | 48.0 | 123.0 | 29.80% | 58.17% |
| 2017 | 23,955 | 44.0 | 118.0 | 29.30% | 59.98% |
| 2018 | 22,337 | 43.0 | 111.0 | 23.32% | 36.76% |

### Key Insights

- **Sex:** Female examinees have a median NMAT percentile of 50.0 vs 49.0 for males (difference: +1.0 points). Females represent the majority of NMAT examinees.

- **Repeat taking:** 33,714 (25.0%) of 134,869 unique examinees have taken the NMAT more than once.

- **Course Group:** Medical & Allied is the largest course group (63,900 examinees, 47.8%). Medical & Allied courses dominate the NMAT-taking population.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

