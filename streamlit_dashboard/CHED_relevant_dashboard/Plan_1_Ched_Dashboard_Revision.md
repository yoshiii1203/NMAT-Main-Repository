# Plan 1: CHED Dashboard Revision — Evidence Quality & Policy Context

**Branch:** `ched-dashboard-revisions`
**Target file:** `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py`
**Status:** Plan — not yet implemented

---

## Clarifying Questions (before implementing)

1. **"Rename 'percentile' to 'bins'"** — does this mean replace every UI occurrence of the word "percentile"? e.g.
   - "Median percentile rank" → "Median bin rank"? (awkward for metric cards)
   - "Percentile Bin" labels → just "Bin"?
   - Or only in contexts like "30th percentile cut-off" → "Bin 4 cut-off"?
   
   *My recommendation: Keep "percentile" for metric cards and cut-off references (policy language uses "40th percentile"), but use "bin" for all distribution/chart labels. This avoids confusion with the CMO's text.*

2. **CLAIM: "matching process (in Pipeline 2) is not strongly defensible"** — this contradicts what the data dictionary says: "All PLE matching is deterministic (exact NMA_AppNo match, manual AppNo match, or deterministic AppNo match). No fuzzy/rapidfuzz matching is used. This ensures full auditability." The DE-FUZZY refactor removed ALL fuzzy matching. The matching IS strongly defensible. Should I still include the caution text?

3. **Clean subset confirmation**: The "only one match" subset exists (`IS_BEST_NMAT_RECORD + IS_PLE_ANALYSIS_SAFE`) and yields **23,357 matched Filipino B5+ passers with >=5yr gap**. This is solid for stress-testing. Confirm this definition is what you want.

---

## Tab Restructuring

### Current: 6 tabs
1. National Profile
2. 30th vs 40th Thresholds
3. Historical PLE-Passer Linkage
4. Institution and Foreign Context
5. Key Evidence for Policy Review
6. Data, Methods, and Limitations

### Proposed: 6 tabs (renamed/reshuffled)
1. **National Profile** — expand with bin-to-range table + UNI_TYPE threshold evidence
2. **Threshold Analysis** — rename from "30th vs 40th Thresholds"; add yearly stacked PLE chart, UNI_TYPE characterization, GIDA/IP context note
3. **PLE-Passer Linkage** — add "clean subset" stress-test, retain existing linkage charts, add caution context
4. **University Type and GIDA Context** — replace current "Institution and Foreign Context"; add evidence about public school examinees already meeting 40th cut-off
5. **Key Evidence for Policy Review** — update findings to reflect new analyses
6. **Data, Methods, and Limitations** — add matching defensibility notes, clean subset definition

---

## Complete TODO List

### TODO 1: Terminology sweep — "percentile" → "bin"
**Scope:** All UI text in dashboard.py
**What:**
- Tab titles: "30th vs 40th Percentile" → "30th vs 40th Thresholds"
- "Percentile Bin" → "Bin" in chart labels
- "Median percentile rank" → keep as-is (metric cards)
- "30th percentile cut-off" → "B4+ threshold (30th percentile)"
- "40th percentile cut-off" → "B5+ threshold (40th percentile)"
- Bin labels: B1 = "Bin 1 (0-9)", B4 = "Bin 4 (30-39)", B10 = "Bin 10 (90-100)"
- Update `BIN_LABELS` dictionary to "Bin 1 (0-9)" format
- Update tab title from "30th vs 40th Percentile" → "B4+ vs B5+ Thresholds"
- Update header/text references throughout

### TODO 2: Add bin-to-score-range reference table
**Tab:** 1 (National Profile) — early section
**What:**
| Bin | Score Range | Threshold |
|-----|-------------|-----------|
| B1 | 0-9 | — |
| B2 | 10-19 | — |
| B3 | 20-29 | — |
| **B4** | **30-39** | **30th percentile (SUC exception floor)** |
| **B5** | **40-49** | **40th percentile (SUC standard)** |
| B6 | 50-59 | — |
| B7 | 60-69 | — |
| B8 | 70-79 | — |
| B9 | 80-89 | — |
| B10 | 90-100 | — |

### TODO 3: Yearly stacked column chart — B5+ PLE counts (count + percentage)
**Tab:** 2 (Threshold Analysis) — new section
**What:** Two-panel visualization:
- Panel A (stacked bar): Year on x-axis, **count** on y-axis. Each bar is total B5+ examinees, stacked by `PLE_STATUS_LABEL` (Confirmed PLE passer vs No confirmed PLE match). Data labels on each segment.
- Panel B (stacked bar, same layout): Year on x-axis, **percentage** on y-axis (within-year B5+ stack). Shows the same data as percentages.

**Data source:** `IS_BEST_NMAT_RECORD`, `Year <= 2014`, `PercentileBin` in B5+. Same cutoff as Tab 3 currently uses.

**Rationale:** The instructor wants to show that even with declining top-bin share, the absolute number of B5+ examinees who later become PLE passers remains substantial.

### TODO 4: Show both percentage and actual count throughout
**Scope:** Audit existing tables and add count columns/rows where only percentages are shown, and vice versa.
**What:**
- Bin distribution tables: show both count matrix and percentage matrix
- PLE linkage by bin: already shows both count and percentage ✅
- Top-bin share: add count column alongside percentage
- Heatmaps: add a companion count table for each percentage heatmap

### TODO 5: Characterize B5+ examinees by UNI_TYPE
**Tab:** 2 (Threshold Analysis) — below threshold comparison table
**What:** Table showing B5+ examinee composition by UNI_TYPE:

| University Type | B5+ Examinees | % of all B5+ | % of that type's examinees |
|----------------|:------------:|:-----------:|:------------------------:|
| Public | X | X% | X% |
| Private | X | X% | X% |
| Foreign | X | X% | X% |
| **All** | **X** | **100%** | **X%** |

**Data:** `df_best`, `PercentileBin` in B5+, grouped by `UNI_TYPE`.

### TODO 6: GIDA/IP evidence — public school examinees already meeting 40th cut-off
**Tab:** 4 (University Type and GIDA Context) — new section
**What:** Evidence that most public school examinees already meet the 40th percentile cut-off, challenging the assumption that lowering the cut-off would primarily help disadvantaged groups.

**Key figure:** "X% of public school examinees (Y out of Z) already meet the 40th percentile cut-off."

**Supporting table:**

| Metric | Public | Private | Foreign |
|--------|:-----:|:-------:|:-------:|
| Total best-record examinees | X | X | X |
| B5+ (40th threshold) | X | X | X |
| B5+ share (%) | X% | X% | X% |
| B4-only (30th-39th) | X | X | X |
| B4-only share (%) | X% | X% | X% |

**Caveat:** Note that UNI_TYPE refers to undergraduate institution, not medical school. GIDA/IP status is NOT available in the dataset — the CMO exception for GIDA/IP requires documentation (NCIP cert, DOH/LGU cert) that is outside the scope of this data.

### TODO 7: Clean PLE subset analysis — stress-test the 40th percentile assumption
**Tab:** 3 (PLE-Passer Linkage) — new section "Stress-Test: Defensible PLE Subset"
**What:** Repeat the PLE linkage analysis using only the strongest possible matching criteria:
- `IS_BEST_NMAT_RECORD` = True (one person, one NMAT record)
- `IS_PLE_ANALYSIS_SAFE` = True (only clean deterministic matches)
- `PLE_YEAR_GAP` >= 5 (at least 5 years between NMAT and PLE)
- `FOREIGNER_STATUS` = 'Filipino' (exclude foreign nationals)

**Result:** 23,357 matched passers meeting all criteria (36.2% of observable cohort).

**Charts:**
- B5+ clean subset: PLE linkage by year (count + percentage)
- Distribution by UNI_TYPE
- Distribution by university (top 15)
- Comparison between clean subset and full observable cohort linkage rates

**Interpretation:** "This subset uses the most defensible matching criteria (clean deterministic match, >=5yr gap, Filipino nationals). The linkage rates are consistent with the full observable cohort analysis, suggesting the broader findings are robust to matching quality concerns."

### TODO 8: Retain existing PLE linkage with caution note
**Tab:** 3 — add caution callout
**What:** After existing PLE linkage charts, add:
> **Note on PLE matching:** The matching process (Pipeline 2) uses deterministic linking via NMAT application numbers. While the DE-FUZZY refactor removed all fuzzy matching for full auditability, the match depends on the application number being recorded consistently across the NMAT and PLE datasets. Undercounting is possible if numbers differ between datasets. The "clean subset" analysis above uses the strictest possible criteria (single best record, >=5yr gap, Filipino nationals) and produces consistent results.

### TODO 9: Update Tab 5 (Key Evidence) findings
**What:** Replace or add findings:
- Finding about absolute B5+ volume remaining substantial despite declining top-bin share
- Finding about public school B5+ threshold attainment
- Finding about robust clean-subset PLE linkage
- Retain existing findings (threshold context, institutional patterns, linkage gradient, foreign presence)

### TODO 10: Add PLE matching defensibility note to Tab 6
**Tab:** 6 — under "Key Methodological Choices" → "Deterministic PLE Matching"
**What:** Expand existing expander to mention:
- The deterministic matching approach (already documented)
- Limitation: depends on consistent application number recording
- The clean subset analysis as a robustness check
- Reference to `PLE_MATCH_MASTER.csv` (43,601 canonical match records)

### TODO 11: Update `ched_compute/` scripts for new analyses
**What:** Add or update scripts:
- `01_national_profile.py` — add bin range table
- `02_thresholds.py` — add yearly stacked PLE chart, UNI_TYPE characterization
- `03_ple_linkage.py` — add clean subset analysis
- `04_institution_gida.py` — rename from `04_foreign_analysis.py`, add GIDA/IP evidence
- `05_evidence_findings.py` — update findings
- `06_data_limitations.py` — add matching notes

### TODO 12: Commit and push to branch
After implementation:
- `git add streamlit_dashboard/CHED_relevant_dashboard/`
- Commit with descriptive message
- Push to `origin/ched-dashboard-revisions`

---

## Implementation Order

| Step | TODO | Effort | Dependency |
|------|------|--------|-----------|
| 1 | TODO 1: Terminology sweep | Medium | None |
| 2 | TODO 2: Bin range table | Low | None |
| 3 | TODO 4: Add counts to existing tables | Medium | None |
| 4 | TODO 3: Yearly stacked PLE chart | Medium | Data verified |
| 5 | TODO 5: UNI_TYPE characterization table | Low | TODO 4 |
| 6 | TODO 6: GIDA/IP evidence section | Medium | TODO 5 |
| 7 | TODO 7: Clean PLE subset analysis | High | Data verified (23,357 records) |
| 8 | TODO 8: PLE caution note | Low | TODO 7 |
| 9 | TODO 9: Update Tab 5 findings | Low | TODOs 3-7 |
| 10 | TODO 10: Tab 6 matching note | Low | TODO 8 |
| 11 | TODO 11: Update compute scripts | Medium | TODOs 1-10 |
| 12 | TODO 12: Commit & push | Low | All above |

---

## Questions Awaiting Your Answer

1. **Terminology scope**: Replace ALL "percentile" with "bin" in UI text, or only chart labels? How should metric cards read (e.g., "Median percentile rank")?

2. **Pipeline 2 defensibility**: The data dictionary states matching is "purely deterministic" and "ensures full auditability" after the DE-FUZZY refactor. Do you still want me to add the caution text, or acknowledge the matching is actually well-defended?

3. **Tab 4 restructure**: The current Tab 4 is "Institution and Foreign Context." I want to rename it to "University Type and GIDA Context" and add the public-school evidence there. The foreign section stays but as a smaller subsection. OK?

4. **Stacked chart placement**: The yearly stacked B5+ PLE chart — should it go in Tab 2 (Thresholds, alongside the threshold comparison) or Tab 3 (PLE Linkage, alongside the existing linkage-by-bin chart)? My recommendation: Tab 2, since it's about the B5+ threshold group's composition over time.
