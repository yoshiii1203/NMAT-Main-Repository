# NMAT R Shiny Dashboard

## Quick start

```r
# 1. Install packages (run once)
source("setup.R")

# 2. Launch the app
shiny::runApp("app.R")
```

The app auto-detects `NMAT_Ultima.parquet` by trying these paths in order:

```
../../dataset/NMAT_Ultima.parquet   ← correct if you keep the folder structure
../dataset/NMAT_Ultima.parquet
dataset/NMAT_Ultima.parquet
NMAT_Ultima.parquet
```

No path changes needed if your folder layout matches the original project tree.

---

## What's covered (all 12 pages from the Streamlit dashboard)

| Page | Content |
|---|---|
| 🏠 Executive Summary | Key metrics, annual trend chart, composition pies, summary table |
| 🧪 Data Integrity | Cohort sizes, raw-score validation, UNI_TYPE/course/PLE distributions |
| 📈 Trends & Stability | Annual score trends, boxplots by year, Kruskal-Wallis test |
| 📊 Deciles & Background | Decile heatmaps & stacked bars by year, university type, course group |
| 🏫 University Type | Type × location matrix, decile distribution, foreign summary, uni listings |
| 🔄 Flow & Pathways | Sankey diagrams: uni→decile, course→decile, decile→PLE |
| 🎯 PLE Alignment | Score profiles, Mann-Whitney effect sizes, **decile→PLE pass-rate bar chart**, policy tables |
| 🔁 Repeat Takers | Attempt counts, improvement stats, first vs last scatter |
| 🧠 Subtests & Profiles | Subtest heatmaps (std + raw) by uni type & course, radar charts |
| ⏰ Year Gap & Gender | Year-gap histogram & boxplot, sex composition, PLE by sex |
| 📐 Statistical Tests | KW by year, Mann-Whitney by PLE status, chi-square, Dunn post-hoc |
| 📋 Policy Tables & Export | Downloadable tables (year/course/uni) + **one-click Excel workbook** |

---

## Key advantage over Streamlit: export buttons are built in

Every table automatically shows **Copy / CSV / Excel / Print** buttons (via the DT package).  
The Policy Tables page also adds a one-click **Excel workbook** with all four policy tables as separate sheets — no manual download handling needed.

---

## Optional packages

| Package | Purpose |
|---|---|
| `dunn.test` | Post-hoc Dunn test on Page 11. If not installed, the tab shows an install prompt instead of crashing. |
| `openxlsx` | Excel workbook on Page 12. Same graceful fallback if missing. |

---

## Global sidebar filters

- **Year** — multi-select (default: all years)
- **Course group** — multi-select (default: all)
- **Sex** — multi-select (default: all)

Filters apply to all pages simultaneously. PLE-linked pages (🎯 PLE Alignment) always use the observable cohort (NMAT year ≤ 2014) regardless of the year filter, consistent with the original analysis.
