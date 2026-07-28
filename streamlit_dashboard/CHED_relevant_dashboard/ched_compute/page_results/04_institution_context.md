# Foreign Examinee Analysis

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/04_institution_context.py`

---

## Results

This section analyzes foreign NMAT examinees using CITIZENSHIP_FINAL and FOREIGNER_STATUS columns. **Important:** All figures represent NMAT examinee counts, not enrolled students. The 10-slot SUC cap applies to enrollment, which we cannot verify from this data.

### Foreign Counts: Best-Record vs All-Records

Two perspectives are provided: **best-record** (one record per examinee, primary) and **all-records** (includes repeat takers, for volume context). Always check which denominator is used.

### Summary Metrics

| Metric | Value |
|--------|-------|
| **Total Examinees (Best Record)** | 133,804 |
| **Total Records (All Attempts)** | 178,927 |
| **** |  |
| **Foreign Examinees (Best Record) — PRIMARY** | 24,079 |
| **Foreign Records (All Attempts, includes repeat takers)** | 32,514 |
| **** |  |
| **Verified Foreigners (Best Record)** | 24,066 |
| **Likely Foreigners (Best Record)** | 13 |
| **Filipino Examinees (Best Record)** | 109,725 |
| **Foreign as % of Total (Best Record)** | 18.00% |
| **Foreign as % of Total (All Records)** | 18.17% |

### Foreign Examinees by University Type

Distribution of foreign examinees across university types (best-record basis).

| UNI_TYPE | Foreign n (Best Record) | % of Foreign | % of UNI_TYPE Total |
|:---------|:-----------------------:|:------------:|:-------------------:|
| Public | 4,514 | 18.75% | 16.34% |
| Private | 18,478 | 76.74% | 17.96% |
| Foreign | 744 | 3.09% | 39.28% |
| Not Specified | 343 | 1.42% | 24.59% |

### Foreign Examinees by Year

Yearly foreign examinee counts and trends (best-record basis).

| Year | Foreign n (Best Record) | % of Year Total | Total Examinees |
|:----:|:-----------------------:|:---------------:|:---------------:|
| 2006 | 142 | 3.87% | 3,665 |
| 2007 | 320 | 8.74% | 3,660 |
| 2008 | 339 | 6.99% | 4,849 |
| 2009 | 452 | 6.57% | 6,881 |
| 2010 | 412 | 5.14% | 8,008 |
| 2011 | 468 | 5.36% | 8,731 |
| 2012 | 563 | 6.16% | 9,145 |
| 2013 | 698 | 7.65% | 9,121 |
| 2014 | 1,660 | 15.90% | 10,441 |
| 2015 | 3,040 | 29.23% | 10,402 |
| 2016 | 3,758 | 29.80% | 12,609 |
| 2017 | 7,018 | 29.30% | 23,955 |
| 2018 | 5,209 | 23.32% | 22,337 |

### Foreign Examinees at SUCs (by Year)

This table shows foreign examinee counts at Public (SUC) institutions by year. **Note:** These are examinee counts (best-record), not enrollment. Actual enrollment figures may differ.

| SUC | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | Total |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| University Of Northern Philippines - ... | 0 | 0 | 0 | 0 | 13 | 0 | 1 | 1 | 17 | 178 | 191 | 281 | 87 | 769 |
| Cagayan State University - Tuguegarao... | 0 | 0 | 0 | 0 | 6 | 11 | 3 | 7 | 13 | 67 | 121 | 150 | 55 | 433 |
| University Of The Philippines - Diliman | 0 | 1 | 1 | 0 | 1 | 0 | 14 | 17 | 37 | 54 | 54 | 120 | 72 | 371 |
| University Of The Philippines - Manila | 0 | 0 | 0 | 1 | 3 | 1 | 11 | 23 | 43 | 56 | 60 | 79 | 82 | 359 |
| University Of The Philippines - Los B... | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 10 | 23 | 32 | 40 | 78 | 39 | 225 |
| West Visayas State University - Main | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 7 | 18 | 28 | 42 | 52 | 44 | 197 |
| Mindanao State University - Iligan In... | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 10 | 15 | 41 | 30 | 59 | 37 | 196 |
| Not Specified/Unlisted | 10 | 21 | 20 | 57 | 50 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 158 |
| Western Mindanao State University | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 6 | 14 | 23 | 22 | 44 | 36 | 147 |
| University Of The Philippines - Visayas | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 14 | 25 | 25 | 40 | 28 | 138 |
| Mindanao State University - Marawi | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 8 | 15 | 20 | 21 | 33 | 31 | 135 |
| Pamantasan Ng Lungsod Ng Maynila | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 8 | 17 | 12 | 29 | 38 | 26 | 135 |
| University Of The Philippines - Baguio | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 8 | 7 | 18 | 21 | 40 | 23 | 119 |
| Bicol University - Main | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 12 | 15 | 10 | 33 | 44 | 118 |
| Central Mindanao University | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 5 | 9 | 14 | 19 | 22 | 73 |
| Palawan State University | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 17 | 7 | 20 | 15 | 64 |
| Polytechnic University Of The Philipp... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 9 | 10 | 21 | 18 | 62 |
| Cagayan State University - Andrews | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 10 | 6 | 14 | 25 | 57 |
| Mariano Marcos State University - Main | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 13 | 5 | 12 | 16 | 52 |
| University Of The Philippines - Mindanao | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 5 | 12 | 3 | 14 | 11 | 49 |
| University Of Northern Philippines, C... | 0 | 0 | 0 | 47 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 47 |
| University Of The Philippines - Colle... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 4 | 2 | 8 | 13 | 9 | 39 |
| Bulacan State University - Main | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 7 | 5 | 6 | 15 | 38 |
| Mindanao State University - General S... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 4 | 2 | 16 | 7 | 33 |
| Cagayan State University - Tuguegarao | 0 | 0 | 0 | 15 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 |
| University Of The Philippines - Manil... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 15 | 13 | 31 |
| Cebu Normal University | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 1 | 2 | 1 | 10 | 8 | 4 | 30 |
| University Of Eastern Philippines | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 3 | 3 | 2 | 13 | 4 | 27 |
| University Of The Philippines In The ... | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 6 | 4 | 2 | 4 | 7 | 27 |
| Central Luzon State University | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 2 | 4 | 10 | 6 | 26 |

*Only top 30 SUCs by total foreign examinees shown.*

### Foreign Examinees by Nationality

Distribution of foreign examinees by citizenship (all-records basis, includes repeat takers).

| Rank | Nationality | n (All Records) | % of Foreign | Median |
|:----:|:------------|:---------------:|:------------:|:-----------------:|
| 1 | India | 26,491 | 110.02% | 14.0 |
| 2 | Nepal | 1,158 | 4.81% | 23.0 |
| 3 | Thailand | 1,062 | 4.41% | 17.5 |
| 4 | United States | 839 | 3.48% | 72.0 |
| 5 | Nigeria | 639 | 2.65% | 23.0 |
| 6 | Sri Lanka | 262 | 1.09% | 53.0 |
| 7 | Korea (South) | 224 | 0.93% | 57.0 |
| 8 | Iran | 163 | 0.68% | 14.0 |
| 9 | Foreign | 156 | 0.65% | 37.0 |
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
| Foreign | 156 | 37.0 | 6.0 | 64.0 | 43.59% |
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
| Filipino | 59,447 | 29,147 | 49.03% |
| Foreign | 5,054 | 126 | 2.49% |

### Key Insight

Of 133,804 NMAT examinees (best-record), 24,079 (18.0%) are foreign nationals based on CITIZENSHIP_FINAL. Across all records (including repeat takers), there are 32,514 foreign test records.

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

