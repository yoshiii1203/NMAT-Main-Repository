# Page 13: CHED Compliance — CMO No. __, s. 2026

**Generated:** 2026-07-28 01:18

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subsets:**
- `bestobservable` (Year <= 2014) — PLE-linked summaries
- `besttrend` (2006-2018) — score distributions and cut-off scenarios

**Filters:** None (full unfiltered dataset)

---

## Section A: National PLE Benchmark

Annual national PLE passing rates and 5-year rolling average. The CHED amendment uses the 5-year rolling average as the benchmark: PHEIs above this benchmark may set cut-off at 30th percentile; those below must maintain 40th percentile.

**Table A1. Annual national PLE passing rates with 5-year rolling average**

|   Year |   n_examinees |   n_confirmed_ple |   ple_rate_pct |   5yr_rolling_avg_pct |
|-------:|--------------:|------------------:|---------------:|----------------------:|
|   2006 |          3665 |              2038 |          55.61 |                   nan |
|   2007 |          3660 |              1868 |          51.04 |                   nan |
|   2008 |          4849 |              2514 |          51.85 |                 52.83 |
|   2009 |          6881 |              3226 |          46.88 |                 51.34 |
|   2010 |          8008 |              3808 |          47.55 |                 50.59 |
|   2011 |          8731 |              3853 |          44.13 |                 48.29 |
|   2012 |          9145 |              4066 |          44.46 |                 46.97 |
|   2013 |          9121 |              3951 |          43.32 |                 45.27 |
|   2014 |         10441 |              3949 |          37.82 |                 43.46 |

**Latest 5-year national average (benchmark):**

| Metric | Value |
|--------|------:|
| Latest 5-year national avg | 43.46% |
| Reference year | 2014 |

---
## Section B: Per-HEI PLE Performance vs National Benchmark

Each HEI's PLE passing rate compared to the national 5-year rolling average. Only HEIs with at least 5 observable best-record examinees are shown. Green = above benchmark (30th percentile eligible), Red = below benchmark (40th percentile required).

**Summary:**

| Metric | Value |
|--------|------:|
| HEIs above benchmark | 197 |
| HEIs below benchmark | 342 |
| National benchmark | 43.46% |

**Table B1. Per-HEI PLE performance vs benchmark**
*(Minimum examinees: 5, sorted by PLE rate descending)*

| UNIVERSITY                                                                            | UNI_TYPE      |   n_examinees |   median_percentile |   ple_rate_pct | status                          |
|:--------------------------------------------------------------------------------------|:--------------|--------------:|--------------------:|---------------:|:--------------------------------|
| SAN SEBASTIAN COLLEGE - RECOLETOS CANLUBANG                                           | Private       |             5 |                74.5 |             80 | Above benchmark (30th eligible) |
| BATANGAS STATE UNIVERSITY BATANGAS CITY                                               | Public        |             5 |                  45 |             80 | Above benchmark (30th eligible) |
| UNIVERSITY OF CEBU - LAPULAPU AND MANDAUE                                             | Private       |             5 |                  44 |             80 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS CEBU                                     | Public        |            34 |                  81 |          79.41 | Above benchmark (30th eligible) |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                               | Public        |            11 |                  50 |          72.73 | Above benchmark (30th eligible) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA - CALAMBA                                   | Private       |            14 |                  73 |          71.43 | Above benchmark (30th eligible) |
| UNIVERSITY OF LUZON ( DAGUPAN CITY )                                                  | Private       |             7 |                  25 |          71.43 | Above benchmark (30th eligible) |
| CATANDUANES STATE COLLEGE                                                             | Public        |             7 |                   9 |          71.43 | Above benchmark (30th eligible) |
| CALAMBA DOCTORS' COLLEGE                                                              | Private       |            10 |                  52 |             70 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES SCH. OF HEALTH SCIENCES -LEYTE                          | Public        |            10 |                23.5 |             70 | Above benchmark (30th eligible) |
| ATENEO DE MANILA UNIVERSITY                                                           | Private       |           721 |                  89 |          69.76 | Above benchmark (30th eligible) |
| UNIVERSITY OF BOHOL TAGBILARAN CITY                                                   | Private       |            13 |                  40 |          69.23 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS ILOILO                                        | Public        |           179 |                  75 |          68.72 | Above benchmark (30th eligible) |
| CATANDUANES STATE COLLEGE - MAIN                                                      | Public        |            19 |                  48 |          68.42 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - LOS BANOS LAGUNA                                      | Public        |           450 |                  81 |          67.56 | Above benchmark (30th eligible) |
| NORTHERN NEGROS STATE COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                        | Public        |             6 |                  68 |          66.67 | Above benchmark (30th eligible) |
| NOTRE DAME OF MIDSAYAP COLLEGE                                                        | Private       |             6 |                  63 |          66.67 | Above benchmark (30th eligible) |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE NEGROS OCCIDENTAL                                | Private       |            12 |                  50 |          66.67 | Above benchmark (30th eligible) |
| FELLOWSHIP BAPTIST COLLEGE                                                            | Private       |             6 |                  72 |          66.67 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - CEBU COLLEGE                                          | Public        |            45 |                  75 |          66.67 | Above benchmark (30th eligible) |
| SAMAR STATE UNIVERSITY - MAIN                                                         | Public        |             6 |                  48 |          66.67 | Above benchmark (30th eligible) |
| UNIVERSITY OF ILOILO                                                                  | Private       |             9 |                  74 |          66.67 | Above benchmark (30th eligible) |
| AGO MEDICAL EDUCATIONAL FOUNDATION LEGASPI CITY                                       | Private       |             6 |                  31 |          66.67 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - TACLOBAN                                              | Public        |            48 |                  62 |          66.67 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                                | Public        |          2344 |                  90 |          64.51 | Above benchmark (30th eligible) |
| VELEZ COLLEGE CEBU                                                                    | Private       |           546 |                  52 |          64.47 | Above benchmark (30th eligible) |
| JOHN PAUL II COLLEGE OF DAVAO                                                         | Private       |            14 |                  43 |          64.29 | Above benchmark (30th eligible) |
| COLLEGE OF HOLY SPIRIT-MANILA                                                         | Private       |            11 |                  18 |          63.64 | Above benchmark (30th eligible) |
| BALIUAG UNIVERSITY                                                                    | Private       |            11 |                  41 |          63.64 | Above benchmark (30th eligible) |
| SILLIMAN UNIVERSITY DUMAGUETE CITY                                                    | Private       |           221 |                  53 |           62.9 | Above benchmark (30th eligible) |
| U.P. VISAYAS (TACLOBAN CITY LEYTE)                                                    | Public        |             8 |                70.5 |           62.5 | Above benchmark (30th eligible) |
| CHIANG KAI SHEK COLLEGE                                                               | Private       |             8 |                58.5 |           62.5 | Above benchmark (30th eligible) |
| Texila American University                                                            | Not Specified |             8 |                  60 |           62.5 | Above benchmark (30th eligible) |
| HOLY NAME UNIVERSITY - TAGBILARAN CITY                                                | Private       |            21 |                  41 |           61.9 | Above benchmark (30th eligible) |
| CANOSSA COLLEGE                                                                       | Private       |            13 |                  73 |          61.54 | Above benchmark (30th eligible) |
| UNIVERSITY OF CEBU (FORMERLY CEBU CENTRAL COLLEGES)                                   | Private       |            28 |                36.5 |          60.71 | Above benchmark (30th eligible) |
| Mariano Marcos State University - College Of Fisheries - Currimao                     | Not Specified |           104 |                46.5 |          60.58 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO CITY                                           | Public        |           190 |                  69 |          60.53 | Above benchmark (30th eligible) |
| COLLEGE OF THE HOLY SPIRIT OF TARLAC                                                  | Private       |             5 |                  52 |             60 | Above benchmark (30th eligible) |
| Adventist University Of Indonesia                                                     | Not Specified |             5 |                  70 |             60 | Above benchmark (30th eligible) |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE                                                  | Private       |            35 |                  61 |             60 | Above benchmark (30th eligible) |
| URDANETA CITY UNIVERSITY                                                              | Public        |            10 |                49.5 |             60 | Above benchmark (30th eligible) |
| CENTRAL COLLEGE OF PANGASINAN - SAN CARLOS CITY PANGASINAN                            | Private       |             5 |                  47 |             60 | Above benchmark (30th eligible) |
| AQUINAS UNIVERSITY LEGASPI CITY                                                       | Private       |            20 |                  29 |             60 | Above benchmark (30th eligible) |
| PLT COLLEGE                                                                           | Private       |             5 |                  57 |             60 | Above benchmark (30th eligible) |
| DE LA SALLE COLLEGE OF SAINT BENILDE - MANILA                                         | Private       |            20 |                57.5 |             60 | Above benchmark (30th eligible) |
| UNIVERSITY OF BOHOL                                                                   | Private       |            10 |                  51 |             60 | Above benchmark (30th eligible) |
| COLEGIO DE SAN JUAN DE LETRAN MANILA                                                  | Private       |             5 |                  41 |             60 | Above benchmark (30th eligible) |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                    | Public        |            17 |                  73 |          58.82 | Above benchmark (30th eligible) |
| DE LA SALLE UNIVERSITY - MANILA                                                       | Private       |          1382 |                  70 |          58.68 | Above benchmark (30th eligible) |
| CEBU NORMAL UNIVERSITY                                                                | Public        |           229 |                  67 |          58.52 | Above benchmark (30th eligible) |
| FAR EASTERN UNIVERSITY - NRMF (FAIRVIEW Q.C.)                                         | Private       |           409 |                  34 |          58.44 | Above benchmark (30th eligible) |
| SACRED HEART COLLEGE OF LUCENA                                                        | Private       |            36 |                52.5 |          58.33 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                               | Public        |          2042 |                  90 |          58.28 | Above benchmark (30th eligible) |
| WESTERN STATE UNIVERSITY OF COLORADO                                                  | Foreign       |            19 |                  50 |          57.89 | Above benchmark (30th eligible) |
| SAINT LOUIS UNIVERSITY - BAGUIO                                                       | Private       |           374 |                  43 |          57.22 | Above benchmark (30th eligible) |
| RUTGERS UNIVERSITY                                                                    | Foreign       |             7 |                  81 |          57.14 | Above benchmark (30th eligible) |
| ARELLANO UNIVERSITY - PASIG                                                           | Private       |            14 |                  44 |          57.14 | Above benchmark (30th eligible) |
| BICOL UNIVERSITY COLLEGE OF SCIENCE LEGAZPI CITY                                      | Public        |            21 |                  17 |          57.14 | Above benchmark (30th eligible) |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - SOUTH LA UNION                         | Public        |             7 |                  67 |          57.14 | Above benchmark (30th eligible) |
| NEGROS ORIENTAL STATE UNIVERSITY                                                      | Public        |             7 |                  13 |          57.14 | Above benchmark (30th eligible) |
| CORDILLERA CAREER DEVELOPMENT COLLEGE                                                 | Private       |             7 |                  60 |          57.14 | Above benchmark (30th eligible) |
| COLEGIO DE SAN LORENZO RUIZ DE MANILA OF NORTHERN SAMAR                               | Private       |             7 |                  55 |          57.14 | Above benchmark (30th eligible) |
| ST. LOUIS UNIVERSITY BAGUIO CITY                                                      | Private       |           199 |                  51 |          56.78 | Above benchmark (30th eligible) |
| MARIANO MARCOS STATE UNIVERSITY ILOCOS NORTE                                          | Public        |            32 |                  35 |          56.25 | Above benchmark (30th eligible) |
| UNIVERSITY OF EASTERN PHILIPPINES - SAMAR                                             | Public        |            16 |                  14 |          56.25 | Above benchmark (30th eligible) |
| LYCEUM NORTHWESTERN DAGUPAN CITY                                                      | Private       |            64 |                  19 |          56.25 | Above benchmark (30th eligible) |
| XAVIER UNIVERSITY CAGAYAN DE ORO CITY                                                 | Private       |           339 |                  52 |          55.75 | Above benchmark (30th eligible) |
| RIVERSIDE COLLEGE BACOLOD CITY                                                        | Private       |            27 |                  37 |          55.56 | Above benchmark (30th eligible) |
| LYCEUM OF ILIGAN FOUNDATION                                                           | Private       |             9 |                  76 |          55.56 | Above benchmark (30th eligible) |
| UNIVERSITY OF SAN CARLOS CEBU CITY                                                    | Private       |           157 |                  40 |          54.78 | Above benchmark (30th eligible) |
| ST. ALEXIUS COLLEGE                                                                   | Private       |            11 |                  63 |          54.55 | Above benchmark (30th eligible) |
| MINDANAO STATE UNIVERSITY ILIGAN CITY                                                 | Public        |           197 |                  53 |          54.31 | Above benchmark (30th eligible) |
| UNIVERSITY OF ASIA AND THE PACIFIC                                                    | Private       |            17 |                  42 |          52.94 | Above benchmark (30th eligible) |
| CAVITE STATE UNIVERSITY - MAIN                                                        | Public        |            19 |                  57 |          52.63 | Above benchmark (30th eligible) |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING & LIBERAL ARTS                            | Private       |            19 |                  47 |          52.63 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                       | Public        |            76 |                  68 |          52.63 | Above benchmark (30th eligible) |
| 13207A                                                                                | Not Specified |            21 |                  34 |          52.38 | Above benchmark (30th eligible) |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                              | Public        |            23 |                85.5 |          52.17 | Above benchmark (30th eligible) |
| WEST NEGROS UNIVERSITY                                                                | Private       |            23 |                  55 |          52.17 | Above benchmark (30th eligible) |
| UNIVERSITY OF ST. LA SALLE BACOLOD CITY                                               | Private       |            96 |                46.5 |          52.08 | Above benchmark (30th eligible) |
| HOLY INFANT COLLEGE                                                                   | Private       |            27 |                  51 |          51.85 | Above benchmark (30th eligible) |
| CENTRAL LUZON DOCTORS' HOSPITAL EDUCATIONAL INSTITUTION                               | Private       |            29 |                  57 |          51.72 | Above benchmark (30th eligible) |
| ATENEO DE MANILA UNIVERSITY - QUEZON CITY                                             | Private       |           973 |                  79 |           51.7 | Above benchmark (30th eligible) |
| WEST VISAYAS STATE UNIVERSITY ILOILO                                                  | Public        |           342 |                  59 |          51.46 | Above benchmark (30th eligible) |
| AQUINAS UNIVERSITY OF LEGAZPI                                                         | Private       |            70 |                  44 |          51.43 | Above benchmark (30th eligible) |
| UNIVERSIDAD DE STA. ISABEL NAGA CITY                                                  | Private       |            39 |                  40 |          51.28 | Above benchmark (30th eligible) |
| CENTRAL LUZON STATE UNIVERSITY                                                        | Public        |            47 |                  54 |          51.06 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE EAST - RAMON MAGSAYSAY MEM. MEDICAL CENTER                          | Private       |            55 |                  57 |          50.91 | Above benchmark (30th eligible) |
| BULACAN STATE UNIVERSITY - MAIN                                                       | Public        |            67 |                  62 |          50.75 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE EAST (C.M. RECTO MANILA)                                            | Private       |           123 |                  55 |          50.41 | Above benchmark (30th eligible) |
| REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION TACLOBAN                               | Private       |           127 |                  38 |          50.39 | Above benchmark (30th eligible) |
| ATENEO DE DAVAO UNIVERSITY                                                            | Private       |           718 |                  50 |          50.14 | Above benchmark (30th eligible) |
| UNIVERSITY OF TEXAS                                                                   | Foreign       |             8 |                  96 |             50 | Above benchmark (30th eligible) |
| ANDRES BONIFACIO COLLEGE                                                              | Private       |             6 |                45.5 |             50 | Above benchmark (30th eligible) |
| CARITAS FAMILY HOSPITAL AND COLLEGES                                                  | Private       |             8 |                  63 |             50 | Above benchmark (30th eligible) |
| LYCEUM OF THE PHILIPPINES                                                             | Private       |            14 |                  46 |             50 | Above benchmark (30th eligible) |
| LA CONSOLACION UNIVERSITY PHILIPPINES                                                 | Private       |             6 |                57.5 |             50 | Above benchmark (30th eligible) |
| SAINT SCHOLASTICA'S COLLEGE TACLOBAN                                                  | Private       |           112 |                  48 |             50 | Above benchmark (30th eligible) |
| SACRED HEART COLLEGE LUCENA CITY                                                      | Private       |            12 |                  39 |             50 | Above benchmark (30th eligible) |
| IMMACULATE CONCEPTION COLLEGE - ALBAY                                                 | Private       |             8 |                  66 |             50 | Above benchmark (30th eligible) |
| MARY HELP OF CHRISTIANS COLLEGE SEMINARY                                              | Private       |            10 |                15.5 |             50 | Above benchmark (30th eligible) |
| BICOL UNIVERSITY - TABACO                                                             | Public        |            24 |                  50 |             50 | Above benchmark (30th eligible) |
| BICOL UNIVERSITY COLLEGE OF NURSING LEGAZPI CITY                                      | Public        |            14 |                53.5 |             50 | Above benchmark (30th eligible) |
| ALDERSGATE COLLEGE                                                                    | Private       |             6 |                53.5 |             50 | Above benchmark (30th eligible) |
| NATIONAL UNIVERSITY                                                                   | Private       |            10 |                51.5 |             50 | Above benchmark (30th eligible) |
| ARRIESGADO COLLEGE FOUNDATION                                                         | Private       |             6 |                50.5 |             50 | Above benchmark (30th eligible) |
| MABINI COLLEGES                                                                       | Private       |             6 |                  81 |             50 | Above benchmark (30th eligible) |
| MANUEL S. ENVERGA UNIVERSITY FOUNDATION - LUCENA                                      | Private       |             8 |                  62 |             50 | Above benchmark (30th eligible) |
| OUR LADY OF FATIMA NOVALICHES                                                         | Private       |             6 |                18.5 |             50 | Above benchmark (30th eligible) |
| PHILIPPINE REHABILITATION INSTITUTE                                                   | Private       |            12 |                  34 |             50 | Above benchmark (30th eligible) |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-ALABANG ZAPOTE                              | Private       |             8 |                25.5 |             50 | Above benchmark (30th eligible) |
| FATHER SATURNINO M. URIOS UNIVERSITY                                                  | Private       |            46 |                  50 |             50 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE IMMACULATE CONCEPCION DAVAO CITY                                    | Private       |            24 |                28.5 |             50 | Above benchmark (30th eligible) |
| SAN LORENZO RUIZ COLLEGE OF ORMOC                                                     | Private       |            16 |                  32 |             50 | Above benchmark (30th eligible) |
| UNIVERSITY OF SANTO TOMAS                                                             | Private       |         10721 |                  64 |          49.79 | Above benchmark (30th eligible) |
| ST. PAUL UNIVERSITY ILOILO                                                            | Private       |           201 |                  59 |          49.75 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                              | Public        |           193 |                  73 |          49.74 | Above benchmark (30th eligible) |
| CEBU DOCTORS COLLEGE CEBU CITY                                                        | Private       |           148 |                  28 |          49.32 | Above benchmark (30th eligible) |
| UNIVERSITY OF SAN AGUSTIN - ILOILO CITY                                               | Private       |           122 |                  40 |          49.18 | Above benchmark (30th eligible) |
| LYCEUM OF THE PHILIPPINES UNIVERSITY - BATANGAS                                       | Private       |           104 |                  52 |          49.04 | Above benchmark (30th eligible) |
| UNIVERSITY OF PANGASINAN                                                              | Private       |            70 |                  46 |          48.57 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                               | Public        |           248 |                  66 |          48.39 | Above benchmark (30th eligible) |
| NEW ERA UNIVERSITY                                                                    | Private       |            56 |                  47 |          48.21 | Above benchmark (30th eligible) |
| UNIVERSIDAD DE STA. ISABEL                                                            | Private       |           152 |                  53 |          48.03 | Above benchmark (30th eligible) |
| CEBU DOCTOR'S UNIVERSITY COLLEGE OF MEDICINE - MANDAUE CITY CEBU                      | Private       |            50 |                  50 |             48 | Above benchmark (30th eligible) |
| UNIVERSITY OF PERPETUAL HELP - DR. JOSE G. TAMAYO MEDICAL UNIVERSITY                  | Private       |            48 |                  59 |          47.92 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                             | Public        |           548 |                  70 |          47.81 | Above benchmark (30th eligible) |
| CENTRAL LUZON DOCTOR'S HOSPITAL TARLAC                                                | Private       |            21 |                  41 |          47.62 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                                | Public        |           332 |                  70 |          47.59 | Above benchmark (30th eligible) |
| AGO MEDICAL AND EDUCATIONAL CENTER LEGAZPI CITY                                       | Private       |            19 |                  28 |          47.37 | Above benchmark (30th eligible) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - LAGUNA                                          | Private       |            38 |                  45 |          47.37 | Above benchmark (30th eligible) |
| UNIVERSITY OF PERPETUAL HELP COLLEGE OF LAS PINAS                                     | Private       |            19 |                  39 |          47.37 | Above benchmark (30th eligible) |
| DE LA SALLE - COLLEGE OF SAINT BENILDE                                                | Private       |            19 |                  68 |          47.37 | Above benchmark (30th eligible) |
| UNIVERSITY OF PANGASINAN DAGUPAN CITY                                                 | Private       |            17 |                  30 |          47.06 | Above benchmark (30th eligible) |
| SAN PEDRO COLLEGE DAVAO CITY                                                          | Private       |           492 |                36.5 |          46.95 | Above benchmark (30th eligible) |
| MINDANAO STATE UNIVERSITY GENERAL SANTOS CITY                                         | Public        |            32 |                37.5 |          46.88 | Above benchmark (30th eligible) |
| SILLIMAN UNIVERSITY                                                                   | Private       |           601 |                  54 |          46.76 | Above benchmark (30th eligible) |
| UNIVERSITY OF ST. LA SALLE                                                            | Private       |           391 |                  58 |          46.55 | Above benchmark (30th eligible) |
| UNIVERSITY OF LA SALETTE SANTIAGO CITY                                                | Private       |            28 |                30.5 |          46.43 | Above benchmark (30th eligible) |
| CEBU INSTITUTE OF TECHNOLOGY - UNIVERSITY                                             | Private       |            13 |                  46 |          46.15 | Above benchmark (30th eligible) |
| ST. JUDE COLLEGE MANILA                                                               | Private       |            39 |                  26 |          46.15 | Above benchmark (30th eligible) |
| ST. SCHOLASTICA'S COLLEGE - TACLOBAN CITY                                             | Private       |            26 |                  31 |          46.15 | Above benchmark (30th eligible) |
| COLEGIO DE DAGUPAN                                                                    | Private       |            13 |                  54 |          46.15 | Above benchmark (30th eligible) |
| AGO MEDICAL AND EDUCATIONAL CENTER - BICOL CHRISTIAN COLLEGE OF MEDICINE              | Private       |            39 |                  49 |          46.15 | Above benchmark (30th eligible) |
| MANILA ADVENTIST MEDICAL CENTER AND COLLEGES                                          | Private       |            26 |                  58 |          46.15 | Above benchmark (30th eligible) |
| NARESUAN UNIVERSITY                                                                   | Foreign       |            13 |                55.5 |          46.15 | Above benchmark (30th eligible) |
| HOLY ANGEL UNIVERSITY                                                                 | Private       |            50 |                44.5 |             46 | Above benchmark (30th eligible) |
| COLEGIO DE SAN AGUSTIN BACOLOD                                                        | Private       |            22 |                  29 |          45.45 | Above benchmark (30th eligible) |
| NOTRE DAME OF MARBEL UNIV.                                                            | Private       |            11 |                  42 |          45.45 | Above benchmark (30th eligible) |
| UNIVERSITY OF CORDILLERAS                                                             | Private       |            11 |                  37 |          45.45 | Above benchmark (30th eligible) |
| BROKENSHIRE COLLEGE                                                                   | Private       |           198 |                  46 |          45.45 | Above benchmark (30th eligible) |
| LEYTE NORMAL UNIVERSITY                                                               | Public        |            11 |                  34 |          45.45 | Above benchmark (30th eligible) |
| LYCEUM OF THE PHILIPPINES - ST. CABRINI COLLEGE OF ALLIED MEDICINE                    | Private       |            11 |                  44 |          45.45 | Above benchmark (30th eligible) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - BINAN LAGUNA                                    | Private       |            44 |                30.5 |          45.45 | Above benchmark (30th eligible) |
| NORTHWESTERN UNIVERSITY                                                               | Private       |            11 |                  33 |          45.45 | Above benchmark (30th eligible) |
| UNIVERSITY OF NUEVA CACERES                                                           | Private       |            33 |                  39 |          45.45 | Above benchmark (30th eligible) |
| SAINT MARY'S UNIVERSITY                                                               | Private       |            75 |                48.5 |          45.33 | Above benchmark (30th eligible) |
| ATENEO DE NAGA UNIVERSITY                                                             | Private       |           137 |                  45 |          45.26 | Above benchmark (30th eligible) |
| VELEZ COLLEGE                                                                         | Private       |           716 |                  60 |          45.25 | Above benchmark (30th eligible) |
| SAINT PAUL UNIVERSITY PHILIPPINES                                                     | Private       |           186 |                  52 |          45.16 | Above benchmark (30th eligible) |
| UNIVERSITY OF NEGROS OCCIDENTAL-RECOLETOS                                             | Private       |            91 |                  54 |          45.05 | Above benchmark (30th eligible) |
| DR. CARLOS S. LANTING COLLEGE                                                         | Private       |            40 |                  38 |             45 | Above benchmark (30th eligible) |
| DE LA SALLE UNIVERSITY - DASMARIÑAS CAVITE                                            | Private       |           452 |                  34 |          44.91 | Above benchmark (30th eligible) |
| UNIVERSITY OF ST. LA SALLE - DASMARIÑAS CAVITE                                        | Private       |            29 |                  36 |          44.83 | Above benchmark (30th eligible) |
| ST. JOSEPH'S COLLEGE OF QUEZON CITY                                                   | Private       |            29 |                  39 |          44.83 | Above benchmark (30th eligible) |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION INC.                                          | Private       |            47 |                  23 |          44.68 | Above benchmark (30th eligible) |
| METROPOLITAN HOSPITAL COLLEGE OF NURSING                                              | Private       |            56 |                  44 |          44.64 | Above benchmark (30th eligible) |
| ATENEO DE ZAMBOANGA UNIVERSITY                                                        | Private       |           672 |                  39 |          44.64 | Above benchmark (30th eligible) |
| NOTRE DAME OF MARBEL COLLEGE SOUTH COTABATO                                           | Private       |             9 |                  38 |          44.44 | Above benchmark (30th eligible) |
| CALAYAN EDUCATIONAL FOUNDATION                                                        | Private       |             9 |                52.5 |          44.44 | Above benchmark (30th eligible) |
| HOLY ANGEL UNIVERSITY ANGELES CITY                                                    | Private       |            18 |                  40 |          44.44 | Above benchmark (30th eligible) |
| CARAGA STATE UNIVERSITY - MAIN                                                        | Public        |             9 |                39.5 |          44.44 | Above benchmark (30th eligible) |
| NAGA COLLEGE FOUNDATION                                                               | Private       |             9 |                  68 |          44.44 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE VISAYAS - MANDAUE                                                   | Private       |            27 |                  40 |          44.44 | Above benchmark (30th eligible) |
| LIPA CITY COLLEGES                                                                    | Private       |             9 |                  50 |          44.44 | Above benchmark (30th eligible) |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                                | Public        |            61 |                  60 |          44.26 | Above benchmark (30th eligible) |
| CENTRO ESCOLAR UNIVERSITY - MENDIOLA MANILA                                           | Private       |           369 |                  28 |          44.17 | Above benchmark (30th eligible) |
| SAINT LOUIS UNIVERSITY                                                                | Private       |          1225 |                  54 |          44.16 | Above benchmark (30th eligible) |
| CEBU DOCTOR'S UNIVERSITY                                                              | Private       |          1149 |                  47 |          44.13 | Above benchmark (30th eligible) |
| UNIVERSITY OF THE EAST RAMON MAGSAYSAY MEMORIAL MEDICAL CENTER                        | Private       |           340 |                57.5 |          44.12 | Above benchmark (30th eligible) |
| UNIVERSITY OF SAN JOSE - RECOLETOS                                                    | Private       |            25 |                  42 |             44 | Above benchmark (30th eligible) |
| UNIVERSITY OF BAGUIO                                                                  | Private       |           175 |                  47 |             44 | Above benchmark (30th eligible) |
| COLEGIO DE SAN JUAN DE LETRAN                                                         | Private       |            66 |                  50 |          43.94 | Above benchmark (30th eligible) |
| UERM MEMORIAL MEDICAL CENTER                                                          | Private       |            82 |                  49 |           43.9 | Above benchmark (30th eligible) |
| MANILA CENTRAL UNIVERSITY                                                             | Private       |           351 |                  38 |          43.87 | Above benchmark (30th eligible) |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                  | Public        |           589 |                  64 |           43.8 | Above benchmark (30th eligible) |
| UNIVERSITY OF SOUTHERN PHILIPPINES FOUNDATION                                         | Private       |            32 |                22.5 |          43.75 | Above benchmark (30th eligible) |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION                                               | Private       |            48 |                42.5 |          43.75 | Above benchmark (30th eligible) |
| UNIVERSITY OF TORONTO                                                                 | Foreign       |            16 |                  80 |          43.75 | Above benchmark (30th eligible) |
| CENTRAL LUZON STATE UNIVERSITY NUEVA ECIJA                                            | Public        |            16 |                31.5 |          43.75 | Above benchmark (30th eligible) |
| UNION CHRISTIAN COLLEGE                                                               | Private       |            16 |                  42 |          43.75 | Above benchmark (30th eligible) |
| UNIVERSITY OF CEBU - BANILAD                                                          | Private       |           103 |                  41 |          43.69 | Above benchmark (30th eligible) |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING AND LIBERAL ARTS                          | Private       |            78 |                  55 |          43.59 | Above benchmark (30th eligible) |
| BENGUET STATE UNIVERSITY                                                              | Public        |            23 |                  42 |          43.48 | Above benchmark (30th eligible) |
| LORMA COLLEGE SAN FERNANDO LA UNION                                                   | Private       |            23 |                  19 |          43.48 | Above benchmark (30th eligible) |
| PILAR COLLEGE                                                                         | Private       |            23 |                  32 |          43.48 | Above benchmark (30th eligible) |
| MOUNTAIN VIEW COLLEGE                                                                 | Private       |           129 |                  52 |          43.41 | Below benchmark (40th required) |
| LYCEUM OF BATANGAS                                                                    | Private       |            30 |                  23 |          43.33 | Below benchmark (40th required) |
| FAR EASTERN UNIVERSITY                                                                | Private       |          2216 |                  45 |          42.96 | Below benchmark (40th required) |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                            | Public        |           447 |                  53 |          42.95 | Below benchmark (40th required) |
| VIRGINIA COMMONWEALTH UNIVERSITY                                                      | Foreign       |             7 |                  77 |          42.86 | Below benchmark (40th required) |
| ARELLANO UNIVERSITY - MANILA                                                          | Private       |            70 |                  46 |          42.86 | Below benchmark (40th required) |
| VISAYAS STATE UNIVERSITY - MAIN                                                       | Public        |             7 |                  54 |          42.86 | Below benchmark (40th required) |
| INTERNATIONAL COLLEGES OF ASIA - TAMBAC PANGASINAN                                    | Private       |             7 |                  26 |          42.86 | Below benchmark (40th required) |
| HOLY TRINITY COLLEGE PUERTO PRINCESA                                                  | Private       |             7 |                  21 |          42.86 | Below benchmark (40th required) |
| 13155D                                                                                | Not Specified |             7 |                  70 |          42.86 | Below benchmark (40th required) |
| ST. PAUL UNIVERSITY SURIGAO                                                           | Private       |             7 |                  56 |          42.86 | Below benchmark (40th required) |
| DE LA SALLE - ARANETA UNIVERSITY                                                      | Private       |             7 |                  27 |          42.86 | Below benchmark (40th required) |
| RIVERSIDE COLLEGE OF NURSING BACOLOD                                                  | Private       |            21 |                  32 |          42.86 | Below benchmark (40th required) |
| ILOCOS SUR COMMUNITY COLLEGE - BANTAY ILOCOS SUR                                      | Public        |            14 |                  27 |          42.86 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA                                             | Private       |           442 |                  59 |          42.76 | Below benchmark (40th required) |
| TRINITY UNIVERSITY OF ASIA                                                            | Private       |           566 |                  56 |          42.76 | Below benchmark (40th required) |
| MINDANAO STATE UNIVERSITY MARAWI CITY                                                 | Public        |           328 |                37.5 |          42.68 | Below benchmark (40th required) |
| BENGUET STATE UNIVERSITY - MAIN                                                       | Public        |            75 |                  57 |          42.67 | Below benchmark (40th required) |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                         | Public        |            68 |                  67 |          42.65 | Below benchmark (40th required) |
| UNIVERSITY OF THE CORDILLERAS (BCF)                                                   | Private       |            61 |                  33 |          42.62 | Below benchmark (40th required) |
| BICOL UNIVERSITY                                                                      | Public        |            47 |                29.5 |          42.55 | Below benchmark (40th required) |
| DE LA SALLE UNIVERSITY - DASMARIÑAS                                                   | Private       |           588 |                  54 |          42.52 | Below benchmark (40th required) |
| MAKATI MEDICAL CENTER COLLEGE OF NURSING                                              | Private       |           137 |                  47 |          42.34 | Below benchmark (40th required) |
| WESTERN MINDANAO STATE UNIVERSITY                                                     | Public        |           345 |                  46 |          42.32 | Below benchmark (40th required) |
| ST. PAUL UNIVERSITY - MANILA                                                          | Private       |           104 |                42.5 |          42.31 | Below benchmark (40th required) |
| OUR LADY OF FATIMA UNIVERSITY - LAGRO QUEZON CITY                                     | Private       |            52 |                  32 |          42.31 | Below benchmark (40th required) |
| MINDANAO MEDICAL FOUNDATION COLLEGE                                                   | Private       |            26 |                  65 |          42.31 | Below benchmark (40th required) |
| FEU - DR. NICANOR REYES MEDICAL FOUNDATION                                            | Private       |           480 |                  52 |          42.29 | Below benchmark (40th required) |
| OUR LADY OF FATIMA UNIVERSITY - QUEZON CITY                                           | Private       |           178 |                  42 |          42.13 | Below benchmark (40th required) |
| CENTRAL PHILIPPINE UNIVERSITY ILOILO                                                  | Private       |           100 |                  46 |             42 | Below benchmark (40th required) |
| LORMA COLLEGES                                                                        | Private       |            50 |                  37 |             42 | Below benchmark (40th required) |
| ADVENTIST UNIVERSITY OF THE PHILIPPINES                                               | Private       |           331 |                  53 |          41.99 | Below benchmark (40th required) |
| BROKENSHIRE COLLEGE DAVAO CITY                                                        | Private       |            43 |                  28 |          41.86 | Below benchmark (40th required) |
| DE LA SALLE - HEALTH SCIENCES CAMPUS                                                  | Private       |           129 |                  38 |          41.86 | Below benchmark (40th required) |
| MISAMIS UNIVERSITY - OZAMIS CITY                                                      | Private       |            55 |                47.5 |          41.82 | Below benchmark (40th required) |
| SOUTHVILLE INTERNATIONAL SCHOOL AND COLLEGES                                          | Private       |           122 |                  53 |           41.8 | Below benchmark (40th required) |
| CENTRAL PHILIPPINE UNIVERSITY                                                         | Private       |           285 |                51.5 |          41.75 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA BERKELEY                                                     | Foreign       |            12 |                  81 |          41.67 | Below benchmark (40th required) |
| OUR LADY OF GUADALUPE COLLEGES                                                        | Private       |            12 |                  32 |          41.67 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP - CALAMBA LAGUNA                                         | Private       |            12 |                  35 |          41.67 | Below benchmark (40th required) |
| SAN PEDRO COLLEGE                                                                     | Private       |           987 |                  52 |          41.44 | Below benchmark (40th required) |
| ANGELES UNIVERSITY FOUNDATION                                                         | Private       |           430 |                  48 |           41.4 | Below benchmark (40th required) |
| WESLEYAN UNIVERSITY - PHILIPPINES (CABANATUAN)                                        | Private       |            63 |                  38 |          41.27 | Below benchmark (40th required) |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                      | Public        |           764 |                  53 |          41.23 | Below benchmark (40th required) |
| LOURDES COLLEGE                                                                       | Private       |            17 |                  49 |          41.18 | Below benchmark (40th required) |
| ST. PAUL UNIVERSITY DUMAGUETE                                                         | Private       |            34 |                  52 |          41.18 | Below benchmark (40th required) |
| BICOL UNIVERSITY - MAIN                                                               | Public        |           241 |                  59 |          41.08 | Below benchmark (40th required) |
| DE LA SALLE HEALTH SCIENCES INSTITUTE                                                 | Private       |           322 |                  53 |          40.99 | Below benchmark (40th required) |
| WESTERN MINDANAO STATE UNIVERSITY ZAMBOANGA CITY                                      | Public        |           144 |                27.5 |          40.97 | Below benchmark (40th required) |
| ASSUMPTION COLLEGE MAKATI                                                             | Private       |            22 |                  45 |          40.91 | Below benchmark (40th required) |
| UNIVERSITY OF SAN AGUSTIN                                                             | Private       |           265 |                  51 |          40.75 | Below benchmark (40th required) |
| MINDANAO STATE UNIVERSITY - MARAWI                                                    | Public        |           443 |                52.5 |          40.63 | Below benchmark (40th required) |
| EASTER COLLEGE                                                                        | Private       |            64 |                37.5 |          40.62 | Below benchmark (40th required) |
| MANILA TYTANA COLLEGES                                                                | Private       |           380 |                43.5 |          40.53 | Below benchmark (40th required) |
| UNIVERSITY OF SAN CARLOS                                                              | Private       |           264 |                47.5 |          40.53 | Below benchmark (40th required) |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                                | Public        |            57 |                  48 |          40.35 | Below benchmark (40th required) |
| SOUTHEAST ASIAN COLLEGE                                                               | Private       |            57 |                40.5 |          40.35 | Below benchmark (40th required) |
| SAN BEDA COLLEGE                                                                      | Private       |           273 |                  45 |          40.29 | Below benchmark (40th required) |
| XAVIER UNIVERSITY                                                                     | Private       |           594 |                  55 |          40.24 | Below benchmark (40th required) |
| WESLEYAN UNIVERSITY-PHILIPPINES CABANATUAN CITY                                       | Private       |            25 |                  33 |             40 | Below benchmark (40th required) |
| University For Development Studies                                                    | Not Specified |             5 |                  21 |             40 | Below benchmark (40th required) |
| MOUNTAIN VIEW COLLEGE BUKIDNON                                                        | Private       |            45 |                  42 |             40 | Below benchmark (40th required) |
| NEW YORK UNIVERSITY NY USA                                                            | Foreign       |             5 |                  88 |             40 | Below benchmark (40th required) |
| COLLEGE OF THE IMMACULATE CONCEPTION                                                  | Private       |             5 |                  43 |             40 | Below benchmark (40th required) |
| ST. PAUL COLLEGE ILOILO                                                               | Private       |            15 |                  50 |             40 | Below benchmark (40th required) |
| FIRST ASIA INSTITUTE OF TECHNOLOGY AND HUMANITIES                                     | Private       |             5 |                  66 |             40 | Below benchmark (40th required) |
| JOSE RIZAL UNIVERSITY                                                                 | Private       |             5 |                  46 |             40 | Below benchmark (40th required) |
| SIENA COLLEGE-TAYTAY                                                                  | Private       |             5 |                  31 |             40 | Below benchmark (40th required) |
| DOMINICAN COLLEGE                                                                     | Private       |            10 |                  36 |             40 | Below benchmark (40th required) |
| DE LOS SANTOS - STI COLLEGE                                                           | Private       |            15 |                  33 |             40 | Below benchmark (40th required) |
| HOLY CROSS OF DAVAO COLLEGE                                                           | Private       |             5 |                  54 |             40 | Below benchmark (40th required) |
| Sti - College Davao                                                                   | Not Specified |             5 |                  15 |             40 | Below benchmark (40th required) |
| UNIV. OF ASIA AND THE PACIFIC - PASIG CITY                                            | Private       |             5 |                  81 |             40 | Below benchmark (40th required) |
| RUTGERS COLLEGE NEW JERSEY                                                            | Foreign       |             5 |                  90 |             40 | Below benchmark (40th required) |
| GORDON COLLEGE                                                                        | Public        |             5 |                  46 |             40 | Below benchmark (40th required) |
| GOOD SAMARITAN COLLEGES                                                               | Private       |             5 |                  41 |             40 | Below benchmark (40th required) |
| REMEDIOS T. ROMUALDEZ MEM. SCH. - MMC                                                 | Private       |            75 |                  54 |             40 | Below benchmark (40th required) |
| PHILIPPINE NORMAL COLLEGE TAFT AVENUE MANILA                                          | Public        |            10 |                  53 |             40 | Below benchmark (40th required) |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                   | Public        |            25 |                45.5 |             40 | Below benchmark (40th required) |
| UNIVERSITY OF HAWAII AT MANOA                                                         | Foreign       |             5 |                  81 |             40 | Below benchmark (40th required) |
| OLIVAREZ COLLEGE - TAGAYTAY                                                           | Private       |             5 |                  46 |             40 | Below benchmark (40th required) |
| TEMPLE UNIVERSITY USA                                                                 | Foreign       |             5 |                  69 |             40 | Below benchmark (40th required) |
| THE COLLEGE OF MAASIN                                                                 | Private       |             5 |                  89 |             40 | Below benchmark (40th required) |
| MANILA DOCTORS COLLEGE - PASAY CITY                                                   | Private       |            83 |                  43 |          39.76 | Below benchmark (40th required) |
| ADAMSON UNIVERSITY                                                                    | Private       |            68 |                  43 |          39.71 | Below benchmark (40th required) |
| OUR LADY OF FATIMA UNIVERSITY (FATIMA MEDICAL SCIENCE FOUNDATION) - VALENZUELA        | Private       |           466 |                  44 |           39.7 | Below benchmark (40th required) |
| CAPITOL UNIVERSITY                                                                    | Private       |            63 |                  36 |          39.68 | Below benchmark (40th required) |
| DE LA SALLE - LIPA BATANGAS                                                           | Private       |            53 |                  45 |          39.62 | Below benchmark (40th required) |
| CENTRO ESCOLAR UNIVERSITY AT MALOLOS                                                  | Private       |            28 |                  56 |          39.29 | Below benchmark (40th required) |
| SAN BEDA COLLEGE MENDIOLA MANILA                                                      | Private       |           166 |                33.5 |          39.16 | Below benchmark (40th required) |
| CENTRO ESCOLAR UNIVERSITY - MANILA                                                    | Private       |           764 |                  46 |          39.14 | Below benchmark (40th required) |
| THE PHILIPPINE WOMEN'S UNIVERSITY SYSTEM - MANILA                                     | Private       |            23 |                65.5 |          39.13 | Below benchmark (40th required) |
| UNIVERSITY OF SOUTHERN MINDANAO NORTH COTABATO                                        | Public        |            23 |                  44 |          39.13 | Below benchmark (40th required) |
| WORLD CITI COLLEGES QUEZON CITY                                                       | Private       |            41 |                  42 |          39.02 | Below benchmark (40th required) |
| RIVERSIDE COLLEGE                                                                     | Private       |            77 |                44.5 |          38.96 | Below benchmark (40th required) |
| PHILIPPINE REHABILITATION INSTITUTE FOUNDATION                                        | Private       |            18 |                  53 |          38.89 | Below benchmark (40th required) |
| DAVAO MEDICAL SCHOOL FOUNDATION INC.                                                  | Private       |            36 |                  42 |          38.89 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA - SAN DIEGO                                                  | Foreign       |            18 |                81.5 |          38.89 | Below benchmark (40th required) |
| ST. SCHOLASTICA'S COLLEGE                                                             | Private       |            80 |                  44 |          38.75 | Below benchmark (40th required) |
| MINDANAO SANITARIUM AND HOSPITAL COLLEGE                                              | Private       |           145 |                  43 |          38.62 | Below benchmark (40th required) |
| 13100A                                                                                | Not Specified |            13 |                  52 |          38.46 | Below benchmark (40th required) |
| LA SALLE UNIVERSITY                                                                   | Private       |            13 |                  32 |          38.46 | Below benchmark (40th required) |
| TARLAC STATE UNIVERSITY                                                               | Public        |            13 |                  56 |          38.46 | Below benchmark (40th required) |
| OLIVAREZ COLLEGE                                                                      | Private       |            13 |                  40 |          38.46 | Below benchmark (40th required) |
| UNIVERSITY OF THE EAST - MANILA                                                       | Private       |           141 |                  59 |           38.3 | Below benchmark (40th required) |
| ST. PAUL UNIVERSITY - TUGUEGARAO CAGAYAN                                              | Private       |            34 |                20.5 |          38.24 | Below benchmark (40th required) |
| CENTRO ESCOLAR UNIVERSITY - MAKATI                                                    | Private       |            58 |                  71 |          37.93 | Below benchmark (40th required) |
| DOÑA REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION                                   | Private       |           140 |                46.5 |          37.86 | Below benchmark (40th required) |
| HOLY NAME UNIVERSITY                                                                  | Private       |            77 |                  55 |          37.66 | Below benchmark (40th required) |
| BUTUAN DOCTORS COLLEGE                                                                | Private       |            24 |                  57 |           37.5 | Below benchmark (40th required) |
| UNIVERSITY OF NORTHERN PHILIPPINES VIGAN ILOCOS SUR                                   | Public        |             8 |                  11 |           37.5 | Below benchmark (40th required) |
| NORTHERN CHRISTIAN COLLEGE                                                            | Private       |             8 |                  50 |           37.5 | Below benchmark (40th required) |
| ASSUMPTION COLLEGE                                                                    | Private       |            16 |                55.5 |           37.5 | Below benchmark (40th required) |
| BROKENSHIRE COLLEGE SOCSKSARGEN                                                       | Private       |             8 |                58.5 |           37.5 | Below benchmark (40th required) |
| BULACAN STATE UNIVERSITY                                                              | Public        |            16 |                46.5 |           37.5 | Below benchmark (40th required) |
| HUACHIEW CHALERMPRAKIET UNIVERSITY                                                    | Foreign       |             8 |                27.5 |           37.5 | Below benchmark (40th required) |
| NOTRE DAME OF KIDAPAWAN COLLEGE                                                       | Private       |             8 |                  27 |           37.5 | Below benchmark (40th required) |
| DELOS SANTOS COLLEGE                                                                  | Private       |             8 |                38.5 |           37.5 | Below benchmark (40th required) |
| UNIVERSITY OF LUZON                                                                   | Private       |            16 |                  20 |           37.5 | Below benchmark (40th required) |
| DE LA SALLE - LIPA                                                                    | Private       |           179 |                  44 |          37.43 | Below benchmark (40th required) |
| DAVAO MEDICAL SCHOOL FOUNDATION                                                       | Private       |           543 |                  54 |          37.38 | Below benchmark (40th required) |
| UNIVERSITY OF THE CORDILLERAS                                                         | Private       |           196 |                  46 |          37.24 | Below benchmark (40th required) |
| NOTRE DAME OF DADIANGAS COLLEGE GEN. SANTOS                                           | Private       |            43 |                  34 |          37.21 | Below benchmark (40th required) |
| UNIVERSITY OF MAKATI                                                                  | Public        |            27 |                  43 |          37.04 | Below benchmark (40th required) |
| UNIVERSIDAD DE ZAMBOANGA                                                              | Private       |            71 |                  27 |          36.62 | Below benchmark (40th required) |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                         | Public        |           222 |                48.5 |          36.49 | Below benchmark (40th required) |
| UNIVERSITY OF THE IMMACULATE CONCEPTION                                               | Private       |            96 |                44.5 |          36.46 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP - RIZAL                                                  | Private       |            11 |                  29 |          36.36 | Below benchmark (40th required) |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                                | Public        |           124 |                  49 |          36.29 | Below benchmark (40th required) |
| NOTRE DAME OF DADIANGAS UNIVERSITY                                                    | Private       |            97 |                  51 |          36.08 | Below benchmark (40th required) |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                            | Public        |            50 |                  59 |             36 | Below benchmark (40th required) |
| SOUTHWESTERN UNIVERSITY CEBU                                                          | Private       |           189 |                  22 |          35.98 | Below benchmark (40th required) |
| LICEO DE CAGAYAN UNIVERSITY                                                           | Private       |           181 |                36.5 |          35.91 | Below benchmark (40th required) |
| NOTRE DAME UNIVERSITY COTABATO CITY                                                   | Private       |            56 |                25.5 |          35.71 | Below benchmark (40th required) |
| Remedios Trinidad Romualdez Medical Foundation                                        | Not Specified |            31 |                  34 |          35.48 | Below benchmark (40th required) |
| TRINITY COLLEGE                                                                       | Foreign       |            40 |                  20 |             35 | Below benchmark (40th required) |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES INC.                                            | Private       |            20 |                  13 |             35 | Below benchmark (40th required) |
| GENERAL SANTOS DOCTORS' MEDICAL SCHOOL FOUNDATION                                     | Private       |            23 |                42.5 |          34.78 | Below benchmark (40th required) |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES                                              | Private       |            92 |                48.5 |          34.78 | Below benchmark (40th required) |
| OUR LADY OF FATIMA UNIVERSITY VALENZUELA CITY                                         | Private       |           245 |                  26 |          34.69 | Below benchmark (40th required) |
| SOUTHWESTERN UNIVERSITY                                                               | Private       |           477 |                  44 |          34.59 | Below benchmark (40th required) |
| GLOBAL CITY INNOVATIVE COLLEGE                                                        | Private       |            81 |                  41 |          34.57 | Below benchmark (40th required) |
| ST. PAUL UNIVERSITY - QUEZON CITY                                                     | Private       |           102 |                  32 |          34.31 | Below benchmark (40th required) |
| UNIVERSITY OF BAGUIO BAGUIO CITY                                                      | Private       |           105 |                  22 |          34.29 | Below benchmark (40th required) |
| LA CONSOLACION COLLEGE - MANILA                                                       | Private       |            47 |                  43 |          34.04 | Below benchmark (40th required) |
| FEU - EAST ASIA COLLEGE                                                               | Private       |            97 |                  42 |          34.02 | Below benchmark (40th required) |
| NOTRE DAME UNIVERSITY                                                                 | Private       |           106 |                37.5 |          33.96 | Below benchmark (40th required) |
| ILOILO DOCTORS COLLEGE                                                                | Private       |           148 |                30.5 |          33.78 | Below benchmark (40th required) |
| COLEGIO SAN AGUSTIN - BACOLOD                                                         | Private       |            75 |                  47 |          33.33 | Below benchmark (40th required) |
| SOUTHWESTERN UNIVERSITY-MATIAS H. AZNAR MEMORIAL COLLEGE OF MEDICINE - CEBU CITY CEBU | Private       |            90 |                  26 |          33.33 | Below benchmark (40th required) |
| UNIVERSITY OF THE PHILIPPINES - PAMPANGA                                              | Public        |            12 |                61.5 |          33.33 | Below benchmark (40th required) |
| NATIONAL UNIVERSITY - CEDCE                                                           | Private       |            12 |                  48 |          33.33 | Below benchmark (40th required) |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                             | Public        |           159 |                  44 |          33.33 | Below benchmark (40th required) |
| CHRIST THE KING COLLEGE - CALBAYOG CITY                                               | Private       |             6 |                32.5 |          33.33 | Below benchmark (40th required) |
| CENTRO ESCOLAR UNIVERSITY-MALOLOS BULACAN                                             | Private       |             9 |                  36 |          33.33 | Below benchmark (40th required) |
| UNCIANO COLLEGES AND GENERAL HOSPITAL                                                 | Private       |             6 |                  41 |          33.33 | Below benchmark (40th required) |
| KESTER GRANT COLLEGE PHILS. INC.                                                      | Private       |             6 |                  12 |          33.33 | Below benchmark (40th required) |
| ST. PAUL UNIVERSITY - MANILA (ST. PAUL UNIVERITY SYSTEM)                              | Private       |           111 |                50.5 |          33.33 | Below benchmark (40th required) |
| SURIGAO EDUCATION CENTER                                                              | Private       |            18 |                  24 |          33.33 | Below benchmark (40th required) |
| UNCIANO COLLEGES                                                                      | Private       |             9 |                  43 |          33.33 | Below benchmark (40th required) |
| UNIVERSIDAD DE MANILA                                                                 | Public        |             9 |                  54 |          33.33 | Below benchmark (40th required) |
| ILIGAN MEDICAL CENTER COLLEGE                                                         | Private       |            51 |                  43 |          33.33 | Below benchmark (40th required) |
| LYCEUM OF THE PHILIPPINES UNIVERSITY                                                  | Private       |            18 |                55.5 |          33.33 | Below benchmark (40th required) |
| LYCEUM OF THE PHILIPPINES - LAGUNA                                                    | Private       |             6 |                67.5 |          33.33 | Below benchmark (40th required) |
| NUEVA ECIJA UNIVERSITY OF SCIENCE AND TECHNOLOGY - MAIN                               | Public        |             6 |                52.5 |          33.33 | Below benchmark (40th required) |
| UNIVERSITY OF LA SALETTE                                                              | Private       |            48 |                39.5 |          33.33 | Below benchmark (40th required) |
| MAE FAH LUANG UNIVERSITY                                                              | Foreign       |             9 |                  64 |          33.33 | Below benchmark (40th required) |
| MEDINA COLLEGE - PAGADIAN                                                             | Private       |             9 |                  44 |          33.33 | Below benchmark (40th required) |
| SAINT MARY'S COLLEGE OF SAN JUAN                                                      | Private       |             6 |                  11 |          33.33 | Below benchmark (40th required) |
| UNIVERSITY OF SAN FRANCISCO                                                           | Foreign       |             9 |                  75 |          33.33 | Below benchmark (40th required) |
| MAPUA INSTITUTE OF TECHNOLOGY                                                         | Private       |            24 |                  49 |          33.33 | Below benchmark (40th required) |
| UNIVERSITY OF SAN JOSE RECOLETOS CEBU                                                 | Private       |            18 |                  31 |          33.33 | Below benchmark (40th required) |
| SOUTHERN LUZON POLYTECHNIC COLLEGE - LUCBAN QUEZON                                    | Private       |             6 |                  28 |          33.33 | Below benchmark (40th required) |
| ST. JOSEPH COLLEGE CAVITE CITY                                                        | Private       |            12 |                45.5 |          33.33 | Below benchmark (40th required) |
| ST. ANTHONY COLLEGE OF ROXAS CITY CAPIZ                                               | Private       |             6 |                  19 |          33.33 | Below benchmark (40th required) |
| LEYTE NORMAL UNIVERSITY TACLOBAN CITY                                                 | Public        |             6 |                  16 |          33.33 | Below benchmark (40th required) |
| MANILA ADVENTIST MEDICAL CENTER - PASAY CITY                                          | Private       |            15 |                  40 |          33.33 | Below benchmark (40th required) |
| EMILIO AGUINALDO COLLEGE MANILA                                                       | Private       |           115 |                  26 |          33.04 | Below benchmark (40th required) |
| NOTRE DAME OF MARBEL UNIVERSITY                                                       | Private       |            52 |                  48 |          32.69 | Below benchmark (40th required) |
| DAVAO DOCTORS COLLEGE                                                                 | Private       |           246 |                  32 |          32.52 | Below benchmark (40th required) |
| VIRGEN MILAGROSA UNIVERSITY FOUNDATION AND VMU INSTITUTE OF MEDICAL FOUNDATION        | Private       |           199 |                  49 |          32.16 | Below benchmark (40th required) |
| MANILA DOCTORS COLLEGE U.N. AVENUE MANILA                                             | Private       |            56 |                  42 |          32.14 | Below benchmark (40th required) |
| ST. JUDE COLLEGE                                                                      | Private       |            28 |                  33 |          32.14 | Below benchmark (40th required) |
| PERPETUAL HELP COLLEGE OF MANILA                                                      | Private       |           140 |                  30 |          32.14 | Below benchmark (40th required) |
| MIRIAM COLLEGE FOUNDATION INC.                                                        | Private       |            53 |                  38 |          32.08 | Below benchmark (40th required) |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                             | Public        |            75 |                  59 |             32 | Below benchmark (40th required) |
| PHILIPPINE CHRISTIAN UNIVERSITY                                                       | Private       |            25 |                  41 |             32 | Below benchmark (40th required) |
| CAPITOL MEDICAL CENTER COLLEGES                                                       | Private       |            97 |                  41 |          31.96 | Below benchmark (40th required) |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES CAGAYAN                                      | Private       |            19 |                  44 |          31.58 | Below benchmark (40th required) |
| RANGSIT UNIVERSITY                                                                    | Foreign       |            38 |                23.5 |          31.58 | Below benchmark (40th required) |
| UNIVERSITY OF CAGAYAN VALLEY                                                          | Private       |            32 |                  52 |          31.25 | Below benchmark (40th required) |
| ST. ANTHONY COLLEGE OF ROXAS CITY                                                     | Private       |            16 |                40.5 |          31.25 | Below benchmark (40th required) |
| DIPOLOG MEDICAL CENTER COLLEGE FOUNDATION                                             | Private       |            13 |                  43 |          30.77 | Below benchmark (40th required) |
| LYCEUM NORTHWESTERN UNIVERSITY                                                        | Private       |           117 |                  48 |          30.77 | Below benchmark (40th required) |
| EMILIO AGUINALDO COLLEGE                                                              | Private       |           212 |                48.5 |          30.66 | Below benchmark (40th required) |
| UNIVERSITY OF ST. LOUIS - TUGUEGARAO                                                  | Private       |            46 |                  50 |          30.43 | Below benchmark (40th required) |
| PHILIPPINE WOMEN'S UNIVERSITY TAFT AVENUE MANILA                                      | Private       |            46 |                47.5 |          30.43 | Below benchmark (40th required) |
| FILAMER CHRISTIAN UNIVERSITY                                                          | Private       |            23 |                  43 |          30.43 | Below benchmark (40th required) |
| ARELLANO UNIVERSITY                                                                   | Private       |            33 |                  25 |           30.3 | Below benchmark (40th required) |
| UNIVERSITY OF BATANGAS                                                                | Private       |            10 |                  41 |             30 | Below benchmark (40th required) |
| CAPITOL MEDICAL CENTER COLLEGE Q.C.                                                   | Private       |            30 |                26.5 |             30 | Below benchmark (40th required) |
| ST. MICHAEL'S COLLEGE                                                                 | Private       |            10 |                  51 |             30 | Below benchmark (40th required) |
| ST. DOMINIC COLLEGE OF ARTS AND SCIENCES OF CAVITE                                    | Private       |            10 |                45.5 |             30 | Below benchmark (40th required) |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES-DAVAO CITY                                     | Public        |            30 |                  25 |             30 | Below benchmark (40th required) |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES                                                 | Private       |            20 |                37.5 |             30 | Below benchmark (40th required) |
| NEW ERA UNIVERSITY QUEZON CITY                                                        | Private       |            37 |                  22 |          29.73 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP RIZAL - MOLINO                                           | Private       |            17 |                  31 |          29.41 | Below benchmark (40th required) |
| COLLEGE OF THE HOLY SPIRIT OF MANILA                                                  | Private       |            34 |                33.5 |          29.41 | Below benchmark (40th required) |
| PALAWAN STATE UNIVERSITY                                                              | Public        |            45 |                  43 |          28.89 | Below benchmark (40th required) |
| NUEVA ECIJA COLLEGES                                                                  | Private       |            14 |                  33 |          28.57 | Below benchmark (40th required) |
| BATANGAS STATE UNIVERSITY - MAIN                                                      | Public        |            14 |                  37 |          28.57 | Below benchmark (40th required) |
| ST. JOSEPH COLLEGE CAVITE                                                             | Private       |             7 |                  14 |          28.57 | Below benchmark (40th required) |
| STONY BROOK UNIVERSITY                                                                | Foreign       |             7 |                  59 |          28.57 | Below benchmark (40th required) |
| WESTERN VISAYAS COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                              | Public        |             7 |                  76 |          28.57 | Below benchmark (40th required) |
| WEST NEGROS COLLEGE BACOLOD                                                           | Private       |             7 |                  19 |          28.57 | Below benchmark (40th required) |
| UNIVERSITY OF SAINT ANTHONY                                                           | Private       |             7 |                  35 |          28.57 | Below benchmark (40th required) |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                    | Public        |            14 |                32.5 |          28.57 | Below benchmark (40th required) |
| NORTH VALLEY COLLEGE FOUNDATION                                                       | Private       |             7 |                  44 |          28.57 | Below benchmark (40th required) |
| MIRIAM COLLEGE                                                                        | Private       |           111 |                  49 |          27.93 | Below benchmark (40th required) |
| CENTRAL MINDANAO UNIVERSITY BUKIDNON                                                  | Public        |            43 |                  30 |          27.91 | Below benchmark (40th required) |
| MAPUA INSTITUTE OF TECHNOLOGY - MANILA                                                | Private       |            18 |                  40 |          27.78 | Below benchmark (40th required) |
| NOT SPECIFIED/UNLISTED                                                                | Public        |           503 |                  36 |          27.63 | Below benchmark (40th required) |
| UNIVERSITY OF THE VISAYAS                                                             | Private       |            58 |                  25 |          27.59 | Below benchmark (40th required) |
| ILIGAN MEDICAL CENTER ILIGAN CITY                                                     | Private       |            33 |                  19 |          27.27 | Below benchmark (40th required) |
| CENTRAL MINDANAO UNIVERSITY                                                           | Public        |            88 |                  43 |          27.27 | Below benchmark (40th required) |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                           | Public        |            11 |                  53 |          27.27 | Below benchmark (40th required) |
| RUTGERS UNIVERSITY NEW JERSEY                                                         | Foreign       |            11 |                  72 |          27.27 | Below benchmark (40th required) |
| MEDINA COLLEGE OZAMIS MISAMIS ORIENTAL                                                | Private       |            11 |                  15 |          27.27 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-LAS PIÑAS                                   | Private       |            67 |                  15 |          26.87 | Below benchmark (40th required) |
| PINES CITY COLLEGES                                                                   | Private       |            71 |                36.5 |          26.76 | Below benchmark (40th required) |
| UNIVERSITY OF EASTERN PHILIPPINES                                                     | Public        |            45 |                  38 |          26.67 | Below benchmark (40th required) |
| UPH-DR. JOSE G. TAMAYO MEDICAL UNIV.                                                  | Private       |            23 |                  20 |          26.09 | Below benchmark (40th required) |
| MINDANAO SANITARIUM & HOSPITAL COLLEGE ILIGAN CITY                                    | Private       |            50 |                  17 |             26 | Below benchmark (40th required) |
| BAGUIO CENTRAL UNIVERSITY                                                             | Private       |            39 |                36.5 |          25.64 | Below benchmark (40th required) |
| COLEGIO DE SAN JUAN DE LETRAN CALAMBA                                                 | Private       |            16 |                  19 |             25 | Below benchmark (40th required) |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                  | Public        |             8 |                41.5 |             25 | Below benchmark (40th required) |
| ARELLANO UNIVERSITY - PASAY                                                           | Private       |             8 |                  31 |             25 | Below benchmark (40th required) |
| CENTRAL COLLEGES OF THE PHILIPPINES                                                   | Private       |            12 |                  51 |             25 | Below benchmark (40th required) |
| LA CONSOLACION COLLEGE                                                                | Private       |            40 |                14.5 |             25 | Below benchmark (40th required) |
| LYCEUM OF APARRI                                                                      | Private       |             8 |                  30 |             25 | Below benchmark (40th required) |
| SAINT TONIS COLLEGE                                                                   | Private       |             8 |                  44 |             25 | Below benchmark (40th required) |
| NOTRE DAME OF TACURONG COLLEGE                                                        | Private       |             8 |                32.5 |             25 | Below benchmark (40th required) |
| OUR LADY OF FATIMA UNIVERSITY - ANTIPOLO                                              | Private       |            48 |                  44 |             25 | Below benchmark (40th required) |
| THAMMASAT UNIVERSITY                                                                  | Foreign       |            12 |                  32 |             25 | Below benchmark (40th required) |
| UNIVERSITY OF THE ASSUMPTION PAMPANGA                                                 | Private       |             8 |                  36 |             25 | Below benchmark (40th required) |
| DIVINE WORD COLLEGE OF LEGAZPI                                                        | Private       |             8 |                  11 |             25 | Below benchmark (40th required) |
| HOLY TRINITY UNIVERSITY                                                               | Private       |            20 |                  37 |             25 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA LOS ANGELES                                                  | Foreign       |            25 |                81.5 |             24 | Below benchmark (40th required) |
| SAINT MARY'S COLLEGE OF TAGUM                                                         | Private       |            17 |                  57 |          23.53 | Below benchmark (40th required) |
| CALIFORNIA STATE UNIVERSITY                                                           | Foreign       |            26 |                57.5 |          23.08 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA - IRVINE                                                     | Foreign       |            35 |                  78 |          22.86 | Below benchmark (40th required) |
| MISAMIS UNIVERSITY                                                                    | Private       |            22 |                18.5 |          22.73 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA SANTA BARBARA                                                | Foreign       |             9 |                  47 |          22.22 | Below benchmark (40th required) |
| SAINT GABRIEL COLLEGE                                                                 | Private       |             9 |                  22 |          22.22 | Below benchmark (40th required) |
| UNIVERSITAS ADVENT INDONESIA                                                          | Foreign       |             9 |                  45 |          22.22 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA - DAVIS                                                      | Foreign       |            32 |                  80 |          21.88 | Below benchmark (40th required) |
| OTHERS (PLEASE SPECIFY)                                                               | Not Specified |            23 |                  75 |          21.74 | Below benchmark (40th required) |
| MANILA THEOLOGICAL COLLEGE                                                            | Private       |            14 |                  37 |          21.43 | Below benchmark (40th required) |
| MAPUA INSTITUTE OF TECHNOLOGY - MAKATI                                                | Private       |            14 |                  19 |          21.43 | Below benchmark (40th required) |
| UNIVERSITY OF THE ASSUMPTION                                                          | Private       |            19 |                  47 |          21.05 | Below benchmark (40th required) |
| PINES CITY COLLEGES - BAGUIO CITY                                                     | Private       |            34 |                18.5 |          20.59 | Below benchmark (40th required) |
| ANGELES UNIVERSITY FOUNDATION ANGELES CITY                                            | Private       |           471 |                  33 |          20.17 | Below benchmark (40th required) |
| UNIVERSITY OF BRITISH COLUMBIA CANADA                                                 | Foreign       |             5 |                  96 |             20 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA RIVERSIDE CA USA                                             | Foreign       |            25 |                  84 |             20 | Below benchmark (40th required) |
| ST. JOSEPH'S COLLEGE QUEZON CITY                                                      | Private       |            10 |                  26 |             20 | Below benchmark (40th required) |
| MARIANO MARCOS STATE UNIVERSITY - COLLEGE OF EDUCATION - LAOAG CITY                   | Public        |            10 |                38.5 |             20 | Below benchmark (40th required) |
| CONCORDIA COLLEGE                                                                     | Private       |             5 |                  46 |             20 | Below benchmark (40th required) |
| LIPA CITY COLLEGES BATANGAS                                                           | Private       |             5 |                  26 |             20 | Below benchmark (40th required) |
| KALAYAAN COLLEGE                                                                      | Private       |             5 |                  24 |             20 | Below benchmark (40th required) |
| ENDERUN COLLEGE                                                                       | Private       |             5 |                  29 |             20 | Below benchmark (40th required) |
| DAVAO CENTRAL COLLEGE                                                                 | Private       |             5 |                  43 |             20 | Below benchmark (40th required) |
| CAVITE STATE UNIVERSITY CAVITE                                                        | Public        |             5 |                  52 |             20 | Below benchmark (40th required) |
| UNIVERSITY OF THE IMMACULATE CONCEPTION COLLEGE DAVAO                                 | Private       |             5 |                   5 |             20 | Below benchmark (40th required) |
| 13206A                                                                                | Not Specified |             5 |                  54 |             20 | Below benchmark (40th required) |
| NOTRE DAME OF JOLO COLLEGE                                                            | Private       |            27 |                  38 |          18.52 | Below benchmark (40th required) |
| OLIVAREZ COLLEGE SUCAT PARA$AQUE                                                      | Private       |            11 |                  27 |          18.18 | Below benchmark (40th required) |
| BRENT HOSPITAL AND COLLEGES INC. ZAMBOANGA CITY                                       | Private       |            11 |                  10 |          18.18 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - GMA                                             | Private       |            11 |                  14 |          18.18 | Below benchmark (40th required) |
| NOTRE DAME OF JOLO COLLEGE - JOLO SULU                                                | Private       |            11 |                  11 |          18.18 | Below benchmark (40th required) |
| BRENT HOSPITAL AND COLLEGES                                                           | Private       |            28 |                  27 |          17.86 | Below benchmark (40th required) |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                         | Public        |            35 |                  32 |          17.14 | Below benchmark (40th required) |
| UNIVERSITY OF WASHINGTON                                                              | Foreign       |            12 |                  87 |          16.67 | Below benchmark (40th required) |
| Qiqihar Medical University                                                            | Not Specified |             6 |                  14 |          16.67 | Below benchmark (40th required) |
| ST. MARY'S UNIVERSITY NUEVA VIZCAYA                                                   | Private       |             6 |                24.5 |          16.67 | Below benchmark (40th required) |
| WORLD CITI COLLEGES                                                                   | Private       |            24 |                  29 |          16.67 | Below benchmark (40th required) |
| BATAAN PENINSULA STATE UNIVERSITY                                                     | Public        |             6 |                  18 |          16.67 | Below benchmark (40th required) |
| LA SALLE COLLEGE - ANTIPOLO                                                           | Private       |             6 |                  18 |          16.67 | Below benchmark (40th required) |
| MAHIDOL UNIVERSITY                                                                    | Foreign       |            24 |                  27 |          16.67 | Below benchmark (40th required) |
| MEDINA COLLEGE                                                                        | Private       |            24 |                  29 |          16.67 | Below benchmark (40th required) |
| SOUTHEAST ASIAN COLLEGE INC.-ESPANA MANILA                                            | Private       |            12 |                   8 |          16.67 | Below benchmark (40th required) |
| SAN DIEGO STATE UNIVERSITY - CALIFORNIA U.S.A.                                        | Foreign       |             6 |                  52 |          16.67 | Below benchmark (40th required) |
| UNIVERSITY OF MARYLAND - MARYLAND U.S.A.                                              | Foreign       |             6 |                55.5 |          16.67 | Below benchmark (40th required) |
| UNIVERSITY OF FLORIDA                                                                 | Foreign       |            12 |                  76 |          16.67 | Below benchmark (40th required) |
| CALIFORNIA STATE UNIVERSITY FRESNO                                                    | Foreign       |             6 |                  23 |          16.67 | Below benchmark (40th required) |
| RUNGSIT UNIVERSITY                                                                    | Foreign       |             6 |                44.5 |          16.67 | Below benchmark (40th required) |
| KESTER GRANT COLLEGE - PHILIPPINES                                                    | Private       |            21 |                  44 |          14.29 | Below benchmark (40th required) |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                                 | Public        |            63 |                  14 |          14.29 | Below benchmark (40th required) |
| UNIVERSITY OF MINDANAO                                                                | Private       |             7 |                  36 |          14.29 | Below benchmark (40th required) |
| UNIVERSITY OF IMMACULATE CONCEPTION-DAVAO CITY                                        | Private       |             7 |                  21 |          14.29 | Below benchmark (40th required) |
| SOUTHEAST ASIAN COLLEGE INC.-QUEZON CITY                                              | Private       |            14 |                  20 |          14.29 | Below benchmark (40th required) |
| SAN SEBASTIAN COLLEGE                                                                 | Private       |             7 |                  22 |          14.29 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA-RIVERSIDE                                                    | Foreign       |             7 |                  80 |          14.29 | Below benchmark (40th required) |
| UNIVERSITY OF PERPETUAL HELP SYSTEM                                                   | Private       |             7 |                  10 |          14.29 | Below benchmark (40th required) |
| BURAPHA UNIVERSITY                                                                    | Foreign       |             7 |                   9 |          14.29 | Below benchmark (40th required) |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                                 | Public        |             7 |                  33 |          14.29 | Below benchmark (40th required) |
| VIRGEN MILAGROSA UNIV. FOUNDATION - SAN CARLOS CITY PANG.                             | Private       |            76 |                  27 |          13.16 | Below benchmark (40th required) |
| UNIVERSITY OF VISAYAS CEBU                                                            | Private       |            69 |                  10 |          11.59 | Below benchmark (40th required) |
| DOMINICAN COLLEGE BLUM SAN JUAN MM                                                    | Private       |             9 |                  25 |          11.11 | Below benchmark (40th required) |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                     | Public        |             9 |                  77 |          11.11 | Below benchmark (40th required) |
| NORTHERN LUZON ADVENTIST COLLEGE                                                      | Private       |             9 |                  51 |          11.11 | Below benchmark (40th required) |
| UNIVERSITY OF CENTRAL FLORIDA                                                         | Foreign       |             9 |                  46 |          11.11 | Below benchmark (40th required) |
| MINDANAO MEDICAL FOUNDATION COLLEGE DAVAO                                             | Private       |             9 |                  15 |          11.11 | Below benchmark (40th required) |
| UNIVERSITY OF NEVADA LAS VEGAS                                                        | Foreign       |             9 |                  77 |          11.11 | Below benchmark (40th required) |
| DR. CARLOS LANTING COLLEGE - NOVALICHES QUEZON CITY                                   | Private       |            10 |                19.5 |             10 | Below benchmark (40th required) |
| SRINAKHARINWIROT UNIVERSITY                                                           | Foreign       |            10 |                  35 |             10 | Below benchmark (40th required) |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                                            | Public        |            53 |                  11 |           9.43 | Below benchmark (40th required) |
| VIRGEN MILAGROSA EDUCATIONAL INSTITUTE SAN CARLOS CITY                                | Private       |            11 |                  38 |           9.09 | Below benchmark (40th required) |
| AMA COMPUTER COLLEGE                                                                  | Private       |            12 |                  19 |           8.33 | Below benchmark (40th required) |
| CHULALONGKORN UNIVERSITY                                                              | Foreign       |            13 |                  38 |           7.69 | Below benchmark (40th required) |
| PALAWAN STATE UNIVERSITY PUERTO PRINCESA CITY                                         | Public        |            15 |                  15 |           6.67 | Below benchmark (40th required) |
| RANGSIT UNIVERSITY THAILAND                                                           | Foreign       |            38 |                  11 |           5.26 | Below benchmark (40th required) |
| CHIANG MAI UNIVERSITY                                                                 | Foreign       |            19 |                  30 |           5.26 | Below benchmark (40th required) |
| MAHIDOL UNIVERSITY THAILAND                                                           | Foreign       |            28 |                35.5 |           3.57 | Below benchmark (40th required) |
| THAMMASAT UNIV.                                                                       | Foreign       |             8 |                  23 |              0 | Below benchmark (40th required) |
| SULU STATE COLLEGE                                                                    | Public        |            10 |                  22 |              0 | Below benchmark (40th required) |
| UNIVERSITY OF BRITISH COLUMBIA                                                        | Foreign       |             5 |                  24 |              0 | Below benchmark (40th required) |
| CALIFORNIA STATE UNIVERSITY - FULLERTON                                               | Foreign       |             6 |                75.5 |              0 | Below benchmark (40th required) |
| UNIVERSITY OF MICHIGAN                                                                | Foreign       |             5 |                  77 |              0 | Below benchmark (40th required) |
| UNIVERSITY OF ILLINOIS CHICAGO                                                        | Foreign       |             8 |                83.5 |              0 | Below benchmark (40th required) |
| RAMKHAMHAENG UNIV.                                                                    | Foreign       |             5 |                   2 |              0 | Below benchmark (40th required) |
| ST. LUKE'S SCHOOL OF MEDICINE INDIA                                                   | Private       |            10 |                35.5 |              0 | Below benchmark (40th required) |
| ST. ANDREW'S INTERNATIONAL ACADEMY INDIA                                              | Foreign       |             5 |                   9 |              0 | Below benchmark (40th required) |
| UNIVERSITY OF CALIFORNIA AT STA. CRUZ U.S.A.                                          | Foreign       |             9 |                  61 |              0 | Below benchmark (40th required) |
| MALASIQUI AGNO VALLEY COLLEGE - MALASIQUI PANGASINAN                                  | Private       |             7 |                   9 |              0 | Below benchmark (40th required) |
| LAGUNA COLLEGE                                                                        | Private       |             7 |                  39 |              0 | Below benchmark (40th required) |
| UNIVERSITY OF SOUTH FLORIDA USA                                                       | Foreign       |             6 |                  53 |              0 | Below benchmark (40th required) |
| KHON KAEN UNIVERSITY THAILAND                                                         | Foreign       |             5 |                  20 |              0 | Below benchmark (40th required) |
| DIVINE WORD COLLEGE OF LAOAG                                                          | Private       |           107 |                  18 |              0 | Below benchmark (40th required) |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                  | Public        |             5 |                  51 |              0 | Below benchmark (40th required) |
| ILOCOS SUR POLYTECHNIC STATE COLLEGE                                                  | Public        |             5 |                  53 |              0 | Below benchmark (40th required) |
| CHULALONGKORN UNIVERSITY THAILAND                                                     | Foreign       |            17 |                  34 |              0 | Below benchmark (40th required) |
| ADVENTIST INDONESIA UNIVERSITY INDONESIA                                              | Foreign       |             5 |                  17 |              0 | Below benchmark (40th required) |

---
## Section C: Cut-off Scenarios — 30th Percentile (B4+) vs 40th Percentile (B5+)

Comparison of examinee counts and PLE outcomes under the 30th percentile (B4+) vs 40th percentile (B5+) cut-off thresholds, broken down by university type.

**Table C1. Cut-off scenario comparison by university type**

| University Type   | Cut-off               |   Admitted (best records) |   PLE passers (observable) |   PLE pass rate (%) |   Median percentile |
|:------------------|:----------------------|--------------------------:|---------------------------:|--------------------:|--------------------:|
| All               | 30th percentile (B4+) |                     91409 |                      26311 |               56.45 |                  66 |
| All               | 40th percentile (B5+) |                     78944 |                      24999 |               61.17 |                  71 |
| Public            | 30th percentile (B4+) |                     19709 |                       6294 |               59.52 |                  71 |
| Public            | 40th percentile (B5+) |                     17482 |                       6135 |               63.38 |                  76 |
| Private           | 30th percentile (B4+) |                     69504 |                      19500 |               56.22 |                  64 |
| Private           | 40th percentile (B5+) |                     59546 |                      18361 |               61.23 |                  70 |
| Foreign           | 30th percentile (B4+) |                      1285 |                        222 |               28.14 |                  69 |
| Foreign           | 40th percentile (B5+) |                      1109 |                        214 |               30.18 |                  74 |

---
## Section D: Foreign Student Enrollment at SUCs — 10-Slot Cap Analysis

The CHED amendment caps foreign student enrollment at 10 per incoming freshmen class at SUCs. This section shows foreign student counts per SUC per year based on CITIZENSHIP_FINAL from Pipeline 4.

**Summary metrics:**

| Metric | Value |
|--------|------:|
| SUC-Year combos exceeding 10-slot cap | 99 |
| Total foreign students at SUCs | 4,514 |

**Table D1. Top 20 SUCs by max foreign enrollment in a single year**

| UNIVERSITY                                                 |   max_foreign |   total_foreign |   years_over_cap |
|:-----------------------------------------------------------|--------------:|----------------:|-----------------:|
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                  |           281 |             770 |                6 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)              |           150 |             433 |                6 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                    |           120 |             371 |                7 |
| UNIVERSITY OF THE PHILIPPINES - MANILA                     |            82 |             359 |                7 |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                  |            78 |             225 |                5 |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY |            59 |             196 |                5 |
| NOT SPECIFIED/UNLISTED                                     |            57 |             158 |                4 |
| WEST VISAYAS STATE UNIVERSITY - MAIN                       |            52 |             197 |                5 |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                 |            47 |              47 |                1 |
| WESTERN MINDANAO STATE UNIVERSITY                          |            44 |             147 |                5 |
| BICOL UNIVERSITY - MAIN                                    |            44 |             118 |                4 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                    |            40 |             138 |                5 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                     |            40 |             119 |                4 |
| PAMANTASAN NG LUNGSOD NG MAYNILA                           |            38 |             135 |                5 |
| MINDANAO STATE UNIVERSITY - MARAWI                         |            33 |             135 |                5 |
| CAGAYAN STATE UNIVERSITY - ANDREWS                         |            25 |              57 |                2 |
| CENTRAL MINDANAO UNIVERSITY                                |            22 |              73 |                3 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                  |            21 |              62 |                2 |
| PALAWAN STATE UNIVERSITY                                   |            20 |              64 |                3 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                      |            17 |              32 |                2 |

**Table D2. Full foreign enrollment detail by SUC and year**
*(Sorted by year ascending, foreign count descending within year)*

| UNIVERSITY                                                                          |   Year |   foreign_count | over_cap   |
|:------------------------------------------------------------------------------------|-------:|----------------:|:-----------|
| NOT SPECIFIED/UNLISTED                                                              |   2006 |              10 | False      |
| NOT SPECIFIED/UNLISTED                                                              |   2007 |              21 | True       |
| VISAYAS UNIVERSITY                                                                  |   2007 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2007 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS ILOILO                                      |   2007 |               1 | False      |
| WESTERN MINDANAO STATE UNIVERSITY ZAMBOANGA CITY                                    |   2007 |               1 | False      |
| NOT SPECIFIED/UNLISTED                                                              |   2008 |              20 | True       |
| PANGASINAN STATE UNIVERSITY                                                         |   2008 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2008 |               1 | False      |
| NOT SPECIFIED/UNLISTED                                                              |   2009 |              57 | True       |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                                          |   2009 |              47 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                               |   2009 |              15 | True       |
| UNIVERSITY OF NORTHERN PHILIPPINES VIGAN ILOCOS SUR                                 |   2009 |               2 | False      |
| BULACAN STATE UNIVERSITY                                                            |   2009 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2009 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS CEBU                                   |   2009 |               1 | False      |
| NOT SPECIFIED/UNLISTED                                                              |   2010 |              50 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                               |   2010 |              17 | True       |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2010 |              13 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2010 |               6 | False      |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2010 |               3 | False      |
| NORTH LUZON PHILIPPINES STATE COLLEGE                                               |   2010 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2010 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2010 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - TACLOBAN                                            |   2010 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2010 |               1 | False      |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2011 |              11 | True       |
| CEBU NORMAL UNIVERSITY                                                              |   2011 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2011 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2012 |              14 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2012 |              11 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2012 |               7 | False      |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2012 |               6 | False      |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2012 |               5 | False      |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2012 |               4 | False      |
| BICOL UNIVERSITY - MAIN                                                             |   2012 |               3 | False      |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2012 |               3 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2012 |               3 | False      |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2012 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2012 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2012 |               3 | False      |
| CAVITE STATE UNIVERSITY - MAIN                                                      |   2012 |               2 | False      |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2012 |               2 | False      |
| PALAWAN STATE UNIVERSITY                                                            |   2012 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2012 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2012 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2012 |               2 | False      |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2012 |               2 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2012 |               1 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2012 |               1 | False      |
| CEBU STATE COLLEGE OF SCIENCE AND TECHNOLOGY-MANDAUE CITY - MANDAUE CITY CEBU       |   2012 |               1 | False      |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                |   2012 |               1 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2012 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG PASIG                                                      |   2012 |               1 | False      |
| SULU STATE COLLEGE                                                                  |   2012 |               1 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2012 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2012 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2013 |              23 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2013 |              17 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2013 |              10 | False      |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2013 |              10 | False      |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2013 |               8 | False      |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2013 |               8 | False      |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2013 |               8 | False      |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2013 |               7 | False      |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2013 |               7 | False      |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2013 |               6 | False      |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2013 |               4 | False      |
| PALAWAN STATE UNIVERSITY                                                            |   2013 |               3 | False      |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2013 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2013 |               3 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2013 |               2 | False      |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2013 |               2 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2013 |               2 | False      |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2013 |               2 | False      |
| SULU STATE COLLEGE                                                                  |   2013 |               2 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2013 |               1 | False      |
| BICOL UNIVERSITY - MAIN                                                             |   2013 |               1 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2013 |               1 | False      |
| MARINDUQUE STATE COLLEGE - MAIN                                                     |   2013 |               1 | False      |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2013 |               1 | False      |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  |   2013 |               1 | False      |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                 |   2013 |               1 | False      |
| PHILIPPINE STATE COLLEGE OF AERONAUTICS - MAIN                                      |   2013 |               1 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2013 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2013 |               1 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2013 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2013 |               1 | False      |
| VISAYAS STATE UNIVERSITY - MAIN                                                     |   2013 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2014 |              43 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2014 |              37 | True       |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2014 |              23 | True       |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2014 |              18 | True       |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2014 |              17 | True       |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2014 |              17 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2014 |              15 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2014 |              15 | True       |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2014 |              14 | True       |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2014 |              14 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2014 |              13 | True       |
| BICOL UNIVERSITY - MAIN                                                             |   2014 |              12 | True       |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2014 |               7 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2014 |               6 | False      |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2014 |               5 | False      |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2014 |               5 | False      |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2014 |               4 | False      |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2014 |               3 | False      |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2014 |               3 | False      |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2014 |               3 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2014 |               3 | False      |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  |   2014 |               2 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2014 |               2 | False      |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                |   2014 |               2 | False      |
| PHILIPPINE NORMAL UNIVERSITY - AGUSAN                                               |   2014 |               2 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2014 |               2 | False      |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                         |   2014 |               1 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2014 |               1 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2014 |               1 | False      |
| BICOL UNIVERSITY - DARAGA                                                           |   2014 |               1 | False      |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            |   2014 |               1 | False      |
| CATANDUANES STATE COLLEGE - MAIN                                                    |   2014 |               1 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2014 |               1 | False      |
| IFUGAO STATE UNIVERSITY - MAIN                                                      |   2014 |               1 | False      |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  |   2014 |               1 | False      |
| NAVAL STATE UNIVERSITY - MAIN                                                       |   2014 |               1 | False      |
| PAMPANGA AGRICULTURAL COLLEGE                                                       |   2014 |               1 | False      |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2014 |               1 | False      |
| SULU STATE COLLEGE                                                                  |   2014 |               1 | False      |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              |   2014 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2015 |             178 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2015 |              67 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2015 |              56 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2015 |              54 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2015 |              41 | True       |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2015 |              32 | True       |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2015 |              28 | True       |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2015 |              25 | True       |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2015 |              23 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2015 |              20 | True       |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2015 |              18 | True       |
| PALAWAN STATE UNIVERSITY                                                            |   2015 |              17 | True       |
| BICOL UNIVERSITY - MAIN                                                             |   2015 |              15 | True       |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2015 |              13 | True       |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2015 |              12 | True       |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2015 |              12 | True       |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  |   2015 |              10 | False      |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2015 |               9 | False      |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2015 |               9 | False      |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2015 |               7 | False      |
| CATANDUANES STATE COLLEGE - MAIN                                                    |   2015 |               5 | False      |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                              |   2015 |               5 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2015 |               4 | False      |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2015 |               4 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2015 |               4 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2015 |               3 | False      |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              |   2015 |               3 | False      |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                         |   2015 |               2 | False      |
| BICOL UNIVERSITY - TABACO                                                           |   2015 |               2 | False      |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            |   2015 |               2 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2015 |               2 | False      |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  |   2015 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2015 |               2 | False      |
| AKLAN STATE UNIVERSITY - MAIN                                                       |   2015 |               1 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2015 |               1 | False      |
| BICOL UNIVERSITY - POLANGUI                                                         |   2015 |               1 | False      |
| BUKIDNON STATE UNIVERSITY                                                           |   2015 |               1 | False      |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG) - TUGUEGARAO CITY (CAPITAL) CAGAYAN   |   2015 |               1 | False      |
| CAMARINES NORTE STATE COLLEGE - MAIN                                                |   2015 |               1 | False      |
| CAVITE STATE UNIVERSITY - MAIN                                                      |   2015 |               1 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2015 |               1 | False      |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                |   2015 |               1 | False      |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                              |   2015 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                   |   2015 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG MUNTINLUPA                                                 |   2015 |               1 | False      |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                               |   2015 |               1 | False      |
| UNIVERSITY OF MAKATI                                                                |   2015 |               1 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2015 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2016 |             191 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2016 |             121 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2016 |              60 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2016 |              54 | True       |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2016 |              42 | True       |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2016 |              40 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2016 |              30 | True       |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2016 |              29 | True       |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2016 |              25 | True       |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2016 |              22 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2016 |              21 | True       |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2016 |              21 | True       |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2016 |              14 | True       |
| BICOL UNIVERSITY - MAIN                                                             |   2016 |              10 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2016 |              10 | False      |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2016 |              10 | False      |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2016 |               8 | False      |
| PALAWAN STATE UNIVERSITY                                                            |   2016 |               7 | False      |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  |   2016 |               6 | False      |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2016 |               5 | False      |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2016 |               5 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2016 |               4 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2016 |               4 | False      |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                              |   2016 |               4 | False      |
| SULU STATE COLLEGE                                                                  |   2016 |               3 | False      |
| UNIVERSITY OF MAKATI                                                                |   2016 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                  |   2016 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2016 |               3 | False      |
| BICOL UNIVERSITY - DARAGA                                                           |   2016 |               2 | False      |
| CAVITE STATE UNIVERSITY - MAIN                                                      |   2016 |               2 | False      |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2016 |               2 | False      |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                 |   2016 |               2 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2016 |               2 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2016 |               2 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2016 |               2 | False      |
| AKLAN STATE UNIVERSITY - MAIN                                                       |   2016 |               1 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2016 |               1 | False      |
| BICOL UNIVERSITY - TABACO                                                           |   2016 |               1 | False      |
| BUKIDNON STATE UNIVERSITY                                                           |   2016 |               1 | False      |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            |   2016 |               1 | False      |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                |   2016 |               1 | False      |
| GORDON COLLEGE                                                                      |   2016 |               1 | False      |
| ISABELA STATE UNIVERSITY - MAIN                                                     |   2016 |               1 | False      |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - SAN PABLO CITY                                |   2016 |               1 | False      |
| LEYTE NORMAL UNIVERSITY                                                             |   2016 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                   |   2016 |               1 | False      |
| UM DIGOS COLLEGE                                                                    |   2016 |               1 | False      |
| UNIVERSIDAD DE MANILA                                                               |   2016 |               1 | False      |
| UNIVERSITY OF CALOOCAN CITY                                                         |   2016 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES-CANDON - CITY OF CANDON ILOCOS SUR               |   2016 |               1 | False      |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              |   2016 |               1 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA             |   2016 |               1 | False      |
| VISAYAS STATE UNIVERSITY - MAIN                                                     |   2016 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2017 |             281 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2017 |             150 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2017 |             120 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2017 |              79 | True       |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2017 |              78 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2017 |              59 | True       |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2017 |              52 | True       |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2017 |              44 | True       |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2017 |              40 | True       |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2017 |              40 | True       |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2017 |              38 | True       |
| BICOL UNIVERSITY - MAIN                                                             |   2017 |              33 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2017 |              33 | True       |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2017 |              21 | True       |
| PALAWAN STATE UNIVERSITY                                                            |   2017 |              20 | True       |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2017 |              19 | True       |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2017 |              16 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                  |   2017 |              15 | True       |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  |   2017 |              14 | True       |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2017 |              14 | True       |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2017 |              13 | True       |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2017 |              13 | True       |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2017 |              12 | True       |
| LEYTE NORMAL UNIVERSITY                                                             |   2017 |              11 | True       |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2017 |              10 | False      |
| CAVITE STATE UNIVERSITY - MAIN                                                      |   2017 |               8 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2017 |               8 | False      |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              |   2017 |               8 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2017 |               6 | False      |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2017 |               6 | False      |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                              |   2017 |               6 | False      |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            |   2017 |               5 | False      |
| SULTAN KUDARAT STATE UNIVERSITY - TACURONG                                          |   2017 |               5 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2017 |               5 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2017 |               4 | False      |
| BICOL UNIVERSITY - TABACO                                                           |   2017 |               3 | False      |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                              |   2017 |               3 | False      |
| JOSE RIZAL MEMORIAL STATE UNIVERSITY - MAIN                                         |   2017 |               3 | False      |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                 |   2017 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA             |   2017 |               3 | False      |
| CARAGA STATE UNIVERSITY - MAIN                                                      |   2017 |               2 | False      |
| GORDON COLLEGE                                                                      |   2017 |               2 | False      |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  |   2017 |               2 | False      |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                             |   2017 |               2 | False      |
| TECHNOLOGICAL UNIVERSITY OF THE PHILIPPINES - AYALA BLVD. MANILA                    |   2017 |               2 | False      |
| UNIVERSIDAD DE MANILA                                                               |   2017 |               2 | False      |
| UNIVERSITY OF MAKATI                                                                |   2017 |               2 | False      |
| VISAYAS STATE UNIVERSITY - MAIN                                                     |   2017 |               2 | False      |
| AKLAN STATE UNIVERSITY - MAIN                                                       |   2017 |               1 | False      |
| BACOLOD CITY COLLEGE                                                                |   2017 |               1 | False      |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                         |   2017 |               1 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2017 |               1 | False      |
| CATANDUANES STATE COLLEGE - MAIN                                                    |   2017 |               1 | False      |
| CAVITE STATE UNIVERSITY - CARMONA                                                   |   2017 |               1 | False      |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                |   2017 |               1 | False      |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                |   2017 |               1 | False      |
| EASTERN SAMAR STATE UNIVERSITY - MAIN                                               |   2017 |               1 | False      |
| MINDANAO STATE UNIVERSITY - BUUG COLLEGE                                            |   2017 |               1 | False      |
| MINDANAO STATE UNIVERSITY - NAAWAN                                                  |   2017 |               1 | False      |
| MISAMIS ORIENTAL STATE COLLEGE OF AGRICULTURE AND TECHNOLOGY                        |   2017 |               1 | False      |
| NUEVA VIZCAYA STATE UNIVERSITY - BAMBANG                                            |   2017 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG PASAY                                                      |   2017 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG PASIG                                                      |   2017 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG VALENZUELA                                                 |   2017 |               1 | False      |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                               |   2017 |               1 | False      |
| SAMAR STATE UNIVERSITY - MAIN                                                       |   2017 |               1 | False      |
| SULTAN KUDARAT STATE UNIVERSITY - MAIN                                              |   2017 |               1 | False      |
| SULU STATE COLLEGE                                                                  |   2017 |               1 | False      |
| UNIVERSITY OF RIZAL SYSTEM - MORONG                                                 |   2017 |               1 | False      |
| WESTERN VISAYAS COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                            |   2017 |               1 | False      |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                           |   2018 |              88 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                              |   2018 |              82 | True       |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                             |   2018 |              72 | True       |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                       |   2018 |              55 | True       |
| BICOL UNIVERSITY - MAIN                                                             |   2018 |              44 | True       |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                |   2018 |              44 | True       |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                           |   2018 |              39 | True       |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                          |   2018 |              37 | True       |
| WESTERN MINDANAO STATE UNIVERSITY                                                   |   2018 |              36 | True       |
| MINDANAO STATE UNIVERSITY - MARAWI                                                  |   2018 |              31 | True       |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                             |   2018 |              28 | True       |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                    |   2018 |              26 | True       |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                  |   2018 |              25 | True       |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                              |   2018 |              23 | True       |
| CENTRAL MINDANAO UNIVERSITY                                                         |   2018 |              22 | True       |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                           |   2018 |              18 | True       |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                              |   2018 |              16 | True       |
| BULACAN STATE UNIVERSITY - MAIN                                                     |   2018 |              15 | True       |
| PALAWAN STATE UNIVERSITY                                                            |   2018 |              15 | True       |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                  |   2018 |              13 | True       |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                            |   2018 |              11 | True       |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                     |   2018 |               9 | False      |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                       |   2018 |               8 | False      |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                          |   2018 |               7 | False      |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                       |   2018 |               7 | False      |
| CENTRAL LUZON STATE UNIVERSITY                                                      |   2018 |               6 | False      |
| CATANDUANES STATE COLLEGE - MAIN                                                    |   2018 |               5 | False      |
| CEBU NORMAL UNIVERSITY                                                              |   2018 |               4 | False      |
| LEYTE NORMAL UNIVERSITY                                                             |   2018 |               4 | False      |
| SAMAR STATE UNIVERSITY - MAIN                                                       |   2018 |               4 | False      |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                              |   2018 |               4 | False      |
| UNIVERSITY OF EASTERN PHILIPPINES                                                   |   2018 |               4 | False      |
| BENGUET STATE UNIVERSITY - MAIN                                                     |   2018 |               3 | False      |
| CAVITE STATE UNIVERSITY - MAIN                                                      |   2018 |               3 | False      |
| MINDANAO UNIVERSITY OF SCIENCE AND TECHNOLOGY                                       |   2018 |               3 | False      |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                             |   2018 |               3 | False      |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                 |   2018 |               3 | False      |
| UNIVERSIDAD DE MANILA                                                               |   2018 |               3 | False      |
| UNIVERSITY OF MAKATI                                                                |   2018 |               3 | False      |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                              |   2018 |               3 | False      |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA             |   2018 |               3 | False      |
| BATANGAS STATE UNIVERSITY - MAIN                                                    |   2018 |               2 | False      |
| BUKIDNON STATE UNIVERSITY                                                           |   2018 |               2 | False      |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                            |   2018 |               2 | False      |
| CARAGA STATE UNIVERSITY - MAIN                                                      |   2018 |               2 | False      |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                              |   2018 |               2 | False      |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                  |   2018 |               2 | False      |
| PANGASINAN STATE UNIVERSITY                                                         |   2018 |               2 | False      |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                               |   2018 |               2 | False      |
| SULTAN KUDARAT STATE UNIVERSITY - TACURONG                                          |   2018 |               2 | False      |
| SULU STATE COLLEGE                                                                  |   2018 |               2 | False      |
| VISAYAS STATE UNIVERSITY - MAIN                                                     |   2018 |               2 | False      |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                         |   2018 |               1 | False      |
| BICOL UNIVERSITY - DARAGA                                                           |   2018 |               1 | False      |
| CENTRAL BICOL STATE UNIVERSITY OF AGRICULTURE - MAIN                                |   2018 |               1 | False      |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                |   2018 |               1 | False      |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - SOUTH LA UNION                       |   2018 |               1 | False      |
| EULOGIO AMANG RODRIGUEZ INSTITUTE OF SCIENCE AND TECHNOLOGY - CAVITE                |   2018 |               1 | False      |
| GORDON COLLEGE                                                                      |   2018 |               1 | False      |
| IFUGAO STATE UNIVERSITY - MAIN                                                      |   2018 |               1 | False      |
| JOSE RIZAL MEMORIAL STATE UNIVERSITY - MAIN                                         |   2018 |               1 | False      |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - LAGUNA COLLEGE OF ARTS AND TRADES - STA. CRUZ |   2018 |               1 | False      |
| MINDANAO STATE UNIVERSITY - BUUG COLLEGE                                            |   2018 |               1 | False      |
| NAVAL STATE UNIVERSITY - MAIN                                                       |   2018 |               1 | False      |
| NORTHERN NEGROS STATE COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                      |   2018 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG MUNTINLUPA                                                 |   2018 |               1 | False      |
| PAMANTASAN NG LUNGSOD NG PASAY                                                      |   2018 |               1 | False      |
| PHILIPPINE NORMAL UNIVERSITY - AGUSAN                                               |   2018 |               1 | False      |
| RAMON MAGSAYSAY TECHNOLOGICAL UNIVERSITY - RAMON MAGSAYSAY POLYTECHNIC COLLEGE      |   2018 |               1 | False      |
| TIWI COMMUNITY COLLEGE                                                              |   2018 |               1 | False      |

---
## Section E: Per-HEI Score Distribution

For every institution (with at least 5 best-record examinees): NMS_PER_num statistics, percentile bin distribution, and cut-off eligibility metrics.

**Total institutions with data: 2,575**

**Table E1. Per-HEI summary statistics**
*(Sorted by total examinees descending; minimum 5 examinees)*

| UNIVERSITY                                                                            | UNI_TYPE      |   Total Examinees |   Median %ile |   Mean %ile |   Q25 %ile |   Q75 %ile |   B4+ % |   B5+ % |   Health Sci % |   PLE pass rate % |
|:--------------------------------------------------------------------------------------|:--------------|------------------:|--------------:|------------:|-----------:|-----------:|--------:|--------:|---------------:|------------------:|
| UNIVERSITY OF SANTO TOMAS                                                             | Private       |             17567 |            58 |        54.7 |         32 |         80 |    77.6 |      69 |           48.7 |              49.8 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA                                             | Private       |              4541 |            45 |          46 |         18 |         72 |    66.7 |    56.6 |           41.5 |              42.8 |
| FAR EASTERN UNIVERSITY                                                                | Private       |              4270 |            45 |        46.5 |         21 |         71 |    67.6 |    57.3 |           53.8 |                43 |
| SAN PEDRO COLLEGE                                                                     | Private       |              3649 |            48 |        47.5 |         20 |         73 |    67.8 |    59.1 |           47.7 |              41.4 |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                                | Public        |              3539 |            81 |        67.6 |         44 |         95 |      83 |    78.2 |             47 |              64.5 |
| SAINT LOUIS UNIVERSITY                                                                | Private       |              3222 |            50 |        49.4 |         24 |         75 |      72 |    61.2 |           53.2 |              44.2 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                               | Public        |              3143 |            78 |        66.2 |         41 |         95 |    82.6 |    76.5 |           32.2 |              58.3 |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                             | Public        |              2469 |            44 |        44.8 |         18 |         70 |    64.9 |      55 |           42.1 |              33.3 |
| CEBU DOCTOR'S UNIVERSITY                                                              | Private       |              2404 |            47 |        47.3 |         21 |         73 |    68.6 |    58.4 |           51.7 |              44.1 |
| DE LA SALLE UNIVERSITY - MANILA                                                       | Private       |              2229 |            63 |        57.3 |         34 |         83 |    78.9 |      72 |           34.7 |              58.7 |
| OUR LADY OF FATIMA UNIVERSITY (FATIMA MEDICAL SCIENCE FOUNDATION) - VALENZUELA        | Private       |              2048 |            43 |        45.5 |         18 |         72 |    65.2 |    55.1 |           46.4 |              39.7 |
| CENTRO ESCOLAR UNIVERSITY - MANILA                                                    | Private       |              2032 |            46 |        47.2 |         20 |         74 |    68.4 |    57.8 |           51.3 |              39.1 |
| SOUTHWESTERN UNIVERSITY                                                               | Private       |              1846 |            46 |        45.9 |         18 |       71.8 |    66.2 |    56.3 |           44.5 |              34.6 |
| ATENEO DE MANILA UNIVERSITY - QUEZON CITY                                             | Private       |              1786 |            62 |        57.6 |         31 |         87 |    77.1 |    68.7 |           47.3 |              51.7 |
| VELEZ COLLEGE                                                                         | Private       |              1742 |            51 |        49.6 |       21.8 |         77 |    69.8 |    60.1 |           52.3 |              45.3 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS                                                   | Private       |              1732 |            49 |        48.3 |         20 |         75 |    69.8 |    60.7 |           43.6 |              42.5 |
| DAVAO MEDICAL SCHOOL FOUNDATION                                                       | Private       |              1671 |            45 |        46.5 |         19 |         73 |    66.7 |    56.1 |           42.7 |              37.4 |
| EMILIO AGUINALDO COLLEGE                                                              | Private       |              1574 |            44 |        45.1 |         18 |         70 |    64.9 |    54.8 |           39.1 |              30.7 |
| AMA COMPUTER COLLEGE - MAKATI                                                         | Private       |              1521 |            41 |        42.9 |         15 |         69 |    61.1 |    52.6 |           36.8 |               nan |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                         | Public        |              1394 |            45 |        45.7 |         16 |         74 |      65 |    55.4 |           43.3 |              36.5 |
| ANGELES UNIVERSITY FOUNDATION                                                         | Private       |              1340 |            47 |          47 |         21 |         72 |    68.7 |    58.6 |           48.2 |              41.4 |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                             | Public        |              1319 |          56.5 |        52.4 |       25.2 |         80 |    72.4 |    64.9 |           43.1 |              47.8 |
| SILLIMAN UNIVERSITY                                                                   | Private       |              1306 |            49 |        48.9 |         23 |         74 |    70.4 |    61.4 |           55.7 |              46.8 |
| AGO MEDICAL AND EDUCATIONAL CENTER - BICOL CHRISTIAN COLLEGE OF MEDICINE              | Private       |              1292 |            38 |        41.3 |         15 |         66 |    60.2 |    49.1 |           37.2 |              46.2 |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                  | Public        |              1246 |            54 |        52.4 |         27 |         80 |    73.2 |    64.3 |           49.3 |              43.8 |
| XAVIER UNIVERSITY                                                                     | Private       |              1234 |            49 |          49 |         23 |         75 |    70.5 |    60.7 |             51 |              40.2 |
| BROKENSHIRE COLLEGE                                                                   | Private       |              1229 |            45 |        45.5 |         17 |       71.5 |    66.4 |    56.7 |           41.6 |              45.5 |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                      | Public        |              1218 |            51 |          50 |         29 |         72 |    75.1 |    65.5 |           35.9 |              41.2 |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                            | Public        |              1192 |            48 |        48.8 |         23 |         76 |    69.2 |      59 |           46.1 |                43 |
| ATENEO DE ZAMBOANGA UNIVERSITY                                                        | Private       |              1162 |          43.5 |        44.7 |         18 |         70 |    63.9 |      54 |           53.3 |              44.6 |
| FEU - DR. NICANOR REYES MEDICAL FOUNDATION                                            | Private       |              1154 |            51 |        48.8 |       23.2 |         74 |    70.8 |    61.8 |           52.9 |              42.3 |
| LYCEUM NORTHWESTERN UNIVERSITY                                                        | Private       |              1051 |            42 |        43.9 |         15 |         70 |    63.3 |    53.6 |           40.7 |              30.8 |
| MINDANAO STATE UNIVERSITY - MARAWI                                                    | Public        |              1008 |            50 |        49.3 |         23 |         76 |    69.8 |      62 |           49.9 |              40.6 |
| UNIVERSITY OF SAN AGUSTIN                                                             | Private       |               991 |            46 |          47 |         19 |         74 |    67.2 |    57.6 |           47.4 |              40.8 |
| ATENEO DE DAVAO UNIVERSITY                                                            | Private       |               971 |            51 |        50.8 |         26 |         76 |    71.6 |    62.5 |           59.6 |              50.1 |
| DE LA SALLE HEALTH SCIENCES INSTITUTE                                                 | Private       |               949 |            48 |        48.3 |         23 |         74 |    69.4 |    57.5 |           53.1 |                41 |
| TRINITY UNIVERSITY OF ASIA                                                            | Private       |               877 |          53.5 |        51.4 |         27 |         76 |    74.1 |    62.8 |           58.4 |              42.8 |
| WESTERN MINDANAO STATE UNIVERSITY                                                     | Public        |               861 |            48 |        47.6 |         19 |         75 |    69.2 |    59.1 |           52.6 |              42.3 |
| MANILA CENTRAL UNIVERSITY                                                             | Private       |               831 |            41 |        43.2 |         17 |         68 |    62.8 |    52.5 |           49.7 |              43.9 |
| BICOL UNIVERSITY - MAIN                                                               | Public        |               740 |            52 |        50.5 |         23 |         78 |      70 |    61.2 |           49.2 |              41.1 |
| ATENEO DE MANILA UNIVERSITY                                                           | Private       |               721 |            89 |        86.2 |         82 |         95 |    99.9 |    99.4 |           14.8 |              69.8 |
| CENTRAL PHILIPPINE UNIVERSITY                                                         | Private       |               702 |            47 |        48.2 |         23 |         73 |      69 |    59.7 |           56.6 |              41.8 |
| VIRGEN MILAGROSA UNIVERSITY FOUNDATION AND VMU INSTITUTE OF MEDICAL FOUNDATION        | Private       |               701 |            45 |        45.1 |         18 |         70 |    67.5 |    57.3 |           43.2 |              32.2 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                                | Public        |               696 |            56 |        53.4 |         25 |         81 |    74.3 |    66.5 |           41.7 |              47.6 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                               | Public        |               674 |            50 |        49.2 |         20 |         76 |    68.3 |    59.7 |           48.1 |              48.4 |
| ADVENTIST UNIVERSITY OF THE PHILIPPINES                                               | Private       |               671 |            50 |        48.9 |         22 |         75 |    68.9 |      61 |           53.2 |                42 |
| SAINT PAUL UNIVERSITY PHILIPPINES                                                     | Private       |               661 |            46 |        46.2 |         18 |         72 |    67.2 |      58 |           47.7 |              45.2 |
| UNIVERSITY OF ST. LA SALLE                                                            | Private       |               631 |            54 |        52.5 |         28 |       77.2 |    74.3 |    64.6 |           58.2 |              46.5 |
| UNIVERSITY OF THE IMMACULATE CONCEPTION                                               | Private       |               602 |            43 |        44.7 |         16 |         71 |      65 |    53.9 |           45.5 |              36.5 |
| UNIVERSITY OF THE EAST RAMON MAGSAYSAY MEMORIAL MEDICAL CENTER                        | Private       |               555 |            54 |        52.2 |         28 |         76 |      75 |    64.9 |           63.4 |              44.1 |
| UNIVERSITY OF SAN CARLOS                                                              | Private       |               553 |            49 |        48.9 |         23 |         76 |    68.6 |    58.4 |           55.5 |              40.5 |
| VELEZ COLLEGE CEBU                                                                    | Private       |               546 |            52 |        51.7 |         33 |         71 |    78.8 |      65 |           69.4 |              64.5 |
| SAN BEDA COLLEGE                                                                      | Private       |               537 |            48 |        47.2 |         21 |         73 |      66 |    57.6 |           55.7 |              40.3 |
| NOT SPECIFIED/UNLISTED                                                                | Public        |               503 |            36 |        40.5 |         13 |         63 |    56.8 |    47.2 |           40.4 |              27.6 |
| SAN PEDRO COLLEGE DAVAO CITY                                                          | Private       |               492 |          36.5 |        38.8 |         18 |         57 |    60.3 |      46 |           68.9 |                47 |
| MANILA TYTANA COLLEGES                                                                | Private       |               485 |            45 |          47 |         22 |       71.2 |    68.7 |    57.7 |           71.8 |              40.5 |
| CENTRO ESCOLAR UNIVERSITY - MAKATI                                                    | Private       |               472 |            48 |        48.3 |         19 |         76 |    69.8 |    58.9 |           39.8 |              37.9 |
| ANGELES UNIVERSITY FOUNDATION ANGELES CITY                                            | Private       |               471 |            33 |        37.8 |         19 |         54 |    57.1 |    40.8 |           46.3 |              20.2 |
| DOÑA REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION                                   | Private       |               467 |            48 |        46.8 |         21 |       71.5 |      68 |    57.9 |           52.5 |              37.9 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS CAVITE                                            | Private       |               452 |            34 |        37.8 |         19 |       53.2 |    57.7 |    42.9 |           15.7 |              44.9 |
| UNIVERSITY OF THE PHILIPPINES - LOS BANOS LAGUNA                                      | Public        |               450 |            81 |        76.6 |       66.5 |         91 |    99.1 |    96.9 |              4 |              67.6 |
| DAVAO DOCTORS COLLEGE                                                                 | Private       |               442 |            35 |        40.1 |         14 |         63 |    57.6 |    46.5 |             55 |              32.5 |
| LICEO DE CAGAYAN UNIVERSITY                                                           | Private       |               431 |            38 |        42.1 |         15 |       66.8 |    61.9 |    48.7 |           56.4 |              35.9 |
| OUR LADY OF FATIMA UNIVERSITY - QUEZON CITY                                           | Private       |               423 |            43 |        46.3 |         19 |       71.8 |    63.3 |    54.5 |           55.8 |              42.1 |
| FAR EASTERN UNIVERSITY - NRMF (FAIRVIEW Q.C.)                                         | Private       |               409 |            34 |        35.9 |         18 |         52 |    57.2 |    40.3 |           60.4 |              58.4 |
| MINDANAO SANITARIUM AND HOSPITAL COLLEGE                                              | Private       |               399 |            44 |        45.7 |         19 |         71 |    66.8 |    57.9 |           51.4 |              38.6 |
| SAINT LOUIS UNIVERSITY - BAGUIO                                                       | Private       |               374 |            43 |        46.9 |         28 |         64 |    73.3 |      58 |           46.8 |              57.2 |
| CENTRO ESCOLAR UNIVERSITY - MENDIOLA MANILA                                           | Private       |               369 |            28 |          32 |         12 |         47 |    47.6 |    34.8 |           54.7 |              44.2 |
| DE LA SALLE - LIPA                                                                    | Private       |               366 |            44 |        46.6 |       22.5 |         73 |    66.8 |    54.8 |           51.9 |              37.4 |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                              | Public        |               356 |            63 |        57.9 |         34 |       84.8 |    80.1 |    71.7 |           36.2 |              49.7 |
| CEBU NORMAL UNIVERSITY                                                                | Public        |               354 |            62 |        57.5 |         37 |         81 |    81.3 |    72.9 |           66.9 |              58.5 |
| UNIVERSITY OF THE EAST - MANILA                                                       | Private       |               350 |            53 |        50.8 |         24 |         77 |    70.7 |      61 |           42.3 |              38.3 |
| UNIVERSITY OF BAGUIO                                                                  | Private       |               345 |            51 |        49.8 |         23 |         77 |    69.6 |    58.5 |           59.4 |                44 |
| WEST VISAYAS STATE UNIVERSITY ILOILO                                                  | Public        |               342 |            59 |        54.7 |       34.2 |         74 |    79.5 |    71.1 |           21.9 |              51.5 |
| XAVIER UNIVERSITY CAGAYAN DE ORO CITY                                                 | Private       |               339 |            52 |        51.1 |         32 |       69.5 |    79.4 |    65.5 |           45.1 |              55.8 |
| CENTRAL MINDANAO UNIVERSITY                                                           | Public        |               328 |            49 |        47.3 |         20 |       73.2 |    68.6 |    58.8 |           44.8 |              27.3 |
| MINDANAO STATE UNIVERSITY MARAWI CITY                                                 | Public        |               328 |          37.5 |        41.5 |         22 |         63 |    62.8 |    47.9 |           18.6 |              42.7 |
| UNIVERSIDAD DE ZAMBOANGA                                                              | Private       |               325 |            45 |        45.6 |         18 |         70 |    65.4 |    56.6 |           43.4 |              36.6 |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                                | Public        |               315 |          50.5 |          49 |         19 |       74.8 |    67.6 |    59.5 |           49.8 |              36.3 |
| UNIVERSITY OF THE CORDILLERAS                                                         | Private       |               312 |            45 |        43.7 |         16 |         70 |    64.3 |    56.1 |           62.2 |              37.2 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                             | Public        |               304 |            51 |        48.8 |         21 |         75 |    70.1 |    59.7 |           43.1 |                32 |
| ILOILO DOCTORS COLLEGE                                                                | Private       |               301 |            39 |        43.6 |         18 |         70 |    61.4 |    50.2 |           56.5 |              33.8 |
| UNIVERSIDAD DE STA. ISABEL                                                            | Private       |               300 |            49 |        49.8 |         24 |         74 |    70.7 |    61.6 |           62.7 |                48 |
| RIVERSIDE COLLEGE                                                                     | Private       |               299 |            46 |        46.8 |       17.5 |         75 |    66.9 |      58 |           48.2 |                39 |
| ST. PAUL UNIVERSITY ILOILO                                                            | Private       |               297 |            53 |        52.3 |         29 |         78 |      76 |    63.8 |             66 |              49.8 |
| MOUNTAIN VIEW COLLEGE                                                                 | Private       |               295 |            46 |        45.5 |         18 |         70 |    66.3 |    56.4 |           49.5 |              43.4 |
| UNIVERSITY OF NEGROS OCCIDENTAL-RECOLETOS                                             | Private       |               278 |            53 |          49 |         21 |         75 |    69.6 |    60.8 |           50.7 |              45.1 |
| NOTRE DAME UNIVERSITY                                                                 | Private       |               277 |          43.5 |        44.2 |         15 |       69.8 |    63.9 |    53.9 |           51.6 |                34 |
| MIRIAM COLLEGE                                                                        | Private       |               256 |            49 |        47.9 |         19 |         74 |    70.2 |    61.3 |           44.5 |              27.9 |
| UNIVERSITY OF THE VISAYAS                                                             | Private       |               254 |            36 |        39.2 |         11 |         62 |    60.7 |    47.5 |           53.5 |              27.6 |
| PALAWAN STATE UNIVERSITY                                                              | Public        |               254 |            48 |        46.6 |         21 |       70.2 |    70.3 |    56.9 |           38.6 |              28.9 |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES                                              | Private       |               253 |            46 |        48.2 |         21 |         74 |    71.5 |    59.3 |           53.4 |              34.8 |
| ATENEO DE NAGA UNIVERSITY                                                             | Private       |               252 |          44.5 |        45.4 |         20 |         70 |    69.1 |    56.8 |           49.2 |              45.3 |
| LYCEUM OF THE PHILIPPINES UNIVERSITY - BATANGAS                                       | Private       |               251 |            48 |        44.9 |         16 |         70 |    61.3 |    55.6 |             55 |                49 |
| SAINT SCHOLASTICA'S COLLEGE TACLOBAN                                                  | Private       |               248 |          45.5 |        46.1 |       19.8 |         70 |    66.5 |    56.9 |             56 |                50 |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                       | Public        |               246 |            55 |        53.3 |         30 |         79 |    76.7 |    68.8 |           39.4 |              52.6 |
| OUR LADY OF FATIMA UNIVERSITY VALENZUELA CITY                                         | Private       |               245 |            26 |          32 |         11 |         48 |    45.7 |    34.7 |           51.4 |              34.7 |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                    | Public        |               242 |            48 |        47.1 |         15 |         77 |    65.2 |    58.4 |             43 |              58.8 |
| LORMA COLLEGES                                                                        | Private       |               233 |            49 |        48.1 |         25 |         70 |    71.3 |      60 |           49.8 |                42 |
| SILLIMAN UNIVERSITY DUMAGUETE CITY                                                    | Private       |               221 |            53 |        54.5 |         34 |         76 |    82.4 |      71 |           60.6 |              62.9 |
| SAINT MARY'S UNIVERSITY                                                               | Private       |               217 |            46 |        46.7 |         19 |         74 |      66 |      59 |           59.9 |              45.3 |
| CAPITOL MEDICAL CENTER COLLEGES                                                       | Private       |               215 |            42 |          46 |       19.5 |       72.5 |    63.6 |    56.1 |             60 |                32 |
| ARELLANO UNIVERSITY - MANILA                                                          | Private       |               203 |            49 |        49.2 |       24.5 |         76 |    70.6 |    60.4 |           53.7 |              42.9 |
| BULACAN STATE UNIVERSITY - MAIN                                                       | Public        |               201 |            51 |        48.9 |         20 |       76.8 |    68.9 |    60.6 |           51.7 |              50.7 |
| ST. LOUIS UNIVERSITY BAGUIO CITY                                                      | Private       |               199 |            51 |        50.6 |         33 |         69 |    79.9 |    68.8 |           42.7 |              56.8 |
| COLEGIO SAN AGUSTIN - BACOLOD                                                         | Private       |               199 |            46 |        47.4 |         23 |       70.5 |    66.7 |    55.6 |           54.3 |              33.3 |
| NOTRE DAME OF DADIANGAS UNIVERSITY                                                    | Private       |               199 |            46 |        46.6 |       18.5 |         73 |    68.6 |    56.2 |           51.3 |              36.1 |
| MINDANAO STATE UNIVERSITY ILIGAN CITY                                                 | Public        |               197 |            53 |        53.5 |         37 |         73 |    80.7 |    72.6 |           16.2 |              54.3 |
| PERPETUAL HELP COLLEGE OF MANILA                                                      | Private       |               197 |            38 |        41.1 |         15 |       64.5 |    56.9 |    48.2 |             69 |              32.1 |
| UNIVERSITY OF PERPETUAL HELP - DR. JOSE G. TAMAYO MEDICAL UNIVERSITY                  | Private       |               196 |            51 |        49.9 |         25 |       73.5 |    69.2 |    61.5 |           53.1 |              47.9 |
| MAKATI MEDICAL CENTER COLLEGE OF NURSING                                              | Private       |               193 |            47 |        46.4 |       21.8 |         69 |    67.9 |      60 |           64.8 |              42.3 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO CITY                                           | Public        |               190 |            69 |        66.8 |       54.2 |         82 |    97.4 |    89.5 |            1.6 |              60.5 |
| SOUTHWESTERN UNIVERSITY CEBU                                                          | Private       |               189 |            22 |        28.2 |          9 |         42 |    40.7 |    29.1 |           67.2 |                36 |
| NOTRE DAME OF MARBEL UNIVERSITY                                                       | Private       |               187 |          46.5 |        47.5 |         20 |       73.8 |    65.4 |    54.6 |             46 |              32.7 |
| ADAMSON UNIVERSITY                                                                    | Private       |               180 |            45 |        45.7 |         18 |       69.8 |    65.5 |    56.3 |           41.7 |              39.7 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS ILOILO                                        | Public        |               179 |            75 |        71.5 |         58 |         89 |    95.5 |    92.7 |           28.5 |              68.7 |
| OUR LADY OF FATIMA UNIVERSITY - ANTIPOLO                                              | Private       |               175 |            43 |        44.6 |       20.2 |         67 |    66.9 |    56.4 |           49.1 |                25 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                         | Public        |               172 |            54 |        53.9 |         30 |         80 |    77.6 |    68.5 |           40.7 |              42.6 |
| NEW ERA UNIVERSITY                                                                    | Private       |               172 |          45.5 |        47.1 |         20 |         73 |    67.9 |    54.2 |           42.4 |              48.2 |
| SAN BEDA COLLEGE MENDIOLA MANILA                                                      | Private       |               166 |          33.5 |        36.4 |         17 |       49.2 |    60.2 |    36.1 |           45.2 |              39.2 |
| HOLY NAME UNIVERSITY                                                                  | Private       |               160 |            48 |        50.6 |         23 |         83 |    67.1 |    60.8 |           51.2 |              37.7 |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                            | Public        |               158 |            49 |        50.2 |         22 |         79 |    70.8 |      61 |           44.9 |                36 |
| ST. SCHOLASTICA'S COLLEGE                                                             | Private       |               158 |          36.5 |        41.5 |         15 |         66 |    58.6 |    47.1 |           32.9 |              38.8 |
| ST. PAUL UNIVERSITY - MANILA (ST. PAUL UNIVERITY SYSTEM)                              | Private       |               157 |            51 |        51.2 |       27.5 |       76.2 |    73.7 |    63.5 |           63.1 |              33.3 |
| UNIVERSITY OF SAN CARLOS CEBU CITY                                                    | Private       |               157 |            40 |        45.3 |         25 |         69 |    65.6 |    53.5 |           49.7 |              54.8 |
| PINES CITY COLLEGES                                                                   | Private       |               153 |            42 |          45 |         23 |         67 |    67.1 |      53 |           60.8 |              26.8 |
| UNIVERSITY OF LA SALETTE                                                              | Private       |               152 |            50 |          52 |       26.5 |         81 |    72.3 |    62.2 |             52 |              33.3 |
| SOUTHVILLE INTERNATIONAL SCHOOL AND COLLEGES                                          | Private       |               150 |            49 |        48.6 |         28 |         68 |    71.1 |    60.4 |           68.7 |              41.8 |
| UNIVERSITY OF ST. LOUIS - TUGUEGARAO                                                  | Private       |               149 |            54 |        50.6 |         20 |       80.5 |    67.6 |    62.8 |           53.7 |              30.4 |
| CEBU DOCTORS COLLEGE CEBU CITY                                                        | Private       |               148 |            28 |        34.7 |       16.8 |         49 |    49.3 |    37.2 |           79.7 |              49.3 |
| WESTERN MINDANAO STATE UNIVERSITY ZAMBOANGA CITY                                      | Public        |               144 |          27.5 |        30.6 |       12.8 |         47 |    47.9 |    33.3 |           43.8 |                41 |
| AQUINAS UNIVERSITY OF LEGAZPI                                                         | Private       |               144 |            43 |        45.3 |         26 |         64 |    72.7 |    57.6 |           61.1 |              51.4 |
| BENGUET STATE UNIVERSITY - MAIN                                                       | Public        |               143 |            53 |        52.6 |         31 |         77 |    76.6 |    65.2 |           53.1 |              42.7 |
| MINDANAO MEDICAL FOUNDATION COLLEGE                                                   | Private       |               142 |          52.5 |        49.6 |         24 |         73 |    69.8 |    62.6 |           42.3 |              42.3 |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                    | Public        |               140 |          42.5 |        45.9 |         16 |         73 |      64 |      54 |           41.4 |                50 |
| CENTRAL LUZON STATE UNIVERSITY                                                        | Public        |               139 |            46 |        47.2 |       17.2 |       76.8 |    63.2 |    55.1 |           42.4 |              51.1 |
| UNIVERSITY OF CEBU - BANILAD                                                          | Private       |               139 |            46 |        45.1 |         19 |         69 |    59.9 |      54 |           65.5 |              43.7 |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                                | Public        |               137 |            48 |        49.5 |       19.5 |       76.5 |    66.7 |    55.6 |           48.9 |              40.4 |
| MISAMIS UNIVERSITY - OZAMIS CITY                                                      | Private       |               129 |            44 |        45.2 |       17.5 |         70 |    62.7 |    54.8 |           49.6 |              41.8 |
| DE LA SALLE - HEALTH SCIENCES CAMPUS                                                  | Private       |               129 |            38 |        41.9 |         25 |         57 |    66.7 |    48.1 |           79.1 |              41.9 |
| REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION TACLOBAN                               | Private       |               127 |            38 |        39.6 |       20.5 |         58 |    60.6 |      48 |           81.1 |              50.4 |
| ST. PAUL UNIVERSITY - QUEZON CITY                                                     | Private       |               127 |          34.5 |        40.9 |       17.2 |       64.5 |    58.4 |    46.4 |           58.3 |              34.3 |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING AND LIBERAL ARTS                          | Private       |               125 |            49 |        51.1 |       24.2 |       78.2 |    72.7 |    66.1 |           64.8 |              43.6 |
| UNIVERSITY OF THE EAST (C.M. RECTO MANILA)                                            | Private       |               123 |            55 |          51 |       31.5 |         70 |      78 |      65 |           13.8 |              50.4 |
| COLEGIO DE SAN JUAN DE LETRAN                                                         | Private       |               122 |            47 |        49.8 |         24 |       79.8 |    67.8 |    59.1 |           48.4 |              43.9 |
| GENERAL SANTOS DOCTORS' MEDICAL SCHOOL FOUNDATION                                     | Private       |               122 |            49 |        47.7 |         21 |         75 |    66.4 |    57.1 |           43.4 |              34.8 |
| UNIVERSITY OF SAN AGUSTIN - ILOILO CITY                                               | Private       |               122 |            40 |          43 |         19 |         64 |    63.6 |    50.4 |           52.5 |              49.2 |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                                | Public        |               120 |            47 |        47.1 |       24.5 |       71.5 |    72.2 |    56.5 |           47.5 |              44.3 |
| UNIVERSITY OF PANGASINAN                                                              | Private       |               119 |            42 |        43.1 |       19.8 |       63.5 |    65.2 |    55.7 |           69.7 |              48.6 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                         | Public        |               118 |            51 |        46.9 |         21 |         70 |    70.2 |    61.4 |           37.3 |              17.1 |
| DIVINE WORD COLLEGE OF LAOAG                                                          | Private       |               116 |            19 |        27.7 |        6.8 |         45 |    40.7 |    31.9 |            3.4 |                 0 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION                                               | Private       |               116 |          42.5 |        43.7 |       14.8 |       66.2 |    67.5 |    54.4 |           53.4 |              43.8 |
| EMILIO AGUINALDO COLLEGE MANILA                                                       | Private       |               115 |            26 |        31.6 |       14.5 |       47.5 |    45.2 |      33 |           48.7 |                33 |
| UNIVERSITY OF EASTERN PHILIPPINES                                                     | Public        |               109 |            41 |          42 |         15 |         67 |      59 |    52.4 |           49.5 |              26.7 |
| CENTRAL LUZON DOCTORS' HOSPITAL EDUCATIONAL INSTITUTION                               | Private       |               108 |            51 |        49.8 |         25 |         72 |    74.3 |    66.7 |           57.4 |              51.7 |
| WESLEYAN UNIVERSITY - PHILIPPINES (CABANATUAN)                                        | Private       |               108 |            36 |        45.1 |       20.5 |         70 |    63.6 |    48.6 |           66.7 |              41.3 |
| UNIVERSITY OF BAGUIO BAGUIO CITY                                                      | Private       |               105 |            22 |        29.7 |          9 |         46 |    41.9 |    30.5 |           49.5 |              34.3 |
| ST. PAUL UNIVERSITY - MANILA                                                          | Private       |               104 |          42.5 |        44.6 |       25.8 |       63.2 |    71.2 |    53.8 |           52.9 |              42.3 |
| Mariano Marcos State University - College Of Fisheries - Currimao                     | Not Specified |               104 |          46.5 |        47.9 |       30.8 |         64 |    76.9 |    62.5 |           13.5 |              60.6 |
| CAPITOL UNIVERSITY                                                                    | Private       |               103 |            42 |        46.3 |       20.2 |         73 |    65.3 |    52.5 |           56.3 |              39.7 |
| HOLY ANGEL UNIVERSITY                                                                 | Private       |               103 |            41 |          44 |       19.5 |         67 |    65.3 |    54.5 |           58.3 |                46 |
| CENTRAL PHILIPPINE UNIVERSITY ILOILO                                                  | Private       |               100 |            46 |          45 |       24.8 |       65.8 |      67 |      60 |             55 |                42 |
| FEU - EAST ASIA COLLEGE                                                               | Private       |                99 |            42 |        44.6 |       17.5 |       67.5 |    62.6 |    52.5 |           77.8 |                34 |
| GLOBAL CITY INNOVATIVE COLLEGE                                                        | Private       |                98 |            41 |        42.9 |         23 |       62.5 |    69.1 |    53.6 |           70.4 |              34.6 |
| UNIVERSITY OF ST. LA SALLE BACOLOD CITY                                               | Private       |                96 |          46.5 |        47.2 |       26.8 |         65 |    71.9 |    57.3 |           44.8 |              52.1 |
| ST. JUDE COLLEGE                                                                      | Private       |                96 |            44 |        44.9 |         17 |       73.8 |      62 |    54.3 |           57.3 |              32.1 |
| FATHER SATURNINO M. URIOS UNIVERSITY                                                  | Private       |                92 |            49 |          48 |         22 |       72.5 |    74.2 |      64 |           58.7 |                50 |
| SOUTHWESTERN UNIVERSITY-MATIAS H. AZNAR MEMORIAL COLLEGE OF MEDICINE - CEBU CITY CEBU | Private       |                90 |            26 |          35 |          7 |         62 |    46.4 |    41.7 |             70 |              33.3 |
| UNIVERSITY OF SOUTHERN PHILIPPINES FOUNDATION                                         | Private       |                89 |            41 |        44.6 |         16 |         71 |    58.4 |    50.6 |           48.3 |              43.8 |
| ILIGAN MEDICAL CENTER COLLEGE                                                         | Private       |                87 |            40 |        40.8 |       12.2 |       63.8 |    63.4 |    57.3 |             54 |              33.3 |
| CENTRO ESCOLAR UNIVERSITY AT MALOLOS                                                  | Private       |                86 |          57.5 |        54.3 |         28 |       80.8 |    74.4 |    69.8 |           45.3 |              39.3 |
| COLLEGE OF THE HOLY SPIRIT OF MANILA                                                  | Private       |                84 |          38.5 |          43 |       18.8 |       69.2 |    65.1 |    49.4 |           52.4 |              29.4 |
| MANILA DOCTORS COLLEGE - PASAY CITY                                                   | Private       |                83 |            43 |        41.8 |         26 |         56 |    68.7 |    54.2 |           89.2 |              39.8 |
| UERM MEMORIAL MEDICAL CENTER                                                          | Private       |                82 |            49 |        46.9 |         31 |       58.8 |    80.5 |      61 |           63.4 |              43.9 |
| HOLY INFANT COLLEGE                                                                   | Private       |                81 |            51 |        47.3 |         21 |         74 |      65 |      60 |           53.1 |              51.9 |
| SOUTHEAST ASIAN COLLEGE                                                               | Private       |                80 |            40 |        40.4 |       12.5 |         67 |    60.5 |    52.6 |           72.5 |              40.4 |
| EASTER COLLEGE                                                                        | Private       |                80 |          39.5 |        43.4 |         24 |       65.5 |    69.2 |    51.3 |           66.2 |              40.6 |
| DR. CARLOS S. LANTING COLLEGE                                                         | Private       |                76 |            37 |          44 |       19.5 |       71.5 |    65.8 |    47.9 |           57.9 |                45 |
| WORLD CITI COLLEGES QUEZON CITY                                                       | Private       |                76 |            46 |        50.7 |         27 |         82 |    69.9 |    58.9 |           56.6 |                39 |
| VIRGEN MILAGROSA UNIV. FOUNDATION - SAN CARLOS CITY PANG.                             | Private       |                76 |            27 |        29.8 |         11 |         41 |    43.2 |    28.4 |           38.2 |              13.2 |
| THE PHILIPPINE WOMEN'S UNIVERSITY SYSTEM - MANILA                                     | Private       |                75 |            57 |        53.6 |       32.2 |         74 |    79.5 |    65.8 |             56 |              39.1 |
| REMEDIOS T. ROMUALDEZ MEM. SCH. - MMC                                                 | Private       |                75 |            54 |        49.3 |       26.5 |       68.5 |      72 |      64 |           78.7 |                40 |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE                                                  | Private       |                75 |            55 |        52.8 |         24 |         83 |    70.8 |    68.1 |           42.7 |                60 |
| METROPOLITAN HOSPITAL COLLEGE OF NURSING                                              | Private       |                75 |            47 |        47.5 |       21.5 |       68.5 |    67.6 |    55.4 |             60 |              44.6 |
| BRENT HOSPITAL AND COLLEGES                                                           | Private       |                73 |            39 |        44.6 |       13.5 |         73 |    58.3 |    48.6 |           52.1 |              17.9 |
| CAVITE STATE UNIVERSITY - MAIN                                                        | Public        |                73 |            53 |        51.6 |         26 |         81 |    72.6 |    60.3 |           46.6 |              52.6 |
| MANILA ADVENTIST MEDICAL CENTER AND COLLEGES                                          | Private       |                72 |            48 |        45.1 |       20.5 |         70 |    67.6 |    54.9 |           62.5 |              46.2 |
| LEYTE NORMAL UNIVERSITY                                                               | Public        |                71 |            39 |        43.3 |         21 |         66 |    60.3 |      50 |           39.4 |              45.5 |
| ST. ALEXIUS COLLEGE                                                                   | Private       |                71 |            58 |        46.5 |       12.5 |         71 |    69.6 |    60.9 |           45.1 |              54.5 |
| UNIVERSITY OF VISAYAS CEBU                                                            | Private       |                69 |            10 |        19.2 |          2 |         32 |    30.3 |    19.7 |           33.3 |              11.6 |
| RANGSIT UNIVERSITY                                                                    | Foreign       |                68 |            36 |          44 |       11.5 |       75.2 |    58.2 |    46.3 |           67.6 |              31.6 |
| UNIVERSITY OF NUEVA CACERES                                                           | Private       |                67 |            40 |        40.1 |         13 |         64 |    59.4 |    51.6 |           61.2 |              45.5 |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-LAS PIÑAS                                   | Private       |                67 |            15 |        23.7 |        5.5 |         33 |    31.8 |    21.2 |           43.3 |              26.9 |
| NOTRE DAME OF JOLO COLLEGE                                                            | Private       |                65 |            40 |        43.5 |         16 |         69 |      60 |    50.8 |           58.5 |              18.5 |
| LYCEUM NORTHWESTERN DAGUPAN CITY                                                      | Private       |                64 |            19 |        26.3 |        6.8 |       44.8 |    31.2 |    28.1 |           51.6 |              56.2 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                                 | Public        |                63 |            14 |        22.8 |          6 |       37.5 |    31.7 |    21.7 |           22.2 |              14.3 |
| ASSUMPTION COLLEGE                                                                    | Private       |                62 |            46 |        47.7 |       25.8 |       68.5 |    66.7 |    56.7 |           43.5 |              37.5 |
| LA CONSOLACION COLLEGE - MANILA                                                       | Private       |                61 |            45 |          48 |         20 |         71 |    68.9 |      59 |             77 |                34 |
| UNIVERSITY OF THE CORDILLERAS (BCF)                                                   | Private       |                61 |            33 |        37.7 |         26 |         50 |    62.3 |    47.5 |             41 |              42.6 |
| CATANDUANES STATE COLLEGE - MAIN                                                      | Public        |                60 |          44.5 |        47.8 |       23.8 |       77.5 |      65 |      55 |             50 |              68.4 |
| UNIVERSITY OF SAN JOSE - RECOLETOS                                                    | Private       |                59 |            42 |        47.1 |         16 |         80 |    66.1 |    54.2 |           45.8 |                44 |
| BUTUAN DOCTORS COLLEGE                                                                | Private       |                58 |            47 |        46.9 |         27 |       70.5 |    70.7 |    62.1 |           56.9 |              37.5 |
| SACRED HEART COLLEGE OF LUCENA                                                        | Private       |                57 |            48 |        44.4 |         18 |         64 |    63.2 |    56.1 |           64.9 |              58.3 |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                   | Public        |                57 |            55 |        50.3 |         28 |       75.5 |    77.4 |    67.9 |           49.1 |                40 |
| MANILA DOCTORS COLLEGE U.N. AVENUE MANILA                                             | Private       |                56 |            42 |        40.1 |       21.5 |       50.5 |    66.1 |    58.9 |           57.1 |              32.1 |
| NOTRE DAME UNIVERSITY COTABATO CITY                                                   | Private       |                56 |          25.5 |        35.4 |        8.5 |         63 |    42.9 |    35.7 |           71.4 |              35.7 |
| UNIVERSITY OF MAKATI                                                                  | Public        |                56 |            42 |        43.7 |         15 |       64.5 |    67.9 |    51.8 |           53.6 |                37 |
| DIPOLOG MEDICAL CENTER COLLEGE FOUNDATION                                             | Private       |                55 |            43 |        42.8 |       16.2 |       65.2 |    65.4 |    57.7 |           43.6 |              30.8 |
| ST. PAUL UNIVERSITY DUMAGUETE                                                         | Private       |                55 |            44 |        44.5 |         16 |         71 |    65.4 |    57.7 |             60 |              41.2 |
| UNIVERSITY OF THE EAST - RAMON MAGSAYSAY MEM. MEDICAL CENTER                          | Private       |                55 |            57 |        53.3 |       39.5 |       65.5 |    89.1 |    74.5 |           96.4 |              50.9 |
| DE LA SALLE - LIPA BATANGAS                                                           | Private       |                53 |            45 |        43.5 |         21 |         58 |      66 |    58.5 |           52.8 |              39.6 |
| MIRIAM COLLEGE FOUNDATION INC.                                                        | Private       |                53 |            38 |        38.4 |         15 |         58 |    62.3 |    45.3 |              0 |              32.1 |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                                            | Public        |                53 |            11 |          24 |          5 |         37 |    33.3 |    25.5 |              0 |               9.4 |
| SAN LORENZO RUIZ COLLEGE OF ORMOC                                                     | Private       |                53 |            38 |        39.9 |         19 |         63 |    64.7 |      49 |           47.2 |                50 |
| OUR LADY OF FATIMA UNIVERSITY - LAGRO QUEZON CITY                                     | Private       |                52 |            32 |        32.7 |       13.5 |         46 |    53.8 |    32.7 |           61.5 |              42.3 |
| SOUTH SEED - LPDH COLLEGE                                                             | Private       |                51 |            53 |        51.3 |       35.5 |         71 |      80 |      64 |           43.1 |                 0 |
| CEBU DOCTOR'S UNIVERSITY COLLEGE OF MEDICINE - MANDAUE CITY CEBU                      | Private       |                50 |            50 |        51.4 |       26.8 |       81.2 |    69.4 |    65.3 |             56 |                48 |
| BAGUIO CENTRAL UNIVERSITY                                                             | Private       |                50 |          36.5 |        43.2 |         11 |       73.2 |    59.6 |    48.9 |             60 |              25.6 |
| MINDANAO SANITARIUM & HOSPITAL COLLEGE ILIGAN CITY                                    | Private       |                50 |            17 |        24.8 |          9 |         42 |      36 |      28 |             80 |                26 |
| NAGA COLLEGE FOUNDATION                                                               | Private       |                50 |            48 |        48.4 |       18.5 |       74.5 |    68.9 |    64.4 |             58 |              44.4 |
| BICOL UNIVERSITY - TABACO                                                             | Public        |                48 |            45 |        45.3 |       23.5 |       68.5 |    70.8 |    52.1 |             50 |                50 |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                              | Public        |                48 |            69 |        57.7 |         34 |       85.5 |    78.3 |    71.7 |             50 |              52.2 |
| UNIVERSITY OF THE PHILIPPINES - TACLOBAN                                              | Public        |                48 |            62 |        60.3 |       45.8 |         81 |    81.2 |    79.2 |            6.2 |              66.7 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION INC.                                          | Private       |                47 |            23 |        32.4 |       12.5 |       48.5 |    42.6 |      34 |           72.3 |              44.7 |
| BICOL UNIVERSITY                                                                      | Public        |                47 |          29.5 |        39.7 |       16.2 |       65.8 |      50 |    45.7 |           19.1 |              42.6 |
| PHILIPPINE WOMEN'S UNIVERSITY TAFT AVENUE MANILA                                      | Private       |                46 |          47.5 |        41.5 |       14.8 |       62.8 |    62.2 |    57.8 |           67.4 |              30.4 |
| DE LA SALLE - COLLEGE OF SAINT BENILDE                                                | Private       |                46 |            54 |        52.4 |         33 |         76 |    77.8 |    62.2 |           56.5 |              47.4 |
| PILAR COLLEGE                                                                         | Private       |                46 |          41.5 |        46.9 |         26 |       72.2 |    69.6 |    56.5 |           56.5 |              43.5 |
| MAPUA INSTITUTE OF TECHNOLOGY - MANILA                                                | Private       |                46 |          37.5 |        45.6 |         20 |       72.8 |    66.7 |    48.9 |           34.8 |              27.8 |
| UNIVERSITY OF THE PHILIPPINES - CEBU COLLEGE                                          | Public        |                45 |            75 |        70.9 |         63 |         87 |    97.8 |    86.7 |            2.2 |              66.7 |
| MOUNTAIN VIEW COLLEGE BUKIDNON                                                        | Private       |                45 |            42 |        40.4 |         16 |         63 |      60 |    51.1 |           71.1 |                40 |
| LYCEUM OF THE PHILIPPINES - LAGUNA                                                    | Private       |                45 |            37 |        43.2 |         15 |         75 |    59.1 |    47.7 |           31.1 |              33.3 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - LAGUNA                                          | Private       |                45 |            45 |        50.4 |         23 |         84 |    70.5 |    61.4 |           64.4 |              47.4 |
| UNIVERSITY OF THE ASSUMPTION                                                          | Private       |                44 |          45.5 |        49.9 |         30 |       75.8 |    80.5 |      61 |           47.7 |              21.1 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - BINAN LAGUNA                                    | Private       |                44 |          30.5 |        35.2 |       16.8 |         54 |    59.1 |    34.1 |           61.4 |              45.5 |
| MEDINA COLLEGE                                                                        | Private       |                44 |            39 |        41.2 |         13 |         68 |    58.1 |    46.5 |             75 |              16.7 |
| PHILIPPINE CHRISTIAN UNIVERSITY                                                       | Private       |                44 |          49.5 |        42.8 |       17.2 |         64 |    65.9 |    59.1 |             50 |                32 |
| NOTRE DAME OF DADIANGAS COLLEGE GEN. SANTOS                                           | Private       |                43 |            34 |        38.4 |         15 |         57 |    58.1 |    46.5 |           25.6 |              37.2 |
| UNIVERSITY OF CAGAYAN VALLEY                                                          | Private       |                43 |          58.5 |        56.4 |       30.5 |       86.8 |    78.6 |    61.9 |           48.8 |              31.2 |
| BROKENSHIRE COLLEGE DAVAO CITY                                                        | Private       |                43 |            28 |        32.7 |         11 |         44 |    46.5 |    34.9 |             93 |              41.9 |
| CENTRAL MINDANAO UNIVERSITY BUKIDNON                                                  | Public        |                43 |            30 |        31.5 |         10 |         47 |    51.2 |    32.6 |           11.6 |              27.9 |
| UNIVERSITY OF CALIFORNIA - DAVIS                                                      | Foreign       |                42 |            73 |        67.7 |       49.2 |         88 |    95.2 |      81 |           28.6 |              21.9 |
| UNIVERSITY OF THE VISAYAS - MANDAUE                                                   | Private       |                42 |            40 |        45.2 |       12.2 |       72.2 |    64.3 |    52.4 |           61.9 |              44.4 |
| TRINITY COLLEGE                                                                       | Foreign       |                40 |            20 |          31 |       11.8 |       49.5 |      40 |    37.5 |             15 |                35 |
| UNIVERSITY OF CALIFORNIA - IRVINE                                                     | Foreign       |                40 |          73.5 |        69.2 |       65.5 |         86 |    92.3 |    89.7 |             35 |              22.9 |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                               | Public        |                40 |            30 |          35 |       11.8 |         51 |    55.3 |    42.1 |             60 |              72.7 |
| LA CONSOLACION COLLEGE                                                                | Private       |                40 |          14.5 |        19.2 |        7.8 |       25.5 |    21.1 |    13.2 |             70 |                25 |
| FILAMER CHRISTIAN UNIVERSITY                                                          | Private       |                40 |            33 |        40.2 |       17.5 |         64 |    56.8 |    43.2 |             50 |              30.4 |
| YAMAN LAHI FOUNDATION - EMILIO AGUINALDO COLLEGE                                      | Private       |                40 |          40.5 |        46.8 |         23 |       76.2 |    65.8 |    55.3 |           47.5 |               nan |
| UNIVERSIDAD DE STA. ISABEL NAGA CITY                                                  | Private       |                39 |            40 |        42.5 |         17 |       63.5 |    68.4 |    52.6 |           53.8 |              51.3 |
| ST. JUDE COLLEGE MANILA                                                               | Private       |                39 |            26 |        30.8 |         12 |       40.5 |    38.5 |    25.6 |           71.8 |              46.2 |
| RANGSIT UNIVERSITY THAILAND                                                           | Foreign       |                38 |            11 |        23.4 |          3 |       35.5 |    31.6 |    23.7 |           68.4 |               5.3 |
| UNIVERSITY OF BOHOL                                                                   | Private       |                37 |          40.5 |        44.4 |       19.8 |         73 |    61.1 |      50 |           43.2 |                60 |
| LOURDES COLLEGE                                                                       | Private       |                37 |            49 |        47.7 |         29 |         66 |      75 |    63.9 |           48.6 |              41.2 |
| NUEVA ECIJA COLLEGES                                                                  | Private       |                37 |            34 |        41.9 |       13.5 |       79.2 |    52.8 |    47.2 |           64.9 |              28.6 |
| NEW ERA UNIVERSITY QUEZON CITY                                                        | Private       |                37 |            22 |        26.3 |          5 |         36 |    35.1 |    24.3 |            2.7 |              29.7 |
| NORTHWESTERN UNIVERSITY                                                               | Private       |                36 |          39.5 |          44 |         18 |         68 |    63.9 |      50 |           38.9 |              45.5 |
| VISAYAS STATE UNIVERSITY - MAIN                                                       | Public        |                36 |          42.5 |        46.1 |       27.8 |       68.2 |    74.3 |    57.1 |           55.6 |              42.9 |
| UNIVERSITY OF LUZON                                                                   | Private       |                36 |            21 |        31.9 |        8.8 |       54.8 |    38.2 |    29.4 |           69.4 |              37.5 |
| MAHIDOL UNIVERSITY                                                                    | Foreign       |                36 |            42 |        41.9 |       19.5 |       68.2 |    54.3 |    51.4 |           52.8 |              16.7 |
| DAVAO MEDICAL SCHOOL FOUNDATION INC.                                                  | Private       |                36 |            42 |        37.9 |       16.2 |       53.8 |    62.9 |    57.1 |           88.9 |              38.9 |
| BATANGAS STATE UNIVERSITY - MAIN                                                      | Public        |                35 |            39 |        43.1 |          6 |       74.5 |    63.6 |    51.5 |           42.9 |              28.6 |
| MEDINA COLLEGE - PAGADIAN                                                             | Private       |                35 |            44 |        48.3 |       25.5 |       73.5 |    65.7 |    54.3 |           34.3 |              33.3 |
| CALAYAN EDUCATIONAL FOUNDATION                                                        | Private       |                35 |          49.5 |          48 |       26.8 |       69.2 |    73.5 |    67.6 |           42.9 |              44.4 |
| ST. PAUL UNIVERSITY - TUGUEGARAO CAGAYAN                                              | Private       |                34 |          20.5 |        25.8 |        8.5 |       39.5 |    35.3 |    26.5 |           32.4 |              38.2 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS CEBU                                     | Public        |                34 |            81 |        75.3 |         68 |       90.8 |    97.1 |    97.1 |           47.1 |              79.4 |
| PINES CITY COLLEGES - BAGUIO CITY                                                     | Private       |                34 |          18.5 |        24.7 |          9 |       34.8 |    29.4 |    20.6 |             50 |              20.6 |
| ARELLANO UNIVERSITY                                                                   | Private       |                33 |            25 |        29.3 |         12 |       40.2 |    43.8 |    28.1 |           75.8 |              30.3 |
| HOLY TRINITY UNIVERSITY                                                               | Private       |                33 |            38 |        44.8 |         22 |         71 |    69.7 |    45.5 |           72.7 |                25 |
| SAN BEDA COLLEGE - ALABANG                                                            | Private       |                33 |            34 |        42.2 |         22 |         63 |    66.7 |    45.5 |           42.4 |                 0 |
| ILIGAN MEDICAL CENTER ILIGAN CITY                                                     | Private       |                33 |            19 |        27.8 |          9 |         42 |    36.4 |    30.3 |           69.7 |              27.3 |
| OUR LADY OF GUADALUPE COLLEGES                                                        | Private       |                33 |          36.5 |        45.7 |       23.2 |       71.8 |    56.2 |    43.8 |           72.7 |              41.7 |
| SAINT MARY'S COLLEGE OF TAGUM                                                         | Private       |                33 |            55 |        52.3 |         33 |         75 |    75.8 |    69.7 |           66.7 |              23.5 |
| MARIANO MARCOS STATE UNIVERSITY ILOCOS NORTE                                          | Public        |                32 |            35 |        44.7 |         22 |         70 |    59.4 |    43.8 |             25 |              56.2 |
| MINDANAO STATE UNIVERSITY GENERAL SANTOS CITY                                         | Public        |                32 |          37.5 |        44.4 |         27 |       65.8 |    65.6 |      50 |              0 |              46.9 |
| Remedios Trinidad Romualdez Medical Foundation                                        | Not Specified |                31 |            34 |        43.4 |         25 |         66 |      60 |      50 |           90.3 |              35.5 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA - CALAMBA                                   | Private       |                31 |          62.5 |        61.2 |       42.8 |       79.2 |      90 |    76.7 |           54.8 |              71.4 |
| LYCEUM OF THE PHILIPPINES - ST. CABRINI COLLEGE OF ALLIED MEDICINE                    | Private       |                31 |            38 |        41.4 |         19 |       55.5 |    64.5 |    48.4 |           51.6 |              45.5 |
| LYCEUM OF THE PHILIPPINES UNIVERSITY                                                  | Private       |                30 |          54.5 |        52.7 |       28.2 |       83.2 |      70 |      60 |           56.7 |              33.3 |
| LYCEUM OF BATANGAS                                                                    | Private       |                30 |            23 |        28.4 |       10.2 |       38.8 |    33.3 |    26.7 |             60 |              43.3 |
| CARAGA STATE UNIVERSITY - MAIN                                                        | Public        |                30 |            45 |        48.3 |       18.5 |         85 |    57.1 |      50 |             40 |              44.4 |
| UNIVERSITY OF CALIFORNIA LOS ANGELES                                                  | Foreign       |                30 |            75 |        69.3 |         59 |         89 |    86.2 |    86.2 |           23.3 |                24 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES-DAVAO CITY                                     | Public        |                30 |            25 |        31.4 |       15.2 |         44 |    43.3 |      30 |              0 |                30 |
| CAPITOL MEDICAL CENTER COLLEGE Q.C.                                                   | Private       |                30 |          26.5 |        29.7 |       12.8 |       42.8 |    46.7 |    33.3 |           56.7 |                30 |
| ST. ANTHONY COLLEGE OF ROXAS CITY                                                     | Private       |                30 |          33.5 |        41.4 |       11.5 |       65.2 |    58.6 |    44.8 |           66.7 |              31.2 |
| CHULALONGKORN UNIVERSITY                                                              | Foreign       |                29 |            50 |        51.9 |         26 |         81 |      69 |    62.1 |           34.5 |               7.7 |
| UNIVERSIDAD DE MANILA                                                                 | Public        |                29 |          65.5 |        54.7 |         32 |         80 |    78.6 |    67.9 |           34.5 |              33.3 |
| UNIVERSITY OF ST. LA SALLE - DASMARIÑAS CAVITE                                        | Private       |                29 |            36 |        38.1 |         21 |         53 |    55.2 |    41.4 |            3.4 |              44.8 |
| ST. JOSEPH'S COLLEGE OF QUEZON CITY                                                   | Private       |                29 |            39 |          43 |       21.8 |         59 |    64.3 |      50 |           72.4 |              44.8 |
| UNIVERSITY OF ASIA AND THE PACIFIC                                                    | Private       |                28 |          40.5 |        43.5 |       18.5 |         69 |    64.3 |      50 |           21.4 |              52.9 |
| UNIVERSITY OF CEBU (FORMERLY CEBU CENTRAL COLLEGES)                                   | Private       |                28 |          36.5 |        38.8 |       25.8 |       55.2 |    67.9 |    46.4 |           89.3 |              60.7 |
| PHILIPPINE REHABILITATION INSTITUTE FOUNDATION                                        | Private       |                28 |            53 |        49.6 |         15 |         79 |    60.7 |    57.1 |           42.9 |              38.9 |
| MAHIDOL UNIVERSITY THAILAND                                                           | Foreign       |                28 |          35.5 |          36 |       13.5 |         55 |    57.1 |    46.4 |           57.1 |               3.6 |
| LA SALLE UNIVERSITY                                                                   | Private       |                28 |          49.5 |        49.2 |       26.8 |       70.8 |    67.9 |    57.1 |           46.4 |              38.5 |
| UNIVERSITY OF LA SALETTE SANTIAGO CITY                                                | Private       |                28 |          30.5 |        36.9 |       14.2 |         49 |      50 |    32.1 |           64.3 |              46.4 |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                    | Public        |                27 |            35 |          44 |         21 |       64.5 |    59.3 |    40.7 |           55.6 |              28.6 |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                           | Public        |                27 |          58.5 |        52.2 |         32 |         71 |    83.3 |      75 |           55.6 |              27.3 |
| SULU STATE COLLEGE                                                                    | Public        |                27 |            34 |        42.1 |          5 |         77 |      64 |      48 |             37 |                 0 |
| RIVERSIDE COLLEGE BACOLOD CITY                                                        | Private       |                27 |            37 |          40 |         23 |         58 |      63 |    48.1 |           55.6 |              55.6 |
| UNION CHRISTIAN COLLEGE                                                               | Private       |                26 |            41 |        41.8 |       26.2 |       47.5 |    69.2 |    53.8 |           80.8 |              43.8 |
| WEST NEGROS UNIVERSITY                                                                | Private       |                26 |            49 |        52.8 |         26 |       81.2 |    70.8 |    58.3 |           69.2 |              52.2 |
| MANUEL S. ENVERGA UNIVERSITY FOUNDATION - LUCENA                                      | Private       |                26 |            58 |        52.3 |       25.2 |       81.5 |    73.1 |    61.5 |           46.2 |                50 |
| CALIFORNIA STATE UNIVERSITY                                                           | Foreign       |                26 |          57.5 |          61 |       48.2 |       78.8 |    92.3 |    76.9 |           30.8 |              23.1 |
| SURIGAO EDUCATION CENTER                                                              | Private       |                26 |            24 |        37.4 |        9.8 |       61.5 |    42.3 |    38.5 |           80.8 |              33.3 |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES                                                 | Private       |                26 |            47 |          43 |       12.2 |         69 |    61.5 |    53.8 |           73.1 |                30 |
| CEBU INSTITUTE OF TECHNOLOGY - UNIVERSITY                                             | Private       |                26 |            48 |        44.3 |       23.2 |       54.8 |    65.4 |    57.7 |           65.4 |              46.2 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA               | Public        |                26 |          50.5 |        47.6 |         15 |       76.8 |    69.2 |    57.7 |           46.2 |                 0 |
| ST. SCHOLASTICA'S COLLEGE - TACLOBAN CITY                                             | Private       |                26 |            31 |        38.6 |         15 |       57.5 |    53.8 |    42.3 |           84.6 |              46.2 |
| ST. DOMINIC COLLEGE OF ARTS AND SCIENCES OF CAVITE                                    | Private       |                25 |            48 |        45.8 |         28 |         62 |      68 |      60 |             60 |                30 |
| UNIVERSITY OF CALIFORNIA RIVERSIDE CA USA                                             | Foreign       |                25 |            84 |        76.1 |         67 |         92 |      96 |      92 |             24 |                20 |
| WESLEYAN UNIVERSITY-PHILIPPINES CABANATUAN CITY                                       | Private       |                25 |            33 |        36.6 |         16 |         51 |      56 |      40 |             64 |                40 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM                                                   | Private       |                25 |            51 |        46.2 |         13 |         81 |      60 |      52 |             52 |              14.3 |
| NATIONAL UNIVERSITY                                                                   | Private       |                24 |            55 |        51.3 |       34.8 |         68 |    79.2 |    66.7 |           58.3 |                50 |
| UNIVERSITY OF MINDANAO                                                                | Private       |                24 |          55.5 |        54.8 |       37.5 |         75 |    83.3 |    70.8 |           62.5 |              14.3 |
| WORLD CITI COLLEGES                                                                   | Private       |                24 |            29 |        36.6 |         14 |       61.5 |    45.8 |    33.3 |             50 |              16.7 |
| MAPUA INSTITUTE OF TECHNOLOGY                                                         | Private       |                24 |            49 |        45.5 |       20.2 |       66.2 |    66.7 |    62.5 |           62.5 |              33.3 |
| UNIVERSITY OF THE IMMACULATE CONCEPCION DAVAO CITY                                    | Private       |                24 |          28.5 |        32.8 |       16.2 |       48.2 |      50 |    33.3 |           70.8 |                50 |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                                | Public        |                24 |            54 |        54.3 |       21.8 |       83.2 |    70.8 |    66.7 |           45.8 |              66.7 |
| PLT COLLEGE                                                                           | Private       |                24 |          43.5 |        39.9 |         12 |       61.8 |    58.3 |    54.2 |           54.2 |                60 |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                                 | Public        |                24 |          44.5 |        43.8 |       17.5 |       62.5 |    77.3 |    59.1 |             50 |              14.3 |
| UNIVERSITY OF SOUTHERN MINDANAO NORTH COTABATO                                        | Public        |                23 |            44 |        42.2 |         16 |         63 |    56.5 |    52.2 |             13 |              39.1 |
| OTHERS (PLEASE SPECIFY)                                                               | Not Specified |                23 |            75 |        71.2 |         60 |         87 |    91.3 |    91.3 |           26.1 |              21.7 |
| UNIVERSITY OF CALIFORNIA - SAN DIEGO                                                  | Foreign       |                23 |            78 |        65.5 |       55.5 |       87.5 |    86.4 |    81.8 |           30.4 |              38.9 |
| BENGUET STATE UNIVERSITY                                                              | Public        |                23 |            42 |        46.3 |         27 |         71 |    73.9 |    65.2 |           60.9 |              43.5 |
| UPH-DR. JOSE G. TAMAYO MEDICAL UNIV.                                                  | Private       |                23 |            20 |        30.9 |       15.5 |         38 |    30.4 |    26.1 |           26.1 |              26.1 |
| LORMA COLLEGE SAN FERNANDO LA UNION                                                   | Private       |                23 |            19 |        24.9 |         10 |         37 |    39.1 |    17.4 |           73.9 |              43.5 |
| UNIVERSITY OF PERPETUAL HELP RIZAL - MOLINO                                           | Private       |                23 |            31 |        35.2 |         14 |         47 |    56.5 |    43.5 |           69.6 |              29.4 |
| AL KWARIZMI INTERNATIONAL COLLEGE FOUNDATION                                          | Foreign       |                23 |            39 |        41.3 |         19 |         55 |    60.9 |    47.8 |           52.2 |              33.3 |
| ST. MICHAEL'S COLLEGE                                                                 | Private       |                23 |            43 |        44.6 |         24 |       61.5 |    65.2 |    52.2 |           65.2 |                30 |
| CHIANG MAI UNIVERSITY                                                                 | Foreign       |                23 |            21 |        31.2 |          7 |       51.5 |    43.5 |    34.8 |           43.5 |               5.3 |
| TARLAC STATE UNIVERSITY                                                               | Public        |                23 |            40 |        43.7 |       15.5 |       67.5 |    60.9 |    56.5 |           52.2 |              38.5 |
| ASSUMPTION COLLEGE MAKATI                                                             | Private       |                22 |            45 |          44 |       33.5 |         57 |    86.4 |    59.1 |            4.5 |              40.9 |
| COLEGIO DE SAN AGUSTIN BACOLOD                                                        | Private       |                22 |            29 |        32.5 |       13.5 |         47 |      50 |    31.8 |           40.9 |              45.5 |
| KESTER GRANT COLLEGE - PHILIPPINES                                                    | Private       |                22 |          40.5 |        47.2 |       26.2 |       66.5 |    63.6 |      50 |           77.3 |              14.3 |
| GOOD SAMARITAN COLLEGES                                                               | Private       |                22 |          49.5 |        50.8 |       37.2 |       72.5 |    81.8 |    68.2 |           40.9 |                40 |
| MISAMIS UNIVERSITY                                                                    | Private       |                22 |          18.5 |          26 |         13 |       35.2 |    36.4 |    22.7 |           63.6 |              22.7 |
| RIVERSIDE COLLEGE OF NURSING BACOLOD                                                  | Private       |                21 |            32 |        36.6 |         20 |         59 |    57.1 |    38.1 |             19 |              42.9 |
| BICOL UNIVERSITY COLLEGE OF SCIENCE LEGAZPI CITY                                      | Public        |                21 |            17 |          30 |          8 |         46 |    38.1 |    38.1 |              0 |              57.1 |
| JOHN PAUL II COLLEGE OF DAVAO                                                         | Private       |                21 |            47 |          48 |         20 |         81 |    61.9 |    52.4 |           66.7 |              64.3 |
| 13207A                                                                                | Not Specified |                21 |            34 |        46.1 |         19 |         84 |    52.4 |    42.9 |             81 |              52.4 |
| DIVINE WORD COLLEGE OF LEGAZPI                                                        | Private       |                21 |            27 |        31.4 |          6 |         51 |    47.6 |    42.9 |           33.3 |                25 |
| DE LOS SANTOS - STI COLLEGE                                                           | Private       |                21 |            44 |        43.4 |         23 |         69 |    66.7 |    52.4 |           71.4 |                40 |
| CENTRAL LUZON DOCTOR'S HOSPITAL TARLAC                                                | Private       |                21 |            41 |          42 |         28 |         66 |    71.4 |    52.4 |           71.4 |              47.6 |
| MANILA THEOLOGICAL COLLEGE                                                            | Private       |                21 |            31 |        35.6 |         13 |         50 |      55 |      35 |           42.9 |              21.4 |
| HOLY NAME UNIVERSITY - TAGBILARAN CITY                                                | Private       |                21 |            41 |        43.7 |         32 |         56 |      81 |    57.1 |           33.3 |              61.9 |
| THAMMASAT UNIVERSITY                                                                  | Foreign       |                20 |            36 |        39.3 |       19.5 |       51.2 |      65 |      50 |             40 |                25 |
| BALIUAG UNIVERSITY                                                                    | Private       |                20 |            43 |        46.2 |       29.8 |       66.5 |    78.9 |    63.2 |             65 |              63.6 |
| AQUINAS UNIVERSITY LEGASPI CITY                                                       | Private       |                20 |            29 |          34 |         16 |       48.2 |    52.6 |    36.8 |             80 |                60 |
| OUR LADY OF MT. CARMEL INSTITUTE OF MEDICAL STUDIES                                   | Private       |                20 |          46.5 |        48.4 |       18.8 |       83.2 |    73.7 |    52.6 |             35 |                 0 |
| OLIVAREZ COLLEGE                                                                      | Private       |                20 |          39.5 |        48.9 |       30.5 |       63.5 |      75 |      50 |             60 |              38.5 |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES INC.                                            | Private       |                20 |            13 |        21.4 |        4.8 |       33.8 |      30 |      25 |             55 |                35 |
| DE LA SALLE COLLEGE OF SAINT BENILDE - MANILA                                         | Private       |                20 |          57.5 |        58.6 |         41 |         81 |      85 |      75 |             25 |                60 |
| COLEGIO DE DAGUPAN                                                                    | Private       |                20 |            53 |        52.5 |       31.8 |       80.5 |      75 |      65 |             80 |              46.2 |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING & LIBERAL ARTS                            | Private       |                19 |            47 |        49.5 |         37 |       63.5 |    89.5 |    68.4 |           63.2 |              52.6 |
| AGO MEDICAL AND EDUCATIONAL CENTER LEGAZPI CITY                                       | Private       |                19 |            28 |        36.1 |         15 |       54.5 |    47.4 |    42.1 |           63.2 |              47.4 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - SOUTH LA UNION                         | Public        |                19 |            45 |        45.9 |       20.5 |         74 |    57.9 |    52.6 |           63.2 |              57.1 |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES CAGAYAN                                      | Private       |                19 |            44 |        37.9 |       21.5 |       51.5 |    63.2 |    57.9 |           52.6 |              31.6 |
| WESTERN STATE UNIVERSITY OF COLORADO                                                  | Foreign       |                19 |            50 |        43.3 |         23 |         59 |    68.4 |    57.9 |           84.2 |              57.9 |
| UNIVERSITY OF PERPETUAL HELP COLLEGE OF LAS PINAS                                     | Private       |                19 |            39 |        36.1 |         14 |       54.5 |    57.9 |    47.4 |           47.4 |              47.4 |
| HOLY ANGEL UNIVERSITY ANGELES CITY                                                    | Private       |                18 |            40 |        45.8 |       24.8 |       60.8 |    61.1 |      50 |           83.3 |              44.4 |
| UNIVERSITY OF SAN JOSE RECOLETOS CEBU                                                 | Private       |                18 |            31 |        30.7 |        7.5 |       50.5 |      50 |    38.9 |           33.3 |              33.3 |
| SAMAR STATE UNIVERSITY - MAIN                                                         | Public        |                18 |            46 |        49.1 |         34 |         65 |    82.4 |    58.8 |           61.1 |              66.7 |
| MAPUA INSTITUTE OF TECHNOLOGY - MAKATI                                                | Private       |                18 |          24.5 |        32.7 |       15.5 |       43.8 |    47.1 |    35.3 |           83.3 |              21.4 |
| TAGUM DOCTORS COLLEGE                                                                 | Private       |                18 |            29 |        37.7 |         15 |         50 |    47.1 |    35.3 |           38.9 |               100 |
| COLEGIO DE STA. LOURDES OF LEYTE FOUNDATION                                           | Private       |                18 |            37 |        40.8 |       14.2 |       74.8 |    55.6 |      50 |           44.4 |                50 |
| UNIVERSITY OF CALIFORNIA BERKELEY                                                     | Foreign       |                18 |            81 |        65.7 |       36.2 |         95 |    81.2 |    81.2 |           38.9 |              41.7 |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                  | Public        |                18 |            64 |        48.3 |          8 |       80.2 |    55.6 |    55.6 |           44.4 |                25 |
| ARELLANO UNIVERSITY - PASIG                                                           | Private       |                18 |          45.5 |        43.6 |         22 |         60 |    66.7 |    66.7 |           61.1 |              57.1 |
| PAMANTASAN NG LUNGSOD NG PASIG                                                        | Public        |                18 |            47 |        46.4 |       13.5 |         82 |    61.1 |    55.6 |           44.4 |                25 |
| UNIVERSITY OF CALIFORNIA-RIVERSIDE                                                    | Foreign       |                18 |            63 |        60.2 |         56 |         82 |    76.5 |    76.5 |           55.6 |              14.3 |
| ST. JOSEPH COLLEGE CAVITE CITY                                                        | Private       |                17 |            42 |        43.4 |         18 |         69 |    73.3 |      60 |           82.4 |              33.3 |
| UNIVERSITY OF TORONTO                                                                 | Foreign       |                17 |            77 |        74.8 |         65 |         91 |    94.1 |    88.2 |           29.4 |              43.8 |
| UNIVERSITY OF PANGASINAN DAGUPAN CITY                                                 | Private       |                17 |            30 |        33.8 |         22 |         42 |    58.8 |    29.4 |           88.2 |              47.1 |
| ANDRES BONIFACIO COLLEGE                                                              | Private       |                17 |          51.5 |        50.9 |       27.2 |       81.5 |      75 |    56.2 |           70.6 |                50 |
| CHULALONGKORN UNIVERSITY THAILAND                                                     | Foreign       |                17 |            34 |        35.9 |         20 |         48 |    58.8 |    41.2 |           52.9 |                 0 |
| OUR LADY OF FATIMA UNIVERSITY - PAMPANGA                                              | Private       |                17 |            29 |        37.7 |         20 |         60 |      50 |    43.8 |           41.2 |               nan |
| BUKIDNON STATE UNIVERSITY                                                             | Public        |                17 |            20 |        39.3 |         12 |         70 |      50 |      50 |           58.8 |                25 |
| LA CONSOLACION UNIVERSITY PHILIPPINES                                                 | Private       |                17 |            54 |        45.5 |         15 |         66 |    64.7 |    58.8 |           58.8 |                50 |
| BULACAN STATE UNIVERSITY                                                              | Public        |                16 |          46.5 |        42.4 |       14.5 |         67 |    62.5 |    56.2 |            6.2 |              37.5 |
| COLEGIO DE SAN JUAN DE LETRAN CALAMBA                                                 | Private       |                16 |            19 |        23.6 |       12.2 |         28 |      25 |    18.8 |           31.2 |                25 |
| CENTRAL LUZON STATE UNIVERSITY NUEVA ECIJA                                            | Public        |                16 |          31.5 |        32.1 |       11.8 |       45.5 |      50 |    37.5 |              0 |              43.8 |
| UNIVERSITY OF EASTERN PHILIPPINES - SAMAR                                             | Public        |                16 |            14 |        17.1 |          4 |       20.8 |    12.5 |     6.2 |           62.5 |              56.2 |
| NORTHERN LUZON ADVENTIST COLLEGE                                                      | Private       |                16 |          51.5 |        48.8 |       29.2 |         70 |      75 |    62.5 |             50 |              11.1 |
| UNIVERSITY OF WASHINGTON                                                              | Foreign       |                16 |            78 |        67.6 |       52.8 |         93 |    87.5 |    87.5 |           12.5 |              16.7 |
| MAE FAH LUANG UNIVERSITY                                                              | Foreign       |                16 |          16.5 |        40.8 |          7 |       75.5 |    43.8 |    43.8 |           43.8 |              33.3 |
| NATIONAL UNIVERSITY - CEDCE                                                           | Private       |                16 |            44 |        40.1 |       14.5 |       54.8 |    56.2 |    56.2 |           56.2 |              33.3 |
| ARELLANO UNIVERSITY - PASAY                                                           | Private       |                16 |          35.5 |        44.9 |       17.2 |       74.5 |      60 |    46.7 |           43.8 |                25 |
| CANOSSA COLLEGE                                                                       | Private       |                16 |            61 |        63.5 |       53.2 |       82.5 |    93.8 |    87.5 |           62.5 |              61.5 |
| DE OCAMPO MEMORIAL COLLEGE                                                            | Private       |                16 |            38 |        39.9 |         19 |         54 |    68.8 |    37.5 |           68.8 |                25 |
| IMMACULATE CONCEPTION COLLEGE - ALBAY                                                 | Private       |                16 |            59 |        50.7 |         34 |         68 |    73.3 |    73.3 |           37.5 |                50 |
| MARY CHILES COLLEGE                                                                   | Private       |                15 |            32 |        38.9 |       16.5 |       67.5 |    53.3 |      40 |           46.7 |                50 |
| LIPA CITY COLLEGES                                                                    | Private       |                15 |            79 |        61.1 |         31 |         91 |    86.7 |    66.7 |           33.3 |              44.4 |
| SAINT PAUL COLLEGE OF ILOCOS SUR                                                      | Private       |                15 |            48 |        50.9 |         31 |       71.5 |    73.3 |    66.7 |             60 |                25 |
| CARITAS FAMILY HOSPITAL AND COLLEGES                                                  | Private       |                15 |            63 |        55.3 |       39.5 |         78 |      80 |    73.3 |           53.3 |                50 |
| ST. PAUL COLLEGE ILOILO                                                               | Private       |                15 |            50 |        56.8 |         43 |       77.5 |    86.7 |      80 |           86.7 |                40 |
| COLLEGE OF THE HOLY SPIRIT OF TARLAC                                                  | Private       |                15 |            56 |        56.6 |       34.5 |         90 |    78.6 |    78.6 |             40 |                60 |
| UNIVERSITY OF BATANGAS                                                                | Private       |                15 |            34 |        34.3 |       22.5 |         48 |      60 |    46.7 |           73.3 |                30 |
| DR. P. OCAMPO COLLEGES                                                                | Private       |                15 |            36 |        43.7 |       13.5 |       71.5 |      60 |    46.7 |             40 |              33.3 |
| PALAWAN STATE UNIVERSITY PUERTO PRINCESA CITY                                         | Public        |                15 |            15 |        24.2 |          9 |         33 |    33.3 |      20 |            6.7 |               6.7 |
| GORDON COLLEGE                                                                        | Public        |                15 |            46 |        48.9 |         25 |       79.5 |    71.4 |    57.1 |           46.7 |                40 |
| NORTH VALLEY COLLEGE FOUNDATION                                                       | Private       |                15 |            40 |        44.3 |       27.5 |       48.5 |    66.7 |    53.3 |           46.7 |              28.6 |
| NARESUAN UNIVERSITY                                                                   | Foreign       |                15 |          55.5 |        54.3 |       29.2 |       83.8 |    71.4 |    64.3 |             80 |              46.2 |
| MANILA ADVENTIST MEDICAL CENTER - PASAY CITY                                          | Private       |                15 |            40 |        50.6 |       35.5 |         75 |    86.7 |    66.7 |           93.3 |              33.3 |
| LYCEUM OF THE PHILIPPINES - CAVITE                                                    | Private       |                15 |            53 |        40.7 |       13.5 |         61 |      60 |    53.3 |           33.3 |               nan |
| UNIVERSITY OF FLORIDA                                                                 | Foreign       |                15 |            73 |        65.5 |       54.5 |         87 |    86.7 |      80 |           66.7 |              16.7 |
| LYCEUM OF THE PHILIPPINES                                                             | Private       |                14 |            46 |        43.9 |       32.8 |         53 |    78.6 |    64.3 |           71.4 |                50 |
| URDANETA CITY UNIVERSITY                                                              | Public        |                14 |          52.5 |        50.5 |         30 |       71.2 |    71.4 |    64.3 |           85.7 |                60 |
| MONAD UNIVERSITY                                                                      | Foreign       |                14 |            55 |        50.6 |       16.5 |         77 |    64.3 |    57.1 |           42.9 |               nan |
| ILOCOS SUR COMMUNITY COLLEGE - BANTAY ILOCOS SUR                                      | Public        |                14 |            27 |        31.3 |       15.2 |       35.8 |      50 |    21.4 |           71.4 |              42.9 |
| LYCEUM OF ILIGAN FOUNDATION                                                           | Private       |                14 |          72.5 |          62 |       39.2 |         90 |    78.6 |    71.4 |           57.1 |              55.6 |
| NOTRE DAME OF TACURONG COLLEGE                                                        | Private       |                14 |            28 |        33.4 |       10.5 |         44 |    42.9 |    35.7 |           71.4 |                25 |
| BICOL UNIVERSITY COLLEGE OF NURSING LEGAZPI CITY                                      | Public        |                14 |          53.5 |        54.6 |       35.2 |       73.8 |    85.7 |    71.4 |           71.4 |                50 |
| ST. PAUL UNIVERSITY SURIGAO                                                           | Private       |                14 |            45 |        42.1 |       12.5 |         74 |    61.5 |    53.8 |           57.1 |              42.9 |
| AKLAN STATE UNIVERSITY - MAIN                                                         | Public        |                14 |            48 |        47.5 |       22.5 |       71.5 |    71.4 |    57.1 |           57.1 |                25 |
| SOUTHEAST ASIAN COLLEGE INC.-QUEZON CITY                                              | Private       |                14 |            20 |        20.7 |        9.2 |         29 |    28.6 |    14.3 |           64.3 |              14.3 |
| SAINT TONIS COLLEGE                                                                   | Private       |                14 |            33 |        41.6 |         21 |         64 |    64.3 |    42.9 |           71.4 |                25 |
| CALAMBA DOCTORS' COLLEGE                                                              | Private       |                14 |          35.5 |        35.8 |       10.2 |       58.8 |    58.3 |    41.7 |           57.1 |                70 |
| CENTRAL COLLEGES OF THE PHILIPPINES                                                   | Private       |                13 |          51.5 |        49.8 |       35.8 |       72.2 |      75 |      75 |           53.8 |                25 |
| DE LA SALLE - ARANETA UNIVERSITY                                                      | Private       |                13 |            32 |        37.9 |          9 |         62 |    53.8 |    46.2 |           30.8 |              42.9 |
| 13100A                                                                                | Not Specified |                13 |            52 |        50.3 |         29 |         74 |    69.2 |    69.2 |           92.3 |              38.5 |
| ST. FERDINAND COLLEGE - ILAGAN                                                        | Private       |                13 |            37 |        46.8 |         31 |         61 |    76.9 |    46.2 |           61.5 |                25 |
| BICOL UNIVERSITY - DARAGA                                                             | Public        |                13 |            34 |        31.5 |          9 |         43 |    53.8 |    38.5 |           30.8 |                 0 |
| COLEGIO DE SAN LORENZO RUIZ DE MANILA OF NORTHERN SAMAR                               | Private       |                13 |            55 |        47.5 |         28 |         58 |    69.2 |    69.2 |           69.2 |              57.1 |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                     | Public        |                13 |            58 |        52.8 |         21 |         83 |    69.2 |    61.5 |           61.5 |              11.1 |
| UNIVERSITY OF BOHOL TAGBILARAN CITY                                                   | Private       |                13 |            40 |        40.5 |          9 |         69 |    61.5 |    53.8 |           76.9 |              69.2 |
| SAINT GABRIEL COLLEGE                                                                 | Private       |                13 |            32 |          39 |         11 |         51 |    53.8 |    38.5 |           53.8 |              22.2 |
| UNIVERSITY OF SAINT ANTHONY                                                           | Private       |                13 |            39 |        41.2 |         31 |         52 |    83.3 |      50 |           46.2 |              28.6 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - GMA                                             | Private       |                13 |            18 |        27.2 |         10 |         43 |      50 |    41.7 |           76.9 |              18.2 |
| WESTERN LEYTE COLLEGE OF ORMOC CITY                                                   | Private       |                13 |            48 |        45.8 |         14 |         76 |    53.8 |    53.8 |           69.2 |               100 |
| LYCEUM OF APARRI                                                                      | Private       |                13 |            35 |        43.4 |         28 |         45 |    61.5 |    38.5 |           46.2 |                25 |
| NOTRE DAME OF MIDSAYAP COLLEGE                                                        | Private       |                13 |            58 |        43.9 |       13.2 |       69.5 |    63.6 |    63.6 |           53.8 |              66.7 |
| University For Development Studies                                                    | Not Specified |                13 |            37 |        42.8 |          2 |         68 |    53.8 |    46.2 |           53.8 |                40 |
| HOLY CROSS OF DAVAO COLLEGE                                                           | Private       |                13 |            33 |        40.8 |          8 |         69 |    53.8 |    46.2 |           38.5 |                40 |
| DOMINICAN COLLEGE                                                                     | Private       |                13 |            27 |        39.6 |       19.5 |         59 |    45.5 |    45.5 |           53.8 |                40 |
| UNCIANO COLLEGES                                                                      | Private       |                12 |            32 |        44.5 |         20 |         69 |    54.5 |    54.5 |             75 |              33.3 |
| SACRED HEART COLLEGE LUCENA CITY                                                      | Private       |                12 |            39 |        47.8 |       26.8 |       64.8 |    58.3 |      50 |           33.3 |                50 |
| FIRST ASIA INSTITUTE OF TECHNOLOGY AND HUMANITIES                                     | Private       |                12 |            48 |        52.3 |         39 |         68 |    91.7 |      75 |           66.7 |                40 |
| UNIVERSITY OF CALIFORNIA SANTA BARBARA                                                | Foreign       |                12 |          47.5 |        49.1 |       33.2 |       66.2 |      75 |    58.3 |             25 |              22.2 |
| UNCIANO COLLEGES AND GENERAL HOSPITAL                                                 | Private       |                12 |            50 |        49.5 |       24.2 |         71 |      70 |      60 |             50 |              33.3 |
| UNIVERSITY OF ILOILO                                                                  | Private       |                12 |          60.5 |          59 |       41.2 |       90.8 |      75 |      75 |           58.3 |              66.7 |
| UNIVERSITY OF PERPETUAL HELP - CALAMBA LAGUNA                                         | Private       |                12 |            35 |          37 |         16 |       53.2 |    66.7 |    41.7 |           66.7 |              41.7 |
| UNIVERSITY OF NEVADA LAS VEGAS                                                        | Foreign       |                12 |            67 |        61.7 |       46.2 |         85 |    83.3 |      75 |           33.3 |              11.1 |
| MEDINA COLLEGE - IPIL                                                                 | Private       |                12 |            42 |        43.3 |       13.8 |         69 |    54.5 |    54.5 |           58.3 |              33.3 |
| SOUTHEAST ASIAN COLLEGE INC.-ESPANA MANILA                                            | Private       |                12 |             8 |         9.9 |        4.5 |         14 |       0 |       0 |           33.3 |              16.7 |
| AMA COMPUTER COLLEGE                                                                  | Private       |                12 |            19 |          24 |          5 |       32.2 |    33.3 |    16.7 |           16.7 |               8.3 |
| UNIVERSITY OF THE PHILIPPINES - PAMPANGA                                              | Public        |                12 |          61.5 |        56.7 |         44 |         67 |    91.7 |    91.7 |           16.7 |              33.3 |
| SRINAKHARINWIROT UNIVERSITY                                                           | Foreign       |                12 |            35 |        38.8 |       24.2 |       54.8 |    72.7 |    45.5 |           41.7 |                10 |
| PHILIPPINE REHABILITATION INSTITUTE                                                   | Private       |                12 |            34 |        35.3 |       16.5 |         54 |      50 |      50 |             50 |                50 |
| DR. YANGA'S COLLEGES                                                                  | Private       |                12 |            44 |          46 |       30.5 |         56 |    81.8 |    54.5 |           33.3 |              33.3 |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE NEGROS OCCIDENTAL                                | Private       |                12 |            50 |        45.2 |       23.5 |         59 |    66.7 |    58.3 |             50 |              66.7 |
| BICOL UNIVERSITY - POLANGUI                                                           | Public        |                12 |            51 |        55.7 |       39.2 |         65 |    91.7 |      75 |           66.7 |                50 |
| MEDINA COLLEGE OZAMIS MISAMIS ORIENTAL                                                | Private       |                11 |            15 |        23.2 |        7.5 |         36 |    27.3 |    27.3 |           54.5 |              27.3 |
| MARIANO MARCOS STATE UNIVERSITY - COLLEGE OF EDUCATION - LAOAG CITY                   | Public        |                11 |            45 |        48.6 |         20 |         75 |    63.6 |    54.5 |           81.8 |                20 |
| LAGUNA COLLEGE                                                                        | Private       |                11 |            50 |        51.4 |       38.5 |         62 |    90.9 |    63.6 |           72.7 |                 0 |
| VIRGEN MILAGROSA EDUCATIONAL INSTITUTE SAN CARLOS CITY                                | Private       |                11 |            38 |        42.5 |       33.5 |       57.5 |    81.8 |    45.5 |           27.3 |               9.1 |
| NORTHERN CHRISTIAN COLLEGE                                                            | Private       |                11 |            57 |        52.5 |         18 |       92.5 |    54.5 |    54.5 |           36.4 |              37.5 |
| NORTHERN NEGROS STATE COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                        | Public        |                11 |            61 |        56.5 |         28 |       89.5 |    72.7 |    63.6 |           45.5 |              66.7 |
| UNIVERSITY OF CORDILLERAS                                                             | Private       |                11 |            37 |        43.4 |       23.5 |         69 |    54.5 |    45.5 |           72.7 |              45.5 |
| MABINI COLLEGES                                                                       | Private       |                11 |            55 |        51.8 |         18 |       81.5 |    63.6 |    54.5 |           63.6 |                50 |
| KIDAPAWAN DOCTORS COLLEGE INC.                                                        | Private       |                11 |            29 |        45.4 |       26.5 |       63.5 |    45.5 |    45.5 |           45.5 |               nan |
| NOTRE DAME OF JOLO COLLEGE - JOLO SULU                                                | Private       |                11 |            11 |        16.5 |        6.5 |       21.5 |    18.2 |    18.2 |           63.6 |              18.2 |
| NOTRE DAME OF MARBEL UNIV.                                                            | Private       |                11 |            42 |        44.8 |       30.5 |         65 |    72.7 |    54.5 |           36.4 |              45.5 |
| UNIVERSITY OF PERPETUAL HELP - RIZAL                                                  | Private       |                11 |            29 |        38.5 |        6.5 |       68.5 |    45.5 |    45.5 |           54.5 |              36.4 |
| HUACHIEW CHALERMPRAKIET UNIVERSITY                                                    | Foreign       |                11 |            36 |        47.2 |         26 |       61.5 |    54.5 |    45.5 |           54.5 |              37.5 |
| FELLOWSHIP BAPTIST COLLEGE                                                            | Private       |                11 |            69 |        57.8 |         41 |       81.5 |    81.8 |    72.7 |           36.4 |              66.7 |
| FOUNDATION UNIVERSITY                                                                 | Private       |                11 |            48 |        50.4 |       34.5 |         78 |      90 |      70 |           36.4 |                 0 |
| UNIVERSITY OF SAN FRANCISCO                                                           | Foreign       |                11 |            75 |        69.7 |         56 |       87.5 |     100 |    81.8 |           36.4 |              33.3 |
| CORDILLERA CAREER DEVELOPMENT COLLEGE                                                 | Private       |                11 |            60 |        59.1 |         45 |         73 |    90.9 |    90.9 |           63.6 |              57.1 |
| RUTGERS UNIVERSITY NEW JERSEY                                                         | Foreign       |                11 |            72 |        73.5 |         62 |       85.5 |     100 |     100 |              0 |              27.3 |
| RUTGERS UNIVERSITY                                                                    | Foreign       |                11 |            78 |        67.1 |       55.5 |       88.5 |    90.9 |    81.8 |           54.5 |              57.1 |
| OLIVAREZ COLLEGE SUCAT PARA$AQUE                                                      | Private       |                11 |            27 |        30.5 |       11.5 |         43 |    45.5 |    27.3 |           54.5 |              18.2 |
| SIENA COLLEGE OF TAYTAY                                                               | Private       |                11 |            62 |        49.5 |       24.5 |         71 |      80 |      70 |           45.5 |                25 |
| COLLEGE OF HOLY SPIRIT-MANILA                                                         | Private       |                11 |            18 |        23.2 |          5 |       37.5 |    45.5 |    27.3 |           36.4 |              63.6 |
| BRENT HOSPITAL AND COLLEGES INC. ZAMBOANGA CITY                                       | Private       |                11 |            10 |        12.9 |          8 |       14.5 |     9.1 |       0 |           63.6 |              18.2 |
| BROKENSHIRE COLLEGE SOCSKSARGEN                                                       | Private       |                11 |            30 |        44.5 |         14 |       76.5 |    54.5 |    45.5 |           63.6 |              37.5 |
| SULTAN KUDARAT STATE UNIVERSITY - MAIN                                                | Public        |                10 |            34 |        30.8 |        5.5 |       51.8 |      50 |      50 |             60 |                 0 |
| SULTAN KUDARAT STATE UNIVERSITY - TACURONG                                            | Public        |                10 |            24 |        27.1 |        7.5 |         40 |    44.4 |    33.3 |             20 |               nan |
| ST. LUKE'S SCHOOL OF MEDICINE INDIA                                                   | Private       |                10 |          35.5 |        34.6 |       24.5 |       44.8 |      60 |      50 |             10 |                 0 |
| ST. JOSEPH'S COLLEGE QUEZON CITY                                                      | Private       |                10 |            26 |        28.3 |         19 |       36.5 |      40 |      20 |             90 |                20 |
| UNIVERSITAS ADVENT INDONESIA                                                          | Foreign       |                10 |          53.5 |        47.8 |       15.2 |       73.5 |      60 |      60 |             50 |              22.2 |
| POLYTECHNIC COLLEGE OF DAVAO DEL SUR                                                  | Private       |                10 |            64 |        55.6 |         15 |       96.2 |      60 |      50 |             60 |              66.7 |
| MARY HELP OF CHRISTIANS COLLEGE SEMINARY                                              | Private       |                10 |          15.5 |        19.7 |       11.8 |         25 |      20 |      10 |            100 |                50 |
| JOSE RIZAL UNIVERSITY                                                                 | Private       |                10 |          53.5 |        56.5 |       38.5 |         81 |      90 |      70 |             70 |                40 |
| NOTRE DAME OF KIDAPAWAN COLLEGE                                                       | Private       |                10 |          39.5 |        32.8 |         13 |       46.8 |      60 |      50 |             70 |              37.5 |
| UNIVERSITY OF CENTRAL FLORIDA                                                         | Foreign       |                10 |          50.5 |        46.3 |       22.5 |       69.8 |      70 |      60 |             50 |              11.1 |
| UNIVERSITY OF GUAM                                                                    | Foreign       |                10 |            38 |        49.1 |       32.8 |       79.8 |      80 |      50 |             50 |                50 |
| PHILIPPINE NORMAL COLLEGE TAFT AVENUE MANILA                                          | Public        |                10 |            53 |        52.2 |         42 |       68.8 |      80 |      80 |              0 |                40 |
| DR. CARLOS LANTING COLLEGE - NOVALICHES QUEZON CITY                                   | Private       |                10 |          19.5 |        24.3 |        4.2 |       31.8 |      40 |      20 |             70 |                10 |
| COLUMBAN COLLEGE - OLONGAPO CITY                                                      | Private       |                10 |            50 |        54.7 |       36.2 |       79.2 |      80 |      70 |             50 |                75 |
| CAMARINES NORTE STATE COLLEGE - MAIN                                                  | Public        |                10 |          48.5 |        48.4 |       19.8 |       78.2 |      60 |      50 |             70 |                 0 |
| CHRIST THE KING COLLEGE - CALBAYOG CITY                                               | Private       |                10 |          38.5 |        43.8 |       22.2 |       71.5 |      60 |      40 |             80 |              33.3 |
| UNIVERSITY OF THE PHILIPPINES SCH. OF HEALTH SCIENCES -LEYTE                          | Public        |                10 |          23.5 |        24.7 |       16.2 |       27.5 |      20 |      20 |             80 |                70 |
| UNIVERSITY OF RIZAL SYSTEM - MORONG                                                   | Public        |                 9 |            53 |        52.2 |         27 |         79 |    66.7 |    55.6 |           66.7 |                25 |
| NOTRE DAME OF MARBEL COLLEGE SOUTH COTABATO                                           | Private       |                 9 |            38 |        40.7 |         23 |         45 |    66.7 |    44.4 |           55.6 |              44.4 |
| UNIVERSITY OF ILLINOIS CHICAGO                                                        | Foreign       |                 9 |            84 |        75.9 |         75 |         93 |    88.9 |    88.9 |              0 |                 0 |
| Texila American University                                                            | Not Specified |                 9 |            46 |        49.2 |         14 |         79 |    66.7 |    66.7 |           55.6 |              62.5 |
| NUEVA ECIJA UNIVERSITY OF SCIENCE AND TECHNOLOGY - MAIN                               | Public        |                 9 |            62 |        53.2 |         35 |         69 |    77.8 |    66.7 |           44.4 |              33.3 |
| WESTERN VISAYAS COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                              | Public        |                 9 |            68 |        53.4 |         31 |         78 |    77.8 |    66.7 |           33.3 |              28.6 |
| VIRGINIA COMMONWEALTH UNIVERSITY                                                      | Foreign       |                 9 |            77 |        77.7 |         65 |         87 |     100 |     100 |           22.2 |              42.9 |
| SAN SEBASTIAN COLLEGE - RECOLETOS DE CAVITE                                           | Private       |                 9 |            36 |        41.7 |         28 |         42 |    66.7 |    33.3 |           55.6 |               100 |
| SAN SEBASTIAN COLLEGE - RECOLETOS CANLUBANG                                           | Private       |                 9 |          53.5 |        49.5 |       27.5 |       72.8 |      75 |    62.5 |           44.4 |                80 |
| STONY BROOK UNIVERSITY                                                                | Foreign       |                 9 |            59 |        58.3 |         36 |         85 |    77.8 |    66.7 |           11.1 |              28.6 |
| UM TAGUM COLLEGE                                                                      | Private       |                 9 |          63.5 |        56.2 |       28.8 |       80.5 |    62.5 |    62.5 |           66.7 |                 0 |
| PATTS COLLEGE OF AERONAUTICS                                                          | Private       |                 9 |            49 |        55.9 |         24 |         75 |    66.7 |    66.7 |           77.8 |                 0 |
| UNIVERSITY OF CALIFORNIA AT STA. CRUZ U.S.A.                                          | Foreign       |                 9 |            61 |        49.8 |         25 |         69 |    66.7 |    66.7 |              0 |                 0 |
| JOSE RIZAL MEMORIAL STATE UNIVERSITY - MAIN                                           | Public        |                 9 |          19.5 |        31.9 |       13.8 |       41.5 |    37.5 |      25 |           44.4 |              66.7 |
| MINDANAO MEDICAL FOUNDATION COLLEGE DAVAO                                             | Private       |                 9 |            15 |        22.9 |          4 |         40 |    33.3 |    33.3 |           77.8 |              11.1 |
| UNIVERSITY OF HAWAII AT MANOA                                                         | Foreign       |                 9 |            73 |        64.8 |         49 |       83.8 |    87.5 |    87.5 |           55.6 |                40 |
| CHIANG KAI SHEK COLLEGE                                                               | Private       |                 9 |            52 |        55.9 |         33 |         78 |    77.8 |    66.7 |            100 |              62.5 |
| DOMINICAN COLLEGE BLUM SAN JUAN MM                                                    | Private       |                 9 |            25 |          31 |         12 |         36 |    33.3 |    22.2 |           44.4 |              11.1 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                  | Public        |                 9 |            51 |        46.4 |         11 |         68 |    66.7 |    66.7 |           66.7 |                 0 |
| CENTRO ESCOLAR UNIVERSITY-MALOLOS BULACAN                                             | Private       |                 9 |            36 |        30.6 |         22 |         37 |    66.7 |    22.2 |           44.4 |              33.3 |
| BURAPHA UNIVERSITY                                                                    | Foreign       |                 9 |            11 |          16 |          2 |         15 |    11.1 |    11.1 |           88.9 |              14.3 |
| CALIFORNIA STATE UNIVERSITY LONG BEACH                                                | Foreign       |                 9 |            35 |        42.6 |          6 |         82 |    62.5 |      50 |           33.3 |                25 |
| CALIFORNIA STATE UNIVERSITY FRESNO                                                    | Foreign       |                 9 |            28 |        37.2 |          6 |         55 |    44.4 |    33.3 |           55.6 |              16.7 |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - LAGUNA COLLEGE OF ARTS AND TRADES - STA. CRUZ   | Public        |                 9 |            63 |        60.9 |         46 |         76 |    88.9 |    88.9 |           44.4 |               nan |
| KALAYAAN COLLEGE                                                                      | Private       |                 9 |            47 |        44.6 |         18 |         74 |    55.6 |    55.6 |           22.2 |                20 |
| LA SALLE COLLEGE - ANTIPOLO                                                           | Private       |                 9 |            18 |        33.7 |          9 |         41 |    44.4 |    33.3 |           22.2 |              16.7 |
| ISABELA STATE UNIVERSITY - ILAGAN                                                     | Public        |                 9 |            75 |        71.6 |         54 |         89 |     100 |    88.9 |           55.6 |               100 |
| UNIVERSITY OF CEBU - LAPULAPU AND MANDAUE                                             | Private       |                 8 |          55.5 |        62.2 |       43.2 |       88.8 |    87.5 |    87.5 |             50 |                80 |
| THAMMASAT UNIV.                                                                       | Foreign       |                 8 |            23 |        21.4 |          8 |         27 |      25 |    12.5 |           12.5 |                 0 |
| U.P. VISAYAS (TACLOBAN CITY LEYTE)                                                    | Public        |                 8 |          70.5 |        62.6 |       58.5 |       75.8 |    87.5 |    87.5 |              0 |              62.5 |
| PHILIPPINE WOMEN'S COLLEGE OF DAVAO                                                   | Private       |                 8 |            37 |        47.1 |       29.2 |       72.2 |      75 |    37.5 |             25 |               nan |
| PRINCE OF SONGKLA UNIVERSITY                                                          | Foreign       |                 8 |          40.5 |        45.2 |         30 |       62.5 |    87.5 |      50 |           62.5 |                 0 |
| RAMKHAMHAENG UNIVERSITY                                                               | Foreign       |                 8 |          64.5 |        58.5 |       42.5 |       81.8 |      75 |      75 |           37.5 |                50 |
| UNIVERSITY OF BRITISH COLUMBIA                                                        | Foreign       |                 8 |          26.5 |        31.8 |        7.5 |         44 |    37.5 |      25 |           37.5 |                 0 |
| UNIVERSITY OF CALIFORNIA SANTA CRUZ                                                   | Foreign       |                 8 |            74 |          60 |         38 |         86 |      75 |      75 |           37.5 |              33.3 |
| PAMANTASAN NG LUNGSOD NG PASAY                                                        | Public        |                 8 |            31 |        34.5 |       18.2 |         49 |      50 |    37.5 |             25 |                25 |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-ALABANG ZAPOTE                              | Private       |                 8 |          25.5 |        24.1 |       10.8 |       33.5 |      50 |    12.5 |           62.5 |                50 |
| MAPANDI MEMORIAL COLLEGE                                                              | Private       |                 8 |          37.5 |        40.5 |       29.8 |         46 |      75 |      50 |             50 |                 0 |
| UNIVERSITY OF NORTHERN PHILIPPINES VIGAN ILOCOS SUR                                   | Public        |                 8 |            11 |        14.1 |          7 |       20.5 |       0 |       0 |           37.5 |              37.5 |
| ENDERUN COLLEGE                                                                       | Private       |                 8 |          33.5 |        35.2 |         15 |       57.8 |      50 |    37.5 |           62.5 |                20 |
| UNIVERSITY OF TEXAS                                                                   | Foreign       |                 8 |            96 |        79.7 |         60 |         97 |     100 |     100 |           62.5 |                50 |
| FELIPE R. VERALLO MEMORIAL FOUNDATION - BOGO                                          | Private       |                 8 |          78.5 |        67.8 |         60 |         82 |    87.5 |    87.5 |           37.5 |               100 |
| UNIVERSITY OF THE ASSUMPTION PAMPANGA                                                 | Private       |                 8 |            36 |        44.8 |         16 |       80.2 |      50 |      50 |             50 |                25 |
| COLLEGE OF ST. JOHN - ROXAS                                                           | Private       |                 8 |            13 |        25.4 |         11 |         37 |    42.9 |    28.6 |             75 |                 0 |
| DELOS SANTOS COLLEGE                                                                  | Private       |                 8 |          38.5 |        38.5 |       22.8 |       53.8 |    62.5 |      50 |           62.5 |              37.5 |
| SAFFRULLAH M. DIPATUAN FOUNDATION ACADEMY                                             | Private       |                 7 |            63 |        60.6 |       34.5 |       94.5 |    71.4 |    71.4 |           28.6 |                50 |
| ALDERSGATE COLLEGE                                                                    | Private       |                 7 |            51 |        44.7 |        7.5 |         75 |    57.1 |    57.1 |           85.7 |                50 |
| SAN SEBASTIAN COLLEGE                                                                 | Private       |                 7 |            22 |        28.3 |         17 |         38 |    42.9 |    28.6 |           14.3 |              14.3 |
| SAINT MARY'S COLLEGE OF SAN JUAN                                                      | Private       |                 7 |            14 |        30.3 |          4 |       47.5 |    28.6 |    28.6 |           71.4 |              33.3 |
| SAINT LOUIS COLLEGE                                                                   | Private       |                 7 |            19 |        35.4 |         11 |         52 |    42.9 |    42.9 |           42.9 |                 0 |
| THE COLLEGE OF MAASIN                                                                 | Private       |                 7 |            63 |          58 |       27.5 |         94 |    57.1 |    57.1 |           71.4 |                40 |
| SAINT LOUIS COLLEGE - CITY OF SAN FERNANDO                                            | Private       |                 7 |            48 |        40.1 |         18 |       57.5 |    83.3 |    66.7 |           57.1 |              33.3 |
| WEST NEGROS COLLEGE BACOLOD                                                           | Private       |                 7 |            19 |        18.7 |          7 |         28 |    28.6 |       0 |           71.4 |              28.6 |
| ST. JOSEPH COLLEGE CAVITE                                                             | Private       |                 7 |            14 |        24.6 |          6 |       46.5 |    42.9 |    42.9 |           28.6 |              28.6 |
| University Of Port Harcourt                                                           | Not Specified |                 7 |            41 |        55.7 |         30 |         91 |    71.4 |    57.1 |           28.6 |                 0 |
| COLLEGE OF THE IMMACULATE CONCEPTION                                                  | Private       |                 7 |            43 |        37.1 |       11.5 |       47.5 |    57.1 |    57.1 |           42.9 |                40 |
| COTABATO MEDICAL FOUNDATION COLLEGE                                                   | Private       |                 7 |            59 |        48.9 |       19.5 |       71.5 |    57.1 |    57.1 |           42.9 |                25 |
| 13155D                                                                                | Not Specified |                 7 |            70 |        51.9 |         21 |         79 |    57.1 |    57.1 |           28.6 |              42.9 |
| CATANDUANES STATE COLLEGE                                                             | Public        |                 7 |             9 |        29.1 |        6.5 |       45.5 |    28.6 |    28.6 |           42.9 |              71.4 |
| NORTHEASTERN COLLEGE                                                                  | Private       |                 7 |          50.5 |        48.5 |       26.8 |       66.8 |    66.7 |    66.7 |           57.1 |                50 |
| MALASIQUI AGNO VALLEY COLLEGE - MALASIQUI PANGASINAN                                  | Private       |                 7 |             9 |        22.6 |        7.5 |         27 |    28.6 |    14.3 |           57.1 |                 0 |
| MINDANAO UNIVERSITY OF SCIENCE AND TECHNOLOGY                                         | Public        |                 7 |            52 |        52.3 |       34.5 |       70.5 |    71.4 |    71.4 |           14.3 |               100 |
| UNIVERSITY OF LUZON ( DAGUPAN CITY )                                                  | Private       |                 7 |            25 |        20.1 |        5.5 |         32 |    28.6 |    14.3 |           57.1 |              71.4 |
| LA CONSOLACION COLLEGE - DAET                                                         | Private       |                 7 |            63 |          60 |       34.5 |         89 |    71.4 |    71.4 |           57.1 |               100 |
| HOLY TRINITY COLLEGE PUERTO PRINCESA                                                  | Private       |                 7 |            21 |          34 |       16.5 |       54.5 |    42.9 |    42.9 |            100 |              42.9 |
| DR. JOSE FABELLA MEMORIAL HOSPITAL SCHOOL OF MIDWIFERY                                | Private       |                 7 |            77 |        63.7 |       38.5 |         87 |    85.7 |    71.4 |           42.9 |               nan |
| INTERNATIONAL COLLEGES OF ASIA - TAMBAC PANGASINAN                                    | Private       |                 7 |            26 |        36.1 |         24 |       46.5 |    28.6 |    28.6 |           71.4 |              42.9 |
| KHON KAEN UNIVERSITY                                                                  | Foreign       |                 7 |            41 |        40.6 |         12 |       59.5 |    57.1 |    57.1 |           14.3 |                 0 |
| NAVAL STATE UNIVERSITY - MAIN                                                         | Public        |                 7 |            77 |          60 |         32 |         84 |    85.7 |    57.1 |           14.3 |                 0 |
| UNIVERSITY OF IMMACULATE CONCEPTION-DAVAO CITY                                        | Private       |                 7 |            21 |        18.1 |       10.5 |       26.5 |    28.6 |       0 |            100 |              14.3 |
| PANPACIFIC UNIVERSITY NORTH PHILIPPINES - URDANETA CITY                               | Private       |                 7 |            48 |        45.6 |         23 |         70 |    71.4 |    57.1 |           57.1 |                50 |
| NEGROS ORIENTAL STATE UNIVERSITY                                                      | Public        |                 7 |            13 |        16.7 |        7.5 |         25 |    28.6 |       0 |              0 |              57.1 |
| UNIVERSITY OF CALIFORNIA MERCED                                                       | Foreign       |                 7 |            48 |        46.1 |       36.5 |         61 |    71.4 |    71.4 |           42.9 |              33.3 |
| OLIVAREZ COLLEGE - TAGAYTAY                                                           | Private       |                 7 |            46 |        52.9 |       24.5 |         83 |    57.1 |    57.1 |           71.4 |                40 |
| ST. BERNADETTE OF LOURDES COLLEGE                                                     | Private       |                 6 |          55.5 |        43.8 |       21.8 |       64.5 |    66.7 |    66.7 |            100 |                50 |
| ASSUMPTION UNIVERSITY                                                                 | Foreign       |                 6 |          33.5 |        36.7 |       24.5 |       38.8 |      80 |      40 |             50 |                 0 |
| ASIA-PACIFIC INTERNATIONAL UNIVERSITY                                                 | Private       |                 6 |          54.5 |        46.2 |         34 |       63.8 |     100 |      80 |             50 |                25 |
| BATAAN PENINSULA STATE UNIVERSITY                                                     | Public        |                 6 |            18 |          28 |        8.5 |       30.5 |    33.3 |    16.7 |           66.7 |              16.7 |
| BICOL COLLEGE                                                                         | Private       |                 6 |          53.5 |        51.7 |       48.5 |       66.8 |    83.3 |    83.3 |           16.7 |              33.3 |
| ARRIESGADO COLLEGE FOUNDATION                                                         | Private       |                 6 |          50.5 |        47.7 |         31 |         70 |    66.7 |    66.7 |            100 |                50 |
| Adventist University Of Indonesia                                                     | Not Specified |                 6 |          59.5 |        54.7 |       40.8 |         73 |    83.3 |    66.7 |           33.3 |                60 |
| COLEGIO DE SAN LORENZO                                                                | Private       |                 6 |            80 |        71.2 |         77 |         86 |    83.3 |    83.3 |             50 |                50 |
| COLEGIO DE KIDAPAWAN                                                                  | Private       |                 6 |            62 |          58 |         43 |         81 |    83.3 |    83.3 |           33.3 |              66.7 |
| CHIANGMAI UNIVERSITY                                                                  | Foreign       |                 6 |            53 |          57 |       26.8 |       88.2 |    66.7 |      50 |             50 |                25 |
| UNIVERSITY OF SOUTH FLORIDA USA                                                       | Foreign       |                 6 |            53 |        51.3 |       30.5 |       66.5 |    66.7 |    66.7 |             50 |                 0 |
| EAST AFRICA UNIVERSITY                                                                | Foreign       |                 6 |          78.5 |        64.2 |         57 |         85 |    83.3 |    83.3 |           33.3 |                 0 |
| DAVAO CENTRAL COLLEGE                                                                 | Private       |                 6 |          39.5 |        41.3 |       14.2 |       67.8 |      80 |      60 |           66.7 |                20 |
| CALIFORNIA STATE UNIVERSITY - FULLERTON                                               | Foreign       |                 6 |          75.5 |        68.3 |       73.2 |         77 |    83.3 |    83.3 |           33.3 |                 0 |
| COR JESU COLLEGE                                                                      | Private       |                 6 |            53 |        54.2 |       41.5 |         75 |    83.3 |    66.7 |           66.7 |               nan |
| EASTERN SAMAR STATE UNIVERSITY - MAIN                                                 | Public        |                 6 |          56.5 |        58.2 |       51.5 |       79.5 |    83.3 |    83.3 |           33.3 |               100 |
| CONCORDIA COLLEGE                                                                     | Private       |                 6 |            44 |        37.5 |       22.5 |       47.5 |    66.7 |    66.7 |           66.7 |                20 |
| UNIVERSITY OF MARYLAND - MARYLAND U.S.A.                                              | Foreign       |                 6 |          55.5 |        58.3 |       35.8 |       84.2 |    83.3 |    66.7 |           33.3 |              16.7 |
| SAN ISIDRO COLLEGE                                                                    | Private       |                 6 |          33.5 |        36.5 |       16.2 |       43.2 |    66.7 |    33.3 |             50 |               nan |
| ST. ANTHONY COLLEGE OF ROXAS CITY CAPIZ                                               | Private       |                 6 |            19 |        26.8 |         10 |       29.5 |    33.3 |    16.7 |           33.3 |              33.3 |
| ST. JOSEPH COLLEGE AMAYA                                                              | Private       |                 6 |          79.5 |        68.2 |         64 |       88.2 |    83.3 |    83.3 |           66.7 |               100 |
| AMA COMPUTER COLLEGE - TUGUEGARAO CITY                                                | Private       |                 6 |            49 |        54.5 |       38.2 |       63.5 |    83.3 |    66.7 |           16.7 |                 0 |
| AGO MEDICAL EDUCATIONAL FOUNDATION LEGASPI CITY                                       | Private       |                 6 |            31 |        31.8 |       17.5 |       44.5 |      50 |    33.3 |              0 |              66.7 |
| ANGELES SYSTEMS PLUS COMPUTER COLLEGE                                                 | Private       |                 6 |            40 |        43.5 |       27.5 |       47.2 |    66.7 |      50 |           33.3 |                 0 |
| ST. MARY'S UNIVERSITY NUEVA VIZCAYA                                                   | Private       |                 6 |          24.5 |        30.7 |       13.5 |       43.8 |      50 |    33.3 |             50 |              16.7 |
| SOUTHERN LUZON POLYTECHNIC COLLEGE - LUCBAN QUEZON                                    | Private       |                 6 |            28 |        24.5 |         14 |         33 |      50 |       0 |             50 |              33.3 |
| SAN DIEGO STATE UNIVERSITY - CALIFORNIA U.S.A.                                        | Foreign       |                 6 |            52 |        48.7 |       36.8 |       64.2 |    83.3 |    66.7 |             50 |              16.7 |
| THE NATIONAL TEACHERS COLLEGE                                                         | Private       |                 6 |            68 |          58 |       30.2 |       86.2 |    66.7 |    66.7 |           66.7 |               nan |
| PAMANTASAN NG LUNGSOD NG MUNTINLUPA                                                   | Public        |                 6 |          50.5 |        49.5 |       30.5 |       67.5 |    66.7 |    66.7 |             50 |               100 |
| RUNGSIT UNIVERSITY                                                                    | Foreign       |                 6 |          44.5 |        45.5 |          3 |         89 |      60 |      60 |           33.3 |              16.7 |
| UNIVERSITY AT BUFFALO                                                                 | Foreign       |                 6 |            47 |        48.8 |         34 |         69 |      80 |      60 |             50 |                 0 |
| Qiqihar Medical University                                                            | Not Specified |                 6 |            14 |        17.3 |        4.2 |       19.2 |    16.7 |    16.7 |            100 |              16.7 |
| LADOKE AKINTOLA UNIVERSITY OF TECHNOLOGY OGBOMOSO                                     | Foreign       |                 6 |            21 |        28.8 |        7.5 |         45 |    33.3 |    33.3 |             50 |                 0 |
| LEYTE NORMAL UNIVERSITY TACLOBAN CITY                                                 | Public        |                 6 |            16 |        23.2 |          6 |       39.5 |    33.3 |    33.3 |              0 |              33.3 |
| MAHARDIKA INSTITUTE OF TECHNOLOGY                                                     | Private       |                 6 |            58 |        50.5 |       32.5 |       69.2 |    66.7 |    66.7 |           33.3 |                 0 |
| KESTER GRANT COLLEGE PHILS. INC.                                                      | Private       |                 6 |            12 |        15.8 |         11 |         19 |    16.7 |       0 |             50 |              33.3 |
| NOVAGEN COLLEGE OF QUEZON CITY                                                        | Private       |                 6 |            14 |        26.7 |        2.8 |       47.8 |    33.3 |    33.3 |           16.7 |                 0 |
| UNIVERSITY OF HOUSTON                                                                 | Foreign       |                 6 |            50 |        46.5 |         15 |       76.8 |    66.7 |      50 |           66.7 |               100 |
| PHILIPPINE NORMAL UNIVERSITY - AGUSAN                                                 | Public        |                 6 |            39 |        44.8 |       28.2 |       55.8 |    66.7 |      50 |           33.3 |                 0 |
| OUR LADY OF FATIMA NOVALICHES                                                         | Private       |                 6 |          18.5 |        28.8 |       12.8 |       44.5 |    33.3 |    33.3 |           33.3 |                50 |
| OUR LADY OF THE PILLAR COLLEGE - CAUAYAN                                              | Private       |                 6 |          20.5 |        29.2 |        5.2 |       43.2 |    33.3 |    33.3 |             50 |              66.7 |
| Christian University Of Thailand                                                      | Not Specified |                 6 |            32 |        26.2 |         18 |         36 |      75 |      25 |             50 |              33.3 |
| LYCEUM NORTHWESTERN - FLORENCIA T. DUQUE COLLEGE                                      | Private       |                 6 |          17.5 |        21.2 |       13.5 |         29 |    33.3 |    16.7 |           66.7 |                 0 |
| MAHASARAKHAM UNIVERSITY                                                               | Foreign       |                 6 |            24 |        21.2 |       16.5 |       29.2 |    33.3 |       0 |           33.3 |                 0 |
| KASETSART UNIVERSITY                                                                  | Foreign       |                 6 |            15 |        36.2 |         15 |         57 |      40 |      40 |           66.7 |                25 |
| RAMKHAMHAENG UNIV.                                                                    | Foreign       |                 5 |             2 |         3.6 |          1 |          7 |       0 |       0 |              0 |                 0 |
| SRI CHAITANYA JUNIOR COLLEGE                                                          | Foreign       |                 5 |            59 |        51.8 |         38 |         77 |      80 |      60 |             20 |               nan |
| SUNRISE UNIVERSITY                                                                    | Foreign       |                 5 |            40 |        41.6 |         35 |         52 |      80 |      60 |             40 |               nan |
| Sti - College Davao                                                                   | Not Specified |                 5 |            15 |        22.2 |          8 |         41 |      40 |      40 |            100 |                40 |
| AMA SCHOOL OF MEDICINE - EAST RIZAL                                                   | Private       |                 5 |            38 |        46.8 |          6 |         91 |      60 |      40 |             60 |                25 |
| SAINT PAUL COLLEGE FOUNDATION                                                         | Private       |                 5 |            54 |        51.2 |         54 |         54 |      80 |      80 |             60 |               100 |
| SAINT MICHAEL'S COLLEGE OF LAGUNA                                                     | Private       |                 5 |            58 |          60 |         49 |         85 |      80 |      80 |             40 |                25 |
| UNIV. OF ASIA AND THE PACIFIC - PASIG CITY                                            | Private       |                 5 |            81 |        64.6 |         36 |         82 |      80 |      60 |             60 |                40 |
| RUTGERS COLLEGE NEW JERSEY                                                            | Foreign       |                 5 |            90 |        85.6 |         86 |         92 |     100 |     100 |              0 |                40 |
| TEMPLE UNIVERSITY USA                                                                 | Foreign       |                 5 |            69 |        60.6 |         56 |         78 |      80 |      80 |             20 |                40 |
| SIAM UNIVERSITY                                                                       | Foreign       |                 5 |             8 |        32.8 |          6 |         59 |      40 |      40 |             20 |                 0 |
| TRACE COLLEGE                                                                         | Private       |                 5 |            73 |        54.4 |         24 |         76 |      60 |      60 |             80 |                50 |
| TECHNOLOGICAL UNIVERSITY OF THE PHILIPPINES - AYALA BLVD. MANILA                      | Public        |                 5 |          44.5 |        38.5 |       32.2 |       50.8 |      75 |      75 |             40 |               nan |
| SIENA COLLEGE-TAYTAY                                                                  | Private       |                 5 |            31 |        37.4 |         16 |         47 |      60 |      40 |             60 |                40 |
| ADVENTIST INDONESIA UNIVERSITY INDONESIA                                              | Foreign       |                 5 |            17 |        13.2 |          7 |         17 |       0 |       0 |              0 |                 0 |
| AKLAN POLYTECHNIC COLLEGE                                                             | Private       |                 5 |            54 |          49 |         11 |         87 |      60 |      60 |             40 |                50 |
| ST. ANDREW'S INTERNATIONAL ACADEMY INDIA                                              | Foreign       |                 5 |             9 |        17.8 |          7 |         21 |      20 |      20 |             20 |                 0 |
| PALAWAN POLYTECHNIC COLLEGE                                                           | Private       |                 5 |            65 |        56.8 |         60 |         70 |      80 |      80 |             40 |                 0 |
| UNIVERSITY OF CONNECTICUT                                                             | Foreign       |                 5 |            48 |          56 |         46 |         79 |      80 |      80 |             40 |                50 |
| NEW SINAI SCHOOL AND COLLEGES STA. ROSA                                               | Private       |                 5 |          34.5 |          36 |       28.5 |         42 |      75 |      25 |             20 |               nan |
| LIPA CITY COLLEGES BATANGAS                                                           | Private       |                 5 |            26 |        31.2 |         15 |         34 |      40 |      20 |            100 |                20 |
| LUNA GOCO COLLEGES                                                                    | Private       |                 5 |            69 |        55.6 |         32 |         80 |      80 |      60 |              0 |               nan |
| NEW YORK UNIVERSITY NY USA                                                            | Foreign       |                 5 |            88 |        87.2 |         84 |         93 |     100 |     100 |             20 |                40 |
| MOGADISHU UNIVERSITY                                                                  | Foreign       |                 5 |            55 |        45.6 |         37 |         61 |      80 |      60 |             60 |               nan |
| UNIVERSITY OF NEW ENGLAND                                                             | Foreign       |                 5 |            44 |        41.4 |         14 |         52 |      60 |      60 |             60 |                 0 |
| UNIVERSITY OF NEVADA - RENO                                                           | Foreign       |                 5 |            41 |        48.8 |         23 |       66.8 |      50 |      50 |             20 |                50 |
| UNIVERSITY OF MICHIGAN                                                                | Foreign       |                 5 |            77 |        70.4 |         68 |         78 |     100 |     100 |             20 |                 0 |
| UNIVERSITY OF NORTHERN PHILIPPINES-CANDON - CITY OF CANDON ILOCOS SUR                 | Public        |                 5 |            16 |        21.8 |          5 |         18 |      25 |      25 |             60 |                 0 |
| UNIVERSITY OF CEBU                                                                    | Private       |                 5 |            60 |          56 |         42 |         72 |    66.7 |    66.7 |             40 |              33.3 |
| UNIVERSITY OF CALOOCAN CITY                                                           | Public        |                 5 |            33 |        51.8 |         30 |         81 |      80 |      40 |             40 |                25 |
| PENSACOLA CHRISTIAN COLLEGE                                                           | Foreign       |                 5 |            34 |          51 |         17 |         95 |      60 |      40 |             80 |               100 |
| UNIVERSITY OF BRITISH COLUMBIA CANADA                                                 | Foreign       |                 5 |            96 |          89 |         94 |         99 |     100 |     100 |              0 |                20 |
| PAMPANGA AGRICULTURAL COLLEGE                                                         | Public        |                 5 |          20.5 |        23.2 |        8.5 |       35.2 |      50 |      25 |             20 |                 0 |
| KHON KAEN UNIVERSITY THAILAND                                                         | Foreign       |                 5 |            20 |        19.6 |         19 |         27 |      20 |       0 |             60 |                 0 |
| FEU - FERN COLLEGE                                                                    | Private       |                 5 |            40 |          42 |         14 |         68 |      60 |      60 |             40 |                50 |
| DR. DOMINGO B. TAMONDONG MEMORIAL SCHOOL                                              | Private       |                 5 |            37 |        49.4 |         28 |         74 |      60 |      40 |             80 |              33.3 |
| UNIVERSITY OF THE IMMACULATE CONCEPTION COLLEGE DAVAO                                 | Private       |                 5 |             5 |        18.4 |          3 |          7 |      20 |      20 |             60 |                20 |
| UNIVERSITY OF TEXAS AT ARLINGTON                                                      | Foreign       |                 5 |            14 |        33.4 |          5 |         54 |      40 |      40 |              0 |                 0 |
| EULOGIO AMANG RODRIGUEZ INSTITUTE OF SCIENCE AND TECHNOLOGY                           | Public        |                 5 |          60.5 |          53 |       39.8 |       73.8 |      75 |      75 |              0 |               nan |
| KITASATO UNIVERSITY                                                                   | Foreign       |                 5 |            55 |          65 |         52 |         86 |     100 |      80 |             60 |               nan |
| ILOCOS SUR POLYTECHNIC STATE COLLEGE                                                  | Public        |                 5 |            53 |        50.8 |         42 |         61 |      80 |      80 |            100 |                 0 |
| FL VARGAS COLLEGE - TUGUEGARAO                                                        | Private       |                 5 |            22 |        37.4 |         18 |         53 |      40 |      40 |             60 |              33.3 |
| COLEGIO DE SAN JUAN DE LETRAN MANILA                                                  | Private       |                 5 |            41 |        41.8 |         22 |         53 |      60 |      60 |             20 |                60 |
| CHAING MAI UNIVERSITY-THAILAND                                                        | Foreign       |                 5 |            15 |        19.2 |          9 |         23 |      25 |      25 |             60 |                 0 |
| CAVITE STATE UNIVERSITY CAVITE                                                        | Public        |                 5 |            52 |        57.4 |         37 |         76 |      80 |      60 |             20 |                20 |
| CENTRAL COLLEGE OF PANGASINAN - SAN CARLOS CITY PANGASINAN                            | Private       |                 5 |            47 |        54.6 |         38 |         74 |     100 |      60 |             40 |                60 |
| CAGAYAN DE ORO COLLEGE                                                                | Private       |                 5 |            34 |        36.2 |          2 |         66 |      60 |      40 |             40 |              33.3 |
| BATANGAS STATE UNIVERSITY BATANGAS CITY                                               | Public        |                 5 |            45 |          51 |         25 |         63 |      60 |      60 |              0 |                80 |
| ARIZONA STATE UNIVERSITY                                                              | Foreign       |                 5 |            77 |        66.6 |         67 |         81 |      80 |      80 |             60 |               100 |
| ASIAN COLLEGE OF SCIENCE AND TECHNOLOGY - CUBAO                                       | Private       |                 5 |            69 |        67.2 |         46 |         87 |     100 |     100 |             80 |                50 |
| UNIVERSITY OF WISCONSIN-MADISON                                                       | Foreign       |                 5 |            92 |        84.6 |         72 |         99 |     100 |     100 |              0 |              33.3 |
| 13206A                                                                                | Not Specified |                 5 |            54 |        59.8 |         44 |         77 |     100 |     100 |             20 |                20 |

**Table E2. Per-HEI percentile bin distribution (full)**

| UNIVERSITY                                                                            | UNI_TYPE      |     N |   B1 |   B2 |   B3 |   B4 |   B5 |   B6 |   B7 |   B8 |   B9 |   B10 |
|:--------------------------------------------------------------------------------------|:--------------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| UNIVERSITY OF SANTO TOMAS                                                             | Private       | 17567 | 1510 | 1132 | 1212 | 1490 | 1627 | 1791 | 1847 | 2133 | 2295 |  2176 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA                                             | Private       |  4541 |  616 |  464 |  391 |  444 |  403 |  466 |  394 |  408 |  394 |   434 |
| FAR EASTERN UNIVERSITY                                                                | Private       |  4270 |  509 |  436 |  407 |  430 |  486 |  424 |  374 |  370 |  340 |   399 |
| SAN PEDRO COLLEGE                                                                     | Private       |  3649 |  437 |  378 |  327 |  309 |  345 |  368 |  339 |  346 |  323 |   379 |
| UNIVERSITY OF THE PHILIPPINES - MANILA                                                | Public        |  3539 |  225 |  180 |  175 |  162 |  202 |  197 |  227 |  277 |  471 |  1295 |
| SAINT LOUIS UNIVERSITY                                                                | Private       |  3222 |  366 |  263 |  250 |  339 |  303 |  349 |  317 |  289 |  297 |   369 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN                                               | Public        |  3143 |  225 |  169 |  138 |  187 |  195 |  193 |  182 |  260 |  389 |  1120 |
| UNIVERSITY OF NORTHERN PHILIPPINES - MAIN                                             | Public        |  2469 |  370 |  233 |  241 |  238 |  229 |  257 |  210 |  208 |  223 |   195 |
| CEBU DOCTOR'S UNIVERSITY                                                              | Private       |  2404 |  292 |  223 |  217 |  239 |  233 |  224 |  220 |  233 |  204 |   248 |
| DE LA SALLE UNIVERSITY - MANILA                                                       | Private       |  2229 |  175 |  139 |  148 |  149 |  198 |  193 |  257 |  300 |  294 |   332 |
| OUR LADY OF FATIMA UNIVERSITY (FATIMA MEDICAL SCIENCE FOUNDATION) - VALENZUELA        | Private       |  2048 |  277 |  232 |  186 |  201 |  189 |  176 |  172 |  193 |  169 |   201 |
| CENTRO ESCOLAR UNIVERSITY - MANILA                                                    | Private       |  2032 |  245 |  205 |  173 |  210 |  203 |  196 |  166 |  173 |  184 |   218 |
| SOUTHWESTERN UNIVERSITY                                                               | Private       |  1846 |  271 |  183 |  152 |  178 |  165 |  155 |  201 |  160 |  167 |   163 |
| ATENEO DE MANILA UNIVERSITY - QUEZON CITY                                             | Private       |  1786 |  165 |  124 |  108 |  145 |  127 |  148 |  129 |  161 |  230 |   393 |
| VELEZ COLLEGE                                                                         | Private       |  1742 |  194 |  155 |  161 |  162 |  132 |  163 |  172 |  150 |  182 |   215 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS                                                   | Private       |  1732 |  225 |  157 |  126 |  153 |  179 |  154 |  173 |  171 |  154 |   189 |
| DAVAO MEDICAL SCHOOL FOUNDATION                                                       | Private       |  1671 |  224 |  161 |  156 |  173 |  146 |  150 |  154 |  132 |  153 |   177 |
| EMILIO AGUINALDO COLLEGE                                                              | Private       |  1574 |  202 |  185 |  153 |  154 |  158 |  153 |  130 |  132 |  118 |   152 |
| AMA COMPUTER COLLEGE - MAKATI                                                         | Private       |  1521 |  247 |  178 |  152 |  127 |  139 |  146 |  120 |  134 |  125 |   117 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO (CARIG)                                         | Public        |  1394 |  219 |  140 |  113 |  130 |  113 |  129 |  111 |  128 |  131 |   136 |
| ANGELES UNIVERSITY FOUNDATION                                                         | Private       |  1340 |  165 |  140 |  106 |  133 |  142 |  145 |  121 |  118 |  108 |   135 |
| UNIVERSITY OF THE PHILIPPINES - LOS BAÑOS                                             | Public        |  1319 |  151 |  101 |  100 |   96 |  100 |  116 |  136 |  142 |  161 |   173 |
| SILLIMAN UNIVERSITY                                                                   | Private       |  1306 |  140 |  130 |  106 |  114 |  142 |  131 |  126 |  122 |  119 |   141 |
| AGO MEDICAL AND EDUCATIONAL CENTER - BICOL CHRISTIAN COLLEGE OF MEDICINE              | Private       |  1292 |  225 |  147 |  132 |  141 |  122 |  121 |   81 |  108 |   91 |    98 |
| WEST VISAYAS STATE UNIVERSITY - MAIN                                                  | Public        |  1246 |  129 |  100 |   99 |  110 |  110 |  131 |  126 |  110 |  125 |   186 |
| XAVIER UNIVERSITY                                                                     | Private       |  1234 |  151 |  100 |  104 |  117 |  127 |  108 |  124 |  125 |  107 |   139 |
| BROKENSHIRE COLLEGE                                                                   | Private       |  1229 |  190 |  111 |   95 |  115 |  120 |  110 |  105 |  118 |   98 |   118 |
| PAMANTASAN NG LUNGSOD NG MAYNILA                                                      | Public        |  1218 |  116 |   75 |  106 |  114 |  157 |  157 |  133 |  120 |  110 |   104 |
| MINDANAO STATE UNIVERSITY - ILIGAN INSTITUTE OF TECHNOLOGY                            | Public        |  1192 |  131 |  109 |  118 |  119 |  114 |  103 |  111 |  112 |  110 |   136 |
| ATENEO DE ZAMBOANGA UNIVERSITY                                                        | Private       |  1162 |  172 |  131 |  109 |  113 |  107 |  121 |   95 |   96 |   97 |   100 |
| FEU - DR. NICANOR REYES MEDICAL FOUNDATION                                            | Private       |  1154 |  145 |   81 |  101 |  101 |  108 |  121 |  120 |  111 |  109 |   122 |
| LYCEUM NORTHWESTERN UNIVERSITY                                                        | Private       |  1051 |  176 |  113 |   88 |  100 |   98 |   98 |   91 |   77 |   91 |    96 |
| MINDANAO STATE UNIVERSITY - MARAWI                                                    | Public        |  1008 |  121 |   97 |   80 |   77 |  104 |  108 |   96 |   86 |  102 |   116 |
| UNIVERSITY OF SAN AGUSTIN                                                             | Private       |   991 |  112 |  115 |   88 |   92 |  100 |   91 |   74 |   96 |   92 |   100 |
| ATENEO DE DAVAO UNIVERSITY                                                            | Private       |   971 |   83 |   95 |   93 |   86 |  102 |   94 |   93 |   92 |   98 |   117 |
| DE LA SALLE HEALTH SCIENCES INSTITUTE                                                 | Private       |   949 |  100 |   91 |   91 |  110 |   76 |   86 |   96 |   82 |   97 |    94 |
| TRINITY UNIVERSITY OF ASIA                                                            | Private       |   877 |   84 |   73 |   66 |   97 |   74 |   80 |   83 |  113 |  101 |    89 |
| WESTERN MINDANAO STATE UNIVERSITY                                                     | Public        |   861 |  109 |   94 |   55 |   85 |   89 |   86 |   76 |   59 |   82 |   103 |
| MANILA CENTRAL UNIVERSITY                                                             | Private       |   831 |  113 |  105 |   83 |   84 |   82 |   81 |   70 |   67 |   59 |    66 |
| BICOL UNIVERSITY - MAIN                                                               | Public        |   740 |   81 |   72 |   65 |   64 |   65 |   58 |   66 |   86 |   75 |    94 |
| ATENEO DE MANILA UNIVERSITY                                                           | Private       |   721 |    0 |    0 |    1 |    3 |    9 |   19 |   38 |   64 |  232 |   348 |
| CENTRAL PHILIPPINE UNIVERSITY                                                         | Private       |   702 |   71 |   75 |   65 |   63 |   73 |   78 |   60 |   50 |   56 |    89 |
| VIRGEN MILAGROSA UNIVERSITY FOUNDATION AND VMU INSTITUTE OF MEDICAL FOUNDATION        | Private       |   701 |  100 |   67 |   52 |   69 |   73 |   72 |   63 |   62 |   52 |    64 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO                                                | Public        |   696 |   65 |   58 |   50 |   53 |   59 |   60 |   59 |   89 |   69 |   112 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS                                               | Public        |   674 |   92 |   63 |   53 |   57 |   57 |   50 |   67 |   80 |   52 |    86 |
| ADVENTIST UNIVERSITY OF THE PHILIPPINES                                               | Private       |   671 |   83 |   64 |   57 |   52 |   65 |   65 |   68 |   63 |   72 |    67 |
| SAINT PAUL UNIVERSITY PHILIPPINES                                                     | Private       |   661 |   88 |   73 |   49 |   59 |   72 |   72 |   57 |   50 |   56 |    65 |
| UNIVERSITY OF ST. LA SALLE                                                            | Private       |   631 |   61 |   50 |   49 |   60 |   59 |   67 |   64 |   67 |   62 |    83 |
| UNIVERSITY OF THE IMMACULATE CONCEPTION                                               | Private       |   602 |   96 |   54 |   56 |   65 |   58 |   46 |   56 |   51 |   52 |    54 |
| UNIVERSITY OF THE EAST RAMON MAGSAYSAY MEMORIAL MEDICAL CENTER                        | Private       |   555 |   41 |   45 |   50 |   55 |   56 |   57 |   58 |   65 |   57 |    60 |
| UNIVERSITY OF SAN CARLOS                                                              | Private       |   553 |   60 |   51 |   59 |   55 |   41 |   55 |   45 |   55 |   57 |    63 |
| VELEZ COLLEGE CEBU                                                                    | Private       |   546 |   28 |   35 |   53 |   75 |   68 |   68 |   62 |   64 |   54 |    39 |
| SAN BEDA COLLEGE                                                                      | Private       |   537 |   64 |   51 |   62 |   44 |   43 |   54 |   48 |   51 |   55 |    49 |
| NOT SPECIFIED/UNLISTED                                                                | Public        |   503 |   95 |   64 |   56 |   48 |   40 |   49 |   45 |   29 |   36 |    36 |
| SAN PEDRO COLLEGE DAVAO CITY                                                          | Private       |   492 |   68 |   65 |   62 |   70 |   60 |   54 |   43 |   34 |   21 |    14 |
| MANILA TYTANA COLLEGES                                                                | Private       |   485 |   55 |   46 |   47 |   52 |   54 |   44 |   44 |   48 |   38 |    45 |
| CENTRO ESCOLAR UNIVERSITY - MAKATI                                                    | Private       |   472 |   60 |   50 |   29 |   50 |   46 |   45 |   34 |   42 |   49 |    55 |
| ANGELES UNIVERSITY FOUNDATION ANGELES CITY                                            | Private       |   471 |   52 |   71 |   79 |   77 |   59 |   33 |   29 |   35 |   25 |    11 |
| DOÑA REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION                                   | Private       |   467 |   56 |   47 |   43 |   46 |   49 |   39 |   52 |   42 |   45 |    37 |
| DE LA SALLE UNIVERSITY - DASMARIÑAS CAVITE                                            | Private       |   452 |   58 |   58 |   75 |   67 |   62 |   42 |   33 |   28 |   23 |     6 |
| UNIVERSITY OF THE PHILIPPINES - LOS BANOS LAGUNA                                      | Public        |   450 |    0 |    3 |    1 |   10 |   20 |   38 |   62 |   80 |   99 |   134 |
| DAVAO DOCTORS COLLEGE                                                                 | Private       |   442 |   78 |   60 |   46 |   48 |   42 |   32 |   38 |   30 |   30 |    30 |
| LICEO DE CAGAYAN UNIVERSITY                                                           | Private       |   431 |   60 |   65 |   36 |   56 |   44 |   32 |   29 |   38 |   34 |    29 |
| OUR LADY OF FATIMA UNIVERSITY - QUEZON CITY                                           | Private       |   423 |   40 |   60 |   50 |   36 |   41 |   30 |   37 |   35 |   32 |    48 |
| FAR EASTERN UNIVERSITY - NRMF (FAIRVIEW Q.C.)                                         | Private       |   409 |   53 |   58 |   64 |   69 |   55 |   43 |   36 |   18 |    8 |     5 |
| MINDANAO SANITARIUM AND HOSPITAL COLLEGE                                              | Private       |   399 |   55 |   37 |   36 |   34 |   47 |   41 |   32 |   34 |   28 |    41 |
| SAINT LOUIS UNIVERSITY - BAGUIO                                                       | Private       |   374 |   14 |   35 |   51 |   57 |   51 |   49 |   42 |   32 |   28 |    15 |
| CENTRO ESCOLAR UNIVERSITY - MENDIOLA MANILA                                           | Private       |   369 |   72 |   67 |   54 |   47 |   41 |   31 |   28 |   12 |   13 |     3 |
| DE LA SALLE - LIPA                                                                    | Private       |   366 |   54 |   27 |   39 |   43 |   40 |   29 |   24 |   37 |   34 |    34 |
| UNIVERSITY OF THE PHILIPPINES - MINDANAO                                              | Public        |   356 |   27 |   19 |   23 |   29 |   24 |   29 |   45 |   38 |   46 |    66 |
| CEBU NORMAL UNIVERSITY                                                                | Public        |   354 |   20 |   20 |   25 |   29 |   29 |   33 |   52 |   46 |   55 |    38 |
| UNIVERSITY OF THE EAST - MANILA                                                       | Private       |   350 |   47 |   22 |   31 |   33 |   25 |   25 |   37 |   45 |   35 |    41 |
| UNIVERSITY OF BAGUIO                                                                  | Private       |   345 |   43 |   33 |   28 |   38 |   22 |   39 |   27 |   33 |   31 |    48 |
| WEST VISAYAS STATE UNIVERSITY ILOILO                                                  | Public        |   342 |   13 |   26 |   31 |   29 |   44 |   30 |   62 |   43 |   33 |    31 |
| XAVIER UNIVERSITY CAGAYAN DE ORO CITY                                                 | Private       |   339 |   12 |   30 |   28 |   47 |   34 |   58 |   45 |   34 |   26 |    25 |
| CENTRAL MINDANAO UNIVERSITY                                                           | Public        |   328 |   47 |   25 |   28 |   31 |   26 |   32 |   40 |   27 |   31 |    31 |
| MINDANAO STATE UNIVERSITY MARAWI CITY                                                 | Public        |   328 |   32 |   42 |   48 |   49 |   40 |   28 |   31 |   27 |   22 |     9 |
| UNIVERSIDAD DE ZAMBOANGA                                                              | Private       |   325 |   49 |   32 |   29 |   28 |   27 |   27 |   43 |   23 |   32 |    28 |
| MARIANO MARCOS STATE UNIVERSITY - MAIN                                                | Public        |   315 |   40 |   39 |   21 |   25 |   27 |   26 |   35 |   35 |   26 |    35 |
| UNIVERSITY OF THE CORDILLERAS                                                         | Private       |   312 |   55 |   29 |   25 |   25 |   34 |   37 |   21 |   41 |   18 |    20 |
| POLYTECHNIC UNIVERSITY OF THE PHILIPPINES                                             | Public        |   304 |   39 |   30 |   20 |   31 |   26 |   33 |   29 |   26 |   31 |    33 |
| ILOILO DOCTORS COLLEGE                                                                | Private       |   301 |   45 |   30 |   39 |   33 |   23 |   30 |   19 |   26 |   23 |    27 |
| UNIVERSIDAD DE STA. ISABEL                                                            | Private       |   300 |   26 |   29 |   31 |   27 |   33 |   28 |   31 |   28 |   29 |    32 |
| RIVERSIDE COLLEGE                                                                     | Private       |   299 |   39 |   39 |   19 |   26 |   36 |   28 |   17 |   28 |   30 |    31 |
| ST. PAUL UNIVERSITY ILOILO                                                            | Private       |   297 |   24 |   20 |   25 |   35 |   24 |   31 |   33 |   25 |   30 |    40 |
| MOUNTAIN VIEW COLLEGE                                                                 | Private       |   295 |   39 |   28 |   28 |   28 |   24 |   32 |   27 |   20 |   25 |    31 |
| UNIVERSITY OF NEGROS OCCIDENTAL-RECOLETOS                                             | Private       |   278 |   32 |   31 |   20 |   24 |   20 |   30 |   26 |   35 |   32 |    23 |
| NOTRE DAME UNIVERSITY                                                                 | Private       |   277 |   50 |   23 |   24 |   27 |   28 |   31 |   17 |   18 |   19 |    32 |
| MIRIAM COLLEGE                                                                        | Private       |   256 |   30 |   30 |   14 |   22 |   33 |   21 |   24 |   23 |   27 |    24 |
| UNIVERSITY OF THE VISAYAS                                                             | Private       |   254 |   51 |   20 |   25 |   32 |   28 |   21 |   15 |   20 |   19 |    13 |
| PALAWAN STATE UNIVERSITY                                                              | Public        |   254 |   29 |   25 |   19 |   33 |   19 |   30 |   26 |   22 |   25 |    18 |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES                                              | Private       |   253 |   26 |   29 |   15 |   30 |   28 |   26 |   22 |   25 |   16 |    29 |
| ATENEO DE NAGA UNIVERSITY                                                             | Private       |   252 |   31 |   23 |   21 |   30 |   31 |   21 |   21 |   24 |   16 |    25 |
| LYCEUM OF THE PHILIPPINES UNIVERSITY - BATANGAS                                       | Private       |   251 |   43 |   31 |   22 |   14 |   20 |   27 |   28 |   22 |   20 |    21 |
| SAINT SCHOLASTICA'S COLLEGE TACLOBAN                                                  | Private       |   248 |   27 |   29 |   24 |   23 |   22 |   28 |   22 |   22 |   18 |    24 |
| UNIVERSITY OF THE PHILIPPINES - COLLEGE OF CEBU                                       | Public        |   246 |   26 |   17 |   13 |   19 |   28 |   29 |   21 |   27 |   28 |    32 |
| OUR LADY OF FATIMA UNIVERSITY VALENZUELA CITY                                         | Private       |   245 |   56 |   39 |   38 |   27 |   27 |   18 |   13 |   11 |   14 |     2 |
| CAGAYAN STATE UNIVERSITY - ANDREWS                                                    | Public        |   242 |   36 |   23 |   22 |   16 |   20 |   22 |   17 |   22 |   30 |    25 |
| LORMA COLLEGES                                                                        | Private       |   233 |   19 |   27 |   20 |   26 |   22 |   32 |   25 |   22 |   17 |    20 |
| SILLIMAN UNIVERSITY DUMAGUETE CITY                                                    | Private       |   221 |    8 |   14 |   17 |   25 |   35 |   24 |   28 |   26 |   22 |    22 |
| SAINT MARY'S UNIVERSITY                                                               | Private       |   217 |   34 |   19 |   19 |   15 |   23 |   24 |   19 |   19 |   19 |    21 |
| CAPITOL MEDICAL CENTER COLLEGES                                                       | Private       |   215 |   26 |   27 |   25 |   16 |   32 |   14 |   15 |   18 |   15 |    26 |
| ARELLANO UNIVERSITY - MANILA                                                          | Private       |   203 |   24 |   19 |   15 |   20 |   21 |   18 |   22 |   18 |   14 |    26 |
| BULACAN STATE UNIVERSITY - MAIN                                                       | Public        |   201 |   23 |   18 |   19 |   16 |   15 |   24 |   12 |   24 |   18 |    24 |
| ST. LOUIS UNIVERSITY BAGUIO CITY                                                      | Private       |   199 |    7 |   14 |   19 |   22 |   31 |   33 |   24 |   24 |   15 |    10 |
| COLEGIO SAN AGUSTIN - BACOLOD                                                         | Private       |   199 |   22 |   21 |   23 |   22 |   19 |   19 |   18 |   15 |   13 |    26 |
| NOTRE DAME OF DADIANGAS UNIVERSITY                                                    | Private       |   199 |   27 |   24 |   10 |   24 |   21 |   11 |   23 |   21 |   11 |    22 |
| MINDANAO STATE UNIVERSITY ILIGAN CITY                                                 | Public        |   197 |    7 |   13 |   18 |   16 |   34 |   27 |   26 |   21 |   21 |    14 |
| PERPETUAL HELP COLLEGE OF MANILA                                                      | Private       |   197 |   36 |   28 |   20 |   17 |   17 |   18 |   18 |   18 |    9 |    14 |
| UNIVERSITY OF PERPETUAL HELP - DR. JOSE G. TAMAYO MEDICAL UNIVERSITY                  | Private       |   196 |   16 |   21 |   23 |   15 |   18 |   27 |   20 |   16 |   22 |    17 |
| MAKATI MEDICAL CENTER COLLEGE OF NURSING                                              | Private       |   193 |   23 |   21 |   17 |   15 |   25 |   21 |   22 |   17 |   17 |    12 |
| UNIVERSITY OF THE PHILIPPINES - BAGUIO CITY                                           | Public        |   190 |    0 |    1 |    4 |   15 |   20 |   21 |   37 |   34 |   38 |    20 |
| SOUTHWESTERN UNIVERSITY CEBU                                                          | Private       |   189 |   50 |   33 |   29 |   22 |   19 |   14 |   10 |    6 |    4 |     2 |
| NOTRE DAME OF MARBEL UNIVERSITY                                                       | Private       |   187 |   25 |   20 |   19 |   20 |   12 |   15 |   19 |   17 |   15 |    23 |
| ADAMSON UNIVERSITY                                                                    | Private       |   180 |   27 |   19 |   14 |   16 |   11 |   19 |   23 |   12 |   15 |    18 |
| UNIVERSITY OF THE PHILIPPINES - VISAYAS ILOILO                                        | Public        |   179 |    2 |    0 |    6 |    5 |   15 |   21 |   25 |   31 |   31 |    43 |
| OUR LADY OF FATIMA UNIVERSITY - ANTIPOLO                                              | Private       |   175 |   23 |   18 |   16 |   18 |   22 |   21 |   18 |    9 |   13 |    14 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS TACLOBAN COLLEGE                         | Public        |   172 |   14 |   10 |   13 |   15 |   20 |   20 |   12 |   17 |   16 |    28 |
| NEW ERA UNIVERSITY                                                                    | Private       |   172 |   23 |   17 |   14 |   23 |   11 |   15 |   15 |   15 |   15 |    20 |
| SAN BEDA COLLEGE MENDIOLA MANILA                                                      | Private       |   166 |   18 |   26 |   22 |   40 |   18 |   14 |    8 |    8 |    7 |     5 |
| HOLY NAME UNIVERSITY                                                                  | Private       |   160 |   20 |   12 |   20 |   10 |   21 |    8 |   12 |   12 |   18 |    25 |
| MINDANAO STATE UNIVERSITY - GENERAL SANTOS                                            | Public        |   158 |   26 |   10 |    9 |   15 |   17 |   12 |    9 |   18 |   19 |    19 |
| ST. SCHOLASTICA'S COLLEGE                                                             | Private       |   158 |   30 |   18 |   17 |   18 |   13 |   10 |   16 |   15 |    8 |    12 |
| ST. PAUL UNIVERSITY - MANILA (ST. PAUL UNIVERITY SYSTEM)                              | Private       |   157 |   14 |   15 |   12 |   16 |   17 |   26 |    6 |   16 |    8 |    26 |
| UNIVERSITY OF SAN CARLOS CEBU CITY                                                    | Private       |   157 |   13 |   15 |   26 |   19 |   20 |   18 |   10 |   11 |   19 |     6 |
| PINES CITY COLLEGES                                                                   | Private       |   153 |   17 |   12 |   20 |   21 |   18 |   13 |   12 |   11 |   11 |    14 |
| UNIVERSITY OF LA SALETTE                                                              | Private       |   152 |   14 |   10 |   17 |   15 |   14 |   13 |   15 |   11 |   15 |    24 |
| SOUTHVILLE INTERNATIONAL SCHOOL AND COLLEGES                                          | Private       |   150 |   12 |    8 |   23 |   16 |   16 |   21 |   16 |   20 |    6 |    11 |
| UNIVERSITY OF ST. LOUIS - TUGUEGARAO                                                  | Private       |   149 |   22 |   12 |   13 |    7 |   13 |   12 |   14 |   11 |   21 |    20 |
| CEBU DOCTORS COLLEGE CEBU CITY                                                        | Private       |   148 |   21 |   27 |   27 |   18 |   19 |    9 |   12 |    7 |    5 |     3 |
| WESTERN MINDANAO STATE UNIVERSITY ZAMBOANGA CITY                                      | Public        |   144 |   25 |   27 |   23 |   21 |   18 |   12 |   13 |    3 |    1 |     1 |
| AQUINAS UNIVERSITY OF LEGAZPI                                                         | Private       |   144 |   15 |    8 |   15 |   21 |   24 |   13 |   12 |   11 |    7 |    13 |
| BENGUET STATE UNIVERSITY - MAIN                                                       | Public        |   143 |   15 |    9 |    9 |   16 |   14 |   22 |   14 |    7 |   13 |    22 |
| MINDANAO MEDICAL FOUNDATION COLLEGE                                                   | Private       |   142 |   11 |   14 |   17 |   10 |   12 |   14 |   18 |   17 |   16 |    10 |
| UNIVERSITY OF THE PHILIPPINES - MANILA - SCHOOL OF HEALTH SCIENCES                    | Public        |   140 |   14 |   28 |    8 |   14 |   15 |    8 |   10 |   15 |   14 |    13 |
| CENTRAL LUZON STATE UNIVERSITY                                                        | Public        |   139 |   16 |   18 |   16 |   11 |   13 |   10 |    8 |   12 |   14 |    18 |
| UNIVERSITY OF CEBU - BANILAD                                                          | Private       |   139 |   21 |   15 |   19 |    8 |   18 |    7 |   15 |    8 |   16 |    10 |
| UNIVERSITY OF SOUTHERN MINDANAO - MAIN                                                | Public        |   137 |   16 |   18 |   11 |   15 |    9 |    8 |   12 |   17 |   11 |    18 |
| MISAMIS UNIVERSITY - OZAMIS CITY                                                      | Private       |   129 |   18 |   16 |   13 |   10 |   16 |   11 |    6 |   12 |   12 |    12 |
| DE LA SALLE - HEALTH SCIENCES CAMPUS                                                  | Private       |   129 |    6 |   20 |   17 |   24 |   17 |   16 |   11 |    8 |    7 |     3 |
| REMEDIOS TRINIDAD ROMUALDEZ MEDICAL FOUNDATION TACLOBAN                               | Private       |   127 |   14 |   17 |   19 |   16 |   19 |   13 |   10 |    9 |    4 |     6 |
| ST. PAUL UNIVERSITY - QUEZON CITY                                                     | Private       |   127 |   17 |   17 |   18 |   15 |    9 |   13 |   10 |   11 |    7 |     8 |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING AND LIBERAL ARTS                          | Private       |   125 |   11 |   12 |   10 |    8 |   20 |   10 |   11 |    9 |   16 |    14 |
| UNIVERSITY OF THE EAST (C.M. RECTO MANILA)                                            | Private       |   123 |    8 |    8 |   11 |   16 |   11 |   15 |   21 |   17 |    6 |    10 |
| COLEGIO DE SAN JUAN DE LETRAN                                                         | Private       |   122 |    6 |   16 |   15 |   10 |   12 |   10 |    6 |   10 |   16 |    14 |
| GENERAL SANTOS DOCTORS' MEDICAL SCHOOL FOUNDATION                                     | Private       |   122 |    9 |   19 |   12 |   11 |    9 |   14 |    9 |    9 |   15 |    12 |
| UNIVERSITY OF SAN AGUSTIN - ILOILO CITY                                               | Private       |   122 |   10 |   21 |   13 |   16 |   11 |   17 |   13 |    8 |    6 |     6 |
| SOUTHERN LUZON STATE UNIVERSITY - MAIN                                                | Public        |   120 |   14 |    7 |   11 |   18 |    9 |   16 |    9 |    8 |   10 |    13 |
| UNIVERSITY OF PANGASINAN                                                              | Private       |   119 |   16 |   12 |   12 |   11 |   16 |   13 |   11 |    9 |    9 |     6 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES - MAIN                                         | Public        |   118 |   12 |   14 |    8 |   10 |   10 |   17 |   13 |   11 |    9 |    10 |
| DIVINE WORD COLLEGE OF LAOAG                                                          | Private       |   116 |   32 |   24 |   11 |   10 |    9 |   10 |    6 |    8 |    3 |     0 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION                                               | Private       |   116 |   16 |   12 |    9 |   15 |   16 |    9 |   11 |   10 |    8 |     8 |
| EMILIO AGUINALDO COLLEGE MANILA                                                       | Private       |   115 |   20 |   26 |   17 |   14 |   11 |   12 |    6 |    2 |    6 |     1 |
| UNIVERSITY OF EASTERN PHILIPPINES                                                     | Public        |   109 |   21 |    8 |   14 |    7 |   11 |    9 |    8 |    8 |   12 |     7 |
| CENTRAL LUZON DOCTORS' HOSPITAL EDUCATIONAL INSTITUTION                               | Private       |   108 |   12 |   10 |    5 |    8 |   12 |   16 |   11 |   10 |   10 |    11 |
| WESLEYAN UNIVERSITY - PHILIPPINES (CABANATUAN)                                        | Private       |   108 |   12 |   14 |   13 |   16 |   10 |    3 |   11 |    9 |   12 |     7 |
| UNIVERSITY OF BAGUIO BAGUIO CITY                                                      | Private       |   105 |   27 |   20 |   14 |   12 |    8 |    9 |    7 |    5 |    2 |     1 |
| ST. PAUL UNIVERSITY - MANILA                                                          | Private       |   104 |   11 |    8 |   11 |   18 |   17 |    6 |   11 |    9 |    8 |     5 |
| Mariano Marcos State University - College Of Fisheries - Currimao                     | Not Specified |   104 |    4 |   11 |    9 |   15 |   14 |   21 |    9 |    8 |    6 |     7 |
| CAPITOL UNIVERSITY                                                                    | Private       |   103 |   15 |    9 |   11 |   13 |    7 |    9 |    5 |   11 |   11 |    10 |
| HOLY ANGEL UNIVERSITY                                                                 | Private       |   103 |   12 |   12 |   11 |   11 |   19 |    7 |    4 |    8 |    4 |    13 |
| CENTRAL PHILIPPINE UNIVERSITY ILOILO                                                  | Private       |   100 |   14 |    8 |   11 |    7 |   16 |   15 |    8 |    7 |    8 |     6 |
| FEU - EAST ASIA COLLEGE                                                               | Private       |    99 |   12 |   17 |    8 |   10 |    9 |   12 |    8 |    5 |    8 |    10 |
| GLOBAL CITY INNOVATIVE COLLEGE                                                        | Private       |    98 |    9 |   10 |   11 |   15 |   13 |   12 |   10 |    6 |    9 |     2 |
| UNIVERSITY OF ST. LA SALLE BACOLOD CITY                                               | Private       |    96 |    5 |   12 |   10 |   14 |    8 |   14 |   12 |    9 |    6 |     6 |
| ST. JUDE COLLEGE                                                                      | Private       |    96 |   12 |   14 |    9 |    7 |    9 |    8 |    8 |    7 |   11 |     7 |
| FATHER SATURNINO M. URIOS UNIVERSITY                                                  | Private       |    92 |   13 |    7 |    3 |    9 |   12 |   13 |    7 |    8 |    9 |     8 |
| SOUTHWESTERN UNIVERSITY-MATIAS H. AZNAR MEMORIAL COLLEGE OF MEDICINE - CEBU CITY CEBU | Private       |    90 |   22 |   11 |   12 |    4 |    8 |    2 |    7 |    5 |    8 |     5 |
| UNIVERSITY OF SOUTHERN PHILIPPINES FOUNDATION                                         | Private       |    89 |   13 |   11 |   13 |    7 |    7 |    6 |    7 |   12 |    3 |    10 |
| ILIGAN MEDICAL CENTER COLLEGE                                                         | Private       |    87 |   16 |   10 |    4 |    5 |   16 |    7 |    5 |    6 |    5 |     8 |
| CENTRO ESCOLAR UNIVERSITY AT MALOLOS                                                  | Private       |    86 |   12 |    4 |    6 |    4 |   10 |    9 |    8 |   10 |   10 |    13 |
| COLLEGE OF THE HOLY SPIRIT OF MANILA                                                  | Private       |    84 |   14 |    9 |    6 |   13 |    8 |    8 |    4 |    7 |    6 |     8 |
| MANILA DOCTORS COLLEGE - PASAY CITY                                                   | Private       |    83 |    6 |    6 |   14 |   12 |   14 |   14 |    9 |    5 |    2 |     1 |
| UERM MEMORIAL MEDICAL CENTER                                                          | Private       |    82 |    2 |    5 |    9 |   16 |   12 |   18 |    7 |    9 |    1 |     3 |
| HOLY INFANT COLLEGE                                                                   | Private       |    81 |   11 |    4 |   13 |    4 |    7 |    9 |    7 |   13 |    5 |     7 |
| SOUTHEAST ASIAN COLLEGE                                                               | Private       |    80 |   15 |    9 |    6 |    6 |   10 |    6 |   10 |    6 |    2 |     6 |
| EASTER COLLEGE                                                                        | Private       |    80 |   11 |    5 |    8 |   14 |   12 |    4 |    6 |    7 |    4 |     7 |
| DR. CARLOS S. LANTING COLLEGE                                                         | Private       |    76 |   10 |    7 |    8 |   13 |    5 |    5 |    5 |    6 |    6 |     8 |
| WORLD CITI COLLEGES QUEZON CITY                                                       | Private       |    76 |    7 |    5 |   10 |    8 |    7 |    4 |    7 |    4 |    9 |    12 |
| VIRGEN MILAGROSA UNIV. FOUNDATION - SAN CARLOS CITY PANG.                             | Private       |    76 |   14 |   13 |   15 |   11 |    7 |    5 |    2 |    4 |    3 |     0 |
| THE PHILIPPINE WOMEN'S UNIVERSITY SYSTEM - MANILA                                     | Private       |    75 |    4 |    6 |    5 |   10 |    5 |    7 |    8 |   15 |    6 |     7 |
| REMEDIOS T. ROMUALDEZ MEM. SCH. - MMC                                                 | Private       |    75 |    5 |    7 |    9 |    6 |    8 |    8 |   14 |    9 |    8 |     1 |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE                                                  | Private       |    75 |    9 |    8 |    4 |    2 |    9 |    6 |    6 |    7 |    9 |    12 |
| METROPOLITAN HOSPITAL COLLEGE OF NURSING                                              | Private       |    75 |    5 |   12 |    7 |    9 |    7 |    7 |    9 |    4 |    7 |     7 |
| BRENT HOSPITAL AND COLLEGES                                                           | Private       |    73 |   13 |   11 |    6 |    7 |    3 |    4 |    7 |    6 |    8 |     7 |
| CAVITE STATE UNIVERSITY - MAIN                                                        | Public        |    73 |    8 |    7 |    5 |    9 |    6 |   10 |    2 |    6 |    9 |    11 |
| MANILA ADVENTIST MEDICAL CENTER AND COLLEGES                                          | Private       |    72 |   13 |    4 |    6 |    9 |    6 |    7 |    7 |    8 |    9 |     2 |
| LEYTE NORMAL UNIVERSITY                                                               | Public        |    71 |    8 |    7 |   12 |    7 |    3 |   10 |    7 |    4 |    7 |     3 |
| ST. ALEXIUS COLLEGE                                                                   | Private       |    71 |   12 |    7 |    2 |    6 |    4 |    6 |   13 |   10 |    5 |     4 |
| UNIVERSITY OF VISAYAS CEBU                                                            | Private       |    69 |   30 |   11 |    5 |    7 |    5 |    4 |    1 |    1 |    1 |     1 |
| RANGSIT UNIVERSITY                                                                    | Foreign       |    68 |   15 |    7 |    6 |    8 |    2 |    3 |    8 |    2 |    6 |    10 |
| UNIVERSITY OF NUEVA CACERES                                                           | Private       |    67 |   10 |   14 |    2 |    5 |    8 |    7 |    5 |    4 |    4 |     5 |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-LAS PIÑAS                                   | Private       |    67 |   25 |   13 |    7 |    7 |    3 |    4 |    2 |    0 |    5 |     0 |
| NOTRE DAME OF JOLO COLLEGE                                                            | Private       |    65 |   12 |    9 |    5 |    6 |    5 |    5 |    9 |    3 |    6 |     5 |
| LYCEUM NORTHWESTERN DAGUPAN CITY                                                      | Private       |    64 |   22 |   14 |    8 |    2 |    3 |    6 |    4 |    3 |    1 |     1 |
| CAGAYAN STATE UNIVERSITY - TUGUEGARAO                                                 | Public        |    63 |   22 |   13 |    6 |    6 |    4 |    3 |    3 |    1 |    2 |     0 |
| ASSUMPTION COLLEGE                                                                    | Private       |    62 |    5 |    3 |   12 |    6 |    7 |    6 |    6 |    6 |    2 |     7 |
| LA CONSOLACION COLLEGE - MANILA                                                       | Private       |    61 |    5 |    9 |    5 |    6 |    6 |    8 |    5 |    5 |    7 |     5 |
| UNIVERSITY OF THE CORDILLERAS (BCF)                                                   | Private       |    61 |    8 |    5 |   10 |    9 |   12 |    9 |    2 |    2 |    3 |     1 |
| CATANDUANES STATE COLLEGE - MAIN                                                      | Public        |    60 |    7 |    5 |    9 |    6 |    7 |    5 |    4 |    4 |    7 |     6 |
| UNIVERSITY OF SAN JOSE - RECOLETOS                                                    | Private       |    59 |   12 |    5 |    3 |    7 |    7 |    3 |    2 |    5 |    7 |     8 |
| BUTUAN DOCTORS COLLEGE                                                                | Private       |    58 |    8 |    5 |    4 |    5 |   10 |    7 |    4 |    8 |    4 |     3 |
| SACRED HEART COLLEGE OF LUCENA                                                        | Private       |    57 |    7 |    9 |    5 |    4 |    4 |    9 |    8 |    6 |    1 |     4 |
| PHILIPPINE NORMAL UNIVERSITY - MAIN                                                   | Public        |    57 |    7 |    3 |    2 |    5 |    8 |    3 |    8 |    7 |    5 |     5 |
| MANILA DOCTORS COLLEGE U.N. AVENUE MANILA                                             | Private       |    56 |    4 |    9 |    6 |    4 |   17 |    5 |    6 |    4 |    0 |     1 |
| NOTRE DAME UNIVERSITY COTABATO CITY                                                   | Private       |    56 |   15 |    6 |   11 |    4 |    3 |    2 |    3 |    5 |    6 |     1 |
| UNIVERSITY OF MAKATI                                                                  | Public        |    56 |    8 |    7 |    3 |    9 |    8 |    4 |    5 |    5 |    1 |     6 |
| DIPOLOG MEDICAL CENTER COLLEGE FOUNDATION                                             | Private       |    55 |    8 |    7 |    3 |    4 |   10 |    3 |    6 |    2 |    3 |     6 |
| ST. PAUL UNIVERSITY DUMAGUETE                                                         | Private       |    55 |   10 |    5 |    3 |    4 |    7 |    5 |    4 |    5 |    3 |     6 |
| UNIVERSITY OF THE EAST - RAMON MAGSAYSAY MEM. MEDICAL CENTER                          | Private       |    55 |    0 |    3 |    3 |    8 |    8 |    9 |   12 |    8 |    3 |     1 |
| DE LA SALLE - LIPA BATANGAS                                                           | Private       |    53 |    2 |    9 |    7 |    4 |    7 |   12 |    4 |    2 |    4 |     2 |
| MIRIAM COLLEGE FOUNDATION INC.                                                        | Private       |    53 |    4 |   15 |    1 |    9 |    6 |    5 |    5 |    6 |    2 |     0 |
| UNIVERSITY OF NORTHERN PHILIPPINES CAGAYAN                                            | Public        |    53 |   22 |    6 |    6 |    4 |    3 |    3 |    2 |    3 |    1 |     1 |
| SAN LORENZO RUIZ COLLEGE OF ORMOC                                                     | Private       |    53 |   10 |    2 |    6 |    8 |    6 |    3 |    8 |    4 |    3 |     1 |
| OUR LADY OF FATIMA UNIVERSITY - LAGRO QUEZON CITY                                     | Private       |    52 |    7 |    8 |    9 |   11 |    6 |    5 |    2 |    2 |    1 |     1 |
| SOUTH SEED - LPDH COLLEGE                                                             | Private       |    51 |    4 |    2 |    4 |    8 |    4 |    6 |    8 |    3 |    9 |     2 |
| CEBU DOCTOR'S UNIVERSITY COLLEGE OF MEDICINE - MANDAUE CITY CEBU                      | Private       |    50 |    3 |    6 |    6 |    2 |    7 |    6 |    3 |    3 |    3 |    10 |
| BAGUIO CENTRAL UNIVERSITY                                                             | Private       |    50 |   10 |    5 |    4 |    5 |    4 |    1 |    3 |    6 |    4 |     5 |
| MINDANAO SANITARIUM & HOSPITAL COLLEGE ILIGAN CITY                                    | Private       |    50 |   16 |   10 |    6 |    4 |    8 |    4 |    0 |    0 |    2 |     0 |
| NAGA COLLEGE FOUNDATION                                                               | Private       |    50 |    7 |    3 |    4 |    2 |    6 |    0 |    6 |   10 |    3 |     4 |
| BICOL UNIVERSITY - TABACO                                                             | Public        |    48 |    8 |    2 |    4 |    9 |    5 |    5 |    3 |    5 |    2 |     5 |
| CAMARINES SUR POLYTECHNIC COLLEGE - MAIN                                              | Public        |    48 |    5 |    5 |    0 |    3 |    3 |    2 |    6 |    5 |    6 |    11 |
| UNIVERSITY OF THE PHILIPPINES - TACLOBAN                                              | Public        |    48 |    1 |    1 |    7 |    1 |    4 |    5 |    9 |    7 |    9 |     4 |
| SAN JUAN DE DIOS EDUCATIONAL FOUNDATION INC.                                          | Private       |    47 |    9 |   10 |    8 |    4 |    4 |    5 |    1 |    0 |    6 |     0 |
| BICOL UNIVERSITY                                                                      | Public        |    47 |    7 |    6 |   10 |    2 |    4 |    5 |    2 |    5 |    2 |     3 |
| PHILIPPINE WOMEN'S UNIVERSITY TAFT AVENUE MANILA                                      | Private       |    46 |    9 |    4 |    4 |    2 |    6 |    7 |    4 |    3 |    5 |     1 |
| DE LA SALLE - COLLEGE OF SAINT BENILDE                                                | Private       |    46 |    4 |    4 |    2 |    7 |    3 |    3 |    5 |    7 |    5 |     5 |
| PILAR COLLEGE                                                                         | Private       |    46 |    9 |    2 |    3 |    6 |    7 |    1 |    5 |    3 |    4 |     6 |
| MAPUA INSTITUTE OF TECHNOLOGY - MANILA                                                | Private       |    46 |    5 |    5 |    5 |    8 |    3 |    2 |    5 |    2 |    5 |     5 |
| UNIVERSITY OF THE PHILIPPINES - CEBU COLLEGE                                          | Public        |    45 |    0 |    0 |    1 |    5 |    1 |    2 |   10 |    9 |   10 |     7 |
| MOUNTAIN VIEW COLLEGE BUKIDNON                                                        | Private       |    45 |    9 |    5 |    4 |    4 |    7 |    3 |    5 |    3 |    2 |     3 |
| LYCEUM OF THE PHILIPPINES - LAGUNA                                                    | Private       |    45 |    7 |    6 |    5 |    5 |    3 |    3 |    2 |    5 |    3 |     5 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - LAGUNA                                          | Private       |    45 |    3 |    5 |    5 |    4 |    5 |    4 |    3 |    2 |    7 |     6 |
| UNIVERSITY OF THE ASSUMPTION                                                          | Private       |    44 |    3 |    2 |    3 |    8 |    6 |    2 |    5 |    1 |    3 |     8 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - BINAN LAGUNA                                    | Private       |    44 |    8 |    5 |    5 |   11 |    3 |    5 |    1 |    4 |    0 |     2 |
| MEDINA COLLEGE                                                                        | Private       |    44 |    9 |    4 |    5 |    5 |    4 |    1 |    8 |    4 |    0 |     3 |
| PHILIPPINE CHRISTIAN UNIVERSITY                                                       | Private       |    44 |    9 |    4 |    2 |    3 |    4 |    8 |    7 |    4 |    2 |     1 |
| NOTRE DAME OF DADIANGAS COLLEGE GEN. SANTOS                                           | Private       |    43 |    6 |    6 |    6 |    5 |    5 |    5 |    5 |    3 |    2 |     0 |
| UNIVERSITY OF CAGAYAN VALLEY                                                          | Private       |    43 |    3 |    3 |    3 |    7 |    1 |    4 |    5 |    2 |    7 |     7 |
| BROKENSHIRE COLLEGE DAVAO CITY                                                        | Private       |    43 |    8 |    7 |    8 |    5 |    7 |    1 |    2 |    1 |    3 |     1 |
| CENTRAL MINDANAO UNIVERSITY BUKIDNON                                                  | Public        |    43 |   11 |    5 |    5 |    8 |    4 |    4 |    4 |    1 |    0 |     1 |
| UNIVERSITY OF CALIFORNIA - DAVIS                                                      | Foreign       |    42 |    2 |    0 |    0 |    6 |    3 |    3 |    5 |    5 |    8 |    10 |
| UNIVERSITY OF THE VISAYAS - MANDAUE                                                   | Private       |    42 |    8 |    4 |    3 |    5 |    3 |    4 |    4 |    1 |    5 |     5 |
| TRINITY COLLEGE                                                                       | Foreign       |    40 |    7 |   11 |    6 |    1 |    5 |    5 |    2 |    1 |    0 |     2 |
| UNIVERSITY OF CALIFORNIA - IRVINE                                                     | Foreign       |    40 |    1 |    1 |    1 |    1 |    2 |    1 |    8 |    7 |    9 |     8 |
| NEGROS ORIENTAL STATE UNIVERSITY - MAIN                                               | Public        |    40 |    8 |    4 |    5 |    5 |    3 |    5 |    2 |    3 |    1 |     2 |
| LA CONSOLACION COLLEGE                                                                | Private       |    40 |   13 |   12 |    5 |    3 |    1 |    2 |    1 |    1 |    0 |     0 |
| FILAMER CHRISTIAN UNIVERSITY                                                          | Private       |    40 |    4 |    7 |    5 |    5 |    3 |    1 |    3 |    4 |    3 |     2 |
| YAMAN LAHI FOUNDATION - EMILIO AGUINALDO COLLEGE                                      | Private       |    40 |    6 |    0 |    7 |    4 |    3 |    3 |    3 |    3 |    4 |     5 |
| UNIVERSIDAD DE STA. ISABEL NAGA CITY                                                  | Private       |    39 |    4 |    6 |    2 |    6 |    5 |    3 |    4 |    4 |    1 |     3 |
| ST. JUDE COLLEGE MANILA                                                               | Private       |    39 |    7 |   10 |    7 |    5 |    2 |    3 |    0 |    1 |    3 |     1 |
| RANGSIT UNIVERSITY THAILAND                                                           | Foreign       |    38 |   17 |    5 |    4 |    3 |    3 |    3 |    0 |    0 |    1 |     2 |
| UNIVERSITY OF BOHOL                                                                   | Private       |    37 |    6 |    3 |    5 |    4 |    3 |    3 |    1 |    6 |    2 |     3 |
| LOURDES COLLEGE                                                                       | Private       |    37 |    5 |    2 |    2 |    4 |    6 |    4 |    4 |    4 |    1 |     4 |
| NUEVA ECIJA COLLEGES                                                                  | Private       |    37 |    8 |    4 |    5 |    2 |    3 |    1 |    3 |    1 |    6 |     3 |
| NEW ERA UNIVERSITY QUEZON CITY                                                        | Private       |    37 |   14 |    4 |    6 |    4 |    2 |    2 |    3 |    1 |    0 |     1 |
| NORTHWESTERN UNIVERSITY                                                               | Private       |    36 |    3 |    8 |    2 |    5 |    3 |    3 |    3 |    3 |    5 |     1 |
| VISAYAS STATE UNIVERSITY - MAIN                                                       | Public        |    36 |    6 |    1 |    2 |    6 |    5 |    4 |    2 |    3 |    1 |     5 |
| UNIVERSITY OF LUZON                                                                   | Private       |    36 |    8 |    7 |    6 |    3 |    0 |    1 |    2 |    3 |    1 |     3 |
| MAHIDOL UNIVERSITY                                                                    | Foreign       |    36 |    6 |    2 |    8 |    1 |    2 |    3 |    5 |    3 |    5 |     0 |
| DAVAO MEDICAL SCHOOL FOUNDATION INC.                                                  | Private       |    36 |    6 |    3 |    4 |    2 |    9 |    3 |    5 |    2 |    1 |     0 |
| BATANGAS STATE UNIVERSITY - MAIN                                                      | Public        |    35 |    8 |    2 |    2 |    4 |    2 |    3 |    1 |    3 |    3 |     5 |
| MEDINA COLLEGE - PAGADIAN                                                             | Private       |    35 |    5 |    1 |    6 |    4 |    2 |    3 |    4 |    3 |    5 |     2 |
| CALAYAN EDUCATIONAL FOUNDATION                                                        | Private       |    35 |    4 |    4 |    1 |    2 |    6 |    6 |    2 |    5 |    2 |     2 |
| ST. PAUL UNIVERSITY - TUGUEGARAO CAGAYAN                                              | Private       |    34 |    9 |    6 |    7 |    3 |    3 |    3 |    2 |    1 |    0 |     0 |
| UNIVERSITY OF THE PHILIPPINES IN THE VISAYAS CEBU                                     | Public        |    34 |    1 |    0 |    0 |    0 |    2 |    4 |    4 |    6 |    6 |    11 |
| PINES CITY COLLEGES - BAGUIO CITY                                                     | Private       |    34 |   10 |    8 |    6 |    3 |    2 |    1 |    2 |    2 |    0 |     0 |
| ARELLANO UNIVERSITY                                                                   | Private       |    33 |    8 |    5 |    5 |    5 |    2 |    5 |    0 |    0 |    1 |     1 |
| HOLY TRINITY UNIVERSITY                                                               | Private       |    33 |    3 |    4 |    3 |    8 |    1 |    4 |    1 |    6 |    0 |     3 |
| SAN BEDA COLLEGE - ALABANG                                                            | Private       |    33 |    7 |    1 |    3 |    7 |    3 |    3 |    1 |    2 |    2 |     4 |
| ILIGAN MEDICAL CENTER ILIGAN CITY                                                     | Private       |    33 |    9 |    8 |    4 |    2 |    4 |    1 |    3 |    0 |    1 |     1 |
| OUR LADY OF GUADALUPE COLLEGES                                                        | Private       |    33 |    2 |    4 |    8 |    4 |    1 |    3 |    1 |    3 |    1 |     5 |
| SAINT MARY'S COLLEGE OF TAGUM                                                         | Private       |    33 |    2 |    4 |    2 |    2 |    3 |    5 |    4 |    4 |    6 |     1 |
| MARIANO MARCOS STATE UNIVERSITY ILOCOS NORTE                                          | Public        |    32 |    3 |    5 |    5 |    5 |    0 |    2 |    3 |    5 |    1 |     3 |
| MINDANAO STATE UNIVERSITY GENERAL SANTOS CITY                                         | Public        |    32 |    1 |    1 |    9 |    5 |    5 |    0 |    5 |    3 |    2 |     1 |
| Remedios Trinidad Romualdez Medical Foundation                                        | Not Specified |    31 |    2 |    1 |    9 |    3 |    4 |    2 |    3 |    2 |    3 |     1 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM DALTA - CALAMBA                                   | Private       |    31 |    1 |    0 |    2 |    4 |    3 |    3 |    7 |    2 |    1 |     7 |
| LYCEUM OF THE PHILIPPINES - ST. CABRINI COLLEGE OF ALLIED MEDICINE                    | Private       |    31 |    1 |    7 |    3 |    5 |    3 |    5 |    2 |    3 |    1 |     1 |
| LYCEUM OF THE PHILIPPINES UNIVERSITY                                                  | Private       |    30 |    1 |    4 |    4 |    3 |    1 |    4 |    3 |    0 |    7 |     3 |
| LYCEUM OF BATANGAS                                                                    | Private       |    30 |    6 |    7 |    7 |    2 |    2 |    2 |    0 |    3 |    1 |     0 |
| CARAGA STATE UNIVERSITY - MAIN                                                        | Public        |    30 |    3 |    5 |    4 |    2 |    0 |    1 |    4 |    1 |    4 |     4 |
| UNIVERSITY OF CALIFORNIA LOS ANGELES                                                  | Foreign       |    30 |    1 |    1 |    2 |    0 |    2 |    2 |    4 |    4 |    6 |     7 |
| UNIVERSITY OF SOUTHEASTERN PHILIPPINES-DAVAO CITY                                     | Public        |    30 |    5 |    7 |    5 |    4 |    3 |    0 |    3 |    2 |    1 |     0 |
| CAPITOL MEDICAL CENTER COLLEGE Q.C.                                                   | Private       |    30 |    7 |    4 |    5 |    4 |    6 |    1 |    1 |    2 |    0 |     0 |
| ST. ANTHONY COLLEGE OF ROXAS CITY                                                     | Private       |    30 |    5 |    4 |    3 |    4 |    1 |    1 |    5 |    1 |    1 |     4 |
| CHULALONGKORN UNIVERSITY                                                              | Foreign       |    29 |    3 |    3 |    3 |    2 |    3 |    1 |    2 |    3 |    5 |     4 |
| UNIVERSIDAD DE MANILA                                                                 | Public        |    29 |    5 |    0 |    1 |    3 |    3 |    1 |    4 |    3 |    5 |     3 |
| UNIVERSITY OF ST. LA SALLE - DASMARIÑAS CAVITE                                        | Private       |    29 |    2 |    5 |    6 |    4 |    3 |    4 |    3 |    1 |    0 |     1 |
| ST. JOSEPH'S COLLEGE OF QUEZON CITY                                                   | Private       |    29 |    4 |    2 |    4 |    4 |    6 |    1 |    2 |    0 |    1 |     4 |
| UNIVERSITY OF ASIA AND THE PACIFIC                                                    | Private       |    28 |    3 |    5 |    2 |    4 |    3 |    2 |    3 |    2 |    0 |     4 |
| UNIVERSITY OF CEBU (FORMERLY CEBU CENTRAL COLLEGES)                                   | Private       |    28 |    3 |    2 |    4 |    6 |    4 |    5 |    2 |    1 |    1 |     0 |
| PHILIPPINE REHABILITATION INSTITUTE FOUNDATION                                        | Private       |    28 |    2 |    7 |    2 |    1 |    2 |    1 |    2 |    4 |    5 |     2 |
| MAHIDOL UNIVERSITY THAILAND                                                           | Foreign       |    28 |    5 |    5 |    2 |    3 |    5 |    2 |    2 |    2 |    2 |     0 |
| LA SALLE UNIVERSITY                                                                   | Private       |    28 |    2 |    3 |    4 |    3 |    2 |    5 |    2 |    1 |    3 |     3 |
| UNIVERSITY OF LA SALETTE SANTIAGO CITY                                                | Private       |    28 |    5 |    4 |    5 |    5 |    3 |    0 |    0 |    3 |    0 |     3 |
| MOUNTAIN PROVINCE STATE POLYTECHNIC COLLEGE - MAIN                                    | Public        |    27 |    4 |    2 |    5 |    5 |    1 |    3 |    0 |    1 |    2 |     4 |
| BATAAN PENINSULA STATE UNIVERSITY - BALANGA                                           | Public        |    27 |    1 |    2 |    1 |    2 |    3 |    2 |    4 |    5 |    2 |     2 |
| SULU STATE COLLEGE                                                                    | Public        |    27 |    6 |    2 |    1 |    4 |    1 |    2 |    1 |    2 |    2 |     4 |
| RIVERSIDE COLLEGE BACOLOD CITY                                                        | Private       |    27 |    5 |    1 |    4 |    4 |    2 |    5 |    2 |    3 |    1 |     0 |
| UNION CHRISTIAN COLLEGE                                                               | Private       |    26 |    2 |    4 |    2 |    4 |    8 |    0 |    1 |    2 |    0 |     3 |
| WEST NEGROS UNIVERSITY                                                                | Private       |    26 |    1 |    2 |    4 |    3 |    2 |    2 |    1 |    2 |    5 |     2 |
| MANUEL S. ENVERGA UNIVERSITY FOUNDATION - LUCENA                                      | Private       |    26 |    4 |    2 |    1 |    3 |    2 |    1 |    5 |    1 |    2 |     5 |
| CALIFORNIA STATE UNIVERSITY                                                           | Foreign       |    26 |    0 |    0 |    2 |    4 |    1 |    7 |    2 |    4 |    3 |     3 |
| SURIGAO EDUCATION CENTER                                                              | Private       |    26 |    7 |    3 |    5 |    1 |    0 |    2 |    3 |    1 |    2 |     2 |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES                                                 | Private       |    26 |    5 |    4 |    1 |    2 |    3 |    3 |    1 |    4 |    2 |     1 |
| CEBU INSTITUTE OF TECHNOLOGY - UNIVERSITY                                             | Private       |    26 |    3 |    3 |    3 |    2 |    2 |    7 |    1 |    1 |    2 |     2 |
| UNIVERSITY OF THE PHILIPPINES - DILIMAN - EXTENSION PROGRAM IN PAMPANGA               | Public        |    26 |    4 |    4 |    0 |    3 |    2 |    2 |    3 |    2 |    4 |     2 |
| ST. SCHOLASTICA'S COLLEGE - TACLOBAN CITY                                             | Private       |    26 |    5 |    4 |    3 |    3 |    3 |    1 |    2 |    2 |    1 |     2 |
| ST. DOMINIC COLLEGE OF ARTS AND SCIENCES OF CAVITE                                    | Private       |    25 |    2 |    3 |    3 |    2 |    4 |    4 |    2 |    2 |    1 |     2 |
| UNIVERSITY OF CALIFORNIA RIVERSIDE CA USA                                             | Foreign       |    25 |    0 |    0 |    1 |    1 |    2 |    1 |    4 |    2 |    6 |     8 |
| WESLEYAN UNIVERSITY-PHILIPPINES CABANATUAN CITY                                       | Private       |    25 |    4 |    3 |    4 |    4 |    3 |    3 |    1 |    2 |    0 |     1 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM                                                   | Private       |    25 |    4 |    3 |    3 |    2 |    0 |    4 |    0 |    2 |    5 |     2 |
| NATIONAL UNIVERSITY                                                                   | Private       |    24 |    4 |    1 |    0 |    3 |    1 |    4 |    5 |    1 |    3 |     2 |
| UNIVERSITY OF MINDANAO                                                                | Private       |    24 |    2 |    2 |    0 |    3 |    3 |    3 |    1 |    6 |    3 |     1 |
| WORLD CITI COLLEGES                                                                   | Private       |    24 |    4 |    4 |    5 |    3 |    0 |    1 |    3 |    3 |    1 |     0 |
| MAPUA INSTITUTE OF TECHNOLOGY                                                         | Private       |    24 |    4 |    2 |    2 |    1 |    3 |    2 |    4 |    3 |    3 |     0 |
| UNIVERSITY OF THE IMMACULATE CONCEPCION DAVAO CITY                                    | Private       |    24 |    4 |    4 |    4 |    4 |    2 |    3 |    2 |    0 |    0 |     1 |
| DAVAO ORIENTAL STATE COLLEGE OF SCIENCE AND TECHNOLOGY                                | Public        |    24 |    3 |    2 |    2 |    1 |    1 |    4 |    2 |    1 |    4 |     4 |
| PLT COLLEGE                                                                           | Private       |    24 |    4 |    4 |    2 |    1 |    3 |    3 |    3 |    2 |    1 |     1 |
| RIZAL TECHNOLOGICAL UNIVERSITY - MAIN                                                 | Public        |    24 |    2 |    2 |    1 |    4 |    3 |    2 |    3 |    1 |    2 |     2 |
| UNIVERSITY OF SOUTHERN MINDANAO NORTH COTABATO                                        | Public        |    23 |    4 |    4 |    2 |    1 |    2 |    3 |    2 |    2 |    2 |     1 |
| OTHERS (PLEASE SPECIFY)                                                               | Not Specified |    23 |    1 |    1 |    0 |    0 |    0 |    4 |    4 |    3 |    5 |     5 |
| UNIVERSITY OF CALIFORNIA - SAN DIEGO                                                  | Foreign       |    23 |    2 |    0 |    1 |    1 |    0 |    2 |    2 |    3 |    6 |     5 |
| BENGUET STATE UNIVERSITY                                                              | Public        |    23 |    3 |    1 |    2 |    2 |    6 |    1 |    2 |    3 |    2 |     1 |
| UPH-DR. JOSE G. TAMAYO MEDICAL UNIV.                                                  | Private       |    23 |    3 |    8 |    5 |    1 |    1 |    0 |    1 |    3 |    1 |     0 |
| LORMA COLLEGE SAN FERNANDO LA UNION                                                   | Private       |    23 |    6 |    6 |    2 |    5 |    1 |    1 |    1 |    0 |    1 |     0 |
| UNIVERSITY OF PERPETUAL HELP RIZAL - MOLINO                                           | Private       |    23 |    3 |    4 |    3 |    3 |    5 |    1 |    3 |    0 |    0 |     1 |
| AL KWARIZMI INTERNATIONAL COLLEGE FOUNDATION                                          | Foreign       |    23 |    3 |    3 |    3 |    3 |    3 |    3 |    0 |    2 |    1 |     2 |
| ST. MICHAEL'S COLLEGE                                                                 | Private       |    23 |    1 |    4 |    3 |    3 |    2 |    4 |    2 |    1 |    2 |     1 |
| CHIANG MAI UNIVERSITY                                                                 | Foreign       |    23 |    8 |    3 |    2 |    2 |    1 |    2 |    0 |    4 |    0 |     1 |
| TARLAC STATE UNIVERSITY                                                               | Public        |    23 |    3 |    4 |    2 |    1 |    2 |    2 |    4 |    1 |    3 |     1 |
| ASSUMPTION COLLEGE MAKATI                                                             | Private       |    22 |    1 |    1 |    1 |    6 |    3 |    6 |    3 |    1 |    0 |     0 |
| COLEGIO DE SAN AGUSTIN BACOLOD                                                        | Private       |    22 |    2 |    6 |    3 |    4 |    2 |    1 |    3 |    0 |    1 |     0 |
| KESTER GRANT COLLEGE - PHILIPPINES                                                    | Private       |    22 |    2 |    1 |    5 |    3 |    2 |    1 |    3 |    0 |    2 |     3 |
| GOOD SAMARITAN COLLEGES                                                               | Private       |    22 |    2 |    1 |    1 |    3 |    4 |    2 |    3 |    4 |    1 |     1 |
| MISAMIS UNIVERSITY                                                                    | Private       |    22 |    5 |    7 |    2 |    3 |    2 |    1 |    0 |    2 |    0 |     0 |
| RIVERSIDE COLLEGE OF NURSING BACOLOD                                                  | Private       |    21 |    2 |    3 |    4 |    4 |    1 |    2 |    3 |    2 |    0 |     0 |
| BICOL UNIVERSITY COLLEGE OF SCIENCE LEGAZPI CITY                                      | Public        |    21 |    7 |    6 |    0 |    0 |    3 |    1 |    0 |    2 |    1 |     1 |
| JOHN PAUL II COLLEGE OF DAVAO                                                         | Private       |    21 |    4 |    1 |    3 |    2 |    1 |    2 |    1 |    1 |    4 |     2 |
| 13207A                                                                                | Not Specified |    21 |    3 |    3 |    4 |    2 |    1 |    1 |    0 |    0 |    2 |     5 |
| DIVINE WORD COLLEGE OF LEGAZPI                                                        | Private       |    21 |    8 |    1 |    2 |    1 |    3 |    2 |    1 |    2 |    1 |     0 |
| DE LOS SANTOS - STI COLLEGE                                                           | Private       |    21 |    4 |    1 |    2 |    3 |    4 |    0 |    2 |    2 |    2 |     1 |
| CENTRAL LUZON DOCTOR'S HOSPITAL TARLAC                                                | Private       |    21 |    2 |    1 |    3 |    4 |    2 |    3 |    4 |    2 |    0 |     0 |
| MANILA THEOLOGICAL COLLEGE                                                            | Private       |    21 |    3 |    4 |    2 |    4 |    1 |    1 |    0 |    3 |    1 |     1 |
| HOLY NAME UNIVERSITY - TAGBILARAN CITY                                                | Private       |    21 |    1 |    1 |    2 |    5 |    6 |    1 |    3 |    1 |    0 |     1 |
| THAMMASAT UNIVERSITY                                                                  | Foreign       |    20 |    1 |    4 |    2 |    3 |    4 |    3 |    0 |    1 |    1 |     1 |
| BALIUAG UNIVERSITY                                                                    | Private       |    20 |    0 |    2 |    2 |    3 |    4 |    1 |    2 |    2 |    3 |     0 |
| AQUINAS UNIVERSITY LEGASPI CITY                                                       | Private       |    20 |    1 |    7 |    1 |    3 |    2 |    2 |    0 |    2 |    1 |     0 |
| OUR LADY OF MT. CARMEL INSTITUTE OF MEDICAL STUDIES                                   | Private       |    20 |    2 |    2 |    1 |    4 |    0 |    2 |    2 |    0 |    5 |     1 |
| OLIVAREZ COLLEGE                                                                      | Private       |    20 |    0 |    2 |    3 |    5 |    3 |    2 |    0 |    0 |    1 |     4 |
| PHILIPPINE COLLEGE OF HEALTH SCIENCES INC.                                            | Private       |    20 |    8 |    4 |    2 |    1 |    4 |    0 |    0 |    1 |    0 |     0 |
| DE LA SALLE COLLEGE OF SAINT BENILDE - MANILA                                         | Private       |    20 |    0 |    1 |    2 |    2 |    2 |    3 |    1 |    3 |    5 |     1 |
| COLEGIO DE DAGUPAN                                                                    | Private       |    20 |    1 |    4 |    0 |    2 |    2 |    2 |    2 |    1 |    4 |     2 |
| CHINESE GENERAL HOSPITAL COLLEGE OF NURSING & LIBERAL ARTS                            | Private       |    19 |    0 |    0 |    2 |    4 |    4 |    3 |    3 |    3 |    0 |     0 |
| AGO MEDICAL AND EDUCATIONAL CENTER LEGAZPI CITY                                       | Private       |    19 |    4 |    2 |    4 |    1 |    3 |    0 |    2 |    2 |    0 |     1 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - SOUTH LA UNION                         | Public        |    19 |    3 |    1 |    4 |    1 |    2 |    2 |    1 |    0 |    2 |     3 |
| MEDICAL COLLEGES OF NORTHERN PHILIPPINES CAGAYAN                                      | Private       |    19 |    2 |    3 |    2 |    1 |    6 |    3 |    1 |    0 |    1 |     0 |
| WESTERN STATE UNIVERSITY OF COLORADO                                                  | Foreign       |    19 |    1 |    2 |    3 |    2 |    1 |    6 |    2 |    1 |    1 |     0 |
| UNIVERSITY OF PERPETUAL HELP COLLEGE OF LAS PINAS                                     | Private       |    19 |    2 |    6 |    0 |    2 |    2 |    3 |    3 |    1 |    0 |     0 |
| HOLY ANGEL UNIVERSITY ANGELES CITY                                                    | Private       |    18 |    0 |    2 |    5 |    2 |    1 |    2 |    2 |    1 |    2 |     1 |
| UNIVERSITY OF SAN JOSE RECOLETOS CEBU                                                 | Private       |    18 |    6 |    1 |    2 |    2 |    2 |    4 |    0 |    0 |    1 |     0 |
| SAMAR STATE UNIVERSITY - MAIN                                                         | Public        |    18 |    2 |    0 |    1 |    4 |    3 |    0 |    3 |    1 |    2 |     1 |
| MAPUA INSTITUTE OF TECHNOLOGY - MAKATI                                                | Private       |    18 |    1 |    5 |    3 |    2 |    2 |    1 |    0 |    2 |    0 |     1 |
| TAGUM DOCTORS COLLEGE                                                                 | Private       |    18 |    3 |    3 |    3 |    2 |    1 |    1 |    0 |    2 |    0 |     2 |
| COLEGIO DE STA. LOURDES OF LEYTE FOUNDATION                                           | Private       |    18 |    3 |    4 |    1 |    1 |    2 |    1 |    0 |    5 |    1 |     0 |
| UNIVERSITY OF CALIFORNIA BERKELEY                                                     | Foreign       |    18 |    1 |    1 |    1 |    0 |    0 |    0 |    1 |    1 |    4 |     7 |
| CEBU TECHNOLOGICAL UNIVERSITY - MAIN                                                  | Public        |    18 |    5 |    2 |    1 |    0 |    0 |    0 |    4 |    1 |    2 |     3 |
| ARELLANO UNIVERSITY - PASIG                                                           | Private       |    18 |    2 |    2 |    2 |    0 |    5 |    2 |    3 |    0 |    1 |     1 |
| PAMANTASAN NG LUNGSOD NG PASIG                                                        | Public        |    18 |    4 |    2 |    1 |    1 |    1 |    2 |    0 |    1 |    5 |     1 |
| UNIVERSITY OF CALIFORNIA-RIVERSIDE                                                    | Foreign       |    18 |    2 |    1 |    1 |    0 |    0 |    2 |    3 |    2 |    4 |     2 |
| ST. JOSEPH COLLEGE CAVITE CITY                                                        | Private       |    17 |    2 |    1 |    1 |    2 |    2 |    0 |    3 |    2 |    1 |     1 |
| UNIVERSITY OF TORONTO                                                                 | Foreign       |    17 |    0 |    1 |    0 |    1 |    0 |    0 |    3 |    4 |    3 |     5 |
| UNIVERSITY OF PANGASINAN DAGUPAN CITY                                                 | Private       |    17 |    1 |    3 |    3 |    5 |    2 |    2 |    0 |    1 |    0 |     0 |
| ANDRES BONIFACIO COLLEGE                                                              | Private       |    17 |    2 |    2 |    0 |    3 |    0 |    4 |    0 |    0 |    3 |     2 |
| CHULALONGKORN UNIVERSITY THAILAND                                                     | Foreign       |    17 |    1 |    3 |    3 |    3 |    4 |    1 |    1 |    0 |    0 |     1 |
| OUR LADY OF FATIMA UNIVERSITY - PAMPANGA                                              | Private       |    17 |    1 |    2 |    5 |    1 |    0 |    2 |    3 |    1 |    1 |     0 |
| BUKIDNON STATE UNIVERSITY                                                             | Public        |    17 |    2 |    5 |    1 |    0 |    0 |    1 |    2 |    2 |    3 |     0 |
| LA CONSOLACION UNIVERSITY PHILIPPINES                                                 | Private       |    17 |    1 |    4 |    1 |    1 |    1 |    2 |    4 |    2 |    0 |     1 |
| BULACAN STATE UNIVERSITY                                                              | Public        |    16 |    2 |    3 |    1 |    1 |    3 |    0 |    2 |    3 |    1 |     0 |
| COLEGIO DE SAN JUAN DE LETRAN CALAMBA                                                 | Private       |    16 |    3 |    5 |    4 |    1 |    1 |    1 |    1 |    0 |    0 |     0 |
| CENTRAL LUZON STATE UNIVERSITY NUEVA ECIJA                                            | Public        |    16 |    3 |    3 |    2 |    2 |    2 |    3 |    0 |    0 |    1 |     0 |
| UNIVERSITY OF EASTERN PHILIPPINES - SAMAR                                             | Public        |    16 |    6 |    5 |    3 |    1 |    0 |    0 |    0 |    1 |    0 |     0 |
| NORTHERN LUZON ADVENTIST COLLEGE                                                      | Private       |    16 |    3 |    0 |    1 |    2 |    1 |    3 |    2 |    1 |    2 |     1 |
| UNIVERSITY OF WASHINGTON                                                              | Foreign       |    16 |    2 |    0 |    0 |    0 |    1 |    3 |    1 |    2 |    1 |     6 |
| MAE FAH LUANG UNIVERSITY                                                              | Foreign       |    16 |    5 |    4 |    0 |    0 |    0 |    0 |    2 |    1 |    2 |     2 |
| NATIONAL UNIVERSITY - CEDCE                                                           | Private       |    16 |    3 |    2 |    2 |    0 |    3 |    4 |    0 |    0 |    0 |     2 |
| ARELLANO UNIVERSITY - PASAY                                                           | Private       |    16 |    1 |    3 |    2 |    2 |    0 |    1 |    0 |    3 |    1 |     2 |
| CANOSSA COLLEGE                                                                       | Private       |    16 |    0 |    1 |    0 |    1 |    1 |    4 |    2 |    2 |    3 |     2 |
| DE OCAMPO MEMORIAL COLLEGE                                                            | Private       |    16 |    3 |    1 |    1 |    5 |    1 |    2 |    0 |    2 |    0 |     1 |
| IMMACULATE CONCEPTION COLLEGE - ALBAY                                                 | Private       |    16 |    3 |    0 |    1 |    0 |    1 |    3 |    3 |    2 |    2 |     0 |
| MARY CHILES COLLEGE                                                                   | Private       |    15 |    2 |    2 |    3 |    2 |    0 |    1 |    3 |    1 |    0 |     1 |
| LIPA CITY COLLEGES                                                                    | Private       |    15 |    1 |    1 |    0 |    3 |    1 |    1 |    0 |    1 |    2 |     5 |
| SAINT PAUL COLLEGE OF ILOCOS SUR                                                      | Private       |    15 |    1 |    2 |    1 |    1 |    3 |    0 |    3 |    1 |    2 |     1 |
| CARITAS FAMILY HOSPITAL AND COLLEGES                                                  | Private       |    15 |    2 |    1 |    0 |    1 |    2 |    1 |    3 |    1 |    2 |     2 |
| ST. PAUL COLLEGE ILOILO                                                               | Private       |    15 |    0 |    0 |    2 |    1 |    4 |    1 |    2 |    3 |    2 |     0 |
| COLLEGE OF THE HOLY SPIRIT OF TARLAC                                                  | Private       |    15 |    1 |    0 |    2 |    0 |    1 |    3 |    2 |    0 |    1 |     4 |
| UNIVERSITY OF BATANGAS                                                                | Private       |    15 |    2 |    2 |    2 |    2 |    4 |    2 |    1 |    0 |    0 |     0 |
| DR. P. OCAMPO COLLEGES                                                                | Private       |    15 |    3 |    3 |    0 |    2 |    0 |    1 |    2 |    1 |    1 |     2 |
| PALAWAN STATE UNIVERSITY PUERTO PRINCESA CITY                                         | Public        |    15 |    5 |    5 |    0 |    2 |    1 |    1 |    0 |    0 |    1 |     0 |
| GORDON COLLEGE                                                                        | Public        |    15 |    0 |    2 |    2 |    2 |    1 |    1 |    1 |    1 |    1 |     3 |
| NORTH VALLEY COLLEGE FOUNDATION                                                       | Private       |    15 |    0 |    2 |    3 |    2 |    4 |    1 |    0 |    1 |    1 |     1 |
| NARESUAN UNIVERSITY                                                                   | Foreign       |    15 |    2 |    0 |    2 |    1 |    2 |    0 |    1 |    2 |    2 |     2 |
| MANILA ADVENTIST MEDICAL CENTER - PASAY CITY                                          | Private       |    15 |    0 |    2 |    0 |    3 |    5 |    0 |    0 |    2 |    2 |     1 |
| LYCEUM OF THE PHILIPPINES - CAVITE                                                    | Private       |    15 |    2 |    4 |    0 |    1 |    0 |    3 |    4 |    0 |    0 |     1 |
| UNIVERSITY OF FLORIDA                                                                 | Foreign       |    15 |    1 |    1 |    0 |    1 |    1 |    0 |    3 |    2 |    4 |     2 |
| LYCEUM OF THE PHILIPPINES                                                             | Private       |    14 |    1 |    0 |    2 |    2 |    4 |    3 |    1 |    0 |    1 |     0 |
| URDANETA CITY UNIVERSITY                                                              | Public        |    14 |    1 |    2 |    1 |    1 |    2 |    1 |    2 |    2 |    1 |     1 |
| MONAD UNIVERSITY                                                                      | Foreign       |    14 |    1 |    3 |    1 |    1 |    1 |    0 |    1 |    3 |    1 |     2 |
| ILOCOS SUR COMMUNITY COLLEGE - BANTAY ILOCOS SUR                                      | Public        |    14 |    2 |    4 |    1 |    4 |    0 |    0 |    2 |    1 |    0 |     0 |
| LYCEUM OF ILIGAN FOUNDATION                                                           | Private       |    14 |    2 |    0 |    1 |    1 |    1 |    1 |    1 |    1 |    1 |     5 |
| NOTRE DAME OF TACURONG COLLEGE                                                        | Private       |    14 |    3 |    2 |    3 |    1 |    2 |    1 |    0 |    0 |    1 |     1 |
| BICOL UNIVERSITY COLLEGE OF NURSING LEGAZPI CITY                                      | Public        |    14 |    1 |    0 |    1 |    2 |    2 |    2 |    1 |    3 |    1 |     1 |
| ST. PAUL UNIVERSITY SURIGAO                                                           | Private       |    14 |    2 |    2 |    1 |    1 |    0 |    2 |    1 |    3 |    1 |     0 |
| AKLAN STATE UNIVERSITY - MAIN                                                         | Public        |    14 |    2 |    2 |    0 |    2 |    1 |    2 |    1 |    1 |    1 |     2 |
| SOUTHEAST ASIAN COLLEGE INC.-QUEZON CITY                                              | Private       |    14 |    4 |    2 |    4 |    2 |    1 |    1 |    0 |    0 |    0 |     0 |
| SAINT TONIS COLLEGE                                                                   | Private       |    14 |    1 |    3 |    1 |    3 |    1 |    1 |    1 |    1 |    1 |     1 |
| CALAMBA DOCTORS' COLLEGE                                                              | Private       |    14 |    3 |    1 |    1 |    2 |    1 |    1 |    2 |    1 |    0 |     0 |
| CENTRAL COLLEGES OF THE PHILIPPINES                                                   | Private       |    13 |    2 |    1 |    0 |    0 |    2 |    3 |    0 |    2 |    1 |     1 |
| DE LA SALLE - ARANETA UNIVERSITY                                                      | Private       |    13 |    4 |    0 |    2 |    1 |    1 |    1 |    2 |    0 |    2 |     0 |
| 13100A                                                                                | Not Specified |    13 |    1 |    2 |    1 |    0 |    2 |    2 |    0 |    3 |    1 |     1 |
| ST. FERDINAND COLLEGE - ILAGAN                                                        | Private       |    13 |    1 |    1 |    1 |    4 |    0 |    2 |    1 |    1 |    1 |     1 |
| BICOL UNIVERSITY - DARAGA                                                             | Public        |    13 |    4 |    1 |    1 |    2 |    2 |    2 |    0 |    0 |    0 |     1 |
| COLEGIO DE SAN LORENZO RUIZ DE MANILA OF NORTHERN SAMAR                               | Private       |    13 |    2 |    1 |    1 |    0 |    2 |    4 |    0 |    1 |    2 |     0 |
| PAMANTASAN NG LUNGSOD NG MARIKINA                                                     | Public        |    13 |    3 |    0 |    1 |    1 |    0 |    2 |    0 |    1 |    3 |     2 |
| UNIVERSITY OF BOHOL TAGBILARAN CITY                                                   | Private       |    13 |    4 |    0 |    1 |    1 |    1 |    2 |    1 |    3 |    0 |     0 |
| SAINT GABRIEL COLLEGE                                                                 | Private       |    13 |    3 |    1 |    2 |    2 |    1 |    1 |    0 |    0 |    2 |     1 |
| UNIVERSITY OF SAINT ANTHONY                                                           | Private       |    13 |    2 |    0 |    0 |    4 |    2 |    1 |    0 |    1 |    1 |     1 |
| UNIVERSITY OF PERPETUAL HELP SYSTEM - GMA                                             | Private       |    13 |    1 |    5 |    0 |    1 |    3 |    2 |    0 |    0 |    0 |     0 |
| WESTERN LEYTE COLLEGE OF ORMOC CITY                                                   | Private       |    13 |    3 |    2 |    1 |    0 |    1 |    0 |    2 |    1 |    1 |     2 |
| LYCEUM OF APARRI                                                                      | Private       |    13 |    0 |    3 |    2 |    3 |    2 |    0 |    0 |    0 |    1 |     2 |
| NOTRE DAME OF MIDSAYAP COLLEGE                                                        | Private       |    13 |    2 |    1 |    1 |    0 |    0 |    1 |    3 |    1 |    2 |     0 |
| University For Development Studies                                                    | Not Specified |    13 |    4 |    0 |    2 |    1 |    0 |    0 |    3 |    1 |    0 |     2 |
| HOLY CROSS OF DAVAO COLLEGE                                                           | Private       |    13 |    4 |    1 |    1 |    1 |    0 |    2 |    1 |    0 |    2 |     1 |
| DOMINICAN COLLEGE                                                                     | Private       |    13 |    1 |    2 |    3 |    0 |    2 |    0 |    1 |    1 |    1 |     0 |
| UNCIANO COLLEGES                                                                      | Private       |    12 |    1 |    0 |    4 |    0 |    1 |    0 |    2 |    0 |    1 |     2 |
| SACRED HEART COLLEGE LUCENA CITY                                                      | Private       |    12 |    0 |    0 |    5 |    1 |    1 |    1 |    1 |    1 |    1 |     1 |
| FIRST ASIA INSTITUTE OF TECHNOLOGY AND HUMANITIES                                     | Private       |    12 |    1 |    0 |    0 |    2 |    3 |    1 |    2 |    2 |    0 |     1 |
| UNIVERSITY OF CALIFORNIA SANTA BARBARA                                                | Foreign       |    12 |    2 |    0 |    1 |    2 |    2 |    0 |    2 |    1 |    0 |     2 |
| UNCIANO COLLEGES AND GENERAL HOSPITAL                                                 | Private       |    12 |    0 |    2 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |     2 |
| UNIVERSITY OF ILOILO                                                                  | Private       |    12 |    2 |    0 |    1 |    0 |    1 |    2 |    1 |    1 |    0 |     4 |
| UNIVERSITY OF PERPETUAL HELP - CALAMBA LAGUNA                                         | Private       |    12 |    1 |    3 |    0 |    3 |    1 |    3 |    0 |    0 |    1 |     0 |
| UNIVERSITY OF NEVADA LAS VEGAS                                                        | Foreign       |    12 |    1 |    0 |    1 |    1 |    0 |    2 |    1 |    2 |    1 |     3 |
| MEDINA COLLEGE - IPIL                                                                 | Private       |    12 |    1 |    2 |    2 |    0 |    0 |    0 |    3 |    0 |    3 |     0 |
| SOUTHEAST ASIAN COLLEGE INC.-ESPANA MANILA                                            | Private       |    12 |    7 |    4 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |     0 |
| AMA COMPUTER COLLEGE                                                                  | Private       |    12 |    4 |    2 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |     1 |
| UNIVERSITY OF THE PHILIPPINES - PAMPANGA                                              | Public        |    12 |    0 |    1 |    0 |    0 |    4 |    0 |    4 |    2 |    1 |     0 |
| SRINAKHARINWIROT UNIVERSITY                                                           | Foreign       |    12 |    1 |    1 |    1 |    3 |    1 |    1 |    1 |    1 |    0 |     1 |
| PHILIPPINE REHABILITATION INSTITUTE                                                   | Private       |    12 |    3 |    1 |    2 |    0 |    2 |    1 |    2 |    1 |    0 |     0 |
| DR. YANGA'S COLLEGES                                                                  | Private       |    12 |    0 |    2 |    0 |    3 |    2 |    2 |    0 |    1 |    0 |     1 |
| CENTRAL PHILIPPINE ADVENTIST COLLEGE NEGROS OCCIDENTAL                                | Private       |    12 |    2 |    0 |    2 |    1 |    1 |    4 |    0 |    0 |    1 |     1 |
| BICOL UNIVERSITY - POLANGUI                                                           | Public        |    12 |    0 |    0 |    1 |    2 |    3 |    1 |    2 |    1 |    0 |     2 |
| MEDINA COLLEGE OZAMIS MISAMIS ORIENTAL                                                | Private       |    11 |    5 |    2 |    1 |    0 |    0 |    2 |    1 |    0 |    0 |     0 |
| MARIANO MARCOS STATE UNIVERSITY - COLLEGE OF EDUCATION - LAOAG CITY                   | Public        |    11 |    0 |    3 |    1 |    1 |    1 |    0 |    2 |    0 |    3 |     0 |
| LAGUNA COLLEGE                                                                        | Private       |    11 |    0 |    1 |    0 |    3 |    1 |    2 |    2 |    1 |    0 |     1 |
| VIRGEN MILAGROSA EDUCATIONAL INSTITUTE SAN CARLOS CITY                                | Private       |    11 |    1 |    1 |    0 |    4 |    1 |    1 |    2 |    0 |    1 |     0 |
| NORTHERN CHRISTIAN COLLEGE                                                            | Private       |    11 |    2 |    3 |    0 |    0 |    0 |    1 |    0 |    0 |    1 |     4 |
| NORTHERN NEGROS STATE COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                        | Public        |    11 |    1 |    1 |    1 |    1 |    1 |    0 |    2 |    0 |    1 |     3 |
| UNIVERSITY OF CORDILLERAS                                                             | Private       |    11 |    1 |    1 |    3 |    1 |    1 |    0 |    1 |    1 |    2 |     0 |
| MABINI COLLEGES                                                                       | Private       |    11 |    2 |    1 |    1 |    1 |    0 |    1 |    0 |    2 |    1 |     2 |
| KIDAPAWAN DOCTORS COLLEGE INC.                                                        | Private       |    11 |    1 |    1 |    4 |    0 |    0 |    1 |    2 |    0 |    0 |     2 |
| NOTRE DAME OF JOLO COLLEGE - JOLO SULU                                                | Private       |    11 |    5 |    2 |    2 |    0 |    2 |    0 |    0 |    0 |    0 |     0 |
| NOTRE DAME OF MARBEL UNIV.                                                            | Private       |    11 |    2 |    0 |    1 |    2 |    2 |    1 |    0 |    2 |    0 |     1 |
| UNIVERSITY OF PERPETUAL HELP - RIZAL                                                  | Private       |    11 |    4 |    0 |    2 |    0 |    0 |    0 |    2 |    3 |    0 |     0 |
| HUACHIEW CHALERMPRAKIET UNIVERSITY                                                    | Foreign       |    11 |    0 |    1 |    4 |    1 |    1 |    0 |    2 |    0 |    0 |     2 |
| FELLOWSHIP BAPTIST COLLEGE                                                            | Private       |    11 |    2 |    0 |    0 |    1 |    2 |    0 |    1 |    1 |    2 |     2 |
| FOUNDATION UNIVERSITY                                                                 | Private       |    11 |    1 |    0 |    0 |    2 |    2 |    1 |    0 |    1 |    2 |     1 |
| UNIVERSITY OF SAN FRANCISCO                                                           | Foreign       |    11 |    0 |    0 |    0 |    2 |    1 |    0 |    1 |    2 |    3 |     2 |
| CORDILLERA CAREER DEVELOPMENT COLLEGE                                                 | Private       |    11 |    1 |    0 |    0 |    0 |    3 |    1 |    3 |    1 |    0 |     2 |
| RUTGERS UNIVERSITY NEW JERSEY                                                         | Foreign       |    11 |    0 |    0 |    0 |    0 |    1 |    1 |    2 |    3 |    2 |     2 |
| RUTGERS UNIVERSITY                                                                    | Foreign       |    11 |    1 |    0 |    0 |    1 |    0 |    2 |    1 |    1 |    2 |     3 |
| OLIVAREZ COLLEGE SUCAT PARA$AQUE                                                      | Private       |    11 |    3 |    2 |    1 |    2 |    0 |    1 |    1 |    1 |    0 |     0 |
| SIENA COLLEGE OF TAYTAY                                                               | Private       |    11 |    0 |    2 |    0 |    1 |    0 |    1 |    1 |    4 |    1 |     0 |
| COLLEGE OF HOLY SPIRIT-MANILA                                                         | Private       |    11 |    4 |    2 |    0 |    2 |    2 |    0 |    1 |    0 |    0 |     0 |
| BRENT HOSPITAL AND COLLEGES INC. ZAMBOANGA CITY                                       | Private       |    11 |    5 |    4 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |     0 |
| BROKENSHIRE COLLEGE SOCSKSARGEN                                                       | Private       |    11 |    2 |    3 |    0 |    1 |    0 |    1 |    1 |    0 |    0 |     3 |
| SULTAN KUDARAT STATE UNIVERSITY - MAIN                                                | Public        |    10 |    3 |    1 |    1 |    0 |    2 |    2 |    1 |    0 |    0 |     0 |
| SULTAN KUDARAT STATE UNIVERSITY - TACURONG                                            | Public        |    10 |    2 |    1 |    2 |    1 |    2 |    0 |    0 |    0 |    1 |     0 |
| ST. LUKE'S SCHOOL OF MEDICINE INDIA                                                   | Private       |    10 |    2 |    0 |    2 |    1 |    3 |    1 |    1 |    0 |    0 |     0 |
| ST. JOSEPH'S COLLEGE QUEZON CITY                                                      | Private       |    10 |    1 |    2 |    3 |    2 |    1 |    0 |    1 |    0 |    0 |     0 |
| UNIVERSITAS ADVENT INDONESIA                                                          | Foreign       |    10 |    1 |    2 |    1 |    0 |    1 |    0 |    2 |    1 |    1 |     1 |
| POLYTECHNIC COLLEGE OF DAVAO DEL SUR                                                  | Private       |    10 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |     5 |
| MARY HELP OF CHRISTIANS COLLEGE SEMINARY                                              | Private       |    10 |    2 |    4 |    2 |    1 |    1 |    0 |    0 |    0 |    0 |     0 |
| JOSE RIZAL UNIVERSITY                                                                 | Private       |    10 |    0 |    1 |    0 |    2 |    1 |    2 |    0 |    1 |    3 |     0 |
| NOTRE DAME OF KIDAPAWAN COLLEGE                                                       | Private       |    10 |    2 |    2 |    0 |    1 |    3 |    1 |    1 |    0 |    0 |     0 |
| UNIVERSITY OF CENTRAL FLORIDA                                                         | Foreign       |    10 |    2 |    1 |    0 |    1 |    1 |    1 |    1 |    2 |    0 |     1 |
| UNIVERSITY OF GUAM                                                                    | Foreign       |    10 |    1 |    1 |    0 |    3 |    1 |    0 |    0 |    1 |    3 |     0 |
| PHILIPPINE NORMAL COLLEGE TAFT AVENUE MANILA                                          | Public        |    10 |    0 |    2 |    0 |    0 |    2 |    3 |    0 |    2 |    0 |     1 |
| DR. CARLOS LANTING COLLEGE - NOVALICHES QUEZON CITY                                   | Private       |    10 |    4 |    1 |    1 |    2 |    0 |    1 |    0 |    1 |    0 |     0 |
| COLUMBAN COLLEGE - OLONGAPO CITY                                                      | Private       |    10 |    1 |    1 |    0 |    1 |    2 |    1 |    0 |    1 |    1 |     2 |
| CAMARINES NORTE STATE COLLEGE - MAIN                                                  | Public        |    10 |    1 |    2 |    1 |    1 |    0 |    0 |    1 |    1 |    2 |     1 |
| CHRIST THE KING COLLEGE - CALBAYOG CITY                                               | Private       |    10 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    2 |     1 |
| UNIVERSITY OF THE PHILIPPINES SCH. OF HEALTH SCIENCES -LEYTE                          | Public        |    10 |    2 |    2 |    4 |    0 |    1 |    1 |    0 |    0 |    0 |     0 |
| UNIVERSITY OF RIZAL SYSTEM - MORONG                                                   | Public        |     9 |    1 |    1 |    1 |    1 |    0 |    1 |    0 |    2 |    1 |     1 |
| NOTRE DAME OF MARBEL COLLEGE SOUTH COTABATO                                           | Private       |     9 |    0 |    2 |    1 |    2 |    2 |    0 |    0 |    2 |    0 |     0 |
| UNIVERSITY OF ILLINOIS CHICAGO                                                        | Foreign       |     9 |    1 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |    3 |     3 |
| Texila American University                                                            | Not Specified |     9 |    1 |    2 |    0 |    0 |    2 |    0 |    0 |    2 |    2 |     0 |
| NUEVA ECIJA UNIVERSITY OF SCIENCE AND TECHNOLOGY - MAIN                               | Public        |     9 |    0 |    2 |    0 |    1 |    1 |    0 |    3 |    1 |    0 |     1 |
| WESTERN VISAYAS COLLEGE OF SCIENCE AND TECHNOLOGY - MAIN                              | Public        |     9 |    2 |    0 |    0 |    1 |    1 |    0 |    1 |    2 |    1 |     1 |
| VIRGINIA COMMONWEALTH UNIVERSITY                                                      | Foreign       |     9 |    0 |    0 |    0 |    0 |    0 |    1 |    2 |    2 |    2 |     2 |
| SAN SEBASTIAN COLLEGE - RECOLETOS DE CAVITE                                           | Private       |     9 |    1 |    1 |    1 |    3 |    1 |    0 |    0 |    0 |    1 |     1 |
| SAN SEBASTIAN COLLEGE - RECOLETOS CANLUBANG                                           | Private       |     9 |    2 |    0 |    0 |    1 |    1 |    0 |    1 |    2 |    0 |     1 |
| STONY BROOK UNIVERSITY                                                                | Foreign       |     9 |    0 |    2 |    0 |    1 |    0 |    2 |    0 |    1 |    1 |     2 |
| UM TAGUM COLLEGE                                                                      | Private       |     9 |    1 |    0 |    2 |    0 |    0 |    1 |    0 |    2 |    0 |     2 |
| PATTS COLLEGE OF AERONAUTICS                                                          | Private       |     9 |    0 |    0 |    3 |    0 |    2 |    0 |    0 |    2 |    0 |     2 |
| UNIVERSITY OF CALIFORNIA AT STA. CRUZ U.S.A.                                          | Foreign       |     9 |    1 |    1 |    1 |    0 |    1 |    0 |    3 |    1 |    1 |     0 |
| JOSE RIZAL MEMORIAL STATE UNIVERSITY - MAIN                                           | Public        |     9 |    1 |    3 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     1 |
| MINDANAO MEDICAL FOUNDATION COLLEGE DAVAO                                             | Private       |     9 |    4 |    1 |    1 |    0 |    2 |    0 |    1 |    0 |    0 |     0 |
| UNIVERSITY OF HAWAII AT MANOA                                                         | Foreign       |     9 |    1 |    0 |    0 |    0 |    2 |    0 |    1 |    1 |    1 |     2 |
| CHIANG KAI SHEK COLLEGE                                                               | Private       |     9 |    0 |    0 |    2 |    1 |    1 |    1 |    0 |    2 |    2 |     0 |
| DOMINICAN COLLEGE BLUM SAN JUAN MM                                                    | Private       |     9 |    1 |    2 |    3 |    1 |    0 |    1 |    0 |    0 |    1 |     0 |
| DON MARIANO MARCOS MEMORIAL STATE UNIVERSITY - NORTH LA UNION - MAIN                  | Public        |     9 |    2 |    1 |    0 |    0 |    1 |    1 |    2 |    1 |    1 |     0 |
| CENTRO ESCOLAR UNIVERSITY-MALOLOS BULACAN                                             | Private       |     9 |    0 |    2 |    1 |    4 |    2 |    0 |    0 |    0 |    0 |     0 |
| BURAPHA UNIVERSITY                                                                    | Foreign       |     9 |    4 |    3 |    1 |    0 |    0 |    0 |    1 |    0 |    0 |     0 |
| CALIFORNIA STATE UNIVERSITY LONG BEACH                                                | Foreign       |     9 |    2 |    1 |    0 |    1 |    0 |    1 |    0 |    0 |    2 |     1 |
| CALIFORNIA STATE UNIVERSITY FRESNO                                                    | Foreign       |     9 |    3 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     2 |
| LAGUNA STATE POLYTECHNIC UNIVERSITY - LAGUNA COLLEGE OF ARTS AND TRADES - STA. CRUZ   | Public        |     9 |    0 |    1 |    0 |    0 |    3 |    0 |    1 |    2 |    1 |     1 |
| KALAYAAN COLLEGE                                                                      | Private       |     9 |    2 |    1 |    1 |    0 |    1 |    1 |    0 |    2 |    0 |     1 |
| LA SALLE COLLEGE - ANTIPOLO                                                           | Private       |     9 |    3 |    2 |    0 |    1 |    1 |    0 |    0 |    0 |    1 |     1 |
| ISABELA STATE UNIVERSITY - ILAGAN                                                     | Public        |     9 |    0 |    0 |    0 |    1 |    1 |    1 |    0 |    2 |    2 |     2 |
| UNIVERSITY OF CEBU - LAPULAPU AND MANDAUE                                             | Private       |     8 |    0 |    0 |    1 |    0 |    2 |    1 |    1 |    0 |    1 |     2 |
| THAMMASAT UNIV.                                                                       | Foreign       |     8 |    3 |    0 |    3 |    1 |    0 |    1 |    0 |    0 |    0 |     0 |
| U.P. VISAYAS (TACLOBAN CITY LEYTE)                                                    | Public        |     8 |    0 |    1 |    0 |    0 |    1 |    0 |    2 |    2 |    2 |     0 |
| PHILIPPINE WOMEN'S COLLEGE OF DAVAO                                                   | Private       |     8 |    0 |    0 |    2 |    3 |    0 |    0 |    0 |    2 |    1 |     0 |
| PRINCE OF SONGKLA UNIVERSITY                                                          | Foreign       |     8 |    1 |    0 |    0 |    3 |    1 |    1 |    0 |    1 |    1 |     0 |
| RAMKHAMHAENG UNIVERSITY                                                               | Foreign       |     8 |    1 |    0 |    1 |    0 |    1 |    1 |    0 |    1 |    2 |     1 |
| UNIVERSITY OF BRITISH COLUMBIA                                                        | Foreign       |     8 |    3 |    0 |    2 |    1 |    0 |    0 |    0 |    2 |    0 |     0 |
| UNIVERSITY OF CALIFORNIA SANTA CRUZ                                                   | Foreign       |     8 |    2 |    0 |    0 |    0 |    1 |    0 |    0 |    2 |    1 |     2 |
| PAMANTASAN NG LUNGSOD NG PASAY                                                        | Public        |     8 |    1 |    2 |    1 |    1 |    2 |    0 |    0 |    1 |    0 |     0 |
| UNIVERSITY OF PERPETUAL HELP DALTA SYSTEM-ALABANG ZAPOTE                              | Private       |     8 |    2 |    1 |    1 |    3 |    1 |    0 |    0 |    0 |    0 |     0 |
| MAPANDI MEMORIAL COLLEGE                                                              | Private       |     8 |    1 |    0 |    1 |    2 |    2 |    1 |    0 |    0 |    0 |     1 |
| UNIVERSITY OF NORTHERN PHILIPPINES VIGAN ILOCOS SUR                                   | Public        |     8 |    4 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |     0 |
| ENDERUN COLLEGE                                                                       | Private       |     8 |    2 |    1 |    1 |    1 |    0 |    1 |    1 |    1 |    0 |     0 |
| UNIVERSITY OF TEXAS                                                                   | Foreign       |     8 |    0 |    0 |    0 |    0 |    1 |    1 |    1 |    0 |    0 |     4 |
| FELIPE R. VERALLO MEMORIAL FOUNDATION - BOGO                                          | Private       |     8 |    0 |    1 |    0 |    0 |    1 |    0 |    1 |    2 |    2 |     1 |
| UNIVERSITY OF THE ASSUMPTION PAMPANGA                                                 | Private       |     8 |    0 |    3 |    1 |    0 |    1 |    0 |    0 |    0 |    3 |     0 |
| COLLEGE OF ST. JOHN - ROXAS                                                           | Private       |     8 |    2 |    2 |    0 |    1 |    1 |    0 |    1 |    0 |    0 |     0 |
| DELOS SANTOS COLLEGE                                                                  | Private       |     8 |    1 |    1 |    1 |    1 |    1 |    2 |    0 |    1 |    0 |     0 |
| SAFFRULLAH M. DIPATUAN FOUNDATION ACADEMY                                             | Private       |     7 |    2 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |    0 |     3 |
| ALDERSGATE COLLEGE                                                                    | Private       |     7 |    2 |    1 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |     2 |
| SAN SEBASTIAN COLLEGE                                                                 | Private       |     7 |    0 |    3 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |     0 |
| SAINT MARY'S COLLEGE OF SAN JUAN                                                      | Private       |     7 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| SAINT LOUIS COLLEGE                                                                   | Private       |     7 |    2 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |     1 |
| THE COLLEGE OF MAASIN                                                                 | Private       |     7 |    1 |    0 |    2 |    0 |    0 |    0 |    1 |    0 |    1 |     2 |
| SAINT LOUIS COLLEGE - CITY OF SAN FERNANDO                                            | Private       |     7 |    1 |    0 |    0 |    1 |    2 |    0 |    1 |    0 |    1 |     0 |
| WEST NEGROS COLLEGE BACOLOD                                                           | Private       |     7 |    3 |    1 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |     0 |
| ST. JOSEPH COLLEGE CAVITE                                                             | Private       |     7 |    3 |    1 |    0 |    0 |    2 |    1 |    0 |    0 |    0 |     0 |
| University Of Port Harcourt                                                           | Not Specified |     7 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    1 |     2 |
| COLLEGE OF THE IMMACULATE CONCEPTION                                                  | Private       |     7 |    2 |    1 |    0 |    0 |    2 |    1 |    0 |    0 |    0 |     1 |
| COTABATO MEDICAL FOUNDATION COLLEGE                                                   | Private       |     7 |    1 |    1 |    1 |    0 |    0 |    1 |    1 |    1 |    0 |     1 |
| 13155D                                                                                | Not Specified |     7 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    2 |    1 |     1 |
| CATANDUANES STATE COLLEGE                                                             | Public        |     7 |    4 |    0 |    1 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| NORTHEASTERN COLLEGE                                                                  | Private       |     7 |    1 |    0 |    1 |    0 |    1 |    1 |    0 |    1 |    0 |     1 |
| MALASIQUI AGNO VALLEY COLLEGE - MALASIQUI PANGASINAN                                  | Private       |     7 |    4 |    0 |    1 |    1 |    0 |    0 |    0 |    1 |    0 |     0 |
| MINDANAO UNIVERSITY OF SCIENCE AND TECHNOLOGY                                         | Public        |     7 |    0 |    1 |    1 |    0 |    1 |    1 |    1 |    1 |    1 |     0 |
| UNIVERSITY OF LUZON ( DAGUPAN CITY )                                                  | Private       |     7 |    3 |    0 |    2 |    1 |    1 |    0 |    0 |    0 |    0 |     0 |
| LA CONSOLACION COLLEGE - DAET                                                         | Private       |     7 |    0 |    2 |    0 |    0 |    0 |    1 |    1 |    0 |    1 |     2 |
| HOLY TRINITY COLLEGE PUERTO PRINCESA                                                  | Private       |     7 |    0 |    2 |    2 |    0 |    0 |    2 |    1 |    0 |    0 |     0 |
| DR. JOSE FABELLA MEMORIAL HOSPITAL SCHOOL OF MIDWIFERY                                | Private       |     7 |    0 |    0 |    1 |    1 |    1 |    0 |    0 |    1 |    1 |     2 |
| INTERNATIONAL COLLEGES OF ASIA - TAMBAC PANGASINAN                                    | Private       |     7 |    1 |    0 |    4 |    0 |    0 |    0 |    1 |    1 |    0 |     0 |
| KHON KAEN UNIVERSITY                                                                  | Foreign       |     7 |    1 |    2 |    0 |    0 |    2 |    0 |    0 |    1 |    0 |     1 |
| NAVAL STATE UNIVERSITY - MAIN                                                         | Public        |     7 |    0 |    1 |    0 |    2 |    0 |    0 |    0 |    1 |    2 |     1 |
| UNIVERSITY OF IMMACULATE CONCEPTION-DAVAO CITY                                        | Private       |     7 |    2 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |     0 |
| PANPACIFIC UNIVERSITY NORTH PHILIPPINES - URDANETA CITY                               | Private       |     7 |    1 |    1 |    0 |    1 |    1 |    0 |    1 |    1 |    1 |     0 |
| NEGROS ORIENTAL STATE UNIVERSITY                                                      | Public        |     7 |    2 |    3 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |     0 |
| UNIVERSITY OF CALIFORNIA MERCED                                                       | Foreign       |     7 |    1 |    0 |    1 |    0 |    2 |    1 |    1 |    1 |    0 |     0 |
| OLIVAREZ COLLEGE - TAGAYTAY                                                           | Private       |     7 |    0 |    1 |    2 |    0 |    1 |    0 |    0 |    1 |    1 |     1 |
| ST. BERNADETTE OF LOURDES COLLEGE                                                     | Private       |     6 |    1 |    1 |    0 |    0 |    0 |    2 |    1 |    1 |    0 |     0 |
| ASSUMPTION UNIVERSITY                                                                 | Foreign       |     6 |    0 |    0 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |     1 |
| ASIA-PACIFIC INTERNATIONAL UNIVERSITY                                                 | Private       |     6 |    0 |    0 |    0 |    1 |    1 |    0 |    2 |    1 |    0 |     0 |
| BATAAN PENINSULA STATE UNIVERSITY                                                     | Public        |     6 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    1 |     0 |
| BICOL COLLEGE                                                                         | Private       |     6 |    0 |    1 |    0 |    0 |    1 |    2 |    0 |    2 |    0 |     0 |
| ARRIESGADO COLLEGE FOUNDATION                                                         | Private       |     6 |    1 |    0 |    1 |    0 |    1 |    1 |    0 |    2 |    0 |     0 |
| Adventist University Of Indonesia                                                     | Not Specified |     6 |    1 |    0 |    0 |    1 |    1 |    0 |    0 |    2 |    0 |     1 |
| COLEGIO DE SAN LORENZO                                                                | Private       |     6 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    2 |     1 |
| COLEGIO DE KIDAPAWAN                                                                  | Private       |     6 |    0 |    1 |    0 |    0 |    1 |    1 |    0 |    1 |    1 |     1 |
| CHIANGMAI UNIVERSITY                                                                  | Foreign       |     6 |    0 |    0 |    2 |    1 |    0 |    0 |    0 |    1 |    0 |     2 |
| UNIVERSITY OF SOUTH FLORIDA USA                                                       | Foreign       |     6 |    0 |    1 |    1 |    0 |    1 |    1 |    1 |    0 |    1 |     0 |
| EAST AFRICA UNIVERSITY                                                                | Foreign       |     6 |    1 |    0 |    0 |    0 |    0 |    1 |    0 |    1 |    3 |     0 |
| DAVAO CENTRAL COLLEGE                                                                 | Private       |     6 |    1 |    0 |    0 |    1 |    1 |    0 |    0 |    1 |    1 |     0 |
| CALIFORNIA STATE UNIVERSITY - FULLERTON                                               | Foreign       |     6 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    4 |    1 |     0 |
| COR JESU COLLEGE                                                                      | Private       |     6 |    1 |    0 |    0 |    1 |    1 |    1 |    0 |    0 |    1 |     1 |
| EASTERN SAMAR STATE UNIVERSITY - MAIN                                                 | Public        |     6 |    1 |    0 |    0 |    0 |    0 |    3 |    0 |    0 |    1 |     1 |
| CONCORDIA COLLEGE                                                                     | Private       |     6 |    0 |    2 |    0 |    0 |    3 |    0 |    1 |    0 |    0 |     0 |
| UNIVERSITY OF MARYLAND - MARYLAND U.S.A.                                              | Foreign       |     6 |    0 |    0 |    1 |    1 |    1 |    0 |    0 |    1 |    1 |     1 |
| SAN ISIDRO COLLEGE                                                                    | Private       |     6 |    1 |    1 |    0 |    2 |    1 |    0 |    0 |    0 |    0 |     1 |
| ST. ANTHONY COLLEGE OF ROXAS CITY CAPIZ                                               | Private       |     6 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    1 |    0 |     0 |
| ST. JOSEPH COLLEGE AMAYA                                                              | Private       |     6 |    1 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |    2 |     1 |
| AMA COMPUTER COLLEGE - TUGUEGARAO CITY                                                | Private       |     6 |    0 |    0 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |     1 |
| AGO MEDICAL EDUCATIONAL FOUNDATION LEGASPI CITY                                       | Private       |     6 |    0 |    2 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |     0 |
| ANGELES SYSTEMS PLUS COMPUTER COLLEGE                                                 | Private       |     6 |    0 |    1 |    1 |    1 |    2 |    0 |    0 |    0 |    0 |     1 |
| ST. MARY'S UNIVERSITY NUEVA VIZCAYA                                                   | Private       |     6 |    0 |    3 |    0 |    1 |    1 |    0 |    1 |    0 |    0 |     0 |
| SOUTHERN LUZON POLYTECHNIC COLLEGE - LUCBAN QUEZON                                    | Private       |     6 |    1 |    1 |    1 |    3 |    0 |    0 |    0 |    0 |    0 |     0 |
| SAN DIEGO STATE UNIVERSITY - CALIFORNIA U.S.A.                                        | Foreign       |     6 |    0 |    1 |    0 |    1 |    0 |    2 |    1 |    1 |    0 |     0 |
| THE NATIONAL TEACHERS COLLEGE                                                         | Private       |     6 |    1 |    1 |    0 |    0 |    0 |    0 |    1 |    1 |    0 |     2 |
| PAMANTASAN NG LUNGSOD NG MUNTINLUPA                                                   | Public        |     6 |    0 |    1 |    1 |    0 |    1 |    0 |    1 |    1 |    1 |     0 |
| RUNGSIT UNIVERSITY                                                                    | Foreign       |     6 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |     2 |
| UNIVERSITY AT BUFFALO                                                                 | Foreign       |     6 |    1 |    0 |    0 |    1 |    1 |    0 |    1 |    0 |    0 |     1 |
| Qiqihar Medical University                                                            | Not Specified |     6 |    2 |    2 |    1 |    0 |    0 |    1 |    0 |    0 |    0 |     0 |
| LADOKE AKINTOLA UNIVERSITY OF TECHNOLOGY OGBOMOSO                                     | Foreign       |     6 |    2 |    1 |    1 |    0 |    0 |    1 |    0 |    1 |    0 |     0 |
| LEYTE NORMAL UNIVERSITY TACLOBAN CITY                                                 | Public        |     6 |    2 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |     0 |
| MAHARDIKA INSTITUTE OF TECHNOLOGY                                                     | Private       |     6 |    1 |    0 |    1 |    0 |    0 |    1 |    1 |    1 |    1 |     0 |
| KESTER GRANT COLLEGE PHILS. INC.                                                      | Private       |     6 |    1 |    3 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |     0 |
| NOVAGEN COLLEGE OF QUEZON CITY                                                        | Private       |     6 |    3 |    0 |    1 |    0 |    0 |    1 |    0 |    1 |    0 |     0 |
| UNIVERSITY OF HOUSTON                                                                 | Foreign       |     6 |    2 |    0 |    0 |    1 |    0 |    0 |    1 |    0 |    2 |     0 |
| PHILIPPINE NORMAL UNIVERSITY - AGUSAN                                                 | Public        |     6 |    0 |    1 |    1 |    1 |    1 |    0 |    1 |    0 |    1 |     0 |
| OUR LADY OF FATIMA NOVALICHES                                                         | Private       |     6 |    0 |    3 |    1 |    0 |    0 |    1 |    1 |    0 |    0 |     0 |
| OUR LADY OF THE PILLAR COLLEGE - CAUAYAN                                              | Private       |     6 |    2 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    1 |     0 |
| Christian University Of Thailand                                                      | Not Specified |     6 |    0 |    1 |    0 |    2 |    1 |    0 |    0 |    0 |    0 |     0 |
| LYCEUM NORTHWESTERN - FLORENCIA T. DUQUE COLLEGE                                      | Private       |     6 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |     0 |
| MAHASARAKHAM UNIVERSITY                                                               | Foreign       |     6 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |     0 |
| KASETSART UNIVERSITY                                                                  | Foreign       |     6 |    1 |    2 |    0 |    0 |    0 |    1 |    0 |    0 |    0 |     1 |
| RAMKHAMHAENG UNIV.                                                                    | Foreign       |     5 |    5 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     0 |
| SRI CHAITANYA JUNIOR COLLEGE                                                          | Foreign       |     5 |    1 |    0 |    0 |    1 |    0 |    1 |    0 |    2 |    0 |     0 |
| SUNRISE UNIVERSITY                                                                    | Foreign       |     5 |    1 |    0 |    0 |    1 |    1 |    1 |    0 |    1 |    0 |     0 |
| Sti - College Davao                                                                   | Not Specified |     5 |    2 |    1 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |     0 |
| AMA SCHOOL OF MEDICINE - EAST RIZAL                                                   | Private       |     5 |    2 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |     2 |
| SAINT PAUL COLLEGE FOUNDATION                                                         | Private       |     5 |    0 |    0 |    1 |    0 |    0 |    3 |    1 |    0 |    0 |     0 |
| SAINT MICHAEL'S COLLEGE OF LAGUNA                                                     | Private       |     5 |    0 |    1 |    0 |    0 |    1 |    1 |    0 |    0 |    1 |     1 |
| UNIV. OF ASIA AND THE PACIFIC - PASIG CITY                                            | Private       |     5 |    0 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    2 |     1 |
| RUTGERS COLLEGE NEW JERSEY                                                            | Foreign       |     5 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |    1 |     3 |
| TEMPLE UNIVERSITY USA                                                                 | Foreign       |     5 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |    1 |    1 |     0 |
| SIAM UNIVERSITY                                                                       | Foreign       |     5 |    3 |    0 |    0 |    0 |    0 |    1 |    0 |    0 |    1 |     0 |
| TRACE COLLEGE                                                                         | Private       |     5 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    2 |    1 |     0 |
| TECHNOLOGICAL UNIVERSITY OF THE PHILIPPINES - AYALA BLVD. MANILA                      | Public        |     5 |    1 |    0 |    0 |    0 |    2 |    1 |    0 |    0 |    0 |     0 |
| SIENA COLLEGE-TAYTAY                                                                  | Private       |     5 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |     1 |
| ADVENTIST INDONESIA UNIVERSITY INDONESIA                                              | Foreign       |     5 |    2 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     0 |
| AKLAN POLYTECHNIC COLLEGE                                                             | Private       |     5 |    1 |    1 |    0 |    0 |    0 |    1 |    0 |    0 |    1 |     1 |
| ST. ANDREW'S INTERNATIONAL ACADEMY INDIA                                              | Foreign       |     5 |    3 |    0 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |     0 |
| PALAWAN POLYTECHNIC COLLEGE                                                           | Private       |     5 |    1 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |    1 |     0 |
| UNIVERSITY OF CONNECTICUT                                                             | Foreign       |     5 |    0 |    1 |    0 |    0 |    2 |    0 |    0 |    1 |    0 |     1 |
| NEW SINAI SCHOOL AND COLLEGES STA. ROSA                                               | Private       |     5 |    0 |    0 |    1 |    2 |    0 |    1 |    0 |    0 |    0 |     0 |
| LIPA CITY COLLEGES BATANGAS                                                           | Private       |     5 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    1 |    0 |     0 |
| LUNA GOCO COLLEGES                                                                    | Private       |     5 |    0 |    1 |    0 |    1 |    0 |    0 |    1 |    0 |    2 |     0 |
| NEW YORK UNIVERSITY NY USA                                                            | Foreign       |     5 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    2 |     2 |
| MOGADISHU UNIVERSITY                                                                  | Foreign       |     5 |    1 |    0 |    0 |    1 |    0 |    1 |    2 |    0 |    0 |     0 |
| UNIVERSITY OF NEW ENGLAND                                                             | Foreign       |     5 |    1 |    1 |    0 |    0 |    1 |    1 |    0 |    0 |    0 |     1 |
| UNIVERSITY OF NEVADA - RENO                                                           | Foreign       |     5 |    0 |    1 |    1 |    0 |    0 |    1 |    0 |    0 |    0 |     1 |
| UNIVERSITY OF MICHIGAN                                                                | Foreign       |     5 |    0 |    0 |    0 |    0 |    1 |    0 |    1 |    2 |    1 |     0 |
| UNIVERSITY OF NORTHERN PHILIPPINES-CANDON - CITY OF CANDON ILOCOS SUR                 | Public        |     5 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     0 |
| UNIVERSITY OF CEBU                                                                    | Private       |     5 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    0 |    1 |     0 |
| UNIVERSITY OF CALOOCAN CITY                                                           | Public        |     5 |    0 |    1 |    0 |    2 |    0 |    0 |    0 |    0 |    1 |     1 |
| PENSACOLA CHRISTIAN COLLEGE                                                           | Foreign       |     5 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |     2 |
| UNIVERSITY OF BRITISH COLUMBIA CANADA                                                 | Foreign       |     5 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |    0 |    0 |     4 |
| PAMPANGA AGRICULTURAL COLLEGE                                                         | Public        |     5 |    1 |    1 |    0 |    1 |    0 |    1 |    0 |    0 |    0 |     0 |
| KHON KAEN UNIVERSITY THAILAND                                                         | Foreign       |     5 |    1 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |     0 |
| FEU - FERN COLLEGE                                                                    | Private       |     5 |    0 |    2 |    0 |    0 |    1 |    0 |    1 |    1 |    0 |     0 |
| DR. DOMINGO B. TAMONDONG MEMORIAL SCHOOL                                              | Private       |     5 |    0 |    0 |    2 |    1 |    0 |    0 |    0 |    1 |    1 |     0 |
| UNIVERSITY OF THE IMMACULATE CONCEPTION COLLEGE DAVAO                                 | Private       |     5 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     0 |
| UNIVERSITY OF TEXAS AT ARLINGTON                                                      | Foreign       |     5 |    2 |    1 |    0 |    0 |    0 |    1 |    0 |    0 |    0 |     1 |
| EULOGIO AMANG RODRIGUEZ INSTITUTE OF SCIENCE AND TECHNOLOGY                           | Public        |     5 |    0 |    1 |    0 |    0 |    1 |    0 |    0 |    2 |    0 |     0 |
| KITASATO UNIVERSITY                                                                   | Foreign       |     5 |    0 |    0 |    0 |    1 |    0 |    2 |    0 |    0 |    1 |     1 |
| ILOCOS SUR POLYTECHNIC STATE COLLEGE                                                  | Public        |     5 |    0 |    0 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |     0 |
| FL VARGAS COLLEGE - TUGUEGARAO                                                        | Private       |     5 |    0 |    2 |    1 |    0 |    0 |    1 |    0 |    0 |    1 |     0 |
| COLEGIO DE SAN JUAN DE LETRAN MANILA                                                  | Private       |     5 |    0 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    1 |     0 |
| CHAING MAI UNIVERSITY-THAILAND                                                        | Foreign       |     5 |    1 |    1 |    1 |    0 |    0 |    1 |    0 |    0 |    0 |     0 |
| CAVITE STATE UNIVERSITY CAVITE                                                        | Public        |     5 |    0 |    0 |    1 |    1 |    0 |    1 |    0 |    1 |    0 |     1 |
| CENTRAL COLLEGE OF PANGASINAN - SAN CARLOS CITY PANGASINAN                            | Private       |     5 |    0 |    0 |    0 |    2 |    1 |    0 |    0 |    2 |    0 |     0 |
| CAGAYAN DE ORO COLLEGE                                                                | Private       |     5 |    2 |    0 |    0 |    1 |    0 |    0 |    1 |    1 |    0 |     0 |
| BATANGAS STATE UNIVERSITY BATANGAS CITY                                               | Public        |     5 |    0 |    0 |    2 |    0 |    1 |    0 |    1 |    0 |    0 |     1 |
| ARIZONA STATE UNIVERSITY                                                              | Foreign       |     5 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |    2 |     0 |
| ASIAN COLLEGE OF SCIENCE AND TECHNOLOGY - CUBAO                                       | Private       |     5 |    0 |    0 |    0 |    0 |    2 |    0 |    1 |    0 |    1 |     1 |
| UNIVERSITY OF WISCONSIN-MADISON                                                       | Foreign       |     5 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |    0 |     3 |
| 13206A                                                                                | Not Specified |     5 |    0 |    0 |    0 |    0 |    2 |    1 |    0 |    1 |    1 |     0 |

---

*Source: NMAT_Exodus.parquet (Pipeline 4). Observable best-record cohort (Year <= 2014) used for all PLE-linked summaries to avoid misclassifying later cohorts as non-passers before their licensure window closes.*
