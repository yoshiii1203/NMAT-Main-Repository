# PLE Linkage Alignment with NMAT Performance

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/06_ple_alignment.py`

---

## Results

This section examines how NMAT percentile bins align with PLE linkage rates. **Important:** All rates shown are NMAT-to-PLE linkage rates — the share of NMAT examinees later found in PLE passer records. These are NOT PLE pass rates.

### Key Metrics

| Metric | Value |
|--------|-------|
| **Pre-2015 Cohort Size** | 64,501 |
| **Matched to PLE Passer Records** | 29,273 |
| **Overall NMAT-to-PLE Linkage Rate** | 45.38% |
| **Source** | NMAT_Exodus.parquet (best records, Year <= 2014) |

### PLE Linkage Rate by Percentile Bin

The NMAT-to-PLE linkage rate for each percentile bin. The B4->B5 jump is the largest adjacent-bin increase.

| PercentileBin | Range | n (Pre-2015) | PLE Matched | Linkage Rate |
|:------------:|:-----:|:------------:|:-----------:|:------------:|
| B1 | 0–10th | 6,104 | 505 | 8.27% |
| B2 | 10–20th | 5,254 | 830 | 15.80% |
| B3 | 20–30th | 5,228 | 997 | 19.07% |
| B4 | 30–40th | 5,741 | 1,312 | 22.85% |
| B5 | 40–50th | 6,229 | 2,882 | 46.27% |
| B6 | 50–60th | 5,831 | 2,992 | 51.31% |
| B7 | 60–70th | 5,942 | 3,359 | 56.53% |
| B8 | 70–80th | 6,355 | 3,819 | 60.09% |
| B9 | 80–90th | 6,854 | 4,595 | 67.04% |
| B10 | 90–100th | 9,657 | 7,352 | 76.13% |

The **B4→B5 jump** is the largest between adjacent bins: +23.41 percentage points (from 22.85% to 46.27%). This validates the tiered cut-off approach — the 40th percentile (B5+) selects a cohort with meaningfully higher PLE linkage.

### PLE Linkage Rate by University Type and Percentile Bin

Heatmap-style table showing how linkage rates vary across both dimensions.

| PercentileBin | Public | Private | Foreign | Not Specified |
|:------------:|:---:|:---:|:---:|:---:|
| B1 | 6.70% | 8.82% | 3.47% | 4.60% |
| B2 | 11.44% | 16.94% | 7.87% | 9.30% |
| B3 | 17.47% | 19.62% | 9.52% | 15.38% |
| B4 | 17.77% | 24.22% | 10.00% | 9.52% |
| B5 | 43.37% | 47.26% | 18.29% | 49.43% |
| B6 | 49.22% | 52.05% | 30.23% | 59.09% |
| B7 | 56.53% | 57.28% | 25.96% | 52.46% |
| B8 | 57.02% | 61.73% | 28.44% | 55.13% |
| B9 | 65.09% | 68.76% | 29.32% | 61.90% |
| B10 | 77.48% | 76.74% | 38.97% | 67.80% |

#### Overall PLE Linkage by University Type

Aggregated across all percentile bins.

| UNI_TYPE | n (Pre-2015) | PLE Matched | Linkage Rate |
|:---------|:------------:|:-----------:|:------------:|
| Public | 13,555 | 6,786 | 50.06% |
| Private | 48,991 | 21,909 | 44.72% |
| Foreign | 1,124 | 248 | 22.06% |
| Not Specified | 831 | 330 | 39.71% |

### PLE Linkage Rate by Course Group and Percentile Bin

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

#### Overall PLE Linkage by Course Group

| Course Group | n (Pre-2015) | PLE Matched | Linkage Rate |
|:-------------|:------------:|:-----------:|:------------:|
| Medical & Allied | 35,433 | 16,061 | 45.33% |
| Natural Sciences | 15,219 | 6,921 | 45.48% |
| Other | 6,189 | 2,853 | 46.10% |
| Social & Behavioral Sciences | 4,385 | 1,783 | 40.66% |
| Education | 2,973 | 1,541 | 51.83% |
| Engineering & Technology | 302 | 114 | 37.75% |

### Interpretation

The NMAT-to-PLE linkage rate increases monotonically from B1 (lowest) to B10 (highest). This monotonic relationship provides empirical support for NMAT cut-off scores as a screening tool: examinees with higher NMAT percentiles are more likely to be found in PLE passer records.

**However, this is an association, not a causal relationship.** Examinees with higher NMAT scores may: (a) attend higher-quality medical schools, (b) have better study habits or preparation, (c) be more motivated, or (d) have other advantages that contribute both to higher NMAT scores and higher PLE linkage. The linkage rate alone cannot be used to set a specific cut-off threshold without consideration of other factors.

**Critical caveat:** Our data contains only PLE passers. The linkage rate is affected by: (1) whether the examinee took PLE, (2) whether they passed, and (3) whether the match succeeded. We cannot distinguish these factors.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

