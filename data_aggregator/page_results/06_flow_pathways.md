# Page 6: Flow Pathways Analysis (Page 06)

**Generated:** 2026-08-14 18:07

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `besttrend + uni + bestobservable`

**Filters:** None (full unfiltered dataset)

---

**Subsets used:**
- **uni** (UNDERGRAD_UNI_TYPE flow): besttrend, UNDERGRAD_UNI_TYPE in [Public, Private, Foreign] — 133,315 records
- **besttrend** (UNDERGRAD_COURSE_GROUP flow): best NMAT record, Year 2006-2018 — 134,869 records
- **bestobservable** (Bin -> PLE flow): best attempt within Year<=2014 (IS_BEST_OBSERVABLE_RECORD) — 69,503 records

---

## 1. Sankey Flow: UNDERGRAD_UNI_TYPE -> PercentileBin

Source: `uni` subset (besttrend, Public/Private/Foreign)

**Table 06-1. University-type to percentile bin flow counts**

| UNDERGRAD_UNI_TYPE   | PercentileBin   |   count |
|:---------------------|:----------------|--------:|
| Public               | B1              |    2874 |
| Public               | B2              |    2176 |
| Public               | B3              |    2016 |
| Public               | B4              |    2209 |
| Public               | B5              |    2288 |
| Public               | B6              |    2385 |
| Public               | B7              |    2442 |
| Public               | B8              |    2586 |
| Public               | B9              |    3029 |
| Public               | B10             |    4854 |
| Private              | B1              |   12248 |
| Private              | B2              |    9857 |
| Private              | B3              |    9151 |
| Private              | B4              |   10082 |
| Private              | B5              |   10058 |
| Private              | B6              |   10104 |
| Private              | B7              |    9622 |
| Private              | B8              |    9833 |
| Private              | B9              |    9876 |
| Private              | B10             |   10784 |
| Foreign              | B1              |     262 |
| Foreign              | B2              |     174 |
| Foreign              | B3              |     140 |
| Foreign              | B4              |     176 |
| Foreign              | B5              |     145 |
| Foreign              | B6              |     164 |
| Foreign              | B7              |     161 |
| Foreign              | B8              |     175 |
| Foreign              | B9              |     197 |
| Foreign              | B10             |     266 |

### 1b. Flow matrix (UNDERGRAD_UNI_TYPE rows, PercentileBin columns)

**Table 06-2. UNDERGRAD_UNI_TYPE -> PercentileBin flow matrix**

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |    B4 |    B5 |    B6 |   B7 |   B8 |   B9 |   B10 |
|:---------------------|------:|-----:|-----:|------:|------:|------:|-----:|-----:|-----:|------:|
| Public               |  2874 | 2176 | 2016 |  2209 |  2288 |  2385 | 2442 | 2586 | 3029 |  4854 |
| Private              | 12248 | 9857 | 9151 | 10082 | 10058 | 10104 | 9622 | 9833 | 9876 | 10784 |
| Foreign              |   262 |  174 |  140 |   176 |   145 |   164 |  161 |  175 |  197 |   266 |

### 1c. Row percentages (within UNDERGRAD_UNI_TYPE)

**Table 06-3. UNDERGRAD_UNI_TYPE -> PercentileBin row percentages**

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Public               |  10.7 |  8.1 | 7.51 | 8.22 | 8.52 | 8.88 | 9.09 | 9.63 | 11.28 | 18.07 |
| Private              | 12.05 |  9.7 | 9.01 | 9.92 |  9.9 | 9.94 | 9.47 | 9.68 |  9.72 | 10.61 |
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |

---

## 2. Sankey Flow: UNDERGRAD_COURSE_GROUP -> PercentileBin

Source: `besttrend` subset

**Table 06-4. Course group to percentile bin flow counts**

| UNDERGRAD_COURSE_GROUP       | PercentileBin   |   count |
|:-----------------------------|:----------------|--------:|
| Medical & Allied             | B1              |    6348 |
| Medical & Allied             | B2              |    6179 |
| Medical & Allied             | B3              |    5988 |
| Medical & Allied             | B4              |    6771 |
| Medical & Allied             | B5              |    6865 |
| Medical & Allied             | B6              |    6765 |
| Medical & Allied             | B7              |    6198 |
| Medical & Allied             | B8              |    6213 |
| Medical & Allied             | B9              |    5960 |
| Medical & Allied             | B10             |    6181 |
| Natural Sciences             | B1              |    4942 |
| Natural Sciences             | B2              |    3425 |
| Natural Sciences             | B3              |    3029 |
| Natural Sciences             | B4              |    3351 |
| Natural Sciences             | B5              |    3358 |
| Natural Sciences             | B6              |    3535 |
| Natural Sciences             | B7              |    3796 |
| Natural Sciences             | B8              |    4011 |
| Natural Sciences             | B9              |    4439 |
| Natural Sciences             | B10             |    6310 |
| Social & Behavioral Sciences | B1              |    3137 |
| Social & Behavioral Sciences | B2              |    1736 |
| Social & Behavioral Sciences | B3              |    1359 |
| Social & Behavioral Sciences | B4              |    1320 |
| Social & Behavioral Sciences | B5              |    1233 |
| Social & Behavioral Sciences | B6              |    1307 |
| Social & Behavioral Sciences | B7              |    1181 |
| Social & Behavioral Sciences | B8              |    1249 |
| Social & Behavioral Sciences | B9              |    1406 |
| Social & Behavioral Sciences | B10             |    1830 |
| Education                    | B1              |     313 |
| Education                    | B2              |     306 |
| Education                    | B3              |     319 |
| Education                    | B4              |     333 |
| Education                    | B5              |     365 |
| Education                    | B6              |     314 |
| Education                    | B7              |     335 |
| Education                    | B8              |     331 |
| Education                    | B9              |     360 |
| Education                    | B10             |     469 |
| Engineering & Technology     | B1              |      38 |
| Engineering & Technology     | B2              |      43 |
| Engineering & Technology     | B3              |      43 |
| Engineering & Technology     | B4              |      41 |
| Engineering & Technology     | B5              |      63 |
| Engineering & Technology     | B6              |      64 |
| Engineering & Technology     | B7              |      55 |
| Engineering & Technology     | B8              |      73 |
| Engineering & Technology     | B9              |     107 |
| Engineering & Technology     | B10             |     203 |
| Other                        | B1              |     805 |
| Other                        | B2              |     699 |
| Other                        | B3              |     699 |
| Other                        | B4              |     773 |
| Other                        | B5              |     774 |
| Other                        | B6              |     794 |
| Other                        | B7              |     794 |
| Other                        | B8              |     859 |
| Other                        | B9              |     959 |
| Other                        | B10             |    1092 |

### 2b. Flow matrix (UNDERGRAD_COURSE_GROUP rows, PercentileBin columns)

**Table 06-5. UNDERGRAD_COURSE_GROUP -> PercentileBin flow matrix**

| UNDERGRAD_COURSE_GROUP       |   B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |   B9 |   B10 |
|:-----------------------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| Medical & Allied             | 6348 | 6179 | 5988 | 6771 | 6865 | 6765 | 6198 | 6213 | 5960 |  6181 |
| Natural Sciences             | 4942 | 3425 | 3029 | 3351 | 3358 | 3535 | 3796 | 4011 | 4439 |  6310 |
| Social & Behavioral Sciences | 3137 | 1736 | 1359 | 1320 | 1233 | 1307 | 1181 | 1249 | 1406 |  1830 |
| Education                    |  313 |  306 |  319 |  333 |  365 |  314 |  335 |  331 |  360 |   469 |
| Engineering & Technology     |   38 |   43 |   43 |   41 |   63 |   64 |   55 |   73 |  107 |   203 |
| Other                        |  805 |  699 |  699 |  773 |  774 |  794 |  794 |  859 |  959 |  1092 |

### 2c. Row percentages (within UNDERGRAD_COURSE_GROUP)

**Table 06-6. UNDERGRAD_COURSE_GROUP -> PercentileBin row percentages**

| UNDERGRAD_COURSE_GROUP       |    B1 |    B2 |   B3 |    B4 |    B5 |    B6 |   B7 |    B8 |    B9 |   B10 |
|:-----------------------------|------:|------:|-----:|------:|------:|------:|-----:|------:|------:|------:|
| Medical & Allied             |    10 |  9.74 | 9.43 | 10.67 | 10.82 | 10.66 | 9.77 |  9.79 |  9.39 |  9.74 |
| Natural Sciences             | 12.29 |  8.52 | 7.54 |  8.34 |  8.35 |  8.79 | 9.44 |  9.98 | 11.04 |  15.7 |
| Social & Behavioral Sciences | 19.91 | 11.02 | 8.62 |  8.38 |  7.82 |  8.29 | 7.49 |  7.93 |  8.92 | 11.61 |
| Education                    |  9.09 |  8.88 | 9.26 |  9.67 |  10.6 |  9.11 | 9.72 |  9.61 | 10.45 | 13.61 |
| Engineering & Technology     |  5.21 |  5.89 | 5.89 |  5.62 |  8.63 |  8.77 | 7.53 |    10 | 14.66 | 27.81 |
| Other                        |  9.76 |  8.47 | 8.47 |  9.37 |  9.38 |  9.63 | 9.63 | 10.41 | 11.63 | 13.24 |

---

## 3. Sankey Flow: PercentileBin -> PLE_STATUS_LABEL

Source: `bestobservable` subset (besttrend, Year <= 2014)

**Table 06-7. Percentile bin to PLE status flow counts (observable cohort)**

| PercentileBin   | PLE_STATUS_LABEL       |   count |
|:----------------|:-----------------------|--------:|
| B1              | Confirmed PLE passer   |     740 |
| B1              | No confirmed PLE match |    6113 |
| B2              | Confirmed PLE passer   |    1219 |
| B2              | No confirmed PLE match |    4665 |
| B3              | Confirmed PLE passer   |    1551 |
| B3              | No confirmed PLE match |    4262 |
| B4              | Confirmed PLE passer   |    2155 |
| B4              | No confirmed PLE match |    4318 |
| B5              | Confirmed PLE passer   |    2852 |
| B5              | No confirmed PLE match |    3730 |
| B6              | Confirmed PLE passer   |    2976 |
| B6              | No confirmed PLE match |    3308 |
| B7              | Confirmed PLE passer   |    3214 |
| B7              | No confirmed PLE match |    3145 |
| B8              | Confirmed PLE passer   |    3534 |
| B8              | No confirmed PLE match |    3170 |
| B9              | Confirmed PLE passer   |    4323 |
| B9              | No confirmed PLE match |    2940 |
| B10             | Confirmed PLE passer   |    6946 |
| B10             | No confirmed PLE match |    3012 |

### 3b. PLE status composition within each bin (row %)

**Table 06-8. PLE status row percentages within each bin**

| PercentileBin   |   Confirmed PLE passer |   No confirmed PLE match |
|:----------------|-----------------------:|-------------------------:|
| B1              |                   10.8 |                     89.2 |
| B2              |                  20.72 |                    79.28 |
| B3              |                  26.68 |                    73.32 |
| B4              |                  33.29 |                    66.71 |
| B5              |                  43.33 |                    56.67 |
| B6              |                  47.36 |                    52.64 |
| B7              |                  50.54 |                    49.46 |
| B8              |                  52.71 |                    47.29 |
| B9              |                  59.52 |                    40.48 |
| B10             |                  69.75 |                    30.25 |

### 3c. Confirmed PLE linkage rate by bin

**Table 06-9. PLE linkage rate by percentile bin**

| PercentileBin   |   Confirmed PLE Passers |   Total in Bin |   PLE Linkage Rate (%) |
|:----------------|------------------------:|---------------:|-----------------------:|
| B1              |                     740 |           6853 |                   10.8 |
| B2              |                    1219 |           5884 |                  20.72 |
| B3              |                    1551 |           5813 |                  26.68 |
| B4              |                    2155 |           6473 |                  33.29 |
| B5              |                    2852 |           6582 |                  43.33 |
| B6              |                    2976 |           6284 |                  47.36 |
| B7              |                    3214 |           6359 |                  50.54 |
| B8              |                    3534 |           6704 |                  52.71 |
| B9              |                    4323 |           7263 |                  59.52 |
| B10             |                    6946 |           9958 |                  69.75 |

---

## 4. Top 10 Pathways: UNDERGRAD_UNI_TYPE -> B8-B10

Source: `uni` subset (besttrend, Public/Private/Foreign)

**Table 06-10. Top 10 UNDERGRAD_UNI_TYPE pathways into B8-B10**

| UNDERGRAD_UNI_TYPE   | PercentileBin   |   Count |
|:---------------------|:----------------|--------:|
| Private              | B10             |   10784 |
| Private              | B9              |    9876 |
| Private              | B8              |    9833 |
| Public               | B10             |    4854 |
| Public               | B9              |    3029 |
| Public               | B8              |    2586 |
| Foreign              | B10             |     266 |
| Foreign              | B9              |     197 |
| Foreign              | B8              |     175 |

**Table 06-11. Top 10 UNDERGRAD_UNI_TYPE pathways (ranked)**

|   Rank | UNDERGRAD_UNI_TYPE   | PercentileBin   |   Count |
|-------:|:---------------------|:----------------|--------:|
|      1 | Private              | B10             |   10784 |
|      2 | Private              | B9              |    9876 |
|      3 | Private              | B8              |    9833 |
|      4 | Public               | B10             |    4854 |
|      5 | Public               | B9              |    3029 |
|      6 | Public               | B8              |    2586 |
|      7 | Foreign              | B10             |     266 |
|      8 | Foreign              | B9              |     197 |
|      9 | Foreign              | B8              |     175 |

### 4b. Full summary: UNDERGRAD_UNI_TYPE top-bin counts

**Table 06-12. Full UNDERGRAD_UNI_TYPE -> top-bin breakdown**

| UNDERGRAD_UNI_TYPE   | PercentileBin   |   Count |
|:---------------------|:----------------|--------:|
| Foreign              | B10             |     266 |
| Foreign              | B8              |     175 |
| Foreign              | B9              |     197 |
| Private              | B10             |   10784 |
| Private              | B8              |    9833 |
| Private              | B9              |    9876 |
| Public               | B10             |    4854 |
| Public               | B8              |    2586 |
| Public               | B9              |    3029 |

---

## 5. Top 10 Pathways: UNDERGRAD_COURSE_GROUP -> B8-B10

Source: `besttrend` subset

**Table 06-13. Top 10 UNDERGRAD_COURSE_GROUP pathways into B8-B10**

| UNDERGRAD_COURSE_GROUP       | PercentileBin   |   Count |
|:-----------------------------|:----------------|--------:|
| Natural Sciences             | B10             |    6310 |
| Medical & Allied             | B8              |    6213 |
| Medical & Allied             | B10             |    6181 |
| Medical & Allied             | B9              |    5960 |
| Natural Sciences             | B9              |    4439 |
| Natural Sciences             | B8              |    4011 |
| Social & Behavioral Sciences | B10             |    1830 |
| Social & Behavioral Sciences | B9              |    1406 |
| Social & Behavioral Sciences | B8              |    1249 |
| Other                        | B10             |    1092 |

**Table 06-14. Top 10 UNDERGRAD_COURSE_GROUP pathways (ranked)**

|   Rank | UNDERGRAD_COURSE_GROUP       | PercentileBin   |   Count |
|-------:|:-----------------------------|:----------------|--------:|
|      1 | Natural Sciences             | B10             |    6310 |
|      2 | Medical & Allied             | B8              |    6213 |
|      3 | Medical & Allied             | B10             |    6181 |
|      4 | Medical & Allied             | B9              |    5960 |
|      5 | Natural Sciences             | B9              |    4439 |
|      6 | Natural Sciences             | B8              |    4011 |
|      7 | Social & Behavioral Sciences | B10             |    1830 |
|      8 | Social & Behavioral Sciences | B9              |    1406 |
|      9 | Social & Behavioral Sciences | B8              |    1249 |
|     10 | Other                        | B10             |    1092 |

### 5b. Full summary: UNDERGRAD_COURSE_GROUP top-bin counts

**Table 06-15. Full UNDERGRAD_COURSE_GROUP -> top-bin breakdown**

| UNDERGRAD_COURSE_GROUP       | PercentileBin   |   Count |
|:-----------------------------|:----------------|--------:|
| Education                    | B10             |     469 |
| Education                    | B8              |     331 |
| Education                    | B9              |     360 |
| Engineering & Technology     | B10             |     203 |
| Engineering & Technology     | B8              |      73 |
| Engineering & Technology     | B9              |     107 |
| Medical & Allied             | B10             |    6181 |
| Medical & Allied             | B8              |    6213 |
| Medical & Allied             | B9              |    5960 |
| Natural Sciences             | B10             |    6310 |
| Natural Sciences             | B8              |    4011 |
| Natural Sciences             | B9              |    4439 |
| Other                        | B10             |    1092 |
| Other                        | B8              |     859 |
| Other                        | B9              |     959 |
| Social & Behavioral Sciences | B10             |    1830 |
| Social & Behavioral Sciences | B8              |    1249 |
| Social & Behavioral Sciences | B9              |    1406 |

---

## 6. Cross-Flow Comparisons

### 6a. Top-bin rate by UNDERGRAD_UNI_TYPE

**Table 06-16. Top-bin rate by UNDERGRAD_UNI_TYPE**

| UNDERGRAD_UNI_TYPE   |   Total N |   Top Bin N |   Top Bin Rate (%) |
|:---------------------|----------:|------------:|-------------------:|
| Foreign              |      1892 |         638 |              33.72 |
| Private              |    103885 |       30493 |              29.35 |
| Public               |     27538 |       10469 |              38.02 |

### 6b. Top-bin rate by UNDERGRAD_COURSE_GROUP

**Table 06-17. Top-bin rate by UNDERGRAD_COURSE_GROUP**

| UNDERGRAD_COURSE_GROUP       |   Total N |   Top Bin N |   Top Bin Rate (%) |
|:-----------------------------|----------:|------------:|-------------------:|
| Education                    |      3479 |        1160 |              33.34 |
| Engineering & Technology     |       751 |         383 |                 51 |
| Medical & Allied             |     64287 |       18354 |              28.55 |
| Natural Sciences             |     41514 |       14760 |              35.55 |
| Other                        |      8346 |        2910 |              34.87 |
| Social & Behavioral Sciences |     16492 |        4485 |               27.2 |

### 6c. Top-bin rate by UNDERGRAD_UNI_TYPE x UNDERGRAD_COURSE_GROUP

**Table 06-18. Top-bin rate by UNDERGRAD_UNI_TYPE x UNDERGRAD_COURSE_GROUP**

| UNDERGRAD_UNI_TYPE   | UNDERGRAD_COURSE_GROUP       |   Total N |   Top Bin N |   Top Bin Rate (%) |
|:---------------------|:-----------------------------|----------:|------------:|-------------------:|
| Public               | Education                    |       748 |         472 |               63.1 |
| Public               | Engineering & Technology     |       156 |          90 |              57.69 |
| Foreign              | Engineering & Technology     |        28 |          14 |                 50 |
| Private              | Engineering & Technology     |       558 |         274 |               49.1 |
| Public               | Other                        |      2133 |         988 |              46.32 |
| Foreign              | Natural Sciences             |       608 |         265 |              43.59 |
| Foreign              | Other                        |       189 |          80 |              42.33 |
| Public               | Natural Sciences             |      9782 |        3928 |              40.16 |
| Public               | Medical & Allied             |     11338 |        3871 |              34.14 |
| Private              | Natural Sciences             |     30609 |       10387 |              33.93 |
| Public               | Social & Behavioral Sciences |      3381 |        1120 |              33.13 |
| Private              | Other                        |      5915 |        1821 |              30.79 |
| Foreign              | Social & Behavioral Sciences |       221 |          65 |              29.41 |
| Private              | Medical & Allied             |     51456 |       14092 |              27.39 |
| Private              | Social & Behavioral Sciences |     12715 |        3255 |               25.6 |
| Foreign              | Medical & Allied             |       764 |         195 |              25.52 |
| Private              | Education                    |      2632 |         664 |              25.23 |
| Foreign              | Education                    |        82 |          19 |              23.17 |

### 6d. Course composition within each UNDERGRAD_UNI_TYPE

**Table 06-19. Course composition within each UNDERGRAD_UNI_TYPE**

| UNDERGRAD_UNI_TYPE   | UNDERGRAD_COURSE_GROUP       |   Count |   Percent within UNDERGRAD_UNI_TYPE |
|:---------------------|:-----------------------------|--------:|------------------------------------:|
| Foreign              | Medical & Allied             |     764 |                               40.38 |
| Foreign              | Natural Sciences             |     608 |                               32.14 |
| Foreign              | Social & Behavioral Sciences |     221 |                               11.68 |
| Foreign              | Other                        |     189 |                                9.99 |
| Foreign              | Education                    |      82 |                                4.33 |
| Foreign              | Engineering & Technology     |      28 |                                1.48 |
| Private              | Medical & Allied             |   51456 |                               49.53 |
| Private              | Natural Sciences             |   30609 |                               29.46 |
| Private              | Social & Behavioral Sciences |   12715 |                               12.24 |
| Private              | Other                        |    5915 |                                5.69 |
| Private              | Education                    |    2632 |                                2.53 |
| Private              | Engineering & Technology     |     558 |                                0.54 |
| Public               | Medical & Allied             |   11338 |                               41.17 |
| Public               | Natural Sciences             |    9782 |                               35.52 |
| Public               | Social & Behavioral Sciences |    3381 |                               12.28 |
| Public               | Other                        |    2133 |                                7.75 |
| Public               | Education                    |     748 |                                2.72 |
| Public               | Engineering & Technology     |     156 |                                0.57 |


---
*Analysis complete. Generated by page_06_flow_pathways.py*
