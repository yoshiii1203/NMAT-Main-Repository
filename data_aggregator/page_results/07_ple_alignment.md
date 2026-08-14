# Page 7: PLE Alignment of NMAT Performance

**Generated:** 2026-08-14 18:07

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `bestobservable`

**Filters:** None (full unfiltered dataset)

---

## 1. Score Profile by PLE Status

Count, median, mean, Q25, and Q75 for each score measure by PLE status.

**Table 23. Score profile by PLE status**

| PLE_STATUS_LABEL       |   TotalRawScoreTRUE_count |   TotalRawScoreTRUE_median |   TotalRawScoreTRUE_mean |   TotalRawScoreTRUE_q25 |   TotalRawScoreTRUE_q75 |   NMS_PER_num_count |   NMS_PER_num_median |   NMS_PER_num_mean |   NMS_PER_num_q25 |   NMS_PER_num_q75 |   NMS_GPS_count |   NMS_GPS_median |   NMS_GPS_mean |   NMS_GPS_q25 |   NMS_GPS_q75 |   NMS_APT_count |   NMS_APT_median |   NMS_APT_mean |   NMS_APT_q25 |   NMS_APT_q75 |   NMS_SA_count |   NMS_SA_median |   NMS_SA_mean |   NMS_SA_q25 |   NMS_SA_q75 |   PartIRawScoreTRUE_count |   PartIRawScoreTRUE_median |   PartIRawScoreTRUE_mean |   PartIRawScoreTRUE_q25 |   PartIRawScoreTRUE_q75 |   PartIIRawScoreTRUE_count |   PartIIRawScoreTRUE_median |   PartIIRawScoreTRUE_mean |   PartIIRawScoreTRUE_q25 |   PartIIRawScoreTRUE_q75 |
|:-----------------------|--------------------------:|---------------------------:|-------------------------:|------------------------:|------------------------:|--------------------:|---------------------:|-------------------:|------------------:|------------------:|----------------:|-----------------:|---------------:|--------------:|--------------:|----------------:|-----------------:|---------------:|--------------:|--------------:|---------------:|----------------:|--------------:|-------------:|-------------:|--------------------------:|---------------------------:|-------------------------:|------------------------:|------------------------:|---------------------------:|----------------------------:|--------------------------:|-------------------------:|-------------------------:|
| Confirmed PLE passer   |                     30104 |                        140 |                   141.37 |                     120 |                     163 |               29510 |                   70 |              65.16 |                46 |                89 |           30105 |              553 |          558.1 |           490 |           626 |           30105 |              549 |         554.47 |           492 |           615 |          30105 |             546 |        547.73 |          484 |          611 |                     30104 |                         74 |                    74.11 |                      64 |                      85 |                      30104 |                          66 |                     67.27 |                       55 |                       79 |
| No confirmed PLE match |                     39356 |                        115 |                   116.87 |                      95 |                     137 |               38663 |                   39 |               43.1 |                17 |                68 |           39398 |              473 |         473.08 |           402 |           545 |           39398 |              484 |         481.17 |           415 |           546 |          39398 |             471 |        475.57 |          409 |          540 |                     39356 |                         62 |                    62.14 |                      51 |                      73 |                      39356 |                          53 |                     54.73 |                       42 |                       65 |


---

## 2. Box-Plot Data by Score and PLE Status

Quantile-based summary for each score variable, split by PLE status.

**Box-plot summary statistics**

| ScoreVariable      | PLE_STATUS_LABEL       |     n |   min |   q05 |   q25 |   median |   mean |   q75 |   q95 |   max |    std |
|:-------------------|:-----------------------|------:|------:|------:|------:|---------:|-------:|------:|------:|------:|-------:|
| TotalRawScoreTRUE  | Confirmed PLE passer   | 30104 |    48 |    95 |   120 |      140 | 141.37 |   163 |   192 |   231 |  29.43 |
| TotalRawScoreTRUE  | No confirmed PLE match | 39356 |     9 |    70 |    95 |      115 | 116.87 |   137 |   171 |   223 |  30.57 |
| NMS_PER_num        | Confirmed PLE passer   | 29510 |     1 |    16 |    46 |       70 |  65.16 |    89 |    98 |    99 |  26.21 |
| NMS_PER_num        | No confirmed PLE match | 38663 |     0 |     3 |    17 |       39 |   43.1 |    68 |    93 |    99 |  29.21 |
| NMS_GPS            | Confirmed PLE passer   | 30105 |   200 |   402 |   490 |      553 |  558.1 |   626 |   726 |   800 |  97.75 |
| NMS_GPS            | No confirmed PLE match | 39398 |     0 |   295 |   402 |      473 | 473.08 |   545 |   653 |   800 | 108.33 |
| NMS_APT            | Confirmed PLE passer   | 30105 |   200 |   404 |   492 |      549 | 554.47 |   615 |   713 |   800 |  92.95 |
| NMS_APT            | No confirmed PLE match | 39398 |   200 |   316 |   415 |      484 | 481.17 |   546 |   645 |   800 | 100.76 |
| NMS_SA             | Confirmed PLE passer   | 30105 |   200 |   398 |   484 |      546 | 547.73 |   611 |   707 |   800 |  92.21 |
| NMS_SA             | No confirmed PLE match | 39398 |     0 |   319 |   409 |      471 | 475.57 |   540 |   642 |   800 |  98.09 |
| PartIRawScoreTRUE  | Confirmed PLE passer   | 30104 |    20 |    50 |    64 |       74 |  74.11 |    85 |    99 |   118 |  15.04 |
| PartIRawScoreTRUE  | No confirmed PLE match | 39356 |     0 |    36 |    51 |       62 |  62.14 |    73 |    90 |   116 |  16.27 |
| PartIIRawScoreTRUE | Confirmed PLE passer   | 30104 |    19 |    41 |    55 |       66 |  67.27 |    79 |    97 |   116 |  16.79 |
| PartIIRawScoreTRUE | No confirmed PLE match | 39356 |     0 |    31 |    42 |       53 |  54.73 |    65 |    86 |   118 |  16.64 |


---

## 3. Mann-Whitney U Tests: Confirmed PLE Passer vs No Confirmed Match

**Table 24. Mann-Whitney comparison**

| Score Variable     |   Median (No confirmed PLE match) |   Median (Confirmed PLE passer) |   U-statistic |   p-value |   Effect size (r) |    N1 |    N2 |
|:-------------------|----------------------------------:|--------------------------------:|--------------:|----------:|------------------:|------:|------:|
| Total Raw Score    |                               115 |                             140 |   3.34004e+08 |         0 |            0.4362 | 39356 | 30104 |
| Percentile Rank    |                                39 |                              70 |   3.28382e+08 |         0 |            0.4244 | 38663 | 29510 |
| GPS Standard Score |                               473 |                             553 |   3.33639e+08 |         0 |            0.4374 | 39398 | 30105 |
| Part I Raw Score   |                                62 |                              74 |    3.5058e+08 |         0 |            0.4082 | 39356 | 30104 |
| Part II Raw Score  |                                53 |                              66 |   3.50305e+08 |         0 |            0.4087 | 39356 | 30104 |


---

## 4. PLE Linkage Rate by Percentile Bin

Within each percentile bin, the number of observable best records, confirmed PLE passers, and the linkage rate (%).

**Figure 21. PLE confirmed share by percentile bin**

| PercentileBin   |    n |   confirmed_passers |   linkage_rate_pct |
|:----------------|-----:|--------------------:|-------------------:|
| B1              | 6853 |                 740 |               10.8 |
| B2              | 5884 |                1219 |              20.72 |
| B3              | 5813 |                1551 |              26.68 |
| B4              | 6473 |                2155 |              33.29 |
| B5              | 6582 |                2852 |              43.33 |
| B6              | 6284 |                2976 |              47.36 |
| B7              | 6359 |                3214 |              50.54 |
| B8              | 6704 |                3534 |              52.71 |
| B9              | 7263 |                4323 |              59.52 |
| B10             | 9958 |                6946 |              69.75 |


---

## 5a. Bin Composition by PLE Status (within-bin %)

Within each bin, the distribution of PLE statuses (row-wise percentages).

**Percent distribution of PLE status within each bin**

| PercentileBin   |   Confirmed PLE passer |   No confirmed PLE match |
|:----------------|-----------------------:|-------------------------:|
| B1              |                   10.8 |                     89.2 |
| B2              |                  20.72 |                    79.28 |
| B3              |                  26.68 |                    73.32 |
| B4              |                  33.29 |                    66.71 |
| B5              |                  43.33 |                    56.67 |
| B6              |                  47.36 |                    52.64 |
| B7              |                  50.54 |                    49.46 |
| B8              |                  52.71 |                    47.29 |
| B9              |                  59.52 |                    40.48 |
| B10             |                  69.75 |                    30.25 |


---

## 5b. PLE Status Distribution Across Bins (within-PLE-status %)

For each PLE status, the distribution across percentile bins (column-wise percentages).

**Bin distribution by PLE status**

| PLE_STATUS_LABEL       |    B1 |    B2 |    B3 |    B4 |   B5 |    B6 |    B7 |    B8 |    B9 |   B10 |
|:-----------------------|------:|------:|------:|------:|-----:|------:|------:|------:|------:|------:|
| Confirmed PLE passer   |  2.51 |  4.13 |  5.26 |   7.3 | 9.66 | 10.08 | 10.89 | 11.98 | 14.65 | 23.54 |
| No confirmed PLE match | 15.81 | 12.07 | 11.02 | 11.17 | 9.65 |  8.56 |  8.13 |   8.2 |   7.6 |  7.79 |


---

## 6. Survival Rate to Top Bins (B8-B10) by Course Group

Share of examinees in each course group who scored in the top three percentile bins.

**Table 26. Course-group representation in top bins**

| UNDERGRAD_COURSE_GROUP       |   total_examinees |   top_bin_n |   survival_rate_pct |
|:-----------------------------|------------------:|------------:|--------------------:|
| Engineering & Technology     |               730 |         383 |               52.47 |
| Natural Sciences             |             40196 |       14760 |               36.72 |
| Other                        |              8248 |        2910 |               35.28 |
| Education                    |              3445 |        1160 |               33.67 |
| Medical & Allied             |             63468 |       18354 |               28.92 |
| Social & Behavioral Sciences |             15758 |        4485 |               28.46 |


---

## 7. Confirmed PLE Alignment by NMAT Year

Observable best records, confirmed passers, no match, and confirmed share by year.

**Table 28. Confirmed PLE alignment by NMAT year**

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

## 8. Confirmed PLE Alignment by Pre-Med Background

Observable best records, confirmed passers, no match, confirmed share, and median percentile rank by course group.

**Table 29. Confirmed PLE alignment by course group**

| UNDERGRAD_COURSE_GROUP       |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Education                    |                        3188 |                    1452 |                     1736 |                     45.55 |                       53 |
| Medical & Allied             |                       38144 |                   17240 |                    20904 |                      45.2 |                       49 |
| Other                        |                        6612 |                    2756 |                     3856 |                     41.68 |                       55 |
| Natural Sciences             |                       16512 |                    6849 |                     9663 |                     41.48 |                       64 |
| Engineering & Technology     |                         318 |                     116 |                      202 |                     36.48 |                       71 |
| Social & Behavioral Sciences |                        4729 |                    1692 |                     3037 |                     35.78 |                       63 |


---

## 9. Confirmed PLE Alignment by University Type

Public, Private, and Foreign university types in the observable best-record cohort.

**Table 27. Confirmed PLE alignment by university type**

| UNDERGRAD_UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|:---------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|
| Foreign              |                        1159 |                     252 |                      907 |                     21.74 |
| Private              |                       53037 |                   22712 |                    30325 |                     42.82 |
| Public               |                       14263 |                    6757 |                     7506 |                     47.37 |


---

## 10. Top Percentile Scores by PLE Status

Top 20 records per PLE status, sorted by highest percentile rank.

**Record-level detail: highest percentile scores per PLE status**

| PERSON_KEY                                     |   APPNO_CLEAN |   Year |   TotalRawScoreTRUE |   NMS_PER_num |   NMS_GPS |   PartIRawScoreTRUE |   PartIIRawScoreTRUE | PercentileBin   | PLE_STATUS_LABEL       | UNDERGRAD_UNI_TYPE   | UNDERGRAD_COURSE_GROUP       |
|:-----------------------------------------------|--------------:|-------:|--------------------:|--------------:|----------:|--------------------:|---------------------:|:----------------|:-----------------------|:---------------------|:-----------------------------|
| YNZON, CHRISTINE DANIELLE DE GUZMAN||8/5/1995  |    1041401347 |   2014 |                 175 |            99 |       717 |                  90 |                   85 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| VICENCIO, JOSEPH LOUIE MANGA||08/25/1991       |    1121210971 |   2012 |                 175 |            99 |       717 |                  91 |                   84 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| VERCELES, JANEL RAE FERRER||03/14/1992         |    1121209980 |   2012 |                 184 |            99 |       751 |                  97 |                   87 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| TAN, RANDALL ISAAC FELITRO||                   |       1080635 |   2008 |                 196 |            99 |       728 |                  96 |                  100 | B10             | Confirmed PLE passer   | Public               | Natural Sciences             |
| SY, MARK JENSEN CORTEZ||                       |       1085966 |   2008 |                 195 |            99 |       725 |                  97 |                   98 | B10             | Confirmed PLE passer   | Public               | Natural Sciences             |
| VILLAR, RYAN MICHAEL BARCELO||07/25/1994       |    1121208289 |   2012 |                 178 |            99 |       726 |                  98 |                   80 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| VILLANUEVA, ANNIE GRACE DAILO||01/17/1992      |    1121213134 |   2012 |                 181 |            99 |       737 |                  89 |                   92 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| VILLANGCA, FRANCIS DOMINIC SANTIAGO||5/1/1992  |    1121208138 |   2012 |                 180 |            99 |       733 |                  95 |                   85 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| VILLARETE, NORMAN RAE TABLAN||01/25/1991       |    1041407434 |   2014 |                 183 |            99 |       746 |                  94 |                   89 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| MANLAPAZ, ARRACHAINE DIOR OLARTE||12/10/1991   |    1121005961 |   2010 |                 196 |            99 |       720 |                 106 |                   90 | B10             | Confirmed PLE passer   | Public               | Social & Behavioral Sciences |
| VILLAGEN, BONNA DAR||04/21/1991                |    1121204857 |   2012 |                 175 |            99 |       717 |                  87 |                   88 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| STO DOMINGO, MA CARMELA LARRAZABAL||           |       1084021 |   2008 |                 200 |            99 |       732 |                  99 |                  101 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| TAN CHI, CAROLYN HOWARD||                      |       1085788 |   2008 |                 203 |            99 |       763 |                 111 |                   92 | B10             | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| VALENCIA, REYNOLD JOHN DACLAN||08/19/1991      |    1121207603 |   2012 |                 180 |            99 |       733 |                  90 |                   90 | B10             | Confirmed PLE passer   | Private              | Engineering & Technology     |
| VALDEZ, MARIA PATRICIA MALABAG||10/2/1994      |    1121206542 |   2012 |                 183 |            99 |       746 |                  98 |                   85 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| SOLIDUM, KARL JOSEF DELA CUESTA||              |       1085616 |   2008 |                 194 |            99 |       720 |                  96 |                   98 | B10             | Confirmed PLE passer   | Private              | Other                        |
| SO, PAOLO NIKOLAI HAO||                        |       1086020 |   2008 |                 202 |            99 |       754 |                 111 |                   91 | B10             | Confirmed PLE passer   | Public               | Natural Sciences             |
| SIY, WALDEMAR TAN||                            |       1083743 |   2008 |                 204 |            99 |       746 |                 107 |                   97 | B10             | Confirmed PLE passer   | Public               | Natural Sciences             |
| WONG, KYLE LENDL NG||07/31/1992                |    1121212068 |   2012 |                 179 |            99 |       729 |                  99 |                   80 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| WHANG, DAVID CHRISTOPHER REYES||9/1/1992       |    1031203381 |   2012 |                 193 |            99 |       720 |                  94 |                   99 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| PASTRANA, MARIA KATRINA RAMOS||5/9/1992        |    1121209716 |   2012 |                 179 |            99 |       729 |                  90 |                   89 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| ALCANTARA, MARK ANGELO MANDAL||                |       1093750 |   2009 |                 200 |            99 |       741 |                 101 |                   99 | B10             | No confirmed PLE match | Private              | Medical & Allied             |
| SETIAWAN, CLAUDIA ANGELA||5/5/1991             |    1121110296 |   2011 |                 198 |            99 |       729 |                 100 |                   98 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| BHIMANI, KEYUR SAVJIBHAI||10/12/1995           |    1111406390 |   2014 |                 182 |            99 |       746 |                  89 |                   93 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| DUMO, MEAGAN JADE ESLAO||09/29/1992            |    1121000226 |   2010 |                 196 |            99 |       725 |                  96 |                  100 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| DUMLAO, ANGELI MAE PAPAGAYO||12/27/1988        |    1121008183 |   2010 |                 196 |            99 |       720 |                  97 |                   99 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| DUMAG, JOANA ROSE GANDOL||02/22/1989           |    1121006502 |   2010 |                 200 |            99 |       738 |                 102 |                   98 | B10             | No confirmed PLE match | Public               | Natural Sciences             |
| TIAM LEE, JOYCE GILLIAN AYROSO||06/13/1993     |    1041401308 |   2014 |                 184 |            99 |       751 |                  99 |                   85 | B10             | No confirmed PLE match | Private              | Medical & Allied             |
| OCAMPO, ROSEMARIE CZARINA SANTIAGO||09/28/1993 |    1111303598 |   2013 |                 184 |            99 |       723 |                  87 |                   97 | B10             | No confirmed PLE match | Private              | Medical & Allied             |
| KIM, YUNGMIN||                                 |       1081037 |   2007 |                 194 |            99 |       720 |                  96 |                   98 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| MUICO, ARABELLA JO MAXEY||10/11/1990           |    2121002750 |   2010 |                 195 |            99 |       720 |                  96 |                   99 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| LUCE, JACQUELINE GRACE GO||9/11/1989           |    1121205831 |   2012 |                 176 |            99 |       720 |                  86 |                   90 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| LAT, KAREN LOISE PEREZ||                       |       1073664 |   2007 |                 193 |            99 |       720 |                  98 |                   95 | B10             | No confirmed PLE match | Public               | Education                    |
| GARCIA, JAN BENZON CHAN||                      |       1084233 |   2008 |                 199 |            99 |       725 |                  99 |                  100 | B10             | No confirmed PLE match | Private              | Medical & Allied             |
| QUIOGUE, KEVIN MANCERA||                       |       1012003 |   2009 |                 211 |            99 |       779 |                 106 |                  105 | B10             | No confirmed PLE match | Public               | Other                        |
| BULAHAO, ALVIN PINKIHAN||01/13/1988            |    1121209628 |   2012 |                 177 |            99 |       723 |                  91 |                   86 | B10             | No confirmed PLE match | Private              | Medical & Allied             |
| DICALI, SITTIE AYEESHA MACAPUNDAG||07/26/1988  |    2121001930 |   2010 |                 213 |            99 |       791 |                 108 |                  105 | B10             | No confirmed PLE match | Public               | Natural Sciences             |
| TE, JOHN CYNRIC TY||                           |       1072418 |   2007 |                 208 |            99 |       733 |                 101 |                  107 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| CHIU, CARLO GO||05/22/1992                     |    1041300154 |   2013 |                 202 |            99 |       746 |                 108 |                   94 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| RABANG, RANDY PERALTA||08/17/1992              |    1111400108 |   2014 |                 203 |            99 |       751 |                 102 |                  101 | B10             | No confirmed PLE match | Private              | Medical & Allied             |

