# Page 4: Score Bins + Citizenship

**Generated:** 2026-08-14 17:29

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `besttrend`/`uni` for bins; `uniobservable` (no-PLE-match, citizenship notna) for citizenship

**Filters:** None (full unfiltered dataset)

---

## Sub-tab 1: By Year

Use this tab to see whether later cohorts became more concentrated in higher bins, lower bins, or the middle of the distribution.

**Table 10: Count of examinees in each bin by NMAT year**

| PercentileBin   |   2006 |   2007 |   2008 |   2009 |   2010 |   2011 |   2012 |   2013 |   2014 |   2015 |   2016 |   2017 |   2018 |
|:----------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| B10             |    464 |    450 |    703 |    931 |   1327 |    955 |   1503 |   1772 |   1763 |   1363 |   1085 |   1822 |   1947 |
| B9              |    396 |    408 |    540 |    737 |   1019 |    894 |    911 |   1032 |   1170 |   1029 |   1217 |   2089 |   1789 |
| B8              |    375 |    385 |    468 |    718 |    908 |    934 |    816 |    899 |   1030 |    968 |   1206 |   2205 |   1824 |
| B7              |    357 |    361 |    495 |    755 |    829 |    847 |    785 |    753 |    974 |   1026 |   1160 |   2200 |   1817 |
| B6              |    372 |    301 |    519 |    802 |    917 |    897 |    741 |    632 |    839 |    900 |   1310 |   2408 |   2141 |
| B5              |    369 |    369 |    499 |    717 |    891 |   1037 |    874 |    708 |    821 |    894 |   1268 |   2059 |   2152 |
| B4              |    354 |    397 |    476 |    805 |    749 |    967 |    777 |    610 |    731 |    697 |   1041 |   2650 |   2335 |
| B3              |    343 |    355 |    394 |    729 |    731 |    801 |    705 |    562 |    686 |    720 |    971 |   2331 |   2109 |
| B2              |    325 |    315 |    417 |    655 |    633 |    751 |    772 |    694 |    710 |    724 |   1160 |   2766 |   2466 |
| B1              |    320 |    324 |    436 |    589 |    525 |    566 |    968 |   1086 |   1292 |   1419 |   1723 |   3082 |   3253 |


**Percentage of examinees in each bin by NMAT year (row %)**

|   Year |    B1 |    B2 |   B3 |    B4 |    B5 |    B6 |    B7 |    B8 |    B9 |   B10 |
|-------:|------:|------:|-----:|------:|------:|------:|------:|------:|------:|------:|
|   2006 |  8.71 |  8.84 | 9.33 |  9.63 | 10.04 | 10.12 |  9.71 |  10.2 | 10.78 | 12.63 |
|   2007 |  8.84 |  8.59 | 9.69 | 10.83 | 10.07 |  8.21 |  9.85 |  10.5 | 11.13 | 12.28 |
|   2008 |  8.81 |  8.43 | 7.96 |  9.62 | 10.09 | 10.49 | 10.01 |  9.46 | 10.92 | 14.21 |
|   2009 |  7.92 |  8.81 |  9.8 | 10.82 |  9.64 | 10.78 | 10.15 |  9.65 |  9.91 | 12.52 |
|   2010 |  6.16 |  7.42 | 8.57 |  8.78 | 10.45 | 10.75 |  9.72 | 10.65 | 11.95 | 15.56 |
|   2011 |  6.54 |  8.68 | 9.26 | 11.18 | 11.99 | 10.37 |  9.79 |  10.8 | 10.34 | 11.04 |
|   2012 | 10.94 |  8.72 | 7.96 |  8.78 |  9.87 |  8.37 |  8.87 |  9.22 | 10.29 | 16.98 |
|   2013 | 12.41 |  7.93 | 6.42 |  6.97 |  8.09 |  7.22 |  8.61 | 10.28 |  11.8 | 20.26 |
|   2014 |  12.9 |  7.09 | 6.85 |   7.3 |   8.2 |  8.38 |  9.72 | 10.28 | 11.68 |  17.6 |
|   2015 | 14.57 |  7.43 | 7.39 |  7.16 |  9.18 |  9.24 | 10.53 |  9.94 | 10.56 | 13.99 |
|   2016 | 14.19 |  9.55 |    8 |  8.57 | 10.44 | 10.79 |  9.55 |  9.93 | 10.02 |  8.94 |
|   2017 | 13.05 | 11.71 | 9.87 | 11.22 |  8.72 |  10.2 |  9.32 |  9.34 |  8.85 |  7.72 |
|   2018 |  14.9 | 11.29 | 9.66 | 10.69 |  9.86 |  9.81 |  8.32 |  8.35 |  8.19 |  8.92 |


**Heatmap data: Bin Distribution by Year (row %, bins as rows, years as columns)**

| Bin   |   2006 |   2007 |   2008 |   2009 |   2010 |   2011 |   2012 |   2013 |   2014 |   2015 |   2016 |   2017 |   2018 |
|:------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| B10   |  12.63 |  12.28 |  14.21 |  12.52 |  15.56 |  11.04 |  16.98 |  20.26 |   17.6 |  13.99 |   8.94 |   7.72 |   8.92 |
| B9    |  10.78 |  11.13 |  10.92 |   9.91 |  11.95 |  10.34 |  10.29 |   11.8 |  11.68 |  10.56 |  10.02 |   8.85 |   8.19 |
| B8    |   10.2 |   10.5 |   9.46 |   9.65 |  10.65 |   10.8 |   9.22 |  10.28 |  10.28 |   9.94 |   9.93 |   9.34 |   8.35 |
| B7    |   9.71 |   9.85 |  10.01 |  10.15 |   9.72 |   9.79 |   8.87 |   8.61 |   9.72 |  10.53 |   9.55 |   9.32 |   8.32 |
| B6    |  10.12 |   8.21 |  10.49 |  10.78 |  10.75 |  10.37 |   8.37 |   7.22 |   8.38 |   9.24 |  10.79 |   10.2 |   9.81 |
| B5    |  10.04 |  10.07 |  10.09 |   9.64 |  10.45 |  11.99 |   9.87 |   8.09 |    8.2 |   9.18 |  10.44 |   8.72 |   9.86 |
| B4    |   9.63 |  10.83 |   9.62 |  10.82 |   8.78 |  11.18 |   8.78 |   6.97 |    7.3 |   7.16 |   8.57 |  11.22 |  10.69 |
| B3    |   9.33 |   9.69 |   7.96 |    9.8 |   8.57 |   9.26 |   7.96 |   6.42 |   6.85 |   7.39 |      8 |   9.87 |   9.66 |
| B2    |   8.84 |   8.59 |   8.43 |   8.81 |   7.42 |   8.68 |   8.72 |   7.93 |   7.09 |   7.43 |   9.55 |  11.71 |  11.29 |
| B1    |   8.71 |   8.84 |   8.81 |   7.92 |   6.16 |   6.54 |  10.94 |  12.41 |   12.9 |  14.57 |  14.19 |  13.05 |   14.9 |


**Figure 7: Top-bin (B8-B10) vs Bottom-bin (B1-B3) share by Year**

|   Year |   Top_B8_B10_pct |   Bottom_B1_B3_pct |
|-------:|-----------------:|-------------------:|
|   2006 |            33.61 |              26.88 |
|   2007 |            33.91 |              27.12 |
|   2008 |            34.59 |               25.2 |
|   2009 |            32.08 |              26.53 |
|   2010 |            38.16 |              22.15 |
|   2011 |            32.18 |              24.48 |
|   2012 |            36.49 |              27.62 |
|   2013 |            42.34 |              26.76 |
|   2014 |            39.56 |              26.84 |
|   2015 |            34.49 |              29.39 |
|   2016 |            28.89 |              31.74 |
|   2017 |            25.91 |              34.63 |
|   2018 |            25.46 |              35.85 |


---
## Sub-tab 2: University Type

Insight: Compare which university types are overrepresented in higher bins.

**Figure 8: Percentile-bin distribution by university type (row %)**

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private              | 12.04 | 9.69 |    9 | 9.92 | 9.91 | 9.94 | 9.47 | 9.69 |  9.73 | 10.63 |
| Public               | 10.83 | 8.18 | 7.56 | 8.25 | 8.52 | 8.89 |  9.1 | 9.57 |  11.2 |  17.9 |


**Figure 9: Share of examinees in B8-B10 by university type**

| UNDERGRAD_UNI_TYPE   |   Top_B8_B10_pct |
|:---------------------|-----------------:|
| Foreign              |             34.3 |
| Private              |            30.05 |
| Public               |            38.67 |


**Table 11: Chi-square test — UNDERGRAD_UNI_TYPE x PercentileBin**

|    chi2 | p_value   |   degrees_of_freedom |   n_observations |   cramers_v |
|--------:|:----------|---------------------:|-----------------:|------------:|
| 1270.33 | <0.001    |                   18 |           130494 |      0.0698 |


**Observed contingency: UNDERGRAD_UNI_TYPE x PercentileBin**

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |    B4 |    B5 |    B6 |   B7 |   B8 |   B9 |   B10 |
|:---------------------|------:|-----:|-----:|------:|------:|------:|-----:|-----:|-----:|------:|
| Foreign              |   262 |  174 |  140 |   176 |   145 |   164 |  161 |  175 |  197 |   266 |
| Private              | 12205 | 9823 | 9127 | 10061 | 10044 | 10079 | 9602 | 9821 | 9864 | 10774 |
| Public               |  2949 | 2228 | 2058 |  2247 |  2320 |  2421 | 2478 | 2606 | 3051 |  4876 |


**Expected frequencies: UNDERGRAD_UNI_TYPE x PercentileBin**

| UNDERGRAD_UNI_TYPE   |      B1 |      B2 |      B3 |      B4 |      B5 |      B6 |      B7 |      B8 |      B9 |     B10 |
|:---------------------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Foreign              | 219.732 | 174.249 | 161.421 | 177.941 | 178.297 | 180.507 | 174.477 | 179.623 | 186.892 | 226.859 |
| Private              |   11979 |  9499.4 | 8800.06 | 9700.66 | 9720.08 | 9840.53 | 9511.84 | 9792.35 | 10188.6 | 12367.5 |
| Public               | 3217.31 | 2551.35 | 2363.52 |  2605.4 | 2610.62 | 2642.97 | 2554.69 | 2630.03 | 2736.46 | 3321.66 |


---
## Sub-tab 3: Course Group

Insight: Compare bin profiles across pre-med backgrounds.

**Figure 10: Percentile-bin distribution by Course Group (row %)**

| UNDERGRAD_COURSE_GROUP       |    B1 |    B2 |   B3 |    B4 |    B5 |    B6 |   B7 |    B8 |    B9 |   B10 |
|:-----------------------------|------:|------:|-----:|------:|------:|------:|-----:|------:|------:|------:|
| Education                    |  9.09 |  8.88 | 9.26 |  9.67 |  10.6 |  9.11 | 9.72 |  9.61 | 10.45 | 13.61 |
| Engineering & Technology     |  5.21 |  5.89 | 5.89 |  5.62 |  8.63 |  8.77 | 7.53 |    10 | 14.66 | 27.81 |
| Medical & Allied             |    10 |  9.74 | 9.43 | 10.67 | 10.82 | 10.66 | 9.77 |  9.79 |  9.39 |  9.74 |
| Natural Sciences             | 12.29 |  8.52 | 7.54 |  8.34 |  8.35 |  8.79 | 9.44 |  9.98 | 11.04 |  15.7 |
| Other                        |  9.76 |  8.47 | 8.47 |  9.37 |  9.38 |  9.63 | 9.63 | 10.41 | 11.63 | 13.24 |
| Social & Behavioral Sciences | 19.91 | 11.02 | 8.62 |  8.38 |  7.82 |  8.29 | 7.49 |  7.93 |  8.92 | 11.61 |


**Figure 11: Share of examinees in B8-B10 by Course Group**

| UNDERGRAD_COURSE_GROUP       |   Top_B8_B10_pct |
|:-----------------------------|-----------------:|
| Education                    |            33.67 |
| Engineering & Technology     |            52.47 |
| Medical & Allied             |            28.92 |
| Natural Sciences             |            36.72 |
| Other                        |            35.28 |
| Social & Behavioral Sciences |            28.46 |


**Chi-square test — UNDERGRAD_COURSE_GROUP x PercentileBin**

|    chi2 | p_value   |   degrees_of_freedom |   n_observations |   cramers_v |
|--------:|:----------|---------------------:|-----------------:|------------:|
| 3014.18 | <0.001    |                   45 |           131845 |      0.0676 |


**Observed contingency: UNDERGRAD_COURSE_GROUP x PercentileBin**

| UNDERGRAD_COURSE_GROUP       |   B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |   B9 |   B10 |
|:-----------------------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| Education                    |  313 |  306 |  319 |  333 |  365 |  314 |  335 |  331 |  360 |   469 |
| Engineering & Technology     |   38 |   43 |   43 |   41 |   63 |   64 |   55 |   73 |  107 |   203 |
| Medical & Allied             | 6348 | 6179 | 5988 | 6771 | 6865 | 6765 | 6198 | 6213 | 5960 |  6181 |
| Natural Sciences             | 4942 | 3425 | 3029 | 3351 | 3358 | 3535 | 3796 | 4011 | 4439 |  6310 |
| Other                        |  805 |  699 |  699 |  773 |  774 |  794 |  794 |  859 |  959 |  1092 |
| Social & Behavioral Sciences | 3137 | 1736 | 1359 | 1320 | 1233 | 1307 | 1181 | 1249 | 1406 |  1830 |


**Expected frequencies: UNDERGRAD_COURSE_GROUP x PercentileBin**

| UNDERGRAD_COURSE_GROUP       |      B1 |      B2 |      B3 |      B4 |      B5 |      B6 |      B7 |      B8 |      B9 |     B10 |
|:-----------------------------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Education                    | 407.171 | 323.688 | 298.839 |  328.94 | 330.743 | 333.905 |  322.93 | 332.781 | 345.715 | 420.288 |
| Engineering & Technology     |   86.28 | 68.5899 | 63.3244 | 69.7028 | 70.0849 | 70.7548 | 68.4294 | 70.5167 | 73.2575 | 89.0595 |
| Medical & Allied             |  7501.4 | 5963.38 | 5505.58 | 6060.14 | 6093.35 |  6151.6 | 5949.42 |  6130.9 | 6369.18 | 7743.05 |
| Natural Sciences             | 4750.84 | 3776.77 | 3486.83 | 3838.05 | 3859.08 | 3895.97 | 3767.93 | 3882.86 | 4033.78 | 4903.88 |
| Other                        | 974.846 | 774.972 | 715.479 | 787.547 | 791.863 | 799.433 | 773.158 | 796.743 | 827.709 | 1006.25 |
| Social & Behavioral Sciences | 1862.47 |  1480.6 | 1366.94 | 1504.63 | 1512.87 | 1527.33 | 1477.14 |  1522.2 | 1581.36 | 1922.47 |


**Table 12: Percentile summary by Course Group**

| UNDERGRAD_COURSE_GROUP       |     n |   median |   q25 |   q75 |
|:-----------------------------|------:|---------:|------:|------:|
| Education                    |  3461 |       52 |    26 |    78 |
| Engineering & Technology     |   731 |       72 |    41 |    91 |
| Medical & Allied             | 63834 |       49 |    25 |    73 |
| Natural Sciences             | 40961 |       54 |    24 |    81 |
| Other                        |  8306 |       54 |    27 |    79 |
| Social & Behavioral Sciences | 16400 |       40 |    11 |    73 |


---
## Citizenship Section (No-PLE-Match, Observable University Cohort)

Citizenship labels (CITIZENSHIP_FINAL, FOREIGNER_STATUS) are baked into NMAT_Exodus.parquet by Pipeline 4 using a 3-tier hierarchy: REAL_FOREIGNERS.csv ground truth -> pseudo-citizenship inference -> Filipino default.

**P4-01 fix:** this section previously computed over ALL 178,927 rows, reporting 32,501 verified foreigners against the dashboard's own filtered figure. It now reproduces the dashboard's exact filter chain: `uniobservable` (IS_BEST_OBSERVABLE_RECORD, UNDERGRAD_UNI_TYPE in [Public, Private, Foreign]) AND PLE_STATUS_LABEL == 'No confirmed PLE match' AND CITIZENSHIP_FINAL notna.

**population:** uniobservable ∩ no-confirmed-PLE-match ∩ citizenship notna | **n:** 37,381 | **denominator:** rows in `uniobservable` (n=68,622)

### Citizenship Profile — Summary Metrics

**Citizenship profile metrics**

| Metric                         |   Value |
|:-------------------------------|--------:|
| Total records with citizenship |   37381 |
| Verified Foreigners            |    5049 |
| Filipinos                      |   32320 |
| Distinct citizenship labels    |      43 |


### CITIZENSHIP_FINAL Distribution

**CITIZENSHIP_FINAL — counts and percentages**

| CITIZENSHIP_FINAL     |     n |   percent |
|:----------------------|------:|----------:|
| Filipino              | 32320 |     86.46 |
| India                 |  2598 |      6.95 |
| Thailand              |   580 |      1.55 |
| Nepal                 |   418 |      1.12 |
| United States         |   340 |      0.91 |
| Nigeria               |   127 |      0.34 |
| Korea (South)         |   125 |      0.33 |
| Iran                  |   125 |      0.33 |
| Sri Lanka             |   124 |      0.33 |
| Foreign (unspecified) |   107 |      0.29 |
| Malaysia              |    76 |       0.2 |
| Indonesia             |    75 |       0.2 |
| Taiwan                |    65 |      0.17 |
| Somalia               |    38 |       0.1 |
| Canada                |    34 |      0.09 |
| Japan                 |    33 |      0.09 |
| China                 |    32 |      0.09 |
| Pakistan              |    26 |      0.07 |
| Kenya                 |    20 |      0.05 |
| Australia             |    19 |      0.05 |
| United Kingdom        |    18 |      0.05 |
| Sudan                 |    14 |      0.04 |
| Ghana                 |    12 |      0.03 |
| Bangladesh            |     8 |      0.02 |
| Myanmar               |     8 |      0.02 |
| Ethiopia              |     5 |      0.01 |
| Germany               |     4 |      0.01 |
| Jordan                |     4 |      0.01 |
| Vietnam               |     3 |      0.01 |
| Rwanda                |     3 |      0.01 |
| Iraq                  |     3 |      0.01 |
| Kuwait                |     2 |      0.01 |
| Bhutan                |     2 |      0.01 |
| Sweden                |     2 |      0.01 |
| Austria               |     2 |      0.01 |
| New Zealand           |     2 |      0.01 |
| Yemen                 |     1 |         0 |
| Cameroon              |     1 |         0 |
| Lebanon               |     1 |         0 |
| Syria                 |     1 |         0 |
| Italy                 |     1 |         0 |
| Guam                  |     1 |         0 |
| Portugal              |     1 |         0 |


### FOREIGNER_STATUS Distribution

**FOREIGNER_STATUS — counts and percentages**

| FOREIGNER_STATUS   |     n |   percent |
|:-------------------|------:|----------:|
| Filipino           | 32320 |     86.46 |
| Verified Foreigner |  5049 |     13.51 |
| Likely Foreigner   |    12 |      0.03 |


### Foreigners vs Filipinos Comparison

**Foreigners vs Filipinos**

| group     |     n |   percent |
|:----------|------:|----------:|
| Foreigner |  5049 |     13.51 |
| Filipino  | 32320 |     86.49 |


### Top 15 Citizenship Groups by Count

**Top 15 citizenship groups**

| CITIZENSHIP_FINAL     |     n |   percent |
|:----------------------|------:|----------:|
| Canada                |    34 |      0.09 |
| Somalia               |    38 |       0.1 |
| Taiwan                |    65 |      0.17 |
| Indonesia             |    75 |       0.2 |
| Malaysia              |    76 |       0.2 |
| Foreign (unspecified) |   107 |      0.29 |
| Sri Lanka             |   124 |      0.33 |
| Korea (South)         |   125 |      0.33 |
| Iran                  |   125 |      0.33 |
| Nigeria               |   127 |      0.34 |
| United States         |   340 |      0.91 |
| Nepal                 |   418 |      1.12 |
| Thailand              |   580 |      1.55 |
| India                 |  2598 |      6.95 |
| Filipino              | 32320 |     86.46 |


### Bin Composition by Citizenship (Top 15 Groups)

**Bin composition by citizenship (row %)**

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


### Full Percentile-Bin Heatmap by Citizenship (All Bins B1-B10)

Each row is one citizenship group; each column is one percentile bin. Values are row percentages.

| Bin   |   Canada |   Filipino |   Foreign (unspecified) |   India |   Indonesia |   Iran |   Korea (South) |   Malaysia |   Nepal |   Nigeria |   Somalia |   Sri Lanka |   Taiwan |   Thailand |   United States |
|:------|---------:|-----------:|------------------------:|--------:|------------:|-------:|----------------:|-----------:|--------:|----------:|----------:|------------:|---------:|-----------:|----------------:|
| B10   |    18.75 |       8.12 |                   12.62 |     2.1 |       12.16 |   3.39 |           18.55 |       4.11 |    2.68 |       7.2 |         0 |        4.88 |     9.38 |       1.41 |           24.85 |
| B9    |    18.75 |       7.84 |                    8.74 |    2.58 |        6.76 |   3.39 |            8.06 |       4.11 |    7.54 |       5.6 |         0 |        7.32 |     7.81 |       1.76 |           18.71 |
| B8    |     12.5 |       8.51 |                     6.8 |    3.84 |        5.41 |   2.54 |            12.1 |       2.74 |    4.62 |       4.8 |         0 |        8.13 |     9.38 |       3.69 |           12.88 |
| B7    |     6.25 |        8.3 |                    4.85 |    5.29 |        4.05 |   4.24 |            9.68 |       1.37 |    6.81 |       5.6 |         0 |       10.57 |     9.38 |       4.39 |            7.67 |
| B6    |     12.5 |       8.68 |                    8.74 |    6.03 |        6.76 |   5.93 |            12.9 |       6.85 |    7.06 |         8 |         0 |       13.01 |     4.69 |       4.92 |            7.36 |
| B5    |     6.25 |       9.86 |                    8.74 |    7.73 |       10.81 |   5.93 |           10.48 |       5.48 |   11.44 |       8.8 |      3.57 |        12.2 |        0 |       6.68 |            5.83 |
| B4    |     6.25 |      11.38 |                    9.71 |    9.44 |        8.11 |   6.78 |            8.87 |      15.07 |   14.11 |       7.2 |         0 |       13.01 |     4.69 |      10.37 |            6.44 |
| B3    |     6.25 |       11.2 |                     6.8 |    9.87 |       10.81 |   6.78 |            5.65 |      15.07 |   10.22 |      11.2 |      7.14 |       10.57 |    10.94 |      13.53 |            3.99 |
| B2    |     6.25 |      12.11 |                   11.65 |   13.63 |       18.92 |  14.41 |            7.26 |      17.81 |   14.36 |      10.4 |      3.57 |       11.38 |    14.06 |      16.52 |            4.29 |
| B1    |     6.25 |         14 |                   21.36 |   39.49 |       16.22 |  46.61 |            6.45 |       27.4 |   21.17 |      31.2 |     85.71 |        8.94 |    29.69 |      36.73 |            7.98 |


### Top-Bin Share (B8-B10) by Citizenship

**Top-bin (B8-B10) share by citizenship (n >= 3)**

| CITIZENSHIP_FINAL     |     n |   top_n |   top_dec_pct |
|:----------------------|------:|--------:|--------------:|
| United Kingdom        |    18 |      14 |          77.8 |
| Vietnam               |     3 |       2 |          66.7 |
| United States         |   340 |     184 |          54.1 |
| Australia             |    19 |       9 |          47.4 |
| Canada                |    34 |      16 |          47.1 |
| Korea (South)         |   125 |      48 |          38.4 |
| China                 |    32 |      11 |          34.4 |
| Iraq                  |     3 |       1 |          33.3 |
| Ghana                 |    12 |       4 |          33.3 |
| Foreign (unspecified) |   107 |      29 |          27.1 |
| Taiwan                |    65 |      17 |          26.2 |
| Germany               |     4 |       1 |            25 |
| Filipino              | 32320 |    7829 |          24.2 |
| Indonesia             |    75 |      18 |            24 |
| Sri Lanka             |   124 |      25 |          20.2 |
| Kenya                 |    20 |       4 |            20 |
| Ethiopia              |     5 |       1 |            20 |
| Japan                 |    33 |       6 |          18.2 |
| Nigeria               |   127 |      22 |          17.3 |
| Pakistan              |    26 |       4 |          15.4 |
| Nepal                 |   418 |      61 |          14.6 |
| Malaysia              |    76 |       8 |          10.5 |
| Iran                  |   125 |      11 |           8.8 |
| India                 |  2598 |     195 |           7.5 |
| Thailand              |   580 |      39 |           6.7 |
| Jordan                |     4 |       0 |             0 |
| Bangladesh            |     8 |       0 |             0 |
| Rwanda                |     3 |       0 |             0 |
| Myanmar               |     8 |       0 |             0 |
| Sudan                 |    14 |       0 |             0 |
| Somalia               |    38 |       0 |             0 |


### Percentile Rank by Citizenship (n >= 5)

**Percentile rank statistics by citizenship (n >= 5)**

| CITIZENSHIP_FINAL     |     n |   mean |   std |   min |   q25 |   median |   q75 |   max |
|:----------------------|------:|-------:|------:|------:|------:|---------:|------:|------:|
| Australia             |    17 |  63.06 | 33.85 |    -1 |    41 |       73 |    92 |    99 |
| Bangladesh            |     8 |  31.88 | 23.47 |     2 | 12.25 |     30.5 | 51.25 |    62 |
| Canada                |    32 |  62.72 |  29.8 |     4 | 41.75 |     69.5 | 88.25 |    99 |
| China                 |    31 |   55.1 | 31.02 |     9 |  27.5 |       55 |    86 |    99 |
| Ethiopia              |     5 |   31.2 | 32.35 |     7 |    11 |       23 |    28 |    87 |
| Filipino              | 32177 |  43.94 | 29.11 |    -1 |    18 |       41 |    69 |    99 |
| Foreign (unspecified) |   106 |  42.13 | 33.27 |    -1 | 10.25 |       39 | 74.75 |    98 |
| Ghana                 |    12 |  50.17 | 23.17 |    19 | 31.25 |     44.5 |    77 |    84 |
| India                 |  2597 |  22.91 |  25.7 |    -1 |     2 |       12 |    39 |    99 |
| Indonesia             |    75 |  40.51 | 31.07 |    -1 |  15.5 |       32 |    63 |    99 |
| Iran                  |   125 |  22.45 | 26.91 |    -1 |     1 |       10 |    37 |    96 |
| Japan                 |    33 |  40.64 | 25.05 |     1 |    23 |       41 |    55 |    89 |
| Kenya                 |    20 |   47.3 | 27.37 |     1 | 37.75 |       52 |    56 |    96 |
| Korea (South)         |   124 |  57.44 | 28.26 |     4 |  34.5 |       58 |    81 |    99 |
| Malaysia              |    76 |   27.8 | 26.06 |    -1 |     6 |       24 | 38.25 |    98 |
| Myanmar               |     8 |   8.62 | 15.88 |    -1 |     2 |      3.5 |   5.5 |    47 |
| Nepal                 |   418 |  35.46 | 27.19 |    -1 |    11 |       32 |    55 |    97 |
| Nigeria               |   127 |  34.09 | 29.98 |    -1 |     6 |       26 |  57.5 |    98 |
| Pakistan              |    26 |  30.31 | 31.21 |    -1 |  3.25 |       14 | 61.75 |    92 |
| Somalia               |    38 |   3.92 |  8.95 |    -1 |  -0.5 |        2 |     3 |    48 |
| Sri Lanka             |   124 |  44.99 | 25.66 |    -1 |    24 |     44.5 |    65 |    96 |
| Sudan                 |    14 |   7.64 |  9.95 |    -1 |    -1 |      4.5 |    12 |    26 |
| Taiwan                |    65 |  37.46 | 33.71 |    -1 |     7 |       25 |    70 |    99 |
| Thailand              |   580 |  24.23 | 23.21 |    -1 |     6 |       16 |    36 |    98 |
| United Kingdom        |    18 |  74.56 | 19.81 |    23 |    74 |     79.5 | 85.75 |    97 |
| United States         |   330 |  63.95 | 30.39 |    -1 | 42.25 |       75 |    89 |    99 |


### TRUE Raw Score by Citizenship (n >= 5)

**TRUE raw score statistics by citizenship (n >= 5)**

| CITIZENSHIP_FINAL     |     n |   mean |   std |   min |    q25 |   median |    q75 |   max |
|:----------------------|------:|-------:|------:|------:|-------:|---------:|-------:|------:|
| Australia             |    19 |    142 | 40.86 |    50 |    120 |      150 |  170.5 |   200 |
| Bangladesh            |     8 | 102.38 | 21.84 |    69 |  89.75 |    102.5 | 116.25 |   135 |
| Canada                |    34 | 141.79 | 35.23 |    77 | 117.25 |      144 |    165 |   223 |
| China                 |    32 | 135.78 | 36.07 |    86 |  104.5 |    127.5 | 163.25 |   215 |
| Ethiopia              |     5 |  109.2 | 32.48 |    82 |     89 |      101 |    110 |   164 |
| Filipino              | 32302 | 118.49 | 29.45 |    37 |     97 |      116 |    138 |   223 |
| Foreign (unspecified) |   107 | 118.91 |  38.5 |    56 |   88.5 |      115 |    150 |   200 |
| Ghana                 |    12 | 116.75 | 18.66 |    94 | 103.75 |      110 |    135 |   151 |
| India                 |  2596 |  91.63 | 28.52 |     9 |     69 |       89 |    112 |   216 |
| Indonesia             |    75 | 117.41 | 33.75 |    56 |     94 |      109 |    134 |   198 |
| Iran                  |   125 |  93.74 | 30.74 |    40 |     69 |       88 |    117 |   171 |
| Japan                 |    33 | 112.91 | 25.07 |    65 |    100 |      115 |    128 |   166 |
| Kenya                 |    19 | 117.21 | 29.08 |    57 |    110 |      121 |    130 |   183 |
| Korea (South)         |   125 | 133.79 | 29.29 |    79 |    111 |      131 |    155 |   194 |
| Malaysia              |    76 |  100.7 | 27.18 |    44 |     84 |     99.5 | 117.25 |   174 |
| Myanmar               |     8 |   77.5 | 22.92 |    50 |   68.5 |       73 |  80.75 |   125 |
| Nepal                 |   417 | 109.52 | 28.26 |    47 |     89 |      108 |    125 |   195 |
| Nigeria               |   127 | 104.34 | 28.03 |    59 |   81.5 |      102 |    125 |   178 |
| Pakistan              |    26 | 100.12 | 33.06 |    48 |     73 |       93 |  129.5 |   176 |
| Somalia               |    38 |  69.34 | 14.53 |    43 |  61.25 |       69 |     74 |   114 |
| Sri Lanka             |   124 | 118.07 | 23.34 |    60 | 100.75 |      119 |    134 |   177 |
| Sudan                 |    14 |  76.43 | 18.81 |    48 |     61 |     76.5 |  91.25 |   104 |
| Taiwan                |    62 | 113.84 | 34.14 |    56 |   85.5 |      110 |    139 |   184 |
| Thailand              |   575 |  97.88 | 24.18 |    46 |     80 |       95 |  112.5 |   176 |
| United Kingdom        |    18 | 149.94 | 22.41 |    99 | 140.25 |      151 |    162 |   186 |
| United States         |   336 | 143.89 | 34.04 |    47 |    122 |      149 | 168.25 |   216 |


### Summary by Citizenship

**Summary statistics by citizenship**

| CITIZENSHIP_FINAL     |   n_examinees |   median_percentile_rank |   median_true_raw_score |   top_decile_n |   top_decile_pct |   bottom_decile_n |   bottom_decile_pct |
|:----------------------|--------------:|-------------------------:|------------------------:|---------------:|-----------------:|------------------:|--------------------:|
| Filipino              |         32320 |                       41 |                     116 |           7829 |            24.22 |             11933 |               36.92 |
| India                 |          2598 |                       12 |                      89 |            195 |             7.51 |              1442 |                55.5 |
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


### Summary by Citizenship and University Type

**By citizenship and university type**

| CITIZENSHIP_FINAL     | UNDERGRAD_UNI_TYPE   |     n |   median_percentile_rank |   median_true_raw_score |
|:----------------------|:---------------------|------:|-------------------------:|------------------------:|
| Australia             | Foreign              |     5 |                       52 |                     130 |
| Australia             | Private              |     8 |                       51 |                     121 |
| Australia             | Public               |     6 |                     94.5 |                   170.5 |
| Austria               | Private              |     2 |                       54 |                   132.5 |
| Bangladesh            | Private              |     7 |                       29 |                     100 |
| Bangladesh            | Public               |     1 |                       61 |                     135 |
| Bhutan                | Private              |     2 |                     47.5 |                   122.5 |
| Cameroon              | Public               |     1 |                        8 |                      87 |
| Canada                | Foreign              |    11 |                       77 |                     152 |
| Canada                | Private              |    17 |                     51.5 |                     121 |
| Canada                | Public               |     6 |                       58 |                   136.5 |
| China                 | Foreign              |     4 |                     64.5 |                   135.5 |
| China                 | Private              |    21 |                       44 |                     121 |
| China                 | Public               |     7 |                       57 |                     117 |
| Ethiopia              | Private              |     4 |                     19.5 |                    99.5 |
| Ethiopia              | Public               |     1 |                       23 |                     101 |
| Filipino              | Foreign              |   418 |                       63 |                     135 |
| Filipino              | Private              | 25341 |                       38 |                     114 |
| Filipino              | Public               |  6561 |                       49 |                     123 |
| Foreign (unspecified) | Foreign              |    25 |                       79 |                     157 |
| Foreign (unspecified) | Private              |    62 |                       20 |                   101.5 |
| Foreign (unspecified) | Public               |    20 |                       63 |                     144 |
| Germany               | Private              |     3 |                        4 |                      76 |
| Germany               | Public               |     1 |                       57 |                     134 |
| Ghana                 | Foreign              |     1 |                       77 |                     135 |
| Ghana                 | Private              |     8 |                     47.5 |                   112.5 |
| Ghana                 | Public               |     3 |                       41 |                     109 |
| Guam                  | Private              |     1 |                        1 |                      66 |
| India                 | Foreign              |    41 |                       12 |                      89 |
| India                 | Private              |  2081 |                       12 |                      89 |
| India                 | Public               |   476 |                        9 |                      87 |
| Indonesia             | Foreign              |    11 |                       15 |                      93 |
| Indonesia             | Private              |    55 |                       36 |                     117 |
| Indonesia             | Public               |     9 |                       46 |                     116 |
| Iran                  | Foreign              |     7 |                       31 |                     113 |
| Iran                  | Private              |    95 |                       11 |                      89 |
| Iran                  | Public               |    23 |                        6 |                      87 |
| Iraq                  | Private              |     3 |                        6 |                      82 |
| Italy                 | Private              |     1 |                       44 |                     119 |
| Japan                 | Foreign              |     4 |                     36.5 |                   114.5 |
| Japan                 | Private              |    20 |                       39 |                     111 |
| Japan                 | Public               |     9 |                       41 |                     117 |
| Jordan                | Private              |     4 |                        2 |                    68.5 |
| Kenya                 | Private              |    15 |                       52 |                   120.5 |
| Kenya                 | Public               |     5 |                       53 |                     130 |
| Korea (South)         | Foreign              |    10 |                     55.5 |                     133 |
| Korea (South)         | Private              |    99 |                       58 |                     129 |
| Korea (South)         | Public               |    16 |                       58 |                   136.5 |
| Kuwait                | Private              |     2 |                      2.5 |                    62.5 |
| Lebanon               | Private              |     1 |                       47 |                     124 |
| Malaysia              | Foreign              |     8 |                     22.5 |                    95.5 |
| Malaysia              | Private              |    58 |                       24 |                   100.5 |
| Malaysia              | Public               |    10 |                       10 |                    86.5 |
| Myanmar               | Foreign              |     1 |                        4 |                      77 |
| Myanmar               | Private              |     4 |                        1 |                      65 |
| Myanmar               | Public               |     3 |                       10 |                      92 |
| Nepal                 | Foreign              |     5 |                       32 |                     104 |
| Nepal                 | Private              |   372 |                       32 |                     109 |
| Nepal                 | Public               |    41 |                       18 |                      94 |
| New Zealand           | Public               |     2 |                     46.5 |                     113 |
| Nigeria               | Foreign              |     5 |                       31 |                     111 |
| Nigeria               | Private              |    95 |                       29 |                     102 |
| Nigeria               | Public               |    27 |                       19 |                      99 |
| Pakistan              | Foreign              |     2 |                     81.5 |                     153 |
| Pakistan              | Private              |    19 |                        8 |                      85 |
| Pakistan              | Public               |     5 |                        6 |                      89 |
| Portugal              | Private              |     1 |                       23 |                      98 |
| Rwanda                | Private              |     3 |                       14 |                      91 |
| Somalia               | Private              |    31 |                        1 |                      69 |
| Somalia               | Public               |     7 |                        3 |                      77 |
| Sri Lanka             | Foreign              |     2 |                       44 |                     114 |
| Sri Lanka             | Private              |   105 |                       42 |                     119 |
| Sri Lanka             | Public               |    17 |                       55 |                     122 |
| Sudan                 | Foreign              |     2 |                     14.5 |                    92.5 |
| Sudan                 | Private              |     8 |                      6.5 |                    83.5 |
| Sudan                 | Public               |     4 |                      0.5 |                    59.5 |
| Sweden                | Public               |     2 |                     35.5 |                     118 |
| Syria                 | Private              |     1 |                       54 |                     132 |
| Taiwan                | Foreign              |    12 |                     41.5 |                     117 |
| Taiwan                | Private              |    41 |                       25 |                     112 |
| Taiwan                | Public               |    12 |                     23.5 |                   102.5 |
| Thailand              | Foreign              |   201 |                       21 |                     101 |
| Thailand              | Private              |   308 |                       15 |                      92 |
| Thailand              | Public               |    71 |                       14 |                      91 |
| United Kingdom        | Foreign              |     1 |                       83 |                     141 |
| United Kingdom        | Private              |    12 |                     76.5 |                   149.5 |
| United Kingdom        | Public               |     5 |                       85 |                     159 |
| United States         | Foreign              |   124 |                       81 |                     158 |
| United States         | Private              |   153 |                       68 |                     139 |
| United States         | Public               |    63 |                       76 |                     143 |
| Vietnam               | Foreign              |     1 |                       93 |                     175 |
| Vietnam               | Public               |     2 |                     62.5 |                   141.5 |
| Yemen                 | Private              |     1 |                       38 |                     114 |


### Summary by Citizenship and Course Group

**By citizenship and course group**

| CITIZENSHIP_FINAL     | UNDERGRAD_COURSE_GROUP       |     n |   median_percentile_rank |   median_true_raw_score |
|:----------------------|:-----------------------------|------:|-------------------------:|------------------------:|
| Australia             | Education                    |     1 |                       52 |                     130 |
| Australia             | Medical & Allied             |     8 |                       73 |                   153.5 |
| Australia             | Natural Sciences             |     4 |                       71 |                   137.5 |
| Australia             | Other                        |     4 |                       84 |                     176 |
| Australia             | Social & Behavioral Sciences |     2 |                       72 |                     147 |
| Austria               | Medical & Allied             |     1 |                       30 |                     111 |
| Austria               | Other                        |     1 |                       78 |                     154 |
| Bangladesh            | Medical & Allied             |     5 |                       32 |                     105 |
| Bangladesh            | Natural Sciences             |     2 |                       45 |                   117.5 |
| Bangladesh            | Social & Behavioral Sciences |     1 |                        7 |                      80 |
| Bhutan                | Natural Sciences             |     2 |                     47.5 |                   122.5 |
| Cameroon              | Social & Behavioral Sciences |     1 |                        8 |                      87 |
| Canada                | Engineering & Technology     |     1 |                       10 |                      86 |
| Canada                | Medical & Allied             |    15 |                       74 |                     143 |
| Canada                | Natural Sciences             |     9 |                       87 |                     166 |
| Canada                | Other                        |     6 |                       84 |                     165 |
| Canada                | Social & Behavioral Sciences |     3 |                       44 |                     117 |
| China                 | Education                    |     4 |                     49.5 |                   127.5 |
| China                 | Medical & Allied             |    18 |                     30.5 |                     110 |
| China                 | Natural Sciences             |     6 |                     94.5 |                   171.5 |
| China                 | Other                        |     2 |                       73 |                   167.5 |
| China                 | Social & Behavioral Sciences |     2 |                       14 |                   154.5 |
| Ethiopia              | Medical & Allied             |     4 |                     25.5 |                   105.5 |
| Ethiopia              | Other                        |     1 |                        7 |                      82 |
| Filipino              | Education                    |  1341 |                       41 |                     123 |
| Filipino              | Engineering & Technology     |   156 |                       64 |                   130.5 |
| Filipino              | Medical & Allied             | 18797 |                       35 |                     111 |
| Filipino              | Natural Sciences             |  6815 |                       54 |                     124 |
| Filipino              | Other                        |  2871 |                       44 |                     123 |
| Filipino              | Social & Behavioral Sciences |  2340 |                       52 |                     123 |
| Foreign (unspecified) | Education                    |     6 |                       57 |                   136.5 |
| Foreign (unspecified) | Engineering & Technology     |     2 |                     63.5 |                     139 |
| Foreign (unspecified) | Medical & Allied             |    41 |                       34 |                     111 |
| Foreign (unspecified) | Natural Sciences             |    37 |                       40 |                     115 |
| Foreign (unspecified) | Other                        |    16 |                       39 |                   125.5 |
| Foreign (unspecified) | Social & Behavioral Sciences |     5 |                       42 |                     131 |
| Germany               | Medical & Allied             |     3 |                       57 |                     134 |
| Germany               | Natural Sciences             |     1 |                        4 |                      76 |
| Ghana                 | Medical & Allied             |     1 |                       77 |                     135 |
| Ghana                 | Natural Sciences             |    11 |                       43 |                     109 |
| Guam                  | Natural Sciences             |     1 |                        1 |                      66 |
| India                 | Education                    |    67 |                     10.5 |                      91 |
| India                 | Engineering & Technology     |     4 |                       10 |                      84 |
| India                 | Medical & Allied             |   335 |                       21 |                     100 |
| India                 | Natural Sciences             |  1545 |                        8 |                      82 |
| India                 | Other                        |   141 |                       24 |                     105 |
| India                 | Social & Behavioral Sciences |   506 |                       21 |                      97 |
| Indonesia             | Education                    |     4 |                     46.5 |                   129.5 |
| Indonesia             | Medical & Allied             |    39 |                       40 |                     113 |
| Indonesia             | Natural Sciences             |    21 |                       30 |                     107 |
| Indonesia             | Other                        |    10 |                       14 |                      95 |
| Indonesia             | Social & Behavioral Sciences |     1 |                       94 |                     181 |
| Iran                  | Education                    |     3 |                        5 |                      86 |
| Iran                  | Medical & Allied             |    21 |                       25 |                     105 |
| Iran                  | Natural Sciences             |    81 |                       10 |                      88 |
| Iran                  | Other                        |    19 |                        2 |                      72 |
| Iran                  | Social & Behavioral Sciences |     1 |                       20 |                     110 |
| Iraq                  | Natural Sciences             |     1 |                       82 |                     140 |
| Iraq                  | Social & Behavioral Sciences |     2 |                        5 |                      80 |
| Italy                 | Other                        |     1 |                       44 |                     119 |
| Japan                 | Education                    |     2 |                     29.5 |                     105 |
| Japan                 | Medical & Allied             |     5 |                       19 |                     100 |
| Japan                 | Natural Sciences             |    11 |                       43 |                     111 |
| Japan                 | Other                        |     7 |                       43 |                     116 |
| Japan                 | Social & Behavioral Sciences |     8 |                       43 |                   119.5 |
| Jordan                | Medical & Allied             |     4 |                        2 |                    68.5 |
| Kenya                 | Medical & Allied             |    12 |                       52 |                   121.5 |
| Kenya                 | Natural Sciences             |     7 |                       53 |                     123 |
| Kenya                 | Other                        |     1 |                        2 |                      72 |
| Korea (South)         | Education                    |     8 |                       30 |                   106.5 |
| Korea (South)         | Engineering & Technology     |     2 |                     65.5 |                   141.5 |
| Korea (South)         | Medical & Allied             |    38 |                       54 |                     129 |
| Korea (South)         | Natural Sciences             |    42 |                       63 |                   125.5 |
| Korea (South)         | Other                        |    27 |                       64 |                     141 |
| Korea (South)         | Social & Behavioral Sciences |     8 |                     75.5 |                   135.5 |
| Kuwait                | Natural Sciences             |     1 |                        1 |                      53 |
| Kuwait                | Other                        |     1 |                        4 |                      72 |
| Lebanon               | Medical & Allied             |     1 |                       47 |                     124 |
| Malaysia              | Medical & Allied             |    20 |                       21 |                      97 |
| Malaysia              | Natural Sciences             |    53 |                       22 |                      99 |
| Malaysia              | Other                        |     3 |                       30 |                     106 |
| Myanmar               | Medical & Allied             |     4 |                        1 |                      65 |
| Myanmar               | Natural Sciences             |     1 |                        3 |                      72 |
| Myanmar               | Other                        |     3 |                       10 |                      92 |
| Nepal                 | Medical & Allied             |    72 |                       33 |                   115.5 |
| Nepal                 | Natural Sciences             |   277 |                       33 |                     107 |
| Nepal                 | Other                        |    68 |                     26.5 |                     105 |
| Nepal                 | Social & Behavioral Sciences |     1 |                        8 |                      84 |
| New Zealand           | Medical & Allied             |     2 |                     46.5 |                     113 |
| Nigeria               | Education                    |     2 |                       30 |                   114.5 |
| Nigeria               | Medical & Allied             |    36 |                     22.5 |                     102 |
| Nigeria               | Natural Sciences             |    79 |                       26 |                     101 |
| Nigeria               | Other                        |     5 |                       40 |                     120 |
| Nigeria               | Social & Behavioral Sciences |     5 |                       21 |                      97 |
| Pakistan              | Education                    |     1 |                       55 |                     133 |
| Pakistan              | Engineering & Technology     |     1 |                        5 |                      73 |
| Pakistan              | Medical & Allied             |    12 |                       37 |                     112 |
| Pakistan              | Natural Sciences             |     8 |                        4 |                    75.5 |
| Pakistan              | Other                        |     4 |                     22.5 |                   108.5 |
| Portugal              | Social & Behavioral Sciences |     1 |                       23 |                      98 |
| Rwanda                | Medical & Allied             |     2 |                       30 |                     107 |
| Rwanda                | Natural Sciences             |     1 |                        4 |                      76 |
| Somalia               | Medical & Allied             |    14 |                      1.5 |                    68.5 |
| Somalia               | Natural Sciences             |    23 |                        2 |                      69 |
| Somalia               | Other                        |     1 |                        1 |                      65 |
| Sri Lanka             | Medical & Allied             |    17 |                       38 |                     115 |
| Sri Lanka             | Natural Sciences             |    90 |                       50 |                     121 |
| Sri Lanka             | Other                        |    16 |                     32.5 |                   114.5 |
| Sri Lanka             | Social & Behavioral Sciences |     1 |                       94 |                     177 |
| Sudan                 | Education                    |     1 |                        7 |                      86 |
| Sudan                 | Medical & Allied             |     5 |                       -1 |                      61 |
| Sudan                 | Natural Sciences             |     3 |                        3 |                      72 |
| Sudan                 | Other                        |     3 |                        9 |                      82 |
| Sudan                 | Social & Behavioral Sciences |     2 |                       16 |                    90.5 |
| Sweden                | Medical & Allied             |     1 |                       45 |                     133 |
| Sweden                | Other                        |     1 |                       26 |                     103 |
| Syria                 | Medical & Allied             |     1 |                       54 |                     132 |
| Taiwan                | Education                    |     9 |                       25 |                     105 |
| Taiwan                | Engineering & Technology     |     1 |                       77 |                     153 |
| Taiwan                | Medical & Allied             |    33 |                       21 |                     109 |
| Taiwan                | Natural Sciences             |     8 |                       14 |                   126.5 |
| Taiwan                | Other                        |    11 |                       29 |                   121.5 |
| Taiwan                | Social & Behavioral Sciences |     3 |                       96 |                     159 |
| Thailand              | Education                    |    27 |                       20 |                     107 |
| Thailand              | Engineering & Technology     |    21 |                       30 |                     109 |
| Thailand              | Medical & Allied             |   365 |                       15 |                      92 |
| Thailand              | Natural Sciences             |    68 |                       27 |                     102 |
| Thailand              | Other                        |    83 |                       20 |                      99 |
| Thailand              | Social & Behavioral Sciences |    16 |                      5.5 |                    80.5 |
| United Kingdom        | Medical & Allied             |     5 |                       85 |                     156 |
| United Kingdom        | Natural Sciences             |     9 |                       83 |                     152 |
| United Kingdom        | Other                        |     1 |                       74 |                     159 |
| United Kingdom        | Social & Behavioral Sciences |     3 |                       62 |                     137 |
| United States         | Education                    |     7 |                       45 |                     128 |
| United States         | Engineering & Technology     |    10 |                       89 |                     172 |
| United States         | Medical & Allied             |    95 |                       51 |                     128 |
| United States         | Natural Sciences             |   120 |                       85 |                     160 |
| United States         | Other                        |    67 |                       76 |                     152 |
| United States         | Social & Behavioral Sciences |    41 |                       73 |                     148 |
| Vietnam               | Natural Sciences             |     1 |                       93 |                     175 |
| Vietnam               | Other                        |     2 |                     62.5 |                   141.5 |
| Yemen                 | Medical & Allied             |     1 |                       38 |                     114 |


### Year Distribution by Citizenship

**Year distribution by citizenship (counts)**

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
| Filipino              |   1562 |   1551 |   2048 |   3250 |   3675 |   4412 |   4756 |   4863 |   6203 |
| Foreign (unspecified) |     10 |      7 |     13 |     19 |     13 |      9 |      7 |     17 |     12 |
| Germany               |      1 |      0 |      1 |      0 |      1 |      0 |      1 |      0 |      0 |
| Ghana                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      2 |      9 |
| Guam                  |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |
| India                 |     43 |    187 |    180 |    140 |     89 |     44 |    147 |    337 |   1431 |
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
| Portugal              |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| Rwanda                |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |      1 |
| Somalia               |      0 |      0 |      0 |      0 |      0 |      3 |     15 |      6 |     14 |
| Sri Lanka             |      0 |      1 |      0 |      7 |     12 |     36 |     26 |     22 |     20 |
| Sudan                 |      2 |      2 |      0 |      1 |      0 |      1 |      3 |      1 |      4 |
| Sweden                |      0 |      0 |      1 |      0 |      1 |      0 |      0 |      0 |      0 |
| Syria                 |      0 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
| Taiwan                |      7 |     11 |      7 |     10 |      7 |      1 |      6 |      4 |     12 |
| Thailand              |     17 |     24 |     26 |     63 |     56 |    105 |     88 |    102 |     99 |
| United Kingdom        |      0 |      0 |      3 |      0 |      5 |      1 |      4 |      3 |      2 |
| United States         |     19 |     18 |     42 |     54 |     55 |     28 |     51 |     40 |     33 |
| Vietnam               |      0 |      1 |      0 |      2 |      0 |      0 |      0 |      0 |      0 |
| Yemen                 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |


---
## Comparative Analysis: Foreigners vs Filipino Students

Compares (1) actual foreigners (non-Filipino, identified via the profiling CSV), (2) Filipinos whose undergraduate degree was from a foreign/international school, (3) all students whose undergraduate degree was from a public school, and (4) all students whose undergraduate degree was from a private school. Groups 1 and 2 come from the profiling-matched observable university subset (`uniobservable`, no PLE-status filter). Groups 3 and 4 use all observable best-record examinees at those institution types (`bestobservable`). **UNDERGRAD_UNI_TYPE / UNDERGRAD_UNIVERSITY record the examinee's undergraduate (pre-NMAT) school, not the medical school they later attended between the NMAT and the licensure exam** -- no medical-school identifier exists in this dataset, so the linkage-rate differences below cannot be attributed to medical-school quality.

**population:** union of the four comparison groups | **n:** 73,293

"PLE linkage rate %" is the share of each group found in the PLE passer source list (IS_PLE_PASSER) -- it is a LINKAGE rate, not a licensure pass rate, since the source contains passers only and absence does not mean failure.

**Summary: key score indicators by comparison group**

| Group                         |     n |   median_percentile_rank |   q25_pct |   q75_pct |   median_raw_score |   PLE linkage rate % |
|:------------------------------|------:|-------------------------:|----------:|----------:|-------------------:|---------------------:|
| Filipinos (foreign undergrad) |   643 |                       66 |        35 |        86 |                137 |                35.89 |
| Filipinos (private undergrad) | 52317 |                       50 |        25 |        76 |                123 |                44.98 |
| Filipinos (public undergrad)  | 14410 |                       66 |        35 |        90 |                137 |                49.35 |
| Foreigners (non-Filipino)     |  5159 |                       23 |         4 |        53 |                100 |                 2.49 |


**Percentile rank distribution by group (five-number summary; underlies the dashboard boxplot)**

| Group                         |   min |   q1 |   median |   q3 |   max |     n |   outliers |
|:------------------------------|------:|-----:|---------:|-----:|------:|------:|-----------:|
| Filipinos (foreign undergrad) |    -1 |   35 |       66 |   86 |    99 |   643 |          0 |
| Filipinos (private undergrad) |    -1 |   25 |       50 |   76 |    99 | 52317 |          0 |
| Filipinos (public undergrad)  |    -1 |   35 |       66 |   90 |    99 | 14410 |          0 |
| Foreigners (non-Filipino)     |    -1 |    4 |       23 |   53 |    99 |  5159 |          0 |


**TRUE raw score distribution by group (five-number summary; underlies the dashboard boxplot)**

| Group                         |   min |   q1 |   median |     q3 |   max |     n |   outliers |
|:------------------------------|------:|-----:|---------:|-------:|------:|------:|-----------:|
| Filipinos (foreign undergrad) |    38 |  110 |      137 | 160.25 |   219 |   652 |          0 |
| Filipinos (private undergrad) |    10 |  103 |      123 |    146 |   227 | 52787 |        116 |
| Filipinos (public undergrad)  |     9 |  111 |      137 |    166 |   231 | 14638 |          7 |
| Foreigners (non-Filipino)     |     9 |   77 |      100 |    124 |   223 |  5162 |         35 |


**Bin distribution by comparison group (row %, B1-B10; underlies the dashboard heatmap and stacked bar)**

| Group                         |    B1 |    B2 |   B3 |    B4 |    B5 |   B6 |    B7 |    B8 |    B9 |   B10 |
|:------------------------------|------:|------:|-----:|------:|------:|-----:|------:|------:|------:|------:|
| Filipinos (foreign undergrad) |  8.27 |   6.4 | 6.24 |  7.02 |  5.62 | 9.36 | 11.39 | 11.39 | 13.88 | 20.44 |
| Filipinos (private undergrad) | 10.46 |  9.18 | 9.16 | 10.16 | 10.28 |  9.7 |  9.44 |  9.83 | 10.18 | 11.61 |
| Filipinos (public undergrad)  |  8.18 |  6.56 | 6.18 |  7.29 |  7.56 | 7.68 |  9.04 |  9.86 | 12.34 |  25.3 |
| Foreigners (non-Filipino)     | 30.95 | 12.42 | 9.75 |  9.48 |  8.14 |  6.7 |  5.72 |  5.41 |  5.51 |  5.93 |

