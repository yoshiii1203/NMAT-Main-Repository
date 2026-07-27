# Page 9: Page 09: Subtest Profiles

**Generated:** 2026-07-28 01:17

**Data source:** NMAT_Exodus.parquet (Pipeline 4)

**Data subset:** `uni (UNI_TYPE) / besttrend (CourseGroup, desc)`

**Filters:** None (full unfiltered dataset)

---

## 1. Subtest Standard Score Means by UNI_TYPE

**Table 34. Standardized subtest means by university type**

| UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Public     |   495.13 |       512.6 |         516.79 |       507.76 |    510.89 |    518.09 |   501.79 |      512.96 |
| Private    |   484.54 |      499.98 |         498.72 |        499.2 |    489.49 |    497.73 |   490.18 |      491.13 |
| Foreign    |   478.65 |      505.37 |         512.03 |       489.31 |    499.53 |    512.45 |   479.05 |      505.86 |

---

## 2. Subtest Raw Score Means by UNI_TYPE

**Table 35. Raw-score subtest means by university type**

| UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Public     |    16.08 |       17.88 |          15.58 |        17.63 |     15.76 |     14.82 |    15.72 |       15.02 |
| Private    |    15.49 |       17.24 |          14.46 |        17.11 |     14.56 |     13.69 |    15.11 |       13.81 |
| Foreign    |    15.48 |       17.48 |          15.41 |        16.68 |     15.46 |     14.79 |    14.85 |       14.87 |

---

## 3. Subtest Standard Score Means by CourseGroup

**Table 36. Standardized subtest means by course group**

| CourseGroup                  |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Medical & Allied             |    498.3 |      510.64 |          497.3 |       505.66 |    483.91 |    493.81 |   506.02 |      483.26 |
| Natural Sciences             |   476.48 |      499.68 |          512.3 |       503.36 |    520.39 |       516 |   470.73 |      518.21 |
| Social & Behavioral Sciences |   453.29 |       469.9 |          490.6 |       476.52 |    466.87 |    490.45 |   481.19 |      485.69 |
| Education                    |   499.92 |      516.65 |         509.01 |       501.04 |    489.29 |    508.95 |   505.87 |      508.66 |
| Engineering & Technology     |   525.14 |      540.71 |         575.47 |       519.32 |    501.14 |    570.94 |   507.58 |      547.06 |
| Other                        |   505.11 |      512.09 |         511.59 |       495.63 |    496.28 |    512.36 |    511.4 |      491.98 |

---

## 4. Subtest Raw Score Means by CourseGroup

**Table 37. Raw-score subtest means by course group**

| CourseGroup                  |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Medical & Allied             |    16.06 |       17.83 |          14.33 |        17.39 |     14.09 |     13.43 |    15.83 |       13.32 |
| Natural Sciences             |     15.1 |       17.12 |          15.25 |        17.43 |     16.11 |     14.59 |    14.16 |       15.26 |
| Social & Behavioral Sciences |    14.15 |       15.66 |          13.99 |        16.01 |     13.44 |     13.18 |    14.67 |       13.41 |
| Education                    |    16.92 |       18.46 |          15.53 |        17.08 |     16.23 |      15.5 |    16.49 |       15.57 |
| Engineering & Technology     |    17.37 |       19.11 |          19.17 |        18.29 |     15.05 |      17.6 |    15.81 |       16.93 |
| Other                        |    17.01 |       18.06 |           15.6 |        16.97 |     16.14 |     15.28 |    16.57 |       14.48 |

---

## 5. Radar Profile Data (Standard Scores Centered for Comparison)

### 5.1 By University Type

**Table 38. Radar-profile values (centered standard scores) by university type**

*Values are mean-centered within each subtest (overall mean subtracted). Negative values indicate below-average performance for that group on that subtest, positive values above-average.*

| UNI_TYPE   |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Public     |     9.02 |        6.62 |           7.61 |            9 |     10.92 |      8.67 |    11.45 |        9.64 |
| Private    |    -1.57 |          -6 |         -10.46 |         0.44 |    -10.48 |    -11.69 |    -0.16 |      -12.19 |
| Foreign    |    -7.46 |       -0.61 |           2.85 |        -9.45 |     -0.44 |      3.03 |   -11.29 |        2.54 |


### 5.2 By Course Group

**Table 39. Radar-profile values (centered standard scores) by course group**

*Values are mean-centered within each subtest (overall mean subtracted). Negative values indicate below-average performance for that group on that subtest, positive values above-average.*

| CourseGroup                  |   Verbal |   Inductive |   Quantitative |   Perceptual |   Biology |   Physics |   Social |   Chemistry |
|:-----------------------------|---------:|------------:|---------------:|-------------:|----------:|----------:|---------:|------------:|
| Medical & Allied             |     5.26 |        2.36 |         -18.74 |          5.4 |     -9.07 |    -21.61 |     8.89 |      -22.55 |
| Natural Sciences             |   -16.56 |        -8.6 |          -3.75 |          3.1 |     27.41 |      0.58 |    -26.4 |        12.4 |
| Social & Behavioral Sciences |   -39.75 |      -38.38 |         -25.44 |       -23.74 |    -26.11 |    -24.97 |   -15.94 |      -20.12 |
| Education                    |     6.88 |        8.37 |          -7.03 |         0.78 |     -3.69 |     -6.47 |     8.74 |        2.85 |
| Engineering & Technology     |     32.1 |       32.43 |          59.43 |        19.06 |      8.16 |     55.52 |    10.45 |       41.25 |
| Other                        |    12.07 |        3.81 |          -4.45 |        -4.63 |       3.3 |     -3.06 |    14.27 |      -13.83 |

---

## 6. Full Descriptive Statistics (n, Mean, Median, Std, Min, Max)

**Table 40. Descriptive statistics for each subtest (standard and raw scores)**

| Subtest      | Type   |      n |   Mean |   Median |   Std |   Min |   Max |
|:-------------|:-------|-------:|-------:|---------:|------:|------:|------:|
| Verbal       | Raw    | 133766 |  15.61 |       16 |  5.27 |     0 |    30 |
| Inductive    | Raw    | 133766 |  17.38 |       18 |  5.85 |     0 |    30 |
| Quantitative | Raw    | 133766 |   14.7 |       14 |  6.04 |     0 |    30 |
| Perceptual   | Raw    | 133766 |  17.21 |       17 |     6 |     0 |    30 |
| Biology      | Raw    | 133766 |  14.81 |       15 |  5.32 |     0 |    30 |
| Physics      | Raw    | 133766 |  13.94 |       13 |  5.36 |     0 |    30 |
| Social       | Raw    | 133766 |  15.23 |       15 |  5.47 |     0 |    30 |
| Chemistry    | Raw    | 133766 |  14.08 |       13 |  5.58 |     0 |    30 |

---

