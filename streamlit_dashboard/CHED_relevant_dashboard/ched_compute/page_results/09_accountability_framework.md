# Accountability Framework & Monitoring (CMO Section IV-B-2, VI, Transitory)

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/09_accountability_framework.py`

---



This section operationalises CMO No. __, s. 2026 provisions on institutional accountability (Section IV-B-2), CHED monitoring (Section VI), and the transitory provision. It identifies private HEIs (PHEIs) whose NMAT-to-PLE linkage rates fall below the national benchmark and provides a monitoring framework and transition timeline for full CMO compliance.

## Overview

| Metric | Value |
|--------|-------|
| **Total PHEIs in Dataset** | 925 |
| **PHEIs with ≥5 Observable Examinees** | 385 |
| **Above National Benchmark (≥43.46%)** | 150 |
| **Below National Benchmark (<43.46%)** | 235 |
| **National PHEI Linkage Benchmark** | 43.46% |
| **Observable Cohort Period** | 2006 – 2014 |

## Section A: PHEI Risk Flags

Each PHEI with ≥5 examinees in the observable cohort (Year ≤ 2014) is assessed against the national NMAT-to-PLE linkage benchmark of **43.46%**. The linkage rate measures the share of NMAT examinees from that HEI who were later found in official PLE passer records — **not** the PLE pass rate. PHEIs below the benchmark are flagged for monitoring; those below the benchmark for every available year are classified as **High Risk**.

### Risk Flag Table (Sorted by Linkage Rate, Worst First)

| HEI | Type | n (Obs.) | PLE Linked | Linkage Rate | Benchmark (43.46%) | Status | Risk Level |
|-----|:----:|:--------:|:----------:|:------------:|:-----------------------------------:|:------:|:----------:|
| St. Luke'S School Of Medicine, India | Private | 10 | 0 | 0.00% | 43.46% | Below Benchmark | High |
| Laguna College | Private | 7 | 0 | 0.00% | 43.46% | Below Benchmark | High |
| St. Paul University Philippines | Private | 5 | 0 | 0.00% | 43.46% | Below Benchmark | High |
| Divine Word College Of Laoag | Private | 107 | 0 | 0.00% | 43.46% | Below Benchmark | High |
| Malasiqui Agno Valley College | Private | 7 | 0 | 0.00% | 43.46% | Below Benchmark | High |
| Ama Computer College | Private | 12 | 1 | 8.33% | 43.46% | Below Benchmark | High |
| Virgen Milagrosa Educational Institute, San Carlos City | Private | 11 | 1 | 9.09% | 43.46% | Below Benchmark | High |
| Dr. Carlos Lanting College - Novaliches, Quezon City | Private | 10 | 1 | 10.00% | 43.46% | Below Benchmark | High |
| Northern Luzon Adventist College | Private | 9 | 1 | 11.11% | 43.46% | Below Benchmark | Monitor |
| Mindanao Medical Foundation College, Davao | Private | 9 | 1 | 11.11% | 43.46% | Below Benchmark | Monitor |
| Dominican College, Blum, San Juan, Mm | Private | 9 | 1 | 11.11% | 43.46% | Below Benchmark | High |
| University Of Visayas, Cebu | Private | 69 | 8 | 11.59% | 43.46% | Below Benchmark | High |
| Virgen Milagrosa Univ. Foundation - San Carlos City, Pa | Private | 76 | 10 | 13.16% | 43.46% | Below Benchmark | High |
| University Of Mindanao | Private | 7 | 1 | 14.29% | 43.46% | Below Benchmark | Monitor |
| Kester Grant College - Philippines | Private | 21 | 3 | 14.29% | 43.46% | Below Benchmark | High |
| University Of Perpetual Help System | Private | 7 | 1 | 14.29% | 43.46% | Below Benchmark | Monitor |
| Southeast Asian College Inc.-Quezon City | Private | 14 | 2 | 14.29% | 43.46% | Below Benchmark | Monitor |
| San Sebastian College | Private | 7 | 1 | 14.29% | 43.46% | Below Benchmark | Monitor |
| St. Paul University Manila | Private | 6 | 1 | 16.67% | 43.46% | Below Benchmark | Monitor |
| Medina College | Private | 24 | 4 | 16.67% | 43.46% | Below Benchmark | High |
| World Citi Colleges | Private | 24 | 4 | 16.67% | 43.46% | Below Benchmark | High |
| Southeast Asian College Inc.-Espana, Manila | Private | 12 | 2 | 16.67% | 43.46% | Below Benchmark | High |
| St. Mary'S University, Nueva Vizcaya | Private | 6 | 1 | 16.67% | 43.46% | Below Benchmark | Monitor |
| La Salle College - Antipolo | Private | 6 | 1 | 16.67% | 43.46% | Below Benchmark | Monitor |
| Brent Hospital And Colleges | Private | 28 | 5 | 17.86% | 43.46% | Below Benchmark | High |
| University Of Perpetual Help System - Gma | Private | 11 | 2 | 18.18% | 43.46% | Below Benchmark | High |
| Brent Hospital And Colleges Inc., Zamboanga City | Private | 11 | 2 | 18.18% | 43.46% | Below Benchmark | Monitor |
| Notre Dame Of Jolo College, Jolo, Sulu | Private | 11 | 2 | 18.18% | 43.46% | Below Benchmark | High |
| Olivarez College, Sucat, Para$Aque | Private | 11 | 2 | 18.18% | 43.46% | Below Benchmark | High |
| Notre Dame Of Jolo College | Private | 27 | 5 | 18.52% | 43.46% | Below Benchmark | High |
| Saint Mary'S College Of Tagum | Private | 16 | 3 | 18.75% | 43.46% | Below Benchmark | High |
| University Of The Immaculate Conception College, Davao | Private | 5 | 1 | 20.00% | 43.46% | Below Benchmark | Monitor |
| St. Joseph'S College, Quezon City | Private | 10 | 2 | 20.00% | 43.46% | Below Benchmark | High |
| Davao Central College | Private | 5 | 1 | 20.00% | 43.46% | Below Benchmark | Monitor |
| Concordia College | Private | 5 | 1 | 20.00% | 43.46% | Below Benchmark | Monitor |
| University Of Immaculate Conception-Davao City | Private | 5 | 1 | 20.00% | 43.46% | Below Benchmark | Monitor |
| Lipa City Colleges, Batangas | Private | 5 | 1 | 20.00% | 43.46% | Below Benchmark | Monitor |
| Kalayaan College | Private | 5 | 1 | 20.00% | 43.46% | Below Benchmark | Monitor |
| Enderun College | Private | 5 | 1 | 20.00% | 43.46% | Below Benchmark | Monitor |
| Angeles University Foundation, Angeles City | Private | 471 | 95 | 20.17% | 43.46% | Below Benchmark | Monitor |
| Pines City Colleges - Baguio City | Private | 34 | 7 | 20.59% | 43.46% | Below Benchmark | Monitor |
| University Of The Assumption | Private | 19 | 4 | 21.05% | 43.46% | Below Benchmark | High |
| Manila Theological College | Private | 14 | 3 | 21.43% | 43.46% | Below Benchmark | High |
| Mapua Institute Of Technology - Makati | Private | 14 | 3 | 21.43% | 43.46% | Below Benchmark | High |
| Saint Gabriel College | Private | 9 | 2 | 22.22% | 43.46% | Below Benchmark | Monitor |
| Misamis University | Private | 22 | 5 | 22.73% | 43.46% | Below Benchmark | High |
| University Of The Assumption, Pampanga | Private | 8 | 2 | 25.00% | 43.46% | Below Benchmark | High |
| Arellano University - Pasay | Private | 8 | 2 | 25.00% | 43.46% | Below Benchmark | Monitor |
| Holy Trinity University | Private | 20 | 5 | 25.00% | 43.46% | Below Benchmark | High |
| Lyceum Of Aparri | Private | 8 | 2 | 25.00% | 43.46% | Below Benchmark | Monitor |
| La Consolacion College | Private | 40 | 10 | 25.00% | 43.46% | Below Benchmark | High |
| Notre Dame Of Tacurong College | Private | 8 | 2 | 25.00% | 43.46% | Below Benchmark | Monitor |
| Divine Word College Of Legazpi | Private | 8 | 2 | 25.00% | 43.46% | Below Benchmark | High |
| Colegio De San Juan De Letran, Calamba | Private | 16 | 4 | 25.00% | 43.46% | Below Benchmark | High |
| Saint Tonis College | Private | 8 | 2 | 25.00% | 43.46% | Below Benchmark | Monitor |
| Central Colleges Of The Philippines | Private | 12 | 3 | 25.00% | 43.46% | Below Benchmark | Monitor |
| Our Lady Of Fatima University - Antipolo | Private | 48 | 12 | 25.00% | 43.46% | Below Benchmark | Monitor |
| Baguio Central University | Private | 39 | 10 | 25.64% | 43.46% | Below Benchmark | Monitor |
| University Of Perpetual Help Dalta System-Las Piñas | Private | 66 | 17 | 25.76% | 43.46% | Below Benchmark | Monitor |
| Mindanao Sanitarium & Hospital College, Iligan City | Private | 50 | 13 | 26.00% | 43.46% | Below Benchmark | High |
| Uph-Dr. Jose G. Tamayo Medical Univ. | Private | 23 | 6 | 26.09% | 43.46% | Below Benchmark | High |
| St. Paul University, Quezon City | Private | 38 | 10 | 26.32% | 43.46% | Below Benchmark | Monitor |
| Pines City Colleges | Private | 71 | 19 | 26.76% | 43.46% | Below Benchmark | Monitor |
| Iligan Medical Center, Iligan City | Private | 33 | 9 | 27.27% | 43.46% | Below Benchmark | Monitor |
| Philippine Women'S University, Taft Avenue, Manila | Private | 33 | 9 | 27.27% | 43.46% | Below Benchmark | High |
| Medina College, Ozamis, Misamis Oriental | Private | 11 | 3 | 27.27% | 43.46% | Below Benchmark | High |
| University Of The Visayas | Private | 58 | 16 | 27.59% | 43.46% | Below Benchmark | Monitor |
| Mapua Institute Of Technology - Manila | Private | 18 | 5 | 27.78% | 43.46% | Below Benchmark | High |
| Miriam College | Private | 111 | 31 | 27.93% | 43.46% | Below Benchmark | High |
| West Negros College, Bacolod | Private | 7 | 2 | 28.57% | 43.46% | Below Benchmark | Monitor |
| Nueva Ecija Colleges | Private | 14 | 4 | 28.57% | 43.46% | Below Benchmark | High |
| St. Joseph College, Cavite | Private | 7 | 2 | 28.57% | 43.46% | Below Benchmark | Monitor |
| University Of Saint Anthony | Private | 7 | 2 | 28.57% | 43.46% | Below Benchmark | Monitor |
| University Of Perpetual Help Rizal - Molino | Private | 17 | 5 | 29.41% | 43.46% | Below Benchmark | Monitor |
| College Of The Holy Spirit Of Manila | Private | 34 | 10 | 29.41% | 43.46% | Below Benchmark | Monitor |
| New Era University, Quezon City | Private | 37 | 11 | 29.73% | 43.46% | Below Benchmark | High |
| Philippine College Of Health Sciences | Private | 20 | 6 | 30.00% | 43.46% | Below Benchmark | High |
| University Of Batangas | Private | 10 | 3 | 30.00% | 43.46% | Below Benchmark | Monitor |
| St. Dominic College Of Arts And Sciences Of Cavite | Private | 10 | 3 | 30.00% | 43.46% | Below Benchmark | Monitor |
| Remedios Trinidad Romualdez Medical Foundation, Tacloba | Private | 10 | 3 | 30.00% | 43.46% | Below Benchmark | High |
| St. Joseph College, Cavite City | Private | 10 | 3 | 30.00% | 43.46% | Below Benchmark | High |
| Capitol Medical Center College, Q.C. | Private | 30 | 9 | 30.00% | 43.46% | Below Benchmark | High |
| St. Michael'S College | Private | 10 | 3 | 30.00% | 43.46% | Below Benchmark | Monitor |
| Arellano University | Private | 33 | 10 | 30.30% | 43.46% | Below Benchmark | Monitor |
| Filamer Christian University | Private | 23 | 7 | 30.43% | 43.46% | Below Benchmark | High |
| Centro Escolar University - Makati | Private | 36 | 11 | 30.56% | 43.46% | Below Benchmark | High |
| Emilio Aguinaldo College | Private | 212 | 65 | 30.66% | 43.46% | Below Benchmark | Monitor |
| Lyceum Northwestern University | Private | 117 | 36 | 30.77% | 43.46% | Below Benchmark | High |
| Dipolog Medical Center College Foundation | Private | 13 | 4 | 30.77% | 43.46% | Below Benchmark | Monitor |
| University Of St. Louis - Tuguegarao | Private | 45 | 14 | 31.11% | 43.46% | Below Benchmark | Monitor |
| University Of Cagayan Valley | Private | 32 | 10 | 31.25% | 43.46% | Below Benchmark | High |
| Medical Colleges Of Northern Philippines, Cagayan | Private | 19 | 6 | 31.58% | 43.46% | Below Benchmark | High |
| Capitol Medical Center Colleges | Private | 97 | 31 | 31.96% | 43.46% | Below Benchmark | Monitor |
| Philippine Christian University | Private | 25 | 8 | 32.00% | 43.46% | Below Benchmark | Monitor |
| Miriam College Foundation Inc. | Private | 53 | 17 | 32.08% | 43.46% | Below Benchmark | Monitor |
| Manila Doctors College, U.N. Avenue, Manila | Private | 56 | 18 | 32.14% | 43.46% | Below Benchmark | Monitor |
| Perpetual Help College Of Manila | Private | 140 | 45 | 32.14% | 43.46% | Below Benchmark | Monitor |
| St. Jude College | Private | 28 | 9 | 32.14% | 43.46% | Below Benchmark | High |
| Virgen Milagrosa University Foundation And Vmu Institut | Private | 198 | 64 | 32.32% | 43.46% | Below Benchmark | Monitor |
| Davao Doctors College | Private | 246 | 80 | 32.52% | 43.46% | Below Benchmark | High |
| Notre Dame Of Marbel University | Private | 52 | 17 | 32.69% | 43.46% | Below Benchmark | Monitor |
| Emilio Aguinaldo College, Manila | Private | 115 | 38 | 33.04% | 43.46% | Below Benchmark | Monitor |
| Iloilo Doctors' College | Private | 105 | 35 | 33.33% | 43.46% | Below Benchmark | Monitor |
| Kester Grant College Phils. Inc. | Private | 6 | 2 | 33.33% | 43.46% | Below Benchmark | High |
| Manila Adventist Medical Center - Pasay City | Private | 15 | 5 | 33.33% | 43.46% | Below Benchmark | High |
| Lyceum Of The Philippines University | Private | 18 | 6 | 33.33% | 43.46% | Below Benchmark | High |
| Lyceum Of The Philippines - Laguna | Private | 6 | 2 | 33.33% | 43.46% | Below Benchmark | Monitor |
| Iligan Medical Center College | Private | 51 | 17 | 33.33% | 43.46% | Below Benchmark | Monitor |
| St. Anthony College Of Roxas City | Private | 15 | 5 | 33.33% | 43.46% | Below Benchmark | High |
| Unciano Colleges | Private | 9 | 3 | 33.33% | 43.46% | Below Benchmark | Monitor |
| Surigao Education Center | Private | 18 | 6 | 33.33% | 43.46% | Below Benchmark | High |
| Centro Escolar University-Malolos, Bulacan | Private | 9 | 3 | 33.33% | 43.46% | Below Benchmark | High |
| Southern Luzon Polytechnic College - Lucban, Quezon | Private | 6 | 2 | 33.33% | 43.46% | Below Benchmark | Monitor |
| Southwestern University-Matias H. Aznar Memorial Colleg | Private | 90 | 30 | 33.33% | 43.46% | Below Benchmark | Monitor |
| National University - Cedce | Private | 12 | 4 | 33.33% | 43.46% | Below Benchmark | Monitor |
| North Valley College Foundation | Private | 6 | 2 | 33.33% | 43.46% | Below Benchmark | Monitor |
| Medina College - Pagadian | Private | 9 | 3 | 33.33% | 43.46% | Below Benchmark | Monitor |
| Mapua Institute Of Technology | Private | 24 | 8 | 33.33% | 43.46% | Below Benchmark | Monitor |
| University Of La Salette | Private | 48 | 16 | 33.33% | 43.46% | Below Benchmark | Monitor |
| Christ The King College - Calbayog City | Private | 6 | 2 | 33.33% | 43.46% | Below Benchmark | Monitor |
| Unciano Colleges And General Hospital | Private | 6 | 2 | 33.33% | 43.46% | Below Benchmark | Monitor |
| Saint Mary'S College Of San Juan | Private | 6 | 2 | 33.33% | 43.46% | Below Benchmark | Monitor |
| St. Anthony College Of Roxas City, Capiz | Private | 6 | 2 | 33.33% | 43.46% | Below Benchmark | Monitor |
| University Of San Jose Recoletos, Cebu | Private | 18 | 6 | 33.33% | 43.46% | Below Benchmark | Monitor |
| St. Paul University - Manila (St. Paul Univerity System | Private | 111 | 37 | 33.33% | 43.46% | Below Benchmark | High |
| Colegio San Agustin - Bacolod | Private | 74 | 25 | 33.78% | 43.46% | Below Benchmark | High |
| Notre Dame University | Private | 106 | 36 | 33.96% | 43.46% | Below Benchmark | Monitor |
| Feu - East Asia College | Private | 97 | 33 | 34.02% | 43.46% | Below Benchmark | Monitor |
| University Of Baguio, Baguio City | Private | 105 | 36 | 34.29% | 43.46% | Below Benchmark | High |
| Global City Innovative College | Private | 81 | 28 | 34.57% | 43.46% | Below Benchmark | Monitor |
| Southwestern University | Private | 477 | 165 | 34.59% | 43.46% | Below Benchmark | High |
| Our Lady Of Fatima University, Valenzuela City | Private | 245 | 85 | 34.69% | 43.46% | Below Benchmark | High |
| Medical Colleges Of Northern Philippines | Private | 92 | 32 | 34.78% | 43.46% | Below Benchmark | Monitor |
| General Santos Doctors' Medical School Foundation | Private | 23 | 8 | 34.78% | 43.46% | Below Benchmark | Monitor |
| La Consolacion College - Manila | Private | 46 | 16 | 34.78% | 43.46% | Below Benchmark | Monitor |
| Iloilo Doctors College | Private | 43 | 15 | 34.88% | 43.46% | Below Benchmark | Monitor |
| Philippine College Of Health Sciences, Inc. | Private | 20 | 7 | 35.00% | 43.46% | Below Benchmark | High |
| Notre Dame University, Cotabato City | Private | 56 | 20 | 35.71% | 43.46% | Below Benchmark | Monitor |
| Liceo De Cagayan University | Private | 181 | 65 | 35.91% | 43.46% | Below Benchmark | Monitor |
| Southwestern University, Cebu | Private | 189 | 68 | 35.98% | 43.46% | Below Benchmark | Monitor |
| Notre Dame Of Dadiangas University | Private | 97 | 35 | 36.08% | 43.46% | Below Benchmark | High |
| University Of Perpetual Help - Rizal | Private | 11 | 4 | 36.36% | 43.46% | Below Benchmark | Monitor |
| University Of The Immaculate Conception | Private | 96 | 35 | 36.46% | 43.46% | Below Benchmark | Monitor |
| Universidad De Zamboanga | Private | 71 | 26 | 36.62% | 43.46% | Below Benchmark | Monitor |
| Butuan Doctors' College | Private | 19 | 7 | 36.84% | 43.46% | Below Benchmark | Monitor |
| Notre Dame Of Dadiangas College, Gen. Santos | Private | 43 | 16 | 37.21% | 43.46% | Below Benchmark | Monitor |
| University Of The Cordilleras | Private | 196 | 73 | 37.24% | 43.46% | Below Benchmark | Monitor |
| Davao Medical School Foundation | Private | 543 | 203 | 37.38% | 43.46% | Below Benchmark | Monitor |
| Doña Remedios Trinidad Romualdez Medical Foundation | Private | 139 | 52 | 37.41% | 43.46% | Below Benchmark | Monitor |
| Delos Santos College | Private | 8 | 3 | 37.50% | 43.46% | Below Benchmark | Monitor |
| Assumption College | Private | 16 | 6 | 37.50% | 43.46% | Below Benchmark | Monitor |
| Northern Christian College | Private | 8 | 3 | 37.50% | 43.46% | Below Benchmark | Monitor |
| Brokenshire College Socsksargen | Private | 8 | 3 | 37.50% | 43.46% | Below Benchmark | Monitor |
| Notre Dame Of Kidapawan College | Private | 8 | 3 | 37.50% | 43.46% | Below Benchmark | Monitor |
| University Of Luzon | Private | 16 | 6 | 37.50% | 43.46% | Below Benchmark | High |
| De La Salle - Lipa | Private | 178 | 67 | 37.64% | 43.46% | Below Benchmark | High |
| Holy Name University | Private | 77 | 29 | 37.66% | 43.46% | Below Benchmark | Monitor |
| St. Paul University - Tuguegarao, Cagayan | Private | 34 | 13 | 38.24% | 43.46% | Below Benchmark | Monitor |
| Olivarez College | Private | 13 | 5 | 38.46% | 43.46% | Below Benchmark | Monitor |
| La Salle University | Private | 13 | 5 | 38.46% | 43.46% | Below Benchmark | Monitor |
| University Of The East - Manila | Private | 140 | 54 | 38.57% | 43.46% | Below Benchmark | Monitor |
| Mindanao Sanitarium And Hospital College | Private | 145 | 56 | 38.62% | 43.46% | Below Benchmark | Monitor |
| St. Paul University Dumaguete | Private | 31 | 12 | 38.71% | 43.46% | Below Benchmark | Monitor |
| St. Scholastica'S College | Private | 80 | 31 | 38.75% | 43.46% | Below Benchmark | Monitor |
| Philippine Rehabilitation Institute Foundation | Private | 18 | 7 | 38.89% | 43.46% | Below Benchmark | Monitor |
| Davao Medical School Foundation, Inc. | Private | 36 | 14 | 38.89% | 43.46% | Below Benchmark | Monitor |
| Riverside College | Private | 77 | 30 | 38.96% | 43.46% | Below Benchmark | Monitor |
| World Citi Colleges, Quezon City | Private | 41 | 16 | 39.02% | 43.46% | Below Benchmark | Monitor |
| The Philippine Women'S University System - Manila | Private | 23 | 9 | 39.13% | 43.46% | Below Benchmark | Monitor |
| Centro Escolar University - Manila | Private | 764 | 299 | 39.14% | 43.46% | Below Benchmark | High |
| San Beda College, Mendiola, Manila | Private | 166 | 65 | 39.16% | 43.46% | Below Benchmark | Monitor |
| Centro Escolar University At Malolos | Private | 28 | 11 | 39.29% | 43.46% | Below Benchmark | Monitor |
| De La Salle - Lipa, Batangas | Private | 53 | 21 | 39.62% | 43.46% | Below Benchmark | High |
| Capitol University | Private | 63 | 25 | 39.68% | 43.46% | Below Benchmark | Monitor |
| Our Lady Of Fatima University (Fatima Medical Science F | Private | 466 | 185 | 39.70% | 43.46% | Below Benchmark | High |
| Adamson University | Private | 68 | 27 | 39.71% | 43.46% | Below Benchmark | Monitor |
| Manila Doctors College - Pasay City | Private | 83 | 33 | 39.76% | 43.46% | Below Benchmark | Monitor |
| Holy Cross Of Davao College | Private | 5 | 2 | 40.00% | 43.46% | Below Benchmark | Monitor |
| Olivarez College - Tagaytay | Private | 5 | 2 | 40.00% | 43.46% | Below Benchmark | Monitor |
| Jose Rizal University | Private | 5 | 2 | 40.00% | 43.46% | Below Benchmark | Monitor |
| First Asia Institute Of Technology And Humanities | Private | 5 | 2 | 40.00% | 43.46% | Below Benchmark | Monitor |
| Dominican College | Private | 10 | 4 | 40.00% | 43.46% | Below Benchmark | Monitor |
| Good Samaritan Colleges | Private | 5 | 2 | 40.00% | 43.46% | Below Benchmark | Monitor |
| The College Of Maasin | Private | 5 | 2 | 40.00% | 43.46% | Below Benchmark | Monitor |
| De Los Santos - Sti College | Private | 15 | 6 | 40.00% | 43.46% | Below Benchmark | High |
| Univ. Of Asia And The Pacific - Pasig City | Private | 5 | 2 | 40.00% | 43.46% | Below Benchmark | High |
| Saint Paul University Manila | Private | 5 | 2 | 40.00% | 43.46% | Below Benchmark | Monitor |
| St. Paul College, Iloilo | Private | 15 | 6 | 40.00% | 43.46% | Below Benchmark | Monitor |
| College Of The Immaculate Conception | Private | 5 | 2 | 40.00% | 43.46% | Below Benchmark | Monitor |
| De La Salle Araneta University | Private | 5 | 2 | 40.00% | 43.46% | Below Benchmark | Monitor |
| Remedios T. Romualdez Mem. Sch. - Mmc | Private | 75 | 30 | 40.00% | 43.46% | Below Benchmark | Monitor |
| Mountain View College, Bukidnon | Private | 45 | 18 | 40.00% | 43.46% | Below Benchmark | Monitor |
| Butuan Doctors College | Private | 5 | 2 | 40.00% | 43.46% | Below Benchmark | Monitor |
| Wesleyan University-Philippines, Cabanatuan City | Private | 25 | 10 | 40.00% | 43.46% | Below Benchmark | Monitor |
| Xavier University | Private | 594 | 239 | 40.24% | 43.46% | Below Benchmark | Monitor |
| San Beda College | Private | 273 | 110 | 40.29% | 43.46% | Below Benchmark | Monitor |
| Southeast Asian College | Private | 57 | 23 | 40.35% | 43.46% | Below Benchmark | Monitor |
| Manila Tytana Colleges | Private | 380 | 154 | 40.53% | 43.46% | Below Benchmark | Monitor |
| University Of San Carlos | Private | 264 | 107 | 40.53% | 43.46% | Below Benchmark | Monitor |
| University Of San Agustin | Private | 264 | 107 | 40.53% | 43.46% | Below Benchmark | Monitor |
| Easter College | Private | 64 | 26 | 40.62% | 43.46% | Below Benchmark | Monitor |
| St. Paul University - Quezon City | Private | 59 | 24 | 40.68% | 43.46% | Below Benchmark | Monitor |
| Assumption College, Makati | Private | 22 | 9 | 40.91% | 43.46% | Below Benchmark | Monitor |
| De La Salle Health Sciences Institute | Private | 322 | 132 | 40.99% | 43.46% | Below Benchmark | Monitor |
| Lourdes College | Private | 17 | 7 | 41.18% | 43.46% | Below Benchmark | Monitor |
| Wesleyan University - Philippines (Cabanatuan) | Private | 63 | 26 | 41.27% | 43.46% | Below Benchmark | Monitor |
| Makati Medical Center College Of Nursing | Private | 133 | 55 | 41.35% | 43.46% | Below Benchmark | Monitor |
| Angeles University Foundation | Private | 430 | 178 | 41.40% | 43.46% | Below Benchmark | Monitor |
| San Pedro College | Private | 987 | 409 | 41.44% | 43.46% | Below Benchmark | Monitor |
| Our Lady Of Guadalupe Colleges | Private | 12 | 5 | 41.67% | 43.46% | Below Benchmark | Monitor |
| University Of Perpetual Help - Calamba, Laguna | Private | 12 | 5 | 41.67% | 43.46% | Below Benchmark | Monitor |
| Central Philippine University | Private | 285 | 119 | 41.75% | 43.46% | Below Benchmark | Monitor |
| Southville International School And Colleges | Private | 122 | 51 | 41.80% | 43.46% | Below Benchmark | Monitor |
| Misamis University - Ozamis City | Private | 55 | 23 | 41.82% | 43.46% | Below Benchmark | Monitor |
| De La Salle - Health Sciences Campus | Private | 129 | 54 | 41.86% | 43.46% | Below Benchmark | Monitor |
| Brokenshire College, Davao City | Private | 43 | 18 | 41.86% | 43.46% | Below Benchmark | Monitor |
| Adventist University Of The Philippines | Private | 331 | 139 | 41.99% | 43.46% | Below Benchmark | Monitor |
| Central Philippine University, Iloilo | Private | 100 | 42 | 42.00% | 43.46% | Below Benchmark | Monitor |
| Lorma Colleges | Private | 50 | 21 | 42.00% | 43.46% | Below Benchmark | Monitor |
| Our Lady Of Fatima University - Quezon City | Private | 178 | 75 | 42.13% | 43.46% | Below Benchmark | Monitor |
| Feu - Dr. Nicanor Reyes Medical Foundation | Private | 480 | 203 | 42.29% | 43.46% | Below Benchmark | Monitor |
| Our Lady Of Fatima University - Lagro, Quezon City | Private | 52 | 22 | 42.31% | 43.46% | Below Benchmark | Monitor |
| Mindanao Medical Foundation College | Private | 26 | 11 | 42.31% | 43.46% | Below Benchmark | Monitor |
| De La Salle University - Dasmariñas | Private | 588 | 250 | 42.52% | 43.46% | Below Benchmark | Monitor |
| Trinity University Of Asia | Private | 566 | 242 | 42.76% | 43.46% | Below Benchmark | Monitor |
| University Of Perpetual Help System Dalta | Private | 442 | 189 | 42.76% | 43.46% | Below Benchmark | Monitor |
| International Colleges Of Asia - Tambac, Pangasinan | Private | 7 | 3 | 42.86% | 43.46% | Below Benchmark | High |
| Riverside College Of Nursing, Bacolod | Private | 21 | 9 | 42.86% | 43.46% | Below Benchmark | Monitor |
| Arellano University - Manila | Private | 70 | 30 | 42.86% | 43.46% | Below Benchmark | Monitor |
| St. Paul University Surigao | Private | 7 | 3 | 42.86% | 43.46% | Below Benchmark | Monitor |
| Holy Trinity College, Puerto Princesa | Private | 7 | 3 | 42.86% | 43.46% | Below Benchmark | Monitor |
| Far Eastern University | Private | 2,216 | 952 | 42.96% | 43.46% | Below Benchmark | Monitor |
| Lyceum Of Batangas | Private | 30 | 13 | 43.33% | 43.46% | Below Benchmark | Monitor |
| University Of The Cordilleras (Bcf) | Private | 60 | 26 | 43.33% | 43.46% | Below Benchmark | Monitor |
| Mountain View College | Private | 129 | 56 | 43.41% | 43.46% | Below Benchmark | Monitor |
| Pilar College | Private | 23 | 10 | 43.48% | 43.46% | Above Benchmark | Low |
| Lorma College, San Fernando, La Union | Private | 23 | 10 | 43.48% | 43.46% | Above Benchmark | Low |
| St. Scholastica'S College - Tacloban City | Private | 23 | 10 | 43.48% | 43.46% | Above Benchmark | Low |
| Chinese General Hospital College Of Nursing And Liberal | Private | 78 | 34 | 43.59% | 43.46% | Above Benchmark | Low |
| University Of Cebu - Banilad | Private | 103 | 45 | 43.69% | 43.46% | Above Benchmark | Low |
| San Juan De Dios Educational Foundation | Private | 48 | 21 | 43.75% | 43.46% | Above Benchmark | Low |
| Union Christian College | Private | 16 | 7 | 43.75% | 43.46% | Above Benchmark | Low |
| University Of Southern Philippines Foundation | Private | 32 | 14 | 43.75% | 43.46% | Above Benchmark | Low |
| Manila Central University | Private | 351 | 154 | 43.87% | 43.46% | Above Benchmark | Low |
| Uerm Memorial Medical Center | Private | 82 | 36 | 43.90% | 43.46% | Above Benchmark | Low |
| Colegio De San Juan De Letran | Private | 66 | 29 | 43.94% | 43.46% | Above Benchmark | Low |
| University Of Baguio | Private | 175 | 77 | 44.00% | 43.46% | Above Benchmark | Low |
| St. Paul University - Manila | Private | 93 | 41 | 44.09% | 43.46% | Above Benchmark | Low |
| University Of The East Ramon Magsaysay Memorial Medical | Private | 340 | 150 | 44.12% | 43.46% | Above Benchmark | Low |
| Cebu Doctor'S University | Private | 1,148 | 507 | 44.16% | 43.46% | Above Benchmark | Low |
| Centro Escolar University - Mendiola, Manila | Private | 369 | 163 | 44.17% | 43.46% | Above Benchmark | Low |
| Saint Louis University | Private | 1,224 | 541 | 44.20% | 43.46% | Above Benchmark | Low |
| Notre Dame Of Marbel College, South Cotabato | Private | 9 | 4 | 44.44% | 43.46% | Above Benchmark | Low |
| Calayan Educational Foundation | Private | 9 | 4 | 44.44% | 43.46% | Above Benchmark | Low |
| Lipa City Colleges | Private | 9 | 4 | 44.44% | 43.46% | Above Benchmark | Low |
| University Of The Visayas - Mandaue | Private | 27 | 12 | 44.44% | 43.46% | Above Benchmark | Low |
| Naga College Foundation | Private | 9 | 4 | 44.44% | 43.46% | Above Benchmark | Low |
| Holy Angel University, Angeles City | Private | 18 | 8 | 44.44% | 43.46% | Above Benchmark | Low |
| Metropolitan Hospital College Of Nursing | Private | 56 | 25 | 44.64% | 43.46% | Above Benchmark | Low |
| Ateneo De Zamboanga University | Private | 672 | 300 | 44.64% | 43.46% | Above Benchmark | Low |
| San Juan De Dios Educational Foundation, Inc. | Private | 47 | 21 | 44.68% | 43.46% | Above Benchmark | Low |
| University Of Negros Occidental - Recoletos | Private | 67 | 30 | 44.78% | 43.46% | Above Benchmark | Low |
| University Of St. La Salle - Dasmariñas Cavite | Private | 29 | 13 | 44.83% | 43.46% | Above Benchmark | Low |
| St. Joseph'S College Of Quezon City | Private | 29 | 13 | 44.83% | 43.46% | Above Benchmark | Low |
| De La Salle University - Dasmariñas, Cavite | Private | 452 | 203 | 44.91% | 43.46% | Above Benchmark | Low |
| Dr. Carlos S. Lanting College | Private | 40 | 18 | 45.00% | 43.46% | Above Benchmark | Low |
| Velez College | Private | 716 | 324 | 45.25% | 43.46% | Above Benchmark | Low |
| Ateneo De Naga University | Private | 137 | 62 | 45.26% | 43.46% | Above Benchmark | Low |
| Saint Mary'S University | Private | 75 | 34 | 45.33% | 43.46% | Above Benchmark | Low |
| University Of Cordilleras | Private | 11 | 5 | 45.45% | 43.46% | Above Benchmark | Low |
| Brokenshire College | Private | 198 | 90 | 45.45% | 43.46% | Above Benchmark | Low |
| Lyceum Of The Philippines - St. Cabrini College Of Alli | Private | 11 | 5 | 45.45% | 43.46% | Above Benchmark | Low |
| University Of Nueva Caceres | Private | 33 | 15 | 45.45% | 43.46% | Above Benchmark | Low |
| Northwestern University | Private | 11 | 5 | 45.45% | 43.46% | Above Benchmark | Low |
| Colegio De San Agustin, Bacolod | Private | 22 | 10 | 45.45% | 43.46% | Above Benchmark | Low |
| University Of Perpetual Help System - Binan, Laguna | Private | 44 | 20 | 45.45% | 43.46% | Above Benchmark | Low |
| Notre Dame Of Marbel Univ. | Private | 11 | 5 | 45.45% | 43.46% | Above Benchmark | Low |
| University Of Negros Occidental-Recoletos | Private | 24 | 11 | 45.83% | 43.46% | Above Benchmark | Low |
| University Of San Jose - Recoletos | Private | 24 | 11 | 45.83% | 43.46% | Above Benchmark | Low |
| Holy Angel University | Private | 50 | 23 | 46.00% | 43.46% | Above Benchmark | Low |
| Cebu Institute Of Technology - University | Private | 13 | 6 | 46.15% | 43.46% | Above Benchmark | Low |
| Manila Adventist Medical Center And Colleges | Private | 26 | 12 | 46.15% | 43.46% | Above Benchmark | Low |
| Ago Medical And Educational Center - Bicol Christian Co | Private | 39 | 18 | 46.15% | 43.46% | Above Benchmark | Low |
| Colegio De Dagupan | Private | 13 | 6 | 46.15% | 43.46% | Above Benchmark | Low |
| Saint Paul University Philippines | Private | 181 | 84 | 46.41% | 43.46% | Above Benchmark | Low |
| University Of St. La Salle | Private | 391 | 182 | 46.55% | 43.46% | Above Benchmark | Low |
| Silliman University | Private | 601 | 281 | 46.76% | 43.46% | Above Benchmark | Low |
| San Pedro College, Davao City | Private | 491 | 231 | 47.05% | 43.46% | Above Benchmark | Low |
| University Of Pangasinan, Dagupan City | Private | 17 | 8 | 47.06% | 43.46% | Above Benchmark | Low |
| Ago Medical And Educational Center, Legazpi City | Private | 19 | 9 | 47.37% | 43.46% | Above Benchmark | Low |
| University Of Perpetual Help System - Laguna | Private | 38 | 18 | 47.37% | 43.46% | Above Benchmark | Low |
| De La Salle - College Of Saint Benilde | Private | 19 | 9 | 47.37% | 43.46% | Above Benchmark | Low |
| University Of Perpetual Help College Of Las Pinas | Private | 19 | 9 | 47.37% | 43.46% | Above Benchmark | Low |
| Central Luzon Doctor'S Hospital, Tarlac | Private | 21 | 10 | 47.62% | 43.46% | Above Benchmark | Low |
| Cebu Doctor'S University College Of Medicine - Mandaue  | Private | 50 | 24 | 48.00% | 43.46% | Above Benchmark | Low |
| Universidad De Sta. Isabel | Private | 152 | 73 | 48.03% | 43.46% | Above Benchmark | Low |
| New Era University | Private | 56 | 27 | 48.21% | 43.46% | Above Benchmark | Low |
| St. Paul University Iloilo | Private | 169 | 82 | 48.52% | 43.46% | Above Benchmark | Low |
| University Of Pangasinan | Private | 70 | 34 | 48.57% | 43.46% | Above Benchmark | Low |
| University Of Perpetual Help - Dr. Jose G. Tamayo Medic | Private | 47 | 23 | 48.94% | 43.46% | Above Benchmark | Low |
| Lyceum Of The Philippines University - Batangas | Private | 104 | 51 | 49.04% | 43.46% | Above Benchmark | Low |
| Cebu Doctors College, Cebu City | Private | 148 | 73 | 49.32% | 43.46% | Above Benchmark | Low |
| University Of Santo Tomas | Private | 10,720 | 5,337 | 49.79% | 43.46% | Above Benchmark | Low |
| St. Jude College, Manila | Private | 36 | 18 | 50.00% | 43.46% | Above Benchmark | Low |
| Arriesgado College Foundation | Private | 6 | 3 | 50.00% | 43.46% | Above Benchmark | Low |
| Our Lady Of Fatima, Novaliches | Private | 6 | 3 | 50.00% | 43.46% | Above Benchmark | Low |
| Philippine Rehabilitation Institute | Private | 12 | 6 | 50.00% | 43.46% | Above Benchmark | Low |
| Mary Help Of Christians College Seminary | Private | 10 | 5 | 50.00% | 43.46% | Above Benchmark | Low |
| National University | Private | 10 | 5 | 50.00% | 43.46% | Above Benchmark | Low |
| Manuel S. Enverga University Foundation - Lucena | Private | 8 | 4 | 50.00% | 43.46% | Above Benchmark | Low |
| Sacred Heart College, Lucena City | Private | 12 | 6 | 50.00% | 43.46% | Above Benchmark | Low |
| Aldersgate College | Private | 6 | 3 | 50.00% | 43.46% | Above Benchmark | Low |
| Andres Bonifacio College | Private | 6 | 3 | 50.00% | 43.46% | Above Benchmark | Low |
| Mabini Colleges | Private | 6 | 3 | 50.00% | 43.46% | Above Benchmark | Low |
| Lyceum Of The Philippines | Private | 14 | 7 | 50.00% | 43.46% | Above Benchmark | Low |
| Immaculate Conception College - Albay | Private | 6 | 3 | 50.00% | 43.46% | Above Benchmark | Low |
| La Consolacion University Philippines | Private | 6 | 3 | 50.00% | 43.46% | Above Benchmark | Low |
| Universidad De Sta. Isabel, Naga City | Private | 38 | 19 | 50.00% | 43.46% | Above Benchmark | Low |
| Father Saturnino M. Urios University | Private | 46 | 23 | 50.00% | 43.46% | Above Benchmark | Low |
| University Of Perpetual Help Dalta System-Alabang Zapot | Private | 8 | 4 | 50.00% | 43.46% | Above Benchmark | Low |
| University Of La Salette, Santiago City | Private | 20 | 10 | 50.00% | 43.46% | Above Benchmark | Low |
| University Of The Immaculate Concepcion, Davao City | Private | 24 | 12 | 50.00% | 43.46% | Above Benchmark | Low |
| Caritas Family Hospital And Colleges | Private | 8 | 4 | 50.00% | 43.46% | Above Benchmark | Low |
| Saint Scholastica'S College Tacloban | Private | 112 | 56 | 50.00% | 43.46% | Above Benchmark | Low |
| San Lorenzo Ruiz College Of Ormoc | Private | 16 | 8 | 50.00% | 43.46% | Above Benchmark | Low |
| Ateneo De Davao University | Private | 718 | 360 | 50.14% | 43.46% | Above Benchmark | Low |
| University Of The East (C.M. Recto, Manila) | Private | 123 | 62 | 50.41% | 43.46% | Above Benchmark | Low |
| University Of The East - Ramon Magsaysay Mem. Medical C | Private | 55 | 28 | 50.91% | 43.46% | Above Benchmark | Low |
| University Of San Agustin - Iloilo City | Private | 104 | 53 | 50.96% | 43.46% | Above Benchmark | Low |
| Ateneo De Manila University - Quezon City | Private | 973 | 503 | 51.70% | 43.46% | Above Benchmark | Low |
| Central Luzon Doctors' Hospital Educational Institution | Private | 29 | 15 | 51.72% | 43.46% | Above Benchmark | Low |
| Holy Infant College | Private | 27 | 14 | 51.85% | 43.46% | Above Benchmark | Low |
| University Of St. La Salle, Bacolod City | Private | 96 | 50 | 52.08% | 43.46% | Above Benchmark | Low |
| West Negros University | Private | 23 | 12 | 52.17% | 43.46% | Above Benchmark | Low |
| Aquinas University Of Legazpi | Private | 69 | 36 | 52.17% | 43.46% | Above Benchmark | Low |
| Remedios Trinidad Romualdez Medical Foundation, Tacloba | Private | 109 | 57 | 52.29% | 43.46% | Above Benchmark | Low |
| Chinese General Hospital College Of Nursing & Liberal A | Private | 19 | 10 | 52.63% | 43.46% | Above Benchmark | Low |
| University Of Asia And The Pacific | Private | 17 | 9 | 52.94% | 43.46% | Above Benchmark | Low |
| University Of San Carlos, Cebu City | Private | 157 | 86 | 54.78% | 43.46% | Above Benchmark | Low |
| Lyceum Of Iligan Foundation | Private | 9 | 5 | 55.56% | 43.46% | Above Benchmark | Low |
| Xavier University, Cagayan De Oro City | Private | 339 | 189 | 55.75% | 43.46% | Above Benchmark | Low |
| Lyceum Northwestern, Dagupan City | Private | 64 | 36 | 56.25% | 43.46% | Above Benchmark | Low |
| St. Louis University, Baguio City | Private | 199 | 113 | 56.78% | 43.46% | Above Benchmark | Low |
| Cordillera Career Development College | Private | 7 | 4 | 57.14% | 43.46% | Above Benchmark | Low |
| Arellano University - Pasig | Private | 14 | 8 | 57.14% | 43.46% | Above Benchmark | Low |
| Saint Paul University Iloilo | Private | 7 | 4 | 57.14% | 43.46% | Above Benchmark | Low |
| Colegio De San Lorenzo Ruiz De Manila Of Northern Samar | Private | 7 | 4 | 57.14% | 43.46% | Above Benchmark | Low |
| Saint Louis University - Baguio | Private | 374 | 214 | 57.22% | 43.46% | Above Benchmark | Low |
| Riverside College, Bacolod City | Private | 26 | 15 | 57.69% | 43.46% | Above Benchmark | Low |
| St. Paul University, Iloilo | Private | 24 | 14 | 58.33% | 43.46% | Above Benchmark | Low |
| Sacred Heart College Of Lucena | Private | 36 | 21 | 58.33% | 43.46% | Above Benchmark | Low |
| Far Eastern University - Nrmf (Fairview, Q.C.) | Private | 409 | 239 | 58.44% | 43.46% | Above Benchmark | Low |
| De La Salle University - Manila | Private | 1,382 | 811 | 58.68% | 43.46% | Above Benchmark | Low |
| University Of Bohol | Private | 10 | 6 | 60.00% | 43.46% | Above Benchmark | Low |
| College Of The Holy Spirit Of Tarlac | Private | 5 | 3 | 60.00% | 43.46% | Above Benchmark | Low |
| Central Philippine Adventist College | Private | 35 | 21 | 60.00% | 43.46% | Above Benchmark | Low |
| De La Salle, College Of Saint Benilde - Manila | Private | 20 | 12 | 60.00% | 43.46% | Above Benchmark | Low |
| Colegio De San Juan De Letran, Manila | Private | 5 | 3 | 60.00% | 43.46% | Above Benchmark | Low |
| Plt College | Private | 5 | 3 | 60.00% | 43.46% | Above Benchmark | Low |
| St. Alexius College | Private | 10 | 6 | 60.00% | 43.46% | Above Benchmark | Low |
| Aquinas University, Legaspi City | Private | 20 | 12 | 60.00% | 43.46% | Above Benchmark | Low |
| Central College Of Pangasinan - San Carlos City, Pangas | Private | 5 | 3 | 60.00% | 43.46% | Above Benchmark | Low |
| Centro Escolar University Makati | Private | 5 | 3 | 60.00% | 43.46% | Above Benchmark | Low |
| University Of Cebu (Formerly Cebu Central Colleges) | Private | 28 | 17 | 60.71% | 43.46% | Above Benchmark | Low |
| Canossa College | Private | 13 | 8 | 61.54% | 43.46% | Above Benchmark | Low |
| Holy Name University - Tagbilaran City | Private | 21 | 13 | 61.90% | 43.46% | Above Benchmark | Low |
| Chiang Kai Shek College | Private | 8 | 5 | 62.50% | 43.46% | Above Benchmark | Low |
| Silliman University, Dumaguete City | Private | 221 | 139 | 62.90% | 43.46% | Above Benchmark | Low |
| Baliuag University | Private | 11 | 7 | 63.64% | 43.46% | Above Benchmark | Low |
| College Of Holy Spirit-Manila | Private | 11 | 7 | 63.64% | 43.46% | Above Benchmark | Low |
| John Paul Ii College Of Davao | Private | 14 | 9 | 64.29% | 43.46% | Above Benchmark | Low |
| Velez College, Cebu | Private | 546 | 352 | 64.47% | 43.46% | Above Benchmark | Low |
| Central Philippine Adventist College, Negros Occidental | Private | 12 | 8 | 66.67% | 43.46% | Above Benchmark | Low |
| University Of Iloilo | Private | 9 | 6 | 66.67% | 43.46% | Above Benchmark | Low |
| Ago Medical Educational Foundation, Legaspi City | Private | 6 | 4 | 66.67% | 43.46% | Above Benchmark | Low |
| Notre Dame Of Midsayap College | Private | 6 | 4 | 66.67% | 43.46% | Above Benchmark | Low |
| Fellowship Baptist College | Private | 6 | 4 | 66.67% | 43.46% | Above Benchmark | Low |
| University Of Bohol, Tagbilaran City | Private | 13 | 9 | 69.23% | 43.46% | Above Benchmark | Low |
| Ateneo De Manila University | Private | 721 | 503 | 69.76% | 43.46% | Above Benchmark | Low |
| University Of Luzon ( Dagupan City ) | Private | 7 | 5 | 71.43% | 43.46% | Above Benchmark | Low |
| University Of Perpetual Help System Dalta - Calamba | Private | 14 | 10 | 71.43% | 43.46% | Above Benchmark | Low |
| Calamba Doctors' College | Private | 9 | 7 | 77.78% | 43.46% | Above Benchmark | Low |
| San Sebastian College - Recoletos, Canlubang | Private | 5 | 4 | 80.00% | 43.46% | Above Benchmark | Low |
| University Of Cebu - Lapulapu And Mandaue | Private | 5 | 4 | 80.00% | 43.46% | Above Benchmark | Low |
| Centro Escolar University-Makati | Private | 6 | 5 | 83.33% | 43.46% | Above Benchmark | Low |

_Table shows 385 PHEIs with ≥5 examinees in the observable cohort, ranked by linkage rate (lowest first). 71 High-risk and 164 Monitor-level PHEIs identified._

### Risk Distribution Summary

| Risk Level | PHEIs | % of Total |
|:----------:|:----:|:----------:|
| High | 71 | 18.4% |
| Monitor | 164 | 42.6% |
| Low | 150 | 39.0% |

### Bottom 20 PHEIs — Detail

The following PHEIs have the lowest NMAT-to-PLE linkage rates in the observable cohort. These institutions warrant priority attention.

| Rank | HEI | n (Obs.) | Linkage Rate | Risk Level |
|:----:|------|:--------:|:------------:|:----------:|
| 1 | St. Luke'S School Of Medicine, India | 10 | 0.00% | High |
| 2 | Laguna College | 7 | 0.00% | High |
| 3 | St. Paul University Philippines | 5 | 0.00% | High |
| 4 | Divine Word College Of Laoag | 107 | 0.00% | High |
| 5 | Malasiqui Agno Valley College | 7 | 0.00% | High |
| 6 | Ama Computer College | 12 | 8.33% | High |
| 7 | Virgen Milagrosa Educational Institute, San Carlos City | 11 | 9.09% | High |
| 8 | Dr. Carlos Lanting College - Novaliches, Quezon City | 10 | 10.00% | High |
| 9 | Northern Luzon Adventist College | 9 | 11.11% | Monitor |
| 10 | Mindanao Medical Foundation College, Davao | 9 | 11.11% | Monitor |
| 11 | Dominican College, Blum, San Juan, Mm | 9 | 11.11% | High |
| 12 | University Of Visayas, Cebu | 69 | 11.59% | High |
| 13 | Virgen Milagrosa Univ. Foundation - San Carlos City, Pang. | 76 | 13.16% | High |
| 14 | University Of Mindanao | 7 | 14.29% | Monitor |
| 15 | Kester Grant College - Philippines | 21 | 14.29% | High |
| 16 | University Of Perpetual Help System | 7 | 14.29% | Monitor |
| 17 | Southeast Asian College Inc.-Quezon City | 14 | 14.29% | Monitor |
| 18 | San Sebastian College | 7 | 14.29% | Monitor |
| 19 | St. Paul University Manila | 6 | 16.67% | Monitor |
| 20 | Medina College | 24 | 16.67% | High |

### Multi-Year Trend Flagging

For each HEI classified as **High Risk**, we examined whether the linkage rate fell below benchmark in **every available year** with ≥5 examinees. This approximates the CMO's intent to track persistent underperformance. Note that the available data covers only 2006–2014 for the observable cohort (9 years), and many HEIs have data for only a subset of those years.


- **71 PHEI(s)** classified as High Risk (below benchmark in all available years)

- **164 PHEI(s)** classified as Monitor (below benchmark overall but above in at least one year)

> **Policy Note:** Full 3-year consecutive tracking (as specified in the draft CMO) cannot be computed from this dataset because NMAT data ends in 2018 and the observable PLE cohort ends in 2014. CHED must collect prospective data starting AY 2026-2027 to enable proper multi-year consecutive monitoring.

## Section B: Monitoring Framework Template

The following template outlines the data CHED should collect annually from each HEI to operationalise CMO Section VI monitoring requirements. This is a **policy design instrument** — the data to populate it does not yet exist in this dataset.

| # | Metric | Definition | Collection Frequency | Responsible Party |
|:-:|--------|------------|:-------------------:|:-----------------:|
| 1 | NMAT Cut-Off Implemented | Whether the HEI has set and published an NMAT cut-off score ≥30th percentile (B4+). | Annual (start of AY) | HEI Registrar / Admissions |
| 2 | Cut-Off Score Value | The specific NMAT percentile ranking adopted as minimum requirement. | Annual (start of AY) | HEI Registrar / Admissions |
| 3 | Composite Ranking System | Whether the HEI uses a holistic ranking (≥60% NMAT + ≤40% GWA or other academic criteria) for admission. | Annual (start of AY) | HEI Academic Council |
| 4 | GWA Collection Rate | Share of applicants with complete GWA records submitted alongside NMAT. | Per admission cycle | HEI Registrar |
| 5 | Foreign Student Slots Used | Number of foreign nationals enrolled, with cap compliance (≤10 per SUC, ≤ per-program limits). | Annual (end of AY) | HEI Office of Student Affairs |
| 6 | NMAT Examinee Volume | Total number of NMAT examinees from the HEI (best-record basis). | Annual (after NMAT release) | CEM / CHED |
| 7 | NMAT-to-PLE Linkage Rate | Share of NMAT examinees from 5+ years prior found in PLE passer records. Proxy for program quality. | Every 3 years (rolling) | CHED / PRC data sharing |
| 8 | PLE Pass Rate (when available) | First-time PLE takers' pass rate for the HEI's medical program. | Annual (after PLE results) | PRC / CHED |
| 9 | Student-Teacher Ratio | Ratio of enrolled medical students to qualified faculty. | Annual | HEI |
| 10 | Program Compliance Status | Overall compliance rating: Compliant, Partially Compliant, Non-Compliant. | Annual | CHED Regional Office |

> **Note:** Metrics 1–5 rely on HEI self-reporting. Metrics 6–8 require data-sharing agreements between CEM, PRC, and CHED. Metric 9 requires HEI faculty records. The PHEI Risk Flags from Section A above serve as a retrospective proxy for Metric 7 until prospective data collection begins.

## Section C: Transition Timeline (CMO Transitory Provision)

The draft CMO No. __, s. 2026 takes effect at the start of **AY 2026-2027**. The following timeline outlines key milestones and actions required of HEIs to achieve full compliance. This is a **policy design document**, not data-driven.

| Phase | Period | Action | Responsible | Verification |
|:-----:|:------:|--------|:-----------:|:------------:|
| Pre-1 | Q1–Q2 2026 | CHED publishes IRR and compliance guidelines; disseminate to all HEIs. | CHED Central Office | IRR published, memo sent to HEIs |
| Pre-2 | Q2–Q3 2026 | HEIs review current NMAT cut-off policies; identify gaps. | HEI Administration | Self-assessment report |
| Pre-3 | Q3 2026 | HEIs set or adjust NMAT cut-off to ≥30th percentile (B4+); publish in admission materials. | HEI Academic Council | Published cut-off, board resolution |
| Pre-4 | Q3 2026 | HEIs design composite ranking system: ≥60% NMAT + ≤40% GWA. | HEI Admissions Office | Approved ranking formula |
| 1 | AY 2026-2027 Start | New admission cycle begins with CMO-compliant cut-off and ranking. | HEI Registrar | Admission records |
| 2 | AY 2026-2027 Mid | First annual compliance report due to CHED. | HEI Compliance Officer | Compliance report submitted |
| 3 | AY 2026-2027 End | CHED conducts first annual monitoring visit or desk audit. | CHED Regional Office | Monitoring report |
| 4 | AY 2027-2028 | First foreign slot cap verification; review of cut-off compliance. | CHED + HEIs | Slot utilization report |
| 5 | AY 2028-2029 | First NMAT-to-PLE linkage rate review (observable 5-year cohort from start) — earliest point for accountability trigger. | CHED + PRC | Linkage rate analysis |
| 6 | AY 2029-2030 | First round of potential sanctions for persistently non-compliant HEIs. | CHED | Show-cause order/remedial plan |

> **Important:** The accountability trigger (consecutive years below benchmark) cannot be evaluated before AY 2028-2029 at the earliest, because it requires at least 3 years of prospective linkage data (from AY 2026-2027 intake) plus 5 years for those students to reach PLE.

## Section D: Data Gap Recommendations

Full implementation of the CMO accountability framework requires data that does not currently exist in the NMAT_Exodus dataset. The following recommendations are ordered by priority and estimated effort.

| Priority | Data Requirement | Purpose | Current Gap | Effort | Timeline |
|:-------:|------------------|---------|:-----------:|:-----:|:--------:|
| P1 | HEI-submitted NMAT cut-off values per program per AY | Verify cut-off ≥30th percentile compliance | Not collected; no baseline | High | AY 2026-2027 |
| P1 | GWA records per examinee (linked to NMAT score) | Enable composite ranking monitoring | Not in dataset; CHED must mandate submission | High | AY 2026-2027 |
| P2 | Annual enrollment counts by citizenship | Verify foreign slot cap (≤10 per SUC) | Dataset has examinee counts only, not enrollment | Medium | AY 2027-2028 |
| P2 | PLE pass/fail records per HEI per year | Compute actual PLE pass rate (not just linkage rate) | PRC PLE data not linked to NMAT person-level data | Medium | AY 2027-2028 |
| P2 | HEI compliance self-report submissions | Populate monitoring template | No reporting mechanism exists yet | Medium | AY 2026-2027 |
| P3 | Faculty-to-student ratios per medical program | Program quality indicator | Not collected in this dataset | Low | AY 2027-2028 |
| P3 | Program accreditation status (e.g., PAASCU, AACCUP) | Context for compliance evaluation | Not linked to NMAT data | Low | AY 2028-2029 |
| P3 | Continuous NMAT data feed from CEM | Enable year-over-year trend monitoring beyond 2018 | CEM data ends at 2018; no agreement for ongoing feed | Low | Ongoing |

**Priority Definitions:** P1 = Required for baseline CMO compliance verification. P2 = Required for full monitoring framework. P3 = Desirable for comprehensive evaluation.

**Effort Estimates:** High = New MOA/data-sharing agreement or legislative mandate required. Medium = Extension of existing data-sharing arrangement. Low = Automated or existing collection mechanism.

> **Recommendation:** CHED should prioritise P1 items before AY 2026-2027 to establish baseline compliance when the CMO takes effect. The NMAT-to-PLE linkage rate (from this dataset) serves as an interim, retrospective accountability tool until prospective P1 data collection begins.

## Limitations

1. **Data recency:** NMAT data covers 2006–2018 only. The 8-year gap to AY 2026-2027 means risk flags are historical, not current.

2. **PLE linkage ≠ PLE pass rate:** Our dataset contains PLE passers only. We cannot distinguish between 'did not take PLE' and 'took PLE and failed.'

3. **HEI name disambiguation:** Some HEIs may appear under slightly different names in different years. We used NMA_College as-is.

4. **Observable cohort limit:** Full accountability can only be assessed 5+ years after CMO implementation (earliest: AY 2031-2032).

5. **No GWA data:** The composite ranking formula (≥60% NMAT + ≤40% GWA) cannot be verified from this dataset.

6. **Foreign slot monitoring:** Our counts are examinee-level, not enrollment-level. Enforcement requires enrollment data from HEIs.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

