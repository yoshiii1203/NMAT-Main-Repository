# Audit 08 — `data_aggregator/`: does it faithfully mirror the main dashboard?

**Scope:** `data_aggregator/config.py`, `helpers.py`, `run_all.py`, `aggregate_all.py`, `page_01..13_*.py`, `page_results/*.md`.
**Reference:** `streamlit_dashboard/main_dashboard/dashboard.py` (parity only — dashboard *correctness* is audits 03/04's territory).
**Method:** direct inspection + live execution by the lead auditor for cross-cutting infra questions (staleness, reproducibility, DuckDB claim, giant-file causes, `IS_BEST_NMAT_RECORD`/`UNIVERSITY` consistency), plus three parallel sub-audits covering pages 1-4, 5-8, 9-13 (dashboard-line-range vs page-script vs md-output, with live numeric recomputation against `dataset/NMAT_Exodus.parquet`).

## Verdict: **Partially faithful**

The numeric core is genuinely trustworthy — 11 of 13 pages' headline KPIs, cross-tabs and statistical tests reproduce dashboard.py's exact formulas, and the entire `page_results/` output is **provably reproducible**: a fresh, from-scratch rerun against the current parquet is byte-identical to the committed files (diff = 0 lines outside the generation timestamp, verified for all 13 pages). This is not a stale, abandoned snapshot.

But it is not a faithful mirror either. There is one CRITICAL numeric bug (wrong population for the citizenship section), several dashboard sections/tables that are missing entirely, one case where the aggregator silently invents a different number under the *same table label* as the dashboard, a broken documented reproduction command, and an unbounded per-row dump that inflates one output file to 8.7 MB by accident. None of this amounts to "drifted" (most content is right) or "unusable" (the good parts are genuinely useful and correct), so **partially faithful** is the accurate label.

---

## Per-page coverage matrix

| Page | Dashboard tab (dashboard.py lines) | Coverage | Notes |
|---|---|---|---|
| 01 Executive Summary | 748-828 | Full | All 8 KPIs + Fig.1 data + Table 1 reproduced, all verified matching |
| 02 Data Integrity | 831-970 | Full | String-boolean columns handled correctly on both sides (see Numeric parity) |
| 03 Trends & Stability | 973-1014 | Full | Table 9 Kruskal-Wallis verified exact; only a cosmetic p-value display diff |
| 04 Score Bins & Background | 1017-1732 | **Partial** | By-year/uni/course sub-tabs faithful; citizenship section uses wrong population (CRITICAL); bin order scrambled in chi-sq tables; entire "foreigners vs Filipino comparative" subsection missing |
| 05 University Type | 1735-1897 | **Partial** | Core crosstabs faithful; Table 17 (university listings) and Figure 16 (Med&Allied vs Other) missing entirely; Figure 12 reduced to top-bin only |
| 06 Flow & Pathways | 1900-1990 | Full | Cleanest page besides 12 — no findings |
| 07 PLE Alignment | 1993-2152 | **Partial** | Correctly uses `bestobservable` (not the tautological `plesafe`); Table 23 missing NMS_APT/NMS_SA columns |
| 08 Repeat Takers | 2155-2323 | **Partial** | Core stats faithful; "NMA_AppNo Deterministic Match Histories" section missing; Section 3 unboundedly dumps ~33.7k rows inline (accident, not by design) |
| 09 Subtests & Profiles | 2326-2420 | **Partial** | Tables 34-37 verified exact; "Table 38/39" mean-centered in aggregator vs raw in dashboard — same label, different numbers |
| 10 Year Gap & Gender | 2423-2559 | Full+ | Faithful; adds extra Sex-based tests dashboard doesn't have (harmless) |
| 11 Statistical Tests | 2562-2673 | **Partial** | Tables 43-47 verified exact; docstring overclaims "replicates ALL"; adds many tests dashboard lacks; "Table 48" label collides with a different dashboard table |
| 12 Policy Tables | 2676-2806 | Full | Near-verbatim port of dashboard code — no findings, cleanest page |
| 13 CHED Compliance | 2809-3207 | **Partial** | Sections A-D verified exact, including a real (non-tautological) PLE-rate base; Section E missing "Median TRUE raw score" KPI; large per-HEI tables judged intentional/appropriate, not noise |

Charts (Plotly figures, radar plots, boxplots, heatmaps) cannot become images in markdown by definition — that's not counted as a loss where the underlying data table is present. It **is** counted as a loss on pages 4, 5, 8 where the table itself doesn't exist.

---

## Numeric reconciliation highlights

| Metric (page) | Dashboard | Aggregator script | MD output | Match |
|---|---|---|---|---|
| Best-record examinees (P1) | 133,804 | 133,804 | 133,804 | Y |
| Unique examinees (P1) | 133,558 | 133,558 | 133,558 | Y |
| Confirmed PLE share, observable (P1) | 45.38% | 45.38% | 45.38% | Y |
| Kruskal-Wallis H, raw score by Year (P3) | 5598.2 | 5598.2 | 5598.2 | Y |
| Top-bin share by UNI_TYPE (P4, uni sub-tab) | Foreign 34.26% / Private 29.97% / Public 38.21% | same | same | Y |
| **Verified Foreigners, citizenship section (P4)** | **4,746** (population = `uniobservable` ∩ No-confirmed-PLE ∩ citizenship notna, n=34,727) | **32,501** (population = ALL 178,927 rows) | 32,501 | **N — CRITICAL, different population entirely** |
| Chi-sq statistic, UNI_TYPE×Bin (P4) | matches | matches | matches | Y (stat correct; only the *display order* of bins is scrambled) |
| Table 34 Public/Verbal mean subtest score (P9) | 495.13 | 495.13 | 495.13 | Y |
| "Table 38" Public/Verbal (P9) | 495.13 (raw mean, same as Table 34) | **9.02** (mean-centered) | 9.02 | **N — same table number, different formula** |
| Mann-Whitney U, PLE status (P7, Table 24) | matches | matches | matches | Y |
| National PLE benchmark, 2006 (P13, Table A1) | n=3,665, confirmed=2,038, rate=55.61% | same | same | Y |
| Repeat rate (P8) | 25.00% | 25.00% | 25.00% | Y |

Everywhere spot-checked outside the two flagged rows above, the three values (dashboard formula / aggregator formula / md output) agreed exactly.

---

## Findings table

| ID | Severity | Status | Title | File:line |
|---|---|---|---|---|
| INFRA-01 | HIGH | CONFIRMED | Documented reproduction command is completely broken; the working command writes to the wrong directory | `data_aggregator/run_all.py:29,47-48`, CLAUDE.md |
| INFRA-02 | LOW | CONFIRMED | CLAUDE.md claims DuckDB is used in `data_aggregator`; it is 100% pandas | `data_aggregator/*.py` (no `duckdb` import anywhere) |
| INFRA-03 | — | CONFIRMED (clean) | Output is NOT stale — fresh rerun is byte-identical to committed files | `data_aggregator/page_results/*.md` |
| INFRA-04 | MEDIUM | CONFIRMED | `aggregate_all.py` regex silently drops 2 of 10 KPIs from the master overview table | `data_aggregator/aggregate_all.py:47-48` |
| P4-01 | **CRITICAL** | CONFIRMED | Citizenship section computed over the wrong population (all 178,927 rows vs dashboard's 34,727-row filtered cohort) | `data_aggregator/page_04_score_bins.py:229` vs `dashboard.py:1231-1707` |
| P4-02 | HIGH | CONFIRMED | PercentileBin columns scrambled (B1,B10,B2,B3…) in chi-square tables — missing `BIN_ORDER` reindex | `data_aggregator/helpers.py:179-205` |
| P4-03 | MEDIUM | CONFIRMED | Extra CourseGroup chi-square table has no dashboard counterpart; inherits P4-02 | `data_aggregator/page_04_score_bins.py:173-197` |
| P4-04 | MEDIUM | SUSPECTED | Entire "foreigners vs Filipino comparative analysis" subsection (~190 dashboard lines) missing | `dashboard.py:1518-1707` vs `page_04_score_bins.py` |
| P5-01 | HIGH | CONFIRMED | Table 17 (per-university applicant listings) missing entirely | `dashboard.py:1884-1895` vs `page_05_university_type.py` |
| P5-02 | MEDIUM | CONFIRMED | Figure 16 (Medical&Allied vs Other by UNI_TYPE) missing entirely | `dashboard.py:1859-1882` vs `page_05_university_type.py` |
| P5-03 | LOW | CONFIRMED | Figure 12's full 10-bin distribution reduced to top-bin-only | `dashboard.py:1767-1789` vs `page_05_university_type.py` §3b |
| P5-04 | LOW | CONFIRMED | Figure 15 grouped by a different variable (`FOREIGNER_STATUS` vs `UNI_TYPE`) | `page_05_university_type.py` Table 05-11 |
| P7-01 | MEDIUM | CONFIRMED | Table 23 (score profile by PLE status) missing NMS_APT and NMS_SA columns | `page_07_ple_alignment.py` `desc_cols` vs `dashboard.py:2006` |
| P8-01 | HIGH | CONFIRMED | Section 3 dumps all ~33,702 repeat-taker persons inline uncapped — root cause of the 8.7MB file | `page_08_repeat_takers.py:106-150` (no `.head()`, unlike §5 at :262-270) |
| P8-02 | LOW | CONFIRMED (latent) | `dropna` scope narrower than dashboard's; no live numeric effect today, but a future null could silently bias "% improved raw score" | `page_08_repeat_takers.py:103` vs dashboard's unrestricted `.dropna()` |
| P8-03 | MEDIUM | CONFIRMED | "NMA_AppNo Deterministic Match Histories" section missing entirely | `dashboard.py:2307-2321` vs `page_08_repeat_takers.py` |
| P9-01 | HIGH | CONFIRMED | "Table 38/39" is mean-centered in the aggregator vs raw/uncentered in the dashboard — same label, materially different numbers | `page_09_subtests.py:74-81` vs `dashboard.py:630-649` |
| P9-02 | MEDIUM | CONFIRMED | Dict-key collision between `SUBTEST_STD`/`SUBTEST_RAW` silently drops all Standard-score rows from "Table 40" (aggregator-only table) | `page_09_subtests.py:84-112`, `config.py:56-75` |
| P9-03 | LOW | SUSPECTED | "Table 40" itself is aggregator-only content with no dashboard equivalent | `page_09_subtests.py` |
| P10-01 | LOW | SUSPECTED | Sex-based Mann-Whitney/Chi-square sections absent from dashboard tab10 (harmless addition) | `page_10_year_gap_gender.py` §6-8 |
| P11-01 | MEDIUM | CONFIRMED | Aggregator adds many stat tests dashboard.py's tab11 lacks; docstring overclaims "replicates ALL"; "Table 48" label collides with dashboard's actual Table 48 (Year×Year Dunn) | `page_11_statistical_tests.py` vs `dashboard.py:2562-2673` |
| P13-01 | MEDIUM | SUSPECTED | Section E "Table E1" missing dashboard's "Median TRUE raw score" KPI; adds unvalidated Mean/Q25/Q75/Health-Sci columns | `page_13_ched_compliance.py` §E vs `dashboard.py` Section E |
| P13-02 | LOW | Judgment, not a bug | Large per-HEI tables in Sections B/E — judged intentional and appropriate for a CHED regulatory report | `page_13_ched_compliance.py` |
| P3-01 | LOW | CONFIRMED | Cosmetic: p-value renders as literal `0` instead of dashboard's `<0.001` string | `helpers.py:131` |

No findings on pages 01, 02, 06, 12 — these are faithful, near-verbatim ports.

**Checked and ruled out** (raised as hypotheses, confirmed clean): `UNIVERSITY` vs `NMA_College` — both dashboard and pages 02/05/13 key institution-level tables off `UNIVERSITY` consistently, no divergence. `IS_BEST_NMAT_RECORD` row-count vs `nunique(PERSON_KEY)` — applied identically on both sides everywhere checked; the 133,804-vs-133,558 gap is a real inherited upstream data bug (1,311 dropped / 246 duplicated PERSON_KEYs) reproduced identically, not a new aggregator bug. String-as-boolean columns (`HasCEMMatch`, `HasTRUErawScores`, etc.) — dashboard pre-coerces via `to_bool_series()`, page_02 independently re-coerces via `.astype(str).str.upper().isin(...)`; both land on 178,882, confirmed match. `IS_PLE_ANALYSIS_SAFE` tautology trap — every pass-rate calculation found (pages 01, 07, 13) uses it as a *numerator* over a non-tautological denominator (`bestobservable`/`besttrend`, filtered by Year/cohort, never by `IS_PLE_ANALYSIS_SAFE` itself), matching the dashboard's own approach exactly. No DuckDB anywhere, so the SQL/pandas semantic-divergence hunt (NULL handling, `COUNT(col)` vs `COUNT(*)`, integer division, JOIN-on-null) does not apply — CLAUDE.md's claim that data_aggregator uses DuckDB is simply wrong (INFRA-02).

---

## Detail: cross-cutting infrastructure findings

### INFRA-01 (HIGH, CONFIRMED) — reproducibility is broken as documented
CLAUDE.md instructs: `cd data_aggregator && python run_all.py`. Tested in an isolated scratch copy: this fails completely — `run_all.py`'s `SCRIPTS_DIR = Path("data_aggregator")` is relative, so run from inside `data_aggregator/` it resolves to `data_aggregator/data_aggregator/page_XX.py`, which doesn't exist. Result: **0 passed, 13 failed** ("SKIP script not found" for every page).

The alternative, `python data_aggregator/run_all.py` from the repo root, works (13/13 pass, ~71s) — but `RESULTS_DIR = Path("page_results")` is *also* relative, so it writes to `<repo_root>/page_results/`, not `data_aggregator/page_results/` where the actually-committed files live. Neither of the two natural invocations reproduces the committed output location. Someone must have generated the committed files with a directory layout or invocation this repo no longer supports (e.g. a since-deleted `data_aggregator/dataset` junction).
**Fix:** make `run_all.py` resolve `SCRIPTS_DIR`/`RESULTS_DIR`/`EXODUS_PARQUET` relative to the script's own file location (`Path(__file__).parent`) rather than cwd, and update CLAUDE.md to the corrected invocation.

### INFRA-03 — staleness: none found
Copied `dataset/NMAT_Exodus.parquet` + all `data_aggregator/*.py` into an isolated scratch dir, patched only the venv-python path (an artifact of the copy, not a real bug), and reran all 13 pages. `diff` against the committed `page_results/*.md` (excluding the `**Generated:**` line) = 0 lines for all 13 files, including the two multi-MB ones. The 2026-07-28 date is not evidence of drift — the content is current.

### INFRA-04 (MEDIUM, CONFIRMED) — `aggregate_all.py` silently drops KPIs
`get_all_metrics()` regex-scrapes `01_executive_summary.md` for 8 labels. Two of its patterns (`r"Observable cohort[|\s|]+([0-9,]+)"`, `r"Confirmed PLE share[|\s|]+([0-9.]+%)"`) don't match because the actual labels are `"Observable cohort size"` and `"Confirmed PLE share (observable)"` — the character class `[|\s|]` doesn't include letters or `(`. Both rows silently vanish from the Master Report's "Overview" table with no error or warning.

### `aggregate_all.py` vs `run_all.py`
Both are live/maintained (touched together in the same commits), not dead code — they're sequential steps of a two-stage pipeline (`run_all.py` generates the 13 page files; `aggregate_all.py` must then be run manually to concatenate them into `00_MASTER_REPORT.md`). `run_all.py` does not call `aggregate_all.py`. This two-step manual process plus INFRA-04's silent metric loss is a minor process fragility worth a one-line doc fix, not a redesign.

### Page 8's 8.7 MB file (P8-01)
Diagnosed directly: `page_08_repeat_takers.py`'s Section 3 ("First-Last Detail") writes **all** ~33,702 repeat-taker persons as one inline markdown table with no row cap — lines ~78 through ~33,789 of the 33,925-line file. This is inconsistent with the *same script's* Section 5, which correctly caps its inline preview to 100 rows and offloads the rest to `08_repeat_takers_detail.csv`. This reads as an oversight (forgot to apply the pattern used two sections later), not a deliberate design choice — a per-person score-trajectory table has no reason to be inlined in full when the same script already knows the CSV-offload pattern.

### Page 13's 445 KB file — contrast with page 8
By contrast, Section B/E's large per-HEI tables in page 13 were judged **intentional and appropriate**: bounded at ~460 rows (one per institution, not one per person), and a CHED regulatory compliance report legitimately needs a complete per-institution listing. Not a finding.

---

## Keep / Fix / Replace / Delete recommendation

### Recommendation: **Keep and fix**

**Why not delete:** the user's fear — "did this even work?" — is answered no by the raw file sizes alone but yes by the actual content. 11 of 13 pages are faithful or better, the whole thing is provably reproducible against current data, and the shared-formula architecture (`helpers.py` mirroring dashboard.py's subset logic) mostly works as intended. Deleting a working, mostly-accurate ~8,000-line reporting layer over one CRITICAL bug and a handful of coverage gaps would be a large loss for a fixable problem.

**Why not a bigger rebuild (shared compute module) right now:** that's the architecturally "correct" long-term answer — today every number is computed twice, once in `dashboard.py` and once in a `page_XX.py`, which is inherently a drift risk even though this snapshot happens to be mostly aligned. But the concrete bug list below is small, mostly one-function-sized fixes, and cheaper than an extraction project. Treat "extract shared compute functions dashboard.py and data_aggregator both call" as a follow-up architectural improvement, not the immediate action.

**Why not "as-is":** one CRITICAL numeric bug (P4-01) means a citizenship figure a stakeholder could read from this report is simply wrong (32,501 vs the dashboard's 4,746, an entirely different population), and P9-01's same-label-different-number issue means anyone cross-checking "Table 38" between the live dashboard and this report will see two different numbers with no indication they're not the same calculation.

**Concrete fix list, roughly in priority order:**
1. **P4-01** — replicate dashboard's exact citizenship-section filter chain (`uniobservable` ∩ `PLE_STATUS_LABEL=="No confirmed PLE match"` ∩ `CITIZENSHIP_FINAL.notna()`) in `page_04_score_bins.py:229`, or clearly retitle the section as a distinct all-records metric.
2. **INFRA-01** — fix path resolution in `run_all.py`/`config.py` to be relative to `__file__`, not cwd; correct the CLAUDE.md command.
3. **P8-01** — cap Section 3's inline table to `.head(100)` + push full detail to a companion CSV, mirroring Section 5's own pattern.
4. **P4-02** — add `.reindex(columns=BIN_ORDER, fill_value=0)` inside the shared `chi_square_table()` in `helpers.py` (one fix covers every caller).
5. **P9-01** — stop mean-centering "Table 38/39", or renumber/relabel it clearly as a derived, centered view distinct from the dashboard's Table 38/39.
6. **INFRA-04** — fix the two regexes in `aggregate_all.py` (or just read the values positionally instead of via fragile regex).
7. Lower priority, straightforward additions: P5-01 (Table 17), P5-02 (Figure 16), P7-01 (add NMS_APT/NMS_SA), P8-03 (NMA_AppNo section), P13-01 (add Median TRUE raw score to Section E).
8. Documentation-only: relabel/renumber the aggregator-only tables in pages 09-11 so they don't imply a false 1:1 correspondence with dashboard table numbers (P9-02/03, P11-01); soften the "replicates ALL computations" docstring claims to "replicates and extends."
