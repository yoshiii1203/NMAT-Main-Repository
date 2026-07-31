# Audit 03 — `streamlit_dashboard/main_dashboard/dashboard.py`, Pages 1–6

Scope confirmed from code: `st.tabs()` at dashboard.py:729 defines 13 tabs. Tabs 1–6 (`tab1`..`tab6`, dashboard.py:748–1990) are:
1. Executive Summary (748–828)
2. Data Integrity (829–970)
3. Trends & Stability (971–1014)
4. Score Bins & Background (1015–1732)
5. University Type Analysis (1733–1897)
6. Flow & Pathways (1898–1990)

Tab 7 (PLE Alignment) starts at line 1991 — out of scope, belongs to auditor 04.

File length: 3,207 lines total. Setup/shared-helper code (lines 1–726, incl. `load_data_and_subsets`, `filter_df`, `ensure_required_columns`) was read in full because pages 1–6 depend on it.

All numbers below were recomputed against `streamlit_dashboard/main_dashboard/NMAT_Exodus.parquet` with `./.venv/Scripts/python.exe` (178,927 rows × 54 cols, matches shared context).

---

## Orchestrator-verified facts folded in (checked against pages 1–6)

The orchestrator supplied three additional verified facts mid-audit. All three were checked specifically against this file's pages-1–6 scope; results below (see F10–F12 for full detail).

1. **`IS_BEST_NMAT_RECORD` is broken** (1,311 people with zero `True` rows, 246 with >1, global deficit of 1,065 vs true `nunique(PERSON_KEY)`, and the 1,497 dropped rows are 100% `IS_PLE_PASSER=True`). **Confirmed present on Page 1**: both KPI cards that claim to count examinees (col1 "Best-record examinees" and col5 "Unique examinees") are wrong, and disagree with each other — see F10. Because the excluded people are 100% PLE passers, every PLE-passer-rate metric built on `bestobservable`/`besttrend` in pages 1–6 is biased low — see F11.
2. **`UNIVERSITY`/`UNI_TYPE` describes the examinee's undergraduate (pre-NMAT) institution, not a medical school** — confirmed: UNIVERSITY contains "UP DILIMAN" for 4,454 rows (1,914 of them PLE passers) despite UP Diliman having no College of Medicine; those rows' `CourseGroup` values are bachelor's-level fields (Medical & Allied 1,470, Natural Sciences 1,358, Social & Behavioral Sciences 826, Other 446, Education 316, Engineering & Technology 38). For pure NMAT-outcome analysis (Tables 13–17, Figures 12–16 on Page 5) this is the *correct* institution to use, since NMAT is a pre-medical-school admissions test. The problem is specifically where a page cross-tabulates this undergraduate field against **PLE** (a post-medical-school outcome) as if it explained board-passing — this happens in Page 4's comparative-analysis subsection, not on Page 5 itself (Page 5 carries no PLE content). See F12. Also confirmed: `NMA_College` (~3,213 distinct normalized values) and `UNIVERSITY` (~2,905 distinct normalized values) disagree by ~300 institutions, and Page 2 (Data Integrity) itself reports **both** as separate, disagreeing institution counts on the same page — see F12.
3. **Bin orientation** — checked. `ensure_required_columns` (dashboard.py:208, `_BIN_EDGES=[0,10,20,...,90,101]` mapped onto `BIN_ORDER=["B1",...,"B10"]`) puts B1 at percentile 0–9 (lowest) and B10 at percentile 90–100 (highest), matching the orchestrator's confirmation. Every caption in pages 1–6 that names B8–B10 calls it "top"/"upper segment" and every caption naming B1–B3 calls it "bottom"/"lower segment" (Figures 5–14, Tables 10–12, Table 21–22) — **no inversion found in this scope.**

---

## Global setup facts relevant to pages 1–6

- `IS_BOARD_OBSERVABLE_COHORT` does **not** exist in the source parquet (confirmed per shared context); dashboard.py:249–250 synthesizes it correctly as `Year <= 2014`. This part is fine.
- `HAS_CONFIRMED_PLE` / `PLE_STATUS_LABEL` (dashboard.py:252–263) are synthesized from `IS_PLE_ANALYSIS_SAFE == True`. Per shared context, `IS_PLE_ANALYSIS_SAFE` is a **byte-for-byte duplicate of `IS_PLE_PASSER`**, not "Year ≤ 2014" as CLAUDE.md/docs claim. So every "Confirmed PLE passer" / "No confirmed PLE match" label in the dashboard is really just the raw pass flag, not a "safe cohort" concept — see Finding F02.
- Sidebar filters (Year/UniType/Course/Sex) are applied via `filter_df` to **every** subset in `subsets.items()` (dashboard.py:687–704), so basic filter propagation into pages 1–6 is correct. The `PLE status` sidebar filter is intentionally applied **only** to the `bestobservable`/`uniobservable` subsets (line 697) — correct, since PLE status is undefined/meaningless outside the observable cohort.
- No instance found in pages 1–6 of code accidentally reading the unfiltered module-level `dfbesttrend`/`dfbestobservable` globals inside a tab body (those globals are only used to populate the sidebar's own filter option lists, lines 669–672) — so the CRITICAL "looks filtered but isn't" bug class was **not found** in this range.
- No in-place mutation of the `@st.cache_data`-returned frame was found in pages 1–6 (checked every `df[...] = `/`dfuni[...] = ` assignment site); all mutating code paths operate on `.copy()`'d frames.
- Boolean-ish string columns (`HasCEMMatch`, `HasTRUErawScores`, `AllRawComponentsPresent`) are coerced via `to_bool_series` before use (`BOOL_COLS`, line 85-88) — safe. `StoredVsDerivedMismatch`/`CalcVsDerivedMismatch` are **not** in `BOOL_COLS` but their only use in this scope (dashboard.py:890-891) goes through `count_true_flags()`, which calls `to_bool_series` internally — also safe. No truthiness bug materialized in pages 1–6.

---

## Page 1 — Executive Summary (dashboard.py:748–828)

| Element | Type | What it shows | Verified? | Issue |
|---|---|---|---|---|
| KPI: Best-record examinees | metric | `len(F["besttrend"])` | Recomputed = 133,804 | **F10 — undercounts true 134,869 unique people by 1,065; also double-counts 246 people and fully omits 1,311** |
| KPI: Years covered | metric | `nunique(Year)` on besttrend | Yes | OK |
| KPI: Median TRUE raw score | metric | median `TotalRawScoreTRUE`, besttrend | Yes | OK (NaNs auto-excluded by `.median()`) |
| KPI: Median percentile rank | metric | median `NMS_PER_num`, besttrend | Yes | OK |
| KPI: Unique examinees | metric | `nunique(PERSON_KEY)`, besttrend | Recomputed = 133,558 | **F10 — undercounts true 134,869 by 1,311 (the zero-flag people are entirely absent from `besttrend`, so `.nunique()` cannot recover them); disagrees with the "Best-record examinees" card two rows above by 246** |
| KPI: Repeat takers | metric | `F['trend']` groupby PERSON_KEY, `nunique(APPNO_CLEAN)>1` | Yes | OK — correctly uses **non**-deduped `trend` subset (needs all sittings) |
| KPI: Observable cohort size | metric | `len(F["bestobservable"])` | Yes, but see F10/F11 | Inherits the same 1,065-person deficit (proportionally ~1,296 of the missing people fall in Year≤2014) |
| KPI: Confirmed PLE share in observable cohort | metric | `HAS_CONFIRMED_PLE.mean()*100` on bestobservable | Recomputed = 45.38%; **corrected estimate ≈ 46.46%** | **F02** (label) + **F11** (value understated ~1.1pp because the excluded 1,296 people are 100% PLE passers) |
| Course-group legend text | narrative | static markdown | n/a | OK, descriptive only |
| Figure 1: Annual score/volume profile | combo line+bar (2x2 subplot) | median raw/Part I/Part II/percentile + examinee count by Year, besttrend | Recomputed | **F03 — examinee-count-by-year series is 60–93% of true sittings, non-uniformly** |
| Figure 2: Course-group composition pie | pie | `CourseGroup.value_counts()`, besttrend | Yes | OK |
| Figure 3: University-type composition pie | pie | `UNI_TYPE.value_counts()`, besttrend | Yes | OK |
| Table 1: Executive summary indicators | table | medians + top/bottom bin share, besttrend | Yes | OK |

## Page 2 — Data Integrity (dashboard.py:829–970)

| Element | Type | What it shows | Verified? | Issue |
|---|---|---|---|---|
| KPI: All NMAT rows | metric | `len(F["all"])` | Yes | OK |
| KPI: Best-record rows | metric | `len(F["best"])` | Yes | OK |
| KPI: Rows with TRUE raw scores | metric | count `HasTRUErawScores==True`, F["all"] | Yes | OK, row-level metric correctly not deduped |
| KPI: Observable best-record rows | metric | `len(F["bestobservable"])` | Yes | OK |
| Table 2: Analysis cohorts used | table | 6 cohort row counts | Recomputed | **F04 — "Interpretation" column is a verbatim duplicate of "Analytic subset" column (dead placeholder text)**; also **F02 — "Confirmed PLE-matched" label misapplied to a passer flag** |
| Table 3: TRUE raw-score validation | table | completeness + formula-mismatch counts, StoredVsDerived/CalcVsDerived flag counts | Yes | OK computationally; note `AllRawComponentsPresent`/`CalcVsDerivedMismatch` are dataset-wide constant (nuniq=1) per shared context, so these counts are structurally either 0 or all-rows — not disclosed |
| Table 4: UNI_TYPE consistency by source college | table | colleges mapping to >1 UNI_TYPE, grouped by `NMA_College` | Yes | **F06 — obeys sidebar filters**; **F12 — "Colleges checked" (~3,213 distinct `NMA_College`) disagrees with the "Universities checked" metric two widgets below (~2,905 distinct `UNIVERSITY`) by ~300 institutions, on the same page, with no explanation that they are two different source fields for nominally the same real-world entity** |
| Table 5 (expander): UNIVERSITY↔UNI_TYPE/LOCATION pairing audit | table | pairing conflicts, grouped by `UNIVERSITY` | Yes | Same F06 caveat; see F12 for the NMA_College-vs-UNIVERSITY count disagreement with Table 4 |
| Table 6: UNI_TYPE distribution | table | value_counts, F["all"] | Yes | OK, explicitly labeled row-level |
| Table 7: CourseGroup distribution | table | value_counts, F["all"] | Yes | OK |
| Table 8: PLE_STATUS_LABEL distribution | table | value_counts, F["all"] | Recomputed | **F01 — CRITICAL: default view mixes non-observable (Year>2014) rows into "No confirmed PLE match," inflating the apparent non-pass rate** |

## Page 3 — Trends & Stability (dashboard.py:971–1014)

| Element | Type | What it shows | Verified? | Issue |
|---|---|---|---|---|
| Figure 4: Annual score trends + volume | combo (reuses `make_trends_figure`) | besttrend | Recomputed | **F03** |
| Boxplot: TRUE raw score by Year | box | besttrend | Yes | Same F03 cohort-composition caveat applies (which examinees appear in which year is biased) |
| Boxplot: Percentile rank by Year | box | besttrend | Yes | Same F03 caveat |
| Boxplot: Part I raw score by Year | box | besttrend | Yes | Same F03 caveat |
| Boxplot: Part II raw score by Year | box | besttrend | Yes | Same F03 caveat |
| Table 9: Kruskal-Wallis by Year | table | H-stat, p, eta² for 5 scores across Year groups, besttrend | Yes, computation itself is correct (uses `stats.kruskal` properly, eta² formula is the standard epsilon-squared approx) | Same F03 caveat: the "Year" groups being compared are not equal-coverage samples of that year's sittings |

## Page 4 — Score Bins & Background (dashboard.py:1015–1732)

This is the largest page (three sub-tabs: By year / University type / Course group), including a large citizenship deep-dive nested under "University type."

| Element | Type | What it shows | Verified? | Issue |
|---|---|---|---|---|
| Figure 5: Bin heatmap by Year | heatmap | row-% within Year, besttrend | Yes | dropna on group/cat cols (see F05-class null handling, magnitude smaller here) |
| Table 10: Bin counts by Year | table | counts, besttrend | Yes | OK |
| Figure 6: Bin composition stacked bar by Year | stacked bar | besttrend | Yes | OK |
| Figure 7: Top vs bottom bin share by Year | line | besttrend | Yes | OK |
| Figure 8: Bin heatmap by UNI_TYPE | heatmap | dfuni (Public/Private/Foreign only) | Yes | OK |
| Figure 9: Top-bin share bar by UNI_TYPE | bar | dfuni | Yes | OK |
| Table 11: Chi-square UNI_TYPE × Bin | table | chi2/p/dof/Cramér's V | Yes, formula correct | OK |
| Figure: Bin composition per year facet by UNI_TYPE | faceted stacked bar | duckdb query on dfuni | Yes | OK |
| Record listings: Foreign/Public/Private (all) | 3 tables | raw record rows, dfuni | Yes | OK, filter-aware |
| Record listings: No-PLE-match by UNI_TYPE | 3 tables | `_nople_df = F["uniobservable"]`, filtered to `PLE_STATUS_LABEL='No confirmed PLE match'` | Recomputed | **F02 — some of these "no match" rows actually did match a PLE record** (caption explicitly says "IS_PLE_ANALYSIS_SAFE != True", line 1172) |
| Citizenship profile KPIs (4 metrics) | metric | profiled no-PLE-match records / foreigners / Filipinos / distinct labels | Yes | Inherits F02 population definition issue |
| Citizenship pie ×2, top-15 bar, bin-composition stacked bar, full bin heatmap | 5 charts | `_pc_base` (no-PLE-match, observable, citizenship-notna) | Yes | Inherits F02; heatmap uses YlOrRd (fine, sequential) |
| Top-bin share by citizenship, percentile box, raw-score box | 3 charts | `_pc_base` | Yes | n≥3 / n≥5 floors applied, reasonable |
| Summary tables by citizenship / ×UNI_TYPE / ×CourseGroup / ×Year | 4 tables | `_pc_base` aggregates | Yes | OK |
| Full record listing (citizenship) | table | `_pc_base` | Yes | OK |
| Comparative analysis: Foreigners vs Filipino-in-foreign-schools vs Public vs Private | summary table + 2 boxplots + heatmap + stacked bar + grouped bar + table | 4 constructed groups, observable cohort | Recomputed pass rates: Foreigners 2.51%, Filipinos-in-foreign-schools 36.23%, Public 50.06%, Private 44.72% | Caption "Foreigners typically show 0% or near-0%" (F09, minor); "PLE pass rate uses IS_PLE_ANALYSIS_SAFE" (F02); **F11 — all four "PLE pass rate %" figures are biased low by the IS_BEST_NMAT_RECORD zero-flag deficit**; **F12 — CRITICAL: "Filipinos (public schools)"/"Filipinos (private schools)" vs "PLE pass rate %" juxtaposes the examinee's undergraduate institution type against a post-medical-school outcome, implying the undergrad school explains board results when the actual (unobserved) medical school sits between the two** |
| Figure 10: Bin heatmap by CourseGroup | heatmap | besttrend | Yes | OK |
| Figure 11: Top-bin share by CourseGroup | bar | besttrend | Yes | OK |
| Table 12: Percentile summary by CourseGroup | table | n/median/IQR | Yes | OK |

## Page 5 — University Type Analysis (dashboard.py:1733–1897)

| Element | Type | What it shows | Verified? | Issue |
|---|---|---|---|---|
| Table 13: Institution type × location mix | table | counts + % of total, `uni_base` | Recomputed | **F05 — `uni_base` drops 3,026/132,409 (2.3%) rows missing PercentileBin, UNI_LOCATION, or UNI_TYPE, even though this table doesn't need PercentileBin** |
| Table 14: Institution type × location matrix (counts + row% + col%) | 3 tables | crosstab, `uni_base` | Yes | Same F05 |
| Figure 12: Bin heatmap by institution×location | heatmap | `uni_base` | Yes | Same F05 (here dropna is at least relevant to the metric) |
| Figure 13: Top-bin share by institution×location | bar | `uni_base` | Yes | Same F05 |
| Figure 14: Bin composition stacked bar by UNI_TYPE | stacked bar | `uni_base` | Yes | Same F05 |
| Table 15: Bin counts by UNI_TYPE | table | `uni_base` | Yes | Same F05 |
| Table 16: Foreign examinee summary (4 metrics) | metrics | `foreign = uni_base[UNI_TYPE=='Foreign']` | Yes | Same F05 |
| Figure 15: Bin distribution among foreign examinees | stacked bar | `foreign` | Yes | Same F05 |
| Figure 16: Medical & Allied vs Other by UNI_TYPE | stacked bar + table | `uni_base` | Yes | Same F05 — unnecessarily inherits the PercentileBin dropna even though this chart doesn't use PercentileBin |
| Table 17: University listings by UNI_TYPE (3 expanders) | table | applicant counts per university | Yes | **F05 — this table has nothing to do with PercentileBin yet still loses 2.3% of applicants because it's built from the shared `uni_base`, not a purpose-built subset** |

## Page 6 — Flow & Pathways (dashboard.py:1898–1990)

| Element | Type | What it shows | Verified? | Issue |
|---|---|---|---|---|
| Figure 17: Sankey UNI_TYPE→Bin | sankey | `uni` (Public/Private/Foreign) | Yes | OK |
| Table 18: UNI_TYPE→Bin flow counts | table | same | Yes | OK |
| Figure 18: Sankey CourseGroup→Bin | sankey | `best` (besttrend) | Yes | OK |
| Table 19: CourseGroup→Bin flow counts | table | same | Yes | OK |
| Figure 19: Sankey Bin→PLE status (observable) | sankey | `observable = F["bestobservable"]` | Recomputed | **F02** — correctly restricted to Year≤2014 (not the 100%-by-construction trap), but the PLE_STATUS_LABEL categories themselves conflate "never matched" with "matched, not flagged passer" |
| Table 20: PLE status composition within each bin | table | row-% of Figure 19 flow | Yes | Same F02 caveat |
| Table 21: Largest UNI_TYPE pathways into B8–B10 | table | top 10 by count | Yes | OK, caption correctly notes "by count, not by rate" |
| Table 22: Largest CourseGroup pathways into B8–B10 | table | top 10 by count | Yes | OK, same caveat present |

---

## Findings table

| ID | Severity | Status | Title | Location |
|---|---|---|---|---|
| F01 | CRITICAL | CONFIRMED | Table 8 default view inflates apparent PLE non-pass rate by mixing in structurally-too-recent rows | dashboard.py:967–968 |
| F02 | CRITICAL | CONFIRMED | `IS_PLE_ANALYSIS_SAFE` (=`IS_PLE_PASSER` duplicate) mislabeled as "Confirmed"/"matched" everywhere; conflates "passed boards" with "matched a PLE record" | dashboard.py:722, 765, 837–873, 1169–1707, 1942–1960 |
| F03 | HIGH | CONFIRMED | Best-record dedup used for year-over-year volume/trend charts undercounts true sittings non-uniformly (60.1%–92.6% of true volume by year) | dashboard.py:783–786, 973–1012 |
| F04 | HIGH | CONFIRMED | Table 2 "Interpretation" column is a verbatim duplicate of "Analytic subset" — dead placeholder content | dashboard.py:848–873 |
| F05 | MEDIUM | CONFIRMED | Page 5's shared `uni_base` drops 2.3% of rows (missing PercentileBin) from every table/chart, including ones that don't use PercentileBin | dashboard.py:1740 |
| F06 | MEDIUM | SUSPECTED | Data-integrity consistency checks (Tables 4–5) obey sidebar filters, undermining their purpose as global invariant checks | dashboard.py:896–953 |
| F07 | MEDIUM | SUSPECTED | RdYlGn diverging colormap used on a magnitude-only (non-diverging) heatmap implies a value judgment not present in the data | dashboard.py:1652–1660 |
| F08 | LOW | CONFIRMED | `derive_ple_status()` defined but never called — dead code | dashboard.py:160–163 |
| F09 | LOW | CONFIRMED | Caption overstates precision ("typically 0%") vs measured 2.51% | dashboard.py:1573 |
| F10 | CRITICAL | CONFIRMED | `IS_BEST_NMAT_RECORD` deficit (1,311 people entirely dropped, 246 double-counted) makes Page 1's two "examinee count" KPIs both wrong and mutually inconsistent | dashboard.py:756, 762 |
| F11 | CRITICAL | CONFIRMED | Every PLE-passer-rate metric built on the best-record cohort in pages 1–6 is biased low, because the people dropped by the F10 defect are 100% PLE passers | dashboard.py:765, 1589–1600, 1946–1960 |
| F12 | CRITICAL | CONFIRMED | `UNIVERSITY`/`UNI_TYPE` is the examinee's pre-NMAT undergraduate institution, not their medical school; Page 4's comparative section implies undergrad institution type explains PLE (board) outcomes; Page 2 separately reports two disagreeing institution counts from `NMA_College` vs `UNIVERSITY` | dashboard.py:1518–1600, 896–953 |

---

## Finding detail

### F01 — CRITICAL — Table 8 default view inflates apparent PLE non-pass rate (dashboard.py:967–968)

**Code:**
```python
st.dataframe(df["PLE_STATUS_LABEL"].value_counts(dropna=False).rename_axis("PLE_STATUS_LABEL").reset_index(name="Count"), use_container_width=True)
```
where `df = F["all"]` (line 834), i.e. all 178,927 rows under default (unfiltered) sidebar state, spanning Year 2006–2018.

**What it produces (recomputed):**
```
No confirmed PLE match    128,941   (72.06%)
Confirmed PLE passer       49,986   (27.94%)
```
But 90,783 of 178,927 rows (50.7%) are Year > 2014 — structurally unable to have a confirmed board-exam outcome yet, since Pipeline 2's PLE matching cannot observe exams that haven't been taken. Within just those post-2014 rows, 89.96% already show "No confirmed PLE match" — not because those examinees failed or never sat boards, but because not enough time has elapsed. This single table, sitting on the page titled "Data Integrity," is the most exposed reading of "72% didn't pass the boards" in the whole app, and it is largely a recency artifact.

**What it should produce:** either (a) restrict Table 8 to the observable cohort (`IS_BOARD_OBSERVABLE_COHORT==True`, Year≤2014) — recomputed observable-only split: 29,273 Confirmed / 35,228 No-confirmed-match (45.38% / 54.62%) — or (b) add a third category ("Not yet observable") for Year>2014 rows, or at minimum a loud caption disclosing the 50.7% non-observable share.

**Fix:** split the metric by `IS_BOARD_OBSERVABLE_COHORT`, or add the caveat directly in the table caption (currently just "Values are row counts under the current filters," line 958).

### F02 — CRITICAL — `IS_PLE_ANALYSIS_SAFE` mislabeled as "Confirmed"/"matched" throughout (dashboard.py:722, 765, 837–873, 1169–1707, 1942–1960)

**Code (representative, dashboard.py:258–263):**
```python
if "PLE_STATUS_LABEL" not in df.columns:
    if "IS_PLE_ANALYSIS_SAFE" in df.columns:
        df["PLE_STATUS_LABEL"] = np.where(df["IS_PLE_ANALYSIS_SAFE"] == True, "Confirmed PLE passer", "No confirmed PLE match")
```
Per shared context, `IS_PLE_ANALYSIS_SAFE` is byte-identical to `IS_PLE_PASSER` (not "Year≤2014" as CLAUDE.md claims). It is a **pass/fail-style flag**, not a **match-confirmation** flag. The dashboard's own read-me expander (dashboard.py:714–724) states: *"Confirmed PLE outcomes refer to IS_PLE_ANALYSIS_SAFE == True."* — internally consistent with the code, but it repeatedly uses "matched" language (Table 2 rows "Confirmed PLE-matched NMAT rows"/"...persons"; tab4 caption line 1172 "no confirmed PLE match (IS_PLE_ANALYSIS_SAFE != True)"; comparative-analysis caption line 1572 "PLE pass rate uses IS_PLE_ANALYSIS_SAFE") when what it is actually showing is a pass flag.

**Numeric consequence (recomputed):** In the observable best-record cohort (Year≤2014, n=64,501):
- Examinees with a confirmed PLE record match (`PLE_MATCH_METHOD.notna()`): 31,891
- Examinees flagged `IS_PLE_ANALYSIS_SAFE==True` ("passer"): 29,273
- **Gap: 2,618 examinees (4.06% of the observable cohort) did match a PLE record but are shown as "No confirmed PLE match"** in every listing/chart that uses `PLE_STATUS_LABEL` in this scope (tab4's no-PLE-match record listings and citizenship deep-dive, tab6's Bin→PLE Sankey and Table 20).

This is not the "100%-by-construction" denominator trap described in shared context (that trap was not found materialized in pages 1–6 — `IS_PLE_ANALYSIS_SAFE` is never used to build the denominator subset here, only as the numerator flag inside an already year-restricted cohort). But the label itself is wrong: "No confirmed PLE match" should read "No confirmed PLE pass" (or the flag should be redefined to reflect actual match status), and any place using the word "matched" for this flag is factually incorrect — those rows measure passing, not matching.

**Fix:** rename `PLE_STATUS_LABEL` categories to reflect "passer" semantics accurately (e.g., "Confirmed PLE passer" / "No confirmed PLE pass"), and stop using the word "matched" for a flag that is actually about passing. If a true match-vs-pass distinction is wanted, build it from `PLE_MATCH_METHOD.notna()` (match) crossed with `IS_PLE_PASSER` (pass) as two separate dimensions.

### F03 — HIGH — Best-record dedup distorts year-over-year volume/trend charts (dashboard.py:783–786, 973–1012)

**Code:** `get_yearly_summary()` (line 532) groups `df` by `Year` and counts `n=("APPNO_CLEAN","count")`, called on `base = F["besttrend"]` — one row per person (their single best NMAT attempt), not one row per exam sitting.

**Recomputed (all sittings vs. best-record-only, by year):**
```
Year  all_sittings  best_record_only  pct_shown
2006   4,376   3,665   83.8%
2007   4,656   3,660   78.6%
2008   6,120   4,849   79.2%
2009   8,362   6,881   82.3%
2010  10,560   8,008   75.8%
2011  11,929   8,731   73.2%
2012  13,320   9,145   68.7%
2013  13,988   9,121   65.2%
2014  14,833  10,441   70.4%
2015  16,284  10,402   63.9%
2016  20,968  12,609   60.1%
2017  25,870  23,955   92.6%
2018  27,661  22,337   80.8%
```
The "Examinee Count by Year" panel (Figure 1/Figure 4) and the score-median lines share this same biased cohort: a repeat-taker's earlier, typically weaker attempts are entirely excluded from the years they actually occurred in, and only appear in whichever year produced their *best* record — usually a later attempt. This depresses shown volume most in 2012–2016 (60–69% of true sittings) and least in 2017 (92.6%), a non-random pattern that can visually read as "volume dipped mid-decade then surged in 2017" when the true sittings series does not show that shape at all. The Kruskal-Wallis year-comparison in Table 9 inherits the same non-representative-by-year sampling.

The dashboard does disclose "best-record trend cohort" in the tab3 caption (line 975) and the global read-me (line 719), so this is not undocumented in the strictest sense — but neither caption warns that this specifically distorts the *volume* trend line, which is the one place a reader would expect the raw testing-volume shape.

**Fix:** compute the "Examinee Count by Year" bar from `F["trend"]` (all sittings, not deduped) instead of `F["besttrend"]`, or add a second series showing true sitting volume alongside the best-record volume.

### F04 — HIGH — Table 2 "Interpretation" column is a duplicate placeholder (dashboard.py:848–873)

**Code:**
```python
cohort_tbl = pd.DataFrame({
    "Analytic subset": [
        "All cleaned NMAT rows", "One best NMAT record per person",
        "Best-record rows within 2006-2018", "Best-record rows in the observable PLE window",
        "Confirmed PLE-matched NMAT rows", "Confirmed PLE-matched best-record persons",
    ],
    "Row count": [...],
    "Interpretation": [
        "All cleaned NMAT rows", "One best NMAT record per person",
        "Best-record rows within 2006-2018", "Best-record rows in the observable PLE window",
        "Confirmed PLE-matched NMAT rows", "Confirmed PLE-matched best-record persons",
    ],
})
```
The "Interpretation" column is a character-for-character copy of "Analytic subset" — it explains nothing and appears to be leftover placeholder text that was never filled in.

**Fix:** either drop the column or write real interpretive text (e.g., what analyses each cohort feeds).

### F05 — MEDIUM — Page 5 drops 2.3% of rows unnecessarily via shared `uni_base` (dashboard.py:1740)

**Code:**
```python
base = F["uni"].copy()
uni_base = base.dropna(subset=["UNI_TYPE", "UNI_LOCATION", "PercentileBin"]).copy()
```
**Recomputed:** `F["uni"]` (best-record, 2006–2018, UNI_TYPE in Public/Private/Foreign) has 132,409 rows; 3,026 of them (2.29%) have a null `PercentileBin` and are silently dropped before every table and chart on the page — including Table 17 (per-university applicant-count listings), Table 13 (institution×location mix), and Figure 16 (Medical & Allied vs. Other), none of which require `PercentileBin` to be non-null. `UNI_LOCATION` had 0 nulls in this subset (confirmed), so the observed 3,026-row loss is entirely attributable to `PercentileBin`.

**Fix:** build `uni_base` only for the bin-dependent charts; build a separate `UNI_TYPE`-only-dropna frame for Tables 13/17 and Figure 16 so they don't lose applicants who simply lack a percentile bin.

### F06 — MEDIUM — Data-integrity checks obey sidebar filters (dashboard.py:896–953)

Tables 4 and 5 check whether each college/university name maps consistently to one `UNI_TYPE`/`UNI_LOCATION` — a data-cleaning invariant that should hold (or not) independent of which years/course groups the user has selected. Because they run on `df = F["all"]` (sidebar-filtered), narrowing the Year or UNI_TYPE filter can hide genuine multi-year inconsistencies (e.g., a college recorded as "Public" in 2008 and "Private" in 2016 would show 0 conflicts if the user filters to a single year), producing false confidence that the pipeline's classification is internally consistent.

**Fix:** run these two checks on the unfiltered `subsets["all"]` regardless of sidebar state, and label them explicitly as global (not filter-scoped).

### F07 — MEDIUM — Diverging colormap on a non-diverging metric (dashboard.py:1652–1660)

`make_heatmap(_cmp_bin_pct, ..., "RdYlGn")` colors "percentage of a comparison group (Foreigners / Filipinos-in-foreign-schools / Public / Private) found in each percentile bin." That is a magnitude (0–100%), not a value with a meaningful "good" (green) vs. "bad" (red) polarity — a citizenship group having 40% of its members in bin B3 isn't inherently "bad" the way red implies. Every other heatmap on the same page uses a sequential scale (Blues, YlOrRd, OrRd); this one alone switches to a red-green diverging scale, which visually implies a quality judgment the underlying data doesn't carry.

**Fix:** use a sequential scale (e.g., Blues or Viridis) consistent with the rest of the page.

### F08 — LOW — Dead code: `derive_ple_status()` (dashboard.py:160–163)

Defined but never invoked; the equivalent logic is inlined at lines 259–262 (`np.where(...)`). Harmless but should be removed to avoid future drift between the two implementations.

### F09 — LOW — Caption overstates precision (dashboard.py:1573)

"Foreigners typically show 0% or near-0% because foreign nationals rarely sit Philippine licensure exams." Recomputed actual: Verified-Foreigner PLE pass rate in the observable cohort is 2.51% (122 of 4,868), not "typically 0%." Directionally correct, imprecise in wording.

### F10 — CRITICAL — `IS_BEST_NMAT_RECORD` deficit breaks both of Page 1's headline examinee-count KPIs (dashboard.py:756, 762)

**Verified by orchestrator, re-confirmed against the Page-1 population specifically:**
```python
best = df[df["IS_BEST_NMAT_RECORD"] == True]
besttrend = best[best["Year"].between(2006, 2018)]
len(besttrend)                       -> 133,804
besttrend["PERSON_KEY"].nunique()    -> 133,558
df[df["Year"].between(2006,2018)]["PERSON_KEY"].nunique()  -> 134,869   (TRUE unique count)
```
1,311 people have **zero** `IS_BEST_NMAT_RECORD=True` rows anywhere and are therefore entirely absent from `besttrend`/`bestobservable`/every other best-record subset; 246 people have **more than one** `True` row and are therefore double-counted in row-count metrics.

**Code:**
```python
col1.metric("Best-record examinees", f"{len(base):,}", ...)                       # line 756 -> 133,804
col1.metric("Unique examinees", f"{base['PERSON_KEY'].nunique():,}", ...)          # line 762 -> 133,558
```
**What it produces:** two different wrong numbers sitting three inches apart on the same page: 133,804 and 133,558 (a 246-person discrepancy between them, matching exactly the count of double-flagged people). **What it should produce:** both cards should read 134,869 if properly deduplicated — a deficit of 1,065 (row-count card) / 1,311 (nunique card) against ground truth, i.e. 0.8–1.0% understatement of examinee volume.

**Fix:** neither of these two metrics is a reliable "examinee count" as long as `IS_BEST_NMAT_RECORD` has zero-flag and multi-flag people. Fix must happen upstream (Pipeline 1/3), but downstream the dashboard should compute "Unique examinees" from `nunique(PERSON_KEY)` on the **unfiltered** trend-window population (`F["trend"]`, not `F["besttrend"]`) so it isn't gated by the broken flag, and should not present `len(base)` as an examinee count at all (it's a row count that can double- or zero-count people).

### F11 — CRITICAL — PLE-passer-rate metrics inherit the F10 deficit, biased low by construction (dashboard.py:765, 1589–1600, 1946–1960)

The 1,497 rows dropped by the F10 defect are **100% `IS_PLE_PASSER=True`** (verified by orchestrator), concentrated in Year 2009 (691) and 2010 (478) — re-confirmed: of the 1,497 dropped rows, 1,471 have Year≤2014 (i.e., would belong to the observable cohort), representing 1,296 unique people. Because every one of them is a passer, dropping them via the broken `IS_BEST_NMAT_RECORD` flag before the observable-cohort filter is even applied **systematically removes only PLE successes from the denominator and numerator alike**, understating every best-record-based PLE pass rate in pages 1–6.

**Recomputed:**
```
Shown: "Confirmed PLE share in observable cohort" (dashboard.py:765) = 45.38%  (29,273 / 64,501)
Corrected (adding back the 1,296 missing all-passer people): ≈ 46.46%  (30,569 / 65,797)
```
This ~1.1 percentage-point understatement is small in isolation but propagates into every other best-record PLE-rate figure in scope: the tab4 comparative-analysis "PLE pass rate %" column (Public 50.06%, Private 44.72%, etc., dashboard.py:1589–1600) and the tab6 Bin→PLE Sankey / Table 20 composition (dashboard.py:1946–1960) all draw from the same defective `bestobservable` subset and are understated by a comparable margin (concentrated specifically in whichever bins/groups the 1,296 2009–2010 examinees fall into, since the bias is not uniform across bins/subgroups).

**Fix:** same as F10 — fix the upstream `IS_BEST_NMAT_RECORD` computation so zero-flag people get a best record assigned, or have downstream PLE-rate calculations fall back to raw `PERSON_KEY`-level dedup instead of trusting the flag.

### F12 — CRITICAL — `UNIVERSITY`/`UNI_TYPE` is the undergraduate institution, not the medical school; Page 4 implies otherwise, and Page 2 reports two disagreeing institution counts (dashboard.py:1518–1600, 896–953)

**Verified (orchestrator + re-confirmed):** `UNIVERSITY="UP DILIMAN"` appears on 4,454 rows (1,914 PLE passers) despite UP Diliman never having offered a medical degree; the `CourseGroup` values for those rows are bachelor's-level fields (Medical & Allied 1,470 — i.e. pre-med/nursing/biology undergrad majors, Natural Sciences 1,358, Social & Behavioral Sciences 826, Other 446, Education 316, Engineering & Technology 38). This confirms `UNIVERSITY`/`UNI_TYPE` records where the examinee did their **bachelor's degree**, which is the correct and expected field for an NMAT (a pre-medical-school admissions test) — Page 5's charts, which only cross `UNI_TYPE`/`UNIVERSITY` against NMAT-derived measures (`PercentileBin`, raw score), are **not** misrepresenting anything and required no correction.

**Where it does become a misrepresentation — dashboard.py:1518–1600 (tab4, "Comparative analysis: foreigners vs Filipino students"):**
```python
_g_pub = F["bestobservable"][F["bestobservable"]["UNI_TYPE"] == "Public"].copy()
_g_pub["_cmp_group"] = "Filipinos (public schools)"
...
_g_prv["_cmp_group"] = "Filipinos (private schools)"
...
_ple_rates = _cmp_df.groupby("_cmp_group", observed=True)["_ple_num"].mean().mul(100)...
```
displayed as a "PLE pass rate %" column (dashboard.py:1589–1600, caption at 1572 "PLE pass rate uses IS_PLE_ANALYSIS_SAFE") next to group labels "Filipinos (public schools)" / "Filipinos (private schools)". A reader naturally reads this as "public [medical] schools have a 50.06% PLE pass rate vs. 44.72% for private" — i.e., that the institution named by `UNI_TYPE` explains or predicts board-exam success. In fact `UNI_TYPE` here is the examinee's **undergraduate** institution; the actual medical school attended between the NMAT and the PLE is a different, **unobserved** institution not present anywhere in this 54-column schema. The dashboard is therefore implicitly attributing a licensure outcome to an institution that had no role in producing it.

**Corrected wording:** rename the group labels to make the undergraduate scope explicit — e.g. "Filipinos (public undergrad)" / "Filipinos (private undergrad)" — and add an explicit caveat near the "PLE pass rate %" column: *"UNI_TYPE/UNIVERSITY reflect the examinee's undergraduate (pre-NMAT) institution, not the medical school attended between NMAT and the licensure exam; this dataset does not capture medical-school identity, so PLE outcomes here cannot be attributed to institutional quality of medical training."*

**Separately, on Page 2 (Data Integrity, dashboard.py:896–953):** Table 4 ("Colleges checked", grouped by `NMA_College`) and the university-pairing metric three widgets below ("Universities checked", grouped by `UNIVERSITY`) report different institution counts for what a reader would assume is the same underlying set of schools:
```
distinct NMA_College (normalized): 3,213
distinct UNIVERSITY (normalized):  2,905
```
a ~300-institution (10%) disagreement, with no caption explaining that these are two different source columns that are supposed to be redundant duplicates of each other but aren't identical after cleaning. This is exactly the kind of silent metric-disagreement the "Data Integrity" page is supposed to surface, not itself commit.

**Fix:** (1) add the undergraduate-vs-medical-school caveat wherever `UNI_TYPE`/`UNIVERSITY` is cross-tabulated against any PLE/board outcome (tab4 comparative section is the only place in scope where this happens); (2) on Page 2, either reconcile `NMA_College` and `UNIVERSITY` to one canonical institution list, or explicitly label both metrics so readers know they're two different — and disagreeing — countings of "institution."

---

## Missing but supportable analyses (pages 1–6 scope)

These are things the 54-column schema already supports but pages 1–6 never surface:

1. **Foreign-share trend by year.** `CITIZENSHIP_FINAL`/`FOREIGNER_STATUS` are loaded and used deeply in tab4's citizenship deep-dive, but only for the "no-PLE-match" subset. A simple "% foreign by Year" trend line (shared context already computed this: 3.9% in 2006 → ~29% in 2015–2017) would be a natural, high-value addition to the Executive Summary or Trends page and uses columns already in memory.
2. **Sex/gender composition on the Executive Summary.** `SEX_CLEAN` is derived and used as a sidebar filter but never shown as a breakdown chart in pages 1–6 (parity with the existing Course-Group and University-Type pies at Figures 2–3 would be a one-line addition).
3. **StoredRawTotal vs. TotalRawScoreTRUE mismatch rate**, to substantiate the CLAUDE.md-cited "42.2% of StoredRawTotal values were incorrect" claim directly on the Data Integrity page. Both columns (`StoredRawTotal`, `CalculatedRawTotal_Source`) are already loaded into `NUMERIC_COLS`; Table 3 currently only checks Total=Part I+Part II internal consistency, not Stored-vs-TRUE, so the headline pipeline claim is never actually shown to the user.
4. **True (non-deduped) sittings-by-year alongside best-record-by-year** — directly addresses F03 and would let users see both series.
