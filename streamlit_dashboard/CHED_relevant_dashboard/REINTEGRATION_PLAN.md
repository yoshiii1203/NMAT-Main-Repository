# CHED Dashboard Reintegration Plan

## What the CHED Dashboard Is Missing from the Original 13-Page Dashboard

**Date:** 2026-07-27  
**Source:** `dashboard.py` (3,207 lines, 13 pages + CHED page 13)

---

## Introduction

The CHED dashboard scaffold focused purely on CMO-specific metrics but omitted the **foundational context** that makes the original dashboard valuable. CHED stakeholders need to see the full picture: who takes the NMAT, how they perform, what their backgrounds are, and how all of this connects to PLE outcomes. The CMO-specific metrics (cut-off scenarios, foreign counts) only make sense WITHIN this broader context.

Below is a page-by-page audit of what exists in the original dashboard vs what the CHED dashboard is missing, with recommendations for what to reintegrate.

---

## Page 1: Executive Summary — ⚠️ CRITICALLY MISSING

The CHED dashboard has **NO executive summary tab**. The original has:

| Element | Original has? | CHED has? | Must add? |
|---------|:-------------:|:---------:|:---------:|
| Metric cards: total examinees, years, median scores | ✅ | ✅ (partial) | ✅ Add unique examinees, repeat takers, observable cohort size |
| Course group composition pie chart | ✅ | ❌ | ✅ **Add** — shows pre-med background diversity |
| University type composition pie chart | ✅ | ❌ | ✅ **Add** — shows SUC vs PHEI split (directly relevant to CHED) |
| Executive summary indicators table | ✅ | ❌ | ✅ **Add** — one-table summary of all key numbers |
| Repeat takers count | ✅ | ❌ | ✅ **Add** — 25% of examinees take NMAT multiple times |
| Observable cohort size & PLE linkage rate | ✅ | ✅ | Already present |

**Relevance to CHED:** The very first thing a policymaker asks: "What's the big picture? How many students, what types of schools, what courses?" The pie charts showing 76.89% Private vs 20.65% Public immediately establish context for why the CMO's SUC/PHEI distinction matters.

---

## Page 2: Data Integrity — 🟡 OPTIONAL

| Element | Original has? | CHED has? | Must add? |
|---------|:-------------:|:---------:|:---------:|
| Cohort definitions table | ✅ | ❌ | ✅ **Add as appendix** — stakeholders need to trust the data |
| Raw score validation | ✅ | ❌ | ❌ Too technical for CHED audience |
| University type consistency | ✅ | ❌ | ❌ Internal audit detail |

**Relevance to CHED:** Low for the main dashboard, but a simplified "How the data was built" section should exist somewhere (Tab 9).

---

## Page 3: Trends & Stability — 🟡 PARTIALLY COVERED

| Element | Original has? | CHED has? | Must add? |
|---------|:-------------:|:---------:|:---------:|
| Yearly median score trend line chart | ✅ | ✅ | Already covered by 07_temporal_trends.py |
| Boxplots by year (raw, percentile, Part I, Part II) | ✅ | ❌ | ❌ Too detailed for CHED |
| Kruskal-Wallis year-to-year stability test | ✅ | ❌ | ❌ Technical detail for analysts, not policymakers |

**Relevance to CHED:** The yearly trend chart is sufficient. The statistical tests are too technical.

---

## Page 4: Score Bins & Background — 🔴 HIGH VALUE, MOSTLY MISSING

| Element | Original has? | CHED has? | Must add? |
|---------|:-------------:|:---------:|:---------:|
| Bin distribution heatmap by year | ✅ | ❌ | ✅ **Add** — visual of how scores shifted over time |
| Top B8-B10 vs bottom B1-B3 share by year | ✅ | ❌ | ✅ **Add** — shows performance polarization trend |
| Bin distribution by university type | ✅ | ❌ | ✅ **Add** — shows Public vs Private score gap |
| Chi-square: UNI_TYPE vs bin | ✅ | ❌ | ❌ Technical |
| **Citizenship profile section** | ✅ | ❌ | ✅ **CRITICAL — FOREIGN STUDENT CONTEXT** |
| Foreigners vs Filipinos comparative analysis | ✅ | ❌ | ✅ **CRITICAL** — performance comparison, bin heatmaps |
| Record listings by university type | ✅ | ❌ | ❌ Too granular |
| Citizenship summary by UNI_TYPE, course, year | ✅ | ❌ | ✅ **Add summary tables** |

**The citizenship section is the most CRITICAL missing piece.** The original dashboard has a full citizenship profile section with:
- Pie: citizenship composition
- Pie: Foreigners vs Filipinos
- Top 15 citizenship groups bar chart
- Bin composition by citizenship
- Heatmap: bin x citizenship
- Top-bin share by citizenship
- Box plots: percentile rank by citizenship
- Box plots: TRUE raw score by citizenship
- Summary tables by citizenship x UNI_TYPE, course, year
- **Comparative analysis** of foreigners vs Filipinos with full bin heatmaps

This is EXACTLY what CHED needs for the foreign student section of the CMO.

---

## Page 5: University Type Analysis — 🟡 PARTIALLY COVERED

| Element | Original has? | CHED has? | Must add? |
|---------|:-------------:|:---------:|:---------:|
| Type x location matrix | ✅ | ❌ | ❌ Low priority |
| Foreign examinee summary | ✅ | ❌ | ✅ **Add** — our CHED script covers this separately |
| Medical vs other courses by type | ✅ | ❌ | ❌ Niche |
| University listings | ✅ | ✅ | Covered by per-HEI analysis |

---

## Page 6: Flow & Pathways — 🔴 HIGH VALUE, MISSING

| Element | Original has? | CHED has? | Must add? |
|---------|:-------------:|:---------:|:---------:|
| Sankey: UNI_TYPE → Bin | ✅ | ❌ | ❌ Sankey is complex; key data points can be table-only |
| Sankey: CourseGroup → Bin | ✅ | ❌ | ❌ |
| Sankey: Bin → PLE status | ✅ | ❌ | ✅ **Add simplified version** — shows how bin predicts PLE linkage |
| Top pathways to B8-B10 | ✅ | ❌ | ❌ Niche |

**Relevance to CHED:** The Bin → PLE status flow is directly relevant. A simple table showing "what % of B4 examinees vs B5 examinees have PLE linkage" supports the cut-off decision. The Sankey itself is optional; the data table is what matters.

---

## Page 7: PLE Alignment — 🔴 HIGH VALUE, PARTIALLY COVERED

| Element | Original has? | CHED has? | Must add? |
|---------|:-------------:|:---------:|:---------:|
| Score profile by PLE status (descriptive stats) | ✅ | ❌ | ✅ **Add** — shows how passers differ from non-passers |
| Box plot: TRUE raw by PLE status | ✅ | ❌ | ✅ **Add** — powerful visual |
| Mann-Whitney test results | ✅ | ❌ | ❌ Technical |
| Bin distribution by PLE status | ✅ | ❌ | ✅ **Add** — our 06 script does this |
| Survival to top bins by course | ✅ | ❌ | ✅ **Add** — which courses produce top performers? |
| PLE status by decile stacked bar | ✅ | ❌ | ✅ **Add** — visual of linkage rate by bin |

---

## Page 8: Repeat Takers — 🟡 NICE TO HAVE

| Element | Original has? | CHED has? | Must add? |
|---------|:-------------:|:---------:|:---------:|
| Attempt count distribution | ✅ | ❌ | ✅ **Add simple metric card** — 25% repeat rate is significant |
| Repeat taker improvement boxplot | ✅ | ❌ | ❌ Too detailed |

**Relevance to CHED:** Knowing that 1 in 4 examinees takes NMAT multiple times is important context for cut-off policy — a strict cut-off may disproportionately affect repeat takers.

---

## Page 9: Subtests & Profiles — 🟡 NICE TO HAVE

| Element | Original has? | CHED has? | Must add? |
|---------|:-------------:|:---------:|:---------:|
| Subtest heatmap by UNI_TYPE | ✅ | ❌ | ✅ **Add summary table** — shows which skills differ by school type |
| Subtest heatmap by CourseGroup | ✅ | ❌ | ✅ **Add summary table** |
| Radar profiles | ✅ | ❌ | ❌ Visual nice-to-have |

---

## Page 10: Year Gap & Gender — 🟡 PARTIALLY COVERED

| Element | Original has? | CHED has? | Must add? |
|---------|:-------------:|:---------:|:---------:|
| PLE year gap distribution | ✅ | ❌ | ✅ **Add metric** — median gap 6 years justifies observable cohort |
| Gender decile distribution | ✅ | ❌ | ✅ **Add** — simple metric card showing female/male split and performance |
| Gender PLE summary | ✅ | ❌ | ✅ **Add** — female vs male PLE linkage rate |
| Mann-Whitney gender test | ✅ | ❌ | ❌ Technical |

**Relevance to CHED:** Gender equity considerations in cut-off policy — if one gender is systematically disadvantaged by a cut-off, that's important to know.

---

## Page 11: Statistical Tests — ❌ OUT OF SCOPE FOR CHED

All technical tests (Kruskal-Wallis, Dunn post-hoc, Chi-square with Cramér's V). Policymakers don't need p-values.

---

## Page 12: Policy Tables — 🟡 PARTIALLY COVERED

Already covered by CHED computation scripts (01_national_benchmark, 02_cutoff_scenarios).

---

## Page 13: CHED Compliance — ✅ Already Designed

This is what the CHED computation scripts focused on. It's covered.

---

## Summary: What Must Be Added to the CHED Dashboard

### Priority 1: Critical (Must Add — Directly Supports CMO)

| Missing Element | Source Page | What to Add |
|----------------|:-----------:|-------------|
| Executive summary metric row | P1 | 8 metric cards: total, best-record, unique examinees, repeat takers, years, median score, median percentile, observable cohort |
| University type pie chart | P1 | Public vs Private vs Foreign split (76.89% Private — key context) |
| Course group pie chart | P1 | Medical & Allied (47.76%) vs Natural Sciences (30.96%) — shows applicant background |
| Citizenship composition section | P4 | Full citizenship profile: composition pie, top 15 nationalities, bin by citizenship, summary tables |
| Foreigners vs Filipinos comparison | P4 | Bin heatmaps, box plots, summary table — critical for understanding foreign applicant pool |
| PLE alignment score profiles | P7 | Descriptive stats by PLE status, box plot, bin distribution |
| Survival to top bins by course | P7 | Which course groups produce the highest performers |
| Gender metrics | P10 | Female/male split, performance comparison, PLE linkage comparison |
| PLE year gap distribution | P10 | Median gap 6 years — justifies observable cohort |
| Repeat taker rate | P8 | Simple metric card: 25% repeat rate |

### Priority 2: Important (Add If Space Allows)

| Missing Element | Source Page | What to Add |
|----------------|:-----------:|-------------|
| Bin distribution heatmap by year | P4 | Visual of score distribution shifts over time |
| Top vs bottom bin share trend | P4 | B8-B10 vs B1-B3 line chart |
| Bin distribution by UNI_TYPE | P4 | Heatmap showing Public vs Private score gap |
| Subtest profiles by UNI_TYPE | P9 | Table showing which subtests differ by school type |
| Flow: Bin → PLE status data | P6 | Table showing PLE linkage rate per bin |

### Priority 3: Appendix (Tab 9)

| Missing Element | Source Page |
|----------------|:-----------:|
| Cohort definitions table | P2 |
| Data source and pipeline overview | P2 |
| Methodology notes | Throughout |

---

## Updated Tab Structure for CHED Dashboard

### Proposed 12-Tab Structure

```
Tab 1:  Executive Summary        ← NEW (was missing)
Tab 2:  National Benchmark       ← Existing (renumbered)
Tab 3:  Cut-Off Scenarios        ← Existing
Tab 4:  Score Bins & Background  ← NEW (reintegrated from P4)
Tab 5:  Per-HEI Analysis         ← Existing (renumbered)
Tab 6:  Foreign Students         ← Existing (expanded with citizenship section)
Tab 7:  PLE Alignment            ← NEW (reintegrated from P7, expanded)
Tab 8:  Demographics             ← NEW (gender + course group + repeat takers)
Tab 9:  Subtest Profiles         ← NEW (reintegrated from P9)
Tab 10: Trends (2006-2018)       ← Existing (renumbered)
Tab 11: Data Appendix            ← Existing (expanded)
```

### Key Changes from Current Skeleton

1. **Tab 1: Executive Summary** — Top of every dashboard. Policymakers see this first. Must have:
   - 8 metric cards in 2 rows of 4
   - University type pie chart
   - Course group pie chart
   - Executive summary table with all key indicators

2. **Tab 4: Score Bins & Background** — Reintegrate from original P4:
   - Bin heatmap by year
   - Top vs bottom bin trend
   - Bin distribution by UNI_TYPE

3. **Tab 6: Foreign Students** — Expand with citizenship section from original P4:
   - Current foreign examinee counts
   - Citizenship composition pie
   - Top 15 nationalities bar
   - Foreigners vs Filipinos comparison (bin heatmaps, box plots)
   - Per-SUC foreign counts

4. **Tab 7: PLE Alignment** — Expand from original P7:
   - Score profiles by PLE status
   - Box plot comparison
   - Bin distribution by PLE status
   - Survival to top bins by course

5. **Tab 8: Demographics** — Add:
   - Gender metrics (split, performance, PLE linkage)
   - Repeat taker rate
   - Course group performance
   - PLE year gap distribution

6. **Tab 11: Data Appendix** — Expand:
   - Cohort definitions
   - How data was produced (pipeline summary)
   - Methodology notes
   - All data caveats and limitations

---

## Implementation Work

| Component | Script | Estimated Lines |
|-----------|--------|:--------------:|
| Executive Summary metrics + charts | ✏️ New: `08_executive_summary.py` | ~100 |
| Score Bins & Background heatmaps | ✏️ New: `09_score_bins_background.py` | ~150 |
| Expanded Foreign + Citizenship section | ✏️ Expand `04_foreign_analysis.py` | ~100 |
| PLE Alignment score profiles + box plots | ✏️ Expand `06_ple_alignment.py` | ~100 |
| Gender metrics + repeat takers | ✏️ New: `10_gender_repeat.py` | ~80 |
| Subtest profiles | ✏️ New: `11_subtest_profiles.py` | ~80 |
| Dashboard restructure (12 tabs) | ✏️ Rewrite `dashboard.py` tabs | ~200 |
| **Total additional** | | **~810 lines** |

---

## Conclusion

The CHED dashboard is currently underwhelming because it presents CMO-specific metrics in isolation, without the foundational context that makes them meaningful. Specifically:

1. **No executive summary** — policymakers see numbers without context
2. **No citizenship comparison** — the Foreigners vs Filipinos analysis is exactly what CHED needs
3. **No PLE alignment visualizations** — box plots and bin distributions show the story behind the numbers
4. **No gender/demographic context** — equity analysis is missing
5. **No score bin background** — the distribution of scores across years and school types sets the stage

The fix is to reintegrate ~5 key sections from the original dashboard's 13 pages into the CHED dashboard, bringing it from 9 tabs to 12 tabs, and adding approximately 810 lines of computation + visualization code.

**Next step:** Implement the 5 new computation scripts and restructure dashboard.py to 12 tabs.
