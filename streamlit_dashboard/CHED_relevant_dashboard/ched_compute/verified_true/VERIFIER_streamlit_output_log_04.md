# Verifier: Tab 4 — Institution and Foreign Context

**Date:** July 28, 2026
**Data:** `NMAT_Exodus.parquet` (178,927 rows, 54 cols)
**Best-record examinees:** 133,804

---

## 1. Score Summary by University Type

Dashboard logic: best-record subset, UNI_TYPE in [Public, Private, Foreign].
Groups by UNI_TYPE; median, Q25, Q75 on NMS_PER_num; median raw + GPS.

uni_subset n: 132,409

| UNI_TYPE | N (best) | Median %ile | Q25 %ile | Q75 %ile | Median Raw | Median GPS |
|:---------|:--------:|:-----------:|:--------:|:--------:|:----------:|:----------:|
| Foreign | 1,894 | 51.0 | 20.0 | 79.0 | 124.0 | 504.0 |
| Private | 102,888 | 48.0 | 21.0 | 74.0 | 120.0 | 497.0 |
| Public | 27,627 | 56.0 | 26.0 | 83.0 | 127.0 | 517.0 |

> **Cross-check note:** Expected values doc shows bin-rank medians for all UNI_TYPE values. Dashboard uses uni_subset (Public/Private/Foreign only, excluding Not Specified).

## 2. Bin Distribution by UNI_TYPE (Row %)

Dashboard uses `make_bin_pct(uni_subset, 'UNI_TYPE')`: cross-tab UNI_TYPE vs PercentileBin, reindexed to B1–B10, row-wise percentages.

**Row % (each UNI_TYPE row sums to ~100%):**

| UNI_TYPE | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 |
|:---------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Foreign | 14.1 | 9.4 | 7.5 | 9.4 | 7.9 | 8.8 | 8.6 | 9.6 | 10.6 | 14.1 |
| Private | 12.1 | 9.8 | 9.0 | 9.9 | 9.9 | 9.9 | 9.4 | 9.7 | 9.7 | 10.6 |
| Public | 10.9 | 8.3 | 7.6 | 8.3 | 8.7 | 8.9 | 9.1 | 9.6 | 11.0 | 17.7 |

**Raw counts:**

| UNI_TYPE | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 |
|:---------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Foreign | 262 | 175 | 140 | 176 | 147 | 164 | 160 | 178 | 197 | 263 |
| Private | 12,208 | 9,806 | 9,066 | 9,958 | 10,007 | 9,934 | 9,458 | 9,716 | 9,730 | 10,701 |
| Public | 2,948 | 2,230 | 2,050 | 2,227 | 2,339 | 2,406 | 2,444 | 2,573 | 2,957 | 4,763 |

## 3. Top-Bin Share (B8–B10) by UNI_TYPE

Dashboard sums B8+B9+B10 row% from bin distribution, sorts ascending.

| UNI_TYPE | B8 % | B9 % | B10 % | B8–B10 Total % |
|:---------|:----:|:----:|:-----:|:--------------:|
| Private | 9.7 | 9.7 | 10.6 | 30.0 |
| Foreign | 9.6 | 10.6 | 14.1 | 34.3 |
| Public | 9.6 | 11.0 | 17.7 | 38.2 |

**With examinee counts (matching dashboard table):**

| UNI_TYPE | Total examinees | B8–B10 % |
|:---------|:---------------:|:--------:|
| Private | 102,888 | 30.0 |
| Foreign | 1,894 | 34.3 |
| Public | 27,627 | 38.2 |

## 4. Foreign Examinee Counts (df_all — all records)

Dashboard uses **all records (df_all)** for citizenship context. FOREIGNER_STATUS == 'Verified Foreigner' defines foreign.

> **Note:** The expected values doc (04_institution_context.md) uses FOREIGNER_STATUS in ['Verified Foreigner', 'Likely Foreigner'] for the nationality distribution table (26,491 India, 32,514 total foreign records), while the dashboard TAB 4 uses only FOREIGNER_STATUS == 'Verified Foreigner' (26,490 India, 32,501 total foreign records). This means the '% of Foreign' columns will differ between the two. The 13 'Likely Foreigner' records are dropped from dashboard TAB 4's nationality chart.


### Summary Metrics (All Records)

| Metric | Value |
|--------|-------|
| Verified Foreign examinees (all records) | 32,501 |
| Likely Foreign examinees (all records) | 13 |
| Filipino examinees (all records) | 146,413 |
| Distinct foreign nationalities | 90 |

### Cross-Check: Best-Record Foreign Counts

Expected values doc (04_institution_context.md) uses best-record for primary counts, combining Verified + Likely Foreigner.

| Metric | Value |
|--------|-------|
| Total examinees (best record) | 133,804 |
| Foreign examinees (best, Verified+Likely) | 24,079 |
|   Verified Foreigners (best) | 24,066 |
|   Likely Foreigners (best) | 13 |
| Filipino examinees (best) | 109,725 |
| Foreign as % of Total (best) | 18.00% |

### Foreign Examinees by UNI_TYPE (Best Record)

| UNI_TYPE | Foreign n (Best) | % of Foreign | % of UNI_TYPE Total |
|:---------|:----------------:|:------------:|:-------------------:|
| Public | 4,514 | 18.75% | 16.34% |
| Private | 18,478 | 76.74% | 17.96% |
| Foreign | 744 | 3.09% | 39.28% |
| Not Specified | 343 | 1.42% | 24.59% |

## 5. Top 10 Nationalities (All Records, Verified Foreign)

Dashboard: `foreign_all['CITIZENSHIP_FINAL'].value_counts().head(10)`

| Rank | Nationality | Count | % of Foreign |
|:----:|:------------|:-----:|:------------:|
| 1 | India | 26,490 | 81.51% |
| 2 | Nepal | 1,158 | 3.56% |
| 3 | Thailand | 1,062 | 3.27% |
| 4 | United States | 839 | 2.58% |
| 5 | Nigeria | 639 | 1.97% |
| 6 | Sri Lanka | 262 | 0.81% |
| 7 | Korea (South) | 224 | 0.69% |
| 8 | Iran | 162 | 0.50% |
| 9 | Foreign | 156 | 0.48% |
| 10 | Indonesia | 124 | 0.38% |

### Extended: Top 20 Nationalities with Median NMS (All Records)

| Rank | Nationality | n (All Records) | % of Foreign | Median | Q1 | Q3 | % Below B4+ |
|:----:|:------------|:---------------:|:------------:|:-----:|:--:|:--:|:-----------:|
| 1 | India | 26,490 | 81.51% | 14.0 | 3.0 | 35.0 | 70.33% |
| 2 | Nepal | 1,158 | 3.56% | 23.0 | 8.0 | 45.0 | 57.34% |
| 3 | Thailand | 1,062 | 3.27% | 17.5 | 6.0 | 38.0 | 66.38% |
| 4 | United States | 839 | 2.58% | 72.0 | 42.0 | 89.0 | 19.67% |
| 5 | Nigeria | 639 | 1.97% | 23.0 | 8.0 | 45.0 | 59.00% |
| 6 | Sri Lanka | 262 | 0.81% | 53.0 | 30.0 | 72.0 | 24.43% |
| 7 | Korea (South) | 224 | 0.69% | 57.0 | 32.0 | 80.0 | 23.21% |
| 8 | Iran | 162 | 0.50% | 14.0 | 2.2 | 49.0 | 62.96% |
| 9 | Foreign | 156 | 0.48% | 37.0 | 6.0 | 64.0 | 43.59% |
| 10 | Indonesia | 124 | 0.38% | 32.5 | 12.8 | 67.0 | 45.16% |
| 11 | Solomon Islands | 116 | 0.36% | 9.0 | 2.0 | 27.0 | 79.31% |
| 12 | Maldives | 113 | 0.35% | 57.0 | 37.0 | 73.0 | 17.70% |
| 13 | Taiwan | 104 | 0.32% | 33.5 | 9.8 | 74.0 | 47.12% |
| 14 | Malaysia | 101 | 0.31% | 24.0 | 5.0 | 45.0 | 59.41% |
| 15 | Japan | 97 | 0.30% | 41.0 | 24.0 | 72.0 | 34.02% |
| 16 | Canada | 83 | 0.26% | 65.0 | 29.5 | 91.0 | 28.92% |
| 17 | Somalia | 75 | 0.23% | 2.0 | 1.0 | 5.5 | 96.00% |
| 18 | China | 70 | 0.22% | 56.0 | 20.0 | 86.0 | 35.71% |
| 19 | Ghana | 70 | 0.22% | 28.5 | 15.0 | 54.0 | 51.43% |
| 20 | Pakistan | 48 | 0.15% | 9.5 | 2.0 | 40.8 | 70.83% |

## 6. Foreign Examinees by Year (Best Record)

| Year | Foreign n | % of Year | Total Examinees |
|:----:|:---------:|:---------:|:---------------:|
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

## 7. Foreign vs Filipino: NMAT-to-PLE Linkage (Best Record, Pre-2015)

| Group | n (Pre-2015, Best Record) | PLE Matched | NMAT-to-PLE Linkage Rate |
|:------|:------------------------:|:-----------:|:------------------------:|
| Filipino | 59,447 | 29,147 | 49.03% |
| Foreign | 5,054 | 126 | 2.49% |

## 8. Key Insight Cross-Check

- India examinees (all records): 26,490
- India examinees (best record): 19,092
- India % of foreign (best): 79.3%
- India median NMS (all records): 14.0
- India median NMS (best record): 18.0
- India % below B4+ (all records): 70.3%

## 9. Verification Summary

### Key Metrics vs Expected

| Metric | Expected | Actual | Match |
|--------|:--------:|:------:|:-----:|
| total_examinees_best | 133,804 | 133,804 | PASS |
| total_records_all | 178,927 | 178,927 | PASS |
| foreign_best_combined | 24,079 | 24,079 | PASS |
| foreign_all_records | 32,514 | 32,514 | PASS |
| verified_foreigners_best | 24,066 | 24,066 | PASS |
| likely_foreigners_best | 13 | 13 | PASS |
| filipinos_best | 109,725 | 109,725 | PASS |
| pct_foreign_best | 18.00 | 18.00 | PASS |
| pct_foreign_all | 18.17 | 18.17 | PASS |

**Overall: ALL METRICS MATCH**

---
