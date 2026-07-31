# Auditor 12 — Upstream Pipelines (1–3), PLE Matching

Scope: `1_Data_Cleaning_Pipeline.ipynb`, `2_PLE_Matching_Pipeline.ipynb`, `3_NMAT_PLE_Analysis.ipynb`, `dataset/fix_univs.py`, `dataset/UNIVS.csv`/`UNIVS_ARCHIVED.csv`, `dataset/PLE_DATA.csv`, `dataset/PLE_UNMATCHED.csv`.

All numbers below were computed with `./.venv/Scripts/python.exe` reading the existing parquet/CSV artifacts (`dataset/NMAT_Exodus.parquet`, `dataset/NMAT_Ultima.parquet`, `dataset/output/*`, `.artifacts/2_PLE_Matching_Results.md` — a saved execution transcript of Pipeline 2). No notebook was executed and no project file was modified.

---

## 1. PLE linkage: what the numbers actually mean (DEFINITIVE)

Everything is produced in `2_PLE_Matching_Pipeline.ipynb`, code cell index **11** ("CELL 12 — Apply IS_PLE_PASSER flag to NMAT_FINAL"), function `get_ple_info()`. Two lookup dicts are built from the deduplicated `master_match` table (one row per distinct `PLE_NAME_NORM`):

- `appno_to_ple`: keyed by `MATCHED_APPNO`, built from **every** `master_match` row that has a non-null matched AppNo, **regardless of `MATCH_STATUS`** (includes `AMBIGUOUS`, `NO_VALID_MATCH`, `APPNO_NOT_IN_NMAT`).
- `name_to_ple`: keyed by `PLE_NAME_NORM`, same unrestricted population.

For every NMAT row, `get_ple_info()` looks itself up first by its own `APPNO_CLEAN`, then falls back to `NAME_NORM`. If found (in **either** dict, at **any** status), it copies `PLE_MATCH_METHOD`, `PLE_YEAR_PASSED`, `PLE_MATCH_STATUS`, etc. from that record — but `IS_PLE_PASSER` is only set `True` if `MATCH_STATUS ∈ {FINAL_MATCH, MANUAL_APPNO_MATCH, DETERMINISTIC_APPNO}`. This single design choice — populate metadata columns for *any* match, gate the boolean flag on *accepted* status only — is the entire explanation for all four counts. Verified directly on `dataset/NMAT_Exodus.parquet`:

| Population | Count | Definition |
|---|---|---|
| `PLE_MATCH_METHOD.notna()` | **57,304** | Row's name/appno hit *something* in `master_match`, any status. = EXACT(54,437) + MANUAL_APPNO_MATCH(2,776) + DETERMINISTIC_APPNO(91) |
| `PLE_YEAR_PASSED.notna()` | **54,528** | Same population **minus** the 2,776 `MANUAL_APPNO_MATCH` rows, which structurally can never carry a year (see below) |
| `IS_PLE_PASSER==True` | **49,986** | Subset of the above whose `MATCH_STATUS` is an *accepted* status (`FINAL_MATCH`/`MANUAL_APPNO_MATCH`/`DETERMINISTIC_APPNO`), i.e. excludes `AMBIGUOUS` and `NO_VALID_MATCH` |
| `PLE_YEAR_GAP.notna()` | **48,842** | Subset of `IS_PLE_PASSER==True` that also has a year (excludes `MANUAL_APPNO_MATCH`'s 2,776 and a further ~1,144 EXACT-accepted rows where year-gap couldn't be computed — see note below) |

**The 57,304 → 54,528 gap (2,776, exactly `MANUAL_APPNO_MATCH`'s count) is real and exact — confirmed:** `PLE_UNMATCHED.csv` (Stage 0's source) has **only two columns**, `FULL_NAME` and `NMA_AppNo` — it carries no year field. In cell index 7 ("CELL 7 — Stage 0"), every Stage-0 result hard-codes `"PLE_YEAR_PASSED": np.nan` (lines "not in PLE_UNMATCHED (no year column)"). Cross-tab confirms 100% of `MANUAL_APPNO_MATCH` rows have `PLE_YEAR_PASSED` null and 0% of `EXACT`/`DETERMINISTIC_APPNO` rows do. This is a structural artifact of the input file schema, not a bug, but it means: **any analysis that filters or joins on `PLE_YEAR_PASSED` silently drops all 2,776 `MANUAL_APPNO_MATCH` rows without a warning.**

**The task brief's assumption that "54,528 − 49,986 = 4,542" is a real subset is FALSE — corrected here.** The three populations are **not** monotonically nested. Verified by direct cross-tab of `PLE_MATCH_METHOD` × `PLE_YEAR_PASSED.notna()` × `IS_PLE_PASSER`:
- Of the 54,528 rows with a non-null year, **7,318** have `IS_PLE_PASSER==False` (these are `EXACT`-method rows whose `MATCH_STATUS` is `NO_VALID_MATCH` [5,595] or `AMBIGUOUS` [1,723] — confirmed via `NMAT_Ultima.parquet`'s `PLE_MATCH_STATUS` column, which still exists there even though it was dropped before `Exodus.parquet`), and 47,210 have `IS_PLE_PASSER==True`.
- Of `IS_PLE_PASSER==True`'s 49,986, 47,210 have a year and **2,776 do not** (the `MANUAL_APPNO_MATCH` rows).
- 47,210 + 2,776 = 49,986 ✓. 47,210 + 7,318 = 54,528 ✓. The arithmetic "54,528 − 49,986 = 4,542" is a coincidental subtraction across two non-nested sets, not a describable population — **do not use it in the corrected data dictionary.**

**Which count is "confirmed PLE passer"?** `IS_PLE_PASSER == True` (49,986 rows / 36,305 unique best-record individuals — see §3) is the correct, intended count. `PLE_MATCH_METHOD.notna()` and `PLE_YEAR_PASSED.notna()` are both broader/leakier populations that include rejected disambiguation outcomes (`AMBIGUOUS`, `NO_VALID_MATCH`) that still happened to inherit method/year metadata from the lookup table. **Any dashboard computing a PLE pass rate from `PLE_YEAR_PASSED.notna()` or `PLE_MATCH_METHOD.notna()` instead of `IS_PLE_PASSER` is silently including rejected/ambiguous matches and will overstate the pass rate.** Recommend a repo-wide grep for `PLE_YEAR_PASSED.notna()` / `PLE_MATCH_METHOD.notna()` used as a passer proxy.

**Suggested corrected data-dictionary language:**
> `IS_PLE_PASSER` (bool): True only for NMAT rows whose PLE match reached an *accepted* disambiguation outcome (`FINAL_MATCH` via exact name, `MANUAL_APPNO_MATCH`, or `DETERMINISTIC_APPNO`). This is the authoritative "confirmed PLE passer" flag (49,986 rows / 36,305 unique best-record persons). `PLE_MATCH_METHOD` and `PLE_YEAR_PASSED` are populated more broadly and also cover matches whose confidence was rejected (`AMBIGUOUS`, `NO_VALID_MATCH`) — never use their `.notna()` as a passer proxy. `PLE_YEAR_PASSED` is additionally null for all 2,776 `MANUAL_APPNO_MATCH` rows because the source file (`PLE_UNMATCHED.csv`) carries no year column — those are still real confirmed passers.

---

## 2. `IS_PLE_ANALYSIS_SAFE` — CRITICAL bug, exact origin

**It was never a `Year<=2014` filter. It was born as a byte-for-byte duplicate of `IS_PLE_PASSER` inside Pipeline 2 itself, and stayed that way through every downstream stage.**

File: `2_PLE_Matching_Pipeline.ipynb`, code cell index **11** (in-notebook label "CELL 12"). Exact lines:

```python
accepted_statuses = {"FINAL_MATCH", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"}
analysis_safe      = {"FINAL_MATCH", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"}   # <-- identical set literal
...
"IS_PLE_PASSER":        status in accepted_statuses,
"IS_PLE_ANALYSIS_SAFE": status in analysis_safe,                                    # <-- always equals IS_PLE_PASSER
```

`analysis_safe` is defined as the **identical set literal** as `accepted_statuses` — there is no `Year` term anywhere in the condition. Confirmed empirically that `NMAT_Ultima.parquet` (Pipeline 2's own output, before Pipelines 3/4 ever touch the data) **already** has `(IS_PLE_ANALYSIS_SAFE == IS_PLE_PASSER).all() == True`, and 9,116 rows have `IS_PLE_ANALYSIS_SAFE==True` with `Year>2014`. Grepped `3_NMAT_PLE_Analysis.ipynb` and `4_Citizenship_Integration.py` for any competing `IS_PLE_ANALYSIS_SAFE` construction — none exists; the column is only ever read downstream, never rebuilt. **There is no "correct version that got clobbered." A `Year<=2014`-based safe-cohort flag never existed in this codebase at all.**

**Fix:** in cell index 11, replace the `analysis_safe` set-membership test with something like:
```python
"IS_PLE_ANALYSIS_SAFE": (status in accepted_statuses) and (pd.notna(nmat_row.get("YEAR_INT")) and nmat_row["YEAR_INT"] <= 2014),
```
(or equivalently compute it once as a vectorized `nmat_ultima["Year"] <= 2014` after the merge in cell 12/13, matching the documented intent in `README.md`/`CLAUDE.md`).

**Blast radius (CONFIRMED via grep):** `IS_PLE_ANALYSIS_SAFE` is read in `data_aggregator/{config,helpers,page_02,page_06,page_10,page_12,page_13}.py`, `streamlit_dashboard/CHED_relevant_dashboard/{dashboard.py,export_markdown.py,ched_compute/*}` (including all 5 `verified_true/verifier_*.py` "verification" scripts and the CHED compliance page), and every `forensic_audit/*.py` script. Every one of these currently computes a "clean/safe cohort" denominator that is actually just `IS_PLE_PASSER` again — i.e., 100% by construction wherever it's used as a filter-then-rate denominator, exactly as the shared context flagged. This is the single highest-priority fix in the whole codebase.

---

## 3. The 3-stage deterministic cascade

Cell indices in `2_PLE_Matching_Pipeline.ipynb`: Stage 0 = cell 7, Stage 1 = cell 9, Stage 2 = cell 10, combine/dedupe = cell 11.

- **Stage 0 (`MANUAL_APPNO_MATCH`)**: direct join of `PLE_UNMATCHED.csv`'s pre-filled `NMA_AppNo` (2,332 of 6,600 rows have one) against `NMAT_FINAL`'s `APPNO_CLEAN`. From the saved execution transcript `.artifacts/2_PLE_Matching_Results.md`: 2,331 found, 1 `APPNO_NOT_IN_NMAT`.
- **Stage 1 (`EXACT`)**: all 43,630 `PLE_DATA.csv` records matched by exact normalized name (`NAME_NORM`) against `NMAT_FINAL`, excluding names already resolved in Stage 0. 0 candidates → `NEEDS_FUZZY` (dropped, not actually fuzzy-matched — see §6). 1 candidate → accept if year-gap ≥5 passes. 2+ candidates → `disambiguate()` (§5).
- **Stage 2 (`DETERMINISTIC_APPNO`)**: residual unmatched names (from `dataset/output/PLE_STILL_UNMATCHED.csv`, 7,207 rows — itself apparently a hand-assembled/second-round file with a pre-filled AppNo column) joined directly on AppNo.
- **Combine**: all three stage outputs concatenated, then **deduplicated by `PLE_NAME_NORM`** keeping the highest-priority/-confidence row (`accepted` statuses rank 1, `AMBIGUOUS` rank 3, rejected ranks 5–6). This guarantees each distinct PLE name appears **exactly once** in `master_match` — i.e., **PLE record → NMAT match is enforced 1:1 at the name level by construction.**

**Can one person match at multiple stages?** No — Stage 1 explicitly skips any `PLE_NAME_NORM` already resolved in Stage 0 (`stage0_resolved_names` set, cell 9), and the final dedup step guarantees one row per name regardless.

**Can one PLE record match multiple distinct NMAT people, or vice versa?** Verified against `NMAT_Ultima.parquet`: among `IS_PLE_PASSER & IS_BEST_NMAT_RECORD` rows (36,305, i.e. one row per confirmed-passer *person*), grouping by `NAME_NORM` and counting distinct `BDATE_CLEAN` finds only **2** name groups with >1 distinct birthdate, and both are data-quality artifacts (one candidate's `BDATE_CLEAN` is a garbled numeric string rather than a real date, not a genuine second person). **So at the person level, false "one PLE record shared by two different real people" collisions are effectively zero (≈2/36,305 ≈ 0.006%).** This is *not* automatic — it works because the disambiguator's Step 2 (DOB majority filter, §5) correctly separates same-name candidates when DOB data exists.

**Is a single confirmed match ever spread across multiple NMAT rows?** Yes, deliberately: `IS_PLE_PASSER`/`PLE_YEAR_PASSED` are applied to **every** NMAT row sharing that person's `APPNO_CLEAN` (direct) or `NAME_NORM` (fallback for repeat attempts under a different AppNo) — so a repeat-taker who eventually passed PLE gets the flag on *all* their attempt-rows, not just their matched/best one. Evidence: `IS_PLE_PASSER==True` has 49,986 rows but only 37,597 distinct `PERSON_KEY`s (avg 1.33 rows/person), while `APPNO_CLEAN` is 49,985-of-49,986 unique (i.e., essentially one row per physical attempt, as expected). This is intentional row-level propagation for a real person, not a duplicate-claim bug — but it means **any count of "confirmed passers" must filter on `IS_BEST_NMAT_RECORD` or it overcounts by ~33%**, exactly as `CLAUDE.md` already warns generally for `IS_BEST_NMAT_RECORD`.

---

## 4. `MANUAL_APPNO_MATCH` (2,776 rows) — reliability & audit trail

**Row count vs. real people:** the 2,776 figure is *rows*, not people — confirmed 2,336 distinct `PERSON_KEY`s / 2,331 people actually found via Stage 0 (`.artifacts/2_PLE_Matching_Results.md`: "Matched via AppNo: 2,331"), inflated to 2,776 rows by the same repeat-attempt propagation described in §3.

**Provenance: none documented.** `PLE_UNMATCHED.csv` (2 columns: `FULL_NAME`, `NMA_AppNo`) is read in Pipeline 2 as a **pre-existing input file** — no script, notebook cell, or document anywhere in the repo generates or explains how its `NMA_AppNo` column was populated. `git log --all -- dataset/PLE_UNMATCHED.csv` returns nothing (file isn't tracked with history). `README.md`/`docs/pipeline_architecture.md` both call this stage "Manual AppNo Recovery" but neither explains the methodology, who performed it, when, or against what evidence. This matches the task brief's concern precisely: **"manual" in a pipeline that otherwise advertises full determinism, with zero audit trail.** Given the raw file has AppNos as bare pre-filled values with no method/confidence/reviewer column, it is impossible to independently verify these 2,331 person-level matches were made correctly — they are simply trusted. Severity: HIGH (affects forensic-audit "genuine mismatch" conclusions that rely on this population, as the task notes).

**Is it reliable in aggregate?** The only indirect evidence of reliability is Stage 0's near-perfect internal consistency (only 1 of 2,332 pre-filled AppNos wasn't found in `NMAT_FINAL` at all) and that these matches carry `MATCH_CONFIDENCE=100` unconditionally (hard-coded, not measured) — i.e. the "100" confidence score is not evidence of correctness, it is a fixed literal assigned regardless of match quality (cell 7, `"MATCH_CONFIDENCE": 100`).

---

## 5. The 5-step disambiguator — CONFIRMED partially circular

Function `disambiguate()`, cell index 6. Steps, exactly as coded:
1. **Year-gap filter**: keep candidates with `PLE_YEAR − NMAT_YEAR ≥ 5`.
2. **DOB/identity filter**: keep candidates sharing the modal `BDATE_CLEAN` among survivors (falls back to keep-all if no DOB data).
3. **Latest NMAT year**: keep only the most recent attempt among survivors.
4. **Percentile floor**: drop candidates with `NMS_PER_num < 40` (falls back to keep-all if percentile is missing for everyone).
5. **Final verdict**: if exactly one candidate remains → `FINAL_MATCH`. If multiple remain, **take the one with the highest `NMS_PER_num` as a tiebreak, and accept it as `FINAL_MATCH` only if it beats the runner-up by ≥5 percentile points** — otherwise mark `AMBIGUOUS` (still saved, but `IS_PLE_PASSER=False`).

**This is CONFIRMED circular exactly as the task hypothesized**: Step 4 filters candidates by `NMS_PER_num` and Step 5 explicitly *selects the match with the highest percentile* among remaining ties. `NMS_PER_num` is the applicant's percentile score — the same variable whose relationship to PLE outcome the downstream analysis studies. Whenever this path is invoked, the "winning" record is chosen partly *because* it scored higher, which will mechanically inflate any later score→PLE-pass association for exactly the population that went through multi-candidate disambiguation.

**Magnitude — bounded but not precisely quantifiable without re-running the pipeline.** This path is only reached when a PLE name maps to **2+ exact-name NMAT candidates that also survive the year-gap and DOB filters and share the same latest attempt year** — i.e., near-exact name collisions among people (or genuine repeat-attempt duplicates of the same person, which is harmless since either "candidate" is really the same individual). Structural upper bound: only 1,301 raw `NAME_NORM` groups exist anywhere in the confirmed-passer population with >1 distinct birthdate (§3), and DOB-based Step 2 resolves nearly all of them before reaching Step 4/5 (final person-level collision count ≈2). The saved run (`.artifacts/2_PLE_Matching_Results.md`) shows 772 `AMBIGUOUS` outcomes in that run (1,723 in the run baked into the current parquet) — these are cases where the percentile tiebreak did **not** clear the 5-point bar and got excluded from `IS_PLE_PASSER`. The complementary case — ties that *did* clear 5 points and got silently accepted as `FINAL_MATCH` via the percentile tiebreak — is not separately logged anywhere and cannot be counted without adding instrumentation and re-running Pipeline 2 (out of scope for a read-only audit). **Recommendation: instrument `disambiguate()` to tag percentile-tiebreak-resolved rows with a distinct `MATCH_REASON`/method so this population becomes filterable, and consider re-running the score→outcome analysis with a leave-out check on that subset.** Severity: MEDIUM (real but almost certainly small population, given the tight funnel above), documented here as SUSPECTED-quantity/CONFIRMED-mechanism.

**Additional confirmed inconsistency in the same cell block:** cell index 16's final print statement claims `"IS_PLE_PASSER=True includes AMBIGUOUS (flag these in PLE plots)"` — this is **false** against the actual code: `accepted_statuses` (cell 11) does not contain `"AMBIGUOUS"`, and empirically 0 of the `AMBIGUOUS`-status rows have `IS_PLE_PASSER=True` in `NMAT_Ultima.parquet`. The code's behavior (excluding ambiguous matches) is the safer, correct one; the print statement is simply stale/wrong. Severity: LOW (misleading in-notebook narration only, does not affect any actual output).

---

## 6. Fuzzy matching — removed for PLE person-matching, **survives in Pipeline 1 university matching**

Grepped all three notebooks and `4_Citizenship_Integration.py` for `difflib`, `SequenceMatcher`, `soundex`, `metaphone`, `rapidfuzz`, `fuzz.`, `process.extract`, `get_close_matches`, `Levenshtein`, `jellyfish`.

- **`2_PLE_Matching_Pipeline.ipynb` (PLE person matching): CLEAN.** Zero hits. The "NEEDS_FUZZY" status label in Stage 1 (cell 9) is a vestigial name only — those rows are simply dropped/left unmatched, no fuzzy step actually runs on them anywhere in this notebook. The documented claim "all fuzzy/rapidfuzz matching removed... for PLE matches" is **TRUE**.
- **`1_Data_Cleaning_Pipeline.ipynb` (university-name matching): NOT clean.** `from rapidfuzz import process, fuzz` (cell 3), used in `match_college_to_univs()` (cell 17) as a genuine fuzzy fallback (`fuzz.token_sort_ratio`, `FUZZY_MATCH_MIN_SCORE=88`, `FUZZY_MATCH_MIN_GAP=5`) when exact `UNIVS.csv` lookups fail. Confirmed live use: `dataset/DsPy_verified.csv` shows **235 of 3,251** colleges (7.2%) were resolved via `UNIVS_FUZZY`, feeding directly into the `UNIVERSITY`/`UNI_TYPE`/`UNI_LOCATION` columns everyone downstream uses. **Found at least one concrete false positive by inspection**: `NMA_College = "Saint Leo University"` (a real, distinct US institution) fuzzy-matched at confidence 90 to `UNIVERSITY = "SAINT LOUIS UNIVERSITY"` — a different school. This does not affect PLE linkage but does affect `UNI_TYPE`/university-level classification for a nontrivial minority of rows. **The blanket claim in `README.md`/`CLAUDE.md` that "all fuzzy/rapidfuzz matching removed" is only true for the PLE-matching pipeline; it is FALSE as a description of Pipeline 1.** Severity: MEDIUM (affects ≤7% of rows' university classification, one demonstrated misclassification, no evidence of systemic damage but unverified beyond spot-check).

---

## 7. Match-rate sanity

`PLE_DATA.csv` = 43,630 passer records (years 2011–2022). `PLE_UNMATCHED.csv` = 6,600 (of which 2,332 had a pre-filled AppNo). So of the 43,630 nominal PLE passers, at most 43,630 total minus the truly-never-attempted-a-match population were run through the cascade; final `master_match` (per the saved transcript) shows **36,395 `FINAL_MATCH`-equivalent + 772 `AMBIGUOUS` + 2,298 `NO_VALID_MATCH` + 4,135 `UNMATCHED_NO_APPNO`** in one captured run — i.e. roughly 15–19% of nominal PLE passers never link to any NMAT record at all (no NMAT_FINAL row with a plausible name/appno), which is unsurprising: NMAT (2006–2018 examinees) and PLE (2011–2022 passers) don't fully overlap in population — PLE includes doctors who took different pre-med entrance routes, foreign-trained returnees, or examinees before 2006.

**The commonly-quoted "~32% of NMAT records link to PLE" number is an underestimate driven entirely by the mechanical year-gap requirement, not by matching failure.** Verified by computing the best-record match rate by NMAT year:

| NMAT Year | n (best-record) | Passer rate |
|---|---|---|
| 2006–2013 | avg ~44–56% | plausible for eventual MDs |
| 2014 | 37.8% | |
| 2015 | 29.3% | fewer have had time to sit boards yet |
| 2016 | 22.5% | |
| 2017 | 4.7% | mechanically too early — needs ≥5yr gap, PLE data ends 2022 |
| 2018 | 0.08% | same |

This is exactly why the `Year<=2014` "observable cohort" rule exists in the docs — and exactly why it matters that `IS_PLE_ANALYSIS_SAFE` (§2) doesn't actually implement it. **The overall ~32% figure conflates a cohort that legitimately hasn't had time to appear in PLE_DATA yet (2015–2018) with the true, much higher, match rate for years where matching had time to complete (≈38–56% for 2006–2014).** Any dashboard quoting a single blended match-rate number without the Year≤2014 restriction is materially misleading.

**Coverage by university: cannot be assessed from PLE-side data.** `PLE_DATA.csv`/`PLE_UNMATCHED.csv` carry no institutional field whatsoever (only `FULL_NAME`, `PLE_YEAR_PASSED`, and sometimes a pre-filled `NMA_AppNo`) — there is no way to check whether particular schools are systematically under-represented among PLE passers, because the PLE side never records where anyone went to school. This reinforces the orchestrator's separate finding that no medical-school identifier exists anywhere in this dataset; it's not recoverable from Pipeline 2's inputs either.

---

## 8. False positives / name-collision risk

Empirically quantified against `NMAT_Ultima.parquet` (see §3 for method): naive collision rate (any two attempt-rows sharing a name, including a person's own repeat attempts) looks alarming — 1,301 `NAME_NORM` groups span >1 distinct `BDATE_CLEAN` among all `IS_PLE_PASSER` rows — but that number is dominated by row-level propagation across repeat attempts, not real collisions. **Restricted to one row per real confirmed-passer person (`IS_BEST_NMAT_RECORD & IS_PLE_PASSER`, 36,305 rows), the same-name/different-birthdate collision count drops to 2, both attributable to a garbled `BDATE_CLEAN` field rather than a genuine second person.** Also confirmed `PLE_DATA.csv` itself has **zero duplicate `FULL_NAME` values** (43,630 unique names, no repeats) — so the dedup-by-name step in `master_match` (§3) never actually has to arbitrate between two different real PLE passers who share a name; that risk is theoretical in this dataset, not realized. **Estimated false-match rate from name collision alone: ≈0.006% at the person level** — low, primarily because the DOB-based Step 2 of the disambiguator is doing real work whenever multiple NMAT candidates share a name.

---

## 9. Pipeline 1 findings

**B1 vs B10 — DEFINITIVE, evidence-based.** `1_Data_Cleaning_Pipeline.ipynb`, cell index 15:
```python
nmat_base["PercentileBin"] = pd.cut(
    nmat_base["NMS_PER_num"],
    bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101],
    labels=["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10"],
    right=False, include_lowest=True
)
```
Confirmed against the parquet: `B1` spans `NMS_PER_num` 0–9 (mean 4.5), `B10` spans 90–99 (mean 94.8). PLE pass rate rises monotonically from B1 (3.2%) to B10 (57.7%). **B1 is the LOWEST-scoring decile; B10 is the HIGHEST-scoring decile.** Any downstream text implying the opposite is wrong and inverts every bin-based conclusion.

**University reconciliation (2,907 vs 3,251) — explained, not a bug.** `NMA_College` (3,251 distinct values) is the raw free-text field as typed on the application form (typos, abbreviation variants, punctuation differences all counted separately). `UNIVERSITY` (2,907 distinct values) is the *post*-matching canonical value produced by the 4-tier `match_college_to_univs()` process in cell 17 (exact-primary → exact-secondary → fuzzy → unmatched-fallback, using `dataset/UNIVS.csv`'s 3,022 reference rows). Many raw-text variants of the same institution correctly collapse onto one canonical `UNIVERSITY` value; genuinely unmatched raw strings pass through unchanged. The 344-value shrinkage (10.6%) is the expected, intended effect of the cleaning step. Confirmed `1_Data_Cleaning_Pipeline.ipynb` cell 17's fallback path retains `clean_text(raw_college)` verbatim when no UNIVS match is found, so unmatched colleges don't artificially collapse into each other. **Note (relayed from orchestrator, verified consistent with Pipeline 1 code): `UNIVERSITY`/`NMA_College`/`UNI_TYPE` describe the applicant's *undergraduate* institution (the school on their NMAT application), not the medical school they later attended — there is no field anywhere in Pipeline 1 or the final schema that records a medical school. Any downstream SUC-vs-PHEI or institution-level PLE claim built on `UNI_TYPE` is describing the wrong institution.**

**Raw-score recalculation is legitimate, but the "42.2% mismatch" framing is misleading — CONFIRMED via `dataset/output/05_raw_score_validation_summary.csv`** (a saved run of cell 25's validation table):
```
cem_rows:                    254,308
stored_total_available:      174,494
stored_vs_derived_mismatch:  107,422
```
`TotalRawScoreTRUE` itself is computed correctly (sum of 8 raw component scores, only when all 8 are present, else `NaN` — cell 25). But **107,422 / 254,308 = 42.24%** — the widely-quoted "42.2%" figure — uses **all CEM rows** as the denominator, including 79,814 rows that have *no* stored total to even compare against (silently treated as "not a mismatch" via `.fillna(False)`). The mismatch rate among rows where a comparison was actually possible is **107,422 / 174,494 = 61.6%** — meaningfully higher than what's advertised. Recommend correcting the data dictionary to state the 61.6% figure (or explicitly define which denominator "42.2%" uses) since the current phrasing ("42.2% of StoredRawTotal values... were incorrect") reads as a claim about the 174,494 rows that actually have a `StoredRawTotal`, which is not what was computed. Severity: MEDIUM (directionally correct — CEM's stored totals are indeed unreliable — but the number itself doesn't mean what the prose says).

**`PERSON_KEY` construction:** built exactly once, in `2_PLE_Matching_Pipeline.ipynb` cell index 5: `NAME_NORM + "||" + BDATE_CLEAN` (normalized full name concatenated with raw birthdate string). Not rebuilt anywhere in Pipeline 1, Pipeline 3, or `4_Citizenship_Integration.py` (confirmed by grep — no other assignment to `PERSON_KEY` exists in the codebase). This is a reasonable, low-tech but functional person-identity key given no government ID is available; its main weakness is that it will fail to unify two rows for the same real person whose birthdate was transcribed inconsistently across attempts, and (rarely, per §8) could theoretically conflate two different people sharing both name and birthdate — not observed in this dataset's confirmed-passer population.

---

## 10. Pipeline 3 — live vs. dead artefacts

`3_NMAT_PLE_Analysis.ipynb`'s documented output directory (`data/`, 95 files) **does not exist in this checkout** (`ls data/` → 0 files), and no file in `data_aggregator/` or `streamlit_dashboard/` references a `data/` path or `analysis_output` path (grep, 0 hits). `dataset/analysis_output/` (Pipeline 1's QA output, ~40+ files) is similarly unreferenced by any live dashboard. **Conclusion: Pipeline 3's entire file-output surface is a dead artefact today — nothing downstream reads it.** Every live consumer (`data_aggregator/page_*.py`, `streamlit_dashboard/CHED_relevant_dashboard/`, `streamlit_dashboard/main_dashboard/dashboard.py`) recomputes statistics directly from `NMAT_Exodus.parquet` using pandas/DuckDB, not from Pipeline 3's saved CSVs.

**Statistical methodology reuse (live, CONFIRMED via grep):** Kruskal-Wallis/Mann-Whitney/chi-square methodology from Pipeline 3 is reused live in `data_aggregator/helpers.py`, `page_03_trends_stability.py`, `page_05_university_type.py`, `page_07_ple_alignment.py`, `page_10_year_gap_gender.py`, `page_11_statistical_tests.py`, and `streamlit_dashboard/main_dashboard/dashboard.py`. This means the §2/§5 findings (broken analysis-safe flag; potentially circular disambiguation for a small subset) flow directly into `page_07_ple_alignment.py` and `page_11_statistical_tests.py`'s live statistical output, not just into a dead notebook.

---

## Findings table

| ID | Severity | Status | Title | Location |
|---|---|---|---|---|
| F1 | CRITICAL | CONFIRMED | `IS_PLE_ANALYSIS_SAFE` is a byte-identical duplicate of `IS_PLE_PASSER`; never implemented `Year<=2014`, from creation onward | `2_PLE_Matching_Pipeline.ipynb` cell idx 11 (`analysis_safe = {...}` identical to `accepted_statuses`) |
| F2 | HIGH | CONFIRMED | `PLE_MATCH_METHOD`/`PLE_YEAR_PASSED` `.notna()` include rejected (`AMBIGUOUS`/`NO_VALID_MATCH`) matches; only `IS_PLE_PASSER` is the safe "confirmed passer" flag — three counts are not nested as commonly assumed | `2_PLE_Matching_Pipeline.ipynb` cell idx 11, `get_ple_info()` |
| F3 | HIGH | CONFIRMED | `MANUAL_APPNO_MATCH` (2,331 real people / 2,776 rows) has zero documented provenance for its pre-filled `NMA_AppNo` values; untracked input file, "100" confidence is a hard-coded literal, not measured | `dataset/PLE_UNMATCHED.csv`; used in `2_PLE_Matching_Pipeline.ipynb` cell idx 7 |
| F4 | MEDIUM | CONFIRMED (mechanism) / SUSPECTED (magnitude) | 5-step disambiguator's Step 5 picks among tied candidates by highest `NMS_PER_num`, then accepts if the gap is ≥5 pts — circular with score→outcome analysis for the (small, funnel-bounded) subset of same-name multi-candidate ties | `2_PLE_Matching_Pipeline.ipynb` cell idx 6, `disambiguate()` steps 4–5 |
| F5 | MEDIUM | CONFIRMED | Fuzzy matching (`rapidfuzz`) survives in Pipeline 1's university-name matching (235/3,251 colleges, 7.2%), contradicting the blanket "no fuzzy matching" claim in README/CLAUDE.md; ≥1 demonstrated false positive (Saint Leo ≠ Saint Louis University) | `1_Data_Cleaning_Pipeline.ipynb` cell idx 3 (import), cell idx 17 (`match_college_to_univs`) |
| F6 | MEDIUM | CONFIRMED | "42.2% of StoredRawTotal mismatched" uses the wrong denominator (all CEM rows, including those with no stored value); true mismatch rate among comparable rows is 61.6% | `dataset/output/05_raw_score_validation_summary.csv`; computed in `1_Data_Cleaning_Pipeline.ipynb` cell idx 25 |
| F7 | MEDIUM | CONFIRMED | Blended ~32% NMAT→PLE match-rate figure conflates cohorts that mechanically can't have matched yet (2015–2018, gap<5yr) with cohorts where matching had time to complete (~38–56% for 2006–2014); no dashboard-side Year filter compensates because F1 broke the mechanism meant to do so | `2_PLE_Matching_Pipeline.ipynb` `YEAR_GAP_MIN=5`; parquet `Year`×`IS_PLE_PASSER` cross-tab |
| F8 | LOW | CONFIRMED | Stale/incorrect in-notebook print statement claims `IS_PLE_PASSER` includes `AMBIGUOUS`; actual code (correctly) excludes it | `2_PLE_Matching_Pipeline.ipynb` cell idx 16, final print block |
| F9 | LOW | CONFIRMED | No per-university PLE coverage check is possible — `PLE_DATA.csv`/`PLE_UNMATCHED.csv` carry no institutional field at all | `dataset/PLE_DATA.csv`, `dataset/PLE_UNMATCHED.csv` (schema) |
| F10 | INFO | CONFIRMED | Pipeline 3's file outputs (`data/`, 95 files) and Pipeline 1's `analysis_output/` are dead — no live dashboard reads them; live consumers recompute from the parquet directly, but reuse Pipeline 3's statistical *methodology* (Kruskal-Wallis/Mann-Whitney/chi-square) | grep across `data_aggregator/`, `streamlit_dashboard/` |

---

## Matching-reliability statement (for dashboard display)

> PLE linkage in this dataset is deterministic, not probabilistic — every match traces to an exact application-number join or an exact normalized-name join, never approximate string matching. However: (1) roughly 4.6% of confirmed matches (2,776 of 49,986 rows / 2,331 of ~36,600 people) come from a pre-filled application-number file (`PLE_UNMATCHED.csv`) whose creation methodology is not documented in this repository and cannot be independently audited; (2) a small, structurally-bounded subset of name-collision cases were resolved by picking the candidate with the higher NMAT percentile score, which can inflate the apparent score→licensure association for that subset; (3) the overall ~32% NMAT-to-PLE match rate understates true linkage success because it includes 2015–2018 examinees who mechanically cannot have appeared in PLE data yet (PLE requires ≥5 years post-NMAT and the source PLE data ends in 2022) — restricting to 2006–2014 examinees, the real match rate is 38–56%; (4) neither PLE_DATA nor NMAT_FINAL records a medical school, so PLE outcomes can only be linked to the applicant's *undergraduate* institution, never to the medical school responsible for producing that outcome — no medical-school-level or CMO-cutoff-privilege claim can be supported by this dataset.

---

## Note on out-of-scope orchestrator message

Mid-task, the orchestrator relayed a finding (apparently intended for a different auditor reviewing a PDF policy brief / CMO requirements-traceability matrix) that `UNIVERSITY`/`NMA_College` is the applicant's undergraduate school, not their medical school, and that GIDA/IP/institutional-PLE-rate provisions of the CMO are therefore not answerable from this data. That PDF brief and requirements matrix are outside this auditor's assigned file scope (§ above), so no independent verification of the brief was performed. The undergraduate-vs-medical-school fact itself **is** independently corroborated here by reading `1_Data_Cleaning_Pipeline.ipynb`'s university-matching code (§9) — there is no medical-school field anywhere in Pipeline 1's schema, UNIVS.csv, or the final parquet — so that part of the relayed finding is consistent with this audit's own evidence.
