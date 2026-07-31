# Auditor 04 — `streamlit_dashboard/main_dashboard/dashboard.py`, Pages 7–13 + Shared Infrastructure

Scope: Tab 7 (PLE Alignment) through Tab 13 (CHED Compliance), plus data loading/caching, sidebar
filters, and shared helpers/constants (auditor 03 owns tabs 1–6 and does not cover infra, per brief).
File is 3,207 lines total; tabs 7–13 span lines 1993–3207 (`with tab7:` … `with tab13:` at lines
1993, 2155, 2326, 2423, 2562, 2676, 2809).

All numbers below were recomputed independently with
`./.venv/Scripts/python.exe` against `streamlit_dashboard/main_dashboard/NMAT_Exodus.parquet`
(178,927 rows × 54 cols, byte-identical to the other two copies per shared context).

---

## 0. Orchestrator-supplied facts folded in (verified independently)

1. **`IS_BEST_NMAT_RECORD` is broken.** `sum(IS_BEST_NMAT_RECORD)=133,804` vs `nunique(PERSON_KEY)=134,869`.
   Confirmed: 1,311 PERSON_KEYs have **zero** `True` rows (1,497 rows dropped entirely), 246 PERSON_KEYs
   have **>1** `True` row (double-counted). Confirmed the dropped rows are **100% `IS_PLE_ANALYSIS_SAFE==True`**
   (`(dropped_rows["IS_PLE_b"]==True).mean() == 1.0`), concentrated in NMAT years 2009 (691 rows) and 2010
   (478 rows). This is the single biggest driver of wrong numbers on every "best-record" page in my range
   (7, 9, 10, 11, 12, 13) — see Finding 04-01.
2. **`UNIVERSITY` is the applicant's undergraduate school, not their medical school.** Corroborated:
   `UNIVERSITY == "UNIVERSITY OF THE PHILIPPINES - DILIMAN"` → 4,454 rows, `UNI_TYPE` 100% "Public",
   `CourseGroup` spread across Natural Sciences/Social & Behavioral/Education/Engineering (not a
   College-of-Medicine population), 1,914 of them `IS_PLE_ANALYSIS_SAFE==True`. UP Diliman has no MD
   program. This invalidates every per-institution PLE claim on Tab 13 — see Finding 04-05 (CRITICAL,
   umbrella finding for Tab 13 Sections B, D, E) and the Tab 7 Table 27/30 "university type" framing.
3. **Bin orientation** (B1 lowest decile 0–9, B10 highest 90–99, monotonic) — checked every page-7/11/13
   narrative and chart in my range; found **no inversions**. "Top bin" always correctly means B8–B10,
   "cut-off" scenarios always correctly treat B4+/B5+ as *above* the threshold. Clean on this dimension.

---

## 1. Element inventory

### Tab 7 — PLE Alignment (lines 1993–2151)
Base cohort declared: `df = F["bestobservable"]` (line 1996), `dfuni = F["uniobservable"]` (1997) — correctly
the Year≤2014 + best-record observable cohort, **not** the pre-filtered `plesafe`/`plebest` subsets. Good:
the "IS_PLE_ANALYSIS_SAFE misused as the *filter* instead of the *outcome*" trap that the brief warned about
is **not present** here — denominator is genuinely the observable population, not pre-filtered to passers only.

| # | Element | Type | Cols/Groupby | Lines |
|---|---|---|---|---|
| Table 23 | Score profile by PLE status | table (count/median/mean/Q1/Q3) | `PLE_STATUS_LABEL` × 5 score cols | 2004–2009 |
| Figure 20 | TRUE raw score by PLE status | boxplot | `PLE_STATUS_LABEL` vs `TotalRawScoreTRUE` | 2011–2017 |
| Table 24 | Mann-Whitney confirmed vs no-match | stat table + effect size | `mann_whitney_ple()` | 2019–2031 |
| Figure 21 | Bin distribution by PLE status | 100%-stacked bar | `PLE_STATUS_LABEL` × `PercentileBin` | 2034–2039 |
| Figure 22 / Table 25 | PLE status composition within bin | 100%-stacked bar + table | `PercentileBin` × `PLE_STATUS_LABEL` | 2041–2055 |
| Table 26 / Figure 23 | Course-group top-bin ("survival") share | table + horiz. bar | `CourseGroup`, `IS_TOP_BIN=B8-10` on `F["besttrend"]` (not observable — correct, it's not a PLE metric) | 2058–2087 |
| Table 27 | Confirmed PLE alignment by university type | table | `UNI_TYPE` on `dfuni` | 2089–2101 |
| Table 28 | Confirmed PLE alignment by NMAT year | table | `Year` | 2106–2116, 2144–2146 |
| Table 29 | Confirmed PLE alignment by "pre-med background" | table | `CourseGroup` | 2118–2129, 2147–2148 |
| Table 30 | Confirmed PLE alignment by university type | table | `UNI_TYPE` | 2131–2142, 2149–2150 |

### Tab 8 — Repeat Takers (lines 2155–2321)
Base: `df = F["trend"]` (2158) — **correctly** all sittings (not best-record), required to count attempts.

| # | Element | Type | Lines |
|---|---|---|---|
| Figure 24 / Table 31 | Attempt-count distribution | bar + table | 2160–2178 |
| Table 32 | Repeat-taker trajectory summary (persons, analytic n, % improved, medians) | table | 2180–2225 |
| (unlabeled) | Change from first→last attempt | boxplot | 2227–2253 |
| (unlabeled) | First vs last percentile scatter | scatter | 2255–2283 |
| Repeat-taker detail table | full unbounded `st.dataframe` | 2285–2303 |
| NMA_AppNo deterministic match histories | full unbounded `st.dataframe` | 2307–2321 |

### Tab 9 — Subtests & Profiles (lines 2326–2419)
Bases: `uni_base = F["uni"]`, `course_base = F["besttrend"]` — both best-record. Correct choice (avoids
repeat-taker inflation of subtest means).

| # | Element | Type | Lines |
|---|---|---|---|
| Figure 27 / Table 34 | Mean standardized subtest scores by university type | heatmap + table | 2336–2358 |
| Table 35 | Raw-score subtest means by university type (expander) | table | 2360–2364 |
| Figure 28 / (table) | Mean standardized subtest scores by course group | heatmap + table | 2366–2387 |
| Table 37 | Raw-score subtest means by course group (expander) | table | 2389–2393 |
| Figure 29 / Table 38 | Radar profile by university type | radar + table | 2402–2407 |
| Figure 30 / Table 39 | Radar profile by course group | radar + table | 2413–2418 |

### Tab 10 — Year Gap & Gender (lines 2423–2557)
Bases: `F["bestobservable"]` for gap, `F["besttrend"]`/`F["bestobservable"]` for gender — both correct.

| # | Element | Type | Lines |
|---|---|---|---|
| KPIs (4) | Confirmed passers, median/Q1/Q3 year gap | metrics | 2439–2443 |
| Figure 31 | PLE year-gap histogram | histogram | 2448–2459 |
| Figure 32 | PLE year gap by course group | boxplot | 2461–2474 |
| Table 40 | Year-gap summary by course group | table | 2476–2491 |
| Table 41 | Score summary by sex | table | 2503–2516 |
| Figure 33 | Percentile-rank distribution by sex | boxplot | 2518–2531 |
| Figure 34 | Sex composition by NMAT year | 100%-stacked bar | 2533–2543 |
| Table 42 / (chart) | PLE status composition by sex (observable) | 100%-stacked bar + table | 2545–2557 |

### Tab 11 — Statistical Tests (lines 2562–2671)

| # | Element | Test | Base | Lines |
|---|---|---|---|---|
| Table 43 | Kruskal-Wallis, scores across Year | KW + η² | `F["besttrend"]` | 2570–2585 |
| Table 44 | Mann-Whitney, PLE status | MW + rank-biserial r | `F["bestobservable"]` | 2587–2604 |
| Table 45–47 / Figure 35 | Chi-square, UNI_TYPE × PercentileBin | χ² + Cramér's V | `F["uni"]` | 2606–2639 |
| Figure 36 / Table 48 | Dunn post-hoc, percentile by Year | Dunn + Bonferroni | `F["besttrend"]` | 2641–2671 |

### Tab 12 — Policy Tables & Export (lines 2676–2805)
Base: `policybase = F["bestobservable"]` throughout. 4 download buttons, one per table.

| # | Element | Lines |
|---|---|---|
| Table 1 (year) / download | 2685–2696, 2748–2749, 2778–2783 |
| Table 2 (course) / download | 2697–2709, 2751–2752, 2784–2790 |
| Table 3 (uni type) / download | 2710–2721, 2754–2755, 2791–2797 |
| Table 4 (top-bin survival) / chart / download | 2723–2772, 2757–2772, 2798–2804 |

### Tab 13 — CHED Compliance (lines 2809–3207)
Bases: `df_obs = F["bestobservable"]`, `df_trend = F["besttrend"]`.

| # | Section | Element | Lines |
|---|---|---|---|
| A | National PLE Benchmark | annual rate line chart + 5yr rolling avg line + table + download | 2824–2895 |
| B | Per-HEI PLE Performance | slider, KPIs, ranked table (✅/🔴 status), download | 2900–2965 |
| C | 30th vs 40th Cut-off Scenarios | scenario table + grouped bar + download | 2969–3032 |
| D | Foreign Student 10-Slot Cap | KPIs, per-SUC summary table, per-SUC-year table, download | 3036–3114 |
| E | Per-HEI Score Distribution Viewer | selectbox, 4 KPIs, bar+box charts, table, download | 3118–3207 |

---

## 2. Findings summary table

| ID | Severity | Status | Title | Location |
|---|---|---|---|---|
| 04-01 | **CRITICAL** | CONFIRMED | Broken `IS_BEST_NMAT_RECORD` silently drops 1,311 confirmed PLE passers, undercounting every best-record PLE rate on pages 7/9/10/11/12/13 | infra (line 276) + every use of `F["best*"]` |
| 04-02 | **CRITICAL** | CONFIRMED | "PLE pass rate" / "PLE passing rate" language on Tab 13 (and "Confirmed PLE passer" elsewhere) is actually a *match* rate against a passers-only source list, not a licensure pass rate | 2839, 2884, 2902, 2922, 2949, 3000, 3012–3014, 3142 |
| 04-03 | **CRITICAL** | CONFIRMED | Tab 13 Section A/B "national/per-HEI PLE benchmark" is computed from NMAT-cohort years (2006–2014), not actual PLE administration years, and the reference year (2014) is 12 years stale relative to the CMO's 2026 effectivity — it cannot be "the average national passing percentage for the last 5 years" the CMO means | 2824–2895 |
| 04-04 | **CRITICAL** | CONFIRMED | Tab 13 "5-year rolling average" is a **positional** pandas `.rolling(5)`, not calendar-year aware — if the sidebar Year filter creates gaps, it silently averages non-contiguous years and mislabels the result as a "5-year" average, while still driving the HEI pass/fail benchmark comparison | 2840 |
| 04-05 | **CRITICAL** | CONFIRMED | Tab 13 Sections B, D, E rank/judge institutions using `UNIVERSITY`/`UNI_TYPE`, which is the applicant's **undergraduate** school, not the medical school the CMO regulates. No medical-school identifier or institutional PLE denominator exists in the 54 columns, so a CMO-compliant per-institution determination is **unsupported by the data**, not merely inaccurate | 2900–2965 (B), 3036–3114 (D), 3118–3207 (E) |
| 04-06 | **HIGH** | CONFIRMED | Tab 13 Section D applies the CHED CMO's 10-foreign-slot cap (effective AY2026-2027) retroactively to 2006–2018 NMAT-taker data as if these are policy violations, and counts NMAT test-takers (not admitted/enrolled freshmen) against a per-incoming-class cap | 3037–3103 |
| 04-07 | **HIGH** | CONFIRMED | Tab 13 Section C juxtaposes "Admitted (best records)" (all years 2006–2018, n=91,409 at B4+) with "PLE pass rate" computed on a different, half-sized, older cohort (observable Year≤2014 only, n=46,609) in the same table row without disclosing the cohort mismatch | 2984–3002 |
| 04-08 | **HIGH** | CONFIRMED | Tab 13 Section B ranks/labels institutions "eligible"/"not eligible" using per-HEI samples as small as n=5; 163 of 539 listed HEIs (30%) have 5–10 examinees, making the ✅/🔴 status highly unstable | 2908–2958 |
| 04-09 | **HIGH** | SUSPECTED | Tab 13 does not address the CMO's GIDA/IP equity provision or reference the actual national PLE passing percentage published by PRC — no such fields exist in the 54 columns, but the page presents itself as CHED-compliance "supporting evidence" without flagging this gap | whole tab13 |
| 04-10 | **MEDIUM** | CONFIRMED | Repeat-taker detail table and NMA_AppNo match-history table render fully unbounded (up to ~33,713 rows unfiltered); the data_aggregator's mirrored static export of this exact logic produced an 8.7 MB markdown file, confirming no row cap is applied anywhere in this code path | 2285–2303, 2307–2321 |
| 04-11 | **LOW** | CONFIRMED | Table 23 (Tab 7) aggregation columns from `lambda` quantile functions render as unlabeled `<lambda_0>`/`<lambda_1>` in the displayed table | 2008 |
| 04-12 | **LOW** | CONFIRMED | Figure/Table 21, 22, 25 silently drop 1,306 of 64,501 (2.0%) observable rows with null `PercentileBin` via `.dropna()` inside `pct_table()`, without any on-page disclosure | 322–332 (helper), used at 2036, 2043–2044 |
| 04-13 | **LOW** | SUSPECTED | `load_data_and_subsets()`'s `_v = "exodus_v1"` local variable (line 270) is a dead value never read or returned; it only "works" as a cache-buster because Streamlit hashes function source text, not because the variable does anything — fragile if someone "fixes" it by removing the unused var | 270 |

Note on statistical methodology (Tab 11, item 5 in brief): **no confirmed issues.** Kruskal-Wallis
reports η² (470–488), Mann-Whitney reports rank-biserial r (491–512), chi-square reports Cramér's V
(515–529), and the Dunn post-hoc explicitly applies Bonferroni correction (2649–2653) for the ~78
pairwise year comparisons implied by 13 groups. Test choice matches data type (ordinal/continuous
scores, independent groups) in all four tabs. This is a clean area of the codebase — flag it as such
rather than inventing a finding.

Note on `IS_BEST_NMAT_RECORD` usage pattern (brief item 1): every tab in my range correctly chooses
all-sittings (`F["trend"]`) only for Tab 8 (repeat-taker counting, where duplicates are the point) and
best-record subsets everywhere else. The *usage pattern* is correct; the underlying flag's *values* are
wrong (04-01).

---

## 3. Finding detail

### 04-01 (CRITICAL) — Broken best-record dedup undercounts confirmed PLE passers on every page 7/9/10/11/12/13 rate

`ensure_required_columns`/`load_data_and_subsets` (dashboard.py:276) does
`dfbest = df[df["IS_BEST_NMAT_RECORD"] == True]` and every "best"/"observable" subset in `F` is derived
from it. The flag itself is corrupted upstream (Pipeline 2/3): 1,311 PERSON_KEYs get **zero** `True` rows
(so they vanish from every best-record page entirely) and 246 get more than one (double-counted). The
1,497 dropped rows are **100% `IS_PLE_ANALYSIS_SAFE==True`** — i.e., the dedup bug selectively deletes
confirmed PLE passers, concentrated in NMAT years 2009 (691) and 2010 (478).

Recomputed, Tab 7's headline observable-cohort rate (also used verbatim on Tab 12 Table 1 and Tab 13
Section A/C):

```
CURRENT (dashboard, broken dedup):   n=64,501   confirmed=29,273   rate=45.38%
CORRECTED (1 row/person, latest-year → highest-percentile tiebreak): n=64,531   confirmed=30,511   rate=47.28%
Delta: +1.90 percentage points, +1,238 confirmed passers
```
(`./.venv/Scripts/python.exe` snippet: sort `df` by `PERSON_KEY, Year desc, NMS_PER_num desc`,
`drop_duplicates(subset="PERSON_KEY", keep="first")` — produces exactly `nunique(PERSON_KEY)=134,869`
rows system-wide, confirming the corrected dedup is well-formed where the shipped flag is not.)

Every downstream "confirmed_ple_share_pct" cell on Tables 27–30 (Tab 7), 43/44 (Tab 11 test inputs),
1–4 (Tab 12), and Section A/B/C (Tab 13) inherits this same downward bias. Fix: correct the
`IS_BEST_NMAT_RECORD` flag at the pipeline level (Pipeline 1/2) so exactly one row per `PERSON_KEY` is
flagged, preferring the actual matched PLE attempt where one exists (per the documented rule in
`docs/data_dictionary.md` line 142) rather than leaving 1,311 known passers unflagged.

### 04-02 (CRITICAL) — Match rate presented as pass rate

`docs/data_dictionary.md:140` itself documents `IS_PLE_PASSER` as "True if the examinee matched a PLE
record (any match status)" and confirms `IS_PLE_ANALYSIS_SAFE` (line 141, "authoritative flag") has the
identical 49,986-True count — i.e., in the shipped parquet they are literally the same boolean
(`(df.IS_PLE_ANALYSIS_SAFE == df.IS_PLE_PASSER).all() == True`, per shared context, re-verified here).
`dataset/PLE_DATA.csv` (the match source) has only two columns — `FULL_NAME, PLE_YEAR_PASSED` — no
fail records exist anywhere in the pipeline. So "confirmed" literally means "found in a name/appno match
against a list that only contains people who eventually passed *at some point, however many years
later*." People who never took the PLE, took it after the data's coverage window, or were missed by the
deterministic matcher (documented false-negative risk given 3 different "matched" counts exist: 49,986 /
54,528 / 57,304 — see shared context) are all folded into "No confirmed PLE match" — i.e., counted as if
they failed. Language on Tab 13 elevates this from an already-loaded "Confirmed PLE passer" label (which
at least Tab 7/12 use) to explicit **"PLE pass rate" / "PLE passing rate"** (lines 2884, 2902, 2922, 2949,
3000, 3012–3014, 3142) — the strongest, most literal misstatement in the file. A stakeholder reading
"PLE pass rate: 43.5%" reasonably infers "43.5% of people who sat the licensure exam passed it," which
is not what is measured; the true denominator is "all NMAT examinees in the observable cohort," most of
whom never appear in the PLE dataset for reasons unrelated to failing.

Fix: rename every "PLE pass rate"/"PLE passing rate" label to "PLE match rate" or "confirmed PLE
match share," and add an explicit caption stating the denominator includes people who may never have
sat the licensure exam.

### 04-03 / 04-04 (CRITICAL) — Tab 13 "national benchmark" measures the wrong population and the wrong time axis, and breaks under filtering

Section A (2824–2895) builds `_annual` by grouping `df_obs` (Year≤2014, best-record NMAT-admission-year
cohort) by **NMAT year**, computing `ple_rate_pct` per NMAT year, then a `.rolling(window=5,
min_periods=3)` over those rows (line 2840), and picks the last non-null row as `_benchmark_val` — which,
recomputed with default filters, is **Year=2014, benchmark=43.46%** (`5yr avg over NMAT years 2010–2014`).
The CMO (`docs/CHED_CMO.md` §IV.B.1.b) means "the average national PLE **passing** percentage for the
last 5 years" — the real-world, PRC-published annual PLE pass rate for the last five *administrations of
the licensure exam*, which this dataset cannot compute (04-02) and which, even if it could, would need to
be indexed by **PLE exam year**, not NMAT admission year four-to-fourteen years earlier. The displayed
"2014" reference year is already 12 years out of date relative to the CMO's 2026 effectivity, and will
never advance because the observable cohort is hard-capped at Year≤2014 by construction — this benchmark
is permanently frozen in the past, not "rolling" in any meaningful sense for a live compliance tool.

Independently: the rolling call at line 2840 operates positionally on `_annual`'s row order, not on
actual Year values. Under default filters `_annual` is contiguous (Years 2006–2014, one row per year) so
the positional window happens to equal a true 5-calendar-year window. But the sidebar Year multiselect
(674, `default=year_options` — all years, user-editable) feeds directly into the same `filter_df` that
builds `F["bestobservable"]` (688–700), and `_annual` is grouped straight off `df_obs = F["bestobservable"]`
with no gap-filling. Deselect any single interior year (e.g. 2011) and `.rolling(5, min_periods=3)`
silently averages across the resulting non-contiguous 8-row series, still labeling the output "5-year
rolling avg" and still using it to assign ✅/🔴 status to every HEI in Section B. Fix: reindex `_annual`
to the full Year range before rolling (so missing years produce NaN gaps rather than window compression),
or disable Section A when the Year filter is non-contiguous.

### 04-05 (CRITICAL) — UNIVERSITY is the undergrad school; Tab 13 institutional judgments are unsupported

Section B (2900–2965) groups `df_obs` by `["UNIVERSITY", "UNI_TYPE"]`, computes a per-institution PLE
match rate, and stamps each with "✅ Above benchmark (30th eligible)" / "🔴 Below benchmark (40th
required)" (2927–2931) — i.e., it presents itself as a per-medical-school CHED compliance verdict.
Orchestrator-verified and independently corroborated: `UNIVERSITY=="UNIVERSITY OF THE PHILIPPINES -
DILIMAN"` (no College of Medicine) yields 4,454 rows, 100% `UNI_TYPE=="Public"`, `CourseGroup` spanning
Natural Sciences/Social & Behavioral/Education/Engineering (an undergraduate population, not an MD
cohort), and 1,914 `IS_PLE_ANALYSIS_SAFE==True`. `UNIVERSITY` is populated from the applicant's
pre-NMAT undergraduate institution; NMAT is sat to apply *to* an MD program, so the medical school
actually attended is not in the dataset at all (no matriculation/enrollment table exists among the 54
columns). Consequences:
- Section B's per-institution ✅/🔴 verdicts (line 2924, `above_benchmark = ple_rate_pct > _benchmark_val`)
  do not measure any PHEI's own PLE performance as CMO §IV.B.1.b requires — they measure "PLE match rate
  of NMAT-takers who once studied at institution X for their bachelor's degree." A PHEI running an MD
  program could show "🔴 below benchmark" purely because its undergrad feeder population differs from
  its MD graduates, or could show up **only** as a source of applicants and never as a medical-education
  provider at all (e.g., UP Diliman has no MD program yet appears ranked in this table).
- Section D's SUC 10-slot-cap analysis (3037–3114) filters `UNI_TYPE=="Public"` and treats `UNIVERSITY`
  as "the SUC," but since `UNIVERSITY`/`UNI_TYPE` describe the undergrad school, this cannot identify
  actual SUC medical-program enrollment, let alone foreign-slot compliance in an MD freshman class.
- Section E's "Select institution" (3126) score-distribution viewer is fine as a descriptive NMAT-score
  tool but its "PLE pass rate (observable)" KPI (3141–3144) inherits the same unsupported per-institution
  attribution.
- The same issue reaches into my Tab 7 scope: Table 27/30 "Confirmed PLE alignment by university type"
  and Tab 9's subtest-by-university-type comparisons describe undergraduate-school type, not
  medical-school type; the tab captions ("University Type Analysis," "per-HEI") should be relabeled to
  make clear this is the applicant's baccalaureate institution.

Fix: either drop Tab 13 Sections B/D/E entirely (the data cannot support them, per the brief's
explicit instruction to mark unsupported claims as CRITICAL) or relabel every element to "undergraduate
institution of examinees who later matched a PLE passer record" and remove the CHED-eligibility ✅/🔴
framing, which implies an authority the data does not have.

### 04-06 (HIGH) — Retroactive application of a not-yet-effective policy

CMO §IV.A.2.a caps foreign enrollment "per incoming freshmen class, effective Academic Year 2026-2027."
Section D (3036–3114) applies this cap to `df_trend` = NMAT years 2006–2018 and labels any SUC-year with
>10 foreign NMAT-takers `"🔴 over_cap"`. Recomputed: 99 SUC-year combinations exceed 10, e.g.
"University of Northern Philippines - Main" shows 281 in 2017, 191 in 2016. Presenting these as
cap violations is doubly wrong: (a) the cap did not exist in 2006–2018, so there is no violation to
report, and (b) even after 2026, the cap applies to admitted/enrolled MD freshmen, not NMAT test-takers
counted by undergraduate-school affiliation (04-05). Fix: caption this section clearly as "illustrative
historical volume, not a compliance check" or remove it.

### 04-07 (HIGH) — Mismatched cohorts juxtaposed in one table row

Section C (2984–3002): for each cut-off/university-type combination, `"Admitted (best records)"` is
computed from `_sub` = `df_trend` (all NMAT years 2006–2018) while `"PLE passers (observable)"` and
`"PLE pass rate (%)"` are computed from `_sub_obs` = `df_obs` (Year≤2014 only). Recomputed for "All"
university types at the 30th-percentile (B4+) cut-off: Admitted = 91,409 (spans 2006–2018) vs. PLE
cohort = 46,609 (spans only 2006–2014) — roughly half the population, yet both numbers sit in the same
table row next to a single "PLE pass rate: 56.45%" figure, inviting the reader to divide 56.45% ×
91,409 and believe that many "admitted" examinees eventually passed, when the rate was never computed
against that larger, more recent group. Fix: either restrict "Admitted" to the same observable window,
or add separate, clearly labeled N columns for each metric's own denominator.

### 04-08 (HIGH) — Tiny per-HEI sample sizes drive binary pass/fail labels

`_hei_threshold` slider defaults to 5 (2908–2911). Recomputed: 539 HEIs qualify at n≥5, of which 342 are
labeled "below benchmark" and 197 "above"; **163 of the 539 (30%) have between 5 and 10 examinees** in
the entire observable window. At n=5, one additional matched/unmatched case moves the rate by 20
percentage points — comfortably enough to flip an institution across the ~43–47% benchmark band computed
in 04-01/04-03. The page presents this as a definitive ✅/🔴 CHED-eligibility signal with no confidence
interval or minimum-n warning stronger than the caption's passing mention of "statistical reliability."
Fix: raise the effective default minimum (or require a Wilson/Clopper-Pearson interval before assigning
status), and never default-display a threshold this low for a page that names specific institutions.

### 04-09 (HIGH, SUSPECTED) — Unaddressed CMO provisions presented as if covered

The CMO's SUC equity carve-out (GIDA/IP applicants, §IV.A.1) and its core "average national passing
percentage" benchmark (§IV.B.1.b) have no corresponding fields anywhere in the 54-column schema (no
GIDA/IP flag, no PRC-published national pass-rate series). Tab 13 never states this gap; its caption
(2811–2815) instead asserts the tables are "Supporting evidence for the amended NMAT cut-off score
policy" without qualification. A reader has no way to know from the page itself that entire clauses of
the CMO cannot be evaluated with this dataset.

### 04-10 (MEDIUM) — Unbounded repeat-taker tables

`st.dataframe(first_last[display_cols]..., use_container_width=True)` (2298–2303) and
`st.dataframe(appno_matches[display_cols]..., use_container_width=True)` (2316–2319) render every
matching row with no `head()`/pagination/row cap. Under default (no sidebar) filters this is up to
33,713 repeat-taker rows (recomputed: 33,713 PERSON_KEYs with >1 unique `APPNO_CLEAN` in 2006–2018,
matching the 25% figure in CLAUDE.md). `data_aggregator/page_08_*` mirrors this exact unrestricted logic
and produced `page_results/08_repeat_takers.md` at **8,692,662 bytes** and a companion CSV at
**10,271,620 bytes** (both file sizes confirmed directly on disk), which is strong evidence the same
unbounded pattern is live in dashboard.py's interactive Streamlit table too (Streamlit's `st.dataframe`
virtualizes rendering so it won't crash the browser, but any "download as CSV"/export built from the
same underlying frame would reproduce the aggregator's 8–10 MB output). Fix: cap displayed/exported
rows or add explicit top-N controls.

### 04-11 / 04-12 / 04-13 (LOW) — Cosmetic / hygiene

- 04-11: `df.groupby(...).agg([..., lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)])` (2008)
  produces pandas' default `<lambda_0>`/`<lambda_1>` column labels with no rename step, unlike every
  other quantile computation in the file which uses named `q25_year_gap`/`q75_year_gap`-style keys
  (e.g. 2481–2482). Purely a display-polish issue.
- 04-12: `pct_table()` (322–332) does `df.dropna(subset=[group_col, cat_col])` before computing
  percentages; used at 2036 and 2043–2044 on `PercentileBin`, which is null for 1,306 of 64,501 (2.0%)
  observable rows (recomputed). Percentages in Figures 21/22/Table 25 are silently computed over
  the remaining 98%, with no on-page note.
- 04-13: `_v = "exodus_v1"` (line 270) is assigned and never used. It happens to still function as a
  manual cache-buster only because `st.cache_data`'s key includes the function's source text, so editing
  this string forces recomputation on next deploy — but that mechanism is undocumented and would silently
  stop working if anyone "cleans up" the apparently-dead variable.

---

## 4. Shared infrastructure audit

**Data loading (`load_data_and_subsets`, lines 268–296, `@st.cache_data(show_spinner=False)`):**
- Cache key: function takes no arguments, so the cache key is effectively fixed; Streamlit invalidates
  it when the function's *source* changes (hence the `_v` cache-buster convention, 04-13) but **not**
  when the underlying parquet file's *contents* change on disk with the same path — if the parquet is
  regenerated in place without a code redeploy, the running app keeps serving stale cached data until
  someone manually clears the cache or restarts. This is a real staleness risk given the pipeline
  regenerates `NMAT_Exodus.parquet` in place (per CLAUDE.md's pipeline description).
- `st.cache_data` (as opposed to `st.cache_resource`) returns a fresh copy of the cached object on every
  call (Streamlit serializes/copies the return value specifically to prevent mutation from leaking back
  into the cache). I traced every caller of `F[...]` (built once per script run via `filter_df`, itself a
  boolean-mask selection that always returns a new pandas object) and found **no in-place mutation of a
  `subsets[...]`/cached object without an explicit `.copy()`** in tabs 7–13 — most tabs that later assign
  new columns do call `.copy()` first (e.g. 2430, 2494–2495, 2571, 2588, 2680); the few that don't (1996,
  1997, 2158, 2330–2331) only ever read from the frame, never assign into it. **No confirmed mutation
  bug**, but this pattern is fragile — the next contributor who adds a `df["x"] = ...` to a `with tab7:`
  block without checking for `.copy()` will get a `SettingWithCopyWarning` at best, silent no-op at worst.
- `dfall = df` (line 275) aliases rather than copies the post-`ensure_required_columns` frame into the
  `"all"` subset entry; harmless today only because `st.cache_data`'s return-value copy already isolates
  the caller from the cache's internal storage.

**Sidebar filters (667–685) / `filter_df` (299–319):** Year/UNI_TYPE/CourseGroup/Sex defaults are "all
options selected" so an untouched sidebar reproduces the full cohort. `ple_status` filtering is
deliberately restricted to `bestobservable`/`uniobservable` only (line 697) — correct, since applying a
PLE-status filter to non-observable subsets (e.g. `F["trend"]` used by Tab 8) would make no sense.
Verified every tab in my range reads exclusively from `F[...]` (never from the raw
`dfbesttrend`/`dfbestobservable`/`subsets[...]` module-level names, which are only used pre-tab to
populate the sidebar widget option lists at 669–672) — **no filter-bypass ("looks filtered but isn't")
bugs found** in pages 7–13.

**Constants/palettes (40–100):** `BIN_ORDER`, `PALETTE_UNI/COURSE/PLE`, `BIN_COLORS`, `NUMERIC_COLS`,
`BOOL_COLS`, `REQUIRED_PIPELINE_COLS` all check out against actual column names/values in the parquet;
bin orientation is correct (item 3, section 0). `to_bool_series` (122–137) correctly round-trips the
string-typed boolean columns identified in shared context (`HasCEMMatch`, `HasTRUErawScores`,
`AllRawComponentsPresent`) via an explicit string-to-boolean mapping before any `== True` comparison —
this defuses the `bool("False") == True` truthiness trap for every column in `BOOL_COLS` and for any
column routed through `count_true_flags()` (166–169); I found no `== True`/`if df[col]` comparisons in
tabs 7–13 against a raw un-converted string boolean column.

---

## 5. "Missing but supportable" — constrained to the 54 available columns

Within pages 7–13's remit, and using only columns confirmed to exist in `NMAT_Exodus.parquet`:

- A genuine PLE **pass rate** (not match rate) is not directly computable, but the page could at least
  narrow the "match" framing's error by restricting the denominator to people whose `PLE_YEAR_GAP` window
  has plausibly closed (Tab 7 already does something like this via the observable-cohort restriction —
  that logic could be surfaced as an explicit caveat on Tab 13's "pass rate" labels instead of being
  silently assumed).
- `PLE_MATCH_CONFIDENCE` and `PLE_MATCH_METHOD` exist and are unused anywhere in Tabs 7–13 as a
  reliability/quality overlay — e.g., Tab 7's Table 27/Table 30 or Tab 13's per-HEI table could show what
  fraction of "confirmed" matches are lower-confidence `MANUAL_APPNO_MATCH`/`DETERMINISTIC_APPNO` (2,776 +
  91 = 2,867 of 49,986, per shared context) versus `EXACT` (54,437 — note this total already exceeds
  49,986, another facet of the 3-inconsistent-counts problem the brief flags), giving readers an explicit
  match-quality caveat instead of a flat, unqualified "confirmed."
- `CITIZENSHIP_FINAL`/`FOREIGNER_STATUS` exist and are used narrowly (Tab 13 Section D only); a
  foreigner-status breakdown of Tab 7's PLE alignment tables (Table 27–30) would be directly computable
  and is currently absent, despite citizenship being a first-class column in this dataset.
- No column identifies the medical school actually attended/enrolled (04-05) — this is a genuine schema
  gap, not merely an unused-column opportunity; it cannot be worked around with existing columns and
  should be stated as a hard limitation on Tab 13, not glossed over.
