# A2 — Pipeline 2 (PLE Matching) Audit

Scope: `2_PLE_Matching_Pipeline.ipynb`. All numbers below are measured by reading
`dataset/NMAT_Ultima.parquet`, `dataset/output/PLE_MATCH_MASTER.csv`,
`dataset/PLE_DATA.csv`, `dataset/PLE_UNMATCHED.csv`, `dataset/output/PLE_STILL_UNMATCHED.csv`,
and by re-executing the notebook's own matching logic in-memory (no files written back).
No file in the repo was modified except this log.

---

## Verdict up front

**The PLE linkage can be trusted at the aggregate/statistical level (band-by-band rates,
the two prior orchestrator fixes are real and sound) but NOT at the individual-identity
level.** There is one clean, reproducible **CRITICAL** bug (Cell 12's name-only fallback,
below) that measurably double-credits distinct people, on top of the already-known
`MANUAL_APPNO_MATCH` false-match risk the project's own forensic audit already documents
(and undercounts). Both are root-caused in code, not speculation.

---

## CRITICAL-1: Cell 12's `name_to_ple` fallback reintroduces the exact double-counting risk `disambiguate()` exists to prevent

`disambiguate()` (Cell 6) is careful: it resolves name-collision candidate groups using
only year-gap, DOB, and latest-year — never percentile/score (confirmed sound, see
finding under Q4). When it can't resolve to a single winner it **rejects rather than
guesses** (`AMBIGUOUS_NAME_COLLISION`).

But **Cell 12's flag-application step throws that discipline away**. `get_ple_info()`
looks up a match first by the row's own `APPNO_CLEAN`; if that fails, it falls back to
`name_to_ple[NAME_NORM]` — a lookup keyed by **normalized name only, with no DOB/PERSON_KEY
check at all**:

```python
info = appno_to_ple.get(appno)
if info is None:
    info = name_to_ple.get(name)      # <-- keyed by NAME_NORM only
```

The fallback's intent (per its own comment) is to propagate a passer's flag to that
*same person's* other NMAT attempts. But because it keys on name alone, it also propagates
the flag onto **a different real person who merely shares that name** — precisely the
ambiguity `disambiguate()` was built to adjudicate and, in these cases, already resolved
correctly by picking the *other* candidate.

**Measured impact** (`NMAT_Ultima.parquet`, rows with `IS_PLE_PASSER=True`):

| Metric | N |
|---|---:|
| Distinct `NAME_NORM` values where 2+ **distinct `PERSON_KEY`s** (name+BDATE) both carry `IS_PLE_PASSER=True` | **1,624** |
| Total "extra" `PERSON_KEY`s credited beyond 1-per-name | 1,632 |
| ...of which **both** competing `PERSON_KEY`s have a populated, genuinely *different* BDATE (i.e. clearly two different people, not a same-person BDATE-format artifact — see caveat) | **232** |
| ...of which at least one side has an *empty* BDATE (ambiguous: could be the same person recorded inconsistently, or a real second person) | 1,398 (minus the ~variable overlap with format artifacts noted below) |

Concrete reproducible example — `ABANO, PAUL ANDREW BAYANI`:
```
PERSON_KEY: ABANO, PAUL ANDREW BAYANI||2/9/1993   APPNO 1111300022  IS_PLE_PASSER=True  METHOD=EXACT
PERSON_KEY: ABANO, PAUL ANDREW BAYANI||3/9/1993   APPNO 1041405823  IS_PLE_PASSER=True  METHOD=EXACT
```
Two people, different birthdates, different application numbers, both stamped as the
same confirmed PLE passer. `disambiguate()` necessarily saw both as competing candidates
(they share one `nmat_by_name` bucket) and picked one — Cell 12 then re-credited the other
anyway.

**Caveat on the 1,398/1,632 figure:** `BDATE_CLEAN` (`nmat["BDATE"].fillna("").str.strip()`)
is **never date-parsed or format-normalized** — the same real date appears as `5/9/1996`,
`09/05/1996 0:00`, and `2/23/1993 12:00:00 AM` depending on source year/system. So some
fraction of the "different PERSON_KEY" pairs are the *same* person whose DOB was recorded
in two string formats across attempts (a PERSON_KEY-fragmentation problem, not a
cross-identity leak), and the true "different-real-people" count is somewhere in the
[232, 1,632] range, not a single crisp number. 232 is the conservative floor: both sides
have a populated, non-format-explainable different date.

**Root cause is one function, one fix location**: replace the `name_to_ple` fallback's key
from `NAME_NORM` to `PERSON_KEY` (or drop the fallback and accept fewer flagged repeat-taker
sittings). This is a Cell-12 defect, not a `disambiguate()` defect — the orchestrator's two
prior fixes to `disambiguate()` did not touch this.

---

## CRITICAL-2 (already known, re-confirmed, and shown to be an undercount): `MANUAL_APPNO_MATCH` has zero identity verification at match time

Stage 0 (`PLE_UNMATCHED.csv`, 6,600 rows, 2,331 with a pre-filled AppNo) joins **directly
on that AppNo with no name check, no year-gap check, no DOB check** — `YEAR_GAP` and
`PLE_YEAR_PASSED` are hardcoded to `NaN` for every Stage-0 row because `PLE_UNMATCHED.csv`
carries no year column at all. 2,330 of these become `FINAL_MATCH` (6.5% of all 35,886
accepted matches) purely on the strength of a manually-supplied AppNo whose provenance
(who determined it, how, when) is not recorded anywhere in the repo.

Found directly while investigating Q1/Q2 (not from the forensic audit's own sample):
`PLE_MATCH_MASTER.csv` row for AppNo `400428`:

```
PLE_FULL_NAME: ABAD, ALBERTO SE?AL   (mangled encoding, itself a separate defect)
MATCHED_NMA_Name: Abad, Albert Caisip
MATCH_METHOD: MANUAL_APPNO_MATCH   MATCH_STATUS: FINAL_MATCH   MATCH_CONFIDENCE: 100
```
"Alberto Señal" and "Albert Caisip" are not the same person by any reasonable reading —
same surname, wholly different given/middle name. This is a **false PLE-passer credit**
sitting at 100% confidence in the accepted-match table, caught by inspection, not by any
automated check in the pipeline.

**The project's own forensic audit undercounts this risk.** `forensic_audit/forensic_audit.py`
classifies APPNO-based matches into buckets; only `genuine_mismatch` (36 of 2,371 checked)
is written to `forensic_audit_exceptions.csv` for human review. But its own classifier logic
puts cases exactly like ABAD/CAISIP into `same_surname_no_given_match` (same surname, no given-name
token overlap) — **22 rows**, verified by reproducing its classifier in this audit — which is
**not treated as an exception and not reviewed**. Every one of the 22 sampled looks like two
different people (e.g. `TOLENTINO, MARIEROSE LABUGUEN` vs `TOLENTINO, DIANA ROSE GILBUENA`).
Combined with the already-reported 36 `genuine_mismatch` and 491 (17.1%) uncoverable rows, the
realistic false-match exposure in the APPNO-matched population is **36 + 22 = 58 of 2,371
checked (2.4%)**, not the 1.5% the report headlines, before even counting the 17.1% that
cannot be checked at all.

---

## Q1 — Passer count semantics

- PLE_DATA.csv: 43,630 rows, **43,630 unique names already** (0 raw duplicates) — the
  "43,630 unique passer names" premise is confirmed exactly.
- `PLE_MATCH_MASTER.csv`: 43,601 rows, one per unique `PLE_NAME_NORM` (deduplicated by
  construction — verified). **29 PLE_DATA names are absent from `PLE_MATCH_MASTER.csv`
  entirely** — not matched, not marked unmatched, not marked ambiguous, just silently gone
  (see the Stage-2 provenance defect under Q3/Q6). Root cause: these 29 have zero exact-name
  NMAT candidates (`NEEDS_FUZZY` in Stage 1, which is explicitly excluded from the master
  table) and are not present in the stale `PLE_STILL_UNMATCHED.csv` checkpoint Stage 2 reads
  either. Small in count (0.066% of PLE_DATA) but a genuine, silent completeness gap.
- `IS_PLE_PASSER=True`: 49,086 sittings / 37,420 unique `PERSON_KEY`s — **matches the
  orchestrator-supplied context exactly.**
- **"Is a single PLE record ever matched to two different PERSON_KEYs?" — Yes, confirmed
  (see CRITICAL-1).** At least 232 clean cases, up to 1,624 candidate cases (name groups),
  1,632 excess `PERSON_KEY`s credited.
- **"Are people matched to more than one PLE record?"** — The pipeline has an *explicit,
  documented* mechanism for this (`PLE_YEAR_UNCERTAIN`, Cell 11's `AMBIGUOUS_YEAR_APPNOS`):
  85 distinct `MATCHED_APPNO` values are credited by 2+ different `PLE_NAME_NORM` entries
  (Case A: WHO is certain, WHICH PLE record/year is not). This produces 110 rows /
  89 `PERSON_KEY`s flagged `PLE_YEAR_UNCERTAIN=True` — surfaced, not hidden. This part of
  the design is sound: it is honestly labeled uncertain rather than silently picking one.

---

## Q2 — Why only 99.4% (not 100%) of a passer's sittings carry the flag

Measured directly: 232 of 37,420 passer `PERSON_KEY`s (0.62%) have some sittings flagged
`True` and others `False` — **matches the ~0.6% given in context exactly.**

This is **not** intentional ("flag applies from the matched sitting onward") — it is a
side effect of the same `appno_to_ple`-then-`name_to_ple` lookup order in Cell 12. When a
`MANUAL_APPNO_MATCH` pins one *specific* sitting's AppNo, that AppNo lookup succeeds only
for that one row; the person's *other* NMAT attempts have a different `APPNO_CLEAN`, so
they fall to the `name_to_ple` fallback — which for these particular `PERSON_KEY`s
apparently fails to find that name (all 8 sampled cases: the un-flagged sitting simply
reads `NOT_IN_PLE`). Sample (`ABAD, ALBERT CAISIP||09/28/1990`): 2010 sitting AppNo 400428
→ `True`/`MANUAL_APPNO_MATCH`; a second 2010 sitting, AppNo 2121003323 → `False`/`NOT_IN_PLE`.
Every sampled partial-flag case traces to `MANUAL_APPNO_MATCH` as the accepting method —
i.e. the 0.6% gap and the CRITICAL-1 leak are two faces of the same underlying design flaw
(name-vs-appno lookup priority interacting inconsistently with which specific sitting was
pinned), not two unrelated phenomena.

---

## Q3 — The matching cascade (measured, stage-by-stage)

Reproduced end-to-end in-memory from `NMAT_FINAL.csv` + `PLE_DATA.csv` + `PLE_UNMATCHED.csv`
(read-only); reconciles with the saved `PLE_MATCH_MASTER.csv` to the row.

| Stage | Input | Processed | Outcome |
|---|---|---:|---|
| **Stage 0** — Manual AppNo (`PLE_UNMATCHED.csv`) | 2,331 rows w/ AppNo | 2,331 | 2,330 `FINAL_MATCH` (100% confidence, **zero verification**), 1 `APPNO_NOT_IN_NMAT` |
| **Stage 1** — Exact name match | 41,300 PLE names (after Stage-0 exclusion) | 41,300 | 4,208 zero exact candidates (dead end); 23,197 single-candidate (23,145 `FINAL_MATCH`, 52 year-gap rejects); 13,895 routed to `disambiguate()` |
| ...within Stage 1, `disambiguate()` | 13,895 name-collision groups | 13,895 | 10,316 resolved to one winner (74.2%), 3,578 rejected `AMBIGUOUS_NAME_COLLISION` (25.7%, correctly refuses to guess), 1 fails year-gap |
| **Stage 2** — "Deterministic AppNo" | 7,207 rows from `dataset/output/PLE_STILL_UNMATCHED.csv` | 4,230 survive cross-stage dedup | 95 `FINAL_MATCH`, 4,135 `UNMATCHED_NO_APPNO` |
| **Total accepted** (`FINAL_MATCH`+`MANUAL_APPNO_MATCH`+`DETERMINISTIC_APPNO`) | | | **35,886** — matches `PLE_MATCH_MASTER.csv` exactly |

**No `rapidfuzz`/`difflib`/`SequenceMatcher` call exists anywhere in the live notebook
code** — grep-confirmed. The only "fuzzy" references left are a dead `MATCH_STATUS` label
(`NEEDS_FUZZY`) and one stale code comment ("goes to Stage 2 (fuzzy)") from when Stage 2
*was* a fuzzy stage.

**However, the "no fuzzy matching" auditability claim does not hold for the pipeline's
actual provenance.** `dataset/output/PLE_STILL_UNMATCHED.csv` — the file Stage 2 reads as
its entire input, unconditionally trusted — is a **fossil of an earlier, since-deleted
version of this pipeline that did run fuzzy matching**: 4,810 of its 7,207 rows carry
`MATCH_METHOD="FUZZY"` with reasons like `"Best fuzzy score 67 < 85 threshold"`, and some
of its `NO_VALID_MATCH` rows are stamped `"Percentile < 40 for all latest-year candidates"`
— literally the old, now-removed `PERCENTILE_FLOOR=40` bug's rejection text, frozen into a
checkpoint file the *current, fixed* notebook still reads as ground truth for "what remains
unmatched." Stage 2's 95 `FINAL_MATCH` rows and the classification of the other 4,135 as
permanently `UNMATCHED_NO_APPNO` both derive from this file, not from a live recomputation.
This also explains the 29-record Q1 gap and the general non-reproducibility of a from-scratch
run of this notebook: it structurally depends on a pre-existing `dataset/output/` file whose
own generation process is no longer present in the repo (self-referential bootstrap — Cell 16
writes `PLE_STILL_UNMATCHED_v2.csv`, and *something*, at some point, renamed a prior version
of that output back to `PLE_STILL_UNMATCHED.csv` for the next run to consume — that step is
undocumented and outside version control).

**Net assessment for Q3:** stage *order* matches the documented claim (AppNo recovery →
exact name → deterministic AppNo). The *"fully deterministic, no fuzzy matching"* claim is
true of the code currently in the notebook, but false of the pipeline's actual lineage —
fuzzy-matching output is silently inherited via Stage 2's input file.

---

## Q4 — `disambiguate()`, post-fix

Read line-by-line (Cell 6, `2_PLE_Matching_Pipeline.ipynb`).

- **Percentile floor: confirmed gone.** `PERCENTILE_FLOOR = 40` is defined but never
  referenced inside `disambiguate()`; the function has exactly 4 steps (year-gap → DOB →
  latest-year → verdict), none touching `NMS_PER_num`/percentile/bin.
- **DOB check ordering: confirmed fixed.** `nmat["BDATE_CLEAN"] = nmat["BDATE"].fillna("").str.strip()`
  (Cell 5, line 268) executes **before** `nmat_records = nmat.to_dict("records")` (line 272),
  which is what `candidates` lists are built from. The dead-code bug (`BDATE_CLEAN` key absent
  from every candidate dict) is gone; Step 2 now genuinely filters on DOB when DOB data exists.
- **No outcome-correlated variable anywhere in `disambiguate()`.** Confirmed: only
  `YEAR_INT` (year gap) and `BDATE_CLEAN` (DOB) are read for filtering; `NMS_PER_num` is
  never referenced. This specific defect class (using the outcome variable — percentile —
  to decide identity) does not survive anywhere in this function. **Sound.**
- **Weakness found (MEDIUM, not the same defect class):** `BDATE_CLEAN` is a raw string
  strip with **no date normalization**. The same date appears as `5/9/1996`,
  `09/05/1996 0:00`, `2/23/1993 12:00:00 AM` across different source years/systems (shown
  under CRITICAL-1's caveat). Step 2's "modal DOB" `Counter` comparison operates on these
  raw strings, so a same-person DOB written in two formats across attempts will not match
  and Step 2 effectively does nothing for that candidate set (it has a safe fallback —
  "if not identity_pass: identity_pass = gap_pass" — so it degrades to no-op rather than
  wrongly excluding, but it also means Step 2 provides less real filtering power than its
  code implies).
- **The real surviving identity-resolution defect is not inside `disambiguate()` at all —
  it's Cell 12's `name_to_ple` fallback (CRITICAL-1).** `disambiguate()` itself is sound
  against the specific defect class asked about (percentile/score used for identity).

---

## Q5 — Name normalization and collision quantification

`normalize_name()` (Cell 3): strips diacritics (`unidecode`), uppercases, keeps only
`[A-Z0-9, ]`, collapses whitespace. It does **not** strip suffixes (Jr./Sr./III), does
**not** reorder or canonicalize middle names, and (as shown above) has a sibling function
`normalize_surname()` for compound Filipino prefixes (De/Dela/San/...) that exists only in
`forensic_audit.py`, **not** in the matching pipeline itself — the pipeline that actually
assigns `IS_PLE_PASSER` never merges `"DE GUZMAN"`/`"DEGUZMAN"` variants.

Measured collision risk, whole NMAT dataset (`NMAT_Ultima.parquet`, 178,927 rows,
134,869 unique `PERSON_KEY`s, 123,736 unique `NAME_NORM`s):

| Metric | N |
|---|---:|
| `NAME_NORM` values shared by 2+ distinct `PERSON_KEY`s | **10,979** |
| Total distinct `PERSON_KEY`s living inside a collision group | **22,112** (16.4% of all persons) |
| Max distinct people sharing one name | 8 (`SHARMA, SHUBHAM`) |
| Names shared by ≥5 distinct people | 2 (`SHARMA, SHUBHAM`=8, `KUMAR, SACHIN`=5) |

The prompt's "common name shared by 5 people" scenario is real and measured — though the
two worst cases in this dataset are common South/West Asian names among the foreign-national
examinee population, not Filipino surnames specifically. **What the pipeline does about it**:
`disambiguate()` resolves 74.2% of 2+-candidate PLE-name groups to a single non-outcome-based
winner and rejects the remaining 25.7% outright rather than guessing (sound, see Q4) — **but**
that discipline is undermined downstream by CRITICAL-1, which can re-flag a name's other
`PERSON_KEY`s as passers regardless of `disambiguate()`'s verdict.

---

## Q6 — `PLE_UNMATCHED.csv` (Stage 0) is an unaudited manual-override channel

`PLE_UNMATCHED.csv` (6,600 rows, `FULL_NAME` + `NMA_AppNo`) is joined directly by AppNo
with no independent check (see CRITICAL-2). **2,330 of 35,886 accepted matches (6.5%)
originate here**, at 100% `MATCH_CONFIDENCE`, with `PLE_YEAR_PASSED`/`YEAR_GAP` hardcoded
to `NaN` (the file carries no year column, so **Q8's chronology check cannot even be run on
this 6.5% of accepted matches** — a real coverage gap in that safeguard). No column in the
repo records who filled in these 2,331 AppNos, when, or by what method — not reproducible,
not auditable. This is the same category of defect as Stage 2's stale checkpoint file
(Q3): **both non-exact stages rest on external, provenance-blank artifacts**, not on logic
that runs live inside the notebook.

---

## Q7 — False-positive risk (forensic audit's own outputs, re-verified)

`forensic_audit/forensic_audit.py` output, re-verified by reproducing its classifier
independently against `NMAT_Ultima.parquet` + `PLE_MATCH_MASTER.csv` (numbers match):

- 2,867 APPNO-based matches (`MANUAL_APPNO_MATCH` + `DETERMINISTIC_APPNO`) in the current
  dataset; only 2,371 (82.7%) checkable against `PLE_MATCH_MASTER.csv`.
- `forensic_audit_exceptions.csv`, 532 rows = 36 `unresolved_genuine_mismatch` + 5
  `ambiguous_source_conflict` + 491 `uncoverable_no_source_record` — reconciles exactly.
- **This audit found an additional, uncounted risk pool**: 22 rows land in
  `same_surname_no_given_match`, a verdict the classifier does not treat as an exception.
  Every sampled example (e.g. `ABAD, ALBERTO SEÑAL` vs `Abad, Albert Caisip`,
  `TOLENTINO, MARIEROSE LABUGUEN` vs `TOLENTINO, DIANA ROSE GILBUENA`) reads as two
  different people sharing only a surname. Realistic mismatch exposure in the checked
  population: **58/2,371 (2.4%)**, not the 36/2,371 (1.5%) the report's headline states —
  before accounting for the 17.1% that cannot be checked at all.
- The `EXACT`-method population (37,040 rows, 82% of all matches) is explicitly **out of
  scope** for this name cross-check by the audit's own design (matched by name equality,
  so checking the name again is tautological) — meaning **the false-positive analysis
  covers only 2,867 of the ~40,000-record accepted population; the majority (EXACT matches)
  has no independent name-based verification at all**, by design. That's defensible (name
  equality *is* the evidence for EXACT matches) but worth stating plainly: Q7's false-positive
  estimate is scoped to 6.4% of accepted matches, not all of them.

---

## Q8 — Chronological sanity (PLE year must not precede NMAT year)

Measured on all `IS_PLE_PASSER=True` rows with both `PLE_YEAR_PASSED` and `YEAR_INT`
present: **0 rows where `PLE_YEAR_PASSED < YEAR_INT`, 0 rows with a 0-year gap.** This
specific test is clean.

**Important caveat**: this test can only run on rows where `PLE_YEAR_PASSED` is populated.
It is **not populated for `MANUAL_APPNO_MATCH`** (2,330 rows, `PLE_UNMATCHED.csv` has no
year column — see Q6) and is uncertain for a subset of `DETERMINISTIC_APPNO` rows sourced
from the stale Stage-2 checkpoint. So this clean result verifies chronology for the
`EXACT`-method majority (33,461 rows) but **provides no evidence either way for the 6.5%
of accepted matches that came from Stage 0**, which is exactly the subset CRITICAL-2 shows
already contains at least one confirmed wrong-person match. A chronology check that could
catch that class of error (comparing `PLE_YEAR_PASSED` to `YEAR_INT`) is structurally
unavailable for the highest-risk stage.

---

## Summary table

| # | Finding | Severity |
|---|---|---|
| 1 | Cell 12 `name_to_ple` fallback double-credits distinct people sharing a name (232 confirmed, up to 1,632 candidate) | **CRITICAL** |
| 2 | `MANUAL_APPNO_MATCH` (2,330 matches, 6.5%) has zero identity verification at match time; confirmed wrong match found (ABAD/CAISIP); forensic audit's own classifier hides 22 more likely-wrong matches in a non-exception bucket | **CRITICAL** |
| 3 | Stage 2 ("Deterministic AppNo") silently depends on a stale checkpoint file that is itself a fossil of a removed fuzzy-matching stage and the old percentile-floor bug; not reproducible from a clean checkout; source of 29 silently-vanished PLE_DATA records | **HIGH** |
| 4 | Q8's chronology safeguard cannot run on Stage-0 matches (no PLE year available) — the one check that could catch CRITICAL-2-class errors is blind to the stage most likely to need it | **HIGH** |
| 5 | `BDATE_CLEAN` has no date-format normalization, weakening `disambiguate()` Step 2 and partly inflating the CRITICAL-1 count | MEDIUM |
| 6 | `disambiguate()` itself (percentile floor removed, DOB-ordering bug fixed, no outcome-correlated variable used) | **Sound, confirmed** |
| 7 | Matching-cascade stage order and "no live fuzzy code" claim | **Sound as stated**, but see Finding 3 for the provenance caveat |
| 8 | `IS_PLE_PASSER` = 49,086 / 37,420 PERSON_KEYs, disambiguator funnel (74.2% resolved / 25.7% honestly rejected) | Confirmed accurate, reconciles to the row |
