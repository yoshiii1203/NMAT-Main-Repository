# Foreign Examinee Analysis

**Date:** July 31, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 53 columns)
**Script:** `ched_compute/04_institution_context.py`

---

## Results

This section analyzes foreign NMAT examinees using CITIZENSHIP_FINAL and FOREIGNER_STATUS columns. **Important:** All figures represent NMAT examinee counts, not enrolled students. The 10-slot SUC cap applies to enrollment, which we cannot verify from this data.

### Foreign Counts: Best-Record vs All-Records

Two perspectives are provided: **best-record** (one record per examinee, primary) and **all-records** (includes repeat takers, for volume context). Always check which denominator is used.

### Summary Metrics

| Metric | Value |
|--------|-------|
| **Total Examinees (Best Record)** | 134,869 |
| **Total Records (All Attempts)** | 178,927 |
| **** |  |
| **Foreign Examinees (Best Record) — PRIMARY** | 24,082 |
| **Foreign Records (All Attempts, includes repeat takers)** | 32,514 |
| **** |  |
| **Verified Foreigners (Best Record)** | 24,069 |
| **Likely Foreigners (Best Record)** | 13 |
| **Filipino Examinees (Best Record)** | 110,787 |
| **Foreign as % of Total (Best Record)** | 17.86% |
| **Foreign as % of Total (All Records)** | 18.17% |

### Foreign Examinees by University Type

Distribution of foreign examinees across university types (best-record basis).

| UNDERGRAD_UNI_TYPE | Foreign n (Best Record) | % of Foreign | % of UNDERGRAD_UNI_TYPE Total |
|:---------|:-----------------------:|:------------:|:-------------------:|
| Public | 4,516 | 18.75% | 16.18% |
| Private | 18,479 | 76.73% | 17.83% |
| Foreign | 744 | 3.09% | 39.32% |
| Not Specified | 343 | 1.42% | 24.64% |

### Foreign Examinees by Year

Yearly foreign examinee counts and trends (best-record basis).

| Year | Foreign n (Best Record) | % of Year Total | Total Examinees |
|:----:|:-----------------------:|:---------------:|:---------------:|
| 2006 | 143 | 3.87% | 3,698 |
| 2007 | 321 | 8.70% | 3,690 |
| 2008 | 339 | 6.83% | 4,965 |
| 2009 | 452 | 6.06% | 7,461 |
| 2010 | 413 | 4.83% | 8,551 |
| 2011 | 469 | 5.39% | 8,701 |
| 2012 | 563 | 6.18% | 9,113 |
| 2013 | 698 | 7.63% | 9,148 |
| 2014 | 1,661 | 15.89% | 10,455 |
| 2015 | 3,038 | 29.42% | 10,326 |
| 2016 | 3,757 | 30.10% | 12,480 |
| 2017 | 7,018 | 29.31% | 23,948 |
| 2018 | 5,210 | 23.33% | 22,333 |

### Foreign Examinees at SUCs (by Year)

This table shows foreign examinee counts at Public (SUC) institutions by year. **Note:** These are examinee counts (best-record), not enrollment. Actual enrollment figures may differ.

| SUC | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | Total |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| UNIVERSITY OF NORTHERN PHILIPPINES - ... | 0 | 0 | 0 | 0 | 13 | 0 | 1 | 1 | 17 | 178 | 191 | 281 | 88 | 770 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO... | 0 | 0 | 0 | 0 | 6 | 11 | 3 | 7 | 13 | 67 | 121 | 150 | 55 | 433 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN | 0 | 1 | 1 | 0 | 1 | 0 | 14 | 17 | 37 | 54 | 54 | 120 | 72 | 371 |
| UNIVERSITY OF THE PHILIPPINES - MANILA | 0 | 0 | 0 | 1 | 3 | 2 | 11 | 23 | 43 | 56 | 60 | 79 | 82 | 360 |
| UNIVERSITY OF THE PHILIPPINES - LOS B... | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 10 | 23 | 32 | 40 | 78 | 39 | 225 |
| WEST VISAYAS STATE UNIVERSITY - MAIN | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 7 | 18 | 28 | 42 | 52 | 44 | 197 |
| MINDANAO STATE UNIVERSITY - ILIGAN IN... | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 10 | 15 | 41 | 30 | 59 | 37 | 196 |
| NOT SPECIFIED/UNLISTED | 11 | 21 | 20 | 57 | 50 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 159 |
| WESTERN MINDANAO STATE UNIVERSITY | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 6 | 14 | 23 | 22 | 44 | 36 | 147 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 14 | 25 | 25 | 40 | 28 | 138 |
| PAMANTASAN NG LUNGSOD NG MAYNILA | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 8 | 17 | 12 | 29 | 38 | 26 | 135 |
| MINDANAO STATE UNIVERSITY - MARAWI | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 8 | 15 | 20 | 21 | 33 | 31 | 135 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 8 | 7 | 18 | 21 | 40 | 23 | 119 |
| BICOL UNIVERSITY - MAIN | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 12 | 15 | 10 | 33 | 44 | 118 |
| CENTRAL MINDANAO UNIVERSITY | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 5 | 9 | 14 | 19 | 22 | 73 |
| PALAWAN STATE UNIVERSITY | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 17 | 7 | 20 | 15 | 64 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPP... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 9 | 10 | 21 | 18 | 62 |
| CAGAYAN STATE UNIVERSITY - ANDREWS | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 10 | 6 | 14 | 25 | 57 |
| MARIANO MARCOS STATE UNIVERSITY - MAIN | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 13 | 5 | 12 | 16 | 52 |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 5 | 12 | 3 | 14 | 11 | 49 |
| UNIVERSITY OF NORTHERN PHILIPPINES CA... | 0 | 0 | 0 | 47 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 47 |
| UNIVERSITY OF THE PHILIPPINES - COLLE... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 4 | 2 | 8 | 13 | 9 | 39 |
| BULACAN STATE UNIVERSITY - MAIN | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 7 | 5 | 6 | 15 | 38 |
| MINDANAO STATE UNIVERSITY - GENERAL S... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 4 | 2 | 16 | 7 | 33 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO | 0 | 0 | 0 | 15 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 |
| UNIVERSITY OF THE PHILIPPINES - MANIL... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 15 | 13 | 31 |
| CEBU NORMAL UNIVERSITY | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 1 | 2 | 1 | 10 | 8 | 4 | 30 |
| UNIVERSITY OF THE PHILIPPINES IN THE ... | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 6 | 4 | 2 | 4 | 7 | 27 |
| UNIVERSITY OF EASTERN PHILIPPINES | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 3 | 3 | 2 | 13 | 4 | 27 |
| CENTRAL LUZON STATE UNIVERSITY | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 2 | 4 | 10 | 6 | 26 |

*Only top 30 SUCs by total foreign examinees shown.*

### Foreign Examinees by Nationality

Distribution of foreign examinees by citizenship (all-records basis, includes repeat takers).

| Rank | Nationality | n (All Records) | % of Foreign | Median |
|:----:|:------------|:---------------:|:------------:|:-----------------:|
| 1 | India | 26,491 | 110.00% | 14.0 |
| 2 | Nepal | 1,158 | 4.81% | 23.0 |
| 3 | Thailand | 1,062 | 4.41% | 17.5 |
| 4 | United States | 839 | 3.48% | 72.0 |
| 5 | Nigeria | 639 | 2.65% | 23.0 |
| 6 | Sri Lanka | 262 | 1.09% | 53.0 |
| 7 | Korea (South) | 224 | 0.93% | 57.0 |
| 8 | Iran | 163 | 0.68% | 14.0 |
| 9 | Foreign (unspecified) | 156 | 0.65% | 37.0 |
| 10 | Indonesia | 125 | 0.52% | 32.0 |
| 11 | Solomon Islands | 116 | 0.48% | 9.0 |
| 12 | Maldives | 113 | 0.47% | 57.0 |
| 13 | Malaysia | 108 | 0.45% | 24.0 |
| 14 | Taiwan | 104 | 0.43% | 33.5 |
| 15 | Japan | 97 | 0.40% | 41.0 |
| 16 | Canada | 83 | 0.34% | 65.0 |
| 17 | Somalia | 75 | 0.31% | 2.0 |
| 18 | China | 71 | 0.29% | 57.0 |
| 19 | Ghana | 70 | 0.29% | 28.5 |
| 20 | Pakistan | 49 | 0.20% | 11.0 |

### NMAT Performance by Nationality

Median NMAT score for top nationalities, showing score distribution (all-records basis).

| Nationality | n (All Records) | Median | Q1 | Q3 | % Below B4+ |
|:------------|:---------------:|:----------:|:-------:|:-------:|:-----------------:|
| India | 26,491 | 14.0 | 3.0 | 35.0 | 70.33% |
| Nepal | 1,158 | 23.0 | 8.0 | 45.0 | 57.34% |
| Thailand | 1,062 | 17.5 | 6.0 | 38.0 | 66.38% |
| United States | 839 | 72.0 | 42.0 | 89.0 | 19.67% |
| Nigeria | 639 | 23.0 | 8.0 | 45.0 | 59.00% |
| Sri Lanka | 262 | 53.0 | 30.0 | 72.0 | 24.43% |
| Korea (South) | 224 | 57.0 | 32.0 | 80.0 | 23.21% |
| Iran | 163 | 14.0 | 2.5 | 49.0 | 62.58% |
| Foreign (unspecified) | 156 | 37.0 | 6.0 | 64.0 | 43.59% |
| Indonesia | 125 | 32.0 | 12.0 | 67.0 | 45.60% |
| Solomon Islands | 116 | 9.0 | 2.0 | 27.0 | 79.31% |
| Maldives | 113 | 57.0 | 37.0 | 73.0 | 17.70% |
| Malaysia | 108 | 24.0 | 5.8 | 43.5 | 59.26% |
| Taiwan | 104 | 33.5 | 9.8 | 74.0 | 47.12% |
| Japan | 97 | 41.0 | 24.0 | 72.0 | 34.02% |
| Canada | 83 | 65.0 | 29.5 | 91.0 | 28.92% |
| Somalia | 75 | 2.0 | 1.0 | 5.5 | 96.00% |
| China | 71 | 57.0 | 20.0 | 86.0 | 35.21% |
| Ghana | 70 | 28.5 | 15.0 | 54.0 | 51.43% |
| Pakistan | 49 | 11.0 | 2.0 | 46.0 | 69.39% |

### Foreign vs Filipino: NMAT-to-PLE Linkage

NMAT-to-PLE linkage rates for foreign vs Filipino examinees (pre-2015 cohort, best-record basis).

| Group | n (Pre-2015, Best Record) | PLE Matched | NMAT-to-PLE Linkage Rate |
|:------|:------------------------:|:-----------:|:------------------------:|
| Filipino | 64,133 | 31,447 | 49.03% |
| Foreign | 5,370 | 134 | 2.50% |

### Key Insight

Of 134,869 NMAT examinees (best-record), 24,082 (17.9%) are foreign nationals based on CITIZENSHIP_FINAL. Across all records (including repeat takers), there are 32,514 foreign test records.

The largest nationality group is from India (26,491, 110.0% of foreign examinees, best-record basis).

Indian-origin examinees have a median score of 14.0 (B2 range), and 70.3% fall below the B4+ threshold. This has significant implications for the proposed B4+/B5+ cut-off policy.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

