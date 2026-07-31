# PLE Linkage Alignment with NMAT Performance

**Date:** July 31, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 53 columns)
**Script:** `ched_compute/03_ple_linkage.py`

---

## Results

This section examines how NMAT score bins align with PLE linkage rates. **Important:** All rates shown are NMAT-to-PLE linkage rates — the share of NMAT examinees later found in PLE passer records. These are NOT PLE pass rates.

### Overview

| Metric | Value |
|--------|-------|
| **Pre-2015 Cohort Size (Best Record)** | 69,503 |
| **Matched to PLE Passer Records** | 31,581 |
| **Overall NMAT-to-PLE Linkage Rate** | 45.44% |
| **Source** | NMAT_Exodus.parquet (best records, Year <= 2014) |

### PLE Linkage by Score Bin

The NMAT-to-PLE linkage rate for each score bin. Linkage rises roughly continuously across bins; the B4->B5 step is comparable in size to the steps on either side of it, not an isolated break concentrated at the 40th-percentile boundary.

| Score Bin | Range | n (Pre-2015) | PLE Matched | NMAT-to-PLE Linkage Rate |
|:------------:|:-----:|:------------:|:-----------:|:------------------------:|
| B1 | 0--10th | 6,853 | 795 | 11.60% |
| B2 | 10--20th | 5,884 | 1,336 | 22.71% |
| B3 | 20--30th | 5,813 | 1,703 | 29.30% |
| B4 | 30--40th | 6,473 | 2,330 | 36.00% |
| B5 | 40--50th | 6,582 | 3,003 | 45.62% |
| B6 | 50--60th | 6,284 | 3,168 | 50.41% |
| B7 | 60--70th | 6,359 | 3,407 | 53.58% |
| B8 | 70--80th | 6,704 | 3,690 | 55.04% |
| B9 | 80--90th | 7,263 | 4,474 | 61.60% |
| B10 | 90--100th | 9,958 | 7,073 | 71.03% |

*B4 linkage: 36.00%, B5 linkage: 45.62%, B4->B5 jump: +9.63 pp*


### Linkage by Score Bin and UNDERGRAD_UNI_TYPE

How linkage rates vary by university type within each score bin.

| Score Bin | Public | Private | Foreign | Not Specified |
|:------------:|:---:|:---:|:---:|:---:|
| B1 | 9.83% (1170) | 12.27% (5428) | 5.23% (153) | 5.88% (102) |
| B2 | 18.87% (938) | 23.78% (4760) | 13.04% (92) | 15.96% (94) |
| B3 | 27.38% (884) | 30.07% (4752) | 11.24% (89) | 25.00% (88) |
| B4 | 31.38% (1042) | 37.42% (5273) | 16.09% (87) | 22.54% (71) |
| B5 | 42.78% (1080) | 46.61% (5332) | 21.18% (85) | 44.71% (85) |
| B6 | 48.63% (1098) | 51.03% (5030) | 30.34% (89) | 59.70% (67) |
| B7 | 53.64% (1292) | 54.22% (4899) | 25.00% (104) | 50.00% (64) |
| B8 | 53.05% (1410) | 56.30% (5101) | 26.85% (108) | 48.24% (85) |
| B9 | 61.56% (1764) | 62.70% (5279) | 24.44% (135) | 52.94% (85) |
| B10 | 73.40% (3617) | 70.82% (6025) | 37.88% (198) | 64.41% (118) |

### Linkage by Score Bin and UNDERGRAD_COURSE_GROUP

How linkage rates differ by course group across the score bin distribution.

| Score Bin | Medical & Allied | Natural Sciences | Other | Social & Behavioral Sciences | Education | Engineering & Technology |
|:------------:|:---:|:---:|:---:|:---:|:---:|:---:|
| B1 | 13.05% | 6.32% | 16.28% | 4.63% | 25.00% | 10.00% |
| B2 | 23.74% | 14.34% | 30.80% | 12.30% | 37.17% | 23.81% |
| B3 | 32.09% | 20.76% | 31.37% | 13.76% | 38.33% | 5.00% |
| B4 | 38.46% | 28.10% | 40.33% | 20.92% | 41.39% | 21.43% |
| B5 | 49.16% | 37.53% | 46.56% | 25.34% | 53.98% | 21.43% |
| B6 | 54.21% | 42.27% | 52.11% | 34.39% | 51.90% | 31.58% |
| B7 | 57.02% | 47.58% | 55.59% | 37.78% | 61.22% | 35.71% |
| B8 | 58.51% | 50.03% | 53.90% | 41.09% | 68.46% | 35.71% |
| B9 | 65.84% | 56.14% | 63.39% | 51.86% | 67.06% | 25.00% |
| B10 | 75.49% | 67.86% | 71.69% | 63.88% | 72.58% | 61.29% |

#### UNDERGRAD_COURSE_GROUP Summary

| Course Group | n (Pre-2015) | PLE Matched | NMAT-to-PLE Linkage Rate |
|:-------------|:------------:|:-----------:|:------------------------:|
| Medical & Allied | 38,144 | 17,833 | 46.75% |
| Natural Sciences | 16,512 | 6,994 | 42.36% |
| Other | 6,612 | 3,201 | 48.41% |
| Social & Behavioral Sciences | 4,729 | 1,736 | 36.71% |
| Education | 3,188 | 1,699 | 53.29% |
| Engineering & Technology | 318 | 118 | 37.11% |

### Score Distribution by PLE Status (Box Plot Data)

Median, Q1, and Q3 of NMAT scores for PLE-linked vs non-linked examinees (pre-2015 cohort, best-record basis).

| Metric | PLE Passers (Linked) | Non-Linked Examinees | Difference |
|--------|:--------------------:|:--------------------:|:----------:|
| n | 31,581 | 37,922 | -6,341 |
| Median Score | 69.0 | 38.0 | +31.0 |
| Q1 Score (25th) | 45.0 | 15.0 | +30.0 |
| Q3 Score (75th) | 88.0 | 66.0 | +22.0 |
| Median TotalRawScore | 139.0 | 114.0 | +25.0 |
| Q1 Raw Score | 120.0 | 94.0 | +26.0 |
| Q3 Raw Score | 162.0 | 136.0 | +26.0 |

PLE-linked examinees have substantially higher NMAT scores across all metrics. The median score for PLE-linked examinees is 69, compared to 38 for non-linked examinees.

### Course Group Survival (B8-B10+)

For each course group, the percentage of examinees in the top 3 score bins (B8-B10+, 70th-100th percentile) and the NMAT-to-PLE linkage rate. Higher B8-B10 share generally correlates with higher linkage.

| Course Group | n (Best Record) | n in B8-B10 | % in B8-B10 | PLE Linkage Rate (Pre-2015) |
|:-------------|:---------------:|:-----------:|:-----------:|:--------------------------:|
| Medical & Allied | 64,287 | 18,354 | 28.55% | 46.75% |
| Natural Sciences | 41,514 | 14,760 | 35.55% | 42.36% |
| Social & Behavioral Sciences | 16,492 | 4,485 | 27.20% | 36.71% |
| Other | 8,346 | 2,910 | 34.87% | 48.41% |
| Education | 3,479 | 1,160 | 33.34% | 53.29% |
| Engineering & Technology | 751 | 383 | 51.00% | 37.11% |

### Matching Limitations


NMAT-to-PLE linkage relies on name-based matching across separate datasets. Several limitations apply:

- **Name variations:** Name changes (e.g., marriage), data entry errors, and inconsistent formatting reduce match rates.
- **Incomplete coverage:** Only PLE passers are in the matched dataset. Examinees who took but did not pass PLE, or who took PLE after the dataset cutoff, are not captured.
- **Observable cohort:** Only pre-2015 NMAT examinees have sufficient PLE follow-up time. More recent cohorts cannot be fully evaluated.
- **Clean subset:** The strictest subset (IS_PLE_PASSER, gap >= 5 years, Filipino only) provides more reliable estimates but with reduced sample size.

These limitations mean linkage rates are conservative lower bounds. True NMAT-to-PLE progression rates are likely higher.


### Clean PLE Subset

A strict, defensible subset for more reliable PLE linkage analysis. This subset filters to best-record examinees with IS_PLE_PASSER=True, PLE_YEAR_GAP >= 5, and Filipino citizenship only.

| Metric | Value |
|--------|-------|
| **Clean Subset Size** | 29,417 |
| **PLE Matched in Clean Subset** | 29,417 |
| **NMAT-to-PLE Linkage Rate (Clean)** | 100.00% |
| **Filters Applied** | Best record, IS_PLE_PASSER, Gap >= 5yrs, Filipino |

#### Clean Subset: Linkage by Score Bin

| Score Bin | n (Clean) | PLE Matched | Linkage Rate |
|:--------:|:---------:|:-----------:|:------------:|
| B1 | 720 | 720 | 100.00% |
| B2 | 1,239 | 1,239 | 100.00% |
| B3 | 1,592 | 1,592 | 100.00% |
| B4 | 2,176 | 2,176 | 100.00% |
| B5 | 2,792 | 2,792 | 100.00% |
| B6 | 2,949 | 2,949 | 100.00% |
| B7 | 3,183 | 3,183 | 100.00% |
| B8 | 3,422 | 3,422 | 100.00% |
| B9 | 4,184 | 4,184 | 100.00% |
| B10 | 6,598 | 6,598 | 100.00% |

**Caution:** This small subset is the most defensible for causal inference but may not be representative of the full examinee population. Use alongside the full observable cohort analysis above.


### Key Interpretation


The NMAT-to-PLE linkage rate increases monotonically from B1 (lowest) to B10 (highest). This monotonic relationship provides empirical support for NMAT cut-off scores as a screening tool: examinees with higher NMAT scores are more likely to be found in PLE passer records.

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

