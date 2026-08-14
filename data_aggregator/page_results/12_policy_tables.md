# Page 12: Policy Tables

**Generated:** 2026-08-14 18:07

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subsets:** `bestobservable` (PLE-linked analyses, Year <= 2014) and `besttrend` (survival analysis, 2006-2018)

**Filters:** None (full unfiltered dataset)

---

## 1. PLE Alignment by Year

PLE status distribution across NMAT years for the observable best-record cohort (Year <= 2014).

**Table: PLE alignment by NMAT year**

|   Year |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|-------:|----------------------------:|------------------------:|-------------------------:|--------------------------:|
|   2006 |                        3698 |                    1973 |                     1725 |                     53.35 |
|   2007 |                        3690 |                    1784 |                     1906 |                     48.35 |
|   2008 |                        4965 |                    2438 |                     2527 |                      49.1 |
|   2009 |                        7461 |                    3054 |                     4407 |                     40.93 |
|   2010 |                        8623 |                    4070 |                     4553 |                      47.2 |
|   2011 |                        8842 |                    3889 |                     4953 |                     43.98 |
|   2012 |                        9405 |                    3979 |                     5426 |                     42.31 |
|   2013 |                        9867 |                    4188 |                     5679 |                     42.44 |
|   2014 |                       12952 |                    4730 |                     8222 |                     36.52 |

---
## 2. PLE Alignment by Course Group

PLE status and median percentile rank by course group (observable best-record cohort).

**Table: PLE alignment by UNDERGRAD_COURSE_GROUP**

| UNDERGRAD_COURSE_GROUP       |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Education                    |                        3188 |                    1452 |                     1736 |                     45.55 |                       53 |
| Medical & Allied             |                       38144 |                   17240 |                    20904 |                      45.2 |                       49 |
| Other                        |                        6612 |                    2756 |                     3856 |                     41.68 |                       55 |
| Natural Sciences             |                       16512 |                    6849 |                     9663 |                     41.48 |                       64 |
| Engineering & Technology     |                         318 |                     116 |                      202 |                     36.48 |                       71 |
| Social & Behavioral Sciences |                        4729 |                    1692 |                     3037 |                     35.78 |                       63 |

---
## 3. PLE Alignment by University Type

PLE status and median percentile rank by university type (Public, Private, Foreign). Observable best-record cohort.

**Table: PLE alignment by UNDERGRAD_UNI_TYPE**

| UNDERGRAD_UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:---------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Foreign              |                        1159 |                     252 |                      907 |                     21.74 |                       57 |
| Private              |                       53037 |                   22712 |                    30325 |                     42.82 |                       50 |
| Public               |                       14263 |                    6757 |                     7506 |                     47.37 |                       68 |

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
