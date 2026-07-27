# Temporal Trends in NMAT Performance (2006–2018)

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/07_temporal_trends.py`

---

## Results

This section analyzes year-over-year trends in NMAT examinee volume, score distribution, and composition across the 13 years of data (2006–2018).

### Key Metrics

| Metric | Value |
|--------|-------|
| **Data Range** | 2006–2018 (13 years) |
| **Total Examinees (Best Record)** | 133,804 |
| **Examinees in 2006 (first year)** | 3,665 |
| **Examinees in 2018 (last year)** | 22,337 |
| **Volume Growth** | +509% |

### Yearly NMAT Score Summary

Median, Q1, Q3 of NMS_PER_num (percentile) and TotalRawScoreTRUE by year.

| Year | n | Median Pctl | Q1 Pctl | Q3 Pctl | IQR | Median Raw | Q1 Raw | Q3 Raw |
|:----:|:-:|:----------:|:-------:|:-------:|:---:|:----------:|:------:|:------:|
| 2006 | 3,665 | 53.0 | 27.0 | 77.0 | 50.0 | 131 | 108 | 154 |
| 2007 | 3,660 | 52.0 | 27.0 | 77.0 | 50.0 | 130 | 107 | 155 |
| 2008 | 4,849 | 54.0 | 28.0 | 80.0 | 52.0 | 129 | 107 | 153 |
| 2009 | 6,881 | 52.0 | 26.0 | 77.0 | 51.0 | 129 | 108 | 152 |
| 2010 | 8,008 | 57.0 | 31.0 | 81.0 | 50.0 | 135 | 113 | 159 |
| 2011 | 8,731 | 52.0 | 30.0 | 76.0 | 46.0 | 129 | 109 | 151 |
| 2012 | 9,145 | 53.0 | 26.0 | 81.0 | 55.0 | 121 | 101 | 145 |
| 2013 | 9,121 | 59.0 | 24.0 | 86.0 | 62.0 | 128 | 103 | 154 |
| 2014 | 10,441 | 57.0 | 24.0 | 83.0 | 59.0 | 120 | 98 | 142 |
| 2015 | 10,402 | 52.0 | 20.0 | 78.0 | 58.0 | 118 | 93 | 142 |
| 2016 | 12,609 | 48.0 | 19.0 | 73.0 | 54.0 | 123 | 98 | 147 |
| 2017 | 23,955 | 44.0 | 19.0 | 70.0 | 51.0 | 118 | 93 | 143 |
| 2018 | 22,337 | 43.0 | 17.0 | 70.0 | 53.0 | 111 | 91 | 132 |

### Yearly Percentile Bin Distribution

Number of examinees in each percentile bin, by year.

| Year | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 | Total |
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:----:|
| 2006 | 321 | 323 | 343 | 355 | 361 | 370 | 349 | 374 | 389 | 457 | 3642 |
| 2007 | 325 | 309 | 358 | 394 | 369 | 301 | 354 | 379 | 401 | 445 | 3635 |
| 2008 | 435 | 410 | 383 | 466 | 490 | 485 | 486 | 459 | 527 | 690 | 4831 |
| 2009 | 586 | 637 | 671 | 723 | 654 | 723 | 659 | 657 | 669 | 880 | 6859 |
| 2010 | 520 | 629 | 710 | 708 | 840 | 825 | 734 | 822 | 924 | 1275 | 7987 |
| 2011 | 566 | 755 | 806 | 963 | 1059 | 905 | 850 | 944 | 890 | 941 | 8679 |
| 2012 | 969 | 780 | 708 | 782 | 910 | 751 | 797 | 800 | 892 | 1478 | 8867 |
| 2013 | 1089 | 698 | 562 | 614 | 720 | 628 | 753 | 893 | 1012 | 1741 | 8710 |
| 2014 | 1293 | 713 | 687 | 736 | 826 | 843 | 960 | 1027 | 1150 | 1750 | 9985 |
| 2015 | 1422 | 726 | 725 | 701 | 918 | 908 | 1032 | 980 | 1027 | 1375 | 9814 |
| 2016 | 1723 | 1162 | 972 | 1040 | 1289 | 1327 | 1188 | 1232 | 1242 | 1095 | 12270 |
| 2017 | 3082 | 2766 | 2331 | 2647 | 2059 | 2410 | 2201 | 2207 | 2093 | 1823 | 23619 |
| 2018 | 3254 | 2466 | 2111 | 2336 | 2152 | 2141 | 1817 | 1824 | 1789 | 1947 | 21837 |

#### Yearly Percentile Bin Distribution (%)

Percentage of each year's examinees in each percentile bin.

| Year | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 |
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2006 | 8.8% | 8.8% | 9.4% | 9.7% | 9.8% | 10.1% | 9.5% | 10.2% | 10.6% | 12.5% |
| 2007 | 8.9% | 8.4% | 9.8% | 10.8% | 10.1% | 8.2% | 9.7% | 10.4% | 11.0% | 12.2% |
| 2008 | 9.0% | 8.5% | 7.9% | 9.6% | 10.1% | 10.0% | 10.0% | 9.5% | 10.9% | 14.2% |
| 2009 | 8.5% | 9.3% | 9.8% | 10.5% | 9.5% | 10.5% | 9.6% | 9.5% | 9.7% | 12.8% |
| 2010 | 6.5% | 7.9% | 8.9% | 8.8% | 10.5% | 10.3% | 9.2% | 10.3% | 11.5% | 15.9% |
| 2011 | 6.5% | 8.6% | 9.2% | 11.0% | 12.1% | 10.4% | 9.7% | 10.8% | 10.2% | 10.8% |
| 2012 | 10.6% | 8.5% | 7.7% | 8.6% | 10.0% | 8.2% | 8.7% | 8.7% | 9.8% | 16.2% |
| 2013 | 11.9% | 7.7% | 6.2% | 6.7% | 7.9% | 6.9% | 8.3% | 9.8% | 11.1% | 19.1% |
| 2014 | 12.4% | 6.8% | 6.6% | 7.0% | 7.9% | 8.1% | 9.2% | 9.8% | 11.0% | 16.8% |
| 2015 | 13.7% | 7.0% | 7.0% | 6.7% | 8.8% | 8.7% | 9.9% | 9.4% | 9.9% | 13.2% |
| 2016 | 13.7% | 9.2% | 7.7% | 8.2% | 10.2% | 10.5% | 9.4% | 9.8% | 9.9% | 8.7% |
| 2017 | 12.9% | 11.5% | 9.7% | 11.0% | 8.6% | 10.1% | 9.2% | 9.2% | 8.7% | 7.6% |
| 2018 | 14.6% | 11.0% | 9.5% | 10.5% | 9.6% | 9.6% | 8.1% | 8.2% | 8.0% | 8.7% |

### Yearly Foreign Examinee Counts

Foreign examinee counts and percentage of total by year.

| Year | Total | Foreign n | % Foreign | Filipino n | % Filipino |
|:----:|:----:|:---------:|:---------:|:----------:|:----------:|
| 2006 | 3,665 | 142 | 3.9% | 3,523 | 96.1% |
| 2007 | 3,660 | 320 | 8.7% | 3,340 | 91.3% |
| 2008 | 4,849 | 339 | 7.0% | 4,510 | 93.0% |
| 2009 | 6,881 | 452 | 6.6% | 6,429 | 93.4% |
| 2010 | 8,008 | 412 | 5.1% | 7,596 | 94.9% |
| 2011 | 8,731 | 468 | 5.4% | 8,263 | 94.6% |
| 2012 | 9,145 | 563 | 6.2% | 8,582 | 93.8% |
| 2013 | 9,121 | 698 | 7.7% | 8,423 | 92.3% |
| 2014 | 10,441 | 1,660 | 15.9% | 8,781 | 84.1% |
| 2015 | 10,402 | 3,040 | 29.2% | 7,362 | 70.8% |
| 2016 | 12,609 | 3,758 | 29.8% | 8,851 | 70.2% |
| 2017 | 23,955 | 7,018 | 29.3% | 16,937 | 70.7% |
| 2018 | 22,337 | 5,209 | 23.3% | 17,128 | 76.7% |

### Yearly PLE Linkage Trend

NMAT-to-PLE linkage rates by year for the observable cohort (Year <= 2014). After 2014, PLE linkage is incomplete as examinees may not have had time to take PLE.

| Year | n (Obs) | PLE Matched | Linkage Rate |
|:----:|:-------:|:-----------:|:------------:|
| 2006 | 3,665 | 2,038 | 55.61% |
| 2007 | 3,660 | 1,868 | 51.04% |
| 2008 | 4,849 | 2,514 | 51.85% |
| 2009 | 6,881 | 3,226 | 46.88% |
| 2010 | 8,008 | 3,808 | 47.55% |
| 2011 | 8,731 | 3,853 | 44.13% |
| 2012 | 9,145 | 4,066 | 44.46% |
| 2013 | 9,121 | 3,951 | 43.32% |
| 2014 | 10,441 | 3,949 | 37.82% |

*Note: PLE linkage declines over time. This may reflect: (a) increasing NMAT examinee volume without proportional increase in medical school capacity, (b) changes in admission policies, or (c) data matching limitations.*

### Interpretation

NMAT examinee volume has grown substantially over the 13-year period, from 3,665 in 2006 to 22,337 in 2018 (+509% increase).

The median NMAT percentile has decreased from 53.0 in 2006 to 43.0 in 2018.

Foreign examinees as a share of total have increased from 3.9% in 2006 to 23.3% in 2018.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

