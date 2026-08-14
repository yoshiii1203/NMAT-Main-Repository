# Page 1: Executive Summary

**Generated:** 2026-08-14 16:58

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `besttrend` (best-record rows 2006-2018) and `bestobservable` (Year <= 2014)

**Filters:** None (full unfiltered dataset)

---

## Metric Cards (Row 1)

| Metric | Value |
|--------|------:|
| Best-record examinees | 134,869 |
| Years covered | 13 |
| Median TRUE raw score | 122.0 |
| Median percentile rank | 50.0 |

## Metric Cards (Row 2)

| Metric | Value |
|--------|------:|
| Unique examinees | 134,869 |
| Repeat takers | 33,713 |
| Observable cohort size | 69,503 |
| Confirmed PLE share (observable) | 45.44% |

---

## Course Group Composition

**Figure 2 data — Course-group pie chart (best-record examinees)**

| UNDERGRAD_COURSE_GROUP       |   Count |   Share (%) |
|:-----------------------------|--------:|------------:|
| Medical & Allied             |   64287 |       47.67 |
| Natural Sciences             |   41514 |       30.78 |
| Social & Behavioral Sciences |   16492 |       12.23 |
| Other                        |    8346 |        6.19 |
| Education                    |    3479 |        2.58 |
| Engineering & Technology     |     751 |        0.56 |

## University Type Composition

**Figure 3 data — University-type pie chart (best-record examinees)**

| UNDERGRAD_UNI_TYPE   |   Count |   Share (%) |
|:---------------------|--------:|------------:|
| Private              |  103669 |       76.87 |
| Public               |   27916 |        20.7 |
| Foreign              |    1892 |         1.4 |
| Not Specified        |    1392 |        1.03 |

---

## Annual NMAT Score and Volume Profile (Figure 1)

**Figure 1. Annual NMAT score and volume profile**

Median TRUE raw score, Part I and Part II medians, median percentile rank, and examinee count by year.

### Yearly Summary (besttrend cohort)

|   Year |     n |   median_raw |   q25_raw |   q75_raw |   median_pct |   q25_pct |   q75_pct |   median_gps |   median_apt |   median_sa |
|-------:|------:|-------------:|----------:|----------:|-------------:|----------:|----------:|-------------:|-------------:|------------:|
|   2006 |  3698 |          131 |       108 |       154 |           53 |        27 |        77 |          510 |          509 |         504 |
|   2007 |  3690 |          130 |       107 |       156 |           52 |        27 |        77 |          507 |          509 |         504 |
|   2008 |  4965 |          129 |       107 |       153 |           54 |        28 |        80 |          511 |          504 |         510 |
|   2009 |  7461 |          130 |       109 |       152 |           52 |        27 |        77 |          505 |          504 |         504 |
|   2010 |  8551 |          136 |       115 |       159 |           57 |        32 |        81 |          518 |          522 |         510 |
|   2011 |  8701 |          129 |       109 |       151 |           52 |        30 |        76 |          505 |          520 |         489 |
|   2012 |  9113 |          122 |       101 |       145 |           54 |        26 |        81 |          513 |          521 |         504 |
|   2013 |  9148 |          128 |       103 |       154 |           60 |        24 |        86 |          529 |          527 |         527 |
|   2014 | 10455 |          120 |        98 |       142 |           57 |        24 |        83 |          522 |          521 |         516 |
|   2015 | 10326 |          118 |        93 |       142 |           52 |        19 |        78 |          506 |          497 |         522 |
|   2016 | 12480 |          123 |        98 |       146 |           48 |        19 |        73 |          495 |          503 |         483 |
|   2017 | 23948 |          118 |        93 |       143 |           44 |        19 |        70 |          485 |          493 |         477 |
|   2018 | 22333 |          111 |        91 |       132 |           43 |        17 |        70 |          481 |          483 |         488 |

### Yearly Part I / Part II Breakdown

|   Year |   Median Part I |   Median Part II |   Median Total Raw |   Part I Share (%) |   Part II Share (%) |
|-------:|----------------:|-----------------:|-------------------:|-------------------:|--------------------:|
|   2006 |              67 |               63 |                131 |              51.15 |               48.09 |
|   2007 |              66 |               65 |                130 |              50.77 |                  50 |
|   2008 |              67 |               61 |                129 |              51.94 |               47.29 |
|   2009 |              68 |               62 |                130 |              52.31 |               47.69 |
|   2010 |              71 |               65 |                136 |              52.21 |               47.79 |
|   2011 |              69 |               60 |                129 |              53.49 |               46.51 |
|   2012 |              67 |               54 |                122 |              54.92 |               44.26 |
|   2013 |              70 |               57 |                128 |              54.69 |               44.53 |
|   2014 |              65 |               55 |                120 |              54.17 |               45.83 |
|   2015 |              61 |               57 |                118 |              51.69 |               48.31 |
|   2016 |              66 |               57 |                123 |              53.66 |               46.34 |
|   2017 |              63 |               54 |                118 |              53.39 |               45.76 |
|   2018 |              59 |               51 |                111 |              53.15 |               45.95 |

---

## Top / Bottom Bin Share Trend

**Yearly bin share breakdown (besttrend cohort)**

|   Year |     N |   Top share % (B8-B10) |   Mid share % (B4-B7) |   Bottom share % (B1-B3) |
|-------:|------:|-----------------------:|----------------------:|-------------------------:|
|   2006 |  3698 |                   33.4 |                 39.26 |                    26.72 |
|   2007 |  3690 |                  33.69 |                  38.7 |                    26.94 |
|   2008 |  4965 |                  34.46 |                 40.06 |                    25.12 |
|   2009 |  7461 |                  31.98 |                 41.27 |                    26.44 |
|   2010 |  8551 |                  38.05 |                  39.6 |                    22.09 |
|   2011 |  8701 |                  31.98 |                 43.08 |                    24.34 |
|   2012 |  9113 |                  35.44 |                 34.86 |                    26.83 |
|   2013 |  9148 |                  40.48 |                 29.55 |                     25.6 |
|   2014 | 10455 |                  37.91 |                 32.19 |                    25.71 |
|   2015 | 10326 |                  32.54 |                 34.06 |                    27.73 |
|   2016 | 12480 |                  28.11 |                 38.29 |                    30.88 |
|   2017 | 23948 |                  25.54 |                 38.91 |                    34.15 |
|   2018 | 22333 |                   24.9 |                 37.81 |                    35.05 |

**Overall bin shares (full besttrend cohort)**

- Top-bin share (B8-B10): 31.18%
- Mid-bin share (B4-B7): 37.36%
- Bottom-bin share (B1-B3): 29.22%

---

## Executive Summary Indicators (Table 1)

| Indicator                |   Value |
|:-------------------------|--------:|
| Median Total Raw Score   |     122 |
| Median Part I Raw Score  |      65 |
| Median Part II Raw Score |      57 |
| Median Percentile Rank   |      50 |
| Top-bin share (B8-B10)   |   31.18 |
| Bottom-bin share (B1-B3) |   29.22 |

---

## Supplementary: All-year overview (besttrend cohort)

| Metric | Value |
|--------|------:|
| Total rows (besttrend) | 134,869 |
| Total unique examinees | 134,869 |
| Years covered | 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018 |
| Median total raw score | 122.00 |
| Mean total raw score | 123.15 |
| Std total raw score | 33.39 |
| Median Part I raw score | 65.00 |
| Median Part II raw score | 57.00 |
| Median percentile rank | 50.00 |
| Mean percentile rank | 49.45 |
| Median GPS | 501.00 |
| Median APT | 504.00 |
| Median SA | 498.00 |

### Score Summary by University Type (besttrend)

| UNDERGRAD_UNI_TYPE   |   ('TotalRawScoreTRUE', 'count') |   ('TotalRawScoreTRUE', 'median') |   ('TotalRawScoreTRUE', 'mean') |   ('PartIRawScoreTRUE', 'count') |   ('PartIRawScoreTRUE', 'median') |   ('PartIRawScoreTRUE', 'mean') |   ('PartIIRawScoreTRUE', 'count') |   ('PartIIRawScoreTRUE', 'median') |   ('PartIIRawScoreTRUE', 'mean') |   ('NMS_PER_num', 'count') |   ('NMS_PER_num', 'median') |   ('NMS_PER_num', 'mean') |   ('NMS_GPS', 'count') |   ('NMS_GPS', 'median') |   ('NMS_GPS', 'mean') |   ('NMS_APT', 'count') |   ('NMS_APT', 'median') |   ('NMS_APT', 'mean') |   ('NMS_SA', 'count') |   ('NMS_SA', 'median') |   ('NMS_SA', 'mean') |
|:---------------------|---------------------------------:|----------------------------------:|--------------------------------:|---------------------------------:|----------------------------------:|--------------------------------:|----------------------------------:|-----------------------------------:|---------------------------------:|---------------------------:|----------------------------:|--------------------------:|-----------------------:|------------------------:|----------------------:|-----------------------:|------------------------:|----------------------:|----------------------:|-----------------------:|---------------------:|
| Foreign              |                             1887 |                               124 |                          125.06 |                             1887 |                                65 |                           65.07 |                              1887 |                                 58 |                            59.99 |                       1880 |                          51 |                     49.88 |                   1892 |                     504 |                498.66 |                   1892 |                     503 |                499.41 |                  1892 |                    503 |               501.13 |
| Not Specified        |                             1392 |                               119 |                           120.4 |                             1392 |                                64 |                           63.71 |                              1392 |                                 55 |                            56.69 |                       1380 |                          47 |                      47.8 |                   1392 |                     494 |                491.72 |                   1392 |                     497 |                493.01 |                  1392 |                    497 |               492.38 |
| Private              |                           103635 |                               121 |                          121.61 |                           103635 |                                65 |                           64.35 |                            103635 |                                 56 |                            57.26 |                     102848 |                          48 |                     48.28 |                 103669 |                     497 |                493.82 |                 103669 |                     500 |                 497.3 |                103669 |                    493 |               492.23 |
| Public               |                            27912 |                               127 |                          128.86 |                            27912 |                                67 |                           67.31 |                             27912 |                                 60 |                            61.55 |                      27585 |                          56 |                     53.85 |                  27916 |                     518 |                515.58 |                  27916 |                     517 |                515.54 |                 27916 |                    516 |               515.29 |

### Score Summary by Course Group (besttrend)

| UNDERGRAD_COURSE_GROUP       |   ('TotalRawScoreTRUE', 'count') |   ('TotalRawScoreTRUE', 'median') |   ('TotalRawScoreTRUE', 'mean') |   ('PartIRawScoreTRUE', 'count') |   ('PartIRawScoreTRUE', 'median') |   ('PartIRawScoreTRUE', 'mean') |   ('PartIIRawScoreTRUE', 'count') |   ('PartIIRawScoreTRUE', 'median') |   ('PartIIRawScoreTRUE', 'mean') |   ('NMS_PER_num', 'count') |   ('NMS_PER_num', 'median') |   ('NMS_PER_num', 'mean') |   ('NMS_GPS', 'count') |   ('NMS_GPS', 'median') |   ('NMS_GPS', 'mean') |   ('NMS_APT', 'count') |   ('NMS_APT', 'median') |   ('NMS_APT', 'mean') |   ('NMS_SA', 'count') |   ('NMS_SA', 'median') |   ('NMS_SA', 'mean') |
|:-----------------------------|---------------------------------:|----------------------------------:|--------------------------------:|---------------------------------:|----------------------------------:|--------------------------------:|----------------------------------:|-----------------------------------:|---------------------------------:|---------------------------:|----------------------------:|--------------------------:|-----------------------:|------------------------:|----------------------:|-----------------------:|------------------------:|----------------------:|----------------------:|-----------------------:|---------------------:|
| Education                    |                             3476 |                               132 |                          132.51 |                             3476 |                                68 |                           68.31 |                              3476 |                                 63 |                            64.19 |                       3461 |                          52 |                     51.95 |                   3479 |                     507 |                508.29 |                   3479 |                     509 |                 511.7 |                  3479 |                    499 |               506.31 |
| Engineering & Technology     |                              751 |                               141 |                          139.38 |                              751 |                                75 |                           73.97 |                               751 |                                 66 |                            65.41 |                        731 |                          72 |                     64.09 |                    751 |                     562 |                556.53 |                    751 |                     567 |                559.01 |                   751 |                    550 |               540.55 |
| Medical & Allied             |                            64268 |                               121 |                          122.41 |                            64268 |                                65 |                           65.65 |                             64268 |                                 55 |                            56.76 |                      63834 |                          49 |                     48.97 |                  64287 |                     498 |                497.82 |                  64287 |                     508 |                505.64 |                 64287 |                    491 |               491.98 |
| Natural Sciences             |                            41503 |                               124 |                          125.09 |                            41503 |                                65 |                           64.93 |                             41503 |                                 59 |                            60.16 |                      40961 |                          54 |                     51.77 |                  41514 |                     513 |                506.65 |                  41514 |                     508 |                502.33 |                 41514 |                    516 |               509.16 |
| Other                        |                             8337 |                               131 |                          130.72 |                             8337 |                                68 |                           67.86 |                              8337 |                                 62 |                            62.86 |                       8306 |                          54 |                     52.38 |                   8346 |                     510 |                507.71 |                   8346 |                     515 |                510.71 |                  8346 |                    504 |               505.35 |
| Social & Behavioral Sciences |                            16491 |                               113 |                           114.6 |                            16491 |                                59 |                           59.84 |                             16491 |                                 53 |                            54.76 |                      16400 |                          40 |                     42.87 |                  16492 |                     476 |                470.21 |                  16492 |                     472 |                470.27 |                 16492 |                    483 |               478.89 |
