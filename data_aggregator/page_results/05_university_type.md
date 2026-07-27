# Page 5: University Type Analysis (Page 05)

**Generated:** 2026-07-28 01:17

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `uni`

**Filters:** None (full unfiltered dataset)

---

**Subset:** besttrend filtered to UNI_TYPE in [Public, Private, Foreign]

**Total records:** 129,383

---

## 1. UNI_TYPE Distribution by UNI_LOCATION

### 1a. Institution type by location mix

**Table 05-1. Institution type by location mix**

| UNI_TYPE   | UNI_LOCATION   |   Count |   Percent of Total |
|:-----------|:---------------|--------:|-------------------:|
| Foreign    | International  |    1862 |               1.44 |
| Private    | Local          |  100584 |              77.74 |
| Public     | Local          |   26937 |              20.82 |

### 1b. Count matrix with margins

**Table 05-2. UNI_TYPE x UNI_LOCATION count matrix (with totals)**

| UNI_TYPE   |   International |   Local |    All |
|:-----------|----------------:|--------:|-------:|
| Foreign    |            1862 |       0 |   1862 |
| Private    |               0 |  100584 | 100584 |
| Public     |               0 |   26937 |  26937 |
| All        |            1862 |  127521 | 129383 |

### 1c. Row percentages (within UNI_TYPE)

**Table 05-3. Row percentages: within UNI_TYPE**

| UNI_TYPE   |   International |   Local |
|:-----------|----------------:|--------:|
| Foreign    |             100 |       0 |
| Private    |               0 |     100 |
| Public     |               0 |     100 |

### 1d. Column percentages (within UNI_LOCATION)

**Table 05-4. Column percentages: within UNI_LOCATION**

| UNI_TYPE   |   International |   Local |
|:-----------|----------------:|--------:|
| Foreign    |             100 |       0 |
| Private    |               0 |   78.88 |
| Public     |               0 |   21.12 |

---

## 2. Bin Distribution by UNI_TYPE

### 2a. Bin counts by UNI_TYPE

**Table 05-5. Bin counts by university type**

| UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |    B5 |   B6 |   B7 |   B8 |   B9 |   B10 |   Total |
|:-----------|------:|-----:|-----:|-----:|------:|-----:|-----:|-----:|-----:|------:|--------:|
| Foreign    |   262 |  175 |  140 |  176 |   147 |  164 |  160 |  178 |  197 |   263 |    1862 |
| Private    | 12208 | 9806 | 9066 | 9958 | 10007 | 9934 | 9458 | 9716 | 9730 | 10701 |  100584 |
| Public     |  2948 | 2230 | 2050 | 2227 |  2339 | 2406 | 2444 | 2573 | 2957 |  4763 |   26937 |

### 2b. Bin percentages by UNI_TYPE

**Table 05-6. Row percentages (within UNI_TYPE) across percentile bins**

| UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:-----------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign    | 14.07 |  9.4 | 7.52 | 9.45 | 7.89 | 8.81 | 8.59 | 9.56 | 10.58 | 14.12 |
| Private    | 12.14 | 9.75 | 9.01 |  9.9 | 9.95 | 9.88 |  9.4 | 9.66 |  9.67 | 10.64 |
| Public     | 10.94 | 8.28 | 7.61 | 8.27 | 8.68 | 8.93 | 9.07 | 9.55 | 10.98 | 17.68 |

---

## 3. Top Bin Share (B8-B10) by UNI_TYPE

**Table 05-7. Top bin (B8-B10) share by university type**

| UNI_TYPE   |   Total N |   Top Bin (B8-B10) Count |   Top Bin Share (%) |
|:-----------|----------:|-------------------------:|--------------------:|
| Foreign    |      1862 |                      638 |               34.26 |
| Private    |    100584 |                    30147 |               29.97 |
| Public     |     26937 |                    10293 |               38.21 |

### 3b. Top bin share by UNI_TYPE x UNI_LOCATION

**Table 05-8. Top bin (B8-B10) share by institution type x location**

| UNI_TYPE   | UNI_LOCATION   |   Total N |   Top Bin Count |   Top Bin Share (%) |
|:-----------|:---------------|----------:|----------------:|--------------------:|
| Foreign    | International  |      1862 |             638 |               34.26 |
| Private    | Local          |    100584 |           30147 |               29.97 |
| Public     | Local          |     26937 |           10293 |               38.21 |

---

## 4. Foreign Examinee Summary

### 4a. Foreign examinee overview (UNI_TYPE = Foreign)

- **Foreign examinees (besttrend):** 1,862
- **Percent of total (uni subset):** 1.44%
- **Median percentile:** 52.0
- **Top bin share (B8-B10):** 34.26%

### 4b. Foreign examinees by FOREIGNER_STATUS

**Table 05-9. Foreign examinee summary by FOREIGNER_STATUS**

| FOREIGNER_STATUS   |    N |   Median Percentile |   Median Raw Total |   Top Bin (B8-B10) Rate |
|:-------------------|-----:|--------------------:|-------------------:|------------------------:|
| Filipino           | 1136 |                  60 |                130 |                   40.49 |
| Likely Foreigner   |   13 |                  27 |                103 |                   30.77 |
| Verified Foreigner |  713 |                  36 |                114 |                    24.4 |

### 4c. FOREIGNER_STATUS x UNI_TYPE cross-tabulation

**Table 05-10. FOREIGNER_STATUS by UNI_TYPE (all types)**

| UNI_TYPE   | FOREIGNER_STATUS   |     N |   Median Percentile |   Median Raw Total |
|:-----------|:-------------------|------:|--------------------:|-------------------:|
| Foreign    | Filipino           |  1136 |                  60 |                130 |
| Foreign    | Likely Foreigner   |    13 |                  27 |                103 |
| Foreign    | Verified Foreigner |   713 |                  36 |                114 |
| Private    | Filipino           | 83240 |                  54 |                125 |
| Private    | Verified Foreigner | 17344 |                  24 |                 99 |
| Public     | Filipino           | 22716 |                  62 |                132 |
| Public     | Verified Foreigner |  4221 |                  24 |                 99 |

**Table 05-11. Bin distribution among foreign examinees by FOREIGNER_STATUS**

| FOREIGNER_STATUS   |    B1 |    B2 |    B3 |    B4 |   B5 |   B6 |   B7 |    B8 |    B9 |   B10 |
|:-------------------|------:|------:|------:|------:|-----:|-----:|-----:|------:|------:|------:|
| Filipino           |  8.54 |   8.1 |  6.43 |   9.6 | 7.04 | 9.86 | 9.95 | 11.71 | 12.24 | 16.55 |
| Likely Foreigner   | 23.08 | 15.38 | 15.38 | 15.38 |    0 |    0 |    0 | 15.38 |     0 | 15.38 |
| Verified Foreigner | 22.72 | 11.36 |  9.12 |  9.12 |  9.4 | 7.29 | 6.59 |  6.03 |  8.13 | 10.24 |

---

## 5. Descriptive Statistics by UNI_TYPE

**Table 05-12. Descriptive statistics by university type**

| UNI_TYPE   |      N |   Median Percentile |   Mean Percentile |   Std Percentile |   Median Raw Total |   Mean Raw Total |   Std Raw Total |   Median GPS |   Median APT |   Median SA |   Q25 Percentile |   Q75 Percentile |   Q25 Raw Total |   Q75 Raw Total |
|:-----------|-------:|--------------------:|------------------:|-----------------:|-------------------:|-----------------:|----------------:|-------------:|-------------:|------------:|-----------------:|-----------------:|----------------:|----------------:|
| Public     |  26937 |                  57 |             54.26 |            31.09 |                127 |           128.53 |           34.77 |          517 |          516 |         516 |               27 |               83 |             102 |             154 |
| Private    | 100584 |                  49 |             48.88 |            29.54 |                121 |           121.78 |           30.76 |          497 |          503 |         494 |               23 |               74 |              99 |             143 |
| Foreign    |   1862 |                  52 |             50.35 |            31.34 |                124 |           125.31 |           34.47 |          504 |          503 |         503 |               21 |               79 |              99 |             150 |

### 5b. Median standard subtest scores by UNI_TYPE

**Table 05-13. Median standard subtest scores by university type**

| Subtest      |   Public (n=26,937) |   Private (n=100,584) |   Foreign (n=1,862) |
|:-------------|--------------------:|----------------------:|--------------------:|
| Verbal       |                 515 |                   500 |                 498 |
| Inductive    |                 529 |                   516 |                 523 |
| Quantitative |                 512 |                   498 |                 512 |
| Perceptual   |                 523 |                   512 |                 500 |
| Biology      |                 512 |                   494 |                 500 |
| Physics      |                 523 |                   500 |                 512 |
| Social       |                 510 |                   498 |                 494 |
| Chemistry    |                 511 |                   494 |                 500 |

### 5c. Median raw subtest scores by UNI_TYPE

**Table 05-14. Median raw subtest scores by university type**

| Subtest      |   Public (n=26,934) |   Private (n=100,557) |   Foreign (n=1,857) |
|:-------------|--------------------:|----------------------:|--------------------:|
| Verbal       |                  16 |                    16 |                  16 |
| Inductive    |                  18 |                    18 |                  18 |
| Quantitative |                  15 |                    14 |                  15 |
| Perceptual   |                  18 |                    17 |                  17 |
| Biology      |                  16 |                    14 |                  15 |
| Physics      |                  14 |                    13 |                  14 |
| Social       |                  16 |                    15 |                  15 |
| Chemistry    |                  14 |                    13 |                  14 |

---

## 6. Kruskal-Wallis Test: UNI_TYPE x NMS_PER_num

### 6a. Omnibus test

**Table 05-15. Kruskal-Wallis test result**

| Score Variable                |   H-statistic |     p-value |   Eta-squared | Effect Size   |   Groups compared |   Total N |
|:------------------------------|--------------:|------------:|--------------:|:--------------|------------------:|----------:|
| NMS_PER_num (Percentile Rank) |       699.887 | 1.0508e-152 |        0.0054 | Negligible    |                 3 |    129383 |

### 6b. Post-hoc pairwise comparisons (Mann-Whitney U)

**Table 05-16. Post-hoc Mann-Whitney U pairwise comparisons**

| Group 1   | Group 2   |   U-statistic |      p-value |   Effect size (r) |     N1 |     N2 |
|:----------|:----------|--------------:|-------------:|------------------:|-------:|-------:|
| Public    | Private   |    1.4967e+09 | 2.65653e-154 |           -0.1048 |  26937 | 100584 |
| Public    | Foreign   |   2.69213e+07 |  1.08352e-07 |           -0.0735 |  26937 |   1862 |
| Private   | Foreign   |   9.10024e+07 |    0.0367098 |            0.0282 | 100584 |   1862 |

### 6c. Kruskal-Wallis by subtest (standard scores)

**Table 05-17. Kruskal-Wallis tests by subtest (standard scores)**

| Subtest      |   H-statistic |      p-value |   Eta-squared |   Groups |   Total N |
|:-------------|--------------:|-------------:|--------------:|---------:|----------:|
| Verbal       |       219.087 |   2.6662e-48 |        0.0017 |        3 |    129383 |
| Inductive    |       256.913 |  1.62921e-56 |         0.002 |        3 |    129383 |
| Quantitative |       575.674 | 9.86384e-126 |        0.0044 |        3 |    129383 |
| Perceptual   |       149.308 |  3.78554e-33 |        0.0011 |        3 |    129383 |
| Biology      |       858.158 | 4.50127e-187 |        0.0066 |        3 |    129383 |
| Physics      |       744.803 | 1.85421e-162 |        0.0057 |        3 |    129383 |
| Social       |       268.741 |  4.40106e-59 |        0.0021 |        3 |    129383 |
| Chemistry    |       861.098 | 1.03508e-187 |        0.0066 |        3 |    129383 |


---
*Analysis complete. Generated by page_05_university_type.py*
