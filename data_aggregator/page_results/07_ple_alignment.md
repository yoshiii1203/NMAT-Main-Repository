# Page 7: PLE Alignment of NMAT Performance

**Generated:** 2026-08-14 17:29

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `bestobservable`

**Filters:** None (full unfiltered dataset)

---

## 1. Score Profile by PLE Status

Count, median, mean, Q25, and Q75 for each score measure by PLE status.

**Table 23. Score profile by PLE status**

| PLE_STATUS_LABEL       |   TotalRawScoreTRUE_count |   TotalRawScoreTRUE_median |   TotalRawScoreTRUE_mean |   TotalRawScoreTRUE_q25 |   TotalRawScoreTRUE_q75 |   NMS_PER_num_count |   NMS_PER_num_median |   NMS_PER_num_mean |   NMS_PER_num_q25 |   NMS_PER_num_q75 |   NMS_GPS_count |   NMS_GPS_median |   NMS_GPS_mean |   NMS_GPS_q25 |   NMS_GPS_q75 |   NMS_APT_count |   NMS_APT_median |   NMS_APT_mean |   NMS_APT_q25 |   NMS_APT_q75 |   NMS_SA_count |   NMS_SA_median |   NMS_SA_mean |   NMS_SA_q25 |   NMS_SA_q75 |   PartIRawScoreTRUE_count |   PartIRawScoreTRUE_median |   PartIRawScoreTRUE_mean |   PartIRawScoreTRUE_q25 |   PartIRawScoreTRUE_q75 |   PartIIRawScoreTRUE_count |   PartIIRawScoreTRUE_median |   PartIIRawScoreTRUE_mean |   PartIIRawScoreTRUE_q25 |   PartIIRawScoreTRUE_q75 |
|:-----------------------|--------------------------:|---------------------------:|-------------------------:|------------------------:|------------------------:|--------------------:|---------------------:|-------------------:|------------------:|------------------:|----------------:|-----------------:|---------------:|--------------:|--------------:|----------------:|-----------------:|---------------:|--------------:|--------------:|---------------:|----------------:|--------------:|-------------:|-------------:|--------------------------:|---------------------------:|-------------------------:|------------------------:|------------------------:|---------------------------:|----------------------------:|--------------------------:|-------------------------:|-------------------------:|
| Confirmed PLE passer   |                     31572 |                        139 |                   141.04 |                     120 |                     162 |               30988 |                   69 |              64.56 |                45 |                88 |           31581 |              552 |         555.86 |           489 |           624 |           31581 |              548 |         552.13 |           491 |           612 |          31581 |             544 |        546.07 |          480 |          610 |                     31572 |                         74 |                    73.85 |                      63 |                      84 |                      31572 |                          66 |                     67.18 |                       55 |                       79 |
| No confirmed PLE match |                     37888 |                        114 |                    116.2 |                      94 |                     136 |               37758 |                   38 |              42.06 |                15 |                66 |           37922 |              470 |         471.63 |           399 |           545 |           37922 |              484 |         480.26 |           415 |           546 |          37922 |             471 |        474.14 |          406 |          539 |                     37888 |                         62 |                    61.89 |                      51 |                      73 |                      37888 |                          52 |                     54.31 |                       42 |                       65 |


---

## 2. Box-Plot Data by Score and PLE Status

Quantile-based summary for each score variable, split by PLE status.

**Box-plot summary statistics**

| ScoreVariable      | PLE_STATUS_LABEL       |     n |   min |   q05 |   q25 |   median |   mean |   q75 |   q95 |   max |    std |
|:-------------------|:-----------------------|------:|------:|------:|------:|---------:|-------:|------:|------:|------:|-------:|
| TotalRawScoreTRUE  | Confirmed PLE passer   | 31572 |    48 |    95 |   120 |      139 | 141.04 |   162 |   192 |   231 |  29.37 |
| TotalRawScoreTRUE  | No confirmed PLE match | 37888 |     9 |    70 |    94 |      114 |  116.2 |   136 |   170 |   223 |   30.5 |
| NMS_PER_num        | Confirmed PLE passer   | 30988 |    -1 |    15 |    45 |       69 |  64.56 |    88 |    98 |    99 |  26.33 |
| NMS_PER_num        | No confirmed PLE match | 37758 |    -1 |     2 |    15 |       38 |  42.06 |    66 |    93 |    99 |  29.54 |
| NMS_GPS            | Confirmed PLE passer   | 31581 |   200 |   399 |   489 |      552 | 555.86 |   624 |   723 |   800 |  97.66 |
| NMS_GPS            | No confirmed PLE match | 37922 |     0 |   293 |   399 |      470 | 471.63 |   545 |   653 |   800 | 108.92 |
| NMS_APT            | Confirmed PLE passer   | 31581 |   200 |   403 |   491 |      548 | 552.13 |   612 |   710 |   800 |  93.24 |
| NMS_APT            | No confirmed PLE match | 37922 |   200 |   316 |   415 |      484 | 480.26 |   546 |   645 |   800 | 101.18 |
| NMS_SA             | Confirmed PLE passer   | 31581 |   200 |   398 |   480 |      544 | 546.07 |   610 |   705 |   800 |  92.22 |
| NMS_SA             | No confirmed PLE match | 37922 |     0 |   318 |   406 |      471 | 474.14 |   539 |   641 |   800 |  98.26 |
| PartIRawScoreTRUE  | Confirmed PLE passer   | 31572 |    12 |    49 |    63 |       74 |  73.85 |    84 |    99 |   118 |  15.03 |
| PartIRawScoreTRUE  | No confirmed PLE match | 37888 |     0 |    36 |    51 |       62 |  61.89 |    73 |    90 |   116 |  16.31 |
| PartIIRawScoreTRUE | Confirmed PLE passer   | 31572 |    19 |    41 |    55 |       66 |  67.18 |    79 |    97 |   116 |  16.75 |
| PartIIRawScoreTRUE | No confirmed PLE match | 37888 |     0 |    31 |    42 |       52 |  54.31 |    65 |    85 |   118 |  16.53 |


---

## 3. Mann-Whitney U Tests: Confirmed PLE Passer vs No Confirmed Match

**Table 24. Mann-Whitney comparison**

| Score Variable     |   Median (No confirmed PLE match) |   Median (Confirmed PLE passer) |   U-statistic |   p-value |   Effect size (r) |    N1 |    N2 |
|:-------------------|----------------------------------:|--------------------------------:|--------------:|----------:|------------------:|------:|------:|
| Total Raw Score    |                               114 |                             139 |   3.33156e+08 |         0 |             0.443 | 37888 | 31572 |
| Percentile Rank    |                                38 |                              69 |   3.34426e+08 |         0 |            0.4284 | 37758 | 30988 |
| GPS Standard Score |                               470 |                             552 |   3.39564e+08 |         0 |            0.4329 | 37922 | 31581 |
| Part I Raw Score   |                                62 |                              74 |   3.54041e+08 |         0 |            0.4081 | 37888 | 31572 |
| Part II Raw Score  |                                52 |                              66 |   3.46502e+08 |         0 |            0.4207 | 37888 | 31572 |


---

## 4. PLE Linkage Rate by Percentile Bin

Within each percentile bin, the number of observable best records, confirmed PLE passers, and the linkage rate (%).

**Figure 21. PLE confirmed share by percentile bin**

| PercentileBin   |    n |   confirmed_passers |   linkage_rate_pct |
|:----------------|-----:|--------------------:|-------------------:|
| B1              | 6853 |                 795 |               11.6 |
| B2              | 5884 |                1336 |              22.71 |
| B3              | 5813 |                1703 |               29.3 |
| B4              | 6473 |                2330 |                 36 |
| B5              | 6582 |                3003 |              45.62 |
| B6              | 6284 |                3168 |              50.41 |
| B7              | 6359 |                3407 |              53.58 |
| B8              | 6704 |                3690 |              55.04 |
| B9              | 7263 |                4474 |               61.6 |
| B10             | 9958 |                7073 |              71.03 |


---

## 5a. Bin Composition by PLE Status (within-bin %)

Within each bin, the distribution of PLE statuses (row-wise percentages).

**Percent distribution of PLE status within each bin**

| PercentileBin   |   Confirmed PLE passer |   No confirmed PLE match |
|:----------------|-----------------------:|-------------------------:|
| B1              |                   11.6 |                     88.4 |
| B2              |                  22.71 |                    77.29 |
| B3              |                   29.3 |                     70.7 |
| B4              |                     36 |                       64 |
| B5              |                  45.62 |                    54.38 |
| B6              |                  50.41 |                    49.59 |
| B7              |                  53.58 |                    46.42 |
| B8              |                  55.04 |                    44.96 |
| B9              |                   61.6 |                     38.4 |
| B10             |                  71.03 |                    28.97 |


---

## 5b. PLE Status Distribution Across Bins (within-PLE-status %)

For each PLE status, the distribution across percentile bins (column-wise percentages).

**Bin distribution by PLE status**

| PLE_STATUS_LABEL       |    B1 |    B2 |    B3 |    B4 |   B5 |    B6 |   B7 |    B8 |    B9 |   B10 |
|:-----------------------|------:|------:|------:|------:|-----:|------:|-----:|------:|------:|------:|
| Confirmed PLE passer   |  2.57 |  4.31 |   5.5 |  7.52 | 9.69 | 10.23 |   11 | 11.91 | 14.44 | 22.83 |
| No confirmed PLE match | 16.29 | 12.23 | 11.05 | 11.14 | 9.62 |  8.38 | 7.94 |   8.1 |   7.5 |  7.76 |


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

## 8. Confirmed PLE Alignment by Pre-Med Background

Observable best records, confirmed passers, no match, confirmed share, and median percentile rank by course group.

**Table 29. Confirmed PLE alignment by course group**

| UNDERGRAD_COURSE_GROUP       |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Education                    |                        3188 |                    1699 |                     1489 |                     53.29 |                       53 |
| Other                        |                        6612 |                    3201 |                     3411 |                     48.41 |                       55 |
| Medical & Allied             |                       38144 |                   17833 |                    20311 |                     46.75 |                       48 |
| Natural Sciences             |                       16512 |                    6994 |                     9518 |                     42.36 |                       63 |
| Engineering & Technology     |                         318 |                     118 |                      200 |                     37.11 |                       71 |
| Social & Behavioral Sciences |                        4729 |                    1736 |                     2993 |                     36.71 |                       63 |


---

## 9. Confirmed PLE Alignment by University Type

Public, Private, and Foreign university types in the observable best-record cohort.

**Table 27. Confirmed PLE alignment by university type**

| UNDERGRAD_UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|:---------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|
| Foreign              |                        1159 |                     258 |                      901 |                     22.26 |
| Private              |                       52821 |                   23757 |                    29064 |                     44.98 |
| Public               |                       14642 |                    7226 |                     7416 |                     49.35 |


---

## 10. Top Percentile Scores by PLE Status

Top 20 records per PLE status, sorted by highest percentile rank.

**Record-level detail: highest percentile scores per PLE status**

| PERSON_KEY                                          |   APPNO_CLEAN |   Year |   TotalRawScoreTRUE |   NMS_PER_num |   NMS_GPS |   PartIRawScoreTRUE |   PartIIRawScoreTRUE | PercentileBin   | PLE_STATUS_LABEL       | UNDERGRAD_UNI_TYPE   | UNDERGRAD_COURSE_GROUP       |
|:----------------------------------------------------|--------------:|-------:|--------------------:|--------------:|----------:|--------------------:|---------------------:|:----------------|:-----------------------|:---------------------|:-----------------------------|
| ROJO, RANIV DAWEY||                                 |       1010366 |   2009 |                 203 |            99 |       738 |                 101 |                  102 | B10             | Confirmed PLE passer   | Public               | Other                        |
| ALEJO, GABRIEL IGNACIO PALMA||9/12/1990             |    1031204633 |   2012 |                 201 |            99 |       741 |                 106 |                   95 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| ALCANTARA, JEROME HERNANDEZ||11/13/1992             |    1121207717 |   2012 |                 182 |            99 |       741 |                  98 |                   84 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| ROQUE, VLADIMIR LENNIN ALCANTARA||                  |       1003529 |   2009 |                 200 |            99 |       732 |                  97 |                  103 | B10             | Confirmed PLE passer   | Public               | Natural Sciences             |
| YENSON, IVAN LENDLE CABANILLA||1/7/1996             |    1111407328 |   2014 |                 180 |            99 |       737 |                 100 |                   80 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| VILLARETE, NORMAN RAE TABLAN||01/25/1991            |    1041407434 |   2014 |                 183 |            99 |       746 |                  94 |                   89 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| VALERA, JUANCHO LORENZO SANTOS||6/10/1991           |    1111303883 |   2013 |                 192 |            99 |       751 |                  97 |                   95 | B10             | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| AUTENTICO, REYSA OMAY||                             |       1061792 |   2007 |                 201 |            99 |       741 |                  96 |                  105 | B10             | Confirmed PLE passer   | Public               | Education                    |
| MAGCALAS, ANNA RICO||09/24/1992                     |    1121000237 |   2010 |                 199 |            99 |       735 |                 105 |                   94 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| JAVIER, KENNETH ARVIOLA||                           |       1002247 |   2009 |                 216 |            99 |       795 |                 106 |                  110 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| MALANYAON, FREDA QUIMBA||5/5/1987                   |    1121001087 |   2010 |                 205 |            99 |       768 |                 108 |                   97 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| UY, JOHN HENRICK GOLAK||5/10/1994                   |    1111307461 |   2013 |                 187 |            99 |       733 |                  93 |                   94 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| VILLANGCA, DANIEL JR GONZALES||09/13/1993           |    1111312014 |   2013 |                 182 |            99 |       717 |                  97 |                   85 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| VILLANUEVA, JOHN CHRISTOPHER CONCEPCION||06/22/1994 |    1111309984 |   2013 |                 190 |            99 |       741 |                  92 |                   98 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| VILLANUEVA, MARK JHERVY SORIANO||01/30/1992         |    1041303851 |   2013 |                 197 |            99 |       726 |                 104 |                   93 | B10             | Confirmed PLE passer   | Private              | Medical & Allied             |
| SALISE, JOEANNE MARIE MAHINAY||                     |       1085671 |   2008 |                 199 |            99 |       738 |                 107 |                   92 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| ANG, FELICE KATRINA CASTRO||02/13/1993              |    1121208269 |   2012 |                 176 |            99 |       720 |                  99 |                   77 | B10             | Confirmed PLE passer   | Public               | Social & Behavioral Sciences |
| ANG, HARLEY GUERALD CO||03/25/1991                  |    1031200875 |   2012 |                 196 |            99 |       729 |                 102 |                   94 | B10             | Confirmed PLE passer   | Public               | Social & Behavioral Sciences |
| SALVAME, ERIKA JEAN ANG||                           |       1085695 |   2008 |                 201 |            99 |       749 |                 108 |                   93 | B10             | Confirmed PLE passer   | Public               | Medical & Allied             |
| SAN JUAN, MARI DES JIMENEZ||                        |       1085386 |   2008 |                 198 |            99 |       743 |                  95 |                  103 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| FLORANO, SOLMUELL MERCADO||12/27/1993               |    1111406933 |   2014 |                 179 |            99 |       733 |                  86 |                   93 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| YOUNG, JAMIE ROSLYN TIU||12/29/1994                 |    1111403809 |   2014 |                 182 |            99 |       751 |                  92 |                   90 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| CORPUZ, KATHLEEN BUENO||                            |       1073266 |   2007 |                 196 |            99 |       726 |                  94 |                  102 | B10             | No confirmed PLE match | Public               | Natural Sciences             |
| TE, JOHN CYNRIC TY||                                |       1072418 |   2007 |                 208 |            99 |       733 |                 101 |                  107 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| GARCIA, JOSEPH BENEDICT TION||09/19/1993            |    1041407093 |   2014 |                 183 |            99 |       746 |                 102 |                   81 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| ALCANTARA, KRISTIA BERNADINE LICUDINE||12/19/1994   |    1111403360 |   2014 |                 177 |            99 |       733 |                  88 |                   89 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| LUCERO, KIMBERLY BALIGUAT||1/10/1990                |    1121003765 |   2010 |                 198 |            99 |       732 |                  98 |                  100 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| DELOS REYES, MA KRISTINA JUAN||                     |       1082641 |   2007 |                 199 |            99 |       737 |                  93 |                  106 | B10             | No confirmed PLE match | Public               | Natural Sciences             |
| YANG, PETER||08/29/1993                             |    1111400534 |   2014 |                 199 |            99 |       737 |                 101 |                   98 | B10             | No confirmed PLE match | Public               | Natural Sciences             |
| LOPEZ, ALENNIE CHARMAINE LEONARDO||02/23/1991       |    1121001950 |   2010 |                 201 |            99 |       743 |                 106 |                   95 | B10             | No confirmed PLE match | Private              | Social & Behavioral Sciences |
| FERRER, FRANCO EMILE RAMIREZ||11/13/1991            |    1041407056 |   2014 |                 175 |            99 |       717 |                  93 |                   82 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| ENDOZO, ALLYSTER ARCEO||7/11/1991                   |    1121208475 |   2012 |                 180 |            99 |       733 |                  97 |                   83 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| ESPIRITU, ENRIQUE MIGUEL VERDE||6/4/1988            |    1031200596 |   2012 |                 200 |            99 |       741 |                 106 |                   94 | B10             | No confirmed PLE match | Private              | Other                        |
| ABERIN, MARVIN ANGELO ESTEBAN||3/6/1994             |    1111400643 |   2014 |                 183 |            99 |       751 |                  94 |                   89 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| ABUNDO, RACELA THERESE BUENCAMINO||7/3/1991         |    1041407593 |   2014 |                 182 |            99 |       741 |                  97 |                   85 | B10             | No confirmed PLE match | Private              | Social & Behavioral Sciences |
| GOH, RACHEL ANNE REYES||04/23/1991                  |        400721 |   2010 |                 208 |            99 |       733 |                 103 |                  105 | B10             | No confirmed PLE match | Public               | Natural Sciences             |
| PASCASIO, THEA KATRINA ANINAG||12/10/1992           |    1121000626 |   2010 |                 205 |            99 |       768 |                 107 |                   98 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| PLIMACO, FIL KRISTIAN BONDOC||08/14/1988            |    1121008392 |   2010 |                 197 |            99 |       728 |                 107 |                   90 | B10             | No confirmed PLE match | Private              | Natural Sciences             |
| GUZMAN, RUTH MARIAN SARRA||                         |       1071093 |   2006 |                 200 |            99 |       737 |                 100 |                  100 | B10             | No confirmed PLE match | Public               | Other                        |
| KIM, YUNGMIN||                                      |       1081037 |   2007 |                 194 |            99 |       720 |                  96 |                   98 | B10             | No confirmed PLE match | Private              | Natural Sciences             |

