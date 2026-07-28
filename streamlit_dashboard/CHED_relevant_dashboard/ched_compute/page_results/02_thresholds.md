# B4+ vs B5+ Threshold Analysis

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/02_thresholds.py`

---

## Results

This section models the impact of two proposed NMAT cut-off thresholds: B4+ (at or above Bin 4) and B5+ (at or above Bin 5). For each threshold, we compute the number and proportion of examinees who qualify, broken down by university type, year, and PLE linkage rate.

### Key Metrics

| Metric | Value |
|--------|-------|
| **Total Examinees (Best Record)** | 133,804 |
| **At or Above B4 (Bin 4+)** | 91,409 |
| **At or Above B5 (Bin 5+)** | 78,944 |
| **Difference (B4+ minus B5+)** | 12,465 |
| **B4+ PLE Linkage Rate (Pre-2015)** | 56.45% (26,311 / 46,609) |
| **B5+ PLE Linkage Rate (Pre-2015)** | 61.17% (24,999 / 40,868) |
| **Linkage Rate Gap (B5+ minus B4+)** | 4.72 pp |

### Threshold Impact by University Type

Table shows the number and percent of examinees qualifying at each threshold, by university type.

| UNI_TYPE | n (Best) | B4+ (Bin 4+) | % B4+ | B5+ (Bin 5+) | % B5+ | B4 Only (Bin 4) |
|:---------|:--------:|:-----------:|:-----:|:-----------:|:-----:|:------------------:|
| Public | 27,627 | 19,709 | 71.34% | 17,482 | 63.28% | 2,227 |
| Private | 102,888 | 69,504 | 67.55% | 59,546 | 57.87% | 9,958 |
| Foreign | 1,894 | 1,285 | 67.85% | 1,109 | 58.55% | 176 |
| Not Specified | 1,395 | 911 | 65.30% | 807 | 57.85% | 104 |

### Threshold Impact by Year

Table shows year-by-year qualifying counts at each threshold.

| Year | n (Best) | B4+ (Bin 4+) | % B4+ | B5+ (Bin 5+) | % B5+ | B4 Only |
|:----:|:--------:|:-----------:|:-----:|:-----------:|:-----:|:--------:|
| 2006 | 3,665 | 2,655 | 72.44% | 2,300 | 62.76% | 355 |
| 2007 | 3,660 | 2,643 | 72.21% | 2,249 | 61.45% | 394 |
| 2008 | 4,849 | 3,603 | 74.30% | 3,137 | 64.69% | 466 |
| 2009 | 6,881 | 4,965 | 72.16% | 4,242 | 61.65% | 723 |
| 2010 | 8,008 | 6,128 | 76.52% | 5,420 | 67.68% | 708 |
| 2011 | 8,731 | 6,552 | 75.04% | 5,589 | 64.01% | 963 |
| 2012 | 9,145 | 6,410 | 70.09% | 5,628 | 61.54% | 782 |
| 2013 | 9,121 | 6,361 | 69.74% | 5,747 | 63.01% | 614 |
| 2014 | 10,441 | 7,292 | 69.84% | 6,556 | 62.79% | 736 |
| 2015 | 10,402 | 6,941 | 66.73% | 6,240 | 59.99% | 701 |
| 2016 | 12,609 | 8,413 | 66.72% | 7,373 | 58.47% | 1,040 |
| 2017 | 23,955 | 15,440 | 64.45% | 12,793 | 53.40% | 2,647 |
| 2018 | 22,337 | 14,006 | 62.70% | 11,670 | 52.25% | 2,336 |

### PLE Linkage Rate by Threshold and University Type

For each university type and threshold, the NMAT-to-PLE linkage rate among the pre-2015 cohort.

| UNI_TYPE | B4+ Linkage | B5+ Linkage | Gap (pp) |
|:---------|:-------------------:|:-------------------:|:--------:|
| Public | 59.52% (6,294/10,575) | 63.38% (6,135/9,680) | 3.86 |
| Private | 56.22% (19,500/34,688) | 61.23% (18,361/29,985) | 5.02 |
| Foreign | 28.14% (222/789) | 30.18% (214/709) | 2.05 |
| Not Specified | 52.96% (295/557) | 58.50% (289/494) | 5.54 |

### Linkage Rate by Individual Score Bin

Shows how the linkage rate changes across each score bin, highlighting the critical B4→B5 transition.

| Score Bin | Score Range | n (Pre-2015) | PLE Matched | Linkage Rate |
|:--------:|:-----------:|:------------:|:-----------:|:------------:|
| B1 | 0–9 | 6,104 | 505 | 8.27% |
| B2 | 10–19 | 5,254 | 830 | 15.80% |
| B3 | 20–29 | 5,228 | 997 | 19.07% |
| B4 | 30–39 | 5,741 | 1,312 | 22.85% |
| B5 | 40–49 | 6,229 | 2,882 | 46.27% |
| B6 | 50–59 | 5,831 | 2,992 | 51.31% |
| B7 | 60–69 | 5,942 | 3,359 | 56.53% |
| B8 | 70–79 | 6,355 | 3,819 | 60.09% |
| B9 | 80–89 | 6,854 | 4,595 | 67.04% |
| B10 | 90–100 | 9,657 | 7,352 | 76.13% |

The sharpest bin-to-bin increase occurs between B4 (30th–39th) and B5 (40th–49th). This is the empirical basis for the tiered cut-off proposal: the B5+ threshold selects a pool with meaningfully higher PLE linkage outcomes.

### Interpretation

Among 133,804 NMAT examinees (best record):
- **91,409 (68.3%)** qualify at the B4+ threshold (Bin 4 and above)
- **78,944 (59.0%)** qualify at the B5+ threshold (Bin 5 and above)
- **12,465 examinees (9.3%)** fall in the B4 band (Bin 4 only) — 
  the marginal pool affected by choosing the higher threshold

The PLE linkage rate at B4+ is 56.45% vs 61.17% at B5+ — a difference of 4.72 percentage points. This supports the tiered approach: the B5+ threshold meaningfully differentiates applicant pools on PLE linkage outcomes.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

