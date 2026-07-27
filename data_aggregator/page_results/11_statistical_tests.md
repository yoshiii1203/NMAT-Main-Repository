# Page 11: Statistical Tests

**Generated:** 2026-07-28 01:17

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
| Total Raw Score    |           13 |    133766 |        5598.2 |         0 |        0.0418 | Small         | ***    |
| Part I Raw Score   |           13 |    133766 |       5453.44 |         0 |        0.0407 | Small         | ***    |
| Part II Raw Score  |           13 |    133766 |       5515.99 |         0 |        0.0412 | Small         | ***    |
| Percentile Rank    |           13 |    132582 |       2226.02 |         0 |        0.0167 | Small         | ***    |
| GPS Standard Score |           13 |    133804 |       2411.01 |         0 |        0.0179 | Small         | ***    |

### 1b. University Type × Percentile Rank

Testing whether percentile rank distributions differ by university type (Public, Private, Foreign).

**Kruskal-Wallis: UNI_TYPE × NMS_PER_num**

| Score Variable   |   Groups (k) |   Total N |   H-statistic |      p-value |   Eta-squared | Effect Size   | Sig.   |
|:-----------------|-------------:|----------:|--------------:|-------------:|--------------:|:--------------|:-------|
| Percentile Rank  |            3 |    131201 |       689.465 | 1.92552e-150 |        0.0052 | Negligible    | ***    |

### 1c. Course Group × Percentile Rank

Testing whether percentile rank distributions differ by CourseGroup.

**Kruskal-Wallis: CourseGroup × NMS_PER_num**

| Score Variable   |   Groups (k) |   Total N |   H-statistic |      p-value |   Eta-squared | Effect Size   | Sig.   |
|:-----------------|-------------:|----------:|--------------:|-------------:|--------------:|:--------------|:-------|
| Percentile Rank  |            6 |    132582 |       1279.83 | 1.49569e-274 |        0.0096 | Negligible    | ***    |

### 1d. University Location × Percentile Rank

Testing whether percentile rank distributions differ by university location (NCR vs Provincial).

**Kruskal-Wallis: UNI_LOCATION × NMS_PER_num**

| Score Variable   |   Groups (k) |   Total N |   H-statistic |   p-value |   Eta-squared | Effect Size   | Sig.   |
|:-----------------|-------------:|----------:|--------------:|----------:|--------------:|:--------------|:-------|
| Percentile Rank  |            3 |    132582 |        3.8005 |   0.14953 |             0 | Negligible    | ns     |

---
## Section 2: Mann-Whitney U Tests

Two-sample non-parametric test for differences between independent groups. Effect size r (rank-biserial correlation): |r| ~ 0.1 small, ~0.3 medium, ~0.5 large.

---

### 2a. PLE Status × Score Variables

Comparing confirmed PLE passers vs no confirmed PLE match across score variables. Uses observable best-record cohort (Year <= 2014).

**Table 44. Mann-Whitney comparisons by PLE status (observable cohort)**

| Score Variable     |   Median (Confirmed PLE passer) |   Median (No confirmed PLE match) |   U-statistic |   p-value |   Effect size (r) |    N1 |    N2 | Sig.   |
|:-------------------|--------------------------------:|----------------------------------:|--------------:|----------:|------------------:|------:|------:|:-------|
| Total Raw Score    |                             143 |                               112 |   7.94198e+08 |         0 |            -0.542 | 29269 | 35194 | ***    |
| Percentile Rank    |                              73 |                                36 |   7.73256e+08 |         0 |           -0.5392 | 28646 | 35075 | ***    |
| GPS Standard Score |                             564 |                               464 |   7.95288e+08 |         0 |           -0.5424 | 29273 | 35228 | ***    |
| Part I Raw Score   |                              76 |                                61 |   7.74202e+08 |         0 |           -0.5032 | 29269 | 35194 | ***    |
| Part II Raw Score  |                              68 |                                51 |    7.7629e+08 |         0 |           -0.5072 | 29269 | 35194 | ***    |

### 2b. Sex × Percentile Rank

Comparing percentile rank distributions by sex.

SEX_CLEAN column not available in dataset.

---
## Section 3: Chi-Square Tests of Independence

Tests whether two categorical variables are independent. Cramer's V measures association strength (0-1).

---

### 3a. University Type × Percentile Bin

Testing independence between university type and percentile bin classification. H0: UNI_TYPE and PercentileBin are independent.

**Table 45. Observed counts — University type × Percentile bin**

| UNI_TYPE   |    B1 |   B10 |   B2 |   B3 |   B4 |    B5 |   B6 |   B7 |   B8 |   B9 |
|:-----------|------:|------:|-----:|-----:|-----:|------:|-----:|-----:|-----:|-----:|
| Foreign    |   262 |   263 |  175 |  140 |  176 |   147 |  164 |  160 |  178 |  197 |
| Private    | 12208 | 10701 | 9806 | 9066 | 9958 | 10007 | 9934 | 9458 | 9716 | 9730 |
| Public     |  2948 |  4763 | 2230 | 2050 | 2227 |  2339 | 2406 | 2444 | 2573 | 2957 |

**Table 46. Chi-square summary — University type × Percentile bin**

|    chi2 |     p_value |   dof |   Cramer's V |      n | Sig.   |
|--------:|------------:|------:|-------------:|-------:|:-------|
| 1168.14 | 7.4919e-237 |    18 |       0.0672 | 129383 | ***    |

**Table 47. Expected counts (under independence)**

| UNI_TYPE   |      B1 |     B10 |      B2 |      B3 |      B4 |      B5 |      B6 |      B7 |      B8 |      B9 |
|:-----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Foreign    | 221.886 | 226.333 | 175.733 | 161.989 | 177.892 | 179.792 |  179.95 | 173.589 | 179.417 | 185.419 |
| Private    | 11986.2 | 12226.4 | 9492.99 | 8750.56 |  9609.6 | 9712.22 | 9720.77 | 9377.15 | 9692.01 | 10016.2 |
| Public     | 3209.96 |  3274.3 | 2542.28 | 2343.45 | 2573.51 | 2600.99 | 2603.28 | 2511.26 | 2595.58 | 2682.39 |

**Row percentages (university type × bin)**

| UNI_TYPE   |    B1 |   B10 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |
|:-----------|------:|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| Foreign    | 14.07 | 14.12 |  9.4 | 7.52 | 9.45 | 7.89 | 8.81 | 8.59 | 9.56 | 10.58 |
| Private    | 12.14 | 10.64 | 9.75 | 9.01 |  9.9 | 9.95 | 9.88 |  9.4 | 9.66 |  9.67 |
| Public     | 10.94 | 17.68 | 8.28 | 7.61 | 8.27 | 8.68 | 8.93 | 9.07 | 9.55 | 10.98 |

### 3b. Course Group × Percentile Bin

Testing independence between course group and percentile bin classification.

**Observed counts — CourseGroup × Percentile bin**

| CourseGroup                  |   B1 |   B10 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |   B9 |
|:-----------------------------|-----:|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
| Education                    |  312 |   451 |  300 |  310 |  313 |  339 |  286 |  298 |  306 |  329 |
| Engineering & Technology     |   38 |   202 |   43 |   43 |   41 |   63 |   64 |   55 |   73 |  107 |
| Medical & Allied             | 6350 |  6116 | 6180 | 5960 | 6713 | 6885 | 6697 | 6144 | 6159 | 5863 |
| Natural Sciences             | 4946 |  6263 | 3431 | 3022 | 3345 | 3374 | 3520 | 3788 | 3993 | 4404 |
| Other                        |  802 |  1047 |  683 |  671 |  734 |  752 |  744 |  721 |  824 |  907 |
| Social & Behavioral Sciences | 3137 |  1818 | 1737 | 1361 | 1319 | 1234 | 1306 | 1174 | 1243 | 1395 |

**Chi-square summary — CourseGroup × Percentile bin**

|    chi2 |   p_value |   dof |   Cramer's V |      n | Sig.   |
|--------:|----------:|------:|-------------:|-------:|:-------|
| 2969.14 |         0 |    45 |       0.0674 | 130735 | ***    |

**Expected counts (under independence) — CourseGroup × Percentile bin**

| CourseGroup                  |      B1 |     B10 |      B2 |      B3 |      B4 |      B5 |      B6 |      B7 |      B8 |      B9 |
|:-----------------------------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Education                    | 386.719 | 394.461 | 307.043 | 282.056 | 309.301 | 313.817 | 313.073 | 302.229 | 312.601 |   322.7 |
| Engineering & Technology     | 86.9045 | 88.6443 | 68.9995 | 63.3843 | 69.5069 | 70.5218 | 70.3545 | 67.9177 | 70.2485 |  72.518 |
| Medical & Allied             | 7518.26 | 7668.77 | 5969.26 | 5483.48 | 6013.16 | 6100.95 | 6086.48 | 5875.67 | 6077.32 | 6273.66 |
| Natural Sciences             | 4778.68 | 4874.34 | 3794.12 | 3485.35 | 3822.02 | 3877.83 | 3868.63 | 3734.63 |  3862.8 |  3987.6 |
| Other                        | 939.976 | 958.793 | 746.311 | 685.576 |   751.8 | 762.777 | 760.967 |  734.61 | 759.821 | 784.369 |
| Social & Behavioral Sciences | 1874.47 | 1911.99 | 1488.27 | 1367.15 | 1499.21 |  1521.1 | 1517.49 | 1464.94 | 1515.21 | 1564.16 |

**Row percentages (CourseGroup × bin)**

| CourseGroup                  |    B1 |   B10 |    B2 |   B3 |    B4 |    B5 |    B6 |   B7 |    B8 |    B9 |
|:-----------------------------|------:|------:|------:|-----:|------:|------:|------:|-----:|------:|------:|
| Education                    |  9.62 |  13.9 |  9.25 | 9.56 |  9.65 | 10.45 |  8.82 | 9.19 |  9.43 | 10.14 |
| Engineering & Technology     |  5.21 | 27.71 |   5.9 |  5.9 |  5.62 |  8.64 |  8.78 | 7.54 | 10.01 | 14.68 |
| Medical & Allied             | 10.07 |   9.7 |   9.8 | 9.45 | 10.64 | 10.92 | 10.62 | 9.74 |  9.77 |   9.3 |
| Natural Sciences             | 12.34 | 15.62 |  8.56 | 7.54 |  8.34 |  8.42 |  8.78 | 9.45 |  9.96 | 10.99 |
| Other                        | 10.17 | 13.28 |  8.66 | 8.51 |  9.31 |  9.54 |  9.44 | 9.14 | 10.45 |  11.5 |
| Social & Behavioral Sciences | 19.95 | 11.56 | 11.05 | 8.66 |  8.39 |  7.85 |  8.31 | 7.47 |  7.91 |  8.87 |

---
## Section 4: Dunn Post-Hoc Pairwise Comparisons

Bonferroni-adjusted pairwise comparisons following significant Kruskal-Wallis results.

---
### 4a. University Type — Pairwise (Dunn + Bonferroni)

Pairwise comparisons of percentile rank across university types.

**Dunn post-hoc adjusted p-value matrix (Bonferroni) — UNI_TYPE × NMS_PER_num**

|         |     Foreign |      Private |       Public |
|:--------|------------:|-------------:|-------------:|
| Foreign |           1 |    0.0555481 |  5.75976e-07 |
| Private |   0.0555481 |            1 | 2.29541e-151 |
| Public  | 5.75976e-07 | 2.29541e-151 |            1 |

**Table 48. Dunn post-hoc pairwise summary — UNI_TYPE**

| Group 1   | Group 2   |   Adjusted p-value | Significant   |
|:----------|:----------|-------------------:|:--------------|
| Foreign   | Private   |          0.0555481 | False         |
| Foreign   | Public    |        5.75976e-07 | True          |
| Private   | Public    |       2.29541e-151 | True          |

### 4b. Course Group — Pairwise (Dunn + Bonferroni)

Pairwise comparisons of percentile rank across course groups.

**Dunn post-hoc adjusted p-value matrix (Bonferroni) — CourseGroup × NMS_PER_num**

|                              |   Education |   Engineering & Technology |   Medical & Allied |   Natural Sciences |        Other |   Social & Behavioral Sciences |
|:-----------------------------|------------:|---------------------------:|-------------------:|-------------------:|-------------:|-------------------------------:|
| Education                    |           1 |                2.68409e-23 |        2.51774e-05 |                  1 |            1 |                    1.48445e-49 |
| Engineering & Technology     | 2.68409e-23 |                          1 |         1.3385e-40 |         4.6107e-27 |  6.63952e-24 |                    2.01125e-76 |
| Medical & Allied             | 2.51774e-05 |                 1.3385e-40 |                  1 |        4.63659e-47 |  3.61185e-17 |                   1.69775e-115 |
| Natural Sciences             |           1 |                 4.6107e-27 |        4.63659e-47 |                  1 |            1 |                   2.65071e-220 |
| Other                        |           1 |                6.63952e-24 |        3.61185e-17 |                  1 |            1 |                   3.14603e-109 |
| Social & Behavioral Sciences | 1.48445e-49 |                2.01125e-76 |       1.69775e-115 |       2.65071e-220 | 3.14603e-109 |                              1 |

**Dunn post-hoc pairwise summary — CourseGroup**

| Group 1                  | Group 2                      |   Adjusted p-value | Significant   |
|:-------------------------|:-----------------------------|-------------------:|:--------------|
| Education                | Engineering & Technology     |        2.68409e-23 | True          |
| Education                | Medical & Allied             |        2.51774e-05 | True          |
| Education                | Natural Sciences             |                  1 | False         |
| Education                | Other                        |                  1 | False         |
| Education                | Social & Behavioral Sciences |        1.48445e-49 | True          |
| Engineering & Technology | Medical & Allied             |         1.3385e-40 | True          |
| Engineering & Technology | Natural Sciences             |         4.6107e-27 | True          |
| Engineering & Technology | Other                        |        6.63952e-24 | True          |
| Engineering & Technology | Social & Behavioral Sciences |        2.01125e-76 | True          |
| Medical & Allied         | Natural Sciences             |        4.63659e-47 | True          |
| Medical & Allied         | Other                        |        3.61185e-17 | True          |
| Medical & Allied         | Social & Behavioral Sciences |       1.69775e-115 | True          |
| Natural Sciences         | Other                        |                  1 | False         |
| Natural Sciences         | Social & Behavioral Sciences |       2.65071e-220 | True          |
| Other                    | Social & Behavioral Sciences |       3.14603e-109 | True          |

### 4c. Year — Pairwise (Dunn + Bonferroni)

Pairwise comparisons of percentile rank across NMAT years (2006-2018).

**Dunn post-hoc adjusted p-value matrix (Bonferroni) — Year × NMS_PER_num**

|      |        2006 |        2007 |        2008 |        2009 |         2010 |        2011 |         2012 |         2013 |         2014 |        2015 |        2016 |         2017 |         2018 |
|-----:|------------:|------------:|------------:|------------:|-------------:|------------:|-------------:|-------------:|-------------:|------------:|------------:|-------------:|-------------:|
| 2006 |           1 |           1 |           1 |           1 |  2.56376e-06 |           1 |            1 |   0.00192206 |            1 |  0.00044216 | 3.39647e-18 |  1.45931e-35 |  5.56285e-46 |
| 2007 |           1 |           1 |           1 |           1 |  1.85725e-07 |           1 |            1 |  0.000235584 |            1 |  0.00359673 | 2.56109e-16 |  8.78421e-33 |  7.89121e-43 |
| 2008 |           1 |           1 |           1 |    0.452616 |  0.000559885 |           1 |            1 |     0.185335 |            1 |  2.0894e-09 | 8.67201e-31 |  1.70782e-57 |  4.97192e-72 |
| 2009 |           1 |           1 |    0.452616 |           1 |  3.81605e-14 |           1 |            1 |  3.26314e-09 |     0.108834 |  0.00280192 | 1.63221e-21 |   1.8058e-48 |  5.61346e-64 |
| 2010 | 2.56376e-06 | 1.85725e-07 | 0.000559885 | 3.81605e-14 |            1 | 2.61956e-10 |  3.01058e-08 |            1 |  1.60823e-06 | 3.08446e-38 | 2.86872e-85 | 7.60189e-149 | 2.25936e-175 |
| 2011 |           1 |           1 |           1 |           1 |  2.61956e-10 |           1 |            1 |  7.69181e-06 |            1 | 5.25676e-08 | 2.91903e-34 |  2.51597e-73 |  1.59014e-93 |
| 2012 |           1 |           1 |           1 |           1 |  3.01058e-08 |           1 |            1 |  0.000333372 |            1 | 1.75013e-10 | 1.25623e-39 |  1.27304e-82 | 4.30995e-104 |
| 2013 |  0.00192206 | 0.000235584 |    0.185335 | 3.26314e-09 |            1 | 7.69181e-06 |  0.000333372 |            1 |   0.00826924 |  5.6094e-30 | 6.02013e-74 |  1.4812e-135 | 5.94487e-162 |
| 2014 |           1 |           1 |           1 |    0.108834 |  1.60823e-06 |           1 |            1 |   0.00826924 |            1 | 2.27424e-14 | 7.45478e-49 | 7.20195e-101 | 2.53022e-125 |
| 2015 |  0.00044216 |  0.00359673 |  2.0894e-09 |  0.00280192 |  3.08446e-38 | 5.25676e-08 |  1.75013e-10 |   5.6094e-30 |  2.27424e-14 |           1 | 1.29787e-08 |  2.10058e-30 |  3.72479e-45 |
| 2016 | 3.39647e-18 | 2.56109e-16 | 8.67201e-31 | 1.63221e-21 |  2.86872e-85 | 2.91903e-34 |  1.25623e-39 |  6.02013e-74 |  7.45478e-49 | 1.29787e-08 |           1 |  5.33601e-05 |  4.85056e-13 |
| 2017 | 1.45931e-35 | 8.78421e-33 | 1.70782e-57 |  1.8058e-48 | 7.60189e-149 | 2.51597e-73 |  1.27304e-82 |  1.4812e-135 | 7.20195e-101 | 2.10058e-30 | 5.33601e-05 |            1 |    0.0406896 |
| 2018 | 5.56285e-46 | 7.89121e-43 | 4.97192e-72 | 5.61346e-64 | 2.25936e-175 | 1.59014e-93 | 4.30995e-104 | 5.94487e-162 | 2.53022e-125 | 3.72479e-45 | 4.85056e-13 |    0.0406896 |            1 |

---

*Significance codes: *** p<0.001, ** p<0.01, * p<0.05, ns not significant*
