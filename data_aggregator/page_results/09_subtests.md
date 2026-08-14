# Page 9: Page 09: Subtest Profiles

**Generated:** 2026-08-14 16:53

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `uni (UNDERGRAD_UNI_TYPE) / besttrend (UNDERGRAD_COURSE_GROUP, desc)`

**Filters:** None (full unfiltered dataset)

---

## 1. Subtest Standard Score Means by UNDERGRAD_UNI_TYPE

**Table 34. Standardized subtest means by university type**

| UNDERGRAD_UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:---------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Public               |    495.8 |       513.2 |         517.49 |       507.63 |    511.66 |    519.09 |   502.65 |      514.03 |
| Private              |   484.74 |      500.32 |         498.91 |       498.96 |    489.61 |    498.09 |   490.48 |       491.4 |
| Foreign              |   478.75 |      505.58 |         512.25 |       489.33 |     499.4 |     512.8 |    479.1 |      506.07 |

---

## 2. Subtest Raw Score Means by UNDERGRAD_UNI_TYPE

**Table 35. Raw-score subtest means by university type**

| UNDERGRAD_UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:---------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Public               |    16.13 |       17.91 |          15.63 |        17.64 |     15.82 |     14.88 |    15.77 |       15.09 |
| Private              |    15.51 |       17.26 |          14.48 |        17.11 |     14.58 |     13.72 |    15.13 |       13.83 |
| Foreign              |    15.49 |       17.48 |          15.42 |        16.68 |     15.45 |      14.8 |    14.84 |       14.89 |

---

## 3. Subtest Standard Score Means by UNDERGRAD_COURSE_GROUP

**Table 36. Standardized subtest means by course group**

| UNDERGRAD_COURSE_GROUP       |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Medical & Allied             |   498.46 |       510.9 |          497.6 |       505.36 |    484.13 |    494.33 |   506.32 |       483.7 |
| Natural Sciences             |   476.56 |       499.9 |         512.44 |       503.34 |    520.45 |    516.25 |   470.86 |      518.52 |
| Social & Behavioral Sciences |   453.52 |      470.05 |         490.79 |       476.44 |    467.09 |    490.76 |   481.38 |      485.91 |
| Education                    |   500.96 |      518.45 |         510.34 |       499.99 |    490.88 |    510.64 |   506.49 |       511.1 |
| Engineering & Technology     |   525.24 |      540.96 |          575.6 |       519.32 |    501.23 |    570.89 |   507.64 |      547.23 |
| Other                        |   506.04 |      513.34 |         512.03 |       495.29 |    497.67 |    513.47 |   512.96 |      493.01 |

---

## 4. Subtest Raw Score Means by UNDERGRAD_COURSE_GROUP

**Table 37. Raw-score subtest means by course group**

| UNDERGRAD_COURSE_GROUP       |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Medical & Allied             |    16.08 |       17.84 |          14.36 |        17.38 |     14.11 |     13.46 |    15.84 |       13.35 |
| Natural Sciences             |     15.1 |       17.13 |          15.26 |        17.43 |     16.11 |      14.6 |    14.17 |       15.28 |
| Social & Behavioral Sciences |    14.17 |       15.66 |             14 |           16 |     13.46 |      13.2 |    14.68 |       13.43 |
| Education                    |    16.99 |       18.59 |          15.63 |         17.1 |     16.35 |      15.6 |    16.54 |        15.7 |
| Engineering & Technology     |    17.38 |       19.12 |          19.18 |        18.29 |     15.05 |      17.6 |    15.81 |       16.94 |
| Other                        |    17.08 |       18.15 |          15.64 |           17 |     16.26 |     15.37 |    16.67 |       14.55 |

---

## 5. Radar Profile Data (Raw Standardized Subtest Means)

*These are the exact values plotted on the dashboard's radar chart (dashboard.py radar_for_group()) — raw standardized subtest means, NOT mean-centered. Numerically identical to Table 34 (by university type) and Table 36 (by course group); reproduced here as the radar chart's per-axis series data per the export format contract.*

### 5.1 By University Type

**Table 38. Radar-profile values (raw standardized subtest means) by university type — population: uni subset, n=133,477**

| UNDERGRAD_UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:---------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Public               |    495.8 |       513.2 |         517.49 |       507.63 |    511.66 |    519.09 |   502.65 |      514.03 |
| Private              |   484.74 |      500.32 |         498.91 |       498.96 |    489.61 |    498.09 |   490.48 |       491.4 |
| Foreign              |   478.75 |      505.58 |         512.25 |       489.33 |     499.4 |     512.8 |    479.1 |      506.07 |


### 5.2 By Course Group

**Table 39. Radar-profile values (raw standardized subtest means) by course group — population: besttrend subset, n=134,869**

| UNDERGRAD_COURSE_GROUP       |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Medical & Allied             |   498.46 |       510.9 |          497.6 |       505.36 |    484.13 |    494.33 |   506.32 |       483.7 |
| Natural Sciences             |   476.56 |       499.9 |         512.44 |       503.34 |    520.45 |    516.25 |   470.86 |      518.52 |
| Social & Behavioral Sciences |   453.52 |      470.05 |         490.79 |       476.44 |    467.09 |    490.76 |   481.38 |      485.91 |
| Education                    |   500.96 |      518.45 |         510.34 |       499.99 |    490.88 |    510.64 |   506.49 |       511.1 |
| Engineering & Technology     |   525.24 |      540.96 |          575.6 |       519.32 |    501.23 |    570.89 |   507.64 |      547.23 |
| Other                        |   506.04 |      513.34 |         512.03 |       495.29 |    497.67 |    513.47 |   512.96 |      493.01 |


### 5.3 Mean-Centered View (aggregator-only, NOT in the dashboard)

*Subtracts the overall per-subtest mean so groups can be compared on a relative scale. This is a derived view with no dashboard counterpart and no table-number collision with Table 38/39 above.*

**Table 38c. Mean-centered standardized subtest scores by university type**

| UNDERGRAD_UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:---------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Public               |     9.37 |        6.83 |           7.94 |         8.99 |     11.44 |       9.1 |    11.91 |        10.2 |
| Private              |    -1.69 |       -6.05 |         -10.64 |         0.32 |    -10.61 |     -11.9 |    -0.26 |      -12.43 |
| Foreign              |    -7.68 |       -0.79 |            2.7 |        -9.31 |     -0.82 |      2.81 |   -11.64 |        2.24 |

**Table 39c. Mean-centered standardized subtest scores by course group**

| UNDERGRAD_COURSE_GROUP       |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Medical & Allied             |        5 |        1.97 |         -18.87 |          5.4 |     -9.45 |    -21.73 |     8.71 |      -22.88 |
| Natural Sciences             |    -16.9 |       -9.03 |          -4.03 |         3.38 |     26.88 |      0.19 |   -26.75 |       11.94 |
| Social & Behavioral Sciences |   -39.94 |      -38.88 |         -25.68 |       -23.52 |    -26.49 |     -25.3 |   -16.23 |      -20.67 |
| Education                    |      7.5 |        9.52 |          -6.13 |         0.03 |      -2.7 |     -5.42 |     8.88 |        4.52 |
| Engineering & Technology     |    31.78 |       32.03 |          59.13 |        19.36 |      7.65 |     54.83 |    10.03 |       40.65 |
| Other                        |    12.58 |        4.41 |          -4.44 |        -4.67 |      4.09 |     -2.59 |    15.35 |      -13.57 |

---

## 6. Full Descriptive Statistics (n, Mean, Median, Std, Min, Max)

**Table 40. Descriptive statistics for each subtest (standard and raw scores)**

| Subtest      | Type   |      n |   Mean |   Median |   Std |   Min |   Max |
|:-------------|:-------|-------:|-------:|---------:|------:|------:|------:|
| Verbal       | Raw    | 134826 |  15.64 |       16 |  5.26 |     0 |    30 |
| Inductive    | Raw    | 134826 |   17.4 |       18 |  5.84 |     0 |    30 |
| Quantitative | Raw    | 134826 |  14.73 |       14 |  6.04 |     0 |    30 |
| Perceptual   | Raw    | 134826 |   17.2 |       17 |  5.99 |     0 |    30 |
| Biology      | Raw    | 134826 |  14.84 |       15 |  5.31 |     0 |    30 |
| Physics      | Raw    | 134826 |  13.97 |       13 |  5.36 |     0 |    30 |
| Social       | Raw    | 134826 |  15.25 |       15 |  5.46 |     0 |    30 |
| Chemistry    | Raw    | 134826 |  14.11 |       13 |  5.58 |     0 |    30 |

---

