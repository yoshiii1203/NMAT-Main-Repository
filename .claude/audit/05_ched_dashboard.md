# Audit 05 — CHED Dashboard (`streamlit_dashboard/CHED_relevant_dashboard/dashboard.py`)

Auditor: 05 of 12. Scope: `dashboard.py` (1,263 lines) — the primary stakeholder deliverable. Supporting files read for context: `export_markdown.py` (834 lines, powers the "Export Complete Dashboard" button and duplicates most tab logic), `README.md`, `ched_compute/verified_true/*` (the project's own self-QA suite), `docs/CHED_CMO.md`.

All numbers below were independently recomputed with `./.venv/Scripts/python.exe` against `streamlit_dashboard/CHED_relevant_dashboard/NMAT_Exodus.parquet` (178,927 rows), not copied from the dashboard or from prior audit notes.

---

## VERDICT: **No — not fit to hand to CHED as-is.**

Two CRITICAL data/logic bugs (F01, F02) and one CRITICAL scope/validity failure (F03) currently ship in the primary deliverable and its markdown export. F01 makes a chart and a stress-test section structurally incapable of showing anything other than "100% linkage," which a reader will reasonably interpret as a genuine finding. F02 is a footnoted statistic repeated three times that does not reconcile with the same parquet's own audit column. F03 is a policy-relevant conflation: the dashboard uses the applicant's **undergraduate** institution type (Public/Private) as if it bore on the CMO's SUC-vs-PHEI and GIDA/IP provisions, in a tab literally titled "Key Evidence for Policy Review." None of these require new data or new pipelines to fix — all are containable edits to `dashboard.py`/`export_markdown.py`. With those three fixed (plus the four lower-severity items), this becomes a genuinely disciplined, well-hedged, appropriately scoped dashboard — it already does many things right (see "What this dashboard gets right," below).

---

## What this dashboard gets right (so fixes aren't misread as "start over")

- The string-as-boolean truthiness bug flagged in the shared context (`bool("False") == True`) is **fixed** in `validate_schema()` (`dashboard.py:87-103`): `IS_BEST_NMAT_RECORD`, `IS_PLE_ANALYSIS_SAFE`, `HasTRUErawScores`, `StoredVsDerivedMismatch`, `CalcVsDerivedMismatch` are all coerced to real bool/numeric dtype before any comparison. Confirmed by direct dtype inspection and by recomputing every downstream metric that depends on these columns — all matched the displayed values.
- "Linkage rate" is consistently used instead of "pass rate" throughout, with an explicit, repeated disclaimer that the dataset contains no PLE failures ("How to read this dashboard" expander, Tab 3 `st.info`, Tab 6 Limitations). This is the single most important trap named in the audit brief, and it is handled correctly everywhere **except** where F01 breaks it (see below).
- Foreign-examinee content correctly restricts to `FOREIGNER_STATUS == "Verified Foreigner"` (32,501 rows) and never leans on the 13-row "Likely Foreigner" bucket.
- No hardcoded absolute file paths — `find_data_path()` uses relative candidates only, safe for Streamlit Cloud deployment.
- `load_data()` is `@st.cache_data`-wrapped and every subset (`df_best`, `df_obs`) is built with explicit `.copy()`, avoiding the classic cached-mutation/SettingWithCopy bugs.
- No p-values, no causal language, no per-institution compliance labels are asserted anywhere in the file.

---

## Per-tab element inventory

### Tab 1 — National Profile

| Element | Type | Displayed value | Recomputed value | Verdict | Issue |
|---|---|---|---|---|---|
| Best-record examinees | KPI | `N_BEST` | 133,804 | MATCH | — |
| Unique persons (PERSON_KEY) | KPI | `N_UNIQUE` | 133,558 | MATCH but see F04 | 246-row gap vs N_BEST never explained |
| NMAT years covered | KPI | 13 | 13 | MATCH | — |
| Median percentile rank | KPI | 50.0 | 50.0 | MATCH | — |
| Examinee Volume by Year (bar) + Median Bin Rank by Year (line) | Chart, 2-panel subplot | growth 3,665→22,337 (2006-18); median 53→43 | growth 3,665(2006)→22,337(2018); median 53(2006)→43(2018) | MATCH | Caption "declined from 53-57 ... to 43-48 in 2016-2018" — recomputed 2016=48, 2017=44, 2018=43; consistent |
| University Type Composition (pie) | Chart | Private/Public/Foreign/Not Specified counts | Private 102,888 (76.9%), Public 27,627 (20.6%), Foreign 1,894 (1.4%), Not Specified 1,395 (1.0%) | MATCH | — |
| Course Group Composition (pie) | Chart | 6 CourseGroup counts | Medical&Allied 63,900; Natural Sciences 41,430; Social&Behav 16,462; Other 7,983; Education 3,279; Eng&Tech 750 | MATCH | — |
| Repeat-taker context (prose) | Narrative | 33,713 (25%) repeat | N_REPEAT=33,713, 33,713/133,558=25.24%→"25%" | MATCH | — |
| Score Bin Reference table | Static table | B1-B10 ranges, B4/B5 threshold labels | matches `docs/CHED_CMO.md` §IV.A (40th floor, 30-39 exception) | MATCH | Correctly mapped |

### Tab 2 — B4+ vs B5+ Thresholds

| Element | Type | Displayed value | Recomputed value | Verdict | Issue |
|---|---|---|---|---|---|
| Score Bin Distribution by Year (heatmap, row %) | Chart | row-normalized % per year×bin | spot-checked several cells | MATCH | — |
| B4+/B5+/B4-only scenario table | Table | n=91,409/78,944/12,465; 69.9%/60.4%/9.5% | same | MATCH | — |
| Threshold Context by University Type table | Table | per-UNI_TYPE B4+/B5+/B4-only shares | Public 64.9% B5+, 8.3% B4-only; Private 59.2% B5+ | MATCH | **F03**: table is captioned as informative for CMO threshold policy, but UNI_TYPE here is undergraduate institution, not SUC/PHEI |
| "Public School Examinees and B5+ Threshold" (3 KPIs + table + prose) | KPI+table+narrative | Public B5+=64.9% (17,482/26,937\*); B4-only=8.3%; Private B5+=59.2% | recomputed identically | MATCH numerically | **F03 CRITICAL**: conclusion "exception may not primarily benefit intended disadvantaged groups" — GIDA/IP is undocumented in this dataset AND "Public" ≠ SUC |
| B4 Group Profile (3 KPIs + bar chart + table) | KPI+chart+table | n=12,465; median raw=109.0; Public share=17.9% | matches | MATCH | — |
| Top (B8-B10) vs Bottom (B1-B3) bin trend | Chart+table | share by year | not independently re-verified cell-by-cell (low risk, same `make_bin_pct` helper as heatmap, which matched) | MATCH (by construction) | — |
| Yearly Examinees Meeting Each Threshold | Table | per-year B4+/B5+ counts+shares+observable counts | spot-checked 2009 (n=6,881, matches shared-context style figures) | MATCH | — |
| **B5+ (Bin 5+) PLE-Passer Composition by Year** (2 stacked bar charts + table) | Chart×2 + table | "Confirmed" (green) vs "No confirmed PLE match" (red) per year | **Recomputed: `no_match` = 0 for every year 2006-2014 (see F01)** | **BROKEN — CRITICAL** | Chart structurally cannot show anything but 100% green / 0% red |

\* Public total recomputed as 26,937 not 27,627 because this table (unlike Tab 1's pie) is restricted to rows with a non-null `PercentileBin` (`df_best_bins`), dropping 690 Public rows with missing bin — an internally consistent choice, not flagged as an issue on its own, but not explained to the reader either (minor).

### Tab 3 — Historical PLE-Passer Linkage

| Element | Type | Displayed value | Recomputed value | Verdict | Issue |
|---|---|---|---|---|---|
| Linkage by bin (bar chart + table) | Chart+table | B1=8.27%→B10=76.13% | B1=8.27%, B4=22.85%, B5=46.27%, B10=76.13% | MATCH | Gradient legitimate as "linkage," not "pass rate" — but see F03/note on selection bias below |
| Score Profile by PLE Status (grouped describe table) | Table | count/median/mean/Q25/Q75 for 4 score cols × 2 PLE groups | not fully re-derived (low-risk pandas `.agg`) | Not independently re-verified | — |
| PLE-Passer Linkage by NMAT Year (line chart) | Chart | 2006 highest → 2014 lowest | 2006=55.61%→2014=37.82% (recomputed via `_ann_link`) | MATCH | — |
| PLE-Passer Linkage by Course Group (bar+table) | Chart+table | Education 51.83%, Medical&Allied 45.33%, Eng&Tech 37.75%, etc. | recomputed identically | MATCH | — |
| PLE-Passer Linkage by University Type (bar+table) | Chart+table | Public 50.06%, Private 44.72%, Foreign 22.06% | recomputed identically | MATCH numerically | **F03**: same undergrad/med-school conflation risk as Tab 2 |
| **Stress-Test: Defensible PLE Matching Subset** (4 KPIs + line chart + table + prose) | KPI+chart+table+narrative | N_CLEAN_PLE=27,151; N_CLEAN_B5=23,357; share=36.2%; median gap=6 yrs; **"Yearly PLE-Passer Linkage (Clean Subset, B5+)" line = flat 100% every year** | recomputed identically, confirming the chart is flat 100% by construction | **BROKEN — CRITICAL (same root cause as F01)** | The stress-test's own narrative claims this "confirms the broader findings are robust to matching quality concerns" — it cannot, because it measures nothing (denominator = numerator by construction) |
| B5+ Clean Subset by University Type (table) | Table | counts by UNI_TYPE | not independently re-verified (low risk) | — | — |

### Tab 4 — Institution and Foreign Context

| Element | Type | Displayed value | Recomputed value | Verdict | Issue |
|---|---|---|---|---|---|
| Score Summary by University Type (table) | Table | Public/Private/Foreign median/Q25/Q75 percentile, median raw, median GPS | Public median=56.0, Private median=48.0, Foreign median=51.0 | MATCH | **F03** applies (undergrad, not med school) |
| Bin Rank Distribution by University Type (box plot) | Chart | distribution shape | not independently re-verified (matches summary table above) | MATCH | — |
| Score Bin Distribution by University Type (heatmap) | Chart | row % per UNI_TYPE×bin | uses same `make_bin_pct` helper, verified elsewhere | MATCH | — |
| Top-Bin Share (B8-B10) by University Type (horizontal bar) | Chart+table | ranked % | not independently re-verified (derivative of verified heatmap) | MATCH | — |
| Foreign Examinee Context (3 KPIs + bar chart + table) | KPI+chart+table | Verified Foreign=32,501; Filipino=146,413; distinct nationalities=90; top-10 nationalities incl. India | India (Verified Foreigner subset)=26,490 vs shared-context all-rows figure 26,491 (1-row diff explained by 1 India row with FOREIGNER_STATUS≠"Verified Foreigner") | MATCH | Uses `df_all` (record-level, includes repeat NMAT sittings) rather than `df_best` — inconsistent denominator vs rest of dashboard (F07, LOW) |

### Tab 5 — Key Evidence for Policy Review

| Finding | Type | Displayed value | Recomputed value | Verdict | Issue |
|---|---|---|---|---|---|
| Finding 1 — National Threshold Context | Narrative | 69.9% B4+, 60.4% B5+, gap 9.5pp | matches | MATCH | — |
| Finding 2 — Institutional Performance Patterns | Narrative | Public median 56 vs Private median 48 | matches | MATCH | **F03** — presented as "institutional... pattern," ambiguous whether reader understands "institution" = undergrad school |
| Finding 3 — NMAT-to-PLE-Passer Linkage Gradient | Narrative | B1 8%→B10 76% | matches (8.27%→76.13%) | MATCH | See selection-bias note below |
| Finding 4 — Historical Linkage Trends | Narrative | 2006 rate → 2014 rate, 5yr rolling avg | 55.61%→37.82%, 5yr avg (2014)=43.46% | MATCH | — |
| Finding 5 — Public School Threshold Attainment | Narrative | 64.9% Public B5+, 8.3% B4-only; "exception may not primarily benefit intended disadvantaged groups" | numerically matches | **CRITICAL — F03** | Explicit policy-evaluative conclusion built on an invalid proxy chain (Public undergrad ≠ GIDA/IP; Public undergrad ≠ SUC) |
| Finding 6 — PLE Matching Robustness | Narrative | "confirming the findings are robust to matching quality concerns" | **the underlying chart this claims robustness from is F01's broken tautology** | **CRITICAL — F01** | Claim of robustness is unsupported; the stress test cannot fail by construction |
| Finding 7 — Foreign Examinee Presence | Narrative | 18.2% foreign of all records | 32,501/178,927=18.17%→18.2% | MATCH | — |

### Tab 6 — Data, Methods, and Limitations

| Element | Type | Displayed value | Recomputed value | Verdict | Issue |
|---|---|---|---|---|---|
| Dataset Overview (bullet list) | Narrative | rows, years, N_UNIQUE, N_OBS, N_REPEAT | all matched above | MATCH | — |
| TRUE Raw Score Recalculation expander | Narrative+KPI | "42.2% of stored totals incorrect"; n_true=178,882 (99.97%); formula mismatches=0 | n_true confirmed 178,882/99.97%; formula mismatches confirmed 0; **42.2% does not reconcile** | **CRITICAL — F02** | See below |
| Best-Record Deduplication expander | Narrative | 33,713 (25%) repeat | matches | MATCH | Silent on the 246-row N_BEST/N_UNIQUE gap (F04) |
| Observable Cohort Definition expander | Narrative+KPI | N_OBS=64,501; median gap=6 yrs | matches; PLE_YEAR_GAP min=5.0 across entire dataset confirms "minimum 5-year window" claim is accurate | MATCH | — |
| Deterministic PLE Matching expander | Narrative+KPI | all-rows confirmed=49,986; obs confirmed=29,273; clean B5+=23,357 | all matched | MATCH numerically | **F05**: three other "PLE matched" columns in the same parquet disagree with the 49,986 figure by up to 7,318 rows; never disclosed |
| Data Integrity Summary expander | KPI | Stored-vs-derived mismatches=56,065; Calc-vs-derived mismatches=0 | 56,065 confirmed; Calc-vs-derived confirmed 0 (column is constant, nuniq=1) | MATCH but see F06 | Second KPI is structurally always 0 — a dead column presented as a live integrity check |
| Limitations (6 cards: PLE Outcomes, GIDA/IP, Admissions/Enrollment, Foreign Cap, Composite Ranking, PHEI Accountability) | Narrative | — | — | Content accurate and appropriately scoped | PHEI Accountability card is the right instinct but should explicitly add: "the dataset has no medical-school identifier at all, so no PHEI-level or SUC-vs-PHEI PLE rate can be computed from it" (currently only says matching is incomplete, not that the entity being matched is unknown) |

---

## Findings table

| ID | Severity | Status | Title | Location |
|---|---|---|---|---|
| F01 | CRITICAL | CONFIRMED | "B5+ PLE-Passer Composition" charts are tautological — always 100% confirmed / 0% no-match | `dashboard.py:189-210, 612-671, 810-869`; `export_markdown.py:455-478, ~540-556` |
| F02 | CRITICAL | CONFIRMED | Hardcoded "42.2%" raw-score-mismatch claim does not reconcile with the parquet's own mismatch column | `dashboard.py:240, 292, 1155`; `export_markdown.py:702, 797` |
| F03 | CRITICAL | CONFIRMED | UNI_TYPE (Public/Private) is the applicant's *undergraduate* institution, not the medical school — used as an invalid proxy for the CMO's SUC-vs-PHEI distinction and for GIDA/IP disadvantage status | `dashboard.py:439-949` (Tab 2), `783-808` (Tab 3), `874-985` (Tab 4), `1039-1046, 1077-1093` (Tab 5) |
| F04 | MEDIUM | CONFIRMED | `IS_BEST_NMAT_RECORD` yields 2 "best" rows for 246 persons (492 rows) — N_BEST overcounts unique persons by 246, undisclosed | `dashboard.py:168-172, 296-299, 1142-1145` |
| F05 | MEDIUM | CONFIRMED | Four mutually inconsistent "PLE matched" columns exist in the parquet; dashboard silently picks one (`IS_PLE_ANALYSIS_SAFE`) without disclosing the disagreement | `dashboard.py:140-145` (definition), used throughout Tabs 2/3/5/6 |
| F06 | LOW | CONFIRMED | "Calc-vs-derived mismatches" KPI displays a structurally constant (dead) column as a live integrity metric | `dashboard.py:1213-1220` |
| F07 | LOW | CONFIRMED | Foreign-examinee KPIs (Tab 4, Finding 7) use record-level `df_all` (includes repeat NMAT sittings) while the rest of the dashboard uses person-level `df_best` | `dashboard.py:961-985, 1096-1101` |
| F08 | INFO (positive) | CONFIRMED | String-as-boolean truthiness bug (commit 619a150) is fixed everywhere in `dashboard.py` | `dashboard.py:87-103` |
| F09 | LOW | CONFIRMED | The shipped self-QA suite (`ched_compute/verified_true/`) explicitly rationalizes F01 as "by design" and never cross-checks the "42.2%" prose claim (F02) against its own computed 56,065 figure — gives false assurance that the deliverable was fully checked | `ched_compute/verified_true/verifier_02_thresholds.py:500-506`, `CONSOLIDATED_VERIFICATION_REPORT.md` (no line flags either issue; concludes "No critical errors found") |

---

## Per-finding detail

### F01 — CRITICAL — Tautological PLE-status split (CONFIRMED)

**Root cause.** `_df_clean_ple` (`dashboard.py:191-195`) is built by filtering `df_obs` to `IS_PLE_ANALYSIS_SAFE == True` — i.e. it is, by construction, **100% confirmed PLE passers**. The subsequent aggregation (`dashboard.py:200-209`) then computes `confirmed = HAS_CONFIRMED_PLE.sum()` on that same already-100%-True subset, where `HAS_CONFIRMED_PLE` is itself defined as `IS_PLE_ANALYSIS_SAFE == True` (`dashboard.py:141`). `confirmed` therefore always equals `total`, and `no_match = total - confirmed` is always **0**.

**Verified by direct recomputation** (ran the identical filter/groupby against the shipped parquet):

```
Year  total  confirmed  no_match
2006   1435       1435         0
2007   1352       1352         0
...
2014   3448       3448         0
```

**Consequence.** Two chart pairs and one narrative section are affected in `dashboard.py`, identically duplicated in `export_markdown.py`:
1. Tab 2, "B5+ (Bin 5 and above) PLE-Passer Composition by Year" — both the count-stacked and percent-stacked bar charts (`dashboard.py:612-665`) always render a solid green bar with a red legend entry ("No confirmed PLE match") that never appears in the data.
2. Tab 3, "Stress-Test: Defensible PLE Matching Subset" line chart "NMAT-to-PLE-Passer Linkage Rate (Clean B5+ Subset)" (`dashboard.py:840-850`) is a flat line at 100% for all 9 years.
3. Finding 6 in Tab 5 (`dashboard.py:1086-1093`) states this "confirms the findings are robust to matching quality concerns" — a claim the chart cannot support, since it cannot fail: no possible input produces anything but 100%.

The project's own `ched_compute/verified_true/verifier_02_thresholds.py` (lines 500-506) is aware of the tautology and comments "This is by design — the chart shows the VOLUME of B5+ examinees meeting the strictest PLE matching criteria." That framing is not what the live dashboard tells the reader: the Tab 2 caption (`dashboard.py:605-609`) says the chart shows "the count and percentage who were later confirmed as PLE passers" — i.e., it promises a genuine split, which does not exist.

**Fix (described, not implemented).** Either (a) redefine `_df_clean_ple`'s "confirmed" indicator against a population that is *not* pre-filtered on the same flag — e.g. build the denominator from `df_obs[df_obs["PercentileBin"].isin(B5_PLUS) & (df_obs["PLE_YEAR_GAP"] >= 5) & (df_obs["FOREIGNER_STATUS"]=="Filipino")]` *without* the `IS_PLE_ANALYSIS_SAFE == True` pre-filter, then compute confirmed/no-match against that broader population; or (b) if the intent genuinely is "volume of matched B5+ examinees under strict criteria" (a legitimate, different chart), rename the chart/caption to say exactly that and drop the misleading "vs no confirmed PLE match" framing and the now-untrue "robustness" claim in Finding 6.

### F02 — CRITICAL — Unreconciled "42.2%" statistic (CONFIRMED)

**Claim, verbatim, appears 3× in `dashboard.py`** (lines 240, 292, 1155) and 2× in `export_markdown.py` (lines 702, 797): "the original stored total was inconsistent for 42.2% of records."

**Recomputed from the same parquet's own audit column** (`StoredVsDerivedMismatch`, normalized to numeric by `validate_schema()`, `dashboard.py:100-103`):
```
StoredRawTotal non-null:                 99,316 of 178,927
StoredVsDerivedMismatch == 1.0:          56,065
  as % of the 99,316 rows with a stored total to compare: 56.45%
  as % of all 178,927 rows:                                31.33%
```
Neither figure is 42.2%. The dashboard's own Tab 6 "Data Integrity Summary" panel (`dashboard.py:1213-1220`) displays the 56,065 figure as a bare KPI a few paragraphs below the "42.2%" prose claim in the same tab — the two numbers sit on the same page and do not agree. This is a hardcoded, non-dynamic number (unlike almost every other statistic in the dashboard, which is computed live) — it is not tied to any column in the current parquet and cannot be verified from the data the dashboard ships with. Note the project's `verified_true/verifier_06_data_limitations.py` computes and confirms the 56,065 figure but never checks it against the "42.2%" prose — this discrepancy exists nowhere in the project's own QA output.

**Fix (described).** Either replace "42.2%" with the dynamically computed reconciled figure (and pick one honest denominator — "of records with a stored total to check" is the more defensible framing, i.e. 56.4%), or, if 42.2% is a legitimate figure from an earlier pipeline stage (e.g. raw CEM data before dedup/merge into Exodus) that is simply no longer reproducible from `NMAT_Exodus.parquet`, say so explicitly and cite the stage it came from — do not present it as a fact verifiable from "this dataset."

### F03 — CRITICAL — Undergraduate institution used as SUC/PHEI and GIDA/IP proxy (CONFIRMED)

Per the orchestrator's verified finding (accepted as established): `UNIVERSITY` / `NMA_College`, and by extension the `UNI_TYPE` classification derived from it, describe the applicant's **undergraduate** institution, not the medical school. `UNIVERSITY` itself is never used anywhere in `dashboard.py` or `export_markdown.py` for any per-institution ranking or pass-rate computation (grep confirms zero matches beyond the `REQUIRED_COLS` schema-validation list at `dashboard.py:51`) — so there is **no** instance of an individual-HEI PLE pass rate being computed or displayed. That specific failure mode does not occur in this file.

However, the coarser **UNI_TYPE (Public/Private/Foreign)** aggregate *is* used extensively — Tab 2's "Threshold Context by University Type" and "Public School Examinees and the B5+ Threshold" sections, Tab 3's "PLE-Passer Linkage by University Type," all of Tab 4, and Tab 5 Findings 2 and 5 — and CMO §IV distinguishes **SUCs** (§IV.A: 40th-percentile floor, 30th-39th GIDA/IP exception) from **PHEIs** (§IV.B: self-set cutoff tied to the PHEI's own 5-year PLE performance). `UNI_TYPE` cannot serve as a proxy for this distinction: it describes where the examinee got their *bachelor's degree*, not which medical school (SUC or PHEI) they subsequently attended — and the dataset has no medical-school identifier at all, so no valid SUC-vs-PHEI split can be constructed from it by any means.

The most acute instance is Tab 2's headline section (`dashboard.py:466-522`) and Tab 5 Finding 5 (`dashboard.py:1077-1084`): "The CMO exception for B4-only (Bin 4) applicants is intended for disadvantaged groups (GIDA, IP communities). If most public school examinees already meet the B5+ threshold, then lowering the cut-off may not primarily benefit the intended disadvantaged groups." This sentence chains two unsupported proxies — "attended a public undergraduate institution" ≈ "GIDA/IP-eligible," and (implicitly, by being framed as evidence for a CMO cut-off decision) "public undergraduate institution" ≈ "SUC medical program" — to reach a specific, actionable policy conclusion in a tab titled "Key Evidence for Policy Review." The dashboard does hedge this at the very end of the paragraph ("GIDA/IP status is not available in this dataset for direct verification," `dashboard.py:520-521`) and in Tab 4's caption ("not necessarily the medical school they applied to or attended," `dashboard.py:878-880`) — so this is not an *affirmative* false statement that UNIVERSITY equals the medical school. But the hedge is a trailing caveat under a headline conclusion, not a framing that prevents the conclusion from being drawn — and it never states the more important, more specific fact: the dataset has **no medical-school identifier**, so no SUC-vs-PHEI comparison is possible at all, by any variable in the file. That is a materially stronger and different statement than "not necessarily the medical school," and it is not made anywhere in the dashboard.

**Fix (described).** (1) In every UNI_TYPE-driven table/chart caption, replace "not necessarily the medical school" with an explicit statement that no medical-school/PHEI/SUC identifier exists in this dataset at all, so UNI_TYPE cannot be used to reason about CMO §IV.A/§IV.B provisions. (2) Remove or substantially reframe the "Public School Examinees and the B5+ Threshold" section and Finding 5: either drop the GIDA/IP-benefit conclusion entirely (it is not answerable from this data), or restate it as a pure description ("X% of examinees whose undergraduate institution was public score at B5+") with no inference about the CMO exception's intended beneficiaries.

### F04 — MEDIUM — `IS_BEST_NMAT_RECORD` is not strictly 1 row per person (CONFIRMED)

```
N_BEST (rows flagged IS_BEST_NMAT_RECORD=True):        133,804
N_UNIQUE (distinct PERSON_KEY among those rows):        133,558
Gap:                                                        246
```
246 `PERSON_KEY` values have **2** rows each flagged `IS_BEST_NMAT_RECORD=True` (492 rows total, e.g. `ABAD, ALBERT CAISIP||09/28/1990` appears twice). Per CLAUDE.md, this flag is supposed to select exactly one best attempt per person. The dashboard displays both `N_BEST` and `N_UNIQUE` side by side (Tab 1 KPIs, Tab 6 bullet list) without reconciling or even acknowledging the 246-row gap, and every "best-record examinees" count elsewhere in the dashboard (91,409 B4+, etc.) inherits this 0.18% overcount.

**Fix (described).** Flag and report the count of duplicate-best-record persons; for dashboard purposes, break the remaining tie deterministically (e.g., keep first `APPNO_CLEAN`) so `N_BEST == N_UNIQUE`, or explain the residual gap explicitly in the Best-Record Deduplication expander.

### F05 — MEDIUM — Undisclosed disagreement among "PLE matched" columns (CONFIRMED/SUSPECTED)

The parquet contains four different columns that could each answer "how many NMAT examinees are confirmed PLE passers," and they disagree substantially:
```
IS_PLE_PASSER == True (= IS_PLE_ANALYSIS_SAFE, used by dashboard): 49,986
PLE_YEAR_PASSED.notna():                                            54,528  (+4,542)
PLE_MATCH_METHOD.notna():                                            57,304  (+7,318)
PLE_YEAR_GAP.notna():                                                48,842  (-1,144)
```
The dashboard consistently uses `IS_PLE_ANALYSIS_SAFE` (aliased as `HAS_CONFIRMED_PLE`) throughout — a defensible, internally consistent choice (it is the most conservative of the three larger counts) — but this inconsistency in the underlying data is never surfaced to the reader anywhere in Tab 6's "Deterministic PLE Matching" methodology section, despite being directly material to every PLE-linkage number in Tabs 2, 3, 5, and 6. Separately: among the 49,986 `IS_PLE_ANALYSIS_SAFE==True` rows, 2,867 (5.7%) have a **null** `PLE_YEAR_GAP` — i.e., "confirmed passer" but no computable year gap — which is itself an internal data-consistency question worth one sentence of disclosure, since the Tab 3 "clean subset" stress-test's `PLE_YEAR_GAP >= 5` filter derives its entire effect from silently dropping exactly these 2,867 rows (the minimum non-null `PLE_YEAR_GAP` across the *entire* dataset is already 5.0, so the "≥5 years" language in the stress-test's methodology, `dashboard.py:813-816`, adds no actual gap-based filtering beyond removing null-gap rows).

**Fix (described).** Add one sentence to the Tab 6 "Deterministic PLE Matching" expander naming the column used (`IS_PLE_ANALYSIS_SAFE`) and noting the size of disagreement with the other three PLE-linkage columns in the parquet, so a technically literate reader can audit the choice.

### F06 — LOW — Dead column displayed as a live integrity check (CONFIRMED)

`CalcVsDerivedMismatch` has exactly one non-null value (`"0.0"`) across all 178,927 rows (`nunique()==1`) — it can never register a mismatch. The Tab 6 "Data Integrity Summary" panel (`dashboard.py:1213-1220`) displays it next to `StoredVsDerivedMismatch` (which is a real, informative 56,065-count metric) as if both carry equal evidentiary weight. A reader has no way to know the second KPI is structurally incapable of ever showing anything but 0.

**Fix (described).** Drop the `CalcVsDerivedMismatch` KPI, or annotate it as "constant in this dataset — retained for schema completeness only."

### F07 — LOW — Inconsistent denominator for foreign-examinee metrics (CONFIRMED)

Tab 4's "Foreign Examinee Context" (`dashboard.py:961-985`) and Finding 7 (`dashboard.py:1095-1101`) deliberately use `df_all` (178,927 rows, includes every repeat NMAT sitting) rather than `df_best` (the person-deduplicated subset used by every other section of the dashboard). The code comment at line 961 documents this as intentional ("consistent with data-aggregator page 04"), and the prose correctly says "NMAT records" rather than "examinees" or "persons" — so this is not a mislabeling, but it is the only section of the dashboard that switches denominators, and a reader moving between tabs is not told why.

**Fix (described).** Either switch to `df_best` for consistency, or add one clause explaining why record-level (not person-level) counting is used here specifically (e.g., because citizenship should not vary by attempt so record-level and person-level would be nearly identical, in which case just confirm that and use `df_best` for uniformity).

### F08 — INFO (positive finding) — Truthiness bug fix verified (CONFIRMED)

The shared audit context flagged that `HasCEMMatch`, `HasTRUErawScores`, `StoredVsDerivedMismatch`, `AllRawComponentsPresent`, `CalcVsDerivedMismatch` are stored as `str` in the parquet, making naive `bool(x)` or `x == True` comparisons unreliable (`bool("False") == True`). In `dashboard.py`, `validate_schema()` (lines 87-103) explicitly coerces every one of these columns that the dashboard actually uses (`HasTRUErawScores`, `StoredVsDerivedMismatch`, `CalcVsDerivedMismatch`, plus `IS_BEST_NMAT_RECORD`/`IS_PLE_ANALYSIS_SAFE` which were already bool) to a real bool/numeric dtype **before** any comparison anywhere downstream. Recomputing every metric that depends on these columns (n_true=178,882/99.97%, mismatch counts=56,065/0) matched the dashboard's displayed values exactly. `HasCEMMatch` and `AllRawComponentsPresent` are not referenced anywhere in `dashboard.py`. No instance of the truthiness bug remains in this file.

### F09 — LOW — Shipped self-QA suite gives false assurance (CONFIRMED)

`ched_compute/verified_true/CONSOLIDATED_VERIFICATION_REPORT.md` concludes "**No critical errors found.** The dashboard's displayed values are correct." Its own `verifier_02_thresholds.py` (lines 500-506) documents F01's tautology and dismisses it as "by design," and no verifier or report anywhere cross-checks the "42.2%" prose claim (F02) against the 56,065 `StoredVsDerivedMismatch` figure the same verifier computes two lines away (`verifier_06_data_limitations.py:81`, its output reproduced at `VERIFIER_streamlit_output_log_06.md:34-35`). Because this folder is presented in `README.md` as "an offline verification layer" with "Verified True Outputs," a maintainer or reviewer who trusts it will not independently catch F01 or F02. This is not a `dashboard.py` bug, but it is part of the same deliverable tree and materially affects how much confidence anyone should place in "verified" claims about this dashboard.

---

## Claims register

Every substantive, non-tautological claim the dashboard makes to a reader, and its status.

| # | Claim (paraphrased) | Location | Status | Corrected wording (if needed) |
|---|---|---|---|---|
| 1 | Dataset has 178,927 records, 2006-2018 | Header caption | SUPPORTED | — |
| 2 | PLE-linked analyses use Year≤2014 to avoid right-censoring | Header caption, Tab 6 | SUPPORTED | — (verified: PLE_YEAR_GAP min=5.0 across the whole dataset, so the ≥5-year claim is empirically true) |
| 3 | "NMAT-to-PLE linkage ... is NOT a PLE pass rate; the dataset does not contain all PLE takers or PLE failures" | "How to read" expander, Tab 3 `st.info`, Tab 6 Limitations | SUPPORTED | Correctly and repeatedly stated |
| 4 | Foreign examinee counts are NMAT examinees, not enrolled medical students | "How to read" expander, Tab 4, Tab 6 Limitations | SUPPORTED | — |
| 5 | Original stored total inconsistent for "42.2%" of records | Tab 1 caption, header caption, Tab 6 expander | **UNSUPPORTED** | Recomputed mismatch rate in this parquet is 56.4% of the 99,316 rows with a stored total (31.3% of all rows) — not 42.2%. Replace with dynamically computed figure or cite the pipeline stage where 42.2% was actually true. (F02) |
| 6 | "B4+ threshold encompasses a substantially larger pool than B5+" | Tab 2 | SUPPORTED | 69.9% vs 60.4%, 9.5pp gap — recomputed exactly |
| 7 | "Even as top-bin share has declined, the absolute number of B5+ examinees who become PLE passers remains substantial" (implying a real confirmed/no-match split) | Tab 2, B5+ PLE Composition caption | **UNSUPPORTED** | The chart cannot show anything but 100% confirmed by construction (F01). Reframe as raw volume of matched B5+ examinees under strict criteria, or fix the denominator. |
| 8 | "If most public school examinees already meet B5+, the [CMO GIDA/IP] exception may not primarily benefit the intended disadvantaged groups" | Tab 2, Tab 5 Finding 5 | **UNSUPPORTED / SCOPE CREEP** | UNI_TYPE=Public is the undergraduate institution, not a GIDA/IP indicator, and not equivalent to "SUC" as the CMO uses the term; the dataset cannot support this conclusion. Should be removed or reframed as pure description with no inference about the exception's intended beneficiaries. (F03) |
| 9 | "The distribution by university type ... confirms the broader findings are robust to matching quality concerns" | Tab 3 stress-test caption, Tab 5 Finding 6 | **UNSUPPORTED** | The underlying stress-test chart is tautological (F01); "robust" cannot be claimed from a metric that cannot fail. |
| 10 | "Public institution examinees show a higher median bin rank (56) than Private (48)" | Tab 5 Finding 2 | SUPPORTED (numerically) | Accurate; caveat that "institution" here means undergraduate school, not medical school, would improve clarity (soft version of F03) |
| 11 | "NMAT-to-PLE-passer linkage increases with score bin, from 8% (B1) to 76% (B10)" | Tab 5 Finding 3 | SUPPORTED but incomplete | Numerically correct; the dashboard already avoids "causal" language ("historical descriptive patterns, not causal predictions") but does not note that this gradient conflates (a) probability of ever enrolling in and completing medical school and (b) probability of subsequently passing PLE — both of which correlate with NMAT score independently, and neither of which can be separated with this data. A one-sentence addition would close this gap. |
| 12 | Foreign nationals ≈18.2% of all NMAT records; India is the largest group | Tab 5 Finding 7, Tab 4 | SUPPORTED | 32,501/178,927=18.17%→18.2% confirmed; India 26,490 of Verified Foreigner subset confirmed |
| 13 | GIDA/IP status, medical school admissions/enrollment, PHEI-level PLE performance are not available in this dataset | Tab 6 Limitations | SUPPORTED, but incomplete on one point | Should additionally state plainly that **no medical-school identifier exists at all**, not just that PHEI-level compliance labeling is out of scope — this is the deeper reason SUC-vs-PHEI analysis (CMO §IV.A/B) is impossible from this data, not merely undesirable. (F03) |
| 14 | Best-record deduplication "prevents repeat takers from inflating counts in any percentile band" | Tab 6 | SUPPORTED with a small caveat | True in the vast majority of cases; 246 persons (0.18%) still have 2 "best" rows each (F04) |
| 15 | Deterministic PLE matching "ensures full auditability" | Tab 6 | SUPPORTED for the matching *method* | True that no fuzzy matching is used; the dashboard does not disclose that four different "match confirmed" columns in the parquet disagree by up to 7,318 rows (F05) |

---

## Summary of severities

- **CRITICAL (3):** F01 (tautological PLE-status charts, 2 chart pairs + 1 finding), F02 (unreconciled 42.2% statistic, 5 occurrences across dashboard+export), F03 (undergrad-institution-as-SUC/PHEI/GIDA-IP-proxy scope creep, concentrated in Tab 2's "Public School" section and Tab 5 Finding 5, but the underlying UNI_TYPE-caveat gap runs through Tabs 2-5).
- **MEDIUM (2):** F04 (246-row best-record duplication), F05 (undisclosed 4-way PLE-match-column disagreement, plus the vacuous "≥5yr" stress-test filter).
- **LOW (3):** F06 (dead column shown as live KPI), F07 (inconsistent denominator in one tab), F09 (self-QA suite gives false assurance).
- **INFO/positive (1):** F08 (truthiness bug confirmed fixed).
