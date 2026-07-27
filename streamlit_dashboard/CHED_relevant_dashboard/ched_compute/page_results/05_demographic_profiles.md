# Demographic Profiles: NMAT Performance and PLE Linkage

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/05_demographic_profiles.py`

---

## Results

This section examines NMAT performance and PLE linkage across demographic dimensions: sex and course group.

### Performance by Sex

| Metric | Value |
|--------|-------|
| **Female Examinees** | 74,153 |
| **Male Examinees** | 59,613 |
| **Sex Not Specified** | 38 |
| **Female Median Percentile** | 50.0 (Q1: 23.0, Q3: 76.0) |
| **Male Median Percentile** | 49.0 (Q1: 22.0, Q3: 76.0) |

#### NMAT Performance by Sex

| Metric | Female | Male | Difference |
|--------|:-----:|:----:|:----------:|
| n | 74,153 | 59,613 | +14,540 |
| Median Percentile | 50.00 | 49.00 | +1.00 |
| Mean Percentile | 49.44 | 49.16 | +0.28 |
| Median TotalRawScore | 122.00 | 121.00 | +1.00 |

#### Percentile Bin Distribution by Sex

| PercentileBin | Female n | Female % | Male n | Male % |
|:------------:|:--------:|:--------:|:------:|:------:|
| B1 | 8,380 | 11.30% | 7,181 | 12.05% |
| B2 | 6,959 | 9.38% | 5,413 | 9.08% |
| B3 | 6,411 | 8.65% | 4,956 | 8.31% |
| B4 | 6,957 | 9.38% | 5,507 | 9.24% |
| B5 | 7,038 | 9.49% | 5,605 | 9.40% |
| B6 | 7,096 | 9.57% | 5,520 | 9.26% |
| B7 | 6,893 | 9.30% | 5,285 | 8.87% |
| B8 | 7,183 | 9.69% | 5,414 | 9.08% |
| B9 | 7,288 | 9.83% | 5,717 | 9.59% |
| B10 | 8,523 | 11.49% | 7,374 | 12.37% |

#### PLE Linkage Rate by Sex

NMAT-to-PLE linkage rates for the observable cohort by sex.

| Sex | n (Observable) | PLE Matched | Linkage Rate |
|:---:|:--------------:|:-----------:|:------------:|
| Female | 38,215 | 17,144 | 44.86% |
| Male | 26,248 | 12,125 | 46.19% |

### Performance by Course Group

| Metric | Value |
|--------|-------|
| **Medical & Allied** | 63,900 (47.8%), Median Pctl: 49.0 |
| **Natural Sciences** | 41,430 (31.0%), Median Pctl: 54.0 |
| **Social & Behavioral Sciences** | 16,462 (12.3%), Median Pctl: 39.0 |
| **Other** | 7,983 (6.0%), Median Pctl: 53.0 |
| **Education** | 3,279 (2.5%), Median Pctl: 51.0 |
| **Engineering & Technology** | 750 (0.6%), Median Pctl: 72.0 |

#### NMAT Performance by Course Group

| Course Group | n | % of Total | Median Pctl | Q1 | Q3 | Median TotalRaw |
|:-------------|:--:|:----------:|:----------:|:--:|:--:|:---------------:|
| Medical & Allied | 63,900 | 47.8% | 49.0 | 25.0 | 73.0 | 121 |
| Natural Sciences | 41,430 | 31.0% | 54.0 | 23.0 | 81.0 | 124 |
| Social & Behavioral Sciences | 16,462 | 12.3% | 39.0 | 11.0 | 73.0 | 112 |
| Other | 7,983 | 6.0% | 53.0 | 26.0 | 79.0 | 130 |
| Education | 3,279 | 2.5% | 51.0 | 26.0 | 78.0 | 130 |
| Engineering & Technology | 750 | 0.6% | 72.0 | 41.0 | 91.0 | 140 |

#### Percentile Bin Distribution by Course Group

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

#### PLE Linkage Rate by Course Group

NMAT-to-PLE linkage rates by course group (observable cohort, Year <= 2014).

| Course Group | n (Observable) | PLE Matched | Linkage Rate |
|:-------------|:--------------:|:-----------:|:------------:|
| Medical & Allied | 35,433 | 16,061 | 45.33% |
| Natural Sciences | 15,219 | 6,921 | 45.48% |
| Other | 6,189 | 2,853 | 46.10% |
| Social & Behavioral Sciences | 4,385 | 1,783 | 40.66% |
| Education | 2,973 | 1,541 | 51.83% |
| Engineering & Technology | 302 | 114 | 37.75% |

### Interpretation

- **Sex:** Female examinees have a median NMAT percentile of 50.0 vs 49.0 for males (difference: +1.0 points). Females represent the majority of NMAT examinees.

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

