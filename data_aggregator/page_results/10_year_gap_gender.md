# Page 10: Page 10: PLE Year Gap and Gender Patterns

**Generated:** 2026-08-14 16:53

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

