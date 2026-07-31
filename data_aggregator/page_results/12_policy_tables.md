# Page 12: Policy Tables

**Generated:** 2026-07-31 16:30

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
