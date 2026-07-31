# Audit 02 — Dataset Lineage, Schema Integrity, Column-Slimming

Scope: `dataset/NMAT_Ultima.parquet` -> `NMAT_Exodus.parquet.bak` (118 cols) -> `NMAT_Exodus.parquet` (54 cols, slim).
All commands run with `./.venv/Scripts/python.exe`. All row/column counts below are CONFIRMED by execution unless marked SUSPECTED.

## Verdict

**The 118 -> 54 column slim is, mechanically, a safe operation.** Every one of the 64 dropped columns was
byte-verified as either (a) never referenced by any of the 5 audited consumer groups (main dashboard, CHED
dashboard, `data_aggregator/*.py`, `ched_compute/*.py`, `forensic_audit/*.py`), or (b) referenced only via a
guarded `if col not in df.columns: recompute-from-scratch` fallback that reconstructs the value correctly from
a surviving column (`YEAR_INT` from `Year`, `IS_BOARD_OBSERVABLE_COHORT` from `Year<=2014`, `NMA_College_norm`
from `NMA_College`). The 54 surviving columns are **provably identical, value-for-value and dtype-for-dtype**,
between `.bak` and the slim parquet (positional row alignment confirmed). Pipeline 4 (`Ultima -> .bak`) touched
nothing except adding 3 new citizenship columns.

**However, the slim parquet is not a safe basis for stakeholder-facing numbers as-is**, because of defects that
predate the slimming and live inside the 54 surviving columns themselves:
- `IS_BEST_NMAT_RECORD` (the flag every "unique examinee" / "repeat taker" / "PLE pass rate" metric in both
  dashboards filters on) silently drops 1,311 confirmed PLE passers to zero best-records, and double-flags 246
  other people — a real, quantified miscount in the dedup logic (Finding 2/3).
- `PERSON_KEY` (`NAME_NORM||BDATE`) collides for different people at a measurable rate — 4.6% of all keys carry
  internally contradictory `SEX`, and ~18% of "repeat taker" counts are built on top of that same construction
  (Finding 4).
- A hardcoded "42.2%" data-quality claim, repeated in the actual CHED-facing deliverable
  (`complete_markdown/CHED_NMAT_Dashboard_Complete.md`), is **wrong** — the true figure is 56.45% (Finding 1).
- One standalone script (`ched_compute/06_data_limitations.py`) still has the string-vs-bool truthiness bug the
  repo's commit 619a150 was supposed to have fixed everywhere; its already-generated output file in the repo
  shows self-contradictory numbers (Finding 5).

None of these four are consequences of the column slim — they would be present with the 118-column `.bak` too.
The slim is a correct extraction of a flawed 54-column subset.

---

## Findings Table

| ID | Severity | Status | Title | file:line |
|----|----------|--------|-------|-----------|
| F1 | CRITICAL | CONFIRMED | "42.2% of StoredRawTotal incorrect" is false; true rate is 56.45% — quoted verbatim in the CHED-facing deliverable | `streamlit_dashboard/CHED_relevant_dashboard/complete_markdown/CHED_NMAT_Dashboard_Complete.md:13,543`; `ched_compute/06_data_limitations.py:69`; `dashboard.py:1155`; `CLAUDE.md` |
| F2 | CRITICAL | CONFIRMED | `IS_BEST_NMAT_RECORD` never set True for 1,311 `PERSON_KEY`s (1,497 rows), all of them confirmed PLE passers — silently excluded from every best-record-filtered metric | `2_PLE_Matching_Pipeline.ipynb` Cell 13 (matched-appno flagging step) |
| F3 | HIGH | CONFIRMED | `IS_BEST_NMAT_RECORD` set True twice for 246 `PERSON_KEY`s — row-count metrics (`len(best)`) overcounted by up to 246; `.nunique()`-based metrics unaffected | `2_PLE_Matching_Pipeline.ipynb` Cell 13 |
| F4 | HIGH | CONFIRMED | `PERSON_KEY = NAME_NORM+"\|\|"+BDATE_CLEAN` is collision-prone: 6,148/134,869 keys (4.6%) contain rows with contradictory `SEX`; 18.2% of "repeat taker" `PERSON_KEY`s show this signature | `2_PLE_Matching_Pipeline.ipynb` Cell 5 |
| F5 | HIGH | CONFIRMED | Unfixed string-vs-bool truthiness bug (`== True` / `== 1.0` on `str` columns) in a live standalone script; its committed output shows "0" contradicted by a hardcoded "(99.97%)" on the same line | `streamlit_dashboard/CHED_relevant_dashboard/ched_compute/06_data_limitations.py:39,48,49,71`; artifact at `ched_compute/page_results/06_data_limitations.md:24,26,27` |
| F6 | MEDIUM | CONFIRMED | `IS_PLE_ANALYSIS_SAFE` is a pure duplicate of `IS_PLE_PASSER`, not "observable cohort Year<=2014" as CLAUDE.md/data dictionary claim; misleading name is a landmine for future contributors, even though current code never triggers the 100%-by-construction trap | pervasive; see Finding 6 |
| F7 | MEDIUM | CONFIRMED | `IS_BEST_NMAT_RECORD` tiebreak order contradicts documentation: code picks highest-percentile-then-latest-year, docs say latest-year-then-highest-percentile; 4,451/97,499 (4.6%) non-PLE-passer persons get a different "best" record under the two rules | `2_PLE_Matching_Pipeline.ipynb` Cell 13 vs `CLAUDE.md` "Best-Record Deduplication" |
| F8 | LOW | CONFIRMED | Duplicate `APPNO_CLEAN` "1073584" is a genuine source data-entry duplicate (identical name/test-date/college, different `NMS_PER_num` 98 vs 80); it is also one of the 246 F3 cases | `dataset/NMAT_CLEANED_DATA.csv` (source), rows 8829/8830 of slim parquet |
| F9 | LOW | CONFIRMED | Column-slimming itself is value-exact and row-order-preserving; Ultima->`.bak` (pipeline 4) added only 3 citizenship columns, changed nothing else | see Finding 9 |
| F10 | LOW | CONFIRMED | `name_based_assessment` (99.5% null), `AllRawComponentsPresent` and `CalcVsDerivedMismatch` (both constant, nuniq=1) are dead weight kept in the 54-col slim for no operational reason | see appendix |
| F11 | INFO | CONFIRMED | 4 different "PLE matched" counts exist in the data (49,986 / 54,528 / 57,304 / 48,842); all dashboards consistently use the `IS_PLE_PASSER`/`IS_PLE_ANALYSIS_SAFE` figure (49,986), so this is not currently a display inconsistency, but the divergence itself is undocumented | shared context; not further pursued in this audit |

---

## Finding 1 — False "42.2%" claim (CRITICAL, CONFIRMED)

CLAUDE.md and the CHED dashboard both claim "42.2% of `StoredRawTotal` values were mathematically incorrect."
Ran the actual comparison on all 99,316 non-null `StoredRawTotal` rows:

```python
sub3 = df.dropna(subset=["StoredRawTotal","TotalRawScoreTRUE"])   # 99,316 rows
mismatch3 = (sub3["StoredRawTotal"].round(6) != sub3["TotalRawScoreTRUE"].round(6))
# Mismatches: 56065 / 99316 = 56.45%
```
This matches `StoredVsDerivedMismatch` value_counts exactly (`'1.0': 56065, '0.0': 43251`). **True mismatch rate
is 56.45%, not 42.2%.** The false "42.2%" figure is hardcoded as prose (not computed from data) in:
- `streamlit_dashboard/CHED_relevant_dashboard/complete_markdown/CHED_NMAT_Dashboard_Complete.md:13,543` — **this is the actual file distributed to CHED**
- `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py:240,292,1155`
- `streamlit_dashboard/CHED_relevant_dashboard/export_markdown.py`
- `streamlit_dashboard/CHED_relevant_dashboard/ched_compute/06_data_limitations.py:69`
- `README.md`, `docs/data_dictionary.md`, `docs/pipeline_architecture.md`, `CLAUDE.md`, and 3 files under `reports/`

The arithmetic recalculation itself is sound (see Finding 9b below) — only the stated *mismatch percentage* is wrong.

## Finding 2 — 1,311 confirmed PLE passers get zero best-record flag (CRITICAL, CONFIRMED)

```python
counts = df.groupby("PERSON_KEY")["IS_BEST_NMAT_RECORD"].sum()
(counts==0).sum()   # -> 1311 PERSON_KEYs
(counts==1).sum()   # -> 133312
(counts>=2).sum()   # -> 246
```
The 1,311 zero-flag `PERSON_KEY`s cover 1,497 rows, and **every single one is `IS_PLE_PASSER == True`**
(`zero_df["IS_PLE_PASSER"].sum() == 1497`). More broadly, 13,681 rows total are `IS_PLE_PASSER==True` but
`IS_BEST_NMAT_RECORD==False` (most belong to `PERSON_KEY`s that *do* have a best row elsewhere from a different
attempt; the 1,497 above are the subset with no best row at all for that person).

Root cause (`2_PLE_Matching_Pipeline.ipynb`, "CELL 13 — IS_BEST_NMAT_RECORD flag"): matched-PLE rows are flagged
by simple `APPNO_CLEAN.isin(matched_appnos)` membership, with no per-`PERSON_KEY` "ensure at least one" fallback
and no dedup safeguard. Any `PERSON_KEY` whose PLE-match row got excluded upstream (e.g. superseded by a later
match, or filtered by `accepted_statuses`) ends up with **no best record at all**, dropping that examinee out of
`len(best)`, `best["PERSON_KEY"].nunique()`, and every tab/page that filters on `IS_BEST_NMAT_RECORD==True`
(main dashboard "Unique examinees" metric, CHED dashboard `N_UNIQUE`, `data_aggregator/page_01/08`,
`ched_compute/verified_true/verifier_01_national_profile.py:33`, etc.) even though the person is a documented
PLE passer.

**Impact:** `best["PERSON_KEY"].nunique()` = 133,558 vs. true unique `PERSON_KEY` count = 134,869 — an
undercount baked into every "unique examinees" statistic across both dashboards.

## Finding 3 — 246 PERSON_KEYs double-flagged as best (HIGH, CONFIRMED)

Same cell: the "unmatched persons" branch groups by `PERSON_KEY` *within the unmatched-only subset* and picks
one row, without checking whether that `PERSON_KEY` already has a matched-and-flagged best row from a *different*
attempt. Result: a person who is a confirmed PLE passer (matched row flagged True) but who also has an earlier,
unrelated, unmatched NMAT attempt gets **that** attempt flagged True too.

```python
dup_pks = counts[counts>=2].index      # 246 keys
best = df[df["IS_BEST_NMAT_RECORD"]]
len(best)                              # 133,804 rows
best["PERSON_KEY"].nunique()           # 133,558 unique persons  <- these two disagree by exactly 246
```
Example (`ABUEVA, AILEEN CRYSTEL DIMAYACYAC||`): both rows are `IS_PLE_PASSER==True` with **different**
`PLE_YEAR_PASSED` (2013 vs 2018) — this person appears to have matched to two separate PLE records.

**Impact:** row-count metrics (`len(best)`, e.g. `f"{len(best):,}"` in several page headers) are inflated by up
to 246; `.nunique()`-based metrics (the more commonly used pattern) self-correct because `nunique()` dedupes
`PERSON_KEY` regardless of row count.

## Finding 4 — PERSON_KEY collision rate (HIGH, CONFIRMED)

`2_PLE_Matching_Pipeline.ipynb` Cell 5:
```python
nmat["PERSON_KEY"] = nmat["NAME_NORM"] + "||" + nmat["BDATE_CLEAN"]
```
`BDATE` is null for 25,204/178,927 raw rows (14%), and even where present is a free-text field with format
inconsistencies (`00/00/0000` placeholders observed). Empirical collision test — same `PERSON_KEY`, contradictory
recorded `SEX`:
```python
sex_nunique = df.dropna(subset=["SEX"]).groupby("PERSON_KEY")["SEX"].nunique()
(sex_nunique > 1).sum()   # 6,148 PERSON_KEYs / 134,869 total = 4.56%
```
Sample (`ABAD, AINA GENE CRUZ||06/25/1997`): 2017 Female @ Far Eastern University (percentile 32) vs. two 2018
Male rows at two different universities (percentile 5, 33) — three different people sharing one `PERSON_KEY`,
not one repeat-taker.

Cross-referenced against "repeat taker" counts (the metric reported on both dashboards' Repeat Taker tabs and
`data_aggregator/page_08_repeat_takers.py`):
```python
repeat_keys = attempt_ct[attempt_ct>1].index          # 33,713 PERSON_KEYs (matches CLAUDE.md's "25%" figure)
len(repeat_keys & contradictory_sex_keys)              # 6,148
6148/33713*100                                         # 18.2%
```
**Up to 18.2% of examinees counted as "repeat takers" may actually be two-or-more different individuals merged
by a name+birthdate collision**, not one person retaking the exam. This also means "unique examinees" (134,869)
is itself an overcount of true unique humans (merges some, but the direction of the *repeat-taker* bias and the
*unique-count* bias are opposite and don't cancel out cleanly — this needs upstream fixing, not adjustment here).

## Finding 5 — Live truthiness bug in `ched_compute/06_data_limitations.py` (HIGH, CONFIRMED)

Both `main_dashboard/dashboard.py` and `CHED_relevant_dashboard/dashboard.py` correctly normalize
`HasTRUErawScores`/`StoredVsDerivedMismatch`/`CalcVsDerivedMismatch` from `str` to real bool/numeric dtype before
any comparison (`main_dashboard/dashboard.py:85-98` `BOOL_COLS`+`to_bool_series`; `CHED dashboard.py:87-103`
`validate_schema`) — this matches the "fixed everywhere" claim for the live Streamlit apps. **But one standalone
script was missed**:

```python
# streamlit_dashboard/CHED_relevant_dashboard/ched_compute/06_data_limitations.py:39,48,49
n_true = int((df["HasTRUErawScores"] == True).sum())              # always 0 (str "True" != bool True)
stored_mismatch = int((df["StoredVsDerivedMismatch"] == 1.0).sum())  # always 0 (str "1.0" != float 1.0)
calc_mismatch = int((df["CalcVsDerivedMismatch"] == 1.0).sum())      # always 0
```
Confirmed empirically:
```python
df["HasTRUErawScores"].dtype              # str; {'True': 178882, 'False': 45}
(df["HasTRUErawScores"] == True).sum()    # 0
```
The already-generated artifact committed to the repo, `ched_compute/page_results/06_data_limitations.md`,
shows the resulting self-contradiction verbatim:
```
- Rows with complete TRUE scores: 0 (99.97%)
- Stored-vs-derived mismatches: 0
- Calc-vs-derived mismatches: 0
```
(line 24, "0" next to a hardcoded, uncomputed "(99.97%)" string literal at `06_data_limitations.py:71`; line 26
should read 56,065.) The repo's own verifier
(`ched_compute/verified_true/verifier_06_data_limitations.py:35-37,72-86`) documents this exact bug and computes
both the buggy value and the "actual" correct value side by side — but its pass/fail check
(`VERIFIER_streamlit_output_log_06.md:31-37`) marks it **"PASS"** because it only checks that the script's output
matches the script's own (buggy) logic, not that the logic is correct. This gives false confidence that page 6 is
verified.

**Mitigating factor:** the actual CHED-facing deliverable (`complete_markdown/CHED_NMAT_Dashboard_Complete.md:547,594`)
shows the *correct* values (178,882 / 56,065), because it is generated via `export_markdown.py`, which receives
`df_all` already normalized by `dashboard.py`'s `validate_schema()` — a different code path than the buggy
standalone script. So this specific bug has not (yet) reached the distributed document, but the wrong artifact
is checked into the repo and could be picked up by a future contributor or re-run of `ched_compute/06_data_limitations.py`.

## Finding 6 — IS_PLE_ANALYSIS_SAFE naming/documentation is false (MEDIUM, CONFIRMED)

Per shared orchestrator context, `IS_PLE_ANALYSIS_SAFE` is byte-identical to `IS_PLE_PASSER`
(`(df.IS_PLE_ANALYSIS_SAFE == df.IS_PLE_PASSER).all() == True`), not "observable cohort Year<=2014" as
CLAUDE.md/data_dictionary.md state. Grepped every use across both dashboards, `ched_compute/*`, and
`data_aggregator/*` (40+ call sites): **every single usage treats it as a passer/confirmation flag**
(`HAS_CONFIRMED_PLE = (IS_PLE_ANALYSIS_SAFE == True)`, `PLE_STATUS_LABEL`, `.sum()`/`.mean()` numerators) —
never as a denominator-restriction ("give me the cohort eligible for analysis"). The actual Year<=2014
restriction is applied separately and correctly everywhere via `Year<=2014` / `IS_BOARD_OBSERVABLE_COHORT`
(itself always recomputed from `Year`, since it does not exist in the parquet — see F9). **So the shared-context
worry ("any pass-rate denominator filtered on IS_PLE_ANALYSIS_SAFE yields 100% by construction") does not
currently manifest in any of the 5 audited consumer groups** — but the column name and the CLAUDE.md doc text
are false, and this is exactly the kind of landmine a future contributor filtering "the observable cohort" by
name would step on.

## Finding 7 — Best-record tiebreak order contradicts documentation (MEDIUM, CONFIRMED)

CLAUDE.md: *"latest year -> highest percentile -> earliest attempt."* Actual code
(`2_PLE_Matching_Pipeline.ipynb` Cell 13):
```python
unmatched_nmat.sort_values(["PERSON_KEY","NMS_PER_num","YEAR_INT"],
                            ascending=[True, False, False]).groupby("PERSON_KEY").head(1)
```
This sorts by **percentile first, year second** — the reverse of the documented order. Quantified the practical
difference on the 97,499 non-PLE-passer persons (the only branch this tiebreak applies to):
```python
# actual rule vs. documented rule, same data:
diff = 4451   # of 97499 (4.6%) persons get a DIFFERENT "best" NMAT attempt selected
```

## Finding 8 — The one duplicate APPNO_CLEAN (LOW, CONFIRMED)

```python
slim["APPNO_CLEAN"].duplicated(keep=False).sum()   # 2 rows, same value: "1073584"
```
Both rows: `VENTANILLA, GLEN TAN`, test date 12/9/2007, `University Of The Philippines - Diliman`, `NMA_Sex=1`,
`NMA_BirthDate=00/00/0000`, `SOURCE_NMAT=NMAT_CLEANED_DATA`, `PLE_MATCH_STATUS=FINAL_MATCH` for both. The only
difference is `NMS_PER_num` (98.0 vs 80.0). This is a **genuine source data-entry duplicate** in
`NMAT_CLEANED_DATA.csv` (identical application, two different recorded percentiles), not a hash collision or a
join bug — `APPNO_CLEAN` itself is copied verbatim from source, not derived. It survived every pipeline stage
unresolved and is also the direct cause of one of the 246 Finding-3 double-best-flag cases (`PERSON_KEY =
"VENTANILLA, GLEN TAN||"`, both rows flagged `IS_BEST_NMAT_RECORD=True` because both share the one
`APPNO_CLEAN` that matched a PLE record).

## Finding 9 — Column slimming is value-exact (LOW / reassuring, CONFIRMED)

```python
bak = pd.read_parquet("dataset/NMAT_Exodus.parquet.bak")   # 178927 x 118
slim = pd.read_parquet("dataset/NMAT_Exodus.parquet")      # 178927 x 54
(bak["APPNO_CLEAN"].values == slim["APPNO_CLEAN"].values).all()   # True -> row order preserved, positional join valid
# for all 54 common columns: dtype AND (values or matching-NaN) identical, zero diffs
```
64 columns were dropped between `.bak` and slim (full list and grouping below). None of the 64 are referenced,
unguarded, by any of the 5 audited consumer groups. Grouping of the 64 dropped columns:
- **Raw NMAT source fields** (superseded by cleaned equivalents): `NMA_AppNo`, `NMA_Name`, `NMA_Sex`,
  `NMA_BirthDate`, `NMA_College_RAW`, `NMA_College_norm`, `NMA_Course`, `NMA_Graduating`, `NMA_TestDate`,
  `NMA_YearGrad`, `NMC_Center`, `NMS_PER`, `STU_NO_clean`, `STU_TESTDATE`, `NMAT_YEAR`, `YEAR_INT`, `KEY`
- **Personal/demographic detail not needed downstream**: `AGE`, `BDATE`, `BDATE_CLEAN`, `CIVIL_STATUS`,
  `NAME_NORM`, `NAC_NATIONALITY`, `NMAT Province local address`, `NMAT Region permanent address`
- **CEM raw/standardized subtest duplicates** (superseded by `Raw_*`/`NMS_*ss`): `Std_Biology_CEM`,
  `Std_Chemistry_CEM`, `Std_InductiveReasoning_CEM`, `Std_PerceptualAcuity_CEM`, `Std_Physics_CEM`,
  `Std_Quantitative_CEM`, `Std_SocialScience_CEM`, `Std_Verbal_CEM`
- **Course/college classification detail**: `COLLEGE_NAME`, `COURSE_DESC`, `Course Classification`,
  `Course_recode`, `School Type_rec2_FINAL`, `MED_SCHOOL_CHOICE1/2/3`
- **Pipeline-1 university verification working columns** (superseded by final `UNI_TYPE`/`UNI_LOCATION`):
  `UNIVERSITY_VERIFIED`, `UNI_LOCATION_VERIFIED`, `UNI_TYPE_VERIFIED`, `draft_hint_method`, `draft_hint_score`,
  `draft_uni_location`, `draft_uni_type`, `draft_university`, `confidence`, `evidence_summary`,
  `final_value_source`, `merge_verified_university`, `verification_method`, `verification_status`
- **Raw score QA working columns**: `STU_RSCORE`, `STU_RSCORE_CALC`, `STU_RSCORE_VALID`, `raw_component_count`
- **PLE matching audit trail**: `PLE_MATCH_REASON`, `PLE_MATCH_STATUS` (superseded by `PLE_MATCH_METHOD`)
- **Merge/source bookkeeping**: `SOURCE_NMAT`, `merge_cem`

9b. Arithmetic checks for the surviving raw-score columns, all rows with data present (178,882):
```python
(sub[raw_8_cols].sum(axis=1).round(6) != sub["TotalRawScoreTRUE"].round(6)).sum()          # 0 mismatches
(sub2["PartIRawScoreTRUE"]+sub2["PartIIRawScoreTRUE"] != sub2["TotalRawScoreTRUE"]).sum()   # 0 mismatches
```
`TotalRawScoreTRUE` is exactly the sum of the 8 `Raw_*` components and exactly `PartI+PartII` for all 178,882
rows with data. This part of the pipeline's design claim is **fully verified correct** — only the "42.2%"
mismatch-rate claim (Finding 1) is wrong.

9c. Ultima -> `.bak` (pipeline 4) delta:
```python
bak_cols - ultima_cols   # set() -> nothing removed
ultima_cols - bak_cols   # set() -> nothing removed either direction except additions below
added_by_p4 = ['CITIZENSHIP_FINAL', 'FOREIGNER_STATUS', 'name_based_assessment']
# all 115 shared columns: zero dtype/value diffs between Ultima and .bak
# row counts: Ultima 178,927 == .bak 178,927 == slim 178,927
```

## Finding 10 — Dead columns kept in the slim (LOW, CONFIRMED)

- `name_based_assessment`: null for 178,056/178,927 rows (99.5%). Only 871 non-null (matches shared-context
  figure). Referenced only in `main_dashboard/dashboard.py`.
- `AllRawComponentsPresent`: constant, `{'True': 178882, NaN: 45}` — every non-null value is the same.
- `CalcVsDerivedMismatch`: constant, `{'0.0': 178882, NaN: 45}` — every non-null value is the same.
- `HasCEMMatch`: not constant (`{'True': 178882, 'False': 45}`) but referenced only in `main_dashboard/dashboard.py`'s
  `BOOL_COLS` list; not consumed by the CHED dashboard, `data_aggregator`, or `forensic_audit`.

None of these cause wrong numbers (the constant ones can't, and `HasCEMMatch`/`name_based_assessment` are
correctly guarded where used) — they're just unused/near-unused weight in the "slim" schema.

---

## Appendix — Full 54-Column Reference (slim `NMAT_Exodus.parquet`)

Consumer legend: **main** = `streamlit_dashboard/main_dashboard/dashboard.py`; **ched** =
`CHED_relevant_dashboard/dashboard.py` + `export_markdown.py`; **compute** = `ched_compute/*.py` (incl.
`verified_true/`); **aggr** = `data_aggregator/*.py`; **forensic** = `forensic_audit/*.py`.

| Column | dtype | Nulls | Meaning | Consumers | Integrity caveat |
|---|---|---|---|---|---|
| APPNO_CLEAN | str | 0 | Cleaned NMAT application number, primary near-unique identifier of one exam attempt | main, ched, compute, aggr, forensic | 1 duplicate value across 2 rows (Finding 8) — do not assume unique without dedup |
| PERSON_KEY | str | 0 | `NAME_NORM + "\|\|" + BDATE_CLEAN`; intended person-level identifier | main, ched, compute, aggr, forensic | Collision-prone: 4.6% of keys have contradictory SEX (Finding 4). Not a true unique-person key. |
| Year | int64 | 0 | NMAT exam year, 2006-2018 | main, ched, compute, aggr, forensic | none found |
| SEX | str | 45 | Recorded sex at time of NMAT registration | main, aggr | Used to detect PERSON_KEY collisions (Finding 4); the 45 nulls track the 45 rows missing across nearly all raw-score fields (likely 45 corrupt/incomplete source rows) |
| NMA_College | str | 0 | Cleaned university/college name as recorded on NMAT application | main, compute, aggr | Distinct from the verified `UNIVERSITY` field |
| UNIVERSITY | str | 0 | Final verified university name (post pipeline-1 4-tier matching) | main, ched, aggr | none found |
| UNI_LOCATION | str | 0 | Verified university location/region | main, aggr | none found |
| UNI_TYPE | str | 0 | Public / Private / Foreign / Not Specified (school classification) | main, ched, compute, aggr | "Foreign" describes the school, not the examinee's citizenship — only 731/2,315 Foreign-UNI_TYPE rows are Verified Foreigners (shared context) |
| CourseGroup | str | 0 | 6-value course classification (Medical & Allied, etc.) | main, ched, compute, aggr | none found |
| PercentileBin | str | 4,141 | B1-B10 decile bin of NMS_PER_num | main, ched, compute, aggr, forensic | Nulls track missing NMS_PER_num |
| NMS_PER_num | float64 | 1,275 | Standardized overall NMAT percentile | main, ched, compute, aggr, forensic | none found beyond nulls |
| NMS_GPS | int64 | 0 | General Point Score subtest, standardized | main, ched, compute, aggr | none found |
| NMS_APT | int64 | 0 | Aptitude subtest, standardized | main, compute, aggr | none found |
| NMS_SA | int64 | 0 | Science Achievement subtest, standardized | main, compute, aggr | none found |
| NMS_VCss | int64 | 0 | Verbal subtest, standardized | main, aggr | none found |
| NMS_IRss | int64 | 0 | Inductive Reasoning subtest, standardized | main, aggr | none found |
| NMS_Qss | int64 | 0 | Quantitative subtest, standardized | main, aggr | none found |
| NMS_PAss | int64 | 0 | Perceptual Acuity subtest, standardized | main, aggr | none found |
| NMS_BIOss | int64 | 0 | Biology subtest, standardized | main, aggr | none found |
| NMS_PHYss | int64 | 0 | Physics subtest, standardized | main, aggr | none found |
| NMS_SSCss | int64 | 0 | Social Science subtest, standardized | main, aggr | none found |
| NMS_CHEMss | int64 | 0 | Chemistry subtest, standardized | main, aggr | none found |
| TotalRawScoreTRUE | float64 | 45 | Recalculated raw total = sum of 8 Raw_* components | main, ched, compute, aggr | Verified arithmetically exact for all 178,882 non-null rows (Finding 9b) |
| PartIRawScoreTRUE | float64 | 45 | Recalculated Part I raw score | main, ched, compute, aggr | Part I + Part II == Total for all rows (Finding 9b) |
| PartIIRawScoreTRUE | float64 | 45 | Recalculated Part II raw score | main, ched, compute, aggr | see above |
| Raw_Verbal | float64 | 45 | Raw score, Verbal component | main, aggr | sums correctly into TotalRawScoreTRUE |
| Raw_InductiveReasoning | float64 | 45 | Raw score, Inductive Reasoning | main, aggr | same |
| Raw_Quantitative | float64 | 45 | Raw score, Quantitative | main, aggr | same |
| Raw_PerceptualAcuity | float64 | 45 | Raw score, Perceptual Acuity | main, aggr | same |
| Raw_Biology | float64 | 45 | Raw score, Biology | main, aggr | same |
| Raw_Physics | float64 | 45 | Raw score, Physics | main, aggr | same |
| Raw_SocialScience | float64 | 45 | Raw score, Social Science | main, aggr | same |
| Raw_Chemistry | float64 | 45 | Raw score, Chemistry | main, aggr | same |
| StoredRawTotal | float64 | 79,611 | Original (uncorrected) raw total from CEM source | main, aggr | 56.45% (56,065/99,316) of non-null values disagree with TotalRawScoreTRUE — CLAUDE.md's "42.2%" claim is wrong (Finding 1) |
| StoredVsDerivedMismatch | str | 79,611 | Flag: does StoredRawTotal disagree with derived total | main, ched, compute, aggr | **Stored as string** ("1.0"/"0.0"/NaN); still causes a live truthiness bug in `ched_compute/06_data_limitations.py` (Finding 5) |
| CalculatedRawTotal_Source | float64 | 45 | Provenance/source flag for the recalculated total | main, aggr | not deeply audited |
| AllRawComponentsPresent | str | 45 | Flag: were all 8 raw components present for this row | main | **Constant** (all non-null = "True") — dead column (Finding 10) |
| CalcVsDerivedMismatch | str | 45 | Flag: calc-vs-derived mismatch | main, ched, compute, aggr | **Constant** (all non-null = "0.0") — dead column (Finding 10) |
| HasTRUErawScores | str | 0 | Flag: row has valid recalculated raw scores | main, ched, compute, aggr | **Stored as string**; correctly normalized in both live dashboards, still buggy in `ched_compute/06_data_limitations.py` (Finding 5) |
| HasCEMMatch | str | 0 | Flag: row matched to a CEM source record | main | Stored as string; only consumed in main dashboard's guarded BOOL_COLS path |
| APT_CEM | float64 | 45 | CEM-source Aptitude score | main, aggr | not deeply audited |
| SA_CEM | float64 | 45 | CEM-source Science Achievement score | main, aggr | not deeply audited |
| GPS_CEM | float64 | 45 | CEM-source General Point Score | main, aggr | not deeply audited |
| Percentile_CEM | float64 | 4,182 | CEM-source percentile | main, compute, aggr | not deeply audited |
| IS_BEST_NMAT_RECORD | bool | 0 | Flag: this is the selected "best" attempt for this PERSON_KEY | main, ched, compute, aggr, forensic | **1,311 PERSON_KEYs have zero True (Finding 2); 246 have two True (Finding 3); tiebreak order contradicts docs for 4.6% of cases (Finding 7)** |
| IS_PLE_PASSER | bool | 0 | Flag: this row's examinee was matched to a PLE-passer record | main, compute | Authoritative passer count = 49,986; 3 other "PLE matched" counts in the data disagree (Finding 11) |
| IS_PLE_ANALYSIS_SAFE | bool | 0 | Documented as "observable cohort Year<=2014"; **actually identical to IS_PLE_PASSER** | main, ched, compute, aggr, forensic | Misleading name/docs (Finding 6); real cohort restriction is applied separately via Year<=2014 everywhere it's used |
| PLE_MATCH_METHOD | str | 121,623 | EXACT / MANUAL_APPNO_MATCH / DETERMINISTIC_APPNO / null | main, aggr, forensic | 57,304 non-null, disagrees with the 49,986 IS_PLE_PASSER count (Finding 11) |
| PLE_MATCH_CONFIDENCE | float64 | 121,623 | Confidence score for the PLE match | main, aggr | not deeply audited |
| PLE_YEAR_PASSED | float64 | 124,399 | Year the examinee passed PLE | main, aggr, forensic | 54,528 non-null, disagrees with the 49,986 IS_PLE_PASSER count (Finding 11) |
| PLE_YEAR_GAP | float64 | 130,085 | Years between NMAT attempt and PLE pass | main, ched, compute, aggr, forensic | 48,842 non-null, disagrees with the 49,986 IS_PLE_PASSER count (Finding 11) |
| CITIZENSHIP_FINAL | str | 0 | Final canonicalized citizenship (91 distinct values) | main, ched, compute, aggr | Added by pipeline 4; not present before Ultima |
| FOREIGNER_STATUS | str | 0 | Filipino / Verified Foreigner / Likely Foreigner | main, ched, compute, aggr, forensic | "Likely Foreigner" is only 13 rows total — near-unused category; added by pipeline 4 |
| name_based_assessment | str | 178,056 | Name-based citizenship inference note | main | 99.5% null; effectively dead weight (Finding 10); added by pipeline 4 |

---

## Notes on scope not fully pursued

- Finding 11 (the 4 disagreeing PLE-match counts) was confirmed present in the data but not traced to its root
  cause in the matching pipeline — that likely belongs to whichever auditor covers PLE-matching logic
  specifically, since it did not manifest as a display bug in the 5 consumer groups I checked (they consistently
  use the `IS_PLE_PASSER`/`IS_PLE_ANALYSIS_SAFE` figure).
- I did not exhaustively re-derive `CITIZENSHIP_FINAL`/`FOREIGNER_STATUS` tier logic (pipeline 4) beyond
  confirming row counts and that no values changed between Ultima and `.bak` outside the 3 added columns — that
  is citizenship-integration territory, likely covered by another auditor.
