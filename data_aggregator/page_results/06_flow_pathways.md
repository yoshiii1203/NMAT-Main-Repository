# Page 6: Flow Pathways Analysis (Page 06)

**Generated:** 2026-07-28 01:17

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `besttrend + uni + bestobservable`

**Filters:** None (full unfiltered dataset)

---

**Subsets used:**
- **uni** (UNI_TYPE flow): besttrend, UNI_TYPE in [Public, Private, Foreign] — 132,409 records
- **besttrend** (CourseGroup flow): best NMAT record, Year 2006-2018 — 133,804 records
- **bestobservable** (Bin -> PLE flow): besttrend, Year <= 2014 — 64,501 records

---

## 1. Sankey Flow: UNI_TYPE -> PercentileBin

Source: `uni` subset (besttrend, Public/Private/Foreign)

**Table 06-1. University-type to percentile bin flow counts**

| UNI_TYPE   | PercentileBin   |   count |
|:-----------|:----------------|--------:|
| Public     | B1              |    2948 |
| Public     | B2              |    2230 |
| Public     | B3              |    2050 |
| Public     | B4              |    2227 |
| Public     | B5              |    2339 |
| Public     | B6              |    2406 |
| Public     | B7              |    2444 |
| Public     | B8              |    2573 |
| Public     | B9              |    2957 |
| Public     | B10             |    4763 |
| Private    | B1              |   12208 |
| Private    | B2              |    9806 |
| Private    | B3              |    9066 |
| Private    | B4              |    9958 |
| Private    | B5              |   10007 |
| Private    | B6              |    9934 |
| Private    | B7              |    9458 |
| Private    | B8              |    9716 |
| Private    | B9              |    9730 |
| Private    | B10             |   10701 |
| Foreign    | B1              |     262 |
| Foreign    | B2              |     175 |
| Foreign    | B3              |     140 |
| Foreign    | B4              |     176 |
| Foreign    | B5              |     147 |
| Foreign    | B6              |     164 |
| Foreign    | B7              |     160 |
| Foreign    | B8              |     178 |
| Foreign    | B9              |     197 |
| Foreign    | B10             |     263 |

### 1b. Flow matrix (UNI_TYPE rows, PercentileBin columns)

**Table 06-2. UNI_TYPE -> PercentileBin flow matrix**

| UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |    B5 |   B6 |   B7 |   B8 |   B9 |   B10 |
|:-----------|------:|-----:|-----:|-----:|------:|-----:|-----:|-----:|-----:|------:|
| Public     |  2948 | 2230 | 2050 | 2227 |  2339 | 2406 | 2444 | 2573 | 2957 |  4763 |
| Private    | 12208 | 9806 | 9066 | 9958 | 10007 | 9934 | 9458 | 9716 | 9730 | 10701 |
| Foreign    |   262 |  175 |  140 |  176 |   147 |  164 |  160 |  178 |  197 |   263 |

### 1c. Row percentages (within UNI_TYPE)

**Table 06-3. UNI_TYPE -> PercentileBin row percentages**

| UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:-----------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Public     | 10.94 | 8.28 | 7.61 | 8.27 | 8.68 | 8.93 | 9.07 | 9.55 | 10.98 | 17.68 |
| Private    | 12.14 | 9.75 | 9.01 |  9.9 | 9.95 | 9.88 |  9.4 | 9.66 |  9.67 | 10.64 |
| Foreign    | 14.07 |  9.4 | 7.52 | 9.45 | 7.89 | 8.81 | 8.59 | 9.56 | 10.58 | 14.12 |

---

## 2. Sankey Flow: CourseGroup -> PercentileBin

Source: `besttrend` subset

**Table 06-4. Course group to percentile bin flow counts**

| CourseGroup                  | PercentileBin   |   count |
|:-----------------------------|:----------------|--------:|
| Medical & Allied             | B1              |    6350 |
| Medical & Allied             | B2              |    6180 |
| Medical & Allied             | B3              |    5960 |
| Medical & Allied             | B4              |    6713 |
| Medical & Allied             | B5              |    6885 |
| Medical & Allied             | B6              |    6697 |
| Medical & Allied             | B7              |    6144 |
| Medical & Allied             | B8              |    6159 |
| Medical & Allied             | B9              |    5863 |
| Medical & Allied             | B10             |    6116 |
| Natural Sciences             | B1              |    4946 |
| Natural Sciences             | B2              |    3431 |
| Natural Sciences             | B3              |    3022 |
| Natural Sciences             | B4              |    3345 |
| Natural Sciences             | B5              |    3374 |
| Natural Sciences             | B6              |    3520 |
| Natural Sciences             | B7              |    3788 |
| Natural Sciences             | B8              |    3993 |
| Natural Sciences             | B9              |    4404 |
| Natural Sciences             | B10             |    6263 |
| Social & Behavioral Sciences | B1              |    3137 |
| Social & Behavioral Sciences | B2              |    1737 |
| Social & Behavioral Sciences | B3              |    1361 |
| Social & Behavioral Sciences | B4              |    1319 |
| Social & Behavioral Sciences | B5              |    1234 |
| Social & Behavioral Sciences | B6              |    1306 |
| Social & Behavioral Sciences | B7              |    1174 |
| Social & Behavioral Sciences | B8              |    1243 |
| Social & Behavioral Sciences | B9              |    1395 |
| Social & Behavioral Sciences | B10             |    1818 |
| Education                    | B1              |     312 |
| Education                    | B2              |     300 |
| Education                    | B3              |     310 |
| Education                    | B4              |     313 |
| Education                    | B5              |     339 |
| Education                    | B6              |     286 |
| Education                    | B7              |     298 |
| Education                    | B8              |     306 |
| Education                    | B9              |     329 |
| Education                    | B10             |     451 |
| Engineering & Technology     | B1              |      38 |
| Engineering & Technology     | B2              |      43 |
| Engineering & Technology     | B3              |      43 |
| Engineering & Technology     | B4              |      41 |
| Engineering & Technology     | B5              |      63 |
| Engineering & Technology     | B6              |      64 |
| Engineering & Technology     | B7              |      55 |
| Engineering & Technology     | B8              |      73 |
| Engineering & Technology     | B9              |     107 |
| Engineering & Technology     | B10             |     202 |
| Other                        | B1              |     802 |
| Other                        | B2              |     683 |
| Other                        | B3              |     671 |
| Other                        | B4              |     734 |
| Other                        | B5              |     752 |
| Other                        | B6              |     744 |
| Other                        | B7              |     721 |
| Other                        | B8              |     824 |
| Other                        | B9              |     907 |
| Other                        | B10             |    1047 |

### 2b. Flow matrix (CourseGroup rows, PercentileBin columns)

**Table 06-5. CourseGroup -> PercentileBin flow matrix**

| CourseGroup                  |   B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |   B9 |   B10 |
|:-----------------------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| Medical & Allied             | 6350 | 6180 | 5960 | 6713 | 6885 | 6697 | 6144 | 6159 | 5863 |  6116 |
| Natural Sciences             | 4946 | 3431 | 3022 | 3345 | 3374 | 3520 | 3788 | 3993 | 4404 |  6263 |
| Social & Behavioral Sciences | 3137 | 1737 | 1361 | 1319 | 1234 | 1306 | 1174 | 1243 | 1395 |  1818 |
| Education                    |  312 |  300 |  310 |  313 |  339 |  286 |  298 |  306 |  329 |   451 |
| Engineering & Technology     |   38 |   43 |   43 |   41 |   63 |   64 |   55 |   73 |  107 |   202 |
| Other                        |  802 |  683 |  671 |  734 |  752 |  744 |  721 |  824 |  907 |  1047 |

### 2c. Row percentages (within CourseGroup)

**Table 06-6. CourseGroup -> PercentileBin row percentages**

| CourseGroup                  |    B1 |    B2 |   B3 |    B4 |    B5 |    B6 |   B7 |    B8 |    B9 |   B10 |
|:-----------------------------|------:|------:|-----:|------:|------:|------:|-----:|------:|------:|------:|
| Medical & Allied             | 10.07 |   9.8 | 9.45 | 10.64 | 10.92 | 10.62 | 9.74 |  9.77 |   9.3 |   9.7 |
| Natural Sciences             | 12.34 |  8.56 | 7.54 |  8.34 |  8.42 |  8.78 | 9.45 |  9.96 | 10.99 | 15.62 |
| Social & Behavioral Sciences | 19.95 | 11.05 | 8.66 |  8.39 |  7.85 |  8.31 | 7.47 |  7.91 |  8.87 | 11.56 |
| Education                    |  9.62 |  9.25 | 9.56 |  9.65 | 10.45 |  8.82 | 9.19 |  9.43 | 10.14 |  13.9 |
| Engineering & Technology     |  5.21 |   5.9 |  5.9 |  5.62 |  8.64 |  8.78 | 7.54 | 10.01 | 14.68 | 27.71 |
| Other                        | 10.17 |  8.66 | 8.51 |  9.31 |  9.54 |  9.44 | 9.14 | 10.45 |  11.5 | 13.28 |

---

## 3. Sankey Flow: PercentileBin -> PLE_STATUS_LABEL

Source: `bestobservable` subset (besttrend, Year <= 2014)

**Table 06-7. Percentile bin to PLE status flow counts (observable cohort)**

| PercentileBin   | PLE_STATUS_LABEL       |   count |
|:----------------|:-----------------------|--------:|
| B1              | Confirmed PLE passer   |     505 |
| B1              | No confirmed PLE match |    5599 |
| B2              | Confirmed PLE passer   |     830 |
| B2              | No confirmed PLE match |    4424 |
| B3              | Confirmed PLE passer   |     997 |
| B3              | No confirmed PLE match |    4231 |
| B4              | Confirmed PLE passer   |    1312 |
| B4              | No confirmed PLE match |    4429 |
| B5              | Confirmed PLE passer   |    2882 |
| B5              | No confirmed PLE match |    3347 |
| B6              | Confirmed PLE passer   |    2992 |
| B6              | No confirmed PLE match |    2839 |
| B7              | Confirmed PLE passer   |    3359 |
| B7              | No confirmed PLE match |    2583 |
| B8              | Confirmed PLE passer   |    3819 |
| B8              | No confirmed PLE match |    2536 |
| B9              | Confirmed PLE passer   |    4595 |
| B9              | No confirmed PLE match |    2259 |
| B10             | Confirmed PLE passer   |    7352 |
| B10             | No confirmed PLE match |    2305 |

### 3b. PLE status composition within each bin (row %)

**Table 06-8. PLE status row percentages within each bin**

| PercentileBin   |   Confirmed PLE passer |   No confirmed PLE match |
|:----------------|-----------------------:|-------------------------:|
| B1              |                   8.27 |                    91.73 |
| B2              |                   15.8 |                     84.2 |
| B3              |                  19.07 |                    80.93 |
| B4              |                  22.85 |                    77.15 |
| B5              |                  46.27 |                    53.73 |
| B6              |                  51.31 |                    48.69 |
| B7              |                  56.53 |                    43.47 |
| B8              |                  60.09 |                    39.91 |
| B9              |                  67.04 |                    32.96 |
| B10             |                  76.13 |                    23.87 |

### 3c. Confirmed PLE passer rate by bin

**Table 06-9. PLE pass rate by percentile bin**

| PercentileBin   |   Confirmed PLE Passers |   Total in Bin |   PLE Pass Rate (%) |
|:----------------|------------------------:|---------------:|--------------------:|
| B1              |                     505 |           6104 |                8.27 |
| B2              |                     830 |           5254 |                15.8 |
| B3              |                     997 |           5228 |               19.07 |
| B4              |                    1312 |           5741 |               22.85 |
| B5              |                    2882 |           6229 |               46.27 |
| B6              |                    2992 |           5831 |               51.31 |
| B7              |                    3359 |           5942 |               56.53 |
| B8              |                    3819 |           6355 |               60.09 |
| B9              |                    4595 |           6854 |               67.04 |
| B10             |                    7352 |           9657 |               76.13 |

---

## 4. Top 10 Pathways: UNI_TYPE -> B8-B10

Source: `uni` subset (besttrend, Public/Private/Foreign)

**Table 06-10. Top 10 UNI_TYPE pathways into B8-B10**

| UNI_TYPE   | PercentileBin   |   Count |
|:-----------|:----------------|--------:|
| Private    | B10             |   10701 |
| Private    | B9              |    9730 |
| Private    | B8              |    9716 |
| Public     | B10             |    4763 |
| Public     | B9              |    2957 |
| Public     | B8              |    2573 |
| Foreign    | B10             |     263 |
| Foreign    | B9              |     197 |
| Foreign    | B8              |     178 |

**Table 06-11. Top 10 UNI_TYPE pathways (ranked)**

|   Rank | UNI_TYPE   | PercentileBin   |   Count |
|-------:|:-----------|:----------------|--------:|
|      1 | Private    | B10             |   10701 |
|      2 | Private    | B9              |    9730 |
|      3 | Private    | B8              |    9716 |
|      4 | Public     | B10             |    4763 |
|      5 | Public     | B9              |    2957 |
|      6 | Public     | B8              |    2573 |
|      7 | Foreign    | B10             |     263 |
|      8 | Foreign    | B9              |     197 |
|      9 | Foreign    | B8              |     178 |

### 4b. Full summary: UNI_TYPE top-bin counts

**Table 06-12. Full UNI_TYPE -> top-bin breakdown**

| UNI_TYPE   | PercentileBin   |   Count |
|:-----------|:----------------|--------:|
| Foreign    | B10             |     263 |
| Foreign    | B8              |     178 |
| Foreign    | B9              |     197 |
| Private    | B10             |   10701 |
| Private    | B8              |    9716 |
| Private    | B9              |    9730 |
| Public     | B10             |    4763 |
| Public     | B8              |    2573 |
| Public     | B9              |    2957 |

---

## 5. Top 10 Pathways: CourseGroup -> B8-B10

Source: `besttrend` subset

**Table 06-13. Top 10 CourseGroup pathways into B8-B10**

| CourseGroup                  | PercentileBin   |   Count |
|:-----------------------------|:----------------|--------:|
| Natural Sciences             | B10             |    6263 |
| Medical & Allied             | B8              |    6159 |
| Medical & Allied             | B10             |    6116 |
| Medical & Allied             | B9              |    5863 |
| Natural Sciences             | B9              |    4404 |
| Natural Sciences             | B8              |    3993 |
| Social & Behavioral Sciences | B10             |    1818 |
| Social & Behavioral Sciences | B9              |    1395 |
| Social & Behavioral Sciences | B8              |    1243 |
| Other                        | B10             |    1047 |

**Table 06-14. Top 10 CourseGroup pathways (ranked)**

|   Rank | CourseGroup                  | PercentileBin   |   Count |
|-------:|:-----------------------------|:----------------|--------:|
|      1 | Natural Sciences             | B10             |    6263 |
|      2 | Medical & Allied             | B8              |    6159 |
|      3 | Medical & Allied             | B10             |    6116 |
|      4 | Medical & Allied             | B9              |    5863 |
|      5 | Natural Sciences             | B9              |    4404 |
|      6 | Natural Sciences             | B8              |    3993 |
|      7 | Social & Behavioral Sciences | B10             |    1818 |
|      8 | Social & Behavioral Sciences | B9              |    1395 |
|      9 | Social & Behavioral Sciences | B8              |    1243 |
|     10 | Other                        | B10             |    1047 |

### 5b. Full summary: CourseGroup top-bin counts

**Table 06-15. Full CourseGroup -> top-bin breakdown**

| CourseGroup                  | PercentileBin   |   Count |
|:-----------------------------|:----------------|--------:|
| Education                    | B10             |     451 |
| Education                    | B8              |     306 |
| Education                    | B9              |     329 |
| Engineering & Technology     | B10             |     202 |
| Engineering & Technology     | B8              |      73 |
| Engineering & Technology     | B9              |     107 |
| Medical & Allied             | B10             |    6116 |
| Medical & Allied             | B8              |    6159 |
| Medical & Allied             | B9              |    5863 |
| Natural Sciences             | B10             |    6263 |
| Natural Sciences             | B8              |    3993 |
| Natural Sciences             | B9              |    4404 |
| Other                        | B10             |    1047 |
| Other                        | B8              |     824 |
| Other                        | B9              |     907 |
| Social & Behavioral Sciences | B10             |    1818 |
| Social & Behavioral Sciences | B8              |    1243 |
| Social & Behavioral Sciences | B9              |    1395 |

---

## 6. Cross-Flow Comparisons

### 6a. Top-bin rate by UNI_TYPE

**Table 06-16. Top-bin rate by UNI_TYPE**

| UNI_TYPE   |   Total N |   Top Bin N |   Top Bin Rate (%) |
|:-----------|----------:|------------:|-------------------:|
| Foreign    |      1894 |         638 |              33.69 |
| Private    |    102888 |       30147 |               29.3 |
| Public     |     27627 |       10293 |              37.26 |

### 6b. Top-bin rate by CourseGroup

**Table 06-17. Top-bin rate by CourseGroup**

| CourseGroup                  |   Total N |   Top Bin N |   Top Bin Rate (%) |
|:-----------------------------|----------:|------------:|-------------------:|
| Education                    |      3279 |        1086 |              33.12 |
| Engineering & Technology     |       750 |         382 |              50.93 |
| Medical & Allied             |     63900 |       18138 |              28.38 |
| Natural Sciences             |     41430 |       14660 |              35.38 |
| Other                        |      7983 |        2778 |               34.8 |
| Social & Behavioral Sciences |     16462 |        4456 |              27.07 |

### 6c. Top-bin rate by UNI_TYPE x CourseGroup

**Table 06-18. Top-bin rate by UNI_TYPE x CourseGroup**

| UNI_TYPE   | CourseGroup                  |   Total N |   Top Bin N |   Top Bin Rate (%) |
|:-----------|:-----------------------------|----------:|------------:|-------------------:|
| Public     | Education                    |       735 |         444 |              60.41 |
| Public     | Engineering & Technology     |       159 |          90 |               56.6 |
| Foreign    | Engineering & Technology     |        28 |          14 |                 50 |
| Private    | Engineering & Technology     |       555 |         274 |              49.37 |
| Public     | Other                        |      2122 |         924 |              43.54 |
| Foreign    | Natural Sciences             |       611 |         266 |              43.54 |
| Foreign    | Other                        |       189 |          80 |              42.33 |
| Public     | Natural Sciences             |      9797 |        3905 |              39.86 |
| Private    | Natural Sciences             |     30534 |       10321 |               33.8 |
| Public     | Medical & Allied             |     11438 |        3826 |              33.45 |
| Public     | Social & Behavioral Sciences |      3376 |        1104 |               32.7 |
| Private    | Other                        |      5609 |        1761 |               31.4 |
| Foreign    | Social & Behavioral Sciences |       220 |          64 |              29.09 |
| Private    | Medical & Allied             |     51037 |       13928 |              27.29 |
| Private    | Social & Behavioral Sciences |     12699 |        3244 |              25.55 |
| Foreign    | Medical & Allied             |       764 |         195 |              25.52 |
| Private    | Education                    |      2454 |         619 |              25.22 |
| Foreign    | Education                    |        82 |          19 |              23.17 |

### 6d. Course composition within each UNI_TYPE

**Table 06-19. Course composition within each UNI_TYPE**

| UNI_TYPE   | CourseGroup                  |   Count |   Percent within UNI_TYPE |
|:-----------|:-----------------------------|--------:|--------------------------:|
| Foreign    | Medical & Allied             |     764 |                     40.34 |
| Foreign    | Natural Sciences             |     611 |                     32.26 |
| Foreign    | Social & Behavioral Sciences |     220 |                     11.62 |
| Foreign    | Other                        |     189 |                      9.98 |
| Foreign    | Education                    |      82 |                      4.33 |
| Foreign    | Engineering & Technology     |      28 |                      1.48 |
| Private    | Medical & Allied             |   51037 |                      49.6 |
| Private    | Natural Sciences             |   30534 |                     29.68 |
| Private    | Social & Behavioral Sciences |   12699 |                     12.34 |
| Private    | Other                        |    5609 |                      5.45 |
| Private    | Education                    |    2454 |                      2.39 |
| Private    | Engineering & Technology     |     555 |                      0.54 |
| Public     | Medical & Allied             |   11438 |                      41.4 |
| Public     | Natural Sciences             |    9797 |                     35.46 |
| Public     | Social & Behavioral Sciences |    3376 |                     12.22 |
| Public     | Other                        |    2122 |                      7.68 |
| Public     | Education                    |     735 |                      2.66 |
| Public     | Engineering & Technology     |     159 |                      0.58 |


---
*Analysis complete. Generated by page_06_flow_pathways.py*
