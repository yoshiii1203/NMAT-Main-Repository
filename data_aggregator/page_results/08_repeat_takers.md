# Page 8: Repeat-Taker Patterns and Score Change

**Generated:** 2026-08-14 16:58

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `trend (2006-2018, unfiltered)`

**Filters:** None (full unfiltered dataset)

---

## 1. Attempt Count Distribution

Number of unique NMAT applications per PERSON_KEY in the trend cohort.

**Table 31. Attempt-count distribution**

|   Attempts |   Count |   Percent |   CumulativePercent |
|-----------:|--------:|----------:|--------------------:|
|          1 |  101156 |        75 |                  75 |
|          2 |   25812 |     19.14 |               94.14 |
|          3 |    6046 |      4.48 |               98.62 |
|          4 |    1411 |      1.05 |               99.67 |
|          5 |     332 |      0.25 |               99.92 |
|          6 |      88 |      0.07 |               99.99 |
|          7 |      17 |      0.01 |                 100 |
|          8 |       6 |         0 |                 100 |
|          9 |       1 |         0 |                 100 |


Figure data: each row shows the number of persons with that many recorded NMAT attempts.


---

## 2. Repeat-Taker Summary

**Repeat-taker overview**

| Indicator                     |   Value |
|:------------------------------|--------:|
| Unique persons (PERSON_KEY)   |  134869 |
| Repeat takers (>1 attempt)    |   33713 |
| Repeat rate (%)               |      25 |
| Max attempts observed         |       9 |
| Mean attempts (all persons)   |    1.33 |
| Median attempts (all persons) |       1 |


---

## 3. Score Improvement: First vs Last Attempt

Among repeat takers with score data on both first and last attempt.

**Table 32. Repeat-taker trajectory summary**

| Indicator                       |   Value |
|:--------------------------------|--------:|
| Repeat-taker persons (analytic) |   33702 |
| Improved percentile rank (%)    |   77.65 |
| Improved raw score (%)          |   73.58 |
| Improved GPS (%)                |   78.83 |
| Median percentile change        |      11 |
| Median raw score change         |      12 |
| Median GPS change               |      46 |
| Mean percentile change          |   13.52 |
| Mean raw score change           |   13.15 |
| Mean GPS change                 |   47.29 |
| Q25 percentile change           |       2 |
| Q75 percentile change           |      25 |
| Q25 raw score change            |       0 |
| Q75 raw score change            |      26 |



### First-Last Detail (per person)

**Preview: first 100 of 33,702 rows (population: repeat takers with score data on both first and last attempt, n=33,702)**

| PERSON_KEY                                      |   n_attempts |   first_year |   last_year |   first_pct |   last_pct |   pct_improvement |   first_raw |   last_raw |   raw_improvement |   first_gps |   last_gps |   gps_improvement |
|:------------------------------------------------|-------------:|-------------:|------------:|------------:|-----------:|------------------:|------------:|-----------:|------------------:|------------:|-----------:|------------------:|
| ANGLOPEZ, MAE THERESE DE JOSE||                 |            2 |         2009 |        2010 |           0 |         94 |                94 |         189 |        189 |                 0 |           0 |        658 |               658 |
| SAAYA SANTHOSH||04/19/1996                      |            2 |         2016 |        2017 |          -1 |         88 |                89 |          51 |        170 |               119 |         200 |        615 |               415 |
| STO DOMINGO, WEIJIN N A||06/20/1994             |            2 |         2013 |        2013 |          12 |         99 |                87 |          96 |        184 |                88 |         383 |        723 |               340 |
| CEREZO, HARRY JOHN||                            |            2 |         2009 |        2010 |           0 |         87 |                87 |         176 |        176 |                 0 |           0 |        613 |               613 |
| ADECER, HANICOLE MORTIZ||                       |            2 |         2007 |        2008 |           7 |         93 |                86 |          78 |        178 |               100 |         355 |        645 |               290 |
| KOTHURU, PENIEL GOSPEL GLORY,||7/6/1996         |            2 |         2014 |        2015 |           3 |         87 |                84 |          74 |        160 |                86 |         316 |        615 |               299 |
| VILLENA, MICHAEL BERNARD SALUD||11/2/1995       |            6 |         2013 |        2017 |           2 |         85 |                83 |          72 |        165 |                93 |         302 |        602 |               300 |
| AUSTRIA, RITA ISABELLE TALAVERA||5/5/1994       |            3 |         2013 |        2014 |          15 |         98 |                83 |          92 |        171 |                79 |         398 |        708 |               310 |
| MAHESH JESU RAJA, ALLEN ROJER||09/24/1996       |            2 |         2015 |        2015 |           1 |         84 |                83 |          64 |        141 |                77 |         243 |        597 |               354 |
| ANUKU, EDNA OMAMUYOVWI||3/5/1976                |            3 |         2016 |        2018 |           6 |         89 |                83 |          75 |        148 |                73 |         347 |        622 |               275 |
| VINARAO, QUERUBIN JADE OLANGCO||7/1/1993        |            3 |         2013 |        2014 |           5 |         88 |                83 |          80 |        146 |                66 |         337 |        618 |               281 |
| GADHAVI, LAKHAMA MANGABHAI||11/8/1993           |            3 |         2014 |        2015 |           1 |         82 |                81 |          66 |        153 |                87 |         264 |        592 |               328 |
| JONGRATANAVANICH, WATCHARAPORN||1/4/1984        |            3 |         2012 |        2014 |           4 |         85 |                81 |          78 |        142 |                64 |         327 |        603 |               276 |
| PRADO, JOSE PAOLO BARAWID||06/18/1994           |            2 |         2013 |        2014 |          10 |         91 |                81 |          87 |        150 |                63 |         373 |        635 |               262 |
| SINGH, SHRISTI||9/7/1995                        |            2 |         2014 |        2015 |          -1 |         79 |                80 |          55 |        150 |                95 |         212 |        582 |               370 |
| THAMBI, PRIYANKA USHA||05/19/1992               |            3 |         2011 |        2013 |           1 |         81 |                80 |          62 |        152 |                90 |         271 |        589 |               318 |
| BAMBHAROLIYA, VIVEK BIPINBHAI||10/24/1994       |            5 |         2013 |        2017 |           6 |         86 |                80 |          81 |        168 |                87 |         348 |        610 |               262 |
| ANSARI, SAJJAD HUSSAIN||04/15/1995              |            2 |         2017 |        2018 |           4 |         84 |                80 |          83 |        142 |                59 |         322 |        599 |               277 |
| CHAUDHARY, ANIL JESUNGBHAI||08/26/1994          |            6 |         2014 |        2017 |           4 |         83 |                79 |          73 |        164 |                91 |         321 |        597 |               276 |
| PATEL, NENSI HASMUKHBHAI||12/28/1997            |            3 |         2016 |        2017 |           1 |         80 |                79 |          73 |        159 |                86 |         275 |        583 |               308 |
| VENKATASAMY, ELAVARASAN||01/21/1998             |            2 |         2015 |        2015 |           2 |         81 |                79 |          74 |        137 |                63 |         293 |        586 |               293 |
| REKHA, PRAVARDHINI REDDY||05/31/1994            |            2 |         2014 |        2015 |           1 |         79 |                78 |          65 |        150 |                85 |         259 |        582 |               323 |
| THAKKAR, KARAN SURESHKUMAR||6/9/1996            |            2 |         2014 |        2015 |           3 |         81 |                78 |          71 |        153 |                82 |         307 |        589 |               282 |
| AGUILERA, EARIC SY||7/7/1995                    |            5 |         2015 |        2017 |           7 |         85 |                78 |          87 |        166 |                79 |         352 |        604 |               252 |
| HABILING, KAVIN BIDANG||05/18/1992              |            6 |         2012 |        2015 |          14 |         92 |                78 |          91 |        168 |                77 |         393 |        639 |               246 |
| VALLABHANENI, SWETHA||1/10/1996                 |            2 |         2015 |        2015 |           5 |         83 |                78 |          84 |        140 |                56 |         333 |        594 |               261 |
| GAMOT, SANDESH LALIT||08/15/1992                |            2 |         2013 |        2015 |          12 |         89 |                77 |          89 |        164 |                75 |         383 |        625 |               242 |
| GARANIYA, VISHAL BAHADURBHAI||03/24/1996        |            3 |         2014 |        2015 |           3 |         80 |                77 |          75 |        136 |                61 |         310 |        583 |               273 |
| RAJKUMAR, GIFTSON JOHN||03/29/1997              |            2 |         2015 |        2015 |           1 |         78 |                77 |          73 |        134 |                61 |         280 |        577 |               297 |
| LEE, JI HWAN||4/1/1999                          |            2 |         2017 |        2018 |          14 |         91 |                77 |          99 |        152 |                53 |         391 |        635 |               244 |
| ESCUETA, ALEXANDRIA VILLARICO||10/15/1993       |            4 |         2013 |        2015 |           2 |         78 |                76 |          75 |        148 |                73 |         293 |        579 |               286 |
| JAIN, SHUBHAM SUNIL||05/21/1996                 |            2 |         2015 |        2015 |          -1 |         75 |                76 |          60 |        131 |                71 |         212 |        568 |               356 |
| GANDLA, SUDHEER KUMAR||9/6/1989                 |            2 |         2010 |        2012 |           6 |         82 |                76 |          83 |        140 |                57 |         345 |        592 |               247 |
| BELIM, FATIMA ABDULKARIM||05/13/1997            |            2 |         2016 |        2017 |           1 |         76 |                75 |          61 |        154 |                93 |         274 |        572 |               298 |
| DEQUITO, KRISTEL JOY LINAO||5/9/1994            |            4 |         2015 |        2017 |           3 |         78 |                75 |          66 |        156 |                90 |         304 |        578 |               274 |
| KARANAM, LALITHA SAI SREE||2/8/1996             |            3 |         2014 |        2015 |           1 |         76 |                75 |          65 |        147 |                82 |         259 |        572 |               313 |
| MACATIGUE, MONIQUE BANTUG||12/17/1992           |            2 |         2012 |        2017 |           5 |         80 |                75 |          79 |        158 |                79 |         333 |        585 |               252 |
| RAJULAPATI, GOVINDARAJA||05/13/1996             |            3 |         2014 |        2015 |           2 |         77 |                75 |          70 |        147 |                77 |         288 |        575 |               287 |
| THAKOR, JAIMINI GULABSINH||09/22/1996           |            2 |         2014 |        2015 |           7 |         82 |                75 |          78 |        153 |                75 |         352 |        592 |               240 |
| KOPPOLU, SOWMITRA PALLAV||08/29/1993            |            3 |         2014 |        2015 |          -1 |         74 |                75 |          56 |        130 |                74 |         200 |        565 |               365 |
| BELLAMKONDA, AJAY KUMAR||9/8/1994               |            2 |         2012 |        2013 |           4 |         79 |                75 |          77 |        140 |                63 |         321 |        582 |               261 |
| BEARIS, NIKKI JILL NIEVA||06/30/1993            |            2 |         2013 |        2014 |           9 |         84 |                75 |          86 |        142 |                56 |         368 |        599 |               231 |
| DIALOGO, AL GIAN MENDOZA||08/31/1993            |            2 |         2014 |        2015 |           9 |         84 |                75 |          85 |        141 |                56 |         368 |        597 |               229 |
| BERNASOL, SANTIA LOUISE YABUT||10/6/1992        |            2 |         2013 |        2014 |          13 |         88 |                75 |          90 |        145 |                55 |         388 |        618 |               230 |
| MANZANO, ALLEN JANE BLANDO||3/1/1994            |            2 |         2016 |        2017 |          10 |         84 |                74 |          80 |        164 |                84 |         370 |        599 |               229 |
| KARANAM, HARSHA JEEVAN KISHORE||2/8/1996        |            3 |         2014 |        2015 |           9 |         83 |                74 |          85 |        155 |                70 |         363 |        596 |               233 |
| KURLI, RAJEEV REDDY||10/8/1995                  |            3 |         2014 |        2015 |          10 |         84 |                74 |          87 |        155 |                68 |         373 |        599 |               226 |
| BOMMA REDDY, SAI SRI KRISHNA REDDY||5/1/1996    |            2 |         2014 |        2014 |           1 |         75 |                74 |          69 |        130 |                61 |         280 |        568 |               288 |
| CRUZ, JOHN PAUL MAGHIRANG||11/12/1992           |            2 |         2012 |        2013 |           8 |         82 |                74 |          84 |        144 |                60 |         357 |        592 |               235 |
| DIVINAGRACIA, BRIAN JOHN DIAZ||11/4/1992        |            2 |         2012 |        2014 |          18 |         92 |                74 |          94 |        151 |                57 |         407 |        639 |               232 |
| HIDALGO, JEDD JOSE MICKAEL MADRONIO||01/21/1993 |            3 |         2013 |        2015 |           9 |         83 |                74 |          85 |        140 |                55 |         363 |        594 |               231 |
| GATDULA, EMANUEL FETIZA||11/28/1992             |            2 |         2013 |        2015 |          18 |         91 |                73 |          94 |        168 |                74 |         407 |        635 |               228 |
| MARQUINO, ALYANA FRANCESCA BAUTISTA||3/4/1995   |            3 |         2014 |        2015 |          18 |         91 |                73 |          94 |        165 |                71 |         407 |        632 |               225 |
| PACKIAMUTHU, PRISHKA||06/15/1997                |            2 |         2015 |        2015 |          -1 |         72 |                73 |          57 |        128 |                71 |         200 |        559 |               359 |
| DY, FRECHELLE LAINE TACTAY||12/11/1991          |            2 |         2012 |        2013 |           6 |         79 |                73 |          81 |        150 |                69 |         343 |        582 |               239 |
| KATTA, REVANTH||03/25/1996                      |            2 |         2014 |        2015 |           6 |         79 |                73 |          82 |        150 |                68 |         348 |        582 |               234 |
| BORRA, RAVALI||01/28/1996                       |            2 |         2015 |        2015 |          18 |         91 |                73 |         100 |        153 |                53 |         407 |        633 |               226 |
| GERONIMO, MONA LEIGH LEVISTE||03/24/1992        |            5 |         2011 |        2013 |          27 |         99 |                72 |         105 |        197 |                92 |         439 |        726 |               287 |
| VYAS, SMIT NILESHKUMAR||07/31/1995              |            2 |         2014 |        2015 |          -1 |         71 |                72 |          57 |        143 |                86 |         212 |        557 |               345 |
| BAWANKAR, SUMIT SUNIL||12/11/1994               |            3 |         2016 |        2017 |           8 |         80 |                72 |          90 |        160 |                70 |         356 |        585 |               229 |
| TUMAMPOS, BEA DESIREE DE LEON||8/9/1993         |            2 |         2012 |        2014 |          23 |         95 |                72 |          98 |        159 |                61 |         425 |        663 |               238 |
| ALCAZAREN, PETERSIAN MAGSULIT||2/9/1993         |            3 |         2012 |        2014 |          21 |         93 |                72 |          97 |        155 |                58 |         420 |        645 |               225 |
| BEERAM, SHIRISHA||11/12/1992                    |            2 |         2014 |        2014 |           5 |         77 |                72 |          79 |        134 |                55 |         333 |        575 |               242 |
| VALA, JAYDIP KALA||11/29/1999                   |            2 |         2017 |        2018 |           6 |         78 |                72 |          89 |        136 |                47 |         347 |        579 |               232 |
| PILAPIL, LUCILLE PILLAR DESCALLAR||9/10/1995    |            2 |         2016 |        2017 |          26 |         97 |                71 |          97 |        191 |                94 |         435 |        686 |               251 |
| JIMENEZ, RUFFA DAWN OLIVA||05/22/1994           |            2 |         2015 |        2016 |           2 |         73 |                71 |          63 |        152 |                89 |         286 |        560 |               274 |
| ASPIRAS, JENNIFER SIGRID PERALTA||7/6/1995      |            3 |         2015 |        2017 |           2 |         73 |                71 |          64 |        151 |                87 |         292 |        560 |               268 |
| CUEVA, JEMELA MAXINE DELA CRUZ||6/2/1995        |            3 |         2015 |        2017 |           2 |         73 |                71 |          64 |        151 |                87 |         292 |        562 |               270 |
| TAN, RAINEER ALAINE JAY CAPCO||9/12/1996        |            2 |         2016 |        2017 |           3 |         74 |                71 |          68 |        152 |                84 |         313 |        565 |               252 |
| ARMENDARES, YOCHA BELLE PAGTANAC||06/28/1994    |            3 |         2015 |        2017 |           8 |         79 |                71 |          76 |        158 |                82 |         357 |        580 |               223 |
| BELADIYA, MAHIPAL KISHORBHAI||10/29/1994        |            5 |         2013 |        2017 |           3 |         74 |                71 |          72 |        152 |                80 |         307 |        565 |               258 |
| BHELE, TRISHA||1/10/1993                        |            2 |         2012 |        2013 |           2 |         73 |                71 |          70 |        142 |                72 |         288 |        560 |               272 |
| OBALDO, JEZREEL MAE JIMENEZ||02/20/1996         |            3 |         2016 |        2018 |          17 |         88 |                71 |          89 |        161 |                72 |         406 |        620 |               214 |
| PETER, LIDIYA||10/8/1996                        |            2 |         2015 |        2015 |          -1 |         70 |                71 |          60 |        126 |                66 |         212 |        552 |               340 |
| COMENDADOR, MAIU LIWEN BURDIOS||6/5/1992        |            3 |         2013 |        2018 |           5 |         76 |                71 |          79 |        134 |                55 |         337 |        572 |               235 |
| MANGROBANG, RAUL JR RAMOS||6/9/1993             |            2 |         2013 |        2013 |          16 |         87 |                71 |          98 |        151 |                53 |         402 |        615 |               213 |
| GANTA, RAVITEJA||10/6/1995                      |            2 |         2014 |        2014 |          10 |         81 |                71 |          87 |        138 |                51 |         373 |        589 |               216 |
| ONG, CINDY LIU||01/31/1992                      |            3 |         2013 |        2014 |           3 |         74 |                71 |          82 |        132 |                50 |         316 |        564 |               248 |
| PATIL, SUBODH PANKAJ||8/3/1997                  |            2 |         2017 |        2018 |          21 |         92 |                71 |         106 |        153 |                47 |         421 |        639 |               218 |
| VADDEBOINA, SAI KRISHNA GOWD||05/14/1996        |            2 |         2015 |        2015 |           9 |         80 |                71 |          90 |        136 |                46 |         363 |        583 |               220 |
| DE LEON, CLAUDETTE PEARL||10/4/1995             |            3 |         2015 |        2017 |           4 |         74 |                70 |          70 |        152 |                82 |         328 |        565 |               237 |
| REGIS, REINA KATRINA SIEGA||01/21/1995          |            2 |         2016 |        2017 |          10 |         80 |                70 |          80 |        157 |                77 |         370 |        583 |               213 |
| INOCENCIO, MAY ANNE SEBELO||05/25/1995          |            3 |         2015 |        2016 |           3 |         73 |                70 |          79 |        152 |                73 |         310 |        560 |               250 |
| BUTRON, GEA CASTRO||4/9/1995                    |            2 |         2016 |        2018 |          26 |         96 |                70 |          97 |        163 |                66 |         435 |        673 |               238 |
| KORRA, BHASKAR NAIK||06/15/1992                 |            2 |         2014 |        2014 |           3 |         73 |                70 |          74 |        129 |                55 |         307 |        560 |               253 |
| GUNREDDY, MAMATHA REDDY||3/10/1995              |            2 |         2014 |        2014 |           7 |         77 |                70 |          83 |        135 |                52 |         352 |        575 |               223 |
| JADEJA, KULDIPSINH RANCHHODJI||1/9/1995         |            2 |         2013 |        2014 |          10 |         80 |                70 |          87 |        138 |                51 |         373 |        585 |               212 |
| VENNU, DIVYA||8/6/1996                          |            2 |         2015 |        2015 |          11 |         81 |                70 |          95 |        138 |                43 |         378 |        589 |               211 |
| CABANES, EENA ROSELLE TAN||05/17/1995           |            4 |         2015 |        2017 |          19 |         88 |                69 |          87 |        170 |                83 |         412 |        615 |               203 |
| OROPEL, ABBY GALE QUIMPO||05/26/1995            |            2 |         2015 |        2017 |          17 |         86 |                69 |          85 |        167 |                82 |         403 |        607 |               204 |
| GUGAR, CHANDRA PRAKASH||10/12/1998              |            2 |         2016 |        2017 |           9 |         78 |                69 |          79 |        157 |                78 |         366 |        578 |               212 |
| LAKHANI, ARMAN SHAUKATBHAI||07/27/1996          |            4 |         2015 |        2017 |          11 |         80 |                69 |          80 |        157 |                77 |         378 |        583 |               205 |
| DHAPA, YASHVANT MEGHJIBHAI||07/29/1993          |            2 |         2012 |        2013 |           2 |         71 |                69 |          70 |        143 |                73 |         288 |        557 |               269 |
| VIRTUSIO, GIAN HARLHEY BELARMINO||06/27/1995    |            2 |         2015 |        2016 |          10 |         79 |                69 |          93 |        159 |                66 |         373 |        580 |               207 |
| FRONDA, PRECIOUS MARLYNNE NOBLE||12/1/1992      |            2 |         2012 |        2013 |          12 |         81 |                69 |          89 |        152 |                63 |         383 |        589 |               206 |
| VITTO, HANNAH LERI LUMANGLAS||09/14/1992        |            3 |         2014 |        2015 |          10 |         79 |                69 |          87 |        150 |                63 |         373 |        582 |               209 |
| LABAY, ANGELO VIOLO GO||05/21/1993              |            3 |         2012 |        2014 |          23 |         92 |                69 |          98 |        153 |                55 |         425 |        639 |               214 |
| REYES, LOUISA CARMINA REJANO||8/2/1994          |            3 |         2013 |        2015 |          16 |         85 |                69 |         100 |        154 |                54 |         402 |        603 |               201 |
| GAUTAM, BIBEK||5/6/1992                         |            3 |         2012 |        2015 |           6 |         75 |                69 |          81 |        131 |                50 |         343 |        568 |               225 |
| VIRPARIA, DARVIN GIRISHBHAI||08/14/1996         |            2 |         2015 |        2015 |           3 |         72 |                69 |          79 |        128 |                49 |         310 |        559 |               249 |

> Full detail: [08_first_last_detail.csv](08_first_last_detail.csv) (33,702 rows, 13 cols)


---

## 4. Distribution of Attempt Counts by Year

For each test year, the number of persons with 1, 2, 3, ... attempts in that year.

**Attempt counts per year**

|   Year |   1 attempt(s) |   2 attempt(s) |   total_persons |
|-------:|---------------:|---------------:|----------------:|
|   2006 |           3860 |            258 |            4118 |
|   2007 |           4101 |            277 |            4378 |
|   2008 |           5410 |            355 |            5765 |
|   2009 |           7312 |            525 |            7837 |
|   2010 |          10008 |            276 |           10284 |
|   2011 |          10593 |            668 |           11261 |
|   2012 |          11626 |            847 |           12473 |
|   2013 |          12034 |            977 |           13011 |
|   2014 |          12309 |           1262 |           13571 |
|   2015 |          13590 |           1347 |           14937 |
|   2016 |          16034 |           2467 |           18501 |
|   2017 |          25870 |              0 |           25870 |
|   2018 |          19825 |           3918 |           23743 |


---

## 5. Repeat-Taker Detail (All Attempts)

All recorded attempts for persons with more than one NMAT application.

**Preview: first 100 rows**

| PERSON_KEY                                        |   APPNO_CLEAN |   Year |   TotalRawScoreTRUE |   NMS_PER_num |   NMS_GPS |   PartIRawScoreTRUE |   PartIIRawScoreTRUE | PercentileBin   | PLE_STATUS_LABEL       | UNDERGRAD_UNI_TYPE   | UNDERGRAD_COURSE_GROUP       |
|:--------------------------------------------------|--------------:|-------:|--------------------:|--------------:|----------:|--------------------:|---------------------:|:----------------|:-----------------------|:---------------------|:-----------------------------|
| AARE, VYSHNAVI||11/1/1996                         |    1041607270 |   2016 |                  90 |             8 |       356 |                  46 |                   44 | B1              | No confirmed PLE match | Private              | Natural Sciences             |
| AARE, VYSHNAVI||11/1/1996                         |    1101605950 |   2016 |                  92 |            20 |       417 |                  42 |                   50 | B3              | No confirmed PLE match | Public               | Natural Sciences             |
| AARON, GLEN ANTON TANGHAL||05/28/1992             |    1121210429 |   2012 |                 129 |            70 |       552 |                  65 |                   64 | B8              | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| AARON, GLEN ANTON TANGHAL||05/28/1992             |    1111302740 |   2013 |                 126 |            60 |       525 |                  71 |                   55 | B7              | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABABA, ERICA OCHADA||3/6/1993                     |    1111405756 |   2014 |                 104 |            35 |       460 |                  58 |                   46 | B4              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABABA, ERICA OCHADA||3/6/1993                     |    1031505145 |   2015 |                 132 |            60 |       525 |                  70 |                   62 | B7              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABABAO, KEESHIA MARI YBARZABAL||10/3/1992         |    1121200934 |   2012 |                 103 |            30 |       448 |                  55 |                   48 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABABAO, KEESHIA MARI YBARZABAL||10/3/1992         |    1041300511 |   2013 |                 129 |            54 |       510 |                  68 |                   61 | B6              | No confirmed PLE match | Private              | Medical & Allied             |
| ABACAN, AIRAH GIZELLE ALCOMENDAS||9/2/1993        |    1111304744 |   2013 |                 109 |            36 |       464 |                  69 |                   40 | B4              | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABACAN, AIRAH GIZELLE ALCOMENDAS||9/2/1993        |    1111403363 |   2014 |                 138 |            80 |       585 |                  79 |                   59 | B9              | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABACAN, MARIELLE JELINNE DEL ROSARIO||06/16/1991  |    1121006939 |   2010 |                 111 |            32 |       454 |                  64 |                   47 | B4              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABACAN, MARIELLE JELINNE DEL ROSARIO||06/16/1991  |    1111302610 |   2013 |                 116 |            48 |       494 |                  72 |                   44 | B5              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABACAN, MARIELLE JELINNE DEL ROSARIO||06/16/1991  |    1041401433 |   2014 |                 129 |            70 |       552 |                  71 |                   58 | B8              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABACAN, REMY JOY GUTIERREZ||06/15/1992            |    1111311636 |   2013 |                 118 |            49 |       498 |                  66 |                   52 | B5              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABACAN, REMY JOY GUTIERREZ||06/15/1992            |    1041407068 |   2014 |                 118 |            54 |       510 |                  62 |                   56 | B6              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD SANTOS, NICOLE ANNE TUMANG||04/30/1994       |    1111407959 |   2014 |                 149 |            89 |       625 |                  80 |                   69 | B9              | No confirmed PLE match | Public               | Social & Behavioral Sciences |
| ABAD SANTOS, NICOLE ANNE TUMANG||04/30/1994       |    1101509037 |   2015 |                 147 |            88 |       616 |                  92 |                   55 | B9              | No confirmed PLE match | Private              | Social & Behavioral Sciences |
| ABAD, AARON ADOLF RAMOS||02/18/1992               |    1031202069 |   2012 |                 156 |            81 |       586 |                  73 |                   83 | B9              | No confirmed PLE match | Public               | Medical & Allied             |
| ABAD, AARON ADOLF RAMOS||02/18/1992               |    1121208977 |   2012 |                 155 |            93 |       645 |                  71 |                   84 | B10             | No confirmed PLE match | Public               | Medical & Allied             |
| ABAD, ADDIELOU FIDELFIO ESPINA||08/21/1993        |    1041602789 |   2016 |                 144 |            64 |       537 |                  75 |                   69 | B7              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, ADDIELOU FIDELFIO ESPINA||08/21/1993        |    1031706452 |   2017 |                 169 |            87 |       613 |                  91 |                   78 | B9              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, AINA GENE CRUZ||06/25/1997                  |    1031700678 |   2017 |                 115 |            32 |       452 |                  56 |                   59 | B4              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAD, AINA GENE CRUZ||06/25/1997                  |    1031807544 |   2018 |                  80 |             5 |       337 |                  54 |                   26 | B1              | No confirmed PLE match | Public               | Natural Sciences             |
| ABAD, AINA GENE CRUZ||06/25/1997                  |    1101809800 |   2018 |                 102 |            33 |       457 |                  54 |                   48 | B4              | No confirmed PLE match | Public               | Natural Sciences             |
| ABAD, ALBERT CAISIP||09/28/1990                   |    2121003323 |   2010 |                 131 |            56 |       514 |                  65 |                   66 | B6              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAD, ALBERT CAISIP||09/28/1990                   |        400428 |   2010 |                 105 |            16 |       399 |                  52 |                   53 | B2              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABAD, ANGELLIE NIKKA SALIVIO||7/10/1996           |    1031800980 |   2018 |                 152 |            91 |       635 |                  90 |                   62 | B10             | No confirmed PLE match | Public               | Other                        |
| ABAD, ANGELLIE NIKKA SALIVIO||7/10/1996           |    1101801542 |   2018 |                 150 |            81 |       586 |                  86 |                   64 | B9              | No confirmed PLE match | Public               | Other                        |
| ABAD, ISRAEL CONRAD PORNOSDORO||01/18/1990        |    1121203499 |   2012 |                  96 |            20 |       416 |                  58 |                   38 | B3              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, ISRAEL CONRAD PORNOSDORO||01/18/1990        |    1041301655 |   2013 |                 121 |            43 |       481 |                  63 |                   58 | B5              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, JAKES KATHERIENE BATUL||12/11/1991          |    1041301575 |   2013 |                  90 |             8 |       357 |                  49 |                   41 | B1              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, JAKES KATHERIENE BATUL||12/11/1991          |    1111304338 |   2013 |                  98 |            21 |       420 |                  55 |                   43 | B3              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, JAKES KATHERIENE BATUL||12/11/1991          |    1041404814 |   2014 |                  99 |            24 |       430 |                  58 |                   41 | B3              | Confirmed PLE passer   | Public               | Medical & Allied             |
| ABAD, JAMAICA LORRAINE UGAY||07/22/1995           |    1101602457 |   2016 |                 141 |            73 |       562 |                  61 |                   80 | B8              | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABAD, JAMAICA LORRAINE UGAY||07/22/1995           |    1031710940 |   2017 |                 177 |            92 |       640 |                  93 |                   84 | B10             | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABAD, JAN CHESTER IGANO||01/31/1993               |    1121211000 |   2012 |                 123 |            62 |       529 |                  68 |                   55 | B7              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, JAN CHESTER IGANO||01/31/1993               |    1041402593 |   2014 |                 163 |            96 |       673 |                  91 |                   72 | B10             | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, JOSEPH ZACHARY MORA||7/1/1989               |    1121005871 |   2010 |                 137 |            63 |       532 |                  69 |                   68 | B7              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, JOSEPH ZACHARY MORA||7/1/1989               |    1041403168 |   2014 |                 146 |            87 |       615 |                  82 |                   64 | B9              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, JOYCE ANNE ACEBUQUE||09/28/1994             |    1111407366 |   2014 |                 105 |            36 |       464 |                  69 |                   36 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, JOYCE ANNE ACEBUQUE||09/28/1994             |    1041607154 |   2016 |                 123 |            38 |       471 |                  76 |                   47 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, KATHERINE ALARCON||05/30/1992               |    1121106602 |   2011 |                 162 |            83 |       595 |                  92 |                   70 | B9              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABAD, KATHERINE ALARCON||05/30/1992               |    1121204426 |   2012 |                 156 |            93 |       649 |                  84 |                   72 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABAD, KRISTELLE ROBARO||10/22/1994                |    1121203659 |   2012 |                 115 |            49 |       498 |                  70 |                   45 | B5              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAD, KRISTELLE ROBARO||10/22/1994                |    1041303800 |   2013 |                 141 |            70 |       552 |                  74 |                   67 | B8              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAD, KRISTELLE ROBARO||10/22/1994                |    1111305415 |   2013 |                 126 |            62 |       529 |                  67 |                   59 | B7              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAD, LIANNE JOY BRILLANTES||10/28/1994           |    1041403511 |   2014 |                 134 |            76 |       572 |                  64 |                   70 | B8              | No confirmed PLE match | Public               | Medical & Allied             |
| ABAD, LIANNE JOY BRILLANTES||10/28/1994           |    1101811332 |   2018 |                 141 |            73 |       562 |                  78 |                   63 | B8              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, MARK MELCHOR GONZAGA||01/22/1995            |    1101612939 |   2016 |                 131 |            64 |       536 |                  67 |                   64 | B7              | No confirmed PLE match | Public               | Medical & Allied             |
| ABAD, MARK MELCHOR GONZAGA||01/22/1995            |    1031800631 |   2018 |                 140 |            82 |       592 |                  77 |                   63 | B9              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, MARLYN ANNE GARCIA||08/15/1992              |    1111402055 |   2014 |                 119 |            55 |       514 |                  67 |                   52 | B6              | Confirmed PLE passer   | Public               | Medical & Allied             |
| ABAD, MARLYN ANNE GARCIA||08/15/1992              |    1031502348 |   2015 |                 134 |            63 |       533 |                  74 |                   60 | B7              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAD, MONIQUE BANTIQUE||5/7/1996                  |    1101605899 |   2016 |                 111 |            43 |       482 |                  63 |                   48 | B5              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABAD, MONIQUE BANTIQUE||5/7/1996                  |    1031701653 |   2017 |                 150 |            72 |       557 |                  92 |                   58 | B8              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABAD, NICOLE MAE GATCHALIAN||05/14/1997           |    1101612938 |   2016 |                  97 |            26 |       435 |                  50 |                   47 | B3              | No confirmed PLE match | Public               | Medical & Allied             |
| ABAD, NICOLE MAE GATCHALIAN||05/14/1997           |    1031810771 |   2018 |                 131 |            73 |       560 |                  78 |                   53 | B8              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, SHEENA POSADAS||2/3/1999                    |    1031812803 |   2018 |                 103 |            30 |       448 |                  60 |                   43 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAD, SHEENA POSADAS||2/3/1999                    |    1101815201 |   2018 |                 133 |            67 |       544 |                  73 |                   60 | B7              | No confirmed PLE match | Private              | Medical & Allied             |
| ABADAM, EDELYN JOY MACADAAN||                     |       1060229 |   2006 |                 156 |            81 |       589 |                  80 |                   76 | B9              | No confirmed PLE match | Public               | Education                    |
| ABADAM, EDELYN JOY MACADAAN||                     |       1071890 |   2006 |                 164 |            85 |       604 |                  85 |                   79 | B9              | No confirmed PLE match | Public               | Education                    |
| ABADIANO, MISHAEL PACHECO||09/24/1995             |    1041401616 |   2014 |                  94 |            18 |       407 |                  48 |                   46 | B2              | No confirmed PLE match | Private              | Medical & Allied             |
| ABADIANO, MISHAEL PACHECO||09/24/1995             |    1101501771 |   2015 |                 105 |            43 |       483 |                  54 |                   51 | B5              | No confirmed PLE match | Private              | Medical & Allied             |
| ABADILLA, AARON AMIL ACEDO||                      |       1002267 |   2009 |                 150 |            74 |       565 |                  78 |                   72 | B8              | No confirmed PLE match | Private              | Natural Sciences             |
| ABADILLA, AARON AMIL ACEDO||                      |        411398 |   2010 |                 155 |            70 |       552 |                  86 |                   69 | B8              | No confirmed PLE match | Private              | Other                        |
| ABADILLA, ANGELA MARIE OROPESA||09/15/1984        |    1041300965 |   2013 |                  66 |             1 |       249 |                  35 |                   31 | B1              | No confirmed PLE match | Private              | Medical & Allied             |
| ABADILLA, ANGELA MARIE OROPESA||09/15/1984        |    1111308784 |   2013 |                  66 |             1 |       271 |                  39 |                   27 | B1              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAGAT, RICK JEYRALD MAGALONG||1/12/1991          |    1121108573 |   2011 |                 118 |            38 |       469 |                  66 |                   52 | B4              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAGAT, RICK JEYRALD MAGALONG||1/12/1991          |    1111300139 |   2013 |                 124 |            59 |       522 |                  71 |                   53 | B6              | Confirmed PLE passer   | Public               | Medical & Allied             |
| ABAGAT, RICK JEYRALD MAGALONG||1/12/1991          |    1041400668 |   2014 |                 129 |            70 |       552 |                  72 |                   57 | B8              | Confirmed PLE passer   | Private              | Medical & Allied             |
| ABAH, RAZHIDA NAZ||1/3/1995                       |    1041608083 |   2016 |                  93 |             9 |       367 |                  52 |                   41 | B1              | No confirmed PLE match | Private              | Medical & Allied             |
| ABAH, RAZHIDA NAZ||1/3/1995                       |    1031815017 |   2018 |                  71 |             2 |       293 |                  45 |                   26 | B1              | No confirmed PLE match | Public               | Medical & Allied             |
| ABAIGAR, MELANIE CHRISTINE CELESTIAL||12/21/1995  |    1101504814 |   2015 |                  99 |            35 |       461 |                  50 |                   49 | B4              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAIGAR, MELANIE CHRISTINE CELESTIAL||12/21/1995  |    1101606653 |   2016 |                 101 |            31 |       450 |                  57 |                   44 | B4              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAIGAR, MELANIE CHRISTINE CELESTIAL||12/21/1995  |    1031708015 |   2017 |                 150 |            73 |       560 |                  71 |                   79 | B8              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAIGAR, MIGUEL III CELESTIAL||5/8/1992           |    1111305543 |   2013 |                  99 |            23 |       425 |                  55 |                   44 | B3              | No confirmed PLE match | Private              | Other                        |
| ABAIGAR, MIGUEL III CELESTIAL||5/8/1992           |    1031706303 |   2017 |                 140 |            62 |       531 |                  77 |                   63 | B7              | No confirmed PLE match | Private              | Other                        |
| ABAINZA, JANSEN MOLATO||11/12/1993                |    1041407161 |   2014 |                  73 |             2 |       302 |                  47 |                   26 | B1              | No confirmed PLE match | Public               | Natural Sciences             |
| ABAINZA, JANSEN MOLATO||11/12/1993                |    1111409896 |   2014 |                  75 |             3 |       316 |                  30 |                   45 | B1              | No confirmed PLE match | Public               | Natural Sciences             |
| ABAINZA, JANSEN MOLATO||11/12/1993                |    1101510046 |   2015 |                  66 |             3 |       304 |                  39 |                   27 | B1              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAINZA, KLARYS MOLATO||11/9/1995                 |    1101508520 |   2015 |                  63 |             2 |       286 |                  26 |                   37 | B1              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAINZA, KLARYS MOLATO||11/9/1995                 |    1041605016 |   2016 |                  93 |             9 |       367 |                  49 |                   44 | B1              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAINZA, KLARYS MOLATO||11/9/1995                 |    1101812585 |   2018 |                 104 |            34 |       460 |                  53 |                   51 | B4              | No confirmed PLE match | Private              | Natural Sciences             |
| ABAJA, CARISSE MACALINAO||                        |       1070806 |   2006 |                 111 |            30 |       447 |                  51 |                   60 | B4              | No confirmed PLE match | Private              | Social & Behavioral Sciences |
| ABAJA, CARISSE MACALINAO||                        |       1082119 |   2007 |                 127 |            50 |       501 |                  55 |                   72 | B6              | No confirmed PLE match | Private              | Natural Sciences             |
| ABALLE, GILLES RADOC||01/19/1988                  |    1121209792 |   2012 |                 107 |            36 |       464 |                  45 |                   62 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALLE, GILLES RADOC||01/19/1988                  |    1111303287 |   2013 |                 140 |            78 |       579 |                  66 |                   74 | B8              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALLE, RAPHUNZEL MONTALBO||06/17/1989            |    1121003605 |   2010 |                 115 |            37 |       467 |                  63 |                   52 | B4              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALLE, RAPHUNZEL MONTALBO||06/17/1989            |    1041609444 |   2016 |                 108 |            21 |       421 |                  63 |                   45 | B3              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALOS, ALYANNA JOSON||03/19/1994                 |    1121209747 |   2012 |                 120 |            57 |       518 |                  70 |                   50 | B6              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALOS, ALYANNA JOSON||03/19/1994                 |    1041303786 |   2013 |                 151 |            80 |       585 |                  80 |                   71 | B9              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALOS, ALYANNA JOSON||03/19/1994                 |    1111311089 |   2013 |                 137 |            75 |       568 |                  79 |                   58 | B8              | No confirmed PLE match | Private              | Medical & Allied             |
| ABALOS, EUNICE ANNE ORTIZ||04/13/1995             |    1111307839 |   2013 |                 165 |            94 |       659 |                 101 |                   64 | B10             | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABALOS, EUNICE ANNE ORTIZ||04/13/1995             |    1101507700 |   2015 |                 177 |            98 |       708 |                  95 |                   82 | B10             | Confirmed PLE passer   | Private              | Social & Behavioral Sciences |
| ABALOS, HANNAH LOUISE PHOEBE BAUTISTA||07/17/1993 |    2121003055 |   2010 |                 147 |            73 |       562 |                  71 |                   76 | B8              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABALOS, HANNAH LOUISE PHOEBE BAUTISTA||07/17/1993 |    1121107319 |   2011 |                 161 |            82 |       592 |                  86 |                   75 | B9              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABALOS, ISAAC ELIZALDE||12/4/1999                 |    1031810735 |   2018 |                 112 |            44 |       485 |                  57 |                   55 | B5              | No confirmed PLE match | Private              | Natural Sciences             |
| ABALOS, ISAAC ELIZALDE||12/4/1999                 |    1101807674 |   2018 |                 132 |            66 |       542 |                  67 |                   65 | B7              | No confirmed PLE match | Private              | Natural Sciences             |
| ABALOS, JOANNA MAE TANGCA||4/7/1994               |    1041403317 |   2014 |                 114 |            48 |       494 |                  63 |                   51 | B5              | Confirmed PLE passer   | Public               | Natural Sciences             |
| ABALOS, JOANNA MAE TANGCA||4/7/1994               |    1111403423 |   2014 |                 128 |            71 |       557 |                  78 |                   50 | B8              | Confirmed PLE passer   | Private              | Natural Sciences             |
| ABALOS, JOANNA MAE TANGCA||4/7/1994               |    1031504785 |   2015 |                 166 |            90 |       628 |                  87 |                   79 | B10             | Confirmed PLE passer   | Private              | Natural Sciences             |

> Full detail: [08_repeat_takers_detail.csv](08_repeat_takers_detail.csv) (77,770 rows, 12 cols)


---

## 6. NMA_AppNo Deterministic Match Histories

Attempt histories exclusively for records matched deterministically via application number (PLE_MATCH_METHOD in MANUAL_APPNO_MATCH, DETERMINISTIC_APPNO), rather than by exact name.

**population: all NMAT rows | n=2,867**

| PERSON_KEY                                              |   APPNO_CLEAN |   Year |   TotalRawScoreTRUE |   NMS_PER_num | PLE_STATUS_LABEL     |
|:--------------------------------------------------------|--------------:|-------:|--------------------:|--------------:|:---------------------|
| ABAD, ALBERT CAISIP||09/28/1990                         |        400428 |   2010 |                 105 |            16 | Confirmed PLE passer |
| ABAD, JOSHUA KIM E||05/17/1996                          |    1101509313 |   2015 |                 121 |            65 | Confirmed PLE passer |
| ABAD, MA JUSTINE DAYANNE CERCADO||09/17/1995            |    1101507389 |   2015 |                 123 |            67 | Confirmed PLE passer |
| ABADIER, AILEEN MESTIDIO||                              |       1061740 |   2007 |                  90 |            14 | Confirmed PLE passer |
| ABALOS, RODRIGO JR SAPIANDANTE||07/21/1990              |    1121007739 |   2010 |                 152 |            78 | Confirmed PLE passer |
| ABALOS, RODRIGO JUNIOR SAPIANDANTE||                    |        411600 |   2010 |                 167 |            81 | Confirmed PLE passer |
| ABANA, MA EDISA CRUZ||                                  |       1003803 |   2009 |                 126 |            47 | Confirmed PLE passer |
| ABANILLA, LYRA JOY LUCAS||01/14/1989                    |    1121209623 |   2012 |                 155 |            93 | Confirmed PLE passer |
| ABARA, MA VICTORIA LOBENDINO||05/14/1996                |    1101504711 |   2015 |                 139 |            82 | Confirmed PLE passer |
| ABBARIAO, MA JESICCA DULIN||9/4/1993                    |    1121213166 |   2012 |                  82 |             6 | Confirmed PLE passer |
| ABBARIAO, MA JESICCA DULIN||9/4/1993                    |    1111309255 |   2013 |                  88 |            11 | Confirmed PLE passer |
| ABBARIAO, MA JESICCA DULIN||9/4/1993                    |    1041401732 |   2014 |                 129 |            70 | Confirmed PLE passer |
| ABDON, MARIA THERESE LUMANOG||11/30/1985                |    1121001533 |   2010 |                  98 |            17 | Confirmed PLE passer |
| ABDULCADER, SANNAH MOHAMMAD||                           |       1003057 |   2009 |                  84 |             6 | Confirmed PLE passer |
| ABDULMALIK, ANIES ANSARY ABDULHAMID||8/2/1992           |    1121206466 |   2012 |                 124 |            63 | Confirmed PLE passer |
| ABEL, JORIZ KEVIN||08/24/1993                           |    1121204887 |   2012 |                 155 |            93 | Confirmed PLE passer |
| ABELITA, MA CARISSA YAN||01/21/1993                     |    1121207124 |   2012 |                 137 |            79 | Confirmed PLE passer |
| ABELLO, MA ANTONIA ELISA RAMOS||2/1/1991                |    1121105620 |   2011 |                 175 |            91 | Confirmed PLE passer |
| ABIAN, KIM CRISOSTOMO||01/23/1994                       |    1121201734 |   2012 |                 121 |            59 | Confirmed PLE passer |
| ABIJAY, LORENZO MIGUEL PENALOZA||09/22/1992             |    1111403797 |   2014 |                 155 |            93 | Confirmed PLE passer |
| ABORKA, MA AYANNE BALDEVIA||03/31/1994                  |    1101506240 |   2015 |                 159 |            94 | Confirmed PLE passer |
| ABORQUE, JESUS CESARIO JR JAVINES||                     |       1000742 |   2009 |                 145 |            70 | Confirmed PLE passer |
| ABOY, MA EDILLA TERESA RATILLA||                        |       1092757 |   2008 |                 131 |            59 | Confirmed PLE passer |
| ABOY, MA EDILLA TERESA RATILLA||04/23/1988              |    2121001487 |   2010 |                 148 |            74 | Confirmed PLE passer |
| ABREA, MA JESSA ALITALIA CARABUENA||                    |        410137 |   2010 |                 111 |            21 | Confirmed PLE passer |
| ABREU, IARA MARIE ANN ABARQUEZ||05/27/1992              |    1041300496 |   2013 |                  63 |            -1 | Confirmed PLE passer |
| ABRIGO, MA ASTRID VILLAROYA||                           |       1052640 |   2006 |                  92 |            11 | Confirmed PLE passer |
| ABRIL, JOANNA BLANCA C JUAN||                           |        410765 |   2010 |                 184 |            91 | Confirmed PLE passer |
| ABUAN, GERLIE PARINGIT||                                |       1082059 |   2007 |                 123 |            47 | Confirmed PLE passer |
| ABUEG, MICHELLE RENEE||                                 |       1001133 |   2009 |                 186 |            97 | Confirmed PLE passer |
| ABUEVA, AILEEN CRYSTEL DIMAYACYAC||                     |       1083653 |   2008 |                 121 |            41 | Confirmed PLE passer |
| ABUTIN, MA VICTORIA MIANO||                             |       1052977 |   2006 |                 125 |            49 | Confirmed PLE passer |
| ABUTIN, MA VICTORIA MIANO||                             |       1071027 |   2006 |                 140 |            63 | Confirmed PLE passer |
| ACEDO, RODY MAE OBLIGADO||05/14/1993                    |    1031504216 |   2015 |                 126 |            54 | Confirmed PLE passer |
| ACLAN, ARRIANE KHAY SACENDONCILLO||06/15/1989           |    1031712565 |   2017 |                 141 |            63 | Confirmed PLE passer |
| ACLAN, MA ANA PATRICIA CUETO||08/21/1991                |    1121004428 |   2010 |                 148 |            74 | Confirmed PLE passer |
| ACLAN, MA ANA PATRICIA CUETO||08/21/1991                |    1041103316 |   2011 |                 146 |            75 | Confirmed PLE passer |
| ACOP, REICHEL ANGELO||11/14/1992                        |    1121204504 |   2012 |                 140 |            82 | Confirmed PLE passer |
| ACOSTA, DONNA ROSE KUAN TIU||5/10/1992                  |    1111308750 |   2013 |                 197 |           nan | Confirmed PLE passer |
| ACOSTA, MA ANGELICA CIELO CABATINGAN||                  |       1000998 |   2009 |                 150 |            75 | Confirmed PLE passer |
| ACOSTA, MA JOANNA EMILY MAMARIL||                       |       1085762 |   2008 |                 175 |            94 | Confirmed PLE passer |
| ACOSTA, NIKOLAI E||12/18/1996                           |    1101602164 |   2016 |                 135 |            68 | Confirmed PLE passer |
| ACUNA, DELFIN JR PLASI||                                |       1001748 |   2009 |                 165 |            87 | Confirmed PLE passer |
| ADA, MA MICHELLE BELTRAN||02/27/1993                    |    1041304910 |   2013 |                 162 |            89 | Confirmed PLE passer |
| ADA, MA MICHELLE BELTRAN||02/27/1993                    |    1111312215 |   2013 |                 148 |            86 | Confirmed PLE passer |
| ADAYA, MA MILDRED BOBADILLA||2/8/1993                   |    1121108002 |   2011 |                 159 |            81 | Confirmed PLE passer |
| ADAYA, MA MILDRED BOBADILLA||2/8/1993                   |    1031203526 |   2012 |                 168 |            89 | Confirmed PLE passer |
| ADDUN, EDZEL JANE JARITO||1/12/1987                     |    1041303533 |   2013 |                 140 |            69 | Confirmed PLE passer |
| ADELAN, MARIA ROTELLE SALVADOR||02/16/1996              |    1101508295 |   2015 |                 151 |            90 | Confirmed PLE passer |
| ADIONG, FELINA JUSTINE VANO||10/8/1996                  |    1101601948 |   2016 |                 159 |            86 | Confirmed PLE passer |
| ADLAON, LANCE ALDWIN||10/27/1986                        |        400801 |   2010 |                 127 |            51 | Confirmed PLE passer |
| ADONA, MA RECCIA ROSE GOK ONG||                         |       1061045 |   2006 |                 136 |            59 | Confirmed PLE passer |
| ADONA, MA RECCIA ROSE GOK ONG||                         |       1072003 |   2006 |                 131 |            53 | Confirmed PLE passer |
| ADRIANO, BUENAVENTURA III||07/18/1988                   |    1121204349 |   2012 |                 134 |            76 | Confirmed PLE passer |
| AGAMATA, ERIKA JANE PAULA TIAM||2/6/1992                |    1041300374 |   2013 |                 128 |            54 | Confirmed PLE passer |
| AGARIN, REA MAY I VILLANUEVA||7/8/1993                  |    1111400439 |   2014 |                 131 |            75 | Confirmed PLE passer |
| AGDAMAG, MA ANGELICA CRUZ||10/30/1995                   |    1031505937 |   2015 |                 165 |            91 | Confirmed PLE passer |
| AGDAMAG, MA ANGELICA CRUZ||10/30/1995                   |    1101509261 |   2015 |                 157 |            93 | Confirmed PLE passer |
| AGGABAO, MA CONCEPCION SOCORRO GRACIA AGAGON||8/12/1992 |    1121105081 |   2011 |                  99 |            19 | Confirmed PLE passer |
| AGGABAO, MA CONCEPCION SOCORRO GRACIA AGAGON||8/12/1992 |    1121203920 |   2012 |                  86 |             9 | Confirmed PLE passer |
| AGGABAO, MA CONCEPCION SOCORRO GRACIA AGAGON||8/12/1992 |    1041302875 |   2013 |                 110 |            30 | Confirmed PLE passer |
| AGGABAO, MA CONCEPCION SOCORRO GRACIA AGAGON||8/12/1992 |    1111308528 |   2013 |                 109 |            36 | Confirmed PLE passer |
| AGRASADA, TANYA KATRINA BUENAFLOR||9/12/1991            |    1121211041 |   2012 |                 126 |            66 | Confirmed PLE passer |
| AGRUPIS, KRISTAL AN CASTANEDA||                         |       1071156 |   2006 |                 179 |            93 | Confirmed PLE passer |
| AGRUPIS, KRISTAL AN CASTANEDA||                         |       1054814 |   2007 |                 174 |            86 | Confirmed PLE passer |
| AGUDA, MARY GRACE SIMANGON||03/30/1987                  |    1041403588 |   2014 |                 124 |            63 | Confirmed PLE passer |
| AGUDO, SHELLEY VANESSA DELA CRUZ||10/3/1992             |    1041300751 |   2013 |                 131 |            60 | Confirmed PLE passer |
| AGUELO, MA ISABEL SALA||12/3/1992                       |    1121106186 |   2011 |                 168 |            88 | Confirmed PLE passer |
| AGUELO, MA ISABEL SALA||12/3/1992                       |    1031202030 |   2012 |                 171 |            90 | Confirmed PLE passer |
| AGUILA, MA THERESSA DE LOS REYES||1/10/1994             |    1041407069 |   2014 |                 154 |            92 | Confirmed PLE passer |
| AGUILA, MA THERESSA DE LOS REYES||1/10/1994             |    1111407511 |   2014 |                 170 |            98 | Confirmed PLE passer |
| AGUILAR, ARDIE ANTONIO||1/2/1988                        |    1121005263 |   2010 |                 129 |            53 | Confirmed PLE passer |
| AGUILAR, JEFF JUSTIN||11/28/1994                        |    1101505909 |   2015 |                 202 |           nan | Confirmed PLE passer |
| AGUILAR, KATRINA ARIELLE ROJAS||5/3/1994                |    1101507482 |   2015 |                 143 |            85 | Confirmed PLE passer |
| AGUIRRE, AYRA JHOANA GUIANAN||3/6/1988                  |    1041300207 |   2013 |                 185 |            97 | Confirmed PLE passer |
| AGUIRRE, EUNICE CUENTO||11/25/1991                      |    1121101329 |   2011 |                 108 |            27 | Confirmed PLE passer |
| AGUIRRE, MA JESSICA ELIZABETH ESPULGAR||9/1/1994        |    1111304915 |   2013 |                  87 |             9 | Confirmed PLE passer |
| AGUIRRE, MA JESSICA ELIZABETH ESPULGAR||9/1/1994        |    1041400753 |   2014 |                 105 |            33 | Confirmed PLE passer |
| AGUSTIN, CRISTINA ANNE SANTOS||11/23/1992               |    1111303407 |   2013 |                 160 |            92 | Confirmed PLE passer |
| AGUSTIN, RAPHAEL JAMES F||10/24/1996                    |    1031705655 |   2017 |                 141 |            63 | Confirmed PLE passer |
| AGUSTINO, ARNULFO JR RICO||9/9/1989                     |    2121001876 |   2010 |                 168 |            90 | Confirmed PLE passer |
| AHMAD, SHAHEEN OSMENA||11/28/1994                       |    1031700610 |   2017 |                 130 |            50 | Confirmed PLE passer |
| AL FAWAZ, BANDR NAFEEZ ABDULLAH LOY OD||12/15/1993      |    1031507043 |   2015 |                 143 |            73 | Confirmed PLE passer |
| ALABADO, JIBIN CANTILLO||06/13/1973                     |    1041100956 |   2011 |                 175 |            94 | Confirmed PLE passer |
| ALAMPAY, NICCOLO SU||03/19/1989                         |    1121005070 |   2010 |                 174 |            93 | Confirmed PLE passer |
| ALATI IT, ROWIE LYNE FERNANDEZ||8/3/1990                |    1121103224 |   2011 |                 160 |            83 | Confirmed PLE passer |
| ALBANO, EMMANUEL JR ESCARLAN||8/4/1990                  |    2121000085 |   2010 |                 142 |            68 | Confirmed PLE passer |
| ALBANO, MARIA ANGELINE PANTUA||                         |       1060769 |   2006 |                 106 |            26 | Confirmed PLE passer |
| ALBESA, MA TRISHA ARIAS||4/9/1996                       |    1101511351 |   2015 |                 155 |            92 | Confirmed PLE passer |
| ALCALA, ANGELLE KATHREEN TUBAN||04/25/1990              |    1041406715 |   2014 |                 108 |            38 | Confirmed PLE passer |
| ALCALDE, MA KATHRINA TERESA TONGCO||                    |       1073528 |   2007 |                 176 |            93 | Confirmed PLE passer |
| ALCANO, MARY CHRISTINE PINO||                           |       1001740 |   2009 |                 107 |            25 | Confirmed PLE passer |
| ALCANTARA, ALEXIS ANNE CONTADO||01/23/1996              |    1041600384 |   2016 |                 138 |            57 | Confirmed PLE passer |
| ALCANTARA, MARK ANGELO MANDAL||                         |       1093750 |   2009 |                 200 |            99 | Confirmed PLE passer |
| ALCANTARA, RANIEL JOHN LUQUE||11/11/1998                |    1031809024 |   2018 |                 119 |            55 | Confirmed PLE passer |
| ALCANZO, JAN HILARY ABELLO||05/29/1990                  |    1041102518 |   2011 |                 180 |            96 | Confirmed PLE passer |
| ALCARAZ, ADRIAN M||04/22/1993                           |    1101813952 |   2018 |                  98 |            27 | Confirmed PLE passer |
| ALCAZAR, ELIZABETH GRACE ALMADIN||                      |       1090183 |   2009 |                 154 |            79 | Confirmed PLE passer |
| ALCAZAR, ESTHER RUTH DE LOS REYES||5/12/1990            |    1121106368 |   2011 |                 134 |            56 | Confirmed PLE passer |
| ALCID, MA ARABELLA JAFFNA CABE||11/29/1993              |    1041301690 |   2013 |                 134 |            63 | Confirmed PLE passer |

> Full detail: [08_appno_match_histories.csv](08_appno_match_histories.csv) (2,867 rows)

