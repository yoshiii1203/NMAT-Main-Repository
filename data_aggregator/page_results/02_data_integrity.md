# Page 2: Data Integrity and Cohort Definition Checks

**Generated:** 2026-07-28 01:17

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `all` (full unfiltered dataset) and derived analytic subsets

**Filters:** None (full unfiltered dataset)

---

## Metric Cards

| Metric | Value |
|--------|------:|
| All NMAT rows | 178,927 |
| Best-record rows | 133,804 |
| Rows with TRUE raw scores | 178,882 |
| Observable best-record rows | 64,501 |

---

## Table 2: Analysis Cohorts Used in the Dashboard

Each row defines one analytic subset used in later pages. Counts are rows, not necessarily unique persons.

| Analytic subset                               |   Row count | Interpretation                                |   Share of all (%) |
|:----------------------------------------------|------------:|:----------------------------------------------|-------------------:|
| All cleaned NMAT rows                         |      178927 | All cleaned NMAT rows                         |                100 |
| One best NMAT record per person               |      133804 | One best NMAT record per person               |              74.78 |
| Best-record rows within 2006-2018             |      133804 | Best-record rows within 2006-2018             |              74.78 |
| Best-record rows in the observable PLE window |       64501 | Best-record rows in the observable PLE window |              36.05 |
| Confirmed PLE-matched NMAT rows               |       49986 | Confirmed PLE-matched NMAT rows               |              27.94 |
| Confirmed PLE-matched best-record persons     |       36305 | Confirmed PLE-matched best-record persons     |              20.29 |

---

## Table 3: TRUE Raw-Score Validation Checks

These checks confirm whether TRUE total raw score is internally consistent with its Part I and Part II components.

| Validation check                              |   Count of rows |   Share of total rows (%) |
|:----------------------------------------------|----------------:|--------------------------:|
| Rows with complete Total + Part I + Part II   |          178882 |                   99.9749 |
| Formula mismatches: Total != Part I + Part II |               0 |                         0 |
| Stored-vs-derived mismatch flag count         |           56065 |                    31.334 |
| Calc-vs-derived mismatch flag count           |               0 |                         0 |

### StoredVsDerivedMismatch detailed distribution

|   Value |   Count |
|--------:|--------:|
|     nan |   79611 |
|       1 |   56065 |
|       0 |   43251 |

### CalcVsDerivedMismatch detailed distribution

|   Value |   Count |
|--------:|--------:|
|       0 |  178882 |
|     nan |      45 |

---

## Table 4: Post-Cleaning UNI_TYPE Consistency by Source College

Each row summarizes how one normalized source college name maps to the cleaned UNI_TYPE field. Any college with more than one mapped type should be reviewed.

**Colleges checked:** 3,213

**Colleges with >1 UNI_TYPE:** 0

### All inconsistent colleges

| NMA_College_norm   | records   | n_types   | mapped_types   |
|--------------------|-----------|-----------|----------------|

**Colleges with exactly 1 UNI_TYPE:** 3,213

---

## Table 5: UNIVERSITY to UNI_TYPE and UNI_LOCATION Pairing Audit

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

| UNI_TYPE      |   Count |   Share (%) |
|:--------------|--------:|------------:|
| Private       |  137476 |       76.83 |
| Public        |   37304 |       20.85 |
| Foreign       |    2315 |        1.29 |
| Not Specified |    1832 |        1.02 |

### Table 7: Distribution of Course Group (all rows)

| CourseGroup                  |   Count |   Share (%) |
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
| No confirmed PLE match |  128941 |       72.06 |
| Confirmed PLE passer   |   49986 |       27.94 |

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

### IS_PLE_ANALYSIS_SAFE Distribution

| IS_PLE_ANALYSIS_SAFE   |   Count |   Share (%) |
|:-----------------------|--------:|------------:|
| False                  |  128941 |       72.06 |
| True                   |   49986 |       27.94 |
