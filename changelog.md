# Changelog — NMAT Analysis

All notable changes to this project are documented below.

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
