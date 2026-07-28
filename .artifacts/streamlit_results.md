NMAT Streamlit Dashboard:

# NMAT Performance Dashboard, 2006–2018

Descriptive, trend-based, and policy-oriented summaries based on the cleaned NMAT_Ultima pipeline. Person-level views use the best NMAT record per examinee where appropriate, while PLE-linked pages use the observable cohort only.  

# NMAT Dashboard

Navigate

🏠 Executive Summary

🧪 Data Integrity

📈 Trends & Stability

📊 Deciles & Background

🏫 University Type Analysis

🔄 Flow & Pathways

🎯 PLE Alignment

🔁 Repeat Takers

🧠 Subtests & Profiles

⏰ Year Gap & Gender

📐 Statistical Tests

📋 Policy Tables & Export

## 🏠 Executive Summary

High-level summary of examinee volume, score levels, composition, and observable PLE alignment using the filtered best-record cohort.

Best-record examinees

133,766

Years covered

13

Median TRUE raw score

122.0

Median percentile rank

50.0

Unique examinees

133,521

Repeat takers

33,711

Observable cohort size

64,463

Confirmed PLE share in observable cohort

45.40%

📚 **Course Group Distribution**

Course groups are sourced directly from the cleaned pipeline output (`CourseGroup`):

- **Medical & Allied**: Medical, Nursing, Pharmacy, Health-related
- **Natural Sciences**: Biology, Physics, Chemistry, Natural Sciences
- **Social & Behavioral Sciences**: Psychology, Economics, Social Sciences
- **Engineering & Technology**: Engineering, Technology fields
- **Education**: Teacher training, Education programs
- **Other**: All remaining courses

### 3 subsections

- 📊 Overview 
- 📈 Composition 
- 📋 Quick Tables

### 📊 Overview

**Figure 1. Annual NMAT score and volume profile**  
This figure combines median TRUE raw score, Part I and Part II medians, median percentile rank, and examinee count by year. Use it to see whether performance and testing volume moved together or in opposite directions over time.

![newplot (15)](./images/newplot-15-2.png)

📈 Composition

**Figure 2. Course-group composition of best-record examinees**

Values are counts of filtered best-record examinees by category.

![newplot (15)](./images/newplot-15-3.png)

**Figure 3. University-type composition of best-record examinees**

Percent shares refer to the current filtered cohort only.

![newplot (17)](./images/newplot-17.png)  

**Table 1. Executive summary indicators**

This table reports central score levels and the shares of examinees in the upper and lower deciles. Top-decile share refers to D8–D10, while bottom-decile share refers to D1–D3.


| Indicator                   | Value |
| --------------------------- | ----- |
| Median Total Raw Score      | 122   |
| Median Part I Raw Score     | 65    |
| Median Part II Raw Score    | 57    |
| Median Percentile Rank      | 50    |
| Top-decile share (D8-D10)   | 30.01 |
| Bottom-decile share (D1-D3) | 30.24 |


# 🧪 Data Integrity

### Data Integrity and Cohort Definition Checks

This page verifies whether the dashboard inputs remain aligned with the cleaned NMAT_Ultima pipeline, including cohort construction, raw-score consistency, and institutional classification fields.

All NMAT rows

178,882

Best-record rows

133,766

Rows with TRUE raw scores

178,882

Observable best-record rows

64,463

### Table 2. Analysis cohorts used in the dashboard

Each row defines one analytic subset used in later pages. Counts should be interpreted as rows, not necessarily unique persons, unless explicitly stated otherwise.

**Table 6. Distribution of university type in the filtered rows**

<table>
  <tr><th>UNI_TYPE</th><th>Count</th></tr>
  <tr><td>Private</td><td>135484</td></tr>
  <tr><td>Public</td><td>37555</td></tr>
  <tr><td>Foreign</td><td>4011</td></tr>
  <tr><td>Not Specified</td><td>1832</td></tr>
</table>

---

**Table 7. Distribution of course group in the filtered rows**

<table>
  <tr><th>CourseGroup</th><th>Count</th></tr>
  <tr><td>Medical &amp; Allied</td><td>86121</td></tr>
  <tr><td>Natural Sciences</td><td>55889</td></tr>
  <tr><td>Social &amp; Behavioral Sciences</td><td>22021</td></tr>
  <tr><td>Other</td><td>9845</td></tr>
  <tr><td>Education</td><td>4158</td></tr>
  <tr><td>Engineering &amp; Technology</td><td>848</td></tr>
</table>

---

**Table 8. Distribution of PLE status label in the filtered rows**

<table>
  <tr><th>PLE_STATUS_LABEL</th><th>Count</th></tr>
  <tr><td>No confirmed PLE match</td><td>128906</td></tr>
  <tr><td>Confirmed PLE passer</td><td>49976</td></tr>
</table>

# 📈 Trends & Stability

### Performance Trends and Year-to-Year Stability

This page summarizes how NMAT score levels and score distributions changed across test years using the filtered best-record trend cohort.

**Figure 4. Annual score trends and examinee volume**

Panels show the median TRUE raw score with interquartile range, median Part I and Part II raw scores, median percentile rank with interquartile range, and examinee count by year.

![newplot (18)](./images/newplot-18.png)

### Table 9. Kruskal-Wallis tests for year-to-year score differences


| Score              | H        | p_value | eta_squared |
| ------------------ | -------- | ------- | ----------- |
| Total Raw Score    | 5598.2   | <0.001  | 0.0418      |
| Part I Raw Score   | 5453.439 | <0.001  | 0.0407      |
| Part II Raw Score  | 5515.988 | <0.001  | 0.0412      |
| Percentile Rank    | 2235.74  | <0.001  | 0.0168      |
| GPS Standard Score | 2420.314 | <0.001  | 0.018       |


# 📊 Deciles & Background

### Decile Distribution by Year and Examinee Background

This page shows how percentile deciles are distributed across NMAT years, university type, and pre-med course background in the best-record trend cohort.

### 3 Subsections:

- By year
- University type
- Course group

### By year

Use this tab to see whether later cohorts became more concentrated in higher deciles, lower deciles, or the middle of the distribution.

**Figure 5. Percentile-decile heatmap by NMAT year**

Heatmap values are within-year percentages; D8–D10 represents the upper segment and D1–D3 represents the lower segment.

![newplot (19)](./images/newplot-19.png)

**Table 10. Count of examinees in each decile by NMAT year**

Counts are rows in the filtered best-record trend cohort. Rows show deciles (D10→D1) and columns show years.

### Percentile Decile Year-to-Year Comparison


| PercentileDecile | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 |
| ---------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **D10**          | 426  | 401  | 630  | 784  | 1166 | 849  | 1396 | 1673 | 1650 | 1262 | 1012 | 1653 | 1796 |
| **D9**           | 388  | 415  | 535  | 713  | 959  | 910  | 893  | 984  | 1143 | 1050 | 1182 | 2012 | 1805 |
| **D8**           | 363  | 365  | 467  | 656  | 815  | 925  | 783  | 860  | 1002 | 936  | 1264 | 2248 | 1774 |
| **D7**           | 357  | 358  | 462  | 630  | 733  | 846  | 775  | 769  | 943  | 1021 | 1143 | 2160 | 1789 |
| **D6**           | 365  | 302  | 508  | 710  | 798  | 890  | 837  | 740  | 991  | 1053 | 1327 | 2379 | 2188 |
| **D5**           | 352  | 363  | 479  | 672  | 836  | 1038 | 897  | 720  | 827  | 918  | 1266 | 2050 | 2145 |
| **D4**           | 368  | 404  | 467  | 725  | 753  | 1001 | 727  | 533  | 642  | 664  | 1174 | 2778 | 2228 |
| **D3**           | 350  | 364  | 392  | 682  | 716  | 821  | 721  | 564  | 706  | 664  | 915  | 2210 | 2138 |
| **D2**           | 302  | 298  | 431  | 651  | 647  | 750  | 768  | 698  | 719  | 759  | 1166 | 2844 | 2512 |
| **D1**           | 371  | 365  | 460  | 619  | 562  | 643  | 1061 | 1168 | 1362 | 1487 | 1821 | 3285 | 3462 |


**Figure 6. Decile composition within each NMAT year**

This figure shows within-year percentile-decile composition (percent). D8–D10 is the upper segment and D1–D3 the lower segment.

![newplot (20)](./images/newplot-20.png)

**Figure 7. Top-decile versus bottom-decile share by NMAT year**

This chart compares combined D8–D10 (top) versus D1–D3 (bottom) shares by year.

![newplot (21)](./images/newplot-21.png)

### University type

Insight: Compare which university types are overrepresented in higher deciles.

**Figure 8. Percentile-decile distribution by university type**

Heatmap values are within-type percentages.

![newplot (22)](./images/newplot-22.png)

### Figure 8. Percentile-decile distribution by university type


| University type | D1   | D2  | D3  | D4   | D5  | D6   | D7  | D8  | D9   | D10  |
| --------------- | ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | ---- |
| **Foreign**     | 12.6 | 8.8 | 8.9 | 10.5 | 9.2 | 10.2 | 9.5 | 9.5 | 10.4 | 10.4 |
| **Private**     | 13.0 | 9.9 | 8.9 | 9.8  | 9.9 | 10.2 | 9.3 | 9.5 | 9.6  | 9.8  |
| **Public**      | 11.9 | 8.5 | 7.6 | 8.4  | 8.6 | 9.2  | 8.8 | 9.5 | 11.0 | 16.5 |


**Figure 9. Share of examinees in D8–D10 by university type**

The bar chart highlights representation in the top three deciles (D8–D10) by university type.


| University Type | Percent in D8-D10 |
| --------------- | ----------------- |
| **Public**      | 37.0%             |
| **Foreign**     | 30.3%             |
| **Private**     | 29.0%             |


**Table 11. Chi-square test for association between university type and percentile decile**

The chi-square table tests whether decile composition differs by university type beyond random variation.


| chi2      | p_value | degrees_of_freedom | n_observations | cramers_v |
| --------- | ------- | ------------------ | -------------- | --------- |
| 1090.8872 | <0.001  | 18                 | 129348         | 0.0649    |


### Course group

Insight: Compare decile profiles across pre-med backgrounds.

**Figure 10. Percentile-decile distribution by course group**

Heatmap values are within-course-group percentages.

### Figure 10. Percentile-decile distribution by course group


| Course group                 | D1   | D2   | D3  | D4   | D5   | D6   | D7  | D8   | D9   | D10  |
| ---------------------------- | ---- | ---- | --- | ---- | ---- | ---- | --- | ---- | ---- | ---- |
| Education                    | 10.7 | 9.1  | 9.6 | 9.8  | 10.3 | 8.8  | 9.3 | 9.1  | 10.3 | 13.0 |
| Engineering & Technology     | 6.2  | 5.6  | 6.3 | 5.9  | 8.1  | 9.1  | 7.3 | 10.3 | 15.1 | 26.2 |
| Medical & Allied             | 10.9 | 10.0 | 9.4 | 10.6 | 10.9 | 11.0 | 9.6 | 9.7  | 9.1  | 8.9  |
| Natural Sciences             | 13.1 | 8.7  | 7.4 | 8.4  | 8.3  | 9.2  | 9.3 | 9.9  | 11.1 | 14.5 |
| Other                        | 10.9 | 8.6  | 8.6 | 9.6  | 9.5  | 9.4  | 9.2 | 10.2 | 12.0 | 12.1 |
| Social & Behavioral Sciences | 21.0 | 11.0 | 8.4 | 8.2  | 7.8  | 8.7  | 7.3 | 7.8  | 8.9  | 10.8 |


**Figure 11. Share of examinees in D8–D10 by course group**

The bar chart highlights representation in the top three deciles by course group.


| Course group                     | Percent in D8-D10 |
| -------------------------------- | ----------------- |
| **Engineering & Technology**     | 51.6%             |
| **Natural Sciences**             | 35.5%             |
| **Other**                        | 34.2%             |
| **Education**                    | 32.4%             |
| **Medical & Allied**             | 27.7%             |
| **Social & Behavioral Sciences** | 27.5%             |


# 🏫 University Type Analysis

### Institutional Profile: University Type and Location

This page focuses on the institutional comparison subset used in the analysis pipeline: Public, Private, and Foreign university types, with location shown as Local or International where available.

Insight: This page follows the institutional comparison subset (Public, Private, Foreign) from the analysis pipeline.

**Table 13. Institution type by location mix**

Values show counts and percentages of examinees within each institutional classification.


| UNI_TYPE | UNI_LOCATION  | Count | Percent of total |
| -------- | ------------- | ----- | ---------------- |
| Foreign  | International | 3218  | 2.49             |
| Private  | Local         | 99026 | 76.56            |
| Public   | International | 326   | 0.25             |
| Public   | Local         | 26778 | 20.7             |


### Table 14. Institution type by location matrix

**Counts (with totals)**


| UNI_TYPE | International | Local      | All        |
| -------- | ------------- | ---------- | ---------- |
| Foreign  | 3218          | 0          | 3218       |
| Private  | 0             | 99026      | 99026      |
| Public   | 326           | 26778      | 27104      |
| **All**  | **3544**      | **125804** | **129348** |


---

**Column percentages: within UNI_LOCATION**


| UNI_TYPE | International | Local |
| -------- | ------------- | ----- |
| Foreign  | 90.8          | 0     |
| Private  | 0             | 78.71 |
| Public   | 9.2           | 21.29 |


---

**Row percentages: within UNI_TYPE**


| UNI_TYPE | International | Local |
| -------- | ------------- | ----- |
| Foreign  | 100           | 0     |
| Private  | 0             | 100   |
| Public   | 1.2           | 98.8  |


**Figure 12. Percentile-decile distribution by institution type and location**

Each row in the heatmap is one institution type-location combination.


| Institution classification | D1   | D2  | D3   | D4   | D5   | D6   | D7  | D8  | D9   | D10  |
| -------------------------- | ---- | --- | ---- | ---- | ---- | ---- | --- | --- | ---- | ---- |
| Foreign (International)    | 12.6 | 8.8 | 8.9  | 10.5 | 9.2  | 10.2 | 9.5 | 9.5 | 10.4 | 10.4 |
| Private (Local)            | 13.0 | 9.9 | 8.9  | 9.8  | 9.9  | 10.2 | 9.3 | 9.5 | 9.6  | 9.8  |
| Public (International)     | 20.6 | 9.2 | 10.7 | 8.9  | 11.3 | 8.3  | 6.4 | 7.1 | 7.7  | 9.8  |
| Public (Local)             | 11.8 | 8.5 | 7.6  | 8.4  | 8.6  | 9.2  | 8.9 | 9.6 | 11.0 | 16.6 |


**Figure 13. Top-decile representation by institution type and location**

Top-decile representation refers to the combined share in D8–D10.


| Institution classification  | Percent in D8-D10 |
| --------------------------- | ----------------- |
| **Public (Local)**          | 37.1%             |
| **Foreign (International)** | 30.3%             |
| **Private (Local)**         | 29.0%             |
| **Public (International)**  | 24.6%             |


**Table 15. Decile counts by university type**

Values show counts of examinees by decile within each university type.


| UNI_TYPE    | D1    | D2   | D3   | D4   | D5   | D6    | D7   | D8   | D9   | D10  | Total students |
| ----------- | ----- | ---- | ---- | ---- | ---- | ----- | ---- | ---- | ---- | ---- | -------------- |
| **Foreign** | 405   | 284  | 286  | 337  | 296  | 329   | 305  | 306  | 335  | 335  | 3218           |
| **Private** | 12857 | 9809 | 8781 | 9759 | 9775 | 10139 | 9164 | 9445 | 9550 | 9747 | 99026          |
| **Public**  | 3218  | 2297 | 2065 | 2267 | 2339 | 2499  | 2398 | 2585 | 2973 | 4463 | 27104          |


**Table 16. Foreign examinee summary**

Foreign examinees are shown separately because they are a small but policy-relevant subgroup.

Foreign examinees

3,218

% of total

2.49%

Median percentile

51.0

Top decile %

30.33%

**Figure 16. Medical and allied versus other courses by university type**

Stacked percentages sum to 100% within each university type.


| UNI_TYPE    | Medical & Allied | Other Courses |
| ----------- | ---------------- | ------------- |
| **Foreign** | 49.35            | 50.65         |
| **Private** | 49.98            | 50.02         |
| **Public**  | 41.8             | 58.2          |


## 🔄 Flow & Pathways

### Pathways from Background to NMAT Outcome

Flow widths represent examinee counts moving from one background category to one score or outcome category under the current filters.

4 Subsections:

- University → Decile
- Course → Decile
- Decile → PLE
- Top pathways

### University → Decile

Insight: Compare how Public, Private, and Foreign flows distribute across deciles.

**Figure 17. Flow from university type to percentile decile**

Each flow width represents the count of examinees moving from university type to percentile decile.


| UNI_TYPE | PercentileDecile | count |
| -------- | ---------------- | ----- |
| Public   | D1               | 3218  |
| Public   | D2               | 2297  |
| Public   | D3               | 2065  |
| Public   | D4               | 2267  |
| Public   | D5               | 2339  |
| Public   | D6               | 2499  |
| Public   | D7               | 2398  |
| Public   | D8               | 2585  |
| Public   | D9               | 2973  |
| Public   | D10              | 4463  |
| Private  | D1               | 12857 |
| Private  | D2               | 9809  |
| Private  | D3               | 8781  |
| Private  | D4               | 9759  |
| Private  | D5               | 9775  |
| Private  | D6               | 10139 |
| Private  | D7               | 9164  |
| Private  | D8               | 9445  |
| Private  | D9               | 9550  |
| Private  | D10              | 9747  |
| Foreign  | D1               | 405   |
| Foreign  | D2               | 284   |
| Foreign  | D3               | 286   |
| Foreign  | D4               | 337   |
| Foreign  | D5               | 296   |
| Foreign  | D6               | 329   |
| Foreign  | D7               | 305   |
| Foreign  | D8               | 306   |
| Foreign  | D9               | 335   |
| Foreign  | D10              | 335   |


### Course → Decile

Insight: Compare which course groups feed higher versus lower deciles.

**Figure 18. Flow from course group to percentile decile**

Each flow width represents the count of examinees moving from course group to percentile decile.

**Table 19. Course-group to decile flow counts**

Each row in the flow table is one source-to-target pathway with its count.


| UNI_TYPE | PercentileDecile | count |
| -------- | ---------------- | ----- |
| Public   | D1               | 3218  |
| Public   | D2               | 2297  |
| Public   | D3               | 2065  |
| Public   | D4               | 2267  |
| Public   | D5               | 2339  |
| Public   | D6               | 2499  |
| Public   | D7               | 2398  |
| Public   | D8               | 2585  |
| Public   | D9               | 2973  |
| Public   | D10              | 4463  |
| Private  | D1               | 12857 |
| Private  | D2               | 9809  |
| Private  | D3               | 8781  |
| Private  | D4               | 9759  |
| Private  | D5               | 9775  |
| Private  | D6               | 10139 |
| Private  | D7               | 9164  |
| Private  | D8               | 9445  |
| Private  | D9               | 9550  |
| Private  | D10              | 9747  |
| Foreign  | D1               | 405   |
| Foreign  | D2               | 284   |
| Foreign  | D3               | 286   |
| Foreign  | D4               | 337   |
| Foreign  | D5               | 296   |
| Foreign  | D6               | 329   |
| Foreign  | D7               | 305   |
| Foreign  | D8               | 306   |
| Foreign  | D9               | 335   |
| Foreign  | D10              | 335   |


### Decile → PLE

Insight: In the observable cohort, this shows how deciles map to confirmed or unmatched PLE status.

**Figure 19. Flow from percentile decile to PLE status in the observable cohort**

Decile-to-PLE flow uses only the observable best-record cohort.

**Table 20. PLE status composition within each decile**

Decile-to-PLE flow uses only the observable best-record cohort; values are percent within each decile.


| PercentileDecile | Confirmed PLE passer | No confirmed PLE match |
| ---------------- | -------------------- | ---------------------- |
| D1               | 8.8                  | 91.2                   |
| D2               | 16.07                | 83.93                  |
| D3               | 19.21                | 80.79                  |
| D4               | 25.66                | 74.34                  |
| D5               | 46.3                 | 53.7                   |
| D6               | 51.82                | 48.18                  |
| D7               | 57.64                | 42.36                  |
| D8               | 60.44                | 39.56                  |
| D9               | 67.82                | 32.18                  |
| D10              | 76.25                | 23.75                  |


### Top pathways

Insight: These are the largest pathways into top deciles (D8-D10).

### Table 21. Largest university-type pathways into D8–D10


| UNI_TYPE | PercentileDecile | Count |
| -------- | ---------------- | ----- |
| Private  | D10              | 9747  |
| Private  | D9               | 9550  |
| Private  | D8               | 9445  |
| Public   | D10              | 4463  |
| Public   | D9               | 2973  |
| Public   | D8               | 2585  |
| Foreign  | D9               | 335   |
| Foreign  | D10              | 335   |
| Foreign  | D8               | 306   |


---

### Table 22. Largest course-group pathways into D8–D10


| CourseGroup                  | PercentileDecile | Count |
| ---------------------------- | ---------------- | ----- |
| Medical & Allied             | D8               | 6083  |
| Natural Sciences             | D10              | 5816  |
| Medical & Allied             | D9               | 5751  |
| Medical & Allied             | D10              | 5619  |
| Natural Sciences             | D9               | 4457  |
| Natural Sciences             | D8               | 3971  |
| Social & Behavioral Sciences | D10              | 1701  |
| Social & Behavioral Sciences | D9               | 1396  |
| Social & Behavioral Sciences | D8               | 1230  |
| Other                        | D10              | 949   |


## 🎯 PLE Alignment

### PLE Alignment of NMAT Performance

This page examines how NMAT performance and background characteristics relate to confirmed PLE outcomes within the observable best-record cohort only.

This page is restricted to the observable best-record cohort so later NMAT cohorts are not misclassified as non-passers before the licensure window is observable.

### 4 Subsections:

- Status profile
- Decile profile
- Background links
- Policy tables

### Status profile

**Table 23. Score profile by PLE status**

Table 23 reports count, median, mean, and interquartile range for each score measure by PLE status.

Each table compares **Confirmed PLE passers** against those with **No confirmed PLE match**.

### 1. Raw Score Distributions

These tables show the performance on the actual test items.

**Total Raw Score**


| PLE Status                 | Count  | Median | Mean   | Q1  | Q3  |
| -------------------------- | ------ | ------ | ------ | --- | --- |
| **Confirmed PLE passer**   | 29,269 | 143    | 144.76 | 125 | 164 |
| **No confirmed PLE match** | 35,194 | 112    | 115.01 | 94  | 134 |


**Part I Raw Score**


| PLE Status                 | Count  | Median | Mean  | Q1  | Q3  |
| -------------------------- | ------ | ------ | ----- | --- | --- |
| **Confirmed PLE passer**   | 29,269 | 76     | 75.75 | 66  | 86  |
| **No confirmed PLE match** | 35,194 | 61     | 61.31 | 51  | 72  |


**Part II Raw Score**


| PLE Status                 | Count  | Median | Mean  | Q1  | Q3  |
| -------------------------- | ------ | ------ | ----- | --- | --- |
| **Confirmed PLE passer**   | 29,269 | 68     | 69.02 | 57  | 80  |
| **No confirmed PLE match** | 35,194 | 51     | 53.69 | 42  | 64  |


---

### 2. Standardized Scores & Percentiles

These tables show the performance relative to the population.

**Percentile Rank (NMS_PER_num)**


| PLE Status                 | Count  | Median | Mean  | Q1  | Q3  |
| -------------------------- | ------ | ------ | ----- | --- | --- |
| **Confirmed PLE passer**   | 28,643 | 73     | 68.64 | 52  | 90  |
| **No confirmed PLE match** | 35,041 | 36     | 40.31 | 15  | 63  |


**General Performance Score (NMS_GPS)**


| PLE Status                 | Count  | Median | Mean   | Q1  | Q3  |
| -------------------------- | ------ | ------ | ------ | --- | --- |
| **Confirmed PLE passer**   | 29,269 | 564    | 569.18 | 506 | 632 |
| **No confirmed PLE match** | 35,194 | 464    | 466.71 | 398 | 533 |


---

### 3. Aptitude and Special Area Scores

**Aptitude Score (NMS_APT)**


| PLE Status                 | Count  | Median | Mean   | Q1  | Q3  |
| -------------------------- | ------ | ------ | ------ | --- | --- |
| **Confirmed PLE passer**   | 29,269 | 563    | 563.95 | 504 | 623 |
| **No confirmed PLE match** | 35,194 | 474    | 475.37 | 410 | 539 |


**Special Area Score (NMS_SA)**


| PLE Status                 | Count  | Median | Mean   | Q1  | Q3  |
| -------------------------- | ------ | ------ | ------ | --- | --- |
| **Confirmed PLE passer**   | 29,269 | 554    | 556.91 | 497 | 618 |
| **No confirmed PLE match** | 35,194 | 464    | 469.60 | 406 | 530 |


**Table 24. Mann-Whitney comparison of confirmed passers versus no confirmed match**

Table 24 compares only confirmed passers with the no-confirmed-match group and includes effect size.


| Score              | U_stat      | p_value | effect_r | Confirmed_median | NoMatch_median |
| ------------------ | ----------- | ------- | -------- | ---------------- | -------------- |
| Total Raw Score    | 794198092   | <0.001  | -0.542   | 143              | 112            |
| Part I             | 774202494   | <0.001  | -0.5032  | 76               | 61             |
| Part II            | 776289550   | <0.001  | -0.5072  | 68               | 51             |
| Percentile Rank    | 772264613   | <0.001  | -0.5389  | 73               | 36             |
| GPS Standard Score | 794239739.5 | <0.001  | -0.5421  | 564              | 464            |


### Decile profile

**Figure 21. Decile distribution by PLE status**

This chart reads within PLE status: how deciles are distributed across each PLE-status group.

**Table 25. Percent distribution of PLE status within each decile**

Values show percent distribution of PLE status within each percentile decile.


| PercentileDecile | Confirmed PLE passer | No confirmed PLE match |
| ---------------- | -------------------- | ---------------------- |
| D1               | 8.8                  | 91.2                   |
| D2               | 16.07                | 83.93                  |
| D3               | 19.21                | 80.79                  |
| D4               | 25.66                | 74.34                  |
| D5               | 46.3                 | 53.7                   |
| D6               | 51.82                | 48.18                  |
| D7               | 57.64                | 42.36                  |
| D8               | 60.44                | 39.56                  |
| D9               | 67.82                | 32.18                  |
| D10              | 76.25                | 23.75                  |


### Background links

**Table 26. Course-group representation in the top deciles**

Top-decile survival here means the share of examinees in D8–D10, not a time-to-event survival model.


| CourseGroup                  | total_examinees | top_decile_n | survival_rate_pct |
| ---------------------------- | --------------- | ------------ | ----------------- |
| Engineering & Technology     | 729             | 376          | 51.58             |
| Natural Sciences             | 40076           | 14244        | 35.54             |
| Other                        | 7876            | 2695         | 34.22             |
| Education                    | 3240            | 1050         | 32.41             |
| Medical & Allied             | 63056           | 17453        | 27.68             |
| Social & Behavioral Sciences | 15723           | 4327         | 27.52            |


**Table 27. Confirmed PLE alignment by university type in the observable cohort**

University-type policy table reports observable best records, confirmed passers, no confirmed match, and confirmed PLE share.


| UNI_TYPE    | n_observable_best_records | confirmed_ple_passers | no_confirmed_ple_match | confirmed_ple_share_pct |
| ----------- | ------------------------- | --------------------- | ---------------------- | ----------------------- |
| **Foreign** | 2117                      | 786                   | 1331                   | 37.13                   |
| **Private** | 47888                     | 21398                 | 26490                  | 44.68                   |
| **Public**  | 13627                     | 6755                  | 6872                   | 49.57                   |


### Policy tables

**Table 28. Confirmed PLE alignment by NMAT year**

These policy tables are designed for direct inclusion in narrative reporting and use only the observable best-record cohort.


| Year | n_observable_best_records | confirmed_ple_passers | no_confirmed_ple_match | confirmed_ple_share_pct |
| ---- | ------------------------- | --------------------- | ---------------------- | ----------------------- |
| 2006 | 3665                      | 2038                  | 1627                   | 55.61                   |
| 2007 | 3660                      | 1868                  | 1792                   | 51.04                   |
| 2008 | 4849                      | 2514                  | 2335                   | 51.85                   |
| 2009 | 6864                      | 3226                  | 3638                   | 47                      |
| 2010 | 8006                      | 3808                  | 4198                   | 47.56                   |
| 2011 | 8725                      | 3852                  | 4873                   | 44.15                   |
| 2012 | 9135                      | 4063                  | 5072                   | 44.48                   |
| 2013 | 9118                      | 3951                  | 5167                   | 43.33                   |
| 2014 | 10441                     | 3949                  | 6492                   | 37.82                   |


---

**Table 29. Confirmed PLE alignment by pre-med background**


| CourseGroup                  | n_observable_best_records | confirmed_ple_passers | no_confirmed_ple_match | confirmed_ple_share_pct | median_percentile_rank |
| ---------------------------- | ------------------------- | --------------------- | ---------------------- | ----------------------- | ---------------------- |
| Education                    | 2969                      | 1541                  | 1428                   | 51.9                    | 52                     |
| Other                        | 6180                      | 2853                  | 3327                   | 46.17                   | 55                     |
| Natural Sciences             | 15208                     | 6920                  | 8288                   | 45.5                    | 66                     |
| Medical & Allied             | 35420                     | 16058                 | 19362                  | 45.34                   | 49                     |
| Social & Behavioral Sciences | 4384                      | 1783                  | 2601                   | 40.67                   | 64                     |
| Engineering & Technology     | 302                       | 114                   | 188                    | 37.75                   | 71                     |


**Table 30. Confirmed PLE alignment by university type**


| UNI_TYPE    | n_observable_best_records | confirmed_ple_passers | no_confirmed_ple_match | confirmed_ple_share_pct | median_percentile_rank |
| ----------- | ------------------------- | --------------------- | ---------------------- | ----------------------- | ---------------------- |
| **Foreign** | 2117                      | 786                   | 1331                   | 37.13                   | 52                     |
| **Private** | 47888                     | 21398                 | 26490                  | 44.68                   | 52                     |
| **Public**  | 13627                     | 6755                  | 6872                   | 49.57                   | 67                     |


## 🔁 Repeat Takers

### Repeat-Taker Patterns and Score Change

This page examines how often examinees retake the NMAT and whether their last recorded attempt differs from their first recorded attempt.

**Figure 24. Distribution of NMAT attempt counts per examinee**

Each examinee is grouped by the number of unique NMAT applications linked to the same PERSON_KEY.

**Table 31. Attempt-count distribution**

Each examinee is grouped by the number of unique NMAT applications linked to the same PERSON_KEY.

### Table 31. Attempt-count distribution


| Attempts | Count  | Percent |
| -------- | ------ | ------- |
| 1        | 101115 | 75      |
| 2        | 25810  | 19.14   |
| 3        | 6046   | 4.48    |
| 4        | 1411   | 1.05    |
| 5        | 332    | 0.25    |
| 6        | 88     | 0.07    |
| 7        | 17     | 0.01    |
| 8        | 6      | 0       |
| 9        | 1      | 0       |


**Table 32. Repeat-taker trajectory summary**

This table summarizes repeat-taker counts and median changes from first to last attempt. Positive values indicate improvement.


| Indicator                    | Value |
| ---------------------------- | ----- |
| Repeat-taker persons         | 33711 |
| Analytic repeat takers       | 33700 |
| Improved percentile rank (%) | 77.65 |
| Improved raw score (%)       | 73.58 |
| Median percentile change     | 11    |
| Median raw score change      | 12    |


## 🧠 Subtests & Profiles

### Subtest Profiles by Institution and Course Background

This page compares standardized NMAT subtest profiles across university type and course group, with optional raw-score tables for reference.

## 3 subsections:

- University type
- Course group
- Radar profiles

**Figure 27. Mean standardized subtest scores by university type**

Higher values indicate stronger average standardized performance in that subtest dimension.

### Mean standardized subtest scores by university type


| University type | Verbal | Inductive | Quantitative | Perceptual | Biology | Physics | Social | Chemistry |
| --------------- | ------ | --------- | ------------ | ---------- | ------- | ------- | ------ | --------- |
| **Public**      | 494.4  | 512.0     | 516.3        | 507.2      | 510.1   | 517.4   | 501.3  | 512.5     |
| **Private**     | 484.6  | 499.9     | 498.8        | 499.4      | 489.8   | 498.0   | 490.2  | 491.5     |
| **Foreign**     | 486.6  | 511.1     | 506.5        | 493.2      | 495.3   | 507.4   | 491.2  | 494.1     |


**Table 34. Standardized subtest means by university type**

Higher values indicate stronger average standardized performance in that subtest dimension.


| UNI_TYPE    | Verbal | Inductive | Quantitative | Perceptual | Biology | Physics | Social | Chemistry |
| ----------- | ------ | --------- | ------------ | ---------- | ------- | ------- | ------ | --------- |
| **Public**  | 494.39 | 511.98    | 516.32       | 507.24     | 510.11  | 517.38  | 501.28 | 512.46    |
| **Private** | 484.55 | 499.88    | 498.82       | 499.37     | 489.78  | 497.97  | 490.17 | 491.52    |
| **Foreign** | 486.64 | 511.12    | 506.47       | 493.23     | 495.25  | 507.36  | 491.23 | 494.08    |


---

**Table 35. Raw-score subtest means by university type**

Raw-score subtest means for reference; these are not standardized scores.


| UNI_TYPE    | Verbal | Inductive | Quantitative | Perceptual | Biology | Physics | Social | Chemistry |
| ----------- | ------ | --------- | ------------ | ---------- | ------- | ------- | ------ | --------- |
| **Foreign** | 15.85  | 17.78     | 15.06        | 16.71      | 15.25   | 14.5    | 15.32  | 14.24     |
| **Private** | 15.49  | 17.24     | 14.46        | 17.12      | 14.56   | 13.7    | 15.11  | 13.82     |
| **Public**  | 16.04  | 17.85     | 15.55        | 17.6       | 15.71   | 14.78   | 15.69  | 14.99     |


### Course group

### Mean standardized subtest scores by course group


| Course group                     | Verbal | Inductive | Quantitative | Perceptual | Biology | Physics | Social | Chemistry |
| -------------------------------- | ------ | --------- | ------------ | ---------- | ------- | ------- | ------ | --------- |
| **Medical & Allied**             | 498.3  | 510.6     | 497.3        | 505.7      | 483.9   | 493.9   | 506.1  | 483.3     |
| **Natural Sciences**             | 476.5  | 499.7     | 512.3        | 503.4      | 520.5   | 516.1   | 470.8  | 518.3     |
| **Social & Behavioral Sciences** | 453.3  | 469.9     | 490.6        | 476.5      | 466.9   | 490.5   | 481.2  | 485.7     |
| **Education**                    | 500.0  | 516.7     | 509.1        | 501.2      | 489.9   | 509.6   | 506.5  | 509.3     |
| **Engineering & Technology**     | 525.1  | 540.7     | 575.5        | 519.3      | 501.1   | 570.9   | 507.6  | 547.1     |
| **Other**                        | 505.1  | 512.1     | 511.6        | 495.8      | 496.8   | 512.9   | 511.9  | 492.5     |


**Figure 28. Mean standardized subtest scores by course group**

Higher values indicate stronger average standardized performance in that subtest dimension.


| CourseGroup                      | Verbal | Inductive | Quantitative | Perceptual | Biology | Physics | Social | Chemistry |
| -------------------------------- | ------ | --------- | ------------ | ---------- | ------- | ------- | ------ | --------- |
| **Medical & Allied**             | 498.3  | 510.64    | 497.3        | 505.66     | 483.95  | 493.85  | 506.05 | 483.3     |
| **Natural Sciences**             | 476.48 | 499.69    | 512.29       | 503.38     | 520.46  | 516.07  | 470.79 | 518.28    |
| **Social & Behavioral Sciences** | 453.29 | 469.91    | 490.62       | 476.53     | 466.89  | 490.48  | 481.22 | 485.72    |
| **Education**                    | 500    | 516.71    | 509.08       | 501.18     | 489.89  | 509.57  | 506.49 | 509.28    |
| **Engineering & Technology**     | 525.14 | 540.71    | 575.47       | 519.32     | 501.14  | 570.94  | 507.58 | 547.06    |
| **Other**                        | 505.15 | 512.11    | 511.56       | 495.79     | 496.79  | 512.89  | 511.94 | 492.49    |


---

**Table 37. Raw-score subtest means by course group**

Raw-score subtest means for reference; these are not standardized scores.


| CourseGroup                      | Verbal | Inductive | Quantitative | Perceptual | Biology | Physics | Social | Chemistry |
| -------------------------------- | ------ | --------- | ------------ | ---------- | ------- | ------- | ------ | --------- |
| **Education**                    | 16.92  | 18.46     | 15.53        | 17.08      | 16.23   | 15.5    | 16.49  | 15.57     |
| **Engineering & Technology**     | 17.37  | 19.11     | 19.17        | 18.29      | 15.05   | 17.6    | 15.81  | 16.93     |
| **Medical & Allied**             | 16.06  | 17.83     | 14.33        | 17.39      | 14.09   | 13.43   | 15.83  | 13.32     |
| **Natural Sciences**             | 15.1   | 17.12     | 15.25        | 17.43      | 16.11   | 14.59   | 14.16  | 15.26     |
| **Other**                        | 17.01  | 18.06     | 15.6         | 16.97      | 16.14   | 15.28   | 16.57  | 14.48     |
| **Social & Behavioral Sciences** | 14.15  | 15.66     | 13.99        | 16.01      | 13.44   | 13.18   | 14.67  | 13.41     |


**Figure 29. Standardized subtest radar profile by university type**

Radar shapes are descriptive profiles and should be read together with the mean-value tables.

**Figure 30. Standardized subtest radar profile by course group**

Radar shapes are descriptive profiles and should be read together with the mean-value tables.

### Table 38. Radar-profile values by university type


| UNI_TYPE    | Verbal | Inductive | Quantitative | Perceptual | Biology | Physics | Social | Chemistry |
| ----------- | ------ | --------- | ------------ | ---------- | ------- | ------- | ------ | --------- |
| **Foreign** | 486.64 | 511.12    | 506.47       | 493.23     | 495.25  | 507.36  | 491.23 | 494.08    |
| **Private** | 484.55 | 499.88    | 498.82       | 499.37     | 489.78  | 497.97  | 490.17 | 491.52    |
| **Public**  | 494.39 | 511.98    | 516.32       | 507.24     | 510.11  | 517.38  | 501.28 | 512.46    |


---

### Table 39. Radar-profile values by course group


| CourseGroup                      | Verbal | Inductive | Quantitative | Perceptual | Biology | Physics | Social | Chemistry |
| -------------------------------- | ------ | --------- | ------------ | ---------- | ------- | ------- | ------ | --------- |
| **Education**                    | 500    | 516.71    | 509.08       | 501.18     | 489.89  | 509.57  | 506.49 | 509.28    |
| **Engineering & Technology**     | 525.14 | 540.71    | 575.47       | 519.32     | 501.14  | 570.94  | 507.58 | 547.06    |
| **Medical & Allied**             | 498.3  | 510.64    | 497.3        | 505.66     | 483.95  | 493.85  | 506.05 | 483.3     |
| **Natural Sciences**             | 476.48 | 499.69    | 512.29       | 503.38     | 520.46  | 516.07  | 470.79 | 518.28    |
| **Other**                        | 505.15 | 512.11    | 511.56       | 495.79     | 496.79  | 512.89  | 511.94 | 492.49    |
| **Social & Behavioral Sciences** | 453.29 | 469.91    | 490.62       | 476.53     | 466.89  | 490.48  | 481.22 | 485.72    |


### ⏰ Year Gap & Gender

### PLE Year Gap and Gender Patterns

This page summarizes the time between NMAT and confirmed PLE passage, and compares sex-coded performance patterns in the filtered cohorts.

### 2 subsections:

- PLE year gap
- Gender patterns

### PLE year gap

Confirmed passers

27,241

Median year gap

6.0

Q1 year gap

6.0

Q3 year gap

7.0

**Figure 31. Distribution of NMAT-to-PLE year gap**

Only confirmed observable PLE passers with non-missing PLE_YEAR_GAP are included.

**Figure 32. PLE year gap by course group**

Only confirmed observable PLE passers with non-missing PLE_YEAR_GAP are included.

### Table 40. Year-gap summary by course group


| CourseGroup                  | confirmed_passers | median_year_gap | q25_year_gap | q75_year_gap | median_percentile |
| ---------------------------- | ----------------- | --------------- | ------------ | ------------ | ----------------- |
| Education                    | 1410              | 6               | 6            | 7            | 69                |
| Engineering & Technology     | 103               | 6               | 6            | 7            | 91                |
| Medical & Allied             | 15022             | 6               | 6            | 7            | 69                |
| Natural Sciences             | 6454              | 6               | 6            | 7            | 84                |
| Other                        | 2620              | 6               | 6            | 7            | 72                |
| Social & Behavioral Sciences | 1631              | 6               | 6            | 7            | 86                |


### Gender patterns

**Table 41. Score summary by sex**

Sex summaries use records with valid SEX_CLEAN coding only.


| SEX_CLEAN  | n     | median_raw | median_pct | median_gps |
| ---------- | ----- | ---------- | ---------- | ---------- |
| **Female** | 73970 | 122        | 50         | 500        |
| **Male**   | 59571 | 121        | 49         | 499        |


**Figure 33. Percentile-rank distribution by sex**

The boxplot shows percentile-rank spread by sex.

**Figure 34. Sex composition by NMAT year**

The stacked bar shows the within-year sex mix.

### 📐 Statistical Tests

### Statistical Test Results

This page reports non-parametric tests used to assess whether observed descriptive differences across groups are statistically detectable in the filtered data.

### 4 subsections:

- Kruskal-Wallis by year
- PLE status tests
- Chi-square tests
- Post hoc

**Table 43. Kruskal-Wallis tests for score distributions across NMAT years**

Each row reports the Kruskal-Wallis H-statistic and p-value testing whether the score distribution differs across NMAT years.


| Score                  | H        | p_value | eta_squared |
| ---------------------- | -------- | ------- | ----------- |
| **Total raw score**    | 5598.2   | <0.001  | 0.0418      |
| **Part I raw score**   | 5453.439 | <0.001  | 0.0407      |
| **Part II raw score**  | 5515.988 | <0.001  | 0.0412      |
| **Percentile rank**    | 2235.74  | <0.001  | 0.0168      |
| **GPS standard score** | 2420.314 | <0.001  | 0.018       |


### PLE status tests

**Table 44. Mann-Whitney comparisons by PLE status (observable cohort)**

Tests compare confirmed passers vs no confirmed match (and other pairings where applicable). Reported values include U and p-value.


| Score                  | U_stat      | p_value | effect_r | Confirmed_median | NoMatch_median |
| ---------------------- | ----------- | ------- | -------- | ---------------- | -------------- |
| **Total raw score**    | 794198092   | <0.001  | -0.542   | 143              | 112            |
| **Part I raw score**   | 774202494   | <0.001  | -0.5032  | 76               | 61             |
| **Part II raw score**  | 776289550   | <0.001  | -0.5072  | 68               | 51             |
| **Percentile rank**    | 772264613   | <0.001  | -0.5389  | 73               | 36             |
| **GPS standard score** | 794239739.5 | <0.001  | -0.5421  | 564              | 464            |


### Chi-square tests

**Table 45. Observed counts by university type and percentile decile**

Cell counts of examinees by university type (rows) and percentile decile (columns).


| UNI_TYPE    | D1    | D2   | D3   | D4   | D5   | D6    | D7   | D8   | D9   | D10  |
| ----------- | ----- | ---- | ---- | ---- | ---- | ----- | ---- | ---- | ---- | ---- |
| **Foreign** | 405   | 284  | 286  | 337  | 296  | 329   | 305  | 306  | 335  | 335  |
| **Private** | 12857 | 9809 | 8781 | 9759 | 9775 | 10139 | 9164 | 9445 | 9550 | 9747 |
| **Public**  | 3218  | 2297 | 2065 | 2267 | 2339 | 2499  | 2398 | 2585 | 2973 | 4463 |


**Table 46. Chi-square summary (university type × decile)**

Chi-square statistic, degrees of freedom, and p-value testing independence between university type and decile.


| chi2      | p_value | degrees_of_freedom | n_observations | cramers_v |
| --------- | ------- | ------------------ | -------------- | --------- |
| 1090.8872 | <0.001  | 18                 | 129348         | 0.0649    |


**Figure 35. University type × decile row percentages**

Heatmap shows row-wise percent distribution (percent of each university type located in each decile).


| University type | D1   | D2  | D3  | D4   | D5  | D6   | D7  | D8  | D9   | D10  |
| --------------- | ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | ---- |
| **Foreign**     | 12.6 | 8.8 | 8.9 | 10.5 | 9.2 | 10.2 | 9.5 | 9.5 | 10.4 | 10.4 |
| **Private**     | 13.0 | 9.9 | 8.9 | 9.8  | 9.9 | 10.2 | 9.3 | 9.5 | 9.6  | 9.8  |
| **Public**      | 11.9 | 8.5 | 7.6 | 8.4  | 8.6 | 9.2  | 8.8 | 9.5 | 11.0 | 16.5 |


**Table 47. Expected counts**

Expected cell counts under the null hypothesis of independence between university type and decile.


| UNI_TYPE    | D1         | D2        | D3        | D4        | D5        | D6        | D7        | D8        | D9        | D10        |
| ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------- |
| **Foreign** | 409.9997   | 308.2461  | 276.9488  | 307.5744  | 308.7437  | 322.6011  | 295.2346  | 306.9027  | 319.8893  | 361.8596   |
| **Private** | 12616.7276 | 9485.513  | 8522.4157 | 9464.8424 | 9500.8246 | 9927.2516 | 9085.1157 | 9444.1718 | 9843.8036 | 11135.3339 |
| **Public**  | 3453.2727  | 2596.2408 | 2332.6354 | 2590.5832 | 2600.4317 | 2717.1473 | 2486.6497 | 2584.9255 | 2694.3071 | 3047.8065  |


### Post hoc

**Figure 36. Dunn post-hoc adjusted p-value matrix (percentile rank by year)**

Bonferroni-adjusted p-values from pairwise Dunn tests; cells < 0.05 indicate significant pairwise differences.

| Year | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **2006** | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.002 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| **2007** | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.004 | 0.000 | 0.000 | 0.000 |
| **2008** | 1.000 | 1.000 | 1.000 | 0.862 | 0.000 | 1.000 | 1.000 | 0.172 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| **2009** | 1.000 | 1.000 | 0.862 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 0.261 | 0.001 | 0.000 | 0.000 | 0.000 |
| **2010** | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| **2011** | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| **2012** | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| **2013** | 0.002 | 0.000 | 0.172 | 0.000 | 1.000 | 0.000 | 0.000 | 1.000 | 0.007 | 0.000 | 0.000 | 0.000 | 0.000 |
| **2014** | 1.000 | 1.000 | 1.000 | 0.261 | 0.000 | 1.000 | 1.000 | 0.007 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| **2015** | 0.000 | 0.004 | 0.000 | 0.001 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 |
| **2016** | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| **2017** | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.041 |
| **2018** | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.041 | 1.000 |

**Table 48. Dunn post-hoc adjusted p-values**   

| Year | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **2006** | 1 | 1 | 1 | 1 | 2.23E-06 | 1 | 1 | 0.00175 | 1 | 0.00044 | 3.37E-18 | 1.43E-35 | 5.42E-46 |
| **2007** | 1 | 1 | 1 | 1 | 1.60E-07 | 1 | 1 | 0.00021 | 1 | 0.00360 | 2.54E-16 | 8.59E-33 | 7.70E-43 |
| **2008** | 1 | 1 | 1 | 0.86198 | 0.00049 | 1 | 1 | 0.17199 | 1 | 2.09E-09 | 8.54E-31 | 1.64E-57 | 4.76E-72 |
| **2009** | 1 | 1 | 0.86198 | 1 | 2.34E-13 | 1 | 1 | 1.52E-08 | 0.26090 | 0.00089 | 1.11E-22 | 2.43E-50 | 4.35E-66 |
| **2010** | 2.23E-06 | 1.60E-07 | 0.00049 | 2.34E-13 | 1 | 2.64E-10 | 3.79E-08 | 1 | 1.34E-06 | 2.03E-38 | 1.46E-85 | 2.80E-149 | 7.77E-176 |
| **2011** | 1 | 1 | 1 | 1 | 2.64E-10 | 1 | 1 | 7.96E-06 | 1 | 4.31E-08 | 1.91E-34 | 1.28E-73 | 7.56E-94 |
| **2012** | 1 | 1 | 1 | 1 | 3.79E-08 | 1 | 1 | 0.00041 | 1 | 1.08E-10 | 4.81E-40 | 2.80E-83 | 8.16E-105 |
| **2013** | 0.00175 | 0.00021 | 0.17199 | 1.52E-08 | 1 | 7.96E-06 | 0.00041 | 1 | 0.00742 | 4.10E-30 | 3.53E-74 | 6.57E-136 | 2.48E-162 |
| **2014** | 1 | 1 | 1 | 0.26090 | 1.34E-06 | 1 | 1 | 0.00742 | 1 | 2.26E-14 | 7.14E-49 | 6.53E-101 | 2.27E-125 |
| **2015** | 0.00044 | 0.00360 | 2.09E-09 | 0.00089 | 2.03E-38 | 4.31E-08 | 1.08E-10 | 4.10E-30 | 2.26E-14 | 1 | 1.28E-08 | 2.01E-30 | 3.54E-45 |
| **2016** | 3.37E-18 | 2.54E-16 | 8.54E-31 | 1.11E-22 | 1.46E-85 | 1.91E-34 | 4.81E-40 | 3.53E-74 | 7.14E-49 | 1.28E-08 | 1 | 5.30E-05 | 4.79E-13 |
| **2017** | 1.43E-35 | 8.59E-33 | 1.64E-57 | 2.43E-50 | 2.80E-149 | 1.28E-73 | 2.80E-83 | 6.57E-136 | 6.53E-101 | 2.01E-30 | 5.30E-05 | 1 | 0.04068 |
| **2018** | 5.42E-46 | 7.70E-43 | 4.76E-72 | 4.35E-66 | 7.77E-176 | 7.56E-94 | 8.16E-105 | 2.48E-162 | 2.27E-125 | 3.54E-45 | 4.79E-13 | 0.04068 | 1 |