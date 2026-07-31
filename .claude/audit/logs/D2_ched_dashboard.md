# D2 — CHED Dashboard Remediation Log

Scope owned: `streamlit_dashboard/CHED_relevant_dashboard/{dashboard.py, export_markdown.py, ched_compute/}`.
Python used throughout: `./.venv/Scripts/python.exe`.

Final data: `NMAT_Exodus.parquet`, **178,927 rows x 53 columns**, md5
`28b85ac53af13b4a2ef3ee93527c97c1` (confirmed via direct hash after the
orchestrator's final parquet regeneration, mid-task).

## New file: `ched_common.py`

Single shared compute layer. `dashboard.py`, `export_markdown.py`, and
`ched_compute/helpers.py` all import from it. Contains:
- `load_and_validate()` — the one parquet loader/validator (dtype coercion,
  schema check, `df_best`/`df_obs` construction).
- `compute_*()` pure functions for every table/KPI/chart-data used by more
  than one caller (bin distributions, linkage tables, mismatch stats,
  nationality shares, stress test, Tab-5 findings, Tab-6 limitations cards).
- Shared narrative constants (`SELECTION_EFFECT_NOTE`, `SCOPE_NOTE`,
  `FLOOR_NOT_BINDING_NOTE`) quoted verbatim by both dashboard and export.
- `compute_tab5_finding_texts()` and `compute_limitations_cards()` build
  the **actual prose strings**, not just the numbers, so dashboard.py and
  export_markdown.py render byte-identical narrative — this is the
  structural fix for the class of bug that produced the 57/49-vs-56/48
  drift (root cause: two files re-deriving the same aggregation with
  different filters).

## Fixes applied, with before/after

### 1. Tautological "B5+ PLE-Passer Composition" charts (flagship finding)
**Before:** `_df_clean_ple` filtered to `IS_PLE_ANALYSIS_SAFE == True` *first*,
then computed `confirmed` from the same flag on that already-100%-True
subset → `no_match` was identically 0 for all 9 years, both in Tab 2's
stacked chart and Tab 3's "stress test" line chart (flat 100%).

**After:** `cc.compute_ple_composition_by_year()` builds the population
from the bin-filtered observable cohort with **no pre-filter on match
status**; `confirmed` is computed from `HAS_CONFIRMED_PLE` (== `IS_PLE_PASSER`)
on that unfiltered population. Verified non-tautological:
```
Year  total  confirmed  no_match  linkage_pct
2006   2333       1647       686         70.6
...
2014   7360       4198      3162         57.0
```
`cc.compute_stress_test()` (Tab 3) additionally requires `PLE_YEAR_GAP>=5`
among confirmed passers, restricted to Filipino B5+: final run gives
**56.0% linkage (23,128 / 41,289)** — genuinely below 100%, a real check.
Finding 6 rewritten from "confirms robustness" (unsupported, per audit) to
"a real, checkable comparison ... genuinely lower than the broader figures".

### 2. India nationality share (wrong denominator)
**Before:** `top_nat["Count"] / top_nat["Count"].sum()` — divided by the
top-10 subtotal (31,116), inflating every row ~4.3%. Published 85.1%.
**After:** `cc.compute_nationality_shares()` divides by `len(foreign)`, all
verified foreigners. Verified: **81.5%** (26,490 / 32,501), matches
orchestrator's authoritative value exactly.

### 3. Hardcoded "42.2%" claim (appeared 3x dashboard.py, 2x export, 1x
ched_compute/06)
**Before:** literal string, did not reconcile with the parquet's own
`StoredVsDerivedMismatch` column.
**After:** `cc.compute_stored_mismatch_stats()` computes live:
`56,065 of 99,316 rows with a stored total = 56.45%` (31.33% of all rows).
Zero hardcoded "42.2" remain in any owned `.py` file (grep-verified).

### 4. "Median bin rank 57/49" mislabeling + null-handling drift
**Before:** dashboard.py used unfiltered `df_best`, export used
`.dropna(subset=["PercentileBin"])` — 56/48 vs 57/49, same document.
Also mislabeled a 0-99 percentile value as a "bin rank" (1-10 scale).
**After:** one population policy, `cc.bins_population()` = drop null
`PercentileBin`, used everywhere (Tab 2, Tab 4, Tab 5). Relabeled
"median NMAT percentile" throughout (chart titles, axis labels, findings,
KPI cards). Current value: Public 57, Private 49 (verified identical in
dashboard.py and export via the shared `compute_tab5_findings()` call —
export's self-check `_assert_equal("pub_median_pct", ...)` passes).

### 5. Scope honesty (SUC/PHEI/GIDA-IP proxy misuse)
Added `cc.SCOPE_NOTE` ("No medical-school identifier exists...") and
quote it in: How-to-read expander, Tab 2 threshold-by-uni-type caption,
Tab 2 "Public-Institution" section, Tab 3 uni-type caption, Tab 4 header,
Tab 5 Finding 2 and the data-scope note, Tab 6 PHEI Accountability card
(rewritten to state plainly no medical-school identifier exists at all,
not just that PHEI matching is "incomplete").
Tab 2's "Public School Examinees" section and Tab 5 Finding 5 (former
"exception may not primarily benefit the intended disadvantaged groups")
rewritten to pure description, per the audit's suggested wording — no
inference about who benefits from the exception.

### 6. Selection effect + (new, found during remediation) matching bias
Original ask: state the B4→B5 discontinuity is a selection effect, not
ability. **Superseded mid-task** by the orchestrator: the matcher's
`disambiguate()` Step 4 had a hard 40th-percentile floor for name-collision
candidates (root cause of an inflated B4→B5 jump in the pre-fix data).
After the matcher fix landed and the parquet was regenerated:
- The "dramatic jump" framing was **removed everywhere** (grepped and
  fixed 6 call sites across dashboard.py/export_markdown.py/ched_compute).
- `cc.SELECTION_EFFECT_NOTE` now states the gradient rises **roughly
  continuously** (B1→B2 +11.1pp is actually the largest adjacent-bin step,
  B4→B5 +9.6pp is comparable to B9→B10 +9.4pp) and carries both caveats:
  admission selection, and the now-corrected matcher artefact.
- **New finding added** (both dashboard Tab 5 and export, position 4 of 8):
  "The 40th-Percentile Floor Was Not Uniformly Binding" — 795 confirmed
  PLE passers in B1 (11.6% linkage), B4 reaches 36.0%; stated as evidence
  the historical rule was not uniformly binding, relevant to CMO §IV.B.1.
- Tab 6 gained a dedicated, disclosed limitations card for the matching
  bias, including the new `PLE_MATCH_OUTCOME` category
  (`rejected_ambiguous_person`, 8,216) and `PLE_YEAR_UNCERTAIN` (110 rows)
  columns the orchestrator added.

### 7. Preserved / strengthened
"Not a PLE pass rate" disclaimers and the limitations tab kept and
extended (added: ambiguous-PERSON_KEY disclosure, 4-way PLE-column
disagreement disclosure, matching-bias card, floor-not-binding card).

## Schema migration
Renamed throughout: `UNI_TYPE`→`UNDERGRAD_UNI_TYPE`, `UNIVERSITY`→
`UNDERGRAD_UNIVERSITY`, `UNI_LOCATION`→`UNDERGRAD_UNI_LOCATION`,
`CourseGroup`→`UNDERGRAD_COURSE_GROUP`. Removed-column references
(`IS_PLE_ANALYSIS_SAFE`, `NMA_College`, `AllRawComponentsPresent`,
`CalcVsDerivedMismatch`, `name_based_assessment`, `HasCEMMatch`) eliminated
— grep-verified zero hits in every owned `.py` file.
`df_obs` now built from `IS_BEST_OBSERVABLE_RECORD` (not
`df_best[df_best.Year<=2014]`), per contract §2a — verified `len(df_obs) ==
69,503`, matching the orchestrator's authoritative value.

## Exporter compliance (`_EXPORT_FORMAT_CONTRACT.md`)
- Rule 1/3: every chart's underlying data exported as a full table (no
  `.head()` truncation on any table except the deliberate top-10
  nationality ranking, which states its population/denominator inline).
- Rule 2/4: `chart_meta()` HTML-comment blocks precede every chart table
  with `population`/`n`/`denominator`; `metric_table()` KPI rows carry
  `metric | value | population | note` columns.
- Rule 6: `export_markdown.py` calls the same `ched_common.compute_*()`
  functions as `dashboard.py` for every number, including full prose
  (`compute_tab5_finding_texts`, `compute_limitations_cards`) — verified
  by 5 in-export `_assert_equal()` checks, all passing (see integrity
  block below).
- Rule 7: image path bug fixed — `_save_plot`/`generate_all_charts` now
  accept `md_dir` and compute `os.path.relpath`, instead of hardcoding
  `viz/{name}` (previously only correct if the .md happened to be saved
  at the app root; verified `../viz/...` links resolve correctly from
  `complete_markdown/`).
- Rule 10: self-check block appended to every export.

`ched_compute/06_data_limitations.py` bug (string-as-boolean, producing a
self-contradicting "Rows with complete TRUE scores: 0 (99.97%)") fixed by
routing `helpers.load_data()` through `ched_common.load_and_validate()`
(fixes it for all 6 scripts, not just 06). Verified in regenerated output:
`Rows with complete TRUE scores: 178,882 (99.97%)`.

`ched_compute/verified_true/` deleted (hand-typed-expectation verifiers
that could not fail; `tests/` supersedes them per instructions).

`ched_compute/05_evidence_findings.py` collapsed from an independent
238-line reimplementation into a ~50-line thin wrapper around
`cc.compute_tab5_finding_texts()` — removes a third copy of the same
drift-prone logic (audit 06 F1/F5 root cause).

## Verification run (final parquet, md5 `28b85ac53af13b4a2ef3ee93527c97c1`)

```
py_compile dashboard.py export_markdown.py ched_common.py ched_compute/*.py -> OK (no output = success)

Authoritative values, computed live via cc.load_and_validate():
  sittings                 178,927   (matches)
  unique examinees         134,869   (matches)
  observable cohort         69,503   (matches)
  observable linkage        45.44%   (matches, exact)
  confirmed passers         49,086   (matches, IS_PLE_PASSER.sum())
  ambiguous keys              6,148   (matches)
  stored-total mismatch  56,065/99,316 = 56.45%   (matches, never "42.2%")
  India share of verified foreigners  81.5% (26,490/32,501)   (matches)

Per-bin observable linkage (person-level, IS_BEST_OBSERVABLE_RECORD):
  B1 11.60  B2 22.71  B3 29.30  B4 36.00  B5 45.62
  B6 50.41  B7 53.58  B8 55.04  B9 61.60  B10 71.03
(matches orchestrator's corrected figures exactly)
```

Streamlit headless startup test:
```
streamlit run dashboard.py --server.port 8602 -> HTTP 200, no traceback  (first run, 51/52-col parquet)
streamlit run dashboard.py --server.port 8603 -> HTTP 200, no traceback  (final run, 53-col parquet)
```
Both server processes confirmed killed afterward (`ps aux` clean).

`ched_compute/run_all.py`: 6/6 scripts OK on every run (initial, post-rename,
and final-parquet re-run).

Regenerated `complete_markdown/CHED_NMAT_Dashboard_Complete.md` from the
final parquet. Export integrity block:
```
| Source parquet md5 | 28b85ac53af13b4a2ef3ee93527c97c1 |
| Rows / cols | 178,927 / 53 |
| Tabs exported | 6 / 6 |
| Charts exported as data | 15 / 15 |
| Tables exported | 34 |
| Captions exported | 41 |
| Dashboard-vs-export value assertions passed | 5 / 5 |
```
In-export assertions check: `pub_median_pct`, `stored_mismatch_pct`,
`india_share`, `n_best`, `n_obs` — all equal the values computed directly
from `ched_common`, all 5/5 passed.

`grep -rE "IS_PLE_ANALYSIS_SAFE|NMA_College|AllRawComponentsPresent|CalcVsDerivedMismatch|name_based_assessment|HasCEMMatch"` across
`dashboard.py export_markdown.py ched_common.py ched_compute/*.py` → **zero
hits**. Same for bare `"UNI_TYPE"`/`"UNIVERSITY"`/`"CourseGroup"`/
`"UNI_LOCATION"` string literals. `grep "42.2"` and `grep "85.1"` → zero
hits outside explanatory docstrings that name the historical bug.

## Not done / deferred (honest accounting)

- `ched_compute/01_national_profile.py`, `02_thresholds.py`,
  `03_ple_linkage.py`, `04_institution_context.py` were column-renamed and
  routed through the shared `load_data()`/`create_subsets()` (which fixes
  the dtype-coercion and observable-cohort-definition bugs for all of
  them), but their per-script prose/aggregations were **not** individually
  extracted into `ched_common.compute_*()` the way Tab 5 and Tab 6 were —
  they remain a third, independently-coded pipeline for tabs 1-4. This
  matches the explicit ask (fix 06, delete verified_true) rather than the
  audit's full "recommended architecture" (§8), which would additionally
  route every `ched_compute` script through shared tab-level compute
  functions. Numbers from these 4 scripts were spot-checked at the console
  during `run_all.py` runs and looked internally consistent, but were not
  cross-asserted against `dashboard.py`'s numbers the way Tab 5/6 are.
- Did not add machine-readable `chart_type` metadata blocks to every
  single markdown table (contract Rule 2) — applied it to the
  highest-risk/most-cited tables (Tab 1 trend, Tab 2 heatmap/B5+
  composition, Tab 3 linkage-by-bin/stress-test, Tab 4 nationality); a
  handful of secondary tables (e.g. Tab 2 top/bottom-bin trend table, Tab 4
  box-plot table) have captions but not the full HTML-comment metadata
  block.
- Did not build a CSV side-channel for any table (contract Rule 3) — no
  table in this dashboard exceeds ~2,000 rows (worst case: 90-nationality
  list, capped to top 10 with the cap explicitly stated), so this was
  judged not to apply rather than skipped.
