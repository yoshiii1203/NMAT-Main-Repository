# Page 12: Policy Tables

**Generated:** 2026-07-28 01:17

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subsets:** `bestobservable` (PLE-linked analyses, Year <= 2014) and `besttrend` (survival analysis, 2006-2018)

**Filters:** None (full unfiltered dataset)

---

## 1. PLE Alignment by Year

PLE status distribution across NMAT years for the observable best-record cohort (Year <= 2014).

**Table: PLE alignment by NMAT year**

|   Year |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|-------:|----------------------------:|------------------------:|-------------------------:|--------------------------:|
|   2006 |                        3665 |                    2038 |                     1627 |                     55.61 |
|   2007 |                        3660 |                    1868 |                     1792 |                     51.04 |
|   2008 |                        4849 |                    2514 |                     2335 |                     51.85 |
|   2009 |                        6881 |                    3226 |                     3655 |                     46.88 |
|   2010 |                        8008 |                    3808 |                     4200 |                     47.55 |
|   2011 |                        8731 |                    3853 |                     4878 |                     44.13 |
|   2012 |                        9145 |                    4066 |                     5079 |                     44.46 |
|   2013 |                        9121 |                    3951 |                     5170 |                     43.32 |
|   2014 |                       10441 |                    3949 |                     6492 |                     37.82 |

---
## 2. PLE Alignment by Course Group

PLE status and median percentile rank by course group (observable best-record cohort).

**Table: PLE alignment by CourseGroup**

| CourseGroup                  |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Education                    |                        2973 |                    1541 |                     1432 |                     51.83 |                       52 |
| Other                        |                        6189 |                    2853 |                     3336 |                      46.1 |                       55 |
| Natural Sciences             |                       15219 |                    6921 |                     8298 |                     45.48 |                       66 |
| Medical & Allied             |                       35433 |                   16061 |                    19372 |                     45.33 |                       49 |
| Social & Behavioral Sciences |                        4385 |                    1783 |                     2602 |                     40.66 |                       64 |
| Engineering & Technology     |                         302 |                     114 |                      188 |                     37.75 |                       71 |

---
## 3. PLE Alignment by University Type

PLE status and median percentile rank by university type (Public, Private, Foreign). Observable best-record cohort.

**Table: PLE alignment by UNI_TYPE**

| UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Foreign    |                        1124 |                     248 |                      876 |                     22.06 |                       58 |
| Private    |                       48991 |                   21909 |                    27082 |                     44.72 |                       51 |
| Public     |                       13555 |                    6786 |                     6769 |                     50.06 |                       68 |

---
## 4. Survival to Top Decile Bins (B8-B10) by Course Group

Proportion of examinees in each course group whose best-record percentile rank falls in the top three bins (B8 = 70th-79th, B9 = 80th-89th, B10 = 90th-99th).

**Table: Survival to top bins (B8-B10) by CourseGroup**

| CourseGroup                  |   total_examinees |   top_decile_n |   survival_rate_pct |
|:-----------------------------|------------------:|---------------:|--------------------:|
| Engineering & Technology     |               729 |            382 |                52.4 |
| Natural Sciences             |             40086 |          14660 |               36.57 |
| Other                        |              7885 |           2778 |               35.23 |
| Education                    |              3244 |           1086 |               33.48 |
| Medical & Allied             |             63067 |          18138 |               28.76 |
| Social & Behavioral Sciences |             15724 |           4456 |               28.34 |

---

*All PLE-linked analyses use the observable best-record cohort (Year <= 2014) to avoid misclassifying later cohorts as non-passers before their licensure window closes.*
