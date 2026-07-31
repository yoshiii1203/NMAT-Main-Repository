# NMAT Analysis — Complete Data Extraction Report

**Generated:** 2026-07-31 16:32

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Total pages:** 13

---

## Overview — Key Metrics at a Glance

| Metric | Value |
|--------|-------|
| Best-record examinees | 134,869 |
| Years covered | 13 |
| Median TRUE raw score | 122.0 |
| Median percentile rank | 50.0 |
| Unique examinees | 134,869 |
| Repeat takers | 33,713 |
| Observable cohort | 69,503 |
| Confirmed PLE share | 45.44% |
| Filipino (citizenship) | 32320 |
| Verified Foreigner | 5049 |
| Likely Foreigner | 12 |

---

## Table of Contents

- [01. Executive Summary](#01-executive-summary)
- [02. Data Integrity](#02-data-integrity)
- [03. Trends & Stability](#03-trends-and-stability)
- [04. Score Bins & Citizenship](#04-score-bins-and-citizenship)
- [05. University Type Analysis](#05-university-type-analysis)
- [06. Flow & Pathways](#06-flow-and-pathways)
- [07. PLE Alignment](#07-ple-alignment)
- [08. Repeat Takers](#08-repeat-takers)
- [09. Subtests & Profiles](#09-subtests-and-profiles)
- [10. Year Gap & Gender](#10-year-gap-and-gender)
- [11. Statistical Tests](#11-statistical-tests)
- [12. Policy Tables & Export](#12-policy-tables-and-export)
- [13. CHED Compliance](#13-ched-compliance)

---



<a id="01-executive-summary"></a>

**Generated:** 2026-07-31 16:31

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

---



<a id="02-data-integrity"></a>

**Generated:** 2026-07-31 16:31

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `all` (full unfiltered dataset) and derived analytic subsets

**Filters:** None (full unfiltered dataset)

---

## Metric Cards

| Metric | Value |
|--------|------:|
| All NMAT rows | 178,927 |
| Best-record rows | 134,869 |
| Rows with TRUE raw scores | 178,882 |
| Observable best-record rows | 69,503 |

---

## Table 2: Analysis Cohorts Used in the Dashboard

Each row defines one analytic subset used in later pages. Counts are rows, not necessarily unique persons.

| Analytic subset                               |   Row count | Interpretation                                |   Share of all (%) |
|:----------------------------------------------|------------:|:----------------------------------------------|-------------------:|
| All cleaned NMAT rows                         |      178927 | All cleaned NMAT rows                         |                100 |
| One best NMAT record per person               |      134869 | One best NMAT record per person               |              75.38 |
| Best-record rows within 2006-2018             |      134869 | Best-record rows within 2006-2018             |              75.38 |
| Best-record rows in the observable PLE window |       69503 | Best-record rows in the observable PLE window |              38.84 |
| Confirmed PLE-matched NMAT rows               |       49086 | Confirmed PLE-matched NMAT rows               |              27.43 |
| Confirmed PLE-matched best-record persons     |       37365 | Confirmed PLE-matched best-record persons     |              20.88 |

---

## Table 3: TRUE Raw-Score Validation Checks

These checks confirm whether TRUE total raw score is internally consistent with its Part I and Part II components.

| Validation check                              |   Count of rows |   Share of total rows (%) |
|:----------------------------------------------|----------------:|--------------------------:|
| Rows with complete Total + Part I + Part II   |          178882 |                   99.9749 |
| Formula mismatches: Total != Part I + Part II |               0 |                         0 |
| Stored-vs-derived mismatch flag count         |           56065 |                    31.334 |
| Calc-vs-derived mismatch flag count           |               0 |                         0 |

**Stored-total mismatch, correctly denominated:** 56,065 of 99,316 rows that have a stored total (`StoredRawTotal` notna) = **56.45%**. (The table above expresses the same numerator, 56,065, as a share of ALL 178,927 rows = 31.33% — a different, smaller-looking denominator. Neither is "42.2%"; that figure is retired.)

### StoredVsDerivedMismatch detailed distribution

| Value   |   Count |
|:--------|--------:|
| <NA>    |   79611 |
| True    |   56065 |
| False   |   43251 |

### CalcVsDerivedMismatch detailed distribution

Column not present.

---

## Table 4: Post-Cleaning UNDERGRAD_UNI_TYPE Consistency by Source College

Each row summarizes how one normalized source college name maps to the cleaned UNDERGRAD_UNI_TYPE field. Any college with more than one mapped type should be reviewed.

NMA_College column not available in the dataset.

---

## Table 5: UNDERGRAD_UNIVERSITY to UNDERGRAD_UNI_TYPE and UNDERGRAD_UNI_LOCATION Pairing Audit

This table checks whether each standardized university name maps consistently to one university type and one location.

**Universities checked:** 2,907

**University pairing conflicts:** 0

### University type distribution across all universities

|   Num UNI_TYPEs |   Universities |
|----------------:|---------------:|
|               1 |           2907 |

---

## Core Distributions (Tables 6-8)

Values are row counts under the current filters (full unfiltered dataset).

### Table 6: Distribution of University Type (all rows)

| UNDERGRAD_UNI_TYPE   |   Count |   Share (%) |
|:---------------------|--------:|------------:|
| Private              |  137476 |       76.83 |
| Public               |   37304 |       20.85 |
| Foreign              |    2315 |        1.29 |
| Not Specified        |    1832 |        1.02 |

### Table 7: Distribution of Course Group (all rows)

| UNDERGRAD_COURSE_GROUP       |   Count |   Share (%) |
|:-----------------------------|--------:|------------:|
| Medical & Allied             |   86140 |       48.14 |
| Natural Sciences             |   55900 |       31.24 |
| Social & Behavioral Sciences |   22022 |       12.31 |
| Other                        |    9855 |        5.51 |
| Education                    |    4162 |        2.33 |
| Engineering & Technology     |     848 |        0.47 |

### Table 8: Distribution of PLE Status Label (all rows)

| PLE_STATUS_LABEL       |   Count |   Share (%) |
|:-----------------------|--------:|------------:|
| No confirmed PLE match |  129841 |       72.57 |
| Confirmed PLE passer   |   49086 |       27.43 |

### Table 9: Distribution of PLE Match Outcome (all rows)

`accepted` rows are counted in IS_PLE_PASSER. `rejected_ambiguous_person` and `rejected` are candidate matches that existed but were NOT counted — the person-key resolved to more than one plausible match and was discarded rather than guessed. `no_match` means no candidate was found at all.

| PLE_MATCH_OUTCOME         |   Count |   Share (%) |
|:--------------------------|--------:|------------:|
| no_match                  |  121623 |       67.97 |
| accepted                  |   49086 |       27.43 |
| rejected_ambiguous_person |    8216 |        4.59 |
| rejected                  |       2 |           0 |

### Table 10: Distribution of PLE Year Uncertainty (all rows)

| PLE_YEAR_UNCERTAIN   |   Count |   Share (%) |
|:---------------------|--------:|------------:|
| False                |  178817 |       99.94 |
| True                 |     110 |        0.06 |

---

## Additional Integrity Checks

### Year Distribution (all rows)

|   Year |   Count |   Share (%) |
|-------:|--------:|------------:|
|   2006 |    4376 |        2.45 |
|   2007 |    4656 |         2.6 |
|   2008 |    6120 |        3.42 |
|   2009 |    8362 |        4.67 |
|   2010 |   10560 |         5.9 |
|   2011 |   11929 |        6.67 |
|   2012 |   13320 |        7.44 |
|   2013 |   13988 |        7.82 |
|   2014 |   14833 |        8.29 |
|   2015 |   16284 |         9.1 |
|   2016 |   20968 |       11.72 |
|   2017 |   25870 |       14.46 |
|   2018 |   27661 |       15.46 |

### HasTRUErawScores Flag Distribution

| HasTRUErawScores   |   Count |
|:-------------------|--------:|
| TRUE               |  178882 |
| FALSE              |      45 |

### Person-Level Duplicate Check

- Total unique PERSON_KEYs: 134,869
- Persons with 1 record: 101,156
- Persons with 2 records: 25,812
- Persons with 3+ records: 7,901
- Max records for one person: 9

### IS_PLE_PASSER Distribution

| IS_PLE_PASSER   |   Count |   Share (%) |
|:----------------|--------:|------------:|
| False           |  129841 |       72.57 |
| True            |   49086 |       27.43 |

---



<a id="03-trends-and-stability"></a>

**Generated:** 2026-07-31 16:31

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `besttrend` (IS_BEST_NMAT_RECORD & Year 2006-2018)

**Filters:** None (full unfiltered dataset)

---

## 1. Annual Score Trends

Yearly summary with n, median_raw, q25_raw, q75_raw, median_pct, q25_pct, q75_pct, median_gps, median_apt, median_sa.

**Table: Annual Score Trends (yearly_summary)**

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


## 2. Box Plot Data (Yearly Distribution Stats)

**Box plot data: Total Raw Score (TotalRawScoreTRUE) by Year**

|   Year |     n |   mean |   std |   min |   q25 |   median |   q75 |   max |
|-------:|------:|-------:|------:|------:|------:|---------:|------:|------:|
|   2006 |  3698 | 131.86 | 32.34 |    50 |   108 |      131 |   154 |   220 |
|   2007 |  3690 | 131.45 | 33.38 |    38 |   107 |      130 |   156 |   222 |
|   2008 |  4965 |  129.9 | 32.29 |    37 |   107 |      129 |   153 |   223 |
|   2009 |  7445 | 131.22 | 30.68 |    48 |   109 |      130 |   152 |   223 |
|   2010 |  8548 | 137.21 |  30.9 |    44 |   115 |      136 |   159 |   231 |
|   2011 |  8692 | 130.99 | 30.38 |    46 |   109 |      129 |   151 |   222 |
|   2012 |  9102 | 123.97 |  31.5 |    43 |   101 |      122 |   145 |   223 |
|   2013 |  9144 | 129.24 | 35.35 |    10 |   103 |      128 |   154 |   227 |
|   2014 | 10455 | 119.87 | 31.33 |     9 |    98 |      120 |   142 |   220 |
|   2015 | 10326 |  118.4 | 35.13 |    27 |    93 |      118 |   142 |   222 |
|   2016 | 12480 | 122.87 | 33.82 |    30 |    98 |      123 |   146 |   223 |
|   2017 | 23948 | 118.85 | 34.45 |     7 |    93 |      118 |   143 |   226 |
|   2018 | 22333 | 113.38 | 30.71 |    25 |    91 |      111 |   132 |   230 |


**Box plot data: Percentile Rank (NMS_PER_num) by Year**

|   Year |     n |   mean |   std |   min |   q25 |   median |   q75 |   max |
|-------:|------:|-------:|------:|------:|------:|---------:|------:|------:|
|   2006 |  3678 |  52.23 |  29.1 |    -1 |    27 |       53 |    77 |    99 |
|   2007 |  3671 |  51.95 | 29.09 |    -1 |    27 |       52 |    77 |    99 |
|   2008 |  4958 |  53.04 | 29.37 |    -1 |    28 |       54 |    80 |    99 |
|   2009 |  7445 |  51.81 | 28.63 |    -1 |    27 |       52 |    77 |    99 |
|   2010 |  8539 |  55.97 | 28.53 |    -1 |    32 |       57 |    81 |    99 |
|   2011 |  8654 |  52.27 | 27.67 |    -1 |    30 |       52 |    76 |    99 |
|   2012 |  8926 |  52.78 | 31.15 |    -1 |    26 |       54 |    81 |    99 |
|   2013 |  8898 |  54.87 | 32.71 |    -1 |    24 |       60 |    86 |    99 |
|   2014 | 10277 |  53.14 | 32.35 |    -1 |    24 |       57 |    83 |    99 |
|   2015 | 10141 |  49.49 | 32.16 |    -1 |    19 |       52 |    78 |    99 |
|   2016 | 12428 |  46.73 | 30.14 |    -1 |    19 |       48 |    73 |    99 |
|   2017 | 23872 |   45.2 |  29.1 |    -1 |    19 |       44 |    70 |    99 |
|   2018 | 22206 |  44.24 | 29.87 |    -1 |    17 |       43 |    70 |    99 |


**Box plot data: Part I Raw Score (PartIRawScoreTRUE) by Year**

|   Year |     n |   mean |   std |   min |   q25 |   median |   q75 |   max |
|-------:|------:|-------:|------:|------:|------:|---------:|------:|------:|
|   2006 |  3698 |  67.39 | 16.33 |    21 |    56 |       67 |    79 |   115 |
|   2007 |  3690 |  65.89 | 16.68 |    15 |    54 |       66 |    77 |   115 |
|   2008 |  4965 |  67.32 | 16.71 |    13 |    56 |       67 |    79 |   113 |
|   2009 |  7445 |  67.87 | 15.95 |    12 |    57 |       68 |    79 |   115 |
|   2010 |  8548 |  71.47 | 15.97 |    16 |    60 |       71 |    83 |   118 |
|   2011 |  8692 |  69.55 | 16.06 |    20 |    58 |       69 |    80 |   116 |
|   2012 |  9102 |  67.52 | 16.43 |    19 |    56 |       67 |    79 |   115 |
|   2013 |  9144 |  69.87 | 18.32 |     7 |    57 |       70 |    83 |   117 |
|   2014 | 10455 |  63.92 | 16.71 |     0 |    53 |       65 |    76 |   116 |
|   2015 | 10326 |  60.91 |  18.1 |    12 |    48 |       61 |    73 |   114 |
|   2016 | 12480 |  65.25 | 17.64 |     1 |    53 |       66 |    78 |   115 |
|   2017 | 23948 |  63.18 | 18.55 |     1 |    50 |       63 |    77 |   116 |
|   2018 | 22333 |  59.74 | 16.32 |    12 |    48 |       59 |    71 |   117 |


**Box plot data: Part II Raw Score (PartIIRawScoreTRUE) by Year**

|   Year |     n |   mean |   std |   min |   q25 |   median |   q75 |   max |
|-------:|------:|-------:|------:|------:|------:|---------:|------:|------:|
|   2006 |  3698 |  64.47 |    18 |    25 |    51 |       63 | 77.75 |   112 |
|   2007 |  3690 |  65.55 | 18.77 |     0 |    52 |       65 |    80 |   110 |
|   2008 |  4965 |  62.59 | 17.51 |     0 |    49 |       61 |    75 |   118 |
|   2009 |  7445 |  63.35 | 16.91 |    21 |    51 |       62 |    75 |   113 |
|   2010 |  8548 |  65.74 | 16.98 |    21 |    53 |       65 |    78 |   116 |
|   2011 |  8692 |  61.44 | 16.28 |    19 |    49 |       60 |    72 |   112 |
|   2012 |  9102 |  56.45 | 17.26 |    14 |    43 |       54 |    68 |   113 |
|   2013 |  9144 |  59.37 | 19.18 |     1 |    45 |       57 |    73 |   115 |
|   2014 | 10455 |  55.95 | 16.96 |     4 |    43 |       55 |    68 |   109 |
|   2015 | 10326 |  57.48 | 19.88 |     2 |    42 |       57 |    71 |   116 |
|   2016 | 12480 |  57.62 | 18.29 |     0 |    43 |       57 |    70 |   115 |
|   2017 | 23948 |  55.67 | 17.97 |     0 |    42 |       54 |    68 |   117 |
|   2018 | 22333 |  53.63 | 16.82 |     6 |    41 |       51 |    64 |   114 |


## 3. Kruskal-Wallis Tests for Year-to-Year Score Differences

Tests whether score distributions differ significantly across NMAT years. Eta-squared included as effect-size indicator.

**Table: Kruskal-Wallis Tests**

| Score Variable     |   H-statistic |   p-value |   Eta-squared | Effect Size   |   Groups compared |   Total N |
|:-------------------|--------------:|----------:|--------------:|:--------------|------------------:|----------:|
| Total Raw Score    |       6028.28 |         0 |        0.0446 | Small         |                13 |    134826 |
| Part I Raw Score   |       5766.34 |         0 |        0.0427 | Small         |                13 |    134826 |
| Part II Raw Score  |       5968.69 |         0 |        0.0442 | Small         |                13 |    134826 |
| Percentile Rank    |       2432.24 |         0 |        0.0181 | Small         |                13 |    133693 |
| GPS Standard Score |       2592.55 |         0 |        0.0191 | Small         |                13 |    134869 |


## 4. IQR Ranges by Year

**Table: IQR Ranges by Year (raw score and percentile rank)**

|   Year |     n |   median_raw |   q25_raw |   q75_raw |   iqr_raw |   median_pct |   q25_pct |   q75_pct |   iqr_pct |
|-------:|------:|-------------:|----------:|----------:|----------:|-------------:|----------:|----------:|----------:|
|   2006 |  3698 |          131 |       108 |       154 |        46 |           53 |        27 |        77 |        50 |
|   2007 |  3690 |          130 |       107 |       156 |        49 |           52 |        27 |        77 |        50 |
|   2008 |  4965 |          129 |       107 |       153 |        46 |           54 |        28 |        80 |        52 |
|   2009 |  7461 |          130 |       109 |       152 |        43 |           52 |        27 |        77 |        50 |
|   2010 |  8551 |          136 |       115 |       159 |        44 |           57 |        32 |        81 |        49 |
|   2011 |  8701 |          129 |       109 |       151 |        42 |           52 |        30 |        76 |        46 |
|   2012 |  9113 |          122 |       101 |       145 |        44 |           54 |        26 |        81 |        55 |
|   2013 |  9148 |          128 |       103 |       154 |        51 |           60 |        24 |        86 |        62 |
|   2014 | 10455 |          120 |        98 |       142 |        44 |           57 |        24 |        83 |        59 |
|   2015 | 10326 |          118 |        93 |       142 |        49 |           52 |        19 |        78 |        59 |
|   2016 | 12480 |          123 |        98 |       146 |        48 |           48 |        19 |        73 |        54 |
|   2017 | 23948 |          118 |        93 |       143 |        50 |           44 |        19 |        70 |        51 |
|   2018 | 22333 |          111 |        91 |       132 |        41 |           43 |        17 |        70 |        53 |

---



<a id="04-score-bins-and-citizenship"></a>

**Generated:** 2026-07-31 16:31

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `besttrend`/`uni` for bins; `uniobservable` (no-PLE-match, citizenship notna) for citizenship

**Filters:** None (full unfiltered dataset)

---

## Sub-tab 1: By Year

Use this tab to see whether later cohorts became more concentrated in higher bins, lower bins, or the middle of the distribution.

**Table 10: Count of examinees in each bin by NMAT year**

| PercentileBin   |   2006 |   2007 |   2008 |   2009 |   2010 |   2011 |   2012 |   2013 |   2014 |   2015 |   2016 |   2017 |   2018 |
|:----------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| B10             |    464 |    450 |    703 |    931 |   1327 |    955 |   1503 |   1772 |   1763 |   1363 |   1085 |   1822 |   1947 |
| B9              |    396 |    408 |    540 |    737 |   1019 |    894 |    911 |   1032 |   1170 |   1029 |   1217 |   2089 |   1789 |
| B8              |    375 |    385 |    468 |    718 |    908 |    934 |    816 |    899 |   1030 |    968 |   1206 |   2205 |   1824 |
| B7              |    357 |    361 |    495 |    755 |    829 |    847 |    785 |    753 |    974 |   1026 |   1160 |   2200 |   1817 |
| B6              |    372 |    301 |    519 |    802 |    917 |    897 |    741 |    632 |    839 |    900 |   1310 |   2408 |   2141 |
| B5              |    369 |    369 |    499 |    717 |    891 |   1037 |    874 |    708 |    821 |    894 |   1268 |   2059 |   2152 |
| B4              |    354 |    397 |    476 |    805 |    749 |    967 |    777 |    610 |    731 |    697 |   1041 |   2650 |   2335 |
| B3              |    343 |    355 |    394 |    729 |    731 |    801 |    705 |    562 |    686 |    720 |    971 |   2331 |   2109 |
| B2              |    325 |    315 |    417 |    655 |    633 |    751 |    772 |    694 |    710 |    724 |   1160 |   2766 |   2466 |
| B1              |    320 |    324 |    436 |    589 |    525 |    566 |    968 |   1086 |   1292 |   1419 |   1723 |   3082 |   3253 |


**Percentage of examinees in each bin by NMAT year (row %)**

|   Year |    B1 |    B2 |   B3 |    B4 |    B5 |    B6 |    B7 |    B8 |    B9 |   B10 |
|-------:|------:|------:|-----:|------:|------:|------:|------:|------:|------:|------:|
|   2006 |  8.71 |  8.84 | 9.33 |  9.63 | 10.04 | 10.12 |  9.71 |  10.2 | 10.78 | 12.63 |
|   2007 |  8.84 |  8.59 | 9.69 | 10.83 | 10.07 |  8.21 |  9.85 |  10.5 | 11.13 | 12.28 |
|   2008 |  8.81 |  8.43 | 7.96 |  9.62 | 10.09 | 10.49 | 10.01 |  9.46 | 10.92 | 14.21 |
|   2009 |  7.92 |  8.81 |  9.8 | 10.82 |  9.64 | 10.78 | 10.15 |  9.65 |  9.91 | 12.52 |
|   2010 |  6.16 |  7.42 | 8.57 |  8.78 | 10.45 | 10.75 |  9.72 | 10.65 | 11.95 | 15.56 |
|   2011 |  6.54 |  8.68 | 9.26 | 11.18 | 11.99 | 10.37 |  9.79 |  10.8 | 10.34 | 11.04 |
|   2012 | 10.94 |  8.72 | 7.96 |  8.78 |  9.87 |  8.37 |  8.87 |  9.22 | 10.29 | 16.98 |
|   2013 | 12.41 |  7.93 | 6.42 |  6.97 |  8.09 |  7.22 |  8.61 | 10.28 |  11.8 | 20.26 |
|   2014 |  12.9 |  7.09 | 6.85 |   7.3 |   8.2 |  8.38 |  9.72 | 10.28 | 11.68 |  17.6 |
|   2015 | 14.57 |  7.43 | 7.39 |  7.16 |  9.18 |  9.24 | 10.53 |  9.94 | 10.56 | 13.99 |
|   2016 | 14.19 |  9.55 |    8 |  8.57 | 10.44 | 10.79 |  9.55 |  9.93 | 10.02 |  8.94 |
|   2017 | 13.05 | 11.71 | 9.87 | 11.22 |  8.72 |  10.2 |  9.32 |  9.34 |  8.85 |  7.72 |
|   2018 |  14.9 | 11.29 | 9.66 | 10.69 |  9.86 |  9.81 |  8.32 |  8.35 |  8.19 |  8.92 |


**Heatmap data: Bin Distribution by Year (row %, bins as rows, years as columns)**

| Bin   |   2006 |   2007 |   2008 |   2009 |   2010 |   2011 |   2012 |   2013 |   2014 |   2015 |   2016 |   2017 |   2018 |
|:------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| B10   |  12.63 |  12.28 |  14.21 |  12.52 |  15.56 |  11.04 |  16.98 |  20.26 |   17.6 |  13.99 |   8.94 |   7.72 |   8.92 |
| B9    |  10.78 |  11.13 |  10.92 |   9.91 |  11.95 |  10.34 |  10.29 |   11.8 |  11.68 |  10.56 |  10.02 |   8.85 |   8.19 |
| B8    |   10.2 |   10.5 |   9.46 |   9.65 |  10.65 |   10.8 |   9.22 |  10.28 |  10.28 |   9.94 |   9.93 |   9.34 |   8.35 |
| B7    |   9.71 |   9.85 |  10.01 |  10.15 |   9.72 |   9.79 |   8.87 |   8.61 |   9.72 |  10.53 |   9.55 |   9.32 |   8.32 |
| B6    |  10.12 |   8.21 |  10.49 |  10.78 |  10.75 |  10.37 |   8.37 |   7.22 |   8.38 |   9.24 |  10.79 |   10.2 |   9.81 |
| B5    |  10.04 |  10.07 |  10.09 |   9.64 |  10.45 |  11.99 |   9.87 |   8.09 |    8.2 |   9.18 |  10.44 |   8.72 |   9.86 |
| B4    |   9.63 |  10.83 |   9.62 |  10.82 |   8.78 |  11.18 |   8.78 |   6.97 |    7.3 |   7.16 |   8.57 |  11.22 |  10.69 |
| B3    |   9.33 |   9.69 |   7.96 |    9.8 |   8.57 |   9.26 |   7.96 |   6.42 |   6.85 |   7.39 |      8 |   9.87 |   9.66 |
| B2    |   8.84 |   8.59 |   8.43 |   8.81 |   7.42 |   8.68 |   8.72 |   7.93 |   7.09 |   7.43 |   9.55 |  11.71 |  11.29 |
| B1    |   8.71 |   8.84 |   8.81 |   7.92 |   6.16 |   6.54 |  10.94 |  12.41 |   12.9 |  14.57 |  14.19 |  13.05 |   14.9 |


**Figure 7: Top-bin (B8-B10) vs Bottom-bin (B1-B3) share by Year**

|   Year |   Top_B8_B10_pct |   Bottom_B1_B3_pct |
|-------:|-----------------:|-------------------:|
|   2006 |            33.61 |              26.88 |
|   2007 |            33.91 |              27.12 |
|   2008 |            34.59 |               25.2 |
|   2009 |            32.08 |              26.53 |
|   2010 |            38.16 |              22.15 |
|   2011 |            32.18 |              24.48 |
|   2012 |            36.49 |              27.62 |
|   2013 |            42.34 |              26.76 |
|   2014 |            39.56 |              26.84 |
|   2015 |            34.49 |              29.39 |
|   2016 |            28.89 |              31.74 |
|   2017 |            25.91 |              34.63 |
|   2018 |            25.46 |              35.85 |


---
## Sub-tab 2: University Type

Insight: Compare which university types are overrepresented in higher bins.

**Figure 8: Percentile-bin distribution by university type (row %)**

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private              | 12.04 | 9.69 |    9 | 9.92 | 9.91 | 9.94 | 9.47 | 9.69 |  9.73 | 10.63 |
| Public               | 10.83 | 8.18 | 7.56 | 8.25 | 8.52 | 8.89 |  9.1 | 9.57 |  11.2 |  17.9 |


**Figure 9: Share of examinees in B8-B10 by university type**

| UNDERGRAD_UNI_TYPE   |   Top_B8_B10_pct |
|:---------------------|-----------------:|
| Foreign              |             34.3 |
| Private              |            30.05 |
| Public               |            38.67 |


**Table 11: Chi-square test — UNDERGRAD_UNI_TYPE x PercentileBin**

|    chi2 | p_value   |   degrees_of_freedom |   n_observations |   cramers_v |
|--------:|:----------|---------------------:|-----------------:|------------:|
| 1270.33 | <0.001    |                   18 |           130494 |      0.0698 |


**Observed contingency: UNDERGRAD_UNI_TYPE x PercentileBin**

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |    B4 |    B5 |    B6 |   B7 |   B8 |   B9 |   B10 |
|:---------------------|------:|-----:|-----:|------:|------:|------:|-----:|-----:|-----:|------:|
| Foreign              |   262 |  174 |  140 |   176 |   145 |   164 |  161 |  175 |  197 |   266 |
| Private              | 12205 | 9823 | 9127 | 10061 | 10044 | 10079 | 9602 | 9821 | 9864 | 10774 |
| Public               |  2949 | 2228 | 2058 |  2247 |  2320 |  2421 | 2478 | 2606 | 3051 |  4876 |


**Expected frequencies: UNDERGRAD_UNI_TYPE x PercentileBin**

| UNDERGRAD_UNI_TYPE   |      B1 |      B2 |      B3 |      B4 |      B5 |      B6 |      B7 |      B8 |      B9 |     B10 |
|:---------------------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Foreign              | 219.732 | 174.249 | 161.421 | 177.941 | 178.297 | 180.507 | 174.477 | 179.623 | 186.892 | 226.859 |
| Private              |   11979 |  9499.4 | 8800.06 | 9700.66 | 9720.08 | 9840.53 | 9511.84 | 9792.35 | 10188.6 | 12367.5 |
| Public               | 3217.31 | 2551.35 | 2363.52 |  2605.4 | 2610.62 | 2642.97 | 2554.69 | 2630.03 | 2736.46 | 3321.66 |


---
## Sub-tab 3: Course Group

Insight: Compare bin profiles across pre-med backgrounds.

**Figure 10: Percentile-bin distribution by Course Group (row %)**

| UNDERGRAD_COURSE_GROUP       |    B1 |    B2 |   B3 |    B4 |    B5 |    B6 |   B7 |    B8 |    B9 |   B10 |
|:-----------------------------|------:|------:|-----:|------:|------:|------:|-----:|------:|------:|------:|
| Education                    |  9.09 |  8.88 | 9.26 |  9.67 |  10.6 |  9.11 | 9.72 |  9.61 | 10.45 | 13.61 |
| Engineering & Technology     |  5.21 |  5.89 | 5.89 |  5.62 |  8.63 |  8.77 | 7.53 |    10 | 14.66 | 27.81 |
| Medical & Allied             |    10 |  9.74 | 9.43 | 10.67 | 10.82 | 10.66 | 9.77 |  9.79 |  9.39 |  9.74 |
| Natural Sciences             | 12.29 |  8.52 | 7.54 |  8.34 |  8.35 |  8.79 | 9.44 |  9.98 | 11.04 |  15.7 |
| Other                        |  9.76 |  8.47 | 8.47 |  9.37 |  9.38 |  9.63 | 9.63 | 10.41 | 11.63 | 13.24 |
| Social & Behavioral Sciences | 19.91 | 11.02 | 8.62 |  8.38 |  7.82 |  8.29 | 7.49 |  7.93 |  8.92 | 11.61 |


**Figure 11: Share of examinees in B8-B10 by Course Group**

| UNDERGRAD_COURSE_GROUP       |   Top_B8_B10_pct |
|:-----------------------------|-----------------:|
| Education                    |            33.67 |
| Engineering & Technology     |            52.47 |
| Medical & Allied             |            28.92 |
| Natural Sciences             |            36.72 |
| Other                        |            35.28 |
| Social & Behavioral Sciences |            28.46 |


**Chi-square test — UNDERGRAD_COURSE_GROUP x PercentileBin**

|    chi2 | p_value   |   degrees_of_freedom |   n_observations |   cramers_v |
|--------:|:----------|---------------------:|-----------------:|------------:|
| 3014.18 | <0.001    |                   45 |           131845 |      0.0676 |


**Observed contingency: UNDERGRAD_COURSE_GROUP x PercentileBin**

| UNDERGRAD_COURSE_GROUP       |   B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |   B9 |   B10 |
|:-----------------------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| Education                    |  313 |  306 |  319 |  333 |  365 |  314 |  335 |  331 |  360 |   469 |
| Engineering & Technology     |   38 |   43 |   43 |   41 |   63 |   64 |   55 |   73 |  107 |   203 |
| Medical & Allied             | 6348 | 6179 | 5988 | 6771 | 6865 | 6765 | 6198 | 6213 | 5960 |  6181 |
| Natural Sciences             | 4942 | 3425 | 3029 | 3351 | 3358 | 3535 | 3796 | 4011 | 4439 |  6310 |
| Other                        |  805 |  699 |  699 |  773 |  774 |  794 |  794 |  859 |  959 |  1092 |
| Social & Behavioral Sciences | 3137 | 1736 | 1359 | 1320 | 1233 | 1307 | 1181 | 1249 | 1406 |  1830 |


**Expected frequencies: UNDERGRAD_COURSE_GROUP x PercentileBin**

| UNDERGRAD_COURSE_GROUP       |      B1 |      B2 |      B3 |      B4 |      B5 |      B6 |      B7 |      B8 |      B9 |     B10 |
|:-----------------------------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Education                    | 407.171 | 323.688 | 298.839 |  328.94 | 330.743 | 333.905 |  322.93 | 332.781 | 345.715 | 420.288 |
| Engineering & Technology     |   86.28 | 68.5899 | 63.3244 | 69.7028 | 70.0849 | 70.7548 | 68.4294 | 70.5167 | 73.2575 | 89.0595 |
| Medical & Allied             |  7501.4 | 5963.38 | 5505.58 | 6060.14 | 6093.35 |  6151.6 | 5949.42 |  6130.9 | 6369.18 | 7743.05 |
| Natural Sciences             | 4750.84 | 3776.77 | 3486.83 | 3838.05 | 3859.08 | 3895.97 | 3767.93 | 3882.86 | 4033.78 | 4903.88 |
| Other                        | 974.846 | 774.972 | 715.479 | 787.547 | 791.863 | 799.433 | 773.158 | 796.743 | 827.709 | 1006.25 |
| Social & Behavioral Sciences | 1862.47 |  1480.6 | 1366.94 | 1504.63 | 1512.87 | 1527.33 | 1477.14 |  1522.2 | 1581.36 | 1922.47 |


**Table 12: Percentile summary by Course Group**

| UNDERGRAD_COURSE_GROUP       |     n |   median |   q25 |   q75 |
|:-----------------------------|------:|---------:|------:|------:|
| Education                    |  3461 |       52 |    26 |    78 |
| Engineering & Technology     |   731 |       72 |    41 |    91 |
| Medical & Allied             | 63834 |       49 |    25 |    73 |
| Natural Sciences             | 40961 |       54 |    24 |    81 |
| Other                        |  8306 |       54 |    27 |    79 |
| Social & Behavioral Sciences | 16400 |       40 |    11 |    73 |


---
## Citizenship Section (No-PLE-Match, Observable University Cohort)

Citizenship labels (CITIZENSHIP_FINAL, FOREIGNER_STATUS) are baked into NMAT_Exodus.parquet by Pipeline 4 using a 3-tier hierarchy: REAL_FOREIGNERS.csv ground truth -> pseudo-citizenship inference -> Filipino default.

**P4-01 fix:** this section previously computed over ALL 178,927 rows, reporting 32,501 verified foreigners against the dashboard's own filtered figure. It now reproduces the dashboard's exact filter chain: `uniobservable` (IS_BEST_OBSERVABLE_RECORD, UNDERGRAD_UNI_TYPE in [Public, Private, Foreign]) AND PLE_STATUS_LABEL == 'No confirmed PLE match' AND CITIZENSHIP_FINAL notna.

**population:** uniobservable ∩ no-confirmed-PLE-match ∩ citizenship notna | **n:** 37,381 | **denominator:** rows in `uniobservable` (n=68,622)

### Citizenship Profile — Summary Metrics

**Citizenship profile metrics**

| Metric                         |   Value |
|:-------------------------------|--------:|
| Total records with citizenship |   37381 |
| Verified Foreigners            |    5049 |
| Filipinos                      |   32320 |
| Distinct citizenship labels    |      43 |


### CITIZENSHIP_FINAL Distribution

**CITIZENSHIP_FINAL — counts and percentages**

| CITIZENSHIP_FINAL     |     n |   percent |
|:----------------------|------:|----------:|
| Filipino              | 32320 |     86.46 |
| India                 |  2598 |      6.95 |
| Thailand              |   580 |      1.55 |
| Nepal                 |   418 |      1.12 |
| United States         |   340 |      0.91 |
| Nigeria               |   127 |      0.34 |
| Korea (South)         |   125 |      0.33 |
| Iran                  |   125 |      0.33 |
| Sri Lanka             |   124 |      0.33 |
| Foreign (unspecified) |   107 |      0.29 |
| Malaysia              |    76 |       0.2 |
| Indonesia             |    75 |       0.2 |
| Taiwan                |    65 |      0.17 |
| Somalia               |    38 |       0.1 |
| Canada                |    34 |      0.09 |
| Japan                 |    33 |      0.09 |
| China                 |    32 |      0.09 |
| Pakistan              |    26 |      0.07 |
| Kenya                 |    20 |      0.05 |
| Australia             |    19 |      0.05 |
| United Kingdom        |    18 |      0.05 |
| Sudan                 |    14 |      0.04 |
| Ghana                 |    12 |      0.03 |
| Bangladesh            |     8 |      0.02 |
| Myanmar               |     8 |      0.02 |
| Ethiopia              |     5 |      0.01 |
| Germany               |     4 |      0.01 |
| Jordan                |     4 |      0.01 |
| Vietnam               |     3 |      0.01 |
| Rwanda                |     3 |      0.01 |
| Iraq                  |     3 |      0.01 |
| Kuwait                |     2 |      0.01 |
| Bhutan                |     2 |      0.01 |
| Sweden                |     2 |      0.01 |
| Austria               |     2 |      0.01 |
| New Zealand           |     2 |      0.01 |
| Yemen                 |     1 |         0 |
| Cameroon              |     1 |         0 |
| Lebanon               |     1 |         0 |
| Syria                 |     1 |         0 |
| Italy                 |     1 |         0 |
| Guam                  |     1 |         0 |
| Portugal              |     1 |         0 |


### FOREIGNER_STATUS Distribution

**FOREIGNER_STATUS — counts and percentages**

| FOREIGNER_STATUS   |     n |   percent |
|:-------------------|------:|----------:|
| Filipino           | 32320 |     86.46 |
| Verified Foreigner |  5049 |     13.51 |
| Likely Foreigner   |    12 |      0.03 |


### Foreigners vs Filipinos Comparison

**Foreigners vs Filipinos**

| group     |     n |   percent |
|:----------|------:|----------:|
| Foreigner |  5049 |     13.51 |
| Filipino  | 32320 |     86.49 |


### Top 15 Citizenship Groups by Count

**Top 15 citizenship groups**

| CITIZENSHIP_FINAL     |     n |   percent |
|:----------------------|------:|----------:|
| Canada                |    34 |      0.09 |
| Somalia               |    38 |       0.1 |
| Taiwan                |    65 |      0.17 |
| Indonesia             |    75 |       0.2 |
| Malaysia              |    76 |       0.2 |
| Foreign (unspecified) |   107 |      0.29 |
| Sri Lanka             |   124 |      0.33 |
| Korea (South)         |   125 |      0.33 |
| Iran                  |   125 |      0.33 |
| Nigeria               |   127 |      0.34 |
| United States         |   340 |      0.91 |
| Nepal                 |   418 |      1.12 |
| Thailand              |   580 |      1.55 |
| India                 |  2598 |      6.95 |
| Filipino              | 32320 |     86.46 |


### Bin Composition by Citizenship (Top 15 Groups)

**Bin composition by citizenship (row %)**

| CITIZENSHIP_FINAL     |    B1 |    B2 |    B3 |    B4 |    B5 |    B6 |    B7 |    B8 |    B9 |   B10 |
|:----------------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| Canada                |  6.25 |  6.25 |  6.25 |  6.25 |  6.25 |  12.5 |  6.25 |  12.5 | 18.75 | 18.75 |
| Filipino              |    14 | 12.11 |  11.2 | 11.38 |  9.86 |  8.68 |   8.3 |  8.51 |  7.84 |  8.12 |
| Foreign (unspecified) | 21.36 | 11.65 |   6.8 |  9.71 |  8.74 |  8.74 |  4.85 |   6.8 |  8.74 | 12.62 |
| India                 | 39.49 | 13.63 |  9.87 |  9.44 |  7.73 |  6.03 |  5.29 |  3.84 |  2.58 |   2.1 |
| Indonesia             | 16.22 | 18.92 | 10.81 |  8.11 | 10.81 |  6.76 |  4.05 |  5.41 |  6.76 | 12.16 |
| Iran                  | 46.61 | 14.41 |  6.78 |  6.78 |  5.93 |  5.93 |  4.24 |  2.54 |  3.39 |  3.39 |
| Korea (South)         |  6.45 |  7.26 |  5.65 |  8.87 | 10.48 |  12.9 |  9.68 |  12.1 |  8.06 | 18.55 |
| Malaysia              |  27.4 | 17.81 | 15.07 | 15.07 |  5.48 |  6.85 |  1.37 |  2.74 |  4.11 |  4.11 |
| Nepal                 | 21.17 | 14.36 | 10.22 | 14.11 | 11.44 |  7.06 |  6.81 |  4.62 |  7.54 |  2.68 |
| Nigeria               |  31.2 |  10.4 |  11.2 |   7.2 |   8.8 |     8 |   5.6 |   4.8 |   5.6 |   7.2 |
| Somalia               | 85.71 |  3.57 |  7.14 |     0 |  3.57 |     0 |     0 |     0 |     0 |     0 |
| Sri Lanka             |  8.94 | 11.38 | 10.57 | 13.01 |  12.2 | 13.01 | 10.57 |  8.13 |  7.32 |  4.88 |
| Taiwan                | 29.69 | 14.06 | 10.94 |  4.69 |     0 |  4.69 |  9.38 |  9.38 |  7.81 |  9.38 |
| Thailand              | 36.73 | 16.52 | 13.53 | 10.37 |  6.68 |  4.92 |  4.39 |  3.69 |  1.76 |  1.41 |
| United States         |  7.98 |  4.29 |  3.99 |  6.44 |  5.83 |  7.36 |  7.67 | 12.88 | 18.71 | 24.85 |


### Full Percentile-Bin Heatmap by Citizenship (All Bins B1-B10)

Each row is one citizenship group; each column is one percentile bin. Values are row percentages.

| Bin   |   Canada |   Filipino |   Foreign (unspecified) |   India |   Indonesia |   Iran |   Korea (South) |   Malaysia |   Nepal |   Nigeria |   Somalia |   Sri Lanka |   Taiwan |   Thailand |   United States |
|:------|---------:|-----------:|------------------------:|--------:|------------:|-------:|----------------:|-----------:|--------:|----------:|----------:|------------:|---------:|-----------:|----------------:|
| B10   |    18.75 |       8.12 |                   12.62 |     2.1 |       12.16 |   3.39 |           18.55 |       4.11 |    2.68 |       7.2 |         0 |        4.88 |     9.38 |       1.41 |           24.85 |
| B9    |    18.75 |       7.84 |                    8.74 |    2.58 |        6.76 |   3.39 |            8.06 |       4.11 |    7.54 |       5.6 |         0 |        7.32 |     7.81 |       1.76 |           18.71 |
| B8    |     12.5 |       8.51 |                     6.8 |    3.84 |        5.41 |   2.54 |            12.1 |       2.74 |    4.62 |       4.8 |         0 |        8.13 |     9.38 |       3.69 |           12.88 |
| B7    |     6.25 |        8.3 |                    4.85 |    5.29 |        4.05 |   4.24 |            9.68 |       1.37 |    6.81 |       5.6 |         0 |       10.57 |     9.38 |       4.39 |            7.67 |
| B6    |     12.5 |       8.68 |                    8.74 |    6.03 |        6.76 |   5.93 |            12.9 |       6.85 |    7.06 |         8 |         0 |       13.01 |     4.69 |       4.92 |            7.36 |
| B5    |     6.25 |       9.86 |                    8.74 |    7.73 |       10.81 |   5.93 |           10.48 |       5.48 |   11.44 |       8.8 |      3.57 |        12.2 |        0 |       6.68 |            5.83 |
| B4    |     6.25 |      11.38 |                    9.71 |    9.44 |        8.11 |   6.78 |            8.87 |      15.07 |   14.11 |       7.2 |         0 |       13.01 |     4.69 |      10.37 |            6.44 |
| B3    |     6.25 |       11.2 |                     6.8 |    9.87 |       10.81 |   6.78 |            5.65 |      15.07 |   10.22 |      11.2 |      7.14 |       10.57 |    10.94 |      13.53 |            3.99 |
| B2    |     6.25 |      12.11 |                   11.65 |   13.63 |       18.92 |  14.41 |            7.26 |      17.81 |   14.36 |      10.4 |      3.57 |       11.38 |    14.06 |      16.52 |            4.29 |
| B1    |     6.25 |         14 |                   21.36 |   39.49 |       16.22 |  46.61 |            6.45 |       27.4 |   21.17 |      31.2 |     85.71 |        8.94 |    29.69 |      36.73 |            7.98 |


### Top-Bin Share (B8-B10) by Citizenship

**Top-bin (B8-B10) share by citizenship (n >= 3)**

| CITIZENSHIP_FINAL     |     n |   top_n |   top_dec_pct |
|:----------------------|------:|--------:|--------------:|
| United Kingdom        |    18 |      14 |          77.8 |
| Vietnam               |     3 |       2 |          66.7 |
| United States         |   340 |     184 |          54.1 |
| Australia             |    19 |       9 |          47.4 |
| Canada                |    34 |      16 |          47.1 |
| Korea (South)         |   125 |      48 |          38.4 |
| China                 |    32 |      11 |          34.4 |
| Iraq                  |     3 |       1 |          33.3 |
| Ghana                 |    12 |       4 |          33.3 |
| Foreign (unspecified) |   107 |      29 |          27.1 |
| Taiwan                |    65 |      17 |          26.2 |
| Germany               |     4 |       1 |            25 |
| Filipino              | 32320 |    7829 |          24.2 |
| Indonesia             |    75 |      18 |            24 |
| Sri Lanka             |   124 |      25 |          20.2 |
| Kenya                 |    20 |       4 |            20 |
| Ethiopia              |     5 |       1 |            20 |
| Japan                 |    33 |       6 |          18.2 |
| Nigeria               |   127 |      22 |          17.3 |
| Pakistan              |    26 |       4 |          15.4 |
| Nepal                 |   418 |      61 |          14.6 |
| Malaysia              |    76 |       8 |          10.5 |
| Iran                  |   125 |      11 |           8.8 |
| India                 |  2598 |     195 |           7.5 |
| Thailand              |   580 |      39 |           6.7 |
| Jordan                |     4 |       0 |             0 |
| Bangladesh            |     8 |       0 |             0 |
| Rwanda                |     3 |       0 |             0 |
| Myanmar               |     8 |       0 |             0 |
| Sudan                 |    14 |       0 |             0 |
| Somalia               |    38 |       0 |             0 |


### Percentile Rank by Citizenship (n >= 5)

**Percentile rank statistics by citizenship (n >= 5)**

| CITIZENSHIP_FINAL     |     n |   mean |   std |   min |   q25 |   median |   q75 |   max |
|:----------------------|------:|-------:|------:|------:|------:|---------:|------:|------:|
| Australia             |    17 |  63.06 | 33.85 |    -1 |    41 |       73 |    92 |    99 |
| Bangladesh            |     8 |  31.88 | 23.47 |     2 | 12.25 |     30.5 | 51.25 |    62 |
| Canada                |    32 |  62.72 |  29.8 |     4 | 41.75 |     69.5 | 88.25 |    99 |
| China                 |    31 |   55.1 | 31.02 |     9 |  27.5 |       55 |    86 |    99 |
| Ethiopia              |     5 |   31.2 | 32.35 |     7 |    11 |       23 |    28 |    87 |
| Filipino              | 32177 |  43.94 | 29.11 |    -1 |    18 |       41 |    69 |    99 |
| Foreign (unspecified) |   106 |  42.13 | 33.27 |    -1 | 10.25 |       39 | 74.75 |    98 |
| Ghana                 |    12 |  50.17 | 23.17 |    19 | 31.25 |     44.5 |    77 |    84 |
| India                 |  2597 |  22.91 |  25.7 |    -1 |     2 |       12 |    39 |    99 |
| Indonesia             |    75 |  40.51 | 31.07 |    -1 |  15.5 |       32 |    63 |    99 |
| Iran                  |   125 |  22.45 | 26.91 |    -1 |     1 |       10 |    37 |    96 |
| Japan                 |    33 |  40.64 | 25.05 |     1 |    23 |       41 |    55 |    89 |
| Kenya                 |    20 |   47.3 | 27.37 |     1 | 37.75 |       52 |    56 |    96 |
| Korea (South)         |   124 |  57.44 | 28.26 |     4 |  34.5 |       58 |    81 |    99 |
| Malaysia              |    76 |   27.8 | 26.06 |    -1 |     6 |       24 | 38.25 |    98 |
| Myanmar               |     8 |   8.62 | 15.88 |    -1 |     2 |      3.5 |   5.5 |    47 |
| Nepal                 |   418 |  35.46 | 27.19 |    -1 |    11 |       32 |    55 |    97 |
| Nigeria               |   127 |  34.09 | 29.98 |    -1 |     6 |       26 |  57.5 |    98 |
| Pakistan              |    26 |  30.31 | 31.21 |    -1 |  3.25 |       14 | 61.75 |    92 |
| Somalia               |    38 |   3.92 |  8.95 |    -1 |  -0.5 |        2 |     3 |    48 |
| Sri Lanka             |   124 |  44.99 | 25.66 |    -1 |    24 |     44.5 |    65 |    96 |
| Sudan                 |    14 |   7.64 |  9.95 |    -1 |    -1 |      4.5 |    12 |    26 |
| Taiwan                |    65 |  37.46 | 33.71 |    -1 |     7 |       25 |    70 |    99 |
| Thailand              |   580 |  24.23 | 23.21 |    -1 |     6 |       16 |    36 |    98 |
| United Kingdom        |    18 |  74.56 | 19.81 |    23 |    74 |     79.5 | 85.75 |    97 |
| United States         |   330 |  63.95 | 30.39 |    -1 | 42.25 |       75 |    89 |    99 |


### TRUE Raw Score by Citizenship (n >= 5)

**TRUE raw score statistics by citizenship (n >= 5)**

| CITIZENSHIP_FINAL     |     n |   mean |   std |   min |    q25 |   median |    q75 |   max |
|:----------------------|------:|-------:|------:|------:|-------:|---------:|-------:|------:|
| Australia             |    19 |    142 | 40.86 |    50 |    120 |      150 |  170.5 |   200 |
| Bangladesh            |     8 | 102.38 | 21.84 |    69 |  89.75 |    102.5 | 116.25 |   135 |
| Canada                |    34 | 141.79 | 35.23 |    77 | 117.25 |      144 |    165 |   223 |
| China                 |    32 | 135.78 | 36.07 |    86 |  104.5 |    127.5 | 163.25 |   215 |
| Ethiopia              |     5 |  109.2 | 32.48 |    82 |     89 |      101 |    110 |   164 |
| Filipino              | 32302 | 118.49 | 29.45 |    37 |     97 |      116 |    138 |   223 |
| Foreign (unspecified) |   107 | 118.91 |  38.5 |    56 |   88.5 |      115 |    150 |   200 |
| Ghana                 |    12 | 116.75 | 18.66 |    94 | 103.75 |      110 |    135 |   151 |
| India                 |  2596 |  91.63 | 28.52 |     9 |     69 |       89 |    112 |   216 |
| Indonesia             |    75 | 117.41 | 33.75 |    56 |     94 |      109 |    134 |   198 |
| Iran                  |   125 |  93.74 | 30.74 |    40 |     69 |       88 |    117 |   171 |
| Japan                 |    33 | 112.91 | 25.07 |    65 |    100 |      115 |    128 |   166 |
| Kenya                 |    19 | 117.21 | 29.08 |    57 |    110 |      121 |    130 |   183 |
| Korea (South)         |   125 | 133.79 | 29.29 |    79 |    111 |      131 |    155 |   194 |
| Malaysia              |    76 |  100.7 | 27.18 |    44 |     84 |     99.5 | 117.25 |   174 |
| Myanmar               |     8 |   77.5 | 22.92 |    50 |   68.5 |       73 |  80.75 |   125 |
| Nepal                 |   417 | 109.52 | 28.26 |    47 |     89 |      108 |    125 |   195 |
| Nigeria               |   127 | 104.34 | 28.03 |    59 |   81.5 |      102 |    125 |   178 |
| Pakistan              |    26 | 100.12 | 33.06 |    48 |     73 |       93 |  129.5 |   176 |
| Somalia               |    38 |  69.34 | 14.53 |    43 |  61.25 |       69 |     74 |   114 |
| Sri Lanka             |   124 | 118.07 | 23.34 |    60 | 100.75 |      119 |    134 |   177 |
| Sudan                 |    14 |  76.43 | 18.81 |    48 |     61 |     76.5 |  91.25 |   104 |
| Taiwan                |    62 | 113.84 | 34.14 |    56 |   85.5 |      110 |    139 |   184 |
| Thailand              |   575 |  97.88 | 24.18 |    46 |     80 |       95 |  112.5 |   176 |
| United Kingdom        |    18 | 149.94 | 22.41 |    99 | 140.25 |      151 |    162 |   186 |
| United States         |   336 | 143.89 | 34.04 |    47 |    122 |      149 | 168.25 |   216 |


### Summary by Citizenship

**Summary statistics by citizenship**

| CITIZENSHIP_FINAL     |   n_examinees |   median_percentile_rank |   median_true_raw_score |   top_decile_n |   top_decile_pct |   bottom_decile_n |   bottom_decile_pct |
|:----------------------|--------------:|-------------------------:|------------------------:|---------------:|-----------------:|------------------:|--------------------:|
| Filipino              |         32320 |                       41 |                     116 |           7829 |            24.22 |             11933 |               36.92 |
| India                 |          2598 |                       12 |                      89 |            195 |             7.51 |              1442 |                55.5 |
| Thailand              |           580 |                       16 |                      95 |             39 |             6.72 |               380 |               65.52 |
| Nepal                 |           418 |                       32 |                     108 |             61 |            14.59 |               188 |               44.98 |
| United States         |           340 |                       75 |                     149 |            184 |            54.12 |                53 |               15.59 |
| Nigeria               |           127 |                       26 |                     102 |             22 |            17.32 |                66 |               51.97 |
| Korea (South)         |           125 |                       58 |                     131 |             48 |             38.4 |                24 |                19.2 |
| Iran                  |           125 |                       10 |                      88 |             11 |              8.8 |                80 |                  64 |
| Sri Lanka             |           124 |                     44.5 |                     119 |             25 |            20.16 |                38 |               30.65 |
| Foreign (unspecified) |           107 |                       39 |                     115 |             29 |             27.1 |                41 |               38.32 |
| Malaysia              |            76 |                       24 |                    99.5 |              8 |            10.53 |                44 |               57.89 |
| Indonesia             |            75 |                       32 |                     109 |             18 |               24 |                34 |               45.33 |
| Taiwan                |            65 |                       25 |                     110 |             17 |            26.15 |                35 |               53.85 |
| Somalia               |            38 |                        2 |                      69 |              0 |                0 |                27 |               71.05 |
| Canada                |            34 |                     69.5 |                     144 |             16 |            47.06 |                 6 |               17.65 |
| Japan                 |            33 |                       41 |                     115 |              6 |            18.18 |                11 |               33.33 |
| China                 |            32 |                       55 |                   127.5 |             11 |            34.38 |                 9 |               28.12 |
| Pakistan              |            26 |                       14 |                      93 |              4 |            15.38 |                14 |               53.85 |
| Kenya                 |            20 |                       52 |                     121 |              4 |               20 |                 5 |                  25 |
| Australia             |            19 |                       73 |                     150 |              9 |            47.37 |                 2 |               10.53 |
| United Kingdom        |            18 |                     79.5 |                     151 |             14 |            77.78 |                 1 |                5.56 |
| Sudan                 |            14 |                      4.5 |                    76.5 |              0 |                0 |                 9 |               64.29 |
| Ghana                 |            12 |                     44.5 |                     110 |              4 |            33.33 |                 3 |                  25 |
| Bangladesh            |             8 |                     30.5 |                   102.5 |              0 |                0 |                 4 |                  50 |
| Myanmar               |             8 |                      3.5 |                      73 |              0 |                0 |                 5 |                62.5 |
| Ethiopia              |             5 |                       23 |                     101 |              1 |               20 |                 4 |                  80 |
| Germany               |             4 |                     30.5 |                     105 |              1 |               25 |                 2 |                  50 |
| Jordan                |             4 |                        2 |                    68.5 |              0 |                0 |                 3 |                  75 |
| Vietnam               |             3 |                       89 |                     171 |              2 |            66.67 |                 0 |                   0 |
| Rwanda                |             3 |                       14 |                      91 |              0 |                0 |                 2 |               66.67 |
| Iraq                  |             3 |                        6 |                      82 |              1 |            33.33 |                 2 |               66.67 |
| Austria               |             2 |                       54 |                   132.5 |              1 |               50 |                 0 |                   0 |
| Bhutan                |             2 |                     47.5 |                   122.5 |              1 |               50 |                 1 |                  50 |
| New Zealand           |             2 |                     46.5 |                     113 |              1 |               50 |                 1 |                  50 |
| Sweden                |             2 |                     35.5 |                     118 |              0 |                0 |                 1 |                  50 |
| Kuwait                |             2 |                      2.5 |                    62.5 |              0 |                0 |                 2 |                 100 |
| Syria                 |             1 |                       54 |                     132 |              0 |                0 |                 0 |                   0 |
| Lebanon               |             1 |                       47 |                     124 |              0 |                0 |                 0 |                   0 |
| Italy                 |             1 |                       44 |                     119 |              0 |                0 |                 0 |                   0 |
| Yemen                 |             1 |                       38 |                     114 |              0 |                0 |                 0 |                   0 |
| Portugal              |             1 |                       23 |                      98 |              0 |                0 |                 1 |                 100 |
| Cameroon              |             1 |                        8 |                      87 |              0 |                0 |                 1 |                 100 |
| Guam                  |             1 |                        1 |                      66 |              0 |                0 |                 1 |                 100 |


### Summary by Citizenship and University Type

**By citizenship and university type**

| CITIZENSHIP_FINAL     | UNDERGRAD_UNI_TYPE   |     n |   median_percentile_rank |   median_true_raw_score |
|:----------------------|:---------------------|------:|-------------------------:|------------------------:|
| Australia             | Foreign              |     5 |                       52 |                     130 |
| Australia             | Private              |     8 |                       51 |                     121 |
| Australia             | Public               |     6 |                     94.5 |                   170.5 |
| Austria               | Private              |     2 |                       54 |                   132.5 |
| Bangladesh            | Private              |     7 |                       29 |                     100 |
| Bangladesh            | Public               |     1 |                       61 |                     135 |
| Bhutan                | Private              |     2 |                     47.5 |                   122.5 |
| Cameroon              | Public               |     1 |                        8 |                      87 |
| Canada                | Foreign              |    11 |                       77 |                     152 |
| Canada                | Private              |    17 |                     51.5 |                     121 |
| Canada                | Public               |     6 |                       58 |                   136.5 |
| China                 | Foreign              |     4 |                     64.5 |                   135.5 |
| China                 | Private              |    21 |                       44 |                     121 |
| China                 | Public               |     7 |                       57 |                     117 |
| Ethiopia              | Private              |     4 |                     19.5 |                    99.5 |
| Ethiopia              | Public               |     1 |                       23 |                     101 |
| Filipino              | Foreign              |   418 |                       63 |                     135 |
| Filipino              | Private              | 25341 |                       38 |                     114 |
| Filipino              | Public               |  6561 |                       49 |                     123 |
| Foreign (unspecified) | Foreign              |    25 |                       79 |                     157 |
| Foreign (unspecified) | Private              |    62 |                       20 |                   101.5 |
| Foreign (unspecified) | Public               |    20 |                       63 |                     144 |
| Germany               | Private              |     3 |                        4 |                      76 |
| Germany               | Public               |     1 |                       57 |                     134 |
| Ghana                 | Foreign              |     1 |                       77 |                     135 |
| Ghana                 | Private              |     8 |                     47.5 |                   112.5 |
| Ghana                 | Public               |     3 |                       41 |                     109 |
| Guam                  | Private              |     1 |                        1 |                      66 |
| India                 | Foreign              |    41 |                       12 |                      89 |
| India                 | Private              |  2081 |                       12 |                      89 |
| India                 | Public               |   476 |                        9 |                      87 |
| Indonesia             | Foreign              |    11 |                       15 |                      93 |
| Indonesia             | Private              |    55 |                       36 |                     117 |
| Indonesia             | Public               |     9 |                       46 |                     116 |
| Iran                  | Foreign              |     7 |                       31 |                     113 |
| Iran                  | Private              |    95 |                       11 |                      89 |
| Iran                  | Public               |    23 |                        6 |                      87 |
| Iraq                  | Private              |     3 |                        6 |                      82 |
| Italy                 | Private              |     1 |                       44 |                     119 |
| Japan                 | Foreign              |     4 |                     36.5 |                   114.5 |
| Japan                 | Private              |    20 |                       39 |                     111 |
| Japan                 | Public               |     9 |                       41 |                     117 |
| Jordan                | Private              |     4 |                        2 |                    68.5 |
| Kenya                 | Private              |    15 |                       52 |                   120.5 |
| Kenya                 | Public               |     5 |                       53 |                     130 |
| Korea (South)         | Foreign              |    10 |                     55.5 |                     133 |
| Korea (South)         | Private              |    99 |                       58 |                     129 |
| Korea (South)         | Public               |    16 |                       58 |                   136.5 |
| Kuwait                | Private              |     2 |                      2.5 |                    62.5 |
| Lebanon               | Private              |     1 |                       47 |                     124 |
| Malaysia              | Foreign              |     8 |                     22.5 |                    95.5 |
| Malaysia              | Private              |    58 |                       24 |                   100.5 |
| Malaysia              | Public               |    10 |                       10 |                    86.5 |
| Myanmar               | Foreign              |     1 |                        4 |                      77 |
| Myanmar               | Private              |     4 |                        1 |                      65 |
| Myanmar               | Public               |     3 |                       10 |                      92 |
| Nepal                 | Foreign              |     5 |                       32 |                     104 |
| Nepal                 | Private              |   372 |                       32 |                     109 |
| Nepal                 | Public               |    41 |                       18 |                      94 |
| New Zealand           | Public               |     2 |                     46.5 |                     113 |
| Nigeria               | Foreign              |     5 |                       31 |                     111 |
| Nigeria               | Private              |    95 |                       29 |                     102 |
| Nigeria               | Public               |    27 |                       19 |                      99 |
| Pakistan              | Foreign              |     2 |                     81.5 |                     153 |
| Pakistan              | Private              |    19 |                        8 |                      85 |
| Pakistan              | Public               |     5 |                        6 |                      89 |
| Portugal              | Private              |     1 |                       23 |                      98 |
| Rwanda                | Private              |     3 |                       14 |                      91 |
| Somalia               | Private              |    31 |                        1 |                      69 |
| Somalia               | Public               |     7 |                        3 |                      77 |
| Sri Lanka             | Foreign              |     2 |                       44 |                     114 |
| Sri Lanka             | Private              |   105 |                       42 |                     119 |
| Sri Lanka             | Public               |    17 |                       55 |                     122 |
| Sudan                 | Foreign              |     2 |                     14.5 |                    92.5 |
| Sudan                 | Private              |     8 |                      6.5 |                    83.5 |
| Sudan                 | Public               |     4 |                      0.5 |                    59.5 |
| Sweden                | Public               |     2 |                     35.5 |                     118 |
| Syria                 | Private              |     1 |                       54 |                     132 |
| Taiwan                | Foreign              |    12 |                     41.5 |                     117 |
| Taiwan                | Private              |    41 |                       25 |                     112 |
| Taiwan                | Public               |    12 |                     23.5 |                   102.5 |
| Thailand              | Foreign              |   201 |                       21 |                     101 |
| Thailand              | Private              |   308 |                       15 |                      92 |
| Thailand              | Public               |    71 |                       14 |                      91 |
| United Kingdom        | Foreign              |     1 |                       83 |                     141 |
| United Kingdom        | Private              |    12 |                     76.5 |                   149.5 |
| United Kingdom        | Public               |     5 |                       85 |                     159 |
| United States         | Foreign              |   124 |                       81 |                     158 |
| United States         | Private              |   153 |                       68 |                     139 |
| United States         | Public               |    63 |                       76 |                     143 |
| Vietnam               | Foreign              |     1 |                       93 |                     175 |
| Vietnam               | Public               |     2 |                     62.5 |                   141.5 |
| Yemen                 | Private              |     1 |                       38 |                     114 |


### Summary by Citizenship and Course Group

**By citizenship and course group**

| CITIZENSHIP_FINAL     | UNDERGRAD_COURSE_GROUP       |     n |   median_percentile_rank |   median_true_raw_score |
|:----------------------|:-----------------------------|------:|-------------------------:|------------------------:|
| Australia             | Education                    |     1 |                       52 |                     130 |
| Australia             | Medical & Allied             |     8 |                       73 |                   153.5 |
| Australia             | Natural Sciences             |     4 |                       71 |                   137.5 |
| Australia             | Other                        |     4 |                       84 |                     176 |
| Australia             | Social & Behavioral Sciences |     2 |                       72 |                     147 |
| Austria               | Medical & Allied             |     1 |                       30 |                     111 |
| Austria               | Other                        |     1 |                       78 |                     154 |
| Bangladesh            | Medical & Allied             |     5 |                       32 |                     105 |
| Bangladesh            | Natural Sciences             |     2 |                       45 |                   117.5 |
| Bangladesh            | Social & Behavioral Sciences |     1 |                        7 |                      80 |
| Bhutan                | Natural Sciences             |     2 |                     47.5 |                   122.5 |
| Cameroon              | Social & Behavioral Sciences |     1 |                        8 |                      87 |
| Canada                | Engineering & Technology     |     1 |                       10 |                      86 |
| Canada                | Medical & Allied             |    15 |                       74 |                     143 |
| Canada                | Natural Sciences             |     9 |                       87 |                     166 |
| Canada                | Other                        |     6 |                       84 |                     165 |
| Canada                | Social & Behavioral Sciences |     3 |                       44 |                     117 |
| China                 | Education                    |     4 |                     49.5 |                   127.5 |
| China                 | Medical & Allied             |    18 |                     30.5 |                     110 |
| China                 | Natural Sciences             |     6 |                     94.5 |                   171.5 |
| China                 | Other                        |     2 |                       73 |                   167.5 |
| China                 | Social & Behavioral Sciences |     2 |                       14 |                   154.5 |
| Ethiopia              | Medical & Allied             |     4 |                     25.5 |                   105.5 |
| Ethiopia              | Other                        |     1 |                        7 |                      82 |
| Filipino              | Education                    |  1341 |                       41 |                     123 |
| Filipino              | Engineering & Technology     |   156 |                       64 |                   130.5 |
| Filipino              | Medical & Allied             | 18797 |                       35 |                     111 |
| Filipino              | Natural Sciences             |  6815 |                       54 |                     124 |
| Filipino              | Other                        |  2871 |                       44 |                     123 |
| Filipino              | Social & Behavioral Sciences |  2340 |                       52 |                     123 |
| Foreign (unspecified) | Education                    |     6 |                       57 |                   136.5 |
| Foreign (unspecified) | Engineering & Technology     |     2 |                     63.5 |                     139 |
| Foreign (unspecified) | Medical & Allied             |    41 |                       34 |                     111 |
| Foreign (unspecified) | Natural Sciences             |    37 |                       40 |                     115 |
| Foreign (unspecified) | Other                        |    16 |                       39 |                   125.5 |
| Foreign (unspecified) | Social & Behavioral Sciences |     5 |                       42 |                     131 |
| Germany               | Medical & Allied             |     3 |                       57 |                     134 |
| Germany               | Natural Sciences             |     1 |                        4 |                      76 |
| Ghana                 | Medical & Allied             |     1 |                       77 |                     135 |
| Ghana                 | Natural Sciences             |    11 |                       43 |                     109 |
| Guam                  | Natural Sciences             |     1 |                        1 |                      66 |
| India                 | Education                    |    67 |                     10.5 |                      91 |
| India                 | Engineering & Technology     |     4 |                       10 |                      84 |
| India                 | Medical & Allied             |   335 |                       21 |                     100 |
| India                 | Natural Sciences             |  1545 |                        8 |                      82 |
| India                 | Other                        |   141 |                       24 |                     105 |
| India                 | Social & Behavioral Sciences |   506 |                       21 |                      97 |
| Indonesia             | Education                    |     4 |                     46.5 |                   129.5 |
| Indonesia             | Medical & Allied             |    39 |                       40 |                     113 |
| Indonesia             | Natural Sciences             |    21 |                       30 |                     107 |
| Indonesia             | Other                        |    10 |                       14 |                      95 |
| Indonesia             | Social & Behavioral Sciences |     1 |                       94 |                     181 |
| Iran                  | Education                    |     3 |                        5 |                      86 |
| Iran                  | Medical & Allied             |    21 |                       25 |                     105 |
| Iran                  | Natural Sciences             |    81 |                       10 |                      88 |
| Iran                  | Other                        |    19 |                        2 |                      72 |
| Iran                  | Social & Behavioral Sciences |     1 |                       20 |                     110 |
| Iraq                  | Natural Sciences             |     1 |                       82 |                     140 |
| Iraq                  | Social & Behavioral Sciences |     2 |                        5 |                      80 |
| Italy                 | Other                        |     1 |                       44 |                     119 |
| Japan                 | Education                    |     2 |                     29.5 |                     105 |
| Japan                 | Medical & Allied             |     5 |                       19 |                     100 |
| Japan                 | Natural Sciences             |    11 |                       43 |                     111 |
| Japan                 | Other                        |     7 |                       43 |                     116 |
| Japan                 | Social & Behavioral Sciences |     8 |                       43 |                   119.5 |
| Jordan                | Medical & Allied             |     4 |                        2 |                    68.5 |
| Kenya                 | Medical & Allied             |    12 |                       52 |                   121.5 |
| Kenya                 | Natural Sciences             |     7 |                       53 |                     123 |
| Kenya                 | Other                        |     1 |                        2 |                      72 |
| Korea (South)         | Education                    |     8 |                       30 |                   106.5 |
| Korea (South)         | Engineering & Technology     |     2 |                     65.5 |                   141.5 |
| Korea (South)         | Medical & Allied             |    38 |                       54 |                     129 |
| Korea (South)         | Natural Sciences             |    42 |                       63 |                   125.5 |
| Korea (South)         | Other                        |    27 |                       64 |                     141 |
| Korea (South)         | Social & Behavioral Sciences |     8 |                     75.5 |                   135.5 |
| Kuwait                | Natural Sciences             |     1 |                        1 |                      53 |
| Kuwait                | Other                        |     1 |                        4 |                      72 |
| Lebanon               | Medical & Allied             |     1 |                       47 |                     124 |
| Malaysia              | Medical & Allied             |    20 |                       21 |                      97 |
| Malaysia              | Natural Sciences             |    53 |                       22 |                      99 |
| Malaysia              | Other                        |     3 |                       30 |                     106 |
| Myanmar               | Medical & Allied             |     4 |                        1 |                      65 |
| Myanmar               | Natural Sciences             |     1 |                        3 |                      72 |
| Myanmar               | Other                        |     3 |                       10 |                      92 |
| Nepal                 | Medical & Allied             |    72 |                       33 |                   115.5 |
| Nepal                 | Natural Sciences             |   277 |                       33 |                     107 |
| Nepal                 | Other                        |    68 |                     26.5 |                     105 |
| Nepal                 | Social & Behavioral Sciences |     1 |                        8 |                      84 |
| New Zealand           | Medical & Allied             |     2 |                     46.5 |                     113 |
| Nigeria               | Education                    |     2 |                       30 |                   114.5 |
| Nigeria               | Medical & Allied             |    36 |                     22.5 |                     102 |
| Nigeria               | Natural Sciences             |    79 |                       26 |                     101 |
| Nigeria               | Other                        |     5 |                       40 |                     120 |
| Nigeria               | Social & Behavioral Sciences |     5 |                       21 |                      97 |
| Pakistan              | Education                    |     1 |                       55 |                     133 |
| Pakistan              | Engineering & Technology     |     1 |                        5 |                      73 |
| Pakistan              | Medical & Allied             |    12 |                       37 |                     112 |
| Pakistan              | Natural Sciences             |     8 |                        4 |                    75.5 |
| Pakistan              | Other                        |     4 |                     22.5 |                   108.5 |
| Portugal              | Social & Behavioral Sciences |     1 |                       23 |                      98 |
| Rwanda                | Medical & Allied             |     2 |                       30 |                     107 |
| Rwanda                | Natural Sciences             |     1 |                        4 |                      76 |
| Somalia               | Medical & Allied             |    14 |                      1.5 |                    68.5 |
| Somalia               | Natural Sciences             |    23 |                        2 |                      69 |
| Somalia               | Other                        |     1 |                        1 |                      65 |
| Sri Lanka             | Medical & Allied             |    17 |                       38 |                     115 |
| Sri Lanka             | Natural Sciences             |    90 |                       50 |                     121 |
| Sri Lanka             | Other                        |    16 |                     32.5 |                   114.5 |
| Sri Lanka             | Social & Behavioral Sciences |     1 |                       94 |                     177 |
| Sudan                 | Education                    |     1 |                        7 |                      86 |
| Sudan                 | Medical & Allied             |     5 |                       -1 |                      61 |
| Sudan                 | Natural Sciences             |     3 |                        3 |                      72 |
| Sudan                 | Other                        |     3 |                        9 |                      82 |
| Sudan                 | Social & Behavioral Sciences |     2 |                       16 |                    90.5 |
| Sweden                | Medical & Allied             |     1 |                       45 |                     133 |
| Sweden                | Other                        |     1 |                       26 |                     103 |
| Syria                 | Medical & Allied             |     1 |                       54 |                     132 |
| Taiwan                | Education                    |     9 |                       25 |                     105 |
| Taiwan                | Engineering & Technology     |     1 |                       77 |                     153 |
| Taiwan                | Medical & Allied             |    33 |                       21 |                     109 |
| Taiwan                | Natural Sciences             |     8 |                       14 |                   126.5 |
| Taiwan                | Other                        |    11 |                       29 |                   121.5 |
| Taiwan                | Social & Behavioral Sciences |     3 |                       96 |                     159 |
| Thailand              | Education                    |    27 |                       20 |                     107 |
| Thailand              | Engineering & Technology     |    21 |                       30 |                     109 |
| Thailand              | Medical & Allied             |   365 |                       15 |                      92 |
| Thailand              | Natural Sciences             |    68 |                       27 |                     102 |
| Thailand              | Other                        |    83 |                       20 |                      99 |
| Thailand              | Social & Behavioral Sciences |    16 |                      5.5 |                    80.5 |
| United Kingdom        | Medical & Allied             |     5 |                       85 |                     156 |
| United Kingdom        | Natural Sciences             |     9 |                       83 |                     152 |
| United Kingdom        | Other                        |     1 |                       74 |                     159 |
| United Kingdom        | Social & Behavioral Sciences |     3 |                       62 |                     137 |
| United States         | Education                    |     7 |                       45 |                     128 |
| United States         | Engineering & Technology     |    10 |                       89 |                     172 |
| United States         | Medical & Allied             |    95 |                       51 |                     128 |
| United States         | Natural Sciences             |   120 |                       85 |                     160 |
| United States         | Other                        |    67 |                       76 |                     152 |
| United States         | Social & Behavioral Sciences |    41 |                       73 |                     148 |
| Vietnam               | Natural Sciences             |     1 |                       93 |                     175 |
| Vietnam               | Other                        |     2 |                     62.5 |                   141.5 |
| Yemen                 | Medical & Allied             |     1 |                       38 |                     114 |


### Year Distribution by Citizenship

**Year distribution by citizenship (counts)**

| CITIZENSHIP_FINAL     |   2006 |   2007 |   2008 |   2009 |   2010 |   2011 |   2012 |   2013 |   2014 |
|:----------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| Australia             |      2 |      0 |      0 |      1 |      2 |      3 |      1 |      2 |      8 |
| Austria               |      0 |      0 |      0 |      1 |      0 |      1 |      0 |      0 |      0 |
| Bangladesh            |      0 |      0 |      1 |      1 |      1 |      1 |      0 |      1 |      3 |
| Bhutan                |      0 |      2 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |
| Cameroon              |      0 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| Canada                |      3 |      0 |      3 |      3 |      5 |      4 |      4 |      7 |      5 |
| China                 |      4 |      0 |      3 |      4 |      3 |      2 |      5 |      3 |      8 |
| Ethiopia              |      0 |      0 |      0 |      2 |      2 |      0 |      1 |      0 |      0 |
| Filipino              |   1562 |   1551 |   2048 |   3250 |   3675 |   4412 |   4756 |   4863 |   6203 |
| Foreign (unspecified) |     10 |      7 |     13 |     19 |     13 |      9 |      7 |     17 |     12 |
| Germany               |      1 |      0 |      1 |      0 |      1 |      0 |      1 |      0 |      0 |
| Ghana                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      2 |      9 |
| Guam                  |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |
| India                 |     43 |    187 |    180 |    140 |     89 |     44 |    147 |    337 |   1431 |
| Indonesia             |      5 |     10 |      6 |      4 |     13 |      6 |     11 |     10 |     10 |
| Iran                  |      0 |     19 |     16 |     26 |     29 |     15 |      9 |      7 |      4 |
| Iraq                  |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      3 |
| Italy                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
| Japan                 |      3 |      2 |      4 |      0 |      5 |      2 |      6 |      4 |      7 |
| Jordan                |      0 |      0 |      0 |      0 |      0 |      1 |      0 |      2 |      1 |
| Kenya                 |      0 |      0 |      1 |      2 |      1 |      6 |      4 |      3 |      3 |
| Korea (South)         |     10 |     17 |      9 |     14 |     10 |     12 |     15 |     17 |     21 |
| Kuwait                |      1 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| Lebanon               |      0 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
| Malaysia              |      0 |      0 |      1 |      9 |      5 |     10 |     22 |     14 |     15 |
| Myanmar               |      0 |      0 |      0 |      2 |      0 |      0 |      2 |      2 |      2 |
| Nepal                 |      2 |      2 |      3 |     55 |     47 |     74 |     88 |     73 |     74 |
| New Zealand           |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |      1 |
| Nigeria               |      1 |      3 |      2 |      4 |      9 |     10 |     10 |     21 |     67 |
| Pakistan              |      1 |      0 |      0 |      4 |      5 |      2 |      9 |      3 |      2 |
| Portugal              |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| Rwanda                |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |      1 |
| Somalia               |      0 |      0 |      0 |      0 |      0 |      3 |     15 |      6 |     14 |
| Sri Lanka             |      0 |      1 |      0 |      7 |     12 |     36 |     26 |     22 |     20 |
| Sudan                 |      2 |      2 |      0 |      1 |      0 |      1 |      3 |      1 |      4 |
| Sweden                |      0 |      0 |      1 |      0 |      1 |      0 |      0 |      0 |      0 |
| Syria                 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
| Taiwan                |      7 |     11 |      7 |     10 |      7 |      1 |      6 |      4 |     12 |
| Thailand              |     17 |     24 |     26 |     63 |     56 |    105 |     88 |    102 |     99 |
| United Kingdom        |      0 |      0 |      3 |      0 |      5 |      1 |      4 |      3 |      2 |
| United States         |     19 |     18 |     42 |     54 |     55 |     28 |     51 |     40 |     33 |
| Vietnam               |      0 |      1 |      0 |      2 |      0 |      0 |      0 |      0 |      0 |
| Yemen                 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |


---
## Comparative Analysis: Foreigners vs Filipino Students

Compares (1) actual foreigners (non-Filipino, identified via the profiling CSV), (2) Filipinos whose undergraduate degree was from a foreign/international school, (3) all students whose undergraduate degree was from a public school, and (4) all students whose undergraduate degree was from a private school. Groups 1 and 2 come from the profiling-matched observable university subset (`uniobservable`, no PLE-status filter). Groups 3 and 4 use all observable best-record examinees at those institution types (`bestobservable`). **UNDERGRAD_UNI_TYPE / UNDERGRAD_UNIVERSITY record the examinee's undergraduate (pre-NMAT) school, not the medical school they later attended between the NMAT and the licensure exam** -- no medical-school identifier exists in this dataset, so the linkage-rate differences below cannot be attributed to medical-school quality.

**population:** union of the four comparison groups | **n:** 73,293

"PLE linkage rate %" is the share of each group found in the PLE passer source list (IS_PLE_PASSER) -- it is a LINKAGE rate, not a licensure pass rate, since the source contains passers only and absence does not mean failure.

**Summary: key score indicators by comparison group**

| Group                         |     n |   median_percentile_rank |   q25_pct |   q75_pct |   median_raw_score |   PLE linkage rate % |
|:------------------------------|------:|-------------------------:|----------:|----------:|-------------------:|---------------------:|
| Filipinos (foreign undergrad) |   643 |                       66 |        35 |        86 |                137 |                35.89 |
| Filipinos (private undergrad) | 52317 |                       50 |        25 |        76 |                123 |                44.98 |
| Filipinos (public undergrad)  | 14410 |                       66 |        35 |        90 |                137 |                49.35 |
| Foreigners (non-Filipino)     |  5159 |                       23 |         4 |        53 |                100 |                 2.49 |


**Percentile rank distribution by group (five-number summary; underlies the dashboard boxplot)**

| Group                         |   min |   q1 |   median |   q3 |   max |     n |   outliers |
|:------------------------------|------:|-----:|---------:|-----:|------:|------:|-----------:|
| Filipinos (foreign undergrad) |    -1 |   35 |       66 |   86 |    99 |   643 |          0 |
| Filipinos (private undergrad) |    -1 |   25 |       50 |   76 |    99 | 52317 |          0 |
| Filipinos (public undergrad)  |    -1 |   35 |       66 |   90 |    99 | 14410 |          0 |
| Foreigners (non-Filipino)     |    -1 |    4 |       23 |   53 |    99 |  5159 |          0 |


**TRUE raw score distribution by group (five-number summary; underlies the dashboard boxplot)**

| Group                         |   min |   q1 |   median |     q3 |   max |     n |   outliers |
|:------------------------------|------:|-----:|---------:|-------:|------:|------:|-----------:|
| Filipinos (foreign undergrad) |    38 |  110 |      137 | 160.25 |   219 |   652 |          0 |
| Filipinos (private undergrad) |    10 |  103 |      123 |    146 |   227 | 52787 |        116 |
| Filipinos (public undergrad)  |     9 |  111 |      137 |    166 |   231 | 14638 |          7 |
| Foreigners (non-Filipino)     |     9 |   77 |      100 |    124 |   223 |  5162 |         35 |


**Bin distribution by comparison group (row %, B1-B10; underlies the dashboard heatmap and stacked bar)**

| Group                         |    B1 |    B2 |   B3 |    B4 |    B5 |   B6 |    B7 |    B8 |    B9 |   B10 |
|:------------------------------|------:|------:|-----:|------:|------:|-----:|------:|------:|------:|------:|
| Filipinos (foreign undergrad) |  8.27 |   6.4 | 6.24 |  7.02 |  5.62 | 9.36 | 11.39 | 11.39 | 13.88 | 20.44 |
| Filipinos (private undergrad) | 10.46 |  9.18 | 9.16 | 10.16 | 10.28 |  9.7 |  9.44 |  9.83 | 10.18 | 11.61 |
| Filipinos (public undergrad)  |  8.18 |  6.56 | 6.18 |  7.29 |  7.56 | 7.68 |  9.04 |  9.86 | 12.34 |  25.3 |
| Foreigners (non-Filipino)     | 30.95 | 12.42 | 9.75 |  9.48 |  8.14 |  6.7 |  5.72 |  5.41 |  5.51 |  5.93 |

---



<a id="05-university-type-analysis"></a>

**Generated:** 2026-07-31 16:31

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `uni`

**Filters:** None (full unfiltered dataset)

---

**Subset:** besttrend filtered to UNDERGRAD_UNI_TYPE in [Public, Private, Foreign]

**Total records:** 130,494

---

## 1. UNDERGRAD_UNI_TYPE Distribution by UNDERGRAD_UNI_LOCATION

### 1a. Institution type by location mix

**Table 05-1. Institution type by location mix**

| UNDERGRAD_UNI_TYPE   | UNDERGRAD_UNI_LOCATION   |   Count |   Percent of Total |
|:---------------------|:-------------------------|--------:|-------------------:|
| Foreign              | International            |    1860 |               1.43 |
| Private              | Local                    |  101400 |               77.7 |
| Public               | Local                    |   27234 |              20.87 |

### 1b. Count matrix with margins

**Table 05-2. UNDERGRAD_UNI_TYPE x UNDERGRAD_UNI_LOCATION count matrix (with totals)**

| UNDERGRAD_UNI_TYPE   |   International |   Local |    All |
|:---------------------|----------------:|--------:|-------:|
| Foreign              |            1860 |       0 |   1860 |
| Private              |               0 |  101400 | 101400 |
| Public               |               0 |   27234 |  27234 |
| All                  |            1860 |  128634 | 130494 |

### 1c. Row percentages (within UNDERGRAD_UNI_TYPE)

**Table 05-3. Row percentages: within UNDERGRAD_UNI_TYPE**

| UNDERGRAD_UNI_TYPE   |   International |   Local |
|:---------------------|----------------:|--------:|
| Foreign              |             100 |       0 |
| Private              |               0 |     100 |
| Public               |               0 |     100 |

### 1d. Column percentages (within UNDERGRAD_UNI_LOCATION)

**Table 05-4. Column percentages: within UNDERGRAD_UNI_LOCATION**

| UNDERGRAD_UNI_TYPE   |   International |   Local |
|:---------------------|----------------:|--------:|
| Foreign              |             100 |       0 |
| Private              |               0 |   78.83 |
| Public               |               0 |   21.17 |

---

## 2. Bin Distribution by UNDERGRAD_UNI_TYPE

### 2a. Bin counts by UNDERGRAD_UNI_TYPE

**Table 05-5. Bin counts by university type**

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |    B4 |    B5 |    B6 |   B7 |   B8 |   B9 |   B10 |   Total |
|:---------------------|------:|-----:|-----:|------:|------:|------:|-----:|-----:|-----:|------:|--------:|
| Foreign              |   262 |  174 |  140 |   176 |   145 |   164 |  161 |  175 |  197 |   266 |    1860 |
| Private              | 12205 | 9823 | 9127 | 10061 | 10044 | 10079 | 9602 | 9821 | 9864 | 10774 |  101400 |
| Public               |  2949 | 2228 | 2058 |  2247 |  2320 |  2421 | 2478 | 2606 | 3051 |  4876 |   27234 |

### 2b. Bin percentages by UNDERGRAD_UNI_TYPE

**Table 05-6. Row percentages (within UNDERGRAD_UNI_TYPE) across percentile bins**

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private              | 12.04 | 9.69 |    9 | 9.92 | 9.91 | 9.94 | 9.47 | 9.69 |  9.73 | 10.63 |
| Public               | 10.83 | 8.18 | 7.56 | 8.25 | 8.52 | 8.89 |  9.1 | 9.57 |  11.2 |  17.9 |

---

## 3. Top Bin Share (B8-B10) by UNDERGRAD_UNI_TYPE

**Table 05-7. Top bin (B8-B10) share by university type**

| UNDERGRAD_UNI_TYPE   |   Total N |   Top Bin (B8-B10) Count |   Top Bin Share (%) |
|:---------------------|----------:|-------------------------:|--------------------:|
| Foreign              |      1860 |                      638 |                34.3 |
| Private              |    101400 |                    30459 |               30.04 |
| Public               |     27234 |                    10533 |               38.68 |

### 3b. Top bin share by UNDERGRAD_UNI_TYPE x UNDERGRAD_UNI_LOCATION

**Table 05-8. Top bin (B8-B10) share by institution type x location**

| UNDERGRAD_UNI_TYPE   | UNDERGRAD_UNI_LOCATION   |   Total N |   Top Bin Count |   Top Bin Share (%) |
|:---------------------|:-------------------------|----------:|----------------:|--------------------:|
| Foreign              | International            |      1860 |             638 |                34.3 |
| Private              | Local                    |    101400 |           30459 |               30.04 |
| Public               | Local                    |     27234 |           10533 |               38.68 |

---

## 4. Foreign Examinee Summary

### 4a. Foreign examinee overview (UNDERGRAD_UNI_TYPE = Foreign)

- **Foreign examinees (besttrend):** 1,860
- **Percent of total (uni subset):** 1.43%
- **Median percentile:** 52.0
- **Top bin share (B8-B10):** 34.30%

### 4b. Foreign examinees by FOREIGNER_STATUS

**Table 05-9. Foreign examinee summary by FOREIGNER_STATUS**

| FOREIGNER_STATUS   |    N |   Median Percentile |   Median Raw Total |   Top Bin (B8-B10) Rate |
|:-------------------|-----:|--------------------:|-------------------:|------------------------:|
| Filipino           | 1134 |                  60 |                130 |                   40.56 |
| Likely Foreigner   |   13 |                  27 |                103 |                   30.77 |
| Verified Foreigner |  713 |                  36 |                114 |                    24.4 |

### 4c. FOREIGNER_STATUS x UNDERGRAD_UNI_TYPE cross-tabulation

**Table 05-10. FOREIGNER_STATUS by UNDERGRAD_UNI_TYPE (all types)**

| UNDERGRAD_UNI_TYPE   | FOREIGNER_STATUS   |     N |   Median Percentile |   Median Raw Total |
|:---------------------|:-------------------|------:|--------------------:|-------------------:|
| Foreign              | Filipino           |  1134 |                  60 |                130 |
| Foreign              | Likely Foreigner   |    13 |                  27 |                103 |
| Foreign              | Verified Foreigner |   713 |                  36 |                114 |
| Private              | Filipino           | 84055 |                  54 |                125 |
| Private              | Verified Foreigner | 17345 |                  24 |                 99 |
| Public               | Filipino           | 23011 |                  63 |                133 |
| Public               | Verified Foreigner |  4223 |                  24 |                 99 |

**Table 05-11. Bin distribution among foreign examinees by FOREIGNER_STATUS**

| FOREIGNER_STATUS   |    B1 |    B2 |    B3 |    B4 |   B5 |   B6 |    B7 |    B8 |    B9 |   B10 |
|:-------------------|------:|------:|------:|------:|-----:|-----:|------:|------:|------:|------:|
| Filipino           |  8.55 |  8.02 |  6.44 |  9.61 | 6.88 | 9.88 | 10.05 | 11.46 | 12.26 | 16.84 |
| Likely Foreigner   | 23.08 | 15.38 | 15.38 | 15.38 |    0 |    0 |     0 | 15.38 |     0 | 15.38 |
| Verified Foreigner | 22.72 | 11.36 |  9.12 |  9.12 |  9.4 | 7.29 |  6.59 |  6.03 |  8.13 | 10.24 |

---

## 5. Descriptive Statistics by UNDERGRAD_UNI_TYPE

**Table 05-12. Descriptive statistics by university type**

| UNDERGRAD_UNI_TYPE   |      N |   Median Percentile |   Mean Percentile |   Std Percentile |   Median Raw Total |   Mean Raw Total |   Std Raw Total |   Median GPS |   Median APT |   Median SA |   Q25 Percentile |   Q75 Percentile |   Q25 Raw Total |   Q75 Raw Total |
|:---------------------|-------:|--------------------:|------------------:|-----------------:|-------------------:|-----------------:|----------------:|-------------:|-------------:|------------:|-----------------:|-----------------:|----------------:|----------------:|
| Public               |  27234 |                  57 |             54.56 |            31.09 |                127 |           128.91 |           34.83 |          518 |          517 |         516 |               27 |               83 |             103 |             154 |
| Private              | 101400 |                  49 |             48.99 |            29.51 |                121 |           121.94 |           30.73 |          498 |          503 |         494 |               23 |               75 |              99 |             143 |
| Foreign              |   1860 |                  52 |             50.43 |            31.38 |                124 |           125.34 |           34.47 |        504.5 |        503.5 |         503 |               21 |               79 |              99 |             150 |

### 5b. Median standard subtest scores by UNDERGRAD_UNI_TYPE

**Table 05-13. Median standard subtest scores by university type**

| Subtest      |   Public (n=27,234) |   Private (n=101,400) |   Foreign (n=1,860) |
|:-------------|--------------------:|----------------------:|--------------------:|
| Verbal       |                 515 |                   500 |                 499 |
| Inductive    |                 529 |                   516 |                 523 |
| Quantitative |                 515 |                   500 |                 512 |
| Perceptual   |                 523 |                   512 |                 500 |
| Biology      |                 515 |                   494 |                 500 |
| Physics      |                 523 |                   500 |                 512 |
| Social       |                 510 |                   500 |                 494 |
| Chemistry    |                 511 |                   494 |                 500 |

### 5c. Median raw subtest scores by UNDERGRAD_UNI_TYPE

**Table 05-14. Median raw subtest scores by university type**

| Subtest      |   Public (n=27,232) |   Private (n=101,368) |   Foreign (n=1,855) |
|:-------------|--------------------:|----------------------:|--------------------:|
| Verbal       |                  16 |                    16 |                  16 |
| Inductive    |                  18 |                    18 |                  18 |
| Quantitative |                  15 |                    14 |                  15 |
| Perceptual   |                  18 |                    17 |                  17 |
| Biology      |                  16 |                    14 |                  15 |
| Physics      |                  14 |                    13 |                  14 |
| Social       |                  16 |                    15 |                  15 |
| Chemistry    |                  15 |                    13 |                  14 |

---

## 6. Kruskal-Wallis Test: UNDERGRAD_UNI_TYPE x NMS_PER_num

### 6a. Omnibus test

**Table 05-15. Kruskal-Wallis test result**

| Score Variable                |   H-statistic |      p-value |   Eta-squared | Effect Size   |   Groups compared |   Total N |
|:------------------------------|--------------:|-------------:|--------------:|:--------------|------------------:|----------:|
| NMS_PER_num (Percentile Rank) |       762.139 | 3.18844e-166 |        0.0058 | Negligible    |                 3 |    130494 |

### 6b. Post-hoc pairwise comparisons (Mann-Whitney U)

**Table 05-16. Post-hoc Mann-Whitney U pairwise comparisons**

| Group 1   | Group 2   |   U-statistic |      p-value |   Effect size (r) |     N1 |     N2 |
|:----------|:----------|--------------:|-------------:|------------------:|-------:|-------:|
| Public    | Private   |   1.53101e+09 | 7.00871e-168 |           -0.1088 |  27234 | 101400 |
| Public    | Foreign   |   2.72905e+07 |   2.1256e-08 |           -0.0775 |  27234 |   1860 |
| Private   | Foreign   |   9.16838e+07 |    0.0398492 |            0.0278 | 101400 |   1860 |

### 6c. Kruskal-Wallis by subtest (standard scores)

**Table 05-17. Kruskal-Wallis tests by subtest (standard scores)**

| Subtest      |   H-statistic |      p-value |   Eta-squared |   Groups |   Total N |
|:-------------|--------------:|-------------:|--------------:|---------:|----------:|
| Verbal       |       243.758 |  1.17144e-53 |        0.0019 |        3 |    130494 |
| Inductive    |       272.773 |  5.86336e-60 |        0.0021 |        3 |    130494 |
| Quantitative |       624.473 | 2.49664e-136 |        0.0048 |        3 |    130494 |
| Perceptual   |       152.684 |  7.00152e-34 |        0.0012 |        3 |    130494 |
| Biology      |       921.439 | 8.16625e-201 |         0.007 |        3 |    130494 |
| Physics      |       802.081 | 6.76683e-175 |        0.0061 |        3 |    130494 |
| Social       |       298.982 |  1.19347e-65 |        0.0023 |        3 |    130494 |
| Chemistry    |       932.624 | 3.04219e-203 |        0.0071 |        3 |    130494 |

---

## 7. Medical & Allied vs Other Courses by UNDERGRAD_UNI_TYPE

Stacked percentages sum to 100% within each university type. Uses 133,477 examinees (does not require a percentile bin — dashboard.py Figure 16).

**Figure 16 data. Medical & Allied vs Other Courses by university type (row %)**

| UNDERGRAD_UNI_TYPE   |   Medical & Allied |   Other Courses |
|:---------------------|-------------------:|----------------:|
| Foreign              |              40.38 |           59.62 |
| Private              |              49.54 |           50.46 |
| Public               |              41.22 |           58.78 |

---

## 8. University Listings by UNDERGRAD_UNI_TYPE

Each row is the standardized university name, cleaned location, and applicant count, over 133,477 examinees (does not require a percentile bin, so this includes applicants dropped from the bin-dependent tables above — dashboard.py Table 17).

### 8.1 Public Universities (215 institutions, 27,916 applicants)

**Table 17 (Public, first 200 of 215)**

| UNDERGRAD_UNIVERSITY                                                                | UNDERGRAD_UNI_LOCATION   |   total_applicants |
|:------------------------------------------------------------------------------------|:-------------------------|-------------------:|
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              | Local                    |               3629 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             | Local                    |               3238 |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           | Local                    |               2458 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       | Local                    |               1386 |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           | Local                    |               1321 |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                | Local                    |               1245 |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    | Local                    |               1238 |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          | Local                    |               1185 |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  | Local                    |               1005 |
| WESTERN MINDANAO STATE UNIVERSITY                                                   | Local                    |                863 |
| BICOL UNIVERSITY - MAIN                                                             | Local                    |                740 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              | Local                    |                693 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             | Local                    |                674 |
| NOT SPECIFIED/UNLISTED                                                              | Local                    |                513 |
| UNIVERSITY OF THE PHILIPPINES - LOS BANOS LAGUNA                                    | Local                    |                487 |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            | Local                    |                363 |
| WEST VISAYAS STATE UNIVERSITY ILOILO                                                | Local                    |                360 |
| CEBU NORMAL UNIVERSITY                                                              | Local                    |                356 |
| MINDANAO STATE UNIVERSITY MARAWI CITY                                               | Local                    |                344 |
| CENTRAL MINDANAO UNIVERSITY                                                         | Local                    |                327 |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              | Local                    |                313 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           | Local                    |                304 |
| PALAWAN STATE UNIVERSITY                                                            | Local                    |                253 |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     | Local                    |                244 |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  | Local                    |                241 |
| MINDANAO STATE UNIVERSITY ILIGAN CITY                                               | Local                    |                203 |
| BULACAN STATE UNIVERSITY - MAIN                                                     | Local                    |                201 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO CITY                                         | Local                    |                195 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS ILOILO                                      | Local                    |                182 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       | Local                    |                171 |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          | Local                    |                158 |
| WESTERN MINDANAO STATE UNIVERSITY ZAMBOANGA CITY                                    | Local                    |                145 |
| BENGUET STATE UNIVERSITY - MAIN                                                     | Local                    |                142 |
| CENTRAL LUZON STATE UNIVERSITY                                                      | Local                    |                140 |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                  | Local                    |                140 |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              | Local                    |                138 |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                              | Local                    |                121 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       | Local                    |                118 |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   | Local                    |                107 |
| CAVITE STATE UNIVERSITY - MAIN                                                      | Local                    |                 72 |
| LEYTE NORMAL UNIVERSITY                                                             | Local                    |                 71 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                               | Local                    |                 63 |
| CATANDUANES STATE COLLEGE - MAIN                                                    | Local                    |                 59 |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                 | Local                    |                 56 |
| UNIVERSITY OF MAKATI                                                                | Local                    |                 56 |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                                          | Local                    |                 53 |
| UNIVERSITY OF THE PHILIPPINES - TACLOBAN                                            | Local                    |                 49 |
| BICOL UNIVERSITY - TABACO                                                           | Local                    |                 48 |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            | Local                    |                 48 |
| UNIVERSITY OF THE PHILIPPINES - CEBU COLLEGE                                        | Local                    |                 46 |
| BICOL UNIVERSITY                                                                    | Local                    |                 46 |
| CENTRAL MINDANAO UNIVERSITY BUKIDNON                                                | Local                    |                 43 |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                             | Local                    |                 40 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS CEBU                                   | Local                    |                 37 |
| VISAYAS STATE UNIVERSITY - MAIN                                                     | Local                    |                 36 |
| BATANGAS STATE UNIVERSITY - MAIN                                                    | Local                    |                 35 |
| MINDANAO STATE UNIVERSITY GENERAL SANTOS CITY                                       | Local                    |                 33 |
| MARIANO MARCOS STATE UNIVERSITY ILOCOS NORTE                                        | Local                    |                 33 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES-DAVAO CITY                                   | Local                    |                 30 |
| CARAGA STATE UNIVERSITY - MAIN                                                      | Local                    |                 29 |
| UNIVERSIDAD DE MANILA                                                               | Local                    |                 29 |
| SULU STATE COLLEGE                                                                  | Local                    |                 27 |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  | Local                    |                 27 |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                         | Local                    |                 27 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA             | Local                    |                 26 |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                               | Local                    |                 24 |
| UNIVERSITY OF SOUTHERN MINDANAO NORTH COTABATO                                      | Local                    |                 24 |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                              | Local                    |                 24 |
| BENGUET STATE UNIVERSITY                                                            | Local                    |                 23 |
| TARLAC STATE UNIVERSITY                                                             | Local                    |                 23 |
| BICOL UNIVERSITY COLLEGE OF SCIENCE LEGAZPI CITY                                    | Local                    |                 22 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - SOUTH LA UNION                       | Local                    |                 19 |
| CENTRAL LUZON STATE UNIVERSITY NUEVA ECIJA                                          | Local                    |                 18 |
| PAMANTASAN NG LUNGSOD NG PASIG                                                      | Local                    |                 18 |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                | Local                    |                 18 |
| SAMAR STATE UNIVERSITY - MAIN                                                       | Local                    |                 18 |
| BICOL UNIVERSITY COLLEGE OF NURSING LEGAZPI CITY                                    | Local                    |                 17 |
| BUKIDNON STATE UNIVERSITY                                                           | Local                    |                 17 |
| BULACAN STATE UNIVERSITY                                                            | Local                    |                 17 |
| UNIVERSITY OF EASTERN PHILIPPINES - SAMAR                                           | Local                    |                 16 |
| GORDON COLLEGE                                                                      | Local                    |                 15 |
| ILOCOS SUR COMMUNITY COLLEGE - BANTAY ILOCOS SUR                                    | Local                    |                 15 |
| PALAWAN STATE UNIVERSITY PUERTO PRINCESA CITY                                       | Local                    |                 15 |
| URDANETA CITY UNIVERSITY                                                            | Local                    |                 14 |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                   | Local                    |                 14 |
| AKLAN STATE UNIVERSITY - MAIN                                                       | Local                    |                 14 |
| BICOL UNIVERSITY - DARAGA                                                           | Local                    |                 13 |
| BICOL UNIVERSITY - POLANGUI                                                         | Local                    |                 12 |
| UNIVERSITY OF THE PHILIPPINES - PAMPANGA                                            | Local                    |                 12 |
| NORTHERN NEGROS STATE COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                      | Local                    |                 11 |
| PHILIPPINE NORMAL COLLEGE TAFT AVENUE MANILA                                        | Local                    |                 11 |
| UNIVERSITY OF THE PHILIPPINES SCH. OF HEALTH SCIENCES -LEYTE                        | Local                    |                 11 |
| MARIANO MARCOS STATE UNIVERSITY - COLLEGE OF EDUCATION - LAOAG CITY                 | Local                    |                 11 |
| CAMARINES NORTE STATE COLLEGE - MAIN                                                | Local                    |                 10 |
| SULTAN KUDARAT STATE UNIVERSITY - TACURONG                                          | Local                    |                 10 |
| SULTAN KUDARAT STATE UNIVERSITY - MAIN                                              | Local                    |                 10 |
| JOSE RIZAL MEMORIAL STATE UNIVERSITY - MAIN                                         | Local                    |                  9 |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - LAGUNA COLLEGE OF ARTS AND TRADES - STA. CRUZ | Local                    |                  9 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                | Local                    |                  9 |
| ISABELA STATE UNIVERSITY - ILAGAN                                                   | Local                    |                  9 |
| UNIVERSITY OF RIZAL SYSTEM - MORONG                                                 | Local                    |                  9 |
| NUEVA ECIJA UNIVERSITY OF SCIENCE AND TECHNOLOGY - MAIN                             | Local                    |                  9 |
| WESTERN VISAYAS COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                            | Local                    |                  9 |
| MINDANAO UNIVERSITY OF SCIENCE AND TECHNOLOGY                                       | Local                    |                  8 |
| U.P. VISAYAS (TACLOBAN CITY LEYTE)                                                  | Local                    |                  8 |
| UNIVERSITY OF NORTHERN PHILIPPINES VIGAN ILOCOS SUR                                 | Local                    |                  8 |
| NAVAL STATE UNIVERSITY - MAIN                                                       | Local                    |                  7 |
| NEGROS ORIENTAL STATE UNIVERSITY                                                    | Local                    |                  7 |
| PAMANTASAN NG LUNGSOD NG PASAY                                                      | Local                    |                  7 |
| CATANDUANES STATE COLLEGE                                                           | Local                    |                  7 |
| EASTERN SAMAR STATE UNIVERSITY - MAIN                                               | Local                    |                  7 |
| LEYTE NORMAL UNIVERSITY TACLOBAN CITY                                               | Local                    |                  6 |
| BATAAN PENINSULA STATE UNIVERSITY                                                   | Local                    |                  6 |
| PHILIPPINE NORMAL UNIVERSITY - AGUSAN                                               | Local                    |                  6 |
| ILOCOS SUR POLYTECHNIC STATE COLLEGE                                                | Local                    |                  6 |
| UNIVERSITY OF CALOOCAN CITY                                                         | Local                    |                  5 |
| UNIVERSITY OF NORTHERN PHILIPPINES-CANDON - CITY OF CANDON ILOCOS SUR               | Local                    |                  5 |
| PAMPANGA AGRICULTURAL COLLEGE                                                       | Local                    |                  5 |
| PAMANTASAN NG LUNGSOD NG MUNTINLUPA                                                 | Local                    |                  5 |
| CAVITE STATE UNIVERSITY CAVITE                                                      | Local                    |                  5 |
| EULOGIO AMANG RODRIGUEZ INSTITUTE OF SCIENCE AND TECHNOLOGY                         | Local                    |                  5 |
| EASTERN VISAYAS STATE UNIVERSITY                                                    | Local                    |                  5 |
| TECHNOLOGICAL UNIVERSITY OF THE PHILIPPINES - AYALA BLVD. MANILA                    | Local                    |                  5 |
| BATANGAS STATE UNIVERSITY BATANGAS CITY                                             | Local                    |                  5 |
| IFUGAO STATE UNIVERSITY - MAIN                                                      | Local                    |                  4 |
| CEBU STATE COLLEGE OF SCIENCE AND TECHNOLOGY-MANDAUE CITY - MANDAUE CITY CEBU       | Local                    |                  4 |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - SAN PABLO CITY                                | Local                    |                  4 |
| UNIVERSITY OF THE PHILIPPINES - OPEN UNIVERSITY                                     | Local                    |                  4 |
| UPM- SCHOOL OF HEALTH SCIENCES PALO LEYTE                                           | Local                    |                  4 |
| PANGASINAN STATE UNIVERSITY                                                         | Local                    |                  4 |
| SURIGAO DEL SUR POLYTECHNIC STATE COLLEGE                                           | Local                    |                  4 |
| NUEVA VIZCAYA STATE UNIVERSITY - BAMBANG                                            | Local                    |                  4 |
| PAMANTASAN NG CABUYAO                                                               | Local                    |                  4 |
| SULTAN KUDARAT POLYTECHNIC STATE COLLEGE                                            | Local                    |                  4 |
| BASILAN STATE COLLEGE                                                               | Local                    |                  3 |
| CAMIGUIN POLYTECHNIC STATE COLLEGE                                                  | Local                    |                  3 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG) - TUGUEGARAO CITY (CAPITAL) CAGAYAN   | Local                    |                  3 |
| ISABELA STATE UNIVERSITY - MAIN                                                     | Local                    |                  3 |
| UNIV. OF SOUTHEASTERN PHIL. BO. OBRERO DAVAO                                        | Local                    |                  3 |
| MINDANAO STATE UNIVERSITY - BUUG COLLEGE                                            | Local                    |                  3 |
| ROMBLON STATE UNIVERSITY - MAIN                                                     | Local                    |                  3 |
| RAMON MAGSAYSAY TECHNOLOGICAL UNIVERSITY - RAMON MAGSAYSAY POLYTECHNIC COLLEGE      | Local                    |                  3 |
| TECHNOLOGICAL UNIVERSITY OF THE PHILIPPINES - VISAYAS                               | Local                    |                  3 |
| PHILIPPINE MILITARY ACADEMY - BAGUIO CITY BENGUET                                   | Local                    |                  3 |
| MINDANAO STATE UNIVERSITY - SULU DEVELOPMENT TECHNICAL COLLEGE                      | Local                    |                  3 |
| MINDANAO STATE UNIVERSITY - NAAWAN                                                  | Local                    |                  3 |
| MARINDUQUE STATE COLLEGE - MAIN                                                     | Local                    |                  3 |
| KALINGA APAYAO STATE COLLEGE KALINGA PROVINCE                                       | Local                    |                  2 |
| JOSEFINA H. CERILLES STATE COLLEGE - PAGADIAN                                       | Local                    |                  2 |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE & TECH.                                     | Local                    |                  2 |
| CITY COLLEGE OF MANILA                                                              | Local                    |                  2 |
| MISAMIS ORIENTAL STATE COLLEGE OF AGRICULTURE AND TECHNOLOGY                        | Local                    |                  2 |
| PHILIPPINE STATE COLLEGE OF AERONAUTICS LAPU-LAPU CITY                              | Local                    |                  2 |
| PARTIDO STATE UNIVERSITY - MAIN                                                     | Local                    |                  2 |
| PAMANTASAN NG LUNGSOD NG VALENZUELA                                                 | Local                    |                  2 |
| VISAYAS UNIVERSITY                                                                  | Local                    |                  2 |
| SURIGAO DEL SUR STATE UNIVERSITY - MAIN                                             | Local                    |                  2 |
| UM DIGOS COLLEGE                                                                    | Local                    |                  2 |
| UNIVERSITY OF RIZAL SYSTEM - MORONG RIZAL                                           | Local                    |                  2 |
| CAPIZ STATE UNIVERSITY - PONTEVEDRA                                                 | Local                    |                  2 |
| CENTRAL BICOL STATE UNIVERSITY OF AGRICULTURE - MAIN                                | Local                    |                  2 |
| CAGAYAN STATE UNIVERSITY - SANCHEZ MIRA                                             | Local                    |                  2 |
| LEYTE STATE UNIVERSITY                                                              | Local                    |                  2 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES - ORIENTAL MINDORO                        | Local                    |                  2 |
| RAMON MAGSAYSAY TECHNOLOGICAL UNIVERSITY                                            | Local                    |                  2 |
| MINDANAO STATE UNIVERSITY - TAWI - TAWI COLLEGE OF TECHNOLOGY AND OCEANOGRAPHY      | Local                    |                  2 |
| NORTH LUZON PHILIPPINES STATE COLLEGE                                               | Local                    |                  2 |
| BULACAN STATE UNIVERSITY - BUSTOS                                                   | Local                    |                  2 |
| CAGAYAN STATE UNIVERSITY - GONZAGA                                                  | Local                    |                  2 |
| BACOLOD CITY COLLEGE                                                                | Local                    |                  1 |
| BAGO CITY COLLEGE                                                                   | Local                    |                  1 |
| BATANGAS STATE UNIVERSITY - ALANGILAN                                               | Local                    |                  1 |
| BATAAN POLYTECHNIC STATE COLLEGE BALANGA CITY                                       | Local                    |                  1 |
| ABRA STATE INSTITUTE OF SCIENCE & TECH. ABRA                                        | Local                    |                  1 |
| AGUSAN DEL SUR STATE COLLEGE OF AGRICULTURE AND TECHNOLOGY                          | Local                    |                  1 |
| COTABATO CITY STATE POLYTECHNIC COLLEGE                                             | Local                    |                  1 |
| BUKIDNON STATE COLLEGE                                                              | Local                    |                  1 |
| CAVITE STATE UNIVERSITY - CARMONA                                                   | Local                    |                  1 |
| CAGAYAN STATE UNIVERSITY - APARRI CAGAYAN                                           | Local                    |                  1 |
| CAGAYAN STATE UNIVERSITY - APARRI                                                   | Local                    |                  1 |
| CAPIZ STATE UNIVERSITY - MAIN                                                       | Local                    |                  1 |
| BATANGAS STATE UNIVERSITY - APOLINARIO R. APACIBLE SCHOOL OF FISHERIES - NASUGBU    | Local                    |                  1 |
| BOHOL ISLAND STATE UNIVERSITY - TAGBILARAN                                          | Local                    |                  1 |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - LOS BAÑOS COLLEGE OF FISHERIES                | Local                    |                  1 |
| KALINGA - APAYAO STATE COLLEGE - MAIN                                               | Local                    |                  1 |
| ISABELA STATE UNIVERSITY - PALANAN                                                  | Local                    |                  1 |
| DAVAO DEL NORTE STATE COLLEGE                                                       | Local                    |                  1 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - MID LA UNION                         | Local                    |                  1 |
| DON HONORIO VENTURA TECHNOLOGICAL STATE UNIVERSITY - MAIN                           | Local                    |                  1 |
| EASTERN SAMAR STATE UNIVERSITY - CAN - AVID                                         | Local                    |                  1 |
| EULOGIO AMANG RODRIGUEZ INSTITUTE OF SCIENCE AND TECHNOLOGY - CAVITE                | Local                    |                  1 |
| PALAWAN STATE UNIVERSITY - SAN RAFAEL PUERTO PRINCESA CITY                          | Local                    |                  1 |
| MINDANAO POLYTECHNIC STATE COLLEGE CAGAYAN DE ORO                                   | Local                    |                  1 |
| MINDANAO STATE UNIVERSITY-SULU                                                      | Local                    |                  1 |
| MSU-SCH. OF MARINE FISHERIES & TECH.- MIS. ORIENTAL                                 | Local                    |                  1 |
| NORTHERN ILOILO POLYTECHNIC STATE COLLEGE - MAIN                                    | Local                    |                  1 |
| NORTHWESTERN MINDANAO STATE COLLEGE OF SCIENCE AND TECHNOLOGY                       | Local                    |                  1 |
| NUEVA VIZCAYA STATE UNIVERSITY BAYOMBONG NUEVA VIZCAYA                              | Local                    |                  1 |
| OCCIDENTAL MINDORO STATE COLLEGE                                                    | Local                    |                  1 |
| RIZAL TECHNOLOGICAL UNIVERSITY - PASIG                                              | Local                    |                  1 |

> Full listing: [05_university_listings_public.csv](05_university_listings_public.csv) (215 rows)

### 8.2 Private Universities (798 institutions, 103,669 applicants)

**Table 17 (Private, first 200 of 798)**

| UNDERGRAD_UNIVERSITY                                                                  | UNDERGRAD_UNI_LOCATION   |   total_applicants |
|:--------------------------------------------------------------------------------------|:-------------------------|-------------------:|
| UNIVERSITY OF SANTO TOMAS                                                             | Local                    |              18038 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA                                             | Local                    |               4528 |
| FAR EASTERN UNIVERSITY                                                                | Local                    |               4309 |
| SAN PEDRO COLLEGE                                                                     | Local                    |               3644 |
| SAINT LOUIS UNIVERSITY                                                                | Local                    |               3221 |
| CEBU DOCTOR'S UNIVERSITY                                                              | Local                    |               2406 |
| DE LA SALLE UNIVERSITY - MANILA                                                       | Local                    |               2242 |
| OUR LADY OF FATIMA UNIVERSITY (FATIMA MEDICAL SCIENCE FOUNDATION) - VALENZUELA        | Local                    |               2041 |
| CENTRO ESCOLAR UNIVERSITY - MANILA                                                    | Local                    |               2022 |
| SOUTHWESTERN UNIVERSITY                                                               | Local                    |               1841 |
| ATENEO DE MANILA UNIVERSITY - QUEZON CITY                                             | Local                    |               1782 |
| VELEZ COLLEGE                                                                         | Local                    |               1750 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS                                                   | Local                    |               1724 |
| DAVAO MEDICAL SCHOOL FOUNDATION                                                       | Local                    |               1665 |
| EMILIO AGUINALDO COLLEGE                                                              | Local                    |               1577 |
| AMA COMPUTER COLLEGE - MAKATI                                                         | Local                    |               1519 |
| ANGELES UNIVERSITY FOUNDATION                                                         | Local                    |               1337 |
| SILLIMAN UNIVERSITY                                                                   | Local                    |               1303 |
| AGO MEDICAL AND EDUCATIONAL CENTER - BICOL CHRISTIAN COLLEGE OF MEDICINE              | Local                    |               1284 |
| XAVIER UNIVERSITY                                                                     | Local                    |               1228 |
| BROKENSHIRE COLLEGE                                                                   | Local                    |               1226 |
| ATENEO DE ZAMBOANGA UNIVERSITY                                                        | Local                    |               1172 |
| FEU - DR. NICANOR REYES MEDICAL FOUNDATION                                            | Local                    |               1151 |
| LYCEUM NORTHWESTERN UNIVERSITY                                                        | Local                    |               1048 |
| UNIVERSITY OF SAN AGUSTIN                                                             | Local                    |                995 |
| ATENEO DE DAVAO UNIVERSITY                                                            | Local                    |                981 |
| DE LA SALLE HEALTH SCIENCES INSTITUTE                                                 | Local                    |                952 |
| TRINITY UNIVERSITY OF ASIA                                                            | Local                    |                897 |
| MANILA CENTRAL UNIVERSITY                                                             | Local                    |                837 |
| ATENEO DE MANILA UNIVERSITY                                                           | Local                    |                751 |
| CENTRAL PHILIPPINE UNIVERSITY                                                         | Local                    |                697 |
| VIRGEN MILAGROSA UNIVERSITY FOUNDATION AND VMU INSTITUTE OF MEDICAL FOUNDATION        | Local                    |                697 |
| ADVENTIST UNIVERSITY OF THE PHILIPPINES                                               | Local                    |                672 |
| SAINT PAUL UNIVERSITY PHILIPPINES                                                     | Local                    |                662 |
| UNIVERSITY OF ST. LA SALLE                                                            | Local                    |                629 |
| UNIVERSITY OF THE IMMACULATE CONCEPTION                                               | Local                    |                601 |
| VELEZ COLLEGE CEBU                                                                    | Local                    |                559 |
| UNIVERSITY OF THE EAST RAMON MAGSAYSAY MEMORIAL MEDICAL CENTER                        | Local                    |                555 |
| UNIVERSITY OF SAN CARLOS                                                              | Local                    |                551 |
| SAN BEDA COLLEGE                                                                      | Local                    |                530 |
| SAN PEDRO COLLEGE DAVAO CITY                                                          | Local                    |                512 |
| MANILA TYTANA COLLEGES                                                                | Local                    |                485 |
| ANGELES UNIVERSITY FOUNDATION ANGELES CITY                                            | Local                    |                481 |
| CENTRO ESCOLAR UNIVERSITY - MAKATI                                                    | Local                    |                472 |
| DOÑA REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION                                   | Local                    |                468 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS CAVITE                                            | Local                    |                456 |
| DAVAO DOCTORS COLLEGE                                                                 | Local                    |                444 |
| LICEO DE CAGAYAN UNIVERSITY                                                           | Local                    |                428 |
| FAR EASTERN UNIVERSITY - NRMF (FAIRVIEW Q.C.)                                         | Local                    |                427 |
| OUR LADY OF FATIMA UNIVERSITY - QUEZON CITY                                           | Local                    |                423 |
| MINDANAO SANITARIUM AND HOSPITAL COLLEGE                                              | Local                    |                393 |
| CENTRO ESCOLAR UNIVERSITY - MENDIOLA MANILA                                           | Local                    |                382 |
| SAINT LOUIS UNIVERSITY - BAGUIO                                                       | Local                    |                380 |
| DE LA SALLE - LIPA                                                                    | Local                    |                365 |
| UNIVERSITY OF THE EAST - MANILA                                                       | Local                    |                352 |
| XAVIER UNIVERSITY CAGAYAN DE ORO CITY                                                 | Local                    |                349 |
| UNIVERSITY OF BAGUIO                                                                  | Local                    |                346 |
| UNIVERSIDAD DE ZAMBOANGA                                                              | Local                    |                323 |
| UNIVERSITY OF THE CORDILLERAS                                                         | Local                    |                310 |
| ST. PAUL UNIVERSITY ILOILO                                                            | Local                    |                305 |
| ILOILO DOCTORS COLLEGE                                                                | Local                    |                303 |
| UNIVERSIDAD DE STA. ISABEL                                                            | Local                    |                302 |
| RIVERSIDE COLLEGE                                                                     | Local                    |                301 |
| MOUNTAIN VIEW COLLEGE                                                                 | Local                    |                294 |
| NOTRE DAME UNIVERSITY                                                                 | Local                    |                277 |
| UNIVERSITY OF NEGROS OCCIDENTAL-RECOLETOS                                             | Local                    |                277 |
| MIRIAM COLLEGE                                                                        | Local                    |                257 |
| UNIVERSITY OF THE VISAYAS                                                             | Local                    |                254 |
| ATENEO DE NAGA UNIVERSITY                                                             | Local                    |                253 |
| SAINT SCHOLASTICA'S COLLEGE TACLOBAN                                                  | Local                    |                250 |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES                                              | Local                    |                250 |
| LYCEUM OF THE PHILIPPINES UNIVERSITY - BATANGAS                                       | Local                    |                249 |
| OUR LADY OF FATIMA UNIVERSITY VALENZUELA CITY                                         | Local                    |                247 |
| LORMA COLLEGES                                                                        | Local                    |                233 |
| SILLIMAN UNIVERSITY DUMAGUETE CITY                                                    | Local                    |                227 |
| SAINT MARY'S UNIVERSITY                                                               | Local                    |                219 |
| CAPITOL MEDICAL CENTER COLLEGES                                                       | Local                    |                217 |
| ST. LOUIS UNIVERSITY BAGUIO CITY                                                      | Local                    |                208 |
| ARELLANO UNIVERSITY - MANILA                                                          | Local                    |                203 |
| COLEGIO SAN AGUSTIN - BACOLOD                                                         | Local                    |                198 |
| NOTRE DAME OF DADIANGAS UNIVERSITY                                                    | Local                    |                198 |
| PERPETUAL HELP COLLEGE OF MANILA                                                      | Local                    |                197 |
| UNIVERSITY OF PERPETUAL HELP - DR. JOSE G. TAMAYO MEDICAL UNIVERSITY                  | Local                    |                196 |
| MAKATI MEDICAL CENTER COLLEGE OF NURSING                                              | Local                    |                191 |
| SOUTHWESTERN UNIVERSITY CEBU                                                          | Local                    |                191 |
| NOTRE DAME OF MARBEL UNIVERSITY                                                       | Local                    |                186 |
| ADAMSON UNIVERSITY                                                                    | Local                    |                184 |
| OUR LADY OF FATIMA UNIVERSITY - ANTIPOLO                                              | Local                    |                175 |
| SAN BEDA COLLEGE MENDIOLA MANILA                                                      | Local                    |                175 |
| NEW ERA UNIVERSITY                                                                    | Local                    |                171 |
| HOLY NAME UNIVERSITY                                                                  | Local                    |                159 |
| ST. PAUL UNIVERSITY - MANILA (ST. PAUL UNIVERITY SYSTEM)                              | Local                    |                159 |
| UNIVERSITY OF SAN CARLOS CEBU CITY                                                    | Local                    |                158 |
| ST. SCHOLASTICA'S COLLEGE                                                             | Local                    |                158 |
| PINES CITY COLLEGES                                                                   | Local                    |                154 |
| UNIVERSITY OF LA SALETTE                                                              | Local                    |                152 |
| SOUTHVILLE INTERNATIONAL SCHOOL AND COLLEGES                                          | Local                    |                151 |
| UNIVERSITY OF ST. LOUIS - TUGUEGARAO                                                  | Local                    |                150 |
| CEBU DOCTORS COLLEGE CEBU CITY                                                        | Local                    |                148 |
| AQUINAS UNIVERSITY OF LEGAZPI                                                         | Local                    |                146 |
| MINDANAO MEDICAL FOUNDATION COLLEGE                                                   | Local                    |                143 |
| UNIVERSITY OF THE EAST (C.M. RECTO MANILA)                                            | Local                    |                143 |
| UNIVERSITY OF CEBU - BANILAD                                                          | Local                    |                140 |
| DE LA SALLE - HEALTH SCIENCES CAMPUS                                                  | Local                    |                136 |
| MISAMIS UNIVERSITY - OZAMIS CITY                                                      | Local                    |                132 |
| REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION TACLOBAN                               | Local                    |                130 |
| ST. PAUL UNIVERSITY - QUEZON CITY                                                     | Local                    |                129 |
| UNIVERSITY OF SAN AGUSTIN - ILOILO CITY                                               | Local                    |                124 |
| GENERAL SANTOS DOCTORS' MEDICAL SCHOOL FOUNDATION                                     | Local                    |                122 |
| COLEGIO DE SAN JUAN DE LETRAN                                                         | Local                    |                121 |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING AND LIBERAL ARTS                          | Local                    |                119 |
| UNIVERSITY OF PANGASINAN                                                              | Local                    |                119 |
| EMILIO AGUINALDO COLLEGE MANILA                                                       | Local                    |                117 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION                                               | Local                    |                117 |
| DIVINE WORD COLLEGE OF LAOAG                                                          | Local                    |                116 |
| WESLEYAN UNIVERSITY - PHILIPPINES (CABANATUAN)                                        | Local                    |                109 |
| ST. PAUL UNIVERSITY - MANILA                                                          | Local                    |                109 |
| CENTRAL LUZON DOCTORS' HOSPITAL EDUCATIONAL INSTITUTION                               | Local                    |                108 |
| UNIVERSITY OF BAGUIO BAGUIO CITY                                                      | Local                    |                106 |
| HOLY ANGEL UNIVERSITY                                                                 | Local                    |                105 |
| CAPITOL UNIVERSITY                                                                    | Local                    |                104 |
| CENTRAL PHILIPPINE UNIVERSITY ILOILO                                                  | Local                    |                104 |
| FEU - EAST ASIA COLLEGE                                                               | Local                    |                101 |
| GLOBAL CITY INNOVATIVE COLLEGE                                                        | Local                    |                101 |
| UNIVERSITY OF ST. LA SALLE BACOLOD CITY                                               | Local                    |                 99 |
| ST. JUDE COLLEGE                                                                      | Local                    |                 95 |
| FATHER SATURNINO M. URIOS UNIVERSITY                                                  | Local                    |                 91 |
| SOUTHWESTERN UNIVERSITY-MATIAS H. AZNAR MEMORIAL COLLEGE OF MEDICINE - CEBU CITY CEBU | Local                    |                 89 |
| UNIVERSITY OF SOUTHERN PHILIPPINES FOUNDATION                                         | Local                    |                 89 |
| UERM MEMORIAL MEDICAL CENTER                                                          | Local                    |                 88 |
| CENTRO ESCOLAR UNIVERSITY AT MALOLOS                                                  | Local                    |                 87 |
| MANILA DOCTORS COLLEGE - PASAY CITY                                                   | Local                    |                 87 |
| ILIGAN MEDICAL CENTER COLLEGE                                                         | Local                    |                 86 |
| COLLEGE OF THE HOLY SPIRIT OF MANILA                                                  | Local                    |                 83 |
| HOLY INFANT COLLEGE                                                                   | Local                    |                 80 |
| SOUTHEAST ASIAN COLLEGE                                                               | Local                    |                 78 |
| EASTER COLLEGE                                                                        | Local                    |                 78 |
| REMEDIOS T. ROMUALDEZ MEM. SCH. - MMC                                                 | Local                    |                 78 |
| DR. CARLOS S. LANTING COLLEGE                                                         | Local                    |                 76 |
| WORLD CITI COLLEGES QUEZON CITY                                                       | Local                    |                 76 |
| VIRGEN MILAGROSA UNIV. FOUNDATION - SAN CARLOS CITY PANG.                             | Local                    |                 76 |
| THE PHILIPPINE WOMEN'S UNIVERSITY SYSTEM - MANILA                                     | Local                    |                 75 |
| METROPOLITAN HOSPITAL COLLEGE OF NURSING                                              | Local                    |                 74 |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE                                                  | Local                    |                 74 |
| BRENT HOSPITAL AND COLLEGES                                                           | Local                    |                 73 |
| ST. ALEXIUS COLLEGE                                                                   | Local                    |                 71 |
| MANILA ADVENTIST MEDICAL CENTER AND COLLEGES                                          | Local                    |                 71 |
| UNIVERSITY OF VISAYAS CEBU                                                            | Local                    |                 69 |
| UNIVERSITY OF NUEVA CACERES                                                           | Local                    |                 67 |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-LAS PIÑAS                                   | Local                    |                 67 |
| NOTRE DAME OF JOLO COLLEGE                                                            | Local                    |                 65 |
| LYCEUM NORTHWESTERN DAGUPAN CITY                                                      | Local                    |                 64 |
| UNIVERSITY OF THE CORDILLERAS (BCF)                                                   | Local                    |                 63 |
| ASSUMPTION COLLEGE                                                                    | Local                    |                 62 |
| LA CONSOLACION COLLEGE - MANILA                                                       | Local                    |                 62 |
| DE LA SALLE - LIPA BATANGAS                                                           | Local                    |                 61 |
| UNIVERSITY OF THE EAST - RAMON MAGSAYSAY MEM. MEDICAL CENTER                          | Local                    |                 60 |
| MANILA DOCTORS COLLEGE U.N. AVENUE MANILA                                             | Local                    |                 59 |
| UNIVERSITY OF SAN JOSE - RECOLETOS                                                    | Local                    |                 58 |
| SACRED HEART COLLEGE OF LUCENA                                                        | Local                    |                 57 |
| BUTUAN DOCTORS COLLEGE                                                                | Local                    |                 57 |
| NOTRE DAME UNIVERSITY COTABATO CITY                                                   | Local                    |                 56 |
| ST. PAUL UNIVERSITY DUMAGUETE                                                         | Local                    |                 55 |
| DIPOLOG MEDICAL CENTER COLLEGE FOUNDATION                                             | Local                    |                 55 |
| OUR LADY OF FATIMA UNIVERSITY - LAGRO QUEZON CITY                                     | Local                    |                 53 |
| MIRIAM COLLEGE FOUNDATION INC.                                                        | Local                    |                 52 |
| BAGUIO CENTRAL UNIVERSITY                                                             | Local                    |                 52 |
| SAN LORENZO RUIZ COLLEGE OF ORMOC                                                     | Local                    |                 51 |
| SOUTH SEED - LPDH COLLEGE                                                             | Local                    |                 50 |
| MINDANAO SANITARIUM & HOSPITAL COLLEGE ILIGAN CITY                                    | Local                    |                 50 |
| NAGA COLLEGE FOUNDATION                                                               | Local                    |                 50 |
| CEBU DOCTOR'S UNIVERSITY COLLEGE OF MEDICINE - MANDAUE CITY CEBU                      | Local                    |                 49 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION INC.                                          | Local                    |                 48 |
| PILAR COLLEGE                                                                         | Local                    |                 47 |
| DE LA SALLE - COLLEGE OF SAINT BENILDE                                                | Local                    |                 47 |
| MAPUA INSTITUTE OF TECHNOLOGY - MANILA                                                | Local                    |                 46 |
| MOUNTAIN VIEW COLLEGE BUKIDNON                                                        | Local                    |                 46 |
| PHILIPPINE WOMEN'S UNIVERSITY TAFT AVENUE MANILA                                      | Local                    |                 46 |
| PHILIPPINE CHRISTIAN UNIVERSITY                                                       | Local                    |                 45 |
| MEDINA COLLEGE                                                                        | Local                    |                 45 |
| LYCEUM OF THE PHILIPPINES - LAGUNA                                                    | Local                    |                 45 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - BINAN LAGUNA                                    | Local                    |                 44 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - LAGUNA                                          | Local                    |                 44 |
| NOTRE DAME OF DADIANGAS COLLEGE GEN. SANTOS                                           | Local                    |                 44 |
| UNIVERSITY OF THE ASSUMPTION                                                          | Local                    |                 44 |
| BROKENSHIRE COLLEGE DAVAO CITY                                                        | Local                    |                 43 |
| UNIVERSITY OF CAGAYAN VALLEY                                                          | Local                    |                 43 |
| UNIVERSITY OF THE VISAYAS - MANDAUE                                                   | Local                    |                 42 |
| FILAMER CHRISTIAN UNIVERSITY                                                          | Local                    |                 41 |
| LA CONSOLACION COLLEGE                                                                | Local                    |                 41 |
| YAMAN LAHI FOUNDATION - EMILIO AGUINALDO COLLEGE                                      | Local                    |                 40 |
| ST. JUDE COLLEGE MANILA                                                               | Local                    |                 39 |
| LOURDES COLLEGE                                                                       | Local                    |                 39 |
| UNIVERSIDAD DE STA. ISABEL NAGA CITY                                                  | Local                    |                 39 |
| UNIVERSITY OF BOHOL                                                                   | Local                    |                 37 |
| NUEVA ECIJA COLLEGES                                                                  | Local                    |                 37 |
| NEW ERA UNIVERSITY QUEZON CITY                                                        | Local                    |                 37 |
| NORTHWESTERN UNIVERSITY                                                               | Local                    |                 36 |
| ILIGAN MEDICAL CENTER ILIGAN CITY                                                     | Local                    |                 36 |
| UNIVERSITY OF LUZON                                                                   | Local                    |                 36 |

> Full listing: [05_university_listings_private.csv](05_university_listings_private.csv) (798 rows)

### 8.3 Foreign Universities (533 institutions, 1,892 applicants)

**Table 17 (Foreign, first 200 of 533)**

| UNDERGRAD_UNIVERSITY                                     | UNDERGRAD_UNI_LOCATION   |   total_applicants |
|:---------------------------------------------------------|:-------------------------|-------------------:|
| RANGSIT UNIVERSITY                                       | International            |                 69 |
| UNIVERSITY OF CALIFORNIA - DAVIS                         | International            |                 43 |
| UNIVERSITY OF CALIFORNIA - IRVINE                        | International            |                 40 |
| TRINITY COLLEGE                                          | International            |                 40 |
| RANGSIT UNIVERSITY THAILAND                              | International            |                 38 |
| MAHIDOL UNIVERSITY                                       | International            |                 36 |
| UNIVERSITY OF CALIFORNIA LOS ANGELES                     | International            |                 30 |
| MAHIDOL UNIVERSITY THAILAND                              | International            |                 28 |
| CHULALONGKORN UNIVERSITY                                 | International            |                 28 |
| CALIFORNIA STATE UNIVERSITY                              | International            |                 27 |
| UNIVERSITY OF CALIFORNIA RIVERSIDE CA USA                | International            |                 25 |
| AL KWARIZMI INTERNATIONAL COLLEGE FOUNDATION             | International            |                 23 |
| UNIVERSITY OF CALIFORNIA - SAN DIEGO                     | International            |                 23 |
| CHIANG MAI UNIVERSITY                                    | International            |                 23 |
| THAMMASAT UNIVERSITY                                     | International            |                 20 |
| UNIVERSITY OF CALIFORNIA-RIVERSIDE                       | International            |                 19 |
| WESTERN STATE UNIVERSITY OF COLORADO                     | International            |                 19 |
| UNIVERSITY OF TORONTO                                    | International            |                 17 |
| UNIVERSITY OF CALIFORNIA BERKELEY                        | International            |                 17 |
| MAE FAH LUANG UNIVERSITY                                 | International            |                 17 |
| CHULALONGKORN UNIVERSITY THAILAND                        | International            |                 17 |
| UNIVERSITY OF WASHINGTON                                 | International            |                 16 |
| NARESUAN UNIVERSITY                                      | International            |                 15 |
| UNIVERSITY OF FLORIDA                                    | International            |                 15 |
| MONAD UNIVERSITY                                         | International            |                 14 |
| UNIVERSITY OF NEVADA LAS VEGAS                           | International            |                 12 |
| UNIVERSITY OF CALIFORNIA SANTA BARBARA                   | International            |                 12 |
| UNIVERSITY OF SAN FRANCISCO                              | International            |                 11 |
| HUACHIEW CHALERMPRAKIET UNIVERSITY                       | International            |                 11 |
| SRINAKHARINWIROT UNIVERSITY                              | International            |                 11 |
| RUTGERS UNIVERSITY NEW JERSEY                            | International            |                 11 |
| RUTGERS UNIVERSITY                                       | International            |                 10 |
| UNIVERSITY OF GUAM                                       | International            |                 10 |
| UNIVERSITAS ADVENT INDONESIA                             | International            |                 10 |
| UNIVERSITY OF CENTRAL FLORIDA                            | International            |                 10 |
| STONY BROOK UNIVERSITY                                   | International            |                  9 |
| CALIFORNIA STATE UNIVERSITY LONG BEACH                   | International            |                  9 |
| CALIFORNIA STATE UNIVERSITY FRESNO                       | International            |                  9 |
| BURAPHA UNIVERSITY                                       | International            |                  9 |
| VIRGINIA COMMONWEALTH UNIVERSITY                         | International            |                  9 |
| UNIVERSITY OF CALIFORNIA AT STA. CRUZ U.S.A.             | International            |                  9 |
| UNIVERSITY OF HAWAII AT MANOA                            | International            |                  9 |
| UNIVERSITY OF ILLINOIS CHICAGO                           | International            |                  9 |
| UNIVERSITY OF CALIFORNIA SANTA CRUZ                      | International            |                  8 |
| THAMMASAT UNIV.                                          | International            |                  8 |
| UNIVERSITY OF BRITISH COLUMBIA                           | International            |                  8 |
| UNIVERSITY OF TEXAS                                      | International            |                  8 |
| RAMKHAMHAENG UNIVERSITY                                  | International            |                  8 |
| PRINCE OF SONGKLA UNIVERSITY                             | International            |                  8 |
| UNIVERSITY OF HOUSTON                                    | International            |                  7 |
| UNIVERSITY OF CALIFORNIA MERCED                          | International            |                  7 |
| UNIVERSITY OF SOUTH FLORIDA USA                          | International            |                  6 |
| EAST AFRICA UNIVERSITY                                   | International            |                  6 |
| UNIVERSITY AT BUFFALO                                    | International            |                  6 |
| KASETSART UNIVERSITY                                     | International            |                  6 |
| RUNGSIT UNIVERSITY                                       | International            |                  6 |
| UNIVERSITY OF MARYLAND - MARYLAND U.S.A.                 | International            |                  6 |
| CHIANGMAI UNIVERSITY                                     | International            |                  6 |
| CALIFORNIA STATE UNIVERSITY - FULLERTON                  | International            |                  6 |
| SAN DIEGO STATE UNIVERSITY - CALIFORNIA U.S.A.           | International            |                  6 |
| MAHASARAKHAM UNIVERSITY                                  | International            |                  6 |
| KHON KAEN UNIVERSITY                                     | International            |                  6 |
| ASSUMPTION UNIVERSITY                                    | International            |                  6 |
| LADOKE AKINTOLA UNIVERSITY OF TECHNOLOGY OGBOMOSO        | International            |                  6 |
| ST. ANDREW'S INTERNATIONAL ACADEMY INDIA                 | International            |                  5 |
| UNIVERSITY OF WISCONSIN-MADISON                          | International            |                  5 |
| UNIVERSITY OF NEVADA - RENO                              | International            |                  5 |
| UNIVERSITY OF MICHIGAN                                   | International            |                  5 |
| UNIVERSITY OF NEW ENGLAND                                | International            |                  5 |
| SUNRISE UNIVERSITY                                       | International            |                  5 |
| UNIVERSITY OF CONNECTICUT                                | International            |                  5 |
| ADVENTIST INDONESIA UNIVERSITY INDONESIA                 | International            |                  5 |
| UNIVERSITY OF TEXAS AT ARLINGTON                         | International            |                  5 |
| ARIZONA STATE UNIVERSITY                                 | International            |                  5 |
| MOGADISHU UNIVERSITY                                     | International            |                  5 |
| KHON KAEN UNIVERSITY THAILAND                            | International            |                  5 |
| KITASATO UNIVERSITY                                      | International            |                  5 |
| TEMPLE UNIVERSITY USA                                    | International            |                  5 |
| SIAM UNIVERSITY                                          | International            |                  5 |
| UNIVERSITY OF BRITISH COLUMBIA CANADA                    | International            |                  5 |
| RAMKHAMHAENG UNIV.                                       | International            |                  5 |
| PENSACOLA CHRISTIAN COLLEGE                              | International            |                  5 |
| NEW YORK UNIVERSITY NY USA                               | International            |                  5 |
| RUTGERS COLLEGE NEW JERSEY                               | International            |                  5 |
| CHAING MAI UNIVERSITY-THAILAND                           | International            |                  5 |
| SRI CHAITANYA JUNIOR COLLEGE                             | International            |                  5 |
| ANAND HOMEOPATHIC MEDICAL COLLEGE AND RESEARCH INSTITUTE | International            |                  4 |
| ANDHRA UNIVERSITY                                        | International            |                  4 |
| RAJAMANGALA UNIVERSITY OF TECHNOLOGY THANYABURI          | International            |                  4 |
| LOYOLA MARYMOUNT UNIVERSITY                              | International            |                  4 |
| BINGHAMTON UNIVERSITY                                    | International            |                  4 |
| UNIVERSITY OF MARYLAND COLLEGE PARK                      | International            |                  4 |
| UNIVERSITY OF SYDNEY                                     | International            |                  4 |
| AZAD UNIVERSITY OF TEHRAN SHAMAL                         | International            |                  4 |
| UNIVERSITY OF WEST FLORIDA                               | International            |                  4 |
| BARUCH COLLEGE                                           | International            |                  4 |
| MADONNA UNIVERSITY                                       | International            |                  4 |
| MEDGAR EVERS COLLEGE                                     | International            |                  4 |
| MMA MATRIC HIGHER SECONDARY SCHOOL                       | International            |                  4 |
| LOYOLA UNIVERSITY CHICAGO U.S.A.                         | International            |                  4 |
| WALAILAK UNIVERSITY                                      | International            |                  4 |
| JOHNS HOPKINS UNIVERSITY                                 | International            |                  4 |
| OPJS UNIVERSITY CHURU                                    | International            |                  4 |
| OLABISI ONABANJO UNVERSITY AGO-IWOYE.                    | International            |                  4 |
| ISLAMIC AZAD UNIVERSITY                                  | International            |                  4 |
| MONASH UNIVERSITY                                        | International            |                  4 |
| SAN DIEGO STATE UNIVERSITY                               | International            |                  4 |
| SRINAKARINWIROTE UNIVERSITY THAILAND                     | International            |                  4 |
| UNIVERSITY OF AUCKLAND                                   | International            |                  4 |
| THE OHIO STATE UNIVERSITY                                | International            |                  4 |
| THE TAMIL NADU DR. M.G.R. MEDICAL UNIVERSITY             | International            |                  4 |
| ST.THERESA INTERNATIONAL COLLEGE                         | International            |                  4 |
| SILPAKORN UNIVERSITY                                     | International            |                  4 |
| UNIVERSITY OF SOUTHERN CALIFORNIA                        | International            |                  4 |
| UNIVERSITY OF SOUTH FLORIDA                              | International            |                  4 |
| BOROMARAJONANI COLLEGE OF NURSING SURIN                  | International            |                  4 |
| UNIVERSITY OF MELBOURNE                                  | International            |                  4 |
| BINGHAM UNIVERSITY                                       | International            |                  4 |
| UNIVERSITY OF IBADAN                                     | International            |                  4 |
| BOSTON UNIVERSITY                                        | International            |                  4 |
| CALIFORNIA STATE UNIVERSITY EAST BAY                     | International            |                  4 |
| UNIVERSITY OF NORTH FLORIDA                              | International            |                  4 |
| SIMON FRASER UNIVERSITY                                  | International            |                  4 |
| GOVERNMENT SCHOOL                                        | International            |                  4 |
| DR.NTR UNIVERSITY OF HEALTH SCIENCE                      | International            |                  4 |
| DREXEL UNIVERSITY                                        | International            |                  4 |
| UNIVERSITY OF ARIZONA                                    | International            |                  4 |
| SJG AYURVEDIC MEDICAL COLLEGE                            | International            |                  4 |
| SRM UNIVERSITY                                           | International            |                  4 |
| DEAKIN UNIVERSITY                                        | International            |                  4 |
| UNIVERSITY OF GHANA                                      | International            |                  4 |
| DR RAM MANOHAR LOHIA AVADH UNIVERSITY FAIZABAD           | International            |                  4 |
| SAN FRANCISCO STATE UNIVERSITY                           | International            |                  4 |
| PRAGATHI DEGREE COLLEGE                                  | International            |                  4 |
| HUACHIEN CHALERMPRAKIET UNIVERSITY THAILAND              | International            |                  4 |
| CHINA MEDICAL COLLEGE                                    | International            |                  3 |
| BHARATI VIDYAPEETH DEEMED UNIVERSITY                     | International            |                  3 |
| CALIFORNIA STATE UNIVERSITY NORTHRIDGE                   | International            |                  3 |
| UNIVERSITY OF ILORIN                                     | International            |                  3 |
| CALIFORNIA STATE UNIVERSITY LOS ANGELES                  | International            |                  3 |
| BAYLOR UNIVERSITY                                        | International            |                  3 |
| BAYLOR UNIVERSITY TEXAS USA                              | International            |                  3 |
| WINONA STATE UNIVERSITY                                  | International            |                  3 |
| YORK UNIVERSITY CANADA                                   | International            |                  3 |
| AMBROSE ALLI UNIVERSITY                                  | International            |                  3 |
| UNIVERSITY OF KENTUCKY - KENTUCKY U.S.A.                 | International            |                  3 |
| BUNDELKHAND UNIVERSITY JHANSI                            | International            |                  3 |
| BOSTON COLLEGE MA USA                                    | International            |                  3 |
| BOWEN UNIVERSITY                                         | International            |                  3 |
| UNIVERSITY OF RAJASTHAN                                  | International            |                  3 |
| UNIVERSITY OF PITTSBURGH USA                             | International            |                  3 |
| UNIVERSITY OF VIRGINIA                                   | International            |                  3 |
| UNIVERSITY OF TEXAS AT AUSTIN                            | International            |                  3 |
| UNIVERSITY OF PORTHARCOURT                               | International            |                  3 |
| UNIVERSITY OF SOUTHERN CALIFORNIA USA                    | International            |                  3 |
| BISHOP HEBER COLLEGE                                     | International            |                  3 |
| SHRIDHAR UNIVERSITY                                      | International            |                  3 |
| HALLYM UNIVERSITY                                        | International            |                  3 |
| UNIVERSITY OF BENIN                                      | International            |                  3 |
| UNIVERSITY OF BRADFORD                                   | International            |                  3 |
| FORDHAM COLLEGE BRONX NEW YORK USA                       | International            |                  3 |
| STANFORD UNIVERSITY CALIFORNIA U.S.A.                    | International            |                  3 |
| DR MGR MEDICAL UNIVERSITY                                | International            |                  3 |
| FRANKLIN & MARSHALL COLLEGE                              | International            |                  3 |
| THE MAHARAJA SAYAJIRAO UNIVERSITY OF BARODA              | International            |                  3 |
| CONSOLATA SCHOOL OF NURSING                              | International            |                  3 |
| CREIGHTON UNIVERSITY                                     | International            |                  3 |
| CALIFORNIA STATE POLYTECHNIC UNIV. CA USA                | International            |                  3 |
| CORNELL UNIVERSITY                                       | International            |                  3 |
| DR NAYAPALI COLLEGE                                      | International            |                  3 |
| HONG KONG METROPOLITAN UNIVERSITY                        | International            |                  3 |
| RAJIV GANDHI UNIVERSITY OF HEALTH SCIENCES               | International            |                  3 |
| OLABISI ONABANJO UNIVERISTY                              | International            |                  3 |
| JAYA COLLEGE OF ARTS AND SCIENCE                         | International            |                  3 |
| NIMS NURSING COLLEGE                                     | International            |                  3 |
| PRINCE OF SONGKHLA UNIVERSITY                            | International            |                  3 |
| GEETANJALI COLLEGE OF NURSHING                           | International            |                  3 |
| IMPHAL COLLEGE                                           | International            |                  3 |
| IMO STATE UNIVERSITY                                     | International            |                  3 |
| PACIFIC UNION COLLEGE                                    | International            |                  3 |
| SANJEEVAN COLLEGE OF PHARMACY                            | International            |                  3 |
| NATIONAL UNIVERSITY OF SINGAPORE                         | International            |                  3 |
| MICHIGAN STATE UNIVERSITY                                | International            |                  3 |
| MIDDLE TENNESSEE STATE UNIVERSITY                        | International            |                  3 |
| NEW YORK UNIVERSITY                                      | International            |                  3 |
| MADHUSUDAN SCHOOL OF NURSING                             | International            |                  3 |
| AMERICAN UNIVERSITY OF NIGERIA                           | International            |                  3 |
| WASHINGTON STATE UNIVERSITY                              | International            |                  3 |
| ALIAH UNIVERSITY                                         | International            |                  2 |
| ADELPHI UNIVERSITY NEW YORK U.S.A.                       | International            |                  2 |
| WESTERN SYDNEY UNIVERSITY                                | International            |                  2 |
| WESTERN UNIVERSITY                                       | International            |                  2 |
| B. R. MIRDHA COLLEGE                                     | International            |                  2 |
| BAPUJI AYURVEDIC MEDICAL COLLEGE                         | International            |                  2 |
| UNIVERSITY OF TEXAS (DALLAS)                             | International            |                  2 |
| UNIVERSITY OF TEXAS SAN ANTONIO                          | International            |                  2 |
| UNIVERSITY OF THE PACIFIC ALBANY CA USA                  | International            |                  2 |
| LOMA LINDA UNIVERSITY RIVERSIDE CA                       | International            |                  2 |
| KAKATIYA UNIVERSITY                                      | International            |                  2 |
| KAMAKHYA PEMTON COLLEGE                                  | International            |                  2 |

> Full listing: [05_university_listings_foreign.csv](05_university_listings_foreign.csv) (533 rows)


---
*Analysis complete. Generated by page_05_university_type.py*

---



<a id="06-flow-and-pathways"></a>

**Generated:** 2026-07-31 16:31

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `besttrend + uni + bestobservable`

**Filters:** None (full unfiltered dataset)

---

**Subsets used:**
- **uni** (UNDERGRAD_UNI_TYPE flow): besttrend, UNDERGRAD_UNI_TYPE in [Public, Private, Foreign] — 133,477 records
- **besttrend** (UNDERGRAD_COURSE_GROUP flow): best NMAT record, Year 2006-2018 — 134,869 records
- **bestobservable** (Bin -> PLE flow): best attempt within Year<=2014 (IS_BEST_OBSERVABLE_RECORD) — 69,503 records

---

## 1. Sankey Flow: UNDERGRAD_UNI_TYPE -> PercentileBin

Source: `uni` subset (besttrend, Public/Private/Foreign)

**Table 06-1. University-type to percentile bin flow counts**

| UNDERGRAD_UNI_TYPE   | PercentileBin   |   count |
|:---------------------|:----------------|--------:|
| Public               | B1              |    2949 |
| Public               | B2              |    2228 |
| Public               | B3              |    2058 |
| Public               | B4              |    2247 |
| Public               | B5              |    2320 |
| Public               | B6              |    2421 |
| Public               | B7              |    2478 |
| Public               | B8              |    2606 |
| Public               | B9              |    3051 |
| Public               | B10             |    4876 |
| Private              | B1              |   12205 |
| Private              | B2              |    9823 |
| Private              | B3              |    9127 |
| Private              | B4              |   10061 |
| Private              | B5              |   10044 |
| Private              | B6              |   10079 |
| Private              | B7              |    9602 |
| Private              | B8              |    9821 |
| Private              | B9              |    9864 |
| Private              | B10             |   10774 |
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
| Public               |  2949 | 2228 | 2058 |  2247 |  2320 |  2421 | 2478 | 2606 | 3051 |  4876 |
| Private              | 12205 | 9823 | 9127 | 10061 | 10044 | 10079 | 9602 | 9821 | 9864 | 10774 |
| Foreign              |   262 |  174 |  140 |   176 |   145 |   164 |  161 |  175 |  197 |   266 |

### 1c. Row percentages (within UNDERGRAD_UNI_TYPE)

**Table 06-3. UNDERGRAD_UNI_TYPE -> PercentileBin row percentages**

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Public               | 10.83 | 8.18 | 7.56 | 8.25 | 8.52 | 8.89 |  9.1 | 9.57 |  11.2 |  17.9 |
| Private              | 12.04 | 9.69 |    9 | 9.92 | 9.91 | 9.94 | 9.47 | 9.69 |  9.73 | 10.63 |
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
| B1              | Confirmed PLE passer   |     795 |
| B1              | No confirmed PLE match |    6058 |
| B2              | Confirmed PLE passer   |    1336 |
| B2              | No confirmed PLE match |    4548 |
| B3              | Confirmed PLE passer   |    1703 |
| B3              | No confirmed PLE match |    4110 |
| B4              | Confirmed PLE passer   |    2330 |
| B4              | No confirmed PLE match |    4143 |
| B5              | Confirmed PLE passer   |    3003 |
| B5              | No confirmed PLE match |    3579 |
| B6              | Confirmed PLE passer   |    3168 |
| B6              | No confirmed PLE match |    3116 |
| B7              | Confirmed PLE passer   |    3407 |
| B7              | No confirmed PLE match |    2952 |
| B8              | Confirmed PLE passer   |    3690 |
| B8              | No confirmed PLE match |    3014 |
| B9              | Confirmed PLE passer   |    4474 |
| B9              | No confirmed PLE match |    2789 |
| B10             | Confirmed PLE passer   |    7073 |
| B10             | No confirmed PLE match |    2885 |

### 3b. PLE status composition within each bin (row %)

**Table 06-8. PLE status row percentages within each bin**

| PercentileBin   |   Confirmed PLE passer |   No confirmed PLE match |
|:----------------|-----------------------:|-------------------------:|
| B1              |                   11.6 |                     88.4 |
| B2              |                  22.71 |                    77.29 |
| B3              |                   29.3 |                     70.7 |
| B4              |                     36 |                       64 |
| B5              |                  45.62 |                    54.38 |
| B6              |                  50.41 |                    49.59 |
| B7              |                  53.58 |                    46.42 |
| B8              |                  55.04 |                    44.96 |
| B9              |                   61.6 |                     38.4 |
| B10             |                  71.03 |                    28.97 |

### 3c. Confirmed PLE linkage rate by bin

**Table 06-9. PLE linkage rate by percentile bin**

| PercentileBin   |   Confirmed PLE Passers |   Total in Bin |   PLE Linkage Rate (%) |
|:----------------|------------------------:|---------------:|-----------------------:|
| B1              |                     795 |           6853 |                   11.6 |
| B2              |                    1336 |           5884 |                  22.71 |
| B3              |                    1703 |           5813 |                   29.3 |
| B4              |                    2330 |           6473 |                     36 |
| B5              |                    3003 |           6582 |                  45.62 |
| B6              |                    3168 |           6284 |                  50.41 |
| B7              |                    3407 |           6359 |                  53.58 |
| B8              |                    3690 |           6704 |                  55.04 |
| B9              |                    4474 |           7263 |                   61.6 |
| B10             |                    7073 |           9958 |                  71.03 |

---

## 4. Top 10 Pathways: UNDERGRAD_UNI_TYPE -> B8-B10

Source: `uni` subset (besttrend, Public/Private/Foreign)

**Table 06-10. Top 10 UNDERGRAD_UNI_TYPE pathways into B8-B10**

| UNDERGRAD_UNI_TYPE   | PercentileBin   |   Count |
|:---------------------|:----------------|--------:|
| Private              | B10             |   10774 |
| Private              | B9              |    9864 |
| Private              | B8              |    9821 |
| Public               | B10             |    4876 |
| Public               | B9              |    3051 |
| Public               | B8              |    2606 |
| Foreign              | B10             |     266 |
| Foreign              | B9              |     197 |
| Foreign              | B8              |     175 |

**Table 06-11. Top 10 UNDERGRAD_UNI_TYPE pathways (ranked)**

|   Rank | UNDERGRAD_UNI_TYPE   | PercentileBin   |   Count |
|-------:|:---------------------|:----------------|--------:|
|      1 | Private              | B10             |   10774 |
|      2 | Private              | B9              |    9864 |
|      3 | Private              | B8              |    9821 |
|      4 | Public               | B10             |    4876 |
|      5 | Public               | B9              |    3051 |
|      6 | Public               | B8              |    2606 |
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
| Private              | B10             |   10774 |
| Private              | B8              |    9821 |
| Private              | B9              |    9864 |
| Public               | B10             |    4876 |
| Public               | B8              |    2606 |
| Public               | B9              |    3051 |

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
| Private              |    103669 |       30459 |              29.38 |
| Public               |     27916 |       10533 |              37.73 |

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
| Public               | Education                    |       776 |         479 |              61.73 |
| Public               | Engineering & Technology     |       160 |          91 |              56.88 |
| Foreign              | Engineering & Technology     |        28 |          14 |                 50 |
| Private              | Engineering & Technology     |       555 |         274 |              49.37 |
| Public               | Other                        |      2241 |        1004 |               44.8 |
| Foreign              | Natural Sciences             |       608 |         265 |              43.59 |
| Foreign              | Other                        |       189 |          80 |              42.33 |
| Public               | Natural Sciences             |      9836 |        3946 |              40.12 |
| Private              | Natural Sciences             |     30582 |       10378 |              33.93 |
| Public               | Medical & Allied             |     11507 |        3890 |              33.81 |
| Public               | Social & Behavioral Sciences |      3396 |        1123 |              33.07 |
| Private              | Other                        |      5853 |        1813 |              30.98 |
| Foreign              | Social & Behavioral Sciences |       221 |          65 |              29.41 |
| Private              | Medical & Allied             |     51357 |       14082 |              27.42 |
| Private              | Social & Behavioral Sciences |     12709 |        3254 |               25.6 |
| Foreign              | Medical & Allied             |       764 |         195 |              25.52 |
| Private              | Education                    |      2613 |         658 |              25.18 |
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
| Private              | Medical & Allied             |   51357 |                               49.54 |
| Private              | Natural Sciences             |   30582 |                                29.5 |
| Private              | Social & Behavioral Sciences |   12709 |                               12.26 |
| Private              | Other                        |    5853 |                                5.65 |
| Private              | Education                    |    2613 |                                2.52 |
| Private              | Engineering & Technology     |     555 |                                0.54 |
| Public               | Medical & Allied             |   11507 |                               41.22 |
| Public               | Natural Sciences             |    9836 |                               35.23 |
| Public               | Social & Behavioral Sciences |    3396 |                               12.17 |
| Public               | Other                        |    2241 |                                8.03 |
| Public               | Education                    |     776 |                                2.78 |
| Public               | Engineering & Technology     |     160 |                                0.57 |


---
*Analysis complete. Generated by page_06_flow_pathways.py*

---



<a id="07-ple-alignment"></a>

**Generated:** 2026-07-31 16:32

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `bestobservable`

**Filters:** None (full unfiltered dataset)

---

## 1. Score Profile by PLE Status

Count, median, mean, Q25, and Q75 for each score measure by PLE status.

**Table 23. Score profile by PLE status**

| PLE_STATUS_LABEL       |   TotalRawScoreTRUE_count |   TotalRawScoreTRUE_median |   TotalRawScoreTRUE_mean |   TotalRawScoreTRUE_q25 |   TotalRawScoreTRUE_q75 |   NMS_PER_num_count |   NMS_PER_num_median |   NMS_PER_num_mean |   NMS_PER_num_q25 |   NMS_PER_num_q75 |   NMS_GPS_count |   NMS_GPS_median |   NMS_GPS_mean |   NMS_GPS_q25 |   NMS_GPS_q75 |   NMS_APT_count |   NMS_APT_median |   NMS_APT_mean |   NMS_APT_q25 |   NMS_APT_q75 |   NMS_SA_count |   NMS_SA_median |   NMS_SA_mean |   NMS_SA_q25 |   NMS_SA_q75 |   PartIRawScoreTRUE_count |   PartIRawScoreTRUE_median |   PartIRawScoreTRUE_mean |   PartIRawScoreTRUE_q25 |   PartIRawScoreTRUE_q75 |   PartIIRawScoreTRUE_count |   PartIIRawScoreTRUE_median |   PartIIRawScoreTRUE_mean |   PartIIRawScoreTRUE_q25 |   PartIIRawScoreTRUE_q75 |
|:-----------------------|--------------------------:|---------------------------:|-------------------------:|------------------------:|------------------------:|--------------------:|---------------------:|-------------------:|------------------:|------------------:|----------------:|-----------------:|---------------:|--------------:|--------------:|----------------:|-----------------:|---------------:|--------------:|--------------:|---------------:|----------------:|--------------:|-------------:|-------------:|--------------------------:|---------------------------:|-------------------------:|------------------------:|------------------------:|---------------------------:|----------------------------:|--------------------------:|-------------------------:|-------------------------:|
| Confirmed PLE passer   |                     31572 |                        139 |                   141.04 |                     120 |                     162 |               30988 |                   69 |              64.56 |                45 |                88 |           31581 |              552 |         555.86 |           489 |           624 |           31581 |              548 |         552.13 |           491 |           612 |          31581 |             544 |        546.07 |          480 |          610 |                     31572 |                         74 |                    73.85 |                      63 |                      84 |                      31572 |                          66 |                     67.18 |                       55 |                       79 |
| No confirmed PLE match |                     37888 |                        114 |                    116.2 |                      94 |                     136 |               37758 |                   38 |              42.06 |                15 |                66 |           37922 |              470 |         471.63 |           399 |           545 |           37922 |              484 |         480.26 |           415 |           546 |          37922 |             471 |        474.14 |          406 |          539 |                     37888 |                         62 |                    61.89 |                      51 |                      73 |                      37888 |                          52 |                     54.31 |                       42 |                       65 |


---

## 2. Box-Plot Data by Score and PLE Status

Quantile-based summary for each score variable, split by PLE status.

**Box-plot summary statistics**

| ScoreVariable      | PLE_STATUS_LABEL       |     n |   min |   q05 |   q25 |   median |   mean |   q75 |   q95 |   max |    std |
|:-------------------|:-----------------------|------:|------:|------:|------:|---------:|-------:|------:|------:|------:|-------:|
| TotalRawScoreTRUE  | Confirmed PLE passer   | 31572 |    48 |    95 |   120 |      139 | 141.04 |   162 |   192 |   231 |  29.37 |
| TotalRawScoreTRUE  | No confirmed PLE match | 37888 |     9 |    70 |    94 |      114 |  116.2 |   136 |   170 |   223 |   30.5 |
| NMS_PER_num        | Confirmed PLE passer   | 30988 |    -1 |    15 |    45 |       69 |  64.56 |    88 |    98 |    99 |  26.33 |
| NMS_PER_num        | No confirmed PLE match | 37758 |    -1 |     2 |    15 |       38 |  42.06 |    66 |    93 |    99 |  29.54 |
| NMS_GPS            | Confirmed PLE passer   | 31581 |   200 |   399 |   489 |      552 | 555.86 |   624 |   723 |   800 |  97.66 |
| NMS_GPS            | No confirmed PLE match | 37922 |     0 |   293 |   399 |      470 | 471.63 |   545 |   653 |   800 | 108.92 |
| NMS_APT            | Confirmed PLE passer   | 31581 |   200 |   403 |   491 |      548 | 552.13 |   612 |   710 |   800 |  93.24 |
| NMS_APT            | No confirmed PLE match | 37922 |   200 |   316 |   415 |      484 | 480.26 |   546 |   645 |   800 | 101.18 |
| NMS_SA             | Confirmed PLE passer   | 31581 |   200 |   398 |   480 |      544 | 546.07 |   610 |   705 |   800 |  92.22 |
| NMS_SA             | No confirmed PLE match | 37922 |     0 |   318 |   406 |      471 | 474.14 |   539 |   641 |   800 |  98.26 |
| PartIRawScoreTRUE  | Confirmed PLE passer   | 31572 |    12 |    49 |    63 |       74 |  73.85 |    84 |    99 |   118 |  15.03 |
| PartIRawScoreTRUE  | No confirmed PLE match | 37888 |     0 |    36 |    51 |       62 |  61.89 |    73 |    90 |   116 |  16.31 |
| PartIIRawScoreTRUE | Confirmed PLE passer   | 31572 |    19 |    41 |    55 |       66 |  67.18 |    79 |    97 |   116 |  16.75 |
| PartIIRawScoreTRUE | No confirmed PLE match | 37888 |     0 |    31 |    42 |       52 |  54.31 |    65 |    85 |   118 |  16.53 |


---

## 3. Mann-Whitney U Tests: Confirmed PLE Passer vs No Confirmed Match

**Table 24. Mann-Whitney comparison**

| Score Variable     |   Median (No confirmed PLE match) |   Median (Confirmed PLE passer) |   U-statistic |   p-value |   Effect size (r) |    N1 |    N2 |
|:-------------------|----------------------------------:|--------------------------------:|--------------:|----------:|------------------:|------:|------:|
| Total Raw Score    |                               114 |                             139 |   3.33156e+08 |         0 |             0.443 | 37888 | 31572 |
| Percentile Rank    |                                38 |                              69 |   3.34426e+08 |         0 |            0.4284 | 37758 | 30988 |
| GPS Standard Score |                               470 |                             552 |   3.39564e+08 |         0 |            0.4329 | 37922 | 31581 |
| Part I Raw Score   |                                62 |                              74 |   3.54041e+08 |         0 |            0.4081 | 37888 | 31572 |
| Part II Raw Score  |                                52 |                              66 |   3.46502e+08 |         0 |            0.4207 | 37888 | 31572 |


---

## 4. PLE Linkage Rate by Percentile Bin

Within each percentile bin, the number of observable best records, confirmed PLE passers, and the linkage rate (%).

**Figure 21. PLE confirmed share by percentile bin**

| PercentileBin   |    n |   confirmed_passers |   linkage_rate_pct |
|:----------------|-----:|--------------------:|-------------------:|
| B1              | 6853 |                 795 |               11.6 |
| B2              | 5884 |                1336 |              22.71 |
| B3              | 5813 |                1703 |               29.3 |
| B4              | 6473 |                2330 |                 36 |
| B5              | 6582 |                3003 |              45.62 |
| B6              | 6284 |                3168 |              50.41 |
| B7              | 6359 |                3407 |              53.58 |
| B8              | 6704 |                3690 |              55.04 |
| B9              | 7263 |                4474 |               61.6 |
| B10             | 9958 |                7073 |              71.03 |


---

## 5a. Bin Composition by PLE Status (within-bin %)

Within each bin, the distribution of PLE statuses (row-wise percentages).

**Percent distribution of PLE status within each bin**

| PercentileBin   |   Confirmed PLE passer |   No confirmed PLE match |
|:----------------|-----------------------:|-------------------------:|
| B1              |                   11.6 |                     88.4 |
| B2              |                  22.71 |                    77.29 |
| B3              |                   29.3 |                     70.7 |
| B4              |                     36 |                       64 |
| B5              |                  45.62 |                    54.38 |
| B6              |                  50.41 |                    49.59 |
| B7              |                  53.58 |                    46.42 |
| B8              |                  55.04 |                    44.96 |
| B9              |                   61.6 |                     38.4 |
| B10             |                  71.03 |                    28.97 |


---

## 5b. PLE Status Distribution Across Bins (within-PLE-status %)

For each PLE status, the distribution across percentile bins (column-wise percentages).

**Bin distribution by PLE status**

| PLE_STATUS_LABEL       |    B1 |    B2 |    B3 |    B4 |   B5 |    B6 |   B7 |    B8 |    B9 |   B10 |
|:-----------------------|------:|------:|------:|------:|-----:|------:|-----:|------:|------:|------:|
| Confirmed PLE passer   |  2.57 |  4.31 |   5.5 |  7.52 | 9.69 | 10.23 |   11 | 11.91 | 14.44 | 22.83 |
| No confirmed PLE match | 16.29 | 12.23 | 11.05 | 11.14 | 9.62 |  8.38 | 7.94 |   8.1 |   7.5 |  7.76 |


---

## 6. Survival Rate to Top Bins (B8-B10) by Course Group

Share of examinees in each course group who scored in the top three percentile bins.

**Table 26. Course-group representation in top bins**

| UNDERGRAD_COURSE_GROUP       |   total_examinees |   top_bin_n |   survival_rate_pct |
|:-----------------------------|------------------:|------------:|--------------------:|
| Engineering & Technology     |               730 |         383 |               52.47 |
| Natural Sciences             |             40196 |       14760 |               36.72 |
| Other                        |              8248 |        2910 |               35.28 |
| Education                    |              3445 |        1160 |               33.67 |
| Medical & Allied             |             63468 |       18354 |               28.92 |
| Social & Behavioral Sciences |             15758 |        4485 |               28.46 |


---

## 7. Confirmed PLE Alignment by NMAT Year

Observable best records, confirmed passers, no match, and confirmed share by year.

**Table 28. Confirmed PLE alignment by NMAT year**

|   Year |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|-------:|----------------------------:|------------------------:|-------------------------:|--------------------------:|
|   2006 |                        3698 |                    2005 |                     1693 |                     54.22 |
|   2007 |                        3690 |                    1832 |                     1858 |                     49.65 |
|   2008 |                        4965 |                    2583 |                     2382 |                     52.02 |
|   2009 |                        7461 |                    3757 |                     3704 |                     50.36 |
|   2010 |                        8623 |                    4534 |                     4089 |                     52.58 |
|   2011 |                        8842 |                    3918 |                     4924 |                     44.31 |
|   2012 |                        9405 |                    4006 |                     5399 |                     42.59 |
|   2013 |                        9867 |                    4210 |                     5657 |                     42.67 |
|   2014 |                       12952 |                    4736 |                     8216 |                     36.57 |


---

## 8. Confirmed PLE Alignment by Pre-Med Background

Observable best records, confirmed passers, no match, confirmed share, and median percentile rank by course group.

**Table 29. Confirmed PLE alignment by course group**

| UNDERGRAD_COURSE_GROUP       |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Education                    |                        3188 |                    1699 |                     1489 |                     53.29 |                       53 |
| Other                        |                        6612 |                    3201 |                     3411 |                     48.41 |                       55 |
| Medical & Allied             |                       38144 |                   17833 |                    20311 |                     46.75 |                       48 |
| Natural Sciences             |                       16512 |                    6994 |                     9518 |                     42.36 |                       63 |
| Engineering & Technology     |                         318 |                     118 |                      200 |                     37.11 |                       71 |
| Social & Behavioral Sciences |                        4729 |                    1736 |                     2993 |                     36.71 |                       63 |


---

## 9. Confirmed PLE Alignment by University Type

Public, Private, and Foreign university types in the observable best-record cohort.

**Table 27. Confirmed PLE alignment by university type**

| UNDERGRAD_UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|:---------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|
| Foreign              |                        1159 |                     258 |                      901 |                     22.26 |
| Private              |                       52821 |                   23757 |                    29064 |                     44.98 |
| Public               |                       14642 |                    7226 |                     7416 |                     49.35 |


---

## 10. Top Percentile Scores by PLE Status

Top 20 records per PLE status, sorted by highest percentile rank.

**Record-level detail: highest percentile scores per PLE status**

| PERSON_KEY                                          |   APPNO_CLEAN |   Year |   TotalRawScoreTRUE |   NMS_PER_num |   NMS_GPS |   PartIRawScoreTRUE |   PartIIRawScoreTRUE | PercentileBin   | PLE_STATUS_LABEL       | UNDERGRAD_UNI_TYPE   | UNDERGRAD_COURSE_GROUP       |
|:----------------------------------------------------|--------------:|-------:|--------------------:|--------------:|----------:|--------------------:|---------------------:|:----------------|:-----------------------|:---------------------|:-----------------------------|
| ROJO, RANIV DAWEY||                                 |       1010366 |   2009 |                 203 |            99 |       738 |                 101 |                  102 | B10             | Confirmed PLE passer   | Public               | Other                        |
| ALEJO, GABRIEL IGNACIO PALMA||9/12/1990             |    1031204633 |   2012 |                 201 |            99 |       741 |                 106 |                   95 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| ALCANTARA, JEROME HERNANDEZ||11/13/1992             |    1121207717 |   2012 |                 182 |            99 |       741 |                  98 |                   84 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| ROQUE, VLADIMIR LENNIN ALCANTARA||                  |       1003529 |   2009 |                 200 |            99 |       732 |                  97 |                  103 | B10             | Confirmed PLE passer   | Public               | Natural Sciences             |
| YENSON, IVAN LENDLE CABANILLA||1/7/1996             |    1111407328 |   2014 |                 180 |            99 |       737 |                 100 |                   80 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| VILLARETE, NORMAN RAE TABLAN||01/25/1991            |    1041407434 |   2014 |                 183 |            99 |       746 |                  94 |                   89 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| VALERA, JUANCHO LORENZO SANTOS||6/10/1991           |    1111303883 |   2013 |                 192 |            99 |       751 |                  97 |                   95 | B10             | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| AUTENTICO, REYSA OMAY||                             |       1061792 |   2007 |                 201 |            99 |       741 |                  96 |                  105 | B10             | Confirmed PLE passer   | Public               | Education                    |
| MAGCALAS, ANNA RICO||09/24/1992                     |    1121000237 |   2010 |                 199 |            99 |       735 |                 105 |                   94 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| JAVIER, KENNETH ARVIOLA||                           |       1002247 |   2009 |                 216 |            99 |       795 |                 106 |                  110 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| MALANYAON, FREDA QUIMBA||5/5/1987                   |    1121001087 |   2010 |                 205 |            99 |       768 |                 108 |                   97 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| UY, JOHN HENRICK GOLAK||5/10/1994                   |    1111307461 |   2013 |                 187 |            99 |       733 |                  93 |                   94 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| VILLANGCA, DANIEL JR GONZALES||09/13/1993           |    1111312014 |   2013 |                 182 |            99 |       717 |                  97 |                   85 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| VILLANUEVA, JOHN CHRISTOPHER CONCEPCION||06/22/1994 |    1111309984 |   2013 |                 190 |            99 |       741 |                  92 |                   98 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| VILLANUEVA, MARK JHERVY SORIANO||01/30/1992         |    1041303851 |   2013 |                 197 |            99 |       726 |                 104 |                   93 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| SALISE, JOEANNE MARIE MAHINAY||                     |       1085671 |   2008 |                 199 |            99 |       738 |                 107 |                   92 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| ANG, FELICE KATRINA CASTRO||02/13/1993              |    1121208269 |   2012 |                 176 |            99 |       720 |                  99 |                   77 | B10             | Confirmed PLE passer   | Public               | Social & Behavioral Sciences |
| ANG, HARLEY GUERALD CO||03/25/1991                  |    1031200875 |   2012 |                 196 |            99 |       729 |                 102 |                   94 | B10             | Confirmed PLE passer   | Public               | Social & Behavioral Sciences |
| SALVAME, ERIKA JEAN ANG||                           |       1085695 |   2008 |                 201 |            99 |       749 |                 108 |                   93 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| SAN JUAN, MARI DES JIMENEZ||                        |       1085386 |   2008 |                 198 |            99 |       743 |                  95 |                  103 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| FLORANO, SOLMUELL MERCADO||12/27/1993               |    1111406933 |   2014 |                 179 |            99 |       733 |                  86 |                   93 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| YOUNG, JAMIE ROSLYN TIU||12/29/1994                 |    1111403809 |   2014 |                 182 |            99 |       751 |                  92 |                   90 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| CORPUZ, KATHLEEN BUENO||                            |       1073266 |   2007 |                 196 |            99 |       726 |                  94 |                  102 | B10             | No confirmed PLE match | Public               | Natural Sciences             |
| TE, JOHN CYNRIC TY||                                |       1072418 |   2007 |                 208 |            99 |       733 |                 101 |                  107 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| GARCIA, JOSEPH BENEDICT TION||09/19/1993            |    1041407093 |   2014 |                 183 |            99 |       746 |                 102 |                   81 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| ALCANTARA, KRISTIA BERNADINE LICUDINE||12/19/1994   |    1111403360 |   2014 |                 177 |            99 |       733 |                  88 |                   89 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| LUCERO, KIMBERLY BALIGUAT||1/10/1990                |    1121003765 |   2010 |                 198 |            99 |       732 |                  98 |                  100 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| DELOS REYES, MA KRISTINA JUAN||                     |       1082641 |   2007 |                 199 |            99 |       737 |                  93 |                  106 | B10             | No confirmed PLE match | Public               | Natural Sciences             |
| YANG, PETER||08/29/1993                             |    1111400534 |   2014 |                 199 |            99 |       737 |                 101 |                   98 | B10             | No confirmed PLE match | Public               | Natural Sciences             |
| LOPEZ, ALENNIE CHARMAINE LEONARDO||02/23/1991       |    1121001950 |   2010 |                 201 |            99 |       743 |                 106 |                   95 | B10             | No confirmed PLE match | Private              | Social & Behavioral Sciences |
| FERRER, FRANCO EMILE RAMIREZ||11/13/1991            |    1041407056 |   2014 |                 175 |            99 |       717 |                  93 |                   82 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| ENDOZO, ALLYSTER ARCEO||7/11/1991                   |    1121208475 |   2012 |                 180 |            99 |       733 |                  97 |                   83 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| ESPIRITU, ENRIQUE MIGUEL VERDE||6/4/1988            |    1031200596 |   2012 |                 200 |            99 |       741 |                 106 |                   94 | B10             | No confirmed PLE match | Private              | Other                        |
| ABERIN, MARVIN ANGELO ESTEBAN||3/6/1994             |    1111400643 |   2014 |                 183 |            99 |       751 |                  94 |                   89 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| ABUNDO, RACELA THERESE BUENCAMINO||7/3/1991         |    1041407593 |   2014 |                 182 |            99 |       741 |                  97 |                   85 | B10             | No confirmed PLE match | Private              | Social & Behavioral Sciences |
| GOH, RACHEL ANNE REYES||04/23/1991                  |        400721 |   2010 |                 208 |            99 |       733 |                 103 |                  105 | B10             | No confirmed PLE match | Public               | Natural Sciences             |
| PASCASIO, THEA KATRINA ANINAG||12/10/1992           |    1121000626 |   2010 |                 205 |            99 |       768 |                 107 |                   98 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| PLIMACO, FIL KRISTIAN BONDOC||08/14/1988            |    1121008392 |   2010 |                 197 |            99 |       728 |                 107 |                   90 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| GUZMAN, RUTH MARIAN SARRA||                         |       1071093 |   2006 |                 200 |            99 |       737 |                 100 |                  100 | B10             | No confirmed PLE match | Public               | Other                        |
| KIM, YUNGMIN||                                      |       1081037 |   2007 |                 194 |            99 |       720 |                  96 |                   98 | B10             | No confirmed PLE match | Private              | Natural Sciences             |

---



<a id="08-repeat-takers"></a>

**Generated:** 2026-07-31 16:32

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `trend (2006-2018, unfiltered)`

**Filters:** None (full unfiltered dataset)

---

## 1. Attempt Count Distribution

Number of unique NMAT applications per PERSON_KEY in the trend cohort.

**Table 31. Attempt-count distribution**

|   Attempts |   Count |   Percent |   CumulativePercent |
|-----------:|--------:|----------:|--------------------:|
|          1 |  101156 |        75 |                  75 |
|          2 |   25812 |     19.14 |               94.14 |
|          3 |    6046 |      4.48 |               98.62 |
|          4 |    1411 |      1.05 |               99.67 |
|          5 |     332 |      0.25 |               99.92 |
|          6 |      88 |      0.07 |               99.99 |
|          7 |      17 |      0.01 |                 100 |
|          8 |       6 |         0 |                 100 |
|          9 |       1 |         0 |                 100 |


Figure data: each row shows the number of persons with that many recorded NMAT attempts.


---

## 2. Repeat-Taker Summary

**Repeat-taker overview**

| Indicator                     |   Value |
|:------------------------------|--------:|
| Unique persons (PERSON_KEY)   |  134869 |
| Repeat takers (>1 attempt)    |   33713 |
| Repeat rate (%)               |      25 |
| Max attempts observed         |       9 |
| Mean attempts (all persons)   |    1.33 |
| Median attempts (all persons) |       1 |


---

## 3. Score Improvement: First vs Last Attempt

Among repeat takers with score data on both first and last attempt.

**Table 32. Repeat-taker trajectory summary**

| Indicator                       |   Value |
|:--------------------------------|--------:|
| Repeat-taker persons (analytic) |   33702 |
| Improved percentile rank (%)    |   77.65 |
| Improved raw score (%)          |   73.58 |
| Improved GPS (%)                |   78.83 |
| Median percentile change        |      11 |
| Median raw score change         |      12 |
| Median GPS change               |      46 |
| Mean percentile change          |   13.52 |
| Mean raw score change           |   13.15 |
| Mean GPS change                 |   47.29 |
| Q25 percentile change           |       2 |
| Q75 percentile change           |      25 |
| Q25 raw score change            |       0 |
| Q75 raw score change            |      26 |



### First-Last Detail (per person)

**Preview: first 100 of 33,702 rows (population: repeat takers with score data on both first and last attempt, n=33,702)**

| PERSON_KEY                                      |   n_attempts |   first_year |   last_year |   first_pct |   last_pct |   pct_improvement |   first_raw |   last_raw |   raw_improvement |   first_gps |   last_gps |   gps_improvement |
|:------------------------------------------------|-------------:|-------------:|------------:|------------:|-----------:|------------------:|------------:|-----------:|------------------:|------------:|-----------:|------------------:|
| ANGLOPEZ, MAE THERESE DE JOSE||                 |            2 |         2009 |        2010 |           0 |         94 |                94 |         189 |        189 |                 0 |           0 |        658 |               658 |
| SAAYA SANTHOSH||04/19/1996                      |            2 |         2016 |        2017 |          -1 |         88 |                89 |          51 |        170 |               119 |         200 |        615 |               415 |
| STO DOMINGO, WEIJIN N A||06/20/1994             |            2 |         2013 |        2013 |          12 |         99 |                87 |          96 |        184 |                88 |         383 |        723 |               340 |
| CEREZO, HARRY JOHN||                            |            2 |         2009 |        2010 |           0 |         87 |                87 |         176 |        176 |                 0 |           0 |        613 |               613 |
| ADECER, HANICOLE MORTIZ||                       |            2 |         2007 |        2008 |           7 |         93 |                86 |          78 |        178 |               100 |         355 |        645 |               290 |
| KOTHURU, PENIEL GOSPEL GLORY,||7/6/1996         |            2 |         2014 |        2015 |           3 |         87 |                84 |          74 |        160 |                86 |         316 |        615 |               299 |
| VILLENA, MICHAEL BERNARD SALUD||11/2/1995       |            6 |         2013 |        2017 |           2 |         85 |                83 |          72 |        165 |                93 |         302 |        602 |               300 |
| AUSTRIA, RITA ISABELLE TALAVERA||5/5/1994       |            3 |         2013 |        2014 |          15 |         98 |                83 |          92 |        171 |                79 |         398 |        708 |               310 |
| MAHESH JESU RAJA, ALLEN ROJER||09/24/1996       |            2 |         2015 |        2015 |           1 |         84 |                83 |          64 |        141 |                77 |         243 |        597 |               354 |
| ANUKU, EDNA OMAMUYOVWI||3/5/1976                |            3 |         2016 |        2018 |           6 |         89 |                83 |          75 |        148 |                73 |         347 |        622 |               275 |
| VINARAO, QUERUBIN JADE OLANGCO||7/1/1993        |            3 |         2013 |        2014 |           5 |         88 |                83 |          80 |        146 |                66 |         337 |        618 |               281 |
| GADHAVI, LAKHAMA MANGABHAI||11/8/1993           |            3 |         2014 |        2015 |           1 |         82 |                81 |          66 |        153 |                87 |         264 |        592 |               328 |
| JONGRATANAVANICH, WATCHARAPORN||1/4/1984        |            3 |         2012 |        2014 |           4 |         85 |                81 |          78 |        142 |                64 |         327 |        603 |               276 |
| PRADO, JOSE PAOLO BARAWID||06/18/1994           |            2 |         2013 |        2014 |          10 |         91 |                81 |          87 |        150 |                63 |         373 |        635 |               262 |
| SINGH, SHRISTI||9/7/1995                        |            2 |         2014 |        2015 |          -1 |         79 |                80 |          55 |        150 |                95 |         212 |        582 |               370 |
| THAMBI, PRIYANKA USHA||05/19/1992               |            3 |         2011 |        2013 |           1 |         81 |                80 |          62 |        152 |                90 |         271 |        589 |               318 |
| BAMBHAROLIYA, VIVEK BIPINBHAI||10/24/1994       |            5 |         2013 |        2017 |           6 |         86 |                80 |          81 |        168 |                87 |         348 |        610 |               262 |
| ANSARI, SAJJAD HUSSAIN||04/15/1995              |            2 |         2017 |        2018 |           4 |         84 |                80 |          83 |        142 |                59 |         322 |        599 |               277 |
| CHAUDHARY, ANIL JESUNGBHAI||08/26/1994          |            6 |         2014 |        2017 |           4 |         83 |                79 |          73 |        164 |                91 |         321 |        597 |               276 |
| PATEL, NENSI HASMUKHBHAI||12/28/1997            |            3 |         2016 |        2017 |           1 |         80 |                79 |          73 |        159 |                86 |         275 |        583 |               308 |
| VENKATASAMY, ELAVARASAN||01/21/1998             |            2 |         2015 |        2015 |           2 |         81 |                79 |          74 |        137 |                63 |         293 |        586 |               293 |
| REKHA, PRAVARDHINI REDDY||05/31/1994            |            2 |         2014 |        2015 |           1 |         79 |                78 |          65 |        150 |                85 |         259 |        582 |               323 |
| THAKKAR, KARAN SURESHKUMAR||6/9/1996            |            2 |         2014 |        2015 |           3 |         81 |                78 |          71 |        153 |                82 |         307 |        589 |               282 |
| AGUILERA, EARIC SY||7/7/1995                    |            5 |         2015 |        2017 |           7 |         85 |                78 |          87 |        166 |                79 |         352 |        604 |               252 |
| HABILING, KAVIN BIDANG||05/18/1992              |            6 |         2012 |        2015 |          14 |         92 |                78 |          91 |        168 |                77 |         393 |        639 |               246 |
| VALLABHANENI, SWETHA||1/10/1996                 |            2 |         2015 |        2015 |           5 |         83 |                78 |          84 |        140 |                56 |         333 |        594 |               261 |
| GAMOT, SANDESH LALIT||08/15/1992                |            2 |         2013 |        2015 |          12 |         89 |                77 |          89 |        164 |                75 |         383 |        625 |               242 |
| GARANIYA, VISHAL BAHADURBHAI||03/24/1996        |            3 |         2014 |        2015 |           3 |         80 |                77 |          75 |        136 |                61 |         310 |        583 |               273 |
| RAJKUMAR, GIFTSON JOHN||03/29/1997              |            2 |         2015 |        2015 |           1 |         78 |                77 |          73 |        134 |                61 |         280 |        577 |               297 |
| LEE, JI HWAN||4/1/1999                          |            2 |         2017 |        2018 |          14 |         91 |                77 |          99 |        152 |                53 |         391 |        635 |               244 |
| ESCUETA, ALEXANDRIA VILLARICO||10/15/1993       |            4 |         2013 |        2015 |           2 |         78 |                76 |          75 |        148 |                73 |         293 |        579 |               286 |
| JAIN, SHUBHAM SUNIL||05/21/1996                 |            2 |         2015 |        2015 |          -1 |         75 |                76 |          60 |        131 |                71 |         212 |        568 |               356 |
| GANDLA, SUDHEER KUMAR||9/6/1989                 |            2 |         2010 |        2012 |           6 |         82 |                76 |          83 |        140 |                57 |         345 |        592 |               247 |
| BELIM, FATIMA ABDULKARIM||05/13/1997            |            2 |         2016 |        2017 |           1 |         76 |                75 |          61 |        154 |                93 |         274 |        572 |               298 |
| DEQUITO, KRISTEL JOY LINAO||5/9/1994            |            4 |         2015 |        2017 |           3 |         78 |                75 |          66 |        156 |                90 |         304 |        578 |               274 |
| KARANAM, LALITHA SAI SREE||2/8/1996             |            3 |         2014 |        2015 |           1 |         76 |                75 |          65 |        147 |                82 |         259 |        572 |               313 |
| MACATIGUE, MONIQUE BANTUG||12/17/1992           |            2 |         2012 |        2017 |           5 |         80 |                75 |          79 |        158 |                79 |         333 |        585 |               252 |
| RAJULAPATI, GOVINDARAJA||05/13/1996             |            3 |         2014 |        2015 |           2 |         77 |                75 |          70 |        147 |                77 |         288 |        575 |               287 |
| THAKOR, JAIMINI GULABSINH||09/22/1996           |            2 |         2014 |        2015 |           7 |         82 |                75 |          78 |        153 |                75 |         352 |        592 |               240 |
| KOPPOLU, SOWMITRA PALLAV||08/29/1993            |            3 |         2014 |        2015 |          -1 |         74 |                75 |          56 |        130 |                74 |         200 |        565 |               365 |
| BELLAMKONDA, AJAY KUMAR||9/8/1994               |            2 |         2012 |        2013 |           4 |         79 |                75 |          77 |        140 |                63 |         321 |        582 |               261 |
| BEARIS, NIKKI JILL NIEVA||06/30/1993            |            2 |         2013 |        2014 |           9 |         84 |                75 |          86 |        142 |                56 |         368 |        599 |               231 |
| DIALOGO, AL GIAN MENDOZA||08/31/1993            |            2 |         2014 |        2015 |           9 |         84 |                75 |          85 |        141 |                56 |         368 |        597 |               229 |
| BERNASOL, SANTIA LOUISE YABUT||10/6/1992        |            2 |         2013 |        2014 |          13 |         88 |                75 |          90 |        145 |                55 |         388 |        618 |               230 |
| MANZANO, ALLEN JANE BLANDO||3/1/1994            |            2 |         2016 |        2017 |          10 |         84 |                74 |          80 |        164 |                84 |         370 |        599 |               229 |
| KARANAM, HARSHA JEEVAN KISHORE||2/8/1996        |            3 |         2014 |        2015 |           9 |         83 |                74 |          85 |        155 |                70 |         363 |        596 |               233 |
| KURLI, RAJEEV REDDY||10/8/1995                  |            3 |         2014 |        2015 |          10 |         84 |                74 |          87 |        155 |                68 |         373 |        599 |               226 |
| BOMMA REDDY, SAI SRI KRISHNA REDDY||5/1/1996    |            2 |         2014 |        2014 |           1 |         75 |                74 |          69 |        130 |                61 |         280 |        568 |               288 |
| CRUZ, JOHN PAUL MAGHIRANG||11/12/1992           |            2 |         2012 |        2013 |           8 |         82 |                74 |          84 |        144 |                60 |         357 |        592 |               235 |
| DIVINAGRACIA, BRIAN JOHN DIAZ||11/4/1992        |            2 |         2012 |        2014 |          18 |         92 |                74 |          94 |        151 |                57 |         407 |        639 |               232 |
| HIDALGO, JEDD JOSE MICKAEL MADRONIO||01/21/1993 |            3 |         2013 |        2015 |           9 |         83 |                74 |          85 |        140 |                55 |         363 |        594 |               231 |
| GATDULA, EMANUEL FETIZA||11/28/1992             |            2 |         2013 |        2015 |          18 |         91 |                73 |          94 |        168 |                74 |         407 |        635 |               228 |
| MARQUINO, ALYANA FRANCESCA BAUTISTA||3/4/1995   |            3 |         2014 |        2015 |          18 |         91 |                73 |          94 |        165 |                71 |         407 |        632 |               225 |
| PACKIAMUTHU, PRISHKA||06/15/1997                |            2 |         2015 |        2015 |          -1 |         72 |                73 |          57 |        128 |                71 |         200 |        559 |               359 |
| DY, FRECHELLE LAINE TACTAY||12/11/1991          |            2 |         2012 |        2013 |           6 |         79 |                73 |          81 |        150 |                69 |         343 |        582 |               239 |
| KATTA, REVANTH||03/25/1996                      |            2 |         2014 |        2015 |           6 |         79 |                73 |          82 |        150 |                68 |         348 |        582 |               234 |
| BORRA, RAVALI||01/28/1996                       |            2 |         2015 |        2015 |          18 |         91 |                73 |         100 |        153 |                53 |         407 |        633 |               226 |
| GERONIMO, MONA LEIGH LEVISTE||03/24/1992        |            5 |         2011 |        2013 |          27 |         99 |                72 |         105 |        197 |                92 |         439 |        726 |               287 |
| VYAS, SMIT NILESHKUMAR||07/31/1995              |            2 |         2014 |        2015 |          -1 |         71 |                72 |          57 |        143 |                86 |         212 |        557 |               345 |
| BAWANKAR, SUMIT SUNIL||12/11/1994               |            3 |         2016 |        2017 |           8 |         80 |                72 |          90 |        160 |                70 |         356 |        585 |               229 |
| TUMAMPOS, BEA DESIREE DE LEON||8/9/1993         |            2 |         2012 |        2014 |          23 |         95 |                72 |          98 |        159 |                61 |         425 |        663 |               238 |
| ALCAZAREN, PETERSIAN MAGSULIT||2/9/1993         |            3 |         2012 |        2014 |          21 |         93 |                72 |          97 |        155 |                58 |         420 |        645 |               225 |
| BEERAM, SHIRISHA||11/12/1992                    |            2 |         2014 |        2014 |           5 |         77 |                72 |          79 |        134 |                55 |         333 |        575 |               242 |
| VALA, JAYDIP KALA||11/29/1999                   |            2 |         2017 |        2018 |           6 |         78 |                72 |          89 |        136 |                47 |         347 |        579 |               232 |
| PILAPIL, LUCILLE PILLAR DESCALLAR||9/10/1995    |            2 |         2016 |        2017 |          26 |         97 |                71 |          97 |        191 |                94 |         435 |        686 |               251 |
| JIMENEZ, RUFFA DAWN OLIVA||05/22/1994           |            2 |         2015 |        2016 |           2 |         73 |                71 |          63 |        152 |                89 |         286 |        560 |               274 |
| ASPIRAS, JENNIFER SIGRID PERALTA||7/6/1995      |            3 |         2015 |        2017 |           2 |         73 |                71 |          64 |        151 |                87 |         292 |        560 |               268 |
| CUEVA, JEMELA MAXINE DELA CRUZ||6/2/1995        |            3 |         2015 |        2017 |           2 |         73 |                71 |          64 |        151 |                87 |         292 |        562 |               270 |
| TAN, RAINEER ALAINE JAY CAPCO||9/12/1996        |            2 |         2016 |        2017 |           3 |         74 |                71 |          68 |        152 |                84 |         313 |        565 |               252 |
| ARMENDARES, YOCHA BELLE PAGTANAC||06/28/1994    |            3 |         2015 |        2017 |           8 |         79 |                71 |          76 |        158 |                82 |         357 |        580 |               223 |
| BELADIYA, MAHIPAL KISHORBHAI||10/29/1994        |            5 |         2013 |        2017 |           3 |         74 |                71 |          72 |        152 |                80 |         307 |        565 |               258 |
| BHELE, TRISHA||1/10/1993                        |            2 |         2012 |        2013 |           2 |         73 |                71 |          70 |        142 |                72 |         288 |        560 |               272 |
| OBALDO, JEZREEL MAE JIMENEZ||02/20/1996         |            3 |         2016 |        2018 |          17 |         88 |                71 |          89 |        161 |                72 |         406 |        620 |               214 |
| PETER, LIDIYA||10/8/1996                        |            2 |         2015 |        2015 |          -1 |         70 |                71 |          60 |        126 |                66 |         212 |        552 |               340 |
| COMENDADOR, MAIU LIWEN BURDIOS||6/5/1992        |            3 |         2013 |        2018 |           5 |         76 |                71 |          79 |        134 |                55 |         337 |        572 |               235 |
| MANGROBANG, RAUL JR RAMOS||6/9/1993             |            2 |         2013 |        2013 |          16 |         87 |                71 |          98 |        151 |                53 |         402 |        615 |               213 |
| GANTA, RAVITEJA||10/6/1995                      |            2 |         2014 |        2014 |          10 |         81 |                71 |          87 |        138 |                51 |         373 |        589 |               216 |
| ONG, CINDY LIU||01/31/1992                      |            3 |         2013 |        2014 |           3 |         74 |                71 |          82 |        132 |                50 |         316 |        564 |               248 |
| PATIL, SUBODH PANKAJ||8/3/1997                  |            2 |         2017 |        2018 |          21 |         92 |                71 |         106 |        153 |                47 |         421 |        639 |               218 |
| VADDEBOINA, SAI KRISHNA GOWD||05/14/1996        |            2 |         2015 |        2015 |           9 |         80 |                71 |          90 |        136 |                46 |         363 |        583 |               220 |
| DE LEON, CLAUDETTE PEARL||10/4/1995             |            3 |         2015 |        2017 |           4 |         74 |                70 |          70 |        152 |                82 |         328 |        565 |               237 |
| REGIS, REINA KATRINA SIEGA||01/21/1995          |            2 |         2016 |        2017 |          10 |         80 |                70 |          80 |        157 |                77 |         370 |        583 |               213 |
| INOCENCIO, MAY ANNE SEBELO||05/25/1995          |            3 |         2015 |        2016 |           3 |         73 |                70 |          79 |        152 |                73 |         310 |        560 |               250 |
| BUTRON, GEA CASTRO||4/9/1995                    |            2 |         2016 |        2018 |          26 |         96 |                70 |          97 |        163 |                66 |         435 |        673 |               238 |
| KORRA, BHASKAR NAIK||06/15/1992                 |            2 |         2014 |        2014 |           3 |         73 |                70 |          74 |        129 |                55 |         307 |        560 |               253 |
| GUNREDDY, MAMATHA REDDY||3/10/1995              |            2 |         2014 |        2014 |           7 |         77 |                70 |          83 |        135 |                52 |         352 |        575 |               223 |
| JADEJA, KULDIPSINH RANCHHODJI||1/9/1995         |            2 |         2013 |        2014 |          10 |         80 |                70 |          87 |        138 |                51 |         373 |        585 |               212 |
| VENNU, DIVYA||8/6/1996                          |            2 |         2015 |        2015 |          11 |         81 |                70 |          95 |        138 |                43 |         378 |        589 |               211 |
| CABANES, EENA ROSELLE TAN||05/17/1995           |            4 |         2015 |        2017 |          19 |         88 |                69 |          87 |        170 |                83 |         412 |        615 |               203 |
| OROPEL, ABBY GALE QUIMPO||05/26/1995            |            2 |         2015 |        2017 |          17 |         86 |                69 |          85 |        167 |                82 |         403 |        607 |               204 |
| GUGAR, CHANDRA PRAKASH||10/12/1998              |            2 |         2016 |        2017 |           9 |         78 |                69 |          79 |        157 |                78 |         366 |        578 |               212 |
| LAKHANI, ARMAN SHAUKATBHAI||07/27/1996          |            4 |         2015 |        2017 |          11 |         80 |                69 |          80 |        157 |                77 |         378 |        583 |               205 |
| DHAPA, YASHVANT MEGHJIBHAI||07/29/1993          |            2 |         2012 |        2013 |           2 |         71 |                69 |          70 |        143 |                73 |         288 |        557 |               269 |
| VIRTUSIO, GIAN HARLHEY BELARMINO||06/27/1995    |            2 |         2015 |        2016 |          10 |         79 |                69 |          93 |        159 |                66 |         373 |        580 |               207 |
| FRONDA, PRECIOUS MARLYNNE NOBLE||12/1/1992      |            2 |         2012 |        2013 |          12 |         81 |                69 |          89 |        152 |                63 |         383 |        589 |               206 |
| VITTO, HANNAH LERI LUMANGLAS||09/14/1992        |            3 |         2014 |        2015 |          10 |         79 |                69 |          87 |        150 |                63 |         373 |        582 |               209 |
| LABAY, ANGELO VIOLO GO||05/21/1993              |            3 |         2012 |        2014 |          23 |         92 |                69 |          98 |        153 |                55 |         425 |        639 |               214 |
| REYES, LOUISA CARMINA REJANO||8/2/1994          |            3 |         2013 |        2015 |          16 |         85 |                69 |         100 |        154 |                54 |         402 |        603 |               201 |
| GAUTAM, BIBEK||5/6/1992                         |            3 |         2012 |        2015 |           6 |         75 |                69 |          81 |        131 |                50 |         343 |        568 |               225 |
| VIRPARIA, DARVIN GIRISHBHAI||08/14/1996         |            2 |         2015 |        2015 |           3 |         72 |                69 |          79 |        128 |                49 |         310 |        559 |               249 |

> Full detail: [08_first_last_detail.csv](08_first_last_detail.csv) (33,702 rows, 13 cols)


---

## 4. Distribution of Attempt Counts by Year

For each test year, the number of persons with 1, 2, 3, ... attempts in that year.

**Attempt counts per year**

|   Year |   1 attempt(s) |   2 attempt(s) |   total_persons |
|-------:|---------------:|---------------:|----------------:|
|   2006 |           3860 |            258 |            4118 |
|   2007 |           4101 |            277 |            4378 |
|   2008 |           5410 |            355 |            5765 |
|   2009 |           7312 |            525 |            7837 |
|   2010 |          10008 |            276 |           10284 |
|   2011 |          10593 |            668 |           11261 |
|   2012 |          11626 |            847 |           12473 |
|   2013 |          12034 |            977 |           13011 |
|   2014 |          12309 |           1262 |           13571 |
|   2015 |          13590 |           1347 |           14937 |
|   2016 |          16034 |           2467 |           18501 |
|   2017 |          25870 |              0 |           25870 |
|   2018 |          19825 |           3918 |           23743 |


---

## 5. Repeat-Taker Detail (All Attempts)

All recorded attempts for persons with more than one NMAT application.

**Preview: first 100 rows**

| PERSON_KEY                                        |   APPNO_CLEAN |   Year |   TotalRawScoreTRUE |   NMS_PER_num |   NMS_GPS |   PartIRawScoreTRUE |   PartIIRawScoreTRUE | PercentileBin   | PLE_STATUS_LABEL       | UNDERGRAD_UNI_TYPE   | UNDERGRAD_COURSE_GROUP       |
|:--------------------------------------------------|--------------:|-------:|--------------------:|--------------:|----------:|--------------------:|---------------------:|:----------------|:-----------------------|:---------------------|:-----------------------------|
| AARE, VYSHNAVI||11/1/1996                         |    1041607270 |   2016 |                  90 |             8 |       356 |                  46 |                   44 | B1              | No confirmed PLE match | Private              | Natural Sciences             |
| AARE, VYSHNAVI||11/1/1996                         |    1101605950 |   2016 |                  92 |            20 |       417 |                  42 |                   50 | B3              | No confirmed PLE match | Public               | Natural Sciences             |
| AARON, GLEN ANTON TANGHAL||05/28/1992             |    1121210429 |   2012 |                 129 |            70 |       552 |                  65 |                   64 | B8              | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| AARON, GLEN ANTON TANGHAL||05/28/1992             |    1111302740 |   2013 |                 126 |            60 |       525 |                  71 |                   55 | B7              | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABABA, ERICA OCHADA||3/6/1993                     |    1111405756 |   2014 |                 104 |            35 |       460 |                  58 |                   46 | B4              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABABA, ERICA OCHADA||3/6/1993                     |    1031505145 |   2015 |                 132 |            60 |       525 |                  70 |                   62 | B7              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABABAO, KEESHIA MARI YBARZABAL||10/3/1992         |    1121200934 |   2012 |                 103 |            30 |       448 |                  55 |                   48 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABABAO, KEESHIA MARI YBARZABAL||10/3/1992         |    1041300511 |   2013 |                 129 |            54 |       510 |                  68 |                   61 | B6              | No confirmed PLE match | Private              | Medical & Allied             |
| ABACAN, AIRAH GIZELLE ALCOMENDAS||9/2/1993        |    1111304744 |   2013 |                 109 |            36 |       464 |                  69 |                   40 | B4              | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABACAN, AIRAH GIZELLE ALCOMENDAS||9/2/1993        |    1111403363 |   2014 |                 138 |            80 |       585 |                  79 |                   59 | B9              | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABACAN, MARIELLE JELINNE DEL ROSARIO||06/16/1991  |    1121006939 |   2010 |                 111 |            32 |       454 |                  64 |                   47 | B4              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABACAN, MARIELLE JELINNE DEL ROSARIO||06/16/1991  |    1111302610 |   2013 |                 116 |            48 |       494 |                  72 |                   44 | B5              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABACAN, MARIELLE JELINNE DEL ROSARIO||06/16/1991  |    1041401433 |   2014 |                 129 |            70 |       552 |                  71 |                   58 | B8              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABACAN, REMY JOY GUTIERREZ||06/15/1992            |    1111311636 |   2013 |                 118 |            49 |       498 |                  66 |                   52 | B5              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABACAN, REMY JOY GUTIERREZ||06/15/1992            |    1041407068 |   2014 |                 118 |            54 |       510 |                  62 |                   56 | B6              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD SANTOS, NICOLE ANNE TUMANG||04/30/1994       |    1111407959 |   2014 |                 149 |            89 |       625 |                  80 |                   69 | B9              | No confirmed PLE match | Public               | Social & Behavioral Sciences |
| ABAD SANTOS, NICOLE ANNE TUMANG||04/30/1994       |    1101509037 |   2015 |                 147 |            88 |       616 |                  92 |                   55 | B9              | No confirmed PLE match | Private              | Social & Behavioral Sciences |
| ABAD, AARON ADOLF RAMOS||02/18/1992               |    1031202069 |   2012 |                 156 |            81 |       586 |                  73 |                   83 | B9              | No confirmed PLE match | Public               | Medical & Allied             |
| ABAD, AARON ADOLF RAMOS||02/18/1992               |    1121208977 |   2012 |                 155 |            93 |       645 |                  71 |                   84 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| ABAD, ADDIELOU FIDELFIO ESPINA||08/21/1993        |    1041602789 |   2016 |                 144 |            64 |       537 |                  75 |                   69 | B7              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, ADDIELOU FIDELFIO ESPINA||08/21/1993        |    1031706452 |   2017 |                 169 |            87 |       613 |                  91 |                   78 | B9              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, AINA GENE CRUZ||06/25/1997                  |    1031700678 |   2017 |                 115 |            32 |       452 |                  56 |                   59 | B4              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAD, AINA GENE CRUZ||06/25/1997                  |    1031807544 |   2018 |                  80 |             5 |       337 |                  54 |                   26 | B1              | No confirmed PLE match | Public               | Natural Sciences             |
| ABAD, AINA GENE CRUZ||06/25/1997                  |    1101809800 |   2018 |                 102 |            33 |       457 |                  54 |                   48 | B4              | No confirmed PLE match | Public               | Natural Sciences             |
| ABAD, ALBERT CAISIP||09/28/1990                   |    2121003323 |   2010 |                 131 |            56 |       514 |                  65 |                   66 | B6              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAD, ALBERT CAISIP||09/28/1990                   |        400428 |   2010 |                 105 |            16 |       399 |                  52 |                   53 | B2              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABAD, ANGELLIE NIKKA SALIVIO||7/10/1996           |    1031800980 |   2018 |                 152 |            91 |       635 |                  90 |                   62 | B10             | No confirmed PLE match | Public               | Other                        |
| ABAD, ANGELLIE NIKKA SALIVIO||7/10/1996           |    1101801542 |   2018 |                 150 |            81 |       586 |                  86 |                   64 | B9              | No confirmed PLE match | Public               | Other                        |
| ABAD, ISRAEL CONRAD PORNOSDORO||01/18/1990        |    1121203499 |   2012 |                  96 |            20 |       416 |                  58 |                   38 | B3              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, ISRAEL CONRAD PORNOSDORO||01/18/1990        |    1041301655 |   2013 |                 121 |            43 |       481 |                  63 |                   58 | B5              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, JAKES KATHERIENE BATUL||12/11/1991          |    1041301575 |   2013 |                  90 |             8 |       357 |                  49 |                   41 | B1              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, JAKES KATHERIENE BATUL||12/11/1991          |    1111304338 |   2013 |                  98 |            21 |       420 |                  55 |                   43 | B3              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, JAKES KATHERIENE BATUL||12/11/1991          |    1041404814 |   2014 |                  99 |            24 |       430 |                  58 |                   41 | B3              | Confirmed PLE passer   | Public               | Medical & Allied             |
| ABAD, JAMAICA LORRAINE UGAY||07/22/1995           |    1101602457 |   2016 |                 141 |            73 |       562 |                  61 |                   80 | B8              | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABAD, JAMAICA LORRAINE UGAY||07/22/1995           |    1031710940 |   2017 |                 177 |            92 |       640 |                  93 |                   84 | B10             | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABAD, JAN CHESTER IGANO||01/31/1993               |    1121211000 |   2012 |                 123 |            62 |       529 |                  68 |                   55 | B7              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, JAN CHESTER IGANO||01/31/1993               |    1041402593 |   2014 |                 163 |            96 |       673 |                  91 |                   72 | B10             | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, JOSEPH ZACHARY MORA||7/1/1989               |    1121005871 |   2010 |                 137 |            63 |       532 |                  69 |                   68 | B7              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, JOSEPH ZACHARY MORA||7/1/1989               |    1041403168 |   2014 |                 146 |            87 |       615 |                  82 |                   64 | B9              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, JOYCE ANNE ACEBUQUE||09/28/1994             |    1111407366 |   2014 |                 105 |            36 |       464 |                  69 |                   36 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, JOYCE ANNE ACEBUQUE||09/28/1994             |    1041607154 |   2016 |                 123 |            38 |       471 |                  76 |                   47 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, KATHERINE ALARCON||05/30/1992               |    1121106602 |   2011 |                 162 |            83 |       595 |                  92 |                   70 | B9              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABAD, KATHERINE ALARCON||05/30/1992               |    1121204426 |   2012 |                 156 |            93 |       649 |                  84 |                   72 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABAD, KRISTELLE ROBARO||10/22/1994                |    1121203659 |   2012 |                 115 |            49 |       498 |                  70 |                   45 | B5              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAD, KRISTELLE ROBARO||10/22/1994                |    1041303800 |   2013 |                 141 |            70 |       552 |                  74 |                   67 | B8              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAD, KRISTELLE ROBARO||10/22/1994                |    1111305415 |   2013 |                 126 |            62 |       529 |                  67 |                   59 | B7              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAD, LIANNE JOY BRILLANTES||10/28/1994           |    1041403511 |   2014 |                 134 |            76 |       572 |                  64 |                   70 | B8              | No confirmed PLE match | Public               | Medical & Allied             |
| ABAD, LIANNE JOY BRILLANTES||10/28/1994           |    1101811332 |   2018 |                 141 |            73 |       562 |                  78 |                   63 | B8              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, MARK MELCHOR GONZAGA||01/22/1995            |    1101612939 |   2016 |                 131 |            64 |       536 |                  67 |                   64 | B7              | No confirmed PLE match | Public               | Medical & Allied             |
| ABAD, MARK MELCHOR GONZAGA||01/22/1995            |    1031800631 |   2018 |                 140 |            82 |       592 |                  77 |                   63 | B9              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, MARLYN ANNE GARCIA||08/15/1992              |    1111402055 |   2014 |                 119 |            55 |       514 |                  67 |                   52 | B6              | Confirmed PLE passer   | Public               | Medical & Allied             |
| ABAD, MARLYN ANNE GARCIA||08/15/1992              |    1031502348 |   2015 |                 134 |            63 |       533 |                  74 |                   60 | B7              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, MONIQUE BANTIQUE||5/7/1996                  |    1101605899 |   2016 |                 111 |            43 |       482 |                  63 |                   48 | B5              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABAD, MONIQUE BANTIQUE||5/7/1996                  |    1031701653 |   2017 |                 150 |            72 |       557 |                  92 |                   58 | B8              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABAD, NICOLE MAE GATCHALIAN||05/14/1997           |    1101612938 |   2016 |                  97 |            26 |       435 |                  50 |                   47 | B3              | No confirmed PLE match | Public               | Medical & Allied             |
| ABAD, NICOLE MAE GATCHALIAN||05/14/1997           |    1031810771 |   2018 |                 131 |            73 |       560 |                  78 |                   53 | B8              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, SHEENA POSADAS||2/3/1999                    |    1031812803 |   2018 |                 103 |            30 |       448 |                  60 |                   43 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, SHEENA POSADAS||2/3/1999                    |    1101815201 |   2018 |                 133 |            67 |       544 |                  73 |                   60 | B7              | No confirmed PLE match | Private              | Medical & Allied             |
| ABADAM, EDELYN JOY MACADAAN||                     |       1060229 |   2006 |                 156 |            81 |       589 |                  80 |                   76 | B9              | No confirmed PLE match | Public               | Education                    |
| ABADAM, EDELYN JOY MACADAAN||                     |       1071890 |   2006 |                 164 |            85 |       604 |                  85 |                   79 | B9              | No confirmed PLE match | Public               | Education                    |
| ABADIANO, MISHAEL PACHECO||09/24/1995             |    1041401616 |   2014 |                  94 |            18 |       407 |                  48 |                   46 | B2              | No confirmed PLE match | Private              | Medical & Allied             |
| ABADIANO, MISHAEL PACHECO||09/24/1995             |    1101501771 |   2015 |                 105 |            43 |       483 |                  54 |                   51 | B5              | No confirmed PLE match | Private              | Medical & Allied             |
| ABADILLA, AARON AMIL ACEDO||                      |       1002267 |   2009 |                 150 |            74 |       565 |                  78 |                   72 | B8              | No confirmed PLE match | Private              | Natural Sciences             |
| ABADILLA, AARON AMIL ACEDO||                      |        411398 |   2010 |                 155 |            70 |       552 |                  86 |                   69 | B8              | No confirmed PLE match | Private              | Other                        |
| ABADILLA, ANGELA MARIE OROPESA||09/15/1984        |    1041300965 |   2013 |                  66 |             1 |       249 |                  35 |                   31 | B1              | No confirmed PLE match | Private              | Medical & Allied             |
| ABADILLA, ANGELA MARIE OROPESA||09/15/1984        |    1111308784 |   2013 |                  66 |             1 |       271 |                  39 |                   27 | B1              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAGAT, RICK JEYRALD MAGALONG||1/12/1991          |    1121108573 |   2011 |                 118 |            38 |       469 |                  66 |                   52 | B4              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAGAT, RICK JEYRALD MAGALONG||1/12/1991          |    1111300139 |   2013 |                 124 |            59 |       522 |                  71 |                   53 | B6              | Confirmed PLE passer   | Public               | Medical & Allied             |
| ABAGAT, RICK JEYRALD MAGALONG||1/12/1991          |    1041400668 |   2014 |                 129 |            70 |       552 |                  72 |                   57 | B8              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAH, RAZHIDA NAZ||1/3/1995                       |    1041608083 |   2016 |                  93 |             9 |       367 |                  52 |                   41 | B1              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAH, RAZHIDA NAZ||1/3/1995                       |    1031815017 |   2018 |                  71 |             2 |       293 |                  45 |                   26 | B1              | No confirmed PLE match | Public               | Medical & Allied             |
| ABAIGAR, MELANIE CHRISTINE CELESTIAL||12/21/1995  |    1101504814 |   2015 |                  99 |            35 |       461 |                  50 |                   49 | B4              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAIGAR, MELANIE CHRISTINE CELESTIAL||12/21/1995  |    1101606653 |   2016 |                 101 |            31 |       450 |                  57 |                   44 | B4              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAIGAR, MELANIE CHRISTINE CELESTIAL||12/21/1995  |    1031708015 |   2017 |                 150 |            73 |       560 |                  71 |                   79 | B8              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAIGAR, MIGUEL III CELESTIAL||5/8/1992           |    1111305543 |   2013 |                  99 |            23 |       425 |                  55 |                   44 | B3              | No confirmed PLE match | Private              | Other                        |
| ABAIGAR, MIGUEL III CELESTIAL||5/8/1992           |    1031706303 |   2017 |                 140 |            62 |       531 |                  77 |                   63 | B7              | No confirmed PLE match | Private              | Other                        |
| ABAINZA, JANSEN MOLATO||11/12/1993                |    1041407161 |   2014 |                  73 |             2 |       302 |                  47 |                   26 | B1              | No confirmed PLE match | Public               | Natural Sciences             |
| ABAINZA, JANSEN MOLATO||11/12/1993                |    1111409896 |   2014 |                  75 |             3 |       316 |                  30 |                   45 | B1              | No confirmed PLE match | Public               | Natural Sciences             |
| ABAINZA, JANSEN MOLATO||11/12/1993                |    1101510046 |   2015 |                  66 |             3 |       304 |                  39 |                   27 | B1              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAINZA, KLARYS MOLATO||11/9/1995                 |    1101508520 |   2015 |                  63 |             2 |       286 |                  26 |                   37 | B1              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAINZA, KLARYS MOLATO||11/9/1995                 |    1041605016 |   2016 |                  93 |             9 |       367 |                  49 |                   44 | B1              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAINZA, KLARYS MOLATO||11/9/1995                 |    1101812585 |   2018 |                 104 |            34 |       460 |                  53 |                   51 | B4              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAJA, CARISSE MACALINAO||                        |       1070806 |   2006 |                 111 |            30 |       447 |                  51 |                   60 | B4              | No confirmed PLE match | Private              | Social & Behavioral Sciences |
| ABAJA, CARISSE MACALINAO||                        |       1082119 |   2007 |                 127 |            50 |       501 |                  55 |                   72 | B6              | No confirmed PLE match | Private              | Natural Sciences             |
| ABALLE, GILLES RADOC||01/19/1988                  |    1121209792 |   2012 |                 107 |            36 |       464 |                  45 |                   62 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALLE, GILLES RADOC||01/19/1988                  |    1111303287 |   2013 |                 140 |            78 |       579 |                  66 |                   74 | B8              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALLE, RAPHUNZEL MONTALBO||06/17/1989            |    1121003605 |   2010 |                 115 |            37 |       467 |                  63 |                   52 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALLE, RAPHUNZEL MONTALBO||06/17/1989            |    1041609444 |   2016 |                 108 |            21 |       421 |                  63 |                   45 | B3              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALOS, ALYANNA JOSON||03/19/1994                 |    1121209747 |   2012 |                 120 |            57 |       518 |                  70 |                   50 | B6              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALOS, ALYANNA JOSON||03/19/1994                 |    1041303786 |   2013 |                 151 |            80 |       585 |                  80 |                   71 | B9              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALOS, ALYANNA JOSON||03/19/1994                 |    1111311089 |   2013 |                 137 |            75 |       568 |                  79 |                   58 | B8              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALOS, EUNICE ANNE ORTIZ||04/13/1995             |    1111307839 |   2013 |                 165 |            94 |       659 |                 101 |                   64 | B10             | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABALOS, EUNICE ANNE ORTIZ||04/13/1995             |    1101507700 |   2015 |                 177 |            98 |       708 |                  95 |                   82 | B10             | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABALOS, HANNAH LOUISE PHOEBE BAUTISTA||07/17/1993 |    2121003055 |   2010 |                 147 |            73 |       562 |                  71 |                   76 | B8              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABALOS, HANNAH LOUISE PHOEBE BAUTISTA||07/17/1993 |    1121107319 |   2011 |                 161 |            82 |       592 |                  86 |                   75 | B9              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABALOS, ISAAC ELIZALDE||12/4/1999                 |    1031810735 |   2018 |                 112 |            44 |       485 |                  57 |                   55 | B5              | No confirmed PLE match | Private              | Natural Sciences             |
| ABALOS, ISAAC ELIZALDE||12/4/1999                 |    1101807674 |   2018 |                 132 |            66 |       542 |                  67 |                   65 | B7              | No confirmed PLE match | Private              | Natural Sciences             |
| ABALOS, JOANNA MAE TANGCA||4/7/1994               |    1041403317 |   2014 |                 114 |            48 |       494 |                  63 |                   51 | B5              | Confirmed PLE passer   | Public               | Natural Sciences             |
| ABALOS, JOANNA MAE TANGCA||4/7/1994               |    1111403423 |   2014 |                 128 |            71 |       557 |                  78 |                   50 | B8              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABALOS, JOANNA MAE TANGCA||4/7/1994               |    1031504785 |   2015 |                 166 |            90 |       628 |                  87 |                   79 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |

> Full detail: [08_repeat_takers_detail.csv](08_repeat_takers_detail.csv) (77,770 rows, 12 cols)


---

## 6. NMA_AppNo Deterministic Match Histories

Attempt histories exclusively for records matched deterministically via application number (PLE_MATCH_METHOD in MANUAL_APPNO_MATCH, DETERMINISTIC_APPNO), rather than by exact name.

**population: all NMAT rows | n=2,867**

| PERSON_KEY                                              |   APPNO_CLEAN |   Year |   TotalRawScoreTRUE |   NMS_PER_num | PLE_STATUS_LABEL     |
|:--------------------------------------------------------|--------------:|-------:|--------------------:|--------------:|:---------------------|
| ABAD, ALBERT CAISIP||09/28/1990                         |        400428 |   2010 |                 105 |            16 | Confirmed PLE passer |
| ABAD, JOSHUA KIM E||05/17/1996                          |    1101509313 |   2015 |                 121 |            65 | Confirmed PLE passer |
| ABAD, MA JUSTINE DAYANNE CERCADO||09/17/1995            |    1101507389 |   2015 |                 123 |            67 | Confirmed PLE passer |
| ABADIER, AILEEN MESTIDIO||                              |       1061740 |   2007 |                  90 |            14 | Confirmed PLE passer |
| ABALOS, RODRIGO JR SAPIANDANTE||07/21/1990              |    1121007739 |   2010 |                 152 |            78 | Confirmed PLE passer |
| ABALOS, RODRIGO JUNIOR SAPIANDANTE||                    |        411600 |   2010 |                 167 |            81 | Confirmed PLE passer |
| ABANA, MA EDISA CRUZ||                                  |       1003803 |   2009 |                 126 |            47 | Confirmed PLE passer |
| ABANILLA, LYRA JOY LUCAS||01/14/1989                    |    1121209623 |   2012 |                 155 |            93 | Confirmed PLE passer |
| ABARA, MA VICTORIA LOBENDINO||05/14/1996                |    1101504711 |   2015 |                 139 |            82 | Confirmed PLE passer |
| ABBARIAO, MA JESICCA DULIN||9/4/1993                    |    1121213166 |   2012 |                  82 |             6 | Confirmed PLE passer |
| ABBARIAO, MA JESICCA DULIN||9/4/1993                    |    1111309255 |   2013 |                  88 |            11 | Confirmed PLE passer |
| ABBARIAO, MA JESICCA DULIN||9/4/1993                    |    1041401732 |   2014 |                 129 |            70 | Confirmed PLE passer |
| ABDON, MARIA THERESE LUMANOG||11/30/1985                |    1121001533 |   2010 |                  98 |            17 | Confirmed PLE passer |
| ABDULCADER, SANNAH MOHAMMAD||                           |       1003057 |   2009 |                  84 |             6 | Confirmed PLE passer |
| ABDULMALIK, ANIES ANSARY ABDULHAMID||8/2/1992           |    1121206466 |   2012 |                 124 |            63 | Confirmed PLE passer |
| ABEL, JORIZ KEVIN||08/24/1993                           |    1121204887 |   2012 |                 155 |            93 | Confirmed PLE passer |
| ABELITA, MA CARISSA YAN||01/21/1993                     |    1121207124 |   2012 |                 137 |            79 | Confirmed PLE passer |
| ABELLO, MA ANTONIA ELISA RAMOS||2/1/1991                |    1121105620 |   2011 |                 175 |            91 | Confirmed PLE passer |
| ABIAN, KIM CRISOSTOMO||01/23/1994                       |    1121201734 |   2012 |                 121 |            59 | Confirmed PLE passer |
| ABIJAY, LORENZO MIGUEL PENALOZA||09/22/1992             |    1111403797 |   2014 |                 155 |            93 | Confirmed PLE passer |
| ABORKA, MA AYANNE BALDEVIA||03/31/1994                  |    1101506240 |   2015 |                 159 |            94 | Confirmed PLE passer |
| ABORQUE, JESUS CESARIO JR JAVINES||                     |       1000742 |   2009 |                 145 |            70 | Confirmed PLE passer |
| ABOY, MA EDILLA TERESA RATILLA||                        |       1092757 |   2008 |                 131 |            59 | Confirmed PLE passer |
| ABOY, MA EDILLA TERESA RATILLA||04/23/1988              |    2121001487 |   2010 |                 148 |            74 | Confirmed PLE passer |
| ABREA, MA JESSA ALITALIA CARABUENA||                    |        410137 |   2010 |                 111 |            21 | Confirmed PLE passer |
| ABREU, IARA MARIE ANN ABARQUEZ||05/27/1992              |    1041300496 |   2013 |                  63 |            -1 | Confirmed PLE passer |
| ABRIGO, MA ASTRID VILLAROYA||                           |       1052640 |   2006 |                  92 |            11 | Confirmed PLE passer |
| ABRIL, JOANNA BLANCA C JUAN||                           |        410765 |   2010 |                 184 |            91 | Confirmed PLE passer |
| ABUAN, GERLIE PARINGIT||                                |       1082059 |   2007 |                 123 |            47 | Confirmed PLE passer |
| ABUEG, MICHELLE RENEE||                                 |       1001133 |   2009 |                 186 |            97 | Confirmed PLE passer |
| ABUEVA, AILEEN CRYSTEL DIMAYACYAC||                     |       1083653 |   2008 |                 121 |            41 | Confirmed PLE passer |
| ABUTIN, MA VICTORIA MIANO||                             |       1052977 |   2006 |                 125 |            49 | Confirmed PLE passer |
| ABUTIN, MA VICTORIA MIANO||                             |       1071027 |   2006 |                 140 |            63 | Confirmed PLE passer |
| ACEDO, RODY MAE OBLIGADO||05/14/1993                    |    1031504216 |   2015 |                 126 |            54 | Confirmed PLE passer |
| ACLAN, ARRIANE KHAY SACENDONCILLO||06/15/1989           |    1031712565 |   2017 |                 141 |            63 | Confirmed PLE passer |
| ACLAN, MA ANA PATRICIA CUETO||08/21/1991                |    1121004428 |   2010 |                 148 |            74 | Confirmed PLE passer |
| ACLAN, MA ANA PATRICIA CUETO||08/21/1991                |    1041103316 |   2011 |                 146 |            75 | Confirmed PLE passer |
| ACOP, REICHEL ANGELO||11/14/1992                        |    1121204504 |   2012 |                 140 |            82 | Confirmed PLE passer |
| ACOSTA, DONNA ROSE KUAN TIU||5/10/1992                  |    1111308750 |   2013 |                 197 |           nan | Confirmed PLE passer |
| ACOSTA, MA ANGELICA CIELO CABATINGAN||                  |       1000998 |   2009 |                 150 |            75 | Confirmed PLE passer |
| ACOSTA, MA JOANNA EMILY MAMARIL||                       |       1085762 |   2008 |                 175 |            94 | Confirmed PLE passer |
| ACOSTA, NIKOLAI E||12/18/1996                           |    1101602164 |   2016 |                 135 |            68 | Confirmed PLE passer |
| ACUNA, DELFIN JR PLASI||                                |       1001748 |   2009 |                 165 |            87 | Confirmed PLE passer |
| ADA, MA MICHELLE BELTRAN||02/27/1993                    |    1041304910 |   2013 |                 162 |            89 | Confirmed PLE passer |
| ADA, MA MICHELLE BELTRAN||02/27/1993                    |    1111312215 |   2013 |                 148 |            86 | Confirmed PLE passer |
| ADAYA, MA MILDRED BOBADILLA||2/8/1993                   |    1121108002 |   2011 |                 159 |            81 | Confirmed PLE passer |
| ADAYA, MA MILDRED BOBADILLA||2/8/1993                   |    1031203526 |   2012 |                 168 |            89 | Confirmed PLE passer |
| ADDUN, EDZEL JANE JARITO||1/12/1987                     |    1041303533 |   2013 |                 140 |            69 | Confirmed PLE passer |
| ADELAN, MARIA ROTELLE SALVADOR||02/16/1996              |    1101508295 |   2015 |                 151 |            90 | Confirmed PLE passer |
| ADIONG, FELINA JUSTINE VANO||10/8/1996                  |    1101601948 |   2016 |                 159 |            86 | Confirmed PLE passer |
| ADLAON, LANCE ALDWIN||10/27/1986                        |        400801 |   2010 |                 127 |            51 | Confirmed PLE passer |
| ADONA, MA RECCIA ROSE GOK ONG||                         |       1061045 |   2006 |                 136 |            59 | Confirmed PLE passer |
| ADONA, MA RECCIA ROSE GOK ONG||                         |       1072003 |   2006 |                 131 |            53 | Confirmed PLE passer |
| ADRIANO, BUENAVENTURA III||07/18/1988                   |    1121204349 |   2012 |                 134 |            76 | Confirmed PLE passer |
| AGAMATA, ERIKA JANE PAULA TIAM||2/6/1992                |    1041300374 |   2013 |                 128 |            54 | Confirmed PLE passer |
| AGARIN, REA MAY I VILLANUEVA||7/8/1993                  |    1111400439 |   2014 |                 131 |            75 | Confirmed PLE passer |
| AGDAMAG, MA ANGELICA CRUZ||10/30/1995                   |    1031505937 |   2015 |                 165 |            91 | Confirmed PLE passer |
| AGDAMAG, MA ANGELICA CRUZ||10/30/1995                   |    1101509261 |   2015 |                 157 |            93 | Confirmed PLE passer |
| AGGABAO, MA CONCEPCION SOCORRO GRACIA AGAGON||8/12/1992 |    1121105081 |   2011 |                  99 |            19 | Confirmed PLE passer |
| AGGABAO, MA CONCEPCION SOCORRO GRACIA AGAGON||8/12/1992 |    1121203920 |   2012 |                  86 |             9 | Confirmed PLE passer |
| AGGABAO, MA CONCEPCION SOCORRO GRACIA AGAGON||8/12/1992 |    1041302875 |   2013 |                 110 |            30 | Confirmed PLE passer |
| AGGABAO, MA CONCEPCION SOCORRO GRACIA AGAGON||8/12/1992 |    1111308528 |   2013 |                 109 |            36 | Confirmed PLE passer |
| AGRASADA, TANYA KATRINA BUENAFLOR||9/12/1991            |    1121211041 |   2012 |                 126 |            66 | Confirmed PLE passer |
| AGRUPIS, KRISTAL AN CASTANEDA||                         |       1071156 |   2006 |                 179 |            93 | Confirmed PLE passer |
| AGRUPIS, KRISTAL AN CASTANEDA||                         |       1054814 |   2007 |                 174 |            86 | Confirmed PLE passer |
| AGUDA, MARY GRACE SIMANGON||03/30/1987                  |    1041403588 |   2014 |                 124 |            63 | Confirmed PLE passer |
| AGUDO, SHELLEY VANESSA DELA CRUZ||10/3/1992             |    1041300751 |   2013 |                 131 |            60 | Confirmed PLE passer |
| AGUELO, MA ISABEL SALA||12/3/1992                       |    1121106186 |   2011 |                 168 |            88 | Confirmed PLE passer |
| AGUELO, MA ISABEL SALA||12/3/1992                       |    1031202030 |   2012 |                 171 |            90 | Confirmed PLE passer |
| AGUILA, MA THERESSA DE LOS REYES||1/10/1994             |    1041407069 |   2014 |                 154 |            92 | Confirmed PLE passer |
| AGUILA, MA THERESSA DE LOS REYES||1/10/1994             |    1111407511 |   2014 |                 170 |            98 | Confirmed PLE passer |
| AGUILAR, ARDIE ANTONIO||1/2/1988                        |    1121005263 |   2010 |                 129 |            53 | Confirmed PLE passer |
| AGUILAR, JEFF JUSTIN||11/28/1994                        |    1101505909 |   2015 |                 202 |           nan | Confirmed PLE passer |
| AGUILAR, KATRINA ARIELLE ROJAS||5/3/1994                |    1101507482 |   2015 |                 143 |            85 | Confirmed PLE passer |
| AGUIRRE, AYRA JHOANA GUIANAN||3/6/1988                  |    1041300207 |   2013 |                 185 |            97 | Confirmed PLE passer |
| AGUIRRE, EUNICE CUENTO||11/25/1991                      |    1121101329 |   2011 |                 108 |            27 | Confirmed PLE passer |
| AGUIRRE, MA JESSICA ELIZABETH ESPULGAR||9/1/1994        |    1111304915 |   2013 |                  87 |             9 | Confirmed PLE passer |
| AGUIRRE, MA JESSICA ELIZABETH ESPULGAR||9/1/1994        |    1041400753 |   2014 |                 105 |            33 | Confirmed PLE passer |
| AGUSTIN, CRISTINA ANNE SANTOS||11/23/1992               |    1111303407 |   2013 |                 160 |            92 | Confirmed PLE passer |
| AGUSTIN, RAPHAEL JAMES F||10/24/1996                    |    1031705655 |   2017 |                 141 |            63 | Confirmed PLE passer |
| AGUSTINO, ARNULFO JR RICO||9/9/1989                     |    2121001876 |   2010 |                 168 |            90 | Confirmed PLE passer |
| AHMAD, SHAHEEN OSMENA||11/28/1994                       |    1031700610 |   2017 |                 130 |            50 | Confirmed PLE passer |
| AL FAWAZ, BANDR NAFEEZ ABDULLAH LOY OD||12/15/1993      |    1031507043 |   2015 |                 143 |            73 | Confirmed PLE passer |
| ALABADO, JIBIN CANTILLO||06/13/1973                     |    1041100956 |   2011 |                 175 |            94 | Confirmed PLE passer |
| ALAMPAY, NICCOLO SU||03/19/1989                         |    1121005070 |   2010 |                 174 |            93 | Confirmed PLE passer |
| ALATI IT, ROWIE LYNE FERNANDEZ||8/3/1990                |    1121103224 |   2011 |                 160 |            83 | Confirmed PLE passer |
| ALBANO, EMMANUEL JR ESCARLAN||8/4/1990                  |    2121000085 |   2010 |                 142 |            68 | Confirmed PLE passer |
| ALBANO, MARIA ANGELINE PANTUA||                         |       1060769 |   2006 |                 106 |            26 | Confirmed PLE passer |
| ALBESA, MA TRISHA ARIAS||4/9/1996                       |    1101511351 |   2015 |                 155 |            92 | Confirmed PLE passer |
| ALCALA, ANGELLE KATHREEN TUBAN||04/25/1990              |    1041406715 |   2014 |                 108 |            38 | Confirmed PLE passer |
| ALCALDE, MA KATHRINA TERESA TONGCO||                    |       1073528 |   2007 |                 176 |            93 | Confirmed PLE passer |
| ALCANO, MARY CHRISTINE PINO||                           |       1001740 |   2009 |                 107 |            25 | Confirmed PLE passer |
| ALCANTARA, ALEXIS ANNE CONTADO||01/23/1996              |    1041600384 |   2016 |                 138 |            57 | Confirmed PLE passer |
| ALCANTARA, MARK ANGELO MANDAL||                         |       1093750 |   2009 |                 200 |            99 | Confirmed PLE passer |
| ALCANTARA, RANIEL JOHN LUQUE||11/11/1998                |    1031809024 |   2018 |                 119 |            55 | Confirmed PLE passer |
| ALCANZO, JAN HILARY ABELLO||05/29/1990                  |    1041102518 |   2011 |                 180 |            96 | Confirmed PLE passer |
| ALCARAZ, ADRIAN M||04/22/1993                           |    1101813952 |   2018 |                  98 |            27 | Confirmed PLE passer |
| ALCAZAR, ELIZABETH GRACE ALMADIN||                      |       1090183 |   2009 |                 154 |            79 | Confirmed PLE passer |
| ALCAZAR, ESTHER RUTH DE LOS REYES||5/12/1990            |    1121106368 |   2011 |                 134 |            56 | Confirmed PLE passer |
| ALCID, MA ARABELLA JAFFNA CABE||11/29/1993              |    1041301690 |   2013 |                 134 |            63 | Confirmed PLE passer |

> Full detail: [08_appno_match_histories.csv](08_appno_match_histories.csv) (2,867 rows)

---



<a id="09-subtests-and-profiles"></a>

**Generated:** 2026-07-31 16:32

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `uni (UNDERGRAD_UNI_TYPE) / besttrend (UNDERGRAD_COURSE_GROUP, desc)`

**Filters:** None (full unfiltered dataset)

---

## 1. Subtest Standard Score Means by UNDERGRAD_UNI_TYPE

**Table 34. Standardized subtest means by university type**

| UNDERGRAD_UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:---------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Public               |    495.8 |       513.2 |         517.49 |       507.63 |    511.66 |    519.09 |   502.65 |      514.03 |
| Private              |   484.74 |      500.32 |         498.91 |       498.96 |    489.61 |    498.09 |   490.48 |       491.4 |
| Foreign              |   478.75 |      505.58 |         512.25 |       489.33 |     499.4 |     512.8 |    479.1 |      506.07 |

---

## 2. Subtest Raw Score Means by UNDERGRAD_UNI_TYPE

**Table 35. Raw-score subtest means by university type**

| UNDERGRAD_UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:---------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Public               |    16.13 |       17.91 |          15.63 |        17.64 |     15.82 |     14.88 |    15.77 |       15.09 |
| Private              |    15.51 |       17.26 |          14.48 |        17.11 |     14.58 |     13.72 |    15.13 |       13.83 |
| Foreign              |    15.49 |       17.48 |          15.42 |        16.68 |     15.45 |      14.8 |    14.84 |       14.89 |

---

## 3. Subtest Standard Score Means by UNDERGRAD_COURSE_GROUP

**Table 36. Standardized subtest means by course group**

| UNDERGRAD_COURSE_GROUP       |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Medical & Allied             |   498.46 |       510.9 |          497.6 |       505.36 |    484.13 |    494.33 |   506.32 |       483.7 |
| Natural Sciences             |   476.56 |       499.9 |         512.44 |       503.34 |    520.45 |    516.25 |   470.86 |      518.52 |
| Social & Behavioral Sciences |   453.52 |      470.05 |         490.79 |       476.44 |    467.09 |    490.76 |   481.38 |      485.91 |
| Education                    |   500.96 |      518.45 |         510.34 |       499.99 |    490.88 |    510.64 |   506.49 |       511.1 |
| Engineering & Technology     |   525.24 |      540.96 |          575.6 |       519.32 |    501.23 |    570.89 |   507.64 |      547.23 |
| Other                        |   506.04 |      513.34 |         512.03 |       495.29 |    497.67 |    513.47 |   512.96 |      493.01 |

---

## 4. Subtest Raw Score Means by UNDERGRAD_COURSE_GROUP

**Table 37. Raw-score subtest means by course group**

| UNDERGRAD_COURSE_GROUP       |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Medical & Allied             |    16.08 |       17.84 |          14.36 |        17.38 |     14.11 |     13.46 |    15.84 |       13.35 |
| Natural Sciences             |     15.1 |       17.13 |          15.26 |        17.43 |     16.11 |      14.6 |    14.17 |       15.28 |
| Social & Behavioral Sciences |    14.17 |       15.66 |             14 |           16 |     13.46 |      13.2 |    14.68 |       13.43 |
| Education                    |    16.99 |       18.59 |          15.63 |         17.1 |     16.35 |      15.6 |    16.54 |        15.7 |
| Engineering & Technology     |    17.38 |       19.12 |          19.18 |        18.29 |     15.05 |      17.6 |    15.81 |       16.94 |
| Other                        |    17.08 |       18.15 |          15.64 |           17 |     16.26 |     15.37 |    16.67 |       14.55 |

---

## 5. Radar Profile Data (Raw Standardized Subtest Means)

*These are the exact values plotted on the dashboard's radar chart (dashboard.py radar_for_group()) — raw standardized subtest means, NOT mean-centered. Numerically identical to Table 34 (by university type) and Table 36 (by course group); reproduced here as the radar chart's per-axis series data per the export format contract.*

### 5.1 By University Type

**Table 38. Radar-profile values (raw standardized subtest means) by university type — population: uni subset, n=133,477**

| UNDERGRAD_UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:---------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Public               |    495.8 |       513.2 |         517.49 |       507.63 |    511.66 |    519.09 |   502.65 |      514.03 |
| Private              |   484.74 |      500.32 |         498.91 |       498.96 |    489.61 |    498.09 |   490.48 |       491.4 |
| Foreign              |   478.75 |      505.58 |         512.25 |       489.33 |     499.4 |     512.8 |    479.1 |      506.07 |


### 5.2 By Course Group

**Table 39. Radar-profile values (raw standardized subtest means) by course group — population: besttrend subset, n=134,869**

| UNDERGRAD_COURSE_GROUP       |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Medical & Allied             |   498.46 |       510.9 |          497.6 |       505.36 |    484.13 |    494.33 |   506.32 |       483.7 |
| Natural Sciences             |   476.56 |       499.9 |         512.44 |       503.34 |    520.45 |    516.25 |   470.86 |      518.52 |
| Social & Behavioral Sciences |   453.52 |      470.05 |         490.79 |       476.44 |    467.09 |    490.76 |   481.38 |      485.91 |
| Education                    |   500.96 |      518.45 |         510.34 |       499.99 |    490.88 |    510.64 |   506.49 |       511.1 |
| Engineering & Technology     |   525.24 |      540.96 |          575.6 |       519.32 |    501.23 |    570.89 |   507.64 |      547.23 |
| Other                        |   506.04 |      513.34 |         512.03 |       495.29 |    497.67 |    513.47 |   512.96 |      493.01 |


### 5.3 Mean-Centered View (aggregator-only, NOT in the dashboard)

*Subtracts the overall per-subtest mean so groups can be compared on a relative scale. This is a derived view with no dashboard counterpart and no table-number collision with Table 38/39 above.*

**Table 38c. Mean-centered standardized subtest scores by university type**

| UNDERGRAD_UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:---------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Public               |     9.37 |        6.83 |           7.94 |         8.99 |     11.44 |       9.1 |    11.91 |        10.2 |
| Private              |    -1.69 |       -6.05 |         -10.64 |         0.32 |    -10.61 |     -11.9 |    -0.26 |      -12.43 |
| Foreign              |    -7.68 |       -0.79 |            2.7 |        -9.31 |     -0.82 |      2.81 |   -11.64 |        2.24 |

**Table 39c. Mean-centered standardized subtest scores by course group**

| UNDERGRAD_COURSE_GROUP       |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Medical & Allied             |        5 |        1.97 |         -18.87 |          5.4 |     -9.45 |    -21.73 |     8.71 |      -22.88 |
| Natural Sciences             |    -16.9 |       -9.03 |          -4.03 |         3.38 |     26.88 |      0.19 |   -26.75 |       11.94 |
| Social & Behavioral Sciences |   -39.94 |      -38.88 |         -25.68 |       -23.52 |    -26.49 |     -25.3 |   -16.23 |      -20.67 |
| Education                    |      7.5 |        9.52 |          -6.13 |         0.03 |      -2.7 |     -5.42 |     8.88 |        4.52 |
| Engineering & Technology     |    31.78 |       32.03 |          59.13 |        19.36 |      7.65 |     54.83 |    10.03 |       40.65 |
| Other                        |    12.58 |        4.41 |          -4.44 |        -4.67 |      4.09 |     -2.59 |    15.35 |      -13.57 |

---

## 6. Full Descriptive Statistics (n, Mean, Median, Std, Min, Max)

**Table 40. Descriptive statistics for each subtest (standard and raw scores)**

| Subtest      | Type   |      n |   Mean |   Median |   Std |   Min |   Max |
|:-------------|:-------|-------:|-------:|---------:|------:|------:|------:|
| Verbal       | Raw    | 134826 |  15.64 |       16 |  5.26 |     0 |    30 |
| Inductive    | Raw    | 134826 |   17.4 |       18 |  5.84 |     0 |    30 |
| Quantitative | Raw    | 134826 |  14.73 |       14 |  6.04 |     0 |    30 |
| Perceptual   | Raw    | 134826 |   17.2 |       17 |  5.99 |     0 |    30 |
| Biology      | Raw    | 134826 |  14.84 |       15 |  5.31 |     0 |    30 |
| Physics      | Raw    | 134826 |  13.97 |       13 |  5.36 |     0 |    30 |
| Social       | Raw    | 134826 |  15.25 |       15 |  5.46 |     0 |    30 |
| Chemistry    | Raw    | 134826 |  14.11 |       13 |  5.58 |     0 |    30 |

---

---



<a id="10-year-gap-and-gender"></a>

**Generated:** 2026-07-31 16:32

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `besttrend / bestobservable`

**Filters:** None (full unfiltered dataset)

---

## 1. PLE Year Gap Distribution

- **Confirmed passers:** 29,519
- **Median year gap:** 6.0
- **Mean year gap:** 6.47
- **Std year gap:** 1.07
- **Min year gap:** 5.0
- **Max year gap:** 15.0
- **Q1 (25th pctile):** 6.0
- **Q3 (75th pctile):** 7.0
- **IQR:** 1.0

**Table 41. Full PLE year gap distribution**

|   PLE_YEAR_GAP |   Count |
|---------------:|--------:|
|              5 |    3424 |
|              6 |   14777 |
|              7 |    7563 |
|              8 |    2366 |
|              9 |     832 |
|             10 |     321 |
|             11 |     138 |
|             12 |      65 |
|             13 |      24 |
|             14 |       5 |
|             15 |       4 |

---

## 2. PLE Year Gap by UNDERGRAD_COURSE_GROUP

**Table 42. Year-gap summary by course group**

| UNDERGRAD_COURSE_GROUP       |   confirmed_passers |   median_year_gap |   mean_year_gap |   std_year_gap |   q25_year_gap |   q75_year_gap |   min_year_gap |   max_year_gap |   median_percentile |
|:-----------------------------|--------------------:|------------------:|----------------:|---------------:|---------------:|---------------:|---------------:|---------------:|--------------------:|
| Education                    |                1563 |                 6 |            6.54 |            1.2 |              6 |              7 |              5 |             15 |                  65 |
| Engineering & Technology     |                 106 |                 6 |             6.6 |           1.15 |              6 |              7 |              5 |             11 |                  91 |
| Medical & Allied             |               16776 |                 6 |            6.41 |           1.03 |              6 |              7 |              5 |             14 |                  63 |
| Natural Sciences             |                6523 |                 6 |            6.54 |           1.01 |              6 |              7 |              5 |             13 |                  81 |
| Other                        |                2962 |                 6 |            6.59 |            1.3 |              6 |              7 |              5 |             15 |                  68 |
| Social & Behavioral Sciences |                1589 |                 6 |            6.56 |           1.07 |              6 |              7 |              5 |             14 |                  83 |

---

## 3. Gender Composition (Overall)

**Table 43. Gender composition (besttrend)**

| Sex    |   Count |   Percent |
|:-------|--------:|----------:|
| Female |   74753 |     55.44 |
| Male   |   60073 |     44.56 |

---

## 4. Gender by Year

**Table 44. Gender counts by NMAT year**

|   Year |   Male |   Female |
|-------:|-------:|---------:|
|   2006 |   1246 |     2452 |
|   2007 |   1368 |     2322 |
|   2008 |   1934 |     3031 |
|   2009 |   2841 |     4604 |
|   2010 |   4454 |     4094 |
|   2011 |   3918 |     4774 |
|   2012 |   3530 |     5572 |
|   2013 |   3438 |     5706 |
|   2014 |   4042 |     6413 |
|   2015 |   4352 |     5974 |
|   2016 |   5242 |     7238 |
|   2017 |   9584 |    14364 |
|   2018 |  14124 |     8209 |


**Table 45. Gender percentages by NMAT year**

|   Year |   Male |   Female |
|-------:|-------:|---------:|
|   2006 |  33.69 |    66.31 |
|   2007 |  37.07 |    62.93 |
|   2008 |  38.95 |    61.05 |
|   2009 |  38.16 |    61.84 |
|   2010 |  52.11 |    47.89 |
|   2011 |  45.08 |    54.92 |
|   2012 |  38.78 |    61.22 |
|   2013 |   37.6 |     62.4 |
|   2014 |  38.66 |    61.34 |
|   2015 |  42.15 |    57.85 |
|   2016 |     42 |       58 |
|   2017 |  40.02 |    59.98 |
|   2018 |  63.24 |    36.76 |

---

## 5. Gender Score Comparison

**Table 46. Score summary by sex**

| SEX_CLEAN   |     n |   median_raw |   mean_raw |   std_raw |   median_pct |   mean_pct |   std_pct |   median_gps |   median_apt |   median_sa |
|:------------|------:|-------------:|-----------:|----------:|-------------:|-----------:|----------:|-------------:|-------------:|------------:|
| Female      | 74753 |          122 |     123.34 |     32.74 |           50 |       49.6 |     30.07 |          502 |          504 |         497 |
| Male        | 60073 |          121 |      122.9 |     34.18 |           49 |      49.29 |     30.69 |          500 |          503 |         498 |

---

## 6. Mann-Whitney U Tests: Sex x NMS_PER_num and Key Scores

**Table 47. Mann-Whitney U tests: Sex differences in key scores**

| Score Variable                |   Median (Female) |   Median (Male) |   U-statistic | p-value   |   Effect size (r) |    N1 |    N2 |
|:------------------------------|------------------:|----------------:|--------------:|:----------|------------------:|------:|------:|
| Percentile Rank (NMS_PER_num) |                50 |              49 |   2.21839e+09 | 0.0658    |           -0.0058 | 74219 | 59432 |
| Total Raw Score               |               122 |             121 |   2.27024e+09 | <0.001    |           -0.0111 | 74753 | 60073 |
| Part I Raw Score              |                66 |              65 |   2.30348e+09 | <0.001    |           -0.0259 | 74753 | 60073 |
| Part II Raw Score             |                57 |              57 |   2.23355e+09 | 0.0976    |            0.0052 | 74753 | 60073 |
| GPS Standard Score            |               502 |             500 |   2.25035e+09 | 0.479     |           -0.0022 | 74753 | 60073 |
| APT Standard Score            |               504 |             503 |   2.29195e+09 | <0.001    |           -0.0208 | 74753 | 60073 |
| SA Standard Score             |               497 |             498 |   2.21384e+09 | <0.001    |             0.014 | 74753 | 60073 |

---

## 7. Sex x PLE Status (Observable Cohort)

**Table 48. PLE status counts by sex (observable cohort)**

| SEX_CLEAN   |   Confirmed PLE passer |   No confirmed PLE match |
|:------------|-----------------------:|-------------------------:|
| Female      |                  18675 |                    22797 |
| Male        |                  12897 |                    15091 |


**Table 49. PLE status percentages by sex (observable cohort)**

| SEX_CLEAN   |   Confirmed PLE passer |   No confirmed PLE match |
|:------------|-----------------------:|-------------------------:|
| Female      |                  45.03 |                    54.97 |
| Male        |                  46.08 |                    53.92 |


**Table 50. Confirmed PLE linkage rate by sex**

| SEX_CLEAN   |   total |   confirmed_passers |   linkage_rate_pct |
|:------------|--------:|--------------------:|-------------------:|
| Female      |   41472 |               18675 |              45.03 |
| Male        |   27988 |               12897 |              46.08 |


**Table 51. Chi-square test: Sex x PLE status**

|   Chi-square |   p-value |   df |     N |   Cramer's V |
|-------------:|----------:|-----:|------:|-------------:|
|       7.3897 |    0.0066 |    1 | 69460 |       0.0103 |

---

## 8. PLE Year Gap by Gender

**Table 52. PLE year gap summary by sex**

| SEX_CLEAN   |     n |   median_gap |   mean_gap |   std_gap |   min_gap |   max_gap |   q25_gap |   q75_gap |
|:------------|------:|-------------:|-----------:|----------:|----------:|----------:|----------:|----------:|
| Female      | 17304 |            6 |       6.43 |      1.05 |         5 |        15 |         6 |         7 |
| Male        | 12206 |            6 |       6.54 |      1.11 |         5 |        15 |         6 |         7 |


**Table 53. Mann-Whitney test: Sex differences in PLE year gap**

| Group 1   | Group 2   |   Median (Female) |   Median (Male) |   U-statistic | p-value   |   Effect size (r) |    N1 |    N2 |
|:----------|:----------|------------------:|----------------:|--------------:|:----------|------------------:|------:|------:|
| Female    | Male      |                 6 |               6 |    1.0011e+08 | <0.001    |             0.052 | 17304 | 12206 |

---

---



<a id="11-statistical-tests"></a>

**Generated:** 2026-07-31 16:32

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Filters:** None (full unfiltered dataset)

---

## Section 1: Kruskal-Wallis Tests

Non-parametric alternative to one-way ANOVA. Tests whether samples originate from the same distribution. Eta-squared (effect size): Negligible (<0.01), Small (0.01-0.06), Medium (0.06-0.14), Large (>=0.14).

---

### 1a. Year × Score Distributions

Testing whether score distributions differ across NMAT years (2006-2018).

**Table 43. Kruskal-Wallis tests for score distributions across NMAT years**

| Score Variable     |   Groups (k) |   Total N |   H-statistic |   p-value |   Eta-squared | Effect Size   | Sig.   |
|:-------------------|-------------:|----------:|--------------:|----------:|--------------:|:--------------|:-------|
| Total Raw Score    |           13 |    134826 |       6028.28 |         0 |        0.0446 | Small         | ***    |
| Part I Raw Score   |           13 |    134826 |       5766.34 |         0 |        0.0427 | Small         | ***    |
| Part II Raw Score  |           13 |    134826 |       5968.69 |         0 |        0.0442 | Small         | ***    |
| Percentile Rank    |           13 |    133693 |       2432.24 |         0 |        0.0181 | Small         | ***    |
| GPS Standard Score |           13 |    134869 |       2592.55 |         0 |        0.0191 | Small         | ***    |

### 1b. University Type × Percentile Rank

Testing whether percentile rank distributions differ by university type (Public, Private, Foreign).

**Kruskal-Wallis: UNDERGRAD_UNI_TYPE × NMS_PER_num**

| Score Variable   |   Groups (k) |   Total N |   H-statistic |      p-value |   Eta-squared | Effect Size   | Sig.   |
|:-----------------|-------------:|----------:|--------------:|-------------:|--------------:|:--------------|:-------|
| Percentile Rank  |            3 |    132313 |       750.763 | 9.41701e-164 |        0.0057 | Negligible    | ***    |

### 1c. Course Group × Percentile Rank

Testing whether percentile rank distributions differ by UNDERGRAD_COURSE_GROUP.

**Kruskal-Wallis: UNDERGRAD_COURSE_GROUP × NMS_PER_num**

| Score Variable   |   Groups (k) |   Total N |   H-statistic |      p-value |   Eta-squared | Effect Size   | Sig.   |
|:-----------------|-------------:|----------:|--------------:|-------------:|--------------:|:--------------|:-------|
| Percentile Rank  |            6 |    133693 |       1306.69 | 2.26405e-280 |        0.0097 | Negligible    | ***    |

### 1d. University Location × Percentile Rank

Testing whether percentile rank distributions differ by university location (NCR vs Provincial).

**Kruskal-Wallis: UNDERGRAD_UNI_LOCATION × NMS_PER_num**

| Score Variable   |   Groups (k) |   Total N |   H-statistic |   p-value |   Eta-squared | Effect Size   | Sig.   |
|:-----------------|-------------:|----------:|--------------:|----------:|--------------:|:--------------|:-------|
| Percentile Rank  |            3 |    133693 |        4.4765 |  0.106646 |             0 | Negligible    | ns     |

---
## Section 2: Mann-Whitney U Tests

Two-sample non-parametric test for differences between independent groups. Effect size r (rank-biserial correlation): |r| ~ 0.1 small, ~0.3 medium, ~0.5 large.

---

### 2a. PLE Status × Score Variables

Comparing confirmed PLE passers vs no confirmed PLE match across score variables. Uses observable best-record cohort (Year <= 2014).

**Table 44. Mann-Whitney comparisons by PLE status (observable cohort)**

| Score Variable     |   Median (Confirmed PLE passer) |   Median (No confirmed PLE match) |   U-statistic |   p-value |   Effect size (r) |    N1 |    N2 | Sig.   |
|:-------------------|--------------------------------:|----------------------------------:|--------------:|----------:|------------------:|------:|------:|:-------|
| Total Raw Score    |                             139 |                               114 |   8.63044e+08 |         0 |            -0.443 | 31572 | 37888 | ***    |
| Percentile Rank    |                              69 |                                38 |   8.35619e+08 |         0 |           -0.4284 | 30988 | 37758 | ***    |
| GPS Standard Score |                             552 |                               470 |   8.58051e+08 |         0 |           -0.4329 | 31581 | 37922 | ***    |
| Part I Raw Score   |                              74 |                                62 |   8.42159e+08 |         0 |           -0.4081 | 31572 | 37888 | ***    |
| Part II Raw Score  |                              66 |                                52 |   8.49698e+08 |         0 |           -0.4207 | 31572 | 37888 | ***    |

### 2b. Sex × Percentile Rank

Comparing percentile rank distributions by sex.

SEX_CLEAN column not available in dataset.

---
## Section 3: Chi-Square Tests of Independence

Tests whether two categorical variables are independent. Cramer's V measures association strength (0-1).

---

### 3a. University Type × Percentile Bin

Testing independence between university type and percentile bin classification. H0: UNDERGRAD_UNI_TYPE and PercentileBin are independent.

**Table 45. Observed counts — University type × Percentile bin**

| UNDERGRAD_UNI_TYPE   |    B1 |   B10 |   B2 |   B3 |    B4 |    B5 |    B6 |   B7 |   B8 |   B9 |
|:---------------------|------:|------:|-----:|-----:|------:|------:|------:|-----:|-----:|-----:|
| Foreign              |   262 |   266 |  174 |  140 |   176 |   145 |   164 |  161 |  175 |  197 |
| Private              | 12205 | 10774 | 9823 | 9127 | 10061 | 10044 | 10079 | 9602 | 9821 | 9864 |
| Public               |  2949 |  4876 | 2228 | 2058 |  2247 |  2320 |  2421 | 2478 | 2606 | 3051 |

**Table 46. Chi-square summary — University type × Percentile bin**

|    chi2 |      p_value |   dof |   Cramer's V |      n | Sig.   |
|--------:|-------------:|------:|-------------:|-------:|:-------|
| 1270.33 | 9.41728e-259 |    18 |       0.0698 | 130494 | ***    |

**Table 47. Expected counts (under independence)**

| UNDERGRAD_UNI_TYPE   |      B1 |     B10 |      B2 |      B3 |      B4 |      B5 |      B6 |      B7 |      B8 |      B9 |
|:---------------------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Foreign              | 219.732 | 226.859 | 174.249 | 161.421 | 177.941 | 178.297 | 180.507 | 174.477 | 179.623 | 186.892 |
| Private              |   11979 | 12367.5 |  9499.4 | 8800.06 | 9700.66 | 9720.08 | 9840.53 | 9511.84 | 9792.35 | 10188.6 |
| Public               | 3217.31 | 3321.66 | 2551.35 | 2363.52 |  2605.4 | 2610.62 | 2642.97 | 2554.69 | 2630.03 | 2736.46 |

**Row percentages (university type × bin)**

| UNDERGRAD_UNI_TYPE   |    B1 |   B10 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |
|:---------------------|------:|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| Foreign              | 14.09 |  14.3 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |
| Private              | 12.04 | 10.63 | 9.69 |    9 | 9.92 | 9.91 | 9.94 | 9.47 | 9.69 |  9.73 |
| Public               | 10.83 |  17.9 | 8.18 | 7.56 | 8.25 | 8.52 | 8.89 |  9.1 | 9.57 |  11.2 |

### 3b. Course Group × Percentile Bin

Testing independence between course group and percentile bin classification.

**Observed counts — UNDERGRAD_COURSE_GROUP × Percentile bin**

| UNDERGRAD_COURSE_GROUP       |   B1 |   B10 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |   B9 |
|:-----------------------------|-----:|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
| Education                    |  313 |   469 |  306 |  319 |  333 |  365 |  314 |  335 |  331 |  360 |
| Engineering & Technology     |   38 |   203 |   43 |   43 |   41 |   63 |   64 |   55 |   73 |  107 |
| Medical & Allied             | 6348 |  6181 | 6179 | 5988 | 6771 | 6865 | 6765 | 6198 | 6213 | 5960 |
| Natural Sciences             | 4942 |  6310 | 3425 | 3029 | 3351 | 3358 | 3535 | 3796 | 4011 | 4439 |
| Other                        |  805 |  1092 |  699 |  699 |  773 |  774 |  794 |  794 |  859 |  959 |
| Social & Behavioral Sciences | 3137 |  1830 | 1736 | 1359 | 1320 | 1233 | 1307 | 1181 | 1249 | 1406 |

**Chi-square summary — UNDERGRAD_COURSE_GROUP × Percentile bin**

|    chi2 |   p_value |   dof |   Cramer's V |      n | Sig.   |
|--------:|----------:|------:|-------------:|-------:|:-------|
| 3014.18 |         0 |    45 |       0.0676 | 131845 | ***    |

**Expected counts (under independence) — UNDERGRAD_COURSE_GROUP × Percentile bin**

| UNDERGRAD_COURSE_GROUP       |      B1 |     B10 |      B2 |      B3 |      B4 |      B5 |      B6 |      B7 |      B8 |      B9 |
|:-----------------------------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Education                    | 407.171 | 420.288 | 323.688 | 298.839 |  328.94 | 330.743 | 333.905 |  322.93 | 332.781 | 345.715 |
| Engineering & Technology     |   86.28 | 89.0595 | 68.5899 | 63.3244 | 69.7028 | 70.0849 | 70.7548 | 68.4294 | 70.5167 | 73.2575 |
| Medical & Allied             |  7501.4 | 7743.05 | 5963.38 | 5505.58 | 6060.14 | 6093.35 |  6151.6 | 5949.42 |  6130.9 | 6369.18 |
| Natural Sciences             | 4750.84 | 4903.88 | 3776.77 | 3486.83 | 3838.05 | 3859.08 | 3895.97 | 3767.93 | 3882.86 | 4033.78 |
| Other                        | 974.846 | 1006.25 | 774.972 | 715.479 | 787.547 | 791.863 | 799.433 | 773.158 | 796.743 | 827.709 |
| Social & Behavioral Sciences | 1862.47 | 1922.47 |  1480.6 | 1366.94 | 1504.63 | 1512.87 | 1527.33 | 1477.14 |  1522.2 | 1581.36 |

**Row percentages (UNDERGRAD_COURSE_GROUP × bin)**

| UNDERGRAD_COURSE_GROUP       |    B1 |   B10 |    B2 |   B3 |    B4 |    B5 |    B6 |   B7 |    B8 |    B9 |
|:-----------------------------|------:|------:|------:|-----:|------:|------:|------:|-----:|------:|------:|
| Education                    |  9.09 | 13.61 |  8.88 | 9.26 |  9.67 |  10.6 |  9.11 | 9.72 |  9.61 | 10.45 |
| Engineering & Technology     |  5.21 | 27.81 |  5.89 | 5.89 |  5.62 |  8.63 |  8.77 | 7.53 |    10 | 14.66 |
| Medical & Allied             |    10 |  9.74 |  9.74 | 9.43 | 10.67 | 10.82 | 10.66 | 9.77 |  9.79 |  9.39 |
| Natural Sciences             | 12.29 |  15.7 |  8.52 | 7.54 |  8.34 |  8.35 |  8.79 | 9.44 |  9.98 | 11.04 |
| Other                        |  9.76 | 13.24 |  8.47 | 8.47 |  9.37 |  9.38 |  9.63 | 9.63 | 10.41 | 11.63 |
| Social & Behavioral Sciences | 19.91 | 11.61 | 11.02 | 8.62 |  8.38 |  7.82 |  8.29 | 7.49 |  7.93 |  8.92 |

---
## Section 4: Dunn Post-Hoc Pairwise Comparisons

Bonferroni-adjusted pairwise comparisons following significant Kruskal-Wallis results.

---
### 4a. University Type — Pairwise (Dunn + Bonferroni)

Pairwise comparisons of percentile rank across university types.

**Dunn post-hoc adjusted p-value matrix (Bonferroni) — UNDERGRAD_UNI_TYPE × NMS_PER_num**

|         |    Foreign |      Private |       Public |
|:--------|-----------:|-------------:|-------------:|
| Foreign |          1 |    0.0609617 |   9.7959e-08 |
| Private |  0.0609617 |            1 | 1.00457e-164 |
| Public  | 9.7959e-08 | 1.00457e-164 |            1 |

**Table 48. Dunn post-hoc pairwise summary — UNDERGRAD_UNI_TYPE**

| Group 1   | Group 2   |   Adjusted p-value | Significant   |
|:----------|:----------|-------------------:|:--------------|
| Foreign   | Private   |          0.0609617 | False         |
| Foreign   | Public    |         9.7959e-08 | True          |
| Private   | Public    |       1.00457e-164 | True          |

### 4b. Course Group — Pairwise (Dunn + Bonferroni)

Pairwise comparisons of percentile rank across course groups.

**Dunn post-hoc adjusted p-value matrix (Bonferroni) — UNDERGRAD_COURSE_GROUP × NMS_PER_num**

|                              |   Education |   Engineering & Technology |   Medical & Allied |   Natural Sciences |        Other |   Social & Behavioral Sciences |
|:-----------------------------|------------:|---------------------------:|-------------------:|-------------------:|-------------:|-------------------------------:|
| Education                    |           1 |                7.05057e-22 |         1.6133e-07 |                  1 |            1 |                    3.20437e-57 |
| Engineering & Technology     | 7.05057e-22 |                          1 |        2.24279e-40 |         7.0766e-27 |  7.47459e-23 |                    3.33311e-76 |
| Medical & Allied             |  1.6133e-07 |                2.24279e-40 |                  1 |        3.30125e-47 |  9.60554e-21 |                   3.96983e-116 |
| Natural Sciences             |           1 |                 7.0766e-27 |        3.30125e-47 |                  1 |            1 |                   4.08018e-221 |
| Other                        |           1 |                7.47459e-23 |        9.60554e-21 |                  1 |            1 |                   6.37992e-119 |
| Social & Behavioral Sciences | 3.20437e-57 |                3.33311e-76 |       3.96983e-116 |       4.08018e-221 | 6.37992e-119 |                              1 |

**Dunn post-hoc pairwise summary — UNDERGRAD_COURSE_GROUP**

| Group 1                  | Group 2                      |   Adjusted p-value | Significant   |
|:-------------------------|:-----------------------------|-------------------:|:--------------|
| Education                | Engineering & Technology     |        7.05057e-22 | True          |
| Education                | Medical & Allied             |         1.6133e-07 | True          |
| Education                | Natural Sciences             |                  1 | False         |
| Education                | Other                        |                  1 | False         |
| Education                | Social & Behavioral Sciences |        3.20437e-57 | True          |
| Engineering & Technology | Medical & Allied             |        2.24279e-40 | True          |
| Engineering & Technology | Natural Sciences             |         7.0766e-27 | True          |
| Engineering & Technology | Other                        |        7.47459e-23 | True          |
| Engineering & Technology | Social & Behavioral Sciences |        3.33311e-76 | True          |
| Medical & Allied         | Natural Sciences             |        3.30125e-47 | True          |
| Medical & Allied         | Other                        |        9.60554e-21 | True          |
| Medical & Allied         | Social & Behavioral Sciences |       3.96983e-116 | True          |
| Natural Sciences         | Other                        |                  1 | False         |
| Natural Sciences         | Social & Behavioral Sciences |       4.08018e-221 | True          |
| Other                    | Social & Behavioral Sciences |       6.37992e-119 | True          |

### 4c. Year — Pairwise (Dunn + Bonferroni)

Pairwise comparisons of percentile rank across NMAT years (2006-2018).

**Dunn post-hoc adjusted p-value matrix (Bonferroni) — Year × NMS_PER_num**

|      |        2006 |        2007 |        2008 |        2009 |         2010 |        2011 |        2012 |         2013 |         2014 |        2015 |        2016 |         2017 |         2018 |
|-----:|------------:|------------:|------------:|------------:|-------------:|------------:|------------:|-------------:|-------------:|------------:|------------:|-------------:|-------------:|
| 2006 |           1 |           1 |           1 |           1 |  3.24101e-08 |           1 |           1 |   0.00055928 |            1 | 9.67143e-05 | 6.12575e-21 |  1.19133e-37 |  4.15263e-48 |
| 2007 |           1 |           1 |           1 |           1 |  1.50122e-09 |           1 |           1 |   5.6096e-05 |            1 | 0.000984605 | 7.67926e-19 |  1.17437e-34 |  9.92299e-45 |
| 2008 |           1 |           1 |           1 |           1 |  4.94325e-06 |           1 |           1 |    0.0419838 |            1 | 3.42111e-10 |   2.159e-34 |  2.70216e-60 |  6.66947e-75 |
| 2009 |           1 |           1 |           1 |           1 |  3.08441e-16 |           1 |           1 |  5.51819e-09 |     0.405923 | 1.80774e-05 | 2.67626e-29 |  4.43261e-59 |  4.80864e-76 |
| 2010 | 3.24101e-08 | 1.50122e-09 | 4.94325e-06 | 3.08441e-16 |            1 | 6.93585e-14 | 5.88197e-10 |            1 |   6.4589e-09 | 2.57584e-47 | 1.9024e-104 | 9.01455e-174 | 6.10759e-202 |
| 2011 |           1 |           1 |           1 |           1 |  6.93585e-14 |           1 |           1 |  5.49386e-07 |            1 | 1.08183e-08 | 4.66063e-38 |  1.67846e-75 |  2.12941e-95 |
| 2012 |           1 |           1 |           1 |           1 |  5.88197e-10 |           1 |           1 |  0.000387413 |            1 |  5.6338e-13 | 3.77019e-47 |  2.63969e-90 |  5.2274e-112 |
| 2013 |  0.00055928 |  5.6096e-05 |   0.0419838 | 5.51819e-09 |            1 | 5.49386e-07 | 0.000387413 |            1 |   0.00277538 | 7.19185e-34 |  6.4552e-84 | 1.92512e-145 | 5.95554e-172 |
| 2014 |           1 |           1 |           1 |    0.405923 |   6.4589e-09 |           1 |           1 |   0.00277538 |            1 | 3.15817e-16 | 1.98045e-55 | 1.03435e-106 | 4.08454e-131 |
| 2015 | 9.67143e-05 | 0.000984605 | 3.42111e-10 | 1.80774e-05 |  2.57584e-47 | 1.08183e-08 |  5.6338e-13 |  7.19185e-34 |  3.15817e-16 |           1 | 6.97069e-10 |  3.45283e-30 |  1.79545e-44 |
| 2016 | 6.12575e-21 | 7.67926e-19 |   2.159e-34 | 2.67626e-29 |  1.9024e-104 | 4.66063e-38 | 3.77019e-47 |   6.4552e-84 |  1.98045e-55 | 6.97069e-10 |           1 |  0.000927839 |  7.00624e-11 |
| 2017 | 1.19133e-37 | 1.17437e-34 | 2.70216e-60 | 4.43261e-59 | 9.01455e-174 | 1.67846e-75 | 2.63969e-90 | 1.92512e-145 | 1.03435e-106 | 3.45283e-30 | 0.000927839 |            1 |    0.0546028 |
| 2018 | 4.15263e-48 | 9.92299e-45 | 6.66947e-75 | 4.80864e-76 | 6.10759e-202 | 2.12941e-95 | 5.2274e-112 | 5.95554e-172 | 4.08454e-131 | 1.79545e-44 | 7.00624e-11 |    0.0546028 |            1 |

---

*Significance codes: *** p<0.001, ** p<0.01, * p<0.05, ns not significant*

---



<a id="12-policy-tables-and-export"></a>

**Generated:** 2026-07-31 16:32

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subsets:** `bestobservable` (PLE-linked analyses, Year <= 2014) and `besttrend` (survival analysis, 2006-2018)

**Filters:** None (full unfiltered dataset)

---

## 1. PLE Alignment by Year

PLE status distribution across NMAT years for the observable best-record cohort (Year <= 2014).

**Table: PLE alignment by NMAT year**

|   Year |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|-------:|----------------------------:|------------------------:|-------------------------:|--------------------------:|
|   2006 |                        3698 |                    2005 |                     1693 |                     54.22 |
|   2007 |                        3690 |                    1832 |                     1858 |                     49.65 |
|   2008 |                        4965 |                    2583 |                     2382 |                     52.02 |
|   2009 |                        7461 |                    3757 |                     3704 |                     50.36 |
|   2010 |                        8623 |                    4534 |                     4089 |                     52.58 |
|   2011 |                        8842 |                    3918 |                     4924 |                     44.31 |
|   2012 |                        9405 |                    4006 |                     5399 |                     42.59 |
|   2013 |                        9867 |                    4210 |                     5657 |                     42.67 |
|   2014 |                       12952 |                    4736 |                     8216 |                     36.57 |

---
## 2. PLE Alignment by Course Group

PLE status and median percentile rank by course group (observable best-record cohort).

**Table: PLE alignment by UNDERGRAD_COURSE_GROUP**

| UNDERGRAD_COURSE_GROUP       |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Education                    |                        3188 |                    1699 |                     1489 |                     53.29 |                       53 |
| Other                        |                        6612 |                    3201 |                     3411 |                     48.41 |                       55 |
| Medical & Allied             |                       38144 |                   17833 |                    20311 |                     46.75 |                       48 |
| Natural Sciences             |                       16512 |                    6994 |                     9518 |                     42.36 |                       63 |
| Engineering & Technology     |                         318 |                     118 |                      200 |                     37.11 |                       71 |
| Social & Behavioral Sciences |                        4729 |                    1736 |                     2993 |                     36.71 |                       63 |

---
## 3. PLE Alignment by University Type

PLE status and median percentile rank by university type (Public, Private, Foreign). Observable best-record cohort.

**Table: PLE alignment by UNDERGRAD_UNI_TYPE**

| UNDERGRAD_UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:---------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Foreign              |                        1159 |                     258 |                      901 |                     22.26 |                       57 |
| Private              |                       52821 |                   23757 |                    29064 |                     44.98 |                       50 |
| Public               |                       14642 |                    7226 |                     7416 |                     49.35 |                       66 |

---
## 4. Survival to Top Decile Bins (B8-B10) by Course Group

Proportion of examinees in each course group whose best-record percentile rank falls in the top three bins (B8 = 70th-79th, B9 = 80th-89th, B10 = 90th-99th).

**Table: Survival to top bins (B8-B10) by UNDERGRAD_COURSE_GROUP**

| UNDERGRAD_COURSE_GROUP       |   total_examinees |   top_decile_n |   survival_rate_pct |
|:-----------------------------|------------------:|---------------:|--------------------:|
| Engineering & Technology     |               730 |            383 |               52.47 |
| Natural Sciences             |             40196 |          14760 |               36.72 |
| Other                        |              8248 |           2910 |               35.28 |
| Education                    |              3445 |           1160 |               33.67 |
| Medical & Allied             |             63468 |          18354 |               28.92 |
| Social & Behavioral Sciences |             15758 |           4485 |               28.46 |

---

*All PLE-linked analyses use the observable best-record cohort (Year <= 2014) to avoid misclassifying later cohorts as non-passers before their licensure window closes.*

---



<a id="13-ched-compliance"></a>

**Generated:** 2026-07-31 16:32

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subsets:**
- `bestobservable` (Year <= 2014) — PLE-linked summaries
- `besttrend` (2006-2018) — score distributions and cut-off scenarios

**Filters:** None (full unfiltered dataset)

---

## Section A: National PLE Benchmark

Annual national PLE linkage rate and 5-year rolling average. The CHED amendment uses the 5-year rolling average as the benchmark: PHEIs above this benchmark may set cut-off at 30th percentile; those below must maintain 40th percentile.

**Table A1. Annual national PLE linkage rate with 5-year rolling average**

|   Year |   n_examinees |   n_confirmed_ple |   ple_linkage_rate_pct |   5yr_rolling_avg_pct |
|-------:|--------------:|------------------:|-----------------------:|----------------------:|
|   2006 |          3698 |              2005 |                  54.22 |                   nan |
|   2007 |          3690 |              1832 |                  49.65 |                   nan |
|   2008 |          4965 |              2583 |                  52.02 |                 51.96 |
|   2009 |          7461 |              3757 |                  50.36 |                 51.56 |
|   2010 |          8623 |              4534 |                  52.58 |                 51.77 |
|   2011 |          8842 |              3918 |                  44.31 |                 49.78 |
|   2012 |          9405 |              4006 |                  42.59 |                 48.37 |
|   2013 |          9867 |              4210 |                  42.67 |                  46.5 |
|   2014 |         12952 |              4736 |                  36.57 |                 43.74 |

**Latest 5-year national average (benchmark):**

| Metric | Value |
|--------|------:|
| Latest 5-year national avg | 43.74% |
| Reference year | 2014 |

---
## Section B: Per-HEI PLE Performance vs National Benchmark

Each HEI's PLE linkage rate compared to the national 5-year rolling average. Only HEIs with at least 5 observable best-record examinees are shown. Green = above benchmark (30th percentile eligible), Red = below benchmark (40th percentile required).

**Summary:**

| Metric | Value |
|--------|------:|
| HEIs above benchmark | 213 |
| HEIs below benchmark | 343 |
| National benchmark | 43.74% |

**Table B1. Per-HEI PLE performance vs benchmark**
*(Minimum examinees: 5, sorted by PLE linkage rate descending)*

| UNDERGRAD_UNIVERSITY                                                                  | UNDERGRAD_UNI_TYPE   |   n_examinees |   median_percentile |   ple_linkage_rate_pct | status                          |
|:--------------------------------------------------------------------------------------|:---------------------|--------------:|--------------------:|-----------------------:|:--------------------------------|
| WESTERN LEYTE COLLEGE OF ORMOC CITY                                                   | Private              |             5 |                  76 |                    100 | Above benchmark (30th eligible) |
| COLLEGE OF THE HOLY SPIRIT OF TARLAC                                                  | Private              |             8 |                53.5 |                   87.5 | Above benchmark (30th eligible) |
| SAN SEBASTIAN COLLEGE - RECOLETOS CANLUBANG                                           | Private              |             6 |                  71 |                  83.33 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES SCH. OF HEALTH SCIENCES -LEYTE                          | Public               |            11 |                  25 |                  81.82 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS CEBU                                     | Public               |            37 |                  78 |                  81.08 | Above benchmark (30th eligible) |
| BATANGAS STATE UNIVERSITY BATANGAS CITY                                               | Public               |             5 |                  45 |                     80 | Above benchmark (30th eligible) |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                               | Public               |            12 |                  50 |                     75 | Above benchmark (30th eligible) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA - CALAMBA                                   | Private              |            16 |                  65 |                     75 | Above benchmark (30th eligible) |
| COLLEGE OF HOLY SPIRIT-MANILA                                                         | Private              |            12 |                  15 |                     75 | Above benchmark (30th eligible) |
| RUTGERS UNIVERSITY                                                                    | Foreign              |             7 |                  81 |                  71.43 | Above benchmark (30th eligible) |
| FELLOWSHIP BAPTIST COLLEGE                                                            | Private              |             7 |                  69 |                  71.43 | Above benchmark (30th eligible) |
| VISAYAS STATE UNIVERSITY - MAIN                                                       | Public               |             7 |                  54 |                  71.43 | Above benchmark (30th eligible) |
| CATANDUANES STATE COLLEGE                                                             | Public               |             7 |                   9 |                  71.43 | Above benchmark (30th eligible) |
| UNIVERSITY OF LUZON ( DAGUPAN CITY )                                                  | Private              |             7 |                  25 |                  71.43 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS ILOILO                                        | Public               |           183 |                  75 |                  71.04 | Above benchmark (30th eligible) |
| CALAMBA DOCTORS' COLLEGE                                                              | Private              |            10 |                  52 |                     70 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - TACLOBAN                                              | Public               |            49 |                  62 |                  69.39 | Above benchmark (30th eligible) |
| UNIVERSITY OF BOHOL TAGBILARAN CITY                                                   | Private              |            13 |                  40 |                  69.23 | Above benchmark (30th eligible) |
| WESTERN STATE UNIVERSITY OF COLORADO                                                  | Foreign              |            19 |                  50 |                  68.42 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - CEBU COLLEGE                                          | Public               |            46 |                  75 |                  67.39 | Above benchmark (30th eligible) |
| ST. LOUIS UNIVERSITY BAGUIO CITY                                                      | Private              |           208 |                  51 |                  67.31 | Above benchmark (30th eligible) |
| VELEZ COLLEGE CEBU                                                                    | Private              |           559 |                  51 |                  66.73 | Above benchmark (30th eligible) |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-ALABANG ZAPOTE                              | Private              |             9 |                  31 |                  66.67 | Above benchmark (30th eligible) |
| UNIVERSITY OF CEBU - LAPULAPU AND MANDAUE                                             | Private              |             6 |                42.5 |                  66.67 | Above benchmark (30th eligible) |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE NEGROS OCCIDENTAL                                | Private              |            12 |                  50 |                  66.67 | Above benchmark (30th eligible) |
| NORTHERN NEGROS STATE COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                        | Public               |             6 |                  68 |                  66.67 | Above benchmark (30th eligible) |
| LYCEUM OF THE PHILIPPINES                                                             | Private              |            18 |                40.5 |                  66.67 | Above benchmark (30th eligible) |
| AGO MEDICAL EDUCATIONAL FOUNDATION LEGASPI CITY                                       | Private              |             6 |                  31 |                  66.67 | Above benchmark (30th eligible) |
| CATANDUANES STATE COLLEGE - MAIN                                                      | Public               |            18 |                  50 |                  66.67 | Above benchmark (30th eligible) |
| SILLIMAN UNIVERSITY DUMAGUETE CITY                                                    | Private              |           227 |                  53 |                   65.2 | Above benchmark (30th eligible) |
| Mariano Marcos State University - College Of Fisheries - Currimao                     | Not Specified        |           110 |                46.5 |                  64.55 | Above benchmark (30th eligible) |
| UNIVERSITY OF CEBU (FORMERLY CEBU CENTRAL COLLEGES)                                   | Private              |            30 |                38.5 |                  63.33 | Above benchmark (30th eligible) |
| U.P. VISAYAS (TACLOBAN CITY LEYTE)                                                    | Public               |             8 |                70.5 |                   62.5 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - LOS BANOS LAGUNA                                      | Public               |           487 |                  80 |                  62.42 | Above benchmark (30th eligible) |
| ATENEO DE MANILA UNIVERSITY                                                           | Private              |           751 |                  89 |                  62.05 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                                | Public               |          2519 |                  90 |                  61.65 | Above benchmark (30th eligible) |
| SACRED HEART COLLEGE LUCENA CITY                                                      | Private              |            13 |                  42 |                  61.54 | Above benchmark (30th eligible) |
| CANOSSA COLLEGE                                                                       | Private              |            13 |                  73 |                  61.54 | Above benchmark (30th eligible) |
| SAINT LOUIS UNIVERSITY - BAGUIO                                                       | Private              |           381 |                  43 |                  61.42 | Above benchmark (30th eligible) |
| FAR EASTERN UNIVERSITY - NRMF (FAIRVIEW Q.C.)                                         | Private              |           428 |                33.5 |                  61.21 | Above benchmark (30th eligible) |
| MARIANO MARCOS STATE UNIVERSITY ILOCOS NORTE                                          | Public               |            33 |                  34 |                  60.61 | Above benchmark (30th eligible) |
| CENTRAL COLLEGE OF PANGASINAN - SAN CARLOS CITY PANGASINAN                            | Private              |             5 |                  47 |                     60 | Above benchmark (30th eligible) |
| COLEGIO DE SAN JUAN DE LETRAN MANILA                                                  | Private              |             5 |                  41 |                     60 | Above benchmark (30th eligible) |
| TEMPLE UNIVERSITY USA                                                                 | Foreign              |             5 |                  69 |                     60 | Above benchmark (30th eligible) |
| Adventist University Of Indonesia                                                     | Not Specified        |             5 |                  70 |                     60 | Above benchmark (30th eligible) |
| SIENA COLLEGE-TAYTAY                                                                  | Private              |             5 |                  31 |                     60 | Above benchmark (30th eligible) |
| AGO MEDICAL AND EDUCATIONAL CENTER LEGAZPI CITY                                       | Private              |            20 |                32.5 |                     60 | Above benchmark (30th eligible) |
| BICOL UNIVERSITY - POLANGUI                                                           | Public               |             5 |                  40 |                     60 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE EAST - RAMON MAGSAYSAY MEM. MEDICAL CENTER                          | Private              |            60 |                  57 |                     60 | Above benchmark (30th eligible) |
| URDANETA CITY UNIVERSITY                                                              | Public               |            10 |                49.5 |                     60 | Above benchmark (30th eligible) |
| CEBU NORMAL UNIVERSITY                                                                | Public               |           242 |                  66 |                   59.5 | Above benchmark (30th eligible) |
| RIVERSIDE COLLEGE BACOLOD CITY                                                        | Private              |            27 |                  37 |                  59.26 | Above benchmark (30th eligible) |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING & LIBERAL ARTS                            | Private              |            22 |                48.5 |                  59.09 | Above benchmark (30th eligible) |
| BICOL UNIVERSITY COLLEGE OF SCIENCE LEGAZPI CITY                                      | Public               |            22 |                17.5 |                  59.09 | Above benchmark (30th eligible) |
| BICOL UNIVERSITY COLLEGE OF NURSING LEGAZPI CITY                                      | Public               |            17 |                  66 |                  58.82 | Above benchmark (30th eligible) |
| WEST VISAYAS STATE UNIVERSITY ILOILO                                                  | Public               |           360 |                  59 |                  58.06 | Above benchmark (30th eligible) |
| XAVIER UNIVERSITY CAGAYAN DE ORO CITY                                                 | Private              |           351 |                  53 |                  57.83 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE IMMACULATE CONCEPCION DAVAO CITY                                    | Private              |            26 |                31.5 |                  57.69 | Above benchmark (30th eligible) |
| UNIVERSITY OF SAN CARLOS CEBU CITY                                                    | Private              |           159 |                  40 |                  57.23 | Above benchmark (30th eligible) |
| ST. ALEXIUS COLLEGE                                                                   | Private              |            14 |                  41 |                  57.14 | Above benchmark (30th eligible) |
| COLEGIO DE SAN LORENZO RUIZ DE MANILA OF NORTHERN SAMAR                               | Private              |             7 |                  55 |                  57.14 | Above benchmark (30th eligible) |
| NEGROS ORIENTAL STATE UNIVERSITY                                                      | Public               |             7 |                  13 |                  57.14 | Above benchmark (30th eligible) |
| HOLY NAME UNIVERSITY - TAGBILARAN CITY                                                | Private              |            21 |                  41 |                  57.14 | Above benchmark (30th eligible) |
| INTERNATIONAL COLLEGES OF ASIA - TAMBAC PANGASINAN                                    | Private              |             7 |                  26 |                  57.14 | Above benchmark (30th eligible) |
| AQUINAS UNIVERSITY LEGASPI CITY                                                       | Private              |            21 |                  33 |                  57.14 | Above benchmark (30th eligible) |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - SOUTH LA UNION                         | Public               |             7 |                  67 |                  57.14 | Above benchmark (30th eligible) |
| ALDERSGATE COLLEGE                                                                    | Private              |             7 |                  51 |                  57.14 | Above benchmark (30th eligible) |
| REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION TACLOBAN                               | Private              |           130 |                  39 |                  56.92 | Above benchmark (30th eligible) |
| UNIVERSITY OF ST. LA SALLE - DASMARIÑAS CAVITE                                        | Private              |            30 |                  33 |                  56.67 | Above benchmark (30th eligible) |
| WEST NEGROS UNIVERSITY                                                                | Private              |            23 |                  57 |                  56.52 | Above benchmark (30th eligible) |
| LYCEUM NORTHWESTERN DAGUPAN CITY                                                      | Private              |            64 |                  19 |                  56.25 | Above benchmark (30th eligible) |
| UNIVERSITY OF EASTERN PHILIPPINES - SAMAR                                             | Public               |            16 |                  14 |                  56.25 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                               | Public               |          2209 |                  90 |                  56.18 | Above benchmark (30th eligible) |
| MINDANAO STATE UNIVERSITY ILIGAN CITY                                                 | Public               |           205 |                  53 |                   56.1 | Above benchmark (30th eligible) |
| FATHER SATURNINO M. URIOS UNIVERSITY                                                  | Private              |            50 |                  50 |                     56 | Above benchmark (30th eligible) |
| DE LA SALLE - LIPA BATANGAS                                                           | Private              |            61 |                  46 |                  55.74 | Above benchmark (30th eligible) |
| UNIVERSITY OF ST. LA SALLE BACOLOD CITY                                               | Private              |            99 |                  45 |                  55.56 | Above benchmark (30th eligible) |
| SACRED HEART COLLEGE OF LUCENA                                                        | Private              |            36 |                52.5 |                  55.56 | Above benchmark (30th eligible) |
| UNIVERSITY OF SAN JOSE - RECOLETOS                                                    | Private              |            27 |                  41 |                  55.56 | Above benchmark (30th eligible) |
| WESLEYAN UNIVERSITY-PHILIPPINES CABANATUAN CITY                                       | Private              |            29 |                  33 |                  55.17 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO CITY                                           | Public               |           196 |                  69 |                   55.1 | Above benchmark (30th eligible) |
| DE LA SALLE UNIVERSITY - MANILA                                                       | Private              |          1464 |                  69 |                  54.64 | Above benchmark (30th eligible) |
| MINDANAO STATE UNIVERSITY GENERAL SANTOS CITY                                         | Public               |            33 |                  38 |                  54.55 | Above benchmark (30th eligible) |
| BALIUAG UNIVERSITY                                                                    | Private              |            11 |                  41 |                  54.55 | Above benchmark (30th eligible) |
| ST. JOSEPH'S COLLEGE QUEZON CITY                                                      | Private              |            11 |                  25 |                  54.55 | Above benchmark (30th eligible) |
| 13207A                                                                                | Not Specified        |            22 |                30.5 |                  54.55 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE EAST (C.M. RECTO MANILA)                                            | Private              |           143 |                  51 |                  54.55 | Above benchmark (30th eligible) |
| NORTHWESTERN UNIVERSITY                                                               | Private              |            11 |                  33 |                  54.55 | Above benchmark (30th eligible) |
| UNIVERSITY OF CORDILLERAS                                                             | Private              |            11 |                  37 |                  54.55 | Above benchmark (30th eligible) |
| DE LA SALLE UNIVERSITY - DASMARIÑAS CAVITE                                            | Private              |           457 |                  34 |                  54.05 | Above benchmark (30th eligible) |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE                                                  | Private              |            39 |                57.5 |                  53.85 | Above benchmark (30th eligible) |
| DE LA SALLE - HEALTH SCIENCES CAMPUS                                                  | Private              |           136 |                  39 |                  53.68 | Above benchmark (30th eligible) |
| UNIVERSITY OF LA SALETTE SANTIAGO CITY                                                | Private              |            28 |                30.5 |                  53.57 | Above benchmark (30th eligible) |
| CEBU INSTITUTE OF TECHNOLOGY - UNIVERSITY                                             | Private              |            15 |                  46 |                  53.33 | Above benchmark (30th eligible) |
| ARELLANO UNIVERSITY - PASIG                                                           | Private              |            15 |                  43 |                  53.33 | Above benchmark (30th eligible) |
| ILOCOS SUR COMMUNITY COLLEGE - BANTAY ILOCOS SUR                                      | Public               |            15 |                  21 |                  53.33 | Above benchmark (30th eligible) |
| JOHN PAUL II COLLEGE OF DAVAO                                                         | Private              |            15 |                  39 |                  53.33 | Above benchmark (30th eligible) |
| ATENEO DE DAVAO UNIVERSITY                                                            | Private              |           753 |                  51 |                  53.25 | Above benchmark (30th eligible) |
| UNIVERSITY OF SAN AGUSTIN - ILOILO CITY                                               | Private              |           126 |                  39 |                  52.38 | Above benchmark (30th eligible) |
| CEBU DOCTORS COLLEGE CEBU CITY                                                        | Private              |           149 |                  28 |                  52.35 | Above benchmark (30th eligible) |
| MOUNTAIN VIEW COLLEGE BUKIDNON                                                        | Private              |            46 |                  42 |                  52.17 | Above benchmark (30th eligible) |
| CENTRAL LUZON STATE UNIVERSITY                                                        | Public               |            52 |                  54 |                  51.92 | Above benchmark (30th eligible) |
| BICOL UNIVERSITY - TABACO                                                             | Public               |            27 |                  48 |                  51.85 | Above benchmark (30th eligible) |
| SAN PEDRO COLLEGE DAVAO CITY                                                          | Private              |           514 |                  37 |                  51.36 | Above benchmark (30th eligible) |
| UERM MEMORIAL MEDICAL CENTER                                                          | Private              |            88 |                48.5 |                  51.14 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                              | Public               |           208 |                  72 |                  50.96 | Above benchmark (30th eligible) |
| UNIVERSITY OF PERPETUAL HELP - DR. JOSE G. TAMAYO MEDICAL UNIVERSITY                  | Private              |            55 |                  49 |                  50.91 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE CORDILLERAS (BCF)                                                   | Private              |            63 |                  33 |                  50.79 | Above benchmark (30th eligible) |
| DE LA SALLE - COLLEGE OF SAINT BENILDE                                                | Private              |            20 |                  70 |                     50 | Above benchmark (30th eligible) |
| PHILIPPINE REHABILITATION INSTITUTE                                                   | Private              |            12 |                  35 |                     50 | Above benchmark (30th eligible) |
| IMMACULATE CONCEPTION COLLEGE - ALBAY                                                 | Private              |             8 |                  66 |                     50 | Above benchmark (30th eligible) |
| ST. JOSEPH'S COLLEGE OF QUEZON CITY                                                   | Private              |            30 |                  41 |                     50 | Above benchmark (30th eligible) |
| FIRST ASIA INSTITUTE OF TECHNOLOGY AND HUMANITIES                                     | Private              |             6 |                  55 |                     50 | Above benchmark (30th eligible) |
| GORDON COLLEGE                                                                        | Public               |             6 |                  53 |                     50 | Above benchmark (30th eligible) |
| SAN LORENZO RUIZ COLLEGE OF ORMOC                                                     | Private              |            20 |                  32 |                     50 | Above benchmark (30th eligible) |
| UNIVERSITY OF TEXAS                                                                   | Foreign              |             8 |                  96 |                     50 | Above benchmark (30th eligible) |
| CENTRAL LUZON STATE UNIVERSITY NUEVA ECIJA                                            | Public               |            18 |                34.5 |                     50 | Above benchmark (30th eligible) |
| LORMA COLLEGE SAN FERNANDO LA UNION                                                   | Private              |            24 |                  20 |                     50 | Above benchmark (30th eligible) |
| SAMAR STATE UNIVERSITY - MAIN                                                         | Public               |             6 |                  48 |                     50 | Above benchmark (30th eligible) |
| LA CONSOLACION UNIVERSITY PHILIPPINES                                                 | Private              |             6 |                57.5 |                     50 | Above benchmark (30th eligible) |
| LEYTE NORMAL UNIVERSITY                                                               | Public               |            12 |                  29 |                     50 | Above benchmark (30th eligible) |
| ST. SCHOLASTICA'S COLLEGE - TACLOBAN CITY                                             | Private              |            26 |                  31 |                     50 | Above benchmark (30th eligible) |
| METROPOLITAN HOSPITAL COLLEGE OF NURSING                                              | Private              |            60 |                  41 |                     50 | Above benchmark (30th eligible) |
| MANILA ADVENTIST MEDICAL CENTER - PASAY CITY                                          | Private              |            16 |                  40 |                     50 | Above benchmark (30th eligible) |
| ANDRES BONIFACIO COLLEGE                                                              | Private              |             6 |                45.5 |                     50 | Above benchmark (30th eligible) |
| DE LA SALLE COLLEGE OF SAINT BENILDE - MANILA                                         | Private              |            20 |                57.5 |                     50 | Above benchmark (30th eligible) |
| MARY HELP OF CHRISTIANS COLLEGE SEMINARY                                              | Private              |            10 |                16.5 |                     50 | Above benchmark (30th eligible) |
| NOTRE DAME OF MARBEL UNIV.                                                            | Private              |            12 |                43.5 |                     50 | Above benchmark (30th eligible) |
| BUKIDNON STATE UNIVERSITY                                                             | Public               |             6 |                  42 |                     50 | Above benchmark (30th eligible) |
| OUR LADY OF FATIMA NOVALICHES                                                         | Private              |             6 |                18.5 |                     50 | Above benchmark (30th eligible) |
| ARRIESGADO COLLEGE FOUNDATION                                                         | Private              |             6 |                50.5 |                     50 | Above benchmark (30th eligible) |
| SOUTHERN LUZON POLYTECHNIC COLLEGE - LUCBAN QUEZON                                    | Private              |             6 |                  28 |                     50 | Above benchmark (30th eligible) |
| SOUTHVILLE INTERNATIONAL SCHOOL AND COLLEGES                                          | Private              |           132 |                  52 |                     50 | Above benchmark (30th eligible) |
| CHIANG KAI SHEK COLLEGE                                                               | Private              |             8 |                58.5 |                     50 | Above benchmark (30th eligible) |
| 13155D                                                                                | Not Specified        |             8 |                  63 |                     50 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                       | Public               |            86 |                  66 |                     50 | Above benchmark (30th eligible) |
| NORTHERN CHRISTIAN COLLEGE                                                            | Private              |             8 |                  50 |                     50 | Above benchmark (30th eligible) |
| ST. PAUL UNIVERSITY ILOILO                                                            | Private              |           221 |                  57 |                  49.32 | Above benchmark (30th eligible) |
| ATENEO DE NAGA UNIVERSITY                                                             | Private              |           146 |                  46 |                  49.32 | Above benchmark (30th eligible) |
| MINDANAO STATE UNIVERSITY MARAWI CITY                                                 | Public               |           346 |                37.5 |                  49.13 | Above benchmark (30th eligible) |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION INC.                                          | Private              |            49 |                  25 |                  48.98 | Above benchmark (30th eligible) |
| UNIVERSITY OF NEGROS OCCIDENTAL-RECOLETOS                                             | Private              |            94 |                  54 |                  48.94 | Above benchmark (30th eligible) |
| AQUINAS UNIVERSITY OF LEGAZPI                                                         | Private              |            80 |                44.5 |                  48.75 | Above benchmark (30th eligible) |
| SAINT SCHOLASTICA'S COLLEGE TACLOBAN                                                  | Private              |           117 |                  48 |                  48.72 | Above benchmark (30th eligible) |
| UNIVERSIDAD DE STA. ISABEL NAGA CITY                                                  | Private              |            39 |                  40 |                  48.72 | Above benchmark (30th eligible) |
| UNIVERSIDAD DE STA. ISABEL                                                            | Private              |           172 |                  53 |                  48.26 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                             | Public               |           595 |                  67 |                  48.24 | Above benchmark (30th eligible) |
| LA CONSOLACION COLLEGE - MANILA                                                       | Private              |            50 |                44.5 |                     48 | Above benchmark (30th eligible) |
| SAINT PAUL UNIVERSITY PHILIPPINES                                                     | Private              |           215 |                  49 |                  47.91 | Above benchmark (30th eligible) |
| RIVERSIDE COLLEGE OF NURSING BACOLOD                                                  | Private              |            23 |                  33 |                  47.83 | Above benchmark (30th eligible) |
| AGO MEDICAL AND EDUCATIONAL CENTER - BICOL CHRISTIAN COLLEGE OF MEDICINE              | Private              |            44 |                45.5 |                  47.73 | Above benchmark (30th eligible) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - BINAN LAGUNA                                    | Private              |            44 |                30.5 |                  47.73 | Above benchmark (30th eligible) |
| UNIVERSITY OF SANTO TOMAS                                                             | Private              |         11724 |                  63 |                  47.69 | Above benchmark (30th eligible) |
| DR. CARLOS S. LANTING COLLEGE                                                         | Private              |            42 |                  36 |                  47.62 | Above benchmark (30th eligible) |
| CAVITE STATE UNIVERSITY - MAIN                                                        | Public               |            21 |                  57 |                  47.62 | Above benchmark (30th eligible) |
| CENTRAL LUZON DOCTOR'S HOSPITAL TARLAC                                                | Private              |            21 |                  41 |                  47.62 | Above benchmark (30th eligible) |
| LYCEUM OF THE PHILIPPINES UNIVERSITY - BATANGAS                                       | Private              |           112 |                48.5 |                  47.32 | Above benchmark (30th eligible) |
| ATENEO DE MANILA UNIVERSITY - QUEZON CITY                                             | Private              |          1026 |                  77 |                  47.27 | Above benchmark (30th eligible) |
| UNIVERSITY OF PANGASINAN DAGUPAN CITY                                                 | Private              |            17 |                  30 |                  47.06 | Above benchmark (30th eligible) |
| UNIVERSITY OF ASIA AND THE PACIFIC                                                    | Private              |            17 |                  42 |                  47.06 | Above benchmark (30th eligible) |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                    | Public               |            17 |                  66 |                  47.06 | Above benchmark (30th eligible) |
| CENTRAL LUZON DOCTORS' HOSPITAL EDUCATIONAL INSTITUTION                               | Private              |            34 |                  53 |                  47.06 | Above benchmark (30th eligible) |
| BULACAN STATE UNIVERSITY                                                              | Public               |            17 |                  45 |                  47.06 | Above benchmark (30th eligible) |
| UNIVERSITY OF SOUTHERN PHILIPPINES FOUNDATION                                         | Private              |            32 |                22.5 |                  46.88 | Above benchmark (30th eligible) |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                                | Public               |            62 |                  46 |                  46.77 | Above benchmark (30th eligible) |
| HOLY INFANT COLLEGE                                                                   | Private              |            30 |                44.5 |                  46.67 | Above benchmark (30th eligible) |
| UNIVERSITY OF PANGASINAN                                                              | Private              |            75 |                  43 |                  46.67 | Above benchmark (30th eligible) |
| ATENEO DE ZAMBOANGA UNIVERSITY                                                        | Private              |           714 |                  38 |                  46.64 | Above benchmark (30th eligible) |
| BROKENSHIRE COLLEGE DAVAO CITY                                                        | Private              |            43 |                  28 |                  46.51 | Above benchmark (30th eligible) |
| SAN BEDA COLLEGE MENDIOLA MANILA                                                      | Private              |           175 |                  34 |                  46.29 | Above benchmark (30th eligible) |
| ST. JUDE COLLEGE MANILA                                                               | Private              |            39 |                  26 |                  46.15 | Above benchmark (30th eligible) |
| COLEGIO DE DAGUPAN                                                                    | Private              |            13 |                  54 |                  46.15 | Above benchmark (30th eligible) |
| LYCEUM OF THE PHILIPPINES - ST. CABRINI COLLEGE OF ALLIED MEDICINE                    | Private              |            13 |                  44 |                  46.15 | Above benchmark (30th eligible) |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                              | Public               |            26 |                  82 |                  46.15 | Above benchmark (30th eligible) |
| UNIVERSITY OF BAGUIO                                                                  | Private              |           195 |                  43 |                  46.15 | Above benchmark (30th eligible) |
| TARLAC STATE UNIVERSITY                                                               | Public               |            13 |                  56 |                  46.15 | Above benchmark (30th eligible) |
| CENTRO ESCOLAR UNIVERSITY - MENDIOLA MANILA                                           | Private              |           384 |                  28 |                  46.09 | Above benchmark (30th eligible) |
| MANILA DOCTORS COLLEGE - PASAY CITY                                                   | Private              |            87 |                  43 |                  45.98 | Above benchmark (30th eligible) |
| SILLIMAN UNIVERSITY                                                                   | Private              |           648 |                  53 |                  45.83 | Above benchmark (30th eligible) |
| ST. PAUL UNIVERSITY - MANILA                                                          | Private              |           112 |                42.5 |                  45.54 | Above benchmark (30th eligible) |
| UNIVERSITY OF BOHOL                                                                   | Private              |            11 |                  47 |                  45.45 | Above benchmark (30th eligible) |
| COLEGIO DE SAN AGUSTIN BACOLOD                                                        | Private              |            22 |                  29 |                  45.45 | Above benchmark (30th eligible) |
| ASSUMPTION COLLEGE MAKATI                                                             | Private              |            22 |                49.5 |                  45.45 | Above benchmark (30th eligible) |
| PHILIPPINE NORMAL COLLEGE TAFT AVENUE MANILA                                          | Public               |            11 |                  54 |                  45.45 | Above benchmark (30th eligible) |
| LYCEUM OF ILIGAN FOUNDATION                                                           | Private              |            11 |                  76 |                  45.45 | Above benchmark (30th eligible) |
| FAR EASTERN UNIVERSITY                                                                | Private              |          2413 |                  44 |                  45.42 | Above benchmark (30th eligible) |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                   | Public               |            31 |                  42 |                  45.16 | Above benchmark (30th eligible) |
| WESLEYAN UNIVERSITY - PHILIPPINES (CABANATUAN)                                        | Private              |            71 |                  36 |                  45.07 | Above benchmark (30th eligible) |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES INC.                                            | Private              |            20 |                  13 |                     45 | Above benchmark (30th eligible) |
| BULACAN STATE UNIVERSITY - MAIN                                                       | Public               |            80 |                  52 |                     45 | Above benchmark (30th eligible) |
| UNIVERSITY OF PERPETUAL HELP COLLEGE OF LAS PINAS                                     | Private              |            20 |                35.5 |                     45 | Above benchmark (30th eligible) |
| SAINT LOUIS UNIVERSITY                                                                | Private              |          1357 |                  52 |                  44.73 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                                | Public               |           376 |                  66 |                  44.68 | Above benchmark (30th eligible) |
| CEBU DOCTOR'S UNIVERSITY COLLEGE OF MEDICINE - MANDAUE CITY CEBU                      | Private              |            56 |                45.5 |                  44.64 | Above benchmark (30th eligible) |
| TRINITY UNIVERSITY OF ASIA                                                            | Private              |           617 |                  54 |                  44.57 | Above benchmark (30th eligible) |
| UNIVERSITY OF ST. LA SALLE                                                            | Private              |           425 |                  55 |                  44.47 | Above benchmark (30th eligible) |
| NOTRE DAME OF MARBEL COLLEGE SOUTH COTABATO                                           | Private              |             9 |                  38 |                  44.44 | Above benchmark (30th eligible) |
| COLEGIO DE SAN JUAN DE LETRAN CALAMBA                                                 | Private              |            18 |                  20 |                  44.44 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE VISAYAS - MANDAUE                                                   | Private              |            27 |                  40 |                  44.44 | Above benchmark (30th eligible) |
| OUR LADY OF FATIMA UNIVERSITY - LAGRO QUEZON CITY                                     | Private              |            54 |                  32 |                  44.44 | Above benchmark (30th eligible) |
| DAVAO MEDICAL SCHOOL FOUNDATION INC.                                                  | Private              |            36 |                  42 |                  44.44 | Above benchmark (30th eligible) |
| DELOS SANTOS COLLEGE                                                                  | Private              |             9 |                  41 |                  44.44 | Above benchmark (30th eligible) |
| HOLY ANGEL UNIVERSITY ANGELES CITY                                                    | Private              |            18 |                  40 |                  44.44 | Above benchmark (30th eligible) |
| UNIVERSIDAD DE MANILA                                                                 | Public               |             9 |                  54 |                  44.44 | Above benchmark (30th eligible) |
| NEW ERA UNIVERSITY                                                                    | Private              |            61 |                  44 |                  44.26 | Above benchmark (30th eligible) |
| CENTRAL PHILIPPINE UNIVERSITY ILOILO                                                  | Private              |           104 |                  47 |                  44.23 | Above benchmark (30th eligible) |
| UNIVERSITY OF NUEVA CACERES                                                           | Private              |            34 |                  39 |                  44.12 | Above benchmark (30th eligible) |
| VELEZ COLLEGE                                                                         | Private              |           794 |                  57 |                  43.95 | Above benchmark (30th eligible) |
| UNIVERSITY OF CEBU - BANILAD                                                          | Private              |           114 |                39.5 |                  43.86 | Above benchmark (30th eligible) |
| BROKENSHIRE COLLEGE                                                                   | Private              |           210 |                  45 |                  43.81 | Above benchmark (30th eligible) |
| CAPITOL MEDICAL CENTER COLLEGE Q.C.                                                   | Private              |            32 |                  27 |                  43.75 | Above benchmark (30th eligible) |
| UNIVERSITY OF TORONTO                                                                 | Foreign              |            16 |                  80 |                  43.75 | Above benchmark (30th eligible) |
| ST. PAUL COLLEGE ILOILO                                                               | Private              |            16 |                  50 |                  43.75 | Above benchmark (30th eligible) |
| MOUNTAIN VIEW COLLEGE                                                                 | Private              |           135 |                  51 |                   43.7 | Below benchmark (40th required) |
| CEBU DOCTOR'S UNIVERSITY                                                              | Private              |          1242 |                  45 |                  43.64 | Below benchmark (40th required) |
| REMEDIOS T. ROMUALDEZ MEM. SCH. - MMC                                                 | Private              |            78 |                53.5 |                  43.59 | Below benchmark (40th required) |
| MANILA CENTRAL UNIVERSITY                                                             | Private              |           374 |                  38 |                  43.58 | Below benchmark (40th required) |
| BENGUET STATE UNIVERSITY                                                              | Public               |            23 |                  42 |                  43.48 | Below benchmark (40th required) |
| ST. JUDE COLLEGE                                                                      | Private              |            30 |                  33 |                  43.33 | Below benchmark (40th required) |
| CENTRO ESCOLAR UNIVERSITY AT MALOLOS                                                  | Private              |            30 |                  56 |                  43.33 | Below benchmark (40th required) |
| LYCEUM OF BATANGAS                                                                    | Private              |            30 |                  23 |                  43.33 | Below benchmark (40th required) |
| MINDANAO MEDICAL FOUNDATION COLLEGE                                                   | Private              |            30 |                  56 |                  43.33 | Below benchmark (40th required) |
| DE LA SALLE UNIVERSITY - DASMARIÑAS                                                   | Private              |           653 |                  51 |                  43.19 | Below benchmark (40th required) |
| HOLY ANGEL UNIVERSITY                                                                 | Private              |            58 |                  43 |                   43.1 | Below benchmark (40th required) |
| WEST NEGROS COLLEGE BACOLOD                                                           | Private              |             7 |                  19 |                  42.86 | Below benchmark (40th required) |
| VIRGINIA COMMONWEALTH UNIVERSITY                                                      | Foreign              |             7 |                  77 |                  42.86 | Below benchmark (40th required) |
| UNIVERSITY OF THE IMMACULATE CONCEPTION                                               | Private              |           105 |                  43 |                  42.86 | Below benchmark (40th required) |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                               | Public               |           280 |                  63 |                  42.86 | Below benchmark (40th required) |
| HOLY TRINITY COLLEGE PUERTO PRINCESA                                                  | Private              |             7 |                  21 |                  42.86 | Below benchmark (40th required) |
| GENERAL SANTOS DOCTORS' MEDICAL SCHOOL FOUNDATION                                     | Private              |            28 |                  36 |                  42.86 | Below benchmark (40th required) |
| NOTRE DAME OF MIDSAYAP COLLEGE                                                        | Private              |             7 |                62.5 |                  42.86 | Below benchmark (40th required) |
| MABINI COLLEGES                                                                       | Private              |             7 |                  75 |                  42.86 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM                                                   | Private              |             7 |                  10 |                  42.86 | Below benchmark (40th required) |
| UNIVERSITY OF HAWAII AT MANOA                                                         | Foreign              |             7 |                  81 |                  42.86 | Below benchmark (40th required) |
| PLT COLLEGE                                                                           | Private              |             7 |                  41 |                  42.86 | Below benchmark (40th required) |
| KESTER GRANT COLLEGE PHILS. INC.                                                      | Private              |             7 |                  13 |                  42.86 | Below benchmark (40th required) |
| ST. PAUL UNIVERSITY DUMAGUETE                                                         | Private              |            35 |                  51 |                  42.86 | Below benchmark (40th required) |
| ADVENTIST UNIVERSITY OF THE PHILIPPINES                                               | Private              |           355 |                  52 |                  42.82 | Below benchmark (40th required) |
| WESTERN MINDANAO STATE UNIVERSITY ZAMBOANGA CITY                                      | Public               |           145 |                  28 |                  42.76 | Below benchmark (40th required) |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                      | Public               |           810 |                  52 |                  42.72 | Below benchmark (40th required) |
| DOÑA REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION                                   | Private              |           157 |                  45 |                  42.68 | Below benchmark (40th required) |
| WESTERN MINDANAO STATE UNIVERSITY                                                     | Public               |           394 |                  42 |                  42.64 | Below benchmark (40th required) |
| UNIVERSITY OF THE EAST RAMON MAGSAYSAY MEMORIAL MEDICAL CENTER                        | Private              |           365 |                  55 |                  42.47 | Below benchmark (40th required) |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                  | Public               |           660 |                  62 |                  42.42 | Below benchmark (40th required) |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                                | Public               |            66 |                  61 |                  42.42 | Below benchmark (40th required) |
| MAPUA INSTITUTE OF TECHNOLOGY                                                         | Private              |            26 |                53.5 |                  42.31 | Below benchmark (40th required) |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION                                               | Private              |            52 |                42.5 |                  42.31 | Below benchmark (40th required) |
| PHILIPPINE CHRISTIAN UNIVERSITY                                                       | Private              |            26 |                42.5 |                  42.31 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA                                             | Private              |           499 |                53.5 |                  42.28 | Below benchmark (40th required) |
| OUR LADY OF FATIMA UNIVERSITY - QUEZON CITY                                           | Private              |           187 |                  41 |                  42.25 | Below benchmark (40th required) |
| RIVERSIDE COLLEGE                                                                     | Private              |            83 |                43.5 |                  42.17 | Below benchmark (40th required) |
| ADAMSON UNIVERSITY                                                                    | Private              |            76 |                  43 |                  42.11 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - LAGUNA                                          | Private              |            38 |                44.5 |                  42.11 | Below benchmark (40th required) |
| FEU - DR. NICANOR REYES MEDICAL FOUNDATION                                            | Private              |           529 |                49.5 |                  41.97 | Below benchmark (40th required) |
| Remedios Trinidad Romualdez Medical Foundation                                        | Not Specified        |            31 |                  34 |                  41.94 | Below benchmark (40th required) |
| SAN PEDRO COLLEGE                                                                     | Private              |          1081 |                  51 |                  41.91 | Below benchmark (40th required) |
| SAINT MARY'S UNIVERSITY                                                               | Private              |            86 |                  46 |                  41.86 | Below benchmark (40th required) |
| CAPITOL UNIVERSITY                                                                    | Private              |            67 |                  36 |                  41.79 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP - RIZAL                                                  | Private              |            12 |                33.5 |                  41.67 | Below benchmark (40th required) |
| NATIONAL UNIVERSITY                                                                   | Private              |            12 |                  41 |                  41.67 | Below benchmark (40th required) |
| ANGELES UNIVERSITY FOUNDATION                                                         | Private              |           464 |                  48 |                  41.59 | Below benchmark (40th required) |
| UNIVERSITY OF THE CORDILLERAS                                                         | Private              |           202 |                  44 |                  41.58 | Below benchmark (40th required) |
| UNIVERSITY OF BAGUIO BAGUIO CITY                                                      | Private              |           106 |                  23 |                  41.51 | Below benchmark (40th required) |
| BICOL UNIVERSITY                                                                      | Public               |            46 |                  28 |                   41.3 | Below benchmark (40th required) |
| CENTRAL PHILIPPINE UNIVERSITY                                                         | Private              |           308 |                  49 |                  41.23 | Below benchmark (40th required) |
| NOTRE DAME UNIVERSITY                                                                 | Private              |           119 |                  38 |                  41.18 | Below benchmark (40th required) |
| MAKATI MEDICAL CENTER COLLEGE OF NURSING                                              | Private              |           146 |                  46 |                   41.1 | Below benchmark (40th required) |
| ARELLANO UNIVERSITY - MANILA                                                          | Private              |            73 |                  44 |                   41.1 | Below benchmark (40th required) |
| LORMA COLLEGES                                                                        | Private              |            56 |                  37 |                  41.07 | Below benchmark (40th required) |
| OUR LADY OF FATIMA UNIVERSITY (FATIMA MEDICAL SCIENCE FOUNDATION) - VALENZUELA        | Private              |           498 |                  41 |                  40.96 | Below benchmark (40th required) |
| MANILA DOCTORS COLLEGE U.N. AVENUE MANILA                                             | Private              |            59 |                  45 |                  40.68 | Below benchmark (40th required) |
| EASTER COLLEGE                                                                        | Private              |            74 |                  36 |                  40.54 | Below benchmark (40th required) |
| MANILA TYTANA COLLEGES                                                                | Private              |           405 |                  43 |                  40.49 | Below benchmark (40th required) |
| WORLD CITI COLLEGES QUEZON CITY                                                       | Private              |            42 |                  42 |                  40.48 | Below benchmark (40th required) |
| DE LA SALLE - LIPA                                                                    | Private              |           188 |                  44 |                  40.43 | Below benchmark (40th required) |
| UNIVERSITY OF SAN CARLOS                                                              | Private              |           280 |                45.5 |                  40.36 | Below benchmark (40th required) |
| COLEGIO DE SAN JUAN DE LETRAN                                                         | Private              |            67 |                  50 |                   40.3 | Below benchmark (40th required) |
| CENTRO ESCOLAR UNIVERSITY - MAKATI                                                    | Private              |            72 |                  63 |                  40.28 | Below benchmark (40th required) |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                            | Public               |           482 |                  51 |                  40.25 | Below benchmark (40th required) |
| XAVIER UNIVERSITY                                                                     | Private              |           646 |                  52 |                  40.09 | Below benchmark (40th required) |
| UNIVERSITY OF SOUTHERN MINDANAO NORTH COTABATO                                        | Public               |            25 |                  43 |                     40 | Below benchmark (40th required) |
| BENGUET STATE UNIVERSITY - MAIN                                                       | Public               |            80 |                  59 |                     40 | Below benchmark (40th required) |
| CARAGA STATE UNIVERSITY - MAIN                                                        | Public               |            10 |                  35 |                     40 | Below benchmark (40th required) |
| THE COLLEGE OF MAASIN                                                                 | Private              |             5 |                  89 |                     40 | Below benchmark (40th required) |
| JOSE RIZAL UNIVERSITY                                                                 | Private              |             5 |                  46 |                     40 | Below benchmark (40th required) |
| ENDERUN COLLEGE                                                                       | Private              |             5 |                  29 |                     40 | Below benchmark (40th required) |
| HOLY CROSS OF DAVAO COLLEGE                                                           | Private              |             5 |                  54 |                     40 | Below benchmark (40th required) |
| AKLAN STATE UNIVERSITY - MAIN                                                         | Public               |             5 |                  16 |                     40 | Below benchmark (40th required) |
| University For Development Studies                                                    | Not Specified        |             5 |                  21 |                     40 | Below benchmark (40th required) |
| NEW YORK UNIVERSITY NY USA                                                            | Foreign              |             5 |                  88 |                     40 | Below benchmark (40th required) |
| RUTGERS COLLEGE NEW JERSEY                                                            | Foreign              |             5 |                  90 |                     40 | Below benchmark (40th required) |
| UNIVERSITY OF ILOILO                                                                  | Private              |            10 |                  70 |                     40 | Below benchmark (40th required) |
| NAGA COLLEGE FOUNDATION                                                               | Private              |            10 |                  66 |                     40 | Below benchmark (40th required) |
| CAVITE STATE UNIVERSITY CAVITE                                                        | Public               |             5 |                  52 |                     40 | Below benchmark (40th required) |
| UNIV. OF ASIA AND THE PACIFIC - PASIG CITY                                            | Private              |             5 |                  81 |                     40 | Below benchmark (40th required) |
| PILAR COLLEGE                                                                         | Private              |            25 |                  38 |                     40 | Below benchmark (40th required) |
| MEDINA COLLEGE - PAGADIAN                                                             | Private              |            10 |                36.5 |                     40 | Below benchmark (40th required) |
| OLIVAREZ COLLEGE - TAGAYTAY                                                           | Private              |             5 |                  46 |                     40 | Below benchmark (40th required) |
| COLUMBAN COLLEGE - OLONGAPO CITY                                                      | Private              |             5 |                  46 |                     40 | Below benchmark (40th required) |
| SAN BEDA COLLEGE                                                                      | Private              |           288 |                  40 |                  39.93 | Below benchmark (40th required) |
| MINDANAO STATE UNIVERSITY - MARAWI                                                    | Public               |           509 |                  49 |                  39.69 | Below benchmark (40th required) |
| UNIVERSITY OF SAN AGUSTIN                                                             | Private              |           295 |                  51 |                  39.66 | Below benchmark (40th required) |
| ILIGAN MEDICAL CENTER COLLEGE                                                         | Private              |            53 |                41.5 |                  39.62 | Below benchmark (40th required) |
| CENTRO ESCOLAR UNIVERSITY - MANILA                                                    | Private              |           823 |                  46 |                  39.61 | Below benchmark (40th required) |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING AND LIBERAL ARTS                          | Private              |            76 |                55.5 |                  39.47 | Below benchmark (40th required) |
| UNIVERSITY OF MAKATI                                                                  | Public               |            28 |                  43 |                  39.29 | Below benchmark (40th required) |
| MINDANAO SANITARIUM AND HOSPITAL COLLEGE                                              | Private              |           158 |                  41 |                  39.24 | Below benchmark (40th required) |
| MISAMIS UNIVERSITY - OZAMIS CITY                                                      | Private              |            64 |                  48 |                  39.06 | Below benchmark (40th required) |
| UNIVERSITY OF LUZON                                                                   | Private              |            18 |                  17 |                  38.89 | Below benchmark (40th required) |
| ST. PAUL UNIVERSITY - QUEZON CITY                                                     | Private              |           108 |                  30 |                  38.89 | Below benchmark (40th required) |
| FEU - EAST ASIA COLLEGE                                                               | Private              |           103 |                  42 |                  38.83 | Below benchmark (40th required) |
| BICOL UNIVERSITY - MAIN                                                               | Public               |           273 |                  55 |                  38.83 | Below benchmark (40th required) |
| NOTRE DAME OF DADIANGAS COLLEGE GEN. SANTOS                                           | Private              |            44 |                34.5 |                  38.64 | Below benchmark (40th required) |
| DE LA SALLE HEALTH SCIENCES INSTITUTE                                                 | Private              |           355 |                  51 |                  38.59 | Below benchmark (40th required) |
| OUR LADY OF GUADALUPE COLLEGES                                                        | Private              |            13 |                  29 |                  38.46 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP - CALAMBA LAGUNA                                         | Private              |            13 |                  34 |                  38.46 | Below benchmark (40th required) |
| ST. PAUL UNIVERSITY - TUGUEGARAO CAGAYAN                                              | Private              |            34 |                22.5 |                  38.24 | Below benchmark (40th required) |
| ARELLANO UNIVERSITY                                                                   | Private              |            34 |                  26 |                  38.24 | Below benchmark (40th required) |
| SOUTHWESTERN UNIVERSITY CEBU                                                          | Private              |           192 |                  22 |                  38.02 | Below benchmark (40th required) |
| ST. SCHOLASTICA'S COLLEGE                                                             | Private              |            87 |                  44 |                  37.93 | Below benchmark (40th required) |
| CARITAS FAMILY HOSPITAL AND COLLEGES                                                  | Private              |             8 |                  63 |                   37.5 | Below benchmark (40th required) |
| NOTRE DAME OF KIDAPAWAN COLLEGE                                                       | Private              |             8 |                  27 |                   37.5 | Below benchmark (40th required) |
| NOTRE DAME UNIVERSITY COTABATO CITY                                                   | Private              |            56 |                25.5 |                   37.5 | Below benchmark (40th required) |
| ST. JOSEPH COLLEGE CAVITE                                                             | Private              |             8 |                  16 |                   37.5 | Below benchmark (40th required) |
| DE LA SALLE - ARANETA UNIVERSITY                                                      | Private              |             8 |                  25 |                   37.5 | Below benchmark (40th required) |
| UNIVERSITY OF SAINT ANTHONY                                                           | Private              |             8 |                36.5 |                   37.5 | Below benchmark (40th required) |
| OLIVAREZ COLLEGE                                                                      | Private              |            16 |                32.5 |                   37.5 | Below benchmark (40th required) |
| CORDILLERA CAREER DEVELOPMENT COLLEGE                                                 | Private              |             8 |                  62 |                   37.5 | Below benchmark (40th required) |
| DAVAO CENTRAL COLLEGE                                                                 | Private              |             8 |                39.5 |                   37.5 | Below benchmark (40th required) |
| UNION CHRISTIAN COLLEGE                                                               | Private              |            16 |                  41 |                   37.5 | Below benchmark (40th required) |
| UNIVERSITY OF NORTHERN PHILIPPINES VIGAN ILOCOS SUR                                   | Public               |             8 |                  11 |                   37.5 | Below benchmark (40th required) |
| NORTH VALLEY COLLEGE FOUNDATION                                                       | Private              |             8 |                45.5 |                   37.5 | Below benchmark (40th required) |
| ST. PAUL UNIVERSITY SURIGAO                                                           | Private              |             8 |                  55 |                   37.5 | Below benchmark (40th required) |
| HUACHIEW CHALERMPRAKIET UNIVERSITY                                                    | Foreign              |             8 |                27.5 |                   37.5 | Below benchmark (40th required) |
| TRINITY COLLEGE                                                                       | Foreign              |            40 |                  20 |                   37.5 | Below benchmark (40th required) |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                         | Public               |           243 |                  46 |                  37.45 | Below benchmark (40th required) |
| ILOILO DOCTORS COLLEGE                                                                | Private              |           163 |                  30 |                  37.42 | Below benchmark (40th required) |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                                | Public               |           132 |                  48 |                  37.12 | Below benchmark (40th required) |
| THE PHILIPPINE WOMEN'S UNIVERSITY SYSTEM - MANILA                                     | Private              |            27 |                53.5 |                  37.04 | Below benchmark (40th required) |
| LYCEUM OF THE PHILIPPINES UNIVERSITY                                                  | Private              |            19 |                  56 |                  36.84 | Below benchmark (40th required) |
| LOURDES COLLEGE                                                                       | Private              |            19 |                  49 |                  36.84 | Below benchmark (40th required) |
| DAVAO MEDICAL SCHOOL FOUNDATION                                                       | Private              |           646 |                  48 |                  36.84 | Below benchmark (40th required) |
| EMILIO AGUINALDO COLLEGE MANILA                                                       | Private              |           117 |                  26 |                  36.75 | Below benchmark (40th required) |
| OUR LADY OF FATIMA UNIVERSITY VALENZUELA CITY                                         | Private              |           248 |                  26 |                  36.69 | Below benchmark (40th required) |
| MANILA ADVENTIST MEDICAL CENTER AND COLLEGES                                          | Private              |            30 |                  51 |                  36.67 | Below benchmark (40th required) |
| HOLY NAME UNIVERSITY                                                                  | Private              |            90 |                  55 |                  36.67 | Below benchmark (40th required) |
| SOUTHEAST ASIAN COLLEGE                                                               | Private              |            60 |                  40 |                  36.67 | Below benchmark (40th required) |
| LA CONSOLACION COLLEGE                                                                | Private              |            41 |                  15 |                  36.59 | Below benchmark (40th required) |
| NOTRE DAME OF DADIANGAS UNIVERSITY                                                    | Private              |           104 |                48.5 |                  36.54 | Below benchmark (40th required) |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                            | Public               |            52 |                  59 |                  36.54 | Below benchmark (40th required) |
| LICEO DE CAGAYAN UNIVERSITY                                                           | Private              |           192 |                  33 |                  36.46 | Below benchmark (40th required) |
| MEDINA COLLEGE OZAMIS MISAMIS ORIENTAL                                                | Private              |            11 |                  15 |                  36.36 | Below benchmark (40th required) |
| CALAYAN EDUCATIONAL FOUNDATION                                                        | Private              |            11 |                  47 |                  36.36 | Below benchmark (40th required) |
| UNIVERSIDAD DE ZAMBOANGA                                                              | Private              |            80 |                  27 |                  36.25 | Below benchmark (40th required) |
| PERPETUAL HELP COLLEGE OF MANILA                                                      | Private              |           152 |                  31 |                  36.18 | Below benchmark (40th required) |
| ILIGAN MEDICAL CENTER ILIGAN CITY                                                     | Private              |            36 |                  20 |                  36.11 | Below benchmark (40th required) |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                         | Public               |            75 |                64.5 |                     36 | Below benchmark (40th required) |
| DIPOLOG MEDICAL CENTER COLLEGE FOUNDATION                                             | Private              |            14 |                  43 |                  35.71 | Below benchmark (40th required) |
| DAVAO DOCTORS COLLEGE                                                                 | Private              |           255 |                  32 |                  35.69 | Below benchmark (40th required) |
| UNIVERSITY OF THE EAST - MANILA                                                       | Private              |           157 |                  57 |                  35.67 | Below benchmark (40th required) |
| NOTRE DAME OF MARBEL UNIVERSITY                                                       | Private              |            59 |                42.5 |                  35.59 | Below benchmark (40th required) |
| ST. ANTHONY COLLEGE OF ROXAS CITY                                                     | Private              |            17 |                  47 |                  35.29 | Below benchmark (40th required) |
| PALAWAN STATE UNIVERSITY                                                              | Public               |            51 |                  41 |                  35.29 | Below benchmark (40th required) |
| GLOBAL CITY INNOVATIVE COLLEGE                                                        | Private              |            88 |                  40 |                  35.23 | Below benchmark (40th required) |
| CAPITOL MEDICAL CENTER COLLEGES                                                       | Private              |           108 |                  40 |                  35.19 | Below benchmark (40th required) |
| SOUTHWESTERN UNIVERSITY                                                               | Private              |           536 |                  43 |                  34.89 | Below benchmark (40th required) |
| UPH-DR. JOSE G. TAMAYO MEDICAL UNIV.                                                  | Private              |            23 |                  20 |                  34.78 | Below benchmark (40th required) |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES                                                 | Private              |            23 |                  20 |                  34.78 | Below benchmark (40th required) |
| MIRIAM COLLEGE FOUNDATION INC.                                                        | Private              |            52 |                  38 |                  34.62 | Below benchmark (40th required) |
| COLEGIO SAN AGUSTIN - BACOLOD                                                         | Private              |            82 |                  42 |                  34.15 | Below benchmark (40th required) |
| BAGUIO CENTRAL UNIVERSITY                                                             | Private              |            41 |                38.5 |                  34.15 | Below benchmark (40th required) |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                             | Public               |           182 |                43.5 |                  34.07 | Below benchmark (40th required) |
| Texila American University                                                            | Not Specified        |             9 |                  43 |                  33.33 | Below benchmark (40th required) |
| UNIVERSITY OF SAN FRANCISCO                                                           | Foreign              |             9 |                  75 |                  33.33 | Below benchmark (40th required) |
| CENTRO ESCOLAR UNIVERSITY-MALOLOS BULACAN                                             | Private              |             9 |                  36 |                  33.33 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP RIZAL - MOLINO                                           | Private              |            18 |                  31 |                  33.33 | Below benchmark (40th required) |
| COLLEGE OF THE IMMACULATE CONCEPTION                                                  | Private              |             6 |                47.5 |                  33.33 | Below benchmark (40th required) |
| CHRIST THE KING COLLEGE - CALBAYOG CITY                                               | Private              |             6 |                32.5 |                  33.33 | Below benchmark (40th required) |
| CONCORDIA COLLEGE                                                                     | Private              |             6 |                  47 |                  33.33 | Below benchmark (40th required) |
| PHILIPPINE REHABILITATION INSTITUTE FOUNDATION                                        | Private              |            21 |                  38 |                  33.33 | Below benchmark (40th required) |
| SAINT TONIS COLLEGE                                                                   | Private              |             9 |                  33 |                  33.33 | Below benchmark (40th required) |
| MAE FAH LUANG UNIVERSITY                                                              | Foreign              |             9 |                  64 |                  33.33 | Below benchmark (40th required) |
| ST. DOMINIC COLLEGE OF ARTS AND SCIENCES OF CAVITE                                    | Private              |            12 |                45.5 |                  33.33 | Below benchmark (40th required) |
| UNIVERSITY OF SAN JOSE RECOLETOS CEBU                                                 | Private              |            18 |                  31 |                  33.33 | Below benchmark (40th required) |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES CAGAYAN                                      | Private              |            21 |                  42 |                  33.33 | Below benchmark (40th required) |
| MINDANAO SANITARIUM & HOSPITAL COLLEGE ILIGAN CITY                                    | Private              |            51 |                  19 |                  33.33 | Below benchmark (40th required) |
| DE LOS SANTOS - STI COLLEGE                                                           | Private              |            18 |                35.5 |                  33.33 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA - SAN DIEGO                                                  | Foreign              |            18 |                81.5 |                  33.33 | Below benchmark (40th required) |
| SAINT MARY'S COLLEGE OF SAN JUAN                                                      | Private              |             6 |                  11 |                  33.33 | Below benchmark (40th required) |
| ST. ANTHONY COLLEGE OF ROXAS CITY CAPIZ                                               | Private              |             6 |                  19 |                  33.33 | Below benchmark (40th required) |
| UNIVERSITY OF THE PHILIPPINES - PAMPANGA                                              | Public               |            12 |                61.5 |                  33.33 | Below benchmark (40th required) |
| BATAAN PENINSULA STATE UNIVERSITY                                                     | Public               |             6 |                  18 |                  33.33 | Below benchmark (40th required) |
| ST. JOSEPH COLLEGE CAVITE CITY                                                        | Private              |            12 |                45.5 |                  33.33 | Below benchmark (40th required) |
| ST. MICHAEL'S COLLEGE                                                                 | Private              |            12 |                  32 |                  33.33 | Below benchmark (40th required) |
| UNIVERSITY OF THE IMMACULATE CONCEPTION COLLEGE DAVAO                                 | Private              |             6 |                   6 |                  33.33 | Below benchmark (40th required) |
| ASSUMPTION COLLEGE                                                                    | Private              |            18 |                55.5 |                  33.33 | Below benchmark (40th required) |
| NATIONAL UNIVERSITY - CEDCE                                                           | Private              |            15 |                  27 |                  33.33 | Below benchmark (40th required) |
| NARESUAN UNIVERSITY                                                                   | Foreign              |            15 |                  42 |                  33.33 | Below benchmark (40th required) |
| NUEVA ECIJA UNIVERSITY OF SCIENCE AND TECHNOLOGY - MAIN                               | Public               |             6 |                52.5 |                  33.33 | Below benchmark (40th required) |
| LEYTE NORMAL UNIVERSITY TACLOBAN CITY                                                 | Public               |             6 |                  16 |                  33.33 | Below benchmark (40th required) |
| LA SALLE UNIVERSITY                                                                   | Private              |            18 |                29.5 |                  33.33 | Below benchmark (40th required) |
| ST. PAUL UNIVERSITY - MANILA (ST. PAUL UNIVERITY SYSTEM)                              | Private              |           125 |                  48 |                   32.8 | Below benchmark (40th required) |
| NEW ERA UNIVERSITY QUEZON CITY                                                        | Private              |            37 |                  22 |                  32.43 | Below benchmark (40th required) |
| UNIVERSITY OF CAGAYAN VALLEY                                                          | Private              |            34 |                  52 |                  32.35 | Below benchmark (40th required) |
| UNIVERSITY OF LA SALETTE                                                              | Private              |            53 |                  36 |                  32.08 | Below benchmark (40th required) |
| BUTUAN DOCTORS COLLEGE                                                                | Private              |            25 |                  57 |                     32 | Below benchmark (40th required) |
| PINES CITY COLLEGES                                                                   | Private              |            75 |                  36 |                     32 | Below benchmark (40th required) |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES                                              | Private              |           104 |                  44 |                  31.73 | Below benchmark (40th required) |
| COLLEGE OF THE HOLY SPIRIT OF MANILA                                                  | Private              |            38 |                  38 |                  31.58 | Below benchmark (40th required) |
| BATANGAS STATE UNIVERSITY - MAIN                                                      | Public               |            16 |                33.5 |                  31.25 | Below benchmark (40th required) |
| VIRGEN MILAGROSA UNIVERSITY FOUNDATION AND VMU INSTITUTE OF MEDICAL FOUNDATION        | Private              |           222 |                45.5 |                  31.08 | Below benchmark (40th required) |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                             | Public               |            78 |                  58 |                  30.77 | Below benchmark (40th required) |
| FILAMER CHRISTIAN UNIVERSITY                                                          | Private              |            26 |                  38 |                  30.77 | Below benchmark (40th required) |
| EMILIO AGUINALDO COLLEGE                                                              | Private              |           231 |                  46 |                   30.3 | Below benchmark (40th required) |
| LYCEUM NORTHWESTERN UNIVERSITY                                                        | Private              |           129 |                  46 |                  30.23 | Below benchmark (40th required) |
| OUR LADY OF FATIMA UNIVERSITY - ANTIPOLO                                              | Private              |            53 |                  43 |                  30.19 | Below benchmark (40th required) |
| MIRIAM COLLEGE                                                                        | Private              |           123 |                48.5 |                  30.08 | Below benchmark (40th required) |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES-DAVAO CITY                                     | Public               |            30 |                  25 |                     30 | Below benchmark (40th required) |
| UNCIANO COLLEGES                                                                      | Private              |            10 |                52.5 |                     30 | Below benchmark (40th required) |
| MANUEL S. ENVERGA UNIVERSITY FOUNDATION - LUCENA                                      | Private              |            10 |                54.5 |                     30 | Below benchmark (40th required) |
| UNIVERSITY OF BATANGAS                                                                | Private              |            10 |                  41 |                     30 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-LAS PIÑAS                                   | Private              |            67 |                  15 |                  29.85 | Below benchmark (40th required) |
| PHILIPPINE WOMEN'S UNIVERSITY TAFT AVENUE MANILA                                      | Private              |            47 |                  46 |                  29.79 | Below benchmark (40th required) |
| NOT SPECIFIED/UNLISTED                                                                | Public               |           514 |                  37 |                  29.38 | Below benchmark (40th required) |
| SOUTHWESTERN UNIVERSITY-MATIAS H. AZNAR MEMORIAL COLLEGE OF MEDICINE - CEBU CITY CEBU | Private              |            92 |                  23 |                  29.35 | Below benchmark (40th required) |
| UNIVERSITY OF ST. LOUIS - TUGUEGARAO                                                  | Private              |            52 |                  47 |                  28.85 | Below benchmark (40th required) |
| MAPUA INSTITUTE OF TECHNOLOGY - MAKATI                                                | Private              |            14 |                  19 |                  28.57 | Below benchmark (40th required) |
| WESTERN VISAYAS COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                              | Public               |             7 |                  76 |                  28.57 | Below benchmark (40th required) |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                    | Public               |            14 |                32.5 |                  28.57 | Below benchmark (40th required) |
| BROKENSHIRE COLLEGE SOCSKSARGEN                                                       | Private              |             7 |                  57 |                  28.57 | Below benchmark (40th required) |
| STONY BROOK UNIVERSITY                                                                | Foreign              |             7 |                  59 |                  28.57 | Below benchmark (40th required) |
| HOLY TRINITY UNIVERSITY                                                               | Private              |            21 |                  38 |                  28.57 | Below benchmark (40th required) |
| UNIVERSITY OF IMMACULATE CONCEPTION-DAVAO CITY                                        | Private              |             7 |                  21 |                  28.57 | Below benchmark (40th required) |
| UNIVERSITY OF THE VISAYAS                                                             | Private              |            60 |                  25 |                  28.33 | Below benchmark (40th required) |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                         | Public               |            39 |                  32 |                  28.21 | Below benchmark (40th required) |
| CENTRAL MINDANAO UNIVERSITY BUKIDNON                                                  | Public               |            43 |                  30 |                  27.91 | Below benchmark (40th required) |
| RANGSIT UNIVERSITY                                                                    | Foreign              |            40 |                23.5 |                   27.5 | Below benchmark (40th required) |
| RUTGERS UNIVERSITY NEW JERSEY                                                         | Foreign              |            11 |                  72 |                  27.27 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA BERKELEY                                                     | Foreign              |            11 |                  81 |                  27.27 | Below benchmark (40th required) |
| BRENT HOSPITAL AND COLLEGES INC. ZAMBOANGA CITY                                       | Private              |            11 |                  10 |                  27.27 | Below benchmark (40th required) |
| MISAMIS UNIVERSITY                                                                    | Private              |            22 |                18.5 |                  27.27 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - GMA                                             | Private              |            11 |                  14 |                  27.27 | Below benchmark (40th required) |
| CENTRAL MINDANAO UNIVERSITY                                                           | Public               |           104 |                  39 |                  26.92 | Below benchmark (40th required) |
| UNIVERSITY OF EASTERN PHILIPPINES                                                     | Public               |            45 |                  38 |                  26.67 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA - DAVIS                                                      | Foreign              |            34 |                  82 |                  26.47 | Below benchmark (40th required) |
| SURIGAO EDUCATION CENTER                                                              | Private              |            19 |                  27 |                  26.32 | Below benchmark (40th required) |
| SAINT MARY'S COLLEGE OF TAGUM                                                         | Private              |            19 |                  54 |                  26.32 | Below benchmark (40th required) |
| CALIFORNIA STATE UNIVERSITY                                                           | Foreign              |            27 |                  57 |                  25.93 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA LOS ANGELES                                                  | Foreign              |            27 |                78.5 |                  25.93 | Below benchmark (40th required) |
| PINES CITY COLLEGES - BAGUIO CITY                                                     | Private              |            35 |                  19 |                  25.71 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA - IRVINE                                                     | Foreign              |            36 |                  77 |                     25 | Below benchmark (40th required) |
| DIVINE WORD COLLEGE OF LEGAZPI                                                        | Private              |             8 |                  11 |                     25 | Below benchmark (40th required) |
| UNIVERSITY OF THE ASSUMPTION PAMPANGA                                                 | Private              |             8 |                  36 |                     25 | Below benchmark (40th required) |
| NOTRE DAME OF TACURONG COLLEGE                                                        | Private              |             8 |                32.5 |                     25 | Below benchmark (40th required) |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                                 | Public               |             8 |                32.5 |                     25 | Below benchmark (40th required) |
| LYCEUM OF APARRI                                                                      | Private              |             8 |                  30 |                     25 | Below benchmark (40th required) |
| LA SALLE COLLEGE - ANTIPOLO                                                           | Private              |             8 |                18.5 |                     25 | Below benchmark (40th required) |
| MAPUA INSTITUTE OF TECHNOLOGY - MANILA                                                | Private              |            20 |                  33 |                     25 | Below benchmark (40th required) |
| KESTER GRANT COLLEGE - PHILIPPINES                                                    | Private              |            24 |                45.5 |                     25 | Below benchmark (40th required) |
| NUEVA ECIJA COLLEGES                                                                  | Private              |            16 |                27.5 |                     25 | Below benchmark (40th required) |
| SOUTHEAST ASIAN COLLEGE INC.-ESPANA MANILA                                            | Private              |            12 |                   8 |                     25 | Below benchmark (40th required) |
| ANGELES UNIVERSITY FOUNDATION ANGELES CITY                                            | Private              |           481 |                  33 |                  23.91 | Below benchmark (40th required) |
| CENTRAL COLLEGES OF THE PHILIPPINES                                                   | Private              |            13 |                  50 |                  23.08 | Below benchmark (40th required) |
| THAMMASAT UNIVERSITY                                                                  | Foreign              |            13 |                  32 |                  23.08 | Below benchmark (40th required) |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                           | Public               |            13 |                  53 |                  23.08 | Below benchmark (40th required) |
| UNIVERSITAS ADVENT INDONESIA                                                          | Foreign              |             9 |                  45 |                  22.22 | Below benchmark (40th required) |
| LIPA CITY COLLEGES                                                                    | Private              |             9 |                  50 |                  22.22 | Below benchmark (40th required) |
| ARELLANO UNIVERSITY - PASAY                                                           | Private              |             9 |                  18 |                  22.22 | Below benchmark (40th required) |
| MEDINA COLLEGE                                                                        | Private              |            27 |                  29 |                  22.22 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA SANTA BARBARA                                                | Foreign              |             9 |                  47 |                  22.22 | Below benchmark (40th required) |
| OTHERS (PLEASE SPECIFY)                                                               | Not Specified        |            23 |                  75 |                  21.74 | Below benchmark (40th required) |
| DOMINICAN COLLEGE                                                                     | Private              |            14 |                  22 |                  21.43 | Below benchmark (40th required) |
| UNIVERSITY OF THE ASSUMPTION                                                          | Private              |            19 |                  47 |                  21.05 | Below benchmark (40th required) |
| ST. FERDINAND COLLEGE - ILAGAN                                                        | Private              |             5 |                  23 |                     20 | Below benchmark (40th required) |
| SAINT LOUIS COLLEGE                                                                   | Private              |             5 |                  14 |                     20 | Below benchmark (40th required) |
| SIENA COLLEGE OF TAYTAY                                                               | Private              |             5 |                  35 |                     20 | Below benchmark (40th required) |
| KALAYAAN COLLEGE                                                                      | Private              |             5 |                  24 |                     20 | Below benchmark (40th required) |
| LIPA CITY COLLEGES BATANGAS                                                           | Private              |             5 |                  26 |                     20 | Below benchmark (40th required) |
| UNIVERSITY OF BRITISH COLUMBIA CANADA                                                 | Foreign              |             5 |                  96 |                     20 | Below benchmark (40th required) |
| COTABATO MEDICAL FOUNDATION COLLEGE                                                   | Private              |             5 |                  23 |                     20 | Below benchmark (40th required) |
| Sti - College Davao                                                                   | Not Specified        |             5 |                  15 |                     20 | Below benchmark (40th required) |
| GOOD SAMARITAN COLLEGES                                                               | Private              |             5 |                  41 |                     20 | Below benchmark (40th required) |
| MARIANO MARCOS STATE UNIVERSITY - COLLEGE OF EDUCATION - LAOAG CITY                   | Public               |            10 |                38.5 |                     20 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA RIVERSIDE CA USA                                             | Foreign              |            25 |                  84 |                     20 | Below benchmark (40th required) |
| DE OCAMPO MEMORIAL COLLEGE                                                            | Private              |             5 |                  18 |                     20 | Below benchmark (40th required) |
| PAMANTASAN NG LUNGSOD NG PASAY                                                        | Public               |             5 |                  23 |                     20 | Below benchmark (40th required) |
| ASIA-PACIFIC INTERNATIONAL UNIVERSITY                                                 | Private              |             5 |                  46 |                     20 | Below benchmark (40th required) |
| BRENT HOSPITAL AND COLLEGES                                                           | Private              |            30 |                33.5 |                     20 | Below benchmark (40th required) |
| 13206A                                                                                | Not Specified        |             5 |                  54 |                     20 | Below benchmark (40th required) |
| SAINT GABRIEL COLLEGE                                                                 | Private              |            10 |                16.5 |                     20 | Below benchmark (40th required) |
| MAHIDOL UNIVERSITY                                                                    | Foreign              |            26 |                  27 |                  19.23 | Below benchmark (40th required) |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                                 | Public               |            63 |                  15 |                  19.05 | Below benchmark (40th required) |
| SOUTHEAST ASIAN COLLEGE INC.-QUEZON CITY                                              | Private              |            16 |                20.5 |                  18.75 | Below benchmark (40th required) |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                     | Public               |            11 |                  75 |                  18.18 | Below benchmark (40th required) |
| DR. CARLOS LANTING COLLEGE - NOVALICHES QUEZON CITY                                   | Private              |            11 |                  24 |                  18.18 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA-RIVERSIDE                                                    | Foreign              |            11 |                71.5 |                  18.18 | Below benchmark (40th required) |
| NOTRE DAME OF JOLO COLLEGE - JOLO SULU                                                | Private              |            11 |                  11 |                  18.18 | Below benchmark (40th required) |
| OLIVAREZ COLLEGE SUCAT PARA$AQUE                                                      | Private              |            11 |                  27 |                  18.18 | Below benchmark (40th required) |
| UNCIANO COLLEGES AND GENERAL HOSPITAL                                                 | Private              |             6 |                  41 |                  16.67 | Below benchmark (40th required) |
| UNIVERSITY OF FLORIDA                                                                 | Foreign              |            12 |                  76 |                  16.67 | Below benchmark (40th required) |
| LYCEUM OF THE PHILIPPINES - LAGUNA                                                    | Private              |             6 |                67.5 |                  16.67 | Below benchmark (40th required) |
| WORLD CITI COLLEGES                                                                   | Private              |            24 |                  29 |                  16.67 | Below benchmark (40th required) |
| AMA COMPUTER COLLEGE                                                                  | Private              |            12 |                  19 |                  16.67 | Below benchmark (40th required) |
| ILOCOS SUR POLYTECHNIC STATE COLLEGE                                                  | Public               |             6 |                47.5 |                  16.67 | Below benchmark (40th required) |
| UNIVERSITY OF RIZAL SYSTEM - MORONG                                                   | Public               |             6 |                  16 |                  16.67 | Below benchmark (40th required) |
| CALIFORNIA STATE UNIVERSITY FRESNO                                                    | Foreign              |             6 |                  23 |                  16.67 | Below benchmark (40th required) |
| UNIVERSITY OF MARYLAND - MARYLAND U.S.A.                                              | Foreign              |             6 |                55.5 |                  16.67 | Below benchmark (40th required) |
| SAN DIEGO STATE UNIVERSITY - CALIFORNIA U.S.A.                                        | Foreign              |             6 |                  52 |                  16.67 | Below benchmark (40th required) |
| ST. MARY'S UNIVERSITY NUEVA VIZCAYA                                                   | Private              |             6 |                24.5 |                  16.67 | Below benchmark (40th required) |
| 13100A                                                                                | Not Specified        |            13 |                  52 |                  15.38 | Below benchmark (40th required) |
| BURAPHA UNIVERSITY                                                                    | Foreign              |             7 |                   9 |                  14.29 | Below benchmark (40th required) |
| RUNGSIT UNIVERSITY                                                                    | Foreign              |             7 |                   6 |                  14.29 | Below benchmark (40th required) |
| SAN SEBASTIAN COLLEGE                                                                 | Private              |             7 |                  22 |                  14.29 | Below benchmark (40th required) |
| NOTRE DAME OF JOLO COLLEGE                                                            | Private              |            30 |                36.5 |                  13.33 | Below benchmark (40th required) |
| VIRGEN MILAGROSA UNIV. FOUNDATION - SAN CARLOS CITY PANG.                             | Private              |            76 |                  27 |                  13.16 | Below benchmark (40th required) |
| MANILA THEOLOGICAL COLLEGE                                                            | Private              |            16 |                34.5 |                   12.5 | Below benchmark (40th required) |
| LAGUNA COLLEGE                                                                        | Private              |             8 |                38.5 |                   12.5 | Below benchmark (40th required) |
| UNIVERSITY OF VISAYAS CEBU                                                            | Private              |            69 |                  10 |                  11.59 | Below benchmark (40th required) |
| UNIVERSITY OF NEVADA LAS VEGAS                                                        | Foreign              |             9 |                  77 |                  11.11 | Below benchmark (40th required) |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                  | Public               |             9 |                  15 |                  11.11 | Below benchmark (40th required) |
| DOMINICAN COLLEGE BLUM SAN JUAN MM                                                    | Private              |             9 |                  25 |                  11.11 | Below benchmark (40th required) |
| UNIVERSITY OF CENTRAL FLORIDA                                                         | Foreign              |             9 |                  46 |                  11.11 | Below benchmark (40th required) |
| NORTHERN LUZON ADVENTIST COLLEGE                                                      | Private              |             9 |                  51 |                  11.11 | Below benchmark (40th required) |
| MINDANAO MEDICAL FOUNDATION COLLEGE DAVAO                                             | Private              |             9 |                  15 |                  11.11 | Below benchmark (40th required) |
| SULU STATE COLLEGE                                                                    | Public               |            10 |                  22 |                     10 | Below benchmark (40th required) |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                                            | Public               |            53 |                  11 |                   9.43 | Below benchmark (40th required) |
| VIRGEN MILAGROSA EDUCATIONAL INSTITUTE SAN CARLOS CITY                                | Private              |            11 |                  38 |                   9.09 | Below benchmark (40th required) |
| UNIVERSITY OF WASHINGTON                                                              | Foreign              |            12 |                  87 |                   8.33 | Below benchmark (40th required) |
| PALAWAN STATE UNIVERSITY PUERTO PRINCESA CITY                                         | Public               |            15 |                  15 |                   6.67 | Below benchmark (40th required) |
| RANGSIT UNIVERSITY THAILAND                                                           | Foreign              |            38 |                  11 |                   5.26 | Below benchmark (40th required) |
| CHIANG MAI UNIVERSITY                                                                 | Foreign              |            20 |                  27 |                      5 | Below benchmark (40th required) |
| MAHIDOL UNIVERSITY THAILAND                                                           | Foreign              |            28 |                35.5 |                   3.57 | Below benchmark (40th required) |
| SILPAKORN UNIVERSITY                                                                  | Foreign              |             5 |                  30 |                      0 | Below benchmark (40th required) |
| ADVENTIST INDONESIA UNIVERSITY INDONESIA                                              | Foreign              |             5 |                  17 |                      0 | Below benchmark (40th required) |
| Qiqihar Medical University                                                            | Not Specified        |             5 |                  11 |                      0 | Below benchmark (40th required) |
| RAMKHAMHAENG UNIV.                                                                    | Foreign              |             5 |                   2 |                      0 | Below benchmark (40th required) |
| KHON KAEN UNIVERSITY THAILAND                                                         | Foreign              |             5 |                  20 |                      0 | Below benchmark (40th required) |
| ST. LUKE'S SCHOOL OF MEDICINE INDIA                                                   | Private              |            10 |                35.5 |                      0 | Below benchmark (40th required) |
| SRINAKHARINWIROT UNIVERSITY                                                           | Foreign              |             9 |                  32 |                      0 | Below benchmark (40th required) |
| ST. ANDREW'S INTERNATIONAL ACADEMY INDIA                                              | Foreign              |             5 |                   9 |                      0 | Below benchmark (40th required) |
| MALASIQUI AGNO VALLEY COLLEGE - MALASIQUI PANGASINAN                                  | Private              |             7 |                   9 |                      0 | Below benchmark (40th required) |
| PRINCE OF SONGKLA UNIVERSITY                                                          | Foreign              |             5 |                  36 |                      0 | Below benchmark (40th required) |
| UNIVERSITY OF MINDANAO                                                                | Private              |            10 |                  48 |                      0 | Below benchmark (40th required) |
| DIVINE WORD COLLEGE OF LAOAG                                                          | Private              |           107 |                  18 |                      0 | Below benchmark (40th required) |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                  | Public               |             5 |                  51 |                      0 | Below benchmark (40th required) |
| THAMMASAT UNIV.                                                                       | Foreign              |             8 |                  23 |                      0 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA AT STA. CRUZ U.S.A.                                          | Foreign              |             9 |                  61 |                      0 | Below benchmark (40th required) |
| UNIVERSITY OF BRITISH COLUMBIA                                                        | Foreign              |             5 |                  24 |                      0 | Below benchmark (40th required) |
| SULTAN KUDARAT STATE UNIVERSITY - MAIN                                                | Public               |             5 |                   3 |                      0 | Below benchmark (40th required) |
| UNIVERSITY OF MICHIGAN                                                                | Foreign              |             5 |                  77 |                      0 | Below benchmark (40th required) |
| UNIVERSITY OF ILLINOIS CHICAGO                                                        | Foreign              |             8 |                83.5 |                      0 | Below benchmark (40th required) |
| PAMANTASAN NG LUNGSOD NG PASIG                                                        | Public               |             6 |                  76 |                      0 | Below benchmark (40th required) |
| UNIVERSITY OF SOUTH FLORIDA USA                                                       | Foreign              |             6 |                  53 |                      0 | Below benchmark (40th required) |
| CHULALONGKORN UNIVERSITY THAILAND                                                     | Foreign              |            17 |                  34 |                      0 | Below benchmark (40th required) |
| CHULALONGKORN UNIVERSITY                                                              | Foreign              |            12 |                  41 |                      0 | Below benchmark (40th required) |
| CALIFORNIA STATE UNIVERSITY - FULLERTON                                               | Foreign              |             6 |                75.5 |                      0 | Below benchmark (40th required) |

---
## Section C: Cut-off Scenarios — 30th Percentile (B4+) vs 40th Percentile (B5+)

Comparison of examinee counts and PLE outcomes under the 30th percentile (B4+) vs 40th percentile (B5+) cut-off thresholds, broken down by university type.

**Table C1. Cut-off scenario comparison by university type**

| University Type   | Cut-off               |   Admitted (best records) |   PLE passers (observable) |   PLE linkage rate (%) |   Median percentile |
|:------------------|:----------------------|--------------------------:|---------------------------:|-----------------------:|--------------------:|
| All               | 30th percentile (B4+) |                     92437 |                      27145 |                   54.7 |                  66 |
| All               | 40th percentile (B5+) |                     79848 |                      24815 |                  57.51 |                  71 |
| Public            | 30th percentile (B4+) |                     19999 |                       6505 |                  57.55 |                  71 |
| Public            | 40th percentile (B5+) |                     17752 |                       6178 |                  60.21 |                  76 |
| Private           | 30th percentile (B4+) |                     70245 |                      20130 |                   54.5 |                  64 |
| Private           | 40th percentile (B5+) |                     60184 |                      18157 |                  57.34 |                  70 |
| Foreign           | 30th percentile (B4+) |                      1284 |                        222 |                  27.54 |                  69 |
| Foreign           | 40th percentile (B5+) |                      1108 |                        208 |                  28.93 |                  74 |

---
## Section D: Foreign Student Enrollment at SUCs — 10-Slot Cap Analysis

The CHED amendment caps foreign student enrollment at 10 per incoming freshmen class at SUCs. This section shows foreign student counts per SUC per year based on CITIZENSHIP_FINAL from Pipeline 4.

**Summary metrics:**

| Metric | Value |
|--------|------:|
| SUC-Year combos exceeding 10-slot cap | 100 |
| Total foreign students at SUCs | 4,516 |

**Table D1. Top 20 SUCs by max foreign enrollment in a single year**

| UNDERGRAD_UNIVERSITY                                       |   max_foreign |   total_foreign |   years_over_cap |
|:-----------------------------------------------------------|--------------:|----------------:|-----------------:|
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                  |           281 |             770 |                6 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)              |           150 |             433 |                6 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                    |           120 |             371 |                7 |
| UNIVERSITY OF THE PHILIPPINES - MANILA                     |            82 |             360 |                7 |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                  |            78 |             225 |                5 |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY |            59 |             196 |                5 |
| NOT SPECIFIED/UNLISTED                                     |            57 |             159 |                5 |
| WEST VISAYAS STATE UNIVERSITY - MAIN                       |            52 |             197 |                5 |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                 |            47 |              47 |                1 |
| WESTERN MINDANAO STATE UNIVERSITY                          |            44 |             147 |                5 |
| BICOL UNIVERSITY - MAIN                                    |            44 |             118 |                4 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                    |            40 |             138 |                5 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                     |            40 |             119 |                4 |
| PAMANTASAN NG LUNGSOD NG MAYNILA                           |            38 |             135 |                5 |
| MINDANAO STATE UNIVERSITY - MARAWI                         |            33 |             135 |                5 |
| CAGAYAN STATE UNIVERSITY - ANDREWS                         |            25 |              57 |                2 |
| CENTRAL MINDANAO UNIVERSITY                                |            22 |              73 |                3 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                  |            21 |              62 |                2 |
| PALAWAN STATE UNIVERSITY                                   |            20 |              64 |                3 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                      |            17 |              32 |                2 |

**Table D2. Full foreign enrollment detail by SUC and year**
*(Sorted by year ascending, foreign count descending within year)*

| UNDERGRAD_UNIVERSITY                                                                |   Year |   foreign_count | over_cap   |
|:------------------------------------------------------------------------------------|-------:|----------------:|:-----------|
| NOT SPECIFIED/UNLISTED                                                              |   2006 |              11 | True       |
| NOT SPECIFIED/UNLISTED                                                              |   2007 |              21 | True       |
| VISAYAS UNIVERSITY                                                                  |   2007 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2007 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS ILOILO                                      |   2007 |               1 | False      |
| WESTERN MINDANAO STATE UNIVERSITY ZAMBOANGA CITY                                    |   2007 |               1 | False      |
| NOT SPECIFIED/UNLISTED                                                              |   2008 |              20 | True       |
| PANGASINAN STATE UNIVERSITY                                                         |   2008 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2008 |               1 | False      |
| NOT SPECIFIED/UNLISTED                                                              |   2009 |              57 | True       |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                                          |   2009 |              47 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                               |   2009 |              15 | True       |
| UNIVERSITY OF NORTHERN PHILIPPINES VIGAN ILOCOS SUR                                 |   2009 |               2 | False      |
| BULACAN STATE UNIVERSITY                                                            |   2009 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2009 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS CEBU                                   |   2009 |               1 | False      |
| NOT SPECIFIED/UNLISTED                                                              |   2010 |              50 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                               |   2010 |              17 | True       |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2010 |              13 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2010 |               6 | False      |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2010 |               3 | False      |
| NORTH LUZON PHILIPPINES STATE COLLEGE                                               |   2010 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2010 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2010 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - TACLOBAN                                            |   2010 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2010 |               1 | False      |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2011 |              11 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2011 |               2 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2011 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2012 |              14 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2012 |              11 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2012 |               7 | False      |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2012 |               6 | False      |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2012 |               5 | False      |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2012 |               4 | False      |
| BICOL UNIVERSITY - MAIN                                                             |   2012 |               3 | False      |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2012 |               3 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2012 |               3 | False      |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2012 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2012 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2012 |               3 | False      |
| CAVITE STATE UNIVERSITY - MAIN                                                      |   2012 |               2 | False      |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2012 |               2 | False      |
| PALAWAN STATE UNIVERSITY                                                            |   2012 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2012 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2012 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2012 |               2 | False      |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2012 |               2 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2012 |               1 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2012 |               1 | False      |
| CEBU STATE COLLEGE OF SCIENCE AND TECHNOLOGY-MANDAUE CITY - MANDAUE CITY CEBU       |   2012 |               1 | False      |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                |   2012 |               1 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2012 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG PASIG                                                      |   2012 |               1 | False      |
| SULU STATE COLLEGE                                                                  |   2012 |               1 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2012 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2012 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2013 |              23 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2013 |              17 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2013 |              10 | False      |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2013 |              10 | False      |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2013 |               8 | False      |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2013 |               8 | False      |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2013 |               8 | False      |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2013 |               7 | False      |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2013 |               7 | False      |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2013 |               6 | False      |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2013 |               4 | False      |
| PALAWAN STATE UNIVERSITY                                                            |   2013 |               3 | False      |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2013 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2013 |               3 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2013 |               2 | False      |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2013 |               2 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2013 |               2 | False      |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2013 |               2 | False      |
| SULU STATE COLLEGE                                                                  |   2013 |               2 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2013 |               1 | False      |
| BICOL UNIVERSITY - MAIN                                                             |   2013 |               1 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2013 |               1 | False      |
| MARINDUQUE STATE COLLEGE - MAIN                                                     |   2013 |               1 | False      |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2013 |               1 | False      |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  |   2013 |               1 | False      |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                 |   2013 |               1 | False      |
| PHILIPPINE STATE COLLEGE OF AERONAUTICS - MAIN                                      |   2013 |               1 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2013 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2013 |               1 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2013 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2013 |               1 | False      |
| VISAYAS STATE UNIVERSITY - MAIN                                                     |   2013 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2014 |              43 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2014 |              37 | True       |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2014 |              23 | True       |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2014 |              18 | True       |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2014 |              17 | True       |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2014 |              17 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2014 |              15 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2014 |              15 | True       |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2014 |              14 | True       |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2014 |              14 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2014 |              13 | True       |
| BICOL UNIVERSITY - MAIN                                                             |   2014 |              12 | True       |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2014 |               7 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2014 |               6 | False      |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2014 |               5 | False      |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2014 |               5 | False      |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2014 |               4 | False      |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2014 |               3 | False      |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2014 |               3 | False      |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2014 |               3 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2014 |               3 | False      |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  |   2014 |               2 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2014 |               2 | False      |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                |   2014 |               2 | False      |
| PHILIPPINE NORMAL UNIVERSITY - AGUSAN                                               |   2014 |               2 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2014 |               2 | False      |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                         |   2014 |               1 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2014 |               1 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2014 |               1 | False      |
| BICOL UNIVERSITY - DARAGA                                                           |   2014 |               1 | False      |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            |   2014 |               1 | False      |
| CATANDUANES STATE COLLEGE - MAIN                                                    |   2014 |               1 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2014 |               1 | False      |
| IFUGAO STATE UNIVERSITY - MAIN                                                      |   2014 |               1 | False      |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  |   2014 |               1 | False      |
| NAVAL STATE UNIVERSITY - MAIN                                                       |   2014 |               1 | False      |
| PAMPANGA AGRICULTURAL COLLEGE                                                       |   2014 |               1 | False      |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2014 |               1 | False      |
| SULU STATE COLLEGE                                                                  |   2014 |               1 | False      |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              |   2014 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2015 |             178 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2015 |              67 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2015 |              56 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2015 |              54 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2015 |              41 | True       |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2015 |              32 | True       |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2015 |              28 | True       |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2015 |              25 | True       |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2015 |              23 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2015 |              20 | True       |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2015 |              18 | True       |
| PALAWAN STATE UNIVERSITY                                                            |   2015 |              17 | True       |
| BICOL UNIVERSITY - MAIN                                                             |   2015 |              15 | True       |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2015 |              13 | True       |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2015 |              12 | True       |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2015 |              12 | True       |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  |   2015 |              10 | False      |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2015 |               9 | False      |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2015 |               9 | False      |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2015 |               7 | False      |
| CATANDUANES STATE COLLEGE - MAIN                                                    |   2015 |               5 | False      |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                              |   2015 |               5 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2015 |               4 | False      |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2015 |               4 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2015 |               4 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2015 |               3 | False      |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              |   2015 |               3 | False      |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                         |   2015 |               2 | False      |
| BICOL UNIVERSITY - TABACO                                                           |   2015 |               2 | False      |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            |   2015 |               2 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2015 |               2 | False      |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  |   2015 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2015 |               2 | False      |
| AKLAN STATE UNIVERSITY - MAIN                                                       |   2015 |               1 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2015 |               1 | False      |
| BICOL UNIVERSITY - POLANGUI                                                         |   2015 |               1 | False      |
| BUKIDNON STATE UNIVERSITY                                                           |   2015 |               1 | False      |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG) - TUGUEGARAO CITY (CAPITAL) CAGAYAN   |   2015 |               1 | False      |
| CAMARINES NORTE STATE COLLEGE - MAIN                                                |   2015 |               1 | False      |
| CAVITE STATE UNIVERSITY - MAIN                                                      |   2015 |               1 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2015 |               1 | False      |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                |   2015 |               1 | False      |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                              |   2015 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                   |   2015 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG MUNTINLUPA                                                 |   2015 |               1 | False      |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                               |   2015 |               1 | False      |
| UNIVERSITY OF MAKATI                                                                |   2015 |               1 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2015 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2016 |             191 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2016 |             121 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2016 |              60 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2016 |              54 | True       |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2016 |              42 | True       |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2016 |              40 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2016 |              30 | True       |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2016 |              29 | True       |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2016 |              25 | True       |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2016 |              22 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2016 |              21 | True       |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2016 |              21 | True       |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2016 |              14 | True       |
| BICOL UNIVERSITY - MAIN                                                             |   2016 |              10 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2016 |              10 | False      |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2016 |              10 | False      |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2016 |               8 | False      |
| PALAWAN STATE UNIVERSITY                                                            |   2016 |               7 | False      |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  |   2016 |               6 | False      |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2016 |               5 | False      |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2016 |               5 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2016 |               4 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2016 |               4 | False      |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                              |   2016 |               4 | False      |
| SULU STATE COLLEGE                                                                  |   2016 |               3 | False      |
| UNIVERSITY OF MAKATI                                                                |   2016 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                  |   2016 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2016 |               3 | False      |
| BICOL UNIVERSITY - DARAGA                                                           |   2016 |               2 | False      |
| CAVITE STATE UNIVERSITY - MAIN                                                      |   2016 |               2 | False      |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2016 |               2 | False      |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                 |   2016 |               2 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2016 |               2 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2016 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2016 |               2 | False      |
| AKLAN STATE UNIVERSITY - MAIN                                                       |   2016 |               1 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2016 |               1 | False      |
| BICOL UNIVERSITY - TABACO                                                           |   2016 |               1 | False      |
| BUKIDNON STATE UNIVERSITY                                                           |   2016 |               1 | False      |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            |   2016 |               1 | False      |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                |   2016 |               1 | False      |
| GORDON COLLEGE                                                                      |   2016 |               1 | False      |
| ISABELA STATE UNIVERSITY - MAIN                                                     |   2016 |               1 | False      |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - SAN PABLO CITY                                |   2016 |               1 | False      |
| LEYTE NORMAL UNIVERSITY                                                             |   2016 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                   |   2016 |               1 | False      |
| UM DIGOS COLLEGE                                                                    |   2016 |               1 | False      |
| UNIVERSIDAD DE MANILA                                                               |   2016 |               1 | False      |
| UNIVERSITY OF CALOOCAN CITY                                                         |   2016 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES-CANDON - CITY OF CANDON ILOCOS SUR               |   2016 |               1 | False      |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              |   2016 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA             |   2016 |               1 | False      |
| VISAYAS STATE UNIVERSITY - MAIN                                                     |   2016 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2017 |             281 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2017 |             150 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2017 |             120 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2017 |              79 | True       |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2017 |              78 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2017 |              59 | True       |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2017 |              52 | True       |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2017 |              44 | True       |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2017 |              40 | True       |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2017 |              40 | True       |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2017 |              38 | True       |
| BICOL UNIVERSITY - MAIN                                                             |   2017 |              33 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2017 |              33 | True       |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2017 |              21 | True       |
| PALAWAN STATE UNIVERSITY                                                            |   2017 |              20 | True       |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2017 |              19 | True       |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2017 |              16 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                  |   2017 |              15 | True       |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  |   2017 |              14 | True       |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2017 |              14 | True       |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2017 |              13 | True       |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2017 |              13 | True       |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2017 |              12 | True       |
| LEYTE NORMAL UNIVERSITY                                                             |   2017 |              11 | True       |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2017 |              10 | False      |
| CAVITE STATE UNIVERSITY - MAIN                                                      |   2017 |               8 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2017 |               8 | False      |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              |   2017 |               8 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2017 |               6 | False      |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2017 |               6 | False      |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                              |   2017 |               6 | False      |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            |   2017 |               5 | False      |
| SULTAN KUDARAT STATE UNIVERSITY - TACURONG                                          |   2017 |               5 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2017 |               5 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2017 |               4 | False      |
| BICOL UNIVERSITY - TABACO                                                           |   2017 |               3 | False      |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                              |   2017 |               3 | False      |
| JOSE RIZAL MEMORIAL STATE UNIVERSITY - MAIN                                         |   2017 |               3 | False      |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                 |   2017 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA             |   2017 |               3 | False      |
| CARAGA STATE UNIVERSITY - MAIN                                                      |   2017 |               2 | False      |
| GORDON COLLEGE                                                                      |   2017 |               2 | False      |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  |   2017 |               2 | False      |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                             |   2017 |               2 | False      |
| TECHNOLOGICAL UNIVERSITY OF THE PHILIPPINES - AYALA BLVD. MANILA                    |   2017 |               2 | False      |
| UNIVERSIDAD DE MANILA                                                               |   2017 |               2 | False      |
| UNIVERSITY OF MAKATI                                                                |   2017 |               2 | False      |
| VISAYAS STATE UNIVERSITY - MAIN                                                     |   2017 |               2 | False      |
| AKLAN STATE UNIVERSITY - MAIN                                                       |   2017 |               1 | False      |
| BACOLOD CITY COLLEGE                                                                |   2017 |               1 | False      |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                         |   2017 |               1 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2017 |               1 | False      |
| CATANDUANES STATE COLLEGE - MAIN                                                    |   2017 |               1 | False      |
| CAVITE STATE UNIVERSITY - CARMONA                                                   |   2017 |               1 | False      |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                |   2017 |               1 | False      |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                |   2017 |               1 | False      |
| EASTERN SAMAR STATE UNIVERSITY - MAIN                                               |   2017 |               1 | False      |
| MINDANAO STATE UNIVERSITY - BUUG COLLEGE                                            |   2017 |               1 | False      |
| MINDANAO STATE UNIVERSITY - NAAWAN                                                  |   2017 |               1 | False      |
| MISAMIS ORIENTAL STATE COLLEGE OF AGRICULTURE AND TECHNOLOGY                        |   2017 |               1 | False      |
| NUEVA VIZCAYA STATE UNIVERSITY - BAMBANG                                            |   2017 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG PASAY                                                      |   2017 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG PASIG                                                      |   2017 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG VALENZUELA                                                 |   2017 |               1 | False      |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                               |   2017 |               1 | False      |
| SAMAR STATE UNIVERSITY - MAIN                                                       |   2017 |               1 | False      |
| SULTAN KUDARAT STATE UNIVERSITY - MAIN                                              |   2017 |               1 | False      |
| SULU STATE COLLEGE                                                                  |   2017 |               1 | False      |
| UNIVERSITY OF RIZAL SYSTEM - MORONG                                                 |   2017 |               1 | False      |
| WESTERN VISAYAS COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                            |   2017 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2018 |              88 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2018 |              82 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2018 |              72 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2018 |              55 | True       |
| BICOL UNIVERSITY - MAIN                                                             |   2018 |              44 | True       |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2018 |              44 | True       |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2018 |              39 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2018 |              37 | True       |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2018 |              36 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2018 |              31 | True       |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2018 |              28 | True       |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2018 |              26 | True       |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  |   2018 |              25 | True       |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2018 |              23 | True       |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2018 |              22 | True       |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2018 |              18 | True       |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2018 |              16 | True       |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2018 |              15 | True       |
| PALAWAN STATE UNIVERSITY                                                            |   2018 |              15 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                  |   2018 |              13 | True       |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2018 |              11 | True       |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2018 |               9 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2018 |               8 | False      |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2018 |               7 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2018 |               7 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2018 |               6 | False      |
| CATANDUANES STATE COLLEGE - MAIN                                                    |   2018 |               5 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2018 |               4 | False      |
| LEYTE NORMAL UNIVERSITY                                                             |   2018 |               4 | False      |
| SAMAR STATE UNIVERSITY - MAIN                                                       |   2018 |               4 | False      |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                              |   2018 |               4 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2018 |               4 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2018 |               3 | False      |
| CAVITE STATE UNIVERSITY - MAIN                                                      |   2018 |               3 | False      |
| MINDANAO UNIVERSITY OF SCIENCE AND TECHNOLOGY                                       |   2018 |               3 | False      |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                             |   2018 |               3 | False      |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                 |   2018 |               3 | False      |
| UNIVERSIDAD DE MANILA                                                               |   2018 |               3 | False      |
| UNIVERSITY OF MAKATI                                                                |   2018 |               3 | False      |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              |   2018 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA             |   2018 |               3 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2018 |               2 | False      |
| BUKIDNON STATE UNIVERSITY                                                           |   2018 |               2 | False      |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            |   2018 |               2 | False      |
| CARAGA STATE UNIVERSITY - MAIN                                                      |   2018 |               2 | False      |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                              |   2018 |               2 | False      |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  |   2018 |               2 | False      |
| PANGASINAN STATE UNIVERSITY                                                         |   2018 |               2 | False      |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                               |   2018 |               2 | False      |
| SULTAN KUDARAT STATE UNIVERSITY - TACURONG                                          |   2018 |               2 | False      |
| SULU STATE COLLEGE                                                                  |   2018 |               2 | False      |
| VISAYAS STATE UNIVERSITY - MAIN                                                     |   2018 |               2 | False      |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                         |   2018 |               1 | False      |
| BICOL UNIVERSITY - DARAGA                                                           |   2018 |               1 | False      |
| CENTRAL BICOL STATE UNIVERSITY OF AGRICULTURE - MAIN                                |   2018 |               1 | False      |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                |   2018 |               1 | False      |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - SOUTH LA UNION                       |   2018 |               1 | False      |
| EULOGIO AMANG RODRIGUEZ INSTITUTE OF SCIENCE AND TECHNOLOGY - CAVITE                |   2018 |               1 | False      |
| GORDON COLLEGE                                                                      |   2018 |               1 | False      |
| IFUGAO STATE UNIVERSITY - MAIN                                                      |   2018 |               1 | False      |
| JOSE RIZAL MEMORIAL STATE UNIVERSITY - MAIN                                         |   2018 |               1 | False      |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - LAGUNA COLLEGE OF ARTS AND TRADES - STA. CRUZ |   2018 |               1 | False      |
| MINDANAO STATE UNIVERSITY - BUUG COLLEGE                                            |   2018 |               1 | False      |
| NAVAL STATE UNIVERSITY - MAIN                                                       |   2018 |               1 | False      |
| NORTHERN NEGROS STATE COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                      |   2018 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG MUNTINLUPA                                                 |   2018 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG PASAY                                                      |   2018 |               1 | False      |
| PHILIPPINE NORMAL UNIVERSITY - AGUSAN                                               |   2018 |               1 | False      |
| RAMON MAGSAYSAY TECHNOLOGICAL UNIVERSITY - RAMON MAGSAYSAY POLYTECHNIC COLLEGE      |   2018 |               1 | False      |
| TIWI COMMUNITY COLLEGE                                                              |   2018 |               1 | False      |

---
## Section E: Per-HEI Score Distribution

For every institution (with at least 5 best-record examinees): NMS_PER_num statistics, percentile bin distribution, and cut-off eligibility metrics.

**Total institutions with data: 2,568**

**Table E1. Per-HEI summary statistics**
*(Sorted by total examinees descending; minimum 5 examinees)*

| UNDERGRAD_UNIVERSITY                                                                  | UNDERGRAD_UNI_TYPE   |   Total Examinees |   Median %ile |   Mean %ile |   Q25 %ile |   Q75 %ile |   Median TRUE raw score |   B4+ % |   B5+ % |   Health Sci % |   PLE linkage rate % |
|:--------------------------------------------------------------------------------------|:---------------------|------------------:|--------------:|------------:|-----------:|-----------:|------------------------:|--------:|--------:|---------------:|---------------------:|
| UNIVERSITY OF SANTO TOMAS                                                             | Private              |             18038 |            58 |        54.9 |         32 |         80 |                     130 |    78.1 |    69.4 |           48.3 |                 47.7 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA                                             | Private              |              4528 |            45 |        45.9 |         18 |         72 |                     116 |    66.6 |    56.5 |           41.5 |                 42.3 |
| FAR EASTERN UNIVERSITY                                                                | Private              |              4309 |            45 |        46.6 |         21 |         71 |                     119 |    67.7 |    57.4 |           53.7 |                 45.4 |
| SAN PEDRO COLLEGE                                                                     | Private              |              3644 |            48 |        47.5 |         20 |         73 |                     118 |    67.8 |    59.1 |           47.8 |                 41.9 |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                                | Public               |              3629 |            81 |        68.1 |         46 |         95 |                     154 |    83.5 |    78.9 |           46.7 |                 61.7 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                               | Public               |              3238 |            80 |        66.9 |         43 |         95 |                     152 |    83.1 |    77.1 |           31.7 |                 56.2 |
| SAINT LOUIS UNIVERSITY                                                                | Private              |              3221 |            51 |        49.5 |         24 |         75 |                     121 |      72 |    61.3 |           53.1 |                 44.7 |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                             | Public               |              2458 |            44 |        44.7 |         18 |         70 |                     116 |    64.7 |    54.8 |           42.2 |                 34.1 |
| CEBU DOCTOR'S UNIVERSITY                                                              | Private              |              2406 |            47 |        47.3 |         21 |         73 |                     118 |    68.7 |    58.5 |             52 |                 43.6 |
| DE LA SALLE UNIVERSITY - MANILA                                                       | Private              |              2242 |            63 |        57.4 |         34 |         83 |                     133 |      79 |    72.1 |           34.3 |                 54.6 |
| OUR LADY OF FATIMA UNIVERSITY (FATIMA MEDICAL SCIENCE FOUNDATION) - VALENZUELA        | Private              |              2041 |            43 |        45.4 |         18 |         72 |                     115 |    65.1 |      55 |           46.4 |                   41 |
| CENTRO ESCOLAR UNIVERSITY - MANILA                                                    | Private              |              2022 |            46 |        47.3 |         20 |         74 |                     118 |    68.5 |    57.8 |           51.1 |                 39.6 |
| SOUTHWESTERN UNIVERSITY                                                               | Private              |              1841 |            45 |        45.8 |         18 |         72 |                     117 |    66.1 |    56.3 |           44.4 |                 34.9 |
| ATENEO DE MANILA UNIVERSITY - QUEZON CITY                                             | Private              |              1782 |            62 |        57.7 |         31 |         88 |                     131 |    77.1 |    68.7 |           47.1 |                 47.3 |
| VELEZ COLLEGE                                                                         | Private              |              1750 |            51 |        49.7 |         22 |         77 |                     121 |    69.9 |    60.3 |           52.3 |                   44 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS                                                   | Private              |              1724 |            49 |        48.3 |         20 |         75 |                     120 |    69.8 |    60.7 |           43.4 |                 43.2 |
| DAVAO MEDICAL SCHOOL FOUNDATION                                                       | Private              |              1665 |            45 |        46.5 |         19 |         73 |                     118 |    66.7 |      56 |           42.5 |                 36.8 |
| EMILIO AGUINALDO COLLEGE                                                              | Private              |              1577 |            44 |        45.2 |         18 |         70 |                     116 |    64.9 |    54.9 |           39.2 |                 30.3 |
| AMA COMPUTER COLLEGE - MAKATI                                                         | Private              |              1519 |            41 |        42.9 |         15 |         69 |                     112 |    61.2 |    52.6 |           36.7 |                  nan |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                         | Public               |              1386 |            45 |        45.5 |         15 |         73 |                     118 |    64.9 |    55.2 |           43.1 |                 37.4 |
| ANGELES UNIVERSITY FOUNDATION                                                         | Private              |              1337 |            48 |          47 |         21 |       71.5 |                     119 |    68.7 |    58.7 |           48.3 |                 41.6 |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                             | Public               |              1321 |            57 |        52.5 |         26 |         80 |                     125 |    72.6 |    65.1 |             43 |                 48.2 |
| SILLIMAN UNIVERSITY                                                                   | Private              |              1303 |            49 |          49 |         23 |         74 |                     121 |    70.4 |    61.5 |           55.6 |                 45.8 |
| AGO MEDICAL AND EDUCATIONAL CENTER - BICOL CHRISTIAN COLLEGE OF MEDICINE              | Private              |              1284 |            37 |        41.3 |         14 |         66 |                     110 |      60 |    48.8 |           37.2 |                 47.7 |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                  | Public               |              1245 |            54 |        52.5 |         27 |         80 |                     124 |    73.2 |    64.2 |           49.2 |                 42.4 |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                      | Public               |              1238 |            51 |          50 |         29 |         72 |                     124 |    75.1 |    65.1 |           35.7 |                 42.7 |
| XAVIER UNIVERSITY                                                                     | Private              |              1228 |            49 |        49.1 |         23 |         76 |                     121 |    70.5 |    60.6 |           50.7 |                 40.1 |
| BROKENSHIRE COLLEGE                                                                   | Private              |              1226 |            45 |        45.4 |         17 |       71.2 |                     116 |    66.4 |    56.6 |           41.5 |                 43.8 |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                            | Public               |              1185 |            48 |        48.8 |         23 |         76 |                     118 |    69.1 |    58.9 |           46.1 |                 40.2 |
| ATENEO DE ZAMBOANGA UNIVERSITY                                                        | Private              |              1172 |            44 |          45 |         18 |         70 |                     117 |    64.1 |    54.2 |           53.2 |                 46.6 |
| FEU - DR. NICANOR REYES MEDICAL FOUNDATION                                            | Private              |              1151 |            51 |        48.9 |         23 |         74 |                     120 |    70.7 |    61.7 |           52.6 |                   42 |
| LYCEUM NORTHWESTERN UNIVERSITY                                                        | Private              |              1048 |            42 |        43.9 |         15 |         70 |                     114 |    63.3 |    53.6 |           40.6 |                 30.2 |
| MINDANAO STATE UNIVERSITY - MARAWI                                                    | Public               |              1005 |            50 |        49.3 |         23 |         76 |                     120 |    69.7 |    61.9 |             50 |                 39.7 |
| UNIVERSITY OF SAN AGUSTIN                                                             | Private              |               995 |            46 |        47.2 |         19 |         74 |                     116 |    67.4 |    57.8 |           47.5 |                 39.7 |
| ATENEO DE DAVAO UNIVERSITY                                                            | Private              |               981 |            51 |        50.9 |         26 |         76 |                     125 |    71.8 |    62.6 |           59.8 |                 53.3 |
| DE LA SALLE HEALTH SCIENCES INSTITUTE                                                 | Private              |               952 |            48 |        48.5 |         23 |         75 |                     120 |    69.7 |    57.8 |             53 |                 38.6 |
| TRINITY UNIVERSITY OF ASIA                                                            | Private              |               897 |            54 |        51.6 |         27 |         76 |                     125 |    74.6 |    63.5 |           58.4 |                 44.6 |
| WESTERN MINDANAO STATE UNIVERSITY                                                     | Public               |               863 |            48 |        47.8 |         19 |       75.8 |                     118 |    69.3 |    59.2 |           52.8 |                 42.6 |
| MANILA CENTRAL UNIVERSITY                                                             | Private              |               837 |            41 |        43.1 |         17 |         68 |                     115 |    62.8 |    52.4 |           50.1 |                 43.6 |
| ATENEO DE MANILA UNIVERSITY                                                           | Private              |               751 |            89 |          86 |         81 |       94.2 |                     171 |    99.9 |    99.5 |             15 |                 62.1 |
| BICOL UNIVERSITY - MAIN                                                               | Public               |               740 |            52 |        50.6 |         23 |         78 |                     121 |    70.1 |    61.3 |           49.3 |                 38.8 |
| CENTRAL PHILIPPINE UNIVERSITY                                                         | Private              |               697 |          46.5 |        48.1 |         23 |         73 |                     119 |    68.7 |    59.4 |           56.2 |                 41.2 |
| VIRGEN MILAGROSA UNIVERSITY FOUNDATION AND VMU INSTITUTE OF MEDICAL FOUNDATION        | Private              |               697 |            45 |        44.9 |         18 |         70 |                     116 |    67.3 |      57 |           43.3 |                 31.1 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                                | Public               |               693 |            57 |        53.4 |       25.2 |         81 |                     126 |    74.5 |    66.6 |           41.3 |                 44.7 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                               | Public               |               674 |            50 |        49.3 |         20 |         77 |                     121 |    68.3 |    59.7 |           48.2 |                 42.9 |
| ADVENTIST UNIVERSITY OF THE PHILIPPINES                                               | Private              |               672 |            50 |        49.1 |         22 |         75 |                     122 |    69.1 |    61.2 |           53.4 |                 42.8 |
| SAINT PAUL UNIVERSITY PHILIPPINES                                                     | Private              |               662 |            46 |        46.3 |         18 |         72 |                     118 |    67.3 |    58.2 |           47.4 |                 47.9 |
| UNIVERSITY OF ST. LA SALLE                                                            | Private              |               629 |            54 |        52.6 |         28 |       77.5 |                     124 |    74.2 |    64.6 |             58 |                 44.5 |
| UNIVERSITY OF THE IMMACULATE CONCEPTION                                               | Private              |               601 |            43 |        44.7 |         16 |       70.8 |                     112 |    64.9 |    53.8 |           45.6 |                 42.9 |
| VELEZ COLLEGE CEBU                                                                    | Private              |               559 |            51 |        51.5 |         33 |         71 |                     127 |    79.1 |    64.6 |           69.4 |                 66.7 |
| UNIVERSITY OF THE EAST RAMON MAGSAYSAY MEMORIAL MEDICAL CENTER                        | Private              |               555 |            54 |        52.1 |       28.2 |         76 |                     125 |      75 |      65 |           63.8 |                 42.5 |
| UNIVERSITY OF SAN CARLOS                                                              | Private              |               551 |            49 |        48.9 |         23 |         76 |                     120 |    68.5 |    58.3 |           55.4 |                 40.4 |
| SAN BEDA COLLEGE                                                                      | Private              |               530 |            48 |        46.9 |         21 |         73 |                     117 |    65.6 |    57.1 |           55.7 |                 39.9 |
| NOT SPECIFIED/UNLISTED                                                                | Public               |               513 |            37 |          41 |         14 |         64 |                   117.5 |    57.5 |    47.8 |           40.4 |                 29.4 |
| SAN PEDRO COLLEGE DAVAO CITY                                                          | Private              |               512 |            37 |        39.5 |         19 |         58 |                     116 |    61.1 |    47.4 |           69.9 |                 51.4 |
| UNIVERSITY OF THE PHILIPPINES - LOS BANOS LAGUNA                                      | Public               |               487 |            80 |        76.3 |         66 |         90 |                     156 |    99.4 |    96.9 |            4.1 |                 62.4 |
| MANILA TYTANA COLLEGES                                                                | Private              |               485 |            45 |        47.1 |         22 |         72 |                     118 |    68.7 |    57.7 |             72 |                 40.5 |
| ANGELES UNIVERSITY FOUNDATION ANGELES CITY                                            | Private              |               481 |            33 |          38 |         19 |         54 |                     114 |    57.8 |    41.4 |           46.4 |                 23.9 |
| CENTRO ESCOLAR UNIVERSITY - MAKATI                                                    | Private              |               472 |            48 |        48.4 |         19 |         77 |                     118 |    69.8 |    59.1 |           39.6 |                 40.3 |
| DOÑA REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION                                   | Private              |               468 |            48 |          47 |         21 |         72 |                     118 |    68.3 |    58.2 |           52.4 |                 42.7 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS CAVITE                                            | Private              |               456 |            34 |        38.1 |         19 |         54 |                   116.5 |    58.6 |    43.4 |           16.2 |                   54 |
| DAVAO DOCTORS COLLEGE                                                                 | Private              |               444 |            35 |        40.2 |       14.5 |       63.5 |                     110 |    57.8 |    46.8 |           55.2 |                 35.7 |
| LICEO DE CAGAYAN UNIVERSITY                                                           | Private              |               428 |            38 |          42 |         15 |       66.5 |                     113 |    61.7 |    48.6 |           56.3 |                 36.5 |
| FAR EASTERN UNIVERSITY - NRMF (FAIRVIEW Q.C.)                                         | Private              |               427 |            34 |          36 |       18.5 |         52 |                     114 |    56.9 |    40.3 |           60.7 |                 61.2 |
| OUR LADY OF FATIMA UNIVERSITY - QUEZON CITY                                           | Private              |               423 |            43 |        46.4 |         19 |         72 |                     118 |    63.4 |    54.6 |             56 |                 42.2 |
| MINDANAO SANITARIUM AND HOSPITAL COLLEGE                                              | Private              |               393 |            44 |        45.6 |         19 |       70.5 |                     117 |    66.5 |    57.8 |           51.1 |                 39.2 |
| CENTRO ESCOLAR UNIVERSITY - MENDIOLA MANILA                                           | Private              |               382 |            28 |        32.1 |       12.2 |         47 |                     110 |      48 |    34.6 |           55.2 |                 46.1 |
| SAINT LOUIS UNIVERSITY - BAGUIO                                                       | Private              |               380 |            43 |        46.9 |         28 |         64 |                     122 |    73.2 |    57.9 |           47.1 |                 61.4 |
| DE LA SALLE - LIPA                                                                    | Private              |               365 |            44 |        46.9 |       22.2 |         74 |                     116 |    66.7 |    54.7 |           51.5 |                 40.4 |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                              | Public               |               363 |            64 |        58.3 |         35 |         85 |                     135 |    80.5 |    72.2 |           35.5 |                   51 |
| WEST VISAYAS STATE UNIVERSITY ILOILO                                                  | Public               |               360 |            59 |        54.9 |         36 |         74 |                     136 |    80.6 |    71.9 |           22.8 |                 58.1 |
| CEBU NORMAL UNIVERSITY                                                                | Public               |               356 |            63 |        57.6 |         37 |         81 |                     135 |    81.4 |    73.1 |           67.1 |                 59.5 |
| UNIVERSITY OF THE EAST - MANILA                                                       | Private              |               352 |            54 |          51 |         24 |       77.5 |                   124.5 |    70.8 |    61.2 |           42.6 |                 35.7 |
| XAVIER UNIVERSITY CAGAYAN DE ORO CITY                                                 | Private              |               349 |            52 |          51 |         32 |         69 |                     128 |    79.4 |    65.6 |           45.3 |                 57.8 |
| UNIVERSITY OF BAGUIO                                                                  | Private              |               346 |          51.5 |        49.8 |         23 |         77 |                     121 |    69.7 |    58.3 |           59.2 |                 46.2 |
| MINDANAO STATE UNIVERSITY MARAWI CITY                                                 | Public               |               344 |          37.5 |        41.7 |         23 |         63 |                     117 |    62.8 |      48 |           20.3 |                 49.1 |
| CENTRAL MINDANAO UNIVERSITY                                                           | Public               |               327 |            50 |        47.3 |         20 |       73.5 |                     118 |    68.5 |    58.7 |             45 |                 26.9 |
| UNIVERSIDAD DE ZAMBOANGA                                                              | Private              |               323 |            44 |        45.5 |         18 |         70 |                     117 |    65.2 |    56.3 |             43 |                 36.2 |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                                | Public               |               313 |          50.5 |        48.9 |         19 |       74.2 |                     122 |    67.4 |      59 |           49.8 |                 37.1 |
| UNIVERSITY OF THE CORDILLERAS                                                         | Private              |               310 |            44 |        43.6 |       15.5 |         70 |                     116 |      64 |    55.8 |           62.3 |                 41.6 |
| ST. PAUL UNIVERSITY ILOILO                                                            | Private              |               305 |            53 |        52.2 |         31 |         77 |                     124 |    76.6 |    64.7 |           66.2 |                 49.3 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                             | Public               |               304 |            51 |        48.7 |         21 |         75 |                     121 |    69.8 |    59.4 |           43.1 |                 30.8 |
| ILOILO DOCTORS COLLEGE                                                                | Private              |               303 |            39 |        43.7 |       18.2 |         70 |                     115 |    61.3 |    50.5 |           56.1 |                 37.4 |
| UNIVERSIDAD DE STA. ISABEL                                                            | Private              |               302 |            50 |        50.1 |         24 |         76 |                     120 |    70.9 |    61.8 |           62.9 |                 48.3 |
| RIVERSIDE COLLEGE                                                                     | Private              |               301 |            46 |        47.1 |         18 |         75 |                     117 |    67.1 |    58.3 |           47.8 |                 42.2 |
| MOUNTAIN VIEW COLLEGE                                                                 | Private              |               294 |            45 |        45.4 |         18 |         70 |                     118 |    66.2 |    56.2 |           49.7 |                 43.7 |
| NOTRE DAME UNIVERSITY                                                                 | Private              |               277 |          43.5 |        44.5 |         15 |         73 |                     116 |    63.9 |    53.9 |             52 |                 41.2 |
| UNIVERSITY OF NEGROS OCCIDENTAL-RECOLETOS                                             | Private              |               277 |          52.5 |        48.9 |       20.8 |         75 |                     123 |    69.5 |    60.7 |           50.5 |                 48.9 |
| MIRIAM COLLEGE                                                                        | Private              |               257 |            49 |        48.2 |         19 |         74 |                     120 |    70.3 |    61.4 |           44.4 |                 30.1 |
| UNIVERSITY OF THE VISAYAS                                                             | Private              |               254 |            36 |        39.2 |         11 |         62 |                     106 |    60.7 |    47.5 |           53.5 |                 28.3 |
| PALAWAN STATE UNIVERSITY                                                              | Public               |               253 |            48 |        46.5 |         21 |         70 |                     117 |    70.2 |    56.7 |           38.3 |                 35.3 |
| ATENEO DE NAGA UNIVERSITY                                                             | Private              |               253 |            45 |        45.6 |         20 |       70.2 |                     120 |    69.4 |    57.1 |           49.4 |                 49.3 |
| SAINT SCHOLASTICA'S COLLEGE TACLOBAN                                                  | Private              |               250 |            46 |        46.5 |         20 |       70.8 |                   118.5 |    66.8 |    57.3 |             56 |                 48.7 |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES                                              | Private              |               250 |            46 |        47.9 |       20.5 |         74 |                     118 |    71.2 |    58.8 |           53.2 |                 31.7 |
| LYCEUM OF THE PHILIPPINES UNIVERSITY - BATANGAS                                       | Private              |               249 |            48 |        44.8 |         16 |       69.5 |                     116 |      61 |    55.3 |           55.4 |                 47.3 |
| OUR LADY OF FATIMA UNIVERSITY VALENZUELA CITY                                         | Private              |               247 |            26 |          32 |         11 |         48 |                     109 |    45.7 |    34.4 |           51.8 |                 36.7 |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                       | Public               |               244 |            55 |        53.4 |         30 |         79 |                     126 |    76.5 |    68.5 |           40.2 |                   50 |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                    | Public               |               241 |            48 |        46.9 |         15 |         77 |                     118 |    65.1 |    58.2 |           43.2 |                 47.1 |
| LORMA COLLEGES                                                                        | Private              |               233 |            49 |        48.1 |         25 |         70 |                     120 |    71.3 |      60 |           49.8 |                 41.1 |
| SILLIMAN UNIVERSITY DUMAGUETE CITY                                                    | Private              |               227 |            53 |        54.2 |         35 |       74.5 |                     131 |    82.8 |    70.9 |           61.7 |                 65.2 |
| SAINT MARY'S UNIVERSITY                                                               | Private              |               219 |            47 |        47.1 |       19.5 |         74 |                   119.5 |    66.4 |    59.3 |           58.9 |                 41.9 |
| CAPITOL MEDICAL CENTER COLLEGES                                                       | Private              |               217 |            42 |        46.1 |         20 |         73 |                     116 |    63.9 |      56 |           60.4 |                 35.2 |
| ST. LOUIS UNIVERSITY BAGUIO CITY                                                      | Private              |               208 |            51 |        50.3 |         33 |       69.2 |                     130 |    78.8 |    66.3 |           42.3 |                 67.3 |
| MINDANAO STATE UNIVERSITY ILIGAN CITY                                                 | Public               |               203 |            53 |        53.5 |         37 |         73 |                     129 |    80.8 |    72.4 |           17.2 |                 56.1 |
| ARELLANO UNIVERSITY - MANILA                                                          | Private              |               203 |            49 |        49.2 |       24.5 |         76 |                     119 |    70.6 |    60.4 |           53.7 |                 41.1 |
| BULACAN STATE UNIVERSITY - MAIN                                                       | Public               |               201 |            51 |        48.9 |         20 |       76.8 |                     120 |    68.9 |    60.6 |           51.2 |                   45 |
| NOTRE DAME OF DADIANGAS UNIVERSITY                                                    | Private              |               198 |          45.5 |        46.5 |       18.2 |       72.5 |                     118 |    68.4 |      56 |             51 |                 36.5 |
| COLEGIO SAN AGUSTIN - BACOLOD                                                         | Private              |               198 |          45.5 |        47.4 |         23 |       70.8 |                     116 |    66.5 |    55.3 |           55.6 |                 34.1 |
| PERPETUAL HELP COLLEGE OF MANILA                                                      | Private              |               197 |            38 |          41 |         15 |         64 |                     114 |    56.9 |    48.2 |           68.5 |                 36.2 |
| UNIVERSITY OF PERPETUAL HELP - DR. JOSE G. TAMAYO MEDICAL UNIVERSITY                  | Private              |               196 |            51 |        49.5 |       24.5 |         72 |                     119 |    69.1 |    61.3 |           53.1 |                 50.9 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO CITY                                           | Public               |               195 |            69 |        66.8 |         54 |         82 |                     144 |    97.4 |    89.7 |            1.5 |                 55.1 |
| SOUTHWESTERN UNIVERSITY CEBU                                                          | Private              |               191 |            22 |        28.4 |          9 |         42 |                     104 |    41.4 |    29.3 |             67 |                   38 |
| MAKATI MEDICAL CENTER COLLEGE OF NURSING                                              | Private              |               191 |            47 |        46.4 |       21.2 |         69 |                     119 |    68.1 |    60.1 |           64.9 |                 41.1 |
| NOTRE DAME OF MARBEL UNIVERSITY                                                       | Private              |               186 |            45 |        47.3 |         20 |         74 |                   118.5 |    65.2 |    54.3 |           45.7 |                 35.6 |
| ADAMSON UNIVERSITY                                                                    | Private              |               184 |            45 |        45.5 |         18 |         69 |                     120 |    65.7 |    56.7 |           41.3 |                 42.1 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS ILOILO                                        | Public               |               182 |            75 |        71.9 |         59 |       88.8 |                   148.5 |    96.2 |    93.4 |           28.6 |                   71 |
| OUR LADY OF FATIMA UNIVERSITY - ANTIPOLO                                              | Private              |               175 |            43 |        44.6 |       20.2 |         67 |                     114 |    66.9 |    56.4 |           49.1 |                 30.2 |
| SAN BEDA COLLEGE MENDIOLA MANILA                                                      | Private              |               175 |            34 |          37 |       17.5 |       50.5 |                     115 |    61.1 |    37.1 |           45.7 |                 46.3 |
| NEW ERA UNIVERSITY                                                                    | Private              |               171 |            47 |        47.2 |         20 |         73 |                     119 |    68.3 |    54.5 |           42.7 |                 44.3 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                         | Public               |               171 |            54 |          54 |         30 |         80 |                     127 |    77.4 |    68.3 |           40.4 |                   36 |
| HOLY NAME UNIVERSITY                                                                  | Private              |               159 |            48 |        50.4 |         23 |         83 |                     120 |    66.9 |    60.5 |           50.3 |                 36.7 |
| ST. PAUL UNIVERSITY - MANILA (ST. PAUL UNIVERITY SYSTEM)                              | Private              |               159 |          51.5 |        51.5 |       28.2 |       76.8 |                     124 |    74.1 |    63.9 |           62.9 |                 32.8 |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                            | Public               |               158 |            49 |        50.2 |         22 |         79 |                     121 |    70.8 |      61 |           44.9 |                 36.5 |
| UNIVERSITY OF SAN CARLOS CEBU CITY                                                    | Private              |               158 |          40.5 |        45.3 |         25 |       68.2 |                   121.5 |    65.8 |    53.8 |             50 |                 57.2 |
| ST. SCHOLASTICA'S COLLEGE                                                             | Private              |               158 |          37.5 |        41.9 |       15.2 |         66 |                     113 |    59.2 |    47.8 |           32.9 |                 37.9 |
| PINES CITY COLLEGES                                                                   | Private              |               154 |            42 |          45 |         23 |         67 |                     115 |    67.3 |    52.7 |             61 |                   32 |
| UNIVERSITY OF LA SALETTE                                                              | Private              |               152 |            50 |          52 |       26.5 |         81 |                     121 |    72.3 |    62.2 |             52 |                 32.1 |
| SOUTHVILLE INTERNATIONAL SCHOOL AND COLLEGES                                          | Private              |               151 |          49.5 |        48.8 |         28 |         68 |                     122 |      72 |      60 |           67.5 |                   50 |
| UNIVERSITY OF ST. LOUIS - TUGUEGARAO                                                  | Private              |               150 |            54 |        50.8 |         20 |       80.2 |                     123 |    67.8 |      63 |           53.3 |                 28.8 |
| CEBU DOCTORS COLLEGE CEBU CITY                                                        | Private              |               148 |            28 |        34.7 |       16.8 |         49 |                   109.5 |    49.3 |    37.2 |           79.7 |                 52.3 |
| AQUINAS UNIVERSITY OF LEGAZPI                                                         | Private              |               146 |            44 |        45.7 |         26 |         65 |                     114 |      73 |    58.2 |           60.3 |                 48.8 |
| WESTERN MINDANAO STATE UNIVERSITY ZAMBOANGA CITY                                      | Public               |               145 |            28 |        30.6 |         13 |         47 |                     108 |    48.3 |    33.8 |           43.4 |                 42.8 |
| MINDANAO MEDICAL FOUNDATION COLLEGE                                                   | Private              |               143 |            53 |        49.9 |         24 |         73 |                     122 |      70 |    62.9 |             42 |                 43.3 |
| UNIVERSITY OF THE EAST (C.M. RECTO MANILA)                                            | Private              |               143 |            51 |        50.2 |       30.5 |       68.5 |                     132 |    76.9 |    64.3 |           13.3 |                 54.5 |
| BENGUET STATE UNIVERSITY - MAIN                                                       | Public               |               142 |          53.5 |        52.6 |         31 |       77.8 |                   124.5 |    76.4 |      65 |           52.1 |                   40 |
| UNIVERSITY OF CEBU - BANILAD                                                          | Private              |               140 |            46 |        45.8 |       19.2 |         70 |                     115 |    60.9 |    55.1 |             65 |                 43.9 |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                    | Public               |               140 |          42.5 |        45.9 |         16 |         73 |                   111.5 |      64 |      54 |           41.4 |                   50 |
| CENTRAL LUZON STATE UNIVERSITY                                                        | Public               |               140 |            46 |        47.4 |       17.5 |       76.5 |                     117 |    63.5 |    55.5 |           42.1 |                 51.9 |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                                | Public               |               138 |          48.5 |        49.7 |       19.8 |         77 |                     121 |    66.9 |    55.9 |           48.6 |                 46.8 |
| DE LA SALLE - HEALTH SCIENCES CAMPUS                                                  | Private              |               136 |            39 |        42.2 |         25 |         57 |                     121 |    67.6 |    49.3 |           77.2 |                 53.7 |
| MISAMIS UNIVERSITY - OZAMIS CITY                                                      | Private              |               132 |          44.5 |        45.9 |       18.2 |       70.8 |                     116 |    63.6 |      55 |             50 |                 39.1 |
| REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION TACLOBAN                               | Private              |               130 |            39 |        40.6 |         22 |         58 |                     116 |    62.3 |      50 |           80.8 |                 56.9 |
| ST. PAUL UNIVERSITY - QUEZON CITY                                                     | Private              |               129 |            34 |        40.7 |       17.8 |       63.5 |                     113 |    58.3 |    45.7 |           58.1 |                 38.9 |
| UNIVERSITY OF SAN AGUSTIN - ILOILO CITY                                               | Private              |               124 |            39 |        42.8 |       20.5 |         63 |                   118.5 |    62.6 |    49.6 |           51.6 |                 52.4 |
| GENERAL SANTOS DOCTORS' MEDICAL SCHOOL FOUNDATION                                     | Private              |               122 |            49 |        47.7 |         21 |         75 |                     117 |    66.4 |    57.1 |           43.4 |                 42.9 |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                                | Public               |               121 |            48 |          48 |         26 |       74.5 |                     115 |    73.3 |    57.8 |           47.1 |                 42.4 |
| COLEGIO DE SAN JUAN DE LETRAN                                                         | Private              |               121 |            47 |        49.8 |         24 |       79.8 |                     117 |    67.8 |    59.1 |           47.9 |                 40.3 |
| UNIVERSITY OF PANGASINAN                                                              | Private              |               119 |            42 |        43.1 |       19.8 |       63.5 |                   116.5 |    65.2 |    55.7 |           69.7 |                 46.7 |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING AND LIBERAL ARTS                          | Private              |               119 |            49 |        51.1 |         24 |         79 |                     124 |    72.4 |    65.5 |           65.5 |                 39.5 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                         | Public               |               118 |            51 |        46.9 |         21 |         70 |                     117 |    70.2 |    61.4 |           37.3 |                 28.2 |
| EMILIO AGUINALDO COLLEGE MANILA                                                       | Private              |               117 |            26 |        32.4 |         15 |         49 |                     109 |    46.2 |    34.2 |           49.6 |                 36.8 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION                                               | Private              |               117 |            43 |        44.2 |         15 |         67 |                     113 |    67.8 |    55.7 |           53.8 |                 42.3 |
| DIVINE WORD COLLEGE OF LAOAG                                                          | Private              |               116 |            19 |        27.7 |        6.8 |         45 |                      97 |    40.7 |    31.9 |            3.4 |                    0 |
| WESLEYAN UNIVERSITY - PHILIPPINES (CABANATUAN)                                        | Private              |               109 |            37 |          45 |       20.8 |       69.2 |                     115 |    63.9 |    49.1 |             67 |                 45.1 |
| ST. PAUL UNIVERSITY - MANILA                                                          | Private              |               109 |            43 |        45.2 |         26 |         64 |                     122 |    72.5 |      55 |           52.3 |                 45.5 |
| CENTRAL LUZON DOCTORS' HOSPITAL EDUCATIONAL INSTITUTION                               | Private              |               108 |            51 |        49.8 |         25 |         72 |                     118 |    74.3 |    66.7 |           57.4 |                 47.1 |
| Mariano Marcos State University - College Of Fisheries - Currimao                     | Not Specified        |               108 |          46.5 |        48.1 |       30.8 |       64.2 |                   124.5 |    76.9 |      62 |             13 |                 64.5 |
| UNIVERSITY OF EASTERN PHILIPPINES                                                     | Public               |               107 |            38 |        41.3 |         12 |         69 |                     111 |    57.3 |    50.5 |           50.5 |                 26.7 |
| UNIVERSITY OF BAGUIO BAGUIO CITY                                                      | Private              |               106 |            23 |        29.8 |        9.2 |         46 |                   108.5 |    42.5 |    30.2 |           49.1 |                 41.5 |
| HOLY ANGEL UNIVERSITY                                                                 | Private              |               105 |            41 |        44.8 |         20 |         73 |                     116 |      66 |    55.3 |           58.1 |                 43.1 |
| CAPITOL UNIVERSITY                                                                    | Private              |               104 |            42 |        46.6 |       20.5 |         74 |                     118 |    65.7 |    52.9 |           56.7 |                 41.8 |
| CENTRAL PHILIPPINE UNIVERSITY ILOILO                                                  | Private              |               104 |            47 |        45.3 |       25.8 |       65.2 |                   125.5 |    68.3 |    60.6 |           54.8 |                 44.2 |
| GLOBAL CITY INNOVATIVE COLLEGE                                                        | Private              |               101 |            41 |        42.8 |         23 |         61 |                     117 |      69 |      53 |           69.3 |                 35.2 |
| FEU - EAST ASIA COLLEGE                                                               | Private              |               101 |            44 |        45.5 |         18 |         69 |                     119 |    63.4 |    53.5 |           77.2 |                 38.8 |
| UNIVERSITY OF ST. LA SALLE BACOLOD CITY                                               | Private              |                99 |            45 |          47 |       26.5 |       64.5 |                     123 |    71.7 |    57.6 |           44.4 |                 55.6 |
| ST. JUDE COLLEGE                                                                      | Private              |                95 |            44 |        44.9 |         17 |         74 |                     115 |    61.5 |    53.8 |           57.9 |                 43.3 |
| FATHER SATURNINO M. URIOS UNIVERSITY                                                  | Private              |                91 |          50.5 |        48.5 |       21.5 |         73 |                     123 |    73.9 |    63.6 |           59.3 |                   56 |
| UNIVERSITY OF SOUTHERN PHILIPPINES FOUNDATION                                         | Private              |                89 |            41 |        44.6 |         16 |         71 |                     112 |    58.4 |    50.6 |           48.3 |                 46.9 |
| SOUTHWESTERN UNIVERSITY-MATIAS H. AZNAR MEMORIAL COLLEGE OF MEDICINE - CEBU CITY CEBU | Private              |                89 |          24.5 |        34.6 |        6.8 |       60.5 |                     104 |    45.8 |      41 |           69.7 |                 29.3 |
| UERM MEMORIAL MEDICAL CENTER                                                          | Private              |                88 |          48.5 |        46.6 |       30.8 |       58.2 |                     125 |    79.5 |    61.4 |           64.8 |                 51.1 |
| MANILA DOCTORS COLLEGE - PASAY CITY                                                   | Private              |                87 |            43 |        42.1 |         26 |         56 |                     122 |    70.1 |    55.2 |           88.5 |                   46 |
| CENTRO ESCOLAR UNIVERSITY AT MALOLOS                                                  | Private              |                87 |            58 |        54.8 |         29 |         82 |                     127 |    74.7 |    70.1 |             46 |                 43.3 |
| ILIGAN MEDICAL CENTER COLLEGE                                                         | Private              |                86 |            40 |        40.8 |         12 |         64 |                   113.5 |      63 |    56.8 |           53.5 |                 39.6 |
| COLLEGE OF THE HOLY SPIRIT OF MANILA                                                  | Private              |                83 |            39 |        43.3 |       18.5 |       69.5 |                     116 |    65.9 |      50 |           51.8 |                 31.6 |
| HOLY INFANT COLLEGE                                                                   | Private              |                80 |          49.5 |          47 |       20.8 |       73.2 |                     119 |    64.6 |    59.5 |           52.5 |                 46.7 |
| EASTER COLLEGE                                                                        | Private              |                78 |          38.5 |        42.7 |         24 |       62.2 |                     116 |    68.4 |      50 |           66.7 |                 40.5 |
| REMEDIOS T. ROMUALDEZ MEM. SCH. - MMC                                                 | Private              |                78 |          53.5 |        49.3 |       26.2 |       68.8 |                   129.5 |    71.8 |    64.1 |           79.5 |                 43.6 |
| SOUTHEAST ASIAN COLLEGE                                                               | Private              |                78 |          39.5 |        40.2 |         12 |         67 |                   115.5 |    59.5 |    51.4 |           73.1 |                 36.7 |
| VIRGEN MILAGROSA UNIV. FOUNDATION - SAN CARLOS CITY PANG.                             | Private              |                76 |            27 |        29.8 |         11 |         41 |                     109 |    43.2 |    28.4 |           38.2 |                 13.2 |
| WORLD CITI COLLEGES QUEZON CITY                                                       | Private              |                76 |            46 |        50.7 |         27 |         82 |                     120 |    69.9 |    58.9 |           56.6 |                 40.5 |
| DR. CARLOS S. LANTING COLLEGE                                                         | Private              |                76 |            37 |          44 |       19.5 |       71.5 |                     115 |    65.8 |    47.9 |           57.9 |                 47.6 |
| THE PHILIPPINE WOMEN'S UNIVERSITY SYSTEM - MANILA                                     | Private              |                75 |            57 |        53.6 |       32.2 |         74 |                     127 |    79.5 |    65.8 |             56 |                   37 |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE                                                  | Private              |                74 |          53.5 |        52.6 |       22.5 |       83.2 |                     126 |    70.4 |    67.6 |           43.2 |                 53.8 |
| METROPOLITAN HOSPITAL COLLEGE OF NURSING                                              | Private              |                74 |          48.5 |        48.4 |         22 |       73.5 |                   117.5 |    68.5 |    56.2 |           58.1 |                   50 |
| BRENT HOSPITAL AND COLLEGES                                                           | Private              |                73 |            39 |        44.6 |       13.5 |         73 |                     113 |    58.3 |    48.6 |           52.1 |                   20 |
| CAVITE STATE UNIVERSITY - MAIN                                                        | Public               |                72 |            54 |        51.6 |       25.2 |         81 |                     120 |    72.2 |    59.7 |           45.8 |                 47.6 |
| LEYTE NORMAL UNIVERSITY                                                               | Public               |                71 |            39 |        43.3 |         21 |         66 |                     115 |    60.3 |      50 |           39.4 |                   50 |
| MANILA ADVENTIST MEDICAL CENTER AND COLLEGES                                          | Private              |                71 |          47.5 |        44.5 |       20.2 |         69 |                     116 |    67.1 |    54.3 |             62 |                 36.7 |
| ST. ALEXIUS COLLEGE                                                                   | Private              |                71 |            58 |        46.5 |       12.5 |         71 |                     124 |    69.6 |    60.9 |           45.1 |                 57.1 |
| UNIVERSITY OF VISAYAS CEBU                                                            | Private              |                69 |            10 |        19.2 |          2 |         32 |                      90 |    30.3 |    19.7 |           33.3 |                 11.6 |
| RANGSIT UNIVERSITY                                                                    | Foreign              |                69 |            36 |        44.2 |         12 |         74 |                     115 |    58.8 |    47.1 |           68.1 |                 27.5 |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-LAS PIÑAS                                   | Private              |                67 |            15 |        23.3 |        5.5 |         33 |                      94 |    30.3 |    19.7 |           44.8 |                 29.9 |
| UNIVERSITY OF NUEVA CACERES                                                           | Private              |                67 |            40 |        40.1 |         13 |         64 |                     116 |    59.4 |    51.6 |           61.2 |                 44.1 |
| NOTRE DAME OF JOLO COLLEGE                                                            | Private              |                65 |            40 |        43.5 |         16 |         69 |                     109 |      60 |    50.8 |           58.5 |                 13.3 |
| LYCEUM NORTHWESTERN DAGUPAN CITY                                                      | Private              |                64 |            19 |        26.3 |        6.8 |       44.8 |                    96.5 |    31.2 |    28.1 |           51.6 |                 56.2 |
| UNIVERSITY OF THE CORDILLERAS (BCF)                                                   | Private              |                63 |            33 |        37.3 |         25 |         50 |                     118 |    61.9 |      46 |           41.3 |                 50.8 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                                 | Public               |                63 |            15 |        23.6 |          6 |         38 |                      98 |    33.3 |    23.3 |           23.8 |                   19 |
| ASSUMPTION COLLEGE                                                                    | Private              |                62 |            46 |        47.7 |       25.8 |       68.5 |                     117 |    66.7 |    56.7 |           43.5 |                 33.3 |
| LA CONSOLACION COLLEGE - MANILA                                                       | Private              |                62 |          49.5 |        48.1 |       20.8 |       70.8 |                   118.5 |    69.4 |    59.7 |           77.4 |                   48 |
| DE LA SALLE - LIPA BATANGAS                                                           | Private              |                61 |            46 |        45.2 |         22 |         63 |                     126 |    68.9 |    60.7 |           55.7 |                 55.7 |
| UNIVERSITY OF THE EAST - RAMON MAGSAYSAY MEM. MEDICAL CENTER                          | Private              |                60 |            57 |        53.8 |       38.5 |       66.8 |                     132 |      90 |    73.3 |           96.7 |                   60 |
| MANILA DOCTORS COLLEGE U.N. AVENUE MANILA                                             | Private              |                59 |            45 |        40.9 |       22.5 |       54.5 |                     124 |    67.8 |    59.3 |           57.6 |                 40.7 |
| CATANDUANES STATE COLLEGE - MAIN                                                      | Public               |                59 |            45 |          48 |       23.5 |         78 |                     110 |    64.4 |    54.2 |           49.2 |                 66.7 |
| UNIVERSITY OF SAN JOSE - RECOLETOS                                                    | Private              |                58 |          41.5 |          47 |       15.5 |       80.5 |                   115.5 |    65.5 |    53.4 |           44.8 |                 55.6 |
| BUTUAN DOCTORS COLLEGE                                                                | Private              |                57 |            46 |        46.4 |         27 |         69 |                     115 |    70.2 |    61.4 |           57.9 |                   32 |
| SACRED HEART COLLEGE OF LUCENA                                                        | Private              |                57 |            48 |        44.4 |         18 |         64 |                     119 |    63.2 |    56.1 |           64.9 |                 55.6 |
| UNIVERSITY OF MAKATI                                                                  | Public               |                56 |            42 |        43.7 |         15 |       64.5 |                     113 |    67.9 |    51.8 |           53.6 |                 39.3 |
| NOTRE DAME UNIVERSITY COTABATO CITY                                                   | Private              |                56 |          25.5 |        35.4 |        8.5 |         63 |                     108 |    42.9 |    35.7 |           71.4 |                 37.5 |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                   | Public               |                56 |            55 |        51.4 |         28 |         78 |                   127.5 |    77.4 |    67.9 |           46.4 |                 45.2 |
| DIPOLOG MEDICAL CENTER COLLEGE FOUNDATION                                             | Private              |                55 |            43 |        42.8 |       16.2 |       65.2 |                     111 |    65.4 |    57.7 |           43.6 |                 35.7 |
| ST. PAUL UNIVERSITY DUMAGUETE                                                         | Private              |                55 |            44 |        44.5 |         16 |         71 |                     114 |    65.4 |    57.7 |             60 |                 42.9 |
| OUR LADY OF FATIMA UNIVERSITY - LAGRO QUEZON CITY                                     | Private              |                53 |            32 |        32.8 |         14 |         46 |                     113 |    54.7 |      34 |           62.3 |                 44.4 |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                                            | Public               |                53 |            11 |          24 |          5 |         37 |                      92 |    33.3 |    25.5 |              0 |                  9.4 |
| BAGUIO CENTRAL UNIVERSITY                                                             | Private              |                52 |          38.5 |        43.6 |         12 |         73 |                   119.5 |    61.2 |      51 |           59.6 |                 34.1 |
| MIRIAM COLLEGE FOUNDATION INC.                                                        | Private              |                52 |            38 |        38.4 |         15 |       58.5 |                   115.5 |    61.5 |    46.2 |              0 |                 34.6 |
| SAN LORENZO RUIZ COLLEGE OF ORMOC                                                     | Private              |                51 |            36 |        38.8 |         16 |       61.5 |                     107 |    63.3 |    46.9 |           47.1 |                   50 |
| NAGA COLLEGE FOUNDATION                                                               | Private              |                50 |            48 |        48.4 |       18.5 |       74.5 |                   126.5 |    68.9 |    64.4 |             58 |                   40 |
| MINDANAO SANITARIUM & HOSPITAL COLLEGE ILIGAN CITY                                    | Private              |                50 |            17 |        24.9 |          9 |         42 |                    97.5 |      36 |      28 |             80 |                 33.3 |
| SOUTH SEED - LPDH COLLEGE                                                             | Private              |                50 |            54 |        51.4 |       35.2 |       71.5 |                     125 |    79.6 |    63.3 |             44 |                    0 |
| CEBU DOCTOR'S UNIVERSITY COLLEGE OF MEDICINE - MANDAUE CITY CEBU                      | Private              |                49 |            48 |        51.3 |         26 |         83 |                     122 |    68.8 |    64.6 |           55.1 |                 44.6 |
| UNIVERSITY OF THE PHILIPPINES - TACLOBAN                                              | Public               |                49 |            62 |        60.4 |         46 |         81 |                     138 |    81.6 |    79.6 |            6.1 |                 69.4 |
| BICOL UNIVERSITY - TABACO                                                             | Public               |                48 |            45 |        45.3 |       23.5 |       68.5 |                     113 |    70.8 |    52.1 |             50 |                 51.9 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION INC.                                          | Private              |                48 |          24.5 |        33.2 |       12.8 |       47.8 |                   102.5 |    45.8 |    37.5 |           72.9 |                   49 |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                              | Public               |                48 |            69 |        57.7 |         34 |       85.5 |                     139 |    78.3 |    71.7 |             50 |                 46.2 |
| DE LA SALLE - COLLEGE OF SAINT BENILDE                                                | Private              |                47 |            57 |        53.3 |       33.5 |       76.8 |                     125 |    78.3 |      63 |           57.4 |                   50 |
| PILAR COLLEGE                                                                         | Private              |                47 |            42 |        47.1 |         26 |       71.5 |                     115 |    70.2 |    57.4 |           57.4 |                   40 |
| MOUNTAIN VIEW COLLEGE BUKIDNON                                                        | Private              |                46 |            42 |        40.7 |       16.8 |       62.2 |                   120.5 |    60.9 |    52.2 |           69.6 |                 52.2 |
| MAPUA INSTITUTE OF TECHNOLOGY - MANILA                                                | Private              |                46 |          37.5 |        45.7 |         20 |       72.8 |                   112.5 |    66.7 |    48.9 |           32.6 |                   25 |
| BICOL UNIVERSITY                                                                      | Public               |                46 |            28 |        38.7 |         16 |         59 |                   114.5 |    48.9 |    44.4 |           19.6 |                 41.3 |
| UNIVERSITY OF THE PHILIPPINES - CEBU COLLEGE                                          | Public               |                46 |            75 |        70.5 |       62.2 |       86.2 |                     149 |    97.8 |      87 |            2.2 |                 67.4 |
| PHILIPPINE WOMEN'S UNIVERSITY TAFT AVENUE MANILA                                      | Private              |                46 |          47.5 |        41.5 |       14.8 |       62.8 |                     127 |    62.2 |    57.8 |           67.4 |                 29.8 |
| LYCEUM OF THE PHILIPPINES - LAGUNA                                                    | Private              |                45 |            37 |        43.2 |         15 |         75 |                     111 |    59.1 |    47.7 |           31.1 |                 16.7 |
| MEDINA COLLEGE                                                                        | Private              |                45 |            39 |        42.4 |         14 |       68.2 |                     113 |    59.1 |    47.7 |           73.3 |                 22.2 |
| PHILIPPINE CHRISTIAN UNIVERSITY                                                       | Private              |                45 |            50 |        43.2 |         18 |         64 |                     118 |    66.7 |      60 |           48.9 |                 42.3 |
| NOTRE DAME OF DADIANGAS COLLEGE GEN. SANTOS                                           | Private              |                44 |          34.5 |        38.5 |         15 |         57 |                     115 |    59.1 |    47.7 |             25 |                 38.6 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - BINAN LAGUNA                                    | Private              |                44 |          30.5 |        35.2 |       16.8 |         54 |                   114.5 |    59.1 |    34.1 |           61.4 |                 47.7 |
| UNIVERSITY OF THE ASSUMPTION                                                          | Private              |                44 |          45.5 |        49.9 |         30 |       75.8 |                   122.5 |    80.5 |      61 |           47.7 |                 21.1 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - LAGUNA                                          | Private              |                44 |            45 |        50.1 |       22.8 |       84.2 |                     120 |    72.1 |    62.8 |           63.6 |                 42.1 |
| CENTRAL MINDANAO UNIVERSITY BUKIDNON                                                  | Public               |                43 |            30 |        31.5 |         10 |         47 |                     108 |    51.2 |    32.6 |           11.6 |                 27.9 |
| BROKENSHIRE COLLEGE DAVAO CITY                                                        | Private              |                43 |            28 |        32.7 |         11 |         44 |                     108 |    46.5 |    34.9 |             93 |                 46.5 |
| UNIVERSITY OF CALIFORNIA - DAVIS                                                      | Foreign              |                43 |            73 |        68.3 |       49.5 |         89 |                     148 |    95.3 |    81.4 |           27.9 |                 26.5 |
| UNIVERSITY OF CAGAYAN VALLEY                                                          | Private              |                43 |          58.5 |        56.4 |       30.5 |       86.8 |                     126 |    78.6 |    61.9 |           48.8 |                 32.4 |
| UNIVERSITY OF THE VISAYAS - MANDAUE                                                   | Private              |                42 |            40 |        45.2 |       12.2 |       72.2 |                     120 |    64.3 |    52.4 |           61.9 |                 44.4 |
| LA CONSOLACION COLLEGE                                                                | Private              |                41 |            15 |        20.6 |          8 |         27 |                      97 |    23.1 |    15.4 |           70.7 |                 36.6 |
| FILAMER CHRISTIAN UNIVERSITY                                                          | Private              |                41 |            33 |        41.1 |       17.8 |       66.5 |                     109 |    57.9 |    44.7 |           51.2 |                 30.8 |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                               | Public               |                40 |            30 |          35 |       11.8 |         51 |                     106 |    55.3 |    42.1 |             60 |                   75 |
| YAMAN LAHI FOUNDATION - EMILIO AGUINALDO COLLEGE                                      | Private              |                40 |          40.5 |        46.8 |         23 |       76.2 |                   108.5 |    65.8 |    55.3 |           47.5 |                  nan |
| UNIVERSITY OF CALIFORNIA - IRVINE                                                     | Foreign              |                40 |          73.5 |        69.2 |       65.5 |         86 |                   153.5 |    92.3 |    89.7 |             35 |                   25 |
| TRINITY COLLEGE                                                                       | Foreign              |                40 |            20 |          31 |       11.8 |       49.5 |                   100.5 |      40 |    37.5 |             15 |                 37.5 |
| UNIVERSIDAD DE STA. ISABEL NAGA CITY                                                  | Private              |                39 |            40 |        42.5 |         17 |       63.5 |                     122 |    68.4 |    52.6 |           53.8 |                 48.7 |
| LOURDES COLLEGE                                                                       | Private              |                39 |            49 |        48.1 |       31.5 |       66.5 |                     118 |    76.3 |    65.8 |           48.7 |                 36.8 |
| ST. JUDE COLLEGE MANILA                                                               | Private              |                39 |            26 |        30.8 |         12 |       40.5 |                     105 |    38.5 |    25.6 |           71.8 |                 46.2 |
| RANGSIT UNIVERSITY THAILAND                                                           | Foreign              |                38 |            11 |        23.4 |          3 |       35.5 |                      90 |    31.6 |    23.7 |           68.4 |                  5.3 |
| NEW ERA UNIVERSITY QUEZON CITY                                                        | Private              |                37 |            22 |        26.3 |          5 |         36 |                     104 |    35.1 |    24.3 |            2.7 |                 32.4 |
| UNIVERSITY OF BOHOL                                                                   | Private              |                37 |          40.5 |        44.4 |       19.8 |         73 |                     113 |    61.1 |      50 |           43.2 |                 45.5 |
| NUEVA ECIJA COLLEGES                                                                  | Private              |                37 |            34 |        41.9 |       13.5 |       79.2 |                     112 |    52.8 |    47.2 |           64.9 |                   25 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS CEBU                                     | Public               |                37 |            78 |        73.2 |         59 |         90 |                     154 |    97.3 |    94.6 |           45.9 |                 81.1 |
| VISAYAS STATE UNIVERSITY - MAIN                                                       | Public               |                36 |          42.5 |        46.1 |       27.8 |       68.2 |                     114 |    74.3 |    57.1 |           55.6 |                 71.4 |
| DAVAO MEDICAL SCHOOL FOUNDATION INC.                                                  | Private              |                36 |            42 |        37.9 |       16.2 |       53.8 |                   122.5 |    62.9 |    57.1 |           88.9 |                 44.4 |
| UNIVERSITY OF LUZON                                                                   | Private              |                36 |            21 |        31.9 |        8.8 |       54.8 |                      97 |    38.2 |    29.4 |           69.4 |                 38.9 |
| MAHIDOL UNIVERSITY                                                                    | Foreign              |                36 |            42 |        41.9 |       19.5 |       68.2 |                     112 |    54.3 |    51.4 |           52.8 |                 19.2 |
| ILIGAN MEDICAL CENTER ILIGAN CITY                                                     | Private              |                36 |            20 |        27.5 |       10.5 |       41.2 |                   101.5 |    36.1 |    27.8 |           69.4 |                 36.1 |
| NORTHWESTERN UNIVERSITY                                                               | Private              |                36 |          39.5 |          44 |         18 |         68 |                   110.5 |    63.9 |      50 |           38.9 |                 54.5 |
| MEDINA COLLEGE - PAGADIAN                                                             | Private              |                35 |            44 |        48.3 |       25.5 |       73.5 |                     117 |    65.7 |    54.3 |           34.3 |                   40 |
| CALAYAN EDUCATIONAL FOUNDATION                                                        | Private              |                35 |          49.5 |          48 |       26.8 |       69.2 |                     117 |    73.5 |    67.6 |           42.9 |                 36.4 |
| PINES CITY COLLEGES - BAGUIO CITY                                                     | Private              |                35 |            19 |        24.7 |          9 |       33.5 |                     102 |    28.6 |      20 |           48.6 |                 25.7 |
| BATANGAS STATE UNIVERSITY - MAIN                                                      | Public               |                35 |            39 |        43.1 |          6 |       74.5 |                     111 |    63.6 |    51.5 |           42.9 |                 31.2 |
| SAINT MARY'S COLLEGE OF TAGUM                                                         | Private              |                34 |          54.5 |        52.3 |       34.2 |       74.5 |                     128 |    76.5 |    70.6 |           67.6 |                 26.3 |
| ST. PAUL UNIVERSITY - TUGUEGARAO CAGAYAN                                              | Private              |                34 |          22.5 |        27.5 |        8.5 |         40 |                     102 |    38.2 |    29.4 |           32.4 |                 38.2 |
| ARELLANO UNIVERSITY                                                                   | Private              |                34 |            26 |        30.1 |         13 |         41 |                   105.5 |    45.5 |    30.3 |           76.5 |                 38.2 |
| MARIANO MARCOS STATE UNIVERSITY ILOCOS NORTE                                          | Public               |                33 |            34 |        44.3 |         23 |         70 |                     117 |    60.6 |    42.4 |           24.2 |                 60.6 |
| HOLY TRINITY UNIVERSITY                                                               | Private              |                33 |            38 |        44.8 |         22 |         71 |                     116 |    69.7 |    45.5 |           72.7 |                 28.6 |
| MINDANAO STATE UNIVERSITY GENERAL SANTOS CITY                                         | Public               |                33 |            38 |        44.2 |         27 |         65 |                     116 |    66.7 |    48.5 |              0 |                 54.5 |
| SAN BEDA COLLEGE - ALABANG                                                            | Private              |                33 |            34 |        42.2 |         22 |         63 |                     111 |    66.7 |    45.5 |           42.4 |                   25 |
| OUR LADY OF GUADALUPE COLLEGES                                                        | Private              |                33 |          36.5 |        45.7 |       23.2 |       71.8 |                     120 |    56.2 |    43.8 |           72.7 |                 38.5 |
| CAPITOL MEDICAL CENTER COLLEGE Q.C.                                                   | Private              |                32 |            27 |        29.8 |       14.2 |       42.2 |                   108.5 |    46.9 |    31.2 |           59.4 |                 43.8 |
| Remedios Trinidad Romualdez Medical Foundation                                        | Not Specified        |                31 |            34 |        43.4 |         25 |         66 |                     114 |      60 |      50 |           90.3 |                 41.9 |
| LYCEUM OF THE PHILIPPINES - ST. CABRINI COLLEGE OF ALLIED MEDICINE                    | Private              |                31 |            38 |        41.4 |         19 |       55.5 |                     112 |    64.5 |    48.4 |           51.6 |                 46.2 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA - CALAMBA                                   | Private              |                30 |            61 |        60.7 |         41 |         80 |                   130.5 |    89.7 |    75.9 |           53.3 |                   75 |
| LYCEUM OF THE PHILIPPINES UNIVERSITY                                                  | Private              |                30 |          54.5 |        52.7 |       28.2 |       83.2 |                     122 |      70 |      60 |           56.7 |                 36.8 |
| LYCEUM OF BATANGAS                                                                    | Private              |                30 |            23 |        28.4 |       10.2 |       38.8 |                     105 |    33.3 |    26.7 |             60 |                 43.3 |
| UNIVERSITY OF ST. LA SALLE - DASMARIÑAS CAVITE                                        | Private              |                30 |            33 |        37.8 |       21.2 |         53 |                   117.5 |    53.3 |      40 |            3.3 |                 56.7 |
| UNIVERSITY OF CALIFORNIA LOS ANGELES                                                  | Foreign              |                30 |            75 |        69.3 |         59 |         89 |                   149.5 |    86.2 |    86.2 |           23.3 |                 25.9 |
| UNIVERSITY OF CEBU (FORMERLY CEBU CENTRAL COLLEGES)                                   | Private              |                30 |          38.5 |        41.4 |       26.5 |       57.5 |                   118.5 |      70 |      50 |           86.7 |                 63.3 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES-DAVAO CITY                                     | Public               |                30 |            25 |        31.4 |       15.2 |         44 |                     103 |    43.3 |      30 |              0 |                   30 |
| ST. JOSEPH'S COLLEGE OF QUEZON CITY                                                   | Private              |                30 |            41 |        43.9 |         22 |         62 |                     114 |    65.5 |    51.7 |           73.3 |                   50 |
| WESLEYAN UNIVERSITY-PHILIPPINES CABANATUAN CITY                                       | Private              |                29 |            33 |        36.7 |         18 |         51 |                     112 |    55.2 |    41.4 |           62.1 |                 55.2 |
| LA SALLE UNIVERSITY                                                                   | Private              |                29 |            50 |        49.9 |         27 |         69 |                     122 |      69 |    58.6 |           48.3 |                 33.3 |
| ST. ANTHONY COLLEGE OF ROXAS CITY                                                     | Private              |                29 |            33 |        40.6 |         11 |         63 |                     105 |    57.1 |    42.9 |           65.5 |                 35.3 |
| CARAGA STATE UNIVERSITY - MAIN                                                        | Public               |                29 |            57 |        49.5 |       20.5 |         85 |                     125 |    59.3 |    51.9 |           37.9 |                   40 |
| UNIVERSIDAD DE MANILA                                                                 | Public               |                29 |          65.5 |        54.7 |         32 |         80 |                     128 |    78.6 |    67.9 |           34.5 |                 44.4 |
| UNIVERSITY OF LA SALETTE SANTIAGO CITY                                                | Private              |                28 |          30.5 |        36.9 |       14.2 |         49 |                     113 |      50 |    32.1 |           64.3 |                 53.6 |
| MAHIDOL UNIVERSITY THAILAND                                                           | Foreign              |                28 |          35.5 |          36 |       13.5 |         55 |                     114 |    57.1 |    46.4 |           57.1 |                  3.6 |
| UNIVERSITY OF ASIA AND THE PACIFIC                                                    | Private              |                28 |          40.5 |        43.5 |       18.5 |         69 |                   116.5 |    64.3 |      50 |           21.4 |                 47.1 |
| CHULALONGKORN UNIVERSITY                                                              | Foreign              |                28 |            56 |        53.3 |       28.2 |       81.8 |                   126.5 |    71.4 |    64.3 |           35.7 |                    0 |
| PHILIPPINE REHABILITATION INSTITUTE FOUNDATION                                        | Private              |                27 |            49 |        48.9 |         15 |         80 |                     118 |    59.3 |    55.6 |           44.4 |                 33.3 |
| RIVERSIDE COLLEGE BACOLOD CITY                                                        | Private              |                27 |            37 |        40.2 |         23 |         58 |                     116 |      63 |    48.1 |           51.9 |                 59.3 |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                           | Public               |                27 |          58.5 |        52.2 |         32 |         71 |                     127 |    83.3 |      75 |           55.6 |                 23.1 |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                    | Public               |                27 |            35 |          44 |         21 |       64.5 |                     112 |    59.3 |    40.7 |           55.6 |                 28.6 |
| SULU STATE COLLEGE                                                                    | Public               |                27 |            34 |        42.1 |          5 |         77 |                     110 |      64 |      48 |             37 |                   10 |
| CALIFORNIA STATE UNIVERSITY                                                           | Foreign              |                27 |            57 |          60 |         43 |       78.5 |                     140 |    92.6 |    74.1 |           33.3 |                 25.9 |
| SURIGAO EDUCATION CENTER                                                              | Private              |                27 |            27 |        37.9 |       10.5 |         61 |                     104 |    44.4 |    40.7 |           81.5 |                 26.3 |
| MAPUA INSTITUTE OF TECHNOLOGY                                                         | Private              |                26 |          53.5 |          47 |       22.5 |       67.2 |                     131 |    69.2 |    65.4 |           61.5 |                 42.3 |
| ST. DOMINIC COLLEGE OF ARTS AND SCIENCES OF CAVITE                                    | Private              |                26 |          48.5 |        46.6 |       28.2 |       66.5 |                     114 |    69.2 |    61.5 |           61.5 |                 33.3 |
| ST. SCHOLASTICA'S COLLEGE - TACLOBAN CITY                                             | Private              |                26 |            31 |        38.6 |         15 |       57.5 |                     112 |    53.8 |    42.3 |           84.6 |                   50 |
| CEBU INSTITUTE OF TECHNOLOGY - UNIVERSITY                                             | Private              |                26 |            48 |        44.3 |       23.2 |       54.8 |                   116.5 |    65.4 |    57.7 |           65.4 |                 53.3 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA               | Public               |                26 |          50.5 |        47.6 |         15 |       76.8 |                     119 |    69.2 |    57.7 |           46.2 |                    0 |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES                                                 | Private              |                26 |            47 |          43 |       12.2 |         69 |                   113.5 |    61.5 |    53.8 |           73.1 |                 34.8 |
| MANUEL S. ENVERGA UNIVERSITY FOUNDATION - LUCENA                                      | Private              |                26 |            58 |        52.3 |       25.2 |       81.5 |                   120.5 |    73.1 |    61.5 |           46.2 |                   30 |
| UNIVERSITY OF CALIFORNIA RIVERSIDE CA USA                                             | Foreign              |                25 |            84 |        76.1 |         67 |         92 |                     162 |      96 |      92 |             24 |                   20 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM                                                   | Private              |                25 |            51 |        46.2 |         13 |         81 |                     113 |      60 |      52 |             52 |                 42.9 |
| WEST NEGROS UNIVERSITY                                                                | Private              |                25 |            55 |        54.6 |         30 |       82.5 |                     130 |    73.9 |    60.9 |             68 |                 56.5 |
| UNIVERSITY OF THE IMMACULATE CONCEPCION DAVAO CITY                                    | Private              |                25 |            30 |        33.5 |         18 |         51 |                     111 |      52 |      36 |             72 |                 57.7 |
| UNION CHRISTIAN COLLEGE                                                               | Private              |                25 |            40 |        41.6 |         26 |         48 |                     118 |      68 |      52 |             84 |                 37.5 |
| WORLD CITI COLLEGES                                                                   | Private              |                24 |            29 |        36.6 |         14 |       61.5 |                     107 |    45.8 |    33.3 |             50 |                 16.7 |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                                | Public               |                24 |            54 |        54.3 |       21.8 |       83.2 |                   131.5 |    70.8 |    66.7 |           45.8 |                 66.7 |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                                 | Public               |                24 |          44.5 |        43.8 |       17.5 |       62.5 |                     118 |    77.3 |    59.1 |             50 |                   25 |
| LORMA COLLEGE SAN FERNANDO LA UNION                                                   | Private              |                24 |            20 |          26 |       10.5 |       37.2 |                   101.5 |    41.7 |    20.8 |             75 |                   50 |
| PLT COLLEGE                                                                           | Private              |                24 |          43.5 |        39.9 |         12 |       61.8 |                   111.5 |    58.3 |    54.2 |           54.2 |                 42.9 |
| UNIVERSITY OF SOUTHERN MINDANAO NORTH COTABATO                                        | Public               |                24 |          43.5 |        42.2 |       16.5 |         62 |                     122 |    58.3 |    54.2 |           16.7 |                   40 |
| UNIVERSITY OF MINDANAO                                                                | Private              |                24 |          55.5 |        54.8 |       37.5 |         75 |                     128 |    83.3 |    70.8 |           62.5 |                    0 |
| NATIONAL UNIVERSITY                                                                   | Private              |                24 |            55 |        51.3 |       34.8 |         68 |                     123 |    79.2 |    66.7 |           58.3 |                 41.7 |
| RIVERSIDE COLLEGE OF NURSING BACOLOD                                                  | Private              |                23 |            33 |        38.3 |       21.5 |         59 |                     115 |    60.9 |    43.5 |           17.4 |                 47.8 |
| TARLAC STATE UNIVERSITY                                                               | Public               |                23 |            40 |        43.7 |       15.5 |       67.5 |                     119 |    60.9 |    56.5 |           52.2 |                 46.2 |
| CHIANG MAI UNIVERSITY                                                                 | Foreign              |                23 |            21 |        31.2 |          7 |       51.5 |                   100.5 |    43.5 |    34.8 |           43.5 |                    5 |
| UNIVERSITY OF PERPETUAL HELP RIZAL - MOLINO                                           | Private              |                23 |            31 |        36.8 |         14 |         47 |                     108 |    56.5 |    43.5 |           73.9 |                 33.3 |
| OTHERS (PLEASE SPECIFY)                                                               | Not Specified        |                23 |            75 |        71.2 |         60 |         87 |                     151 |    91.3 |    91.3 |           26.1 |                 21.7 |
| AL KWARIZMI INTERNATIONAL COLLEGE FOUNDATION                                          | Foreign              |                23 |            39 |        41.3 |         19 |         55 |                     107 |    60.9 |    47.8 |           52.2 |                 33.3 |
| BENGUET STATE UNIVERSITY                                                              | Public               |                23 |            42 |        46.3 |         27 |         71 |                     122 |    73.9 |    65.2 |           60.9 |                 43.5 |
| UNIVERSITY OF CALIFORNIA - SAN DIEGO                                                  | Foreign              |                23 |            78 |        65.5 |       55.5 |       87.5 |                     148 |    86.4 |    81.8 |           30.4 |                 33.3 |
| UPH-DR. JOSE G. TAMAYO MEDICAL UNIV.                                                  | Private              |                23 |            20 |        30.9 |       15.5 |         38 |                     105 |    30.4 |    26.1 |           26.1 |                 34.8 |
| ASSUMPTION COLLEGE MAKATI                                                             | Private              |                22 |          49.5 |        44.4 |       33.5 |         57 |                   124.5 |    86.4 |    59.1 |            4.5 |                 45.5 |
| MISAMIS UNIVERSITY                                                                    | Private              |                22 |          18.5 |          26 |         13 |       35.2 |                     100 |    36.4 |    22.7 |           63.6 |                 27.3 |
| GOOD SAMARITAN COLLEGES                                                               | Private              |                22 |          49.5 |        50.8 |       37.2 |       72.5 |                   125.5 |    81.8 |    68.2 |           40.9 |                   20 |
| ST. MICHAEL'S COLLEGE                                                                 | Private              |                22 |            46 |        46.5 |       26.2 |       62.8 |                   120.5 |    68.2 |    54.5 |           63.6 |                 33.3 |
| KESTER GRANT COLLEGE - PHILIPPINES                                                    | Private              |                22 |          40.5 |        48.8 |       26.2 |       76.8 |                     114 |    63.6 |      50 |           77.3 |                   25 |
| COLEGIO DE SAN AGUSTIN BACOLOD                                                        | Private              |                22 |            29 |        32.5 |       13.5 |         47 |                   110.5 |      50 |    31.8 |           40.9 |                 45.5 |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING & LIBERAL ARTS                            | Private              |                22 |          48.5 |        48.2 |         34 |         62 |                     124 |    81.8 |    63.6 |           59.1 |                 59.1 |
| BICOL UNIVERSITY COLLEGE OF SCIENCE LEGAZPI CITY                                      | Public               |                22 |          17.5 |        31.7 |        8.2 |       53.5 |                   100.5 |    40.9 |    40.9 |              0 |                 59.1 |
| MANILA THEOLOGICAL COLLEGE                                                            | Private              |                21 |            31 |        35.6 |         13 |         50 |                      99 |      55 |      35 |           42.9 |                 12.5 |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES CAGAYAN                                      | Private              |                21 |            42 |        35.1 |         14 |         49 |                     121 |    57.1 |    52.4 |           52.4 |                 33.3 |
| HOLY NAME UNIVERSITY - TAGBILARAN CITY                                                | Private              |                21 |            41 |        43.7 |         32 |         56 |                     120 |      81 |    57.1 |           33.3 |                 57.1 |
| JOHN PAUL II COLLEGE OF DAVAO                                                         | Private              |                21 |            47 |          48 |         20 |         81 |                     119 |    61.9 |    52.4 |           66.7 |                 53.3 |
| DE LOS SANTOS - STI COLLEGE                                                           | Private              |                21 |            44 |        43.4 |         23 |         69 |                     115 |    66.7 |    52.4 |           71.4 |                 33.3 |
| DIVINE WORD COLLEGE OF LEGAZPI                                                        | Private              |                21 |            27 |        31.4 |          6 |         51 |                      95 |    47.6 |    42.9 |           33.3 |                   25 |
| 13207A                                                                                | Not Specified        |                21 |            34 |        46.1 |         19 |         84 |                     111 |    52.4 |    42.9 |             81 |                 54.5 |
| CENTRAL LUZON DOCTOR'S HOSPITAL TARLAC                                                | Private              |                21 |            41 |          42 |         28 |         66 |                     123 |    71.4 |    52.4 |           71.4 |                 47.6 |
| AQUINAS UNIVERSITY LEGASPI CITY                                                       | Private              |                21 |            33 |          35 |         16 |         52 |                     112 |      55 |      40 |           76.2 |                 57.1 |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES INC.                                            | Private              |                20 |            13 |        21.4 |        4.8 |       33.8 |                    93.5 |      30 |      25 |             55 |                   45 |
| COLEGIO DE DAGUPAN                                                                    | Private              |                20 |            53 |        52.5 |       31.8 |       80.5 |                     127 |      75 |      65 |             80 |                 46.2 |
| DE LA SALLE COLLEGE OF SAINT BENILDE - MANILA                                         | Private              |                20 |          57.5 |        58.6 |         41 |         81 |                     135 |      85 |      75 |             25 |                   50 |
| BALIUAG UNIVERSITY                                                                    | Private              |                20 |            43 |        46.2 |       29.8 |       66.5 |                     118 |    78.9 |    63.2 |             65 |                 54.5 |
| THAMMASAT UNIVERSITY                                                                  | Foreign              |                20 |            36 |        39.3 |       19.5 |       51.2 |                     111 |      65 |      50 |             40 |                 23.1 |
| OUR LADY OF MT. CARMEL INSTITUTE OF MEDICAL STUDIES                                   | Private              |                20 |          46.5 |        48.4 |       18.8 |       83.2 |                   118.5 |    73.7 |    52.6 |             35 |                    0 |
| AGO MEDICAL AND EDUCATIONAL CENTER LEGAZPI CITY                                       | Private              |                20 |          32.5 |        36.2 |         17 |       49.2 |                   116.5 |      50 |      40 |             60 |                   60 |
| UNIVERSITY OF CALIFORNIA-RIVERSIDE                                                    | Foreign              |                19 |            68 |        62.3 |       56.2 |       82.8 |                     140 |    77.8 |    77.8 |           57.9 |                 18.2 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - SOUTH LA UNION                         | Public               |                19 |            45 |        45.9 |       20.5 |         74 |                     117 |    57.9 |    52.6 |           63.2 |                 57.1 |
| OLIVAREZ COLLEGE                                                                      | Private              |                19 |            39 |        49.2 |         29 |         69 |                     115 |    73.7 |    47.4 |           63.2 |                 37.5 |
| WESTERN STATE UNIVERSITY OF COLORADO                                                  | Foreign              |                19 |            50 |        43.3 |         23 |         59 |                     124 |    68.4 |    57.9 |           84.2 |                 68.4 |
| UNIVERSITY OF PERPETUAL HELP COLLEGE OF LAS PINAS                                     | Private              |                19 |            39 |        36.1 |         14 |       54.5 |                     119 |    57.9 |    47.4 |           47.4 |                   45 |
| ARELLANO UNIVERSITY - PASIG                                                           | Private              |                18 |          45.5 |        43.6 |         22 |         60 |                   118.5 |    66.7 |    66.7 |           61.1 |                 53.3 |
| LYCEUM OF THE PHILIPPINES                                                             | Private              |                18 |          40.5 |        40.7 |         28 |       49.8 |                     123 |    72.2 |      50 |           72.2 |                 66.7 |
| PAMANTASAN NG LUNGSOD NG PASIG                                                        | Public               |                18 |            47 |        46.4 |       13.5 |         82 |                     119 |    61.1 |    55.6 |           44.4 |                    0 |
| MAPUA INSTITUTE OF TECHNOLOGY - MAKATI                                                | Private              |                18 |          24.5 |        32.7 |       15.5 |       43.8 |                     100 |    47.1 |    35.3 |           83.3 |                 28.6 |
| HOLY ANGEL UNIVERSITY ANGELES CITY                                                    | Private              |                18 |            40 |        45.8 |       24.8 |       60.8 |                   122.5 |    61.1 |      50 |           83.3 |                 44.4 |
| SAMAR STATE UNIVERSITY - MAIN                                                         | Public               |                18 |            46 |        49.1 |         34 |         65 |                     123 |    82.4 |    58.8 |           61.1 |                   50 |
| UNIVERSITY OF SAN JOSE RECOLETOS CEBU                                                 | Private              |                18 |            31 |        30.7 |        7.5 |       50.5 |                     109 |      50 |    38.9 |           33.3 |                 33.3 |
| COLEGIO DE SAN JUAN DE LETRAN CALAMBA                                                 | Private              |                18 |            20 |        26.1 |         13 |         30 |                   104.5 |    27.8 |    22.2 |           33.3 |                 44.4 |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                  | Public               |                18 |            64 |        48.3 |          8 |       80.2 |                     123 |    55.6 |    55.6 |           44.4 |                 11.1 |
| TAGUM DOCTORS COLLEGE                                                                 | Private              |                18 |            29 |        37.7 |         15 |         50 |                     110 |    47.1 |    35.3 |           38.9 |                 66.7 |
| COLLEGE OF THE HOLY SPIRIT OF TARLAC                                                  | Private              |                18 |          55.5 |        55.7 |       29.8 |       85.8 |                     129 |    76.5 |    76.5 |             50 |                 87.5 |
| CENTRAL LUZON STATE UNIVERSITY NUEVA ECIJA                                            | Public               |                18 |          34.5 |        32.4 |       13.8 |       42.2 |                     115 |    55.6 |    33.3 |              0 |                   50 |
| COLEGIO DE STA. LOURDES OF LEYTE FOUNDATION                                           | Private              |                18 |            37 |        40.8 |       14.2 |       74.8 |                   108.5 |    55.6 |      50 |           44.4 |                   50 |
| ANDRES BONIFACIO COLLEGE                                                              | Private              |                17 |          51.5 |        50.9 |       27.2 |       81.5 |                     117 |      75 |    56.2 |           70.6 |                   50 |
| ST. JOSEPH COLLEGE CAVITE CITY                                                        | Private              |                17 |            42 |        43.4 |         18 |         69 |                     118 |    73.3 |      60 |           82.4 |                 33.3 |
| CHULALONGKORN UNIVERSITY THAILAND                                                     | Foreign              |                17 |            34 |        35.9 |         20 |         48 |                     115 |    58.8 |    41.2 |           52.9 |                    0 |
| UNIVERSITY OF TORONTO                                                                 | Foreign              |                17 |            77 |        74.8 |         65 |         91 |                     151 |    94.1 |    88.2 |           29.4 |                 43.8 |
| OUR LADY OF FATIMA UNIVERSITY - PAMPANGA                                              | Private              |                17 |            29 |        37.7 |         20 |         60 |                     102 |      50 |    43.8 |           41.2 |                  nan |
| LA CONSOLACION UNIVERSITY PHILIPPINES                                                 | Private              |                17 |            54 |        45.5 |         15 |         66 |                     118 |    64.7 |    58.8 |           58.8 |                   50 |
| UNIVERSITY OF PANGASINAN DAGUPAN CITY                                                 | Private              |                17 |            30 |        33.8 |         22 |         42 |                     109 |    58.8 |    29.4 |           88.2 |                 47.1 |
| MAE FAH LUANG UNIVERSITY                                                              | Foreign              |                17 |            19 |          44 |          7 |         83 |                     105 |    47.1 |    47.1 |           41.2 |                 33.3 |
| BICOL UNIVERSITY COLLEGE OF NURSING LEGAZPI CITY                                      | Public               |                17 |            66 |        60.7 |         42 |         83 |                     141 |    88.2 |    76.5 |           76.5 |                 58.8 |
| BUKIDNON STATE UNIVERSITY                                                             | Public               |                17 |            20 |        39.3 |         12 |         70 |                     105 |      50 |      50 |           58.8 |                   50 |
| BULACAN STATE UNIVERSITY                                                              | Public               |                17 |            45 |        42.2 |         15 |         66 |                     126 |    64.7 |    52.9 |           11.8 |                 47.1 |
| UNIVERSITY OF CALIFORNIA BERKELEY                                                     | Foreign              |                17 |            81 |        65.1 |         26 |         96 |                     158 |      80 |      80 |           35.3 |                 27.3 |
| CANOSSA COLLEGE                                                                       | Private              |                16 |            61 |        63.5 |       53.2 |       82.5 |                     125 |    93.8 |    87.5 |           62.5 |                 61.5 |
| IMMACULATE CONCEPTION COLLEGE - ALBAY                                                 | Private              |                16 |            59 |        50.7 |         34 |         68 |                   128.5 |    73.3 |    73.3 |           37.5 |                   50 |
| DE OCAMPO MEMORIAL COLLEGE                                                            | Private              |                16 |            38 |        39.9 |         19 |         54 |                   111.5 |    68.8 |    37.5 |           68.8 |                   20 |
| NORTHERN LUZON ADVENTIST COLLEGE                                                      | Private              |                16 |          51.5 |        48.8 |       29.2 |         70 |                   119.5 |      75 |    62.5 |             50 |                 11.1 |
| UNIVERSITY OF EASTERN PHILIPPINES - SAMAR                                             | Public               |                16 |            14 |        17.1 |          4 |       20.8 |                    92.5 |    12.5 |     6.2 |           62.5 |                 56.2 |
| MANILA ADVENTIST MEDICAL CENTER - PASAY CITY                                          | Private              |                16 |            40 |        49.4 |       32.8 |       74.5 |                   120.5 |    87.5 |    62.5 |           93.8 |                   50 |
| UNIVERSITY OF WASHINGTON                                                              | Foreign              |                16 |            78 |        67.6 |       52.8 |         93 |                   152.5 |    87.5 |    87.5 |           12.5 |                  8.3 |
| ST. PAUL COLLEGE ILOILO                                                               | Private              |                16 |            50 |        56.4 |       44.5 |       77.2 |                   128.5 |    87.5 |    81.2 |           87.5 |                 43.8 |
| SOUTHEAST ASIAN COLLEGE INC.-QUEZON CITY                                              | Private              |                16 |          20.5 |        24.1 |       11.8 |       33.5 |                     100 |    37.5 |      25 |           62.5 |                 18.8 |
| SAINT PAUL COLLEGE OF ILOCOS SUR                                                      | Private              |                16 |            54 |        53.1 |         33 |       76.5 |                   128.5 |      75 |    68.8 |           62.5 |                   25 |
| NATIONAL UNIVERSITY - CEDCE                                                           | Private              |                16 |            44 |        40.1 |       14.5 |       54.8 |                   122.5 |    56.2 |    56.2 |           56.2 |                 33.3 |
| PALAWAN STATE UNIVERSITY PUERTO PRINCESA CITY                                         | Public               |                15 |            15 |        24.2 |          9 |         33 |                      95 |    33.3 |      20 |            6.7 |                  6.7 |
| NORTH VALLEY COLLEGE FOUNDATION                                                       | Private              |                15 |            40 |        44.3 |       27.5 |       48.5 |                     112 |    66.7 |    53.3 |           46.7 |                 37.5 |
| MARY CHILES COLLEGE                                                                   | Private              |                15 |            32 |        38.9 |       16.5 |       67.5 |                     100 |    53.3 |      40 |           46.7 |                   50 |
| LYCEUM OF ILIGAN FOUNDATION                                                           | Private              |                15 |            76 |        63.3 |       40.5 |         90 |                     136 |      80 |    73.3 |           53.3 |                 45.5 |
| ARELLANO UNIVERSITY - PASAY                                                           | Private              |                15 |            35 |        42.1 |       16.5 |       72.5 |                     109 |    57.1 |    42.9 |           46.7 |                 22.2 |
| LYCEUM OF THE PHILIPPINES - CAVITE                                                    | Private              |                15 |            53 |        40.7 |       13.5 |         61 |                     120 |      60 |    53.3 |           33.3 |                    0 |
| NARESUAN UNIVERSITY                                                                   | Foreign              |                15 |          55.5 |        54.3 |       29.2 |       83.8 |                     130 |    71.4 |    64.3 |             80 |                 33.3 |
| CARITAS FAMILY HOSPITAL AND COLLEGES                                                  | Private              |                15 |            63 |        55.3 |       39.5 |         78 |                     129 |      80 |    73.3 |           53.3 |                 37.5 |
| UNIVERSITY OF BATANGAS                                                                | Private              |                15 |            34 |        34.3 |       22.5 |         48 |                     109 |      60 |    46.7 |           73.3 |                   30 |
| DR. P. OCAMPO COLLEGES                                                                | Private              |                15 |            36 |        43.7 |       13.5 |       71.5 |                     107 |      60 |    46.7 |             40 |                   50 |
| GORDON COLLEGE                                                                        | Public               |                15 |            46 |        48.9 |         25 |       79.5 |                     116 |    71.4 |    57.1 |           46.7 |                   50 |
| LIPA CITY COLLEGES                                                                    | Private              |                15 |            79 |        61.1 |         31 |         91 |                     137 |    86.7 |    66.7 |           33.3 |                 22.2 |
| ILOCOS SUR COMMUNITY COLLEGE - BANTAY ILOCOS SUR                                      | Public               |                15 |            21 |        29.8 |       13.5 |       35.5 |                     103 |    46.7 |      20 |           66.7 |                 53.3 |
| UNIVERSITY OF FLORIDA                                                                 | Foreign              |                15 |            73 |        65.5 |       54.5 |         87 |                     136 |    86.7 |      80 |           66.7 |                 16.7 |
| CALAMBA DOCTORS' COLLEGE                                                              | Private              |                14 |          35.5 |        35.8 |       10.2 |       58.8 |                   118.5 |    58.3 |    41.7 |           57.1 |                   70 |
| SAINT TONIS COLLEGE                                                                   | Private              |                14 |            33 |        41.6 |         21 |         64 |                     107 |    64.3 |    42.9 |           71.4 |                 33.3 |
| ST. PAUL UNIVERSITY SURIGAO                                                           | Private              |                14 |            45 |        42.1 |       12.5 |         74 |                   112.5 |    61.5 |    53.8 |           57.1 |                 37.5 |
| URDANETA CITY UNIVERSITY                                                              | Public               |                14 |          52.5 |        50.5 |         30 |       71.2 |                   120.5 |    71.4 |    64.3 |           85.7 |                   60 |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                     | Public               |                14 |          66.5 |        54.4 |       24.5 |       82.2 |                     134 |    71.4 |    64.3 |           64.3 |                 18.2 |
| NOTRE DAME OF TACURONG COLLEGE                                                        | Private              |                14 |            28 |        33.4 |       10.5 |         44 |                   102.5 |    42.9 |    35.7 |           71.4 |                   25 |
| AKLAN STATE UNIVERSITY - MAIN                                                         | Public               |                14 |            48 |        47.5 |       22.5 |       71.5 |                     117 |    71.4 |    57.1 |           57.1 |                   40 |
| MONAD UNIVERSITY                                                                      | Foreign              |                14 |            55 |        50.6 |       16.5 |         77 |                     135 |    64.3 |    57.1 |           42.9 |                  nan |
| SAINT GABRIEL COLLEGE                                                                 | Private              |                13 |            32 |          39 |         11 |         51 |                     104 |    53.8 |    38.5 |           53.8 |                   20 |
| COLEGIO DE SAN LORENZO RUIZ DE MANILA OF NORTHERN SAMAR                               | Private              |                13 |            55 |        47.5 |         28 |         58 |                     124 |    69.2 |    69.2 |           69.2 |                 57.1 |
| UNIVERSITY OF SAINT ANTHONY                                                           | Private              |                13 |            39 |        41.2 |         31 |         52 |                     117 |    83.3 |      50 |           46.2 |                 37.5 |
| NOTRE DAME OF MIDSAYAP COLLEGE                                                        | Private              |                13 |            58 |        43.9 |       13.2 |       69.5 |                     123 |    63.6 |    63.6 |           53.8 |                 42.9 |
| WESTERN LEYTE COLLEGE OF ORMOC CITY                                                   | Private              |                13 |            48 |        45.8 |         14 |         76 |                     115 |    53.8 |    53.8 |           69.2 |                  100 |
| CENTRAL COLLEGES OF THE PHILIPPINES                                                   | Private              |                13 |          51.5 |        49.8 |       35.8 |       72.2 |                     127 |      75 |      75 |           53.8 |                 23.1 |
| UNIVERSITY OF BOHOL TAGBILARAN CITY                                                   | Private              |                13 |            40 |        40.5 |          9 |         69 |                     118 |    61.5 |    53.8 |           76.9 |                 69.2 |
| HOLY CROSS OF DAVAO COLLEGE                                                           | Private              |                13 |            33 |        40.8 |          8 |         69 |                     100 |    53.8 |    46.2 |           38.5 |                   40 |
| SACRED HEART COLLEGE LUCENA CITY                                                      | Private              |                13 |            42 |        48.8 |         27 |         63 |                     122 |    61.5 |    53.8 |           30.8 |                 61.5 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - GMA                                             | Private              |                13 |            18 |        27.2 |         10 |         43 |                      96 |      50 |    41.7 |           76.9 |                 27.3 |
| University For Development Studies                                                    | Not Specified        |                13 |            37 |        42.8 |          2 |         68 |                     122 |    53.8 |    46.2 |           53.8 |                   40 |
| 13100A                                                                                | Not Specified        |                13 |            52 |        50.3 |         29 |         74 |                     121 |    69.2 |    69.2 |           92.3 |                 15.4 |
| BICOL UNIVERSITY - DARAGA                                                             | Public               |                13 |            34 |        31.5 |          9 |         43 |                     104 |    53.8 |    38.5 |           30.8 |                    0 |
| ST. FERDINAND COLLEGE - ILAGAN                                                        | Private              |                13 |            37 |        46.8 |         31 |         61 |                     118 |    76.9 |    46.2 |           61.5 |                   20 |
| DE LA SALLE - ARANETA UNIVERSITY                                                      | Private              |                13 |            32 |        37.9 |          9 |         62 |                     113 |    53.8 |    46.2 |           30.8 |                 37.5 |
| DOMINICAN COLLEGE                                                                     | Private              |                13 |            27 |        39.6 |       19.5 |         59 |                     115 |    45.5 |    45.5 |           53.8 |                 21.4 |
| UNCIANO COLLEGES AND GENERAL HOSPITAL                                                 | Private              |                12 |            50 |        49.5 |       24.2 |         71 |                   130.5 |      70 |      60 |             50 |                 16.7 |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE NEGROS OCCIDENTAL                                | Private              |                12 |            50 |        45.2 |       23.5 |         59 |                     128 |    66.7 |    58.3 |             50 |                 66.7 |
| UNIVERSITY OF THE PHILIPPINES - PAMPANGA                                              | Public               |                12 |          61.5 |        56.7 |         44 |         67 |                     137 |    91.7 |    91.7 |           16.7 |                 33.3 |
| BICOL UNIVERSITY - POLANGUI                                                           | Public               |                12 |            51 |        55.7 |       39.2 |         65 |                   122.5 |    91.7 |      75 |           66.7 |                   60 |
| UNCIANO COLLEGES                                                                      | Private              |                12 |            32 |        44.5 |         20 |         69 |                   111.5 |    54.5 |    54.5 |             75 |                   30 |
| SOUTHEAST ASIAN COLLEGE INC.-ESPANA MANILA                                            | Private              |                12 |             8 |         9.9 |        4.5 |         14 |                      88 |       0 |       0 |           33.3 |                   25 |
| UNIVERSITY OF CALIFORNIA SANTA BARBARA                                                | Foreign              |                12 |          47.5 |        49.1 |       33.2 |       66.2 |                   126.5 |      75 |    58.3 |             25 |                 22.2 |
| PHILIPPINE REHABILITATION INSTITUTE                                                   | Private              |                12 |            35 |        35.5 |       16.5 |         54 |                   115.5 |      50 |      50 |             50 |                   50 |
| FIRST ASIA INSTITUTE OF TECHNOLOGY AND HUMANITIES                                     | Private              |                12 |            48 |        52.3 |         39 |         68 |                     123 |    91.7 |      75 |           66.7 |                   50 |
| DR. YANGA'S COLLEGES                                                                  | Private              |                12 |            44 |          46 |       30.5 |         56 |                   111.5 |    81.8 |    54.5 |           33.3 |                   25 |
| COLLEGE OF HOLY SPIRIT-MANILA                                                         | Private              |                12 |            15 |        20.6 |          6 |         34 |                      93 |    33.3 |    16.7 |           41.7 |                   75 |
| MEDINA COLLEGE - IPIL                                                                 | Private              |                12 |            42 |        43.3 |       13.8 |         69 |                     115 |    54.5 |    54.5 |           58.3 |                 33.3 |
| UNIVERSITY OF NEVADA LAS VEGAS                                                        | Foreign              |                12 |            67 |        61.7 |       46.2 |         85 |                     131 |    83.3 |      75 |           33.3 |                 11.1 |
| UNIVERSITY OF PERPETUAL HELP - CALAMBA LAGUNA                                         | Private              |                12 |            35 |          37 |         16 |       53.2 |                     114 |    66.7 |    41.7 |           66.7 |                 38.5 |
| NOTRE DAME OF MARBEL UNIV.                                                            | Private              |                12 |          43.5 |        45.3 |       33.2 |       61.5 |                   122.5 |      75 |    58.3 |           41.7 |                   50 |
| AMA COMPUTER COLLEGE                                                                  | Private              |                12 |            19 |          24 |          5 |       32.2 |                     104 |    33.3 |    16.7 |           16.7 |                 16.7 |
| LYCEUM OF APARRI                                                                      | Private              |                12 |          35.5 |        44.1 |       24.8 |         54 |                     108 |    58.3 |    41.7 |             50 |                   25 |
| LAGUNA COLLEGE                                                                        | Private              |                11 |            50 |        51.4 |       38.5 |         62 |                     120 |    90.9 |    63.6 |           72.7 |                 12.5 |
| UNIVERSITY OF ILOILO                                                                  | Private              |                11 |            66 |        59.4 |       34.5 |       91.5 |                     136 |    72.7 |    72.7 |           54.5 |                   40 |
| NOTRE DAME OF JOLO COLLEGE - JOLO SULU                                                | Private              |                11 |            11 |        16.5 |        6.5 |       21.5 |                      91 |    18.2 |    18.2 |           63.6 |                 18.2 |
| NORTHERN NEGROS STATE COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                        | Public               |                11 |            61 |        56.5 |         28 |       89.5 |                     140 |    72.7 |    63.6 |           45.5 |                 66.7 |
| MABINI COLLEGES                                                                       | Private              |                11 |            55 |        51.8 |         18 |       81.5 |                     120 |    63.6 |    54.5 |           63.6 |                 42.9 |
| MEDINA COLLEGE OZAMIS MISAMIS ORIENTAL                                                | Private              |                11 |            15 |        23.2 |        7.5 |         36 |                      92 |    27.3 |    27.3 |           54.5 |                 36.4 |
| NORTHERN CHRISTIAN COLLEGE                                                            | Private              |                11 |            57 |        52.5 |         18 |       92.5 |                     124 |    54.5 |    54.5 |           36.4 |                   50 |
| MARIANO MARCOS STATE UNIVERSITY - COLLEGE OF EDUCATION - LAOAG CITY                   | Public               |                11 |            45 |        48.6 |         20 |         75 |                     122 |    63.6 |    54.5 |           81.8 |                   20 |
| UNIVERSITY OF CORDILLERAS                                                             | Private              |                11 |            37 |        43.4 |       23.5 |         69 |                     117 |    54.5 |    45.5 |           72.7 |                 54.5 |
| UNIVERSITY OF THE PHILIPPINES SCH. OF HEALTH SCIENCES -LEYTE                          | Public               |                11 |            25 |        27.9 |       16.5 |         37 |                     106 |    27.3 |    27.3 |           81.8 |                 81.8 |
| BRENT HOSPITAL AND COLLEGES INC. ZAMBOANGA CITY                                       | Private              |                11 |            10 |        12.9 |          8 |       14.5 |                      88 |     9.1 |       0 |           63.6 |                 27.3 |
| VIRGEN MILAGROSA EDUCATIONAL INSTITUTE SAN CARLOS CITY                                | Private              |                11 |            38 |        42.5 |       33.5 |       57.5 |                     117 |    81.8 |    45.5 |           27.3 |                  9.1 |
| ST. JOSEPH'S COLLEGE QUEZON CITY                                                      | Private              |                11 |            25 |        27.6 |       19.5 |         35 |                     107 |    36.4 |    18.2 |           90.9 |                 54.5 |
| SRINAKHARINWIROT UNIVERSITY                                                           | Foreign              |                11 |            32 |        34.1 |       21.5 |         46 |                     104 |      70 |      40 |           45.5 |                    0 |
| OLIVAREZ COLLEGE SUCAT PARA$AQUE                                                      | Private              |                11 |            27 |        30.5 |       11.5 |         43 |                     113 |    45.5 |    27.3 |           54.5 |                 18.2 |
| UNIVERSITY OF PERPETUAL HELP - RIZAL                                                  | Private              |                11 |            38 |        39.5 |        6.5 |       68.5 |                     119 |    54.5 |    45.5 |           63.6 |                 41.7 |
| CHRIST THE KING COLLEGE - CALBAYOG CITY                                               | Private              |                11 |            38 |        42.7 |       23.5 |         63 |                     113 |    63.6 |    36.4 |           81.8 |                 33.3 |
| RUTGERS UNIVERSITY NEW JERSEY                                                         | Foreign              |                11 |            72 |        73.5 |         62 |       85.5 |                     151 |     100 |     100 |              0 |                 27.3 |
| PHILIPPINE NORMAL COLLEGE TAFT AVENUE MANILA                                          | Public               |                11 |            54 |        53.9 |         43 |       71.5 |                     130 |    81.8 |    81.8 |              0 |                 45.5 |
| HUACHIEW CHALERMPRAKIET UNIVERSITY                                                    | Foreign              |                11 |            36 |        47.2 |         26 |       61.5 |                     107 |    54.5 |    45.5 |           54.5 |                 37.5 |
| KIDAPAWAN DOCTORS COLLEGE INC.                                                        | Private              |                11 |            29 |        45.4 |       26.5 |       63.5 |                     102 |    45.5 |    45.5 |           45.5 |                  nan |
| UNIVERSITY OF SAN FRANCISCO                                                           | Foreign              |                11 |            75 |        69.7 |         56 |       87.5 |                     148 |     100 |    81.8 |           36.4 |                 33.3 |
| FOUNDATION UNIVERSITY                                                                 | Private              |                11 |            48 |        50.4 |       34.5 |         78 |                     117 |      90 |      70 |           36.4 |                    0 |
| FELLOWSHIP BAPTIST COLLEGE                                                            | Private              |                11 |            69 |        57.8 |         41 |       81.5 |                     127 |    81.8 |    72.7 |           36.4 |                 71.4 |
| DR. CARLOS LANTING COLLEGE - NOVALICHES QUEZON CITY                                   | Private              |                11 |            24 |        30.3 |        4.5 |         45 |                     108 |    45.5 |    27.3 |           63.6 |                 18.2 |
| CORDILLERA CAREER DEVELOPMENT COLLEGE                                                 | Private              |                11 |            60 |        59.1 |         45 |         73 |                     125 |    90.9 |    90.9 |           63.6 |                 37.5 |
| UNIVERSITY OF CENTRAL FLORIDA                                                         | Foreign              |                10 |          50.5 |        46.3 |       22.5 |       69.8 |                     121 |      70 |      60 |             50 |                 11.1 |
| UNIVERSITY OF GUAM                                                                    | Foreign              |                10 |            38 |        49.1 |       32.8 |       79.8 |                     115 |      80 |      50 |             50 |                   25 |
| NOTRE DAME OF KIDAPAWAN COLLEGE                                                       | Private              |                10 |          39.5 |        32.8 |         13 |       46.8 |                     109 |      60 |      50 |             70 |                 37.5 |
| MARY HELP OF CHRISTIANS COLLEGE SEMINARY                                              | Private              |                10 |          16.5 |        20.8 |       14.2 |         25 |                    97.5 |      20 |      10 |            100 |                   50 |
| JOSE RIZAL UNIVERSITY                                                                 | Private              |                10 |          53.5 |        56.5 |       38.5 |         81 |                   126.5 |      90 |      70 |             70 |                   40 |
| COLUMBAN COLLEGE - OLONGAPO CITY                                                      | Private              |                10 |            50 |        54.7 |       36.2 |       79.2 |                   120.5 |      80 |      70 |             50 |                   40 |
| RUTGERS UNIVERSITY                                                                    | Foreign              |                10 |          79.5 |        70.5 |       58.5 |       91.2 |                     145 |      90 |      90 |             60 |                 71.4 |
| POLYTECHNIC COLLEGE OF DAVAO DEL SUR                                                  | Private              |                10 |            64 |        55.6 |         15 |       96.2 |                   127.5 |      60 |      50 |             60 |                 66.7 |
| UNIVERSITAS ADVENT INDONESIA                                                          | Foreign              |                10 |          53.5 |        47.8 |       15.2 |       73.5 |                   122.5 |      60 |      60 |             50 |                 22.2 |
| CAMARINES NORTE STATE COLLEGE - MAIN                                                  | Public               |                10 |          48.5 |        48.4 |       19.8 |       78.2 |                     130 |      60 |      50 |             70 |                  100 |
| SIENA COLLEGE OF TAYTAY                                                               | Private              |                10 |            57 |        47.5 |       19.8 |       71.5 |                     120 |    77.8 |    66.7 |             50 |                   20 |
| ST. LUKE'S SCHOOL OF MEDICINE INDIA                                                   | Private              |                10 |          35.5 |        34.6 |       24.5 |       44.8 |                     116 |      60 |      50 |             10 |                    0 |
| BROKENSHIRE COLLEGE SOCSKSARGEN                                                       | Private              |                10 |            24 |          43 |       12.5 |         84 |                     106 |      50 |      40 |             70 |                 28.6 |
| UM TAGUM COLLEGE                                                                      | Private              |                10 |            57 |        53.6 |         29 |         77 |                     123 |    66.7 |    55.6 |             60 |                    0 |
| SULTAN KUDARAT STATE UNIVERSITY - TACURONG                                            | Public               |                10 |            24 |        27.1 |        7.5 |         40 |                     105 |    44.4 |    33.3 |             20 |                  nan |
| SULTAN KUDARAT STATE UNIVERSITY - MAIN                                                | Public               |                10 |            34 |        30.8 |        5.5 |       51.8 |                   103.5 |      50 |      50 |             60 |                    0 |
| VIRGINIA COMMONWEALTH UNIVERSITY                                                      | Foreign              |                 9 |            77 |        77.7 |         65 |         87 |                     143 |     100 |     100 |           22.2 |                 42.9 |
| SAN SEBASTIAN COLLEGE - RECOLETOS CANLUBANG                                           | Private              |                 9 |          53.5 |        49.5 |       27.5 |       72.8 |                     128 |      75 |    62.5 |           44.4 |                 83.3 |
| Texila American University                                                            | Not Specified        |                 9 |            46 |        49.2 |         14 |         79 |                     113 |    66.7 |    66.7 |           55.6 |                 33.3 |
| STONY BROOK UNIVERSITY                                                                | Foreign              |                 9 |            59 |        58.3 |         36 |         85 |                     130 |    77.8 |    66.7 |           11.1 |                 28.6 |
| SAN SEBASTIAN COLLEGE - RECOLETOS DE CAVITE                                           | Private              |                 9 |            36 |        41.7 |         28 |         42 |                     109 |    66.7 |    33.3 |           55.6 |                  100 |
| WESTERN VISAYAS COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                              | Public               |                 9 |            68 |        53.4 |         31 |         78 |                     134 |    77.8 |    66.7 |           33.3 |                 28.6 |
| NUEVA ECIJA UNIVERSITY OF SCIENCE AND TECHNOLOGY - MAIN                               | Public               |                 9 |            62 |        53.2 |         35 |         69 |                     130 |    77.8 |    66.7 |           44.4 |                 33.3 |
| UNIVERSITY OF ILLINOIS CHICAGO                                                        | Foreign              |                 9 |            84 |        75.9 |         75 |         93 |                     160 |    88.9 |    88.9 |              0 |                    0 |
| UNIVERSITY OF CALIFORNIA AT STA. CRUZ U.S.A.                                          | Foreign              |                 9 |            61 |        49.8 |         25 |         69 |                     138 |    66.7 |    66.7 |              0 |                    0 |
| ISABELA STATE UNIVERSITY - ILAGAN                                                     | Public               |                 9 |            75 |        71.6 |         54 |         89 |                     148 |     100 |    88.9 |           55.6 |                   50 |
| JOSE RIZAL MEMORIAL STATE UNIVERSITY - MAIN                                           | Public               |                 9 |          19.5 |        31.9 |       13.8 |       41.5 |                      92 |    37.5 |      25 |           44.4 |                 66.7 |
| KALAYAAN COLLEGE                                                                      | Private              |                 9 |            47 |        44.6 |         18 |         74 |                     122 |    55.6 |    55.6 |           22.2 |                   20 |
| DOMINICAN COLLEGE BLUM SAN JUAN MM                                                    | Private              |                 9 |            25 |          31 |         12 |         36 |                     103 |    33.3 |    22.2 |           44.4 |                 11.1 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                  | Public               |                 9 |            51 |        46.4 |         11 |         68 |                     130 |    66.7 |    66.7 |           66.7 |                    0 |
| MINDANAO MEDICAL FOUNDATION COLLEGE DAVAO                                             | Private              |                 9 |            15 |        22.9 |          4 |         40 |                      91 |    33.3 |    33.3 |           77.8 |                 11.1 |
| UNIVERSITY OF RIZAL SYSTEM - MORONG                                                   | Public               |                 9 |            53 |        52.2 |         27 |         79 |                     127 |    66.7 |    55.6 |           66.7 |                 16.7 |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - LAGUNA COLLEGE OF ARTS AND TRADES - STA. CRUZ   | Public               |                 9 |            63 |        60.9 |         46 |         76 |                     124 |    88.9 |    88.9 |           44.4 |                  nan |
| NOTRE DAME OF MARBEL COLLEGE SOUTH COTABATO                                           | Private              |                 9 |            38 |        40.7 |         23 |         45 |                     116 |    66.7 |    44.4 |           55.6 |                 44.4 |
| LA SALLE COLLEGE - ANTIPOLO                                                           | Private              |                 9 |            18 |        33.7 |          9 |         41 |                      98 |    44.4 |    33.3 |           22.2 |                   25 |
| BURAPHA UNIVERSITY                                                                    | Foreign              |                 9 |            11 |          16 |          2 |         15 |                      86 |    11.1 |    11.1 |           88.9 |                 14.3 |
| CALIFORNIA STATE UNIVERSITY FRESNO                                                    | Foreign              |                 9 |            28 |        37.2 |          6 |         55 |                     105 |    44.4 |    33.3 |           55.6 |                 16.7 |
| CALIFORNIA STATE UNIVERSITY LONG BEACH                                                | Foreign              |                 9 |            35 |        42.6 |          6 |         82 |                     114 |    62.5 |      50 |           33.3 |                   25 |
| DELOS SANTOS COLLEGE                                                                  | Private              |                 9 |            41 |        38.8 |         24 |         53 |                     120 |    66.7 |    55.6 |           66.7 |                 44.4 |
| CHIANG KAI SHEK COLLEGE                                                               | Private              |                 9 |            52 |        55.9 |         33 |         78 |                     122 |    77.8 |    66.7 |            100 |                   50 |
| CENTRO ESCOLAR UNIVERSITY-MALOLOS BULACAN                                             | Private              |                 9 |            36 |        30.6 |         22 |         37 |                     113 |    66.7 |    22.2 |           44.4 |                 33.3 |
| PATTS COLLEGE OF AERONAUTICS                                                          | Private              |                 9 |            49 |        55.9 |         24 |         75 |                     115 |    66.7 |    66.7 |           77.8 |                    0 |
| UNIVERSITY OF HAWAII AT MANOA                                                         | Foreign              |                 9 |            73 |        64.8 |         49 |       83.8 |                     159 |    87.5 |    87.5 |           55.6 |                 42.9 |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-ALABANG ZAPOTE                              | Private              |                 9 |            31 |        30.3 |         12 |         38 |                     110 |    55.6 |    22.2 |           55.6 |                 66.7 |
| UNIVERSITY OF BRITISH COLUMBIA                                                        | Foreign              |                 8 |          26.5 |        31.8 |        7.5 |         44 |                     100 |    37.5 |      25 |           37.5 |                    0 |
| THAMMASAT UNIV.                                                                       | Foreign              |                 8 |            23 |        21.4 |          8 |         27 |                     106 |      25 |    12.5 |           12.5 |                    0 |
| UNIVERSITY OF CEBU - LAPULAPU AND MANDAUE                                             | Private              |                 8 |          55.5 |        62.2 |       43.2 |       88.8 |                     128 |    87.5 |    87.5 |             50 |                 66.7 |
| MINDANAO UNIVERSITY OF SCIENCE AND TECHNOLOGY                                         | Public               |                 8 |          57.5 |        56.6 |       40.2 |       79.8 |                   122.5 |      75 |      75 |             25 |                  100 |
| UNIVERSITY OF NORTHERN PHILIPPINES VIGAN ILOCOS SUR                                   | Public               |                 8 |            11 |        14.1 |          7 |       20.5 |                    89.5 |       0 |       0 |           37.5 |                 37.5 |
| MAPANDI MEMORIAL COLLEGE                                                              | Private              |                 8 |          37.5 |        40.5 |       29.8 |         46 |                   107.5 |      75 |      50 |             50 |                    0 |
| UNIVERSITY OF THE ASSUMPTION PAMPANGA                                                 | Private              |                 8 |            36 |        44.8 |         16 |       80.2 |                   114.5 |      50 |      50 |             50 |                   25 |
| RAMKHAMHAENG UNIVERSITY                                                               | Foreign              |                 8 |          64.5 |        58.5 |       42.5 |       81.8 |                     128 |      75 |      75 |           37.5 |                 33.3 |
| PHILIPPINE WOMEN'S COLLEGE OF DAVAO                                                   | Private              |                 8 |            37 |        47.1 |       29.2 |       72.2 |                   115.5 |      75 |    37.5 |             25 |                  nan |
| PRINCE OF SONGKLA UNIVERSITY                                                          | Foreign              |                 8 |          40.5 |        45.2 |         30 |       62.5 |                     111 |    87.5 |      50 |           62.5 |                    0 |
| ALDERSGATE COLLEGE                                                                    | Private              |                 8 |          39.5 |        42.6 |        9.8 |       65.5 |                     110 |      50 |      50 |           87.5 |                 57.1 |
| ST. JOSEPH COLLEGE CAVITE                                                             | Private              |                 8 |            16 |        23.8 |          7 |       45.8 |                    99.5 |    37.5 |    37.5 |           37.5 |                 37.5 |
| U.P. VISAYAS (TACLOBAN CITY LEYTE)                                                    | Public               |                 8 |          70.5 |        62.6 |       58.5 |       75.8 |                     144 |    87.5 |    87.5 |              0 |                 62.5 |
| LA CONSOLACION COLLEGE - DAET                                                         | Private              |                 8 |            74 |        63.1 |       43.2 |       87.5 |                   133.5 |      75 |      75 |           62.5 |                   50 |
| ENDERUN COLLEGE                                                                       | Private              |                 8 |          33.5 |        35.2 |         15 |       57.8 |                   103.5 |      50 |    37.5 |           62.5 |                   40 |
| FELIPE R. VERALLO MEMORIAL FOUNDATION - BOGO                                          | Private              |                 8 |          78.5 |        67.8 |         60 |         82 |                     137 |    87.5 |    87.5 |           37.5 |                    0 |
| UNIVERSITY OF TEXAS                                                                   | Foreign              |                 8 |            96 |        79.7 |         60 |         97 |                     183 |     100 |     100 |           62.5 |                   50 |
| COLLEGE OF ST. JOHN - ROXAS                                                           | Private              |                 8 |            13 |        25.4 |         11 |         37 |                    93.5 |    42.9 |    28.6 |             75 |                    0 |
| 13155D                                                                                | Not Specified        |                 8 |            63 |        52.4 |         24 |         78 |                     140 |    62.5 |    62.5 |           37.5 |                   50 |
| UNIVERSITY OF CALIFORNIA SANTA CRUZ                                                   | Foreign              |                 8 |            74 |          60 |         38 |         86 |                     140 |      75 |      75 |           37.5 |                 33.3 |
| KESTER GRANT COLLEGE PHILS. INC.                                                      | Private              |                 7 |            13 |        22.7 |         11 |         26 |                      94 |    28.6 |    14.3 |           57.1 |                 42.9 |
| BICOL COLLEGE                                                                         | Private              |                 7 |            57 |        58.1 |         49 |       72.5 |                     124 |    85.7 |    85.7 |           28.6 |                   50 |
| CATANDUANES STATE COLLEGE                                                             | Public               |                 7 |             9 |        29.1 |        6.5 |       45.5 |                      95 |    28.6 |    28.6 |           42.9 |                 71.4 |
| University Of Port Harcourt                                                           | Not Specified        |                 7 |            41 |        55.7 |         30 |         91 |                     118 |    71.4 |    57.1 |           28.6 |                    0 |
| DR. JOSE FABELLA MEMORIAL HOSPITAL SCHOOL OF MIDWIFERY                                | Private              |                 7 |            77 |        63.7 |       38.5 |         87 |                     151 |    85.7 |    71.4 |           42.9 |                  nan |
| COLLEGE OF THE IMMACULATE CONCEPTION                                                  | Private              |                 7 |            43 |        37.1 |       11.5 |       47.5 |                     109 |    57.1 |    57.1 |           42.9 |                 33.3 |
| CONCORDIA COLLEGE                                                                     | Private              |                 7 |            46 |        39.6 |         29 |         50 |                     113 |    71.4 |    71.4 |           57.1 |                 33.3 |
| DAVAO CENTRAL COLLEGE                                                                 | Private              |                 7 |            43 |        43.3 |       21.5 |       65.5 |                     113 |    83.3 |    66.7 |           57.1 |                 37.5 |
| HOLY TRINITY COLLEGE PUERTO PRINCESA                                                  | Private              |                 7 |            21 |          34 |       16.5 |       54.5 |                     102 |    42.9 |    42.9 |            100 |                 42.9 |
| NORTHEASTERN COLLEGE                                                                  | Private              |                 7 |          50.5 |        48.5 |       26.8 |       66.8 |                     118 |    66.7 |    66.7 |           57.1 |                   50 |
| UNIVERSITY OF IMMACULATE CONCEPTION-DAVAO CITY                                        | Private              |                 7 |            21 |        18.1 |       10.5 |       26.5 |                     104 |    28.6 |       0 |            100 |                 28.6 |
| NEGROS ORIENTAL STATE UNIVERSITY                                                      | Public               |                 7 |            13 |        16.7 |        7.5 |         25 |                      90 |    28.6 |       0 |              0 |                 57.1 |
| EASTERN SAMAR STATE UNIVERSITY - MAIN                                                 | Public               |                 7 |            56 |        57.3 |         51 |         72 |                     129 |    85.7 |    85.7 |           42.9 |                  100 |
| UNIVERSITY OF LUZON ( DAGUPAN CITY )                                                  | Private              |                 7 |            25 |        20.1 |        5.5 |         32 |                     104 |    28.6 |    14.3 |           57.1 |                 71.4 |
| MALASIQUI AGNO VALLEY COLLEGE - MALASIQUI PANGASINAN                                  | Private              |                 7 |             9 |        22.6 |        7.5 |         27 |                      85 |    28.6 |    14.3 |           57.1 |                    0 |
| INTERNATIONAL COLLEGES OF ASIA - TAMBAC PANGASINAN                                    | Private              |                 7 |            26 |        36.1 |         24 |       46.5 |                     109 |    28.6 |    28.6 |           71.4 |                 57.1 |
| NAVAL STATE UNIVERSITY - MAIN                                                         | Public               |                 7 |            77 |          60 |         32 |         84 |                     140 |    85.7 |    57.1 |           14.3 |                    0 |
| OLIVAREZ COLLEGE - TAGAYTAY                                                           | Private              |                 7 |            46 |        52.9 |       24.5 |         83 |                     125 |    57.1 |    57.1 |           71.4 |                   40 |
| WEST NEGROS COLLEGE BACOLOD                                                           | Private              |                 7 |            19 |        18.7 |          7 |         28 |                      98 |    28.6 |       0 |           71.4 |                 42.9 |
| SAFFRULLAH M. DIPATUAN FOUNDATION ACADEMY                                             | Private              |                 7 |            63 |        60.6 |       34.5 |       94.5 |                     129 |    71.4 |    71.4 |           28.6 |                   50 |
| THE COLLEGE OF MAASIN                                                                 | Private              |                 7 |            63 |          58 |       27.5 |         94 |                     124 |    57.1 |    57.1 |           71.4 |                   40 |
| SAINT LOUIS COLLEGE - CITY OF SAN FERNANDO                                            | Private              |                 7 |            48 |        40.1 |         18 |       57.5 |                     114 |    83.3 |    66.7 |           57.1 |                 33.3 |
| SAINT LOUIS COLLEGE                                                                   | Private              |                 7 |            19 |        35.4 |         11 |         52 |                      95 |    42.9 |    42.9 |           42.9 |                   20 |
| SAN SEBASTIAN COLLEGE                                                                 | Private              |                 7 |            22 |        28.3 |         17 |         38 |                     108 |    42.9 |    28.6 |           14.3 |                 14.3 |
| COTABATO MEDICAL FOUNDATION COLLEGE                                                   | Private              |                 7 |            59 |        48.9 |       19.5 |       71.5 |                     125 |    57.1 |    57.1 |           42.9 |                   20 |
| PANPACIFIC UNIVERSITY NORTH PHILIPPINES - URDANETA CITY                               | Private              |                 7 |            48 |        45.6 |         23 |         70 |                     128 |    71.4 |    57.1 |           57.1 |                   50 |
| PAMANTASAN NG LUNGSOD NG PASAY                                                        | Public               |                 7 |            39 |        38.6 |         21 |         49 |                     109 |    57.1 |    42.9 |           28.6 |                   20 |
| UNIVERSITY OF CALIFORNIA MERCED                                                       | Foreign              |                 7 |            48 |        46.1 |       36.5 |         61 |                     116 |    71.4 |    71.4 |           42.9 |                 66.7 |
| UNIVERSITY OF HOUSTON                                                                 | Foreign              |                 7 |            64 |          53 |         22 |       83.5 |                     129 |    71.4 |    57.1 |           57.1 |                  100 |
| SAINT MARY'S COLLEGE OF SAN JUAN                                                      | Private              |                 7 |            14 |        30.3 |          4 |       47.5 |                      85 |    28.6 |    28.6 |           71.4 |                 33.3 |
| ASSUMPTION UNIVERSITY                                                                 | Foreign              |                 6 |          33.5 |        36.7 |       24.5 |       38.8 |                     109 |      80 |      40 |             50 |                    0 |
| Christian University Of Thailand                                                      | Not Specified        |                 6 |            32 |        26.2 |         18 |         36 |                     105 |      75 |      25 |             50 |                 33.3 |
| COR JESU COLLEGE                                                                      | Private              |                 6 |            53 |        54.2 |       41.5 |         75 |                     124 |    83.3 |    66.7 |           66.7 |                  nan |
| UNIVERSITY OF SOUTH FLORIDA USA                                                       | Foreign              |                 6 |            53 |        51.3 |       30.5 |       66.5 |                   135.5 |    66.7 |    66.7 |             50 |                    0 |
| ASIA-PACIFIC INTERNATIONAL UNIVERSITY                                                 | Private              |                 6 |          54.5 |        46.2 |         34 |       63.8 |                   123.5 |     100 |      80 |             50 |                   20 |
| BATAAN PENINSULA STATE UNIVERSITY                                                     | Public               |                 6 |            18 |          28 |        8.5 |       30.5 |                     101 |    33.3 |    16.7 |           66.7 |                 33.3 |
| Adventist University Of Indonesia                                                     | Not Specified        |                 6 |          59.5 |        54.7 |       40.8 |         73 |                   120.5 |    83.3 |    66.7 |           33.3 |                   60 |
| CHIANGMAI UNIVERSITY                                                                  | Foreign              |                 6 |            53 |          57 |       26.8 |       88.2 |                     116 |    66.7 |      50 |             50 |                   25 |
| ARRIESGADO COLLEGE FOUNDATION                                                         | Private              |                 6 |          50.5 |        47.7 |         31 |         70 |                   127.5 |    66.7 |    66.7 |            100 |                   50 |
| ST. JOSEPH COLLEGE AMAYA                                                              | Private              |                 6 |          79.5 |        68.2 |         64 |       88.2 |                     144 |    83.3 |    83.3 |           66.7 |                  100 |
| ST. MARY'S UNIVERSITY NUEVA VIZCAYA                                                   | Private              |                 6 |          24.5 |        30.7 |       13.5 |       43.8 |                   107.5 |      50 |    33.3 |             50 |                 16.7 |
| THE NATIONAL TEACHERS COLLEGE                                                         | Private              |                 6 |            68 |          58 |       30.2 |       86.2 |                     135 |    66.7 |    66.7 |           66.7 |                  nan |
| ST. BERNADETTE OF LOURDES COLLEGE                                                     | Private              |                 6 |          55.5 |        43.8 |       21.8 |       64.5 |                     119 |    66.7 |    66.7 |            100 |                   50 |
| ST. ANTHONY COLLEGE OF ROXAS CITY CAPIZ                                               | Private              |                 6 |            19 |        26.8 |         10 |       29.5 |                     104 |    33.3 |    16.7 |           33.3 |                 33.3 |
| AGO MEDICAL EDUCATIONAL FOUNDATION LEGASPI CITY                                       | Private              |                 6 |            31 |        31.8 |       17.5 |       44.5 |                     111 |      50 |    33.3 |              0 |                 66.7 |
| AMA COMPUTER COLLEGE - TUGUEGARAO CITY                                                | Private              |                 6 |            49 |        54.5 |       38.2 |       63.5 |                     127 |    83.3 |    66.7 |           16.7 |                    0 |
| SAN DIEGO STATE UNIVERSITY - CALIFORNIA U.S.A.                                        | Foreign              |                 6 |            52 |        48.7 |       36.8 |       64.2 |                   134.5 |    83.3 |    66.7 |             50 |                 16.7 |
| SAN ISIDRO COLLEGE                                                                    | Private              |                 6 |          33.5 |        36.5 |       16.2 |       43.2 |                      99 |    66.7 |    33.3 |             50 |                    0 |
| UNIVERSITY AT BUFFALO                                                                 | Foreign              |                 6 |            47 |        48.8 |         34 |         69 |                   135.5 |      80 |      60 |             50 |                    0 |
| ANGELES SYSTEMS PLUS COMPUTER COLLEGE                                                 | Private              |                 6 |            40 |        43.5 |       27.5 |       47.2 |                     116 |    66.7 |      50 |           33.3 |                    0 |
| ILOCOS SUR POLYTECHNIC STATE COLLEGE                                                  | Public               |                 6 |          47.5 |          47 |       31.5 |         59 |                     124 |    66.7 |    66.7 |            100 |                 16.7 |
| KHON KAEN UNIVERSITY                                                                  | Foreign              |                 6 |          30.5 |        40.5 |       11.5 |       65.2 |                   106.5 |      50 |      50 |           16.7 |                    0 |
| COLEGIO DE KIDAPAWAN                                                                  | Private              |                 6 |            62 |          58 |         43 |         81 |                     129 |    83.3 |    83.3 |           33.3 |                 66.7 |
| CALIFORNIA STATE UNIVERSITY - FULLERTON                                               | Foreign              |                 6 |          75.5 |        68.3 |       73.2 |         77 |                     149 |    83.3 |    83.3 |           33.3 |                    0 |
| SOUTHERN LUZON POLYTECHNIC COLLEGE - LUCBAN QUEZON                                    | Private              |                 6 |            28 |        24.5 |         14 |         33 |                     105 |      50 |       0 |             50 |                   50 |
| LADOKE AKINTOLA UNIVERSITY OF TECHNOLOGY OGBOMOSO                                     | Foreign              |                 6 |            21 |        28.8 |        7.5 |         45 |                    92.5 |    33.3 |    33.3 |             50 |                    0 |
| MAHASARAKHAM UNIVERSITY                                                               | Foreign              |                 6 |            24 |        21.2 |       16.5 |       29.2 |                     101 |    33.3 |       0 |           33.3 |                    0 |
| OUR LADY OF THE PILLAR COLLEGE - CAUAYAN                                              | Private              |                 6 |          20.5 |        29.2 |        5.2 |       43.2 |                    99.5 |    33.3 |    33.3 |             50 |                 66.7 |
| LYCEUM NORTHWESTERN - FLORENCIA T. DUQUE COLLEGE                                      | Private              |                 6 |          17.5 |        21.2 |       13.5 |         29 |                    94.5 |    33.3 |    16.7 |           66.7 |                    0 |
| NOVAGEN COLLEGE OF QUEZON CITY                                                        | Private              |                 6 |            14 |        26.7 |        2.8 |       47.8 |                      90 |    33.3 |    33.3 |           16.7 |                    0 |
| LEYTE NORMAL UNIVERSITY TACLOBAN CITY                                                 | Public               |                 6 |            16 |        23.2 |          6 |       39.5 |                    96.5 |    33.3 |    33.3 |              0 |                 33.3 |
| RUNGSIT UNIVERSITY                                                                    | Foreign              |                 6 |          44.5 |        45.5 |          3 |         89 |                     107 |      60 |      60 |           33.3 |                 14.3 |
| UNIVERSITY OF MARYLAND - MARYLAND U.S.A.                                              | Foreign              |                 6 |          55.5 |        58.3 |       35.8 |       84.2 |                     138 |    83.3 |    66.7 |           33.3 |                 16.7 |
| OUR LADY OF FATIMA NOVALICHES                                                         | Private              |                 6 |          18.5 |        28.8 |       12.8 |       44.5 |                    98.5 |    33.3 |    33.3 |           33.3 |                   50 |
| PHILIPPINE NORMAL UNIVERSITY - AGUSAN                                                 | Public               |                 6 |            39 |        44.8 |       28.2 |       55.8 |                     114 |    66.7 |      50 |           33.3 |                    0 |
| MAHARDIKA INSTITUTE OF TECHNOLOGY                                                     | Private              |                 6 |            58 |        50.5 |       32.5 |       69.2 |                     129 |    66.7 |    66.7 |           33.3 |                    0 |
| KASETSART UNIVERSITY                                                                  | Foreign              |                 6 |            15 |        36.2 |         15 |         57 |                   107.5 |      40 |      40 |           66.7 |                   25 |
| UNIVERSITY OF THE IMMACULATE CONCEPTION COLLEGE DAVAO                                 | Private              |                 6 |             6 |        18.5 |        3.5 |         16 |                    81.5 |    16.7 |    16.7 |             50 |                 33.3 |
| EAST AFRICA UNIVERSITY                                                                | Foreign              |                 6 |          78.5 |        64.2 |         57 |         85 |                   143.5 |    83.3 |    83.3 |           33.3 |                    0 |
| COLEGIO DE SAN LORENZO                                                                | Private              |                 6 |            80 |        71.2 |         77 |         86 |                   156.5 |    83.3 |    83.3 |             50 |                   50 |
| ADVENTIST INDONESIA UNIVERSITY INDONESIA                                              | Foreign              |                 5 |            17 |        13.2 |          7 |         17 |                      93 |       0 |       0 |              0 |                    0 |
| AKLAN POLYTECHNIC COLLEGE                                                             | Private              |                 5 |            54 |          49 |         11 |         87 |                     133 |      60 |      60 |             40 |                   50 |
| AMA SCHOOL OF MEDICINE - EAST RIZAL                                                   | Private              |                 5 |            38 |        46.8 |          6 |         91 |                     117 |      60 |      40 |             60 |                   25 |
| SIENA COLLEGE-TAYTAY                                                                  | Private              |                 5 |            31 |        37.4 |         16 |         47 |                     112 |      60 |      40 |             60 |                   60 |
| SIAM UNIVERSITY                                                                       | Foreign              |                 5 |             8 |        32.8 |          6 |         59 |                      90 |      40 |      40 |             20 |                    0 |
| UNIV. OF ASIA AND THE PACIFIC - PASIG CITY                                            | Private              |                 5 |            81 |        64.6 |         36 |         82 |                     159 |      80 |      60 |             60 |                   40 |
| SRI CHAITANYA JUNIOR COLLEGE                                                          | Foreign              |                 5 |            59 |        51.8 |         38 |         77 |                     116 |      80 |      60 |             20 |                  nan |
| ST. ANDREW'S INTERNATIONAL ACADEMY INDIA                                              | Foreign              |                 5 |             9 |        17.8 |          7 |         21 |                      89 |      20 |      20 |             20 |                    0 |
| TEMPLE UNIVERSITY USA                                                                 | Foreign              |                 5 |            69 |        60.6 |         56 |         78 |                     143 |      80 |      80 |             20 |                   60 |
| SUNRISE UNIVERSITY                                                                    | Foreign              |                 5 |            40 |        41.6 |         35 |         52 |                     120 |      80 |      60 |             40 |                  nan |
| TRACE COLLEGE                                                                         | Private              |                 5 |            73 |        54.4 |         24 |         76 |                     131 |      60 |      60 |             80 |                   50 |
| TECHNOLOGICAL UNIVERSITY OF THE PHILIPPINES - AYALA BLVD. MANILA                      | Public               |                 5 |          44.5 |        38.5 |       32.2 |       50.8 |                     126 |      75 |      75 |             40 |                  100 |
| Sti - College Davao                                                                   | Not Specified        |                 5 |            15 |        22.2 |          8 |         41 |                      92 |      40 |      40 |            100 |                   20 |
| RUTGERS COLLEGE NEW JERSEY                                                            | Foreign              |                 5 |            90 |        85.6 |         86 |         92 |                     168 |     100 |     100 |              0 |                   40 |
| UNIVERSITY OF BRITISH COLUMBIA CANADA                                                 | Foreign              |                 5 |            96 |          89 |         94 |         99 |                     184 |     100 |     100 |              0 |                   20 |
| RAMKHAMHAENG UNIV.                                                                    | Foreign              |                 5 |             2 |         3.6 |          1 |          7 |                      75 |       0 |       0 |              0 |                    0 |
| SAINT MICHAEL'S COLLEGE OF LAGUNA                                                     | Private              |                 5 |            58 |          60 |         49 |         85 |                     125 |      80 |      80 |             40 |                   25 |
| PAMANTASAN NG LUNGSOD NG MUNTINLUPA                                                   | Public               |                 5 |            60 |        51.2 |         27 |         70 |                     126 |      60 |      60 |             40 |                  nan |
| UNIVERSITY OF CONNECTICUT                                                             | Foreign              |                 5 |            48 |          56 |         46 |         79 |                     114 |      80 |      80 |             40 |                   50 |
| LUNA GOCO COLLEGES                                                                    | Private              |                 5 |            69 |        55.6 |         32 |         80 |                     136 |      80 |      60 |              0 |                  nan |
| LIPA CITY COLLEGES BATANGAS                                                           | Private              |                 5 |            26 |        31.2 |         15 |         34 |                     107 |      40 |      20 |            100 |                   20 |
| MOGADISHU UNIVERSITY                                                                  | Foreign              |                 5 |            55 |        45.6 |         37 |         61 |                     121 |      80 |      60 |             60 |                  nan |
| UNIVERSITY OF NEVADA - RENO                                                           | Foreign              |                 5 |            41 |        48.8 |         23 |       66.8 |                     131 |      50 |      50 |             20 |                   50 |
| UNIVERSITY OF NEW ENGLAND                                                             | Foreign              |                 5 |            44 |        41.4 |         14 |         52 |                     119 |      60 |      60 |             60 |                    0 |
| UNIVERSITY OF NORTHERN PHILIPPINES-CANDON - CITY OF CANDON ILOCOS SUR                 | Public               |                 5 |            16 |        21.8 |          5 |         18 |                      86 |      25 |      25 |             60 |                    0 |
| NEW YORK UNIVERSITY NY USA                                                            | Foreign              |                 5 |            88 |        87.2 |         84 |         93 |                     161 |     100 |     100 |             20 |                   40 |
| NEW SINAI SCHOOL AND COLLEGES STA. ROSA                                               | Private              |                 5 |          34.5 |          36 |       28.5 |         42 |                     109 |      75 |      25 |             20 |                  nan |
| UNIVERSITY OF MICHIGAN                                                                | Foreign              |                 5 |            77 |        70.4 |         68 |         78 |                     150 |     100 |     100 |             20 |                    0 |
| Qiqihar Medical University                                                            | Not Specified        |                 5 |            11 |        10.4 |          2 |         17 |                      89 |       0 |       0 |            100 |                    0 |
| UNIVERSITY OF CALOOCAN CITY                                                           | Public               |                 5 |            33 |        51.8 |         30 |         81 |                     105 |      80 |      40 |             40 |                   25 |
| PAMPANGA AGRICULTURAL COLLEGE                                                         | Public               |                 5 |          20.5 |        23.2 |        8.5 |       35.2 |                     101 |      50 |      25 |             20 |                    0 |
| PENSACOLA CHRISTIAN COLLEGE                                                           | Foreign              |                 5 |            34 |          51 |         17 |         95 |                     102 |      60 |      40 |             80 |                  100 |
| PALAWAN POLYTECHNIC COLLEGE                                                           | Private              |                 5 |            65 |        56.8 |         60 |         70 |                     139 |      80 |      80 |             40 |                    0 |
| EULOGIO AMANG RODRIGUEZ INSTITUTE OF SCIENCE AND TECHNOLOGY                           | Public               |                 5 |          60.5 |          53 |       39.8 |       73.8 |                     131 |      75 |      75 |              0 |                  nan |
| FEU - FERN COLLEGE                                                                    | Private              |                 5 |            40 |          42 |         14 |         68 |                     108 |      60 |      60 |             40 |                   50 |
| UNIVERSITY OF TEXAS AT ARLINGTON                                                      | Foreign              |                 5 |            14 |        33.4 |          5 |         54 |                      94 |      40 |      40 |              0 |                    0 |
| FL VARGAS COLLEGE - TUGUEGARAO                                                        | Private              |                 5 |            22 |        37.4 |         18 |         53 |                     100 |      40 |      40 |             60 |                    0 |
| DR. DOMINGO B. TAMONDONG MEMORIAL SCHOOL                                              | Private              |                 5 |            37 |        49.4 |         28 |         74 |                     117 |      60 |      40 |             80 |                 33.3 |
| EASTERN VISAYAS STATE UNIVERSITY                                                      | Public               |                 5 |            40 |          54 |         21 |         97 |                     109 |      60 |      60 |             40 |                  100 |
| KITASATO UNIVERSITY                                                                   | Foreign              |                 5 |            55 |          65 |         52 |         86 |                     127 |     100 |      80 |             60 |                  nan |
| KHON KAEN UNIVERSITY THAILAND                                                         | Foreign              |                 5 |            20 |        19.6 |         19 |         27 |                     103 |      20 |       0 |             60 |                    0 |
| CHAING MAI UNIVERSITY-THAILAND                                                        | Foreign              |                 5 |            15 |        19.2 |          9 |         23 |                      86 |      25 |      25 |             60 |                    0 |
| COLEGIO DE SAN JUAN DE LETRAN MANILA                                                  | Private              |                 5 |            41 |        41.8 |         22 |         53 |                     121 |      60 |      60 |             20 |                   60 |
| CAVITE STATE UNIVERSITY CAVITE                                                        | Public               |                 5 |            52 |        57.4 |         37 |         76 |                     125 |      80 |      60 |             20 |                   40 |
| CENTRAL COLLEGE OF PANGASINAN - SAN CARLOS CITY PANGASINAN                            | Private              |                 5 |            47 |        54.6 |         38 |         74 |                     135 |     100 |      60 |             40 |                   60 |
| CAGAYAN DE ORO COLLEGE                                                                | Private              |                 5 |            34 |        36.2 |          2 |         66 |                     104 |      60 |      40 |             40 |                 33.3 |
| BATANGAS STATE UNIVERSITY BATANGAS CITY                                               | Public               |                 5 |            45 |          51 |         25 |         63 |                     124 |      60 |      60 |              0 |                   80 |
| ARIZONA STATE UNIVERSITY                                                              | Foreign              |                 5 |            77 |        66.6 |         67 |         81 |                     143 |      80 |      80 |             60 |                  100 |
| ASIAN COLLEGE OF SCIENCE AND TECHNOLOGY - CUBAO                                       | Private              |                 5 |            69 |        67.2 |         46 |         87 |                     125 |     100 |     100 |             80 |                   50 |
| UNIVERSITY OF WISCONSIN-MADISON                                                       | Foreign              |                 5 |            92 |        84.6 |         72 |         99 |                     171 |     100 |     100 |              0 |                   50 |
| 13206A                                                                                | Not Specified        |                 5 |            54 |        59.8 |         44 |         77 |                     132 |     100 |     100 |             20 |                   20 |

**Table E2. Per-HEI percentile bin distribution (full)**

| UNDERGRAD_UNIVERSITY                                                                  | UNDERGRAD_UNI_TYPE   |     N |   B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |   B9 |   B10 |
|:--------------------------------------------------------------------------------------|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| UNIVERSITY OF SANTO TOMAS                                                             | Private              | 18038 | 1510 | 1134 | 1240 | 1530 | 1677 | 1882 | 1953 | 2199 | 2369 |  2203 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA                                             | Private              |  4528 |  615 |  463 |  391 |  445 |  402 |  465 |  394 |  398 |  396 |   433 |
| FAR EASTERN UNIVERSITY                                                                | Private              |  4309 |  508 |  435 |  417 |  437 |  486 |  427 |  384 |  375 |  345 |   401 |
| SAN PEDRO COLLEGE                                                                     | Private              |  3644 |  437 |  378 |  326 |  308 |  340 |  370 |  342 |  344 |  322 |   379 |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                                | Public               |  3629 |  225 |  179 |  175 |  161 |  200 |  203 |  234 |  286 |  500 |  1339 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                               | Public               |  3238 |  225 |  169 |  140 |  187 |  194 |  188 |  189 |  268 |  418 |  1176 |
| SAINT LOUIS UNIVERSITY                                                                | Private              |  3221 |  367 |  263 |  249 |  337 |  298 |  348 |  320 |  286 |  299 |   376 |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                             | Public               |  2458 |  370 |  233 |  241 |  237 |  223 |  256 |  210 |  205 |  225 |   194 |
| CEBU DOCTOR'S UNIVERSITY                                                              | Private              |  2406 |  290 |  224 |  217 |  239 |  232 |  227 |  220 |  234 |  205 |   247 |
| DE LA SALLE UNIVERSITY - MANILA                                                       | Private              |  2242 |  175 |  139 |  147 |  152 |  199 |  193 |  257 |  303 |  298 |   335 |
| OUR LADY OF FATIMA UNIVERSITY (FATIMA MEDICAL SCIENCE FOUNDATION) - VALENZUELA        | Private              |  2041 |  277 |  232 |  186 |  201 |  189 |  174 |  170 |  191 |  170 |   199 |
| CENTRO ESCOLAR UNIVERSITY - MANILA                                                    | Private              |  2022 |  244 |  203 |  171 |  210 |  202 |  194 |  165 |  173 |  182 |   219 |
| SOUTHWESTERN UNIVERSITY                                                               | Private              |  1841 |  271 |  183 |  152 |  177 |  165 |  153 |  198 |  161 |  167 |   163 |
| ATENEO DE MANILA UNIVERSITY - QUEZON CITY                                             | Private              |  1782 |  165 |  125 |  106 |  144 |  127 |  147 |  128 |  159 |  229 |   396 |
| VELEZ COLLEGE                                                                         | Private              |  1750 |  194 |  155 |  161 |  163 |  132 |  163 |  173 |  152 |  183 |   218 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS                                                   | Private              |  1724 |  225 |  156 |  125 |  153 |  180 |  152 |  170 |  171 |  154 |   189 |
| DAVAO MEDICAL SCHOOL FOUNDATION                                                       | Private              |  1665 |  224 |  160 |  155 |  173 |  145 |  149 |  153 |  131 |  153 |   177 |
| EMILIO AGUINALDO COLLEGE                                                              | Private              |  1577 |  202 |  185 |  154 |  154 |  157 |  154 |  129 |  132 |  121 |   153 |
| AMA COMPUTER COLLEGE - MAKATI                                                         | Private              |  1519 |  247 |  177 |  152 |  127 |  139 |  145 |  119 |  135 |  125 |   117 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                         | Public               |  1386 |  219 |  140 |  113 |  130 |  112 |  130 |  111 |  126 |  127 |   135 |
| ANGELES UNIVERSITY FOUNDATION                                                         | Private              |  1337 |  165 |  140 |  105 |  131 |  141 |  148 |  122 |  118 |  107 |   134 |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                             | Public               |  1321 |  151 |  100 |  100 |   96 |  101 |  115 |  139 |  143 |  163 |   171 |
| SILLIMAN UNIVERSITY                                                                   | Private              |  1303 |  139 |  130 |  106 |  113 |  141 |  132 |  127 |  123 |  117 |   141 |
| AGO MEDICAL AND EDUCATIONAL CENTER - BICOL CHRISTIAN COLLEGE OF MEDICINE              | Private              |  1284 |  225 |  146 |  132 |  141 |  121 |  119 |   79 |  107 |   89 |    99 |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                  | Public               |  1245 |  129 |  100 |   99 |  111 |  109 |  129 |  123 |  108 |  130 |   187 |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                      | Public               |  1238 |  116 |   78 |  108 |  121 |  159 |  155 |  135 |  124 |  111 |   105 |
| XAVIER UNIVERSITY                                                                     | Private              |  1228 |  151 |  100 |  102 |  118 |  123 |  104 |  125 |  125 |  110 |   138 |
| BROKENSHIRE COLLEGE                                                                   | Private              |  1226 |  190 |  111 |   95 |  115 |  119 |  110 |  103 |  118 |   97 |   119 |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                            | Public               |  1185 |  131 |  108 |  118 |  118 |  112 |  104 |  109 |  112 |  110 |   135 |
| ATENEO DE ZAMBOANGA UNIVERSITY                                                        | Private              |  1172 |  172 |  130 |  111 |  115 |  104 |  123 |   96 |   99 |  100 |   102 |
| FEU - DR. NICANOR REYES MEDICAL FOUNDATION                                            | Private              |  1151 |  145 |   81 |  101 |  101 |  109 |  116 |  119 |  112 |  111 |   122 |
| LYCEUM NORTHWESTERN UNIVERSITY                                                        | Private              |  1048 |  176 |  113 |   87 |  100 |   98 |   97 |   89 |   78 |   91 |    96 |
| MINDANAO STATE UNIVERSITY - MARAWI                                                    | Public               |  1005 |  121 |   97 |   80 |   77 |  102 |  107 |   96 |   87 |  102 |   115 |
| UNIVERSITY OF SAN AGUSTIN                                                             | Private              |   995 |  112 |  115 |   88 |   92 |  100 |   91 |   74 |   99 |   92 |   102 |
| ATENEO DE DAVAO UNIVERSITY                                                            | Private              |   981 |   83 |   95 |   94 |   88 |  101 |   96 |   95 |   96 |   98 |   117 |
| DE LA SALLE HEALTH SCIENCES INSTITUTE                                                 | Private              |   952 |  100 |   90 |   91 |  110 |   74 |   87 |   97 |   82 |   99 |    96 |
| TRINITY UNIVERSITY OF ASIA                                                            | Private              |   897 |   84 |   73 |   67 |   98 |   77 |   84 |   90 |  116 |  101 |    91 |
| WESTERN MINDANAO STATE UNIVERSITY                                                     | Public               |   863 |  109 |   94 |   55 |   85 |   86 |   86 |   79 |   59 |   84 |   103 |
| MANILA CENTRAL UNIVERSITY                                                             | Private              |   837 |  115 |  105 |   84 |   85 |   83 |   83 |   70 |   66 |   60 |    66 |
| ATENEO DE MANILA UNIVERSITY                                                           | Private              |   751 |    0 |    0 |    1 |    3 |    9 |   21 |   38 |   75 |  243 |   354 |
| BICOL UNIVERSITY - MAIN                                                               | Public               |   740 |   81 |   71 |   65 |   64 |   64 |   58 |   67 |   86 |   75 |    95 |
| CENTRAL PHILIPPINE UNIVERSITY                                                         | Private              |   697 |   71 |   75 |   65 |   63 |   72 |   76 |   59 |   49 |   56 |    89 |
| VIRGEN MILAGROSA UNIVERSITY FOUNDATION AND VMU INSTITUTE OF MEDICAL FOUNDATION        | Private              |   697 |   99 |   67 |   53 |   69 |   72 |   74 |   62 |   61 |   49 |    64 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                                | Public               |   693 |   65 |   57 |   49 |   53 |   59 |   59 |   60 |   89 |   67 |   113 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                               | Public               |   674 |   92 |   63 |   53 |   57 |   56 |   50 |   66 |   79 |   53 |    88 |
| ADVENTIST UNIVERSITY OF THE PHILIPPINES                                               | Private              |   672 |   83 |   64 |   56 |   52 |   65 |   65 |   68 |   64 |   72 |    68 |
| SAINT PAUL UNIVERSITY PHILIPPINES                                                     | Private              |   662 |   88 |   73 |   49 |   59 |   71 |   74 |   56 |   51 |   57 |    65 |
| UNIVERSITY OF ST. LA SALLE                                                            | Private              |   629 |   61 |   50 |   49 |   60 |   58 |   65 |   65 |   67 |   61 |    85 |
| UNIVERSITY OF THE IMMACULATE CONCEPTION                                               | Private              |   601 |   96 |   54 |   56 |   65 |   57 |   47 |   56 |   50 |   52 |    54 |
| VELEZ COLLEGE CEBU                                                                    | Private              |   559 |   29 |   35 |   53 |   81 |   71 |   68 |   63 |   65 |   54 |    40 |
| UNIVERSITY OF THE EAST RAMON MAGSAYSAY MEMORIAL MEDICAL CENTER                        | Private              |   555 |   41 |   45 |   50 |   55 |   57 |   57 |   58 |   66 |   57 |    59 |
| UNIVERSITY OF SAN CARLOS                                                              | Private              |   551 |   60 |   51 |   59 |   55 |   41 |   53 |   44 |   55 |   58 |    63 |
| SAN BEDA COLLEGE                                                                      | Private              |   530 |   64 |   51 |   62 |   44 |   44 |   52 |   47 |   50 |   52 |    49 |
| NOT SPECIFIED/UNLISTED                                                                | Public               |   513 |   95 |   65 |   56 |   49 |   39 |   51 |   47 |   32 |   37 |    37 |
| SAN PEDRO COLLEGE DAVAO CITY                                                          | Private              |   512 |   68 |   68 |   63 |   70 |   63 |   56 |   46 |   40 |   23 |    14 |
| UNIVERSITY OF THE PHILIPPINES - LOS BANOS LAGUNA                                      | Public               |   487 |    0 |    3 |    0 |   12 |   22 |   42 |   65 |   90 |  113 |   137 |
| MANILA TYTANA COLLEGES                                                                | Private              |   485 |   55 |   46 |   47 |   52 |   54 |   42 |   44 |   49 |   39 |    45 |
| ANGELES UNIVERSITY FOUNDATION ANGELES CITY                                            | Private              |   481 |   52 |   71 |   80 |   79 |   63 |   35 |   29 |   36 |   25 |    11 |
| CENTRO ESCOLAR UNIVERSITY - MAKATI                                                    | Private              |   472 |   60 |   50 |   29 |   49 |   45 |   45 |   35 |   42 |   50 |    55 |
| DOÑA REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION                                   | Private              |   468 |   56 |   47 |   42 |   46 |   49 |   39 |   52 |   44 |   45 |    37 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS CAVITE                                            | Private              |   456 |   58 |   57 |   74 |   69 |   62 |   44 |   35 |   28 |   23 |     6 |
| DAVAO DOCTORS COLLEGE                                                                 | Private              |   444 |   78 |   60 |   46 |   48 |   42 |   33 |   38 |   30 |   30 |    31 |
| LICEO DE CAGAYAN UNIVERSITY                                                           | Private              |   428 |   60 |   65 |   36 |   55 |   44 |   31 |   29 |   38 |   33 |    29 |
| FAR EASTERN UNIVERSITY - NRMF (FAIRVIEW Q.C.)                                         | Private              |   427 |   55 |   60 |   69 |   71 |   55 |   46 |   37 |   20 |    9 |     5 |
| OUR LADY OF FATIMA UNIVERSITY - QUEZON CITY                                           | Private              |   423 |   40 |   60 |   50 |   36 |   42 |   30 |   36 |   35 |   34 |    47 |
| MINDANAO SANITARIUM AND HOSPITAL COLLEGE                                              | Private              |   393 |   55 |   36 |   36 |   33 |   47 |   39 |   32 |   34 |   28 |    39 |
| CENTRO ESCOLAR UNIVERSITY - MENDIOLA MANILA                                           | Private              |   382 |   73 |   68 |   57 |   51 |   42 |   33 |   29 |   12 |   13 |     3 |
| SAINT LOUIS UNIVERSITY - BAGUIO                                                       | Private              |   380 |   14 |   35 |   53 |   58 |   51 |   50 |   43 |   33 |   28 |    15 |
| DE LA SALLE - LIPA                                                                    | Private              |   365 |   54 |   27 |   39 |   43 |   38 |   29 |   23 |   36 |   36 |    35 |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                              | Public               |   363 |   27 |   19 |   23 |   29 |   24 |   30 |   46 |   38 |   50 |    67 |
| WEST VISAYAS STATE UNIVERSITY ILOILO                                                  | Public               |   360 |   13 |   26 |   31 |   31 |   46 |   35 |   67 |   45 |   35 |    31 |
| CEBU NORMAL UNIVERSITY                                                                | Public               |   356 |   20 |   20 |   25 |   29 |   29 |   34 |   53 |   46 |   55 |    39 |
| UNIVERSITY OF THE EAST - MANILA                                                       | Private              |   352 |   47 |   22 |   31 |   33 |   24 |   26 |   36 |   47 |   36 |    41 |
| XAVIER UNIVERSITY CAGAYAN DE ORO CITY                                                 | Private              |   349 |   12 |   30 |   30 |   48 |   35 |   60 |   49 |   34 |   26 |    25 |
| UNIVERSITY OF BAGUIO                                                                  | Private              |   346 |   43 |   33 |   28 |   39 |   21 |   39 |   27 |   35 |   31 |    47 |
| MINDANAO STATE UNIVERSITY MARAWI CITY                                                 | Public               |   344 |   33 |   43 |   52 |   51 |   41 |   30 |   33 |   27 |   24 |    10 |
| CENTRAL MINDANAO UNIVERSITY                                                           | Public               |   327 |   47 |   25 |   28 |   31 |   24 |   33 |   40 |   27 |   31 |    31 |
| UNIVERSIDAD DE ZAMBOANGA                                                              | Private              |   323 |   49 |   32 |   29 |   28 |   27 |   27 |   42 |   22 |   32 |    28 |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                                | Public               |   313 |   41 |   38 |   21 |   26 |   25 |   26 |   34 |   36 |   25 |    35 |
| UNIVERSITY OF THE CORDILLERAS                                                         | Private              |   310 |   55 |   29 |   25 |   25 |   34 |   36 |   20 |   42 |   18 |    19 |
| ST. PAUL UNIVERSITY ILOILO                                                            | Private              |   305 |   24 |   20 |   25 |   35 |   26 |   36 |   34 |   25 |   31 |    39 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                             | Public               |   304 |   39 |   31 |   20 |   31 |   26 |   32 |   29 |   26 |   31 |    33 |
| ILOILO DOCTORS COLLEGE                                                                | Private              |   303 |   45 |   31 |   39 |   32 |   23 |   30 |   19 |   28 |   23 |    27 |
| UNIVERSIDAD DE STA. ISABEL                                                            | Private              |   302 |   26 |   29 |   31 |   27 |   32 |   28 |   31 |   29 |   30 |    33 |
| RIVERSIDE COLLEGE                                                                     | Private              |   301 |   39 |   39 |   19 |   26 |   35 |   28 |   18 |   29 |   31 |    31 |
| MOUNTAIN VIEW COLLEGE                                                                 | Private              |   294 |   39 |   28 |   28 |   28 |   23 |   33 |   27 |   19 |   25 |    31 |
| NOTRE DAME UNIVERSITY                                                                 | Private              |   277 |   50 |   23 |   24 |   27 |   26 |   31 |   17 |   18 |   20 |    33 |
| UNIVERSITY OF NEGROS OCCIDENTAL-RECOLETOS                                             | Private              |   277 |   32 |   31 |   20 |   24 |   20 |   30 |   26 |   34 |   32 |    23 |
| MIRIAM COLLEGE                                                                        | Private              |   257 |   30 |   30 |   14 |   22 |   33 |   21 |   24 |   22 |   27 |    26 |
| UNIVERSITY OF THE VISAYAS                                                             | Private              |   254 |   51 |   20 |   25 |   32 |   28 |   21 |   15 |   20 |   19 |    13 |
| PALAWAN STATE UNIVERSITY                                                              | Public               |   253 |   29 |   25 |   19 |   33 |   19 |   30 |   26 |   22 |   24 |    18 |
| ATENEO DE NAGA UNIVERSITY                                                             | Private              |   253 |   31 |   23 |   21 |   30 |   32 |   21 |   21 |   24 |   17 |    25 |
| SAINT SCHOLASTICA'S COLLEGE TACLOBAN                                                  | Private              |   250 |   27 |   29 |   24 |   23 |   22 |   28 |   22 |   22 |   19 |    25 |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES                                              | Private              |   250 |   26 |   29 |   15 |   30 |   28 |   26 |   21 |   23 |   16 |    29 |
| LYCEUM OF THE PHILIPPINES UNIVERSITY - BATANGAS                                       | Private              |   249 |   43 |   31 |   22 |   14 |   19 |   27 |   28 |   21 |   19 |    22 |
| OUR LADY OF FATIMA UNIVERSITY VALENZUELA CITY                                         | Private              |   247 |   56 |   40 |   38 |   28 |   27 |   18 |   13 |   11 |   14 |     2 |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                       | Public               |   244 |   26 |   17 |   13 |   19 |   27 |   28 |   21 |   27 |   27 |    33 |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                    | Public               |   241 |   36 |   23 |   22 |   16 |   20 |   22 |   17 |   22 |   29 |    25 |
| LORMA COLLEGES                                                                        | Private              |   233 |   19 |   27 |   20 |   26 |   22 |   32 |   25 |   22 |   17 |    20 |
| SILLIMAN UNIVERSITY DUMAGUETE CITY                                                    | Private              |   227 |    8 |   14 |   17 |   27 |   38 |   24 |   28 |   27 |   23 |    21 |
| SAINT MARY'S UNIVERSITY                                                               | Private              |   219 |   34 |   19 |   19 |   15 |   22 |   24 |   20 |   20 |   19 |    22 |
| CAPITOL MEDICAL CENTER COLLEGES                                                       | Private              |   217 |   26 |   27 |   25 |   17 |   32 |   14 |   15 |   18 |   15 |    27 |
| ST. LOUIS UNIVERSITY BAGUIO CITY                                                      | Private              |   208 |    7 |   15 |   22 |   26 |   29 |   33 |   24 |   25 |   16 |    11 |
| MINDANAO STATE UNIVERSITY ILIGAN CITY                                                 | Public               |   203 |    7 |   13 |   19 |   17 |   36 |   28 |   26 |   20 |   22 |    15 |
| ARELLANO UNIVERSITY - MANILA                                                          | Private              |   203 |   24 |   19 |   15 |   20 |   21 |   18 |   22 |   18 |   14 |    26 |
| BULACAN STATE UNIVERSITY - MAIN                                                       | Public               |   201 |   23 |   18 |   19 |   16 |   15 |   24 |   12 |   24 |   18 |    24 |
| NOTRE DAME OF DADIANGAS UNIVERSITY                                                    | Private              |   198 |   27 |   24 |   10 |   24 |   21 |   11 |   23 |   20 |   11 |    22 |
| COLEGIO SAN AGUSTIN - BACOLOD                                                         | Private              |   198 |   22 |   21 |   23 |   22 |   18 |   19 |   18 |   14 |   14 |    26 |
| PERPETUAL HELP COLLEGE OF MANILA                                                      | Private              |   197 |   36 |   28 |   20 |   17 |   17 |   18 |   19 |   18 |    9 |    13 |
| UNIVERSITY OF PERPETUAL HELP - DR. JOSE G. TAMAYO MEDICAL UNIVERSITY                  | Private              |   196 |   16 |   21 |   23 |   15 |   18 |   27 |   20 |   15 |   22 |    17 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO CITY                                           | Public               |   195 |    0 |    1 |    4 |   15 |   20 |   22 |   39 |   34 |   40 |    20 |
| SOUTHWESTERN UNIVERSITY CEBU                                                          | Private              |   191 |   50 |   33 |   29 |   23 |   19 |   15 |   10 |    6 |    4 |     2 |
| MAKATI MEDICAL CENTER COLLEGE OF NURSING                                              | Private              |   191 |   23 |   21 |   16 |   15 |   25 |   21 |   21 |   17 |   17 |    12 |
| NOTRE DAME OF MARBEL UNIVERSITY                                                       | Private              |   186 |   25 |   20 |   19 |   20 |   12 |   15 |   19 |   17 |   15 |    22 |
| ADAMSON UNIVERSITY                                                                    | Private              |   184 |   27 |   20 |   14 |   16 |   13 |   20 |   23 |   12 |   15 |    18 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS ILOILO                                        | Public               |   182 |    1 |    0 |    6 |    5 |   15 |   21 |   27 |   31 |   33 |    43 |
| OUR LADY OF FATIMA UNIVERSITY - ANTIPOLO                                              | Private              |   175 |   23 |   18 |   16 |   18 |   22 |   21 |   18 |    9 |   13 |    14 |
| SAN BEDA COLLEGE MENDIOLA MANILA                                                      | Private              |   175 |   18 |   28 |   22 |   42 |   19 |   15 |    9 |    9 |    8 |     5 |
| NEW ERA UNIVERSITY                                                                    | Private              |   171 |   23 |   17 |   13 |   23 |   11 |   15 |   15 |   15 |   15 |    20 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                         | Public               |   171 |   14 |   10 |   13 |   15 |   19 |   20 |   12 |   17 |   16 |    28 |
| HOLY NAME UNIVERSITY                                                                  | Private              |   159 |   20 |   12 |   20 |   10 |   21 |    8 |   12 |   11 |   18 |    25 |
| ST. PAUL UNIVERSITY - MANILA (ST. PAUL UNIVERITY SYSTEM)                              | Private              |   159 |   14 |   15 |   12 |   16 |   17 |   26 |    7 |   16 |    9 |    26 |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                            | Public               |   158 |   26 |   10 |    9 |   15 |   17 |   12 |    9 |   18 |   19 |    19 |
| UNIVERSITY OF SAN CARLOS CEBU CITY                                                    | Private              |   158 |   13 |   15 |   26 |   19 |   20 |   19 |   10 |   11 |   19 |     6 |
| ST. SCHOLASTICA'S COLLEGE                                                             | Private              |   158 |   29 |   18 |   17 |   18 |   13 |   10 |   17 |   15 |    8 |    12 |
| PINES CITY COLLEGES                                                                   | Private              |   154 |   17 |   12 |   20 |   22 |   18 |   13 |   12 |   11 |   11 |    14 |
| UNIVERSITY OF LA SALETTE                                                              | Private              |   152 |   14 |   10 |   17 |   15 |   14 |   13 |   15 |   11 |   15 |    24 |
| SOUTHVILLE INTERNATIONAL SCHOOL AND COLLEGES                                          | Private              |   151 |   12 |    8 |   22 |   18 |   15 |   21 |   17 |   20 |    6 |    11 |
| UNIVERSITY OF ST. LOUIS - TUGUEGARAO                                                  | Private              |   150 |   22 |   12 |   13 |    7 |   13 |   12 |   15 |   11 |   21 |    20 |
| CEBU DOCTORS COLLEGE CEBU CITY                                                        | Private              |   148 |   21 |   27 |   27 |   18 |   19 |    9 |   12 |    7 |    5 |     3 |
| AQUINAS UNIVERSITY OF LEGAZPI                                                         | Private              |   146 |   15 |    8 |   15 |   21 |   24 |   13 |   13 |   11 |    8 |    13 |
| WESTERN MINDANAO STATE UNIVERSITY ZAMBOANGA CITY                                      | Public               |   145 |   25 |   27 |   23 |   21 |   19 |   12 |   13 |    3 |    1 |     1 |
| MINDANAO MEDICAL FOUNDATION COLLEGE                                                   | Private              |   143 |   11 |   14 |   17 |   10 |   12 |   14 |   18 |   17 |   17 |    10 |
| UNIVERSITY OF THE EAST (C.M. RECTO MANILA)                                            | Private              |   143 |    8 |   10 |   15 |   18 |   15 |   18 |   24 |   18 |    6 |    11 |
| BENGUET STATE UNIVERSITY - MAIN                                                       | Public               |   142 |   15 |    9 |    9 |   16 |   13 |   23 |   13 |    7 |   13 |    22 |
| UNIVERSITY OF CEBU - BANILAD                                                          | Private              |   140 |   21 |   14 |   19 |    8 |   18 |    7 |   15 |   10 |   16 |    10 |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                    | Public               |   140 |   14 |   28 |    8 |   14 |   15 |    8 |   10 |   15 |   14 |    13 |
| CENTRAL LUZON STATE UNIVERSITY                                                        | Public               |   140 |   16 |   18 |   16 |   11 |   13 |   10 |    8 |   13 |   14 |    18 |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                                | Public               |   138 |   16 |   18 |   11 |   15 |    9 |    8 |   12 |   17 |   12 |    18 |
| DE LA SALLE - HEALTH SCIENCES CAMPUS                                                  | Private              |   136 |    6 |   20 |   18 |   25 |   19 |   17 |   12 |    8 |    8 |     3 |
| MISAMIS UNIVERSITY - OZAMIS CITY                                                      | Private              |   132 |   18 |   16 |   13 |   11 |   15 |   11 |    7 |   12 |   14 |    12 |
| REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION TACLOBAN                               | Private              |   130 |   14 |   16 |   19 |   16 |   20 |   13 |   11 |   10 |    4 |     7 |
| ST. PAUL UNIVERSITY - QUEZON CITY                                                     | Private              |   129 |   17 |   19 |   17 |   16 |    9 |   12 |   11 |   11 |    7 |     8 |
| UNIVERSITY OF SAN AGUSTIN - ILOILO CITY                                               | Private              |   124 |   10 |   21 |   15 |   16 |   10 |   17 |   14 |    8 |    6 |     6 |
| GENERAL SANTOS DOCTORS' MEDICAL SCHOOL FOUNDATION                                     | Private              |   122 |    9 |   19 |   12 |   11 |    9 |   14 |    9 |    9 |   15 |    12 |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                                | Public               |   121 |   14 |    6 |   11 |   18 |    9 |   16 |    9 |    9 |   10 |    14 |
| COLEGIO DE SAN JUAN DE LETRAN                                                         | Private              |   121 |    6 |   16 |   15 |   10 |   12 |   10 |    6 |   10 |   16 |    14 |
| UNIVERSITY OF PANGASINAN                                                              | Private              |   119 |   16 |   12 |   12 |   11 |   16 |   13 |   11 |    9 |    9 |     6 |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING AND LIBERAL ARTS                          | Private              |   119 |   11 |   11 |   10 |    8 |   19 |    9 |   10 |    9 |   15 |    14 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                         | Public               |   118 |   12 |   14 |    8 |   10 |   10 |   17 |   13 |   11 |    9 |    10 |
| EMILIO AGUINALDO COLLEGE MANILA                                                       | Private              |   117 |   20 |   26 |   17 |   14 |   11 |   13 |    6 |    2 |    6 |     2 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION                                               | Private              |   117 |   16 |   12 |    9 |   14 |   16 |   10 |   11 |   11 |    8 |     8 |
| DIVINE WORD COLLEGE OF LAOAG                                                          | Private              |   116 |   32 |   24 |   11 |   10 |    9 |   10 |    6 |    8 |    3 |     0 |
| WESLEYAN UNIVERSITY - PHILIPPINES (CABANATUAN)                                        | Private              |   109 |   12 |   14 |   13 |   16 |   10 |    5 |   11 |    8 |   12 |     7 |
| ST. PAUL UNIVERSITY - MANILA                                                          | Private              |   109 |   11 |    8 |   11 |   19 |   17 |    7 |   14 |    9 |    8 |     5 |
| CENTRAL LUZON DOCTORS' HOSPITAL EDUCATIONAL INSTITUTION                               | Private              |   108 |   12 |   10 |    5 |    8 |   12 |   16 |   11 |   10 |   10 |    11 |
| Mariano Marcos State University - College Of Fisheries - Currimao                     | Not Specified        |   108 |    4 |   11 |   10 |   16 |   14 |   21 |    9 |   10 |    6 |     7 |
| UNIVERSITY OF EASTERN PHILIPPINES                                                     | Public               |   107 |   21 |    9 |   14 |    7 |   10 |    8 |    7 |    8 |   12 |     7 |
| UNIVERSITY OF BAGUIO BAGUIO CITY                                                      | Private              |   106 |   27 |   20 |   14 |   13 |    8 |    9 |    7 |    5 |    2 |     1 |
| HOLY ANGEL UNIVERSITY                                                                 | Private              |   105 |   12 |   12 |   11 |   11 |   19 |    7 |    4 |    9 |    4 |    14 |
| CAPITOL UNIVERSITY                                                                    | Private              |   104 |   15 |    9 |   11 |   13 |    7 |    9 |    5 |   12 |   11 |    10 |
| CENTRAL PHILIPPINE UNIVERSITY ILOILO                                                  | Private              |   104 |   14 |    8 |   11 |    8 |   16 |   17 |    9 |    7 |    8 |     6 |
| GLOBAL CITY INNOVATIVE COLLEGE                                                        | Private              |   101 |    9 |   11 |   11 |   16 |   14 |   12 |   10 |    5 |   10 |     2 |
| FEU - EAST ASIA COLLEGE                                                               | Private              |   101 |   12 |   17 |    8 |   10 |    9 |   12 |    8 |    5 |    8 |    12 |
| UNIVERSITY OF ST. LA SALLE BACOLOD CITY                                               | Private              |    99 |    5 |   12 |   11 |   14 |   10 |   14 |   12 |    9 |    6 |     6 |
| ST. JUDE COLLEGE                                                                      | Private              |    95 |   12 |   14 |    9 |    7 |    8 |    8 |    8 |    7 |   11 |     7 |
| FATHER SATURNINO M. URIOS UNIVERSITY                                                  | Private              |    91 |   13 |    7 |    3 |    9 |   10 |   13 |    7 |    8 |   10 |     8 |
| UNIVERSITY OF SOUTHERN PHILIPPINES FOUNDATION                                         | Private              |    89 |   13 |   11 |   13 |    7 |    7 |    6 |    7 |   12 |    3 |    10 |
| SOUTHWESTERN UNIVERSITY-MATIAS H. AZNAR MEMORIAL COLLEGE OF MEDICINE - CEBU CITY CEBU | Private              |    89 |   22 |   11 |   12 |    4 |    8 |    2 |    7 |    4 |    8 |     5 |
| UERM MEMORIAL MEDICAL CENTER                                                          | Private              |    88 |    2 |    6 |   10 |   16 |   14 |   19 |    7 |   10 |    1 |     3 |
| MANILA DOCTORS COLLEGE - PASAY CITY                                                   | Private              |    87 |    6 |    6 |   14 |   13 |   15 |   15 |   10 |    5 |    2 |     1 |
| CENTRO ESCOLAR UNIVERSITY AT MALOLOS                                                  | Private              |    87 |   12 |    4 |    6 |    4 |   10 |    9 |    8 |   10 |   10 |    14 |
| ILIGAN MEDICAL CENTER COLLEGE                                                         | Private              |    86 |   16 |   10 |    4 |    5 |   15 |    7 |    5 |    6 |    5 |     8 |
| COLLEGE OF THE HOLY SPIRIT OF MANILA                                                  | Private              |    83 |   14 |    9 |    5 |   13 |    8 |    8 |    4 |    7 |    6 |     8 |
| HOLY INFANT COLLEGE                                                                   | Private              |    80 |   11 |    4 |   13 |    4 |    7 |    9 |    7 |   12 |    5 |     7 |
| EASTER COLLEGE                                                                        | Private              |    78 |   11 |    5 |    8 |   14 |   12 |    4 |    5 |    6 |    4 |     7 |
| REMEDIOS T. ROMUALDEZ MEM. SCH. - MMC                                                 | Private              |    78 |    5 |    8 |    9 |    6 |    8 |    9 |   14 |    9 |    9 |     1 |
| SOUTHEAST ASIAN COLLEGE                                                               | Private              |    78 |   15 |    9 |    6 |    6 |    9 |    5 |   10 |    6 |    2 |     6 |
| VIRGEN MILAGROSA UNIV. FOUNDATION - SAN CARLOS CITY PANG.                             | Private              |    76 |   14 |   13 |   15 |   11 |    7 |    5 |    2 |    4 |    3 |     0 |
| WORLD CITI COLLEGES QUEZON CITY                                                       | Private              |    76 |    7 |    5 |   10 |    8 |    7 |    4 |    7 |    4 |    9 |    12 |
| DR. CARLOS S. LANTING COLLEGE                                                         | Private              |    76 |   10 |    7 |    8 |   13 |    5 |    5 |    5 |    6 |    6 |     8 |
| THE PHILIPPINE WOMEN'S UNIVERSITY SYSTEM - MANILA                                     | Private              |    75 |    4 |    6 |    5 |   10 |    5 |    7 |    8 |   15 |    6 |     7 |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE                                                  | Private              |    74 |    9 |    8 |    4 |    2 |    9 |    6 |    5 |    7 |    9 |    12 |
| METROPOLITAN HOSPITAL COLLEGE OF NURSING                                              | Private              |    74 |    5 |   11 |    7 |    9 |    6 |    7 |    9 |    4 |    8 |     7 |
| BRENT HOSPITAL AND COLLEGES                                                           | Private              |    73 |   13 |   11 |    6 |    7 |    3 |    4 |    7 |    6 |    8 |     7 |
| CAVITE STATE UNIVERSITY - MAIN                                                        | Public               |    72 |    8 |    7 |    5 |    9 |    6 |    9 |    2 |    6 |    9 |    11 |
| LEYTE NORMAL UNIVERSITY                                                               | Public               |    71 |    8 |    7 |   12 |    7 |    3 |   10 |    7 |    4 |    7 |     3 |
| MANILA ADVENTIST MEDICAL CENTER AND COLLEGES                                          | Private              |    71 |   13 |    4 |    6 |    9 |    6 |    7 |    7 |    8 |    8 |     2 |
| ST. ALEXIUS COLLEGE                                                                   | Private              |    71 |   12 |    7 |    2 |    6 |    4 |    6 |   13 |   10 |    5 |     4 |
| UNIVERSITY OF VISAYAS CEBU                                                            | Private              |    69 |   30 |   11 |    5 |    7 |    5 |    4 |    1 |    1 |    1 |     1 |
| RANGSIT UNIVERSITY                                                                    | Foreign              |    69 |   15 |    7 |    6 |    8 |    2 |    3 |    9 |    2 |    6 |    10 |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-LAS PIÑAS                                   | Private              |    67 |   25 |   13 |    8 |    7 |    3 |    3 |    2 |    0 |    5 |     0 |
| UNIVERSITY OF NUEVA CACERES                                                           | Private              |    67 |   10 |   14 |    2 |    5 |    8 |    7 |    5 |    4 |    4 |     5 |
| NOTRE DAME OF JOLO COLLEGE                                                            | Private              |    65 |   12 |    9 |    5 |    6 |    5 |    5 |    9 |    3 |    6 |     5 |
| LYCEUM NORTHWESTERN DAGUPAN CITY                                                      | Private              |    64 |   22 |   14 |    8 |    2 |    3 |    6 |    4 |    3 |    1 |     1 |
| UNIVERSITY OF THE CORDILLERAS (BCF)                                                   | Private              |    63 |    8 |    6 |   10 |   10 |   12 |    9 |    2 |    2 |    3 |     1 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                                 | Public               |    63 |   22 |   12 |    6 |    6 |    4 |    4 |    3 |    1 |    2 |     0 |
| ASSUMPTION COLLEGE                                                                    | Private              |    62 |    5 |    3 |   12 |    6 |    7 |    6 |    6 |    6 |    2 |     7 |
| LA CONSOLACION COLLEGE - MANILA                                                       | Private              |    62 |    5 |    9 |    5 |    6 |    6 |    9 |    5 |    5 |    7 |     5 |
| DE LA SALLE - LIPA BATANGAS                                                           | Private              |    61 |    2 |   10 |    7 |    5 |    7 |   14 |    6 |    3 |    5 |     2 |
| UNIVERSITY OF THE EAST - RAMON MAGSAYSAY MEM. MEDICAL CENTER                          | Private              |    60 |    0 |    4 |    2 |   10 |    8 |   10 |   12 |    8 |    4 |     2 |
| MANILA DOCTORS COLLEGE U.N. AVENUE MANILA                                             | Private              |    59 |    4 |    9 |    6 |    5 |   16 |    7 |    7 |    4 |    0 |     1 |
| CATANDUANES STATE COLLEGE - MAIN                                                      | Public               |    59 |    7 |    5 |    9 |    6 |    6 |    5 |    4 |    4 |    7 |     6 |
| UNIVERSITY OF SAN JOSE - RECOLETOS                                                    | Private              |    58 |   12 |    5 |    3 |    7 |    6 |    4 |    1 |    5 |    7 |     8 |
| BUTUAN DOCTORS COLLEGE                                                                | Private              |    57 |    8 |    5 |    4 |    5 |   10 |    7 |    4 |    7 |    4 |     3 |
| SACRED HEART COLLEGE OF LUCENA                                                        | Private              |    57 |    7 |    9 |    5 |    4 |    4 |    9 |    8 |    6 |    1 |     4 |
| UNIVERSITY OF MAKATI                                                                  | Public               |    56 |    8 |    7 |    3 |    9 |    8 |    4 |    5 |    5 |    1 |     6 |
| NOTRE DAME UNIVERSITY COTABATO CITY                                                   | Private              |    56 |   15 |    6 |   11 |    4 |    3 |    2 |    3 |    5 |    6 |     1 |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                   | Public               |    56 |    7 |    3 |    2 |    5 |    8 |    2 |    7 |    7 |    6 |     6 |
| DIPOLOG MEDICAL CENTER COLLEGE FOUNDATION                                             | Private              |    55 |    8 |    7 |    3 |    4 |   10 |    3 |    6 |    2 |    3 |     6 |
| ST. PAUL UNIVERSITY DUMAGUETE                                                         | Private              |    55 |   10 |    5 |    3 |    4 |    7 |    5 |    4 |    5 |    3 |     6 |
| OUR LADY OF FATIMA UNIVERSITY - LAGRO QUEZON CITY                                     | Private              |    53 |    7 |    8 |    9 |   11 |    7 |    5 |    2 |    2 |    1 |     1 |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                                            | Public               |    53 |   22 |    6 |    6 |    4 |    3 |    3 |    2 |    3 |    1 |     1 |
| BAGUIO CENTRAL UNIVERSITY                                                             | Private              |    52 |   10 |    5 |    4 |    5 |    4 |    3 |    3 |    6 |    4 |     5 |
| MIRIAM COLLEGE FOUNDATION INC.                                                        | Private              |    52 |    4 |   15 |    1 |    8 |    6 |    5 |    5 |    6 |    2 |     0 |
| SAN LORENZO RUIZ COLLEGE OF ORMOC                                                     | Private              |    51 |   10 |    2 |    6 |    8 |    6 |    3 |    7 |    3 |    3 |     1 |
| NAGA COLLEGE FOUNDATION                                                               | Private              |    50 |    7 |    3 |    4 |    2 |    6 |    0 |    6 |   10 |    3 |     4 |
| MINDANAO SANITARIUM & HOSPITAL COLLEGE ILIGAN CITY                                    | Private              |    50 |   16 |   10 |    6 |    4 |    8 |    4 |    0 |    0 |    2 |     0 |
| SOUTH SEED - LPDH COLLEGE                                                             | Private              |    50 |    4 |    2 |    4 |    8 |    3 |    6 |    8 |    3 |    9 |     2 |
| CEBU DOCTOR'S UNIVERSITY COLLEGE OF MEDICINE - MANDAUE CITY CEBU                      | Private              |    49 |    3 |    6 |    6 |    2 |    7 |    5 |    3 |    3 |    3 |    10 |
| UNIVERSITY OF THE PHILIPPINES - TACLOBAN                                              | Public               |    49 |    1 |    1 |    7 |    1 |    4 |    5 |   10 |    7 |    9 |     4 |
| BICOL UNIVERSITY - TABACO                                                             | Public               |    48 |    8 |    2 |    4 |    9 |    5 |    5 |    3 |    5 |    2 |     5 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION INC.                                          | Private              |    48 |    9 |    9 |    8 |    4 |    6 |    5 |    1 |    0 |    6 |     0 |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                              | Public               |    48 |    5 |    5 |    0 |    3 |    3 |    2 |    6 |    5 |    6 |    11 |
| DE LA SALLE - COLLEGE OF SAINT BENILDE                                                | Private              |    47 |    4 |    4 |    2 |    7 |    3 |    3 |    5 |    7 |    5 |     6 |
| PILAR COLLEGE                                                                         | Private              |    47 |    9 |    2 |    3 |    6 |    7 |    2 |    5 |    3 |    4 |     6 |
| MOUNTAIN VIEW COLLEGE BUKIDNON                                                        | Private              |    46 |    9 |    5 |    4 |    4 |    7 |    4 |    5 |    3 |    2 |     3 |
| MAPUA INSTITUTE OF TECHNOLOGY - MANILA                                                | Private              |    46 |    5 |    5 |    5 |    8 |    3 |    2 |    5 |    2 |    5 |     5 |
| BICOL UNIVERSITY                                                                      | Public               |    46 |    7 |    6 |   10 |    2 |    4 |    5 |    2 |    5 |    1 |     3 |
| UNIVERSITY OF THE PHILIPPINES - CEBU COLLEGE                                          | Public               |    46 |    0 |    0 |    1 |    5 |    1 |    3 |   10 |    9 |   10 |     7 |
| PHILIPPINE WOMEN'S UNIVERSITY TAFT AVENUE MANILA                                      | Private              |    46 |    9 |    4 |    4 |    2 |    6 |    7 |    4 |    3 |    5 |     1 |
| LYCEUM OF THE PHILIPPINES - LAGUNA                                                    | Private              |    45 |    7 |    6 |    5 |    5 |    3 |    3 |    2 |    5 |    3 |     5 |
| MEDINA COLLEGE                                                                        | Private              |    45 |    9 |    4 |    5 |    5 |    4 |    1 |    8 |    4 |    0 |     4 |
| PHILIPPINE CHRISTIAN UNIVERSITY                                                       | Private              |    45 |    9 |    4 |    2 |    3 |    4 |    8 |    8 |    4 |    2 |     1 |
| NOTRE DAME OF DADIANGAS COLLEGE GEN. SANTOS                                           | Private              |    44 |    6 |    6 |    6 |    5 |    6 |    5 |    5 |    3 |    2 |     0 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - BINAN LAGUNA                                    | Private              |    44 |    8 |    5 |    5 |   11 |    3 |    5 |    1 |    4 |    0 |     2 |
| UNIVERSITY OF THE ASSUMPTION                                                          | Private              |    44 |    3 |    2 |    3 |    8 |    6 |    2 |    5 |    1 |    3 |     8 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - LAGUNA                                          | Private              |    44 |    3 |    5 |    4 |    4 |    6 |    4 |    3 |    1 |    7 |     6 |
| CENTRAL MINDANAO UNIVERSITY BUKIDNON                                                  | Public               |    43 |   11 |    5 |    5 |    8 |    4 |    4 |    4 |    1 |    0 |     1 |
| BROKENSHIRE COLLEGE DAVAO CITY                                                        | Private              |    43 |    8 |    7 |    8 |    5 |    7 |    1 |    2 |    1 |    3 |     1 |
| UNIVERSITY OF CALIFORNIA - DAVIS                                                      | Foreign              |    43 |    2 |    0 |    0 |    6 |    3 |    3 |    5 |    5 |    8 |    11 |
| UNIVERSITY OF CAGAYAN VALLEY                                                          | Private              |    43 |    3 |    3 |    3 |    7 |    1 |    4 |    5 |    2 |    7 |     7 |
| UNIVERSITY OF THE VISAYAS - MANDAUE                                                   | Private              |    42 |    8 |    4 |    3 |    5 |    3 |    4 |    4 |    1 |    5 |     5 |
| LA CONSOLACION COLLEGE                                                                | Private              |    41 |   13 |   12 |    5 |    3 |    1 |    2 |    1 |    2 |    0 |     0 |
| FILAMER CHRISTIAN UNIVERSITY                                                          | Private              |    41 |    4 |    7 |    5 |    5 |    3 |    1 |    3 |    5 |    3 |     2 |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                               | Public               |    40 |    8 |    4 |    5 |    5 |    3 |    5 |    2 |    3 |    1 |     2 |
| YAMAN LAHI FOUNDATION - EMILIO AGUINALDO COLLEGE                                      | Private              |    40 |    6 |    0 |    7 |    4 |    3 |    3 |    3 |    3 |    4 |     5 |
| UNIVERSITY OF CALIFORNIA - IRVINE                                                     | Foreign              |    40 |    1 |    1 |    1 |    1 |    2 |    1 |    8 |    7 |    9 |     8 |
| TRINITY COLLEGE                                                                       | Foreign              |    40 |    7 |   11 |    6 |    1 |    5 |    5 |    2 |    1 |    0 |     2 |
| UNIVERSIDAD DE STA. ISABEL NAGA CITY                                                  | Private              |    39 |    4 |    6 |    2 |    6 |    5 |    3 |    4 |    4 |    1 |     3 |
| LOURDES COLLEGE                                                                       | Private              |    39 |    5 |    2 |    2 |    4 |    7 |    4 |    5 |    4 |    1 |     4 |
| ST. JUDE COLLEGE MANILA                                                               | Private              |    39 |    7 |   10 |    7 |    5 |    2 |    3 |    0 |    1 |    3 |     1 |
| RANGSIT UNIVERSITY THAILAND                                                           | Foreign              |    38 |   17 |    5 |    4 |    3 |    3 |    3 |    0 |    0 |    1 |     2 |
| NEW ERA UNIVERSITY QUEZON CITY                                                        | Private              |    37 |   14 |    4 |    6 |    4 |    2 |    2 |    3 |    1 |    0 |     1 |
| UNIVERSITY OF BOHOL                                                                   | Private              |    37 |    6 |    3 |    5 |    4 |    3 |    3 |    1 |    6 |    2 |     3 |
| NUEVA ECIJA COLLEGES                                                                  | Private              |    37 |    8 |    4 |    5 |    2 |    3 |    1 |    3 |    1 |    6 |     3 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS CEBU                                     | Public               |    37 |    1 |    0 |    0 |    1 |    2 |    6 |    4 |    6 |    6 |    11 |
| VISAYAS STATE UNIVERSITY - MAIN                                                       | Public               |    36 |    6 |    1 |    2 |    6 |    5 |    4 |    2 |    3 |    1 |     5 |
| DAVAO MEDICAL SCHOOL FOUNDATION INC.                                                  | Private              |    36 |    6 |    3 |    4 |    2 |    9 |    3 |    5 |    2 |    1 |     0 |
| UNIVERSITY OF LUZON                                                                   | Private              |    36 |    8 |    7 |    6 |    3 |    0 |    1 |    2 |    3 |    1 |     3 |
| MAHIDOL UNIVERSITY                                                                    | Foreign              |    36 |    6 |    2 |    8 |    1 |    2 |    3 |    5 |    3 |    5 |     0 |
| ILIGAN MEDICAL CENTER ILIGAN CITY                                                     | Private              |    36 |    9 |    9 |    5 |    3 |    4 |    1 |    3 |    0 |    1 |     1 |
| NORTHWESTERN UNIVERSITY                                                               | Private              |    36 |    3 |    8 |    2 |    5 |    3 |    3 |    3 |    3 |    5 |     1 |
| MEDINA COLLEGE - PAGADIAN                                                             | Private              |    35 |    5 |    1 |    6 |    4 |    2 |    3 |    4 |    3 |    5 |     2 |
| CALAYAN EDUCATIONAL FOUNDATION                                                        | Private              |    35 |    4 |    4 |    1 |    2 |    6 |    6 |    2 |    5 |    2 |     2 |
| PINES CITY COLLEGES - BAGUIO CITY                                                     | Private              |    35 |   10 |    8 |    7 |    3 |    2 |    1 |    2 |    2 |    0 |     0 |
| BATANGAS STATE UNIVERSITY - MAIN                                                      | Public               |    35 |    8 |    2 |    2 |    4 |    2 |    3 |    1 |    3 |    3 |     5 |
| SAINT MARY'S COLLEGE OF TAGUM                                                         | Private              |    34 |    2 |    4 |    2 |    2 |    3 |    6 |    4 |    4 |    6 |     1 |
| ST. PAUL UNIVERSITY - TUGUEGARAO CAGAYAN                                              | Private              |    34 |    9 |    5 |    7 |    3 |    3 |    3 |    2 |    2 |    0 |     0 |
| ARELLANO UNIVERSITY                                                                   | Private              |    34 |    8 |    5 |    5 |    5 |    2 |    6 |    0 |    0 |    1 |     1 |
| MARIANO MARCOS STATE UNIVERSITY ILOCOS NORTE                                          | Public               |    33 |    3 |    5 |    5 |    6 |    0 |    2 |    3 |    5 |    1 |     3 |
| HOLY TRINITY UNIVERSITY                                                               | Private              |    33 |    3 |    4 |    3 |    8 |    1 |    4 |    1 |    6 |    0 |     3 |
| MINDANAO STATE UNIVERSITY GENERAL SANTOS CITY                                         | Public               |    33 |    1 |    1 |    9 |    6 |    5 |    0 |    5 |    3 |    2 |     1 |
| SAN BEDA COLLEGE - ALABANG                                                            | Private              |    33 |    7 |    1 |    3 |    7 |    3 |    3 |    1 |    2 |    2 |     4 |
| OUR LADY OF GUADALUPE COLLEGES                                                        | Private              |    33 |    2 |    4 |    8 |    4 |    1 |    3 |    1 |    3 |    1 |     5 |
| CAPITOL MEDICAL CENTER COLLEGE Q.C.                                                   | Private              |    32 |    7 |    4 |    6 |    5 |    6 |    1 |    1 |    2 |    0 |     0 |
| Remedios Trinidad Romualdez Medical Foundation                                        | Not Specified        |    31 |    2 |    1 |    9 |    3 |    4 |    2 |    3 |    2 |    3 |     1 |
| LYCEUM OF THE PHILIPPINES - ST. CABRINI COLLEGE OF ALLIED MEDICINE                    | Private              |    31 |    1 |    7 |    3 |    5 |    3 |    5 |    2 |    3 |    1 |     1 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA - CALAMBA                                   | Private              |    30 |    1 |    0 |    2 |    4 |    3 |    3 |    7 |    1 |    1 |     7 |
| LYCEUM OF THE PHILIPPINES UNIVERSITY                                                  | Private              |    30 |    1 |    4 |    4 |    3 |    1 |    4 |    3 |    0 |    7 |     3 |
| LYCEUM OF BATANGAS                                                                    | Private              |    30 |    6 |    7 |    7 |    2 |    2 |    2 |    0 |    3 |    1 |     0 |
| UNIVERSITY OF ST. LA SALLE - DASMARIÑAS CAVITE                                        | Private              |    30 |    2 |    5 |    7 |    4 |    3 |    4 |    3 |    1 |    0 |     1 |
| UNIVERSITY OF CALIFORNIA LOS ANGELES                                                  | Foreign              |    30 |    1 |    1 |    2 |    0 |    2 |    2 |    4 |    4 |    6 |     7 |
| UNIVERSITY OF CEBU (FORMERLY CEBU CENTRAL COLLEGES)                                   | Private              |    30 |    3 |    2 |    4 |    6 |    4 |    5 |    2 |    2 |    2 |     0 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES-DAVAO CITY                                     | Public               |    30 |    5 |    7 |    5 |    4 |    3 |    0 |    3 |    2 |    1 |     0 |
| ST. JOSEPH'S COLLEGE OF QUEZON CITY                                                   | Private              |    30 |    4 |    2 |    4 |    4 |    6 |    1 |    2 |    1 |    1 |     4 |
| WESLEYAN UNIVERSITY-PHILIPPINES CABANATUAN CITY                                       | Private              |    29 |    4 |    4 |    5 |    4 |    4 |    3 |    1 |    3 |    0 |     1 |
| LA SALLE UNIVERSITY                                                                   | Private              |    29 |    2 |    3 |    4 |    3 |    2 |    5 |    3 |    1 |    3 |     3 |
| ST. ANTHONY COLLEGE OF ROXAS CITY                                                     | Private              |    29 |    5 |    4 |    3 |    4 |    1 |    1 |    4 |    1 |    1 |     4 |
| CARAGA STATE UNIVERSITY - MAIN                                                        | Public               |    29 |    3 |    4 |    4 |    2 |    0 |    1 |    4 |    1 |    4 |     4 |
| UNIVERSIDAD DE MANILA                                                                 | Public               |    29 |    5 |    0 |    1 |    3 |    3 |    1 |    4 |    3 |    5 |     3 |
| UNIVERSITY OF LA SALETTE SANTIAGO CITY                                                | Private              |    28 |    5 |    4 |    5 |    5 |    3 |    0 |    0 |    3 |    0 |     3 |
| MAHIDOL UNIVERSITY THAILAND                                                           | Foreign              |    28 |    5 |    5 |    2 |    3 |    5 |    2 |    2 |    2 |    2 |     0 |
| UNIVERSITY OF ASIA AND THE PACIFIC                                                    | Private              |    28 |    3 |    5 |    2 |    4 |    3 |    2 |    3 |    2 |    0 |     4 |
| CHULALONGKORN UNIVERSITY                                                              | Foreign              |    28 |    3 |    2 |    3 |    2 |    3 |    1 |    2 |    3 |    5 |     4 |
| PHILIPPINE REHABILITATION INSTITUTE FOUNDATION                                        | Private              |    27 |    2 |    7 |    2 |    1 |    2 |    1 |    1 |    4 |    5 |     2 |
| RIVERSIDE COLLEGE BACOLOD CITY                                                        | Private              |    27 |    4 |    2 |    4 |    4 |    2 |    5 |    2 |    3 |    1 |     0 |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                           | Public               |    27 |    1 |    2 |    1 |    2 |    3 |    2 |    4 |    5 |    2 |     2 |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                    | Public               |    27 |    4 |    2 |    5 |    5 |    1 |    3 |    0 |    1 |    2 |     4 |
| SULU STATE COLLEGE                                                                    | Public               |    27 |    6 |    2 |    1 |    4 |    1 |    2 |    1 |    2 |    2 |     4 |
| CALIFORNIA STATE UNIVERSITY                                                           | Foreign              |    27 |    0 |    0 |    2 |    5 |    1 |    7 |    2 |    4 |    3 |     3 |
| SURIGAO EDUCATION CENTER                                                              | Private              |    27 |    7 |    3 |    5 |    1 |    1 |    2 |    3 |    1 |    2 |     2 |
| MAPUA INSTITUTE OF TECHNOLOGY                                                         | Private              |    26 |    4 |    2 |    2 |    1 |    3 |    3 |    5 |    3 |    3 |     0 |
| ST. DOMINIC COLLEGE OF ARTS AND SCIENCES OF CAVITE                                    | Private              |    26 |    2 |    3 |    3 |    2 |    4 |    4 |    3 |    2 |    1 |     2 |
| ST. SCHOLASTICA'S COLLEGE - TACLOBAN CITY                                             | Private              |    26 |    5 |    4 |    3 |    3 |    3 |    1 |    2 |    2 |    1 |     2 |
| CEBU INSTITUTE OF TECHNOLOGY - UNIVERSITY                                             | Private              |    26 |    3 |    3 |    3 |    2 |    2 |    7 |    1 |    1 |    2 |     2 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA               | Public               |    26 |    4 |    4 |    0 |    3 |    2 |    2 |    3 |    2 |    4 |     2 |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES                                                 | Private              |    26 |    5 |    4 |    1 |    2 |    3 |    3 |    1 |    4 |    2 |     1 |
| MANUEL S. ENVERGA UNIVERSITY FOUNDATION - LUCENA                                      | Private              |    26 |    4 |    2 |    1 |    3 |    2 |    1 |    5 |    1 |    2 |     5 |
| UNIVERSITY OF CALIFORNIA RIVERSIDE CA USA                                             | Foreign              |    25 |    0 |    0 |    1 |    1 |    2 |    1 |    4 |    2 |    6 |     8 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM                                                   | Private              |    25 |    4 |    3 |    3 |    2 |    0 |    4 |    0 |    2 |    5 |     2 |
| WEST NEGROS UNIVERSITY                                                                | Private              |    25 |    1 |    1 |    4 |    3 |    2 |    2 |    1 |    2 |    5 |     2 |
| UNIVERSITY OF THE IMMACULATE CONCEPCION DAVAO CITY                                    | Private              |    25 |    4 |    4 |    4 |    4 |    2 |    4 |    2 |    0 |    0 |     1 |
| UNION CHRISTIAN COLLEGE                                                               | Private              |    25 |    2 |    4 |    2 |    4 |    7 |    0 |    1 |    2 |    0 |     3 |
| WORLD CITI COLLEGES                                                                   | Private              |    24 |    4 |    4 |    5 |    3 |    0 |    1 |    3 |    3 |    1 |     0 |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                                | Public               |    24 |    3 |    2 |    2 |    1 |    1 |    4 |    2 |    1 |    4 |     4 |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                                 | Public               |    24 |    2 |    2 |    1 |    4 |    3 |    2 |    3 |    1 |    2 |     2 |
| LORMA COLLEGE SAN FERNANDO LA UNION                                                   | Private              |    24 |    6 |    6 |    2 |    5 |    1 |    2 |    1 |    0 |    1 |     0 |
| PLT COLLEGE                                                                           | Private              |    24 |    4 |    4 |    2 |    1 |    3 |    3 |    3 |    2 |    1 |     1 |
| UNIVERSITY OF SOUTHERN MINDANAO NORTH COTABATO                                        | Public               |    24 |    4 |    4 |    2 |    1 |    3 |    3 |    2 |    2 |    2 |     1 |
| UNIVERSITY OF MINDANAO                                                                | Private              |    24 |    2 |    2 |    0 |    3 |    3 |    3 |    1 |    6 |    3 |     1 |
| NATIONAL UNIVERSITY                                                                   | Private              |    24 |    4 |    1 |    0 |    3 |    1 |    4 |    5 |    1 |    3 |     2 |
| RIVERSIDE COLLEGE OF NURSING BACOLOD                                                  | Private              |    23 |    2 |    3 |    4 |    4 |    1 |    4 |    3 |    2 |    0 |     0 |
| TARLAC STATE UNIVERSITY                                                               | Public               |    23 |    3 |    4 |    2 |    1 |    2 |    2 |    4 |    1 |    3 |     1 |
| CHIANG MAI UNIVERSITY                                                                 | Foreign              |    23 |    8 |    3 |    2 |    2 |    1 |    2 |    0 |    4 |    0 |     1 |
| UNIVERSITY OF PERPETUAL HELP RIZAL - MOLINO                                           | Private              |    23 |    3 |    4 |    3 |    3 |    5 |    0 |    3 |    0 |    0 |     2 |
| OTHERS (PLEASE SPECIFY)                                                               | Not Specified        |    23 |    1 |    1 |    0 |    0 |    0 |    4 |    4 |    3 |    5 |     5 |
| AL KWARIZMI INTERNATIONAL COLLEGE FOUNDATION                                          | Foreign              |    23 |    3 |    3 |    3 |    3 |    3 |    3 |    0 |    2 |    1 |     2 |
| BENGUET STATE UNIVERSITY                                                              | Public               |    23 |    3 |    1 |    2 |    2 |    6 |    1 |    2 |    3 |    2 |     1 |
| UNIVERSITY OF CALIFORNIA - SAN DIEGO                                                  | Foreign              |    23 |    2 |    0 |    1 |    1 |    0 |    2 |    2 |    3 |    6 |     5 |
| UPH-DR. JOSE G. TAMAYO MEDICAL UNIV.                                                  | Private              |    23 |    3 |    8 |    5 |    1 |    1 |    0 |    1 |    3 |    1 |     0 |
| ASSUMPTION COLLEGE MAKATI                                                             | Private              |    22 |    1 |    1 |    1 |    6 |    2 |    7 |    3 |    1 |    0 |     0 |
| MISAMIS UNIVERSITY                                                                    | Private              |    22 |    5 |    7 |    2 |    3 |    2 |    1 |    0 |    2 |    0 |     0 |
| GOOD SAMARITAN COLLEGES                                                               | Private              |    22 |    2 |    1 |    1 |    3 |    4 |    2 |    3 |    4 |    1 |     1 |
| ST. MICHAEL'S COLLEGE                                                                 | Private              |    22 |    0 |    4 |    3 |    3 |    2 |    4 |    2 |    1 |    2 |     1 |
| KESTER GRANT COLLEGE - PHILIPPINES                                                    | Private              |    22 |    2 |    1 |    5 |    3 |    1 |    1 |    3 |    0 |    3 |     3 |
| COLEGIO DE SAN AGUSTIN BACOLOD                                                        | Private              |    22 |    2 |    6 |    3 |    4 |    2 |    1 |    3 |    0 |    1 |     0 |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING & LIBERAL ARTS                            | Private              |    22 |    0 |    0 |    4 |    4 |    3 |    5 |    3 |    3 |    0 |     0 |
| BICOL UNIVERSITY COLLEGE OF SCIENCE LEGAZPI CITY                                      | Public               |    22 |    7 |    6 |    0 |    0 |    3 |    2 |    0 |    1 |    2 |     1 |
| MANILA THEOLOGICAL COLLEGE                                                            | Private              |    21 |    3 |    4 |    2 |    4 |    1 |    1 |    0 |    3 |    1 |     1 |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES CAGAYAN                                      | Private              |    21 |    3 |    4 |    2 |    1 |    6 |    3 |    1 |    0 |    1 |     0 |
| HOLY NAME UNIVERSITY - TAGBILARAN CITY                                                | Private              |    21 |    1 |    1 |    2 |    5 |    6 |    1 |    3 |    1 |    0 |     1 |
| JOHN PAUL II COLLEGE OF DAVAO                                                         | Private              |    21 |    4 |    1 |    3 |    2 |    1 |    2 |    1 |    1 |    4 |     2 |
| DE LOS SANTOS - STI COLLEGE                                                           | Private              |    21 |    4 |    1 |    2 |    3 |    4 |    0 |    2 |    2 |    2 |     1 |
| DIVINE WORD COLLEGE OF LEGAZPI                                                        | Private              |    21 |    8 |    1 |    2 |    1 |    3 |    2 |    1 |    2 |    1 |     0 |
| 13207A                                                                                | Not Specified        |    21 |    3 |    3 |    4 |    2 |    1 |    1 |    0 |    0 |    2 |     5 |
| CENTRAL LUZON DOCTOR'S HOSPITAL TARLAC                                                | Private              |    21 |    2 |    1 |    3 |    4 |    2 |    3 |    4 |    2 |    0 |     0 |
| AQUINAS UNIVERSITY LEGASPI CITY                                                       | Private              |    21 |    1 |    7 |    1 |    3 |    2 |    3 |    0 |    2 |    1 |     0 |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES INC.                                            | Private              |    20 |    8 |    4 |    2 |    1 |    4 |    0 |    0 |    1 |    0 |     0 |
| COLEGIO DE DAGUPAN                                                                    | Private              |    20 |    1 |    4 |    0 |    2 |    2 |    2 |    2 |    1 |    4 |     2 |
| DE LA SALLE COLLEGE OF SAINT BENILDE - MANILA                                         | Private              |    20 |    0 |    1 |    2 |    2 |    2 |    3 |    1 |    3 |    5 |     1 |
| BALIUAG UNIVERSITY                                                                    | Private              |    20 |    0 |    2 |    2 |    3 |    4 |    1 |    2 |    2 |    3 |     0 |
| THAMMASAT UNIVERSITY                                                                  | Foreign              |    20 |    1 |    4 |    2 |    3 |    4 |    3 |    0 |    1 |    1 |     1 |
| OUR LADY OF MT. CARMEL INSTITUTE OF MEDICAL STUDIES                                   | Private              |    20 |    2 |    2 |    1 |    4 |    0 |    2 |    2 |    0 |    5 |     1 |
| AGO MEDICAL AND EDUCATIONAL CENTER LEGAZPI CITY                                       | Private              |    20 |    4 |    2 |    4 |    2 |    3 |    0 |    2 |    2 |    0 |     1 |
| UNIVERSITY OF CALIFORNIA-RIVERSIDE                                                    | Foreign              |    19 |    2 |    1 |    1 |    0 |    0 |    2 |    3 |    2 |    4 |     3 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - SOUTH LA UNION                         | Public               |    19 |    3 |    1 |    4 |    1 |    2 |    2 |    1 |    0 |    2 |     3 |
| OLIVAREZ COLLEGE                                                                      | Private              |    19 |    0 |    2 |    3 |    5 |    2 |    2 |    0 |    0 |    1 |     4 |
| WESTERN STATE UNIVERSITY OF COLORADO                                                  | Foreign              |    19 |    1 |    2 |    3 |    2 |    1 |    6 |    2 |    1 |    1 |     0 |
| UNIVERSITY OF PERPETUAL HELP COLLEGE OF LAS PINAS                                     | Private              |    19 |    2 |    6 |    0 |    2 |    2 |    3 |    3 |    1 |    0 |     0 |
| ARELLANO UNIVERSITY - PASIG                                                           | Private              |    18 |    2 |    2 |    2 |    0 |    5 |    2 |    3 |    0 |    1 |     1 |
| LYCEUM OF THE PHILIPPINES                                                             | Private              |    18 |    1 |    0 |    4 |    4 |    4 |    3 |    1 |    0 |    1 |     0 |
| PAMANTASAN NG LUNGSOD NG PASIG                                                        | Public               |    18 |    4 |    2 |    1 |    1 |    1 |    2 |    0 |    1 |    5 |     1 |
| MAPUA INSTITUTE OF TECHNOLOGY - MAKATI                                                | Private              |    18 |    1 |    5 |    3 |    2 |    2 |    1 |    0 |    2 |    0 |     1 |
| HOLY ANGEL UNIVERSITY ANGELES CITY                                                    | Private              |    18 |    0 |    2 |    5 |    2 |    1 |    2 |    2 |    1 |    2 |     1 |
| SAMAR STATE UNIVERSITY - MAIN                                                         | Public               |    18 |    2 |    0 |    1 |    4 |    3 |    0 |    3 |    1 |    2 |     1 |
| UNIVERSITY OF SAN JOSE RECOLETOS CEBU                                                 | Private              |    18 |    6 |    1 |    2 |    2 |    2 |    4 |    0 |    0 |    1 |     0 |
| COLEGIO DE SAN JUAN DE LETRAN CALAMBA                                                 | Private              |    18 |    3 |    6 |    4 |    1 |    1 |    1 |    1 |    1 |    0 |     0 |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                  | Public               |    18 |    5 |    2 |    1 |    0 |    0 |    0 |    4 |    1 |    2 |     3 |
| TAGUM DOCTORS COLLEGE                                                                 | Private              |    18 |    3 |    3 |    3 |    2 |    1 |    1 |    0 |    2 |    0 |     2 |
| COLLEGE OF THE HOLY SPIRIT OF TARLAC                                                  | Private              |    18 |    1 |    1 |    2 |    0 |    1 |    4 |    2 |    0 |    2 |     4 |
| CENTRAL LUZON STATE UNIVERSITY NUEVA ECIJA                                            | Public               |    18 |    3 |    3 |    2 |    4 |    2 |    3 |    0 |    0 |    1 |     0 |
| COLEGIO DE STA. LOURDES OF LEYTE FOUNDATION                                           | Private              |    18 |    3 |    4 |    1 |    1 |    2 |    1 |    0 |    5 |    1 |     0 |
| ANDRES BONIFACIO COLLEGE                                                              | Private              |    17 |    2 |    2 |    0 |    3 |    0 |    4 |    0 |    0 |    3 |     2 |
| ST. JOSEPH COLLEGE CAVITE CITY                                                        | Private              |    17 |    2 |    1 |    1 |    2 |    2 |    0 |    3 |    2 |    1 |     1 |
| CHULALONGKORN UNIVERSITY THAILAND                                                     | Foreign              |    17 |    1 |    3 |    3 |    3 |    4 |    1 |    1 |    0 |    0 |     1 |
| UNIVERSITY OF TORONTO                                                                 | Foreign              |    17 |    0 |    1 |    0 |    1 |    0 |    0 |    3 |    4 |    3 |     5 |
| OUR LADY OF FATIMA UNIVERSITY - PAMPANGA                                              | Private              |    17 |    1 |    2 |    5 |    1 |    0 |    2 |    3 |    1 |    1 |     0 |
| LA CONSOLACION UNIVERSITY PHILIPPINES                                                 | Private              |    17 |    1 |    4 |    1 |    1 |    1 |    2 |    4 |    2 |    0 |     1 |
| UNIVERSITY OF PANGASINAN DAGUPAN CITY                                                 | Private              |    17 |    1 |    3 |    3 |    5 |    2 |    2 |    0 |    1 |    0 |     0 |
| MAE FAH LUANG UNIVERSITY                                                              | Foreign              |    17 |    5 |    4 |    0 |    0 |    0 |    0 |    2 |    1 |    2 |     3 |
| BICOL UNIVERSITY COLLEGE OF NURSING LEGAZPI CITY                                      | Public               |    17 |    1 |    0 |    1 |    2 |    2 |    2 |    1 |    3 |    3 |     2 |
| BUKIDNON STATE UNIVERSITY                                                             | Public               |    17 |    2 |    5 |    1 |    0 |    0 |    1 |    2 |    2 |    3 |     0 |
| BULACAN STATE UNIVERSITY                                                              | Public               |    17 |    2 |    3 |    1 |    2 |    3 |    0 |    2 |    3 |    1 |     0 |
| UNIVERSITY OF CALIFORNIA BERKELEY                                                     | Foreign              |    17 |    1 |    1 |    1 |    0 |    0 |    0 |    1 |    0 |    4 |     7 |
| CANOSSA COLLEGE                                                                       | Private              |    16 |    0 |    1 |    0 |    1 |    1 |    4 |    2 |    2 |    3 |     2 |
| IMMACULATE CONCEPTION COLLEGE - ALBAY                                                 | Private              |    16 |    3 |    0 |    1 |    0 |    1 |    3 |    3 |    2 |    2 |     0 |
| DE OCAMPO MEMORIAL COLLEGE                                                            | Private              |    16 |    3 |    1 |    1 |    5 |    1 |    2 |    0 |    2 |    0 |     1 |
| NORTHERN LUZON ADVENTIST COLLEGE                                                      | Private              |    16 |    3 |    0 |    1 |    2 |    1 |    3 |    2 |    1 |    2 |     1 |
| UNIVERSITY OF EASTERN PHILIPPINES - SAMAR                                             | Public               |    16 |    6 |    5 |    3 |    1 |    0 |    0 |    0 |    1 |    0 |     0 |
| MANILA ADVENTIST MEDICAL CENTER - PASAY CITY                                          | Private              |    16 |    0 |    2 |    0 |    4 |    5 |    0 |    0 |    2 |    2 |     1 |
| UNIVERSITY OF WASHINGTON                                                              | Foreign              |    16 |    2 |    0 |    0 |    0 |    1 |    3 |    1 |    2 |    1 |     6 |
| ST. PAUL COLLEGE ILOILO                                                               | Private              |    16 |    0 |    0 |    2 |    1 |    4 |    2 |    2 |    3 |    2 |     0 |
| SOUTHEAST ASIAN COLLEGE INC.-QUEZON CITY                                              | Private              |    16 |    4 |    2 |    4 |    2 |    2 |    2 |    0 |    0 |    0 |     0 |
| SAINT PAUL COLLEGE OF ILOCOS SUR                                                      | Private              |    16 |    1 |    2 |    1 |    1 |    3 |    0 |    3 |    1 |    3 |     1 |
| NATIONAL UNIVERSITY - CEDCE                                                           | Private              |    16 |    3 |    2 |    2 |    0 |    3 |    4 |    0 |    0 |    0 |     2 |
| PALAWAN STATE UNIVERSITY PUERTO PRINCESA CITY                                         | Public               |    15 |    5 |    5 |    0 |    2 |    1 |    1 |    0 |    0 |    1 |     0 |
| NORTH VALLEY COLLEGE FOUNDATION                                                       | Private              |    15 |    0 |    2 |    3 |    2 |    4 |    1 |    0 |    1 |    1 |     1 |
| MARY CHILES COLLEGE                                                                   | Private              |    15 |    2 |    2 |    3 |    2 |    0 |    1 |    3 |    1 |    0 |     1 |
| LYCEUM OF ILIGAN FOUNDATION                                                           | Private              |    15 |    2 |    0 |    1 |    1 |    1 |    1 |    1 |    1 |    2 |     5 |
| ARELLANO UNIVERSITY - PASAY                                                           | Private              |    15 |    1 |    3 |    2 |    2 |    0 |    1 |    0 |    3 |    0 |     2 |
| LYCEUM OF THE PHILIPPINES - CAVITE                                                    | Private              |    15 |    2 |    4 |    0 |    1 |    0 |    3 |    4 |    0 |    0 |     1 |
| NARESUAN UNIVERSITY                                                                   | Foreign              |    15 |    2 |    0 |    2 |    1 |    2 |    0 |    1 |    2 |    2 |     2 |
| CARITAS FAMILY HOSPITAL AND COLLEGES                                                  | Private              |    15 |    2 |    1 |    0 |    1 |    2 |    1 |    3 |    1 |    2 |     2 |
| UNIVERSITY OF BATANGAS                                                                | Private              |    15 |    2 |    2 |    2 |    2 |    4 |    2 |    1 |    0 |    0 |     0 |
| DR. P. OCAMPO COLLEGES                                                                | Private              |    15 |    3 |    3 |    0 |    2 |    0 |    1 |    2 |    1 |    1 |     2 |
| GORDON COLLEGE                                                                        | Public               |    15 |    0 |    2 |    2 |    2 |    1 |    1 |    1 |    1 |    1 |     3 |
| LIPA CITY COLLEGES                                                                    | Private              |    15 |    1 |    1 |    0 |    3 |    1 |    1 |    0 |    1 |    2 |     5 |
| ILOCOS SUR COMMUNITY COLLEGE - BANTAY ILOCOS SUR                                      | Public               |    15 |    3 |    4 |    1 |    4 |    0 |    0 |    2 |    1 |    0 |     0 |
| UNIVERSITY OF FLORIDA                                                                 | Foreign              |    15 |    1 |    1 |    0 |    1 |    1 |    0 |    3 |    2 |    4 |     2 |
| CALAMBA DOCTORS' COLLEGE                                                              | Private              |    14 |    3 |    1 |    1 |    2 |    1 |    1 |    2 |    1 |    0 |     0 |
| SAINT TONIS COLLEGE                                                                   | Private              |    14 |    1 |    3 |    1 |    3 |    1 |    1 |    1 |    1 |    1 |     1 |
| ST. PAUL UNIVERSITY SURIGAO                                                           | Private              |    14 |    2 |    2 |    1 |    1 |    0 |    2 |    1 |    3 |    1 |     0 |
| URDANETA CITY UNIVERSITY                                                              | Public               |    14 |    1 |    2 |    1 |    1 |    2 |    1 |    2 |    2 |    1 |     1 |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                     | Public               |    14 |    3 |    0 |    1 |    1 |    0 |    2 |    0 |    2 |    3 |     2 |
| NOTRE DAME OF TACURONG COLLEGE                                                        | Private              |    14 |    3 |    2 |    3 |    1 |    2 |    1 |    0 |    0 |    1 |     1 |
| AKLAN STATE UNIVERSITY - MAIN                                                         | Public               |    14 |    2 |    2 |    0 |    2 |    1 |    2 |    1 |    1 |    1 |     2 |
| MONAD UNIVERSITY                                                                      | Foreign              |    14 |    1 |    3 |    1 |    1 |    1 |    0 |    1 |    3 |    1 |     2 |
| SAINT GABRIEL COLLEGE                                                                 | Private              |    13 |    3 |    1 |    2 |    2 |    1 |    1 |    0 |    0 |    2 |     1 |
| COLEGIO DE SAN LORENZO RUIZ DE MANILA OF NORTHERN SAMAR                               | Private              |    13 |    2 |    1 |    1 |    0 |    2 |    4 |    0 |    1 |    2 |     0 |
| UNIVERSITY OF SAINT ANTHONY                                                           | Private              |    13 |    2 |    0 |    0 |    4 |    2 |    1 |    0 |    1 |    1 |     1 |
| NOTRE DAME OF MIDSAYAP COLLEGE                                                        | Private              |    13 |    2 |    1 |    1 |    0 |    0 |    1 |    3 |    1 |    2 |     0 |
| WESTERN LEYTE COLLEGE OF ORMOC CITY                                                   | Private              |    13 |    3 |    2 |    1 |    0 |    1 |    0 |    2 |    1 |    1 |     2 |
| CENTRAL COLLEGES OF THE PHILIPPINES                                                   | Private              |    13 |    2 |    1 |    0 |    0 |    2 |    3 |    0 |    2 |    1 |     1 |
| UNIVERSITY OF BOHOL TAGBILARAN CITY                                                   | Private              |    13 |    4 |    0 |    1 |    1 |    1 |    2 |    1 |    3 |    0 |     0 |
| HOLY CROSS OF DAVAO COLLEGE                                                           | Private              |    13 |    4 |    1 |    1 |    1 |    0 |    2 |    1 |    0 |    2 |     1 |
| SACRED HEART COLLEGE LUCENA CITY                                                      | Private              |    13 |    0 |    0 |    5 |    1 |    1 |    1 |    2 |    1 |    1 |     1 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - GMA                                             | Private              |    13 |    1 |    5 |    0 |    1 |    3 |    2 |    0 |    0 |    0 |     0 |
| University For Development Studies                                                    | Not Specified        |    13 |    4 |    0 |    2 |    1 |    0 |    0 |    3 |    1 |    0 |     2 |
| 13100A                                                                                | Not Specified        |    13 |    1 |    2 |    1 |    0 |    2 |    2 |    0 |    3 |    1 |     1 |
| BICOL UNIVERSITY - DARAGA                                                             | Public               |    13 |    4 |    1 |    1 |    2 |    2 |    2 |    0 |    0 |    0 |     1 |
| ST. FERDINAND COLLEGE - ILAGAN                                                        | Private              |    13 |    1 |    1 |    1 |    4 |    0 |    2 |    1 |    1 |    1 |     1 |
| DE LA SALLE - ARANETA UNIVERSITY                                                      | Private              |    13 |    4 |    0 |    2 |    1 |    1 |    1 |    2 |    0 |    2 |     0 |
| DOMINICAN COLLEGE                                                                     | Private              |    13 |    1 |    2 |    3 |    0 |    2 |    0 |    1 |    1 |    1 |     0 |
| UNCIANO COLLEGES AND GENERAL HOSPITAL                                                 | Private              |    12 |    0 |    2 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |     2 |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE NEGROS OCCIDENTAL                                | Private              |    12 |    2 |    0 |    2 |    1 |    1 |    4 |    0 |    0 |    1 |     1 |
| UNIVERSITY OF THE PHILIPPINES - PAMPANGA                                              | Public               |    12 |    0 |    1 |    0 |    0 |    4 |    0 |    4 |    2 |    1 |     0 |
| BICOL UNIVERSITY - POLANGUI                                                           | Public               |    12 |    0 |    0 |    1 |    2 |    3 |    1 |    2 |    1 |    0 |     2 |
| UNCIANO COLLEGES                                                                      | Private              |    12 |    1 |    0 |    4 |    0 |    1 |    0 |    2 |    0 |    1 |     2 |
| SOUTHEAST ASIAN COLLEGE INC.-ESPANA MANILA                                            | Private              |    12 |    7 |    4 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |     0 |
| UNIVERSITY OF CALIFORNIA SANTA BARBARA                                                | Foreign              |    12 |    2 |    0 |    1 |    2 |    2 |    0 |    2 |    1 |    0 |     2 |
| PHILIPPINE REHABILITATION INSTITUTE                                                   | Private              |    12 |    3 |    1 |    2 |    0 |    2 |    1 |    2 |    1 |    0 |     0 |
| FIRST ASIA INSTITUTE OF TECHNOLOGY AND HUMANITIES                                     | Private              |    12 |    1 |    0 |    0 |    2 |    3 |    1 |    2 |    2 |    0 |     1 |
| DR. YANGA'S COLLEGES                                                                  | Private              |    12 |    0 |    2 |    0 |    3 |    2 |    2 |    0 |    1 |    0 |     1 |
| COLLEGE OF HOLY SPIRIT-MANILA                                                         | Private              |    12 |    4 |    3 |    1 |    2 |    1 |    0 |    1 |    0 |    0 |     0 |
| MEDINA COLLEGE - IPIL                                                                 | Private              |    12 |    1 |    2 |    2 |    0 |    0 |    0 |    3 |    0 |    3 |     0 |
| UNIVERSITY OF NEVADA LAS VEGAS                                                        | Foreign              |    12 |    1 |    0 |    1 |    1 |    0 |    2 |    1 |    2 |    1 |     3 |
| UNIVERSITY OF PERPETUAL HELP - CALAMBA LAGUNA                                         | Private              |    12 |    1 |    3 |    0 |    3 |    1 |    3 |    0 |    0 |    1 |     0 |
| NOTRE DAME OF MARBEL UNIV.                                                            | Private              |    12 |    2 |    0 |    1 |    2 |    2 |    2 |    0 |    2 |    0 |     1 |
| AMA COMPUTER COLLEGE                                                                  | Private              |    12 |    4 |    2 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |     1 |
| LYCEUM OF APARRI                                                                      | Private              |    12 |    0 |    3 |    2 |    2 |    2 |    0 |    0 |    0 |    1 |     2 |
| LAGUNA COLLEGE                                                                        | Private              |    11 |    0 |    1 |    0 |    3 |    1 |    2 |    2 |    1 |    0 |     1 |
| UNIVERSITY OF ILOILO                                                                  | Private              |    11 |    2 |    0 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |     4 |
| NOTRE DAME OF JOLO COLLEGE - JOLO SULU                                                | Private              |    11 |    5 |    2 |    2 |    0 |    2 |    0 |    0 |    0 |    0 |     0 |
| NORTHERN NEGROS STATE COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                        | Public               |    11 |    1 |    1 |    1 |    1 |    1 |    0 |    2 |    0 |    1 |     3 |
| MABINI COLLEGES                                                                       | Private              |    11 |    2 |    1 |    1 |    1 |    0 |    1 |    0 |    2 |    1 |     2 |
| MEDINA COLLEGE OZAMIS MISAMIS ORIENTAL                                                | Private              |    11 |    5 |    2 |    1 |    0 |    0 |    2 |    1 |    0 |    0 |     0 |
| NORTHERN CHRISTIAN COLLEGE                                                            | Private              |    11 |    2 |    3 |    0 |    0 |    0 |    1 |    0 |    0 |    1 |     4 |
| MARIANO MARCOS STATE UNIVERSITY - COLLEGE OF EDUCATION - LAOAG CITY                   | Public               |    11 |    0 |    3 |    1 |    1 |    1 |    0 |    2 |    0 |    3 |     0 |
| UNIVERSITY OF CORDILLERAS                                                             | Private              |    11 |    1 |    1 |    3 |    1 |    1 |    0 |    1 |    1 |    2 |     0 |
| UNIVERSITY OF THE PHILIPPINES SCH. OF HEALTH SCIENCES -LEYTE                          | Public               |    11 |    2 |    2 |    4 |    0 |    1 |    1 |    1 |    0 |    0 |     0 |
| BRENT HOSPITAL AND COLLEGES INC. ZAMBOANGA CITY                                       | Private              |    11 |    5 |    4 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |     0 |
| VIRGEN MILAGROSA EDUCATIONAL INSTITUTE SAN CARLOS CITY                                | Private              |    11 |    1 |    1 |    0 |    4 |    1 |    1 |    2 |    0 |    1 |     0 |
| ST. JOSEPH'S COLLEGE QUEZON CITY                                                      | Private              |    11 |    1 |    2 |    4 |    2 |    1 |    0 |    1 |    0 |    0 |     0 |
| SRINAKHARINWIROT UNIVERSITY                                                           | Foreign              |    11 |    1 |    1 |    1 |    3 |    1 |    1 |    1 |    1 |    0 |     0 |
| OLIVAREZ COLLEGE SUCAT PARA$AQUE                                                      | Private              |    11 |    3 |    2 |    1 |    2 |    0 |    1 |    1 |    1 |    0 |     0 |
| UNIVERSITY OF PERPETUAL HELP - RIZAL                                                  | Private              |    11 |    4 |    0 |    1 |    1 |    0 |    0 |    2 |    3 |    0 |     0 |
| CHRIST THE KING COLLEGE - CALBAYOG CITY                                               | Private              |    11 |    2 |    0 |    2 |    3 |    1 |    0 |    0 |    0 |    2 |     1 |
| RUTGERS UNIVERSITY NEW JERSEY                                                         | Foreign              |    11 |    0 |    0 |    0 |    0 |    1 |    1 |    2 |    3 |    2 |     2 |
| PHILIPPINE NORMAL COLLEGE TAFT AVENUE MANILA                                          | Public               |    11 |    0 |    2 |    0 |    0 |    2 |    3 |    0 |    3 |    0 |     1 |
| HUACHIEW CHALERMPRAKIET UNIVERSITY                                                    | Foreign              |    11 |    0 |    1 |    4 |    1 |    1 |    0 |    2 |    0 |    0 |     2 |
| KIDAPAWAN DOCTORS COLLEGE INC.                                                        | Private              |    11 |    1 |    1 |    4 |    0 |    0 |    1 |    2 |    0 |    0 |     2 |
| UNIVERSITY OF SAN FRANCISCO                                                           | Foreign              |    11 |    0 |    0 |    0 |    2 |    1 |    0 |    1 |    2 |    3 |     2 |
| FOUNDATION UNIVERSITY                                                                 | Private              |    11 |    1 |    0 |    0 |    2 |    2 |    1 |    0 |    1 |    2 |     1 |
| FELLOWSHIP BAPTIST COLLEGE                                                            | Private              |    11 |    2 |    0 |    0 |    1 |    2 |    0 |    1 |    1 |    2 |     2 |
| DR. CARLOS LANTING COLLEGE - NOVALICHES QUEZON CITY                                   | Private              |    11 |    4 |    1 |    1 |    2 |    0 |    1 |    0 |    1 |    0 |     1 |
| CORDILLERA CAREER DEVELOPMENT COLLEGE                                                 | Private              |    11 |    1 |    0 |    0 |    0 |    3 |    1 |    3 |    1 |    0 |     2 |
| UNIVERSITY OF CENTRAL FLORIDA                                                         | Foreign              |    10 |    2 |    1 |    0 |    1 |    1 |    1 |    1 |    2 |    0 |     1 |
| UNIVERSITY OF GUAM                                                                    | Foreign              |    10 |    1 |    1 |    0 |    3 |    1 |    0 |    0 |    1 |    3 |     0 |
| NOTRE DAME OF KIDAPAWAN COLLEGE                                                       | Private              |    10 |    2 |    2 |    0 |    1 |    3 |    1 |    1 |    0 |    0 |     0 |
| MARY HELP OF CHRISTIANS COLLEGE SEMINARY                                              | Private              |    10 |    1 |    5 |    2 |    1 |    1 |    0 |    0 |    0 |    0 |     0 |
| JOSE RIZAL UNIVERSITY                                                                 | Private              |    10 |    0 |    1 |    0 |    2 |    1 |    2 |    0 |    1 |    3 |     0 |
| COLUMBAN COLLEGE - OLONGAPO CITY                                                      | Private              |    10 |    1 |    1 |    0 |    1 |    2 |    1 |    0 |    1 |    1 |     2 |
| RUTGERS UNIVERSITY                                                                    | Foreign              |    10 |    1 |    0 |    0 |    0 |    0 |    2 |    1 |    1 |    2 |     3 |
| POLYTECHNIC COLLEGE OF DAVAO DEL SUR                                                  | Private              |    10 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |     5 |
| UNIVERSITAS ADVENT INDONESIA                                                          | Foreign              |    10 |    1 |    2 |    1 |    0 |    1 |    0 |    2 |    1 |    1 |     1 |
| CAMARINES NORTE STATE COLLEGE - MAIN                                                  | Public               |    10 |    1 |    2 |    1 |    1 |    0 |    0 |    1 |    1 |    2 |     1 |
| SIENA COLLEGE OF TAYTAY                                                               | Private              |    10 |    0 |    2 |    0 |    1 |    0 |    1 |    1 |    3 |    1 |     0 |
| ST. LUKE'S SCHOOL OF MEDICINE INDIA                                                   | Private              |    10 |    2 |    0 |    2 |    1 |    3 |    1 |    1 |    0 |    0 |     0 |
| BROKENSHIRE COLLEGE SOCSKSARGEN                                                       | Private              |    10 |    2 |    3 |    0 |    1 |    0 |    1 |    0 |    0 |    0 |     3 |
| UM TAGUM COLLEGE                                                                      | Private              |    10 |    1 |    0 |    2 |    1 |    0 |    1 |    0 |    2 |    0 |     2 |
| SULTAN KUDARAT STATE UNIVERSITY - TACURONG                                            | Public               |    10 |    2 |    1 |    2 |    1 |    2 |    0 |    0 |    0 |    1 |     0 |
| SULTAN KUDARAT STATE UNIVERSITY - MAIN                                                | Public               |    10 |    3 |    1 |    1 |    0 |    2 |    2 |    1 |    0 |    0 |     0 |
| VIRGINIA COMMONWEALTH UNIVERSITY                                                      | Foreign              |     9 |    0 |    0 |    0 |    0 |    0 |    1 |    2 |    2 |    2 |     2 |
| SAN SEBASTIAN COLLEGE - RECOLETOS CANLUBANG                                           | Private              |     9 |    2 |    0 |    0 |    1 |    1 |    0 |    1 |    2 |    0 |     1 |
| Texila American University                                                            | Not Specified        |     9 |    1 |    2 |    0 |    0 |    2 |    0 |    0 |    2 |    2 |     0 |
| STONY BROOK UNIVERSITY                                                                | Foreign              |     9 |    0 |    2 |    0 |    1 |    0 |    2 |    0 |    1 |    1 |     2 |
| SAN SEBASTIAN COLLEGE - RECOLETOS DE CAVITE                                           | Private              |     9 |    1 |    1 |    1 |    3 |    1 |    0 |    0 |    0 |    1 |     1 |
| WESTERN VISAYAS COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                              | Public               |     9 |    2 |    0 |    0 |    1 |    1 |    0 |    1 |    2 |    1 |     1 |
| NUEVA ECIJA UNIVERSITY OF SCIENCE AND TECHNOLOGY - MAIN                               | Public               |     9 |    0 |    2 |    0 |    1 |    1 |    0 |    3 |    1 |    0 |     1 |
| UNIVERSITY OF ILLINOIS CHICAGO                                                        | Foreign              |     9 |    1 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |    3 |     3 |
| UNIVERSITY OF CALIFORNIA AT STA. CRUZ U.S.A.                                          | Foreign              |     9 |    1 |    1 |    1 |    0 |    1 |    0 |    3 |    1 |    1 |     0 |
| ISABELA STATE UNIVERSITY - ILAGAN                                                     | Public               |     9 |    0 |    0 |    0 |    1 |    1 |    1 |    0 |    2 |    2 |     2 |
| JOSE RIZAL MEMORIAL STATE UNIVERSITY - MAIN                                           | Public               |     9 |    1 |    3 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     1 |
| KALAYAAN COLLEGE                                                                      | Private              |     9 |    2 |    1 |    1 |    0 |    1 |    1 |    0 |    2 |    0 |     1 |
| DOMINICAN COLLEGE BLUM SAN JUAN MM                                                    | Private              |     9 |    1 |    2 |    3 |    1 |    0 |    1 |    0 |    0 |    1 |     0 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                  | Public               |     9 |    2 |    1 |    0 |    0 |    1 |    1 |    2 |    1 |    1 |     0 |
| MINDANAO MEDICAL FOUNDATION COLLEGE DAVAO                                             | Private              |     9 |    4 |    1 |    1 |    0 |    2 |    0 |    1 |    0 |    0 |     0 |
| UNIVERSITY OF RIZAL SYSTEM - MORONG                                                   | Public               |     9 |    1 |    1 |    1 |    1 |    0 |    1 |    0 |    2 |    1 |     1 |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - LAGUNA COLLEGE OF ARTS AND TRADES - STA. CRUZ   | Public               |     9 |    0 |    1 |    0 |    0 |    3 |    0 |    1 |    2 |    1 |     1 |
| NOTRE DAME OF MARBEL COLLEGE SOUTH COTABATO                                           | Private              |     9 |    0 |    2 |    1 |    2 |    2 |    0 |    0 |    2 |    0 |     0 |
| LA SALLE COLLEGE - ANTIPOLO                                                           | Private              |     9 |    3 |    2 |    0 |    1 |    1 |    0 |    0 |    0 |    1 |     1 |
| BURAPHA UNIVERSITY                                                                    | Foreign              |     9 |    4 |    3 |    1 |    0 |    0 |    0 |    1 |    0 |    0 |     0 |
| CALIFORNIA STATE UNIVERSITY FRESNO                                                    | Foreign              |     9 |    3 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     2 |
| CALIFORNIA STATE UNIVERSITY LONG BEACH                                                | Foreign              |     9 |    2 |    1 |    0 |    1 |    0 |    1 |    0 |    0 |    2 |     1 |
| DELOS SANTOS COLLEGE                                                                  | Private              |     9 |    1 |    1 |    1 |    1 |    2 |    2 |    0 |    1 |    0 |     0 |
| CHIANG KAI SHEK COLLEGE                                                               | Private              |     9 |    0 |    0 |    2 |    1 |    1 |    1 |    0 |    2 |    2 |     0 |
| CENTRO ESCOLAR UNIVERSITY-MALOLOS BULACAN                                             | Private              |     9 |    0 |    2 |    1 |    4 |    2 |    0 |    0 |    0 |    0 |     0 |
| PATTS COLLEGE OF AERONAUTICS                                                          | Private              |     9 |    0 |    0 |    3 |    0 |    2 |    0 |    0 |    2 |    0 |     2 |
| UNIVERSITY OF HAWAII AT MANOA                                                         | Foreign              |     9 |    1 |    0 |    0 |    0 |    2 |    0 |    1 |    1 |    1 |     2 |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-ALABANG ZAPOTE                              | Private              |     9 |    2 |    1 |    1 |    3 |    1 |    0 |    0 |    0 |    1 |     0 |
| UNIVERSITY OF BRITISH COLUMBIA                                                        | Foreign              |     8 |    3 |    0 |    2 |    1 |    0 |    0 |    0 |    2 |    0 |     0 |
| THAMMASAT UNIV.                                                                       | Foreign              |     8 |    3 |    0 |    3 |    1 |    0 |    1 |    0 |    0 |    0 |     0 |
| UNIVERSITY OF CEBU - LAPULAPU AND MANDAUE                                             | Private              |     8 |    0 |    0 |    1 |    0 |    2 |    1 |    1 |    0 |    1 |     2 |
| MINDANAO UNIVERSITY OF SCIENCE AND TECHNOLOGY                                         | Public               |     8 |    0 |    1 |    1 |    0 |    1 |    1 |    1 |    1 |    2 |     0 |
| UNIVERSITY OF NORTHERN PHILIPPINES VIGAN ILOCOS SUR                                   | Public               |     8 |    4 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |     0 |
| MAPANDI MEMORIAL COLLEGE                                                              | Private              |     8 |    1 |    0 |    1 |    2 |    2 |    1 |    0 |    0 |    0 |     1 |
| UNIVERSITY OF THE ASSUMPTION PAMPANGA                                                 | Private              |     8 |    0 |    3 |    1 |    0 |    1 |    0 |    0 |    0 |    3 |     0 |
| RAMKHAMHAENG UNIVERSITY                                                               | Foreign              |     8 |    1 |    0 |    1 |    0 |    1 |    1 |    0 |    1 |    2 |     1 |
| PHILIPPINE WOMEN'S COLLEGE OF DAVAO                                                   | Private              |     8 |    0 |    0 |    2 |    3 |    0 |    0 |    0 |    2 |    1 |     0 |
| PRINCE OF SONGKLA UNIVERSITY                                                          | Foreign              |     8 |    1 |    0 |    0 |    3 |    1 |    1 |    0 |    1 |    1 |     0 |
| ALDERSGATE COLLEGE                                                                    | Private              |     8 |    2 |    1 |    1 |    0 |    0 |    2 |    0 |    0 |    0 |     2 |
| ST. JOSEPH COLLEGE CAVITE                                                             | Private              |     8 |    3 |    2 |    0 |    0 |    2 |    1 |    0 |    0 |    0 |     0 |
| U.P. VISAYAS (TACLOBAN CITY LEYTE)                                                    | Public               |     8 |    0 |    1 |    0 |    0 |    1 |    0 |    2 |    2 |    2 |     0 |
| LA CONSOLACION COLLEGE - DAET                                                         | Private              |     8 |    0 |    2 |    0 |    0 |    0 |    1 |    1 |    0 |    2 |     2 |
| ENDERUN COLLEGE                                                                       | Private              |     8 |    2 |    1 |    1 |    1 |    0 |    1 |    1 |    1 |    0 |     0 |
| FELIPE R. VERALLO MEMORIAL FOUNDATION - BOGO                                          | Private              |     8 |    0 |    1 |    0 |    0 |    1 |    0 |    1 |    2 |    2 |     1 |
| UNIVERSITY OF TEXAS                                                                   | Foreign              |     8 |    0 |    0 |    0 |    0 |    1 |    1 |    1 |    0 |    0 |     4 |
| COLLEGE OF ST. JOHN - ROXAS                                                           | Private              |     8 |    2 |    2 |    0 |    1 |    1 |    0 |    1 |    0 |    0 |     0 |
| 13155D                                                                                | Not Specified        |     8 |    1 |    1 |    1 |    0 |    0 |    1 |    0 |    2 |    1 |     1 |
| UNIVERSITY OF CALIFORNIA SANTA CRUZ                                                   | Foreign              |     8 |    2 |    0 |    0 |    0 |    1 |    0 |    0 |    2 |    1 |     2 |
| KESTER GRANT COLLEGE PHILS. INC.                                                      | Private              |     7 |    1 |    3 |    1 |    1 |    0 |    0 |    1 |    0 |    0 |     0 |
| BICOL COLLEGE                                                                         | Private              |     7 |    0 |    1 |    0 |    0 |    1 |    2 |    0 |    2 |    0 |     1 |
| CATANDUANES STATE COLLEGE                                                             | Public               |     7 |    4 |    0 |    1 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| University Of Port Harcourt                                                           | Not Specified        |     7 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    1 |     2 |
| DR. JOSE FABELLA MEMORIAL HOSPITAL SCHOOL OF MIDWIFERY                                | Private              |     7 |    0 |    0 |    1 |    1 |    1 |    0 |    0 |    1 |    1 |     2 |
| COLLEGE OF THE IMMACULATE CONCEPTION                                                  | Private              |     7 |    2 |    1 |    0 |    0 |    2 |    1 |    0 |    0 |    0 |     1 |
| CONCORDIA COLLEGE                                                                     | Private              |     7 |    0 |    2 |    0 |    0 |    3 |    1 |    1 |    0 |    0 |     0 |
| DAVAO CENTRAL COLLEGE                                                                 | Private              |     7 |    1 |    0 |    0 |    1 |    1 |    1 |    0 |    1 |    1 |     0 |
| HOLY TRINITY COLLEGE PUERTO PRINCESA                                                  | Private              |     7 |    0 |    2 |    2 |    0 |    0 |    2 |    1 |    0 |    0 |     0 |
| NORTHEASTERN COLLEGE                                                                  | Private              |     7 |    1 |    0 |    1 |    0 |    1 |    1 |    0 |    1 |    0 |     1 |
| UNIVERSITY OF IMMACULATE CONCEPTION-DAVAO CITY                                        | Private              |     7 |    2 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |     0 |
| NEGROS ORIENTAL STATE UNIVERSITY                                                      | Public               |     7 |    2 |    3 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |     0 |
| EASTERN SAMAR STATE UNIVERSITY - MAIN                                                 | Public               |     7 |    1 |    0 |    0 |    0 |    0 |    4 |    0 |    0 |    1 |     1 |
| UNIVERSITY OF LUZON ( DAGUPAN CITY )                                                  | Private              |     7 |    3 |    0 |    2 |    1 |    1 |    0 |    0 |    0 |    0 |     0 |
| MALASIQUI AGNO VALLEY COLLEGE - MALASIQUI PANGASINAN                                  | Private              |     7 |    4 |    0 |    1 |    1 |    0 |    0 |    0 |    1 |    0 |     0 |
| INTERNATIONAL COLLEGES OF ASIA - TAMBAC PANGASINAN                                    | Private              |     7 |    1 |    0 |    4 |    0 |    0 |    0 |    1 |    1 |    0 |     0 |
| NAVAL STATE UNIVERSITY - MAIN                                                         | Public               |     7 |    0 |    1 |    0 |    2 |    0 |    0 |    0 |    1 |    2 |     1 |
| OLIVAREZ COLLEGE - TAGAYTAY                                                           | Private              |     7 |    0 |    1 |    2 |    0 |    1 |    0 |    0 |    1 |    1 |     1 |
| WEST NEGROS COLLEGE BACOLOD                                                           | Private              |     7 |    3 |    1 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |     0 |
| SAFFRULLAH M. DIPATUAN FOUNDATION ACADEMY                                             | Private              |     7 |    2 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |    0 |     3 |
| THE COLLEGE OF MAASIN                                                                 | Private              |     7 |    1 |    0 |    2 |    0 |    0 |    0 |    1 |    0 |    1 |     2 |
| SAINT LOUIS COLLEGE - CITY OF SAN FERNANDO                                            | Private              |     7 |    1 |    0 |    0 |    1 |    2 |    0 |    1 |    0 |    1 |     0 |
| SAINT LOUIS COLLEGE                                                                   | Private              |     7 |    2 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |     1 |
| SAN SEBASTIAN COLLEGE                                                                 | Private              |     7 |    0 |    3 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |     0 |
| COTABATO MEDICAL FOUNDATION COLLEGE                                                   | Private              |     7 |    1 |    1 |    1 |    0 |    0 |    1 |    1 |    1 |    0 |     1 |
| PANPACIFIC UNIVERSITY NORTH PHILIPPINES - URDANETA CITY                               | Private              |     7 |    1 |    1 |    0 |    1 |    1 |    0 |    1 |    1 |    1 |     0 |
| PAMANTASAN NG LUNGSOD NG PASAY                                                        | Public               |     7 |    0 |    2 |    1 |    1 |    2 |    0 |    0 |    1 |    0 |     0 |
| UNIVERSITY OF CALIFORNIA MERCED                                                       | Foreign              |     7 |    1 |    0 |    1 |    0 |    2 |    1 |    1 |    1 |    0 |     0 |
| UNIVERSITY OF HOUSTON                                                                 | Foreign              |     7 |    2 |    0 |    0 |    1 |    0 |    0 |    1 |    0 |    2 |     1 |
| SAINT MARY'S COLLEGE OF SAN JUAN                                                      | Private              |     7 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| ASSUMPTION UNIVERSITY                                                                 | Foreign              |     6 |    0 |    0 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |     1 |
| Christian University Of Thailand                                                      | Not Specified        |     6 |    0 |    1 |    0 |    2 |    1 |    0 |    0 |    0 |    0 |     0 |
| COR JESU COLLEGE                                                                      | Private              |     6 |    1 |    0 |    0 |    1 |    1 |    1 |    0 |    0 |    1 |     1 |
| UNIVERSITY OF SOUTH FLORIDA USA                                                       | Foreign              |     6 |    0 |    1 |    1 |    0 |    1 |    1 |    1 |    0 |    1 |     0 |
| ASIA-PACIFIC INTERNATIONAL UNIVERSITY                                                 | Private              |     6 |    0 |    0 |    0 |    1 |    1 |    0 |    2 |    1 |    0 |     0 |
| BATAAN PENINSULA STATE UNIVERSITY                                                     | Public               |     6 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    1 |     0 |
| Adventist University Of Indonesia                                                     | Not Specified        |     6 |    1 |    0 |    0 |    1 |    1 |    0 |    0 |    2 |    0 |     1 |
| CHIANGMAI UNIVERSITY                                                                  | Foreign              |     6 |    0 |    0 |    2 |    1 |    0 |    0 |    0 |    1 |    0 |     2 |
| ARRIESGADO COLLEGE FOUNDATION                                                         | Private              |     6 |    1 |    0 |    1 |    0 |    1 |    1 |    0 |    2 |    0 |     0 |
| ST. JOSEPH COLLEGE AMAYA                                                              | Private              |     6 |    1 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |    2 |     1 |
| ST. MARY'S UNIVERSITY NUEVA VIZCAYA                                                   | Private              |     6 |    0 |    3 |    0 |    1 |    1 |    0 |    1 |    0 |    0 |     0 |
| THE NATIONAL TEACHERS COLLEGE                                                         | Private              |     6 |    1 |    1 |    0 |    0 |    0 |    0 |    1 |    1 |    0 |     2 |
| ST. BERNADETTE OF LOURDES COLLEGE                                                     | Private              |     6 |    1 |    1 |    0 |    0 |    0 |    2 |    1 |    1 |    0 |     0 |
| ST. ANTHONY COLLEGE OF ROXAS CITY CAPIZ                                               | Private              |     6 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    1 |    0 |     0 |
| AGO MEDICAL EDUCATIONAL FOUNDATION LEGASPI CITY                                       | Private              |     6 |    0 |    2 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |     0 |
| AMA COMPUTER COLLEGE - TUGUEGARAO CITY                                                | Private              |     6 |    0 |    0 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |     1 |
| SAN DIEGO STATE UNIVERSITY - CALIFORNIA U.S.A.                                        | Foreign              |     6 |    0 |    1 |    0 |    1 |    0 |    2 |    1 |    1 |    0 |     0 |
| SAN ISIDRO COLLEGE                                                                    | Private              |     6 |    1 |    1 |    0 |    2 |    1 |    0 |    0 |    0 |    0 |     1 |
| UNIVERSITY AT BUFFALO                                                                 | Foreign              |     6 |    1 |    0 |    0 |    1 |    1 |    0 |    1 |    0 |    0 |     1 |
| ANGELES SYSTEMS PLUS COMPUTER COLLEGE                                                 | Private              |     6 |    0 |    1 |    1 |    1 |    2 |    0 |    0 |    0 |    0 |     1 |
| ILOCOS SUR POLYTECHNIC STATE COLLEGE                                                  | Public               |     6 |    0 |    0 |    2 |    0 |    1 |    1 |    1 |    1 |    0 |     0 |
| KHON KAEN UNIVERSITY                                                                  | Foreign              |     6 |    1 |    2 |    0 |    0 |    1 |    0 |    0 |    1 |    0 |     1 |
| COLEGIO DE KIDAPAWAN                                                                  | Private              |     6 |    0 |    1 |    0 |    0 |    1 |    1 |    0 |    1 |    1 |     1 |
| CALIFORNIA STATE UNIVERSITY - FULLERTON                                               | Foreign              |     6 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    4 |    1 |     0 |
| SOUTHERN LUZON POLYTECHNIC COLLEGE - LUCBAN QUEZON                                    | Private              |     6 |    1 |    1 |    1 |    3 |    0 |    0 |    0 |    0 |    0 |     0 |
| LADOKE AKINTOLA UNIVERSITY OF TECHNOLOGY OGBOMOSO                                     | Foreign              |     6 |    2 |    1 |    1 |    0 |    0 |    1 |    0 |    1 |    0 |     0 |
| MAHASARAKHAM UNIVERSITY                                                               | Foreign              |     6 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |     0 |
| OUR LADY OF THE PILLAR COLLEGE - CAUAYAN                                              | Private              |     6 |    2 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    1 |     0 |
| LYCEUM NORTHWESTERN - FLORENCIA T. DUQUE COLLEGE                                      | Private              |     6 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |     0 |
| NOVAGEN COLLEGE OF QUEZON CITY                                                        | Private              |     6 |    3 |    0 |    1 |    0 |    0 |    1 |    0 |    1 |    0 |     0 |
| LEYTE NORMAL UNIVERSITY TACLOBAN CITY                                                 | Public               |     6 |    2 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |     0 |
| RUNGSIT UNIVERSITY                                                                    | Foreign              |     6 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |     2 |
| UNIVERSITY OF MARYLAND - MARYLAND U.S.A.                                              | Foreign              |     6 |    0 |    0 |    1 |    1 |    1 |    0 |    0 |    1 |    1 |     1 |
| OUR LADY OF FATIMA NOVALICHES                                                         | Private              |     6 |    0 |    3 |    1 |    0 |    0 |    1 |    1 |    0 |    0 |     0 |
| PHILIPPINE NORMAL UNIVERSITY - AGUSAN                                                 | Public               |     6 |    0 |    1 |    1 |    1 |    1 |    0 |    1 |    0 |    1 |     0 |
| MAHARDIKA INSTITUTE OF TECHNOLOGY                                                     | Private              |     6 |    1 |    0 |    1 |    0 |    0 |    1 |    1 |    1 |    1 |     0 |
| KASETSART UNIVERSITY                                                                  | Foreign              |     6 |    1 |    2 |    0 |    0 |    0 |    1 |    0 |    0 |    0 |     1 |
| UNIVERSITY OF THE IMMACULATE CONCEPTION COLLEGE DAVAO                                 | Private              |     6 |    4 |    1 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     0 |
| EAST AFRICA UNIVERSITY                                                                | Foreign              |     6 |    1 |    0 |    0 |    0 |    0 |    1 |    0 |    1 |    3 |     0 |
| COLEGIO DE SAN LORENZO                                                                | Private              |     6 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    2 |     1 |
| ADVENTIST INDONESIA UNIVERSITY INDONESIA                                              | Foreign              |     5 |    2 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     0 |
| AKLAN POLYTECHNIC COLLEGE                                                             | Private              |     5 |    1 |    1 |    0 |    0 |    0 |    1 |    0 |    0 |    1 |     1 |
| AMA SCHOOL OF MEDICINE - EAST RIZAL                                                   | Private              |     5 |    2 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |     2 |
| SIENA COLLEGE-TAYTAY                                                                  | Private              |     5 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |     1 |
| SIAM UNIVERSITY                                                                       | Foreign              |     5 |    3 |    0 |    0 |    0 |    0 |    1 |    0 |    0 |    1 |     0 |
| UNIV. OF ASIA AND THE PACIFIC - PASIG CITY                                            | Private              |     5 |    0 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    2 |     1 |
| SRI CHAITANYA JUNIOR COLLEGE                                                          | Foreign              |     5 |    1 |    0 |    0 |    1 |    0 |    1 |    0 |    2 |    0 |     0 |
| ST. ANDREW'S INTERNATIONAL ACADEMY INDIA                                              | Foreign              |     5 |    3 |    0 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |     0 |
| TEMPLE UNIVERSITY USA                                                                 | Foreign              |     5 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |    1 |    1 |     0 |
| SUNRISE UNIVERSITY                                                                    | Foreign              |     5 |    1 |    0 |    0 |    1 |    1 |    1 |    0 |    1 |    0 |     0 |
| TRACE COLLEGE                                                                         | Private              |     5 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    2 |    1 |     0 |
| TECHNOLOGICAL UNIVERSITY OF THE PHILIPPINES - AYALA BLVD. MANILA                      | Public               |     5 |    1 |    0 |    0 |    0 |    2 |    1 |    0 |    0 |    0 |     0 |
| Sti - College Davao                                                                   | Not Specified        |     5 |    2 |    1 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |     0 |
| RUTGERS COLLEGE NEW JERSEY                                                            | Foreign              |     5 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |    1 |     3 |
| UNIVERSITY OF BRITISH COLUMBIA CANADA                                                 | Foreign              |     5 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |    0 |    0 |     4 |
| RAMKHAMHAENG UNIV.                                                                    | Foreign              |     5 |    5 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     0 |
| SAINT MICHAEL'S COLLEGE OF LAGUNA                                                     | Private              |     5 |    0 |    1 |    0 |    0 |    1 |    1 |    0 |    0 |    1 |     1 |
| PAMANTASAN NG LUNGSOD NG MUNTINLUPA                                                   | Public               |     5 |    0 |    1 |    1 |    0 |    0 |    0 |    1 |    1 |    1 |     0 |
| UNIVERSITY OF CONNECTICUT                                                             | Foreign              |     5 |    0 |    1 |    0 |    0 |    2 |    0 |    0 |    1 |    0 |     1 |
| LUNA GOCO COLLEGES                                                                    | Private              |     5 |    0 |    1 |    0 |    1 |    0 |    0 |    1 |    0 |    2 |     0 |
| LIPA CITY COLLEGES BATANGAS                                                           | Private              |     5 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    1 |    0 |     0 |
| MOGADISHU UNIVERSITY                                                                  | Foreign              |     5 |    1 |    0 |    0 |    1 |    0 |    1 |    2 |    0 |    0 |     0 |
| UNIVERSITY OF NEVADA - RENO                                                           | Foreign              |     5 |    0 |    1 |    1 |    0 |    0 |    1 |    0 |    0 |    0 |     1 |
| UNIVERSITY OF NEW ENGLAND                                                             | Foreign              |     5 |    1 |    1 |    0 |    0 |    1 |    1 |    0 |    0 |    0 |     1 |
| UNIVERSITY OF NORTHERN PHILIPPINES-CANDON - CITY OF CANDON ILOCOS SUR                 | Public               |     5 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     0 |
| NEW YORK UNIVERSITY NY USA                                                            | Foreign              |     5 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    2 |     2 |
| NEW SINAI SCHOOL AND COLLEGES STA. ROSA                                               | Private              |     5 |    0 |    0 |    1 |    2 |    0 |    1 |    0 |    0 |    0 |     0 |
| UNIVERSITY OF MICHIGAN                                                                | Foreign              |     5 |    0 |    0 |    0 |    0 |    1 |    0 |    1 |    2 |    1 |     0 |
| Qiqihar Medical University                                                            | Not Specified        |     5 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |     0 |
| UNIVERSITY OF CALOOCAN CITY                                                           | Public               |     5 |    0 |    1 |    0 |    2 |    0 |    0 |    0 |    0 |    1 |     1 |
| PAMPANGA AGRICULTURAL COLLEGE                                                         | Public               |     5 |    1 |    1 |    0 |    1 |    0 |    1 |    0 |    0 |    0 |     0 |
| PENSACOLA CHRISTIAN COLLEGE                                                           | Foreign              |     5 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |     2 |
| PALAWAN POLYTECHNIC COLLEGE                                                           | Private              |     5 |    1 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |    1 |     0 |
| EULOGIO AMANG RODRIGUEZ INSTITUTE OF SCIENCE AND TECHNOLOGY                           | Public               |     5 |    0 |    1 |    0 |    0 |    1 |    0 |    0 |    2 |    0 |     0 |
| FEU - FERN COLLEGE                                                                    | Private              |     5 |    0 |    2 |    0 |    0 |    1 |    0 |    1 |    1 |    0 |     0 |
| UNIVERSITY OF TEXAS AT ARLINGTON                                                      | Foreign              |     5 |    2 |    1 |    0 |    0 |    0 |    1 |    0 |    0 |    0 |     1 |
| FL VARGAS COLLEGE - TUGUEGARAO                                                        | Private              |     5 |    0 |    2 |    1 |    0 |    0 |    1 |    0 |    0 |    1 |     0 |
| DR. DOMINGO B. TAMONDONG MEMORIAL SCHOOL                                              | Private              |     5 |    0 |    0 |    2 |    1 |    0 |    0 |    0 |    1 |    1 |     0 |
| EASTERN VISAYAS STATE UNIVERSITY                                                      | Public               |     5 |    0 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |     2 |
| KITASATO UNIVERSITY                                                                   | Foreign              |     5 |    0 |    0 |    0 |    1 |    0 |    2 |    0 |    0 |    1 |     1 |
| KHON KAEN UNIVERSITY THAILAND                                                         | Foreign              |     5 |    1 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |     0 |
| CHAING MAI UNIVERSITY-THAILAND                                                        | Foreign              |     5 |    1 |    1 |    1 |    0 |    0 |    1 |    0 |    0 |    0 |     0 |
| COLEGIO DE SAN JUAN DE LETRAN MANILA                                                  | Private              |     5 |    0 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    1 |     0 |
| CAVITE STATE UNIVERSITY CAVITE                                                        | Public               |     5 |    0 |    0 |    1 |    1 |    0 |    1 |    0 |    1 |    0 |     1 |
| CENTRAL COLLEGE OF PANGASINAN - SAN CARLOS CITY PANGASINAN                            | Private              |     5 |    0 |    0 |    0 |    2 |    1 |    0 |    0 |    2 |    0 |     0 |
| CAGAYAN DE ORO COLLEGE                                                                | Private              |     5 |    2 |    0 |    0 |    1 |    0 |    0 |    1 |    1 |    0 |     0 |
| BATANGAS STATE UNIVERSITY BATANGAS CITY                                               | Public               |     5 |    0 |    0 |    2 |    0 |    1 |    0 |    1 |    0 |    0 |     1 |
| ARIZONA STATE UNIVERSITY                                                              | Foreign              |     5 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |    2 |     0 |
| ASIAN COLLEGE OF SCIENCE AND TECHNOLOGY - CUBAO                                       | Private              |     5 |    0 |    0 |    0 |    0 |    2 |    0 |    1 |    0 |    1 |     1 |
| UNIVERSITY OF WISCONSIN-MADISON                                                       | Foreign              |     5 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |    0 |     3 |
| 13206A                                                                                | Not Specified        |     5 |    0 |    0 |    0 |    0 |    2 |    1 |    0 |    1 |    1 |     0 |

---

*Source: NMAT_Exodus.parquet (Pipeline 4). Observable best-record cohort (Year <= 2014) used for all PLE-linked summaries to avoid misclassifying later cohorts as non-passers before their licensure window closes.*

---



*Report generated by `aggregate_all.py`. All data from NMAT_Exodus.parquet.*
