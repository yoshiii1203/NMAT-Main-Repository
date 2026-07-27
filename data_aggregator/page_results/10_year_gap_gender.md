# Page 10: Page 10: PLE Year Gap and Gender Patterns

**Generated:** 2026-07-28 01:17

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `besttrend / bestobservable`

**Filters:** None (full unfiltered dataset)

---

## 1. PLE Year Gap Distribution

- **Confirmed passers:** 27,245
- **Median year gap:** 6.0
- **Mean year gap:** 6.51
- **Std year gap:** 1.05
- **Min year gap:** 5.0
- **Max year gap:** 15.0
- **Q1 (25th pctile):** 6.0
- **Q3 (75th pctile):** 7.0
- **IQR:** 1.0

**Table 41. Full PLE year gap distribution**

|   PLE_YEAR_GAP |   Count |
|---------------:|--------:|
|              5 |    2308 |
|              6 |   14282 |
|              7 |    7160 |
|              8 |    2224 |
|              9 |     763 |
|             10 |     290 |
|             11 |     124 |
|             12 |      62 |
|             13 |      23 |
|             14 |       5 |
|             15 |       4 |

---

## 2. PLE Year Gap by CourseGroup

**Table 42. Year-gap summary by course group**

| CourseGroup                  |   confirmed_passers |   median_year_gap |   mean_year_gap |   std_year_gap |   q25_year_gap |   q75_year_gap |   min_year_gap |   max_year_gap |   median_percentile |
|:-----------------------------|--------------------:|------------------:|----------------:|---------------:|---------------:|---------------:|---------------:|---------------:|--------------------:|
| Education                    |                1410 |                 6 |            6.54 |            1.2 |              6 |              7 |              5 |             15 |                  69 |
| Engineering & Technology     |                 103 |                 6 |            6.58 |           1.12 |              6 |              7 |              5 |             11 |                  91 |
| Medical & Allied             |               15025 |                 6 |            6.45 |              1 |              6 |              7 |              5 |             14 |                  69 |
| Natural Sciences             |                6455 |                 6 |            6.59 |           0.99 |              6 |              7 |              5 |             13 |                  84 |
| Other                        |                2620 |                 6 |            6.61 |            1.3 |              6 |              7 |              5 |             15 |                  72 |
| Social & Behavioral Sciences |                1631 |                 6 |            6.56 |           1.02 |              6 |              7 |              5 |             14 |                  86 |

---

## 3. Gender Composition (Overall)

**Table 43. Gender composition (besttrend)**

| Sex    |   Count |   Percent |
|:-------|--------:|----------:|
| Female |   74153 |     55.43 |
| Male   |   59613 |     44.57 |

---

## 4. Gender by Year

**Table 44. Gender counts by NMAT year**

|   Year |   Male |   Female |
|-------:|-------:|---------:|
|   2006 |   1230 |     2435 |
|   2007 |   1350 |     2310 |
|   2008 |   1887 |     2962 |
|   2009 |   2643 |     4221 |
|   2010 |   4230 |     3776 |
|   2011 |   3917 |     4808 |
|   2012 |   3526 |     5609 |
|   2013 |   3433 |     5685 |
|   2014 |   4032 |     6409 |
|   2015 |   4378 |     6024 |
|   2016 |   5274 |     7335 |
|   2017 |   9586 |    14369 |
|   2018 |  14127 |     8210 |


**Table 45. Gender percentages by NMAT year**

|   Year |   Male |   Female |
|-------:|-------:|---------:|
|   2006 |  33.56 |    66.44 |
|   2007 |  36.89 |    63.11 |
|   2008 |  38.92 |    61.08 |
|   2009 |  38.51 |    61.49 |
|   2010 |  52.84 |    47.16 |
|   2011 |  44.89 |    55.11 |
|   2012 |   38.6 |     61.4 |
|   2013 |  37.65 |    62.35 |
|   2014 |  38.62 |    61.38 |
|   2015 |  42.09 |    57.91 |
|   2016 |  41.83 |    58.17 |
|   2017 |  40.02 |    59.98 |
|   2018 |  63.24 |    36.76 |

---

## 5. Gender Score Comparison

**Table 46. Score summary by sex**

| SEX_CLEAN   |     n |   median_raw |   mean_raw |   std_raw |   median_pct |   mean_pct |   std_pct |   median_gps |   median_apt |   median_sa |
|:------------|------:|-------------:|-----------:|----------:|-------------:|-----------:|----------:|-------------:|-------------:|------------:|
| Female      | 73970 |          122 |     123.13 |     32.76 |           50 |      49.44 |     30.08 |          500 |          504 |         497 |
| Male        | 59571 |          121 |     122.76 |     34.22 |           49 |      49.16 |     30.71 |          499 |          503 |         498 |

---

## 6. Mann-Whitney U Tests: Sex x NMS_PER_num and Key Scores

**Table 47. Mann-Whitney U tests: Sex differences in key scores**

| Score Variable                |   Median (Female) |   Median (Male) |   U-statistic | p-value   |   Effect size (r) |    N1 |    N2 |
|:------------------------------|------------------:|----------------:|--------------:|:----------|------------------:|------:|------:|
| Percentile Rank (NMS_PER_num) |                50 |              49 |   2.18068e+09 | 0.0958    |           -0.0053 | 73603 | 58942 |
| Total Raw Score               |               122 |             121 |   2.23247e+09 | 0.0015    |           -0.0101 | 74153 | 59613 |
| Part I Raw Score              |                65 |              64 |   2.26671e+09 | <0.001    |           -0.0255 | 74153 | 59613 |
| Part II Raw Score             |                57 |              57 |   2.19529e+09 | 0.0331    |            0.0068 | 74153 | 59613 |
| GPS Standard Score            |               500 |             499 |   2.21334e+09 | 0.6586    |           -0.0014 | 74153 | 59613 |
| APT Standard Score            |               504 |             503 |   2.25585e+09 | <0.001    |           -0.0206 | 74153 | 59613 |
| SA Standard Score             |               497 |             498 |   2.17683e+09 | <0.001    |            0.0151 | 74153 | 59613 |

---

## 7. Sex x PLE Status (Observable Cohort)

**Table 48. PLE status counts by sex (observable cohort)**

| SEX_CLEAN   |   Confirmed PLE passer |   No confirmed PLE match |
|:------------|-----------------------:|-------------------------:|
| Female      |                  17144 |                    21071 |
| Male        |                  12125 |                    14123 |


**Table 49. PLE status percentages by sex (observable cohort)**

| SEX_CLEAN   |   Confirmed PLE passer |   No confirmed PLE match |
|:------------|-----------------------:|-------------------------:|
| Female      |                  44.86 |                    55.14 |
| Male        |                  46.19 |                    53.81 |


**Table 50. Confirmed PLE pass rate by sex**

| SEX_CLEAN   |   total |   confirmed_passers |   pass_rate_pct |
|:------------|--------:|--------------------:|----------------:|
| Female      |   38215 |               17144 |           44.86 |
| Male        |   26248 |               12125 |           46.19 |


**Table 51. Chi-square test: Sex x PLE status**

|   Chi-square | p-value   |   df |     N |   Cramer's V |
|-------------:|:----------|-----:|------:|-------------:|
|       11.084 | <0.001    |    1 | 64463 |       0.0131 |

---

## 8. PLE Year Gap by Gender

**Table 52. PLE year gap summary by sex**

| SEX_CLEAN   |     n |   median_gap |   mean_gap |   std_gap |   min_gap |   max_gap |   q25_gap |   q75_gap |
|:------------|------:|-------------:|-----------:|----------:|----------:|----------:|----------:|----------:|
| Female      | 15790 |            6 |       6.48 |      1.02 |         5 |        15 |         6 |         7 |
| Male        | 11450 |            6 |       6.56 |      1.08 |         5 |        15 |         6 |         7 |


**Table 53. Mann-Whitney test: Sex differences in PLE year gap**

| Group 1   | Group 2   |   Median (Female) |   Median (Male) |   U-statistic | p-value   |   Effect size (r) |    N1 |    N2 |
|:----------|:----------|------------------:|----------------:|--------------:|:----------|------------------:|------:|------:|
| Female    | Male      |                 6 |               6 |   8.65287e+07 | <0.001    |            0.0429 | 15790 | 11451 |

---

