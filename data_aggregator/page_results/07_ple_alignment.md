# Page 7: PLE Alignment of NMAT Performance

**Generated:** 2026-07-28 01:17

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `bestobservable`

**Filters:** None (full unfiltered dataset)

---

## 1. Score Profile by PLE Status

Count, median, mean, Q25, and Q75 for each score measure by PLE status.

**Table 23. Score profile by PLE status**

| PLE_STATUS_LABEL       |   TotalRawScoreTRUE_count |   TotalRawScoreTRUE_median |   TotalRawScoreTRUE_mean |   TotalRawScoreTRUE_q25 |   TotalRawScoreTRUE_q75 |   NMS_PER_num_count |   NMS_PER_num_median |   NMS_PER_num_mean |   NMS_PER_num_q25 |   NMS_PER_num_q75 |   NMS_GPS_count |   NMS_GPS_median |   NMS_GPS_mean |   NMS_GPS_q25 |   NMS_GPS_q75 |   PartIRawScoreTRUE_count |   PartIRawScoreTRUE_median |   PartIRawScoreTRUE_mean |   PartIRawScoreTRUE_q25 |   PartIRawScoreTRUE_q75 |   PartIIRawScoreTRUE_count |   PartIIRawScoreTRUE_median |   PartIIRawScoreTRUE_mean |   PartIIRawScoreTRUE_q25 |   PartIIRawScoreTRUE_q75 |
|:-----------------------|--------------------------:|---------------------------:|-------------------------:|------------------------:|------------------------:|--------------------:|---------------------:|-------------------:|------------------:|------------------:|----------------:|-----------------:|---------------:|--------------:|--------------:|--------------------------:|---------------------------:|-------------------------:|------------------------:|------------------------:|---------------------------:|----------------------------:|--------------------------:|-------------------------:|-------------------------:|
| Confirmed PLE passer   |                     29269 |                        143 |                   144.76 |                     125 |                     164 |               28646 |                   73 |              68.64 |                52 |                90 |           29273 |              564 |         569.18 |           506 |           632 |                     29269 |                         76 |                    75.75 |                      66 |                      86 |                      29269 |                          68 |                     69.02 |                       57 |                       80 |
| No confirmed PLE match |                     35194 |                        112 |                   115.01 |                      94 |                     134 |               35075 |                   36 |              40.28 |                15 |                63 |           35228 |              464 |         466.41 |           398 |           533 |                     35194 |                         61 |                    61.31 |                      51 |                      72 |                      35194 |                          51 |                     53.69 |                       42 |                       64 |


---

## 2. Box-Plot Data by Score and PLE Status

Quantile-based summary for each score variable, split by PLE status.

**Box-plot summary statistics**

| ScoreVariable      | PLE_STATUS_LABEL       |     n |   min |   q05 |   q25 |   median |   mean |   q75 |   q95 |   max |    std |
|:-------------------|:-----------------------|------:|------:|------:|------:|---------:|-------:|------:|------:|------:|-------:|
| TotalRawScoreTRUE  | Confirmed PLE passer   | 29269 |    48 |   100 |   125 |      143 | 144.76 |   164 |   193 |   231 |  27.83 |
| TotalRawScoreTRUE  | No confirmed PLE match | 35194 |     9 |    70 |    94 |      112 | 115.01 |   134 |   169 |   223 |  29.79 |
| NMS_PER_num        | Confirmed PLE passer   | 28646 |    -1 |    21 |    52 |       73 |  68.64 |    90 |    98 |    99 |   24.3 |
| NMS_PER_num        | No confirmed PLE match | 35075 |    -1 |     2 |    15 |       36 |  40.28 |    63 |    92 |    99 |  28.64 |
| NMS_GPS            | Confirmed PLE passer   | 29273 |   200 |   420 |   506 |      564 | 569.18 |   632 | 726.8 |   800 |   92.7 |
| NMS_GPS            | No confirmed PLE match | 35228 |     0 |   293 |   398 |      464 | 466.41 |   533 |   645 |   800 | 106.06 |
| PartIRawScoreTRUE  | Confirmed PLE passer   | 29269 |    20 |    52 |    66 |       76 |  75.75 |    86 |   100 |   118 |  14.34 |
| PartIRawScoreTRUE  | No confirmed PLE match | 35194 |     0 |    36 |    51 |       61 |  61.31 |    72 |    89 |   116 |  15.96 |
| PartIIRawScoreTRUE | Confirmed PLE passer   | 29269 |    19 |    44 |    57 |       68 |  69.02 |    80 |    97 |   115 |  16.05 |
| PartIIRawScoreTRUE | No confirmed PLE match | 35194 |     0 |    31 |    42 |       51 |  53.69 |    64 |    85 |   118 |  16.23 |


---

## 3. Mann-Whitney U Tests: Confirmed PLE Passer vs No Confirmed Match

**Table 24. Mann-Whitney comparison**

| Score Variable     |   Median (No confirmed PLE match) |   Median (Confirmed PLE passer) |   U-statistic |   p-value |   Effect size (r) |    N1 |    N2 |
|:-------------------|----------------------------------:|--------------------------------:|--------------:|----------:|------------------:|------:|------:|
| Total Raw Score    |                               112 |                             143 |   2.35895e+08 |         0 |             0.542 | 35194 | 29269 |
| Percentile Rank    |                                36 |                              73 |   2.31503e+08 |         0 |            0.5392 | 35075 | 28646 |
| GPS Standard Score |                               464 |                             564 |   2.35941e+08 |         0 |            0.5424 | 35228 | 29273 |
| Part I Raw Score   |                                61 |                              76 |   2.55891e+08 |         0 |            0.5032 | 35194 | 29269 |
| Part II Raw Score  |                                51 |                              68 |   2.53804e+08 |         0 |            0.5072 | 35194 | 29269 |


---

## 4. PLE Pass Rate by Percentile Bin

Within each percentile bin, the number of observable best records, confirmed PLE passers, and the pass rate (%).

**Figure 21. PLE confirmed share by percentile bin**

| PercentileBin   |    n |   confirmed_passers |   pass_rate_pct |
|:----------------|-----:|--------------------:|----------------:|
| B1              | 6104 |                 505 |            8.27 |
| B2              | 5254 |                 830 |            15.8 |
| B3              | 5228 |                 997 |           19.07 |
| B4              | 5741 |                1312 |           22.85 |
| B5              | 6229 |                2882 |           46.27 |
| B6              | 5831 |                2992 |           51.31 |
| B7              | 5942 |                3359 |           56.53 |
| B8              | 6355 |                3819 |           60.09 |
| B9              | 6854 |                4595 |           67.04 |
| B10             | 9657 |                7352 |           76.13 |


---

## 5a. Bin Composition by PLE Status (within-bin %)

Within each bin, the distribution of PLE statuses (row-wise percentages).

**Percent distribution of PLE status within each bin**

| PercentileBin   |   Confirmed PLE passer |   No confirmed PLE match |
|:----------------|-----------------------:|-------------------------:|
| B1              |                   8.27 |                    91.73 |
| B2              |                   15.8 |                     84.2 |
| B3              |                  19.07 |                    80.93 |
| B4              |                  22.85 |                    77.15 |
| B5              |                  46.27 |                    53.73 |
| B6              |                  51.31 |                    48.69 |
| B7              |                  56.53 |                    43.47 |
| B8              |                  60.09 |                    39.91 |
| B9              |                  67.04 |                    32.96 |
| B10             |                  76.13 |                    23.87 |


---

## 5b. PLE Status Distribution Across Bins (within-PLE-status %)

For each PLE status, the distribution across percentile bins (column-wise percentages).

**Bin distribution by PLE status**

| PLE_STATUS_LABEL       |   B1 |   B2 |    B3 |    B4 |    B5 |    B6 |    B7 |    B8 |    B9 |   B10 |
|:-----------------------|-----:|-----:|------:|------:|------:|------:|------:|------:|------:|------:|
| Confirmed PLE passer   | 1.76 |  2.9 |  3.48 |  4.58 | 10.06 | 10.45 | 11.73 | 13.33 | 16.04 | 25.67 |
| No confirmed PLE match | 16.2 | 12.8 | 12.25 | 12.82 |  9.69 |  8.22 |  7.48 |  7.34 |  6.54 |  6.67 |


---

## 6. Survival Rate to Top Bins (B8-B10) by Course Group

Share of examinees in each course group who scored in the top three percentile bins.

**Table 26. Course-group representation in top bins**

| CourseGroup                  |   total_examinees |   top_bin_n |   survival_rate_pct |
|:-----------------------------|------------------:|------------:|--------------------:|
| Engineering & Technology     |               729 |         382 |                52.4 |
| Natural Sciences             |             40086 |       14660 |               36.57 |
| Other                        |              7885 |        2778 |               35.23 |
| Education                    |              3244 |        1086 |               33.48 |
| Medical & Allied             |             63067 |       18138 |               28.76 |
| Social & Behavioral Sciences |             15724 |        4456 |               28.34 |


---

## 7. Confirmed PLE Alignment by NMAT Year

Observable best records, confirmed passers, no match, and confirmed share by year.

**Table 28. Confirmed PLE alignment by NMAT year**

|   Year |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|-------:|----------------------------:|------------------------:|-------------------------:|--------------------------:|
|   2006 |                        3665 |                    2038 |                     1627 |                     55.61 |
|   2007 |                        3660 |                    1868 |                     1792 |                     51.04 |
|   2008 |                        4849 |                    2514 |                     2335 |                     51.85 |
|   2009 |                        6881 |                    3226 |                     3655 |                     46.88 |
|   2010 |                        8008 |                    3808 |                     4200 |                     47.55 |
|   2011 |                        8731 |                    3853 |                     4878 |                     44.13 |
|   2012 |                        9145 |                    4066 |                     5079 |                     44.46 |
|   2013 |                        9121 |                    3951 |                     5170 |                     43.32 |
|   2014 |                       10441 |                    3949 |                     6492 |                     37.82 |


---

## 8. Confirmed PLE Alignment by Pre-Med Background

Observable best records, confirmed passers, no match, confirmed share, and median percentile rank by course group.

**Table 29. Confirmed PLE alignment by course group**

| CourseGroup                  |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |   median_percentile_rank |
|:-----------------------------|----------------------------:|------------------------:|-------------------------:|--------------------------:|-------------------------:|
| Education                    |                        2973 |                    1541 |                     1432 |                     51.83 |                       52 |
| Other                        |                        6189 |                    2853 |                     3336 |                      46.1 |                       55 |
| Natural Sciences             |                       15219 |                    6921 |                     8298 |                     45.48 |                       66 |
| Medical & Allied             |                       35433 |                   16061 |                    19372 |                     45.33 |                       49 |
| Social & Behavioral Sciences |                        4385 |                    1783 |                     2602 |                     40.66 |                       64 |
| Engineering & Technology     |                         302 |                     114 |                      188 |                     37.75 |                       71 |


---

## 9. Confirmed PLE Alignment by University Type

Public, Private, and Foreign university types in the observable best-record cohort.

**Table 27. Confirmed PLE alignment by university type**

| UNI_TYPE   |   n_observable_best_records |   confirmed_ple_passers |   no_confirmed_ple_match |   confirmed_ple_share_pct |
|:-----------|----------------------------:|------------------------:|-------------------------:|--------------------------:|
| Foreign    |                        1124 |                     248 |                      876 |                     22.06 |
| Private    |                       48991 |                   21909 |                    27082 |                     44.72 |
| Public     |                       13555 |                    6786 |                     6769 |                     50.06 |


---

## 10. Top Percentile Scores by PLE Status

Top 20 records per PLE status, sorted by highest percentile rank.

**Record-level detail: highest percentile scores per PLE status**

| PERSON_KEY                                    |   APPNO_CLEAN |   Year |   TotalRawScoreTRUE |   NMS_PER_num |   NMS_GPS |   PartIRawScoreTRUE |   PartIIRawScoreTRUE | PercentileBin   | PLE_STATUS_LABEL       | UNI_TYPE      | CourseGroup                  |
|:----------------------------------------------|--------------:|-------:|--------------------:|--------------:|----------:|--------------------:|---------------------:|:----------------|:-----------------------|:--------------|:-----------------------------|
| YUNQUE, VANESSA AURA TERRITORIO||09/24/1993   |    1111409579 |   2014 |                 178 |            99 |       733 |                  88 |                   90 | B10             | Confirmed PLE passer   | Public        | Medical & Allied             |
| YNZON, CHRISTINE DANIELLE DE GUZMAN||8/5/1995 |    1041401347 |   2014 |                 175 |            99 |       717 |                  90 |                   85 | B10             | Confirmed PLE passer   | Private       | Natural Sciences             |
| YOUNG, JAMIE ROSLYN TIU||12/29/1994           |    1111403809 |   2014 |                 182 |            99 |       751 |                  92 |                   90 | B10             | Confirmed PLE passer   | Private       | Natural Sciences             |
| CORTES, FREDERIK KHO||08/15/1990              |    2121001513 |   2010 |                 196 |            99 |       720 |                 105 |                   91 | B10             | Confirmed PLE passer   | Private       | Social & Behavioral Sciences |
| CORTEZ, JAKE BRYAN SARMIENTO||11/13/1989      |    1121000144 |   2010 |                 195 |            99 |       720 |                  94 |                  101 | B10             | Confirmed PLE passer   | Private       | Medical & Allied             |
| CONSUNJI, MARY VERONICA SALDANA||08/28/1988   |    1121002729 |   2010 |                 203 |            99 |       754 |                 104 |                   99 | B10             | Confirmed PLE passer   | Private       | Other                        |
| CORANEZ, ALDRIN JAVIER||10/11/1991            |    1121004233 |   2010 |                 208 |            99 |       775 |                 107 |                  101 | B10             | Confirmed PLE passer   | Private       | Natural Sciences             |
| WEE ENG, ATRIO ERICMOND TAN||12/5/1994        |    1111404887 |   2014 |                 182 |            99 |       751 |                  83 |                   99 | B10             | Confirmed PLE passer   | Foreign       | Natural Sciences             |
| WONG, ENA NICOLE ASHLEE ENRILE||03/20/1997    |    1111405991 |   2014 |                 173 |            99 |       717 |                  91 |                   82 | B10             | Confirmed PLE passer   | Private       | Medical & Allied             |
| AGGABAO, LARIELYN HOPE CAYADO||4/9/1991       |    1041100628 |   2011 |                 197 |            99 |       732 |                 104 |                   93 | B10             | Confirmed PLE passer   | Public        | Natural Sciences             |
| OLIVERA, JANNA ELYZA PERALTA||                |       1085363 |   2008 |                 195 |            99 |       725 |                 101 |                   94 | B10             | Confirmed PLE passer   | Public        | Medical & Allied             |
| ONG, KIMBERLY MAE CHUA||                      |       1080742 |   2008 |                 203 |            99 |       743 |                 109 |                   94 | B10             | Confirmed PLE passer   | Public        | Social & Behavioral Sciences |
| GRANADA, BRANTLEY GO||02/26/1995              |    1111308631 |   2013 |                 183 |            99 |       720 |                 106 |                   77 | B10             | Confirmed PLE passer   | Private       | Medical & Allied             |
| CRUZ, ELLA MAE DE GUZMAN||05/31/1989          |    1121001164 |   2010 |                 200 |            99 |       738 |                  88 |                  112 | B10             | Confirmed PLE passer   | Public        | Medical & Allied             |
| CORONEL, INAH JANE TEJADA||05/30/1994         |    1121000638 |   2010 |                 205 |            99 |       768 |                 109 |                   96 | B10             | Confirmed PLE passer   | Public        | Medical & Allied             |
| CORPUZ, HASMIN LISA HERRAS||09/19/1990        |    1121002328 |   2010 |                 212 |            99 |       788 |                 110 |                  102 | B10             | Confirmed PLE passer   | Public        | Natural Sciences             |
| HABAJAB, VANESSA MARIE MAGAHIN||07/27/1994    |    1111304898 |   2013 |                 183 |            99 |       717 |                  92 |                   91 | B10             | Confirmed PLE passer   | Not Specified | Medical & Allied             |
| CRUZ, PATRICIO LORENZO SANTOS||4/10/1990      |    1121001069 |   2010 |                 209 |            99 |       779 |                 104 |                  105 | B10             | Confirmed PLE passer   | Public        | Natural Sciences             |
| COTINGTING, CRYSTLE TAN||7/9/1990             |    1121004765 |   2010 |                 202 |            99 |       749 |                  99 |                  103 | B10             | Confirmed PLE passer   | Public        | Medical & Allied             |
| GONZALES, JOANNA FRANCHESCA DATOR||6/8/1993   |    1111310619 |   2013 |                 183 |            99 |       720 |                 100 |                   83 | B10             | Confirmed PLE passer   | Private       | Natural Sciences             |
| ZAULDA, FIDES ANGELI DELA CRUZ||              |       1011880 |   2009 |                 210 |            99 |       778 |                 104 |                  106 | B10             | No confirmed PLE match | Public        | Medical & Allied             |
| RODRIGUEZ, ISAGANI BEAU JR RANA||9/10/1994    |    1111303271 |   2013 |                 188 |            99 |       733 |                 105 |                   83 | B10             | No confirmed PLE match | Private       | Natural Sciences             |
| YOON, CHARLOTTE SEONGEUN||02/21/1989          |    1111401646 |   2014 |                 200 |            99 |       741 |                 100 |                  100 | B10             | No confirmed PLE match | Public        | Natural Sciences             |
| HERMO, DEO PAOLO MARCIANO VENIDA||11/23/1989  |    1041103978 |   2011 |                 195 |            99 |       725 |                 104 |                   91 | B10             | No confirmed PLE match | Public        | Natural Sciences             |
| PASCASIO, THEA KATRINA ANINAG||12/10/1992     |    1121000626 |   2010 |                 205 |            99 |       768 |                 107 |                   98 | B10             | No confirmed PLE match | Public        | Medical & Allied             |
| GARCIA, MARTIN KEITH||10/29/1990              |    1111304705 |   2013 |                 183 |            99 |       720 |                  99 |                   84 | B10             | No confirmed PLE match | Private       | Natural Sciences             |
| ANG, JOANNE MARIE BACAR||                     |       1054579 |   2006 |                 205 |            99 |       768 |                 104 |                  101 | B10             | No confirmed PLE match | Private       | Other                        |
| SARSAGAT, JINO MART ERIK DOLOR||              |       1003440 |   2009 |                 201 |            99 |       735 |                 101 |                  100 | B10             | No confirmed PLE match | Private       | Medical & Allied             |
| SAUTER, LAUREN REBECCA||                      |       1092025 |   2009 |                 199 |            99 |       735 |                 102 |                   97 | B10             | No confirmed PLE match | Foreign       | Medical & Allied             |
| DOMINGO, JUSTINE PERRY TOMINES||              |       1093892 |   2009 |                 199 |            99 |       729 |                 103 |                   96 | B10             | No confirmed PLE match | Public        | Natural Sciences             |
| CABALES, MAE PERCI BELLE GONZALES||2/5/1988   |    1121108963 |   2011 |                 199 |            99 |       733 |                 104 |                   95 | B10             | No confirmed PLE match | Foreign       | Natural Sciences             |
| LAO, PRISCILLA APRIL ONG||04/25/1992          |    2121002448 |   2011 |                 208 |            99 |       771 |                 100 |                  108 | B10             | No confirmed PLE match | Not Specified | Natural Sciences             |
| GANIPIS, KENNY ROLEX LUKEN||08/23/1988        |    1111310775 |   2013 |                 187 |            99 |       726 |                 102 |                   85 | B10             | No confirmed PLE match | Private       | Medical & Allied             |
| CORPUZ, KATHLEEN BUENO||                      |       1073266 |   2007 |                 196 |            99 |       726 |                  94 |                  102 | B10             | No confirmed PLE match | Public        | Natural Sciences             |
| ENDOZO, ALLYSTER ARCEO||7/11/1991             |    1121208475 |   2012 |                 180 |            99 |       733 |                  97 |                   83 | B10             | No confirmed PLE match | Private       | Natural Sciences             |
| GIGANTE, IAN PAULO CALICDAN||04/15/1992       |    1111301173 |   2013 |                 182 |            99 |       717 |                  79 |                  103 | B10             | No confirmed PLE match | Private       | Medical & Allied             |
| GUION, GINAREY GRACE ANN SARMIENTO||9/8/1993  |    1121104797 |   2011 |                 200 |            99 |       733 |                 102 |                   98 | B10             | No confirmed PLE match | Public        | Medical & Allied             |
| WANG, WUDA||8/8/1989                          |    1111408204 |   2014 |                 173 |            99 |       720 |                  81 |                   92 | B10             | No confirmed PLE match | Public        | Natural Sciences             |
| SABBAN, FREDERICO BUNUAN||6/6/1994            |    1041304943 |   2013 |                 196 |            99 |       723 |                  96 |                  100 | B10             | No confirmed PLE match | Private       | Natural Sciences             |
| DE PANO, JOJIEMAR SALONGA||01/29/1989         |    1121006520 |   2010 |                 208 |            99 |       778 |                 110 |                   98 | B10             | No confirmed PLE match | Public        | Natural Sciences             |

