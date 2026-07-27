# PLE Linkage Alignment with NMAT Performance

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/06_ple_alignment.py`

---

## Results

This section examines how NMAT percentile bins align with PLE linkage rates. **Important:** All rates shown are NMAT-to-PLE linkage rates — the share of NMAT examinees later found in PLE passer records. These are NOT PLE pass rates.

### Overview

| Metric | Value |
|--------|-------|
| **Pre-2015 Cohort Size (Best Record)** | 64,501 |
| **Matched to PLE Passer Records** | 29,273 |
| **Overall NMAT-to-PLE Linkage Rate** | 45.38% |
| **Source** | NMAT_Exodus.parquet (best records, Year <= 2014) |

### PLE Linkage by PercentileBin

The NMAT-to-PLE linkage rate for each percentile bin. The B4->B5 jump is the largest adjacent-bin increase.

| PercentileBin | Range | n (Pre-2015) | PLE Matched | NMAT-to-PLE Linkage Rate |
|:------------:|:-----:|:------------:|:-----------:|:------------------------:|
| B1 | 0--10th | 6,104 | 505 | 8.27% |
| B2 | 10--20th | 5,254 | 830 | 15.80% |
| B3 | 20--30th | 5,228 | 997 | 19.07% |
| B4 | 30--40th | 5,741 | 1,312 | 22.85% |
| B5 | 40--50th | 6,229 | 2,882 | 46.27% |
| B6 | 50--60th | 5,831 | 2,992 | 51.31% |
| B7 | 60--70th | 5,942 | 3,359 | 56.53% |
| B8 | 70--80th | 6,355 | 3,819 | 60.09% |
| B9 | 80--90th | 6,854 | 4,595 | 67.04% |
| B10 | 90--100th | 9,657 | 7,352 | 76.13% |

*B4 linkage: 22.85%, B5 linkage: 46.27%, B4->B5 jump: +23.41 pp*


### Linkage by PercentileBin and UNI_TYPE

How linkage rates vary by university type within each percentile bin.

| PercentileBin | Public | Private | Foreign | Not Specified |
|:------------:|:---:|:---:|:---:|:---:|
| B1 | 6.70% (1030) | 8.82% (4843) | 3.47% (144) | 4.60% (87) |
| B2 | 11.44% (822) | 16.94% (4257) | 7.87% (89) | 9.30% (86) |
| B3 | 17.47% (790) | 19.62% (4276) | 9.52% (84) | 15.38% (78) |
| B4 | 17.77% (895) | 24.22% (4703) | 10.00% (80) | 9.52% (63) |
| B5 | 43.37% (1026) | 47.26% (5034) | 18.29% (82) | 49.43% (87) |
| B6 | 49.22% (1022) | 52.05% (4657) | 30.23% (86) | 59.09% (66) |
| B7 | 56.53% (1210) | 57.28% (4567) | 25.96% (104) | 52.46% (61) |
| B8 | 57.02% (1324) | 61.73% (4844) | 28.44% (109) | 55.13% (78) |
| B9 | 65.09% (1630) | 68.76% (5007) | 29.32% (133) | 61.90% (84) |
| B10 | 77.48% (3468) | 76.74% (5876) | 38.97% (195) | 67.80% (118) |

### Linkage by PercentileBin and CourseGroup

How linkage rates differ by course group across the percentile distribution.

| PercentileBin | Medical & Allied | Natural Sciences | Other | Social & Behavioral Sciences | Education | Engineering & Technology |
|:------------:|:---:|:---:|:---:|:---:|:---:|:---:|
| B1 | 8.83% | 3.97% | 12.50% | 3.47% | 22.38% | 10.53% |
| B2 | 16.08% | 8.47% | 21.76% | 9.43% | 31.80% | 16.67% |
| B3 | 19.75% | 13.36% | 21.32% | 11.79% | 32.49% | 5.88% |
| B4 | 24.04% | 14.95% | 29.89% | 12.50% | 31.43% | 14.29% |
| B5 | 49.99% | 38.62% | 45.90% | 25.29% | 53.21% | 22.22% |
| B6 | 55.21% | 44.49% | 50.18% | 37.54% | 48.08% | 31.58% |
| B7 | 59.41% | 54.22% | 53.65% | 40.79% | 62.91% | 38.46% |
| B8 | 62.90% | 57.93% | 57.06% | 46.48% | 70.48% | 30.77% |
| B9 | 70.07% | 64.80% | 65.75% | 59.65% | 69.61% | 26.47% |
| B10 | 79.86% | 73.23% | 75.26% | 72.31% | 78.45% | 63.74% |

#### CourseGroup Summary

| Course Group | n (Pre-2015) | PLE Matched | NMAT-to-PLE Linkage Rate |
|:-------------|:------------:|:-----------:|:------------------------:|
| Medical & Allied | 35,433 | 16,061 | 45.33% |
| Natural Sciences | 15,219 | 6,921 | 45.48% |
| Other | 6,189 | 2,853 | 46.10% |
| Social & Behavioral Sciences | 4,385 | 1,783 | 40.66% |
| Education | 2,973 | 1,541 | 51.83% |
| Engineering & Technology | 302 | 114 | 37.75% |

### Score Distribution by PLE Status (Box Plot Data)

Median, Q1, and Q3 of NMAT scores for PLE-linked vs non-linked examinees (pre-2015 cohort, best-record basis).

| Metric | PLE Passers (Linked) | Non-Linked Examinees | Difference |
|--------|:--------------------:|:--------------------:|:----------:|
| n | 29,273 | 35,228 | -5,955 |
| Median Percentile | 73.0 | 36.0 | +37.0 |
| Q1 Percentile (25th) | 52.0 | 15.0 | +37.0 |
| Q3 Percentile (75th) | 90.0 | 63.0 | +27.0 |
| Median TotalRawScore | 143.0 | 112.0 | +31.0 |
| Q1 Raw Score | 125.0 | 94.0 | +31.0 |
| Q3 Raw Score | 164.0 | 134.0 | +30.0 |

PLE-linked examinees have substantially higher NMAT scores across all metrics. The median percentile for PLE-linked examinees is 73, compared to 36 for non-linked examinees.

### Course Group Survival (B8-B10)

For each course group, the percentage of examinees in the top 3 percentile bins (B8-B10, 70th-100th percentile) and the NMAT-to-PLE linkage rate. Higher B8-B10 share generally correlates with higher linkage.

| Course Group | n (Best Record) | n in B8-B10 | % in B8-B10 | PLE Linkage Rate (Pre-2015) |
|:-------------|:---------------:|:-----------:|:-----------:|:--------------------------:|
| Medical & Allied | 63,900 | 18,138 | 28.38% | 45.33% |
| Natural Sciences | 41,430 | 14,660 | 35.38% | 45.48% |
| Social & Behavioral Sciences | 16,462 | 4,456 | 27.07% | 40.66% |
| Other | 7,983 | 2,778 | 34.80% | 46.10% |
| Education | 3,279 | 1,086 | 33.12% | 51.83% |
| Engineering & Technology | 750 | 382 | 50.93% | 37.75% |

### Key Interpretation


The NMAT-to-PLE linkage rate increases monotonically from B1 (lowest) to B10 (highest). This monotonic relationship provides empirical support for NMAT cut-off scores as a screening tool: examinees with higher NMAT percentiles are more likely to be found in PLE passer records.

**However, this is an association, not a causal relationship.** Examinees with higher NMAT scores may: (a) attend higher-quality medical schools, (b) have better study habits or preparation, (c) be more motivated, or (d) have other advantages that contribute both to higher NMAT scores and higher PLE linkage. The linkage rate alone cannot be used to set a specific cut-off threshold without consideration of other factors.

**Critical caveat:** Our data contains only PLE passers. The linkage rate is affected by: (1) whether the examinee took PLE, (2) whether they passed, and (3) whether the match succeeded. We cannot distinguish these factors.

**Course group survival:** The share of examinees in B8-B10 varies notably by course group, from ~27% (Social & Behavioral Sciences) to ~51% (Engineering & Technology). However, smaller sample sizes for some groups warrant cautious interpretation.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

