# NMAT Performance Dashboard -- Complete Export

> Complete Markdown export generated 2026-08-14 18:06. Every number below is computed by the same functions the live dashboard renders from (`main_common.py`) -- this document is a faithful transcript, not a paraphrase. **This export always reflects the FULL, UNFILTERED dataset**, not whatever sidebar filters happened to be applied in the browser session that generated it.

**Source:** NMAT_Exodus.parquet, 178,927 rows x 58 columns loaded (source parquet on disk is 53 columns; the rest are derived at load time -- see Export Integrity at the end).

## How to Read This Document

- **Best-record examinees** -- one NMAT record per person (`IS_BEST_NMAT_RECORD`): highest percentile, latest year, lowest APPNO_CLEAN tiebreak.
- **Observable cohort** -- each person's best NMAT attempt with Year <= 2014 (`IS_BEST_OBSERVABLE_RECORD`). This is NOT the same as filtering the overall best-record flag to Year<=2014, which silently drops people whose overall-best attempt fell later.
- **NMAT-to-PLE linkage** -- the share of examinees later matched to PLE passer records. This is NEVER a pass rate: the PLE source list contains passers only, so "No confirmed PLE match" is not evidence of failure.
- **Score bins** -- B1 (0-9, lowest) through B10 (90-100, highest). Always ordered B1..B10, never string-sorted.
- **People vs sittings** -- best-record filtering counts people; unfiltered subsets (e.g. Tab 8 Repeat Takers) count exam sittings.
- **Box-plot charts** are exported as a five-number summary (min/Q1/median/Q3/max) plus n and outlier count per group, never as raw points (export contract Rule 1).
- **No medical-school identifier exists in this dataset.** UNDERGRAD_UNI_TYPE / UNDERGRAD_UNIVERSITY describe the examinee's undergraduate institution, never the medical school.

## Global KPIs

| Metric | Value | Population | Note |
|---|---|---|---|
| Total NMAT sittings | 178,927 | all years, all rows | - |
| Unique examinees | 134,869 | best-record | - |
| Observable cohort | 69,503 | best attempt, Year<=2014 | >=5yr PLE window |
| PLE linkage rate, observable cohort | 43.31% | observable cohort | linkage, not pass rate |
| Repeat takers | 33,713 (25.0%) | unique examinees | - |

---

## Chart-to-Table Index

Every chart the live dashboard renders (`st.plotly_chart`, 59 total), and the exact heading in this document carrying its underlying values as data.

| # | Tab | Chart | Backing table (heading) |
|---|---|---|---|
| 1 | Tab 1 | Annual NMAT score and volume profile | Annual Trend |
| 2 | Tab 1 | Course-group composition pie | Course-Group Composition |
| 3 | Tab 1 | University-type composition pie | University-Type Composition |
| 4 | Tab 3 | Annual score trends and volume | Annual Score Trends |
| 5 | Tab 3 | Total raw score by year (box) | Box Summary: Total Raw Score by Year |
| 6 | Tab 3 | Percentile rank by year (box) | Box Summary: Percentile Rank by Year |
| 7 | Tab 3 | Part I raw score by year (box) | Box Summary: Part I Raw Score by Year |
| 8 | Tab 3 | Part II raw score by year (box) | Box Summary: Part II Raw Score by Year |
| 9 | Tab 4 | Bin distribution heatmap by year | Bin Distribution by Year |
| 10 | Tab 4 | Bin composition stacked bar by year | Bin Distribution by Year |
| 11 | Tab 4 | Top vs bottom bin share by year | Top vs Bottom Bin Share by Year |
| 12 | Tab 4 | Bin distribution heatmap by university type | Bin Distribution by University Type |
| 13 | Tab 4 | Top-bin share bar by university type | Bin Distribution by University Type |
| 14 | Tab 4 | Bin composition facet by year x university type | Bin Count by Year x University Type |
| 15 | Tab 4 | Citizenship composition pie | Citizenship Counts |
| 16 | Tab 4 | Foreigners vs Filipinos pie | Citizenship Profile KPIs |
| 17 | Tab 4 | Top-15 citizenship groups bar | Citizenship Counts |
| 18 | Tab 4 | Bin composition by citizenship (stacked) | Bin Distribution by Citizenship (Top 15) |
| 19 | Tab 4 | Full bin heatmap by citizenship | Bin Distribution by Citizenship (Top 15) |
| 20 | Tab 4 | Top-bin share by citizenship | Top-Bin Share (B8-B10) by Citizenship (n>=3) |
| 21 | Tab 4 | Percentile rank by citizenship (box, n>=5) | Box Summary: Percentile Rank by Citizenship (n>=5) |
| 22 | Tab 4 | TRUE raw score by citizenship (box, n>=5) | Box Summary: TRUE Raw Score by Citizenship (n>=5) |
| 23 | Tab 4 | Percentile rank by comparison group (box) | Box Summary: Percentile Rank by Comparison Group |
| 24 | Tab 4 | TRUE raw score by comparison group (box) | Box Summary: TRUE Raw Score by Comparison Group |
| 25 | Tab 4 | Full bin heatmap by comparison group | Bin Distribution by Comparison Group |
| 26 | Tab 4 | Bin composition by comparison group (stacked) | Bin Distribution by Comparison Group |
| 27 | Tab 4 | Top vs bottom bin share by comparison group | Top vs Bottom Bin Share by Comparison Group |
| 28 | Tab 4 | Bin distribution heatmap by course group | Bin Distribution by Course Group |
| 29 | Tab 4 | Top-bin share bar by course group | Bin Distribution by Course Group |
| 30 | Tab 5 | Bin distribution by institution type x location | Bin Distribution by Institution Type x Location |
| 31 | Tab 5 | Top-bin share by institution type x location | Bin Distribution by Institution Type x Location |
| 32 | Tab 5 | Bin composition by university type (stacked) | Bin Composition by University Type (%) |
| 33 | Tab 5 | Bin distribution among foreign examinees | Bin Distribution Among Foreign Examinees |
| 34 | Tab 5 | Medical & Allied vs other courses by university type | Figure 16 -- Medical & Allied vs Other Courses by University Type |
| 35 | Tab 6 | University type to bin flow (Sankey) | Table 18 -- University Type to Bin Flow |
| 36 | Tab 6 | Course group to bin flow (Sankey) | Table 19 -- Course Group to Bin Flow |
| 37 | Tab 6 | Bin to PLE status flow (Sankey) | Table 20 -- Bin to PLE Status Flow (Observable Cohort) |
| 38 | Tab 7 | TRUE raw score by PLE status (box) | Box Summary: TRUE Raw Score by PLE Status |
| 39 | Tab 7 | Bin distribution by PLE status | Figure 21 -- Bin Distribution by PLE Status |
| 40 | Tab 7 | PLE status composition within each bin | Table 25 -- PLE Status Composition within Each Bin |
| 41 | Tab 7 | Top-bin share by course group | Table 26 -- Course-Group Top-Bin Survival |
| 42 | Tab 8 | NMAT attempt-count distribution | Table 31 -- Attempt-Count Distribution |
| 43 | Tab 8 | First-to-last attempt change (box) | Box Summary: First-to-Last Attempt Change |
| 44 | Tab 8 | First vs last percentile (scatter) | First vs Last Percentile (Repeat Takers, Preview) |
| 45 | Tab 9 | Standardized subtest means by university type | Table 34 -- Standardized Subtest Means by University Type |
| 46 | Tab 9 | Standardized subtest means by course group | Table 36 -- Standardized Subtest Means by Course Group |
| 47 | Tab 9 | Subtest radar profile by university type | Table 38 -- Radar-Profile Values by University Type |
| 48 | Tab 9 | Subtest radar profile by course group | Table 39 -- Radar-Profile Values by Course Group |
| 49 | Tab 10 | PLE year-gap distribution (histogram) | PLE Year-Gap Distribution |
| 50 | Tab 10 | PLE year gap by course group (box) | Box Summary: PLE Year Gap by Course Group |
| 51 | Tab 10 | Percentile rank by sex (box) | Box Summary: Percentile Rank by Sex |
| 52 | Tab 10 | Sex composition by year | Figure 34 -- Sex Composition by Year |
| 53 | Tab 10 | PLE status composition by sex | Table 42 -- PLE Status Composition by Sex (Observable Cohort) |
| 54 | Tab 11 | University type x bin row percentages | University Type x Bin Row Percentages |
| 55 | Tab 11 | Dunn post-hoc adjusted p-values | Table 48 -- Dunn Post-Hoc Adjusted P-Values |
| 56 | Tab 12 | Survival to top bins by course group | Table 4 -- Survival to Top Bins by Course Group |
| 57 | Tab 13 | PLE linkage rate by cut-off scenario | Section A -- Applicant-Pool Cut-off Scenarios (30th vs 40th Percentile) |
| 58 | Tab 13 | Bin composition: foreigner vs Filipino | Section B -- Foreign vs Filipino Applicant-Pool Composition |
| 59 | Tab 13 | PLE linkage rate by percentile bin | Section C -- Individual-Level PLE Linkage Gradient by Percentile Bin |

# Tab 1 -- Executive Summary

| Metric | Value | Population | Note |
|---|---|---|---|
| Examinees (best-record) | 134,869 | one row per person | - |
| Years covered | 13 | - | - |
| Median TRUE raw score | 122.0 | best-record examinees | - |
| Median percentile rank | 51.0 | best-record examinees | 0-99 scale |
| Repeat takers | 33,713 (25.0%) | unique examinees, all sittings | - |
| Observable cohort (IS_BEST_OBSERVABLE_RECORD) | 69,503 | best attempt, Year<=2014 | - |
| PLE linkage rate, observable cohort | 43.31% | observable cohort | linkage, not pass rate |

---


## Annual Trend

<!-- chart_type: bar+line | x: Year | y: n, raw_median, per_median | series: none
     population: best-record examinees, all years
     n: 134,869 | denominator: one row per person
     source_tab: 1 | element_id: fig_t1_trends -->

|   Year |      n |   raw_median |   raw_q25 |   raw_q75 |   part1_median |   part2_median |   per_median |   per_q25 |   per_q75 |   gps_median |   iqr_raw |   part1_share_pct |   part2_share_pct |
|-------:|-------:|-------------:|----------:|----------:|---------------:|---------------:|-------------:|----------:|----------:|-------------:|----------:|------------------:|------------------:|
|  2,006 |  3,698 |          131 |       108 |       154 |             67 |             63 |           53 |        27 |        77 |          510 |        46 |             51.15 |             48.09 |
|  2,007 |  3,690 |          130 |       107 |       156 |             66 |             65 |           52 |        27 |        77 |          507 |        49 |             50.77 |                50 |
|  2,008 |  4,965 |          129 |       107 |       153 |             67 |             61 |           54 |        29 |        80 |          511 |        46 |             51.94 |             47.29 |
|  2,009 |  7,461 |          130 |       109 |       152 |             68 |             62 |           52 |        27 |        77 |          505 |        43 |             52.31 |             47.69 |
|  2,010 |  8,551 |          136 |       115 |       159 |             71 |             65 |           57 |        32 |        81 |          518 |        44 |             52.21 |             47.79 |
|  2,011 |  8,701 |          129 |       109 |       151 |             69 |             60 |           52 |        30 |        76 |          505 |        42 |             53.49 |             46.51 |
|  2,012 |  9,113 |          122 |       101 |       145 |             67 |             54 |           54 |        26 |        82 |          513 |        44 |             54.92 |             44.26 |
|  2,013 |  9,148 |          128 |       103 |       154 |             70 |             57 |           60 |        27 |        86 |          529 |        51 |             54.69 |             44.53 |
|  2,014 | 10,455 |          120 |        98 |       142 |             65 |             55 |           59 |        27 |        84 |          522 |        44 |             54.17 |             45.83 |
|  2,015 | 10,326 |          118 |        93 |       142 |             61 |             57 |           54 |        24 |        79 |          506 |        49 |             51.69 |             48.31 |
|  2,016 | 12,480 |          123 |        98 |       146 |             66 |             57 |           49 |        21 |        73 |          495 |        48 |             53.66 |             46.34 |
|  2,017 | 23,948 |          118 |        93 |       143 |             63 |             54 |           44 |        20 |        71 |          485 |        50 |             53.39 |             45.76 |
|  2,018 | 22,333 |          111 |        91 |       132 |             59 |             51 |           43 |        19 |        70 |          481 |        41 |             53.15 |             45.95 |

---


## Course-Group Composition

<!-- chart_type: pie | x: UNDERGRAD_COURSE_GROUP | y: Count | series: none
     population: best-record examinees
     n: 134,869 | denominator: best-record examinees
     source_tab: 1 | element_id: fig_t1_course_pie -->

| UNDERGRAD_COURSE_GROUP       |   Count |   Share (%) |
|:-----------------------------|--------:|------------:|
| Medical & Allied             |  64,287 |       47.67 |
| Natural Sciences             |  41,514 |       30.78 |
| Social & Behavioral Sciences |  16,492 |       12.23 |
| Other                        |   8,346 |        6.19 |
| Education                    |   3,479 |        2.58 |
| Engineering & Technology     |     751 |        0.56 |

---


## University-Type Composition

<!-- chart_type: pie | x: UNDERGRAD_UNI_TYPE | y: Count | series: none
     population: best-record examinees
     n: 134,869 | denominator: best-record examinees
     source_tab: 1 | element_id: fig_t1_uni_pie -->

| UNDERGRAD_UNI_TYPE   |   Count |   Share (%) |
|:---------------------|--------:|------------:|
| Private              | 103,885 |       77.03 |
| Public               |  27,538 |       20.42 |
| Foreign              |   1,892 |         1.4 |
| Not Specified        |   1,554 |        1.15 |

---


## Table 1 -- Executive Summary Indicators

| Indicator                |   Value |
|:-------------------------|--------:|
| Median Total Raw Score   |     122 |
| Median Part I Raw Score  |      65 |
| Median Part II Raw Score |      57 |
| Median Percentile Rank   |      51 |
| Top-bin share (B8-B10)   |   31.18 |
| Bottom-bin share (B1-B3) |   29.22 |

---


# Tab 2 -- Data Integrity

| Metric | Value | Population | Note |
|---|---|---|---|
| All NMAT rows | 178,927 | all sittings | - |
| Best-record rows | 134,869 | one row per person | - |
| Rows with TRUE raw scores | 178,882 | all rows | - |
| Observable best-record rows | 69,503 | IS_BEST_OBSERVABLE_RECORD | - |

---


## Table 2 -- Analysis Cohorts

*Population: 6 analytic subsets defined over the full, unfiltered dataset (n varies by row -- see Row count column)*

| Analytic subset                               |   Row count | Interpretation                                                                                                                                          |
|:----------------------------------------------|------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| All cleaned NMAT rows                         |     178,927 | Every cleaned NMAT sitting, any year, all applicants.                                                                                                   |
| One best NMAT record per person               |     134,869 | One row per unique PERSON_KEY -- their single best NMAT attempt (highest percentile, latest year, lowest APPNO_CLEAN tiebreak).                         |
| Best-record rows within 2006-2018             |     134,869 | Best-record rows restricted to NMAT years 2006-2018 (the trend window).                                                                                 |
| Best-record rows in the observable PLE window |      69,503 | One row per person: their best attempt among sittings with Year <= 2014 (IS_BEST_OBSERVABLE_RECORD) -- the correct PLE-linked person-level cohort.      |
| Confirmed PLE-passer NMAT rows                |      47,485 | All rows (any year) flagged IS_PLE_PASSER == True -- found in the PLE passer source list. This is a linkage flag, not evidence of failure for the rest. |
| Confirmed PLE-passer best-record persons      |      35,746 | Rows above further restricted to IS_BEST_NMAT_RECORD == True (one row per passer).                                                                      |

---


## Table 3 -- TRUE Raw-Score Validation Checks

| Metric | Value | Population | Note |
|---|---|---|---|
| Rows with complete Total + Part I + Part II | 178,882 | all rows | - |
| Formula mismatches (Total != Part I + Part II) | 0 | rows above | - |
| Rows with a stored raw total | 99,316 | all rows | - |
| Stored-vs-derived mismatch flag count | 56,065 | rows with a stored total | 56.45% |
Stored-vs-derived mismatch rate: 56,065 of 99,316 rows with a stored total disagree with the recalculated TotalRawScoreTRUE (56.45% of that denominator). Never state this as "42.2%" -- that figure divided the mismatch count by the wrong (unique-examinee) denominator.


---


## Table 4 -- University Pairing Audit

| Metric | Value | Population | Note |
|---|---|---|---|
| Universities checked | 2,907 | distinct UNDERGRAD_UNIVERSITY values | - |
| University pairing conflicts | 2 | universities above | >1 UNDERGRAD_UNI_TYPE or >1 UNDERGRAD_UNI_LOCATION |
*Population: conflicting universities only, 2 of 2,907 checked*

| UNDERGRAD_UNIVERSITY    |   records |   n_uni_types |   n_locations | uni_types                        | locations       |
|:------------------------|----------:|--------------:|--------------:|:---------------------------------|:----------------|
| NOT SPECIFIED/UNLISTED  |       561 |             3 |             2 | Not Specified | Private | Public | Local | Unknown |
| OTHERS (PLEASE SPECIFY) |        25 |             2 |             2 | Not Specified | Private          | Local | Unknown |

---


## Tables 6-8 -- Core Distributions

*Population: all rows, n=178,927*

| UNDERGRAD_UNI_TYPE   |   Count |   Share (%) |
|:---------------------|--------:|------------:|
| Private              | 137,711 |       76.96 |
| Public               |  36,890 |       20.62 |
| Foreign              |   2,315 |        1.29 |
| Not Specified        |   2,011 |        1.12 |
| UNDERGRAD_COURSE_GROUP       |   Count |   Share (%) |
|:-----------------------------|--------:|------------:|
| Medical & Allied             |  86,140 |       48.14 |
| Natural Sciences             |  55,900 |       31.24 |
| Social & Behavioral Sciences |  22,022 |       12.31 |
| Other                        |   9,855 |        5.51 |
| Education                    |   4,162 |        2.33 |
| Engineering & Technology     |     848 |        0.47 |
*Population: observable cohort only (Year<=2014); 90,783 of 178,927 rows (50.7%) excluded as Year>2014*

| PLE_STATUS_LABEL       |   Count |
|:-----------------------|--------:|
| No confirmed PLE match |  50,014 |
| Confirmed PLE passer   |  38,130 |

---


## Table 9 -- PLE Match-Outcome Breakdown

*Population: all rows, n=178,927*

| PLE_MATCH_OUTCOME         |   Count |   Percent |
|:--------------------------|--------:|----------:|
| no_match                  | 123,233 |     68.87 |
| accepted                  |  47,485 |     26.54 |
| rejected_ambiguous_person |   8,207 |      4.59 |
| rejected                  |       2 |         0 |
79 confirmed passers have PLE_YEAR_UNCERTAIN == True.


---


# Tab 3 -- Trends & Stability


## Annual Score Trends

<!-- chart_type: line (4-panel) | x: Year | y: raw/percentile median + IQR, n | series: none
     population: best-record trend cohort
     n: 134,869 | denominator: best-record examinees, 2006-2018
     source_tab: 3 | element_id: fig_t3_trends -->

|   Year |      n |   raw_median |   raw_q25 |   raw_q75 |   part1_median |   part2_median |   per_median |   per_q25 |   per_q75 |   gps_median |   iqr_raw |   part1_share_pct |   part2_share_pct |
|-------:|-------:|-------------:|----------:|----------:|---------------:|---------------:|-------------:|----------:|----------:|-------------:|----------:|------------------:|------------------:|
|  2,006 |  3,698 |          131 |       108 |       154 |             67 |             63 |           53 |        27 |        77 |          510 |        46 |             51.15 |             48.09 |
|  2,007 |  3,690 |          130 |       107 |       156 |             66 |             65 |           52 |        27 |        77 |          507 |        49 |             50.77 |                50 |
|  2,008 |  4,965 |          129 |       107 |       153 |             67 |             61 |           54 |        29 |        80 |          511 |        46 |             51.94 |             47.29 |
|  2,009 |  7,461 |          130 |       109 |       152 |             68 |             62 |           52 |        27 |        77 |          505 |        43 |             52.31 |             47.69 |
|  2,010 |  8,551 |          136 |       115 |       159 |             71 |             65 |           57 |        32 |        81 |          518 |        44 |             52.21 |             47.79 |
|  2,011 |  8,701 |          129 |       109 |       151 |             69 |             60 |           52 |        30 |        76 |          505 |        42 |             53.49 |             46.51 |
|  2,012 |  9,113 |          122 |       101 |       145 |             67 |             54 |           54 |        26 |        82 |          513 |        44 |             54.92 |             44.26 |
|  2,013 |  9,148 |          128 |       103 |       154 |             70 |             57 |           60 |        27 |        86 |          529 |        51 |             54.69 |             44.53 |
|  2,014 | 10,455 |          120 |        98 |       142 |             65 |             55 |           59 |        27 |        84 |          522 |        44 |             54.17 |             45.83 |
|  2,015 | 10,326 |          118 |        93 |       142 |             61 |             57 |           54 |        24 |        79 |          506 |        49 |             51.69 |             48.31 |
|  2,016 | 12,480 |          123 |        98 |       146 |             66 |             57 |           49 |        21 |        73 |          495 |        48 |             53.66 |             46.34 |
|  2,017 | 23,948 |          118 |        93 |       143 |             63 |             54 |           44 |        20 |        71 |          485 |        50 |             53.39 |             45.76 |
|  2,018 | 22,333 |          111 |        91 |       132 |             59 |             51 |           43 |        19 |        70 |          481 |        41 |             53.15 |             45.95 |

---


## Box Summary: Total Raw Score by Year

<!-- chart_type: box | x: Year | y: TotalRawScoreTRUE | series: none
     population: best-record trend cohort
     n: 134,869 | denominator: best-record examinees, 2006-2018
     source_tab: 3 | element_id: fig_t3_box_raw -->

|   Year |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|-------:|-------:|------:|-----:|---------:|-----:|------:|-----------:|
|  2,006 |  3,698 |    50 |  108 |      131 |  154 |   220 |          0 |
|  2,007 |  3,690 |    38 |  107 |      130 |  156 |   222 |          0 |
|  2,008 |  4,965 |    37 |  107 |      129 |  153 |   223 |          2 |
|  2,009 |  7,445 |    48 |  109 |      130 |  152 |   223 |          5 |
|  2,010 |  8,548 |    44 |  115 |      136 |  159 |   231 |          3 |
|  2,011 |  8,692 |    46 |  109 |      129 |  151 |   222 |         10 |
|  2,012 |  9,102 |    43 |  101 |      122 |  145 |   223 |         20 |
|  2,013 |  9,144 |    10 |  103 |      128 |  154 |   227 |          5 |
|  2,014 | 10,455 |     9 |   98 |      120 |  142 |   220 |         28 |
|  2,015 | 10,326 |    27 |   93 |      118 |  142 |   222 |         10 |
|  2,016 | 12,480 |    30 |   98 |      123 |  146 |   223 |          2 |
|  2,017 | 23,948 |     7 |   93 |      118 |  143 |   226 |         11 |
|  2,018 | 22,333 |    25 |   91 |      111 |  132 |   230 |        219 |

---


## Box Summary: Percentile Rank by Year

<!-- chart_type: box | x: Year | y: NMS_PER_num | series: none
     population: best-record trend cohort
     n: 134,869 | denominator: best-record examinees, 2006-2018
     source_tab: 3 | element_id: fig_t3_box_pct -->

|   Year |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|-------:|-------:|------:|-----:|---------:|-----:|------:|-----------:|
|  2,006 |  3,675 |     1 |   27 |       53 |   77 |    99 |          0 |
|  2,007 |  3,665 |     1 |   27 |       52 |   77 |    99 |          0 |
|  2,008 |  4,947 |     1 |   29 |       54 |   80 |    99 |          0 |
|  2,009 |  7,438 |     0 |   27 |       52 |   77 |    99 |          0 |
|  2,010 |  8,529 |     0 |   32 |       57 |   81 |    99 |          0 |
|  2,011 |  8,649 |     1 |   30 |       52 |   76 |    99 |          0 |
|  2,012 |  8,852 |     0 |   26 |       54 |   82 |    99 |          0 |
|  2,013 |  8,748 |     1 |   27 |       60 |   86 |    99 |          0 |
|  2,014 | 10,016 |     1 |   27 |       59 |   84 |    99 |          0 |
|  2,015 |  9,740 |     1 |   24 |       54 |   79 |    99 |          0 |
|  2,016 | 12,141 |     1 |   21 |       49 |   73 |    99 |          0 |
|  2,017 | 23,612 |     1 |   20 |       44 |   71 |    99 |          0 |
|  2,018 | 21,833 |     1 |   19 |       43 |   70 |    99 |          0 |

---


## Box Summary: Part I Raw Score by Year

<!-- chart_type: box | x: Year | y: PartIRawScoreTRUE | series: none
     population: best-record trend cohort
     n: 134,869 | denominator: best-record examinees, 2006-2018
     source_tab: 3 | element_id: fig_t3_box_p1 -->

|   Year |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|-------:|-------:|------:|-----:|---------:|-----:|------:|-----------:|
|  2,006 |  3,698 |    21 |   56 |       67 |   79 |   115 |          3 |
|  2,007 |  3,690 |    15 |   54 |       66 |   77 |   115 |          3 |
|  2,008 |  4,965 |    13 |   56 |       67 |   79 |   113 |          7 |
|  2,009 |  7,445 |    12 |   57 |       68 |   79 |   115 |         13 |
|  2,010 |  8,548 |    16 |   60 |       71 |   83 |   118 |         12 |
|  2,011 |  8,692 |    20 |   58 |       69 |   80 |   116 |         21 |
|  2,012 |  9,102 |    19 |   56 |       67 |   79 |   115 |         11 |
|  2,013 |  9,144 |     7 |   57 |       70 |   83 |   117 |         14 |
|  2,014 | 10,455 |     0 |   53 |       65 |   76 |   116 |         37 |
|  2,015 | 10,326 |    12 |   48 |       61 |   73 |   114 |          9 |
|  2,016 | 12,480 |     1 |   53 |       66 |   78 |   115 |          5 |
|  2,017 | 23,948 |     1 |   50 |       63 |   77 |   116 |          5 |
|  2,018 | 22,333 |    12 |   48 |       59 |   71 |   117 |         49 |

---


## Box Summary: Part II Raw Score by Year

<!-- chart_type: box | x: Year | y: PartIIRawScoreTRUE | series: none
     population: best-record trend cohort
     n: 134,869 | denominator: best-record examinees, 2006-2018
     source_tab: 3 | element_id: fig_t3_box_p2 -->

|   Year |      n |   min |   q1 |   median |    q3 |   max |   outliers |
|-------:|-------:|------:|-----:|---------:|------:|------:|-----------:|
|  2,006 |  3,698 |    25 |   51 |       63 | 77.75 |   112 |          0 |
|  2,007 |  3,690 |     0 |   52 |       65 |    80 |   110 |          5 |
|  2,008 |  4,965 |     0 |   49 |       61 |    75 |   118 |          2 |
|  2,009 |  7,445 |    21 |   51 |       62 |    75 |   113 |          2 |
|  2,010 |  8,548 |    21 |   53 |       65 |    78 |   116 |          1 |
|  2,011 |  8,692 |    19 |   49 |       60 |    72 |   112 |          9 |
|  2,012 |  9,102 |    14 |   43 |       54 |    68 |   113 |         21 |
|  2,013 |  9,144 |     1 |   45 |       57 |    73 |   115 |          1 |
|  2,014 | 10,455 |     4 |   43 |       55 |    68 |   109 |         17 |
|  2,015 | 10,326 |     2 |   42 |       57 |    71 |   116 |          2 |
|  2,016 | 12,480 |     0 |   43 |       57 |    70 |   115 |         12 |
|  2,017 | 23,948 |     0 |   42 |       54 |    68 |   117 |         62 |
|  2,018 | 22,333 |     6 |   41 |       51 |    64 |   114 |        232 |

---


## Table 9 -- Kruskal-Wallis Tests by Year

| Score              |       H | p_value   |   eta_squared |
|:-------------------|--------:|:----------|--------------:|
| Total Raw Score    | 6028.28 | <0.001    |          0.04 |
| Part I Raw Score   | 5766.34 | <0.001    |          0.04 |
| Part II Raw Score  | 5968.69 | <0.001    |          0.04 |
| Percentile Rank    | 2384.82 | <0.001    |          0.02 |
| GPS Standard Score | 2592.55 | <0.001    |          0.02 |

---


# Tab 4 -- Score Bins & Background


## Bin Distribution by Year

<!-- chart_type: heatmap+stacked_bar | x: Year | y: PercentileBin | series: fig_t4_heatmap_year
     population: row %
     n: best-record trend cohort | denominator: 134,869
     source_tab: best-record examinees, 2006-2018 | element_id: 4 -->

|   Year |    B1 |    B2 |   B3 |    B4 |    B5 |    B6 |    B7 |    B8 |    B9 |   B10 |
|-------:|------:|------:|-----:|------:|------:|------:|------:|------:|------:|------:|
|  2,006 |  8.71 |  8.84 | 9.33 |  9.63 | 10.04 | 10.12 |  9.71 |  10.2 | 10.78 | 12.63 |
|  2,007 |  8.84 |  8.59 | 9.69 | 10.83 | 10.07 |  8.21 |  9.85 |  10.5 | 11.13 | 12.28 |
|  2,008 |  8.81 |  8.43 | 7.96 |  9.62 | 10.09 | 10.49 | 10.01 |  9.46 | 10.92 | 14.21 |
|  2,009 |  7.92 |  8.81 |  9.8 | 10.82 |  9.64 | 10.78 | 10.15 |  9.65 |  9.91 | 12.52 |
|  2,010 |  6.16 |  7.42 | 8.57 |  8.78 | 10.45 | 10.75 |  9.72 | 10.65 | 11.95 | 15.56 |
|  2,011 |  6.54 |  8.68 | 9.26 | 11.18 | 11.99 | 10.37 |  9.79 |  10.8 | 10.34 | 11.04 |
|  2,012 | 10.94 |  8.72 | 7.96 |  8.78 |  9.87 |  8.37 |  8.87 |  9.22 | 10.29 | 16.98 |
|  2,013 | 12.41 |  7.93 | 6.42 |  6.97 |  8.09 |  7.22 |  8.61 | 10.28 |  11.8 | 20.26 |
|  2,014 |  12.9 |  7.09 | 6.85 |   7.3 |   8.2 |  8.38 |  9.72 | 10.28 | 11.68 |  17.6 |
|  2,015 | 14.57 |  7.43 | 7.39 |  7.16 |  9.18 |  9.24 | 10.53 |  9.94 | 10.56 | 13.99 |
|  2,016 | 14.19 |  9.55 |    8 |  8.57 | 10.44 | 10.79 |  9.55 |  9.93 | 10.02 |  8.94 |
|  2,017 | 13.05 | 11.71 | 9.87 | 11.22 |  8.72 |  10.2 |  9.32 |  9.34 |  8.85 |  7.72 |
|  2,018 |  14.9 | 11.29 | 9.66 | 10.69 |  9.86 |  9.81 |  8.32 |  8.35 |  8.19 |  8.92 |

---


## Top vs Bottom Bin Share by Year

|   Year |   Top B8-B10 (%) |   Bottom B1-B3 (%) |   Difference (pp) |
|-------:|-----------------:|-------------------:|------------------:|
|   2006 |            33.61 |              26.88 |               6.7 |
|   2007 |            33.91 |              27.12 |               6.8 |
|   2008 |            34.59 |               25.2 |               9.4 |
|   2009 |            32.08 |              26.53 |               5.5 |
|   2010 |            38.16 |              22.15 |                16 |
|   2011 |            32.18 |              24.48 |               7.7 |
|   2012 |            36.49 |              27.62 |               8.9 |
|   2013 |            42.34 |              26.76 |              15.6 |
|   2014 |            39.56 |              26.84 |              12.7 |
|   2015 |            34.49 |              29.39 |               5.1 |
|   2016 |            28.89 |              31.74 |              -2.9 |
|   2017 |            25.91 |              34.63 |              -8.7 |
|   2018 |            25.46 |              35.85 |             -10.4 |

---


## Bin Distribution by University Type

*Population: best-record, Public/Private/Foreign, n=133,315*

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private              | 12.05 |  9.7 | 9.01 | 9.92 |  9.9 | 9.94 | 9.47 | 9.68 |  9.72 | 10.61 |
| Public               |  10.7 |  8.1 | 7.51 | 8.22 | 8.52 | 8.88 | 9.09 | 9.63 | 11.28 | 18.07 |

---


## Table 11 -- Chi-Square: University Type x Bin

|    chi2 | p_value   |   degrees_of_freedom |   n_observations |   cramers_v |
|--------:|:----------|---------------------:|-----------------:|------------:|
| 1327.86 | <0.001    |                   18 |          130,334 |        0.07 |

---


## Bin Count by Year x University Type

*Population: best-record, Public/Private/Foreign, valid year+bin, n=130,334 sittings across 390 year x unitype x bin cells*

|   Year | UNDERGRAD_UNI_TYPE   | PercentileBin   |     n |
|-------:|:---------------------|:----------------|------:|
|  2,006 | Foreign              | B1              |    23 |
|  2,006 | Foreign              | B2              |    11 |
|  2,006 | Foreign              | B3              |     9 |
|  2,006 | Foreign              | B4              |     9 |
|  2,006 | Foreign              | B5              |    13 |
|  2,006 | Foreign              | B6              |    16 |
|  2,006 | Foreign              | B7              |     9 |
|  2,006 | Foreign              | B8              |     8 |
|  2,006 | Foreign              | B9              |    15 |
|  2,006 | Foreign              | B10             |    25 |
|  2,006 | Private              | B1              |   246 |
|  2,006 | Private              | B2              |   266 |
|  2,006 | Private              | B3              |   276 |
|  2,006 | Private              | B4              |   288 |
|  2,006 | Private              | B5              |   280 |
|  2,006 | Private              | B6              |   278 |
|  2,006 | Private              | B7              |   255 |
|  2,006 | Private              | B8              |   268 |
|  2,006 | Private              | B9              |   252 |
|  2,006 | Private              | B10             |   190 |
|  2,006 | Public               | B1              |    51 |
|  2,006 | Public               | B2              |    48 |
|  2,006 | Public               | B3              |    58 |
|  2,006 | Public               | B4              |    57 |
|  2,006 | Public               | B5              |    76 |
|  2,006 | Public               | B6              |    78 |
|  2,006 | Public               | B7              |    93 |
|  2,006 | Public               | B8              |    99 |
|  2,006 | Public               | B9              |   129 |
|  2,006 | Public               | B10             |   249 |
|  2,007 | Foreign              | B1              |    10 |
|  2,007 | Foreign              | B2              |     8 |
|  2,007 | Foreign              | B3              |     3 |
|  2,007 | Foreign              | B4              |     2 |
|  2,007 | Foreign              | B5              |     6 |
|  2,007 | Foreign              | B6              |     6 |
|  2,007 | Foreign              | B7              |     6 |
|  2,007 | Foreign              | B8              |     2 |
|  2,007 | Foreign              | B9              |     5 |
|  2,007 | Foreign              | B10             |    12 |
|  2,007 | Private              | B1              |   263 |
|  2,007 | Private              | B2              |   262 |
|  2,007 | Private              | B3              |   307 |
|  2,007 | Private              | B4              |   353 |
|  2,007 | Private              | B5              |   293 |
|  2,007 | Private              | B6              |   237 |
|  2,007 | Private              | B7              |   263 |
|  2,007 | Private              | B8              |   286 |
|  2,007 | Private              | B9              |   264 |
|  2,007 | Private              | B10             |   169 |
|  2,007 | Public               | B1              |    50 |
|  2,007 | Public               | B2              |    45 |
|  2,007 | Public               | B3              |    44 |
|  2,007 | Public               | B4              |    42 |
|  2,007 | Public               | B5              |    70 |
|  2,007 | Public               | B6              |    58 |
|  2,007 | Public               | B7              |    92 |
|  2,007 | Public               | B8              |    97 |
|  2,007 | Public               | B9              |   139 |
|  2,007 | Public               | B10             |   269 |
|  2,008 | Foreign              | B1              |     7 |
|  2,008 | Foreign              | B2              |     5 |
|  2,008 | Foreign              | B3              |     4 |
|  2,008 | Foreign              | B4              |    12 |
|  2,008 | Foreign              | B5              |    11 |
|  2,008 | Foreign              | B6              |    11 |
|  2,008 | Foreign              | B7              |    11 |
|  2,008 | Foreign              | B8              |    16 |
|  2,008 | Foreign              | B9              |    16 |
|  2,008 | Foreign              | B10             |    14 |
|  2,008 | Private              | B1              |   387 |
|  2,008 | Private              | B2              |   354 |
|  2,008 | Private              | B3              |   339 |
|  2,008 | Private              | B4              |   405 |
|  2,008 | Private              | B5              |   421 |
|  2,008 | Private              | B6              |   423 |
|  2,008 | Private              | B7              |   382 |
|  2,008 | Private              | B8              |   331 |
|  2,008 | Private              | B9              |   370 |
|  2,008 | Private              | B10             |   271 |
|  2,008 | Public               | B1              |    41 |
|  2,008 | Public               | B2              |    53 |
|  2,008 | Public               | B3              |    49 |
|  2,008 | Public               | B4              |    55 |
|  2,008 | Public               | B5              |    64 |
|  2,008 | Public               | B6              |    75 |
|  2,008 | Public               | B7              |    99 |
|  2,008 | Public               | B8              |   116 |
|  2,008 | Public               | B9              |   150 |
|  2,008 | Public               | B10             |   416 |
|  2,009 | Foreign              | B1              |    18 |
|  2,009 | Foreign              | B2              |    15 |
|  2,009 | Foreign              | B3              |    13 |
|  2,009 | Foreign              | B4              |    16 |
|  2,009 | Foreign              | B5              |     8 |
|  2,009 | Foreign              | B6              |    13 |
|  2,009 | Foreign              | B7              |    10 |
|  2,009 | Foreign              | B8              |    12 |
|  2,009 | Foreign              | B9              |    19 |
|  2,009 | Foreign              | B10             |    37 |
|  2,009 | Private              | B1              |   474 |
|  2,009 | Private              | B2              |   561 |
|  2,009 | Private              | B3              |   618 |
|  2,009 | Private              | B4              |   676 |
|  2,009 | Private              | B5              |   599 |
|  2,009 | Private              | B6              |   636 |
|  2,009 | Private              | B7              |   586 |
|  2,009 | Private              | B8              |   538 |
|  2,009 | Private              | B9              |   492 |
|  2,009 | Private              | B10             |   388 |
|  2,009 | Public               | B1              |    92 |
|  2,009 | Public               | B2              |    75 |
|  2,009 | Public               | B3              |    92 |
|  2,009 | Public               | B4              |   105 |
|  2,009 | Public               | B5              |   100 |
|  2,009 | Public               | B6              |   146 |
|  2,009 | Public               | B7              |   154 |
|  2,009 | Public               | B8              |   167 |
|  2,009 | Public               | B9              |   225 |
|  2,009 | Public               | B10             |   504 |
|  2,010 | Foreign              | B1              |    15 |
|  2,010 | Foreign              | B2              |    10 |
|  2,010 | Foreign              | B3              |     9 |
|  2,010 | Foreign              | B4              |     6 |
|  2,010 | Foreign              | B5              |    14 |
|  2,010 | Foreign              | B6              |     9 |
|  2,010 | Foreign              | B7              |    15 |
|  2,010 | Foreign              | B8              |    19 |
|  2,010 | Foreign              | B9              |    20 |
|  2,010 | Foreign              | B10             |    31 |
|  2,010 | Private              | B1              |   421 |
|  2,010 | Private              | B2              |   535 |
|  2,010 | Private              | B3              |   620 |
|  2,010 | Private              | B4              |   632 |
|  2,010 | Private              | B5              |   751 |
|  2,010 | Private              | B6              |   770 |
|  2,010 | Private              | B7              |   643 |
|  2,010 | Private              | B8              |   675 |
|  2,010 | Private              | B9              |   714 |
|  2,010 | Private              | B10             |   618 |
|  2,010 | Public               | B1              |    53 |
|  2,010 | Public               | B2              |    65 |
|  2,010 | Public               | B3              |    81 |
|  2,010 | Public               | B4              |    86 |
|  2,010 | Public               | B5              |   104 |
|  2,010 | Public               | B6              |   117 |
|  2,010 | Public               | B7              |   149 |
|  2,010 | Public               | B8              |   192 |
|  2,010 | Public               | B9              |   268 |
|  2,010 | Public               | B10             |   656 |
|  2,011 | Foreign              | B1              |    21 |
|  2,011 | Foreign              | B2              |    10 |
|  2,011 | Foreign              | B3              |    21 |
|  2,011 | Foreign              | B4              |    10 |
|  2,011 | Foreign              | B5              |     9 |
|  2,011 | Foreign              | B6              |     8 |
|  2,011 | Foreign              | B7              |    11 |
|  2,011 | Foreign              | B8              |    19 |
|  2,011 | Foreign              | B9              |    14 |
|  2,011 | Foreign              | B10             |    30 |
|  2,011 | Private              | B1              |   460 |
|  2,011 | Private              | B2              |   640 |
|  2,011 | Private              | B3              |   681 |
|  2,011 | Private              | B4              |   842 |
|  2,011 | Private              | B5              |   900 |
|  2,011 | Private              | B6              |   762 |
|  2,011 | Private              | B7              |   689 |
|  2,011 | Private              | B8              |   715 |
|  2,011 | Private              | B9              |   652 |
|  2,011 | Private              | B10             |   430 |
|  2,011 | Public               | B1              |    57 |
|  2,011 | Public               | B2              |    77 |
|  2,011 | Public               | B3              |    77 |
|  2,011 | Public               | B4              |   102 |
|  2,011 | Public               | B5              |   110 |
|  2,011 | Public               | B6              |   116 |
|  2,011 | Public               | B7              |   135 |
|  2,011 | Public               | B8              |   183 |
|  2,011 | Public               | B9              |   214 |
|  2,011 | Public               | B10             |   477 |
|  2,012 | Foreign              | B1              |    15 |
|  2,012 | Foreign              | B2              |    13 |
|  2,012 | Foreign              | B3              |    10 |
|  2,012 | Foreign              | B4              |    12 |
|  2,012 | Foreign              | B5              |     6 |
|  2,012 | Foreign              | B6              |    12 |
|  2,012 | Foreign              | B7              |    13 |
|  2,012 | Foreign              | B8              |     6 |
|  2,012 | Foreign              | B9              |    15 |
|  2,012 | Foreign              | B10             |    17 |
|  2,012 | Private              | B1              |   758 |
|  2,012 | Private              | B2              |   609 |
|  2,012 | Private              | B3              |   537 |
|  2,012 | Private              | B4              |   587 |
|  2,012 | Private              | B5              |   668 |
|  2,012 | Private              | B6              |   577 |
|  2,012 | Private              | B7              |   587 |
|  2,012 | Private              | B8              |   646 |
|  2,012 | Private              | B9              |   682 |
|  2,012 | Private              | B10             | 1,144 |
|  2,012 | Public               | B1              |   180 |
|  2,012 | Public               | B2              |   136 |
|  2,012 | Public               | B3              |   135 |
|  2,012 | Public               | B4              |   160 |
|  2,012 | Public               | B5              |   183 |
|  2,012 | Public               | B6              |   144 |
|  2,012 | Public               | B7              |   174 |
|  2,012 | Public               | B8              |   152 |
|  2,012 | Public               | B9              |   191 |
|  2,012 | Public               | B10             |   315 |
|  2,013 | Foreign              | B1              |    18 |
|  2,013 | Foreign              | B2              |     8 |
|  2,013 | Foreign              | B3              |     7 |
|  2,013 | Foreign              | B4              |     2 |
|  2,013 | Foreign              | B5              |     8 |
|  2,013 | Foreign              | B6              |     4 |
|  2,013 | Foreign              | B7              |     9 |
|  2,013 | Foreign              | B8              |    14 |
|  2,013 | Foreign              | B9              |    13 |
|  2,013 | Foreign              | B10             |    17 |
|  2,013 | Private              | B1              |   837 |
|  2,013 | Private              | B2              |   532 |
|  2,013 | Private              | B3              |   436 |
|  2,013 | Private              | B4              |   474 |
|  2,013 | Private              | B5              |   549 |
|  2,013 | Private              | B6              |   508 |
|  2,013 | Private              | B7              |   586 |
|  2,013 | Private              | B8              |   707 |
|  2,013 | Private              | B9              |   818 |
|  2,013 | Private              | B10             | 1,397 |
|  2,013 | Public               | B1              |   219 |
|  2,013 | Public               | B2              |   138 |
|  2,013 | Public               | B3              |   109 |
|  2,013 | Public               | B4              |   129 |
|  2,013 | Public               | B5              |   136 |
|  2,013 | Public               | B6              |   114 |
|  2,013 | Public               | B7              |   149 |
|  2,013 | Public               | B8              |   165 |
|  2,013 | Public               | B9              |   181 |
|  2,013 | Public               | B10             |   328 |
|  2,014 | Foreign              | B1              |    17 |
|  2,014 | Foreign              | B2              |     8 |
|  2,014 | Foreign              | B3              |     8 |
|  2,014 | Foreign              | B4              |    11 |
|  2,014 | Foreign              | B5              |     7 |
|  2,014 | Foreign              | B6              |     7 |
|  2,014 | Foreign              | B7              |    20 |
|  2,014 | Foreign              | B8              |    12 |
|  2,014 | Foreign              | B9              |    15 |
|  2,014 | Foreign              | B10             |    15 |
|  2,014 | Private              | B1              | 1,041 |
|  2,014 | Private              | B2              |   552 |
|  2,014 | Private              | B3              |   555 |
|  2,014 | Private              | B4              |   570 |
|  2,014 | Private              | B5              |   647 |
|  2,014 | Private              | B6              |   655 |
|  2,014 | Private              | B7              |   771 |
|  2,014 | Private              | B8              |   825 |
|  2,014 | Private              | B9              |   930 |
|  2,014 | Private              | B10             | 1,372 |
|  2,014 | Public               | B1              |   213 |
|  2,014 | Public               | B2              |   132 |
|  2,014 | Public               | B3              |   111 |
|  2,014 | Public               | B4              |   142 |
|  2,014 | Public               | B5              |   150 |
|  2,014 | Public               | B6              |   162 |
|  2,014 | Public               | B7              |   168 |
|  2,014 | Public               | B8              |   174 |
|  2,014 | Public               | B9              |   211 |
|  2,014 | Public               | B10             |   348 |
|  2,015 | Foreign              | B1              |    24 |
|  2,015 | Foreign              | B2              |     5 |
|  2,015 | Foreign              | B3              |     8 |
|  2,015 | Foreign              | B4              |     8 |
|  2,015 | Foreign              | B5              |     9 |
|  2,015 | Foreign              | B6              |    14 |
|  2,015 | Foreign              | B7              |    11 |
|  2,015 | Foreign              | B8              |    10 |
|  2,015 | Foreign              | B9              |    16 |
|  2,015 | Foreign              | B10             |    20 |
|  2,015 | Private              | B1              | 1,060 |
|  2,015 | Private              | B2              |   534 |
|  2,015 | Private              | B3              |   536 |
|  2,015 | Private              | B4              |   514 |
|  2,015 | Private              | B5              |   687 |
|  2,015 | Private              | B6              |   663 |
|  2,015 | Private              | B7              |   791 |
|  2,015 | Private              | B8              |   724 |
|  2,015 | Private              | B9              |   773 |
|  2,015 | Private              | B10             | 1,024 |
|  2,015 | Public               | B1              |   319 |
|  2,015 | Public               | B2              |   172 |
|  2,015 | Public               | B3              |   168 |
|  2,015 | Public               | B4              |   165 |
|  2,015 | Public               | B5              |   189 |
|  2,015 | Public               | B6              |   209 |
|  2,015 | Public               | B7              |   208 |
|  2,015 | Public               | B8              |   218 |
|  2,015 | Public               | B9              |   228 |
|  2,015 | Public               | B10             |   303 |
|  2,016 | Foreign              | B1              |    16 |
|  2,016 | Foreign              | B2              |    11 |
|  2,016 | Foreign              | B3              |    12 |
|  2,016 | Foreign              | B4              |    13 |
|  2,016 | Foreign              | B5              |     8 |
|  2,016 | Foreign              | B6              |     9 |
|  2,016 | Foreign              | B7              |     8 |
|  2,016 | Foreign              | B8              |    12 |
|  2,016 | Foreign              | B9              |    12 |
|  2,016 | Foreign              | B10             |     6 |
|  2,016 | Private              | B1              | 1,312 |
|  2,016 | Private              | B2              |   898 |
|  2,016 | Private              | B3              |   755 |
|  2,016 | Private              | B4              |   789 |
|  2,016 | Private              | B5              |   952 |
|  2,016 | Private              | B6              | 1,013 |
|  2,016 | Private              | B7              |   892 |
|  2,016 | Private              | B8              |   910 |
|  2,016 | Private              | B9              |   926 |
|  2,016 | Private              | B10             |   832 |
|  2,016 | Public               | B1              |   377 |
|  2,016 | Public               | B2              |   237 |
|  2,016 | Public               | B3              |   199 |
|  2,016 | Public               | B4              |   234 |
|  2,016 | Public               | B5              |   288 |
|  2,016 | Public               | B6              |   276 |
|  2,016 | Public               | B7              |   249 |
|  2,016 | Public               | B8              |   275 |
|  2,016 | Public               | B9              |   268 |
|  2,016 | Public               | B10             |   232 |
|  2,017 | Foreign              | B1              |    39 |
|  2,017 | Foreign              | B2              |    41 |
|  2,017 | Foreign              | B3              |    21 |
|  2,017 | Foreign              | B4              |    44 |
|  2,017 | Foreign              | B5              |    31 |
|  2,017 | Foreign              | B6              |    33 |
|  2,017 | Foreign              | B7              |    24 |
|  2,017 | Foreign              | B8              |    26 |
|  2,017 | Foreign              | B9              |    22 |
|  2,017 | Foreign              | B10             |    26 |
|  2,017 | Private              | B1              | 2,417 |
|  2,017 | Private              | B2              | 2,133 |
|  2,017 | Private              | B3              | 1,800 |
|  2,017 | Private              | B4              | 2,057 |
|  2,017 | Private              | B5              | 1,599 |
|  2,017 | Private              | B6              | 1,892 |
|  2,017 | Private              | B7              | 1,736 |
|  2,017 | Private              | B8              | 1,753 |
|  2,017 | Private              | B9              | 1,608 |
|  2,017 | Private              | B10             | 1,407 |
|  2,017 | Public               | B1              |   610 |
|  2,017 | Public               | B2              |   569 |
|  2,017 | Public               | B3              |   500 |
|  2,017 | Public               | B4              |   538 |
|  2,017 | Public               | B5              |   419 |
|  2,017 | Public               | B6              |   476 |
|  2,017 | Public               | B7              |   431 |
|  2,017 | Public               | B8              |   420 |
|  2,017 | Public               | B9              |   456 |
|  2,017 | Public               | B10             |   380 |
|  2,018 | Foreign              | B1              |    39 |
|  2,018 | Foreign              | B2              |    29 |
|  2,018 | Foreign              | B3              |    15 |
|  2,018 | Foreign              | B4              |    31 |
|  2,018 | Foreign              | B5              |    15 |
|  2,018 | Foreign              | B6              |    22 |
|  2,018 | Foreign              | B7              |    14 |
|  2,018 | Foreign              | B8              |    19 |
|  2,018 | Foreign              | B9              |    15 |
|  2,018 | Foreign              | B10             |    16 |
|  2,018 | Private              | B1              | 2,572 |
|  2,018 | Private              | B2              | 1,981 |
|  2,018 | Private              | B3              | 1,691 |
|  2,018 | Private              | B4              | 1,895 |
|  2,018 | Private              | B5              | 1,712 |
|  2,018 | Private              | B6              | 1,690 |
|  2,018 | Private              | B7              | 1,441 |
|  2,018 | Private              | B8              | 1,455 |
|  2,018 | Private              | B9              | 1,395 |
|  2,018 | Private              | B10             | 1,542 |
|  2,018 | Public               | B1              |   612 |
|  2,018 | Public               | B2              |   429 |
|  2,018 | Public               | B3              |   393 |
|  2,018 | Public               | B4              |   394 |
|  2,018 | Public               | B5              |   399 |
|  2,018 | Public               | B6              |   414 |
|  2,018 | Public               | B7              |   341 |
|  2,018 | Public               | B8              |   328 |
|  2,018 | Public               | B9              |   369 |
|  2,018 | Public               | B10             |   377 |

---


## Citizenship Profile for No-PLE-Match Examinees

| Metric | Value | Population | Note |
|---|---|---|---|
| Profiled no-PLE-match records | 38,738 | no-PLE-match, observable, uni subset | - |
| Foreigners | 5,002 | rows above | Verified Foreigner |
| Filipinos | 33,723 | rows above | - |
| Distinct citizenship labels | 43 | rows above | - |

### Citizenship Profile KPIs

(Foreigners vs Filipinos pie chart uses the two rows above: Foreigners and Filipinos.)


### Citizenship Counts

*Population: no-PLE-match observable examinees with a citizenship label, n=38,738*

| CITIZENSHIP_FINAL     |      n |
|:----------------------|-------:|
| Filipino              | 33,723 |
| India                 |  2,588 |
| Thailand              |    573 |
| Nepal                 |    418 |
| United States         |    327 |
| Nigeria               |    127 |
| Sri Lanka             |    124 |
| Korea (South)         |    123 |
| Iran                  |    121 |
| Foreign (unspecified) |    102 |
| Indonesia             |     76 |
| Malaysia              |     76 |
| Taiwan                |     63 |
| Somalia               |     38 |
| Canada                |     35 |
| China                 |     32 |
| Japan                 |     30 |
| Pakistan              |     26 |
| Kenya                 |     20 |
| Australia             |     18 |
| United Kingdom        |     18 |
| Sudan                 |     14 |
| Ghana                 |     12 |
| Bangladesh            |      8 |
| Myanmar               |      8 |
| Ethiopia              |      5 |
| Germany               |      4 |
| Jordan                |      4 |
| Vietnam               |      3 |
| Rwanda                |      3 |
| Iraq                  |      3 |
| Kuwait                |      2 |
| Bhutan                |      2 |
| Austria               |      2 |
| New Zealand           |      2 |
| Sweden                |      1 |
| Yemen                 |      1 |
| Cameroon              |      1 |
| Lebanon               |      1 |
| Syria                 |      1 |
| Italy                 |      1 |
| Guam                  |      1 |
| Portugal              |      1 |

### Bin Distribution by Citizenship (Top 15)

| CITIZENSHIP_FINAL     |    B1 |    B2 |    B3 |    B4 |    B5 |    B6 |    B7 |    B8 |    B9 |   B10 |
|:----------------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| Canada                |  6.06 |  6.06 |  6.06 |  6.06 |  6.06 | 12.12 |  6.06 | 12.12 | 18.18 | 21.21 |
| Filipino              | 13.53 | 11.91 | 11.17 | 11.41 |  9.87 |  8.88 |  8.52 |  8.61 |  7.96 |  8.15 |
| Foreign (unspecified) | 22.45 | 12.24 |   5.1 |  10.2 |  8.16 |  9.18 |  4.08 |  6.12 |  9.18 | 13.27 |
| India                 | 39.53 | 13.65 |  9.83 |  9.43 |  7.68 |  6.01 |  5.31 |  3.86 |  2.59 |  2.11 |
| Indonesia             | 17.33 | 18.67 | 10.67 |     8 | 10.67 |  6.67 |     4 |  5.33 |  6.67 |    12 |
| Iran                  | 46.49 | 14.91 |  6.14 |  7.02 |  6.14 |  6.14 |  3.51 |  2.63 |  3.51 |  3.51 |
| Korea (South)         |  6.56 |  7.38 |  5.74 |  7.38 | 10.66 | 13.11 |  9.84 |  12.3 |   8.2 | 18.85 |
| Malaysia              |  27.4 | 17.81 | 15.07 | 15.07 |  5.48 |  6.85 |  1.37 |  2.74 |  4.11 |  4.11 |
| Nepal                 | 21.17 | 14.36 | 10.22 | 14.11 | 11.44 |  7.06 |  6.81 |  4.62 |  7.54 |  2.68 |
| Nigeria               |  31.2 |  10.4 |  11.2 |   7.2 |   8.8 |     8 |   5.6 |   4.8 |   5.6 |   7.2 |
| Somalia               | 85.71 |  3.57 |  7.14 |     0 |  3.57 |     0 |     0 |     0 |     0 |     0 |
| Sri Lanka             |  8.94 | 11.38 | 10.57 | 13.01 |  12.2 | 13.01 | 10.57 |  8.13 |  7.32 |  4.88 |
| Taiwan                | 27.42 | 14.52 | 11.29 |  4.84 |     0 |  4.84 |  9.68 |  9.68 |  8.06 |  9.68 |
| Thailand              | 36.48 | 16.37 |  13.7 | 10.32 |  6.76 |  4.98 |  4.45 |  3.74 |  1.78 |  1.42 |
| United States         |  8.28 |  4.46 |  3.82 |  6.37 |  6.37 |  7.32 |  7.64 | 13.06 | 18.15 | 24.52 |

### Top-Bin Share (B8-B10) by Citizenship (n>=3)

| CITIZENSHIP_FINAL     |      n |   top_n |   top_dec_pct |
|:----------------------|-------:|--------:|--------------:|
| Bangladesh            |      8 |       0 |             0 |
| Jordan                |      4 |       0 |             0 |
| Somalia               |     38 |       0 |             0 |
| Myanmar               |      8 |       0 |             0 |
| Sudan                 |     14 |       0 |             0 |
| Rwanda                |      3 |       0 |             0 |
| Thailand              |    573 |      39 |           6.8 |
| India                 |  2,588 |     195 |           7.5 |
| Iran                  |    121 |      11 |           9.1 |
| Malaysia              |     76 |       8 |          10.5 |
| Nepal                 |    418 |      61 |          14.6 |
| Pakistan              |     26 |       4 |          15.4 |
| Japan                 |     30 |       5 |          16.7 |
| Nigeria               |    127 |      22 |          17.3 |
| Kenya                 |     20 |       4 |            20 |
| Ethiopia              |      5 |       1 |            20 |
| Sri Lanka             |    124 |      25 |          20.2 |
| Indonesia             |     76 |      18 |          23.7 |
| Filipino              | 33,723 |   8,252 |          24.5 |
| Germany               |      4 |       1 |            25 |
| Taiwan                |     63 |      17 |            27 |
| Foreign (unspecified) |    102 |      28 |          27.5 |
| Ghana                 |     12 |       4 |          33.3 |
| Iraq                  |      3 |       1 |          33.3 |
| China                 |     32 |      11 |          34.4 |
| Korea (South)         |    123 |      48 |            39 |
| Australia             |     18 |       8 |          44.4 |
| Canada                |     35 |      17 |          48.6 |
| United States         |    327 |     175 |          53.5 |
| Vietnam               |      3 |       2 |          66.7 |
| United Kingdom        |     18 |      14 |          77.8 |

### Box Summary: Percentile Rank by Citizenship (n>=5)

<!-- chart_type: box | x: CITIZENSHIP_FINAL | y: NMS_PER_num | series: none
     population: citizenship groups with n>=5
     n: 38,705 | denominator: no-PLE-match observable examinees
     source_tab: 4 | element_id: fig_pc_box_pct -->

| CITIZENSHIP_FINAL     |      n |   min |    q1 |   median |    q3 |   max |   outliers |
|:----------------------|-------:|------:|------:|---------:|------:|------:|-----------:|
| Australia             |     15 |     1 |    43 |       73 |  93.5 |    99 |          0 |
| Bangladesh            |      8 |     2 | 12.25 |     30.5 | 51.25 |    62 |          0 |
| Canada                |     33 |     4 |    43 |       74 |    89 |    99 |          0 |
| China                 |     31 |     9 |  27.5 |       55 |    86 |    99 |          0 |
| Ethiopia              |      5 |     7 |    11 |       23 |    28 |    87 |          1 |
| Filipino              | 33,387 |     0 |    19 |       41 |    69 |    99 |          0 |
| Foreign (unspecified) |     98 |     1 |    11 |     39.5 | 75.75 |    98 |          0 |
| Ghana                 |     12 |    19 | 31.25 |     44.5 |    77 |    84 |          0 |
| India                 |  2,279 |     0 |     4 |       16 |    43 |    99 |          0 |
| Indonesia             |     75 |     1 |  15.5 |       32 |    63 |    99 |          0 |
| Iran                  |    114 |     1 |     2 |       11 | 39.75 |    96 |          0 |
| Japan                 |     30 |     1 | 22.25 |     38.5 |  54.5 |    89 |          0 |
| Kenya                 |     20 |     1 | 37.75 |       52 |    56 |    96 |          5 |
| Korea (South)         |    122 |     4 | 35.25 |     58.5 |    81 |    99 |          0 |
| Malaysia              |     73 |     1 |     9 |       24 |    39 |    98 |          4 |
| Myanmar               |      6 |     3 |  3.25 |        4 |   8.5 |    47 |          1 |
| Nepal                 |    411 |     1 |    12 |       32 |    55 |    97 |          0 |
| Nigeria               |    125 |     1 |     8 |       26 |    59 |    98 |          0 |
| Pakistan              |     25 |     1 |     4 |       20 |    64 |    92 |          0 |
| Somalia               |     28 |     1 |     1 |        2 |     4 |    48 |          4 |
| Sri Lanka             |    123 |     1 |  25.5 |       45 |    65 |    96 |          0 |
| Sudan                 |      9 |     2 |     6 |        9 |    20 |    26 |          0 |
| Taiwan                |     62 |     0 |  7.25 |       28 |    70 |    99 |          0 |
| Thailand              |    562 |     0 |     6 |       18 | 36.75 |    98 |         16 |
| United Kingdom        |     18 |    23 |    74 |     79.5 | 85.75 |    97 |          3 |
| United States         |    314 |     0 |    43 |       75 |    89 |    99 |          0 |

### Box Summary: TRUE Raw Score by Citizenship (n>=5)

<!-- chart_type: box | x: CITIZENSHIP_FINAL | y: TotalRawScoreTRUE | series: none
     population: citizenship groups with n>=5
     n: 38,705 | denominator: no-PLE-match observable examinees
     source_tab: 4 | element_id: fig_pc_box_raw -->

| CITIZENSHIP_FINAL     |      n |   min |     q1 |   median |     q3 |   max |   outliers |
|:----------------------|-------:|------:|-------:|---------:|-------:|------:|-----------:|
| Australia             |     18 |    50 |  119.5 |      146 | 168.75 |   200 |          0 |
| Bangladesh            |      8 |    69 |  89.75 |    102.5 | 116.25 |   135 |          0 |
| Canada                |     35 |    77 |  117.5 |      145 |  166.5 |   223 |          0 |
| China                 |     32 |    86 |  104.5 |    127.5 | 163.25 |   215 |          0 |
| Ethiopia              |      5 |    82 |     89 |      101 |    110 |   164 |          1 |
| Filipino              | 33,697 |    37 |     97 |      117 |    139 |   223 |        118 |
| Foreign (unspecified) |    102 |    56 |  87.25 |    114.5 |  150.5 |   200 |          0 |
| Ghana                 |     12 |    94 | 103.75 |      110 |    135 |   151 |          0 |
| India                 |  2,586 |     9 |     69 |       89 |    111 |   216 |         10 |
| Indonesia             |     76 |    56 |  93.75 |      108 |  132.5 |   198 |          2 |
| Iran                  |    121 |    40 |     68 |       88 |    117 |   171 |          0 |
| Japan                 |     30 |    65 |    100 |      111 |    126 |   166 |          1 |
| Kenya                 |     19 |    57 |    110 |      121 |    130 |   183 |          4 |
| Korea (South)         |    123 |    79 |  111.5 |      131 |    156 |   194 |          0 |
| Malaysia              |     76 |    44 |     84 |     99.5 | 117.25 |   174 |          1 |
| Myanmar               |      8 |    50 |   68.5 |       73 |  80.75 |   125 |          2 |
| Nepal                 |    417 |    47 |     89 |      108 |    125 |   195 |          5 |
| Nigeria               |    127 |    59 |   81.5 |      102 |    125 |   178 |          0 |
| Pakistan              |     26 |    48 |     73 |       93 |  129.5 |   176 |          0 |
| Somalia               |     38 |    43 |  61.25 |       69 |     74 |   114 |          3 |
| Sri Lanka             |    124 |    60 | 100.75 |      119 |    134 |   177 |          0 |
| Sudan                 |     14 |    48 |     61 |     76.5 |  91.25 |   104 |          0 |
| Taiwan                |     60 |    56 |   86.5 |      112 |    140 |   184 |          0 |
| Thailand              |    568 |    46 |     80 |       95 |    113 |   176 |          8 |
| United Kingdom        |     18 |    99 | 140.25 |      151 |    162 |   186 |          1 |
| United States         |    323 |    47 |  120.5 |      148 |    168 |   216 |          1 |

### Summary by Citizenship

| CITIZENSHIP_FINAL     |   n_examinees |   median_percentile_rank |   median_true_raw_score |   top_decile_n |   top_decile_pct |   bottom_decile_n |   bottom_decile_pct |
|:----------------------|--------------:|-------------------------:|------------------------:|---------------:|-----------------:|------------------:|--------------------:|
| Filipino              |        33,723 |                       41 |                     117 |          8,252 |            24.47 |            12,222 |               36.24 |
| India                 |         2,588 |                       16 |                      89 |            195 |             7.53 |             1,436 |               55.49 |
| Thailand              |           573 |                       18 |                      95 |             39 |             6.81 |               374 |               65.27 |
| Nepal                 |           418 |                       32 |                     108 |             61 |            14.59 |               188 |               44.98 |
| United States         |           327 |                       75 |                     148 |            175 |            53.52 |                52 |                15.9 |
| Nigeria               |           127 |                       26 |                     102 |             22 |            17.32 |                66 |               51.97 |
| Sri Lanka             |           124 |                       45 |                     119 |             25 |            20.16 |                38 |               30.65 |
| Korea (South)         |           123 |                     58.5 |                     131 |             48 |            39.02 |                24 |               19.51 |
| Iran                  |           121 |                       11 |                      88 |             11 |             9.09 |                77 |               63.64 |
| Foreign (unspecified) |           102 |                     39.5 |                   114.5 |             28 |            27.45 |                39 |               38.24 |
| Indonesia             |            76 |                       32 |                     108 |             18 |            23.68 |                35 |               46.05 |
| Malaysia              |            76 |                       24 |                    99.5 |              8 |            10.53 |                44 |               57.89 |
| Taiwan                |            63 |                       28 |                     112 |             17 |            26.98 |                33 |               52.38 |
| Somalia               |            38 |                        2 |                      69 |              0 |                0 |                27 |               71.05 |
| Canada                |            35 |                       74 |                     145 |             17 |            48.57 |                 6 |               17.14 |
| China                 |            32 |                       55 |                   127.5 |             11 |            34.38 |                 9 |               28.12 |
| Japan                 |            30 |                     38.5 |                     111 |              5 |            16.67 |                11 |               36.67 |
| Pakistan              |            26 |                       20 |                      93 |              4 |            15.38 |                14 |               53.85 |
| Kenya                 |            20 |                       52 |                     121 |              4 |               20 |                 5 |                  25 |
| United Kingdom        |            18 |                     79.5 |                     151 |             14 |            77.78 |                 1 |                5.56 |
| Australia             |            18 |                       73 |                     146 |              8 |            44.44 |                 2 |               11.11 |
| Sudan                 |            14 |                        9 |                    76.5 |              0 |                0 |                 9 |               64.29 |
| Ghana                 |            12 |                     44.5 |                     110 |              4 |            33.33 |                 3 |                  25 |
| Bangladesh            |             8 |                     30.5 |                   102.5 |              0 |                0 |                 4 |                  50 |
| Myanmar               |             8 |                        4 |                      73 |              0 |                0 |                 5 |                62.5 |
| Ethiopia              |             5 |                       23 |                     101 |              1 |               20 |                 4 |                  80 |
| Germany               |             4 |                     30.5 |                     105 |              1 |               25 |                 2 |                  50 |
| Jordan                |             4 |                        3 |                    68.5 |              0 |                0 |                 3 |                  75 |
| Vietnam               |             3 |                       89 |                     171 |              2 |            66.67 |                 0 |                   0 |
| Rwanda                |             3 |                       14 |                      91 |              0 |                0 |                 2 |               66.67 |
| Iraq                  |             3 |                        6 |                      82 |              1 |            33.33 |                 2 |               66.67 |
| Austria               |             2 |                       54 |                   132.5 |              1 |               50 |                 0 |                   0 |
| Bhutan                |             2 |                     47.5 |                   122.5 |              1 |               50 |                 1 |                  50 |
| New Zealand           |             2 |                     46.5 |                     113 |              1 |               50 |                 1 |                  50 |
| Kuwait                |             2 |                      2.5 |                    62.5 |              0 |                0 |                 2 |                 100 |
| Syria                 |             1 |                       54 |                     132 |              0 |                0 |                 0 |                   0 |
| Lebanon               |             1 |                       47 |                     124 |              0 |                0 |                 0 |                   0 |
| Italy                 |             1 |                       44 |                     119 |              0 |                0 |                 0 |                   0 |
| Yemen                 |             1 |                       38 |                     114 |              0 |                0 |                 0 |                   0 |
| Sweden                |             1 |                       26 |                     103 |              0 |                0 |                 1 |                 100 |
| Portugal              |             1 |                       23 |                      98 |              0 |                0 |                 1 |                 100 |
| Cameroon              |             1 |                        8 |                      87 |              0 |                0 |                 1 |                 100 |
| Guam                  |             1 |                        1 |                      66 |              0 |                0 |                 1 |                 100 |

### Year Distribution by Citizenship

| CITIZENSHIP_FINAL     |   2006 |   2007 |   2008 |   2009 |   2010 |   2011 |   2012 |   2013 |   2014 |
|:----------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| Australia             |      2 |      0 |      0 |      1 |      1 |      3 |      1 |      2 |      8 |
| Austria               |      0 |      0 |      0 |      1 |      0 |      1 |      0 |      0 |      0 |
| Bangladesh            |      0 |      0 |      1 |      1 |      1 |      1 |      0 |      1 |      3 |
| Bhutan                |      0 |      2 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |
| Cameroon              |      0 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| Canada                |      3 |      1 |      3 |      3 |      5 |      4 |      4 |      7 |      5 |
| China                 |      4 |      0 |      3 |      4 |      3 |      2 |      5 |      3 |      8 |
| Ethiopia              |      0 |      0 |      0 |      2 |      2 |      0 |      1 |      0 |      0 |
| Filipino              |  1,594 |  1,597 |  2,193 |  3,947 |  4,074 |  4,441 |  4,782 |  4,886 |  6,209 |
| Foreign (unspecified) |     10 |      7 |     13 |     19 |      8 |      9 |      7 |     17 |     12 |
| Germany               |      1 |      0 |      1 |      0 |      1 |      0 |      1 |      0 |      0 |
| Ghana                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      2 |      9 |
| Guam                  |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |
| India                 |     43 |    187 |    180 |    140 |     79 |     44 |    147 |    337 |  1,431 |
| Indonesia             |      5 |     10 |      6 |      5 |     13 |      6 |     11 |     10 |     10 |
| Iran                  |      0 |     19 |     16 |     26 |     25 |     15 |      9 |      7 |      4 |
| Iraq                  |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      3 |
| Italy                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
| Japan                 |      3 |      2 |      4 |      0 |      2 |      2 |      6 |      4 |      7 |
| Jordan                |      0 |      0 |      0 |      0 |      0 |      1 |      0 |      2 |      1 |
| Kenya                 |      0 |      0 |      1 |      2 |      1 |      6 |      4 |      3 |      3 |
| Korea (South)         |     10 |     17 |      9 |     14 |      8 |     12 |     15 |     17 |     21 |
| Kuwait                |      1 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| Lebanon               |      0 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
| Malaysia              |      0 |      0 |      1 |      9 |      5 |     10 |     22 |     14 |     15 |
| Myanmar               |      0 |      0 |      0 |      2 |      0 |      0 |      2 |      2 |      2 |
| Nepal                 |      2 |      2 |      3 |     55 |     47 |     74 |     88 |     73 |     74 |
| New Zealand           |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |      1 |
| Nigeria               |      1 |      3 |      2 |      4 |      9 |     10 |     10 |     21 |     67 |
| Pakistan              |      1 |      0 |      0 |      4 |      5 |      2 |      9 |      3 |      2 |
Person-level record detail (38,738 rows) is available in the live dashboard and its CSV downloads; not dumped inline here per export contract Rule 3.


---


## Comparative Analysis: Foreigners vs Filipino Undergrad Groups

*Population: 4 groups (Verified Foreigner; Filipino+foreign undergrad; Filipino+public undergrad; Filipino+private undergrad), n=73,080 combined*

| Group                         |      n |   median_percentile_rank |   q25_pct |   q75_pct |   median_raw_score |   PLE linkage rate % |
|:------------------------------|-------:|-------------------------:|----------:|----------:|-------------------:|---------------------:|
| Filipinos (foreign undergrad) |    641 |                       66 |        35 |        86 |                137 |                35.12 |
| Filipinos (private undergrad) | 52,094 |                       50 |        25 |        76 |                123 |                42.82 |
| Filipinos (public undergrad)  | 13,919 |                       68 |        36 |        90 |                138 |                47.37 |
| Foreigners (non-Filipino)     |  4,742 |                       26 |         6 |        55 |                100 |                 2.46 |

### Box Summary: Percentile Rank by Comparison Group

<!-- chart_type: box | x: _cmp_group | y: NMS_PER_num | series: none
     population: 4 comparison groups
     n: 73,080 | denominator: combined comparison population
     source_tab: 4 | element_id: fig_cmp_pct_box -->

| _cmp_group                    |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|:------------------------------|-------:|------:|-----:|---------:|-----:|------:|-----------:|
| Filipinos (foreign undergrad) |    641 |     1 |   35 |       66 |   86 |    99 |          0 |
| Filipinos (private undergrad) | 52,094 |     0 |   25 |       50 |   76 |    99 |          0 |
| Filipinos (public undergrad)  | 13,919 |     0 |   36 |       68 |   90 |    99 |          0 |
| Foreigners (non-Filipino)     |  4,742 |     0 |    6 |       26 |   55 |    99 |          0 |

### Box Summary: TRUE Raw Score by Comparison Group

<!-- chart_type: box | x: _cmp_group | y: TotalRawScoreTRUE | series: none
     population: 4 comparison groups
     n: 73,080 | denominator: combined comparison population
     source_tab: 4 | element_id: fig_cmp_raw_box -->

| _cmp_group                    |      n |   min |   q1 |   median |     q3 |   max |   outliers |
|:------------------------------|-------:|------:|-----:|---------:|-------:|------:|-----------:|
| Filipinos (foreign undergrad) |    652 |    38 |  110 |      137 | 160.25 |   219 |          0 |
| Filipinos (private undergrad) | 53,003 |    10 |  103 |      123 |    146 |   227 |        116 |
| Filipinos (public undergrad)  | 14,259 |     9 |  111 |      138 |    167 |   225 |          7 |
| Foreigners (non-Filipino)     |  5,112 |     9 |   77 |      100 |    124 |   223 |         34 |

### Bin Distribution by Comparison Group

| _cmp_group                    |    B1 |    B2 |   B3 |    B4 |    B5 |   B6 |    B7 |    B8 |    B9 |   B10 |
|:------------------------------|------:|------:|-----:|------:|------:|-----:|------:|------:|------:|------:|
| Filipinos (foreign undergrad) |  8.27 |   6.4 | 6.24 |  7.02 |  5.62 | 9.36 | 11.39 | 11.39 | 13.88 | 20.44 |
| Filipinos (private undergrad) |  10.5 |   9.2 | 9.17 | 10.16 | 10.26 |  9.7 |  9.44 |  9.81 | 10.16 | 11.58 |
| Filipinos (public undergrad)  |  7.86 |  6.37 | 6.05 |  7.21 |  7.53 | 7.63 |  9.02 |  9.99 | 12.52 | 25.83 |
| Foreigners (non-Filipino)     | 31.04 | 12.48 | 9.72 |  9.45 |  8.12 | 6.71 |  5.71 |  5.42 |  5.46 |  5.88 |

### Top vs Bottom Bin Share by Comparison Group

| Group                         |   Top B8-B10 (%) |   Bottom B1-B3 (%) |
|:------------------------------|-----------------:|-------------------:|
| Filipinos (foreign undergrad) |            45.71 |              20.91 |
| Filipinos (private undergrad) |            31.55 |              28.87 |
| Filipinos (public undergrad)  |            48.34 |              20.28 |
| Foreigners (non-Filipino)     |            16.76 |              53.24 |

---


## Bin Distribution by Course Group

<!-- chart_type: heatmap+top_share_bar | x: UNDERGRAD_COURSE_GROUP | y: PercentileBin | series: fig_t4_heatmap_course
     population: row %
     n: best-record trend cohort | denominator: 134,869
     source_tab: best-record examinees | element_id: 4 -->

| UNDERGRAD_COURSE_GROUP       |    B1 |    B2 |   B3 |    B4 |    B5 |    B6 |   B7 |    B8 |    B9 |   B10 |
|:-----------------------------|------:|------:|-----:|------:|------:|------:|-----:|------:|------:|------:|
| Education                    |  9.09 |  8.88 | 9.26 |  9.67 |  10.6 |  9.11 | 9.72 |  9.61 | 10.45 | 13.61 |
| Engineering & Technology     |  5.21 |  5.89 | 5.89 |  5.62 |  8.63 |  8.77 | 7.53 |    10 | 14.66 | 27.81 |
| Medical & Allied             |    10 |  9.74 | 9.43 | 10.67 | 10.82 | 10.66 | 9.77 |  9.79 |  9.39 |  9.74 |
| Natural Sciences             | 12.29 |  8.52 | 7.54 |  8.34 |  8.35 |  8.79 | 9.44 |  9.98 | 11.04 |  15.7 |
| Other                        |  9.76 |  8.47 | 8.47 |  9.37 |  9.38 |  9.63 | 9.63 | 10.41 | 11.63 | 13.24 |
| Social & Behavioral Sciences | 19.91 | 11.02 | 8.62 |  8.38 |  7.82 |  8.29 | 7.49 |  7.93 |  8.92 | 11.61 |

---


## Table 12 -- Percentile Summary by Course Group

| UNDERGRAD_COURSE_GROUP       |      n |   median |   q25 |   q75 |
|:-----------------------------|-------:|---------:|------:|------:|
| Education                    |  3,445 |       53 |    27 |    78 |
| Engineering & Technology     |    730 |       72 | 41.25 |    91 |
| Medical & Allied             | 63,468 |       49 |    25 |    73 |
| Natural Sciences             | 40,196 |       55 |    25 |    81 |
| Other                        |  8,248 |       54 |    27 |    79 |
| Social & Behavioral Sciences | 15,758 |       42 |    14 |    74 |

---


# Tab 5 -- University Type Analysis


## Table 13 -- Institution Type by Location Mix

*Population: undergrad type+location present, n=133,315*

| UNDERGRAD_UNI_TYPE   | UNDERGRAD_UNI_LOCATION   |   Count |   Percent of total |
|:---------------------|:-------------------------|--------:|-------------------:|
| Foreign              | International            |   1,892 |               1.42 |
| Private              | Local                    | 103,885 |              77.92 |
| Public               | Local                    |  27,538 |              20.66 |

---


## Table 14 -- Institution Type by Location Matrix


### Counts (with totals)

| UNDERGRAD_UNI_TYPE   |   International |   Local |     All |
|:---------------------|----------------:|--------:|--------:|
| Foreign              |           1,892 |       0 |   1,892 |
| Private              |               0 | 103,885 | 103,885 |
| Public               |               0 |  27,538 |  27,538 |
| All                  |           1,892 | 131,423 | 133,315 |

### Row % (within UNDERGRAD_UNI_TYPE)

| UNDERGRAD_UNI_TYPE   |   International |   Local |
|:---------------------|----------------:|--------:|
| Foreign              |             100 |       0 |
| Private              |               0 |     100 |
| Public               |               0 |     100 |

### Column % (within UNDERGRAD_UNI_LOCATION)

| UNDERGRAD_UNI_TYPE   |   International |   Local |
|:---------------------|----------------:|--------:|
| Foreign              |             100 |       0 |
| Private              |               0 |   79.05 |
| Public               |               0 |   20.95 |

---


## Bin Distribution by Institution Type x Location

<!-- chart_type: heatmap+top_share_bar | x: PercentileBin | y: UNDERGRAD_UNI_TYPE x LOCATION | series: fig_t5_heatmap_instloc
     population: row %
     n: valid percentile bin | denominator: 130,334
     source_tab: best-record uni subset | element_id: 5 -->

| index                   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:------------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign (International) | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private (Local)         | 12.05 |  9.7 | 9.01 | 9.92 |  9.9 | 9.94 | 9.47 | 9.68 |  9.72 | 10.61 |
| Public (Local)          |  10.7 |  8.1 | 7.51 | 8.22 | 8.52 | 8.88 | 9.09 | 9.63 | 11.28 | 18.07 |

---


## Bin Composition by University Type (%)

<!-- chart_type: stacked_bar | x: UNDERGRAD_UNI_TYPE | y: PercentileBin | series: fig_t5_stacked_uni
     population: row %
     n: valid percentile bin | denominator: 130,334
     source_tab: best-record uni subset | element_id: 5 -->

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private              | 12.05 |  9.7 | 9.01 | 9.92 |  9.9 | 9.94 | 9.47 | 9.68 |  9.72 | 10.61 |
| Public               |  10.7 |  8.1 | 7.51 | 8.22 | 8.52 | 8.88 | 9.09 | 9.63 | 11.28 | 18.07 |

---


## Table 15 -- Bin Counts by University Type

| UNDERGRAD_UNI_TYPE   |     B1 |    B2 |    B3 |     B4 |     B5 |     B6 |    B7 |    B8 |    B9 |    B10 |   Total students |
|:---------------------|-------:|------:|------:|-------:|-------:|-------:|------:|------:|------:|-------:|-----------------:|
| Foreign              |    262 |   174 |   140 |    176 |    145 |    164 |   161 |   175 |   197 |    266 |            1,860 |
| Private              | 12,248 | 9,857 | 9,151 | 10,082 | 10,058 | 10,104 | 9,622 | 9,833 | 9,876 | 10,784 |          101,615 |
| Public               |  2,874 | 2,176 | 2,016 |  2,209 |  2,288 |  2,385 | 2,442 | 2,586 | 3,029 |  4,854 |           26,859 |

---


## Table 16 -- Foreign Examinee Summary

| Metric | Value | Population | Note |
|---|---|---|---|
| Foreign examinees | 1,860 | uni_base | - |
| % of total | 1.43% | uni_base | - |
| Median percentile | 52.0 | foreign subset | - |
| Top-bin (B8-B10) % | 34.30% | foreign subset | - |

---


## Bin Distribution Among Foreign Examinees

<!-- chart_type: stacked_bar | x: UNDERGRAD_UNI_TYPE | y: PercentileBin | series: fig_t5_foreign_bin
     population: row %
     n: Foreign examinees only | denominator: 1,860
     source_tab: Foreign university-type subset | element_id: 5 -->

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |

---


## Figure 16 -- Medical & Allied vs Other Courses by University Type

*Population: undergrad type+location present, n=133,315*

| UNDERGRAD_UNI_TYPE   |   Medical & Allied |   Other Courses |
|:---------------------|-------------------:|----------------:|
| Foreign              |              40.38 |           59.62 |
| Private              |              49.53 |           50.47 |
| Public               |              41.17 |           58.83 |

---


## Table 17 -- University Listings by University Type


### Public Universities

| UNDERGRAD_UNIVERSITY                                               | UNDERGRAD_UNI_LOCATION   |   total_applicants |
|:-------------------------------------------------------------------|:-------------------------|-------------------:|
| UNIVERSITY OF THE PHILIPPINES - MANILA                             | Local                    |              3,629 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                            | Local                    |              3,238 |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                          | Local                    |              2,458 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                      | Local                    |              1,386 |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                          | Local                    |              1,321 |
| WEST VISAYAS STATE UNIVERSITY - MAIN                               | Local                    |              1,245 |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                   | Local                    |              1,238 |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY         | Local                    |              1,185 |
| MINDANAO STATE UNIVERSITY - MARAWI                                 | Local                    |              1,005 |
| WESTERN MINDANAO STATE UNIVERSITY                                  | Local                    |                863 |
| BICOL UNIVERSITY - MAIN                                            | Local                    |                740 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                             | Local                    |                693 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                            | Local                    |                674 |
| UNIVERSITY OF THE PHILIPPINES - LOS BANOS LAGUNA                   | Local                    |                487 |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                           | Local                    |                363 |
| WEST VISAYAS STATE UNIVERSITY ILOILO                               | Local                    |                360 |
| CEBU NORMAL UNIVERSITY                                             | Local                    |                356 |
| MINDANAO STATE UNIVERSITY MARAWI CITY                              | Local                    |                344 |
| CENTRAL MINDANAO UNIVERSITY                                        | Local                    |                327 |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                             | Local                    |                313 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                          | Local                    |                304 |
| PALAWAN STATE UNIVERSITY                                           | Local                    |                253 |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                    | Local                    |                244 |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                 | Local                    |                241 |
| MINDANAO STATE UNIVERSITY ILIGAN CITY                              | Local                    |                203 |
| BULACAN STATE UNIVERSITY - MAIN                                    | Local                    |                201 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO CITY                        | Local                    |                195 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS ILOILO                     | Local                    |                182 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE      | Local                    |                171 |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                         | Local                    |                158 |
| WESTERN MINDANAO STATE UNIVERSITY ZAMBOANGA CITY                   | Local                    |                145 |
| BENGUET STATE UNIVERSITY - MAIN                                    | Local                    |                142 |
| CENTRAL LUZON STATE UNIVERSITY                                     | Local                    |                140 |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES | Local                    |                140 |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                             | Local                    |                138 |
| NOT SPECIFIED/UNLISTED                                             | Local                    |                135 |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                             | Local                    |                121 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                      | Local                    |                118 |
| UNIVERSITY OF EASTERN PHILIPPINES                                  | Local                    |                107 |
| CAVITE STATE UNIVERSITY - MAIN                                     | Local                    |                 72 |
| LEYTE NORMAL UNIVERSITY                                            | Local                    |                 71 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                              | Local                    |                 63 |
| CATANDUANES STATE COLLEGE - MAIN                                   | Local                    |                 59 |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                | Local                    |                 56 |
| UNIVERSITY OF MAKATI                                               | Local                    |                 56 |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                         | Local                    |                 53 |
| UNIVERSITY OF THE PHILIPPINES - TACLOBAN                           | Local                    |                 49 |
| BICOL UNIVERSITY - TABACO                                          | Local                    |                 48 |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                           | Local                    |                 48 |
| UNIVERSITY OF THE PHILIPPINES - CEBU COLLEGE                       | Local                    |                 46 |
<!-- truncated: true | shown: 50 | total: 215 -->


### Private Universities

| UNDERGRAD_UNIVERSITY                                                           | UNDERGRAD_UNI_LOCATION   |   total_applicants |
|:-------------------------------------------------------------------------------|:-------------------------|-------------------:|
| UNIVERSITY OF SANTO TOMAS                                                      | Local                    |             18,038 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA                                      | Local                    |              4,528 |
| FAR EASTERN UNIVERSITY                                                         | Local                    |              4,309 |
| SAN PEDRO COLLEGE                                                              | Local                    |              3,644 |
| SAINT LOUIS UNIVERSITY                                                         | Local                    |              3,221 |
| CEBU DOCTOR'S UNIVERSITY                                                       | Local                    |              2,406 |
| DE LA SALLE UNIVERSITY - MANILA                                                | Local                    |              2,242 |
| OUR LADY OF FATIMA UNIVERSITY (FATIMA MEDICAL SCIENCE FOUNDATION) - VALENZUELA | Local                    |              2,041 |
| CENTRO ESCOLAR UNIVERSITY - MANILA                                             | Local                    |              2,022 |
| SOUTHWESTERN UNIVERSITY                                                        | Local                    |              1,841 |
| ATENEO DE MANILA UNIVERSITY - QUEZON CITY                                      | Local                    |              1,782 |
| VELEZ COLLEGE                                                                  | Local                    |              1,750 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS                                            | Local                    |              1,724 |
| DAVAO MEDICAL SCHOOL FOUNDATION                                                | Local                    |              1,665 |
| EMILIO AGUINALDO COLLEGE                                                       | Local                    |              1,577 |
| AMA COMPUTER COLLEGE - MAKATI                                                  | Local                    |              1,519 |
| ANGELES UNIVERSITY FOUNDATION                                                  | Local                    |              1,337 |
| SILLIMAN UNIVERSITY                                                            | Local                    |              1,303 |
| AGO MEDICAL AND EDUCATIONAL CENTER - BICOL CHRISTIAN COLLEGE OF MEDICINE       | Local                    |              1,284 |
| XAVIER UNIVERSITY                                                              | Local                    |              1,228 |
| BROKENSHIRE COLLEGE                                                            | Local                    |              1,226 |
| ATENEO DE ZAMBOANGA UNIVERSITY                                                 | Local                    |              1,172 |
| FEU - DR. NICANOR REYES MEDICAL FOUNDATION                                     | Local                    |              1,151 |
| LYCEUM NORTHWESTERN UNIVERSITY                                                 | Local                    |              1,048 |
| UNIVERSITY OF SAN AGUSTIN                                                      | Local                    |                995 |
| ATENEO DE DAVAO UNIVERSITY                                                     | Local                    |                981 |
| DE LA SALLE HEALTH SCIENCES INSTITUTE                                          | Local                    |                952 |
| TRINITY UNIVERSITY OF ASIA                                                     | Local                    |                897 |
| MANILA CENTRAL UNIVERSITY                                                      | Local                    |                837 |
| ATENEO DE MANILA UNIVERSITY                                                    | Local                    |                751 |
| CENTRAL PHILIPPINE UNIVERSITY                                                  | Local                    |                697 |
| VIRGEN MILAGROSA UNIVERSITY FOUNDATION AND VMU INSTITUTE OF MEDICAL FOUNDATION | Local                    |                697 |
| ADVENTIST UNIVERSITY OF THE PHILIPPINES                                        | Local                    |                672 |
| SAINT PAUL UNIVERSITY PHILIPPINES                                              | Local                    |                662 |
| UNIVERSITY OF ST. LA SALLE                                                     | Local                    |                629 |
| UNIVERSITY OF THE IMMACULATE CONCEPTION                                        | Local                    |                601 |
| VELEZ COLLEGE CEBU                                                             | Local                    |                559 |
| UNIVERSITY OF THE EAST RAMON MAGSAYSAY MEMORIAL MEDICAL CENTER                 | Local                    |                555 |
| UNIVERSITY OF SAN CARLOS                                                       | Local                    |                551 |
| SAN BEDA COLLEGE                                                               | Local                    |                530 |
| SAN PEDRO COLLEGE DAVAO CITY                                                   | Local                    |                512 |
| MANILA TYTANA COLLEGES                                                         | Local                    |                485 |
| ANGELES UNIVERSITY FOUNDATION ANGELES CITY                                     | Local                    |                481 |
| CENTRO ESCOLAR UNIVERSITY - MAKATI                                             | Local                    |                472 |
| DOÑA REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION                            | Local                    |                468 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS CAVITE                                     | Local                    |                456 |
| DAVAO DOCTORS COLLEGE                                                          | Local                    |                444 |
| LICEO DE CAGAYAN UNIVERSITY                                                    | Local                    |                428 |
| FAR EASTERN UNIVERSITY - NRMF (FAIRVIEW Q.C.)                                  | Local                    |                427 |
| OUR LADY OF FATIMA UNIVERSITY - QUEZON CITY                                    | Local                    |                423 |
<!-- truncated: true | shown: 50 | total: 800 -->


### Foreign Universities

| UNDERGRAD_UNIVERSITY                         | UNDERGRAD_UNI_LOCATION   |   total_applicants |
|:---------------------------------------------|:-------------------------|-------------------:|
| RANGSIT UNIVERSITY                           | International            |                 69 |
| UNIVERSITY OF CALIFORNIA - DAVIS             | International            |                 43 |
| UNIVERSITY OF CALIFORNIA - IRVINE            | International            |                 40 |
| TRINITY COLLEGE                              | International            |                 40 |
| RANGSIT UNIVERSITY THAILAND                  | International            |                 38 |
| MAHIDOL UNIVERSITY                           | International            |                 36 |
| UNIVERSITY OF CALIFORNIA LOS ANGELES         | International            |                 30 |
| MAHIDOL UNIVERSITY THAILAND                  | International            |                 28 |
| CHULALONGKORN UNIVERSITY                     | International            |                 28 |
| CALIFORNIA STATE UNIVERSITY                  | International            |                 27 |
| UNIVERSITY OF CALIFORNIA RIVERSIDE CA USA    | International            |                 25 |
| AL KWARIZMI INTERNATIONAL COLLEGE FOUNDATION | International            |                 23 |
| UNIVERSITY OF CALIFORNIA - SAN DIEGO         | International            |                 23 |
| CHIANG MAI UNIVERSITY                        | International            |                 23 |
| THAMMASAT UNIVERSITY                         | International            |                 20 |
| UNIVERSITY OF CALIFORNIA-RIVERSIDE           | International            |                 19 |
| WESTERN STATE UNIVERSITY OF COLORADO         | International            |                 19 |
| UNIVERSITY OF TORONTO                        | International            |                 17 |
| UNIVERSITY OF CALIFORNIA BERKELEY            | International            |                 17 |
| MAE FAH LUANG UNIVERSITY                     | International            |                 17 |
| CHULALONGKORN UNIVERSITY THAILAND            | International            |                 17 |
| UNIVERSITY OF WASHINGTON                     | International            |                 16 |
| NARESUAN UNIVERSITY                          | International            |                 15 |
| UNIVERSITY OF FLORIDA                        | International            |                 15 |
| MONAD UNIVERSITY                             | International            |                 14 |
| UNIVERSITY OF NEVADA LAS VEGAS               | International            |                 12 |
| UNIVERSITY OF CALIFORNIA SANTA BARBARA       | International            |                 12 |
| UNIVERSITY OF SAN FRANCISCO                  | International            |                 11 |
| HUACHIEW CHALERMPRAKIET UNIVERSITY           | International            |                 11 |
| SRINAKHARINWIROT UNIVERSITY                  | International            |                 11 |
| RUTGERS UNIVERSITY NEW JERSEY                | International            |                 11 |
| RUTGERS UNIVERSITY                           | International            |                 10 |
| UNIVERSITY OF GUAM                           | International            |                 10 |
| UNIVERSITAS ADVENT INDONESIA                 | International            |                 10 |
| UNIVERSITY OF CENTRAL FLORIDA                | International            |                 10 |
| STONY BROOK UNIVERSITY                       | International            |                  9 |
| CALIFORNIA STATE UNIVERSITY LONG BEACH       | International            |                  9 |
| CALIFORNIA STATE UNIVERSITY FRESNO           | International            |                  9 |
| BURAPHA UNIVERSITY                           | International            |                  9 |
| VIRGINIA COMMONWEALTH UNIVERSITY             | International            |                  9 |
| UNIVERSITY OF CALIFORNIA AT STA. CRUZ U.S.A. | International            |                  9 |
| UNIVERSITY OF HAWAII AT MANOA                | International            |                  9 |
| UNIVERSITY OF ILLINOIS CHICAGO               | International            |                  9 |
| UNIVERSITY OF CALIFORNIA SANTA CRUZ          | International            |                  8 |
| THAMMASAT UNIV.                              | International            |                  8 |
| UNIVERSITY OF BRITISH COLUMBIA               | International            |                  8 |
| UNIVERSITY OF TEXAS                          | International            |                  8 |
| RAMKHAMHAENG UNIVERSITY                      | International            |                  8 |
| PRINCE OF SONGKLA UNIVERSITY                 | International            |                  8 |
| UNIVERSITY OF HOUSTON                        | International            |                  7 |
<!-- truncated: true | shown: 50 | total: 533 -->


---


# Tab 6 -- Flow & Pathways


## Table 18 -- University Type to Bin Flow

<!-- chart_type: sankey | x: UNDERGRAD_UNI_TYPE | y: PercentileBin | series: fig_t6_sankey_uni
     population: source->target->value
     n: uni subset | denominator: 130,334
     source_tab: best-record, Public/Private/Foreign | element_id: 6 -->

| UNDERGRAD_UNI_TYPE   | PercentileBin   |   count |
|:---------------------|:----------------|--------:|
| Public               | B1              |   2,874 |
| Public               | B2              |   2,176 |
| Public               | B3              |   2,016 |
| Public               | B4              |   2,209 |
| Public               | B5              |   2,288 |
| Public               | B6              |   2,385 |
| Public               | B7              |   2,442 |
| Public               | B8              |   2,586 |
| Public               | B9              |   3,029 |
| Public               | B10             |   4,854 |
| Private              | B1              |  12,248 |
| Private              | B2              |   9,857 |
| Private              | B3              |   9,151 |
| Private              | B4              |  10,082 |
| Private              | B5              |  10,058 |
| Private              | B6              |  10,104 |
| Private              | B7              |   9,622 |
| Private              | B8              |   9,833 |
| Private              | B9              |   9,876 |
| Private              | B10             |  10,784 |
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

---


## Table 19 -- Course Group to Bin Flow

<!-- chart_type: sankey | x: UNDERGRAD_COURSE_GROUP | y: PercentileBin | series: fig_t6_sankey_course
     population: source->target->value
     n: best-record trend cohort | denominator: 131,845
     source_tab: best-record examinees | element_id: 6 -->

| UNDERGRAD_COURSE_GROUP       | PercentileBin   |   count |
|:-----------------------------|:----------------|--------:|
| Medical & Allied             | B1              |   6,348 |
| Medical & Allied             | B2              |   6,179 |
| Medical & Allied             | B3              |   5,988 |
| Medical & Allied             | B4              |   6,771 |
| Medical & Allied             | B5              |   6,865 |
| Medical & Allied             | B6              |   6,765 |
| Medical & Allied             | B7              |   6,198 |
| Medical & Allied             | B8              |   6,213 |
| Medical & Allied             | B9              |   5,960 |
| Medical & Allied             | B10             |   6,181 |
| Natural Sciences             | B1              |   4,942 |
| Natural Sciences             | B2              |   3,425 |
| Natural Sciences             | B3              |   3,029 |
| Natural Sciences             | B4              |   3,351 |
| Natural Sciences             | B5              |   3,358 |
| Natural Sciences             | B6              |   3,535 |
| Natural Sciences             | B7              |   3,796 |
| Natural Sciences             | B8              |   4,011 |
| Natural Sciences             | B9              |   4,439 |
| Natural Sciences             | B10             |   6,310 |
| Social & Behavioral Sciences | B1              |   3,137 |
| Social & Behavioral Sciences | B2              |   1,736 |
| Social & Behavioral Sciences | B3              |   1,359 |
| Social & Behavioral Sciences | B4              |   1,320 |
| Social & Behavioral Sciences | B5              |   1,233 |
| Social & Behavioral Sciences | B6              |   1,307 |
| Social & Behavioral Sciences | B7              |   1,181 |
| Social & Behavioral Sciences | B8              |   1,249 |
| Social & Behavioral Sciences | B9              |   1,406 |
| Social & Behavioral Sciences | B10             |   1,830 |
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
| Other                        | B10             |   1,092 |

---


## Table 20 -- Bin to PLE Status Flow (Observable Cohort)

<!-- chart_type: sankey | x: PercentileBin | y: PLE_STATUS_LABEL | series: fig_t6_sankey_ple
     population: source->target->value
     n: observable cohort | denominator: 68,173
     source_tab: observable best-record examinees | element_id: 6 -->

| PercentileBin   | PLE_STATUS_LABEL       |   count |
|:----------------|:-----------------------|--------:|
| B1              | Confirmed PLE passer   |     740 |
| B1              | No confirmed PLE match |   6,113 |
| B2              | Confirmed PLE passer   |   1,219 |
| B2              | No confirmed PLE match |   4,665 |
| B3              | Confirmed PLE passer   |   1,551 |
| B3              | No confirmed PLE match |   4,262 |
| B4              | Confirmed PLE passer   |   2,155 |
| B4              | No confirmed PLE match |   4,318 |
| B5              | Confirmed PLE passer   |   2,852 |
| B5              | No confirmed PLE match |   3,730 |
| B6              | Confirmed PLE passer   |   2,976 |
| B6              | No confirmed PLE match |   3,308 |
| B7              | Confirmed PLE passer   |   3,214 |
| B7              | No confirmed PLE match |   3,145 |
| B8              | Confirmed PLE passer   |   3,534 |
| B8              | No confirmed PLE match |   3,170 |
| B9              | Confirmed PLE passer   |   4,323 |
| B9              | No confirmed PLE match |   2,940 |
| B10             | Confirmed PLE passer   |   6,946 |
| B10             | No confirmed PLE match |   3,012 |

### PLE Status Composition within Each Bin (%)

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

---


## Tables 21-22 -- Largest Pathways into B8-B10

| UNDERGRAD_UNI_TYPE   | PercentileBin   |   Count |
|:---------------------|:----------------|--------:|
| Private              | B10             |  10,784 |
| Private              | B9              |   9,876 |
| Private              | B8              |   9,833 |
| Public               | B10             |   4,854 |
| Public               | B9              |   3,029 |
| Public               | B8              |   2,586 |
| Foreign              | B10             |     266 |
| Foreign              | B9              |     197 |
| Foreign              | B8              |     175 |
| UNDERGRAD_COURSE_GROUP       | PercentileBin   |   Count |
|:-----------------------------|:----------------|--------:|
| Natural Sciences             | B10             |   6,310 |
| Medical & Allied             | B8              |   6,213 |
| Medical & Allied             | B10             |   6,181 |
| Medical & Allied             | B9              |   5,960 |
| Natural Sciences             | B9              |   4,439 |
| Natural Sciences             | B8              |   4,011 |
| Social & Behavioral Sciences | B10             |   1,830 |
| Social & Behavioral Sciences | B9              |   1,406 |
| Social & Behavioral Sciences | B8              |   1,249 |
| Other                        | B10             |   1,092 |

---


# Tab 7 -- PLE Alignment


## Table 23 -- Score Profile by PLE Status

| PLE_STATUS_LABEL       |   TotalRawScoreTRUE / count |   TotalRawScoreTRUE / median |   TotalRawScoreTRUE / mean |   TotalRawScoreTRUE / q25 |   TotalRawScoreTRUE / q75 |   PartIRawScoreTRUE / count |   PartIRawScoreTRUE / median |   PartIRawScoreTRUE / mean |   PartIRawScoreTRUE / q25 |   PartIRawScoreTRUE / q75 |   PartIIRawScoreTRUE / count |   PartIIRawScoreTRUE / median |   PartIIRawScoreTRUE / mean |   PartIIRawScoreTRUE / q25 |   PartIIRawScoreTRUE / q75 |   NMS_PER_num / count |   NMS_PER_num / median |   NMS_PER_num / mean |   NMS_PER_num / q25 |   NMS_PER_num / q75 |   NMS_GPS / count |   NMS_GPS / median |   NMS_GPS / mean |   NMS_GPS / q25 |   NMS_GPS / q75 |   NMS_APT / count |   NMS_APT / median |   NMS_APT / mean |   NMS_APT / q25 |   NMS_APT / q75 |   NMS_SA / count |   NMS_SA / median |   NMS_SA / mean |   NMS_SA / q25 |   NMS_SA / q75 |
|:-----------------------|----------------------------:|-----------------------------:|---------------------------:|--------------------------:|--------------------------:|----------------------------:|-----------------------------:|---------------------------:|--------------------------:|--------------------------:|-----------------------------:|------------------------------:|----------------------------:|---------------------------:|---------------------------:|----------------------:|-----------------------:|---------------------:|--------------------:|--------------------:|------------------:|-------------------:|-----------------:|----------------:|----------------:|------------------:|-------------------:|-----------------:|----------------:|----------------:|-----------------:|------------------:|----------------:|---------------:|---------------:|
| Confirmed PLE passer   |                      30,104 |                          140 |                     141.37 |                       120 |                       163 |                      30,104 |                           74 |                      74.11 |                        64 |                        85 |                       30,104 |                            66 |                       67.27 |                         55 |                         79 |                29,510 |                     70 |                65.16 |                  46 |                  89 |            30,105 |                553 |            558.1 |             490 |             626 |            30,105 |                549 |           554.47 |             492 |             615 |           30,105 |               546 |          547.73 |            484 |            611 |
| No confirmed PLE match |                      39,356 |                          115 |                     116.87 |                        95 |                       137 |                      39,356 |                           62 |                      62.14 |                        51 |                        73 |                       39,356 |                            53 |                       54.73 |                         42 |                         65 |                38,663 |                     39 |                 43.1 |                  17 |                  68 |            39,398 |                473 |           473.08 |             402 |             545 |            39,398 |                484 |           481.17 |             415 |             546 |           39,398 |               471 |          475.57 |            409 |            540 |

---


## Box Summary: TRUE Raw Score by PLE Status

<!-- chart_type: box | x: PLE_STATUS_LABEL | y: TotalRawScoreTRUE | series: none
     population: observable cohort
     n: 69,503 | denominator: observable best-record examinees
     source_tab: 7 | element_id: fig_t7_box_raw_ple -->

| PLE_STATUS_LABEL       |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|:-----------------------|-------:|------:|-----:|---------:|-----:|------:|-----------:|
| Confirmed PLE passer   | 30,104 |    48 |  120 |      140 |  163 |   231 |          3 |
| No confirmed PLE match | 39,356 |     9 |   95 |      115 |  137 |   223 |        185 |

---


## Table 24 -- Mann-Whitney: Confirmed vs No Match

| Score              |      U_stat | p_value   |   effect_r |   Confirmed_median |   NoMatch_median |
|:-------------------|------------:|:----------|-----------:|-------------------:|-----------------:|
| Total Raw Score    | 8.50769e+08 | <0.001    |      -0.44 |                140 |              115 |
| Part I             | 8.34193e+08 | <0.001    |      -0.41 |                 74 |               62 |
| Part II            | 8.34468e+08 | <0.001    |      -0.41 |                 66 |               53 |
| Percentile Rank    | 8.12563e+08 | <0.001    |      -0.42 |                 70 |               39 |
| GPS Standard Score | 8.52438e+08 | <0.001    |      -0.44 |                553 |              473 |

---


## Figure 21 -- Bin Distribution by PLE Status

<!-- chart_type: stacked_bar | x: PLE_STATUS_LABEL | y: PercentileBin | series: fig_t7_bin_ple
     population: row %
     n: observable cohort | denominator: 69,503
     source_tab: observable best-record examinees | element_id: 7 -->

| PLE_STATUS_LABEL       |    B1 |    B2 |    B3 |    B4 |   B5 |    B6 |    B7 |    B8 |    B9 |   B10 |
|:-----------------------|------:|------:|------:|------:|-----:|------:|------:|------:|------:|------:|
| Confirmed PLE passer   |  2.51 |  4.13 |  5.26 |   7.3 | 9.66 | 10.08 | 10.89 | 11.98 | 14.65 | 23.54 |
| No confirmed PLE match | 15.81 | 12.07 | 11.02 | 11.17 | 9.65 |  8.56 |  8.13 |   8.2 |   7.6 |  7.79 |

---


## Table 25 -- PLE Status Composition within Each Bin

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

---


## Table 26 -- Course-Group Top-Bin Survival

| UNDERGRAD_COURSE_GROUP       |   total_examinees |   top_decile_n |   survival_rate_pct |
|:-----------------------------|------------------:|---------------:|--------------------:|
| Engineering & Technology     |               730 |            383 |               52.47 |
| Natural Sciences             |            40,196 |         14,760 |               36.72 |
| Other                        |             8,248 |          2,910 |               35.28 |
| Education                    |             3,445 |          1,160 |               33.67 |
| Medical & Allied             |            63,468 |         18,354 |               28.92 |
| Social & Behavioral Sciences |            15,758 |          4,485 |               28.46 |

---


## Table 27 -- Confirmed PLE Alignment by University Type

| UNDERGRAD_UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|:---------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|
| Foreign              |                        1159 |                     252 |                      907 |                     21.74 |
| Private              |                       53037 |                   22712 |                    30325 |                     42.82 |
| Public               |                       14263 |                    6757 |                     7506 |                     47.37 |

---


## Tables 28-30 -- Confirmed PLE Alignment by Year / Course / University Type

|   Year |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|-------:|----------------------------:|------------------------:|-------------------------:|--------------------------:|
|  2,006 |                        3698 |                    1973 |                     1725 |                     53.35 |
|  2,007 |                        3690 |                    1784 |                     1906 |                     48.35 |
|  2,008 |                        4965 |                    2438 |                     2527 |                      49.1 |
|  2,009 |                        7461 |                    3054 |                     4407 |                     40.93 |
|  2,010 |                        8623 |                    4070 |                     4553 |                      47.2 |
|  2,011 |                        8842 |                    3889 |                     4953 |                     43.98 |
|  2,012 |                        9405 |                    3979 |                     5426 |                     42.31 |
|  2,013 |                        9867 |                    4188 |                     5679 |                     42.44 |
|  2,014 |                       12952 |                    4730 |                     8222 |                     36.52 |
| UNDERGRAD_COURSE_GROUP       |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Education                    |                        3188 |                    1452 |                     1736 |                     45.55 |                       53 |
| Medical & Allied             |                       38144 |                   17240 |                    20904 |                      45.2 |                       49 |
| Other                        |                        6612 |                    2756 |                     3856 |                     41.68 |                       55 |
| Natural Sciences             |                       16512 |                    6849 |                     9663 |                     41.48 |                       64 |
| Engineering & Technology     |                         318 |                     116 |                      202 |                     36.48 |                       71 |
| Social & Behavioral Sciences |                        4729 |                    1692 |                     3037 |                     35.78 |                       63 |
| UNDERGRAD_UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:---------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Foreign              |                        1159 |                     252 |                      907 |                     21.74 |                       57 |
| Private              |                       53037 |                   22712 |                    30325 |                     42.82 |                       50 |
| Public               |                       14263 |                    6757 |                     7506 |                     47.37 |                       68 |

---


# Tab 8 -- Repeat Takers


## Table 31 -- Attempt-Count Distribution

<!-- chart_type: bar | x: Attempts | y: Count | series: none
     population: all sittings, 2006-2018
     n: 178,927 | denominator: all NMAT sittings in the trend window
     source_tab: 8 | element_id: fig_t8_attempts -->

|   Attempts |   Count |   Percent |
|-----------:|--------:|----------:|
|          1 | 101,156 |        75 |
|          2 |  25,812 |     19.14 |
|          3 |   6,046 |      4.48 |
|          4 |   1,411 |      1.05 |
|          5 |     332 |      0.25 |
|          6 |      88 |      0.07 |
|          7 |      17 |      0.01 |
|          8 |       6 |         0 |
|          9 |       1 |         0 |

---


## Table 32 -- Repeat-Taker Trajectory Summary

| Metric | Value | Population | Note |
|---|---|---|---|
| Repeat-taker persons | 33,713 | unique PERSON_KEY, >1 attempt | - |
| Analytic repeat takers | 33,620 | with complete first/last scores | - |
| Improved percentile rank | 76.43% | analytic repeat takers | - |
| Improved raw score | 73.66% | analytic repeat takers | - |
| Median percentile change | 11.00 | analytic repeat takers | - |
| Median raw score change | 12.00 | analytic repeat takers | - |

## Box Summary: First-to-Last Attempt Change

<!-- chart_type: box | x: Measure | y: Change | series: none
     population: analytic repeat takers
     n: 33,620 | denominator: repeat takers with complete first/last scores
     source_tab: 8 | element_id: fig_t8_box_change -->

| Measure           |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|:------------------|-------:|------:|-----:|---------:|-----:|------:|-----------:|
| Percentile change | 33,620 |   -71 |    1 |       11 |   25 |    94 |        305 |
| Raw score change  | 33,620 |   -84 |    0 |       12 |   26 |   119 |        313 |

---


## First vs Last Percentile (Repeat Takers, Preview)

<!-- chart_type: scatter | x: first_pct | y: last_pct | series: none
     population: analytic repeat takers
     n: 33,620 | denominator: repeat takers with complete first/last scores
     source_tab: 8 | element_id: fig_t8_scatter_repeat -->

| PERSON_KEY                                              |   first_pct |   last_pct |   n_attempts |
|:--------------------------------------------------------|------------:|-----------:|-------------:|
| ASUNCION, JESLY ANNE BULUSAN||8/10/1992                 |           6 |         11 |            9 |
| GONZAGA, CATHERINE KAYE SALVACION||01/29/1993           |          11 |         25 |            8 |
| LLANES, RUDOLPH RICAMARA||5/12/1988                     |           5 |         40 |            8 |
| LAMBON, EMMANUEL YENUBE||04/27/1987                     |           5 |         67 |            8 |
| H ISMAEL, DONORAIN EDRES||2/6/1989                      |          24 |          3 |            8 |
| PASCUAL, KENNETH TRISTAN NAZARENO||05/13/1990           |           6 |         40 |            8 |
| QUIMING, LYAN DJAMILLE BUSTAMANTE||11/11/1992           |          32 |         56 |            8 |
| CAPOQUIAN, WILMARY PAJARES||12/2/1993                   |           9 |         38 |            7 |
| COLLANTES, ANTHONY AVENA||11/9/1993                     |          49 |         80 |            7 |
| EVANGELIO, JEAN MARIE AGUILA||1/8/1991                  |           4 |         30 |            7 |
| AGABIN, AIZA ANGOLLUAN||12/9/1988                       |          19 |         41 |            7 |
| ERNI, HANZEL CHARZON ALEGRE||06/15/1987                 |          10 |         60 |            7 |
| CAJANDIG, PRINCESS MAY TEE||3/5/1992                    |           1 |          3 |            7 |
| MACALANGCOM, JAWAHER SALI||03/15/1989                   |           1 |          2 |            7 |
| DIZON, GINA PAULA DENSING||3/6/1991                     |          19 |         63 |            7 |
| CAVAN, LUCKY ANGELO BARUIS||8/6/1993                    |           2 |         28 |            7 |
| MONJE, REEMA LI VALDEZ||06/24/1994                      |           5 |         33 |            7 |
| MUKSAN, RAYHAN JAINA ABAM||9/2/1991                     |          15 |         25 |            7 |
| NARVASA, JAMES JR ROSALES||03/14/1989                   |           1 |          2 |            7 |
| PEREZ, APRIL HAMILI GRACE CAYDE||04/24/1987             |          18 |         37 |            7 |
| QUILLOPE, AIMIE KLAIN MAGAS||12/9/1991                  |           6 |         20 |            7 |
| SAMPULNA, JIM II DURUIN||7/6/1989                       |           8 |         33 |            7 |
| TURGANO, LOIS KATHLEEN MARY JAVILLONAR||05/18/1985      |           2 |         49 |            7 |
| VELOSO, JOSE CARLOS GLIANE||09/13/1990                  |           9 |         26 |            7 |
| LORESCA, ROSE LEEN CRISANTO||9/3/1992                   |           3 |         15 |            6 |
| ACUNA, JANELLA MARA VILLANUEVA||02/16/1994              |           3 |         45 |            6 |
| BANZON, ANA KRISTIANA LOUISE AUSTRIA||11/14/1993        |          15 |         68 |            6 |
| DALMAN, JENDEE DEMORITO||8/7/1992                       |           2 |         28 |            6 |
| BANDARI, LAXMI PRASANNA||06/19/1996                     |          12 |         27 |            6 |
| DEMAFILES, DEAN ROBERT ANCHETA||06/29/1988              |           7 |         33 |            6 |
| AGOR, ELIS MARIE MALLANAO||8/10/1994                    |           6 |          8 |            6 |
| LOGO, JOHN CYRUS PEREZ||02/20/1992                      |          25 |         62 |            6 |
| CLERIGO, APRILLE VANESSA ROA||12/4/1994                 |           8 |         59 |            6 |
| ASUAKO, FRANCIS||10/6/1987                              |          12 |         59 |            6 |
| ANDREWS, DOLL SUZANNE||1/12/1996                        |           3 |         57 |            6 |
| KUMAR, ARUN||09/21/1995                                 |           9 |         15 |            6 |
| CABALLERO, NIKKOLE NICOLAS||4/7/1993                    |          16 |         12 |            6 |
| CHAUDHARY, ANIL JESUNGBHAI||08/26/1994                  |           4 |         83 |            6 |
| BAGTILAY, APRIL DIANN JUAN||7/4/1992                    |          29 |         45 |            6 |
| AGOJO, ERYLL JOY HOLGADO||1/10/1993                     |           5 |         57 |            6 |
| ISIDRO, IAN QUILON||04/27/1990                          |          16 |         15 |            6 |
| GARCIA, KEITH CACHO||9/11/1984                          |          14 |         18 |            6 |
| BARRIOS, KEVIN GEORGE BEARE||04/27/1991                 |          72 |         88 |            6 |
| CUDAL, RIO CLAIRE IYADAN||03/31/1996                    |           6 |         48 |            6 |
| CATEDRAL, GLENNA HOPE JOYCE TUAZON||10/12/1989          |           9 |         15 |            6 |
| LAWRENCE, NICKSON||06/17/1997                           |          10 |          5 |            6 |
| ADEWALE, FISAYO FOLASADE||08/15/1989                    |           6 |         26 |            6 |
| CONCEPCION, MA CARMELA MENDOZA||01/22/1991              |           3 |          4 |            6 |
| CONDE, MA THELMA PRECY CONSULTA||11/25/1993             |          18 |         60 |            6 |
| HABILING, KAVIN BIDANG||05/18/1992                      |          14 |         92 |            6 |
| ANANDAN, MUGUNTHAN||03/21/1997                          |           3 |         39 |            6 |
| GUEVARRA, MARIE THERESE TAEZA||09/21/1993               |          39 |         43 |            6 |
| BARIA, TARUNKUMAR GULABSINH||06/28/1996                 |           6 |         28 |            6 |
| CASIN, DENISE ARIELLE ACERO||1/8/1992                   |           9 |         55 |            6 |
| DILLA, PERCIVAL CALIXTO||6/6/1990                       |          10 |         13 |            6 |
| GONZALES, CHRYZEL ANGELICA BABAAN||09/22/1990           |          31 |         46 |            6 |
| DE GUZMAN, NINA GAE CAMAGAY||02/26/1995                 |           2 |          6 |            6 |
| DAYANDAYAN, DARWIN ADRIAN UMALI||01/25/1992             |          24 |         36 |            6 |
| CARANGUIAN, MARIFE DURAN||12/2/1992                     |           5 |         47 |            6 |
| LIM, KATRINA ROSE LAO||2/6/1990                         |          12 |         35 |            6 |
| GILERA, HANNA PATRICIA VALLEJA||12/2/1995               |          16 |         37 |            6 |
| BHOJAK, NIDHIBEN VIKRAMBHAI||03/29/1997                 |          17 |         48 |            6 |
| FIGUEROA, RALPH BERNARD MOJICA||9/9/1992                |           2 |         13 |            6 |
| ALDEA, ALDA LOU MATEUM||5/1/1992                        |           6 |         22 |            6 |
| HIPOLITO, JAYVY RAMOS||7/4/1992                         |           3 |         16 |            6 |
| CASTRO, JEANINE||10/16/1974                             |           6 |         24 |            6 |
| GONZALES, MAJESTY DELA CRUZ||12/1/1996                  |           2 |         11 |            6 |
| CAMPOS, CRISTINE SEDANO||1/4/1988                       |           8 |         33 |            6 |
| BAUTISTA, KAYE DOLFO||4/8/1992                          |           9 |         29 |            6 |
| DOMINGO, PAMELA CASTANO||01/20/1993                     |          14 |         32 |            6 |
| MADRIAGA, KATRIN VELASCO||06/30/1990                    |          11 |         34 |            6 |
| MAHARJAN, SUNILA||02/16/1995                            |          13 |          3 |            6 |
| MALLILLIN, KARLA MAY CANTOR||05/22/1990                 |          21 |         41 |            6 |
| DAOWAG, FAITH ASWIGUE||10/19/1991                       |           7 |         44 |            6 |
| MORALES, JANINE CARLA MANZANERO||6/12/1990              |           5 |         28 |            6 |
| LACANDULA, GISELLE ALFORQUE||5/4/1988                   |          43 |         30 |            6 |
| NANDAKUMAR NAIR, SREEKUMAR||1/6/1996                    |          21 |          4 |            6 |
| ENTERO, ALLANA GHISEL BAUTISTA||09/27/1995              |          13 |         51 |            6 |
| NUNES, XERYL ANN DIMACULANGAN||3/5/1991                 |          34 |         57 |            6 |
| PANGAN, DESIREE CLEMENTE||12/9/1987                     |          23 |         40 |            6 |
| PASAO, CATHERINE PALIZA||3/11/1992                      |           5 |         54 |            6 |
| GEORGE SELVAMARY, SAGAYA HELAN MARY||1/11/1996          |           1 |         11 |            6 |
| PASUPATHY, DIVYA||5/1/1997                              |           4 |         11 |            6 |
| PATEL, PUJAN MUKESHKUMAR||1/1/1997                      |          86 |         16 |            6 |
| GUTIERREZ, PAOLO GABRIEL FERRER||05/17/1995             |          30 |         52 |            6 |
| PROFETANA, ERLA RHYN VEGA||03/28/1992                   |          13 |         34 |            6 |
| GOTICO, AARON SAMUEL TIBAYAN||09/26/1994                |          32 |         59 |            6 |
| DONADILLA, ROSELLINE ZAPATA||09/19/1993                 |           3 |         46 |            6 |
| RABARI, AMIT MANABHAI||1/3/1997                         |           9 |         13 |            6 |
| RAGUVEL, MANIBHARATHI||10/15/1996                       |          14 |         24 |            6 |
| REYES, JAIRUS REYES||5/7/1991                           |          49 |         80 |            6 |
| RIVERA, KEZIA EARL DIGNOS||04/24/1986                   |           4 |         36 |            6 |
| ROMANCAP, JAMELA KASID||10/5/1990                       |           2 |          1 |            6 |
| SAADRA, RAEFAH YUSOPH||09/28/1994                       |           8 |         24 |            6 |
| SALIK, FAYDHAL AMPATUAN||07/30/1990                     |          16 |         28 |            6 |
| CANGAS, MARI LEN BATALLA||11/20/1993                    |           1 |         26 |            6 |
| SANCHEZ, KATRINA MANGAOANG||7/7/1992                    |           2 |         18 |            6 |
| SANCHEZ, MA KRISTINE JOY KALAW||12/26/1993              |           1 |          4 |            6 |
| SEMBRANO, GABRIELYNE DELA CRUZ||07/29/1992              |          12 |         25 |            6 |
| SUBRAMANIAN, KUMARAVEL||7/11/1997                       |           8 |         32 |            6 |
| SUBU, UMAMAHESWARI||05/30/1996                          |           6 |         55 |            6 |
| THAKOR, DHAVAL RAKESHKUMAR||09/22/1996                  |          16 |         21 |            6 |
| GAERLAN, LOURD DERICK JURADO||02/24/1991                |          15 |         46 |            6 |
| TUTING, JULIE ANN DENIEGA||4/7/1988                     |           8 |          9 |            6 |
| VALDERRAMA, BEA AIRA BALMACEDA||10/10/1992              |           4 |         11 |            6 |
| VAZA, JIGNASA VAJUBHAI||07/31/1996                      |          23 |         17 |            6 |
| GALLARDO, JOSHUA PENAREDONDA||11/29/1990                |          16 |          9 |            6 |
| VERZOSA, JEROME TURINGAN||04/30/1990                    |          14 |         47 |            6 |
| VIDAL, JEANNETTE ANNE NAVARRO||07/27/1995               |           6 |         34 |            6 |
| VILLENA, MICHAEL BERNARD SALUD||11/2/1995               |           2 |         85 |            6 |
| WAL, MICHAEL JUDE CASTANEDA||05/29/1993                 |           8 |         64 |            6 |
| WATANABE, MAKOTO||10/18/1979                            |           1 |         24 |            6 |
| CORDERO, ANI HOSANNA ODONZO||11/14/1993                 |           2 |         30 |            5 |
| ATIENZA, EMILIANNE WEE ENG||04/22/1995                  |          87 |         82 |            5 |
| ESGUERRA, NADYNNE MARIE RAAGAS||09/14/1992              |          20 |         45 |            5 |
| LANGEBAN, MARREM JANELLE ANGELES||01/20/1994            |           2 |         20 |            5 |
| DEL PRADO, ROSE MYSTICA FERNANDEZ||11/9/1992            |           6 |         63 |            5 |
| BERMEJO, JARETTE LORENZO||08/27/1985                    |          20 |         27 |            5 |
| ANDRES, KHRISTINE MAE NAPOLES||6/5/1989                 |          11 |         29 |            5 |
| FRANCISCO, PRECIOUS EVE BETITA||08/28/1994              |           4 |         25 |            5 |
| BERMOY, FRANCIS CARLO ALMARIO||10/12/1994               |          20 |         67 |            5 |
| DE ASIS, JILBERT DARONG||11/27/1991                     |          17 |         40 |            5 |
| DAO AYAN, KIAREI BAGGAS||04/15/1994                     |           6 |         34 |            5 |
| LADUMOR, VIJAY LAKHABHAI||12/30/1996                    |           9 |          4 |            5 |
| BUMANGLAG, KATRINA MARIE DIAZ||06/15/1994               |           4 |         31 |            5 |
| KARIYAPATTINAM NEELAMEGAM, BARANI||05/31/1997           |           9 |         21 |            5 |
| DEBUTON, AIRON GANTALA||08/26/1994                      |          11 |         16 |            5 |
| BAYAOA, KAREN FAYE GARCIA||10/21/1991                   |          11 |         48 |            5 |
| ENGINEER, PARTH BABUBHAI||09/23/1997                    |           1 |         31 |            5 |
| BENDITA, JESSELINE MARIE GUAY||03/16/1995               |           6 |         14 |            5 |
| ALAS, KARLA PATRICIA CIRERA||02/25/1992                 |          20 |         31 |            5 |
| COCJIN, JEHU MILES SUPERIO||08/26/1995                  |          21 |          9 |            5 |
| ISRAEL, LEONIDES RAMONETTE CANAPI||12/27/1991           |          14 |         43 |            5 |
| DAYAG, CORY SIBBALUCA||1/3/1986                         |           2 |         41 |            5 |
| ACLAN, NOELIE JOY MOSQUITO||10/10/1992                  |           1 |         37 |            5 |
| GAUDIANO, JOSELLE LORRAINE ALMEDA||1/5/1993             |          11 |         43 |            5 |
| ALVAREZ, VINCENT PAUL STA TERESA||08/23/1991            |           7 |         12 |            5 |
| FIRMALINO, ANGELLENE DIESTO||10/10/1994                 |          26 |         61 |            5 |
| GERONIMO, MONA LEIGH LEVISTE||03/24/1992                |          27 |         99 |            5 |
| KHATRI, ALI ASGAR||3/6/1995                             |           1 |          3 |            5 |
| CASIPIT, CARLO GABRIEL CANONIGO||10/22/1995             |          57 |         98 |            5 |
| BUENSALIDA, ANGELA CASTILLO||02/26/1995                 |          48 |         86 |            5 |
| JADEJA, SATYAJITSINH ASHOKSINH||08/19/1997              |          10 |         15 |            5 |
| FACTOR, MANUELITO LIBO ON||12/6/1991                    |           4 |         41 |            5 |
| ANTONIO, ROBIN VALDEZ||09/18/1992                       |          21 |         62 |            5 |
| KUMAR, ROHIT||10/8/1996                                 |           2 |          9 |            5 |
| HADJA, MARLINA JADJULI||12/18/1992                      |           3 |         40 |            5 |
| ALVENIZ, SHENNA MAE VILLEGAS||1/8/1994                  |           1 |          2 |            5 |
| KORRA, RAJARAM||07/27/1998                              |           6 |          6 |            5 |
| CHEKURU, VAISHNAVI||08/28/1998                          |           1 |          9 |            5 |
| KORRA, VIVEKRAM||04/14/1996                             |          15 |         37 |            5 |
| GALEON, EDELAINE MARIE JABANES||3/10/1994               |          15 |         37 |            5 |
| CHIJIOKA, ONYEMAECHI||10/23/1987                        |          13 |          9 |            5 |
| BANIQUED, NAPHTALI ROSALES||05/25/1987                  |          15 |         46 |            5 |
| JAMILI, JAMES WILLIAM TEROL||07/15/1994                 |           3 |         51 |            5 |
| BAUTISTA, CRYSLER ALCANTARA||6/11/1987                  |           1 |          4 |            5 |
| CHAUDHARY, MANISH||12/11/1998                           |           5 |         40 |            5 |
| BADUA, KHRISTAN JAY FIESTA||10/26/1991                  |           9 |         24 |            5 |
| ALMIREZ, NIKKI CIARA SEVERINO||08/22/1995               |          26 |         52 |            5 |
| BALBIN, MANRIC LASAGA||1/3/1992                         |           1 |         19 |            5 |
| LACERNA, JOHN CHRISTOPHER LUCENA||11/17/1994            |          46 |         69 |            5 |
| FADEROG, JOAN CAMPILLOS||11/4/1991                      |           9 |          8 |            5 |
| KORADIYA, RAVIKUMAR BALABHAI||7/9/1997                  |           4 |         15 |            5 |
| KUMAR, GOPAL||12/15/1997                                |           6 |         17 |            5 |
| DAVE, MILAN DEVENDRAKUMAR||05/15/1997                   |          32 |          6 |            5 |
| DELA ROSA, MA KAREN JOY FONTECHA||09/21/1994            |           1 |         24 |            5 |
| ELEAZAR, GENICA SUMAMPONG||10/11/1994                   |          12 |         25 |            5 |
| GAMEZ, JOHN PAUL TRANK ILAGAN||11/8/1995                |          14 |         65 |            5 |
| CAMPOS, KIM JUSTINE ROSALI||08/13/1993                  |           4 |         17 |            5 |
| DOCENA, RUTCHEL RISOS||9/3/1992                         |          16 |         73 |            5 |
| ABDULLAH, BAI MICHELLE KABUNTALAN||06/25/1993           |           2 |         16 |            5 |
| ARAGA, AKHIL RAGHAVENDRA REDDY||08/29/1996              |           2 |          9 |            5 |
| BHATT, HARSH ATULKUMAR||11/20/1997                      |          21 |         19 |            5 |
| BALLUNGAY, JOHN HARLEY CUNTAPAY||12/3/1990              |          18 |         17 |            5 |
| CORREA, SUZETTE ANGELICA LOZADA||05/14/1993             |          10 |         34 |            5 |
| HEBRON, REYNOLD DOMINGO||12/3/1992                      |          13 |         51 |            5 |
| CHAUDHARY, VELABHAI BHALABHAI||09/19/1998               |           3 |          5 |            5 |
| ATING, ALMERAH BANSAO||8/1/1993                         |           9 |         38 |            5 |
| ASENCIO, CHARISSA MAEH PASCUA||08/19/1989               |          26 |         49 |            5 |
| LACAMBRA, CRISA PERALTA||01/17/1988                     |          15 |         37 |            5 |
| LAMENTA, MAYGELIN ALINCHAWANG||3/5/1991                 |          30 |         54 |            5 |
| BAMBHAROLIYA, VIVEK BIPINBHAI||10/24/1994               |           6 |         86 |            5 |
| CHENG SY , MARIA PAULINA ORANTE||11/7/1994              |           7 |         63 |            5 |
| FERNANDO, MARIA KATHERINE CHARMAINE CALLADA||11/30/1993 |           7 |         10 |            5 |
| GOZO, CHARISSE LEI MALDOS||01/31/1992                   |          20 |         39 |            5 |
| LAMUNA, ALEANETTE CYRIL HERNANDO||09/20/1990            |          31 |         57 |            5 |
| BOLISAY, MA LOIS EMMANUELLE CAUSING||5/8/1992           |          29 |         37 |            5 |
| AGUILAR, SHARMAINE GUILLERMO||11/19/1992                |           1 |         32 |            5 |
| ANGNEN, GENESIS WAG IYEN||04/15/1994                    |          54 |         70 |            5 |
| ALBURO, HOPE FERIGORA||10/12/1989                       |          64 |         45 |            5 |
| DAKHARA, SAGARBHAI VINUBHAI||8/12/1997                  |          13 |         38 |            5 |
| ABEDIN, HAFEIDAH YUSOPH||1/3/1994                       |          18 |         18 |            5 |
| LALICAN, MARIE FRANCES LABILLES||12/23/1991             |          31 |         66 |            5 |
| CHAUHAN, RAHUL GHANSHYAM||08/19/1996                    |           2 |         44 |            5 |
| CALYA EN, KEREN TINDA AN||5/10/1991                     |          38 |         46 |            5 |
| AGUILERA, EARIC SY||7/7/1995                            |           7 |         85 |            5 |
| ESPADILA, NORDAN JR PANGOLIMA||4/11/1993                |          12 |         14 |            5 |
| GUMARU, JAYCEELYN TANGO||12/25/1988                     |          26 |         79 |            5 |
| ESPIRITU, MARIE CHRISTINE ILAGAN||8/9/1993              |          27 |         42 |            5 |
| KASANI, JYOTHIRMAI||02/17/1996                          |           3 |         32 |            5 |
<!-- truncated: true | shown: 200 | total: 33620 | full_csv: repeat_taker_detail_full.csv (download button in live dashboard, Tab 8) -->


---


## NMA_AppNo Deterministic Match Histories

| Metric | Value | Population | Note |
|---|---|---|---|
| Deterministically matched rows | 3,057 | PLE_MATCH_METHOD in MANUAL_APPNO_MATCH/DETERMINISTIC_APPNO | - |
Full record-level detail is available via CSV download in the live dashboard; not dumped inline here per export contract Rule 3.


---


# Tab 9 -- Subtests & Profiles


## Table 34 -- Standardized Subtest Means by University Type

<!-- chart_type: heatmap | x: subtest | y: UNDERGRAD_UNI_TYPE | series: none
     population: mean standardized score
     n: 133,315 | denominator: best-record uni subset
     source_tab: 9 | element_id: fig_t9_heatmap_uni -->

| UNDERGRAD_UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:---------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Foreign              |   478.75 |      505.58 |         512.25 |       489.33 |     499.4 |     512.8 |    479.1 |      506.07 |
| Private              |   484.71 |      500.28 |         498.85 |       498.89 |    489.54 |    498.05 |   490.46 |       491.3 |
| Public               |   496.15 |      513.66 |         518.08 |       508.27 |    512.35 |    519.55 |   502.96 |      514.78 |

---


## Table 36 -- Standardized Subtest Means by Course Group

<!-- chart_type: heatmap | x: subtest | y: UNDERGRAD_COURSE_GROUP | series: none
     population: mean standardized score
     n: 134,869 | denominator: best-record trend cohort
     source_tab: 9 | element_id: fig_t9_heatmap_course -->

| UNDERGRAD_COURSE_GROUP       |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Education                    |   500.96 |      518.45 |         510.34 |       499.99 |    490.88 |    510.64 |   506.49 |       511.1 |
| Engineering & Technology     |   525.24 |      540.96 |          575.6 |       519.32 |    501.23 |    570.89 |   507.64 |      547.23 |
| Medical & Allied             |   498.46 |       510.9 |          497.6 |       505.36 |    484.13 |    494.33 |   506.32 |       483.7 |
| Natural Sciences             |   476.56 |       499.9 |         512.44 |       503.34 |    520.45 |    516.25 |   470.86 |      518.52 |
| Other                        |   506.04 |      513.34 |         512.03 |       495.29 |    497.67 |    513.47 |   512.96 |      493.01 |
| Social & Behavioral Sciences |   453.52 |      470.05 |         490.79 |       476.44 |    467.09 |    490.76 |   481.38 |      485.91 |

---


## Table 38 -- Radar-Profile Values by University Type

| UNDERGRAD_UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:---------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Foreign              |   478.75 |      505.58 |         512.25 |       489.33 |     499.4 |     512.8 |    479.1 |      506.07 |
| Private              |   484.71 |      500.28 |         498.85 |       498.89 |    489.54 |    498.05 |   490.46 |       491.3 |
| Public               |   496.15 |      513.66 |         518.08 |       508.27 |    512.35 |    519.55 |   502.96 |      514.78 |

---


## Table 39 -- Radar-Profile Values by Course Group

| UNDERGRAD_COURSE_GROUP       |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Education                    |   500.96 |      518.45 |         510.34 |       499.99 |    490.88 |    510.64 |   506.49 |       511.1 |
| Engineering & Technology     |   525.24 |      540.96 |          575.6 |       519.32 |    501.23 |    570.89 |   507.64 |      547.23 |
| Medical & Allied             |   498.46 |       510.9 |          497.6 |       505.36 |    484.13 |    494.33 |   506.32 |       483.7 |
| Natural Sciences             |   476.56 |       499.9 |         512.44 |       503.34 |    520.45 |    516.25 |   470.86 |      518.52 |
| Other                        |   506.04 |      513.34 |         512.03 |       495.29 |    497.67 |    513.47 |   512.96 |      493.01 |
| Social & Behavioral Sciences |   453.52 |      470.05 |         490.79 |       476.44 |    467.09 |    490.76 |   481.38 |      485.91 |

---


# Tab 10 -- Year Gap & Gender


## PLE Year Gap

| Metric | Value | Population | Note |
|---|---|---|---|
| Confirmed passers (with year gap) | 28,097 | observable, confirmed, PLE_YEAR_GAP notna | - |
| Median year gap | 6.0 | rows above | - |
| Q1 year gap | 6.0 | rows above | - |
| Q3 year gap | 7.0 | rows above | - |

## PLE Year-Gap Distribution

<!-- chart_type: histogram | x: PLE_YEAR_GAP | y: Count | series: none
     population: confirmed observable passers with a year gap
     n: 28,097 | denominator: rows above
     source_tab: 10 | element_id: fig_t10_gap_hist -->

|   PLE_YEAR_GAP |   Count |
|---------------:|--------:|
|              1 |       3 |
|              2 |       2 |
|              3 |      24 |
|              4 |      54 |
|              5 |   2,512 |
|              6 |  13,283 |
|              7 |   7,705 |
|              8 |   2,825 |
|              9 |   1,022 |
|             10 |     382 |
|             11 |     164 |
|             12 |      82 |
|             13 |      30 |
|             14 |       5 |
|             15 |       4 |

---


## Box Summary: PLE Year Gap by Course Group

<!-- chart_type: box | x: UNDERGRAD_COURSE_GROUP | y: PLE_YEAR_GAP | series: none
     population: confirmed observable passers with a year gap
     n: 28,097 | denominator: rows above
     source_tab: 10 | element_id: fig_t10_gap_box -->

| UNDERGRAD_COURSE_GROUP       |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|:-----------------------------|-------:|------:|-----:|---------:|-----:|------:|-----------:|
| Education                    |  1,334 |     4 |    6 |        6 |    7 |    15 |         86 |
| Engineering & Technology     |    104 |     5 |    6 |        6 |    7 |    11 |          7 |
| Medical & Allied             | 16,208 |     1 |    6 |        6 |    7 |    14 |        991 |
| Natural Sciences             |  6,379 |     4 |    6 |        6 |    7 |    13 |        378 |
| Other                        |  2,533 |     3 |    6 |        6 |    7 |    15 |        207 |
| Social & Behavioral Sciences |  1,539 |     1 |    6 |        6 |    7 |    14 |        103 |

---


### Table 40 -- Year-Gap Summary by Course Group

| UNDERGRAD_COURSE_GROUP       |   confirmed_passers |   median_year_gap |   q25_year_gap |   q75_year_gap |   median_percentile |
|:-----------------------------|--------------------:|------------------:|---------------:|---------------:|--------------------:|
| Education                    |               1,334 |                 6 |              6 |              7 |                  66 |
| Engineering & Technology     |                 104 |                 6 |              6 |              7 |                  91 |
| Medical & Allied             |              16,208 |                 6 |              6 |              7 |                  63 |
| Natural Sciences             |               6,379 |                 6 |              6 |              7 |                  81 |
| Other                        |               2,533 |                 6 |              6 |              7 |                  70 |
| Social & Behavioral Sciences |               1,539 |                 6 |              6 |              7 |                  84 |

---


## Table 41 -- Score Summary by Sex

| SEX_CLEAN       |      n | median_raw   |   median_pct |   median_gps |
|:----------------|-------:|:-------------|-------------:|-------------:|
| (not specified) |     43 | -            |            0 |          200 |
| Female          | 74,753 | 122.00       |           51 |          502 |
| Male            | 60,073 | 121.00       |           50 |          500 |

---


## Box Summary: Percentile Rank by Sex

<!-- chart_type: box | x: SEX_CLEAN | y: NMS_PER_num | series: none
     population: best-record trend cohort, valid SEX_CLEAN
     n: 134,869 | denominator: sex_base
     source_tab: 10 | element_id: fig_t10_box_sex -->

| SEX_CLEAN       |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|:----------------|-------:|------:|-----:|---------:|-----:|------:|-----------:|
| (not specified) |     39 |     0 |    0 |        0 | 38.5 |    70 |          0 |
| Female          | 73,344 |     1 |   24 |       51 |   76 |    99 |          0 |
| Male            | 58,462 |     1 |   24 |       50 |   77 |    99 |          0 |

---


## Figure 34 -- Sex Composition by Year

<!-- chart_type: stacked_bar | x: Year | y: SEX_CLEAN | series: fig_t10_sex_year
     population: row %
     n: best-record trend cohort, valid SEX_CLEAN | denominator: 134,869
     source_tab: sex_base | element_id: 10 -->

|   Year |   Male |   Female |
|-------:|-------:|---------:|
|  2,006 |  33.69 |    66.31 |
|  2,007 |  37.07 |    62.93 |
|  2,008 |  38.95 |    61.05 |
|  2,009 |  38.16 |    61.84 |
|  2,010 |  52.11 |    47.89 |
|  2,011 |  45.08 |    54.92 |
|  2,012 |  38.78 |    61.22 |
|  2,013 |   37.6 |     62.4 |
|  2,014 |  38.66 |    61.34 |
|  2,015 |  42.15 |    57.85 |
|  2,016 |     42 |       58 |
|  2,017 |  40.02 |    59.98 |
|  2,018 |  63.24 |    36.76 |

---


## Table 42 -- PLE Status Composition by Sex (Observable Cohort)

| SEX_CLEAN       |   Confirmed PLE passer |   No confirmed PLE match |
|:----------------|-----------------------:|-------------------------:|
| (not specified) |                   2.33 |                    97.67 |
| Female          |                   42.8 |                     57.2 |
| Male            |                  44.13 |                    55.87 |

---


# Tab 11 -- Statistical Tests


## Table 43 -- Kruskal-Wallis Tests by Year

| Score              |       H | p_value   |   eta_squared |
|:-------------------|--------:|:----------|--------------:|
| Total raw score    | 6028.28 | <0.001    |          0.04 |
| Part I raw score   | 5766.34 | <0.001    |          0.04 |
| Part II raw score  | 5968.69 | <0.001    |          0.04 |
| Percentile rank    | 2384.82 | <0.001    |          0.02 |
| GPS standard score | 2592.55 | <0.001    |          0.02 |

---


## Table 44 -- Mann-Whitney by PLE Status

| Score              |      U_stat | p_value   |   effect_r |   Confirmed_median |   NoMatch_median |
|:-------------------|------------:|:----------|-----------:|-------------------:|-----------------:|
| Total raw score    | 8.50769e+08 | <0.001    |      -0.44 |                140 |              115 |
| Part I raw score   | 8.34193e+08 | <0.001    |      -0.41 |                 74 |               62 |
| Part II raw score  | 8.34468e+08 | <0.001    |      -0.41 |                 66 |               53 |
| Percentile rank    | 8.12563e+08 | <0.001    |      -0.42 |                 70 |               39 |
| GPS standard score | 8.52438e+08 | <0.001    |      -0.44 |                553 |              473 |

---


## Tables 45-47 -- Chi-Square: University Type x Bin

| UNDERGRAD_UNI_TYPE   |     B1 |    B2 |    B3 |     B4 |     B5 |     B6 |    B7 |    B8 |    B9 |    B10 |
|:---------------------|-------:|------:|------:|-------:|-------:|-------:|------:|------:|------:|-------:|
| Foreign              |    262 |   174 |   140 |    176 |    145 |    164 |   161 |   175 |   197 |    266 |
| Private              | 12,248 | 9,857 | 9,151 | 10,082 | 10,058 | 10,104 | 9,622 | 9,833 | 9,876 | 10,784 |
| Public               |  2,874 | 2,176 | 2,016 |  2,209 |  2,288 |  2,385 | 2,442 | 2,586 | 3,029 |  4,854 |
|    chi2 | p_value   |   degrees_of_freedom |   n_observations |   cramers_v |
|--------:|:----------|---------------------:|-----------------:|------------:|
| 1327.86 | <0.001    |                   18 |          130,334 |        0.07 |
| UNDERGRAD_UNI_TYPE   |      B1 |     B2 |      B3 |      B4 |      B5 |      B6 |      B7 |      B8 |      B9 |     B10 |
|:---------------------|--------:|-------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Foreign              |  219.55 | 174.21 |  161.36 |  177.92 |  178.26 |  180.57 |  174.46 |  179.73 |  186.98 |  226.97 |
| Private              | 11994.1 | 9517.2 | 8815.51 | 9719.91 | 9738.62 | 9864.92 | 9531.23 | 9818.92 |   10215 | 12399.6 |
| Public               | 3170.31 | 2515.6 | 2330.13 | 2569.18 | 2574.12 | 2607.51 | 2519.31 | 2595.35 | 2700.04 | 3277.47 |

---


## University Type x Bin Row Percentages

<!-- chart_type: heatmap | x: PercentileBin | y: UNDERGRAD_UNI_TYPE | series: fig_t11_heatmap_chi
     population: row %
     n: best-record uni subset | denominator: 133,315
     source_tab: chi_base | element_id: 11 -->

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private              | 12.05 |  9.7 | 9.01 | 9.92 |  9.9 | 9.94 | 9.47 | 9.68 |  9.72 | 10.61 |
| Public               |  10.7 |  8.1 | 7.51 | 8.22 | 8.52 | 8.88 | 9.09 | 9.63 | 11.28 | 18.07 |

---


## Table 48 -- Dunn Post-Hoc Adjusted P-Values

|   index |   2006 |   2007 |   2008 |   2009 |   2010 |   2011 |   2012 |   2013 |   2014 |   2015 |   2016 |   2017 |   2018 |
|--------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|    2006 |      1 |      1 |      1 |      1 |      0 |      1 |      1 |      0 |   0.01 |      1 |      0 |      0 |      0 |
|    2007 |      1 |      1 |      1 |      1 |      0 |      1 |      1 |      0 |      0 |      1 |      0 |      0 |      0 |
|    2008 |      1 |      1 |      1 |      1 |      0 |      1 |      1 |      0 |   0.67 |   0.14 |      0 |      0 |      0 |
|    2009 |      1 |      1 |      1 |      1 |      0 |      1 |   0.17 |      0 |      0 |      1 |      0 |      0 |      0 |
|    2010 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |      1 |   0.05 |      0 |      0 |      0 |      0 |
|    2011 |      1 |      1 |      1 |      1 |      0 |      1 |      1 |      0 |      0 |      1 |      0 |      0 |      0 |
|    2012 |      1 |      1 |      1 |   0.17 |      0 |      1 |      1 |      0 |   0.34 |   0.01 |      0 |      0 |      0 |
|    2013 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |      1 |   0.16 |      0 |      0 |      0 |      0 |
|    2014 |   0.01 |      0 |   0.67 |      0 |   0.05 |      0 |   0.34 |   0.16 |      1 |      0 |      0 |      0 |      0 |
|    2015 |      1 |      1 |   0.14 |      1 |      0 |      1 |   0.01 |      0 |      0 |      1 |      0 |      0 |      0 |
|    2016 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|    2017 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      1 |
|    2018 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      1 |

---


# Tab 12 -- Policy Tables & Export


## Table 1 -- Confirmed PLE Alignment by NMAT Year

|   Year |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|-------:|----------------------------:|------------------------:|-------------------------:|--------------------------:|
|  2,006 |                        3698 |                    1973 |                     1725 |                     53.35 |
|  2,007 |                        3690 |                    1784 |                     1906 |                     48.35 |
|  2,008 |                        4965 |                    2438 |                     2527 |                      49.1 |
|  2,009 |                        7461 |                    3054 |                     4407 |                     40.93 |
|  2,010 |                        8623 |                    4070 |                     4553 |                      47.2 |
|  2,011 |                        8842 |                    3889 |                     4953 |                     43.98 |
|  2,012 |                        9405 |                    3979 |                     5426 |                     42.31 |
|  2,013 |                        9867 |                    4188 |                     5679 |                     42.44 |
|  2,014 |                       12952 |                    4730 |                     8222 |                     36.52 |

## Table 2 -- Confirmed PLE Alignment by Pre-Med Background

| UNDERGRAD_COURSE_GROUP       |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Education                    |                        3188 |                    1452 |                     1736 |                     45.55 |                       53 |
| Medical & Allied             |                       38144 |                   17240 |                    20904 |                      45.2 |                       49 |
| Other                        |                        6612 |                    2756 |                     3856 |                     41.68 |                       55 |
| Natural Sciences             |                       16512 |                    6849 |                     9663 |                     41.48 |                       64 |
| Engineering & Technology     |                         318 |                     116 |                      202 |                     36.48 |                       71 |
| Social & Behavioral Sciences |                        4729 |                    1692 |                     3037 |                     35.78 |                       63 |

## Table 3 -- Confirmed PLE Alignment by University Type

| UNDERGRAD_UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:---------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Foreign              |                        1159 |                     252 |                      907 |                     21.74 |                       57 |
| Private              |                       53037 |                   22712 |                    30325 |                     42.82 |                       50 |
| Public               |                       14263 |                    6757 |                     7506 |                     47.37 |                       68 |

## Table 4 -- Survival to Top Bins by Course Group

<!-- chart_type: bar | x: UNDERGRAD_COURSE_GROUP | y: survival_rate_pct | series: none
     population: best-record trend cohort, valid bin
     n: 134,869 | denominator: besttrend
     source_tab: 12 | element_id: fig_t12_survival -->

| UNDERGRAD_COURSE_GROUP       |   total_examinees |   top_decile_n |   survival_rate_pct |
|:-----------------------------|------------------:|---------------:|--------------------:|
| Engineering & Technology     |               730 |            383 |               52.47 |
| Natural Sciences             |            40,196 |         14,760 |               36.72 |
| Other                        |             8,248 |          2,910 |               35.28 |
| Education                    |             3,445 |          1,160 |               33.67 |
| Medical & Allied             |            63,468 |         18,354 |               28.92 |
| Social & Behavioral Sciences |            15,758 |          4,485 |               28.46 |

---


# Tab 13 -- CHED Compliance


## Section A -- Applicant-Pool Cut-off Scenarios (30th vs 40th Percentile)

<!-- chart_type: bar | x: University Type | y: PLE linkage rate (%) | series: none
     population: observable cohort
     n: 69,503 | denominator: observable best-record examinees
     source_tab: 13 | element_id: fig_t13_scenario -->

| University Type   | Cut-off               |   Observable-cohort applicants at/above cut-off |   PLE passers (observable) |   PLE linkage rate (%) |   Median percentile |
|:------------------|:----------------------|------------------------------------------------:|---------------------------:|-----------------------:|--------------------:|
| All               | 30th percentile (B4+) |                                          49,623 |                     26,000 |                   52.4 |                  68 |
| All               | 40th percentile (B5+) |                                          43,150 |                     23,845 |                  55.26 |                  73 |
| Public            | 30th percentile (B4+) |                                          11,097 |                      6,109 |                  55.05 |                  78 |
| Public            | 40th percentile (B5+) |                                          10,093 |                      5,817 |                  57.63 |                  81 |
| Private           | 30th percentile (B4+) |                                          37,053 |                     19,356 |                  52.24 |                  65 |
| Private           | 40th percentile (B5+) |                                          31,759 |                     17,524 |                  55.18 |                  70 |
| Foreign           | 30th percentile (B4+) |                                             806 |                        219 |                  27.17 |                  73 |
| Foreign           | 40th percentile (B5+) |                                             719 |                        206 |                  28.65 |                  77 |

---


## Section B -- Foreign vs Filipino Applicant-Pool Composition

<!-- chart_type: stacked_bar | x: Group | y: PercentileBin | series: fig_t13_citz_stacked
     population: row %
     n: observable uni subset | denominator: 68,459
     source_tab: uniobservable | element_id: 13 -->

| Group     |      n |
|:----------|-------:|
| Filipino  | 63,318 |
| Foreigner |  5,141 |
| Group     |    B1 |    B2 |   B3 |   B4 |   B5 |   B6 |   B7 |    B8 |    B9 |   B10 |
|:----------|------:|------:|-----:|-----:|-----:|-----:|-----:|------:|------:|------:|
| Filipino  |   8.4 |   8.3 |  8.4 | 9.51 | 9.77 | 9.44 | 9.63 | 10.18 | 11.07 |  15.3 |
| Foreigner | 31.02 | 12.49 | 9.74 | 9.46 |  8.1 | 6.69 |  5.7 |  5.45 |  5.45 |  5.91 |

---


## Section C -- Individual-Level PLE Linkage Gradient by Percentile Bin

<!-- chart_type: bar | x: PercentileBin | y: linkage_rate_pct | series: none
     population: observable cohort
     n: 68,173 | denominator: observable best-record examinees with a valid bin
     source_tab: 13 | element_id: fig_t13_gradient -->

| PercentileBin   |     n |   linked_n |   linkage_rate_pct |
|:----------------|------:|-----------:|-------------------:|
| B1              | 6,853 |        740 |               10.8 |
| B2              | 5,884 |      1,219 |              20.72 |
| B3              | 5,813 |      1,551 |              26.68 |
| B4              | 6,473 |      2,155 |              33.29 |
| B5              | 6,582 |      2,852 |              43.33 |
| B6              | 6,284 |      2,976 |              47.36 |
| B7              | 6,359 |      3,214 |              50.54 |
| B8              | 6,704 |      3,534 |              52.71 |
| B9              | 7,263 |      4,323 |              59.52 |
| B10             | 9,958 |      6,946 |              69.75 |
The gradient rises steadily from the lowest to the highest bin, with no sharp step at the 30th (B4) or 40th (B5) percentile threshold. 740 B1 (lowest-decile) examinees in the observable cohort are confirmed PLE passers -- a strictly binding 40th-percentile admission floor would predict this group should barely exist.


---


# Export Integrity

| check | result |
|---|---|
| Source parquet md5 | 72b2808bb8bb9c3594980c5735f814e1 |
| Rows / cols (source parquet on disk) | 178,927 / 53 |
| Derived columns added at load time | 5 (YEAR_INT, SEX_CLEAN, IS_BOARD_OBSERVABLE_COHORT, HAS_CONFIRMED_PLE, PLE_STATUS_LABEL) |
| Tabs exported | 13 / 13 |
| Charts exported as data | 59 / 59 |
| Tables exported | 102 |
| Captions/population notes exported | 23 |
| Dashboard-vs-export value assertions passed | 5 / 5 |