# Per-HEI NMAT Score Distribution Analysis

**Date:** July 28, 2026
**Data Source:** `NMAT_Exodus.parquet` (178,927 records, 54 columns)
**Script:** `ched_compute/03_per_hei_distribution.py`

---

## Results

This section examines the NMAT score distribution at the institution (HEI) level. Only HEIs with 5 or more examinees are included in the detailed analysis. HEIs with fewer than 5 examinees are flagged as having insufficient data.

### Key Metrics

| Metric | Value |
|--------|-------|
| **Total HEIs Represented** | 2,856 |
| **HEIs with >=5 Examinees (Analyzed)** | 669 |
| **HEIs with <5 Examinees (Insufficient Data)** | 2,187 |
| **Total Examinees in Analyzed HEIs** | 130,715 |
| **Total Examinees in Insufficient-Data HEIs** | 3,089 |
| **Top HEI by Median Percentile** | University Of British Columbia, Canada |
| **Bottom HEI by Median Percentile** | Ramkhamhaeng Univ. |

### Top 25 HEIs by Median NMAT Percentile

HEIs with >=5 examinees, ranked by median NMS_PER_num (percentile).

| Rank | HEI | UNI_TYPE | n | Median Pctl |  | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 |
|:----:|------|:--------:|:--:|:----------:| :---: :---: :---: :---: :---: :---: :---: :---: :---: :---:
| 1 | University Of British Columbia, Canada | Foreign | 5 | 96.0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 4 |
| 2 | University Of Texas | Foreign | 8 | 96.0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 4 |
| 3 | Centro Escolar University-Makati | Private | 6 | 90.0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 3 |
| 4 | Rutgers College, New Jersey | Foreign | 5 | 90.0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 3 |
| 5 | Ateneo De Manila University | Private | 721 | 89.0 | 0 | 0 | 1 | 3 | 9 | 19 | 38 | 64 | 232 | 348 |
| 6 | University of the Philippines - Manila | Public | 5 | 87.0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 2 |
| 7 | University Of California, Riverside, ... | Foreign | 25 | 84.0 | 0 | 0 | 1 | 1 | 2 | 1 | 4 | 2 | 6 | 8 |
| 8 | University Of Illinois, Chicago | Foreign | 8 | 83.5 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 3 |
| 9 | University Of California, Los Angeles | Foreign | 24 | 83.0 | 1 | 0 | 0 | 0 | 1 | 2 | 3 | 3 | 6 | 7 |
| 10 | California State University, Long Beach | Foreign | 5 | 82.0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 1 |
| 11 | Univ. Of Asia And The Pacific - Pasig... | Private | 5 | 81.0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 1 |
| 12 | University Of California, San Diego | Foreign | 19 | 81.0 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 3 | 6 | 5 |
| 13 | University Of The Philippines - Los B... | Public | 450 | 81.0 | 0 | 3 | 1 | 10 | 20 | 38 | 62 | 80 | 99 | 134 |
| 14 | University Of The Philippines - Manila | Public | 3,533 | 81.0 | 225 | 180 | 175 | 162 | 202 | 197 | 226 | 277 | 470 | 1292 |
| 15 | University Of The Philippines In The ... | Public | 34 | 81.0 | 1 | 0 | 0 | 0 | 2 | 4 | 4 | 6 | 6 | 11 |
| 16 | University of Santo Tomas | Private | 26 | 81.0 | 1 | 1 | 0 | 0 | 2 | 2 | 1 | 5 | 7 | 7 |
| 17 | Virginia Commonwealth University | Foreign | 8 | 81.0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 2 | 2 |
| 18 | Colegio De San Lorenzo | Private | 6 | 80.0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 1 |
| 19 | University Of California, Berkeley | Foreign | 15 | 80.0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 3 | 5 |
| 20 | University Of California, Davis | Foreign | 34 | 80.0 | 2 | 0 | 0 | 4 | 2 | 1 | 3 | 5 | 7 | 10 |
| 21 | St. Joseph College Amaya | Private | 6 | 79.5 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 1 |
| 22 | University Of California, Irvine | Foreign | 34 | 79.5 | 0 | 1 | 1 | 0 | 1 | 0 | 8 | 6 | 9 | 8 |
| 23 | Lipa City Colleges | Private | 15 | 79.0 | 1 | 1 | 0 | 3 | 1 | 1 | 0 | 1 | 2 | 5 |
| 24 | University Of Washington | Foreign | 15 | 79.0 | 1 | 0 | 0 | 0 | 1 | 3 | 1 | 2 | 1 | 6 |
| 25 | East Africa University | Foreign | 6 | 78.5 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 3 | 0 |

### Bottom 25 HEIs by Median NMAT Percentile

HEIs with >=5 examinees, ranked by lowest median NMS_PER_num.

| Rank | HEI | UNI_TYPE | n | Median Pctl |  | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 |
|:----:|------|:--------:|:--:|:----------:| :---: :---: :---: :---: :---: :---: :---: :---: :---: :---:
| 1 | Ramkhamhaeng Univ. | Foreign | 5 | 2.0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | University Of The Immaculate Concepti... | Private | 5 | 5.0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 3 | Siam University | Foreign | 5 | 8.0 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| 4 | Southeast Asian College Inc.-Espana, ... | Private | 12 | 8.0 | 7 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | Catanduanes State College | Public | 7 | 9.0 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| 6 | Malasiqui Agno Valley College | Private | 7 | 9.0 | 4 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 7 | St. Andrew'S International Academy, I... | Foreign | 5 | 9.0 | 3 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 8 | Brent Hospital And Colleges Inc., Zam... | Private | 11 | 10.0 | 5 | 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 9 | University Of Visayas, Cebu | Private | 69 | 10.0 | 30 | 11 | 5 | 7 | 5 | 4 | 1 | 1 | 1 | 1 |
| 10 | Burapha University | Foreign | 9 | 11.0 | 4 | 3 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 11 | Notre Dame Of Jolo College, Jolo, Sulu | Private | 11 | 11.0 | 5 | 2 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| 12 | Rangsit University, Thailand | Foreign | 33 | 11.0 | 16 | 4 | 4 | 3 | 3 | 2 | 0 | 0 | 0 | 1 |
| 13 | University Of Northern Philippines, C... | Public | 53 | 11.0 | 22 | 6 | 6 | 4 | 3 | 3 | 2 | 3 | 1 | 1 |
| 14 | University Of Northern Philippines, V... | Public | 8 | 11.0 | 4 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 15 | Kester Grant College Phils. Inc. | Private | 6 | 12.0 | 1 | 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 16 | College Of St. John - Roxas | Private | 8 | 13.0 | 2 | 2 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| 17 | Negros Oriental State University | Public | 7 | 13.0 | 2 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 18 | Philippine College Of Health Sciences... | Private | 20 | 13.0 | 8 | 4 | 2 | 1 | 4 | 0 | 0 | 1 | 0 | 0 |
| 19 | Cagayan State University - Tuguegarao | Public | 63 | 14.0 | 22 | 13 | 6 | 6 | 4 | 3 | 3 | 1 | 2 | 0 |
| 20 | Novagen College Of Quezon City | Private | 6 | 14.0 | 3 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| 21 | Qiqihar Medical University | Not Specified | 6 | 14.0 | 2 | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| 22 | Saint Mary'S College Of San Juan | Private | 7 | 14.0 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| 23 | St. Joseph College, Cavite | Private | 7 | 14.0 | 3 | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 |
| 24 | University Of Eastern Philippines - S... | Public | 16 | 14.0 | 6 | 5 | 3 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 25 | University Of Texas At Arlington | Foreign | 5 | 14.0 | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |

### Summary by University Type

Aggregated HEI-level statistics by UNI_TYPE.

| UNI_TYPE | HEIs (>=5) | Total Examinees | Median Pctl (Median of HEI Medians) | Avg HEI Size |
|:---------|:----------:|:---------------:|:-----------------------------------:|:------------:|
| Public | 123 | 27,426 | 48.0 | 223 |
| Private | 453 | 102,055 | 43.0 | 225 |
| Foreign | 79 | 978 | 50.0 | 12 |
| Not Specified | 14 | 256 | 43.5 | 18 |

### HEIs with Insufficient Data (<5 Examinees)

There are 2187 HEIs with fewer than 5 examinees (totaling 3089 examinees). These are excluded from ranking analysis but listed below.

| HEI | UNI_TYPE | n |
|-----|:--------:|:-:|
| 08059A | Not Specified | 1 |
| A-Jou University | Not Specified | 1 |
| A.K.P.S.B.P.Collage Of Education | Not Specified | 1 |
| A.L Ayurvedic Medical College | Not Specified | 1 |
| A.M.Shaikh Homoeopathic Medical College/Rajiv G... | Not Specified | 1 |
| A.P.S University, Rewa | Not Specified | 1 |
| AMA Computer College - Makati | Private | 3 |
| AMINU KANO TEACHING HOSPITAL SCHOOL OF HEALTH I... | Not Specified | 1 |
| ARIZONA STATE UNIVERSITY | Foreign | 1 |
| Abada College | Private | 4 |
| Abcd | Not Specified | 1 |
| Abd | Not Specified | 1 |
| Abe International Business College - Caloocan City | Not Specified | 1 |
| Abe International College Of Business And Accou... | Private | 3 |
| Abe International College Of Business And Econo... | Private | 1 |
| Abia State University | Not Specified | 1 |
| Abia State University Uturu | Not Specified | 1 |
| Abilene Christian University | Not Specified | 1 |
| Abra State Institute Of Science & Tech., Abra | Public | 1 |
| Abra Valley Colleges | Private | 2 |
| Access Computer And Technical Colleges - Manila | Private | 1 |
| Acharya Nagarjuna University | Foreign | 1 |
| Aclc College - Ormoc | Not Specified | 1 |
| Aclc College Of Bukidnon | Private | 1 |
| Addis Ababa University | Not Specified | 1 |
| Adekunle Ajasin University, Akungba -Akoko, Ond... | Not Specified | 1 |
| Adelphi University, New York, U.S.A. | Foreign | 2 |
| Adhiyaman Matric Higher Secondary School | Not Specified | 1 |
| Adventist University Of Health Sciences | Not Specified | 1 |
| Adventist University of the Philippines | Private | 1 |
| Ago Foundation College - Naga City, Camarines Sur | Private | 1 |
| Ago Medical And Educational Center | Private | 1 |
| Ago Medical Foundation, Naga City | Private | 3 |
| Ago Medical and Educational Center - Bicol Chri... | Private | 3 |
| Agoo Computer College Philippines | Not Specified | 2 |
| Agro - Industrial Foundation College Of The Phi... | Not Specified | 1 |
| Agusan Del Sur State College Of Agriculture And... | Public | 1 |
| Ahmadu Bello University Zaria | Not Specified | 1 |
| Ahmadu Bello University, Zaria | Not Specified | 1 |
| Ahmadu Bello University,Zaria,Nigeria | Not Specified | 1 |
| Air Link International Aviation College | Private | 1 |
| Airlangga University | Foreign | 1 |
| Ajayi Crowther University | Foreign | 1 |
| Akt Matric Higer Seondary School | Not Specified | 1 |
| Akt Matric Higher Secondary School | Foreign | 1 |
| Al-Hai Mahavidhyalaya | Not Specified | 1 |
| Al-Quds University | Foreign | 1 |
| Al-Quds University (Bard College) | Not Specified | 1 |
| Aliah University | Foreign | 2 |
| All India Jat Heros Memorial Collage | Not Specified | 1 |
| Allahabad University India | Not Specified | 1 |
| Allahabad University, India | Not Specified | 1 |
| Alliance Medical Colege | Not Specified | 1 |
| Alphacrest Academy | Not Specified | 1 |
| Ama Computer College - Dasmariñas | Private | 1 |
| Ama Computer College - Davao | Not Specified | 1 |
| Ama Computer College - East Rizal | Not Specified | 3 |
| Ama Computer College - Sta. Mesa | Private | 1 |
| Ama Computer College - Sta.Cruz | Private | 1 |
| Ama Computer College - Zamboanga City | Private | 1 |
| Ama Computer University | Private | 2 |
| Amando Cope College | Private | 1 |
| Ambrose Alli University | Foreign | 3 |
| Ambrose Alli University Ekpoma | Not Specified | 1 |
| Ambrose Alli University, Ekpoma, Edo State, Nig... | Not Specified | 1 |
| Ambrose Alli University,Ekpoma | Not Specified | 1 |
| American University Of Nigeria | Foreign | 3 |
| American University Of Sharjah | Not Specified | 1 |
| American University, Washington Dc, Usa | Not Specified | 1 |
| Aminu Kano Teaching Hospital School Of Health | Not Specified | 1 |
| Aminu Kano Teaching Hospital School Of Health I... | Not Specified | 1 |
| Amity University | Foreign | 1 |
| Amoud University College Of Health Science | Not Specified | 1 |
| Anambra State University | Foreign | 1 |
| Anambra State University, Uli | Foreign | 1 |
| Anambra State University, Uli, Anambra State, N... | Not Specified | 1 |
| Anand Homeopathic Medical College And Research ... | Foreign | 4 |
| Anantha Lakshmi Gout Ayurvdic Collage | Not Specified | 1 |
| Ananthalaxmi Ayurvedic Medical College | Not Specified | 1 |
| Andhra University | Foreign | 4 |
| Anhui University Of Chinese Medicine | Not Specified | 1 |
| Ankara University | Not Specified | 1 |
| Annamalai University | Foreign | 2 |
| Annammal Collage Of Nursing | Foreign | 1 |
| Antonio R. Pacheco College | Not Specified | 1 |
| Apex Institute Of Management And Science | Not Specified | 1 |
| Aquinas University College Of Legazpi | Not Specified | 1 |
| Aquinas University Of Legaspi | Private | 1 |
| Araullo University | Private | 4 |
| Arizona State University | Foreign | 4 |
| Arizona State University, Usa | Foreign | 1 |
| Arizona State University- Polytechnic | Not Specified | 1 |
| Arni University | Foreign | 2 |
| Arriesgado College Foundation., Inc.,Tagum City | Private | 1 |
| Art Institute Of California-Orange County | Not Specified | 1 |
| Asbury College | Private | 4 |
| Asia Pacific College | Private | 2 |
| Asia Pacific College Of Advanced Studies | Private | 2 |
| Asia Pacific College, Makati City | Private | 2 |
| Asia Pacific International University | Private | 2 |
| Asia-Pacific International University | Private | 4 |
| Asiacareer College Foundation | Not Specified | 1 |
| Asian College Foundation | Private | 1 |
| Asian College Of Science And Technology | Private | 3 |
| Asian College Of Science And Technology - Dumag... | Private | 2 |
| Asian Development Foundation College | Private | 3 |
| Asian Institute For Distance Education | Private | 2 |
| Asian Institute Of E - Commerce | Not Specified | 1 |
| Asian Institute Of Management - City Of Makati,... | Private | 1 |
| Asian Seminary Of Christian Ministries | Private | 1 |
| Aslkhaydg | Not Specified | 1 |
| Asmara University | Private | 1 |
| Assumption | Not Specified | 1 |
| Assumption College Of Nabunturan | Private | 4 |
| Assumption Univaersity | Foreign | 1 |
| Assumption University Of Thailand | Foreign | 1 |
| Assumption University, Bangkok, Thailand | Foreign | 1 |
| Assumption University, Thailand | Foreign | 1 |
| Ateneo De Cagayan University | Private | 4 |
| Ateneo Graduate School Of Business - City Of Ma... | Private | 1 |
| Atsvs Siddha Medical College And Hospital | Not Specified | 1 |
| Attarkiah Islamiah | Not Specified | 1 |
| Augusta University | Foreign | 1 |
| Augustana College | Foreign | 1 |
| Austin Peay State University | Not Specified | 1 |
| Australian Catholic University | Foreign | 1 |
| Auxillium College,Vellore, Tamil Nadu,India | Not Specified | 1 |
| Ave Maria University | Not Specified | 1 |
| Avs Ayurveda Mahavidyalaya | Not Specified | 1 |
| Avs Mahavidyalaya | Foreign | 1 |
| Azad University (Iran) | Not Specified | 1 |
| Azad University Of Tehran Shamal | Foreign | 4 |
| Azarbaijan Taribiat Moallem University, Tabriz,... | Not Specified | 1 |
| Azusa Pacific University | Not Specified | 2 |
| B R A B University | Not Specified | 1 |
| B S College Danapur Patna | Foreign | 1 |
| B. M. Memorial Degree College | Foreign | 1 |
| B. R. Mirdha College | Foreign | 2 |
| B.L.P.College,Masaurhi | Not Specified | 1 |
| B.M. Memorial Degree Collage Kakrahi Kishunpur | Not Specified | 1 |
| B.M. Memorial Degree College | Foreign | 1 |
| B.S College Danapur Patna India | Foreign | 1 |
| Baccarra Medical Center School Of Midwifery | Private | 1 |
| Bachelor Of Nursing Science,Affiliated To Princ... | Not Specified | 1 |
| Bacolod City College | Public | 1 |
| Bago City College | Public | 1 |
| Baguio Colleges Foundation, Baguio City | Private | 2 |
| Baliuag Colleges, Baliuag, Bulacan | Private | 4 |
| Banadir University, Somalia, 2012 | Not Specified | 1 |
| Bangabasi College | Not Specified | 1 |
| Bangalore University | Not Specified | 1 |
| Bangalore University, India | Foreign | 1 |
| Bangkok Thonburi University | Not Specified | 1 |
| Bangkok University | Not Specified | 1 |
| Bannari Amman College,Tirupur,Tamil Nadu,India | Not Specified | 1 |
| Baptist Bible Seminary And Institute | Private | 2 |
| Baptist Theological College | Private | 1 |
| Bapuji Ayurvedic Medical College | Foreign | 2 |
| Baruch College | Foreign | 4 |
| Basilan State College | Public | 3 |
| Bataan Polytechnic State College, Balanga City | Public | 1 |
| Batangas State University - Alangilan | Public | 1 |
| Batangas State University - Apolinario R. Apaci... | Public | 1 |
| Bayero University, Kano | Not Specified | 1 |
| Baylor University | Foreign | 2 |
| Baylor University (Waco, Tx Usa) | Not Specified | 1 |
| Baylor University, Texas, Usa | Foreign | 3 |
| Bcnkk Thailand | Not Specified | 1 |
| Beihang University | Not Specified | 1 |
| Bellarmine Univeristy | Not Specified | 1 |
| Bellevue University | Not Specified | 1 |
| Benedicto College | Private | 1 |
| Benue State University | Foreign | 1 |
| Bethel College | Not Specified | 1 |
| Bethel University | Not Specified | 1 |
| Bharathiar University | Not Specified | 1 |
| Bharathidasan University | Foreign | 1 |
| Bharati Vidyapeeth Deemed University | Foreign | 2 |
| Bharati Vidyapeeth University | Foreign | 1 |
| Bharti Vidhyapeeth College Of Nursing | Not Specified | 1 |
| Bharti Vidhyapeeth Deemed University Collage Of... | Not Specified | 1 |
| Bhartiya Homeopathic Medical College & Hospital... | Not Specified | 1 |
| Bhartiya Homeopathic Medical College And Hospit... | Not Specified | 1 |
| Bhausaheb Mulak Ayurved Mahavidyalaya Nagpur | Not Specified | 1 |
| Bigard Memorial Seminary College | Not Specified | 1 |
| Bigard Memorial Seminary, Enugu | Not Specified | 1 |
| Bingham University | Foreign | 4 |
| Bingham University, Nigeria | Not Specified | 1 |
| Binghamton University | Foreign | 3 |
| Binghamton University, State University Of New ... | Not Specified | 1 |
| Binghamton University, Suny | Foreign | 1 |
| Biola University | Public | 2 |
| Birbhum Vivekananda Homoeopathic Medical Colleg... | Not Specified | 1 |
| Birla Institute Of Science And Technology, Duba... | Not Specified | 1 |
| Birmingham School Of Law | Not Specified | 1 |
| Bishop Heber | Not Specified | 1 |
| Bishop Heber College | Foreign | 3 |
| Bit International College - Tagbilaran | Not Specified | 1 |
| Bits Information Technollogy | Not Specified | 1 |
| Blessed Mother College | Private | 2 |
| Bohol Island State University - Tagbilaran | Public | 1 |
| Bond University | Foreign | 2 |
| Boromajonani Collegg Of Uttaradit | Not Specified | 1 |
| Boromarajonani Collage Of Nursingnopparatvajira... | Not Specified | 1 |
| Boromarajonani College Nursing Nakhon Si Thammarat | Not Specified | 1 |
| Boromarajonani College Of Nursing | Foreign | 2 |
| Boromarajonani College Of Nursing ,Suphan Buri | Not Specified | 1 |
| Boromarajonani College Of Nursing Changwat Nont... | Foreign | 1 |
| Boromarajonani College Of Nursing Khonkaen | Foreign | 1 |
| Boromarajonani College Of Nursing Sanpasithipra... | Not Specified | 1 |
| Boromarajonani College Of Nursing Suratthani | Foreign | 1 |
| Boromarajonani College Of Nursing Surin | Foreign | 2 |
| Boromarajonani College Of Nursing, Khon Kaen | Not Specified | 1 |
| Boromarajonani College Of Nursing, Knon Kaen | Not Specified | 1 |
| Boromarajonani College Of Nursing, Nakhonratcha... | Not Specified | 1 |
| Boromarajonani College Of Nursing, Ratchaburi | Not Specified | 1 |
| Boromarajonani College Of Nursing, Sappasithipr... | Not Specified | 1 |
| Boromarajonani College Of Nursing, Sappasitthip... | Not Specified | 2 |
| Boromarajonani College Of Nursing, Sappsitthipr... | Not Specified | 1 |
| Boromarajonani College Of Nursing, Saraburi | Foreign | 1 |
| Boromarajonani College Of Nursing, Suphanburi | Not Specified | 1 |
| Boromarajonani College Of Nursing,Khonkaen | Foreign | 1 |
| Boromarajonani College Of Nursing,Sappasithipra... | Not Specified | 1 |
| Boromarajonani College Of'Nurclng, Sappasithipr... | Not Specified | 1 |
| Boromrajonani College Of Nursing,Nakhon Lampang | Not Specified | 1 |
| Boromrajonani Surin Nursing College,Prince Of S... | Not Specified | 1 |
| Boromrajonani Yala, Boromrajonani Ratchaburi Nu... | Not Specified | 1 |
| Boston College | Not Specified | 1 |
| Boston College, Ma, Usa | Foreign | 3 |
| Boston University | Foreign | 4 |
| Bowen University | Foreign | 3 |
| Bowen University,Iwo.Osun State.Nigeria | Not Specified | 1 |
| Bowring And Lady Curzon Hospital | Not Specified | 1 |
| Br Mirdha Govt College - M.D.S. University, Ajamer | Not Specified | 1 |
| Brent Hospital And Colleges Incorporated | Private | 1 |
| Brigham Young University Hawaii | Foreign | 1 |
| Brigham Young University, Hawaii | Foreign | 1 |
| Brigham Young University-Idaho | Not Specified | 1 |
| Bright Career Girls Degree Collage Baba Hazara ... | Not Specified | 1 |
| Brightwood College | Not Specified | 1 |
| Brock University | Not Specified | 1 |
| Brown University | Not Specified | 1 |
| Bryan College | Not Specified | 1 |
| Bsbt College | Private | 1 |
| Bucknell University | Not Specified | 1 |
| Bukidnon State College | Public | 1 |
| Bukidnon State University - Alubijid | Not Specified | 1 |
| Bukyo University | Not Specified | 1 |
| Bulacan State University - Bustos | Public | 2 |
| Bundelkhand University, Jhansi | Foreign | 1 |
| Bundelkhand University,Jhansi | Foreign | 1 |
| Bundlekhand University Jhansi | Foreign | 1 |
| Burapha University Thailand | Not Specified | 1 |
| Bvb Matric School | Not Specified | 1 |
| C.P.U. | Private | 1 |
| Cagayan Capitol College, Cagayan De Oro | Private | 1 |
| Cagayan State University | Public | 3 |
| Cagayan State University - Aparri | Public | 1 |
| Cagayan State University - Aparri Cagayan | Public | 1 |
| Cagayan State University - Gonzaga | Public | 2 |
| Cagayan State University - Sanchez Mira | Public | 2 |
| Cal Poly Pomona | Foreign | 2 |
| Calamba Doctors College | Private | 1 |
| Calayan Educational Foundation, Inc., Lucena City | Private | 1 |
| Cali Paramedical College Foundation | Private | 1 |
| California Polytechnic State University, San Lu... | Foreign | 1 |
| California State Polytechnic Univ., Ca, Usa | Foreign | 3 |
| California State Polytechnic University, Pomona | Not Specified | 3 |
| California State University - Fullerton | Foreign | 3 |
| California State University - Northridge, Ca | Foreign | 1 |
| California State University Bakersfield | Foreign | 1 |
| California State University Dominguez Hills | Not Specified | 2 |
| California State University East Bay | Foreign | 2 |
| California State University Fresno | Foreign | 3 |
| California State University Fullerton | Foreign | 1 |
| California State University Long Beach | Foreign | 2 |
| California State University Los Angeles | Foreign | 1 |
| California State University Northridge | Foreign | 2 |
| California State University Of East Bay | Foreign | 1 |
| California State University Of Fullerton | Foreign | 1 |
| California State University Of Long Beach | Foreign | 2 |
| California State University Of Sacramento | Foreign | 1 |
| California State University Sacramento | Foreign | 1 |
| California State University San Marcos | Not Specified | 2 |
| California State University, Dominguez Hills | Not Specified | 1 |
| California State University, East Bay | Foreign | 1 |
| California State University, Fresno | Foreign | 1 |
| California State University, Fullerton | Foreign | 1 |
| California State University, Hayward | Foreign | 2 |
| California State University, Los Angeles | Foreign | 2 |
| California State University, Northridge | Foreign | 1 |
| California State University, Sacramento | Foreign | 3 |
| California State University, San Bernardino | Not Specified | 1 |
| California State University- San Marcos | Not Specified | 1 |
| Camiguin Polytechnic State College | Public | 3 |
| Canadian University College | Not Specified | 1 |
| Canberra University | Foreign | 1 |
| Canossa College-San Pablo, Laguna | Private | 2 |
| Cap College Foundation | Private | 1 |
| Capiz State University - Main | Public | 1 |
| Capiz State University - Pontevedra | Public | 2 |
| Caraga State University | Public | 1 |
| Caritas | Not Specified | 1 |
| Carleton University | Foreign | 1 |
| Carnegie Mellon University | Not Specified | 1 |
| Casa Di Mir Matric School | Not Specified | 1 |
| Catholic University Institute Of Buea | Not Specified | 1 |
| Catholic University Of America | Not Specified | 1 |
| Catholic University Of Buea | Foreign | 1 |
| Cavite State University - Carmona | Public | 1 |
| Cebu Aeronautical Technical School | Private | 1 |
| Cebu City Medical Center- College Of Nursing | Not Specified | 2 |
| Cebu Doctor&#039;S University | Private | 1 |
| Cebu Doctor's University | Private | 2 |
| Cebu Institute Of Medicine - Cebu City, Cebu | Private | 1 |
| Cebu Sacred Heart College | Private | 1 |
| Cebu Sacred Heart College, Talisay, Cebu | Private | 2 |
| Cebu State College Of Science And Technology-Ma... | Public | 4 |
| Central Academy Vikas | Foreign | 1 |
| Central Bicol State University Of Agriculture -... | Public | 2 |
| Central Luzon College Of Technology - Olongapo | Private | 3 |
| Central Methodist University | Private | 1 |
| Central University | Foreign | 1 |
| Centro Escolar University (Gil Puyat Makati City) | Not Specified | 1 |
| Centro Escolar University - Gil Puyat, Makati City | Not Specified | 1 |
| Centro Escolar University - Makati City | Private | 2 |
| Centro Escolar University - Makati Gil Puyat | Not Specified | 1 |
| Centro Escolar University Gil Puyat Makati City... | Not Specified | 1 |
| Centro Escolar University Makati City | Private | 2 |
| Centro Escolar University, Makati | Private | 2 |
| Centro Escolar University, Makati City | Private | 1 |
| Centro Escolar University, Makati Gil Puyat Ave... | Not Specified | 1 |
| Centro Escolar University- Makati | Private | 3 |
| Centro Escolar University- Makati, Gil Puyat | Not Specified | 1 |
| Centro Escular University-Makati | Private | 1 |
| Chaing Mai University | Foreign | 2 |
| Chaing Mai University-Thailand | Foreign | 1 |
| Chaingmai University | Not Specified | 1 |
| Chaingmai University, Thailand | Foreign | 1 |
| Chaitanya Medical Foundation College Of Physiot... | Not Specified | 1 |
| Chandrakasem Rajabhat University | Not Specified | 1 |
| Chang Jung Christian University | Not Specified | 1 |
| Chang-Gung Coll. Of Medicine And Tech., Taiwan | Foreign | 1 |
| Chaudhary Charan Singh University | Foreign | 1 |
| Cheran Matriculation Higher Secondary School | Not Specified | 1 |
| Chhadamilal Chouksey Homoeopathic Medical College | Not Specified | 1 |
| Chhatrapati Shahu Ji Maharaj University | Foreign | 1 |
| Chia-Nan Pharmacy College, Taiwan | Foreign | 2 |
| Chiang Kai Shek College, Tondo, Manila | Private | 2 |
| Chiang Mai University,Thailand | Foreign | 1 |
| Chico State University | Foreign | 1 |
| China Medical College | Foreign | 3 |
| China Medical University, Taiwan | Foreign | 1 |
| China Medicine University | Not Specified | 1 |
| Christ Church P.G Colllege Kanpur | Not Specified | 1 |
| Christ The King College - Gingoog City | Private | 1 |
| Christ The King Mission Seminary, Q.C. | Private | 2 |
| Christhu Jyothi Matriculation Higher Secondary ... | Not Specified | 1 |
| Christian Colleges Of Southeast Asia | Private | 2 |
| Christian Medical College | Not Specified | 1 |
| Christian Medical College, Vellore | Foreign | 1 |
| Christian Medical College,Vellore | Foreign | 1 |
| Christian Univeristy | Not Specified | 1 |
| Christian University Of Thailand/Bachelor Nursi... | Not Specified | 1 |
| Christopher Newport University | Not Specified | 1 |
| Chulalongkhon Bangkok | Not Specified | 1 |
| Chulalongkorn | Not Specified | 1 |
| Chulalongkorn University,Thailand | Foreign | 1 |
| Chung Hwa University Of Medical Technology | Not Specified | 2 |
| Chung Shan Medical College | Foreign | 1 |
| Chung Shan Medical University | Not Specified | 1 |
| Chungshan Medical University, Taiwan | Foreign | 1 |
| Chungtai Institute Of Health Sciences And Techn... | Foreign | 1 |
| Cicosat Colleges | Private | 2 |
| City College Of Manila | Public | 2 |
| City University, New York | Foreign | 1 |
| Colegio De San Francisco Javier | Private | 1 |
| Colegio De San Gabriel Arcangel | Private | 1 |
| Colegio De San Lorenzo - Q.C. | Private | 3 |
| Colegio De San Lorenzo Ruiz De Manila | Private | 1 |
| Colegio De San Sebastian | Private | 1 |
| Colegio De Santa Monica - Manila | Private | 3 |
| Colegio De Sta. Catalina De Alejandria | Private | 3 |
| Colegio De Sta. Lourdes Of Leyte Foundation, Inc | Private | 1 |
| Colegio San Agustin Bacolod | Private | 1 |
| Colgate University | Not Specified | 1 |
| Colleage Of Nursing Borommarajachonnee | Not Specified | 1 |
| College Of Allied Medical Sciences | Private | 1 |
| College Of Basic Science & Humanities | Private | 1 |
| College Of Immaculate Conception, Cabanatuan | Private | 1 |
| College Of Medicine University Of Lagos | Not Specified | 1 |
| College Of Medicine/King Abdulaziz University/J... | Not Specified | 1 |
| College Of Mount Saint Vincent | Not Specified | 1 |
| College Of Natural Sciences | Not Specified | 1 |
| College Of Nursing Dhamtari Christian Hospital | Foreign | 1 |
| College Of Nursing, D.C.H, Dhamtari | Foreign | 1 |
| College Of Our Lady Of Mt. Carmel | Not Specified | 1 |
| College Of Staten Island, The City University O... | Not Specified | 1 |
| College Of Technological Sciences - Cebu | Not Specified | 2 |
| College Of William And Mary | Not Specified | 2 |
| Columbia University/University Of Virginia | Not Specified | 1 |
| Computer Communication Development Institute | Not Specified | 1 |
| Computer Technologies Institute Of Zamboanga City | Private | 1 |
| Concordia College, Paco, Manila | Private | 4 |
| Concordia University Irvine | Foreign | 1 |
| Congress College - Agoo, La Union | Private | 1 |
| Connecticut College - Usa | Foreign | 1 |
| Consolata School Of Nursing | Foreign | 3 |
| Consolatrix College Of Toledo City | Private | 1 |
| Convent Of Gagan Bharati Mohan Garden New Delhi | Not Specified | 1 |
| Cornell University | Foreign | 3 |
| Cotabato City State Polytechnic College | Public | 1 |
| Cotabato Foundation College Of Science And Tech... | Private | 1 |
| Council Of Electro Homoeopathic System Of Medicine | Not Specified | 1 |
| County College Of Morris | Not Specified | 1 |
| Covenant University, Ota. Ogun State. Nigeria. | Not Specified | 2 |
| Credit Bank System | Not Specified | 1 |
| Creighton University | Foreign | 3 |
| Crist College ,Eringalakuda,Thrissur,Kerala,India | Not Specified | 1 |
| Crist College, Eringalakuda.Thrissur ,Kerala,India | Not Specified | 1 |
| Csi College Of Nursing | Foreign | 1 |
| Csu Stanislaus | Not Specified | 1 |
| Ctu- Cebu City Medical Center-College Of Nursing | Not Specified | 1 |
| Cuny Brooklyn College | Not Specified | 1 |
| Cuny Hunter College | Not Specified | 1 |
| Cuny Medgar Evers College | Foreign | 1 |
| Cuny Queens College | Not Specified | 1 |
| Cure Med Inst Of Electropathy & Hospital | Not Specified | 1 |
| D.D.U Gorakhpur University ,Gorakhpur Up | Not Specified | 1 |
| D.R.Nayapali College | Foreign | 1 |
| D.Z.Patel English Medium School | Not Specified | 1 |
| Daejeon University | Not Specified | 1 |
| Dagupan Colleges Foundation | Private | 2 |
| Dalhousie Universty | Foreign | 1 |
| Dallas Baptist University, Dallas Texas | Not Specified | 1 |
| Data Center College Of The Philippines Of Laoag... | Private | 1 |
| Dav College | Not Specified | 1 |
| Dav Pub School | Foreign | 1 |
| Davao Del Norte State College | Public | 1 |
| Davao Oriental State College Of Science & Tech. | Public | 2 |
| Davidson College | Not Specified | 1 |
| De La Salle - Canlubang | Private | 1 |
| De La Salle - Canlubang (Leandro V. Locsin) | Private | 2 |
| De La Salle Lipa | Private | 1 |
| De Montfort University | Foreign | 2 |
| De Ocampo Memorial College, Sta. Mesa, Manila | Private | 4 |
| Deakin University | Foreign | 4 |
| Dee Hwa Liong College Foundation | Foreign | 1 |
| Deen Dayal Upadhyaya Gorakhpur University | Not Specified | 1 |
| Deen Dayal Upadhyaya Gorakhpur University, Gora... | Foreign | 1 |
| Delhi Public School Nr Sewar | Not Specified | 1 |
| Devry University | Not Specified | 1 |
| Devry University, Phoenix Arizona | Not Specified | 1 |
| Dhamtari Christian Hospital Dhamtari | Not Specified | 1 |
| Dharani Matric Hr Sec School | Not Specified | 1 |
| Dharani Matric.Hr.Sec.School | Not Specified | 1 |
| Dharma Ayurveda Medical College And Hospital | Not Specified | 1 |
| Dipolog Medical Center | Private | 4 |
| District Homeopathic Medical College Ratlam | Not Specified | 1 |
| Divine Word College Of Bangued | Private | 4 |
| Divine Word College Of San Jose | Private | 3 |
| Divine Word College Of Urdaneta | Private | 1 |
| Divine Word College Of Vigan | Private | 2 |
| Divine Word College-Laoag City | Private | 1 |
| Divine Word Mission Seminary | Private | 2 |
| Divine Word Seminary | Private | 1 |
| Divine Word University | Not Specified | 1 |
| Divine Word University, Tacloban City | Private | 2 |
| Dmma College Of Southern Philippines | Private | 3 |
| Dmmc Institute Of Health Sciences | Private | 3 |
| Dmsf | Not Specified | 1 |
| Dolhi Model Public School | Foreign | 1 |
| Dolhi Public School | Foreign | 1 |
| Dominican College - Sta. Rosa | Private | 2 |
| Dominican University Of California | Not Specified | 1 |
| Don Honorio Ventura Technological State Univers... | Public | 1 |
| Don Mariano Marcos Memorial State University - ... | Public | 1 |
| Dona Remedios T. Romualdez Medical Foundation-T... | Not Specified | 1 |
| Dong-A University, Korea | Foreign | 1 |
| Doshisha University | Not Specified | 1 |
| Dowling College | Not Specified | 1 |
| Dr Dy Patil University | Not Specified | 1 |
| Dr Mgr Medical University | Foreign | 3 |
| Dr Nayapali College | Foreign | 2 |
| Dr Ram Manohar Lohia Avadh University | Foreign | 1 |
| Dr Ram Manohar Lohia Avadh University Faizabad ... | Foreign | 1 |
| Dr Ram Manohar Lohia Avadh University, Faizabad | Foreign | 1 |
| Dr. Baba Saheb Ambedkar Technological University | Not Specified | 2 |
| Dr. G G H Medical College | Not Specified | 1 |
| Dr. Gloria D. Lacson Foundation Colleges - Nuev... | Private | 2 |
| Dr. M G R Medical University | Foreign | 1 |
| Dr. Ntr University Of Health Science | Foreign | 1 |
| Dr. Ntr University Of Health Science : A.P. Vij... | Not Specified | 1 |
| Dr. Ntr University Of Health Sciences | Foreign | 1 |
| Dr. Ntr University Of Health Sciences : A.P. | Not Specified | 1 |
| Dr. Ntr University Of Health Sciences, Vijayawa... | Not Specified | 1 |
| Dr. P. Ocampo College, Inc., Cotabato City | Private | 3 |
| Dr. Ram Manohar Lohiya Degree College | Foreign | 1 |
| Dr. Shankar Dayal Sharma College Of Nursing , B... | Foreign | 1 |
| Dr. Shankar Dayal Sharma College Of Nursing, Bh... | Foreign | 1 |
| Dr. V. H. Dave Homeopathic Medical College | Not Specified | 1 |
| Dr. V. Orestes Romualdez Educational Foundation | Private | 1 |
| Dr. V.H.Dave.Hmc | Not Specified | 1 |
| Dr. Yangas Francisco Balagtas, Bulacan | Private | 3 |
| Dr.Babasaheb Ambedkar,Marathwasa University Aur... | Not Specified | 1 |
| Dr.D.Y.Patil Institute Of Optometry And Visual ... | Not Specified | 1 |
| Dr.G.V.N.School Of Nursing | Foreign | 1 |
| Dr.M.G.R. College Of Nursing | Not Specified | 1 |
| Dr.M.G.R. Educational And Research Institute Un... | Not Specified | 1 |
| Dr.Mahalingam Institute Of Paramedical Science ... | Not Specified | 1 |
| Dr.Mgr University | Not Specified | 1 |
| Dr.Ntr University Of Health Science | Foreign | 3 |
| Dr.Ntr University-Vijayavada,Ap,India | Not Specified | 1 |
| Dr.Ram Manohar Lohia Avadh University Faizabad | Foreign | 1 |
| Dr.Ram Manohar Lohia Avadh University Faizabad Up | Foreign | 1 |
| Dr> Babasaaheb Ambedkar, Marathwada University,... | Not Specified | 1 |
| Drew University | Foreign | 2 |
| Drexel University | Foreign | 4 |
| Drexel University (Philadelphia,Pa,Usa) | Not Specified | 1 |
| Drury University | Not Specified | 1 |
| East Central University | Not Specified | 1 |
| Eastern Asia University | Foreign | 1 |
| Eastern Michigan University, Usa | Foreign | 1 |
| Eastern Samar State University - Can - Avid | Public | 1 |
| Eastern Visayas State University | Public | 4 |
| Ebenezer Mat.Hr.Sec School | Not Specified | 1 |
| Ebenezer,Mat,Hr,Sec School | Not Specified | 1 |
| Ebonyi State University Abakaliki Ebonyi | Foreign | 1 |
| Ecumenical Christian College | Private | 4 |
| Edith Cowan University | Foreign | 1 |
| Edwardes College Peshawar | Foreign | 2 |
| Einu Shamsi | Not Specified | 1 |
| Ekiti State University, Ado Ekiti | Not Specified | 1 |
| Elisa R. Ochoa Memorial Northern Mindanao Schoo... | Private | 3 |
| Embry-Riddle Aeronautical University | Not Specified | 2 |
| Emilio Aguinaldo College - Cavite | Not Specified | 1 |
| Emilio Aguinaldo College - Dasmarinas, Cavite | Not Specified | 1 |
| Emilio Aguinaldo College Cavite | Not Specified | 1 |
| Emilio Aguinaldo College Dasmariñas, Cavite | Not Specified | 1 |
| Emilio Aguinaldo College-Cavite | Not Specified | 1 |
| Emilio Aguinaldo College-Dasmariñas, Cavite | Not Specified | 1 |
| Entrepreneurs School Of Asia | Private | 1 |
| Enugu State University Of Sc. And Tech | Not Specified | 1 |
| Escuela De Nuestra Sra. De La Salette | Private | 3 |
| Ethiraj | Not Specified | 1 |
| Ethiraj College | Not Specified | 4 |
| Eulogio Amang Rodriguez Institute Of Science An... | Public | 1 |
| Excelsior College | Foreign | 1 |
| Expert'S International College | Not Specified | 1 |
| Faculty Of Nursing, Mahidol University | Foreign | 1 |
| Faculty Of Optometry, Rangsit University | Not Specified | 1 |
| Faculty Of Pharmacy Alexandria University | Not Specified | 1 |
| Faculty Of Pharmacy Mahidol University Thailand | Not Specified | 1 |
| Faculty Of Science, King Mongkut'S Institute Of... | Not Specified | 1 |
| Family Clinic Inc. Colleges, Manila | Private | 4 |
| Far Eastern College - Silang | Private | 3 |
| Far Eastern University - Dr. Nicanor Reyes Medi... | Not Specified | 1 |
| Far Eastern University - Makati | Private | 1 |
| Far Eastern University Dr Nicanor Reyes Medical... | Not Specified | 1 |
| Far Eastern University Nicanor Reyes Medical Fo... | Not Specified | 1 |
| Far Eastern University, Morayta Manila | Not Specified | 1 |
| Far Eastern University, West Sampaloc, Manila | Not Specified | 1 |
| Far Eastern University- Dr. Nicanor Medical Fou... | Not Specified | 1 |
| Far Eastern University- Dr. Nicanor Reyes Medic... | Not Specified | 2 |
| Far Eastern University-Dr. Nicanor Reyes Medica... | Not Specified | 1 |
| Far Eastern University-Manila | Not Specified | 1 |
| Father Saturnino Urios University | Private | 1 |
| Fatih University | Private | 1 |
| Fatima Medical Science Foundation Inc. - Lagro ... | Private | 1 |
| Fatima Medical Science Foundation Inc.-Valenzuela | Private | 3 |
| Fatima University (Marulas, Valenzuela) | Private | 2 |
| Feati University | Private | 2 |
| Febias College Of Bible | Private | 2 |
| Federal Polytechnic Kogi State Nigeria | Not Specified | 1 |
| Federal Polytechnic Mubi | Not Specified | 2 |
| Federal Polytechnic Mubi, Adamawa State | Not Specified | 1 |
| Federal Polytechnic,Bida | Not Specified | 2 |
| Federal University Of Agriculture, Abeokuta | Foreign | 1 |
| Federal University Of Technology, Akure. | Foreign | 1 |
| Federal University Of Technology,Akure | Foreign | 1 |
| Federation University Australia | Not Specified | 1 |
| Felician College | Not Specified | 1 |
| Felipe Verallo College, Cebu | Private | 2 |
| Feu - Institute Of Nursing Sampaloc, City Of Ma... | Not Specified | 1 |
| Filamer Christian College, Roxas City | Private | 4 |
| Filamer Christian University Roxas City, Capiz | Not Specified | 1 |
| First City Providential College | Private | 2 |
| Fitchburg State University | Foreign | 1 |
| Fl Vargas College - Abulug | Not Specified | 3 |
| Flight School International | Private | 1 |
| Flinders University | Not Specified | 1 |
| Fooyin University | Not Specified | 1 |
| Fordham College, Bronx, New York, Usa | Foreign | 3 |
| Fordham University | Foreign | 2 |
| Foundation University, Dumaguete City | Private | 3 |
| Francis Marion University | Not Specified | 1 |
| Franklin & Marshall College | Foreign | 3 |
| Freed Hardeman University | Foreign | 1 |
| Frostburg State University | Foreign | 1 |
| Fu Jen University | Foreign | 1 |
| Fujen University | Foreign | 1 |
| G Prasad Shukla Ic Gaura Chauki Gonda | Foreign | 1 |
| G.K College | Foreign | 1 |
| G.T.P. College. Nandurbar. Mh, India. | Not Specified | 1 |
| Gandhi S K Coll Bera Mathura | Foreign | 1 |
| Gauhati University | Foreign | 1 |
| Gayathri Devi College Of Nursing | Not Specified | 1 |
| Gaziantep University | Foreign | 1 |
| Geetanjali College Of Nurshing | Foreign | 1 |
| Geetanjali College Of Nursing | Foreign | 2 |
| Genius Collage Of Nursing Bhilwara (Rajasthan) | Not Specified | 1 |
| Gensantos Foundation College | Private | 3 |
| George Dewey Medical College | Private | 2 |
| George Mason University | Not Specified | 2 |
| George Mason University, Virginia, Usa | Foreign | 2 |
| Georgetown University | Foreign | 1 |
| Georgia Institute Of Technology | Not Specified | 1 |
| Georgia Institute Of Technology/ Georgia Tech | Not Specified | 1 |
| Georgia Southern University | Foreign | 1 |
| Georgia State University | Not Specified | 2 |
| Georgian Court University | Not Specified | 1 |
| Giffard Memorial Hospital Of S.D.A | Not Specified | 1 |
| Gingoog City Junior College | Private | 1 |
| Girne American University | Not Specified | 2 |
| Glasgow University United Kingdom | Not Specified | 1 |
| Glyndwr University | Not Specified | 1 |
| Goa University | Not Specified | 1 |
| Goenka College Of Pharmacy Rajasthan University... | Not Specified | 1 |
| Goethals Memorial | Not Specified | 1 |
| Gonzaga University | Not Specified | 3 |
| Good Samaritan College, Cabanatuan City | Private | 1 |
| Goverment Degree College Sumbal | Foreign | 1 |
| Governement Yoga And Naturopathic Medical Colle... | Foreign | 1 |
| Government Ayurveda Medical College, Mysore | Not Specified | 1 |
| Government College Of Physiotherapy | Not Specified | 1 |
| Government Degree College(Boys) Anantnag | Not Specified | 1 |
| Government Holkar Science Collage Indore Mp | Foreign | 1 |
| Government School | Foreign | 4 |
| Government Science College, Bengaluru | Not Specified | 1 |
| Government Science College; Bengaluru | Not Specified | 1 |
| Government Siddha Medical College | Not Specified | 1 |
| Govt Ayurvedic College Balangir | Foreign | 1 |
| Govt Hr.Sec School Kullanur Dharmapuri | Not Specified | 1 |
| Govt Polytechnic College Rohroo, Shimla | Not Specified | 1 |
| Govt. Auto. Ashtang Ayurvedic College,Indore | Not Specified | 1 |
| Govt. J.D.B. Girls College | Foreign | 1 |
| Govt. Mahavidyalaya, Bilaspur | Not Specified | 2 |
| Govt. Pg. College, Jhalawar | Not Specified | 1 |
| Govt.Ayurvedic College,Balangir | Foreign | 1 |
| Graceland University | Foreign | 1 |
| Grand Canyon University | Not Specified | 1 |
| Great Plebian College | Private | 4 |
| Green Park Matric Higher Secondary School | Not Specified | 1 |
| Greenwood Higher Secondary School | Foreign | 1 |
| Guagua National Colleges | Private | 1 |
| Gujarat Technological University | Not Specified | 1 |
| Guru Ghashidas University | Foreign | 1 |
| Guru Ghasidas Central University | Not Specified | 1 |
| Guru Govind Singh Indraprastha University Delhi | Not Specified | 1 |
| Gyan Bharti | Not Specified | 1 |
| H.N.G.University,Patan, Gujarat,India | Not Specified | 1 |
| Hallym University | Foreign | 3 |
| Han Young University, Seoul, Korea | Foreign | 1 |
| Happy Child College | Not Specified | 1 |
| Harbin Medical University | Not Specified | 1 |
| Hardam Furigay Colleges Foundation | Private | 1 |
| Haria High School | Foreign | 1 |
| Harvard University, Boston, Mas. | Foreign | 2 |
| Hawaii Pacific University | Foreign | 2 |
| Hemchandracharya North Gujarat University | Not Specified | 2 |
| Henan University Of Tcm In China | Not Specified | 1 |
| High School Piyaji | Not Specified | 1 |
| Himachal Pradesh Technical Board India | Not Specified | 1 |
| Himalayan University | Foreign | 1 |
| Hiroshima University | Foreign | 1 |
| Hitotsubashi University | Not Specified | 1 |
| Hofstra University, New York | Foreign | 1 |
| Holy Child Colleges Of Butuan City | Private | 2 |
| Holy Child School Of Davao | Private | 1 |
| Holy Cross College | Not Specified | 2 |
| Holy Cross College Of Calinan | Private | 1 |
| Holy Cross School Tadong Sikkim | Not Specified | 1 |
| Holy Cross of Davao College | Private | 1 |
| Holy Rosary Minor Seminary | Private | 4 |
| Homoeopathic Medical College & Hospital | Not Specified | 1 |
| Hong Kong University Of Science And Technology | Not Specified | 1 |
| Hua Siong College Of Iloilo | Private | 1 |
| Huachien Chalermprakiet University, Thailand | Foreign | 3 |
| Huachiew Chalermprakeit University | Foreign | 1 |
| Huachiew Chalermprakiat University | Foreign | 1 |
| Huachiew Chalermprakiet University Of Thailand | Foreign | 1 |
| Huachiewchalermprakiet University | Not Specified | 1 |
| Huazhong Agricultural University | Not Specified | 1 |
| Hubei University Of Chinese Medicine | Not Specified | 1 |
| Hungkuang University | Not Specified | 1 |
| Hungkuang University (Taiwan) | Foreign | 1 |
| Hunter College | Foreign | 1 |
| Hunter College, Usa | Foreign | 2 |
| I-Shou University | Not Specified | 1 |
| ICCT Colleges | Private | 1 |
| Icct Colleges | Private | 2 |
| Ieti College Of Science And Technology - Marikina | Private | 1 |
| Ifugao State University - Main | Public | 4 |
| Ilocos Sur Polytechnic State College | Public | 3 |
| Ilocos Sur Polytechnic State College - Santiago | Public | 2 |
| Iloilo Doctors' College Of Medicine - Iloilo Ci... | Private | 1 |
| Immaculate Concepcion College-Albay | Private | 2 |
| Immaculate Conception Archdiocesan School | Private | 1 |
| Immaculate Conception College, Ozamis City | Private | 2 |
| Imo State University | Foreign | 2 |
| Imo State University Owerri | Not Specified | 1 |
| Imperial College London | Not Specified | 1 |
| Imphal College | Foreign | 3 |
| Indiana University | Foreign | 1 |
| Indiana University - Bloomington, Indiana, U.S.A. | Foreign | 1 |
| Indira Gandhi National Open University | Foreign | 2 |
| Indonesia Adventist University | Not Specified | 1 |
| Indonesian Adventist University | Not Specified | 4 |
| Informatics College - Eastwood | Private | 2 |
| Information And Communications Technology Academy | Private | 3 |
| Inha University/Incheon City | Not Specified | 1 |
| Inha University/South Korea | Not Specified | 1 |
| Institute Of Pharmacetuicals Education And Rese... | Not Specified | 1 |
| Institute Of Pharmaceutical Education And Rease... | Not Specified | 1 |
| Institute Of Pharmaceutical Education And Research | Not Specified | 1 |
| Institute Of Technology Ayothaya | Not Specified | 2 |
| Integral University | Foreign | 1 |
| International American University | Not Specified | 2 |
| International American University College Of Me... | Foreign | 1 |
| International Christian University Tokyo Japan | Not Specified | 1 |
| International College Of Hotel Management | Not Specified | 1 |
| International College, Nagaur | Foreign | 1 |
| International Quantum University | Not Specified | 1 |
| International School Of Asia And The Pacific - ... | Private | 2 |
| International University Of Health Sciences | Not Specified | 1 |
| Iona College | Not Specified | 1 |
| Ipsp/Eps | Private | 3 |
| Isabela State University - Main | Public | 3 |
| Isabela State University - Palanan | Public | 1 |
| Ishrm School System | Foreign | 1 |
| Islamic Azad University | Foreign | 4 |
| Islamic Azad University Of North, Tehran | Not Specified | 1 |
| Islamic Azad University Science And Research Br... | Not Specified | 1 |
| Islamic Azad University Shahr-E Ray Branch | Not Specified | 1 |
| Istituto Di Istruzione "Marco Fanno" | Not Specified | 1 |
| J.H.Tarapore School, Jamshedpur | Not Specified | 1 |
| J.K.K Nattraja College Of Pharmacy | Not Specified | 1 |
| J.P. Sioson Colleges | Private | 2 |
| J.P. Sioson General Hospital And Colleges | Private | 4 |
| Jackson State University | Foreign | 1 |
| Jaffna University, Sri Lanka | Not Specified | 1 |
| Jahghjf | Not Specified | 1 |
| Jaipur Hospital College Of Nursing | Not Specified | 1 |
| James Madison University | Foreign | 2 |
| Jamiatu Marawi Al - Islamia Foundation | Private | 2 |
| Janki Devi Bajaj College Of Science Wardha | Not Specified | 1 |
| Janta Degree College | Foreign | 2 |
| Jawaharlal Institude Of Postgraduate Medical Ed... | Foreign | 1 |
| Jaya College Of Arts And Science | Foreign | 3 |
| Jecrc Jaipur | Not Specified | 1 |
| Jenderal Soedirman University | Not Specified | 1 |
| Jesus The Loving Shepherd Christian College | Private | 1 |
| Jinnah Post Graduate Medical Centre Karachi (Pa... | Not Specified | 1 |
| Jipmer | Not Specified | 2 |
| Jodhpur National University | Not Specified | 1 |
| Jodhupur National University | Foreign | 1 |
| Jodhupur Natonal University | Foreign | 1 |
| John B. Lacson Colleges Foundation - Bacolod | Private | 3 |
| Johns Hopkins University | Foreign | 4 |
| Joint Degree English Program | Private | 1 |
| Jordan University Of Science And Technology | Public | 2 |
| Jose C. Feliciano College | Private | 2 |
| Jose Maria College | Private | 2 |
| Jose Rizal Memorial State University - Dipolog | Not Specified | 1 |
| Josefina H. Cerilles State College - Pagadian | Public | 2 |
| Jupiter College | Not Specified | 2 |
| Justice Basheer Ahmed Sayeed College For Women | Not Specified | 1 |
| K.D Dental College | Not Specified | 1 |
| K.L.E'S, S.Nijalingappa Society | Not Specified | 1 |
| K.M.C.H. College Of Nursing | Foreign | 1 |
| Kaduna State University | Foreign | 2 |
| Kainan University, Taiwan | Not Specified | 1 |
| Kakatiya University | Foreign | 2 |
| Kalasalingam University | Not Specified | 1 |
| Kalinga - Apayao State College - Main | Public | 1 |
| Kalinga Apayao State College, Kalinga Province | Public | 2 |
| Kalinga University | Foreign | 1 |
| Kalpataru College Of Bsc. Nursing | Not Specified | 1 |
| Kalptaru B.Sc Nursing College Udaipur | Not Specified | 1 |
| Kamakhya Pemton College | Foreign | 2 |
| Kamakhya Pemton College,Hiyangthang | Not Specified | 1 |
| Kamakhyanagar College , Kamakhyanagar | Not Specified | 1 |
| Kamineni Institute Of Dental Sciences | Not Specified | 1 |
| Kamphaeng Phet Rajabhat University | Not Specified | 2 |
| Kanjanapisek Wittayalai Nakornphathom | Not Specified | 1 |
| Kanpur University | Not Specified | 1 |
| Kaohsiung Medical University | Foreign | 1 |
| Karnataka College Of Nursing | Not Specified | 1 |
| Karnataka College Of Nursing , Bangalore | Not Specified | 1 |
| Karnataka State Pharmacy Council | Not Specified | 1 |
| Karunya University | Not Specified | 1 |
| Kasetsant University, Thailand | Foreign | 1 |
| Kasetsart University Bangkok 10900,Thailand | Not Specified | 1 |
| Kasetsart University, Thailand | Foreign | 1 |
| Kasetsert University | Foreign | 1 |
| Kcmt Bareilly / Mahatama Jyotiba Phule Rohilkha... | Not Specified | 1 |
| Kcon, Bangalore | Not Specified | 1 |
| Kd Dental College | Not Specified | 1 |
| Keins Matric.Hr.Sec.School | Not Specified | 1 |
| Keio University | Not Specified | 1 |
| Kempegowda College Of Nursing | Not Specified | 1 |
| Kharagpur Homoeopathic Medical College And Hosp... | Not Specified | 1 |
| Khonkaen University | Foreign | 1 |
| Khonkean University | Foreign | 1 |
| Khulna University | Not Specified | 2 |
| King Mongkut'S Institute Of Teachnology Ladkrabang | Foreign | 1 |
| King Mongkut'S Institute Of Technology Ladkrabang | Foreign | 1 |
| King Saud University | Not Specified | 1 |
| King Saud University, Saudi Arabia | Foreign | 2 |
| King'S College University Of London | Not Specified | 1 |
| Kitasato University,Japan | Not Specified | 1 |
| Kmitl | Not Specified | 1 |
| Kmitnb | Not Specified | 1 |
| Kobe University | Not Specified | 1 |
| Kochi University | Foreign | 1 |
| Komazawa University | Not Specified | 1 |
| Komazawa Unniversity | Not Specified | 1 |
| Konkuk University | Not Specified | 1 |
| Korea University | Foreign | 1 |
| Korean University | Foreign | 1 |
| Kovai Medical Center And Hospital Limited | Foreign | 1 |
| Krishna Science School | Not Specified | 1 |
| Kristu Jayanti College | Not Specified | 2 |
| Kurushetra University | Not Specified | 1 |
| Kv Zurich, Business School, Zurich | Foreign | 1 |
| Kwame Nkrumah University Of Science And Technology | Foreign | 1 |
| Kwansei Gakuin University | Not Specified | 1 |
| Kwansei University | Not Specified | 1 |
| Kwanseigakuin University | Not Specified | 1 |
| La Consolacion College - Bacolod | Private | 2 |
| La Consolacion College - Pasig | Private | 1 |
| La Consolacion College Manila | Private | 1 |
| La Salle Affiliate College, Roxas City | Private | 1 |
| La Salle University- Ozamiz City | Not Specified | 1 |
| La Sierra University | Foreign | 1 |
| La Union College Of Nursing, Arts And Sciences | Private | 4 |
| Ladoke Akintola University Of Technology | Foreign | 1 |
| Ladoke Akintola University Of Technology Ogbomoso | Foreign | 1 |
| Ladoke Akintola University Of Technology Ogbomo... | Foreign | 1 |
| Ladoke Akintola University Of Technology, Ogbomoso | Foreign | 3 |
| Ladoke Akintola University Of Technology, Ogbom... | Foreign | 1 |
| Laguna Northwestern College | Private | 1 |
| Laguna State Polytechnic University - Los Baños... | Public | 1 |
| Laguna State Polytechnic University - San Pablo... | Public | 4 |
| Lanao School Of Science And Technology | Private | 2 |
| Larmen De Guia Memorial College | Private | 1 |
| Las Pinas College, Las Pinas, Metro Manila | Private | 3 |
| Las Piñas College | Private | 2 |
| Laurentian University, Ontario, Canada | Not Specified | 1 |
| Lead City University | Foreign | 1 |
| Lebanese American University | Not Specified | 1 |
| Lehigh University | Not Specified | 1 |
| Lehman College City University Of New York | Not Specified | 1 |
| Leyte State University | Public | 2 |
| Liberty College Of Nursing, Mansarovar | Foreign | 1 |
| Liberty University, Usa | Foreign | 1 |
| Little Flower College,Guruvayoor,Kerala,India | Not Specified | 1 |
| Liverpool Hope University | Not Specified | 1 |
| Loma Linda University | Foreign | 1 |
| Loma Linda University, Riverside, Ca | Foreign | 2 |
| London Metropolitan University | Foreign | 3 |
| Loras College | Not Specified | 1 |
| Louisiana State University | Not Specified | 1 |
| Loyala College | Not Specified | 1 |
| Loyola | Not Specified | 1 |
| Loyola College | Not Specified | 2 |
| Loyola College In Maryland, Baltimore, U.S.A. | Foreign | 1 |
| Loyola College(Autonomous) | Not Specified | 1 |
| Loyola Marymount University | Foreign | 4 |
| Loyola Marymount University, Los Angeles, Calif... | Foreign | 1 |
| Loyola University Of Maryland | Not Specified | 1 |
| Loyola University, Chicago, U.S.A. | Foreign | 4 |
| Luna Colleges | Private | 3 |
| Luna Goco | Private | 1 |
| Luther Rice University / Catholic University Of... | Not Specified | 1 |
| Lvtg College Of Physiotherapy | Not Specified | 1 |
| Lyceum North Western University | Foreign | 1 |
| Lyceum Of Northern Luzon | Private | 4 |
| Lyceum Of Subic Bay | Private | 1 |
| M A Public School | Foreign | 1 |
| M.D.S.U Ajmer Rajasthan | Not Specified | 1 |
| M.L.V. Govt. College, Bhilwara | Not Specified | 1 |
| M.S.Pathak Hom Med College & Hospital,Vadodara ... | Not Specified | 1 |
| M.S.Univesity Of Vadodara,Gujarat,India | Not Specified | 1 |
| Maastricht | Not Specified | 1 |
| Mabalacat College | Private | 1 |
| Mackay Medical College | Not Specified | 1 |
| Madhrasathul Ahmadhiyya | Not Specified | 1 |
| Madhusudan School Of Nursing | Foreign | 3 |
| Madonna University | Foreign | 4 |
| Madonna University Nigeria | Foreign | 2 |
| Madonna University, Livonia, Michigan, Usa | Not Specified | 1 |
| Madonna University, Okija, Anambara State, Nige... | Not Specified | 1 |
| Madras Christian College | Foreign | 1 |
| Madras University | Not Specified | 1 |
| Mae Fah Luang | Foreign | 1 |
| Mae Fah Luang University, Thailand | Not Specified | 2 |
| Mae Fah Luang Univesity | Not Specified | 1 |
| Mae Fha Laung | Not Specified | 1 |
| Maefahluang University,Thailand | Not Specified | 1 |
| Magadh University | Foreign | 1 |
| Mahanakorn University | Not Specified | 1 |
| Mahanakorn University Of Technology | Not Specified | 1 |
| Maharaja Surajmal Senior Secondary School | Foreign | 1 |
| Maharana Pratap Homoeopathic Medical College | Not Specified | 1 |
| Maharanapratap Homoeopathic Medical College | Not Specified | 1 |
| Maharani Janki Kunwar College | Not Specified | 3 |
| Maharashi Dayanand University | Foreign | 1 |
| Maharashi Dayanand University(Rohtak) | Foreign | 1 |
| Maharashtra University Of Health Sciences | Foreign | 1 |
| Maharashtra University Of Health Sciences Nashik | Foreign | 1 |
| Maharna Pratap Homeopathic Medical College | Not Specified | 1 |
| Maharshi Dayanand Sarswati University Ajmer Raj... | Not Specified | 1 |
| Mahasaraswati University Denpasar Bali | Not Specified | 1 |
| Mahashrakham University | Not Specified | 1 |
| Mahatma Gandhi Kashi Vidyapith | Foreign | 1 |
| Mahatma Gandhi University | Foreign | 1 |
| Mahidol | Foreign | 2 |
| Mahidol University . Thailand | Foreign | 1 |
| Mahidol University Bangkok, Thailand | Not Specified | 1 |
| Mahidol University International College | Foreign | 2 |
| Mahipal Singh Mahavidhalya Khumaripur Behta Sad... | Not Specified | 1 |
| Mahipal Singh Mahavidyalaya, Khumaripur, Behta,... | Not Specified | 1 |
| Majo Univ., Thailand | Foreign | 1 |
| Makati Medical Center - College Of Nursing | Private | 2 |
| Makati Medical Center College | Not Specified | 4 |
| Makati Medical Center Collge | Not Specified | 1 |
| Makati Medical Center- College Of Nursing | Private | 1 |
| Makati Medical Center-College Of Nursing | Private | 1 |
| Malayan Colleges Laguna | Private | 1 |
| Management &Amp;Amp; Science University | Not Specified | 1 |
| Management Science University | Not Specified | 1 |
| Manasa College Of Nursing | Not Specified | 1 |
| Mangalore University | Not Specified | 1 |
| Manila Sanitarium Hospital & School Of Medical ... | Private | 1 |
| Manipal University, Karnatarka State , India | Not Specified | 1 |
| Manonmaniam Sundaranar University | Not Specified | 1 |
| Manuel L. Quezon University, Quiapo, Manila | Private | 1 |
| Manuel S. Enverga University Foundation - Cande... | Private | 3 |
| Manuel V. Gallego Foundation Colleges | Private | 1 |
| Mapandi Memorial Medical & Educational Center, ... | Private | 2 |
| Marawi Islamic Computer College | Not Specified | 1 |
| Margoschiss Higher Secondary School | Not Specified | 1 |
| Mariano Marcos State University - College Of Ag... | Not Specified | 3 |
| Mariano Marcos State University - College Of Te... | Not Specified | 2 |
| Marie - Bernarde College | Private | 2 |
| Marinduque State College - Main | Public | 3 |
| Mariners' Polytechnic Colleges | Private | 1 |
| Maritime Academy Of Asia And The Pacific | Private | 2 |
| Marthoma Higer Secondary School Pathanamthitta | Not Specified | 1 |
| Martin Homoeopathiy Medical College | Not Specified | 1 |
| Martinez Memorial College | Private | 3 |
| Martinez Memorial College, Caloocan | Private | 2 |
| Martinez Memorial Colleges | Not Specified | 1 |
| Mary Chiles College, Manila | Private | 2 |
| Mary Help Of Christians College Seminary, Panga... | Private | 1 |
| Mary Johnston College | Private | 3 |
| Marymount University | Not Specified | 1 |
| Maryville University | Foreign | 2 |
| Masbate Colleges | Private | 2 |
| Mater Dei College - Bohol | Private | 2 |
| Matha College Of Physiotherapy | Not Specified | 1 |
| Mathidol University Bkk | Not Specified | 1 |
| Mati Doctors College | Private | 4 |
| Mati Polytechnic College | Private | 1 |
| Mayurbhanj Homoeopathic Medical College & Hospital | Foreign | 1 |
| Mcgill University | Not Specified | 3 |
| Mcgill University (Canada), University Of Sydne... | Not Specified | 1 |
| Mcmaster University | Not Specified | 1 |
| Mds Ajmer | Not Specified | 3 |
| Medgar Evers Cillege | Foreign | 1 |
| Medgar Evers College | Foreign | 2 |
| Medical Colleges of Northern Philippines | Private | 1 |
| Medical Institute Jorhat | Foreign | 2 |
| Medical Science Of Shahid Beheshti University (... | Not Specified | 1 |
| Medical Technical Assistant Academy In Karlsruh... | Not Specified | 1 |
| Meenakshi Arts And Science College ,Madurai,Tam... | Not Specified | 1 |
| Meiji University | Not Specified | 2 |
| Meijo University | Not Specified | 1 |
| Mendero College | Private | 3 |
| Menlo College - Atherton, Ca | Not Specified | 1 |
| Mercer University | Foreign | 1 |
| Meridian International College | Private | 1 |
| Messiah College Foundation | Private | 3 |
| Metro State University | Not Specified | 1 |
| Metro Subic Colleges | Private | 2 |
| Metropolitan Hospital College | Private | 4 |
| Mgr Medical University | Foreign | 1 |
| Mhasarakham University Thailand | Not Specified | 1 |
| Michigan State University | Foreign | 3 |
| Middle East Technical University | Not Specified | 1 |
| Middle Tennessee State University | Foreign | 3 |
| Middlebury College | Not Specified | 1 |
| Midwestern State University | Not Specified | 1 |
| Millat College Laheriasarai | Not Specified | 1 |
| Millennia Institute Singapore | Not Specified | 1 |
| Mina De Oro Institute Of Science & Tech. - Orie... | Private | 1 |
| Mina De Oro Institute Of Science And Technology | Private | 4 |
| Mindanao Autonomous College Foundation | Private | 3 |
| Mindanao Institute Of Healthcare Professionals,... | Private | 2 |
| Mindanao Kokosai Daigaku | Private | 2 |
| Mindanao Polytechnic State College, Cagayan De Oro | Public | 1 |
| Mindanao State University - Buug College | Public | 3 |
| Mindanao State University - Iligan Institute of... | Public | 2 |
| Mindanao State University - Lanao National Coll... | Not Specified | 3 |
| Mindanao State University - Naawan | Public | 3 |
| Mindanao State University - Sulu Development Te... | Public | 3 |
| Mindanao State University - Tawi - Tawi College... | Public | 2 |
| Mindanao State University-Sulu | Public | 1 |
| Minot State University | Foreign | 1 |
| Misamis Oriental State College Of Agriculture A... | Public | 2 |
| Mission College | Not Specified | 2 |
| Missouri State University | Not Specified | 2 |
| Missouri State Univversity | Not Specified | 1 |
| Mma Matric Higher Secondary School | Foreign | 1 |
| Modern Delhi Public School | Foreign | 1 |
| Modern Public Senior Secondary School | Foreign | 1 |
| Mogadishu University, Somalia | Not Specified | 1 |
| Monash University | Foreign | 4 |
| Monash University Clayton, Melbourne, Victoria,... | Not Specified | 1 |
| Morigaon | Not Specified | 1 |
| Mother Theresa Hr Sec School | Not Specified | 1 |
| Mother Theresa Post Graduate And Research Insti... | Foreign | 1 |
| Mothervannini College Of Nursing | Not Specified | 1 |
| Mount Carmel College - Baler | Private | 1 |
| Mount Moriah College | Foreign | 1 |
| Mount St. Mary'S College | Not Specified | 1 |
| Msu Malaysia | Not Specified | 1 |
| Msu-Sch. Of Marine Fisheries & Tech.- Mis. Orie... | Public | 1 |
| Mt. Carmel College Of Bocaue, Bulacan | Private | 3 |
| Mts. V. B. M. College Of Pharmacy | Not Specified | 1 |
| Mudanjiang Medical University | Not Specified | 1 |
| Muqadisho University | Not Specified | 1 |
| Muqdisho University | Not Specified | 1 |
| Murdoch University | Foreign | 1 |
| Musa Bin Nusair | Not Specified | 1 |
| N R Public School | Foreign | 1 |
| Naga College, Naga City | Private | 3 |
| Nagoya | Not Specified | 1 |
| Naish College | Not Specified | 1 |
| Nakhon Ratchasima Rajabhat University | Not Specified | 1 |
| Nakonratchasima College | Foreign | 1 |
| Nakorn Ratchasima Rajabhat University | Not Specified | 1 |
| Nanyang Polytechnic | Foreign | 1 |
| Narayana Junior College Kukatpally | Not Specified | 1 |
| Narayana Pu College | Not Specified | 1 |
| Narayana Vidyalayam | Foreign | 1 |
| Narayanan Junior Collage | Foreign | 1 |
| Naresuan University ,Thailand | Not Specified | 1 |
| Naresuan University /Thailand | Not Specified | 1 |
| Naresuan University Thailand | Not Specified | 1 |
| Naresuan University,Thailand | Not Specified | 1 |
| Naresun University | Foreign | 1 |
| Nat. Sun-Yat Sen Univ, Taiwan | Foreign | 1 |
| Nation Yangming University | Not Specified | 1 |
| National Chung Hsing University | Not Specified | 2 |
| National College | Not Specified | 1 |
| National College Of Business And Arts - Fairview | Private | 1 |
| National College Of Business And Arts - Taytay | Private | 1 |
| National College Of Pharmacy | Not Specified | 1 |
| National College Of Science And Technology - La... | Not Specified | 1 |
| National First Grade College | Private | 3 |
| National Taiwan University | Foreign | 1 |
| National University Of Bangladesh | Not Specified | 1 |
| National University Of Singapore | Foreign | 3 |
| National University, Sampaloc, Manila | Private | 3 |
| Navajyothi,Kannur,Kerala,India | Not Specified | 1 |
| Navamindrahiraj | Not Specified | 1 |
| Navyug Senior Secondary School Abohar | Not Specified | 1 |
| Nazarenus College Foundation | Private | 4 |
| Nevada State College | Not Specified | 1 |
| New England College | Private | 1 |
| New English School | Not Specified | 1 |
| New Jersey City University | Not Specified | 2 |
| New Jersey Institute Of Technology | Foreign | 1 |
| New Jersey Institute Of Technology, New Jersey | Foreign | 1 |
| New Mexico State University | Not Specified | 1 |
| New York Institute Of Technology | Not Specified | 2 |
| New York Medical College | Not Specified | 1 |
| New York University | Foreign | 2 |
| New York University, Ny, Usa | Foreign | 4 |
| New York University, Ny,Usa | Foreign | 1 |
| Niims Nursing College | Foreign | 1 |
| Nims Nursing College | Foreign | 2 |
| Nims Nursing College Jaipur | Not Specified | 1 |
| Nims University College Of Physio Therapy | Not Specified | 1 |
| Nimt Institute Of Medical And Para Medical Scie... | Not Specified | 1 |
| Nirmala College Muvattupuzha | Not Specified | 1 |
| Nirwana College | Not Specified | 1 |
| Nj Valdez Colleges Foundation | Private | 1 |
| Nnamdi Azekiwe University | Not Specified | 1 |
| Nnamdi Azikiwe University | Not Specified | 1 |
| Nnamdi Azikiwe University, Awka | Not Specified | 2 |
| Nnamdi Azikiwe University,(Unizik) | Not Specified | 1 |
| North Carolina Wesleyan College, Usa | Not Specified | 1 |
| North Central Mindanao Colleges | Private | 3 |
| North Davao College (Ndc) Tagum Foundation, Davao | Private | 1 |
| North Davao College - Tagum Foundation | Private | 1 |
| North East Frontier Technical University | Foreign | 1 |
| North Luzon Philippines State College | Public | 2 |
| North Negros College | Private | 1 |
| North Park College, Il, Usa | Foreign | 1 |
| North Valley College Foundation, Inc | Private | 1 |
| Northeastern College Santiago City | Not Specified | 1 |
| Northeastern University | Foreign | 1 |
| Northern Christian College, Laoag City | Private | 1 |
| Northern Illinois University | Foreign | 1 |
| Northern Iloilo Polytechnic State College - Main | Public | 1 |
| Northern Michigan University, Usa | Not Specified | 1 |
| Northern Negros State College Of Science And Te... | Public | 1 |
| Northern Philippines College For Maritime, Scie... | Private | 1 |
| Northwestern College | Private | 1 |
| Northwestern Mindanao State College Of Science ... | Public | 1 |
| Northwestern University, Laoag City | Private | 3 |
| Notre Dame De Namur University | Foreign | 2 |
| Notre Dame Hospital And School Of Midwifery | Private | 3 |
| Notre Dame Of Kidapawan Colleges | Private | 1 |
| Notre Dame University, Indiana, U.S.A. | Foreign | 1 |
| Notre Dame University,Notre Dame Avenue,Cotabat... | Not Specified | 1 |
| Notre Dame of Dadiangas University | Private | 1 |
| Nshm College Of Management &Technology | Foreign | 1 |
| Ntr University Of Health Science | Not Specified | 1 |
| Ntr University Of Health Sciences | Not Specified | 1 |
| Nueva Vizcaya State University - Bambang | Public | 4 |
| Nueva Vizcaya State University, Bayombong, Nuev... | Public | 1 |
| Nursing College | Private | 1 |
| Nyu | Foreign | 1 |
| Oasis Matric Higher Secondary School | Foreign | 1 |
| Oberlin College | Not Specified | 1 |
| Occidental Mindoro State College | Public | 1 |
| Odaiyappa College Of Engineering And Technology | Not Specified | 1 |
| Ohio State University | Not Specified | 1 |
| Olabisi Onabanjo University | Foreign | 3 |
| Olabisi Onabanjo University Ago-Iwoye | Foreign | 1 |
| Olabisi Onabanjo University, Ago Iwoye, Nigeria | Foreign | 1 |
| Olabisi Onabanjo University, Ago Iwoye. | Foreign | 1 |
| Olabisi Onabanjo University, Ago-Iwoye, Ogun State | Not Specified | 1 |
| Olabisi Onabanjo University,Ogun State ,Nigeria. | Not Specified | 1 |
| Olabisi Onabanjo University/Ogun State University | Not Specified | 1 |
| Olabisi Onabanjo Unversity, Ago-Iwoye. | Foreign | 1 |
| Om Sai College | Not Specified | 1 |
| Oman Medical College | Not Specified | 1 |
| Opjs Univarsity Churu | Foreign | 1 |
| Opjs University Churu | Foreign | 3 |
| Opjs University,Churu (Rajasthan) | Foreign | 1 |
| Osaka Gakuin University | Not Specified | 1 |
| Osaka International University | Foreign | 2 |
| Osaka University | Foreign | 1 |
| Osias Educational Foundation | Private | 3 |
| Osmania University | Not Specified | 1 |
| Osun State University | Not Specified | 3 |
| Our Lady Of Lourdes College Foundation | Private | 1 |
| Our Lady Of Lourdes College, Camarines Norte | Private | 2 |
| Our Lady Of Mercy College | Private | 1 |
| Our Lady Of Penafrancia, Sorsogon | Private | 1 |
| Our Lady Of Peñafrancia Seminary | Not Specified | 1 |
| Our Lady Of The Angels Seminary | Private | 1 |
| Our Lady of Fatima University (Fatima Medical S... | Private | 2 |
| Our Lady of Fatima University - Antipolo | Private | 1 |
| Our Lady of Fatima University - Quezon City | Private | 1 |
| Outemon Gakuen University | Not Specified | 1 |
| Overseas Pakistani Foundation | Foreign | 1 |
| Oxford Brookes University | Not Specified | 2 |
| Oxford Matric Higher Secondary School | Not Specified | 1 |
| Oxford Matriculation Higher Secondary School | Not Specified | 1 |
| Pacasum College | Private | 1 |
| Pace University, New York | Foreign | 2 |
| Pacific Union College | Foreign | 3 |
| Palaris College | Private | 1 |
| Palawan State University - San Rafael, Puerto P... | Public | 1 |
| Palmer College Of Chiropractic | Not Specified | 1 |
| Pamantasan Ng Araullo | Private | 4 |
| Pamantasan Ng Cabuyao | Public | 4 |
| Pamantasan Ng Lungsod Ng Valenzuela | Public | 2 |
| Pampanga Agricultural College, Pampanga | Public | 1 |
| Panakronrajabhat University | Not Specified | 1 |
| Panchasheel Homoeopathic Medical College,Khamgaon | Not Specified | 1 |
| Pangasinan Colleges Of Science And Technology | Private | 1 |
| Pangasinan Memorial College - Lingayen, Pangasinan | Private | 1 |
| Pangasinan Merchant Marine Academy | Private | 1 |
| Pangasinan State University | Public | 4 |
| Pangasinan State University - Bayambang | Public | 1 |
| Pangasinan State University - Binmaley | Not Specified | 1 |
| Pangasinan State University - Infanta | Not Specified | 1 |
| Pangasinan State University - San Carlos City | Not Specified | 1 |
| Pangasinan State University - Urdaneta City | Public | 1 |
| Pangasinan Universal Institute | Not Specified | 1 |
| Parco Nord Eugenio Montale | Not Specified | 1 |
| Partido State University - Main | Public | 2 |
| Pasig Catholic College | Private | 3 |
| Pastor Bonus Seminary | Private | 1 |
| Patna University | Foreign | 1 |
| Pennsylvania State University, Usa | Foreign | 2 |
| Pepperdine University | Foreign | 1 |
| Pepperdine University, California | Foreign | 2 |
| Pepperdine University/Usa | Foreign | 1 |
| Perpetual Help College Of Pangasinan | Private | 1 |
| Perpetual Help College Of Pangasinan-Malasique,... | Private | 1 |
| Pharmed Academy | Not Specified | 1 |
| Phil Schl Of Business Admn (Psba)-R.Papa St. Sa... | Private | 1 |
| Philadelphia University | Not Specified | 1 |
| Philippine Advent College | Private | 2 |
| Philippine College Of Criminology | Private | 2 |
| Philippine College Of Science And Technology | Private | 4 |
| Philippine Cultural College | Private | 1 |
| Philippine Law School | Private | 1 |
| Philippine Military Academy - Baguio City, Benguet | Public | 3 |
| Philippine National Police Academy | Public | 1 |
| Philippine State College Of Aeronautics - Main | Public | 1 |
| Philippine State College Of Aeronautics, Lapu-L... | Public | 2 |
| Philippine Women&#039;S University - Manila | Not Specified | 1 |
| Philippine Women&#039;S University -Taft Avenue... | Private | 1 |
| Philippine Women&#039;S University Quezon City | Not Specified | 1 |
| Philippine Women&#039;S University(Taft,Manila) | Private | 1 |
| Philippine Women&Amp;#039;S University - Malate... | Not Specified | 1 |
| Philippine Women'S University | Private | 2 |
| Philippine Women'S University (Taft) | Private | 1 |
| Philippine Women'S University (Taft, Manila) | Not Specified | 1 |
| Philippine Women'S University - Taft Ave. Manila | Private | 1 |
| Philippine Women'S University - Taft Avenue, Ma... | Private | 1 |
| Philippine Women'S University -Taft Ave, Manila | Private | 1 |
| Philippine Women'S University Manila | Not Specified | 1 |
| Philippine Women'S University Taft Avenue | Private | 1 |
| Philippine Women'S University Taft Avenue Manila | Private | 1 |
| Philippine Women'S University Taft Avenue, Manila | Private | 2 |
| Philippine Women'S University Taft Manila | Not Specified | 2 |
| Philippine Women'S University [Taft Avenue, Man... | Private | 1 |
| Philippine Women'S University, Taft Manila | Not Specified | 1 |
| Philippine Women'S University- Taft Avenue, Manila | Private | 2 |
| Philippine Women'S University- Taft, Manila | Not Specified | 1 |
| Philippine Womens University Manila | Not Specified | 1 |
| Philippine Womens University, Taft Avenue Manila | Private | 1 |
| Phuket Rajabhat University | Not Specified | 1 |
| Pibulsongkram Rajabhat University | Not Specified | 1 |
| Pibulsongkroam Rajabhat University | Not Specified | 1 |
| Pillai'S College Of Arts, Commerce And Science | Not Specified | 1 |
| Pimsat Colleges - Dagupan | Not Specified | 1 |
| Pines City Educational Center, Baguio City | Private | 2 |
| Plt College Incorporated | Not Specified | 1 |
| Point Loma Nazarene University, San Diego, Cali... | Not Specified | 1 |
| Polytechnic College Of La Union | Private | 1 |
| Polytechnic University Of The Philippines - Ori... | Public | 2 |
| Polytechnic University Of The Philippines - Taguig | Public | 1 |
| Polytechnic University of the Philippines | Public | 1 |
| Pooja Vidhyalaya | Not Specified | 1 |
| Portland State University | Not Specified | 2 |
| Post Graduate College Of Science,Saifabad,Hyder... | Not Specified | 1 |
| Prachomkiao College Of Nursing | Foreign | 1 |
| Pragathi Degree College | Foreign | 4 |
| Prakprokklao Nursing College | Not Specified | 1 |
| Pre University | Not Specified | 1 |
| Prefectural University Of Hiroshima | Not Specified | 1 |
| Prema Katiyar Shikshan Sansthan | Not Specified | 1 |
| Presbyterian University College | Not Specified | 1 |
| Prince Of Songkhla University | Foreign | 3 |
| Prince Of Songkla | Not Specified | 1 |
| Prince Of Songkla University, Indonesia | Foreign | 1 |
| Prince Of Sonkla University | Not Specified | 1 |
| Princess Of Naradhiwas University | Not Specified | 1 |
| Priyadarshini Dental College | Not Specified | 1 |
| Psg Arts And Science College .Coimbatore.Tamil ... | Not Specified | 1 |
| Psg Arts And Science College,Coimbatore,Tamil Nadu | Not Specified | 1 |
| Pt. L.M.S. Govt. P.G. College, Rishikesh | Foreign | 1 |
| Pt.Jagnarain Shukla Gramodya Mahavidyalaya Rani... | Not Specified | 1 |
| Pt.L.M.S Govt.Autonomous Pg College | Not Specified | 1 |
| Punjab Medical Institute | Not Specified | 1 |
| Purchase College, State University Of New York | Not Specified | 1 |
| Purdue Univ. | Foreign | 1 |
| Purdue University | Foreign | 2 |
| Pusan National University, Korea | Not Specified | 1 |
| Pushpagiri Collage Of Nursing,Mahatma Gandhi Un... | Not Specified | 1 |
| Qiqihaer Medical University | Not Specified | 1 |
| Qiqihar Medical College | Not Specified | 4 |
| Qiqijar Medical University | Not Specified | 1 |
| Queen Mary University Of London | Not Specified | 1 |
| Queen'S University | Not Specified | 1 |
| Queen'S University Belfast | Foreign | 1 |
| Quincy University | Not Specified | 1 |
| R K Vigyan Mahavidhyalaya | Not Specified | 1 |
| R.L.S.Y College Ranchi | Not Specified | 1 |
| R.L.S.Y College, Ranchi University | Foreign | 1 |
| R.R. Degree College, Sarai Pratham, Bidhuna | Not Specified | 1 |
| Radha Krushna, Toshniwal Ayurved Mahavidyalaya | Foreign | 1 |
| Ragiv Gandhi University | Not Specified | 1 |
| Raj Rishi College | Not Specified | 2 |
| Rajabhat Institute Bansomedjchaopraya | Not Specified | 1 |
| Rajabhat Institute Suan Dusit | Not Specified | 1 |
| Rajabhat Institute Suansunandha | Not Specified | 1 |
| Rajah,S Higher Sec School | Not Specified | 1 |
| Rajamangala University Of Technology Srivijaya | Not Specified | 1 |
| Rajamangala University Of Technology Srivijaya ... | Not Specified | 1 |
| Rajamangala University Of Technology Thanyaburi | Foreign | 4 |
| Rajamangala University Of Technologysrivijaya | Not Specified | 1 |
| Rajamankala University Of Thechnology Thanyaburi | Not Specified | 1 |
| Rajasthan University | Foreign | 1 |
| Rajasthan Vidyapeeth Homoeopathic Medical College | Not Specified | 1 |
| Rajeev College Of Nursing , Hassan 573201 , Kar... | Not Specified | 1 |
| Rajinibon School | Not Specified | 1 |
| Rajiv Gandhi Medical College Of Electropathy & ... | Not Specified | 1 |
| Rajiv Gandhi University Health Science | Foreign | 1 |
| Rajiv Gandhi University Of Health Sciences | Foreign | 1 |
| Rajiv Gandhi University Of Health Sciences,Karn... | Not Specified | 3 |
| Rajiv Gandhi University Of Health Sciences. | Foreign | 2 |
| Rajiv Ghandhi University,Karnataka,India | Not Specified | 1 |
| Rajrishi College | Not Specified | 1 |
| Ram Manohar Lohia Avadh University | Not Specified | 1 |
| Ram-Eesh Institute Of Vocational And Technical ... | Foreign | 1 |
| Ramachandra | Not Specified | 1 |
| Ramakrishna Ayurvedic Medical College | Not Specified | 1 |
| Ramapo College Of New Jersey | Not Specified | 2 |
| Ramkhamhaeng University, Thailand | Not Specified | 1 |
| Ramkrishna Institute Of Physiotherapy Raipur | Not Specified | 1 |
| Ramon Magsaysay Technological University | Public | 2 |
| Ramon Magsaysay Technological University - Mond... | Public | 1 |
| Ramon Magsaysay Technological University - Ramo... | Public | 3 |
| Rana Pratap P.G. College | Not Specified | 1 |
| Rangsit | Not Specified | 4 |
| Rangsit Univerity | Foreign | 1 |
| Rangsit Universiti | Foreign | 2 |
| Rangsit University Thailand | Foreign | 1 |
| Rangsit University,Thailand | Foreign | 4 |
| Rangsit University. | Foreign | 1 |
| Rani Tirumala Devi Degree College Of Sciences | Not Specified | 1 |
| Ratchathani University | Foreign | 2 |
| Remedios T Romualdez Medical Foundation -Taclob... | Not Specified | 1 |
| Remedios T. Romualdez Medical Foundation | Not Specified | 4 |
| Remedios T. Romualdez Medical Foundation (Taclo... | Not Specified | 1 |
| Remedios T. Romualdez Medical Foundation College | Not Specified | 2 |
| Remedios T. Romualdez Medical Foundation Taclob... | Not Specified | 2 |
| Remedios T. Romualdez Medical Foundation Taclob... | Not Specified | 1 |
| Remedios T. Romualdez Medical Foundation, Taclo... | Not Specified | 3 |
| Remedios T. Romualdez Medical Foundation, Taclo... | Not Specified | 1 |
| Remedios T. Romualdez Medical School Foundation... | Not Specified | 1 |
| Remedios T. Romualdez Memorial Foundation | Not Specified | 1 |
| Remedios Trinidad Romualdez Medical Center Tacl... | Not Specified | 1 |
| Remedios Trinidad Romualdez Medical Foundation ... | Private | 1 |
| Remedios Trinidad Romualdez Medical Foundation ... | Private | 2 |
| Remedios Trinidad Romualdez Medical Foundation ... | Private | 1 |
| Remedios Trinidad Romualdez Medical Foundation ... | Private | 3 |
| Remedios Trinidad Romualdez Medical Foundation ... | Private | 1 |
| Remedios Trinidad Romualdez Medical Foundation,... | Private | 1 |
| Remedios Trinidad Romualdez Medical School Foun... | Not Specified | 1 |
| Remedios Trinidad Romualdez School, Tacloban | Private | 1 |
| Remedios Trinidad Romualdezmedical Foundation | Not Specified | 1 |
| Rensselaer Polytechnic Institute | Not Specified | 1 |
| Riverside College Bacolod | Private | 1 |
| Rizal Memorial Colleges | Private | 1 |
| Rizal Technological University - Pasig | Public | 1 |
| Rmit University | Not Specified | 1 |
| Rochville University | Not Specified | 1 |
| Rogationist Seminary College | Private | 2 |
| Romblon State University - Main | Public | 3 |
| Roosevelt College - Cainta | Not Specified | 1 |
| Rosalind Franklin University Of Medicine And Sc... | Not Specified | 1 |
| Royal Girls Science School | Not Specified | 1 |
| Royal Melbourne Institute Of Technology University | Not Specified | 1 |
| Rtr Memorial School-Makati Med. Ctr., Makati | Foreign | 2 |
| Rtrms Makati Medical Center, Makati | Private | 1 |
| Rutgers University - New Brunswick Campus | Not Specified | 1 |
| Rutgers University New Brunswick | Not Specified | 2 |
| Rutgers University Of New Brunswick, Nj | Not Specified | 1 |
| Rutgers University State Of New Jersey | Not Specified | 1 |
| Rutgers University, New Brunswick | Not Specified | 1 |
| Rutgers, The State University Of New Jersey | Not Specified | 2 |
| Rutgers- The State University Of New Jersey | Not Specified | 1 |
| Ryerson University | Foreign | 1 |
| S R V Matric Hr Sec School Samayapuram Tiruchir... | Not Specified | 1 |
| S V M Science And Technology Pg College | Foreign | 1 |
| S. P. Y Gaya | Foreign | 1 |
| S.M.D College Nechuya Jalalpur | Foreign | 1 |
| S.P.Y College Gaya | Not Specified | 1 |
| S.P.Y.C Gaya | Foreign | 1 |
| S.V.S Medical College | Not Specified | 1 |
| Sacred Heart Convent | Not Specified | 1 |
| Sagxh | Not Specified | 1 |
| Saint Anne College Of Lucena | Private | 1 |
| Saint Anthony College Of Roxas City | Private | 1 |
| Saint Columban College | Private | 2 |
| Saint Columban'S College | Private | 1 |
| Saint Ferdinand College | Private | 4 |
| Saint Francis Of Assisi College | Private | 2 |
| Saint James School Of Medicine | Not Specified | 1 |
| Saint John Colleges | Private | 1 |
| Saint Joseph College | Private | 1 |
| Saint Joseph College Cavite City | Not Specified | 1 |
| Saint Joseph Institute Of Technology | Private | 4 |
| Saint Joseph Institute Of Technology, Butuan City | Private | 1 |
| Saint Joseph Of Quezon City | Not Specified | 1 |
| Saint Leo University | Private | 1 |
| Saint Louis College / Bachelor Of Nursing Science | Not Specified | 1 |
| Saint Louis College, Bangkok | Not Specified | 1 |
| Saint Louis University, Baguio City | Not Specified | 1 |
| Saint Mary'S College | Private | 3 |
| Saint Mary'S College Of Baliuag | Private | 4 |
| Saint Mary'S University, Bayombong, Nueva Vizcaya | Private | 1 |
| Saint Mary's University | Private | 1 |
| Saint Marys University Bayombong, Nueva Vizcaya | Private | 1 |
| Saint Michael'S College, Iligan City | Not Specified | 1 |
| Saint Paul University - Dumaguete | Private | 1 |
| Saint Paul University Dumaguete | Private | 2 |
| Saint Paul University Philippines, Tuguegarao C... | Private | 1 |
| Saint Paul'S Business School | Private | 2 |
| Saint Sahara Ayurvedic Medical College & Hospit... | Foreign | 1 |
| Saint Sahara Ayurvedic Medical College & Hospit... | Foreign | 1 |
| Saint Scholastica&#039;S College Malate, Manila | Not Specified | 1 |
| Saint Scholastica&#039;S College Tacloban | Not Specified | 1 |
| Saint Scholastica'S College, Tacloban City | Private | 3 |
| Saint Theresa College Inc., Surigao Del Sur | Private | 1 |
| Saint Theresa College Of Tandag | Private | 2 |
| Saint Theresa'S College Of Cebu | Private | 1 |
| Saint Vincent'S College, Dipolog City | Private | 2 |
| Saintlouis Collage | Not Specified | 1 |
| Saints John And Paul Colleges | Private | 2 |
| Saitama Prefectural University | Foreign | 2 |
| Salazar Colleges Of Science And Institute Of Te... | Private | 2 |
| Samuel Merritt University | Not Specified | 2 |
| San Carlos College | Private | 1 |
| San Carlos Seminary | Private | 1 |
| San Carlos Seminary College | Private | 1 |
| San Diego State University | Foreign | 4 |
| San Francisco State Univeristy | Foreign | 1 |
| San Francisco State University | Foreign | 3 |
| San Francisco State University, Usa | Foreign | 2 |
| San Jose State University | Foreign | 2 |
| San Pablo Major Seminary | Private | 3 |
| San Pedro College Davao City | Private | 1 |
| San Pedro College Of Davao | Not Specified | 1 |
| San Sebastian College - Recoletos | Private | 2 |
| Sancta Maria, Mater Et Regina, Seminarium | Private | 3 |
| Sanjeevan College Of Pharmacy | Foreign | 3 |
| Sann Institute Of Nursing,Baluwatar,Nepal | Not Specified | 1 |
| Santa Clara University | Foreign | 2 |
| Santa Clara University, California, Usa | Foreign | 2 |
| Santosh College Of Occupational Therapy | Not Specified | 1 |
| Santosh Kumar Mahavidyalaya, Kasimpur , Behdar ... | Not Specified | 1 |
| Sappasithiprasong Nursing College | Not Specified | 1 |
| Sappasitthiprasong Nursing College | Not Specified | 1 |
| Sarada Vilas College | Not Specified | 1 |
| Sardar Patel University | Foreign | 1 |
| Sardar Patel University, India | Foreign | 1 |
| Sarvanand Shandilya Yogeshwar Mahavidalya | Foreign | 1 |
| Schola De San Jose | Private | 1 |
| School Of Achiver | Not Specified | 1 |
| School Of Physiotherapy,Rkuniversity | Not Specified | 1 |
| Scott Christen College | Private | 1 |
| Scott Christian College | Private | 1 |
| Scripps College | Foreign | 2 |
| Sea And Sky College | Private | 1 |
| Sejong University, Korea | Foreign | 1 |
| Sekolah Tinggi Filsafat Driyarkara | Foreign | 2 |
| Seoul Cyber University | Not Specified | 1 |
| Seoul National University | Foreign | 2 |
| Seton Hall University, Nj, Usa | Foreign | 1 |
| Shandong Medical University | Foreign | 1 |
| Shanghai Jaio Tiang Unversity School Of Medicine | Not Specified | 1 |
| Shanxi Medical University | Foreign | 1 |
| Shivaji College Of Nursing, Ruhs | Foreign | 2 |
| Shobhit University, Meerut | Not Specified | 1 |
| Showa Women'S University | Not Specified | 3 |
| Shree Babu Singh Degree College Nawabganj | Not Specified | 1 |
| Shree Khrishna Govt. Ayurvedic College And Hosp... | Not Specified | 1 |
| Shree Krishna Govt.Ayurvedic College And Hospit... | Foreign | 1 |
| Shree Krishna Govt.Ayurvedic College,Kurukshetra | Not Specified | 1 |
| Shree P.K Desai Vidhyalaya,Kim | Not Specified | 1 |
| Shree Shree Gourgobind Girls College | Foreign | 1 |
| Shree Shree Gourgovind Girls' College | Foreign | 1 |
| Shree Vasishtha Vidhyalaya | Not Specified | 1 |
| Shri Ayurved Mahavidyalaya | Not Specified | 1 |
| Shri K.M Patel Vidhyamandir | Not Specified | 1 |
| Shri Kashi Chandradev Yadav Mahavidyalaya Hajip... | Not Specified | 1 |
| Shri Kashi Chandradev Yadav Mahavidyalaya Hazip... | Not Specified | 1 |
| Shri Krishana Govt. Ayurvedic College | Not Specified | 2 |
| Shri Sitaram Jaju Govt.Girls College Neemuch | Not Specified | 1 |
| Shridhar University | Foreign | 3 |
| Shrishit Vidyashram Brammapuram Village Vellore | Not Specified | 1 |
| Siena College | Private | 1 |
| Siena College-Taytay | Private | 4 |
| Sigma Institute Of Physiotherapy | Not Specified | 1 |
| Siit, Thammasat University | Foreign | 1 |
| Sil[Akorn University | Foreign | 1 |
| Silpahorm College, Thailand | Foreign | 1 |
| Silpakorn University | Foreign | 4 |
| Silpakorn University.Thailand | Not Specified | 1 |
| Simon Fracer University | Foreign | 1 |
| Simon Fraser University | Foreign | 4 |
| Singapore Institute Of Commerce | Not Specified | 1 |
| Singhania University | Not Specified | 2 |
| Sirindhorn College Of Public Health Khon Kaen | Not Specified | 1 |
| Sirindhorn College Public Health | Not Specified | 1 |
| Sjg Ayurvedic Medical College | Foreign | 4 |
| Skamc | Foreign | 1 |
| Skv Matric Higher Secondary School | Foreign | 1 |
| Slopeland Public School | Not Specified | 1 |
| Smith College | Not Specified | 1 |
| Smt,A.J.Savla Homoeopathic Medical College | Not Specified | 1 |
| Smt. Genda Devi Mahavidyalaya | Not Specified | 1 |
| Smt. Vidyawati College Of Pharmacy, Jhansi | Foreign | 1 |
| Smt.A.J.Savla Homeopathic Medical College Mehsa... | Not Specified | 1 |
| Smt.A.J.Savla Homoeopathic Medical College | Not Specified | 1 |
| Smt.Nilaben Manubhai Padalia Pharmacy College | Not Specified | 1 |
| Sofia College Of Nursing,Rguhs Bangalore | Not Specified | 1 |
| Songkhla Nursing College | Not Specified | 1 |
| Soni Nursing College | Private | 1 |
| Sonoma State University | Foreign | 2 |
| Sony Academy Sr Sec School, Nimda Gate | Not Specified | 1 |
| South Western | Private | 1 |
| South Western University | Private | 2 |
| South Western University Phinma | Not Specified | 1 |
| Southeast Missouri State Universe | Not Specified | 1 |
| Southern Bicol Colleges, Masbate | Private | 1 |
| Southern Christian College | Private | 1 |
| Southern Illinois University Of Carbondale - Il... | Foreign | 1 |
| Southern Luzon State University - Tiaong | Public | 1 |
| Southern Methodist University-Dallas, Texas | Foreign | 1 |
| Southern Mindanao Colleges | Private | 1 |
| Southern Philippines Agriculture, Business, Mar... | Private | 1 |
| Southway College Of Technology | Private | 1 |
| Southwestern Mindanao Islamic Institute | Private | 1 |
| Southwestern University Cebu City | Not Specified | 1 |
| Southwestren University Cebu City | Not Specified | 1 |
| Spa College - Datu Piang, Maguindanao | Private | 2 |
| Srd Modi College | Not Specified | 1 |
| Sree Venkateswara Institute Of Medical Sciences | Not Specified | 1 |
| Sri B. R. Mirdha Govt. College Nagaur | Foreign | 1 |
| Sri Chaitanya Junior Collage | Foreign | 1 |
| Sri Chaitanya Junior College | Foreign | 3 |
| Sri Chiatanya Junior College | Foreign | 1 |
| Sri Guru Harkrishan Ss Pub Sch Gt Rd Amritsar P... | Not Specified | 1 |
| Sri Kalabairaveswara Swamy Ayurvedic Medical Co... | Not Specified | 1 |
| Sri Krishnadevaraya University | Not Specified | 1 |
| Sri Lankan College Of Pharmacy | Not Specified | 1 |
| Sri Ram Charan Singh Mahavidyalaya Jatora Balde... | Not Specified | 1 |
| Sri Sai Ram Siddha Medical College | Not Specified | 1 |
| Sri Shanthi College Of Nursing | Not Specified | 1 |
| Sri Venkata Sai | Not Specified | 1 |
| Sri Venkata Sai College Of Diploma In Lab Techn... | Not Specified | 1 |
| Sri Venkata Sai College Of Nursing | Foreign | 2 |
| Sri Venkateswara Institute Of Medical Sciences | Not Specified | 1 |
| Sri Vidhya Mandir Matric Hr Sec School | Not Specified | 1 |
| Sri Vidya Mandir Mat Hr Sec School Krishnagiri | Not Specified | 1 |
| Sri Vijay Vidhyalaya Matric Higher Secondary Sc... | Not Specified | 1 |
| Sri Vijay Vidyalaya | Not Specified | 1 |
| Sri Vijay Vidyalaya Matric Higher Secondary School | Not Specified | 1 |
| Srimahasarakham College Of Nursing | Not Specified | 2 |
| Srinakarinwirot University | Foreign | 1 |
| Srinakarinwirote University, Thailand | Foreign | 2 |
| Srinakharinwirot | Not Specified | 2 |
| Srinakharinwirot University, Nakhonnayok, Thailand | Not Specified | 1 |
| Srinakharinwirot University, Thailand | Foreign | 2 |
| Srm University | Foreign | 3 |
| Srm Univesity | Foreign | 1 |
| Srv Boys Higher Secondary School | Foreign | 1 |
| Srv Matric Hr Sec School | Not Specified | 2 |
| Srv.Matric.Hr.Sec.School | Not Specified | 1 |
| St Bernadette Of Lourdes College | Private | 1 |
| St George&#039;S University Of London | Not Specified | 1 |
| St Marys Higher Secondary School | Not Specified | 1 |
| St Paul University, Tuguegarao | Not Specified | 1 |
| St Theresa International College | Foreign | 1 |
| St. Aleexius College | Private | 1 |
| St. Anne College Lucena, Inc.-Gulang-Gulang, Lu... | Private | 1 |
| St. Anthony College Of Calapan City | Private | 1 |
| St. Augustine School Of Nursing | Private | 1 |
| St. Benedict College | Private | 1 |
| St. Columbian College, Pagadian City | Private | 1 |
| St. Crispin'S Sec School | Foreign | 1 |
| St. Dominic College Of Asia | Private | 1 |
| St. Dominic Savio College | Private | 4 |
| St. Gabriel College - Kalibo, Aklan | Private | 3 |
| St. James College Of Quezon City | Private | 1 |
| St. John & Paul Colleges, Laguna | Private | 1 |
| St. John'S University, New York, Usa | Foreign | 1 |
| St. Joseph College | Private | 1 |
| St. Joseph College - Cavite City | Private | 1 |
| St. Joseph College, Maasin, Southern Leyte | Private | 2 |
| St. Joseph'S College Of Rodriguez | Private | 1 |
| St. Joseph'S University, Philadelphia, Pa | Not Specified | 1 |
| St. Jude College - Manila | Private | 1 |
| St. Jude College Manila | Private | 2 |
| St. Louis University Baguio | Not Specified | 1 |
| St. Luke School Of Medicine | Private | 1 |
| St. Mary'S College | Private | 3 |
| St. Mary'S College Of Borongan | Private | 1 |
| St. Mary'S College Of Ca | Not Specified | 1 |
| St. Mary'S College Of California, Usa | Private | 2 |
| St. Mary'S College Of Maryland | Not Specified | 1 |
| St. Mary'S College Of Tagum | Private | 1 |
| St. Mary'S University | Private | 1 |
| St. Michael'S College Iligan City | Not Specified | 1 |
| St. Michael'S College Of Iligan City | Not Specified | 1 |
| St. Michael'S College Of Laguna | Private | 2 |
| St. Michael'S College- Iligan City | Not Specified | 1 |
| St. Paul College, Dumaguete City | Private | 2 |
| St. Paul University Philippines (Tuguegarao City) | Not Specified | 1 |
| St. Paul University Philippines - Tuguegarao, C... | Not Specified | 1 |
| St. Paul University Philippines Tuguegarao | Not Specified | 3 |
| St. Paul University Philippines Tuguegarao City | Not Specified | 2 |
| St. Paul University Philippines Tuguegarao City... | Private | 1 |
| St. Paul University Philippines, Tuguegarao | Not Specified | 1 |
| St. Paul University Philippines, Tuguegarao City | Not Specified | 1 |
| St. Paul University Philippines, Tuguegarao Cit... | Private | 1 |
| St. Paul University Quezon City | Private | 4 |
| St. Paul'S Inter College | Not Specified | 1 |
| St. Paul'S School Of Ormoc Foundation, Inc. | Not Specified | 1 |
| St. Pauls University Quezon City | Private | 1 |
| St. Peter College Seminary, Agusan Del Sur | Private | 1 |
| St. Peter'S College | Private | 3 |
| St. Peter'S College - New Jersey, Usa | Private | 3 |
| St. Peter's College | Private | 1 |
| St. Rita Hospital Coll. Of Nursing, Tondo, Manila | Private | 1 |
| St. Rita Hospital College Of Nursing And School... | Private | 4 |
| St. Scholastica&#039;S College Of Health Sciences | Not Specified | 1 |
| St. Scholastica'S College - Manila | Not Specified | 1 |
| St. Scholastica'S College Of Tacloban | Not Specified | 1 |
| St. Scholastica'S College Tacloban | Private | 2 |
| St. Scholastica'S Colloege-Tacloban | Private | 1 |
| St. Scj\Holastica College Tacloban | Not Specified | 1 |
| St. Theresa International College | Foreign | 1 |
| St. Theresa Inti College Thailand | Not Specified | 1 |
| St. Theresa'S College, Cebu | Private | 2 |
| St. Thomas Aquianas Major Seminary | Not Specified | 1 |
| St. Vincent Fermer Seminary | Private | 1 |
| St.Ann'S College Of Nursing | Private | 3 |
| St.Ann'S Degree College For Womens | Private | 1 |
| St.Francis College | Private | 1 |
| St.Francis Hss,Aluva | Not Specified | 1 |
| St.Francis Xavier'S Hr.Sec.School | Not Specified | 1 |
| St.Joans College Of Vocational Studies | Private | 1 |
| St.John'S College Of Nursing | Not Specified | 1 |
| St.Joseph College Cavite City | Private | 1 |
| St.Joseph'S College For Women(A) | Not Specified | 1 |
| St.Marys College | Private | 1 |
| St.Paul University Iloilo | Private | 1 |
| St.Theresa International College | Foreign | 2 |
| Stanford University | Not Specified | 1 |
| Stanford University, California, U.S.A. | Foreign | 3 |
| State University Of New York | Foreign | 2 |
| State University Of New York (Suny) At Stony Brook | Not Specified | 1 |
| State University Of New York - Brockport - New ... | Not Specified | 1 |
| State University Of New York At Binghamton | Not Specified | 1 |
| State University Of New York At Cortland | Not Specified | 1 |
| State University Of New York At Stony Brook | Not Specified | 1 |
| State University Of New York-Plattsburgh | Not Specified | 1 |
| Stephen F. Austin State University | Not Specified | 1 |
| Sti Baguio City | Not Specified | 1 |
| Sti College - Legazpi City | Private | 1 |
| Sti College - Lucena | Not Specified | 1 |
| Sti College - Quezon Avenue | Private | 2 |
| Sti College - Sta. Cruz | Not Specified | 1 |
| Sti College - Sta. Maria | Private | 4 |
| Sti College - Tacloban | Not Specified | 1 |
| Sti College - Zamboanga | Private | 4 |
| Sti College Baguio City | Not Specified | 1 |
| Sti College Zamboanga Branch | Not Specified | 1 |
| Sti Colleges Of Mindanao | Private | 2 |
| Sti Ecollege Southwoods | Private | 1 |
| Sti Education Services Group | Private | 3 |
| Sti Education Services Group - Global City | Private | 4 |
| Stockton University | Not Specified | 1 |
| Study Well Pub Sch Lakhimpur Rd Sitapur Up | Not Specified | 1 |
| Sukhothai Thammathirat Open University | Foreign | 1 |
| Sukhothai Thammathirat Open University, Thailand | Foreign | 2 |
| Sultan Kudarat Educational Institution | Private | 4 |
| Sultan Kudarat Polytechnic State College | Public | 4 |
| Sunchon National University, Korea | Foreign | 1 |
| Sung Kyun Kwan University, Korea | Foreign | 1 |
| Sunrise University, Alwar | Not Specified | 1 |
| Suny (State University Of New York) Stony Brook | Not Specified | 1 |
| Suny Binghamton | Not Specified | 1 |
| Suny Stony Brook, New York | Foreign | 1 |
| Suratthani Rajabhat University | Not Specified | 1 |
| Surigao Del Sur Polytechnic State College | Public | 4 |
| Surigao Del Sur State University - Main | Public | 2 |
| Suwon Women'S Colleage | Not Specified | 1 |
| Suwon Women'S College | Not Specified | 1 |
| Swami Dayanand Degree College | Not Specified | 1 |
| Swami Vivekanand College Phulera (Jaipur Raj.) | Not Specified | 1 |
| Swami Vivekanand College, Phulera (Jaipur) | Not Specified | 1 |
| Syracuse University | Not Specified | 1 |
| Systems Plus College Foundation | Not Specified | 2 |
| T. John College Of Pharmacy | Not Specified | 1 |
| T.B.D.S. Janta College,Goh | Not Specified | 1 |
| Tabaco College | Private | 1 |
| Tadikela Subbaiah College Of Nursing | Foreign | 1 |
| Tagore Matric Higher Secondary School | Not Specified | 1 |
| Taishan Medical University | Not Specified | 1 |
| Taiwan Medical University | Not Specified | 1 |
| Tajen University | Not Specified | 2 |
| Tamilnadu Dr. M G R University | Not Specified | 2 |
| Tanchuling College | Private | 1 |
| Tarlac College Of Agriculture | Private | 1 |
| Technological Institute Of The Philippines - Ma... | Private | 1 |
| Technological Institute Of The Philippines - Qu... | Private | 2 |
| Technological University Of The Philippines - V... | Public | 3 |
| Teerthanker Mahaveer University | Foreign | 1 |
| Tehran | Not Specified | 1 |
| Tehran University | Not Specified | 1 |
| Temple University | Foreign | 1 |
| Temple University Philadelphia, Pa | Not Specified | 1 |
| Temple University, Usa | Foreign | 4 |
| Tennessee Technological University | Not Specified | 1 |
| Texas A & M University, Usa | Foreign | 1 |
| Texas A & M University-Corpus Christi | Not Specified | 1 |
| Texas A&Amp;M University | Not Specified | 1 |
| Texas A&M University | Not Specified | 1 |
| Texas A&M University At Corpus Christi | Not Specified | 1 |
| Texas Christian University | Not Specified | 1 |
| Texas Tech University | Foreign | 1 |
| Thai Red Cross College Of Nursing | Not Specified | 1 |
| Thai Red Cross. | Not Specified | 1 |
| Thamasat University | Foreign | 1 |
| Thammasart University | Foreign | 1 |
| Thammasat | Not Specified | 1 |
| Thammasat University,Bangkok Thailand | Not Specified | 1 |
| Thammasat University,Bangkok,Thailand | Not Specified | 1 |
| The Adelphi College | Private | 1 |
| The Art Institute Of California — Silicon Valley | Not Specified | 1 |
| The College Of New Jersey | Foreign | 1 |
| The College Of Staten Island Of The City Univer... | Not Specified | 1 |
| The Doctor'S Clinic And Hospital School Foundat... | Private | 1 |
| The Family Clinic Incorporated | Not Specified | 1 |
| The George Washington University | Not Specified | 1 |
| The Gujarat Nursing Council | Not Specified | 1 |
| The Hindu Hss | Foreign | 1 |
| The Maharaja Sayaji Rao University Of Baroda | Foreign | 1 |
| The Maharaja Sayajirao University Of Baroda | Foreign | 2 |
| The Master'S College | Not Specified | 1 |
| The Nigerian Institute Of Homoeopathy | Not Specified | 1 |
| The Ohio State Univ. | Foreign | 2 |
| The Ohio State University | Foreign | 4 |
| The Philippine Women'S University System - Quez... | Private | 4 |
| The Tamil Nadu Dr M.G.R Medical University | Foreign | 1 |
| The Tamil Nadu Dr Mgr Medical University | Not Specified | 1 |
| The Tamil Nadu Dr.M.G.R .Medical University | Foreign | 2 |
| The Tamil Nadu Dr.M.G.R. Medical University | Foreign | 1 |
| The Tamilnadu Dr.M.G.R. Medical University | Not Specified | 1 |
| The Tamilnadudr.M.G.R.Medical University Chenna... | Not Specified | 1 |
| The Thai Red Cross College Of Nursing | Not Specified | 1 |
| The University Of British Columbia | Foreign | 2 |
| The University Of Houston | Not Specified | 1 |
| The University Of Melbourne | Foreign | 2 |
| The University Of North Carolina At Greensboro | Not Specified | 1 |
| The University Of Pittsburgh | Foreign | 1 |
| The University Of Queensland | Foreign | 1 |
| The University Of Rajasthan | Foreign | 1 |
| The University Of Sydney | Foreign | 1 |
| The University Of Texas At Austin | Foreign | 1 |
| The University Of Texas At San Antonio | Not Specified | 1 |
| The University Of The Thai Chamber Of Commerce ... | Not Specified | 1 |
| Thonburi University | Not Specified | 1 |
| Tiwi Community College | Public | 1 |
| Tmm College Of Nursing/Mg University/ India | Not Specified | 1 |
| Tokyo Medical University | Not Specified | 1 |
| Tokyo University | Not Specified | 1 |
| Tolani Institute Of Pharmacy,Adipur | Foreign | 1 |
| Tomas Claudio Memorial College | Private | 3 |
| Tomas Del Rosario College | Private | 3 |
| Touro University | Not Specified | 1 |
| Towson University | Foreign | 2 |
| Trace College - City Of Makati, Fourth District | Private | 1 |
| Trace College-Los Baños, Laguna | Private | 2 |
| Tribhuwan University | Not Specified | 1 |
| Tribhuwan University Trichandra College, Nepal | Not Specified | 1 |
| Trinity College Dublin | Foreign | 1 |
| Trinity College Dublin, Ireland | Not Specified | 1 |
| Trinity University of Asia | Private | 1 |
| Trinity Western University | Not Specified | 1 |
| Tufts University | Not Specified | 1 |
| Tulane University | Foreign | 2 |
| Tulane University Of Louisiana | Not Specified | 1 |
| Tung Wah College | Foreign | 2 |
| Tuscia University | Not Specified | 1 |
| Tzuchiuniversity | Foreign | 1 |
| Türk Hava Kurumu Üniversitesi | Not Specified | 1 |
| U. N. P. G College, Padrauna, Kushinagar | Not Specified | 1 |
| U.N.P.G College, Padrauna | Foreign | 1 |
| Ubon Ratchathani Rajabhat University | Not Specified | 2 |
| Ubon Ratchathani University | Not Specified | 2 |
| Ubonratchathanee University | Not Specified | 1 |
| Ubonratchathani Nursing Collage | Not Specified | 1 |
| Ubonratchathani University | Not Specified | 1 |
| Uc Irvine | Not Specified | 1 |
| Ucla | Not Specified | 1 |
| Ucla University Of California, Los Angeles | Foreign | 1 |
| Ucsd | Not Specified | 1 |
| Udayana University | Foreign | 1 |
| Udonthani Rajabhat University | Not Specified | 1 |
| Ukzn Westville Campus | Not Specified | 1 |
| Um Digos College | Public | 2 |
| Unciano College Of Antipolo - Circumferential Road | Private | 1 |
| Unciano College, Sta. Mesa, Manila | Private | 4 |
| Union College | Not Specified | 1 |
| Union University | Private | 1 |
| United Doctors Medical Center | Private | 1 |
| United Institute Of Information Technology & Ma... | Not Specified | 1 |
| United School Of Science And Technology Colleges | Private | 3 |
| Univ. Of Southeastern Phil., Bo. Obrero, Davao | Public | 3 |
| Univeristy Of Nevada, Reno | Foreign | 1 |
| Univeristy Of Portharcort | Foreign | 1 |
| Univeristy Of The East Manila | Private | 1 |
| Universal Colleges Of Parañaque | Private | 3 |
| Universidad Central Del Ecuador | Foreign | 1 |
| Universidad De Manila, Mehan Garden Manila | Not Specified | 1 |
| Universidad De Santa Isabel | Private | 1 |
| Universidad De Sta. Isabel/Naga City | Private | 1 |
| Universitas Indonesia | Not Specified | 1 |
| Universite De Bourgogne, Dijon, France | Not Specified | 1 |
| Universite De Lubumbashi | Not Specified | 1 |
| Universiti Brunei Darussalam | Not Specified | 1 |
| University At Albany | Foreign | 1 |
| University At Buffalo, New York | Not Specified | 1 |
| University At Buffalo, The State University Of ... | Foreign | 2 |
| University Canada West | Not Specified | 1 |
| University Central Of Nicaragua | Not Specified | 1 |
| University In United States | Not Specified | 1 |
| University Of Abuja, Abuja - Nigeria | Not Specified | 1 |
| University Of Akron | Foreign | 1 |
| University Of Alberta, Canada | Foreign | 1 |
| University Of Arizona | Foreign | 3 |
| University Of Auckland | Foreign | 4 |
| University Of Auckland Auckland, New Zealand | Not Specified | 1 |
| University Of Balamand | Not Specified | 1 |
| University Of Batangas, Batangas City | Private | 2 |
| University Of Benin | Foreign | 3 |
| University Of Benin, Edo State Nigeria | Not Specified | 1 |
| University Of Bradford | Foreign | 2 |
| University Of Bradford,Uk | Foreign | 1 |
| University Of British Columbia - Vancouver Campus | Foreign | 1 |
| University Of British Columbia, Vancouver | Foreign | 1 |
| University Of Calabar | Not Specified | 4 |
| University Of Calgary | Foreign | 1 |
| University Of Calgary - Qatar | Foreign | 1 |
| University Of Calgary, Canada | Foreign | 1 |
| University Of California - San Diego | Foreign | 1 |
| University Of California - Santa Barbara | Foreign | 1 |
| University Of California At Berkeley | Foreign | 1 |
| University Of California At Davis | Foreign | 1 |
| University Of California At Irvine | Foreign | 1 |
| University Of California At Riverside | Not Specified | 1 |
| University Of California Berkeley | Foreign | 1 |
| University Of California Los Angeles | Foreign | 4 |
| University Of California Merced | Foreign | 1 |
| University Of California San Diego | Foreign | 3 |
| University Of California Santa Barbara | Foreign | 2 |
| University Of California, Davis (Usa) | Not Specified | 1 |
| University Of California, Los Angeles (Ucla) | Foreign | 1 |
| University Of California, Santa Cruz | Foreign | 3 |
| University Of California- Berkeley | Foreign | 1 |
| University Of California- Los Angeles | Foreign | 1 |
| University Of California-Merced | Foreign | 1 |
| University Of California-Riverside | Foreign | 1 |
| University Of California: Davis | Foreign | 1 |
| University Of California: Los Angeles | Foreign | 1 |
| University Of California: Riverside | Foreign | 1 |
| University Of Canberra | Foreign | 1 |
| University Of Canberra - Australia | Not Specified | 1 |
| University Of Canterbury | Not Specified | 1 |
| University Of Cape Coast | Foreign | 1 |
| University Of Chicago | Not Specified | 1 |
| University Of Chicago, Loyola | Foreign | 1 |
| University Of Cincinnati | Foreign | 1 |
| University Of Cologne | Not Specified | 1 |
| University Of Connecticut - Storrs | Not Specified | 1 |
| University Of Dayton | Not Specified | 1 |
| University Of Delaware | Not Specified | 1 |
| University Of Detroit Mercy | Not Specified | 1 |
| University Of East Anglia | Not Specified | 1 |
| University Of Essex | Not Specified | 2 |
| University Of Florida, Gainesville, Florida, Usa | Not Specified | 1 |
| University Of Georgia | Foreign | 2 |
| University Of Georgia (Ga, Usa) | Not Specified | 1 |
| University Of Georgia, U.S.A. | Foreign | 2 |
| University Of Ghana | Foreign | 4 |
| University Of Glasgow | Foreign | 1 |
| University Of Greenwich | Foreign | 2 |
| University Of Hamburg | Not Specified | 1 |
| University Of Hawaii | Foreign | 2 |
| University Of Hawaii At Hilo | Not Specified | 1 |
| University Of Hertfordshire | Not Specified | 2 |
| University Of Houston, Texas | Foreign | 1 |
| University Of Ibadan | Foreign | 4 |
| University Of Ibadan, Ibadan, Oyo State, Nigeria. | Not Specified | 1 |
| University Of Ibadan, Nigeria | Not Specified | 1 |
| University Of Illinois - Chicago | Foreign | 1 |
| University Of Illinois At Champaign-Urbana | Not Specified | 1 |
| University Of Illinois At Urbana-Champaign | Not Specified | 1 |
| University Of Iloilo, Iloilo | Private | 4 |
| University Of Ilorin | Foreign | 3 |
| University Of Immaculate Conception | Private | 1 |
| University Of Immaculate Conception Davao City | Private | 1 |
| University Of Iowa, Usa | Foreign | 1 |
| University Of Jos | Not Specified | 1 |
| University Of Kansas | Foreign | 2 |
| University Of Kashmir | Not Specified | 1 |
| University Of Kentucky | Foreign | 2 |
| University Of Kentucky - Kentucky, U.S.A. | Foreign | 1 |
| University Of Kerala | Not Specified | 1 |
| University Of Kerala,India | Not Specified | 1 |
| University Of Khartoum | Foreign | 1 |
| University Of Khartoum, Sudan | Foreign | 1 |
| University Of La Salette ( Santiago City , Isab... | Private | 1 |
| University Of La Salette (City Of Santiago, Isa... | Not Specified | 1 |
| University Of La Salette City Of Santiago, Isabela | Not Specified | 1 |
| University Of La Salette College | Not Specified | 1 |
| University Of La Salette Santiago City, Isabela | Private | 4 |
| University Of La Salette, Santiago City Isabela | Private | 1 |
| University Of La Salette, Santiago City, Isabela | Private | 1 |
| University Of La Salette- Santiago City | Private | 1 |
| University Of Leicester | Not Specified | 1 |
| University Of London | Not Specified | 1 |
| University Of Los Angeles | Not Specified | 1 |
| University Of Lubumbashi | Not Specified | 2 |
| University Of Lucknow | Foreign | 2 |
| University Of Madison Wisconsin, Usa | Foreign | 1 |
| University Of Maiduguri | Not Specified | 4 |
| University Of Maine, Orono, U.S.A. | Not Specified | 1 |
| University Of Malta | Not Specified | 1 |
| University Of Manila | Private | 1 |
| University Of Manitoba | Foreign | 1 |
| University Of Mary Washington | Foreign | 1 |
| University Of Maryland, College Park | Foreign | 4 |
| University Of Maryland, University College | Not Specified | 1 |
| University Of Massachusetts | Foreign | 1 |
| University Of Massachusetts, Amherst | Foreign | 1 |
| University Of Massachusetts, U.S.A. | Foreign | 1 |
| University Of Melbourne | Foreign | 4 |
| University Of Memphis - Memphis Usa | Foreign | 1 |
| University Of Miami - Florida, U.S.A. | Foreign | 2 |
| University Of Michigan, Ann Arbor Mi Usa | Not Specified | 1 |
| University Of Mindanao, Davao | Private | 3 |
| University Of Minnesota | Foreign | 1 |
| University Of Missouri | Foreign | 1 |
| University Of Missouri: Missouri, Usa | Not Specified | 1 |
| University Of Mysore | Not Specified | 1 |
| University Of Namibia | Not Specified | 1 |
| University Of Nebraska - Lincoln | Not Specified | 1 |
| University Of Nebraska-Omaha | Not Specified | 1 |
| University Of Nevada Las Vegas | Foreign | 3 |
| University Of Nevada Reno | Foreign | 1 |
| University Of Nevada, Reno | Foreign | 3 |
| University Of New England, Australia | Not Specified | 1 |
| University Of New South Wales | Not Specified | 2 |
| University Of New South Wales (Australia) | Not Specified | 2 |
| University Of New South Wales, Sydney, Australia | Not Specified | 1 |
| University Of Nigeria | Foreign | 2 |
| University Of Nigeria Enugu Campus | Not Specified | 1 |
| University Of Nigeria,Enugu Campus | Not Specified | 1 |
| University Of North Carolina At Chapel Hill | Not Specified | 2 |
| University Of North Carolina At Charlotte | Foreign | 1 |
| University Of North Carolina At Pembroke | Not Specified | 1 |
| University Of North Carolina Wilmington | Not Specified | 1 |
| University Of North Florida | Foreign | 4 |
| University Of Northeastern Philippines | Private | 4 |
| University Of Notre Dame | Private | 3 |
| University Of Nueva Caceres, Naga City | Private | 4 |
| University Of Oklahoma | Foreign | 2 |
| University Of Ottawa | Not Specified | 1 |
| University Of Oulu | Not Specified | 1 |
| University Of Padua | Not Specified | 2 |
| University Of Pangasinan,Dagupan City(Dagupan C... | Private | 3 |
| University Of Pangasinan-Phinma | Not Specified | 1 |
| University Of Papua New Guinea | Foreign | 1 |
| University Of Pennsylvania, Usa | Foreign | 1 |
| University Of Perpetual Help | Private | 1 |
| University Of Perpetual Help - Gma | Private | 3 |
| University Of Perpetual Help System Dalta Las P... | Not Specified | 2 |
| University Of Perpetual Help System-Dalta Las P... | Private | 1 |
| University Of Perpetual Help-Las Piñas | Not Specified | 1 |
| University Of Phayao | Foreign | 1 |
| University Of Pittsburgh | Not Specified | 3 |
| University Of Pittsburgh, Usa | Foreign | 3 |
| University Of Port Harcort Choba | Not Specified | 1 |
| University Of Port Harcourt Nigeria | Not Specified | 1 |
| University Of Port Harcourt, Rivers State, Nige... | Not Specified | 1 |
| University Of Portharcourt | Foreign | 2 |
| University Of Portharcourt,Rivers State, Nigeria. | Not Specified | 1 |
| University Of Portland | Foreign | 1 |
| University Of Pune, Pune, Maharashtra State, India | Not Specified | 1 |
| University Of Queensland | Foreign | 1 |
| University Of Queensland, Australia | Foreign | 1 |
| University Of Rajasthan | Foreign | 2 |
| University Of Regina Carmeli, Malolos, Bulacan | Private | 3 |
| University Of Rizal System - Morong, Rizal | Public | 2 |
| University Of Rizal System - Tanay | Public | 1 |
| University Of Rizal System - Taytay | Public | 1 |
| University Of Saint Louis Tuguegarao | Private | 1 |
| University Of Saint Thomas | Private | 1 |
| University Of San Agustin Iloilo | Private | 4 |
| University Of San Agustin Iloilo City | Private | 2 |
| University Of San Agustin Iloilo City, Iloilo | Private | 1 |
| University Of San Agustin, Iloilo | Private | 2 |
| University Of San Agustin, Iloilo City | Private | 4 |
| University Of San Agustin- Iloilo City | Private | 3 |
| University Of San Agustin-Iloilo | Private | 1 |
| University Of San Agustin-Iloilo City | Private | 2 |
| University Of San Agustine | Private | 1 |
| University Of San Diego | Not Specified | 3 |
| University Of San Diego, Ca, Usa | Foreign | 1 |
| University Of San Jose-Recoletos | Private | 1 |
| University Of Scranton | Foreign | 1 |
| University Of Scranton, Usa | Foreign | 1 |
| University Of Seychelles American Institute Of ... | Not Specified | 1 |
| University Of South Alabama | Not Specified | 1 |
| University Of South Carolina | Foreign | 1 |
| University Of South Florida | Foreign | 4 |
| University Of Southampton | Not Specified | 1 |
| University Of Southeastern Philippines | Public | 1 |
| University Of Southeastern Philippines - Mintal | Public | 1 |
| University Of Southern California | Foreign | 4 |
| University Of Southern California, Usa | Foreign | 3 |
| University Of Southern Indiana | Not Specified | 1 |
| University Of Southern Philippines, Davao | Private | 1 |
| University Of St Francis, Joliet | Not Specified | 1 |
| University Of St. Anthony, Iriga City | Private | 1 |
| University Of St. Thomas | Private | 2 |
| University Of Sydney | Foreign | 3 |
| University Of Sydney And Then University Of Wes... | Not Specified | 1 |
| University Of Sydney, Australia | Foreign | 2 |
| University Of Tampa (Usa) | Not Specified | 1 |
| University Of Tasmania | Not Specified | 1 |
| University Of Technology, Sydney | Foreign | 1 |
| University Of Tennessee - Knoxville | Foreign | 1 |
| University Of Texas (Dallas) | Foreign | 2 |
| University Of Texas - Austin | Not Specified | 1 |
| University Of Texas At Austin | Foreign | 1 |
| University Of Texas At Austin, Usa | Foreign | 1 |
| University Of Texas At Dallas | Not Specified | 1 |
| University Of Texas At San Antonio | Foreign | 1 |
| University Of Texas San Antonio | Foreign | 1 |
| University Of Texas-Rio Grande Valley | Foreign | 1 |
| University Of Thai Chamber Of Commerce, Thailand | Foreign | 1 |
| University Of The Cordilleras Baguio City, Benguet | Private | 1 |
| University Of The Cordilleras-Formerly Bcf | Private | 1 |
| University Of The East - Caloocan | Private | 3 |
| University Of The Free State, South Africa | Not Specified | 1 |
| University Of The Pacific, Albany, Ca, Usa | Foreign | 2 |
| University Of The Pacific, Arthur A. Dugoni Sch... | Not Specified | 1 |
| University Of The Philippines - Open University | Public | 4 |
| University Of The Philippines Cebu | Not Specified | 1 |
| University Of The Philippines College Of Nursing | Not Specified | 1 |
| University Of The Philippines-Manila | Public | 1 |
| University Of The Ryukyus | Not Specified | 1 |
| University Of The Sciences In Philadelphia | Not Specified | 1 |
| University Of The Visayas - Gullas College Ming... | Private | 1 |
| University Of The West Of England | Not Specified | 2 |
| University Of Toronto - Mississauga | Not Specified | 1 |
| University Of Toronto Scarborough | Not Specified | 1 |
| University Of Vermont | Not Specified | 1 |
| University Of Virginia | Foreign | 3 |
| University Of Warwick | Foreign | 1 |
| University Of Washington - Seattle | Foreign | 1 |
| University Of Washington Bothell | Not Specified | 1 |
| University Of Washington-Tacoma | Not Specified | 1 |
| University Of Waterloo | Not Specified | 1 |
| University Of West Florida | Foreign | 4 |
| University Of West Yangon | Not Specified | 1 |
| University Of Western Ontario | Foreign | 1 |
| University Of Western Sydney | Foreign | 2 |
| University Of Wisconsin - Madison | Foreign | 2 |
| University Of Wisconsin-Madison | Foreign | 2 |
| University Of Wolverhampton | Not Specified | 1 |
| University Of Worcester | Foreign | 1 |
| University Of Wyoming | Foreign | 1 |
| University Of York | Foreign | 1 |
| University of Baguio | Private | 1 |
| University of Northern Philippines - Main | Public | 1 |
| University of Nueva Caceres | Private | 1 |
| University of San Agustin | Private | 1 |
| University of Southeastern Philippines - Main | Public | 1 |
| University of Southern Philippines Foundation | Private | 2 |
| University of St. La Salle | Private | 1 |
| University of St. Louis - Tuguegarao | Private | 2 |
| University of The Philippines - Visayas | Public | 1 |
| University of the Immaculate Conception | Private | 1 |
| University of the Philippines - College of Cebu | Public | 1 |
| University of the Philippines - Diliman | Public | 4 |
| University of the Philippines - Los Baños | Public | 4 |
| University of the Visayas | Private | 1 |
| Universtiy Of North Dakota | Not Specified | 1 |
| Univiricity Of Northen Philippinas | Not Specified | 1 |
| Unsw Sydney | Foreign | 1 |
| Upm- School Of Health Sciences, Palo, Leyte | Public | 4 |
| Urban University, Rome | Not Specified | 1 |
| Urdaneta Community College, Pangasinan | Public | 1 |
| Urios College | Private | 1 |
| Usaim | Not Specified | 1 |
| Usman Danfodiyo University Sokoto, Nigeria | Not Specified | 1 |
| Uv Gullas - Banilad | Not Specified | 1 |
| Uv-Gullas College Of Medicine - Mandaue City, Cebu | Private | 4 |
| V B S Purvancal University | Foreign | 1 |
| V.H.Dave Homeopathic College | Foreign | 1 |
| Vaagdevi Ayurvedic Medical College | Not Specified | 1 |
| Vagdevi College Of Pharmacy | Not Specified | 1 |
| Valley View University | Not Specified | 1 |
| Vancouver Island University | Not Specified | 1 |
| Vanderbilt University | Not Specified | 1 |
| Vanmathi Matri Hr Sec School | Not Specified | 1 |
| Vasantdada Patil Ayurvedic Medical College & In... | Not Specified | 1 |
| Velammal Matric Higher Secondary School | Not Specified | 1 |
| Velammal Matric Hr Sec School | Foreign | 1 |
| Vetri Vikaas Boys Higher Secondary School | Not Specified | 1 |
| Victoria University Of Wellington | Foreign | 1 |
| Vidhyaa Vikas Hr Sec School | Not Specified | 1 |
| Vidyaa Vikas Boys Higher Secondary School | Not Specified | 1 |
| Vijayanta Model Higher Secondary School | Not Specified | 1 |
| Vikas Concept School | Not Specified | 1 |
| Vikas Junior College Vikarabad | Not Specified | 1 |
| Villanova University | Not Specified | 1 |
| Vimala College Thrissur | Not Specified | 1 |
| Vinayaka Mission Kirupananda Variyar Medical Co... | Foreign | 1 |
| Vinayaka Mission University | Foreign | 1 |
| Vinayaka Mission'S Kirupananda Variyar Medical ... | Not Specified | 1 |
| Virgen Milagrosa University Foundation | Not Specified | 1 |
| Virgen Milagrosa University Foundation And Vmu ... | Private | 1 |
| Virgin Milagrosa University Foundation | Not Specified | 3 |
| Virginia Commonwealth University, Usa | Foreign | 1 |
| Virginia Polytechnic Institute And State Univer... | Not Specified | 1 |
| Visayas University | Public | 2 |
| Vishwa Bharti Mahavidhyalaya | Not Specified | 1 |
| Vishwa Bharti Mahavidhyalaya Sikar | Not Specified | 1 |
| Vit University | Not Specified | 1 |
| Vivek Bharti Trust Pharmacy College, Junagadh | Not Specified | 1 |
| Vivekananadhd Matric Higher Secondary School Attur | Not Specified | 1 |
| Vpsv Ayurveda College Kottakkal | Not Specified | 1 |
| Wabash College | Not Specified | 1 |
| Wake Forest University | Not Specified | 1 |
| Walailak University | Foreign | 4 |
| Waseda University | Not Specified | 1 |
| Waseem Turki Muslim Degree College Fatehpur Maf... | Not Specified | 1 |
| Washington State University | Foreign | 3 |
| Washington State University - Vancouver, Wa | Not Specified | 1 |
| Washington State University Vancouver | Not Specified | 1 |
| Webster University | Foreign | 2 |
| Webster University, Saint Louis, Mo, Usa | Not Specified | 1 |
| Wesleyan College Of Manila | Private | 1 |
| Wesleyan University, Middletown, Ct | Not Specified | 1 |
| Wesleyan University-Philippines | Not Specified | 1 |
| West Bay College | Private | 1 |
| West Virginia University | Not Specified | 1 |
| West Virginia Wesleyan College | Foreign | 1 |
| Western Governors University | Not Specified | 1 |
| Western Institute Of Technology | Private | 1 |
| Western Institute Of Technology, La Paz, Iloilo | Private | 1 |
| Western Leyte College Of Ormoc City, Inc. | Private | 1 |
| Western Mindanao Cooperative College | Private | 1 |
| Western Ontario | Not Specified | 1 |
| Western Philippines University - Puerto Princesa | Public | 1 |
| Western University | Foreign | 2 |
| Wheaton College | Not Specified | 1 |
| Whitireia Polytechnic New Zealand | Not Specified | 1 |
| Wichita State University | Not Specified | 1 |
| Wilkes University | Not Specified | 2 |
| William Carey University | Foreign | 1 |
| William Carey University Meghalaya | Foreign | 1 |
| William Carey University, Meghalaya | Foreign | 1 |
| William Paterson University | Foreign | 1 |
| Windsor University | Foreign | 1 |
| Windsor University School Of Medicine | Not Specified | 1 |
| Windsor University School Of Medicne | Not Specified | 1 |
| Winona State University | Foreign | 3 |
| Wongkwang /University /Korea | Not Specified | 1 |
| World Citi Colleges - Antipolo | Private | 2 |
| World Classical Tamil University | Foreign | 1 |
| Xavier | Not Specified | 1 |
| Xavier University Ateneo De Cagayan | Private | 1 |
| Xavier University School Of Medicine | Not Specified | 1 |
| Xavier University, San Francisco | Not Specified | 1 |
| Xavier University-Ateneo De Cagayan | Private | 1 |
| Yashoda College Of Nursing | Foreign | 1 |
| Yashoda College Of Nursing Hyderabad | Foreign | 1 |
| Yenepoya University | Not Specified | 1 |
| York University, Canada | Foreign | 3 |
| Yuan Pei Institute Of Medical Technology, Taiwan | Foreign | 1 |
| Zamboanga Agricultural Engineering College | Private | 1 |
| Zamboanga State College Of Marine Sciences And ... | Public | 1 |
| Zaparozhy State Medical University | Foreign | 1 |
| Zhejiang University | Not Specified | 1 |

### Data Quality Notes

- **HEI column used:** `NMA_College`
- **Examinee count:** best record per person (IS_BEST_NMAT_RECORD == True)
- **Total unique HEIs:** 2856
- **HEIs with >=5 examinees:** 669
- **HEIs with <5 examinees (flagged):** 2187
- HEI names are as recorded in `NMA_College`. Name variations across years are not normalized.


> **Data Caveats:**
> 1. NMAT-to-PLE linkage rates measure the share of NMAT examinees later found in PLE passer records — NOT the PLE pass rate. Our dataset contains only PLE passers; PLE failers are not available.
> 2. Foreign examinee counts represent NMAT test-takers, not enrolled students. The 10-slot SUC cap applies to enrollment, not examinee volume.
> 3. NMAT data covers 2006–2018 only. CMO No. __, s. 2026 takes effect AY 2026-2027 — there is an 8-year data gap.
> 4. "Observable cohort" = NMAT examinees from Year ≤ 2014 who have had sufficient time to take and pass PLE.
> 5. Person-level analysis uses the best NMAT record per individual (IS_BEST_NMAT_RECORD == True).


> **Observable Cohort Caveat:** PLE linkage rates are computed using best NMAT records with Year ≤ 2014
> (the "pre-2015 cohort"). Examinees from Year > 2014 may not have had time to take PLE yet.
> The linkage rate underestimates for recent years because PLE typically occurs 5+ years after NMAT.

