# A1 — Pipeline 1 Audit (`1_Data_Cleaning_Pipeline.ipynb`)

Auditor: A1. Scope: verify every transformation claim empirically against
`dataset/NMAT_CLEANED_DATA.csv`, `dataset/CEM_DATA.csv`, `dataset/UNIVS.csv`,
and the notebook's actual code (39 cells). All numbers below were produced by
independently re-running the pipeline's logic against the real source files
(not by trusting markdown cells or reading `NMAT_FINAL.csv` alone), and
cross-checked against the pipeline's own pre-generated `dataset/output/*.csv`
artifacts from the most recent real run (2026-07-31), which matched my
independent replication on every metric.

Source shapes confirmed: NMAT_CLEANED_DATA.csv = 178,927 × 29,
CEM_DATA.csv = 254,308 × 36, UNIVS.csv = 3,022 × 8.

---

## 1. Row conservation — SOUND

- NMAT: 178,927 rows, `NMA_AppNo_clean` has 178,926 unique values (**1 exact
  duplicate pair**, see §7 below).
- CEM: 254,308 rows, `STU_NO_clean` has 254,304 unique values (8 duplicate
  rows / 4 groups), deduplicated to 254,304 via a deterministic priority sort
  (`valid_priority` → `raw_component_count` → `calc_total_present` →
  `stored_total_present` → `NMAT_YEAR_num`, all descending) before the merge.
- **Merge 1** (Cell 15, `nmat_base.merge(verified_dim..., on="NMA_College",
  how="left")`): right side is explicitly `.drop_duplicates(subset=["NMA_College"])`
  first, so it is unique on the join key → no fan-out possible.
- **Merge 2** (Cell 16, `nmat_base.merge(cem_best, left_on="NMA_AppNo_clean",
  right_on="STU_NO_clean", how="left")`): `cem_best` is unique on
  `STU_NO_clean` by construction → no fan-out possible. The notebook itself
  asserts `len(nmat_master) == len(nmat_base)` immediately after — I verified
  this assertion actually passes.

Independent replication:
```
nmat_base rows: 178927
nmat_master rows after left merge: 178927
Row count preserved: PASS
```
No row filter (`.query`, boolean `df[mask]`, `dropna(subset=...)` on
row-bearing frames) exists anywhere against `nmat`/`cem`/`nmat_base`/
`nmat_master` in the notebook — I grepped every cell for filter patterns; the
only `dropna(subset=...)` calls operate on the UNIVS lookup table used to
build a matching dictionary, never on NMAT/CEM rows. **178,927 in, 178,927
out, verified structurally (no filter exists) and empirically (assert
passes, final CSV has 178,928 lines = 178,927 rows + header).**

**Verdict: SOUND.** No silent drops, no duplication, no many-to-many fan-out.

---

## 2. The CEM join — SOUND, 45-row gap confirmed genuine

Join key: `NMA_AppNo_clean` (NMAT, digits-only from `NMA_AppNo`) ↔
`STU_NO_clean` (CEM, digits-only from `STU_NO`). Both keys have zero nulls.
CEM side is unique after the priority dedup (254,304 rows for 254,304 keys).
NMAT side is used as the left/base table so its 1 internal duplicate key
does not cause CEM-side fan-out (see §7).

```
merge_cem indicator counts:
both          178882
left_only      45
right_only      0
```
`178,927 − 178,882 = 45` — **exactly matches** the claimed 45-row gap. I
confirmed the 45 unmatched rows are precisely the same 45 rows lacking a
CEM record (`no_cem & no_true == 45`, `no_cem & ~no_true == 0`).

I pulled all 45 unmatched application numbers and checked them against
CEM_DATA.csv directly — none of the 45 app numbers exist anywhere in CEM,
under any cleaning. They are concentrated in specific years: 2009 (18),
2012 (11), 2011 (9), 2013 (4), 2010 (3) — plausible late-registrant / CEM
data-entry gaps in the source system for those years, not an artifact of
key-cleaning or the join logic. **The 45-row gap is genuine, not a bug.**

---

## 3. Raw score recalculation identity — HOLDS PERFECTLY

`raw_cols = [STU_RS_CA01..CA08]` (Verbal, Inductive Reasoning, Quantitative,
Perceptual Acuity, Biology, Physics, Social Science, Chemistry — the correct
8 NMAT subtests, Part I = first 4 aptitude tests, Part II = last 4 subject
tests, matching standard NMAT structure).

```
Rows with all 8 components present: 254,308 (100% of CEM)
Rows where TotalRawScoreTRUE != sum(8 components): 0
Rows where PartIRawScoreTRUE + PartIIRawScoreTRUE != TotalRawScoreTRUE: 0
```
Identity holds on **every single row**, zero exceptions, out of 254,308.

**Verdict: SOUND.**

---

## 4. The stored-total mismatch claim — CONFIRMED, AND SOUNDER THAN THE PROJECT REALIZES

This is the most important question. Full results, computed from the raw
CEM file:

```
Full CEM file (254,308 rows):
  AllRawComponentsPresent: 254,308 (100%)
  StoredRawTotal present:   174,494
  Mismatch (Stored != Derived) among those: 107,422  →  61.56%
  107,422 / 254,308 (all CEM rows) = 42.24%   <-- matches CLAUDE.md's "42.2%" claim exactly

NMAT-aligned subset (after CEM dedup + left join onto the 178,927 NMAT rows):
  StoredRawTotal present: 99,316
  Mismatch: 56,065  →  56.45%   <-- matches the audit brief's cited figure EXACTLY
```
Both headline figures in project docs are reproducible from the raw data;
they are simply two different denominators (all of CEM vs. the
NMAT-matched subset) — not two independent, uncorroborated numbers.

**Is the stored total "wrong," or a different quantity?** I tested this
directly using two facts already present in the *raw, unmodified* CEM file
(not derived by the pipeline):

1. `STU_RSCORE_CALC` (CEM's own pre-existing "calculated total" column) —
   compared against this pipeline's `TotalRawScoreTRUE` (sum of the 8 raw
   components): **0 mismatches across all 254,308 rows.** CEM's own
   calculated-total field is byte-for-byte identical to the pipeline's
   recalculation, on every row.
2. `STU_RSCORE_VALID` (CEM's own pre-existing VALID/INVALID flag) —
   cross-tabulated against `StoredRawTotal == TotalRawScoreTRUE`:
   ```
   StoredVsDerivedMismatch    False    True
   STU_RSCORE_VALID
   INVALID                        0  107422
   VALID                      67072       0
   ```
   Exact, deterministic correspondence — VALID always means stored=derived,
   INVALID always means stored≠derived, with **zero exceptions**.

Distribution of `StoredRawTotal − TotalRawScoreTRUE` among the 107,422
mismatches (full CEM file): mean +0.37, median +1, IQR [−2, +3], min −22,
max +28. 28.5% of mismatches are off by exactly ±1; 88.6% are within ±5;
only 0.12% exceed ±20. These are small, arithmetic-scale discrepancies on
the same point scale as the raw score itself — **not** a different scale,
a subset of components, or a pre-adjustment value. The stored total is
genuinely, mathematically wrong in these rows, not "a different quantity."

**HIGH finding (documentation/characterization, not a numeric error):** The
project's framing ("we discovered 42.2%/56.45% of stored totals were
incorrect") implies this was found via independent recalculation. In fact
CEM's own source data already carries this exact information twice over —
via `STU_RSCORE_CALC` (identical to the recalculation) and
`STU_RSCORE_VALID` (a perfect binary predictor of the mismatch). The
pipeline's "recalculation" is not discovering anything CEM didn't already
know; it is reproducing a QA judgment CEM's system already made and
already exposed in two other columns. This *strengthens* confidence that
`TotalRawScoreTRUE`/the mismatch rate are correct (two independent
source-system fields corroborate it exactly), but the project's headline
claim of "identifying" a defect via recalculation is a mischaracterization
of what the recalculation actually adds — it adds a resummed, auditable,
independently-reproducible value, not a new discovery. This does not
invalidate the number; it changes its epistemic status from "novel finding"
to "confirmed reproduction of a pre-existing internal flag," which is
worth being explicit about since it is the project's marquee data-quality
claim.

**Verdict: The 42.2% / 56.45% figures are both real, both reproducible, and
both correctly characterized as "the stored total is wrong" (not a
different quantity) — but their novelty is overstated.**

---

## 5. Percentile bins — SOUND, with one silent-sentinel issue

```
Bin boundaries: [0,10,20,30,40,50,60,70,80,90,101), right=False, include_lowest=True
B1   0.0–9.0    (24,434 rows)
B2  10.0–19.0   (19,393)
B3  20.0–29.0   (17,443)
B4  30.0–39.0   (18,600)
B5  40.0–49.0   (15,857)
B6  50.0–59.0   (15,829)
B7  60.0–69.0   (15,282)
B8  70.0–79.0   (15,407)
B9  80.0–89.0   (15,500)
B10 90.0–99.0   (17,041)
No overlap detected between any consecutive bin's min/max.
```
B1 is the lowest decile, B10 the highest, intervals are left-closed and
non-overlapping — confirmed exactly as claimed.

**MEDIUM finding:** `NMS_PER_num` contains 1,275 true nulls **and 2,866
rows with the sentinel value `-1`** (min of the column is −1, which is
outside the valid 0–100 percentile range). Both groups fall through
`pd.cut` unassigned (4,141 total `NaN` bins = 1,275 + 2,866, confirmed by
direct count). The `-1` sentinel is silently indistinguishable from "no
bin assigned" downstream — nothing in the pipeline flags or documents that
~1.6% of rows carry this out-of-range sentinel rather than a true missing
value. Any downstream analysis treating `PercentileBin.isna()` as "missing
percentile" is implicitly conflating "no data" with "sentinel -1," which
may or may not be the intended semantics — undocumented either way.

---

## 6. University matching against UNIVS.csv — SOUND overall, one confirmed defect

The cascade (Cell 9) is genuinely 3 deterministic tiers + fuzzy, not 4
independent tiers as the project shorthand ("4-tier") suggests: (1) exact
match on `NMA_College_norm` against UNIVS' primary key, (2) exact match on
`COLLEGE_UNIV_norm` (secondary key), (3) fuzzy match (`rapidfuzz
token_sort_ratio`, min score 88, min gap 5 over the top-2 candidates) on
primary keys only, (4) unmatched → fallback to raw college string /
"Not Specified" / "Unknown". Non-matches are **not dropped** — they flow
through with `UNIVERSITY = raw NMA_College string`, `UNI_TYPE = "Not
Specified"`, `UNI_LOCATION = "Unknown"`.

Measured (matches the pipeline's own regenerated `dataset/output/*.csv`
exactly):
```
Distinct raw NMA_College strings: 3,251
verification_method counts (college×hint level, n=4,367 rows):
  UNIVS_EXACT_PRIMARY:    2,674
  UNIVS_EXACT_SECONDARY:     72
  UNIVS_FUZZY:               235
  NO_UNIVS_MATCH:          1,386

Distinct-college level (true unique colleges, n=3,251):
  At least one hint-variant VERIFIED: 1,953 (60.1%)
  All hint-variants UNMATCHED:        1,298 (39.9%)

Row level (178,927 NMAT rows, after fallback logic applied):
  VERIFIED: 177,120 (99.0%)
  UNMATCHED: 1,807 (1.0%)
```

**MEDIUM finding (mislabeling):** The notebook's own printed summary in
Cell 9 ("Total unique colleges: 4,367 ... Unmatched: 1,386 (31.7%)") labels
`len(verified_dim)` as "unique colleges." It is not — `college_dim` (Cell
7) is built by `drop_duplicates()` over **three** columns
(`NMA_College`, `NMA_College_norm`, `School Type_rec2_FINAL`), so the same
raw college string appears multiple times whenever it co-occurs with
different `School Type_rec2_FINAL` hint values in the source data (760 of
3,251 colleges do — e.g. "University of Santo Tomas" appears 4 times with
4 different hints). The true distinct-college unmatched rate is not 31.7%;
depending on how you count it, it's 39.9% (college-level, strict) or 1.0%
(row-level, what actually reaches the dataset). The printed "31.7%"
figure overstates the practical unmatched rate by roughly 30x relative to
what real examinee rows experience.

**HIGH finding (confirmed ambiguous mapping, method unsound):** The task
asked whether any raw string maps to two different `UNI_TYPE` values —
**yes, confirmed for 2 of 3,251 strings**: the placeholder values
`"Not Specified/Unlisted"` and `"Others (Please Specify)"`. Because UNIVS.csv
itself contains separate rows for these placeholders keyed by different
`School Type_rec2_FINAL` hints, Cell 9's per-row matching correctly produces
3 (resp. 2) different verified `UNI_TYPE` outcomes for these strings. But
Cell 15's merge back into `nmat_base` joins on `NMA_College` **alone** (not
including the hint) and uses `verified_dim[...].drop_duplicates(subset=["NMA_College"], keep="first")`
— silently discarding the very hint-based distinction Cell 9 computed, and
picking whichever row happens to sort first. Measured impact:
```
"Not Specified/Unlisted": 561 NMAT rows. Own School_Type hint distribution:
  Private: 233, Not Specified: 181, Public: 147
  -> ALL 561 rows get assigned UNI_TYPE="Public" (whatever sorted first)
  -> 414 rows (233+181) receive a UNI_TYPE that contradicts their own hint

"Others (Please Specify)": 25 NMAT rows. Own hint distribution:
  Not Specified: 23, Private: 2
  -> ALL 25 rows get UNI_TYPE="Not Specified"
  -> 2 rows receive a UNI_TYPE that contradicts their own hint
```
**Total: 416 rows (0.23% of 178,927) have a demonstrably wrong, silently
overwritten `UNI_TYPE`.** Scope is small — confined to the two generic
placeholder college strings, which are inherently low-information inputs —
but the defect is real, deterministic, and 100% reproducible, and it means
"no raw string maps to two different UNI_TYPE values" is technically false.
Any dashboard figure segmented by `UNI_TYPE` (e.g., Public vs Private
pass-rate comparisons) silently misclassifies these 416 students. Given the
tiny scope this does not move headline statistics, but the underlying
method — join-then-arbitrary-first-row-wins on a key that is known to be
ambiguous for some values — is unsound and could bite harder if UNIVS.csv
or the source hint column changes in the future.

`UNI_TYPE` value set confirmed clean otherwise: only 4 values in the final
178,927-row output (`Private`=137,476, `Public`=37,304, `Foreign`=2,315,
`Not Specified`=1,832 — sums to 178,927 exactly), matching
`canon_uni_type_final`'s valid set with no stray values.

---

## 7. PERSON_KEY — OUT OF SCOPE for Pipeline 1 (flagging for the record)

I grepped every cell of `1_Data_Cleaning_Pipeline.ipynb` for `PERSON_KEY`:
**it does not appear anywhere.** `PERSON_KEY` is constructed in
`2_PLE_Matching_Pipeline.ipynb` (found in 4 cells there), not Pipeline 1.
I cannot verify the "6,148 keys carry contradictory SEX" claim within this
audit's scope — that belongs to whoever audits Pipeline 2. Flagging this
explicitly so it isn't silently skipped: **item 7 of the audit brief is not
answerable from Pipeline 1's code or outputs.**

Related, in-scope observation: NMAT_CLEANED_DATA.csv has **1 exact
duplicate row-pair** on `NMA_AppNo_clean` (app no. 1073584, both rows
identical on `NMA_Name`="Ventanilla, Glen Tan", `Year`=2007, `NMA_College`
= "University Of The Philippines - Diliman"). This looks like a literal
duplicate data-entry in the source file rather than two different people
colliding on a key. Both rows flow through Pipeline 1 unchanged (no
dedup on NMAT's own key is ever applied — only CEM is deduped), so the
178,927-row output contains this person twice. **LOW/MEDIUM finding:**
negligible in scope (1 row of 178,927) but confirms Pipeline 1 performs no
NMAT-side deduplication at all; if this class of exact-duplicate exists in
the source with n>1 instances elsewhere, they'd propagate the same way and
inflate per-person counts by exactly 1 for each pair (does not affect
`IS_BEST_NMAT_RECORD` dedup logic which is a Pipeline-1/2/3 concern I did
not chase further, being out of Pipeline-1 scope).

---

## 8. Columns/rows dropped — NONE

I grepped every code cell in the notebook for row-filtering patterns
(`.query(`, boolean-mask indexing like `df[mask]`, `dropna(subset=...)`
against NMAT/CEM/merged frames). The only `dropna(subset=...)` calls are
against the UNIVS lookup dictionary used purely to build the matching
table — they never touch NMAT or CEM rows. No `nmat = nmat[...]` or similar
row-filter exists anywhere.

Column-wise: the final assembly (`nmat_final = nmat_master[priority_cols +
other_cols]`) explicitly does `other_cols = [c for c in nmat_master.columns
if c not in priority_cols]`, i.e. every column not in the curated priority
list is still appended at the end — nothing is dropped. Confirmed
empirically: `NMAT_FINAL.csv` has exactly 101 columns and 178,928 lines
(178,927 data rows + 1 header), matching `CLAUDE.md`'s documented "101
cols" and the row count exactly.

**Verdict: No rows dropped anywhere in Pipeline 1. No columns dropped.**
(Some columns are renamed at the very end via `rename_map`, e.g.
`STU_RS_CA01_num` → `Raw_Verbal` — renaming only, not dropping.)

---

## Summary of ranked findings

| Rank | Finding |
|---|---|
| HIGH | §4: The 42.2%/56.45% "stored total is wrong" claim is numerically correct and reproducible, but its framing as an independent discovery is a mischaracterization — CEM's own `STU_RSCORE_CALC` and `STU_RSCORE_VALID` columns already encode this exact fact with zero exceptions. Recommend documenting that the recalculation *confirms* an existing CEM QA flag rather than *discovers* a new defect. |
| HIGH | §6: Confirmed 416 rows (0.23%) get a demonstrably wrong `UNI_TYPE` because Cell 15's merge collapses per-row `School_Type` hint distinctions via an order-dependent `drop_duplicates(subset=["NMA_College"], keep="first")`, silently discarding logic Cell 9 correctly computed. Affects only the 2 generic placeholder college strings, but the method (arbitrary first-row-wins on a key known to be ambiguous) is unsound. |
| MEDIUM | §6: The notebook's own printed "Unmatched: 31.7%" mislabels a college×hint-pair count (4,367) as "unique colleges" (true count 3,251); real row-level unmatched rate is 1.0%, not 31.7% — the 31.7% figure, if ever surfaced in a report, would badly overstate the practical unmatched rate. |
| MEDIUM | §5: 2,866 rows (1.6%) carry a `-1` sentinel in `NMS_PER_num`, indistinguishable downstream from the 1,275 true nulls once binned — undocumented conflation of "no data" and "sentinel -1." |
| LOW/MEDIUM | §7: 1 exact-duplicate NMAT row (same appno/name/year/college) passes through unchanged — Pipeline 1 performs no NMAT-side deduplication. Negligible scope but confirms the mechanism exists. |
| — (scope note) | §7: `PERSON_KEY` is not built in Pipeline 1 at all (confirmed by full-notebook grep); the "6,148 contradictory-SEX keys" claim is unverifiable from this pipeline and must be checked against Pipeline 2. |

## Confirmed sound (stated plainly)

- Row conservation: 178,927 in, 178,927 out. No filter exists; the
  notebook's own `assert` passes; independently re-verified.
- Both merges are provably 1:1 on their right-hand join keys — no fan-out
  is possible, and none was observed.
- The CEM join key (`NMA_AppNo_clean`/`STU_NO_clean`) is correct, unique on
  the CEM side after dedup, and the 45-row unmatched gap is a genuine,
  traceable data gap (rows never existed in CEM_DATA.csv), not a bug.
- `TotalRawScoreTRUE` = sum of the correct 8 raw components, with
  `PartI+PartII=Total`, holding on **all 254,308 CEM rows with zero
  exceptions**. The 8 raw-score columns used are the correct subtests.
- The 56.45% (56,065/99,316) and 42.2% (107,422/254,308) mismatch figures
  are both exactly reproducible from the raw CEM file.
- Percentile bins B1–B10 are correctly bounded deciles, non-overlapping,
  left-closed, matching the claimed design exactly.
- `UNI_TYPE` in the final output takes only the 4 expected values, summing
  exactly to 178,927 rows.
- No columns or rows are silently dropped anywhere in the pipeline; 101
  output columns / 178,927 output rows confirmed exactly.

## Overall verdict

**Pipeline 1 is trustworthy on its core numeric deliverables.** Row
conservation, the CEM join, the raw-score recalculation identity, the
stored-total mismatch rate, and the percentile-bin construction all
independently reproduce exactly what the project claims, with real command
output as evidence (not restated markdown). The two HIGH findings are
real but narrow: one is a documentation/characterization issue (the
"discovery" framing of the stored-total mismatch oversells what the
recalculation adds, though the number itself is right), and the other is a
confirmed but small-scope (416 rows, 0.23%) `UNI_TYPE` corruption from an
order-dependent merge that should be fixed by deduplicating/joining on
`(NMA_College, School Type_rec2_FINAL)` instead of `NMA_College` alone.
Neither finding changes any headline statistic in the project's
deliverables. `PERSON_KEY` and its associated SEX-contradiction defect are
not in Pipeline 1's code at all and must be verified against Pipeline 2
separately.
