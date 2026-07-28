# NMAT Performance Evidence for CHED Cut-Off Policy Review

> Complete Markdown export generated from the dashboard's underlying computations and data tables. This document mirrors all six dashboard tabs.

**Scope:** Descriptive evidence from NMAT_Exodus.parquet (178,927 examinee records, 2006-2018) to inform the CMO amendment on NMAT cut-off scores. PLE-linked analyses use the observable cohort (Year <= 2014) to avoid right-censoring bias.

**Definitions:**
- **Best-record examinees** — one NMAT record per person (removes repeat-taker inflation).
- **Observable cohort** — examinees with Year <= 2014, who have had time to take the PLE.
- **Score bins** — B1 (0-9) through B10 (90-100). B4+ means at or above Bin 4 (30th-39th). B5+ means at or above Bin 5 (40th-49th).
- **NMAT-to-PLE linkage** — the proportion of NMAT examinees who were later matched to PLE passer records. This is NOT a PLE pass rate. The dataset does not contain all PLE takers or PLE failures.
- **Foreign examinee counts** — these are NMAT examinees, not enrolled medical students.
- **All score summaries use recalculated TRUE raw scores** — the original stored total was inconsistent for 42.2% of records and has been corrected.

---


# Tab 1 — National Profile

| Metric | Value |
|--------|-------|
| Best-record examinees | 133,804 |
| Unique persons (PERSON_KEY) | 133,558 |
| NMAT years covered | 13 |
| Median percentile rank | 50.0 |

---


## Annual Trend Chart Data


### Examinee Volume by Year / Median Bin Rank by Year

Two-panel chart: examinee count (bar) and median bin rank (line) by NMAT year.

|   Year |   Examinees |   Median percentile rank |   Median TRUE raw score |
|-------:|------------:|-------------------------:|------------------------:|
|   2006 |       3,665 |                       53 |                     131 |
|   2007 |       3,660 |                       52 |                     130 |
|   2008 |       4,849 |                       54 |                     129 |
|   2009 |       6,881 |                       52 |                     129 |
|   2010 |       8,008 |                       57 |                     135 |
|   2011 |       8,731 |                       52 |                     129 |
|   2012 |       9,145 |                       53 |                     121 |
|   2013 |       9,121 |                       59 |                     128 |
|   2014 |      10,441 |                       57 |                     120 |
|   2015 |      10,402 |                       52 |                     118 |
|   2016 |      12,609 |                       48 |                     123 |
|   2017 |      23,955 |                       44 |                     118 |
|   2018 |      22,337 |                       43 |                     111 |


---


## University Type Composition

| UNI_TYPE      |   Count |   Share (%) |
|:--------------|--------:|------------:|
| Private       | 102,888 |        76.9 |
| Public        |  27,627 |        20.6 |
| Foreign       |   1,894 |         1.4 |
| Not Specified |   1,395 |           1 |

---


## Course Group Composition

| CourseGroup                  |   Count |   Share (%) |
|:-----------------------------|--------:|------------:|
| Medical & Allied             |  63,900 |        47.8 |
| Natural Sciences             |  41,430 |          31 |
| Social & Behavioral Sciences |  16,462 |        12.3 |
| Other                        |   7,983 |           6 |
| Education                    |   3,279 |         2.5 |
| Engineering & Technology     |     750 |         0.6 |

---


## Repeat-Taker Context

Of 133,558 unique examinees, 33,713 (25%) took the NMAT more than once (up to 9 attempts). All threshold counts use each examinee's best-record NMAT attempt to avoid inflating the applicant pool with repeat attempts.


---


## Score Bin Reference

| Bin   | Score Range   | Threshold                 |
|:------|:--------------|:--------------------------|
| B1    | 0-9           |                           |
| B2    | 10-19         |                           |
| B3    | 20-29         |                           |
| B4    | 30-39         | CMO exception floor (B4+) |
| B5    | 40-49         | SUC standard floor (B5+)  |
| B6    | 50-59         |                           |
| B7    | 60-69         |                           |
| B8    | 70-79         |                           |
| B9    | 80-89         |                           |
| B10   | 90-100        |                           |

---

![University Type Composition Pie Chart](../viz/01_uni_type_pie.png)

![Course Group Composition Pie Chart](../viz/01_course_group_pie.png)

![Annual Trend Chart: Examinee Volume and Median Bin Rank](../viz/01_annual_trend.png)


# Tab 2 — B4+ vs B5+ Thresholds


## Score Bin Distribution by NMAT Year

Heatmap values are row percentages. Rows = NMAT years, columns = score bins. Darker red = higher concentration in that bin for that year.

|   Year |   B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |   B9 |   B10 |
|-------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
|   2006 |  8.8 |  8.9 |  9.4 |  9.7 |  9.9 | 10.2 |  9.6 | 10.3 | 10.7 |  12.5 |
|   2007 |  8.9 |  8.5 |  9.8 | 10.8 | 10.2 |  8.3 |  9.7 | 10.4 |   11 |  12.2 |
|   2008 |    9 |  8.5 |  7.9 |  9.6 | 10.1 |   10 | 10.1 |  9.5 | 10.9 |  14.3 |
|   2009 |  8.5 |  9.3 |  9.8 | 10.5 |  9.5 | 10.5 |  9.6 |  9.6 |  9.8 |  12.8 |
|   2010 |  6.5 |  7.9 |  8.9 |  8.9 | 10.5 | 10.3 |  9.2 | 10.3 | 11.6 |    16 |
|   2011 |  6.5 |  8.7 |  9.3 | 11.1 | 12.2 | 10.4 |  9.8 | 10.9 | 10.3 |  10.8 |
|   2012 | 10.9 |  8.8 |    8 |  8.8 | 10.3 |  8.5 |    9 |    9 | 10.1 |  16.7 |
|   2013 | 12.5 |    8 |  6.5 |    7 |  8.3 |  7.2 |  8.6 | 10.3 | 11.6 |    20 |
|   2014 | 12.9 |  7.1 |  6.9 |  7.4 |  8.3 |  8.4 |  9.6 | 10.3 | 11.5 |  17.5 |
|   2015 | 14.5 |  7.4 |  7.4 |  7.1 |  9.4 |  9.3 | 10.5 |   10 | 10.5 |    14 |
|   2016 |   14 |  9.5 |  7.9 |  8.5 | 10.5 | 10.8 |  9.7 |   10 | 10.1 |   8.9 |
|   2017 |   13 | 11.7 |  9.9 | 11.2 |  8.7 | 10.2 |  9.3 |  9.3 |  8.9 |   7.7 |
|   2018 | 14.9 | 11.3 |  9.7 | 10.7 |  9.9 |  9.8 |  8.3 |  8.4 |  8.2 |   8.9 |

---


## Examinees Meeting Each Threshold

| Threshold             |   Best-record examinees |   Share of all (%) |   Observable cohort size |
|:----------------------|------------------------:|-------------------:|-------------------------:|
| B4+ (Bin 4 and above) |                  91,409 |               69.9 |                   46,609 |
| B5+ (Bin 5 and above) |                  78,944 |               60.4 |                   40,868 |
| B4 only (Bin 4)       |                  12,465 |                9.5 |                    5,741 |

---


## Threshold Context by University Type

| University Type   |   Best-record examinees | B4+            | B5+            | B4-only      |
|:------------------|------------------------:|:---------------|:---------------|:-------------|
| Public            |                  26,937 | 19,709 (73.2%) | 17,482 (64.9%) | 2,227 (8.3%) |
| Private           |                 100,584 | 69,504 (69.1%) | 59,546 (59.2%) | 9,958 (9.9%) |
| Foreign           |                   1,862 | 1,285 (69.0%)  | 1,109 (59.6%)  | 176 (9.5%)   |
| Not Specified     |                   1,352 | 911 (67.4%)    | 807 (59.7%)    | 104 (7.7%)   |

---


## Public School Examinees and B5+ Threshold

| Metric | Value |
|--------|-------|
| Public B5+ count | 17,482 (64.9%) |
| Public B4-only count | 2,227 (8.3%) |
| Private B5+ count | 59,546 (59.2%) |
| Metric                      | Public         | Private        |
|:----------------------------|:---------------|:---------------|
| Total best-record examinees | 26,937         | 100,584        |
| B5+ (Bin 5+)                | 17,482 (64.9%) | 59,546 (59.2%) |
| B4-only                     | 2,227 (8.3%)   | 9,958 (9.9%)   |
Note: UNI_TYPE refers to the examinee's undergraduate institution, not necessarily the medical school they applied to. GIDA/IP status is not available in this dataset.


---


## Profile of the B4 Group (Bin 4 Only)

| Metric | Value |
|--------|-------|
| B4 examinees (best record) | 12,465 |
| Median TRUE raw score | 109.0 |
| UNI_TYPE      |   count |   share |
|:--------------|--------:|--------:|
| Foreign       |     176 |     1.4 |
| Not Specified |     104 |     0.8 |
| Private       |   9,958 |    79.9 |
| Public        |   2,227 |    17.9 |

---


## Top Bins (B8-B10) vs Bottom Bins (B1-B3) Trend

|   Year |   Top B8-B10 (%) |   Bottom B1-B3 (%) |   Difference (pp) |
|-------:|-----------------:|-------------------:|------------------:|
|   2006 |             33.5 |               27.1 |               6.4 |
|   2007 |             33.6 |               27.2 |               6.4 |
|   2008 |             34.7 |               25.4 |               9.3 |
|   2009 |             32.2 |               27.6 |               4.6 |
|   2010 |             37.9 |               23.3 |              14.6 |
|   2011 |               32 |               24.5 |               7.5 |
|   2012 |             35.8 |               27.7 |               8.1 |
|   2013 |             41.9 |                 27 |              14.9 |
|   2014 |             39.3 |               26.9 |              12.4 |
|   2015 |             34.5 |               29.3 |               5.2 |
|   2016 |               29 |               31.4 |              -2.4 |
|   2017 |             25.9 |               34.6 |              -8.7 |
|   2018 |             25.5 |               35.9 |             -10.4 |

---


## Yearly Examinees Meeting Each Threshold

|   Year |   Total best-record |   B4+ count |   B4+ share (%) |   B5+ count |   B5+ share (%) |   Observable B4+ |   Observable B5+ |
|-------:|--------------------:|------------:|----------------:|------------:|----------------:|-----------------:|-----------------:|
|  2,006 |               3,642 |       2,655 |            72.9 |       2,300 |            63.2 |            2,655 |            2,300 |
|  2,007 |               3,635 |       2,643 |            72.7 |       2,249 |            61.9 |            2,643 |            2,249 |
|  2,008 |               4,831 |       3,603 |            74.6 |       3,137 |            64.9 |            3,603 |            3,137 |
|  2,009 |               6,859 |       4,965 |            72.4 |       4,242 |            61.8 |            4,965 |            4,242 |
|  2,010 |               7,987 |       6,128 |            76.7 |       5,420 |            67.9 |            6,128 |            5,420 |
|  2,011 |               8,679 |       6,552 |            75.5 |       5,589 |            64.4 |            6,552 |            5,589 |
|  2,012 |               8,867 |       6,410 |            72.3 |       5,628 |            63.5 |            6,410 |            5,628 |
|  2,013 |               8,710 |       6,361 |              73 |       5,747 |              66 |            6,361 |            5,747 |
|  2,014 |               9,985 |       7,292 |              73 |       6,556 |            65.7 |            7,292 |            6,556 |
|  2,015 |               9,814 |       6,941 |            70.7 |       6,240 |            63.6 |                0 |                0 |
|  2,016 |              12,270 |       8,413 |            68.6 |       7,373 |            60.1 |                0 |                0 |
|  2,017 |              23,619 |      15,440 |            65.4 |      12,793 |            54.2 |                0 |                0 |
|  2,018 |              21,837 |      14,006 |            64.1 |      11,670 |            53.4 |                0 |                0 |

---


## B5+ PLE-Passer Composition by Year


### B5+ Examinees by PLE Status (Count) — B5+ Examinees by PLE Status (Percent)

Two stacked bar charts showing Count (upper) and Percent (lower) of B5+ examinees by PLE-match status across NMAT years.

|   Year |   Total B5+ observable |   Confirmed PLE passers |   No confirmed PLE match |   Linkage rate (%) |   No-match share (%) |
|-------:|-----------------------:|------------------------:|-------------------------:|-------------------:|---------------------:|
|  2,006 |                  1,435 |                   1,435 |                        0 |                100 |                    0 |
|  2,007 |                  1,352 |                   1,352 |                        0 |                100 |                    0 |
|  2,008 |                  1,953 |                   1,953 |                        0 |                100 |                    0 |
|  2,009 |                  2,432 |                   2,432 |                        0 |                100 |                    0 |
|  2,010 |                  3,059 |                   3,059 |                        0 |                100 |                    0 |
|  2,011 |                  3,084 |                   3,084 |                        0 |                100 |                    0 |
|  2,012 |                  3,283 |                   3,283 |                        0 |                100 |                    0 |
|  2,013 |                  3,311 |                   3,311 |                        0 |                100 |                    0 |
|  2,014 |                  3,448 |                   3,448 |                        0 |                100 |                    0 |

This is NMAT-to-PLE-passer linkage, not a PLE pass rate.


---

![Score Bin Distribution Heatmap by Year](../viz/02_bin_heatmap.png)

![Top Bins vs Bottom Bins Trend](../viz/02_top_bottom_trend.png)

![B4 Examinees by Institution Type](../viz/02_b4_group.png)


# Tab 3 — PLE-Passer Linkage


## PLE Linkage by Score Bin

| Score Bin   | Range   |   N (observable cohort) |   Confirmed PLE Passers |   Linkage Rate (%) |
|:------------|:--------|------------------------:|------------------------:|-------------------:|
| B1          | 0-9     |                   6,104 |                     505 |                8.3 |
| B2          | 10-19   |                   5,254 |                     830 |               15.8 |
| B3          | 20-29   |                   5,228 |                     997 |               19.1 |
| B4          | 30-39   |                   5,741 |                   1,312 |               22.9 |
| B5          | 40-49   |                   6,229 |                   2,882 |               46.3 |
| B6          | 50-59   |                   5,831 |                   2,992 |               51.3 |
| B7          | 60-69   |                   5,942 |                   3,359 |               56.5 |
| B8          | 70-79   |                   6,355 |                   3,819 |               60.1 |
| B9          | 80-89   |                   6,854 |                   4,595 |                 67 |
| B10         | 90-100  |                   9,657 |                   7,352 |               76.1 |

---


## Score Profile by PLE Status

|   ('TotalRawScoreTRUE', 'count') |   ('TotalRawScoreTRUE', 'median') |   ('TotalRawScoreTRUE', 'mean') |   ('TotalRawScoreTRUE', '<lambda_0>') |   ('TotalRawScoreTRUE', '<lambda_1>') |   ('NMS_PER_num', 'count') |   ('NMS_PER_num', 'median') |   ('NMS_PER_num', 'mean') |   ('NMS_PER_num', '<lambda_0>') |   ('NMS_PER_num', '<lambda_1>') |   ('PartIRawScoreTRUE', 'count') |   ('PartIRawScoreTRUE', 'median') |   ('PartIRawScoreTRUE', 'mean') |   ('PartIRawScoreTRUE', '<lambda_0>') |   ('PartIRawScoreTRUE', '<lambda_1>') |   ('PartIIRawScoreTRUE', 'count') |   ('PartIIRawScoreTRUE', 'median') |   ('PartIIRawScoreTRUE', 'mean') |   ('PartIIRawScoreTRUE', '<lambda_0>') |   ('PartIIRawScoreTRUE', '<lambda_1>') |
|---------------------------------:|----------------------------------:|--------------------------------:|--------------------------------------:|--------------------------------------:|---------------------------:|----------------------------:|--------------------------:|--------------------------------:|--------------------------------:|---------------------------------:|----------------------------------:|--------------------------------:|--------------------------------------:|--------------------------------------:|----------------------------------:|-----------------------------------:|---------------------------------:|---------------------------------------:|---------------------------------------:|
|                           35,194 |                               112 |                             115 |                                    94 |                                   134 |                     35,075 |                          36 |                      40.3 |                              15 |                              63 |                           35,194 |                                61 |                            61.3 |                                    51 |                                    72 |                            35,194 |                                 51 |                             53.7 |                                     42 |                                     64 |
|                           29,269 |                               143 |                           144.8 |                                   125 |                                   164 |                     28,646 |                          73 |                      68.6 |                              52 |                              90 |                           29,269 |                                76 |                            75.8 |                                    66 |                                    86 |                            29,269 |                                 68 |                               69 |                                     57 |                                     80 |

---


## PLE-Passer Linkage by NMAT Year

|   Year |      N |   Confirmed |   Linkage Rate (%) |
|-------:|-------:|------------:|-------------------:|
|  2,006 |  3,665 |       2,038 |               55.6 |
|  2,007 |  3,660 |       1,868 |                 51 |
|  2,008 |  4,849 |       2,514 |               51.9 |
|  2,009 |  6,881 |       3,226 |               46.9 |
|  2,010 |  8,008 |       3,808 |               47.5 |
|  2,011 |  8,731 |       3,853 |               44.1 |
|  2,012 |  9,145 |       4,066 |               44.5 |
|  2,013 |  9,121 |       3,951 |               43.3 |
|  2,014 | 10,441 |       3,949 |               37.8 |

---


## PLE-Passer Linkage by Course Group

| CourseGroup                  |      N |   Confirmed |   Median_percentile |   Linkage Rate (%) |
|:-----------------------------|-------:|------------:|--------------------:|-------------------:|
| Education                    |  2,973 |       1,541 |                  52 |               51.8 |
| Engineering & Technology     |    302 |         114 |                  71 |               37.8 |
| Medical & Allied             | 35,433 |      16,061 |                  49 |               45.3 |
| Natural Sciences             | 15,219 |       6,921 |                  66 |               45.5 |
| Other                        |  6,189 |       2,853 |                  55 |               46.1 |
| Social & Behavioral Sciences |  4,385 |       1,783 |                  64 |               40.7 |

---


## PLE-Passer Linkage by University Type

| UNI_TYPE   |      N |   Confirmed |   Median_percentile |   Linkage Rate (%) |
|:-----------|-------:|------------:|--------------------:|-------------------:|
| Foreign    |  1,124 |         248 |                  58 |               22.1 |
| Private    | 48,991 |      21,909 |                  51 |               44.7 |
| Public     | 13,555 |       6,786 |                  68 |               50.1 |
The observed difference in linkage rates between institution types reflects the set of NMAT examinees who were later matched to PLE passer records. The data does not identify the reasons for these differences.


---


## Clean PLE Subset Stress Test

Criteria: IS_BEST_NMAT_RECORD + IS_PLE_ANALYSIS_SAFE + PLE_YEAR_GAP >= 5 + FOREIGNER_STATUS == 'Filipino'

| Metric | Value |
|--------|-------|
| Clean subset (all bins) | 27,151 |
| B5+ in clean subset | 23,357 |
| Share of observable cohort | 36.2% |
| Median PLE year gap | 6 yrs |

### Yearly Clean Subset B5+ Data

|   Year |   total |   confirmed |   no_match |   linkage_pct |
|-------:|--------:|------------:|-----------:|--------------:|
|  2,006 |   1,435 |       1,435 |          0 |           100 |
|  2,007 |   1,352 |       1,352 |          0 |           100 |
|  2,008 |   1,953 |       1,953 |          0 |           100 |
|  2,009 |   2,432 |       2,432 |          0 |           100 |
|  2,010 |   3,059 |       3,059 |          0 |           100 |
|  2,011 |   3,084 |       3,084 |          0 |           100 |
|  2,012 |   3,283 |       3,283 |          0 |           100 |
|  2,013 |   3,311 |       3,311 |          0 |           100 |
|  2,014 |   3,448 |       3,448 |          0 |           100 |

### Clean B5+ by University Type

| UNI_TYPE      |      N |   Share (%) |
|:--------------|-------:|------------:|
| Foreign       |    172 |         0.7 |
| Not Specified |    275 |         1.2 |
| Private       | 17,180 |        73.6 |
| Public        |  5,730 |        24.5 |
This subset uses the strictest defensible criteria. Results mirror the broader analysis.


---

![PLE Linkage Rate by Score Bin](../viz/03_ple_linkage_bin.png)

![PLE Linkage Rate by NMAT Year](../viz/03_ple_linkage_year.png)

![PLE Linkage Rate by Course Group](../viz/03_ple_linkage_course.png)

![PLE Linkage Rate by University Type](../viz/03_ple_linkage_uni.png)


# Tab 4 — Institution and Foreign Context


## Score Summary by University Type

| UNI_TYPE   |   N (best record) |   Median %ile |   Q25 %ile |   Q75 %ile |   Median TRUE raw score |   Median GPS |
|:-----------|------------------:|--------------:|-----------:|-----------:|------------------------:|-------------:|
| Foreign    |             1,894 |            51 |         20 |         79 |                     124 |          504 |
| Private    |           102,888 |            48 |         21 |         74 |                     120 |          497 |
| Public     |            27,627 |            56 |         26 |         83 |                     127 |          517 |

---


## Percentile Rank Distribution by University Type (Box Plot Data)

| University Type   |       N |   Minimum |   Q25 |   Median |   Q75 |   Maximum |
|:------------------|--------:|----------:|------:|---------:|------:|----------:|
| Public            |  27,288 |        -1 |    26 |       56 |    83 |        99 |
| Private           | 102,031 |        -1 |    21 |       48 |    74 |        99 |
| Foreign           |   1,882 |        -1 |    20 |       51 |    79 |        99 |

---


## Score Bin Distribution by University Type

| UNI_TYPE   |   B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |   B9 |   B10 |
|:-----------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| Foreign    | 14.1 |  9.4 |  7.5 |  9.5 |  7.9 |  8.8 |  8.6 |  9.6 | 10.6 |  14.1 |
| Private    | 12.1 |  9.7 |    9 |  9.9 |  9.9 |  9.9 |  9.4 |  9.7 |  9.7 |  10.6 |
| Public     | 10.9 |  8.3 |  7.6 |  8.3 |  8.7 |  8.9 |  9.1 |  9.6 |   11 |  17.7 |

---


## Top-Bin Share (B8-B10) by University Type

| University Type   |   Total Examinees |   Top B8-B10 (%) |   Top B8-B10 Count |
|:------------------|------------------:|-----------------:|-------------------:|
| Foreign           |             1,862 |             34.3 |                638 |
| Private           |           100,584 |               30 |             30,147 |
| Public            |            26,937 |             38.2 |             10,293 |

---


## Foreign Examinee Context

| Metric | Value |
|--------|-------|
| Verified Foreign NMAT examinees (all records) | 32,501 |
| Filipino examinees | 146,413 |
| Distinct foreign nationalities | 90 |

### Top 10 Nationalities

|   Rank | Nationality   |   Count |   Share of verified foreign (%) |
|-------:|:--------------|--------:|--------------------------------:|
|      1 | India         |  26,490 |                            85.1 |
|      2 | Nepal         |   1,158 |                             3.7 |
|      3 | Thailand      |   1,062 |                             3.4 |
|      4 | United States |     839 |                             2.7 |
|      5 | Nigeria       |     639 |                             2.1 |
|      6 | Sri Lanka     |     262 |                             0.8 |
|      7 | Korea (South) |     224 |                             0.7 |
|      8 | Iran          |     162 |                             0.5 |
|      9 | Foreign       |     156 |                             0.5 |
|     10 | Indonesia     |     124 |                             0.4 |
These are NMAT examinees, not enrolled medical students.


---

![Bin Rank Distribution by University Type - Box Plot](../viz/04_uni_box.png)

![Bin Distribution by University Type Heatmap](../viz/04_uni_bin_heatmap.png)

![Top-Bin Share by University Type](../viz/04_top_bin_uni.png)

![Top 10 Foreign Nationalities](../viz/04_foreign_top10.png)


# Tab 5 — Key Evidence for Policy Review

The following findings are descriptive observations based on historical NMAT data (2006-2018). They do not constitute regulatory recommendations.


---


### National Threshold Context

The historical NMAT examinee pool ranges from approximately 70% meeting a B4+ threshold to 60% meeting a B5+ threshold (best-record examinees, 2006-2018). The marginal group between the two thresholds — B4 only — accounts for roughly 10 percentage points of the examinee population.


### Institutional Performance Patterns

Public institution examinees show a higher median bin rank (57) than Private institution examinees (49).


### NMAT-to-PLE-Passer Linkage Gradient

NMAT-to-PLE-passer linkage increases with score bin, from 8% in the lowest bin (B1) to 76% in the highest bin (B10). This is not a PLE pass rate.


### Historical Linkage Trends

The observable NMAT-to-PLE-passer linkage rate declined from 55.6% in 2006 to 37.8% in 2014 across the observable cohort. The 5-year rolling average was 43.5% as of 2014.


### Public School Threshold Attainment

Public school examinees already meet the B5+ threshold at a high rate: 64.9% (17,482 out of 26,937) score at Bin 5 or above. Only 8.3% fall in the B4-only band that the CMO exception addresses.


### PLE Matching Robustness

Using the strictest defensible PLE matching criteria (single best-record, clean deterministic match, >=5 year gap, Filipino nationals only), the analysis yields 23,357 B5+ matched passers representing 36.2% of the observable cohort.


### Foreign Examinee Presence

Foreign nationals represent approximately 18.2% of all NMAT records (32,501 verified foreign records out of 178,927 total). India accounts for the largest share of foreign examinees. These are NMAT examinee counts, not enrolled medical students.


---

**Note on data scope.** These findings are limited to the NMAT examinee population captured in NMAT_Exodus.parquet. Key gaps in the available data include PLE failure rates (only passers are identifiable), GIDA/IP status, medical school admissions and enrollment figures, and institutional admission criteria.


# Tab 6 — Data, Methods, and Limitations


## Dataset Overview

| Metric | Value |
|--------|-------|
| Source file | NMAT_Exodus.parquet (54 columns) |
| Total rows | 178,927 |
| Examination years | 2006-2018 |
| Unique examinees (best record) | 133,558 |
| Observable PLE cohort (Year <= 2014) | 64,501 |
| Repeat takers | 33,713 (25%) |

---


## TRUE Raw Score Recalculation

The pipeline recalculated all raw scores from the 8 individual subtest components because 42.2% of the original stored totals were incorrect. All analyses use the recalculated TotalRawScoreTRUE scores.

| Metric | Value |
|--------|-------|
| Rows with complete TRUE scores | 178,882 (99.97%) |
| Formula mismatches (Total != Part I + Part II) | 0 |

---


## Best-Record Deduplication

33,713 examinees (25%) took the NMAT more than once (up to 9 attempts). Person-level analyses use the best-record flag (IS_BEST_NMAT_RECORD), which selects:

- For PLE passers: the specific NMAT attempt that matched to the PLE record.

- For others: the highest percentile attempt, with latest year as tiebreaker.


---


## Observable Cohort Definition (Year <= 2014)

PLE-linked analyses are restricted to examinees whose NMAT year is 2014 or earlier, ensuring a minimum 5-year window for PLE passage.

| Metric | Value |
|--------|-------|
| Observable best-record cohort | 64,501 |
| Median NMAT-to-PLE year gap | 6.0 years |

---


## Deterministic PLE Matching

All PLE matching is deterministic (exact NMA_AppNo match, manual AppNo match, or deterministic AppNo match). No fuzzy/rapidfuzz matching is used. This ensures full auditability but has important caveats: the NMAT application number (NMA_AppNo) is not a well-established, consistent identifier across datasets. The clean subset analysis uses the strictest criteria as a robustness check.

| Metric | Value |
|--------|-------|
| Confirmed PLE passers (all rows) | 49,986 |
| Confirmed PLE passers (best record, observable) | 29,273 |
| Clean subset (B5+, Filipino, >=5yr gap) | 23,357 |

---


## Data Integrity Summary

| Metric | Value |
|--------|-------|
| Stored-vs-derived mismatches | 56,065 |
| Calc-vs-derived mismatches | 0 |

---


## Limitations Relevant to CHED Decision-Making


### PLE Outcomes

The dataset only identifies NMAT examinees later matched to PLE passer records. It does not contain all PLE takers or PLE failures. Therefore, this dashboard reports NMAT-to-PLE-passer linkage rates, not PLE pass rates. Official PLE passing rates published by the PRC should be used for benchmarking purposes.


### GIDA and IP Status

The dataset does not contain indicators for Geographically Isolated and Disadvantaged Area (GIDA) residence or Indigenous Peoples (IP) membership. The CMO exception for B4-only applicants from these groups requires documentation not available in this dataset.


### Medical School Admissions and Enrollment

This dataset records NMAT examinees, not enrolled medical students. The number of examinees at or above a threshold represents the available applicant pool, not actual enrollment.


### Foreign Student Enrollment Cap

The CMO caps foreign student enrollment at 10 slots per incoming class at SUCs. The dataset shows NMAT examinees by citizenship, not enrolled foreign students.


### Composite Ranking for Foreign Applicants

The dataset does not contain GWA, interview scores, or other admission criteria needed for composite ranking analysis.


### PHEI Accountability and Sanctions

This dashboard does not assign compliance labels or risk ratings to individual HEIs. The NMAT-linked PLE data is not a complete measure of institutional PLE performance.
