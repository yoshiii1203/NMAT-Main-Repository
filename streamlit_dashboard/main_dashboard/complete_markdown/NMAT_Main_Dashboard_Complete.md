# NMAT Performance Dashboard -- Complete Export

> Complete Markdown export generated 2026-08-14 17:25. Every number below is computed by the same functions the live dashboard renders from (`main_common.py`) -- this document is a faithful transcript, not a paraphrase. **This export always reflects the FULL, UNFILTERED dataset**, not whatever sidebar filters happened to be applied in the browser session that generated it.

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
| PLE linkage rate, observable cohort | 45.44% | observable cohort | linkage, not pass rate |
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
| Median percentile rank | 50.0 | best-record examinees | 0-99 scale |
| Repeat takers | 33,713 (25.0%) | unique examinees, all sittings | - |
| Observable cohort (IS_BEST_OBSERVABLE_RECORD) | 69,503 | best attempt, Year<=2014 | - |
| PLE linkage rate, observable cohort | 45.44% | observable cohort | linkage, not pass rate |

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
|  2,008 |  4,965 |          129 |       107 |       153 |             67 |             61 |           54 |        28 |        80 |          511 |        46 |             51.94 |             47.29 |
|  2,009 |  7,461 |          130 |       109 |       152 |             68 |             62 |           52 |        27 |        77 |          505 |        43 |             52.31 |             47.69 |
|  2,010 |  8,551 |          136 |       115 |       159 |             71 |             65 |           57 |        32 |        81 |          518 |        44 |             52.21 |             47.79 |
|  2,011 |  8,701 |          129 |       109 |       151 |             69 |             60 |           52 |        30 |        76 |          505 |        42 |             53.49 |             46.51 |
|  2,012 |  9,113 |          122 |       101 |       145 |             67 |             54 |           54 |        26 |        81 |          513 |        44 |             54.92 |             44.26 |
|  2,013 |  9,148 |          128 |       103 |       154 |             70 |             57 |           60 |        24 |        86 |          529 |        51 |             54.69 |             44.53 |
|  2,014 | 10,455 |          120 |        98 |       142 |             65 |             55 |           57 |        24 |        83 |          522 |        44 |             54.17 |             45.83 |
|  2,015 | 10,326 |          118 |        93 |       142 |             61 |             57 |           52 |        19 |        78 |          506 |        49 |             51.69 |             48.31 |
|  2,016 | 12,480 |          123 |        98 |       146 |             66 |             57 |           48 |        19 |        73 |          495 |        48 |             53.66 |             46.34 |
|  2,017 | 23,948 |          118 |        93 |       143 |             63 |             54 |           44 |        19 |        70 |          485 |        50 |             53.39 |             45.76 |
|  2,018 | 22,333 |          111 |        91 |       132 |             59 |             51 |           43 |        17 |        70 |          481 |        41 |             53.15 |             45.95 |

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
| Private              | 103,669 |       76.87 |
| Public               |  27,916 |        20.7 |
| Foreign              |   1,892 |         1.4 |
| Not Specified        |   1,392 |        1.03 |

---


## Table 1 -- Executive Summary Indicators

| Indicator                |   Value |
|:-------------------------|--------:|
| Median Total Raw Score   |     122 |
| Median Part I Raw Score  |      65 |
| Median Part II Raw Score |      57 |
| Median Percentile Rank   |      50 |
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
| Confirmed PLE-passer NMAT rows                |      49,086 | All rows (any year) flagged IS_PLE_PASSER == True -- found in the PLE passer source list. This is a linkage flag, not evidence of failure for the rest. |
| Confirmed PLE-passer best-record persons      |      37,365 | Rows above further restricted to IS_BEST_NMAT_RECORD == True (one row per passer).                                                                      |

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
| University pairing conflicts | 0 | universities above | >1 UNDERGRAD_UNI_TYPE or >1 UNDERGRAD_UNI_LOCATION |
*Population: conflicting universities only, 0 of 2,907 checked*

_(no data under the current population)_

---


## Tables 6-8 -- Core Distributions

*Population: all rows, n=178,927*

| UNDERGRAD_UNI_TYPE   |   Count |   Share (%) |
|:---------------------|--------:|------------:|
| Private              | 137,476 |       76.83 |
| Public               |  37,304 |       20.85 |
| Foreign              |   2,315 |        1.29 |
| Not Specified        |   1,832 |        1.02 |
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
| No confirmed PLE match |  48,507 |
| Confirmed PLE passer   |  39,637 |

---


## Table 9 -- PLE Match-Outcome Breakdown

*Population: all rows, n=178,927*

| PLE_MATCH_OUTCOME         |   Count |   Percent |
|:--------------------------|--------:|----------:|
| no_match                  | 121,623 |     67.97 |
| accepted                  |  49,086 |     27.43 |
| rejected_ambiguous_person |   8,216 |      4.59 |
| rejected                  |       2 |         0 |
110 confirmed passers have PLE_YEAR_UNCERTAIN == True.


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
|  2,008 |  4,965 |          129 |       107 |       153 |             67 |             61 |           54 |        28 |        80 |          511 |        46 |             51.94 |             47.29 |
|  2,009 |  7,461 |          130 |       109 |       152 |             68 |             62 |           52 |        27 |        77 |          505 |        43 |             52.31 |             47.69 |
|  2,010 |  8,551 |          136 |       115 |       159 |             71 |             65 |           57 |        32 |        81 |          518 |        44 |             52.21 |             47.79 |
|  2,011 |  8,701 |          129 |       109 |       151 |             69 |             60 |           52 |        30 |        76 |          505 |        42 |             53.49 |             46.51 |
|  2,012 |  9,113 |          122 |       101 |       145 |             67 |             54 |           54 |        26 |        81 |          513 |        44 |             54.92 |             44.26 |
|  2,013 |  9,148 |          128 |       103 |       154 |             70 |             57 |           60 |        24 |        86 |          529 |        51 |             54.69 |             44.53 |
|  2,014 | 10,455 |          120 |        98 |       142 |             65 |             55 |           57 |        24 |        83 |          522 |        44 |             54.17 |             45.83 |
|  2,015 | 10,326 |          118 |        93 |       142 |             61 |             57 |           52 |        19 |        78 |          506 |        49 |             51.69 |             48.31 |
|  2,016 | 12,480 |          123 |        98 |       146 |             66 |             57 |           48 |        19 |        73 |          495 |        48 |             53.66 |             46.34 |
|  2,017 | 23,948 |          118 |        93 |       143 |             63 |             54 |           44 |        19 |        70 |          485 |        50 |             53.39 |             45.76 |
|  2,018 | 22,333 |          111 |        91 |       132 |             59 |             51 |           43 |        17 |        70 |          481 |        41 |             53.15 |             45.95 |

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
|  2,006 |  3,678 |    -1 |   27 |       53 |   77 |    99 |          0 |
|  2,007 |  3,671 |    -1 |   27 |       52 |   77 |    99 |          0 |
|  2,008 |  4,958 |    -1 |   28 |       54 |   80 |    99 |          0 |
|  2,009 |  7,445 |    -1 |   27 |       52 |   77 |    99 |          0 |
|  2,010 |  8,539 |    -1 |   32 |       57 |   81 |    99 |          0 |
|  2,011 |  8,654 |    -1 |   30 |       52 |   76 |    99 |          0 |
|  2,012 |  8,926 |    -1 |   26 |       54 |   81 |    99 |          0 |
|  2,013 |  8,898 |    -1 |   24 |       60 |   86 |    99 |          0 |
|  2,014 | 10,277 |    -1 |   24 |       57 |   83 |    99 |          0 |
|  2,015 | 10,141 |    -1 |   19 |       52 |   78 |    99 |          0 |
|  2,016 | 12,428 |    -1 |   19 |       48 |   73 |    99 |          0 |
|  2,017 | 23,872 |    -1 |   19 |       44 |   70 |    99 |          0 |
|  2,018 | 22,206 |    -1 |   17 |       43 |   70 |    99 |          0 |

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
| Percentile Rank    | 2432.24 | <0.001    |          0.02 |
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

*Population: best-record, Public/Private/Foreign, n=133,477*

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private              | 12.04 | 9.69 |    9 | 9.92 | 9.91 | 9.94 | 9.47 | 9.69 |  9.73 | 10.63 |
| Public               | 10.83 | 8.18 | 7.56 | 8.25 | 8.52 | 8.89 |  9.1 | 9.57 |  11.2 |  17.9 |

---


## Table 11 -- Chi-Square: University Type x Bin

|    chi2 | p_value   |   degrees_of_freedom |   n_observations |   cramers_v |
|--------:|:----------|---------------------:|-----------------:|------------:|
| 1270.33 | <0.001    |                   18 |          130,494 |        0.07 |

---


## Bin Count by Year x University Type

*Population: best-record, Public/Private/Foreign, valid year+bin, n=130,494 sittings across 390 year x unitype x bin cells*

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
|  2,006 | Private              | B1              |   242 |
|  2,006 | Private              | B2              |   258 |
|  2,006 | Private              | B3              |   275 |
|  2,006 | Private              | B4              |   285 |
|  2,006 | Private              | B5              |   279 |
|  2,006 | Private              | B6              |   276 |
|  2,006 | Private              | B7              |   253 |
|  2,006 | Private              | B8              |   264 |
|  2,006 | Private              | B9              |   251 |
|  2,006 | Private              | B10             |   189 |
|  2,006 | Public               | B1              |    55 |
|  2,006 | Public               | B2              |    56 |
|  2,006 | Public               | B3              |    59 |
|  2,006 | Public               | B4              |    60 |
|  2,006 | Public               | B5              |    77 |
|  2,006 | Public               | B6              |    80 |
|  2,006 | Public               | B7              |    95 |
|  2,006 | Public               | B8              |   103 |
|  2,006 | Public               | B9              |   130 |
|  2,006 | Public               | B10             |   250 |
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
|  2,007 | Private              | B1              |   257 |
|  2,007 | Private              | B2              |   259 |
|  2,007 | Private              | B3              |   307 |
|  2,007 | Private              | B4              |   349 |
|  2,007 | Private              | B5              |   290 |
|  2,007 | Private              | B6              |   233 |
|  2,007 | Private              | B7              |   261 |
|  2,007 | Private              | B8              |   285 |
|  2,007 | Private              | B9              |   263 |
|  2,007 | Private              | B10             |   169 |
|  2,007 | Public               | B1              |    56 |
|  2,007 | Public               | B2              |    48 |
|  2,007 | Public               | B3              |    44 |
|  2,007 | Public               | B4              |    46 |
|  2,007 | Public               | B5              |    73 |
|  2,007 | Public               | B6              |    62 |
|  2,007 | Public               | B7              |    94 |
|  2,007 | Public               | B8              |    98 |
|  2,007 | Public               | B9              |   140 |
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
|  2,008 | Private              | B1              |   379 |
|  2,008 | Private              | B2              |   347 |
|  2,008 | Private              | B3              |   334 |
|  2,008 | Private              | B4              |   403 |
|  2,008 | Private              | B5              |   420 |
|  2,008 | Private              | B6              |   419 |
|  2,008 | Private              | B7              |   379 |
|  2,008 | Private              | B8              |   331 |
|  2,008 | Private              | B9              |   369 |
|  2,008 | Private              | B10             |   271 |
|  2,008 | Public               | B1              |    49 |
|  2,008 | Public               | B2              |    60 |
|  2,008 | Public               | B3              |    54 |
|  2,008 | Public               | B4              |    57 |
|  2,008 | Public               | B5              |    65 |
|  2,008 | Public               | B6              |    79 |
|  2,008 | Public               | B7              |   102 |
|  2,008 | Public               | B8              |   116 |
|  2,008 | Public               | B9              |   151 |
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
|  2,009 | Private              | B1              |   450 |
|  2,009 | Private              | B2              |   546 |
|  2,009 | Private              | B3              |   602 |
|  2,009 | Private              | B4              |   664 |
|  2,009 | Private              | B5              |   591 |
|  2,009 | Private              | B6              |   622 |
|  2,009 | Private              | B7              |   575 |
|  2,009 | Private              | B8              |   532 |
|  2,009 | Private              | B9              |   484 |
|  2,009 | Private              | B10             |   382 |
|  2,009 | Public               | B1              |   116 |
|  2,009 | Public               | B2              |    90 |
|  2,009 | Public               | B3              |   108 |
|  2,009 | Public               | B4              |   117 |
|  2,009 | Public               | B5              |   108 |
|  2,009 | Public               | B6              |   160 |
|  2,009 | Public               | B7              |   165 |
|  2,009 | Public               | B8              |   173 |
|  2,009 | Public               | B9              |   233 |
|  2,009 | Public               | B10             |   510 |
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
|  2,010 | Public               | B1              |    85 |
|  2,010 | Public               | B2              |    83 |
|  2,010 | Public               | B3              |    99 |
|  2,010 | Public               | B4              |   102 |
|  2,010 | Public               | B5              |   121 |
|  2,010 | Public               | B6              |   128 |
|  2,010 | Public               | B7              |   165 |
|  2,010 | Public               | B8              |   200 |
|  2,010 | Public               | B9              |   279 |
|  2,010 | Public               | B10             |   669 |
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
|  2,012 | Private              | B1              |   757 |
|  2,012 | Private              | B2              |   608 |
|  2,012 | Private              | B3              |   535 |
|  2,012 | Private              | B4              |   587 |
|  2,012 | Private              | B5              |   667 |
|  2,012 | Private              | B6              |   576 |
|  2,012 | Private              | B7              |   585 |
|  2,012 | Private              | B8              |   645 |
|  2,012 | Private              | B9              |   681 |
|  2,012 | Private              | B10             | 1,141 |
|  2,012 | Public               | B1              |   181 |
|  2,012 | Public               | B2              |   137 |
|  2,012 | Public               | B3              |   137 |
|  2,012 | Public               | B4              |   161 |
|  2,012 | Public               | B5              |   185 |
|  2,012 | Public               | B6              |   145 |
|  2,012 | Public               | B7              |   176 |
|  2,012 | Public               | B8              |   153 |
|  2,012 | Public               | B9              |   191 |
|  2,012 | Public               | B10             |   317 |
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
| Profiled no-PLE-match records | 37,381 | no-PLE-match, observable, uni subset | - |
| Foreigners | 5,049 | rows above | Verified Foreigner |
| Filipinos | 32,320 | rows above | - |
| Distinct citizenship labels | 43 | rows above | - |

### Citizenship Profile KPIs

(Foreigners vs Filipinos pie chart uses the two rows above: Foreigners and Filipinos.)


### Citizenship Counts

*Population: no-PLE-match observable examinees with a citizenship label, n=37,381*

| CITIZENSHIP_FINAL     |      n |
|:----------------------|-------:|
| Filipino              | 32,320 |
| India                 |  2,598 |
| Thailand              |    580 |
| Nepal                 |    418 |
| United States         |    340 |
| Nigeria               |    127 |
| Korea (South)         |    125 |
| Iran                  |    125 |
| Sri Lanka             |    124 |
| Foreign (unspecified) |    107 |
| Malaysia              |     76 |
| Indonesia             |     75 |
| Taiwan                |     65 |
| Somalia               |     38 |
| Canada                |     34 |
| Japan                 |     33 |
| China                 |     32 |
| Pakistan              |     26 |
| Kenya                 |     20 |
| Australia             |     19 |
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
| Sweden                |      2 |
| Austria               |      2 |
| New Zealand           |      2 |
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

### Top-Bin Share (B8-B10) by Citizenship (n>=3)

| CITIZENSHIP_FINAL     |      n |   top_n |   top_dec_pct |
|:----------------------|-------:|--------:|--------------:|
| Bangladesh            |      8 |       0 |             0 |
| Jordan                |      4 |       0 |             0 |
| Somalia               |     38 |       0 |             0 |
| Myanmar               |      8 |       0 |             0 |
| Sudan                 |     14 |       0 |             0 |
| Rwanda                |      3 |       0 |             0 |
| Thailand              |    580 |      39 |           6.7 |
| India                 |  2,598 |     195 |           7.5 |
| Iran                  |    125 |      11 |           8.8 |
| Malaysia              |     76 |       8 |          10.5 |
| Nepal                 |    418 |      61 |          14.6 |
| Pakistan              |     26 |       4 |          15.4 |
| Nigeria               |    127 |      22 |          17.3 |
| Japan                 |     33 |       6 |          18.2 |
| Kenya                 |     20 |       4 |            20 |
| Ethiopia              |      5 |       1 |            20 |
| Sri Lanka             |    124 |      25 |          20.2 |
| Indonesia             |     75 |      18 |            24 |
| Filipino              | 32,320 |   7,829 |          24.2 |
| Germany               |      4 |       1 |            25 |
| Taiwan                |     65 |      17 |          26.2 |
| Foreign (unspecified) |    107 |      29 |          27.1 |
| Ghana                 |     12 |       4 |          33.3 |
| Iraq                  |      3 |       1 |          33.3 |
| China                 |     32 |      11 |          34.4 |
| Korea (South)         |    125 |      48 |          38.4 |
| Canada                |     34 |      16 |          47.1 |
| Australia             |     19 |       9 |          47.4 |
| United States         |    340 |     184 |          54.1 |
| Vietnam               |      3 |       2 |          66.7 |
| United Kingdom        |     18 |      14 |          77.8 |

### Box Summary: Percentile Rank by Citizenship (n>=5)

<!-- chart_type: box | x: CITIZENSHIP_FINAL | y: NMS_PER_num | series: none
     population: citizenship groups with n>=5
     n: 37,347 | denominator: no-PLE-match observable examinees
     source_tab: 4 | element_id: fig_pc_box_pct -->

| CITIZENSHIP_FINAL     |      n |   min |    q1 |   median |    q3 |   max |   outliers |
|:----------------------|-------:|------:|------:|---------:|------:|------:|-----------:|
| Australia             |     17 |    -1 |    41 |       73 |    92 |    99 |          0 |
| Bangladesh            |      8 |     2 | 12.25 |     30.5 | 51.25 |    62 |          0 |
| Canada                |     32 |     4 | 41.75 |     69.5 | 88.25 |    99 |          0 |
| China                 |     31 |     9 |  27.5 |       55 |    86 |    99 |          0 |
| Ethiopia              |      5 |     7 |    11 |       23 |    28 |    87 |          1 |
| Filipino              | 32,177 |    -1 |    18 |       41 |    69 |    99 |          0 |
| Foreign (unspecified) |    106 |    -1 | 10.25 |       39 | 74.75 |    98 |          0 |
| Ghana                 |     12 |    19 | 31.25 |     44.5 |    77 |    84 |          0 |
| India                 |  2,597 |    -1 |     2 |       12 |    39 |    99 |         18 |
| Indonesia             |     75 |    -1 |  15.5 |       32 |    63 |    99 |          0 |
| Iran                  |    125 |    -1 |     1 |       10 |    37 |    96 |          2 |
| Japan                 |     33 |     1 |    23 |       41 |    55 |    89 |          0 |
| Kenya                 |     20 |     1 | 37.75 |       52 |    56 |    96 |          5 |
| Korea (South)         |    124 |     4 |  34.5 |       58 |    81 |    99 |          0 |
| Malaysia              |     76 |    -1 |     6 |       24 | 38.25 |    98 |          4 |
| Myanmar               |      8 |    -1 |     2 |      3.5 |   5.5 |    47 |          1 |
| Nepal                 |    418 |    -1 |    11 |       32 |    55 |    97 |          0 |
| Nigeria               |    127 |    -1 |     6 |       26 |  57.5 |    98 |          0 |
| Pakistan              |     26 |    -1 |  3.25 |       14 | 61.75 |    92 |          0 |
| Somalia               |     38 |    -1 |  -0.5 |        2 |     3 |    48 |          4 |
| Sri Lanka             |    124 |    -1 |    24 |     44.5 |    65 |    96 |          0 |
| Sudan                 |     14 |    -1 |    -1 |      4.5 |    12 |    26 |          0 |
| Taiwan                |     65 |    -1 |     7 |       25 |    70 |    99 |          0 |
| Thailand              |    580 |    -1 |     6 |       16 |    36 |    98 |         16 |
| United Kingdom        |     18 |    23 |    74 |     79.5 | 85.75 |    97 |          3 |
| United States         |    330 |    -1 | 42.25 |       75 |    89 |    99 |          0 |

### Box Summary: TRUE Raw Score by Citizenship (n>=5)

<!-- chart_type: box | x: CITIZENSHIP_FINAL | y: TotalRawScoreTRUE | series: none
     population: citizenship groups with n>=5
     n: 37,347 | denominator: no-PLE-match observable examinees
     source_tab: 4 | element_id: fig_pc_box_raw -->

| CITIZENSHIP_FINAL     |      n |   min |     q1 |   median |     q3 |   max |   outliers |
|:----------------------|-------:|------:|-------:|---------:|-------:|------:|-----------:|
| Australia             |     19 |    50 |    120 |      150 |  170.5 |   200 |          0 |
| Bangladesh            |      8 |    69 |  89.75 |    102.5 | 116.25 |   135 |          0 |
| Canada                |     34 |    77 | 117.25 |      144 |    165 |   223 |          0 |
| China                 |     32 |    86 |  104.5 |    127.5 | 163.25 |   215 |          0 |
| Ethiopia              |      5 |    82 |     89 |      101 |    110 |   164 |          1 |
| Filipino              | 32,302 |    37 |     97 |      116 |    138 |   223 |        163 |
| Foreign (unspecified) |    107 |    56 |   88.5 |      115 |    150 |   200 |          0 |
| Ghana                 |     12 |    94 | 103.75 |      110 |    135 |   151 |          0 |
| India                 |  2,596 |     9 |     69 |       89 |    112 |   216 |          9 |
| Indonesia             |     75 |    56 |     94 |      109 |    134 |   198 |          1 |
| Iran                  |    125 |    40 |     69 |       88 |    117 |   171 |          0 |
| Japan                 |     33 |    65 |    100 |      115 |    128 |   166 |          0 |
| Kenya                 |     19 |    57 |    110 |      121 |    130 |   183 |          4 |
| Korea (South)         |    125 |    79 |    111 |      131 |    155 |   194 |          0 |
| Malaysia              |     76 |    44 |     84 |     99.5 | 117.25 |   174 |          1 |
| Myanmar               |      8 |    50 |   68.5 |       73 |  80.75 |   125 |          2 |
| Nepal                 |    417 |    47 |     89 |      108 |    125 |   195 |          5 |
| Nigeria               |    127 |    59 |   81.5 |      102 |    125 |   178 |          0 |
| Pakistan              |     26 |    48 |     73 |       93 |  129.5 |   176 |          0 |
| Somalia               |     38 |    43 |  61.25 |       69 |     74 |   114 |          3 |
| Sri Lanka             |    124 |    60 | 100.75 |      119 |    134 |   177 |          0 |
| Sudan                 |     14 |    48 |     61 |     76.5 |  91.25 |   104 |          0 |
| Taiwan                |     62 |    56 |   85.5 |      110 |    139 |   184 |          0 |
| Thailand              |    575 |    46 |     80 |       95 |  112.5 |   176 |          8 |
| United Kingdom        |     18 |    99 | 140.25 |      151 |    162 |   186 |          1 |
| United States         |    336 |    47 |    122 |      149 | 168.25 |   216 |          1 |

### Summary by Citizenship

| CITIZENSHIP_FINAL     |   n_examinees |   median_percentile_rank |   median_true_raw_score |   top_decile_n |   top_decile_pct |   bottom_decile_n |   bottom_decile_pct |
|:----------------------|--------------:|-------------------------:|------------------------:|---------------:|-----------------:|------------------:|--------------------:|
| Filipino              |        32,320 |                       41 |                     116 |          7,829 |            24.22 |            11,933 |               36.92 |
| India                 |         2,598 |                       12 |                      89 |            195 |             7.51 |             1,442 |                55.5 |
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

### Year Distribution by Citizenship

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
| Filipino              |  1,562 |  1,551 |  2,048 |  3,250 |  3,675 |  4,412 |  4,756 |  4,863 |  6,203 |
| Foreign (unspecified) |     10 |      7 |     13 |     19 |     13 |      9 |      7 |     17 |     12 |
| Germany               |      1 |      0 |      1 |      0 |      1 |      0 |      1 |      0 |      0 |
| Ghana                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      2 |      9 |
| Guam                  |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |
| India                 |     43 |    187 |    180 |    140 |     89 |     44 |    147 |    337 |  1,431 |
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
Person-level record detail (37,381 rows) is available in the live dashboard and its CSV downloads; not dumped inline here per export contract Rule 3.


---


## Comparative Analysis: Foreigners vs Filipino Undergrad Groups

*Population: 4 groups (Verified Foreigner; Filipino+foreign undergrad; Filipino+public undergrad; Filipino+private undergrad), n=73,293 combined*

| Group                         |      n |   median_percentile_rank |   q25_pct |   q75_pct |   median_raw_score |   PLE linkage rate % |
|:------------------------------|-------:|-------------------------:|----------:|----------:|-------------------:|---------------------:|
| Filipinos (foreign undergrad) |    643 |                       66 |        35 |        86 |                137 |                35.89 |
| Filipinos (private undergrad) | 52,317 |                       50 |        25 |        76 |                123 |                44.98 |
| Filipinos (public undergrad)  | 14,410 |                       66 |        35 |        90 |                137 |                49.35 |
| Foreigners (non-Filipino)     |  5,159 |                       23 |         4 |        53 |                100 |                 2.49 |

### Box Summary: Percentile Rank by Comparison Group

<!-- chart_type: box | x: _cmp_group | y: NMS_PER_num | series: none
     population: 4 comparison groups
     n: 73,293 | denominator: combined comparison population
     source_tab: 4 | element_id: fig_cmp_pct_box -->

| _cmp_group                    |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|:------------------------------|-------:|------:|-----:|---------:|-----:|------:|-----------:|
| Filipinos (foreign undergrad) |    643 |    -1 |   35 |       66 |   86 |    99 |          0 |
| Filipinos (private undergrad) | 52,317 |    -1 |   25 |       50 |   76 |    99 |          0 |
| Filipinos (public undergrad)  | 14,410 |    -1 |   35 |       66 |   90 |    99 |          0 |
| Foreigners (non-Filipino)     |  5,159 |    -1 |    4 |       23 |   53 |    99 |          0 |

### Box Summary: TRUE Raw Score by Comparison Group

<!-- chart_type: box | x: _cmp_group | y: TotalRawScoreTRUE | series: none
     population: 4 comparison groups
     n: 73,293 | denominator: combined comparison population
     source_tab: 4 | element_id: fig_cmp_raw_box -->

| _cmp_group                    |      n |   min |   q1 |   median |     q3 |   max |   outliers |
|:------------------------------|-------:|------:|-----:|---------:|-------:|------:|-----------:|
| Filipinos (foreign undergrad) |    652 |    38 |  110 |      137 | 160.25 |   219 |          0 |
| Filipinos (private undergrad) | 52,787 |    10 |  103 |      123 |    146 |   227 |        116 |
| Filipinos (public undergrad)  | 14,638 |     9 |  111 |      137 |    166 |   231 |          7 |
| Foreigners (non-Filipino)     |  5,162 |     9 |   77 |      100 |    124 |   223 |         35 |

### Bin Distribution by Comparison Group

| _cmp_group                    |    B1 |    B2 |   B3 |    B4 |    B5 |   B6 |    B7 |    B8 |    B9 |   B10 |
|:------------------------------|------:|------:|-----:|------:|------:|-----:|------:|------:|------:|------:|
| Filipinos (foreign undergrad) |  8.27 |   6.4 | 6.24 |  7.02 |  5.62 | 9.36 | 11.39 | 11.39 | 13.88 | 20.44 |
| Filipinos (private undergrad) | 10.46 |  9.18 | 9.16 | 10.16 | 10.28 |  9.7 |  9.44 |  9.83 | 10.18 | 11.61 |
| Filipinos (public undergrad)  |  8.18 |  6.56 | 6.18 |  7.29 |  7.56 | 7.68 |  9.04 |  9.86 | 12.34 |  25.3 |
| Foreigners (non-Filipino)     | 30.95 | 12.42 | 9.75 |  9.48 |  8.14 |  6.7 |  5.72 |  5.41 |  5.51 |  5.93 |

### Top vs Bottom Bin Share by Comparison Group

| Group                         |   Top B8-B10 (%) |   Bottom B1-B3 (%) |
|:------------------------------|-----------------:|-------------------:|
| Filipinos (foreign undergrad) |            45.71 |              20.91 |
| Filipinos (private undergrad) |            31.62 |               28.8 |
| Filipinos (public undergrad)  |             47.5 |              20.92 |
| Foreigners (non-Filipino)     |            16.85 |              53.12 |

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
| Education                    |  3,461 |       52 |    26 |    78 |
| Engineering & Technology     |    731 |       72 |    41 |    91 |
| Medical & Allied             | 63,834 |       49 |    25 |    73 |
| Natural Sciences             | 40,961 |       54 |    24 |    81 |
| Other                        |  8,306 |       54 |    27 |    79 |
| Social & Behavioral Sciences | 16,400 |       40 |    11 |    73 |

---


# Tab 5 -- University Type Analysis


## Table 13 -- Institution Type by Location Mix

*Population: undergrad type+location present, n=133,477*

| UNDERGRAD_UNI_TYPE   | UNDERGRAD_UNI_LOCATION   |   Count |   Percent of total |
|:---------------------|:-------------------------|--------:|-------------------:|
| Foreign              | International            |   1,892 |               1.42 |
| Private              | Local                    | 103,669 |              77.67 |
| Public               | Local                    |  27,916 |              20.91 |

---


## Table 14 -- Institution Type by Location Matrix


### Counts (with totals)

| UNDERGRAD_UNI_TYPE   |   International |   Local |     All |
|:---------------------|----------------:|--------:|--------:|
| Foreign              |           1,892 |       0 |   1,892 |
| Private              |               0 | 103,669 | 103,669 |
| Public               |               0 |  27,916 |  27,916 |
| All                  |           1,892 | 131,585 | 133,477 |

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
| Private              |               0 |   78.78 |
| Public               |               0 |   21.22 |

---


## Bin Distribution by Institution Type x Location

<!-- chart_type: heatmap+top_share_bar | x: PercentileBin | y: UNDERGRAD_UNI_TYPE x LOCATION | series: fig_t5_heatmap_instloc
     population: row %
     n: valid percentile bin | denominator: 130,494
     source_tab: best-record uni subset | element_id: 5 -->

| index                   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:------------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign (International) | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private (Local)         | 12.04 | 9.69 |    9 | 9.92 | 9.91 | 9.94 | 9.47 | 9.69 |  9.73 | 10.63 |
| Public (Local)          | 10.83 | 8.18 | 7.56 | 8.25 | 8.52 | 8.89 |  9.1 | 9.57 |  11.2 |  17.9 |

---


## Bin Composition by University Type (%)

<!-- chart_type: stacked_bar | x: UNDERGRAD_UNI_TYPE | y: PercentileBin | series: fig_t5_stacked_uni
     population: row %
     n: valid percentile bin | denominator: 130,494
     source_tab: best-record uni subset | element_id: 5 -->

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private              | 12.04 | 9.69 |    9 | 9.92 | 9.91 | 9.94 | 9.47 | 9.69 |  9.73 | 10.63 |
| Public               | 10.83 | 8.18 | 7.56 | 8.25 | 8.52 | 8.89 |  9.1 | 9.57 |  11.2 |  17.9 |

---


## Table 15 -- Bin Counts by University Type

| UNDERGRAD_UNI_TYPE   |     B1 |    B2 |    B3 |     B4 |     B5 |     B6 |    B7 |    B8 |    B9 |    B10 |   Total students |
|:---------------------|-------:|------:|------:|-------:|-------:|-------:|------:|------:|------:|-------:|-----------------:|
| Foreign              |    262 |   174 |   140 |    176 |    145 |    164 |   161 |   175 |   197 |    266 |            1,860 |
| Private              | 12,205 | 9,823 | 9,127 | 10,061 | 10,044 | 10,079 | 9,602 | 9,821 | 9,864 | 10,774 |          101,400 |
| Public               |  2,949 | 2,228 | 2,058 |  2,247 |  2,320 |  2,421 | 2,478 | 2,606 | 3,051 |  4,876 |           27,234 |

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

*Population: undergrad type+location present, n=133,477*

| UNDERGRAD_UNI_TYPE   |   Medical & Allied |   Other Courses |
|:---------------------|-------------------:|----------------:|
| Foreign              |              40.38 |           59.62 |
| Private              |              49.54 |           50.46 |
| Public               |              41.22 |           58.78 |

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
| NOT SPECIFIED/UNLISTED                                             | Local                    |                513 |
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
<!-- truncated: true | shown: 50 | total: 798 -->


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
     n: uni subset | denominator: 130,494
     source_tab: best-record, Public/Private/Foreign | element_id: 6 -->

| UNDERGRAD_UNI_TYPE   | PercentileBin   |   count |
|:---------------------|:----------------|--------:|
| Public               | B1              |   2,949 |
| Public               | B2              |   2,228 |
| Public               | B3              |   2,058 |
| Public               | B4              |   2,247 |
| Public               | B5              |   2,320 |
| Public               | B6              |   2,421 |
| Public               | B7              |   2,478 |
| Public               | B8              |   2,606 |
| Public               | B9              |   3,051 |
| Public               | B10             |   4,876 |
| Private              | B1              |  12,205 |
| Private              | B2              |   9,823 |
| Private              | B3              |   9,127 |
| Private              | B4              |  10,061 |
| Private              | B5              |  10,044 |
| Private              | B6              |  10,079 |
| Private              | B7              |   9,602 |
| Private              | B8              |   9,821 |
| Private              | B9              |   9,864 |
| Private              | B10             |  10,774 |
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
| B1              | Confirmed PLE passer   |     795 |
| B1              | No confirmed PLE match |   6,058 |
| B2              | Confirmed PLE passer   |   1,336 |
| B2              | No confirmed PLE match |   4,548 |
| B3              | Confirmed PLE passer   |   1,703 |
| B3              | No confirmed PLE match |   4,110 |
| B4              | Confirmed PLE passer   |   2,330 |
| B4              | No confirmed PLE match |   4,143 |
| B5              | Confirmed PLE passer   |   3,003 |
| B5              | No confirmed PLE match |   3,579 |
| B6              | Confirmed PLE passer   |   3,168 |
| B6              | No confirmed PLE match |   3,116 |
| B7              | Confirmed PLE passer   |   3,407 |
| B7              | No confirmed PLE match |   2,952 |
| B8              | Confirmed PLE passer   |   3,690 |
| B8              | No confirmed PLE match |   3,014 |
| B9              | Confirmed PLE passer   |   4,474 |
| B9              | No confirmed PLE match |   2,789 |
| B10             | Confirmed PLE passer   |   7,073 |
| B10             | No confirmed PLE match |   2,885 |

### PLE Status Composition within Each Bin (%)

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


## Tables 21-22 -- Largest Pathways into B8-B10

| UNDERGRAD_UNI_TYPE   | PercentileBin   |   Count |
|:---------------------|:----------------|--------:|
| Private              | B10             |  10,774 |
| Private              | B9              |   9,864 |
| Private              | B8              |   9,821 |
| Public               | B10             |   4,876 |
| Public               | B9              |   3,051 |
| Public               | B8              |   2,606 |
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
| Confirmed PLE passer   |                      31,572 |                          139 |                     141.04 |                       120 |                       162 |                      31,572 |                           74 |                      73.85 |                        63 |                        84 |                       31,572 |                            66 |                       67.18 |                         55 |                         79 |                30,988 |                     69 |                64.56 |                  45 |                  88 |            31,581 |                552 |           555.86 |             489 |             624 |            31,581 |                548 |           552.13 |             491 |             612 |           31,581 |               544 |          546.07 |            480 |            610 |
| No confirmed PLE match |                      37,888 |                          114 |                      116.2 |                        94 |                       136 |                      37,888 |                           62 |                      61.89 |                        51 |                        73 |                       37,888 |                            52 |                       54.31 |                         42 |                         65 |                37,758 |                     38 |                42.06 |                  15 |                  66 |            37,922 |                470 |           471.63 |             399 |             545 |            37,922 |                484 |           480.26 |             415 |             546 |           37,922 |               471 |          474.14 |            406 |            539 |

---


## Box Summary: TRUE Raw Score by PLE Status

<!-- chart_type: box | x: PLE_STATUS_LABEL | y: TotalRawScoreTRUE | series: none
     population: observable cohort
     n: 69,503 | denominator: observable best-record examinees
     source_tab: 7 | element_id: fig_t7_box_raw_ple -->

| PLE_STATUS_LABEL       |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|:-----------------------|-------:|------:|-----:|---------:|-----:|------:|-----------:|
| Confirmed PLE passer   | 31,572 |    48 |  120 |      139 |  162 |   231 |          5 |
| No confirmed PLE match | 37,888 |     9 |   94 |      114 |  136 |   223 |        201 |

---


## Table 24 -- Mann-Whitney: Confirmed vs No Match

| Score              |      U_stat | p_value   |   effect_r |   Confirmed_median |   NoMatch_median |
|:-------------------|------------:|:----------|-----------:|-------------------:|-----------------:|
| Total Raw Score    | 8.63044e+08 | <0.001    |      -0.44 |                139 |              114 |
| Part I             | 8.42159e+08 | <0.001    |      -0.41 |                 74 |               62 |
| Part II            | 8.49698e+08 | <0.001    |      -0.42 |                 66 |               52 |
| Percentile Rank    | 8.35619e+08 | <0.001    |      -0.43 |                 69 |               38 |
| GPS Standard Score | 8.58051e+08 | <0.001    |      -0.43 |                552 |              470 |

---


## Figure 21 -- Bin Distribution by PLE Status

<!-- chart_type: stacked_bar | x: PLE_STATUS_LABEL | y: PercentileBin | series: fig_t7_bin_ple
     population: row %
     n: observable cohort | denominator: 69,503
     source_tab: observable best-record examinees | element_id: 7 -->

| PLE_STATUS_LABEL       |    B1 |    B2 |    B3 |    B4 |   B5 |    B6 |   B7 |    B8 |    B9 |   B10 |
|:-----------------------|------:|------:|------:|------:|-----:|------:|-----:|------:|------:|------:|
| Confirmed PLE passer   |  2.57 |  4.31 |   5.5 |  7.52 | 9.69 | 10.23 |   11 | 11.91 | 14.44 | 22.83 |
| No confirmed PLE match | 16.29 | 12.23 | 11.05 | 11.14 | 9.62 |  8.38 | 7.94 |   8.1 |   7.5 |  7.76 |

---


## Table 25 -- PLE Status Composition within Each Bin

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
| Foreign              |                        1159 |                     258 |                      901 |                     22.26 |
| Private              |                       52821 |                   23757 |                    29064 |                     44.98 |
| Public               |                       14642 |                    7226 |                     7416 |                     49.35 |

---


## Tables 28-30 -- Confirmed PLE Alignment by Year / Course / University Type

|   Year |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|-------:|----------------------------:|------------------------:|-------------------------:|--------------------------:|
|  2,006 |                        3698 |                    2005 |                     1693 |                     54.22 |
|  2,007 |                        3690 |                    1832 |                     1858 |                     49.65 |
|  2,008 |                        4965 |                    2583 |                     2382 |                     52.02 |
|  2,009 |                        7461 |                    3757 |                     3704 |                     50.36 |
|  2,010 |                        8623 |                    4534 |                     4089 |                     52.58 |
|  2,011 |                        8842 |                    3918 |                     4924 |                     44.31 |
|  2,012 |                        9405 |                    4006 |                     5399 |                     42.59 |
|  2,013 |                        9867 |                    4210 |                     5657 |                     42.67 |
|  2,014 |                       12952 |                    4736 |                     8216 |                     36.57 |
| UNDERGRAD_COURSE_GROUP       |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Education                    |                        3188 |                    1699 |                     1489 |                     53.29 |                       53 |
| Other                        |                        6612 |                    3201 |                     3411 |                     48.41 |                       55 |
| Medical & Allied             |                       38144 |                   17833 |                    20311 |                     46.75 |                       48 |
| Natural Sciences             |                       16512 |                    6994 |                     9518 |                     42.36 |                       63 |
| Engineering & Technology     |                         318 |                     118 |                      200 |                     37.11 |                       71 |
| Social & Behavioral Sciences |                        4729 |                    1736 |                     2993 |                     36.71 |                       63 |
| UNDERGRAD_UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:---------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Foreign              |                        1159 |                     258 |                      901 |                     22.26 |                       57 |
| Private              |                       52821 |                   23757 |                    29064 |                     44.98 |                       50 |
| Public               |                       14642 |                    7226 |                     7416 |                     49.35 |                       66 |

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
| Analytic repeat takers | 33,702 | with complete first/last scores | - |
| Improved percentile rank | 77.65% | analytic repeat takers | - |
| Improved raw score | 73.58% | analytic repeat takers | - |
| Median percentile change | 11.00 | analytic repeat takers | - |
| Median raw score change | 12.00 | analytic repeat takers | - |

## Box Summary: First-to-Last Attempt Change

<!-- chart_type: box | x: Measure | y: Change | series: none
     population: analytic repeat takers
     n: 33,702 | denominator: repeat takers with complete first/last scores
     source_tab: 8 | element_id: fig_t8_box_change -->

| Measure           |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|:------------------|-------:|------:|-----:|---------:|-----:|------:|-----------:|
| Percentile change | 33,702 |   -71 |    2 |       11 |   25 |    94 |        444 |
| Raw score change  | 33,702 |   -84 |    0 |       12 |   26 |   119 |        313 |

---


## First vs Last Percentile (Repeat Takers, Preview)

<!-- chart_type: scatter | x: first_pct | y: last_pct | series: none
     population: analytic repeat takers
     n: 33,702 | denominator: repeat takers with complete first/last scores
     source_tab: 8 | element_id: fig_t8_scatter_repeat -->

| PERSON_KEY                                               |   first_pct |   last_pct |   n_attempts |
|:---------------------------------------------------------|------------:|-----------:|-------------:|
| ASUNCION, JESLY ANNE BULUSAN||8/10/1992                  |          -1 |         11 |            9 |
| H ISMAEL, DONORAIN EDRES||2/6/1989                       |          24 |          3 |            8 |
| LLANES, RUDOLPH RICAMARA||5/12/1988                      |           5 |         40 |            8 |
| PASCUAL, KENNETH TRISTAN NAZARENO||05/13/1990            |           6 |         40 |            8 |
| LAMBON, EMMANUEL YENUBE||04/27/1987                      |           5 |         67 |            8 |
| GONZAGA, CATHERINE KAYE SALVACION||01/29/1993            |          11 |         25 |            8 |
| QUIMING, LYAN DJAMILLE BUSTAMANTE||11/11/1992            |          32 |         56 |            8 |
| QUILLOPE, AIMIE KLAIN MAGAS||12/9/1991                   |           6 |         20 |            7 |
| CAVAN, LUCKY ANGELO BARUIS||8/6/1993                     |           2 |         28 |            7 |
| EVANGELIO, JEAN MARIE AGUILA||1/8/1991                   |           4 |         30 |            7 |
| PEREZ, APRIL HAMILI GRACE CAYDE||04/24/1987              |          18 |         37 |            7 |
| AGABIN, AIZA ANGOLLUAN||12/9/1988                        |          19 |         41 |            7 |
| COLLANTES, ANTHONY AVENA||11/9/1993                      |          49 |         80 |            7 |
| NARVASA, JAMES JR ROSALES||03/14/1989                    |           1 |          2 |            7 |
| MUKSAN, RAYHAN JAINA ABAM||9/2/1991                      |          15 |         25 |            7 |
| CAJANDIG, PRINCESS MAY TEE||3/5/1992                     |           1 |          3 |            7 |
| ERNI, HANZEL CHARZON ALEGRE||06/15/1987                  |          10 |         60 |            7 |
| CAPOQUIAN, WILMARY PAJARES||12/2/1993                    |           9 |         38 |            7 |
| DIZON, GINA PAULA DENSING||3/6/1991                      |          19 |         63 |            7 |
| MONJE, REEMA LI VALDEZ||06/24/1994                       |           5 |         33 |            7 |
| VELOSO, JOSE CARLOS GLIANE||09/13/1990                   |           9 |         26 |            7 |
| MACALANGCOM, JAWAHER SALI||03/15/1989                    |          -1 |          2 |            7 |
| TURGANO, LOIS KATHLEEN MARY JAVILLONAR||05/18/1985       |           2 |         49 |            7 |
| SAMPULNA, JIM II DURUIN||7/6/1989                        |           8 |         33 |            7 |
| CATEDRAL, GLENNA HOPE JOYCE TUAZON||10/12/1989           |           9 |         15 |            6 |
| GAERLAN, LOURD DERICK JURADO||02/24/1991                 |          15 |         46 |            6 |
| CAMPOS, CRISTINE SEDANO||1/4/1988                        |           8 |         33 |            6 |
| FIGUEROA, RALPH BERNARD MOJICA||9/9/1992                 |           2 |         13 |            6 |
| LIM, KATRINA ROSE LAO||2/6/1990                          |          12 |         35 |            6 |
| CONCEPCION, MA CARMELA MENDOZA||01/22/1991               |           3 |          4 |            6 |
| LOGO, JOHN CYRUS PEREZ||02/20/1992                       |          25 |         62 |            6 |
| BANZON, ANA KRISTIANA LOUISE AUSTRIA||11/14/1993         |          15 |         68 |            6 |
| DONADILLA, ROSELLINE ZAPATA||09/19/1993                  |           3 |         46 |            6 |
| BANDARI, LAXMI PRASANNA||06/19/1996                      |          12 |         27 |            6 |
| LORESCA, ROSE LEEN CRISANTO||9/3/1992                    |           3 |         15 |            6 |
| MADRIAGA, KATRIN VELASCO||06/30/1990                     |          11 |         34 |            6 |
| HIPOLITO, JAYVY RAMOS||7/4/1992                          |           3 |         16 |            6 |
| CANGAS, MARI LEN BATALLA||11/20/1993                     |           1 |         26 |            6 |
| DOMINGO, PAMELA CASTANO||01/20/1993                      |          14 |         32 |            6 |
| CASTRO, JEANINE||10/16/1974                              |          -1 |         24 |            6 |
| DEMAFILES, DEAN ROBERT ANCHETA||06/29/1988               |           7 |         33 |            6 |
| DAOWAG, FAITH ASWIGUE||10/19/1991                        |           7 |         44 |            6 |
| MAHARJAN, SUNILA||02/16/1995                             |          13 |          3 |            6 |
| ANANDAN, MUGUNTHAN||03/21/1997                           |           3 |         39 |            6 |
| MALLILLIN, KARLA MAY CANTOR||05/22/1990                  |          21 |         41 |            6 |
| GILERA, HANNA PATRICIA VALLEJA||12/2/1995                |          16 |         37 |            6 |
| MORALES, JANINE CARLA MANZANERO||6/12/1990               |           5 |         28 |            6 |
| NANDAKUMAR NAIR, SREEKUMAR||1/6/1996                     |          21 |          4 |            6 |
| NUNES, XERYL ANN DIMACULANGAN||3/5/1991                  |          34 |         57 |            6 |
| PANGAN, DESIREE CLEMENTE||12/9/1987                      |          23 |         40 |            6 |
| CONDE, MA THELMA PRECY CONSULTA||11/25/1993              |          18 |         60 |            6 |
| PASAO, CATHERINE PALIZA||3/11/1992                       |           5 |         54 |            6 |
| GOTICO, AARON SAMUEL TIBAYAN||09/26/1994                 |          32 |         59 |            6 |
| CLERIGO, APRILLE VANESSA ROA||12/4/1994                  |           8 |         59 |            6 |
| CHAUDHARY, ANIL JESUNGBHAI||08/26/1994                   |           4 |         83 |            6 |
| CARANGUIAN, MARIFE DURAN||12/2/1992                      |           5 |         47 |            6 |
| DALMAN, JENDEE DEMORITO||8/7/1992                        |           2 |         28 |            6 |
| BAUTISTA, KAYE DOLFO||4/8/1992                           |           9 |         29 |            6 |
| PASUPATHY, DIVYA||5/1/1997                               |          -1 |         11 |            6 |
| PATEL, PUJAN MUKESHKUMAR||1/1/1997                       |          86 |         16 |            6 |
| ACUNA, JANELLA MARA VILLANUEVA||02/16/1994               |           3 |         45 |            6 |
| GONZALES, MAJESTY DELA CRUZ||12/1/1996                   |           2 |         11 |            6 |
| KUMAR, ARUN||09/21/1995                                  |           9 |         15 |            6 |
| GUEVARRA, MARIE THERESE TAEZA||09/21/1993                |          39 |         43 |            6 |
| PROFETANA, ERLA RHYN VEGA||03/28/1992                    |          13 |         34 |            6 |
| RABARI, AMIT MANABHAI||1/3/1997                          |           9 |         13 |            6 |
| GALLARDO, JOSHUA PENAREDONDA||11/29/1990                 |          16 |          9 |            6 |
| RAGUVEL, MANIBHARATHI||10/15/1996                        |          -1 |         24 |            6 |
| DE GUZMAN, NINA GAE CAMAGAY||02/26/1995                  |           2 |          6 |            6 |
| REYES, JAIRUS REYES||5/7/1991                            |          49 |         80 |            6 |
| BARIA, TARUNKUMAR GULABSINH||06/28/1996                  |           6 |         28 |            6 |
| RIVERA, KEZIA EARL DIGNOS||04/24/1986                    |           4 |         36 |            6 |
| ADEWALE, FISAYO FOLASADE||08/15/1989                     |           6 |         26 |            6 |
| ROMANCAP, JAMELA KASID||10/5/1990                        |           2 |          1 |            6 |
| CABALLERO, NIKKOLE NICOLAS||4/7/1993                     |          16 |         12 |            6 |
| SAADRA, RAEFAH YUSOPH||09/28/1994                        |          -1 |         24 |            6 |
| SALIK, FAYDHAL AMPATUAN||07/30/1990                      |          16 |         28 |            6 |
| SANCHEZ, KATRINA MANGAOANG||7/7/1992                     |           2 |         18 |            6 |
| HABILING, KAVIN BIDANG||05/18/1992                       |          14 |         92 |            6 |
| SANCHEZ, MA KRISTINE JOY KALAW||12/26/1993               |          -1 |          4 |            6 |
| SEMBRANO, GABRIELYNE DELA CRUZ||07/29/1992               |          12 |         25 |            6 |
| ALDEA, ALDA LOU MATEUM||5/1/1992                         |           6 |         22 |            6 |
| SUBRAMANIAN, KUMARAVEL||7/11/1997                        |           8 |         32 |            6 |
| DAYANDAYAN, DARWIN ADRIAN UMALI||01/25/1992              |          24 |         36 |            6 |
| AGOR, ELIS MARIE MALLANAO||8/10/1994                     |           6 |          8 |            6 |
| SUBU, UMAMAHESWARI||05/30/1996                           |           6 |         55 |            6 |
| LAWRENCE, NICKSON||06/17/1997                            |          10 |          5 |            6 |
| GONZALES, CHRYZEL ANGELICA BABAAN||09/22/1990            |          31 |         46 |            6 |
| THAKOR, DHAVAL RAKESHKUMAR||09/22/1996                   |          16 |         21 |            6 |
| AGOJO, ERYLL JOY HOLGADO||1/10/1993                      |           5 |         57 |            6 |
| BHOJAK, NIDHIBEN VIKRAMBHAI||03/29/1997                  |          17 |         48 |            6 |
| TUTING, JULIE ANN DENIEGA||4/7/1988                      |           8 |          9 |            6 |
| VALDERRAMA, BEA AIRA BALMACEDA||10/10/1992               |           4 |         11 |            6 |
| BARRIOS, KEVIN GEORGE BEARE||04/27/1991                  |          72 |         88 |            6 |
| VAZA, JIGNASA VAJUBHAI||07/31/1996                       |          23 |         17 |            6 |
| CASIN, DENISE ARIELLE ACERO||1/8/1992                    |           9 |         55 |            6 |
| ISIDRO, IAN QUILON||04/27/1990                           |          16 |         15 |            6 |
| DILLA, PERCIVAL CALIXTO||6/6/1990                        |          10 |         13 |            6 |
| ENTERO, ALLANA GHISEL BAUTISTA||09/27/1995               |          13 |         51 |            6 |
| ASUAKO, FRANCIS||10/6/1987                               |          12 |         59 |            6 |
| VERZOSA, JEROME TURINGAN||04/30/1990                     |          14 |         47 |            6 |
| VIDAL, JEANNETTE ANNE NAVARRO||07/27/1995                |           6 |         34 |            6 |
| LACANDULA, GISELLE ALFORQUE||5/4/1988                    |          43 |         30 |            6 |
| VILLENA, MICHAEL BERNARD SALUD||11/2/1995                |           2 |         85 |            6 |
| GARCIA, KEITH CACHO||9/11/1984                           |          14 |         18 |            6 |
| ANDREWS, DOLL SUZANNE||1/12/1996                         |           3 |         57 |            6 |
| WAL, MICHAEL JUDE CASTANEDA||05/29/1993                  |           8 |         64 |            6 |
| GUTIERREZ, PAOLO GABRIEL FERRER||05/17/1995              |          30 |         52 |            6 |
| BAGTILAY, APRIL DIANN JUAN||7/4/1992                     |          29 |         45 |            6 |
| CUDAL, RIO CLAIRE IYADAN||03/31/1996                     |           6 |         48 |            6 |
| WATANABE, MAKOTO||10/18/1979                             |          -1 |         24 |            6 |
| GEORGE SELVAMARY, SAGAYA HELAN MARY||1/11/1996           |           1 |         11 |            6 |
| GERONIMO, MONA LEIGH LEVISTE||03/24/1992                 |          27 |         99 |            5 |
| LACERNA, JOHN CHRISTOPHER LUCENA||11/17/1994             |          46 |         69 |            5 |
| ESPIRITU, MARIE CHRISTINE ILAGAN||8/9/1993               |          27 |         42 |            5 |
| CHRISTOPHER MANI, ELIJAH OSBORN||11/6/1996               |          -1 |         43 |            5 |
| IGNACIO, NICOLE TARA JAVIER||04/28/1993                  |           1 |         19 |            5 |
| ELEAZAR, GENICA SUMAMPONG||10/11/1994                    |          12 |         25 |            5 |
| ATIENZA, AHRJAY DE GUZMAN||11/8/1992                     |           6 |         19 |            5 |
| BANGAYAN, BONNA ALLAM||5/4/1992                          |          12 |         52 |            5 |
| SOSA, KIMBERLY ANN PAYAWAL||12/1/1992                    |          -1 |          9 |            5 |
| KHRUSHEV, SWATHI||03/13/1997                             |          12 |         23 |            5 |
| LANGEBAN, MARREM JANELLE ANGELES||01/20/1994             |           2 |         20 |            5 |
| AWA, JULIE SUMINGUIT||08/15/1991                         |           8 |         41 |            5 |
| COLLERA, CARMINA DELA CRUZ||10/23/1992                   |           3 |         23 |            5 |
| ABIERAS, AMAE JAY BULCASE||1/10/1993                     |           8 |         75 |            5 |
| CAMPOS, KIM JUSTINE ROSALI||08/13/1993                   |           4 |         17 |            5 |
| DAMARILLO, BEN JOHN CELIS||04/29/1991                    |           4 |         20 |            5 |
| ATIENZA, DON DANIEL||5/10/1992                           |          19 |         41 |            5 |
| BANGGOLLAY, FAITH ANNE MANGANIP||01/19/1990              |          14 |         26 |            5 |
| ATIENZA, EMILIANNE WEE ENG||04/22/1995                   |          87 |         82 |            5 |
| EZHAVA, ADHIRA SURENDRAN||06/17/1996                     |          -1 |         -1 |            5 |
| BAGUIWAN, JOAN SIBLAG||05/29/1993                        |           4 |         47 |            5 |
| DOCENA, RUTCHEL RISOS||9/3/1992                          |          16 |         73 |            5 |
| ENGINEER, PARTH BABUBHAI||09/23/1997                     |           1 |         31 |            5 |
| GATLA, SHRUTHI REDDY||11/9/1994                          |          14 |         52 |            5 |
| AMPELOQUIO, BERNADETTE SUYO||01/27/1994                  |           6 |         17 |            5 |
| DEBUTON, AIRON GANTALA||08/26/1994                       |          11 |         16 |            5 |
| GUDEN, DIANA ARCE||12/2/1995                             |           3 |         60 |            5 |
| LABANA, ANAND RAMANLAL||11/22/1997                       |           2 |         15 |            5 |
| DAO AYAN, KIAREI BAGGAS||04/15/1994                      |           6 |         34 |            5 |
| BANIQUED, NAPHTALI ROSALES||05/25/1987                   |          15 |         46 |            5 |
| DE ASIS, JILBERT DARONG||11/27/1991                      |          17 |         40 |            5 |
| BHATT, HARSH ATULKUMAR||11/20/1997                       |          21 |         19 |            5 |
| ANDRES, KHRISTINE MAE NAPOLES||6/5/1989                  |          11 |         29 |            5 |
| KOILRAJ, SHARUTI ROYCE||8/6/1996                         |           2 |         15 |            5 |
| KUMAR, GOPAL||12/15/1997                                 |           6 |         17 |            5 |
| BEL IDA, JASTENE VILLACORTA||12/13/1995                  |          -1 |         12 |            5 |
| ESPIRITU, SARAH JANE BIEN||2/11/1993                     |           1 |         19 |            5 |
| IBARRA, CHRISTINE ANNE FERNANDEZ||05/27/1990             |          12 |         21 |            5 |
| BELADIYA, MAHIPAL KISHORBHAI||10/29/1994                 |           3 |         74 |            5 |
| CHINTHOJU, MAYURI||12/7/1997                             |           2 |         21 |            5 |
| BAMBHAROLIYA, VIVEK BIPINBHAI||10/24/1994                |           6 |         86 |            5 |
| CABATBAT, JENVIRLI VALERIC GLORINA II LIGAYA||09/27/1986 |          20 |         20 |            5 |
| DAYAG, CORY SIBBALUCA||1/3/1986                          |           2 |         41 |            5 |
| ALVAREZ, VINCENT PAUL STA TERESA||08/23/1991             |          -1 |         12 |            5 |
| ISMAEL, JUHANISA DELINOGUN||10/13/1990                   |           9 |         21 |            5 |
| DELDACAN, FREDLAND UBALDO||3/12/1981                     |           7 |         13 |            5 |
| DHAYAL, UDDIPTA||6/6/1996                                |           2 |         18 |            5 |
| GOVINDAN, RANJITH||12/24/1996                            |          -1 |          9 |            5 |
| ALAS, KARLA PATRICIA CIRERA||02/25/1992                  |          20 |         31 |            5 |
| FERNANDO, MARIA KATHERINE CHARMAINE CALLADA||11/30/1993  |           7 |         10 |            5 |
| HILARIO, MYOLAINE CHU||05/20/1987                        |           3 |         43 |            5 |
| KHATRI, ALI ASGAR||3/6/1995                              |           1 |         -1 |            5 |
| LANDINGIN, AGNES JOYCE BARROZO||07/21/1993               |           5 |         43 |            5 |
| GALEON, EDELAINE MARIE JABANES||3/10/1994                |          15 |         37 |            5 |
| ACLAN, NOELIE JOY MOSQUITO||10/10/1992                   |           1 |         37 |            5 |
| GATBONTON, BIANCA MARGUERITE DE GUZMAN||9/7/1994         |          18 |         81 |            5 |
| BERMEJO, JARETTE LORENZO||08/27/1985                     |          20 |         27 |            5 |
| JOSYULA, SREE NEEHARIKA||02/26/1996                      |          36 |          6 |            5 |
| GUTIERREZ, JUAN MIGUEL ICARO||07/23/1990                 |          26 |         50 |            5 |
| BAYAOA, KAREN FAYE GARCIA||10/21/1991                    |          11 |         48 |            5 |
| BUMANGLAG, KATRINA MARIE DIAZ||06/15/1994                |           4 |         31 |            5 |
| BERMOY, FRANCIS CARLO ALMARIO||10/12/1994                |          20 |         67 |            5 |
| KORADIYA, RAVIKUMAR BALABHAI||7/9/1997                   |           4 |         15 |            5 |
| KORRA, RAJARAM||07/27/1998                               |           6 |          6 |            5 |
| DEL PRADO, ROSE MYSTICA FERNANDEZ||11/9/1992             |           6 |         63 |            5 |
| JOSUE, ADMIRANTE JR MAMARIL||04/14/1994                  |          16 |         27 |            5 |
| ESGUERRA, NADYNNE MARIE RAAGAS||09/14/1992               |          20 |         45 |            5 |
| CASIPIT, CARLO GABRIEL CANONIGO||10/22/1995              |          57 |         98 |            5 |
| ANTONIO, ROBIN VALDEZ||09/18/1992                        |          21 |         62 |            5 |
| BENDITA, JESSELINE MARIE GUAY||03/16/1995                |           6 |         14 |            5 |
| COCJIN, JEHU MILES SUPERIO||08/26/1995                   |          21 |          9 |            5 |
| BADUA, KHRISTAN JAY FIESTA||10/26/1991                   |           9 |         24 |            5 |
| BALBIN, MANRIC LASAGA||1/3/1992                          |           1 |         19 |            5 |
| LADUMOR, VIJAY LAKHABHAI||12/30/1996                     |           9 |          4 |            5 |
| ALVENIZ, SHENNA MAE VILLEGAS||1/8/1994                   |          -1 |          2 |            5 |
| JADAV, RIDHAM DHIRUBHAI||01/22/1998                      |          17 |          3 |            5 |
| DENNA, PRINCESS MARY ABBYGAIL MANGAGOM||05/21/1991       |          10 |         43 |            5 |
| ARAGA, AKHIL RAGHAVENDRA REDDY||08/29/1996               |           2 |          9 |            5 |
| ISRAEL, LEONIDES RAMONETTE CANAPI||12/27/1991            |          14 |         43 |            5 |
| BALLUNGAY, JOHN HARLEY CUNTAPAY||12/3/1990               |          18 |         17 |            5 |
| ASENCIO, CHARISSA MAEH PASCUA||08/19/1989                |          26 |         49 |            5 |
| BUENSALIDA, ANGELA CASTILLO||02/26/1995                  |          48 |         86 |            5 |
| FRANCISCO, PRECIOUS EVE BETITA||08/28/1994               |           4 |         25 |            5 |
| ALMIREZ, NIKKI CIARA SEVERINO||08/22/1995                |          26 |         52 |            5 |
| IGNACIO, KHAYLA MARIE CRISOSTOMO||6/3/1992               |          50 |         63 |            5 |
| GAUDIANO, JOSELLE LORRAINE ALMEDA||1/5/1993              |          11 |         43 |            5 |
| KORRA, VIVEKRAM||04/14/1996                              |          15 |         37 |            5 |
| KHATRI, FIROZ||01/16/1995                                |           1 |          5 |            5 |
<!-- truncated: true | shown: 200 | total: 33702 | full_csv: repeat_taker_detail_full.csv (download button in live dashboard, Tab 8) -->


---


## NMA_AppNo Deterministic Match Histories

| Metric | Value | Population | Note |
|---|---|---|---|
| Deterministically matched rows | 2,867 | PLE_MATCH_METHOD in MANUAL_APPNO_MATCH/DETERMINISTIC_APPNO | - |
Full record-level detail is available via CSV download in the live dashboard; not dumped inline here per export contract Rule 3.


---


# Tab 9 -- Subtests & Profiles


## Table 34 -- Standardized Subtest Means by University Type

<!-- chart_type: heatmap | x: subtest | y: UNDERGRAD_UNI_TYPE | series: none
     population: mean standardized score
     n: 133,477 | denominator: best-record uni subset
     source_tab: 9 | element_id: fig_t9_heatmap_uni -->

| UNDERGRAD_UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:---------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Foreign              |   478.75 |      505.58 |         512.25 |       489.33 |     499.4 |     512.8 |    479.1 |      506.07 |
| Private              |   484.74 |      500.32 |         498.91 |       498.96 |    489.61 |    498.09 |   490.48 |       491.4 |
| Public               |    495.8 |       513.2 |         517.49 |       507.63 |    511.66 |    519.09 |   502.65 |      514.03 |

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
| Private              |   484.74 |      500.32 |         498.91 |       498.96 |    489.61 |    498.09 |   490.48 |       491.4 |
| Public               |    495.8 |       513.2 |         517.49 |       507.63 |    511.66 |    519.09 |   502.65 |      514.03 |

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
| Confirmed passers (with year gap) | 29,519 | observable, confirmed, PLE_YEAR_GAP notna | - |
| Median year gap | 6.0 | rows above | - |
| Q1 year gap | 6.0 | rows above | - |
| Q3 year gap | 7.0 | rows above | - |

## PLE Year-Gap Distribution

<!-- chart_type: histogram | x: PLE_YEAR_GAP | y: Count | series: none
     population: confirmed observable passers with a year gap
     n: 29,519 | denominator: rows above
     source_tab: 10 | element_id: fig_t10_gap_hist -->

|   PLE_YEAR_GAP |   Count |
|---------------:|--------:|
|              5 |   3,424 |
|              6 |  14,777 |
|              7 |   7,563 |
|              8 |   2,366 |
|              9 |     832 |
|             10 |     321 |
|             11 |     138 |
|             12 |      65 |
|             13 |      24 |
|             14 |       5 |
|             15 |       4 |

---


## Box Summary: PLE Year Gap by Course Group

<!-- chart_type: box | x: UNDERGRAD_COURSE_GROUP | y: PLE_YEAR_GAP | series: none
     population: confirmed observable passers with a year gap
     n: 29,519 | denominator: rows above
     source_tab: 10 | element_id: fig_t10_gap_box -->

| UNDERGRAD_COURSE_GROUP       |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|:-----------------------------|-------:|------:|-----:|---------:|-----:|------:|-----------:|
| Education                    |  1,563 |     5 |    6 |        6 |    7 |    15 |         93 |
| Engineering & Technology     |    106 |     5 |    6 |        6 |    7 |    11 |          7 |
| Medical & Allied             | 16,776 |     5 |    6 |        6 |    7 |    14 |        696 |
| Natural Sciences             |  6,523 |     5 |    6 |        6 |    7 |    13 |        299 |
| Other                        |  2,962 |     5 |    6 |        6 |    7 |    15 |        208 |
| Social & Behavioral Sciences |  1,589 |     5 |    6 |        6 |    7 |    14 |         86 |

---


### Table 40 -- Year-Gap Summary by Course Group

| UNDERGRAD_COURSE_GROUP       |   confirmed_passers |   median_year_gap |   q25_year_gap |   q75_year_gap |   median_percentile |
|:-----------------------------|--------------------:|------------------:|---------------:|---------------:|--------------------:|
| Education                    |               1,563 |                 6 |              6 |              7 |                  65 |
| Engineering & Technology     |                 106 |                 6 |              6 |              7 |                  91 |
| Medical & Allied             |              16,776 |                 6 |              6 |              7 |                  63 |
| Natural Sciences             |               6,523 |                 6 |              6 |              7 |                  81 |
| Other                        |               2,962 |                 6 |              6 |              7 |                  68 |
| Social & Behavioral Sciences |               1,589 |                 6 |              6 |              7 |                  83 |

---


## Table 41 -- Score Summary by Sex

| SEX_CLEAN       |      n | median_raw   |   median_pct |   median_gps |
|:----------------|-------:|:-------------|-------------:|-------------:|
| (not specified) |     43 | -            |            0 |          200 |
| Female          | 74,753 | 122.00       |           50 |          502 |
| Male            | 60,073 | 121.00       |           49 |          500 |

---


## Box Summary: Percentile Rank by Sex

<!-- chart_type: box | x: SEX_CLEAN | y: NMS_PER_num | series: none
     population: best-record trend cohort, valid SEX_CLEAN
     n: 134,869 | denominator: sex_base
     source_tab: 10 | element_id: fig_t10_box_sex -->

| SEX_CLEAN       |      n |   min |   q1 |   median |   q3 |   max |   outliers |
|:----------------|-------:|------:|-----:|---------:|-----:|------:|-----------:|
| (not specified) |     42 |    -1 |    0 |        0 | 34.5 |    70 |          0 |
| Female          | 74,219 |    -1 |   23 |       50 |   76 |    99 |          0 |
| Male            | 59,432 |    -1 |   22 |       49 |   76 |    99 |          0 |

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
| (not specified) |                  20.93 |                    79.07 |
| Female          |                  45.03 |                    54.97 |
| Male            |                  46.08 |                    53.92 |

---


# Tab 11 -- Statistical Tests


## Table 43 -- Kruskal-Wallis Tests by Year

| Score              |       H | p_value   |   eta_squared |
|:-------------------|--------:|:----------|--------------:|
| Total raw score    | 6028.28 | <0.001    |          0.04 |
| Part I raw score   | 5766.34 | <0.001    |          0.04 |
| Part II raw score  | 5968.69 | <0.001    |          0.04 |
| Percentile rank    | 2432.24 | <0.001    |          0.02 |
| GPS standard score | 2592.55 | <0.001    |          0.02 |

---


## Table 44 -- Mann-Whitney by PLE Status

| Score              |      U_stat | p_value   |   effect_r |   Confirmed_median |   NoMatch_median |
|:-------------------|------------:|:----------|-----------:|-------------------:|-----------------:|
| Total raw score    | 8.63044e+08 | <0.001    |      -0.44 |                139 |              114 |
| Part I raw score   | 8.42159e+08 | <0.001    |      -0.41 |                 74 |               62 |
| Part II raw score  | 8.49698e+08 | <0.001    |      -0.42 |                 66 |               52 |
| Percentile rank    | 8.35619e+08 | <0.001    |      -0.43 |                 69 |               38 |
| GPS standard score | 8.58051e+08 | <0.001    |      -0.43 |                552 |              470 |

---


## Tables 45-47 -- Chi-Square: University Type x Bin

| UNDERGRAD_UNI_TYPE   |     B1 |    B2 |    B3 |     B4 |     B5 |     B6 |    B7 |    B8 |    B9 |    B10 |
|:---------------------|-------:|------:|------:|-------:|-------:|-------:|------:|------:|------:|-------:|
| Foreign              |    262 |   174 |   140 |    176 |    145 |    164 |   161 |   175 |   197 |    266 |
| Private              | 12,205 | 9,823 | 9,127 | 10,061 | 10,044 | 10,079 | 9,602 | 9,821 | 9,864 | 10,774 |
| Public               |  2,949 | 2,228 | 2,058 |  2,247 |  2,320 |  2,421 | 2,478 | 2,606 | 3,051 |  4,876 |
|    chi2 | p_value   |   degrees_of_freedom |   n_observations |   cramers_v |
|--------:|:----------|---------------------:|-----------------:|------------:|
| 1270.33 | <0.001    |                   18 |          130,494 |        0.07 |
| UNDERGRAD_UNI_TYPE   |      B1 |      B2 |      B3 |      B4 |      B5 |      B6 |      B7 |      B8 |      B9 |     B10 |
|:---------------------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Foreign              |  219.73 |  174.25 |  161.42 |  177.94 |   178.3 |  180.51 |  174.48 |  179.62 |  186.89 |  226.86 |
| Private              |   11979 |  9499.4 | 8800.06 | 9700.66 | 9720.08 | 9840.53 | 9511.84 | 9792.35 | 10188.6 | 12367.5 |
| Public               | 3217.31 | 2551.35 | 2363.52 |  2605.4 | 2610.62 | 2642.97 | 2554.69 | 2630.03 | 2736.46 | 3321.66 |

---


## University Type x Bin Row Percentages

<!-- chart_type: heatmap | x: PercentileBin | y: UNDERGRAD_UNI_TYPE | series: fig_t11_heatmap_chi
     population: row %
     n: best-record uni subset | denominator: 133,477
     source_tab: chi_base | element_id: 11 -->

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private              | 12.04 | 9.69 |    9 | 9.92 | 9.91 | 9.94 | 9.47 | 9.69 |  9.73 | 10.63 |
| Public               | 10.83 | 8.18 | 7.56 | 8.25 | 8.52 | 8.89 |  9.1 | 9.57 |  11.2 |  17.9 |

---


## Table 48 -- Dunn Post-Hoc Adjusted P-Values

|   index |   2006 |   2007 |   2008 |   2009 |   2010 |   2011 |   2012 |   2013 |   2014 |   2015 |   2016 |   2017 |   2018 |
|--------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|    2006 |      1 |      1 |      1 |      1 |      0 |      1 |      1 |      0 |      1 |      0 |      0 |      0 |      0 |
|    2007 |      1 |      1 |      1 |      1 |      0 |      1 |      1 |      0 |      1 |      0 |      0 |      0 |      0 |
|    2008 |      1 |      1 |      1 |      1 |      0 |      1 |      1 |   0.04 |      1 |      0 |      0 |      0 |      0 |
|    2009 |      1 |      1 |      1 |      1 |      0 |      1 |      1 |      0 |   0.41 |      0 |      0 |      0 |      0 |
|    2010 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|    2011 |      1 |      1 |      1 |      1 |      0 |      1 |      1 |      0 |      1 |      0 |      0 |      0 |      0 |
|    2012 |      1 |      1 |      1 |      1 |      0 |      1 |      1 |      0 |      1 |      0 |      0 |      0 |      0 |
|    2013 |      0 |      0 |   0.04 |      0 |      1 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|    2014 |      1 |      1 |      1 |   0.41 |      0 |      1 |      1 |      0 |      1 |      0 |      0 |      0 |      0 |
|    2015 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|    2016 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|    2017 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |   0.05 |
|    2018 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |   0.05 |      1 |

---


# Tab 12 -- Policy Tables & Export


## Table 1 -- Confirmed PLE Alignment by NMAT Year

|   Year |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|-------:|----------------------------:|------------------------:|-------------------------:|--------------------------:|
|  2,006 |                        3698 |                    2005 |                     1693 |                     54.22 |
|  2,007 |                        3690 |                    1832 |                     1858 |                     49.65 |
|  2,008 |                        4965 |                    2583 |                     2382 |                     52.02 |
|  2,009 |                        7461 |                    3757 |                     3704 |                     50.36 |
|  2,010 |                        8623 |                    4534 |                     4089 |                     52.58 |
|  2,011 |                        8842 |                    3918 |                     4924 |                     44.31 |
|  2,012 |                        9405 |                    4006 |                     5399 |                     42.59 |
|  2,013 |                        9867 |                    4210 |                     5657 |                     42.67 |
|  2,014 |                       12952 |                    4736 |                     8216 |                     36.57 |

## Table 2 -- Confirmed PLE Alignment by Pre-Med Background

| UNDERGRAD_COURSE_GROUP       |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Education                    |                        3188 |                    1699 |                     1489 |                     53.29 |                       53 |
| Other                        |                        6612 |                    3201 |                     3411 |                     48.41 |                       55 |
| Medical & Allied             |                       38144 |                   17833 |                    20311 |                     46.75 |                       48 |
| Natural Sciences             |                       16512 |                    6994 |                     9518 |                     42.36 |                       63 |
| Engineering & Technology     |                         318 |                     118 |                      200 |                     37.11 |                       71 |
| Social & Behavioral Sciences |                        4729 |                    1736 |                     2993 |                     36.71 |                       63 |

## Table 3 -- Confirmed PLE Alignment by University Type

| UNDERGRAD_UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:---------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Foreign              |                        1159 |                     258 |                      901 |                     22.26 |                       57 |
| Private              |                       52821 |                   23757 |                    29064 |                     44.98 |                       50 |
| Public               |                       14642 |                    7226 |                     7416 |                     49.35 |                       66 |

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
| All               | 30th percentile (B4+) |                                          49,623 |                     27,145 |                   54.7 |                  68 |
| All               | 40th percentile (B5+) |                                          43,150 |                     24,815 |                  57.51 |                  73 |
| Public            | 30th percentile (B4+) |                                          11,303 |                      6,505 |                  57.55 |                  78 |
| Public            | 40th percentile (B5+) |                                          10,261 |                      6,178 |                  60.21 |                  81 |
| Private           | 30th percentile (B4+) |                                          36,939 |                     20,130 |                   54.5 |                  65 |
| Private           | 40th percentile (B5+) |                                          31,666 |                     18,157 |                  57.34 |                  70 |
| Foreign           | 30th percentile (B4+) |                                             806 |                        222 |                  27.54 |                  73 |
| Foreign           | 40th percentile (B5+) |                                             719 |                        208 |                  28.93 |                  77 |

---


## Section B -- Foreign vs Filipino Applicant-Pool Composition

<!-- chart_type: stacked_bar | x: Group | y: PercentileBin | series: fig_t13_citz_stacked
     population: row %
     n: observable uni subset | denominator: 68,622
     source_tab: uniobservable | element_id: 13 -->

| Group     |      n |
|:----------|-------:|
| Filipino  | 63,431 |
| Foreigner |  5,191 |
| Group     |    B1 |    B2 |   B3 |   B4 |   B5 |   B6 |   B7 |    B8 |    B9 |   B10 |
|:----------|------:|------:|-----:|-----:|-----:|-----:|-----:|------:|------:|------:|
| Filipino  |  8.42 |  8.31 | 8.41 | 9.51 | 9.77 | 9.43 | 9.63 | 10.17 | 11.06 | 15.28 |
| Foreigner | 30.93 | 12.43 | 9.76 | 9.49 | 8.12 | 6.68 |  5.7 |  5.43 |   5.5 |  5.95 |

---


## Section C -- Individual-Level PLE Linkage Gradient by Percentile Bin

<!-- chart_type: bar | x: PercentileBin | y: linkage_rate_pct | series: none
     population: observable cohort
     n: 68,173 | denominator: observable best-record examinees with a valid bin
     source_tab: 13 | element_id: fig_t13_gradient -->

| PercentileBin   |     n |   linked_n |   linkage_rate_pct |
|:----------------|------:|-----------:|-------------------:|
| B1              | 6,853 |        795 |               11.6 |
| B2              | 5,884 |      1,336 |              22.71 |
| B3              | 5,813 |      1,703 |               29.3 |
| B4              | 6,473 |      2,330 |                 36 |
| B5              | 6,582 |      3,003 |              45.62 |
| B6              | 6,284 |      3,168 |              50.41 |
| B7              | 6,359 |      3,407 |              53.58 |
| B8              | 6,704 |      3,690 |              55.04 |
| B9              | 7,263 |      4,474 |               61.6 |
| B10             | 9,958 |      7,073 |              71.03 |
The gradient rises steadily from the lowest to the highest bin, with no sharp step at the 30th (B4) or 40th (B5) percentile threshold. 795 B1 (lowest-decile) examinees in the observable cohort are confirmed PLE passers -- a strictly binding 40th-percentile admission floor would predict this group should barely exist.


---


# Export Integrity

| check | result |
|---|---|
| Source parquet md5 | 28b85ac53af13b4a2ef3ee93527c97c1 |
| Rows / cols (source parquet on disk) | 178,927 / 53 |
| Derived columns added at load time | 5 (YEAR_INT, SEX_CLEAN, IS_BOARD_OBSERVABLE_COHORT, HAS_CONFIRMED_PLE, PLE_STATUS_LABEL) |
| Tabs exported | 13 / 13 |
| Charts exported as data | 59 / 59 |
| Tables exported | 102 |
| Captions/population notes exported | 23 |
| Dashboard-vs-export value assertions passed | 5 / 5 |