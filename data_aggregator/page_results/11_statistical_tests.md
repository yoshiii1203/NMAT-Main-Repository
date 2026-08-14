# Page 11: Statistical Tests

**Generated:** 2026-08-14 17:29

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
