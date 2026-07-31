# Page 5: University Type Analysis (Page 05)

**Generated:** 2026-07-31 16:31

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `uni`

**Filters:** None (full unfiltered dataset)

---

**Subset:** besttrend filtered to UNDERGRAD_UNI_TYPE in [Public, Private, Foreign]

**Total records:** 130,494

---

## 1. UNDERGRAD_UNI_TYPE Distribution by UNDERGRAD_UNI_LOCATION

### 1a. Institution type by location mix

**Table 05-1. Institution type by location mix**

| UNDERGRAD_UNI_TYPE   | UNDERGRAD_UNI_LOCATION   |   Count |   Percent of Total |
|:---------------------|:-------------------------|--------:|-------------------:|
| Foreign              | International            |    1860 |               1.43 |
| Private              | Local                    |  101400 |               77.7 |
| Public               | Local                    |   27234 |              20.87 |

### 1b. Count matrix with margins

**Table 05-2. UNDERGRAD_UNI_TYPE x UNDERGRAD_UNI_LOCATION count matrix (with totals)**

| UNDERGRAD_UNI_TYPE   |   International |   Local |    All |
|:---------------------|----------------:|--------:|-------:|
| Foreign              |            1860 |       0 |   1860 |
| Private              |               0 |  101400 | 101400 |
| Public               |               0 |   27234 |  27234 |
| All                  |            1860 |  128634 | 130494 |

### 1c. Row percentages (within UNDERGRAD_UNI_TYPE)

**Table 05-3. Row percentages: within UNDERGRAD_UNI_TYPE**

| UNDERGRAD_UNI_TYPE   |   International |   Local |
|:---------------------|----------------:|--------:|
| Foreign              |             100 |       0 |
| Private              |               0 |     100 |
| Public               |               0 |     100 |

### 1d. Column percentages (within UNDERGRAD_UNI_LOCATION)

**Table 05-4. Column percentages: within UNDERGRAD_UNI_LOCATION**

| UNDERGRAD_UNI_TYPE   |   International |   Local |
|:---------------------|----------------:|--------:|
| Foreign              |             100 |       0 |
| Private              |               0 |   78.83 |
| Public               |               0 |   21.17 |

---

## 2. Bin Distribution by UNDERGRAD_UNI_TYPE

### 2a. Bin counts by UNDERGRAD_UNI_TYPE

**Table 05-5. Bin counts by university type**

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |    B4 |    B5 |    B6 |   B7 |   B8 |   B9 |   B10 |   Total |
|:---------------------|------:|-----:|-----:|------:|------:|------:|-----:|-----:|-----:|------:|--------:|
| Foreign              |   262 |  174 |  140 |   176 |   145 |   164 |  161 |  175 |  197 |   266 |    1860 |
| Private              | 12205 | 9823 | 9127 | 10061 | 10044 | 10079 | 9602 | 9821 | 9864 | 10774 |  101400 |
| Public               |  2949 | 2228 | 2058 |  2247 |  2320 |  2421 | 2478 | 2606 | 3051 |  4876 |   27234 |

### 2b. Bin percentages by UNDERGRAD_UNI_TYPE

**Table 05-6. Row percentages (within UNDERGRAD_UNI_TYPE) across percentile bins**

| UNDERGRAD_UNI_TYPE   |    B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |    B9 |   B10 |
|:---------------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|
| Foreign              | 14.09 | 9.35 | 7.53 | 9.46 |  7.8 | 8.82 | 8.66 | 9.41 | 10.59 |  14.3 |
| Private              | 12.04 | 9.69 |    9 | 9.92 | 9.91 | 9.94 | 9.47 | 9.69 |  9.73 | 10.63 |
| Public               | 10.83 | 8.18 | 7.56 | 8.25 | 8.52 | 8.89 |  9.1 | 9.57 |  11.2 |  17.9 |

---

## 3. Top Bin Share (B8-B10) by UNDERGRAD_UNI_TYPE

**Table 05-7. Top bin (B8-B10) share by university type**

| UNDERGRAD_UNI_TYPE   |   Total N |   Top Bin (B8-B10) Count |   Top Bin Share (%) |
|:---------------------|----------:|-------------------------:|--------------------:|
| Foreign              |      1860 |                      638 |                34.3 |
| Private              |    101400 |                    30459 |               30.04 |
| Public               |     27234 |                    10533 |               38.68 |

### 3b. Top bin share by UNDERGRAD_UNI_TYPE x UNDERGRAD_UNI_LOCATION

**Table 05-8. Top bin (B8-B10) share by institution type x location**

| UNDERGRAD_UNI_TYPE   | UNDERGRAD_UNI_LOCATION   |   Total N |   Top Bin Count |   Top Bin Share (%) |
|:---------------------|:-------------------------|----------:|----------------:|--------------------:|
| Foreign              | International            |      1860 |             638 |                34.3 |
| Private              | Local                    |    101400 |           30459 |               30.04 |
| Public               | Local                    |     27234 |           10533 |               38.68 |

---

## 4. Foreign Examinee Summary

### 4a. Foreign examinee overview (UNDERGRAD_UNI_TYPE = Foreign)

- **Foreign examinees (besttrend):** 1,860
- **Percent of total (uni subset):** 1.43%
- **Median percentile:** 52.0
- **Top bin share (B8-B10):** 34.30%

### 4b. Foreign examinees by FOREIGNER_STATUS

**Table 05-9. Foreign examinee summary by FOREIGNER_STATUS**

| FOREIGNER_STATUS   |    N |   Median Percentile |   Median Raw Total |   Top Bin (B8-B10) Rate |
|:-------------------|-----:|--------------------:|-------------------:|------------------------:|
| Filipino           | 1134 |                  60 |                130 |                   40.56 |
| Likely Foreigner   |   13 |                  27 |                103 |                   30.77 |
| Verified Foreigner |  713 |                  36 |                114 |                    24.4 |

### 4c. FOREIGNER_STATUS x UNDERGRAD_UNI_TYPE cross-tabulation

**Table 05-10. FOREIGNER_STATUS by UNDERGRAD_UNI_TYPE (all types)**

| UNDERGRAD_UNI_TYPE   | FOREIGNER_STATUS   |     N |   Median Percentile |   Median Raw Total |
|:---------------------|:-------------------|------:|--------------------:|-------------------:|
| Foreign              | Filipino           |  1134 |                  60 |                130 |
| Foreign              | Likely Foreigner   |    13 |                  27 |                103 |
| Foreign              | Verified Foreigner |   713 |                  36 |                114 |
| Private              | Filipino           | 84055 |                  54 |                125 |
| Private              | Verified Foreigner | 17345 |                  24 |                 99 |
| Public               | Filipino           | 23011 |                  63 |                133 |
| Public               | Verified Foreigner |  4223 |                  24 |                 99 |

**Table 05-11. Bin distribution among foreign examinees by FOREIGNER_STATUS**

| FOREIGNER_STATUS   |    B1 |    B2 |    B3 |    B4 |   B5 |   B6 |    B7 |    B8 |    B9 |   B10 |
|:-------------------|------:|------:|------:|------:|-----:|-----:|------:|------:|------:|------:|
| Filipino           |  8.55 |  8.02 |  6.44 |  9.61 | 6.88 | 9.88 | 10.05 | 11.46 | 12.26 | 16.84 |
| Likely Foreigner   | 23.08 | 15.38 | 15.38 | 15.38 |    0 |    0 |     0 | 15.38 |     0 | 15.38 |
| Verified Foreigner | 22.72 | 11.36 |  9.12 |  9.12 |  9.4 | 7.29 |  6.59 |  6.03 |  8.13 | 10.24 |

---

## 5. Descriptive Statistics by UNDERGRAD_UNI_TYPE

**Table 05-12. Descriptive statistics by university type**

| UNDERGRAD_UNI_TYPE   |      N |   Median Percentile |   Mean Percentile |   Std Percentile |   Median Raw Total |   Mean Raw Total |   Std Raw Total |   Median GPS |   Median APT |   Median SA |   Q25 Percentile |   Q75 Percentile |   Q25 Raw Total |   Q75 Raw Total |
|:---------------------|-------:|--------------------:|------------------:|-----------------:|-------------------:|-----------------:|----------------:|-------------:|-------------:|------------:|-----------------:|-----------------:|----------------:|----------------:|
| Public               |  27234 |                  57 |             54.56 |            31.09 |                127 |           128.91 |           34.83 |          518 |          517 |         516 |               27 |               83 |             103 |             154 |
| Private              | 101400 |                  49 |             48.99 |            29.51 |                121 |           121.94 |           30.73 |          498 |          503 |         494 |               23 |               75 |              99 |             143 |
| Foreign              |   1860 |                  52 |             50.43 |            31.38 |                124 |           125.34 |           34.47 |        504.5 |        503.5 |         503 |               21 |               79 |              99 |             150 |

### 5b. Median standard subtest scores by UNDERGRAD_UNI_TYPE

**Table 05-13. Median standard subtest scores by university type**

| Subtest      |   Public (n=27,234) |   Private (n=101,400) |   Foreign (n=1,860) |
|:-------------|--------------------:|----------------------:|--------------------:|
| Verbal       |                 515 |                   500 |                 499 |
| Inductive    |                 529 |                   516 |                 523 |
| Quantitative |                 515 |                   500 |                 512 |
| Perceptual   |                 523 |                   512 |                 500 |
| Biology      |                 515 |                   494 |                 500 |
| Physics      |                 523 |                   500 |                 512 |
| Social       |                 510 |                   500 |                 494 |
| Chemistry    |                 511 |                   494 |                 500 |

### 5c. Median raw subtest scores by UNDERGRAD_UNI_TYPE

**Table 05-14. Median raw subtest scores by university type**

| Subtest      |   Public (n=27,232) |   Private (n=101,368) |   Foreign (n=1,855) |
|:-------------|--------------------:|----------------------:|--------------------:|
| Verbal       |                  16 |                    16 |                  16 |
| Inductive    |                  18 |                    18 |                  18 |
| Quantitative |                  15 |                    14 |                  15 |
| Perceptual   |                  18 |                    17 |                  17 |
| Biology      |                  16 |                    14 |                  15 |
| Physics      |                  14 |                    13 |                  14 |
| Social       |                  16 |                    15 |                  15 |
| Chemistry    |                  15 |                    13 |                  14 |

---

## 6. Kruskal-Wallis Test: UNDERGRAD_UNI_TYPE x NMS_PER_num

### 6a. Omnibus test

**Table 05-15. Kruskal-Wallis test result**

| Score Variable                |   H-statistic |      p-value |   Eta-squared | Effect Size   |   Groups compared |   Total N |
|:------------------------------|--------------:|-------------:|--------------:|:--------------|------------------:|----------:|
| NMS_PER_num (Percentile Rank) |       762.139 | 3.18844e-166 |        0.0058 | Negligible    |                 3 |    130494 |

### 6b. Post-hoc pairwise comparisons (Mann-Whitney U)

**Table 05-16. Post-hoc Mann-Whitney U pairwise comparisons**

| Group 1   | Group 2   |   U-statistic |      p-value |   Effect size (r) |     N1 |     N2 |
|:----------|:----------|--------------:|-------------:|------------------:|-------:|-------:|
| Public    | Private   |   1.53101e+09 | 7.00871e-168 |           -0.1088 |  27234 | 101400 |
| Public    | Foreign   |   2.72905e+07 |   2.1256e-08 |           -0.0775 |  27234 |   1860 |
| Private   | Foreign   |   9.16838e+07 |    0.0398492 |            0.0278 | 101400 |   1860 |

### 6c. Kruskal-Wallis by subtest (standard scores)

**Table 05-17. Kruskal-Wallis tests by subtest (standard scores)**

| Subtest      |   H-statistic |      p-value |   Eta-squared |   Groups |   Total N |
|:-------------|--------------:|-------------:|--------------:|---------:|----------:|
| Verbal       |       243.758 |  1.17144e-53 |        0.0019 |        3 |    130494 |
| Inductive    |       272.773 |  5.86336e-60 |        0.0021 |        3 |    130494 |
| Quantitative |       624.473 | 2.49664e-136 |        0.0048 |        3 |    130494 |
| Perceptual   |       152.684 |  7.00152e-34 |        0.0012 |        3 |    130494 |
| Biology      |       921.439 | 8.16625e-201 |         0.007 |        3 |    130494 |
| Physics      |       802.081 | 6.76683e-175 |        0.0061 |        3 |    130494 |
| Social       |       298.982 |  1.19347e-65 |        0.0023 |        3 |    130494 |
| Chemistry    |       932.624 | 3.04219e-203 |        0.0071 |        3 |    130494 |

---

## 7. Medical & Allied vs Other Courses by UNDERGRAD_UNI_TYPE

Stacked percentages sum to 100% within each university type. Uses 133,477 examinees (does not require a percentile bin — dashboard.py Figure 16).

**Figure 16 data. Medical & Allied vs Other Courses by university type (row %)**

| UNDERGRAD_UNI_TYPE   |   Medical & Allied |   Other Courses |
|:---------------------|-------------------:|----------------:|
| Foreign              |              40.38 |           59.62 |
| Private              |              49.54 |           50.46 |
| Public               |              41.22 |           58.78 |

---

## 8. University Listings by UNDERGRAD_UNI_TYPE

Each row is the standardized university name, cleaned location, and applicant count, over 133,477 examinees (does not require a percentile bin, so this includes applicants dropped from the bin-dependent tables above — dashboard.py Table 17).

### 8.1 Public Universities (215 institutions, 27,916 applicants)

**Table 17 (Public, first 200 of 215)**

| UNDERGRAD_UNIVERSITY                                                                | UNDERGRAD_UNI_LOCATION   |   total_applicants |
|:------------------------------------------------------------------------------------|:-------------------------|-------------------:|
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              | Local                    |               3629 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             | Local                    |               3238 |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           | Local                    |               2458 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       | Local                    |               1386 |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           | Local                    |               1321 |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                | Local                    |               1245 |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    | Local                    |               1238 |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          | Local                    |               1185 |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  | Local                    |               1005 |
| WESTERN MINDANAO STATE UNIVERSITY                                                   | Local                    |                863 |
| BICOL UNIVERSITY - MAIN                                                             | Local                    |                740 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              | Local                    |                693 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             | Local                    |                674 |
| NOT SPECIFIED/UNLISTED                                                              | Local                    |                513 |
| UNIVERSITY OF THE PHILIPPINES - LOS BANOS LAGUNA                                    | Local                    |                487 |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            | Local                    |                363 |
| WEST VISAYAS STATE UNIVERSITY ILOILO                                                | Local                    |                360 |
| CEBU NORMAL UNIVERSITY                                                              | Local                    |                356 |
| MINDANAO STATE UNIVERSITY MARAWI CITY                                               | Local                    |                344 |
| CENTRAL MINDANAO UNIVERSITY                                                         | Local                    |                327 |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              | Local                    |                313 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           | Local                    |                304 |
| PALAWAN STATE UNIVERSITY                                                            | Local                    |                253 |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     | Local                    |                244 |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  | Local                    |                241 |
| MINDANAO STATE UNIVERSITY ILIGAN CITY                                               | Local                    |                203 |
| BULACAN STATE UNIVERSITY - MAIN                                                     | Local                    |                201 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO CITY                                         | Local                    |                195 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS ILOILO                                      | Local                    |                182 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       | Local                    |                171 |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          | Local                    |                158 |
| WESTERN MINDANAO STATE UNIVERSITY ZAMBOANGA CITY                                    | Local                    |                145 |
| BENGUET STATE UNIVERSITY - MAIN                                                     | Local                    |                142 |
| CENTRAL LUZON STATE UNIVERSITY                                                      | Local                    |                140 |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                  | Local                    |                140 |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              | Local                    |                138 |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                              | Local                    |                121 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       | Local                    |                118 |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   | Local                    |                107 |
| CAVITE STATE UNIVERSITY - MAIN                                                      | Local                    |                 72 |
| LEYTE NORMAL UNIVERSITY                                                             | Local                    |                 71 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                               | Local                    |                 63 |
| CATANDUANES STATE COLLEGE - MAIN                                                    | Local                    |                 59 |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                 | Local                    |                 56 |
| UNIVERSITY OF MAKATI                                                                | Local                    |                 56 |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                                          | Local                    |                 53 |
| UNIVERSITY OF THE PHILIPPINES - TACLOBAN                                            | Local                    |                 49 |
| BICOL UNIVERSITY - TABACO                                                           | Local                    |                 48 |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            | Local                    |                 48 |
| UNIVERSITY OF THE PHILIPPINES - CEBU COLLEGE                                        | Local                    |                 46 |
| BICOL UNIVERSITY                                                                    | Local                    |                 46 |
| CENTRAL MINDANAO UNIVERSITY BUKIDNON                                                | Local                    |                 43 |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                             | Local                    |                 40 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS CEBU                                   | Local                    |                 37 |
| VISAYAS STATE UNIVERSITY - MAIN                                                     | Local                    |                 36 |
| BATANGAS STATE UNIVERSITY - MAIN                                                    | Local                    |                 35 |
| MINDANAO STATE UNIVERSITY GENERAL SANTOS CITY                                       | Local                    |                 33 |
| MARIANO MARCOS STATE UNIVERSITY ILOCOS NORTE                                        | Local                    |                 33 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES-DAVAO CITY                                   | Local                    |                 30 |
| CARAGA STATE UNIVERSITY - MAIN                                                      | Local                    |                 29 |
| UNIVERSIDAD DE MANILA                                                               | Local                    |                 29 |
| SULU STATE COLLEGE                                                                  | Local                    |                 27 |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  | Local                    |                 27 |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                         | Local                    |                 27 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA             | Local                    |                 26 |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                               | Local                    |                 24 |
| UNIVERSITY OF SOUTHERN MINDANAO NORTH COTABATO                                      | Local                    |                 24 |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                              | Local                    |                 24 |
| BENGUET STATE UNIVERSITY                                                            | Local                    |                 23 |
| TARLAC STATE UNIVERSITY                                                             | Local                    |                 23 |
| BICOL UNIVERSITY COLLEGE OF SCIENCE LEGAZPI CITY                                    | Local                    |                 22 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - SOUTH LA UNION                       | Local                    |                 19 |
| CENTRAL LUZON STATE UNIVERSITY NUEVA ECIJA                                          | Local                    |                 18 |
| PAMANTASAN NG LUNGSOD NG PASIG                                                      | Local                    |                 18 |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                | Local                    |                 18 |
| SAMAR STATE UNIVERSITY - MAIN                                                       | Local                    |                 18 |
| BICOL UNIVERSITY COLLEGE OF NURSING LEGAZPI CITY                                    | Local                    |                 17 |
| BUKIDNON STATE UNIVERSITY                                                           | Local                    |                 17 |
| BULACAN STATE UNIVERSITY                                                            | Local                    |                 17 |
| UNIVERSITY OF EASTERN PHILIPPINES - SAMAR                                           | Local                    |                 16 |
| GORDON COLLEGE                                                                      | Local                    |                 15 |
| ILOCOS SUR COMMUNITY COLLEGE - BANTAY ILOCOS SUR                                    | Local                    |                 15 |
| PALAWAN STATE UNIVERSITY PUERTO PRINCESA CITY                                       | Local                    |                 15 |
| URDANETA CITY UNIVERSITY                                                            | Local                    |                 14 |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                   | Local                    |                 14 |
| AKLAN STATE UNIVERSITY - MAIN                                                       | Local                    |                 14 |
| BICOL UNIVERSITY - DARAGA                                                           | Local                    |                 13 |
| BICOL UNIVERSITY - POLANGUI                                                         | Local                    |                 12 |
| UNIVERSITY OF THE PHILIPPINES - PAMPANGA                                            | Local                    |                 12 |
| NORTHERN NEGROS STATE COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                      | Local                    |                 11 |
| PHILIPPINE NORMAL COLLEGE TAFT AVENUE MANILA                                        | Local                    |                 11 |
| UNIVERSITY OF THE PHILIPPINES SCH. OF HEALTH SCIENCES -LEYTE                        | Local                    |                 11 |
| MARIANO MARCOS STATE UNIVERSITY - COLLEGE OF EDUCATION - LAOAG CITY                 | Local                    |                 11 |
| CAMARINES NORTE STATE COLLEGE - MAIN                                                | Local                    |                 10 |
| SULTAN KUDARAT STATE UNIVERSITY - TACURONG                                          | Local                    |                 10 |
| SULTAN KUDARAT STATE UNIVERSITY - MAIN                                              | Local                    |                 10 |
| JOSE RIZAL MEMORIAL STATE UNIVERSITY - MAIN                                         | Local                    |                  9 |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - LAGUNA COLLEGE OF ARTS AND TRADES - STA. CRUZ | Local                    |                  9 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                | Local                    |                  9 |
| ISABELA STATE UNIVERSITY - ILAGAN                                                   | Local                    |                  9 |
| UNIVERSITY OF RIZAL SYSTEM - MORONG                                                 | Local                    |                  9 |
| NUEVA ECIJA UNIVERSITY OF SCIENCE AND TECHNOLOGY - MAIN                             | Local                    |                  9 |
| WESTERN VISAYAS COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                            | Local                    |                  9 |
| MINDANAO UNIVERSITY OF SCIENCE AND TECHNOLOGY                                       | Local                    |                  8 |
| U.P. VISAYAS (TACLOBAN CITY LEYTE)                                                  | Local                    |                  8 |
| UNIVERSITY OF NORTHERN PHILIPPINES VIGAN ILOCOS SUR                                 | Local                    |                  8 |
| NAVAL STATE UNIVERSITY - MAIN                                                       | Local                    |                  7 |
| NEGROS ORIENTAL STATE UNIVERSITY                                                    | Local                    |                  7 |
| PAMANTASAN NG LUNGSOD NG PASAY                                                      | Local                    |                  7 |
| CATANDUANES STATE COLLEGE                                                           | Local                    |                  7 |
| EASTERN SAMAR STATE UNIVERSITY - MAIN                                               | Local                    |                  7 |
| LEYTE NORMAL UNIVERSITY TACLOBAN CITY                                               | Local                    |                  6 |
| BATAAN PENINSULA STATE UNIVERSITY                                                   | Local                    |                  6 |
| PHILIPPINE NORMAL UNIVERSITY - AGUSAN                                               | Local                    |                  6 |
| ILOCOS SUR POLYTECHNIC STATE COLLEGE                                                | Local                    |                  6 |
| UNIVERSITY OF CALOOCAN CITY                                                         | Local                    |                  5 |
| UNIVERSITY OF NORTHERN PHILIPPINES-CANDON - CITY OF CANDON ILOCOS SUR               | Local                    |                  5 |
| PAMPANGA AGRICULTURAL COLLEGE                                                       | Local                    |                  5 |
| PAMANTASAN NG LUNGSOD NG MUNTINLUPA                                                 | Local                    |                  5 |
| CAVITE STATE UNIVERSITY CAVITE                                                      | Local                    |                  5 |
| EULOGIO AMANG RODRIGUEZ INSTITUTE OF SCIENCE AND TECHNOLOGY                         | Local                    |                  5 |
| EASTERN VISAYAS STATE UNIVERSITY                                                    | Local                    |                  5 |
| TECHNOLOGICAL UNIVERSITY OF THE PHILIPPINES - AYALA BLVD. MANILA                    | Local                    |                  5 |
| BATANGAS STATE UNIVERSITY BATANGAS CITY                                             | Local                    |                  5 |
| IFUGAO STATE UNIVERSITY - MAIN                                                      | Local                    |                  4 |
| CEBU STATE COLLEGE OF SCIENCE AND TECHNOLOGY-MANDAUE CITY - MANDAUE CITY CEBU       | Local                    |                  4 |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - SAN PABLO CITY                                | Local                    |                  4 |
| UNIVERSITY OF THE PHILIPPINES - OPEN UNIVERSITY                                     | Local                    |                  4 |
| UPM- SCHOOL OF HEALTH SCIENCES PALO LEYTE                                           | Local                    |                  4 |
| PANGASINAN STATE UNIVERSITY                                                         | Local                    |                  4 |
| SURIGAO DEL SUR POLYTECHNIC STATE COLLEGE                                           | Local                    |                  4 |
| NUEVA VIZCAYA STATE UNIVERSITY - BAMBANG                                            | Local                    |                  4 |
| PAMANTASAN NG CABUYAO                                                               | Local                    |                  4 |
| SULTAN KUDARAT POLYTECHNIC STATE COLLEGE                                            | Local                    |                  4 |
| BASILAN STATE COLLEGE                                                               | Local                    |                  3 |
| CAMIGUIN POLYTECHNIC STATE COLLEGE                                                  | Local                    |                  3 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG) - TUGUEGARAO CITY (CAPITAL) CAGAYAN   | Local                    |                  3 |
| ISABELA STATE UNIVERSITY - MAIN                                                     | Local                    |                  3 |
| UNIV. OF SOUTHEASTERN PHIL. BO. OBRERO DAVAO                                        | Local                    |                  3 |
| MINDANAO STATE UNIVERSITY - BUUG COLLEGE                                            | Local                    |                  3 |
| ROMBLON STATE UNIVERSITY - MAIN                                                     | Local                    |                  3 |
| RAMON MAGSAYSAY TECHNOLOGICAL UNIVERSITY - RAMON MAGSAYSAY POLYTECHNIC COLLEGE      | Local                    |                  3 |
| TECHNOLOGICAL UNIVERSITY OF THE PHILIPPINES - VISAYAS                               | Local                    |                  3 |
| PHILIPPINE MILITARY ACADEMY - BAGUIO CITY BENGUET                                   | Local                    |                  3 |
| MINDANAO STATE UNIVERSITY - SULU DEVELOPMENT TECHNICAL COLLEGE                      | Local                    |                  3 |
| MINDANAO STATE UNIVERSITY - NAAWAN                                                  | Local                    |                  3 |
| MARINDUQUE STATE COLLEGE - MAIN                                                     | Local                    |                  3 |
| KALINGA APAYAO STATE COLLEGE KALINGA PROVINCE                                       | Local                    |                  2 |
| JOSEFINA H. CERILLES STATE COLLEGE - PAGADIAN                                       | Local                    |                  2 |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE & TECH.                                     | Local                    |                  2 |
| CITY COLLEGE OF MANILA                                                              | Local                    |                  2 |
| MISAMIS ORIENTAL STATE COLLEGE OF AGRICULTURE AND TECHNOLOGY                        | Local                    |                  2 |
| PHILIPPINE STATE COLLEGE OF AERONAUTICS LAPU-LAPU CITY                              | Local                    |                  2 |
| PARTIDO STATE UNIVERSITY - MAIN                                                     | Local                    |                  2 |
| PAMANTASAN NG LUNGSOD NG VALENZUELA                                                 | Local                    |                  2 |
| VISAYAS UNIVERSITY                                                                  | Local                    |                  2 |
| SURIGAO DEL SUR STATE UNIVERSITY - MAIN                                             | Local                    |                  2 |
| UM DIGOS COLLEGE                                                                    | Local                    |                  2 |
| UNIVERSITY OF RIZAL SYSTEM - MORONG RIZAL                                           | Local                    |                  2 |
| CAPIZ STATE UNIVERSITY - PONTEVEDRA                                                 | Local                    |                  2 |
| CENTRAL BICOL STATE UNIVERSITY OF AGRICULTURE - MAIN                                | Local                    |                  2 |
| CAGAYAN STATE UNIVERSITY - SANCHEZ MIRA                                             | Local                    |                  2 |
| LEYTE STATE UNIVERSITY                                                              | Local                    |                  2 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES - ORIENTAL MINDORO                        | Local                    |                  2 |
| RAMON MAGSAYSAY TECHNOLOGICAL UNIVERSITY                                            | Local                    |                  2 |
| MINDANAO STATE UNIVERSITY - TAWI - TAWI COLLEGE OF TECHNOLOGY AND OCEANOGRAPHY      | Local                    |                  2 |
| NORTH LUZON PHILIPPINES STATE COLLEGE                                               | Local                    |                  2 |
| BULACAN STATE UNIVERSITY - BUSTOS                                                   | Local                    |                  2 |
| CAGAYAN STATE UNIVERSITY - GONZAGA                                                  | Local                    |                  2 |
| BACOLOD CITY COLLEGE                                                                | Local                    |                  1 |
| BAGO CITY COLLEGE                                                                   | Local                    |                  1 |
| BATANGAS STATE UNIVERSITY - ALANGILAN                                               | Local                    |                  1 |
| BATAAN POLYTECHNIC STATE COLLEGE BALANGA CITY                                       | Local                    |                  1 |
| ABRA STATE INSTITUTE OF SCIENCE & TECH. ABRA                                        | Local                    |                  1 |
| AGUSAN DEL SUR STATE COLLEGE OF AGRICULTURE AND TECHNOLOGY                          | Local                    |                  1 |
| COTABATO CITY STATE POLYTECHNIC COLLEGE                                             | Local                    |                  1 |
| BUKIDNON STATE COLLEGE                                                              | Local                    |                  1 |
| CAVITE STATE UNIVERSITY - CARMONA                                                   | Local                    |                  1 |
| CAGAYAN STATE UNIVERSITY - APARRI CAGAYAN                                           | Local                    |                  1 |
| CAGAYAN STATE UNIVERSITY - APARRI                                                   | Local                    |                  1 |
| CAPIZ STATE UNIVERSITY - MAIN                                                       | Local                    |                  1 |
| BATANGAS STATE UNIVERSITY - APOLINARIO R. APACIBLE SCHOOL OF FISHERIES - NASUGBU    | Local                    |                  1 |
| BOHOL ISLAND STATE UNIVERSITY - TAGBILARAN                                          | Local                    |                  1 |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - LOS BAÑOS COLLEGE OF FISHERIES                | Local                    |                  1 |
| KALINGA - APAYAO STATE COLLEGE - MAIN                                               | Local                    |                  1 |
| ISABELA STATE UNIVERSITY - PALANAN                                                  | Local                    |                  1 |
| DAVAO DEL NORTE STATE COLLEGE                                                       | Local                    |                  1 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - MID LA UNION                         | Local                    |                  1 |
| DON HONORIO VENTURA TECHNOLOGICAL STATE UNIVERSITY - MAIN                           | Local                    |                  1 |
| EASTERN SAMAR STATE UNIVERSITY - CAN - AVID                                         | Local                    |                  1 |
| EULOGIO AMANG RODRIGUEZ INSTITUTE OF SCIENCE AND TECHNOLOGY - CAVITE                | Local                    |                  1 |
| PALAWAN STATE UNIVERSITY - SAN RAFAEL PUERTO PRINCESA CITY                          | Local                    |                  1 |
| MINDANAO POLYTECHNIC STATE COLLEGE CAGAYAN DE ORO                                   | Local                    |                  1 |
| MINDANAO STATE UNIVERSITY-SULU                                                      | Local                    |                  1 |
| MSU-SCH. OF MARINE FISHERIES & TECH.- MIS. ORIENTAL                                 | Local                    |                  1 |
| NORTHERN ILOILO POLYTECHNIC STATE COLLEGE - MAIN                                    | Local                    |                  1 |
| NORTHWESTERN MINDANAO STATE COLLEGE OF SCIENCE AND TECHNOLOGY                       | Local                    |                  1 |
| NUEVA VIZCAYA STATE UNIVERSITY BAYOMBONG NUEVA VIZCAYA                              | Local                    |                  1 |
| OCCIDENTAL MINDORO STATE COLLEGE                                                    | Local                    |                  1 |
| RIZAL TECHNOLOGICAL UNIVERSITY - PASIG                                              | Local                    |                  1 |

> Full listing: [05_university_listings_public.csv](05_university_listings_public.csv) (215 rows)

### 8.2 Private Universities (798 institutions, 103,669 applicants)

**Table 17 (Private, first 200 of 798)**

| UNDERGRAD_UNIVERSITY                                                                  | UNDERGRAD_UNI_LOCATION   |   total_applicants |
|:--------------------------------------------------------------------------------------|:-------------------------|-------------------:|
| UNIVERSITY OF SANTO TOMAS                                                             | Local                    |              18038 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA                                             | Local                    |               4528 |
| FAR EASTERN UNIVERSITY                                                                | Local                    |               4309 |
| SAN PEDRO COLLEGE                                                                     | Local                    |               3644 |
| SAINT LOUIS UNIVERSITY                                                                | Local                    |               3221 |
| CEBU DOCTOR'S UNIVERSITY                                                              | Local                    |               2406 |
| DE LA SALLE UNIVERSITY - MANILA                                                       | Local                    |               2242 |
| OUR LADY OF FATIMA UNIVERSITY (FATIMA MEDICAL SCIENCE FOUNDATION) - VALENZUELA        | Local                    |               2041 |
| CENTRO ESCOLAR UNIVERSITY - MANILA                                                    | Local                    |               2022 |
| SOUTHWESTERN UNIVERSITY                                                               | Local                    |               1841 |
| ATENEO DE MANILA UNIVERSITY - QUEZON CITY                                             | Local                    |               1782 |
| VELEZ COLLEGE                                                                         | Local                    |               1750 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS                                                   | Local                    |               1724 |
| DAVAO MEDICAL SCHOOL FOUNDATION                                                       | Local                    |               1665 |
| EMILIO AGUINALDO COLLEGE                                                              | Local                    |               1577 |
| AMA COMPUTER COLLEGE - MAKATI                                                         | Local                    |               1519 |
| ANGELES UNIVERSITY FOUNDATION                                                         | Local                    |               1337 |
| SILLIMAN UNIVERSITY                                                                   | Local                    |               1303 |
| AGO MEDICAL AND EDUCATIONAL CENTER - BICOL CHRISTIAN COLLEGE OF MEDICINE              | Local                    |               1284 |
| XAVIER UNIVERSITY                                                                     | Local                    |               1228 |
| BROKENSHIRE COLLEGE                                                                   | Local                    |               1226 |
| ATENEO DE ZAMBOANGA UNIVERSITY                                                        | Local                    |               1172 |
| FEU - DR. NICANOR REYES MEDICAL FOUNDATION                                            | Local                    |               1151 |
| LYCEUM NORTHWESTERN UNIVERSITY                                                        | Local                    |               1048 |
| UNIVERSITY OF SAN AGUSTIN                                                             | Local                    |                995 |
| ATENEO DE DAVAO UNIVERSITY                                                            | Local                    |                981 |
| DE LA SALLE HEALTH SCIENCES INSTITUTE                                                 | Local                    |                952 |
| TRINITY UNIVERSITY OF ASIA                                                            | Local                    |                897 |
| MANILA CENTRAL UNIVERSITY                                                             | Local                    |                837 |
| ATENEO DE MANILA UNIVERSITY                                                           | Local                    |                751 |
| CENTRAL PHILIPPINE UNIVERSITY                                                         | Local                    |                697 |
| VIRGEN MILAGROSA UNIVERSITY FOUNDATION AND VMU INSTITUTE OF MEDICAL FOUNDATION        | Local                    |                697 |
| ADVENTIST UNIVERSITY OF THE PHILIPPINES                                               | Local                    |                672 |
| SAINT PAUL UNIVERSITY PHILIPPINES                                                     | Local                    |                662 |
| UNIVERSITY OF ST. LA SALLE                                                            | Local                    |                629 |
| UNIVERSITY OF THE IMMACULATE CONCEPTION                                               | Local                    |                601 |
| VELEZ COLLEGE CEBU                                                                    | Local                    |                559 |
| UNIVERSITY OF THE EAST RAMON MAGSAYSAY MEMORIAL MEDICAL CENTER                        | Local                    |                555 |
| UNIVERSITY OF SAN CARLOS                                                              | Local                    |                551 |
| SAN BEDA COLLEGE                                                                      | Local                    |                530 |
| SAN PEDRO COLLEGE DAVAO CITY                                                          | Local                    |                512 |
| MANILA TYTANA COLLEGES                                                                | Local                    |                485 |
| ANGELES UNIVERSITY FOUNDATION ANGELES CITY                                            | Local                    |                481 |
| CENTRO ESCOLAR UNIVERSITY - MAKATI                                                    | Local                    |                472 |
| DOÑA REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION                                   | Local                    |                468 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS CAVITE                                            | Local                    |                456 |
| DAVAO DOCTORS COLLEGE                                                                 | Local                    |                444 |
| LICEO DE CAGAYAN UNIVERSITY                                                           | Local                    |                428 |
| FAR EASTERN UNIVERSITY - NRMF (FAIRVIEW Q.C.)                                         | Local                    |                427 |
| OUR LADY OF FATIMA UNIVERSITY - QUEZON CITY                                           | Local                    |                423 |
| MINDANAO SANITARIUM AND HOSPITAL COLLEGE                                              | Local                    |                393 |
| CENTRO ESCOLAR UNIVERSITY - MENDIOLA MANILA                                           | Local                    |                382 |
| SAINT LOUIS UNIVERSITY - BAGUIO                                                       | Local                    |                380 |
| DE LA SALLE - LIPA                                                                    | Local                    |                365 |
| UNIVERSITY OF THE EAST - MANILA                                                       | Local                    |                352 |
| XAVIER UNIVERSITY CAGAYAN DE ORO CITY                                                 | Local                    |                349 |
| UNIVERSITY OF BAGUIO                                                                  | Local                    |                346 |
| UNIVERSIDAD DE ZAMBOANGA                                                              | Local                    |                323 |
| UNIVERSITY OF THE CORDILLERAS                                                         | Local                    |                310 |
| ST. PAUL UNIVERSITY ILOILO                                                            | Local                    |                305 |
| ILOILO DOCTORS COLLEGE                                                                | Local                    |                303 |
| UNIVERSIDAD DE STA. ISABEL                                                            | Local                    |                302 |
| RIVERSIDE COLLEGE                                                                     | Local                    |                301 |
| MOUNTAIN VIEW COLLEGE                                                                 | Local                    |                294 |
| NOTRE DAME UNIVERSITY                                                                 | Local                    |                277 |
| UNIVERSITY OF NEGROS OCCIDENTAL-RECOLETOS                                             | Local                    |                277 |
| MIRIAM COLLEGE                                                                        | Local                    |                257 |
| UNIVERSITY OF THE VISAYAS                                                             | Local                    |                254 |
| ATENEO DE NAGA UNIVERSITY                                                             | Local                    |                253 |
| SAINT SCHOLASTICA'S COLLEGE TACLOBAN                                                  | Local                    |                250 |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES                                              | Local                    |                250 |
| LYCEUM OF THE PHILIPPINES UNIVERSITY - BATANGAS                                       | Local                    |                249 |
| OUR LADY OF FATIMA UNIVERSITY VALENZUELA CITY                                         | Local                    |                247 |
| LORMA COLLEGES                                                                        | Local                    |                233 |
| SILLIMAN UNIVERSITY DUMAGUETE CITY                                                    | Local                    |                227 |
| SAINT MARY'S UNIVERSITY                                                               | Local                    |                219 |
| CAPITOL MEDICAL CENTER COLLEGES                                                       | Local                    |                217 |
| ST. LOUIS UNIVERSITY BAGUIO CITY                                                      | Local                    |                208 |
| ARELLANO UNIVERSITY - MANILA                                                          | Local                    |                203 |
| COLEGIO SAN AGUSTIN - BACOLOD                                                         | Local                    |                198 |
| NOTRE DAME OF DADIANGAS UNIVERSITY                                                    | Local                    |                198 |
| PERPETUAL HELP COLLEGE OF MANILA                                                      | Local                    |                197 |
| UNIVERSITY OF PERPETUAL HELP - DR. JOSE G. TAMAYO MEDICAL UNIVERSITY                  | Local                    |                196 |
| MAKATI MEDICAL CENTER COLLEGE OF NURSING                                              | Local                    |                191 |
| SOUTHWESTERN UNIVERSITY CEBU                                                          | Local                    |                191 |
| NOTRE DAME OF MARBEL UNIVERSITY                                                       | Local                    |                186 |
| ADAMSON UNIVERSITY                                                                    | Local                    |                184 |
| OUR LADY OF FATIMA UNIVERSITY - ANTIPOLO                                              | Local                    |                175 |
| SAN BEDA COLLEGE MENDIOLA MANILA                                                      | Local                    |                175 |
| NEW ERA UNIVERSITY                                                                    | Local                    |                171 |
| HOLY NAME UNIVERSITY                                                                  | Local                    |                159 |
| ST. PAUL UNIVERSITY - MANILA (ST. PAUL UNIVERITY SYSTEM)                              | Local                    |                159 |
| UNIVERSITY OF SAN CARLOS CEBU CITY                                                    | Local                    |                158 |
| ST. SCHOLASTICA'S COLLEGE                                                             | Local                    |                158 |
| PINES CITY COLLEGES                                                                   | Local                    |                154 |
| UNIVERSITY OF LA SALETTE                                                              | Local                    |                152 |
| SOUTHVILLE INTERNATIONAL SCHOOL AND COLLEGES                                          | Local                    |                151 |
| UNIVERSITY OF ST. LOUIS - TUGUEGARAO                                                  | Local                    |                150 |
| CEBU DOCTORS COLLEGE CEBU CITY                                                        | Local                    |                148 |
| AQUINAS UNIVERSITY OF LEGAZPI                                                         | Local                    |                146 |
| MINDANAO MEDICAL FOUNDATION COLLEGE                                                   | Local                    |                143 |
| UNIVERSITY OF THE EAST (C.M. RECTO MANILA)                                            | Local                    |                143 |
| UNIVERSITY OF CEBU - BANILAD                                                          | Local                    |                140 |
| DE LA SALLE - HEALTH SCIENCES CAMPUS                                                  | Local                    |                136 |
| MISAMIS UNIVERSITY - OZAMIS CITY                                                      | Local                    |                132 |
| REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION TACLOBAN                               | Local                    |                130 |
| ST. PAUL UNIVERSITY - QUEZON CITY                                                     | Local                    |                129 |
| UNIVERSITY OF SAN AGUSTIN - ILOILO CITY                                               | Local                    |                124 |
| GENERAL SANTOS DOCTORS' MEDICAL SCHOOL FOUNDATION                                     | Local                    |                122 |
| COLEGIO DE SAN JUAN DE LETRAN                                                         | Local                    |                121 |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING AND LIBERAL ARTS                          | Local                    |                119 |
| UNIVERSITY OF PANGASINAN                                                              | Local                    |                119 |
| EMILIO AGUINALDO COLLEGE MANILA                                                       | Local                    |                117 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION                                               | Local                    |                117 |
| DIVINE WORD COLLEGE OF LAOAG                                                          | Local                    |                116 |
| WESLEYAN UNIVERSITY - PHILIPPINES (CABANATUAN)                                        | Local                    |                109 |
| ST. PAUL UNIVERSITY - MANILA                                                          | Local                    |                109 |
| CENTRAL LUZON DOCTORS' HOSPITAL EDUCATIONAL INSTITUTION                               | Local                    |                108 |
| UNIVERSITY OF BAGUIO BAGUIO CITY                                                      | Local                    |                106 |
| HOLY ANGEL UNIVERSITY                                                                 | Local                    |                105 |
| CAPITOL UNIVERSITY                                                                    | Local                    |                104 |
| CENTRAL PHILIPPINE UNIVERSITY ILOILO                                                  | Local                    |                104 |
| FEU - EAST ASIA COLLEGE                                                               | Local                    |                101 |
| GLOBAL CITY INNOVATIVE COLLEGE                                                        | Local                    |                101 |
| UNIVERSITY OF ST. LA SALLE BACOLOD CITY                                               | Local                    |                 99 |
| ST. JUDE COLLEGE                                                                      | Local                    |                 95 |
| FATHER SATURNINO M. URIOS UNIVERSITY                                                  | Local                    |                 91 |
| SOUTHWESTERN UNIVERSITY-MATIAS H. AZNAR MEMORIAL COLLEGE OF MEDICINE - CEBU CITY CEBU | Local                    |                 89 |
| UNIVERSITY OF SOUTHERN PHILIPPINES FOUNDATION                                         | Local                    |                 89 |
| UERM MEMORIAL MEDICAL CENTER                                                          | Local                    |                 88 |
| CENTRO ESCOLAR UNIVERSITY AT MALOLOS                                                  | Local                    |                 87 |
| MANILA DOCTORS COLLEGE - PASAY CITY                                                   | Local                    |                 87 |
| ILIGAN MEDICAL CENTER COLLEGE                                                         | Local                    |                 86 |
| COLLEGE OF THE HOLY SPIRIT OF MANILA                                                  | Local                    |                 83 |
| HOLY INFANT COLLEGE                                                                   | Local                    |                 80 |
| SOUTHEAST ASIAN COLLEGE                                                               | Local                    |                 78 |
| EASTER COLLEGE                                                                        | Local                    |                 78 |
| REMEDIOS T. ROMUALDEZ MEM. SCH. - MMC                                                 | Local                    |                 78 |
| DR. CARLOS S. LANTING COLLEGE                                                         | Local                    |                 76 |
| WORLD CITI COLLEGES QUEZON CITY                                                       | Local                    |                 76 |
| VIRGEN MILAGROSA UNIV. FOUNDATION - SAN CARLOS CITY PANG.                             | Local                    |                 76 |
| THE PHILIPPINE WOMEN'S UNIVERSITY SYSTEM - MANILA                                     | Local                    |                 75 |
| METROPOLITAN HOSPITAL COLLEGE OF NURSING                                              | Local                    |                 74 |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE                                                  | Local                    |                 74 |
| BRENT HOSPITAL AND COLLEGES                                                           | Local                    |                 73 |
| ST. ALEXIUS COLLEGE                                                                   | Local                    |                 71 |
| MANILA ADVENTIST MEDICAL CENTER AND COLLEGES                                          | Local                    |                 71 |
| UNIVERSITY OF VISAYAS CEBU                                                            | Local                    |                 69 |
| UNIVERSITY OF NUEVA CACERES                                                           | Local                    |                 67 |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-LAS PIÑAS                                   | Local                    |                 67 |
| NOTRE DAME OF JOLO COLLEGE                                                            | Local                    |                 65 |
| LYCEUM NORTHWESTERN DAGUPAN CITY                                                      | Local                    |                 64 |
| UNIVERSITY OF THE CORDILLERAS (BCF)                                                   | Local                    |                 63 |
| ASSUMPTION COLLEGE                                                                    | Local                    |                 62 |
| LA CONSOLACION COLLEGE - MANILA                                                       | Local                    |                 62 |
| DE LA SALLE - LIPA BATANGAS                                                           | Local                    |                 61 |
| UNIVERSITY OF THE EAST - RAMON MAGSAYSAY MEM. MEDICAL CENTER                          | Local                    |                 60 |
| MANILA DOCTORS COLLEGE U.N. AVENUE MANILA                                             | Local                    |                 59 |
| UNIVERSITY OF SAN JOSE - RECOLETOS                                                    | Local                    |                 58 |
| SACRED HEART COLLEGE OF LUCENA                                                        | Local                    |                 57 |
| BUTUAN DOCTORS COLLEGE                                                                | Local                    |                 57 |
| NOTRE DAME UNIVERSITY COTABATO CITY                                                   | Local                    |                 56 |
| ST. PAUL UNIVERSITY DUMAGUETE                                                         | Local                    |                 55 |
| DIPOLOG MEDICAL CENTER COLLEGE FOUNDATION                                             | Local                    |                 55 |
| OUR LADY OF FATIMA UNIVERSITY - LAGRO QUEZON CITY                                     | Local                    |                 53 |
| MIRIAM COLLEGE FOUNDATION INC.                                                        | Local                    |                 52 |
| BAGUIO CENTRAL UNIVERSITY                                                             | Local                    |                 52 |
| SAN LORENZO RUIZ COLLEGE OF ORMOC                                                     | Local                    |                 51 |
| SOUTH SEED - LPDH COLLEGE                                                             | Local                    |                 50 |
| MINDANAO SANITARIUM & HOSPITAL COLLEGE ILIGAN CITY                                    | Local                    |                 50 |
| NAGA COLLEGE FOUNDATION                                                               | Local                    |                 50 |
| CEBU DOCTOR'S UNIVERSITY COLLEGE OF MEDICINE - MANDAUE CITY CEBU                      | Local                    |                 49 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION INC.                                          | Local                    |                 48 |
| PILAR COLLEGE                                                                         | Local                    |                 47 |
| DE LA SALLE - COLLEGE OF SAINT BENILDE                                                | Local                    |                 47 |
| MAPUA INSTITUTE OF TECHNOLOGY - MANILA                                                | Local                    |                 46 |
| MOUNTAIN VIEW COLLEGE BUKIDNON                                                        | Local                    |                 46 |
| PHILIPPINE WOMEN'S UNIVERSITY TAFT AVENUE MANILA                                      | Local                    |                 46 |
| PHILIPPINE CHRISTIAN UNIVERSITY                                                       | Local                    |                 45 |
| MEDINA COLLEGE                                                                        | Local                    |                 45 |
| LYCEUM OF THE PHILIPPINES - LAGUNA                                                    | Local                    |                 45 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - BINAN LAGUNA                                    | Local                    |                 44 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - LAGUNA                                          | Local                    |                 44 |
| NOTRE DAME OF DADIANGAS COLLEGE GEN. SANTOS                                           | Local                    |                 44 |
| UNIVERSITY OF THE ASSUMPTION                                                          | Local                    |                 44 |
| BROKENSHIRE COLLEGE DAVAO CITY                                                        | Local                    |                 43 |
| UNIVERSITY OF CAGAYAN VALLEY                                                          | Local                    |                 43 |
| UNIVERSITY OF THE VISAYAS - MANDAUE                                                   | Local                    |                 42 |
| FILAMER CHRISTIAN UNIVERSITY                                                          | Local                    |                 41 |
| LA CONSOLACION COLLEGE                                                                | Local                    |                 41 |
| YAMAN LAHI FOUNDATION - EMILIO AGUINALDO COLLEGE                                      | Local                    |                 40 |
| ST. JUDE COLLEGE MANILA                                                               | Local                    |                 39 |
| LOURDES COLLEGE                                                                       | Local                    |                 39 |
| UNIVERSIDAD DE STA. ISABEL NAGA CITY                                                  | Local                    |                 39 |
| UNIVERSITY OF BOHOL                                                                   | Local                    |                 37 |
| NUEVA ECIJA COLLEGES                                                                  | Local                    |                 37 |
| NEW ERA UNIVERSITY QUEZON CITY                                                        | Local                    |                 37 |
| NORTHWESTERN UNIVERSITY                                                               | Local                    |                 36 |
| ILIGAN MEDICAL CENTER ILIGAN CITY                                                     | Local                    |                 36 |
| UNIVERSITY OF LUZON                                                                   | Local                    |                 36 |

> Full listing: [05_university_listings_private.csv](05_university_listings_private.csv) (798 rows)

### 8.3 Foreign Universities (533 institutions, 1,892 applicants)

**Table 17 (Foreign, first 200 of 533)**

| UNDERGRAD_UNIVERSITY                                     | UNDERGRAD_UNI_LOCATION   |   total_applicants |
|:---------------------------------------------------------|:-------------------------|-------------------:|
| RANGSIT UNIVERSITY                                       | International            |                 69 |
| UNIVERSITY OF CALIFORNIA - DAVIS                         | International            |                 43 |
| UNIVERSITY OF CALIFORNIA - IRVINE                        | International            |                 40 |
| TRINITY COLLEGE                                          | International            |                 40 |
| RANGSIT UNIVERSITY THAILAND                              | International            |                 38 |
| MAHIDOL UNIVERSITY                                       | International            |                 36 |
| UNIVERSITY OF CALIFORNIA LOS ANGELES                     | International            |                 30 |
| MAHIDOL UNIVERSITY THAILAND                              | International            |                 28 |
| CHULALONGKORN UNIVERSITY                                 | International            |                 28 |
| CALIFORNIA STATE UNIVERSITY                              | International            |                 27 |
| UNIVERSITY OF CALIFORNIA RIVERSIDE CA USA                | International            |                 25 |
| AL KWARIZMI INTERNATIONAL COLLEGE FOUNDATION             | International            |                 23 |
| UNIVERSITY OF CALIFORNIA - SAN DIEGO                     | International            |                 23 |
| CHIANG MAI UNIVERSITY                                    | International            |                 23 |
| THAMMASAT UNIVERSITY                                     | International            |                 20 |
| UNIVERSITY OF CALIFORNIA-RIVERSIDE                       | International            |                 19 |
| WESTERN STATE UNIVERSITY OF COLORADO                     | International            |                 19 |
| UNIVERSITY OF TORONTO                                    | International            |                 17 |
| UNIVERSITY OF CALIFORNIA BERKELEY                        | International            |                 17 |
| MAE FAH LUANG UNIVERSITY                                 | International            |                 17 |
| CHULALONGKORN UNIVERSITY THAILAND                        | International            |                 17 |
| UNIVERSITY OF WASHINGTON                                 | International            |                 16 |
| NARESUAN UNIVERSITY                                      | International            |                 15 |
| UNIVERSITY OF FLORIDA                                    | International            |                 15 |
| MONAD UNIVERSITY                                         | International            |                 14 |
| UNIVERSITY OF NEVADA LAS VEGAS                           | International            |                 12 |
| UNIVERSITY OF CALIFORNIA SANTA BARBARA                   | International            |                 12 |
| UNIVERSITY OF SAN FRANCISCO                              | International            |                 11 |
| HUACHIEW CHALERMPRAKIET UNIVERSITY                       | International            |                 11 |
| SRINAKHARINWIROT UNIVERSITY                              | International            |                 11 |
| RUTGERS UNIVERSITY NEW JERSEY                            | International            |                 11 |
| RUTGERS UNIVERSITY                                       | International            |                 10 |
| UNIVERSITY OF GUAM                                       | International            |                 10 |
| UNIVERSITAS ADVENT INDONESIA                             | International            |                 10 |
| UNIVERSITY OF CENTRAL FLORIDA                            | International            |                 10 |
| STONY BROOK UNIVERSITY                                   | International            |                  9 |
| CALIFORNIA STATE UNIVERSITY LONG BEACH                   | International            |                  9 |
| CALIFORNIA STATE UNIVERSITY FRESNO                       | International            |                  9 |
| BURAPHA UNIVERSITY                                       | International            |                  9 |
| VIRGINIA COMMONWEALTH UNIVERSITY                         | International            |                  9 |
| UNIVERSITY OF CALIFORNIA AT STA. CRUZ U.S.A.             | International            |                  9 |
| UNIVERSITY OF HAWAII AT MANOA                            | International            |                  9 |
| UNIVERSITY OF ILLINOIS CHICAGO                           | International            |                  9 |
| UNIVERSITY OF CALIFORNIA SANTA CRUZ                      | International            |                  8 |
| THAMMASAT UNIV.                                          | International            |                  8 |
| UNIVERSITY OF BRITISH COLUMBIA                           | International            |                  8 |
| UNIVERSITY OF TEXAS                                      | International            |                  8 |
| RAMKHAMHAENG UNIVERSITY                                  | International            |                  8 |
| PRINCE OF SONGKLA UNIVERSITY                             | International            |                  8 |
| UNIVERSITY OF HOUSTON                                    | International            |                  7 |
| UNIVERSITY OF CALIFORNIA MERCED                          | International            |                  7 |
| UNIVERSITY OF SOUTH FLORIDA USA                          | International            |                  6 |
| EAST AFRICA UNIVERSITY                                   | International            |                  6 |
| UNIVERSITY AT BUFFALO                                    | International            |                  6 |
| KASETSART UNIVERSITY                                     | International            |                  6 |
| RUNGSIT UNIVERSITY                                       | International            |                  6 |
| UNIVERSITY OF MARYLAND - MARYLAND U.S.A.                 | International            |                  6 |
| CHIANGMAI UNIVERSITY                                     | International            |                  6 |
| CALIFORNIA STATE UNIVERSITY - FULLERTON                  | International            |                  6 |
| SAN DIEGO STATE UNIVERSITY - CALIFORNIA U.S.A.           | International            |                  6 |
| MAHASARAKHAM UNIVERSITY                                  | International            |                  6 |
| KHON KAEN UNIVERSITY                                     | International            |                  6 |
| ASSUMPTION UNIVERSITY                                    | International            |                  6 |
| LADOKE AKINTOLA UNIVERSITY OF TECHNOLOGY OGBOMOSO        | International            |                  6 |
| ST. ANDREW'S INTERNATIONAL ACADEMY INDIA                 | International            |                  5 |
| UNIVERSITY OF WISCONSIN-MADISON                          | International            |                  5 |
| UNIVERSITY OF NEVADA - RENO                              | International            |                  5 |
| UNIVERSITY OF MICHIGAN                                   | International            |                  5 |
| UNIVERSITY OF NEW ENGLAND                                | International            |                  5 |
| SUNRISE UNIVERSITY                                       | International            |                  5 |
| UNIVERSITY OF CONNECTICUT                                | International            |                  5 |
| ADVENTIST INDONESIA UNIVERSITY INDONESIA                 | International            |                  5 |
| UNIVERSITY OF TEXAS AT ARLINGTON                         | International            |                  5 |
| ARIZONA STATE UNIVERSITY                                 | International            |                  5 |
| MOGADISHU UNIVERSITY                                     | International            |                  5 |
| KHON KAEN UNIVERSITY THAILAND                            | International            |                  5 |
| KITASATO UNIVERSITY                                      | International            |                  5 |
| TEMPLE UNIVERSITY USA                                    | International            |                  5 |
| SIAM UNIVERSITY                                          | International            |                  5 |
| UNIVERSITY OF BRITISH COLUMBIA CANADA                    | International            |                  5 |
| RAMKHAMHAENG UNIV.                                       | International            |                  5 |
| PENSACOLA CHRISTIAN COLLEGE                              | International            |                  5 |
| NEW YORK UNIVERSITY NY USA                               | International            |                  5 |
| RUTGERS COLLEGE NEW JERSEY                               | International            |                  5 |
| CHAING MAI UNIVERSITY-THAILAND                           | International            |                  5 |
| SRI CHAITANYA JUNIOR COLLEGE                             | International            |                  5 |
| ANAND HOMEOPATHIC MEDICAL COLLEGE AND RESEARCH INSTITUTE | International            |                  4 |
| ANDHRA UNIVERSITY                                        | International            |                  4 |
| RAJAMANGALA UNIVERSITY OF TECHNOLOGY THANYABURI          | International            |                  4 |
| LOYOLA MARYMOUNT UNIVERSITY                              | International            |                  4 |
| BINGHAMTON UNIVERSITY                                    | International            |                  4 |
| UNIVERSITY OF MARYLAND COLLEGE PARK                      | International            |                  4 |
| UNIVERSITY OF SYDNEY                                     | International            |                  4 |
| AZAD UNIVERSITY OF TEHRAN SHAMAL                         | International            |                  4 |
| UNIVERSITY OF WEST FLORIDA                               | International            |                  4 |
| BARUCH COLLEGE                                           | International            |                  4 |
| MADONNA UNIVERSITY                                       | International            |                  4 |
| MEDGAR EVERS COLLEGE                                     | International            |                  4 |
| MMA MATRIC HIGHER SECONDARY SCHOOL                       | International            |                  4 |
| LOYOLA UNIVERSITY CHICAGO U.S.A.                         | International            |                  4 |
| WALAILAK UNIVERSITY                                      | International            |                  4 |
| JOHNS HOPKINS UNIVERSITY                                 | International            |                  4 |
| OPJS UNIVERSITY CHURU                                    | International            |                  4 |
| OLABISI ONABANJO UNVERSITY AGO-IWOYE.                    | International            |                  4 |
| ISLAMIC AZAD UNIVERSITY                                  | International            |                  4 |
| MONASH UNIVERSITY                                        | International            |                  4 |
| SAN DIEGO STATE UNIVERSITY                               | International            |                  4 |
| SRINAKARINWIROTE UNIVERSITY THAILAND                     | International            |                  4 |
| UNIVERSITY OF AUCKLAND                                   | International            |                  4 |
| THE OHIO STATE UNIVERSITY                                | International            |                  4 |
| THE TAMIL NADU DR. M.G.R. MEDICAL UNIVERSITY             | International            |                  4 |
| ST.THERESA INTERNATIONAL COLLEGE                         | International            |                  4 |
| SILPAKORN UNIVERSITY                                     | International            |                  4 |
| UNIVERSITY OF SOUTHERN CALIFORNIA                        | International            |                  4 |
| UNIVERSITY OF SOUTH FLORIDA                              | International            |                  4 |
| BOROMARAJONANI COLLEGE OF NURSING SURIN                  | International            |                  4 |
| UNIVERSITY OF MELBOURNE                                  | International            |                  4 |
| BINGHAM UNIVERSITY                                       | International            |                  4 |
| UNIVERSITY OF IBADAN                                     | International            |                  4 |
| BOSTON UNIVERSITY                                        | International            |                  4 |
| CALIFORNIA STATE UNIVERSITY EAST BAY                     | International            |                  4 |
| UNIVERSITY OF NORTH FLORIDA                              | International            |                  4 |
| SIMON FRASER UNIVERSITY                                  | International            |                  4 |
| GOVERNMENT SCHOOL                                        | International            |                  4 |
| DR.NTR UNIVERSITY OF HEALTH SCIENCE                      | International            |                  4 |
| DREXEL UNIVERSITY                                        | International            |                  4 |
| UNIVERSITY OF ARIZONA                                    | International            |                  4 |
| SJG AYURVEDIC MEDICAL COLLEGE                            | International            |                  4 |
| SRM UNIVERSITY                                           | International            |                  4 |
| DEAKIN UNIVERSITY                                        | International            |                  4 |
| UNIVERSITY OF GHANA                                      | International            |                  4 |
| DR RAM MANOHAR LOHIA AVADH UNIVERSITY FAIZABAD           | International            |                  4 |
| SAN FRANCISCO STATE UNIVERSITY                           | International            |                  4 |
| PRAGATHI DEGREE COLLEGE                                  | International            |                  4 |
| HUACHIEN CHALERMPRAKIET UNIVERSITY THAILAND              | International            |                  4 |
| CHINA MEDICAL COLLEGE                                    | International            |                  3 |
| BHARATI VIDYAPEETH DEEMED UNIVERSITY                     | International            |                  3 |
| CALIFORNIA STATE UNIVERSITY NORTHRIDGE                   | International            |                  3 |
| UNIVERSITY OF ILORIN                                     | International            |                  3 |
| CALIFORNIA STATE UNIVERSITY LOS ANGELES                  | International            |                  3 |
| BAYLOR UNIVERSITY                                        | International            |                  3 |
| BAYLOR UNIVERSITY TEXAS USA                              | International            |                  3 |
| WINONA STATE UNIVERSITY                                  | International            |                  3 |
| YORK UNIVERSITY CANADA                                   | International            |                  3 |
| AMBROSE ALLI UNIVERSITY                                  | International            |                  3 |
| UNIVERSITY OF KENTUCKY - KENTUCKY U.S.A.                 | International            |                  3 |
| BUNDELKHAND UNIVERSITY JHANSI                            | International            |                  3 |
| BOSTON COLLEGE MA USA                                    | International            |                  3 |
| BOWEN UNIVERSITY                                         | International            |                  3 |
| UNIVERSITY OF RAJASTHAN                                  | International            |                  3 |
| UNIVERSITY OF PITTSBURGH USA                             | International            |                  3 |
| UNIVERSITY OF VIRGINIA                                   | International            |                  3 |
| UNIVERSITY OF TEXAS AT AUSTIN                            | International            |                  3 |
| UNIVERSITY OF PORTHARCOURT                               | International            |                  3 |
| UNIVERSITY OF SOUTHERN CALIFORNIA USA                    | International            |                  3 |
| BISHOP HEBER COLLEGE                                     | International            |                  3 |
| SHRIDHAR UNIVERSITY                                      | International            |                  3 |
| HALLYM UNIVERSITY                                        | International            |                  3 |
| UNIVERSITY OF BENIN                                      | International            |                  3 |
| UNIVERSITY OF BRADFORD                                   | International            |                  3 |
| FORDHAM COLLEGE BRONX NEW YORK USA                       | International            |                  3 |
| STANFORD UNIVERSITY CALIFORNIA U.S.A.                    | International            |                  3 |
| DR MGR MEDICAL UNIVERSITY                                | International            |                  3 |
| FRANKLIN & MARSHALL COLLEGE                              | International            |                  3 |
| THE MAHARAJA SAYAJIRAO UNIVERSITY OF BARODA              | International            |                  3 |
| CONSOLATA SCHOOL OF NURSING                              | International            |                  3 |
| CREIGHTON UNIVERSITY                                     | International            |                  3 |
| CALIFORNIA STATE POLYTECHNIC UNIV. CA USA                | International            |                  3 |
| CORNELL UNIVERSITY                                       | International            |                  3 |
| DR NAYAPALI COLLEGE                                      | International            |                  3 |
| HONG KONG METROPOLITAN UNIVERSITY                        | International            |                  3 |
| RAJIV GANDHI UNIVERSITY OF HEALTH SCIENCES               | International            |                  3 |
| OLABISI ONABANJO UNIVERISTY                              | International            |                  3 |
| JAYA COLLEGE OF ARTS AND SCIENCE                         | International            |                  3 |
| NIMS NURSING COLLEGE                                     | International            |                  3 |
| PRINCE OF SONGKHLA UNIVERSITY                            | International            |                  3 |
| GEETANJALI COLLEGE OF NURSHING                           | International            |                  3 |
| IMPHAL COLLEGE                                           | International            |                  3 |
| IMO STATE UNIVERSITY                                     | International            |                  3 |
| PACIFIC UNION COLLEGE                                    | International            |                  3 |
| SANJEEVAN COLLEGE OF PHARMACY                            | International            |                  3 |
| NATIONAL UNIVERSITY OF SINGAPORE                         | International            |                  3 |
| MICHIGAN STATE UNIVERSITY                                | International            |                  3 |
| MIDDLE TENNESSEE STATE UNIVERSITY                        | International            |                  3 |
| NEW YORK UNIVERSITY                                      | International            |                  3 |
| MADHUSUDAN SCHOOL OF NURSING                             | International            |                  3 |
| AMERICAN UNIVERSITY OF NIGERIA                           | International            |                  3 |
| WASHINGTON STATE UNIVERSITY                              | International            |                  3 |
| ALIAH UNIVERSITY                                         | International            |                  2 |
| ADELPHI UNIVERSITY NEW YORK U.S.A.                       | International            |                  2 |
| WESTERN SYDNEY UNIVERSITY                                | International            |                  2 |
| WESTERN UNIVERSITY                                       | International            |                  2 |
| B. R. MIRDHA COLLEGE                                     | International            |                  2 |
| BAPUJI AYURVEDIC MEDICAL COLLEGE                         | International            |                  2 |
| UNIVERSITY OF TEXAS (DALLAS)                             | International            |                  2 |
| UNIVERSITY OF TEXAS SAN ANTONIO                          | International            |                  2 |
| UNIVERSITY OF THE PACIFIC ALBANY CA USA                  | International            |                  2 |
| LOMA LINDA UNIVERSITY RIVERSIDE CA                       | International            |                  2 |
| KAKATIYA UNIVERSITY                                      | International            |                  2 |
| KAMAKHYA PEMTON COLLEGE                                  | International            |                  2 |

> Full listing: [05_university_listings_foreign.csv](05_university_listings_foreign.csv) (533 rows)


---
*Analysis complete. Generated by page_05_university_type.py*
