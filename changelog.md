# Changelog — NMAT Analysis

All notable changes to this project are documented below.

---

## [2026-08-14] — PLE Identity-Propagation & Sentinel-Value Fix (chain 1→2→4→5 re-run)

A follow-on pass found five further defects in the matcher and pipeline that the RC-0/O-24
remediation below did not catch, and re-ran the chain 1→2→4→5 against the live parquet.

**Fixes:**
- **`get_ple_info()` name-only fallback** (the most consequential): it re-applied a name-only match
  to *every* row sharing that name, even after `disambiguate()` had already adjudicated a single
  `MATCHED_APPNO` for that name — silently undoing the disambiguator and crediting one PLE passer
  record to multiple distinct people. Restricted the fallback to rows with no `MATCHED_APPNO`.
  Effect: names with 2+ distinct passer `PERSON_KEY`s fell **1,624 → 4**; people involved
  **3,256 → 8**; those with conflicting birthdates among them **232 → 1**.
- Person-level `IS_PLE_PASSER` propagation now keys on `PERSON_KEY` (name+DOB), not name alone.
- **`NMS_PER_num`'s `-1` sentinel (2,866 rows) fixed at source** in Pipeline 1 — now `NaN` instead
  of silently passing every `< 40` predicate (`-1 < 40` is `True`). `NMS_PER_num` nulls: 1,275 → 4,141.
- **University merge now keys on `(NMA_College, School Type_rec2_FINAL)`**, fixing 416 rows whose
  assigned `UNDERGRAD_UNI_TYPE` contradicted their own source hint (233 of them hinted Private but
  were counted Public).
- **`FUZZY`-derived rows dropped from the fossil `PLE_STILL_UNMATCHED.csv`**, so the
  deterministic-only matching guarantee holds for the full lineage, not just the current source.
  Real historical exposure was 269 usable AppNos, not the 4,810 raw `FUZZY` rows.
- Combined effect: confirmed PLE passers moved from **49,086 to 47,485** (37,420 → **35,746**
  distinct people); observable linkage 45.44% → **43.31%**; linkage by bin reshaped again
  (B1 11.6%→**10.8%**, B4 36.0%→**33.3%**, B10 71.0%→**69.8%**); median percentile (best-record)
  50.0 → **51.0**; `PLE_YEAR_UNCERTAIN` 110 → **79**; `rejected_ambiguous_person` 8,216 → **8,207**;
  non-nested counts (8,218 / 2,775) → **(8,209 / 3,005)**; `UNDERGRAD_UNI_TYPE` Public 37,304 →
  **36,890**, Private 137,476 → **137,711**, Not Specified 1,832 → **2,011**.
- **The below-40th-percentile headline finding is re-quantified, not overturned:** 5,665 of 25,023
  below-40 observable examinees (**22.6%**, was 24.1% of 6,173/25,596) are confirmed PLE passers —
  **740** in the lowest decile (was 795). Ambiguous-key rate among them is **3.3%** (was 3.0%),
  still close to the 3.5% cohort base rate; **5,645 of 5,665** are Filipino (was 6,152 of 6,173).
  The gradient stays monotone (B1 10.8% → B10 69.8%) and the lowest-decile confirmed passers remain
  incompatible with a uniformly enforced 40th-percentile floor.
- **Equal-exposure figures** (accounting for `PLE_DATA.csv`'s 2011–2022 coverage window):
  observable linkage at a fixed 8-year horizon is **38.0%**; below-40 linkage at 8 years is
  **18.3%**.

---

## [2026-08] — Schema & Matcher Remediation (chain 1→5, RC-0/O-24 fixes, docs rewrite)

A full-repo audit (12 specialist agents + orchestrator verification) found that the shipped
54-column `NMAT_Exodus.parquet` had two identity-resolution defects in its PLE matcher and no
generating code at all for its final column-slimming step. This remediation fixed both at the
source and rewrote every downstream consumer and every piece of project documentation against the
corrected data. Full detail: `docs/pipeline_architecture.md` §7, `.claude/audit/_ORCHESTRATOR_FINDINGS.md` (O-1..O-24).

**Data-layer fixes (Pipelines 1–5):**
- **RC-0 (most consequential defect found):** `2_PLE_Matching_Pipeline.ipynb`'s `disambiguate()`
  had a hard `PERCENTILE_FLOOR = 40` step that discarded and outright rejected PLE-match
  candidates scoring below the 40th percentile — the exact population and exact CMO threshold this
  project studies. Removed. Identity now resolves only on year-gap, DOB/sex, and latest-year
  evidence; name-collision ties are rejected as ambiguous, never decided by score.
- **O-24:** the documented DOB/sex identity check was dead code — `BDATE_CLEAN` was added to the
  DataFrame after the row-dict snapshot `disambiguate()` reads from, so it never actually ran, in
  any historical execution. Fixed by reordering the assignment.
- Combined effect: confirmed PLE passers moved from 49,986 to **49,086**; observable per-bin
  linkage rate reshaped substantially (B1 8.1%→11.6%, B4 25.9%→36.0%, B10 76.6%→71.0%).
- **A previously-published finding is withdrawn**: the 21-point B4→B5 "policy discontinuity" and
  the regression-discontinuity recommendation built on it. Corrected, the step is 9.6 points, in
  line with the rest of the gradient — it was substantially an artefact of the matcher's own
  percentile floor.
- **New headline finding**, replacing it: 6,173 of 25,596 below-40th-percentile observable
  examinees (24.1%) are confirmed PLE passers — 795 in the lowest decile (B1).
- `IS_BEST_NMAT_RECORD` unified to one unbiased rule for every person (was silently using a
  different rule for PLE passers than everyone else, dropping 1,311 people from every
  person-level count).
- Added `IS_OBSERVABLE_COHORT`, `IS_BEST_OBSERVABLE_RECORD` (the correct observable-cohort
  filter — `IS_BEST_NMAT_RECORD & Year<=2014` silently drops 3,721 people), `PERSON_KEY_AMBIGUOUS`
  (6,148 keys with contradictory SEX, exposing `PERSON_KEY` name-collision risk),
  `PLE_MATCH_OUTCOME`, `PLE_YEAR_UNCERTAIN`.
- Removed `IS_PLE_ANALYSIS_SAFE` (byte-identical duplicate of `IS_PLE_PASSER`), `NMA_College`,
  `AllRawComponentsPresent`, `CalcVsDerivedMismatch`, `name_based_assessment`, `HasCEMMatch`
  (byte-identical to `HasTRUErawScores`).
- Renamed `UNIVERSITY`/`UNI_TYPE`/`UNI_LOCATION`/`CourseGroup` to `UNDERGRAD_*` — this data has no
  medical-school identifier; the old names invited institution-level PLE claims the dataset cannot
  support (proof: UP Diliman, which has no College of Medicine, shows 1,914 confirmed PLE passers
  under the old `UNIVERSITY` column).
- **Pipeline 5 (`5_Slim_Exodus.py`) added** — the 118→53 column slim previously had no generating
  code at all; it is now explicit, deterministic, and self-asserting (structural hard-fail checks
  + non-blocking reference-count warnings, recorded in `dataset/EXODUS_MANIFEST.json`).
- Clarified the stored-total mismatch: 42.24% of the whole CEM file (107,422/254,308) and **56.45% of the 99,316 NMAT-matched records that
  carry a stored total** (31.33% of all rows) — the old figure divided the mismatch count by the
  wrong (and separately wrong) denominator.
- Result: `dataset/NMAT_Exodus.parquet`, 178,927 rows × **53 columns**, md5
  `72b2808bb8bb9c3594980c5735f814e1`, shipped as 3 byte-identical copies (`dataset/` + both live
  dashboard folders), verified by `pytest tests/` (36 passed).

**Dataset hygiene:** removed 3 confirmed-dead files with zero readers anywhere in the
repo — `dataset/NMAT_Exodus.csv`, `dataset/output/NMAT_FINAL.parquet`,
`dataset/UNIVS_ARCHIVED.csv`. `dataset/NMAT_Exodus.parquet.bak` (118 cols) is deliberately kept as
the sole remaining full-column audit trail. See `dataset/DATASET_MANIFEST.md`.

**Consumers migrated to the new schema:** `streamlit_dashboard/CHED_relevant_dashboard/`,
`data_aggregator/` (all 13 pages, `run_all.py` now resolves paths from any cwd), `tests/` (new
`test_data_invariants.py`, 36 tests asserting the schema contract).

**Forensic audit suite consolidated** into a single `forensic_audit/forensic_audit.py` (was 3+
separate scripts across several iterations); unsupported claims from earlier audit runs withdrawn.

**Documentation rewritten wholesale** against the live 53-column file and the corrected pipeline:
`README.md`, `docs/data_dictionary.md`, `docs/pipeline_architecture.md`, `CLAUDE.md`. Every count
in the rewritten docs was independently re-verified against `dataset/NMAT_Exodus.parquet`, not
carried forward from prior drafts. `RShiny_Dashboard/`, `reports/`, and root `dashboard.py` /
`dashboard.py.bak` are now explicitly marked legacy/not-maintained rather than presented as live
deliverables.

---

## [2026-07-28] — Export & Deployment Polish

| Commit | Description |
|--------|-------------|
| `7fa0f18` | Fix image paths in complete_markdown export (`viz/` → `../viz/`) |
| `113d00d` | Add `export_markdown.py` with full markdown + 14-chart PNG export, lazy generation trigger, one-click `start_dashboard.ps1` launcher |
| `619a150` | Fix `HasTRUErawScores` / `StoredVsDerivedMismatch` dtype bug — string columns now properly coerced to bool/float |
| `43b5fb5` | Remove `.artifacts` dir, add `.temp/` to `.gitignore` |
| `830fc67` | Increase vertical spacing in subplot titles (0.12 → 0.22) |
| `e69dd6c` | Remove explicit `engine='pyarrow'` (auto-detect), replace `text_auto='.1f'` with `True` for Pylance stubs |
| `ec8ec8c` | Fix Pylance ExtensionArray rounding warnings — use `to_numpy(dtype=float)` instead of `.values.round()` |
| `aa0a947` | Add `runtime.txt` (Python 3.12), remove `use_threads=True` for Streamlit Cloud compatibility |
| `c78670a` | Add `.gitignore` for standalone dashboard repos, update CHED README, remove prayer.md |

## [2026-07-27] — CHED Dashboard: Reviewer Revisions & Verification

| Commit | Description |
|--------|-------------|
| `85b6f33` | Restructure compute scripts to 6-tab match, add `verified_true/` verifier outputs with full cross-check logs |
| `2b02ec7` | Fix foreign context section to use ALL records (not best-record) — matches data-aggregator page 04 |
| `6851005` | Full reviewer revision: remove compliance framing, vectorize bin filtering, dynamic captions, synthesis tab, schema validation |
| `7932bc6` | Remove stale planning docs and `ched_compute` artifacts |
| `c921943` | Fix PyArrow `value_counts()` / crosstab numeric coercion in CHED dashboard |

## [2026-07-27] — CHED Dashboard: Initial Build

| Commit | Description |
|--------|-------------|
| `4e230ea` | Context doc for Claude Sonnet 5 — prayer.md |
| `0f9b4f9` | Final cleanup and documentation |
| `3b914e2` | Remove computation button, fix surrogate unicode in dashboard.py |
| `05e41e0` | CHED dashboard complete — all 9 scripts + 10-tab dashboard |
| `352e122` | CHED dashboard Phase 0/1 complete |
| `428f9f0` | CHED dashboard council decision + computation suite |

## [2026-07-27] — Core Pipeline & Data Refinements

| Commit | Description |
|--------|-------------|
| `be08185` | Move docs to `docs/`, archive pipeline results to `.artifacts/` |
| `76f1bf2` | Comprehensive data dictionary for `NMAT_Exodus.parquet` (54 columns) |
| `60acfc1` | Pipeline architecture document with Mermaid charts |
| `4cf444c` | Fix `data_aggregator` to point to `NMAT_Exodus.parquet` |
| `9b084b2` | Create `NMAT_Exodus_Lite.parquet` (54 cols, 10.5 MB, 62% smaller) |
| `39d3284` | Archive planning docs, remove `fix_dashboard.py` |
| `49cce08` | Fix 3 stale `NMAT_Ultima` error messages → `NMAT_Exodus` |
| `86c2bdb` | Add CHED Compliance page (Page 13) to Streamlit dashboard |
| `f56fb55` | Audit findings — 5 critical bugs fixed |
| `632b5bd` | Restore emoji icons in dashboard.py tab labels |

## [2026-07-27] — Dashboard & R Shiny Migration (I decided that Streamlit would be the best approach compared to Rmarkdowns)

| Commit | Description |
|--------|-------------|
| `87c7d4e` | R Shiny dashboards now load from `NMAT_Exodus.parquet` |
| `00b8eee` | Streamlit dashboard now loads from `NMAT_Exodus.parquet`, cache busted |
| `16e2fc6` | Pipeline 4 & dashboard migration complete |
| `418f0bc` | Pipeline 4 — `NMAT_Ultima` → `NMAT_Exodus` with citizenship integration |
| `38bb2ff` | Remove obsolete `.ipynb`, replacing with `.py` version |

## [2026-07-26] — Project Setup

| Commit | Description |
|--------|-------------|
| `1f81910` | Initial commit — NMAT Analysis project scaffolded |
| `e112537` | Gitignore vault/ directory |
| `f25b2cc` | Fix 00_RUN_ME.ipynb description |
| `24e271e` | Remove rapidfuzz dependency, update requirements.txt |
| `549eeb5` | Add 00_RUN_ME.ipynb master orchestrator to README |
| `9a5272b` | Update README and add LICENSE (GNU GPL v3) |

---

**Total commits:** 36
**Latest:** `7fa0f18` (2026-07-28)
**Main branch:** `master`
