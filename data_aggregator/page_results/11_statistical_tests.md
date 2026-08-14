# Page 11: Statistical Tests

**Generated:** 2026-08-14 18:07

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
| Percentile Rank    |           13 |    131845 |       2384.82 |         0 |         0.018 | Small         | ***    |
| GPS Standard Score |           13 |    134869 |       2592.55 |         0 |        0.0191 | Small         | ***    |

### 1b. University Type × Percentile Rank

Testing whether percentile rank distributions differ by university type (Public, Private, Foreign).

**Kruskal-Wallis: UNDERGRAD_UNI_TYPE × NMS_PER_num**

| Score Variable   |   Groups (k) |   Total N |   H-statistic |      p-value |   Eta-squared | Effect Size   | Sig.   |
|:-----------------|-------------:|----------:|--------------:|-------------:|--------------:|:--------------|:-------|
| Percentile Rank  |            3 |    130334 |       821.601 | 3.90526e-179 |        0.0063 | Negligible    | ***    |

### 1c. Course Group × Percentile Rank

Testing whether percentile rank distributions differ by UNDERGRAD_COURSE_GROUP.

**Kruskal-Wallis: UNDERGRAD_COURSE_GROUP × NMS_PER_num**

| Score Variable   |   Groups (k) |   Total N |   H-statistic |      p-value |   Eta-squared | Effect Size   | Sig.   |
|:-----------------|-------------:|----------:|--------------:|-------------:|--------------:|:--------------|:-------|
| Percentile Rank  |            6 |    131845 |       1138.93 | 4.95361e-244 |        0.0086 | Negligible    | ***    |

### 1d. University Location × Percentile Rank

Testing whether percentile rank distributions differ by university location (NCR vs Provincial).

**Kruskal-Wallis: UNDERGRAD_UNI_LOCATION × NMS_PER_num**

| Score Variable   |   Groups (k) |   Total N |   H-statistic |   p-value |   Eta-squared | Effect Size   | Sig.   |
|:-----------------|-------------:|----------:|--------------:|----------:|--------------:|:--------------|:-------|
| Percentile Rank  |            3 |    131845 |        8.4154 | 0.0148806 |             0 | Negligible    | *      |

---
## Section 2: Mann-Whitney U Tests

Two-sample non-parametric test for differences between independent groups. Effect size r (rank-biserial correlation): |r| ~ 0.1 small, ~0.3 medium, ~0.5 large.

---

### 2a. PLE Status × Score Variables

Comparing confirmed PLE passers vs no confirmed PLE match across score variables. Uses observable best-record cohort (Year <= 2014).

**Table 44. Mann-Whitney comparisons by PLE status (observable cohort)**

| Score Variable     |   Median (Confirmed PLE passer) |   Median (No confirmed PLE match) |   U-statistic |   p-value |   Effect size (r) |    N1 |    N2 | Sig.   |
|:-------------------|--------------------------------:|----------------------------------:|--------------:|----------:|------------------:|------:|------:|:-------|
| Total Raw Score    |                             140 |                               115 |   8.50769e+08 |         0 |           -0.4362 | 30104 | 39356 | ***    |
| Percentile Rank    |                              70 |                                39 |   8.12563e+08 |         0 |           -0.4244 | 29510 | 38663 | ***    |
| GPS Standard Score |                             553 |                               473 |   8.52438e+08 |         0 |           -0.4374 | 30105 | 39398 | ***    |
| Part I Raw Score   |                              74 |                                62 |   8.34193e+08 |         0 |           -0.4082 | 30104 | 39356 | ***    |
| Part II Raw Score  |                              66 |                                53 |   8.34468e+08 |         0 |           -0.4087 | 30104 | 39356 | ***    |

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
| Private              | 12248 | 10784 | 9857 | 9151 | 10082 | 10058 | 10104 | 9622 | 9833 | 9876 |
| Public               |  2874 |  4854 | 2176 | 2016 |  2209 |  2288 |  2385 | 2442 | 2586 | 3029 |

**Table 46. Chi-square summary — University type × Percentile bin**

|    chi2 |      p_value |   dof |   Cramer's V |      n | Sig.   |
|--------:|-------------:|------:|-------------:|-------:|:-------|
| 1327.86 | 4.32187e-271 |    18 |       0.0714 | 130334 | ***    |

**Table 47. Expected counts (under independence)**

| UNDERGRAD_UNI_TYPE   |      B1 |     B10 |      B2 |      B3 |      B4 |      B5 |      B6 |      B7 |      B8 |      B9 |
|:---------------------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Foreign              | 219.545 | 226.966 | 174.206 | 161.362 | 177.917 | 178.259 | 180.571 | 174.463 | 179.729 | 186.979 |
| Private              | 11994.1 | 12399.6 |  9517.2 | 8815.51 | 9719.91 | 9738.62 | 9864.92 | 9531.23 | 9818.92 |   10215 |
| Public               | 3170.31 | 3277.47 |  2515.6 | 2330.13 | 2569.18 | 2574.12 | 2607.51 | 2519.31 | 2595.35 | 2700.04 |

**Row percentages (university type × bin)**

| UNDERGRAD_UNI_TYPE   |    B1 |   B10 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |
|:---------------------|------:|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| Foreign              | 14.09 |  14.3 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |
| Private              | 12.05 | 10.61 |  9.7 | 9.01 | 9.92 |  9.9 | 9.94 | 9.47 | 9.68 |  9.72 |
| Public               |  10.7 | 18.07 |  8.1 | 7.51 | 8.22 | 8.52 | 8.88 | 9.09 | 9.63 | 11.28 |

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

|         |     Foreign |      Private |       Public |
|:--------|------------:|-------------:|-------------:|
| Foreign |           1 |    0.0956645 |  3.03824e-09 |
| Private |   0.0956645 |            1 | 3.51438e-180 |
| Public  | 3.03824e-09 | 3.51438e-180 |            1 |

**Table 48. Dunn post-hoc pairwise summary — UNDERGRAD_UNI_TYPE**

| Group 1   | Group 2   |   Adjusted p-value | Significant   |
|:----------|:----------|-------------------:|:--------------|
| Foreign   | Private   |          0.0956645 | False         |
| Foreign   | Public    |        3.03824e-09 | True          |
| Private   | Public    |       3.51438e-180 | True          |

### 4b. Course Group — Pairwise (Dunn + Bonferroni)

Pairwise comparisons of percentile rank across course groups.

**Dunn post-hoc adjusted p-value matrix (Bonferroni) — UNDERGRAD_COURSE_GROUP × NMS_PER_num**

|                              |   Education |   Engineering & Technology |   Medical & Allied |   Natural Sciences |       Other |   Social & Behavioral Sciences |
|:-----------------------------|------------:|---------------------------:|-------------------:|-------------------:|------------:|-------------------------------:|
| Education                    |           1 |                7.29653e-22 |        1.77906e-07 |                  1 |           1 |                    6.69101e-40 |
| Engineering & Technology     | 7.29653e-22 |                          1 |        2.37994e-40 |        1.23642e-23 | 2.57532e-22 |                    6.37048e-66 |
| Medical & Allied             | 1.77906e-07 |                2.37994e-40 |                  1 |        8.27369e-76 | 2.84836e-22 |                    8.32413e-65 |
| Natural Sciences             |           1 |                1.23642e-23 |        8.27369e-76 |                  1 |           1 |                   9.43943e-182 |
| Other                        |           1 |                2.57532e-22 |        2.84836e-22 |                  1 |           1 |                    2.47389e-86 |
| Social & Behavioral Sciences | 6.69101e-40 |                6.37048e-66 |        8.32413e-65 |       9.43943e-182 | 2.47389e-86 |                              1 |

**Dunn post-hoc pairwise summary — UNDERGRAD_COURSE_GROUP**

| Group 1                  | Group 2                      |   Adjusted p-value | Significant   |
|:-------------------------|:-----------------------------|-------------------:|:--------------|
| Education                | Engineering & Technology     |        7.29653e-22 | True          |
| Education                | Medical & Allied             |        1.77906e-07 | True          |
| Education                | Natural Sciences             |                  1 | False         |
| Education                | Other                        |                  1 | False         |
| Education                | Social & Behavioral Sciences |        6.69101e-40 | True          |
| Engineering & Technology | Medical & Allied             |        2.37994e-40 | True          |
| Engineering & Technology | Natural Sciences             |        1.23642e-23 | True          |
| Engineering & Technology | Other                        |        2.57532e-22 | True          |
| Engineering & Technology | Social & Behavioral Sciences |        6.37048e-66 | True          |
| Medical & Allied         | Natural Sciences             |        8.27369e-76 | True          |
| Medical & Allied         | Other                        |        2.84836e-22 | True          |
| Medical & Allied         | Social & Behavioral Sciences |        8.32413e-65 | True          |
| Natural Sciences         | Other                        |                  1 | False         |
| Natural Sciences         | Social & Behavioral Sciences |       9.43943e-182 | True          |
| Other                    | Social & Behavioral Sciences |        2.47389e-86 | True          |

### 4c. Year — Pairwise (Dunn + Bonferroni)

Pairwise comparisons of percentile rank across NMAT years (2006-2018).

**Dunn post-hoc adjusted p-value matrix (Bonferroni) — Year × NMS_PER_num**

|      |        2006 |        2007 |        2008 |        2009 |         2010 |        2011 |         2012 |         2013 |         2014 |        2015 |        2016 |         2017 |         2018 |
|-----:|------------:|------------:|------------:|------------:|-------------:|------------:|-------------:|-------------:|-------------:|------------:|------------:|-------------:|-------------:|
| 2006 |           1 |           1 |           1 |           1 |  1.44464e-08 |           1 |            1 |  6.69815e-08 |   0.00728792 |           1 | 1.28102e-13 |  1.49125e-33 |  1.71296e-40 |
| 2007 |           1 |           1 |           1 |           1 |  1.03369e-09 |           1 |            1 |  5.19589e-09 |   0.00126682 |           1 | 3.67987e-12 |  4.14043e-31 |    8.162e-38 |
| 2008 |           1 |           1 |           1 |           1 |  5.89994e-06 |           1 |            1 |  2.50214e-05 |     0.666946 |    0.140068 | 1.36558e-24 |  1.21332e-55 |  2.07478e-65 |
| 2009 |           1 |           1 |           1 |           1 |  7.88569e-17 |           1 |      0.17042 |  9.01284e-16 |  3.54237e-07 |           1 | 2.59268e-18 |  3.24281e-52 |  2.82651e-63 |
| 2010 | 1.44464e-08 | 1.03369e-09 | 5.89994e-06 | 7.88569e-17 |            1 | 1.44684e-14 |  1.05856e-07 |            1 |    0.0486703 | 2.43395e-22 | 6.26442e-83 | 2.44748e-163 | 9.31461e-182 |
| 2011 |           1 |           1 |           1 |           1 |  1.44684e-14 |           1 |            1 |  1.55515e-13 |  2.34209e-05 |           1 | 1.10637e-24 |  5.32592e-67 |  6.34811e-80 |
| 2012 |           1 |           1 |           1 |     0.17042 |  1.05856e-07 |           1 |            1 |   6.7278e-07 |     0.342854 |  0.00506479 | 1.34229e-37 |  1.55364e-90 | 2.86138e-105 |
| 2013 | 6.69815e-08 | 5.19589e-09 | 2.50214e-05 | 9.01284e-16 |            1 | 1.55515e-13 |   6.7278e-07 |            1 |     0.156005 | 4.27194e-21 | 4.93249e-81 | 1.87255e-161 | 6.26878e-180 |
| 2014 |  0.00728792 |  0.00126682 |    0.666946 | 3.54237e-07 |    0.0486703 | 2.34209e-05 |     0.342854 |     0.156005 |            1 | 1.48471e-10 | 1.15262e-60 |  7.6198e-134 | 1.02211e-151 |
| 2015 |           1 |           1 |    0.140068 |           1 |  2.43395e-22 |           1 |   0.00506479 |  4.27194e-21 |  1.48471e-10 |           1 | 2.83492e-18 |    2.311e-57 |  5.82817e-70 |
| 2016 | 1.28102e-13 | 3.67987e-12 | 1.36558e-24 | 2.59268e-18 |  6.26442e-83 | 1.10637e-24 |  1.34229e-37 |  4.93249e-81 |  1.15262e-60 | 2.83492e-18 |           1 |  2.31916e-08 |  1.33343e-14 |
| 2017 | 1.49125e-33 | 4.14043e-31 | 1.21332e-55 | 3.24281e-52 | 2.44748e-163 | 5.32592e-67 |  1.55364e-90 | 1.87255e-161 |  7.6198e-134 |   2.311e-57 | 2.31916e-08 |            1 |            1 |
| 2018 | 1.71296e-40 |   8.162e-38 | 2.07478e-65 | 2.82651e-63 | 9.31461e-182 | 6.34811e-80 | 2.86138e-105 | 6.26878e-180 | 1.02211e-151 | 5.82817e-70 | 1.33343e-14 |            1 |            1 |

---

*Significance codes: *** p<0.001, ** p<0.01, * p<0.05, ns not significant*
