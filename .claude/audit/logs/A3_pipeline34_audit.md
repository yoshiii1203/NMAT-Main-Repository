# A3 — Pipelines 3 & 4 Audit

Scope: `3_NMAT_PLE_Analysis.ipynb`, `4_Citizenship_Integration.py`. All numbers below were
produced by running code (`.venv/Scripts/python.exe`) directly against the live repo files —
`dataset/NMAT_Ultima.parquet`, `dataset/NMAT_Exodus.parquet.bak`, `dataset/NMAT_Exodus.parquet`,
`dataset/REAL_FOREIGNERS.csv`, `dataset/analysis_output/*` — as they exist today
(post-remediation, per `RESUME.md`, closed 2026-08-14). Nothing was written to `dataset/`, no
notebook was executed, no file was modified except this log. No git commands were run.

A large prior audit (`.claude/audit/12_upstream_pipelines.md` §10, `.claude/audit/01_citizenship_pipeline.md`,
`.claude/audit/logs/P2_pipelines_4_5_tests.md`) already covered these two pipelines in depth,
**before** the current remediation closed. Where this audit reconfirms a prior finding, that is
stated explicitly with independently-run numbers, not a restatement. Where this audit found
something the prior work did not (notably: Pipeline 3's true output path, and that Pipeline 3
cannot execute against the current schema at all), that is flagged as new.

---

## Verdict up front

**Pipeline 3 is unambiguously stale, and — beyond staleness — is now structurally broken against
the current upstream schema; it cannot be re-run without code changes.** Nothing in the live
dashboards or `data_aggregator/` reads its output, so for those consumers staleness is
housekeeping only. But its stale, since-withdrawn output is still quoted as a live finding in
`reports/*.md`, which makes it a genuine correctness problem for those deliverable documents.

**Pipeline 4's citizenship layer is sound in mechanism** (precedence is correctly enforced, no
row/merge corruption, canonicalization has no material errors) **but the foreigner/Filipino split
rests on a large, quantified default: 81.83% of all rows (146,413 / 178,927) are labeled
"Filipino" purely by absence of foreign evidence, not by any positive Filipino confirmation.**
That default is empirically well-bounded (see F4-13 below) but is the load-bearing assumption of
every foreigner-vs-Filipino comparison in the project and should be stated as such wherever those
comparisons appear.

---

## Pipeline 3 findings

### P3-1 — CRITICAL (documentation error, corrects the task brief and prior docs): the real output directory is `dataset/analysis_output/`, not `data/`

`CLAUDE.md`, `README.md`, and the earlier `12_upstream_pipelines.md` audit (§10) all say Pipeline
3 writes to `data/` and that this directory "does not exist in this checkout." Read directly from
the notebook's own code (`3_NMAT_PLE_Analysis.ipynb`, config cell):

```python
ROOT   = next((p for p in ROOT_CANDIDATES if p.exists()), None)   # resolves to dataset/
OUTDIR = ROOT / "analysis_output"
```

`dataset/analysis_output/` exists, with **98 files** (CSVs, PNGs, 2 HTML Sankeys) — this is
Pipeline 3's real, and only, output surface. `data/` genuinely does not exist anywhere in the
project (confirmed via glob), but that was never where Pipeline 3 wrote; the prior audit's
grep for `data/` simply didn't find the actual path either, since it isn't named that in code.
This matters because it means Pipeline 3's output was findable and gradeable, and I did grade it
(P3-2 below) — the earlier "does not exist" conclusion undersold the staleness problem, it didn't
solve it.

### P3-2 — CRITICAL (confirmed, quantified): all 98 output files are stale by 2-3 months, computed under the pre-fix matcher

```
NMAT_Ultima.parquet   mtime 2026-07-31 16:19  (current, post-remediation, IS_PLE_PASSER=49,086)
dataset/analysis_output/*  (98 files)  mtime range 2026-05-05 15:59 -- 2026-05-26 13:41
Files in analysis_output/ older than NMAT_Ultima.parquet: 98 / 98 (100%)
```

Every single output file predates the corrected linkage by weeks to months. Concrete,
measured demonstration of impact — the decile→PLE-pass-rate table in the stale output
(`06F_ple_status_by_decile_observable_pct.csv`) vs. the same statistic computed fresh against the
live, corrected `NMAT_Exodus.parquet` (`IS_BEST_OBSERVABLE_RECORD` cohort, `PercentileBin`):

| Bin | Stale (`analysis_output`, pre-fix) | Live (`NMAT_Exodus.parquet`, corrected) |
|---|---:|---:|
| B4 (D4) | 25.66% | 35.996% |
| B5 (D5) | 46.30% | 45.624% |
| **B4→B5 step** | **+20.64 pp** | **+9.63 pp** |

The stale +20.6pp jump is *exactly* the "21-point B4→B5 discontinuity" that `RESUME.md` records
as explicitly **withdrawn** during remediation ("Corrected step is 9.6 points, in line with
B1→B2... It was mostly our own filter [artifact of the PERCENTILE_FLOOR=40 matcher bug]"). This
is not a hypothetical risk — it is the specific bug the remediation fixed, still sitting in
`dataset/analysis_output/` as if current.

### P3-3 — CRITICAL: the withdrawn finding is still asserted as fact in policy-facing report documents

`reports/01_Technical_Report.md:315-323`, `reports/02_Stakeholder_Report.md:105-113`,
`reports/03_Slide_Deck.md:208-209,481`, and `reports/04_Plain_Language_Results_Analysis.md:185`
all state the stale D4→D5 numbers (25.66% → 46.30%, +20.6pp) verbatim, and
`02_Stakeholder_Report.md:113` goes further, calling it *"the strongest empirical evidence in the
dataset that crossing the 40th NMAT percentile is the critical performance threshold for
board-passage probability."* That specific claim is the one `RESUME.md` says was withdrawn because
the underlying matcher had a hard `PERCENTILE_FLOOR=40` filter — i.e., the "evidence" was
partly manufactured by the exact bug being cited as a threshold-crossing effect. `reports/` is
marked "legacy" in the current remediation's outstanding-items list, but it is not deleted,
not labeled stale in-document, and nothing prevents a reader from citing it as current. This is
the one place in the whole repo where Pipeline 3's staleness is an active, deployed factual error
rather than housekeeping.

**Answers Q2 (does anything downstream consume `data/`/`analysis_output/`?):** grepped
`dashboard.py`, `streamlit_dashboard/*`, `RShiny_Dashboard/*`, `data_aggregator/*.py` for
`analysis_output` and `data/` — **zero hits**. Only docs (`CLAUDE.md`, `README.md`,
`docs/pipeline_architecture.md`) and `reports/*.md` reference the path. Verdict: for every
interactive consumer, stale output is pure housekeeping (they recompute directly from
`NMAT_Exodus.parquet`, confirmed by reading the relevant page/dashboard code). For `reports/*.md`,
it is a correctness problem (P3-3).

### P3-4 — HIGH: Pipeline 3 cannot be re-run against the current corrected schema — two hard `KeyError`s

Not just stale — orphaned. Two columns Pipeline 3's code reads unconditionally no longer exist in
the current `NMAT_Ultima.parquet`:

1. `IS_PLE_ANALYSIS_SAFE` — read at cell "ANALYSIS CELL 3" (`df_raw["HAS_CONFIRMED_PLE"] =
   (df_raw["IS_PLE_ANALYSIS_SAFE"] == True)...`) and cell 4 (`df_ple_safe =
   df_raw[df_raw["IS_PLE_ANALYSIS_SAFE"] == True]`). Confirmed absent from the live
   `NMAT_Ultima.parquet` (`'IS_PLE_ANALYSIS_SAFE' in df.columns` → `False`). It was the byte-for-byte
   duplicate of `IS_PLE_PASSER` that the prior audit (`12_upstream_pipelines.md` §2, F1 CRITICAL)
   flagged and remediation removed, replaced by the correctly-computed `IS_OBSERVABLE_COHORT` /
   `IS_BEST_OBSERVABLE_RECORD` — columns Pipeline 3 was never updated to use.
2. `PercentileDecile` (categorical D1-D10, used throughout: decile heatmaps, decile-by-year,
   PLE-by-decile, gap-by-decile, Dunn tests) — also confirmed absent from the current
   `NMAT_Ultima.parquet`; the current schema only carries `PercentileBin` (B1-B10). Confirmed:
   `'PercentileDecile' in df.columns` → `False`, `'PercentileBin' in df.columns` → `True`.

Re-running the notebook today would `KeyError` at the first of these (cell 3, line ~145) before a
single chart is produced. This is the definitive answer to "is Pipeline 3's output stale": yes,
and the notebook itself is no longer compatible with the pipeline chain that produced the data it
would need to refresh against.

### P3-5 — Statistical method review: mostly sound, one real cohort-mixing bug, no global multiple-comparison correction

Verified population/cohort choice for every test in the notebook by reading the code (not just
grepping for the test function names):

**Sound (independence + cohort correctly applied):**
- Kruskal-Wallis (Section 2, year-stability; Section 4A, UNI_TYPE; Section 4B, CourseGroup) and
  chi-square (Section 4D, UNI_TYPE×Decile; Section 4B, CourseGroup×Decile) all run on
  `df_best_trend` / `df_uni` — i.e. `IS_BEST_NMAT_RECORD==True` deduplicated, one row per person.
  No repeat-taker independence violation in any of these.
- Mann-Whitney (Section 6C, PLE status; Section 9C, linkage by uni type) both correctly use
  `df_best_observable` / `df_uni_observable` — best-record **and** `IS_BOARD_OBSERVABLE_COHORT`
  (`Year<=2014`, computed directly as `df_raw["Year"].le(2014)` at load time, independent of the
  broken `IS_PLE_ANALYSIS_SAFE` flag — so this specific restriction was correct even in the
  pre-remediation run that produced the stale files).
- Dunn post-hoc (Section 12, 3 families: UNI_TYPE, CourseGroup, Year) uses
  `sp.posthoc_dunn(..., p_adjust="bonferroni")` — multiple-comparison correction is applied
  correctly, within each family.

**HIGH — Section 11 (Gender) mixes an unrestricted cohort into a PLE-outcome comparison.**
`gender_valid = df_best_trend[...]` (best-record, but **Year 2006-2018, not Year<=2014**) is the
base for `gender_ple`'s `ple_passers`/`ple_pct` columns (cell 18). This blends 2015-2018
examinees — who mechanically cannot yet have a PLE match (the prior audit's F7 measured the
match rate mechanically falling from ~30% in 2016 to 0.08% in 2018, purely from the ≥5-year gap
requirement, not matching failure) — into a "Gender: PLE Pass Rate" table, understating both
sexes' rates and creating a spurious gender confound if the cohort's gender mix shifted across
years. This is inconsistent with the correct restriction applied two sections earlier (6C) and one
section later (9C, uni-type) in the *same notebook*. **This is confined to the dead notebook and
does not appear to have propagated to the live dashboard**: checked
`data_aggregator/page_10_year_gap_gender.py` (the live equivalent) directly — its PLE-status ×
gender table (line 288-293) correctly uses `bestobservable` (`IS_BEST_OBSERVABLE_RECORD`), so the
live, currently-shipped report does not repeat Pipeline 3's mistake.

**MEDIUM — no family-wise correction for two clusters of correlated same-hypothesis tests.**
Section 2 runs 5 uncorrected Kruskal-Wallis tests (Total/PartI/PartII/Percentile/GPS × Year) and
Section 6C runs 5 uncorrected Mann-Whitney tests (same 5 score variables × PLE status) — each
testing highly overlapping/derived variables (Part I + Part II = Total; Percentile is derived from
Total) without any Holm/Bonferroni adjustment across the family. Effect is muted by the high
intercorrelation between the 5 variables (they are not 5 independent hypotheses), but it is still
an uncorrected multiple-testing exposure that the notebook's own Dunn tests (Section 12) are
careful about and these two sections are not.

**LOW/sound-mechanism:** Section 6C's `r = 1 - 2*U/(n1*n2)` rank-biserial effect size is the
standard, correctly-implemented formula.

---

## Pipeline 4 findings

Pipeline 4's tier logic, canonicalization, and row-safety were already the subject of a thorough
prior audit (`.claude/audit/01_citizenship_pipeline.md`) whose 3 material findings (dead
`name_based_assessment` column, literal `"Foreign"` masquerading as a country, missing slim step)
were subsequently fixed during remediation. This audit independently re-verified all of that
against the **live, currently-shipped file** rather than trusting the prior log — every number
below was measured fresh.

### P4-1 — SOUND (verified): 3-tier precedence is correctly enforced, confirmed by code trace and live output

```python
df["CITIZENSHIP_FINAL"] = "Filipino"          # Tier 3 default, unprotected
df["FOREIGNER_STATUS"]  = "Filipino"
... tier1a_mask = RF_NATIONALITY notna & not-Filipino-variant       -> overwrite
... tier1b_mask = IN_REAL_FOREIGNERS & ~tier1a_mask                  -> overwrite
... tier2_mask  = ~tier1_mask & pseudo FOREIGN override              -> overwrite (guarded by ~tier1_mask)
```
No code path after Tier 2's assignment touches `CITIZENSHIP_FINAL`/`FOREIGNER_STATUS` again, and
Tier 2's mask explicitly excludes anything already claimed by Tier 1 — a later tier cannot
overwrite an earlier one, and Tier 3 is overwritten by design (it's the fallback). Confirmed live
on `dataset/NMAT_Exodus.parquet`:

```
FOREIGNER_STATUS:  Filipino 146,413 | Verified Foreigner 32,501 | Likely Foreigner 13   (sums to 178,927)
```
This exactly matches the prior audit's independently-replicated numbers, confirming the shipped
file matches the current script's logic (not a stale artifact from a different run).

### P4-2 — HIGH (quantified, answers Q6): 81.83% of the dataset is "Filipino" by default, not by evidence

```
Tier 3 default (FOREIGNER_STATUS == "Filipino"): 146,413 / 178,927 rows = 81.83%
```
There is no "is-Filipino" ground-truth file anywhere in the pipeline — Tier 3 fires whenever a
row is absent from both `REAL_FOREIGNERS.csv` and the pseudo-citizenship `FOREIGN`-override list.
**This is the load-bearing assumption underneath every foreigner-vs-Filipino comparison in the
project**, and it should be named as such (an absence-of-evidence default, not a positive
classification) wherever such a comparison is presented.

Bounding context (re-derived, not just cited): `REAL_FOREIGNERS.csv` cross-checked against
`NMAT_Ultima.parquet`'s own pre-existing raw `NAC_NATIONALITY` field shows only 4 of 32,505 rows
with a non-Filipino raw nationality are absent from `REAL_FOREIGNERS.csv` (the prior audit's F7,
independently plausible given `REAL_FOREIGNERS.csv`'s own internal completeness). So the risk is
empirically small *relative to the dataset's own self-reported nationality field* — but that field
is itself a self-reported value captured at NMAT registration, not cross-validated against any
immigration or passport record. "Verified Foreigner" should be read as "verified against the
registration record," not "verified against government citizenship status" — a nuance worth
stating in any dashboard caption that uses the word "verified."

### P4-3 — SOUND (re-verified independently): nationality canonicalization has no material merge errors; the "96 canonical values" documentation claim is still wrong

Ran `normalize_nationality()` (the actual pipeline function, not a re-implementation) against the
live `REAL_FOREIGNERS.csv`:

```
Raw unique NAC_NATIONALITY values (title-cased): 129   (matches "129" everywhere it's cited)
Canonical values after normalize_nationality(), excluding ambiguous->None: 89
Ambiguous (fall through to Tier 1b/"Foreign (unspecified)"): 156 rows
  Others 79, African 47, Not Stated 18, Arab 10, Not Specified 2
```
This exactly reproduces the prior audit's F5 finding (129 → 89, not the documented "~96") —
independently confirmed here, not merely restated. Manually inspected all 129→89 mappings
(demonym/spelling variants, e.g. `Indian→India`, `Sri Lankan→Sri Lanka`, `Camerdon→Cameroon`
[typo fix], `R.O.C.→Taiwan`, `Congo, Democratic Republic Of The→Democratic Republic of the Congo`)
and found **no incorrect merges** — no two genuinely distinct nationalities were collapsed into
one, and no nationality was split across two canonical values by a missed spelling variant.
One minor gap, immaterial in size: `"West Indies"` (1 record) is kept as its own literal
"nationality" even though it is a region, not a country — the same category of ambiguity as
`"Others"`/`"Arab"`/`"African"` (which are correctly mapped to `None`), but not caught by the map.
n=1, no effect on any headline number.

Documentation is still inconsistent and still wrong: `CLAUDE.md`/`docs/pipeline_architecture.md`
say "~96 canonical," `docs/data_dictionary.md` says "108 unique values" — neither matches the
measured 89 (excl. Filipino/unspecified) or 91 (`CITIZENSHIP_FINAL.nunique()` on the live file,
independently confirmed here). This is a pre-existing, already-logged LOW finding
(`10_docs_verification.md` F9, HIGH severity there for the doc-contradiction itself) that remains
unfixed as of this audit — flagged again since it's directly in this pipeline's scope.

### P4-4 — LOW: `FOREIGNER_STATUS` "Likely Foreigner" (13 records) — evidence, and inconsistent (but immaterial) downstream treatment

13 records get `FOREIGNER_STATUS = "Likely Foreigner"`: rows where the pseudo-citizenship file's
`override_applied == "FOREIGN"` fires and the row is *not* already covered by Tier-1 ground truth
(of 317 total `FOREIGN`-override rows, 304 are shadowed by Tier 1, leaving 13). That is the entire
evidentiary basis — a name-based inference signal, not independently verifiable further from this
repo.

Grepped every "foreigner count" call site across `dashboard.py`, `data_aggregator/`, and both
`streamlit_dashboard/*` folders. Most (`dashboard.py:1246,1532`; `data_aggregator/page_04_score_bins.py:249,519`;
`main_common.py:739,824`; `ched_common.py:506,519,634`) filter strictly on
`FOREIGNER_STATUS == "Verified Foreigner"`, excluding the 13 "Likely" rows. A few
(`dashboard.py:3046`; `data_aggregator/page_13_ched_compliance.py:210`; `main_common.py:1183`) use
`FOREIGNER_STATUS != "Filipino"`, which *includes* them. One place
(`ched_compute/04_institution_context.py:61-75`) reports both counts separately and transparently
(`verified_foreign`/`likely_foreign` as distinct fields). With n=13 against 178,927 rows the
numeric effect of this inconsistency is negligible (≤0.007 percentage points on any rate), but the
operational definition of "foreigner" is not uniform across the codebase, and no caption anywhere
tells the reader which definition a given number uses.

### P4-5 — SOUND (re-verified): row conservation holds at every stage, no merge fan-out

```
NMAT_Ultima.parquet            178,927 rows x 119 cols   (Pipeline 4's input)
NMAT_Exodus.parquet.bak        178,927 rows x 121 cols   (Pipeline 4's direct output)
NMAT_Exodus.parquet            178,927 rows x  53 cols   (after 5_Slim_Exodus.py)
```
178,927 in, 178,927 out at every stage — confirmed directly, not inferred. Both join keys are
one-to-one: `REAL_FOREIGNERS.csv` (32,501 rows) and `pseudo_citizenship_profiling_FINAL.csv` (871
rows) are each `drop_duplicates(subset=["APPNO_CLEAN"])`'d immediately before their left-merge, so
neither can fan out a row.

### P4-6 — INFO (confirmed fixed): the prior audit's 3 material findings are live-verified as resolved

Checked the live script and shipped file directly rather than trusting the remediation log:
`name_based_assessment` is absent from `dataset/NMAT_Exodus.parquet`'s columns (was dead weight,
now dropped); `CITIZENSHIP_FINAL` has zero rows equal to the bare literal `"Foreign"` (156 rows now
correctly read `"Foreign (unspecified)"`); `5_Slim_Exodus.py` exists and is the script that
produces the shipped 53-col file, and `4_Citizenship_Integration.py` now writes to
`NMAT_Exodus.parquet.bak` rather than overwriting the shipped file directly. All three previously
documented gaps are closed.

---

## Summary table

| ID | Severity | Pipeline | Title |
|---|---|---|---|
| P3-1 | CRITICAL (doc error) | 3 | Real output dir is `dataset/analysis_output/` (98 files), not `data/` — corrects CLAUDE.md/README/prior audit |
| P3-2 | CRITICAL | 3 | All 98 output files predate the matcher fix by 2-3 months; concretely reproduces the withdrawn 21pp B4→B5 discontinuity (measured: stale +20.64pp vs. live +9.63pp) |
| P3-3 | CRITICAL | 3 | The withdrawn discontinuity claim is still asserted as fact in 4 `reports/*.md` deliverable documents, one calling it "the strongest empirical evidence" for a 40th-percentile CMO threshold |
| P3-4 | HIGH | 3 | Notebook cannot re-run against the current schema — `IS_PLE_ANALYSIS_SAFE` and `PercentileDecile` no longer exist upstream; hard `KeyError` at load |
| P3-5a | HIGH | 3 | Section 11 (gender) mixes non-observable years (2015-2018) into a PLE pass-rate comparison; confirmed NOT propagated to the live `data_aggregator/page_10_year_gap_gender.py` |
| P3-5b | MEDIUM | 3 | No multiple-comparison correction across 2 clusters of 5 correlated same-hypothesis tests (Section 2 KW, Section 6C Mann-Whitney); Dunn tests correctly use Bonferroni |
| P4-2 | HIGH | 4 | 81.83% of rows (146,413) are "Filipino" by default/absence-of-evidence, not by positive confirmation — the load-bearing assumption of every foreigner comparison; empirically bounded but not eliminated |
| P4-3 | LOW (re-confirmed) | 4 | 129→89 canonicalization has no material merge errors; doc still wrongly claims "96" (pre-existing, unfixed) |
| P4-4 | LOW | 4 | "Likely Foreigner" (13 rows) treated inconsistently as foreign/not-foreign across call sites; immaterial in magnitude, undisclosed to readers |
| P3-sound | — | 3 | KW/chi-square tests correctly deduplicate to best-record; PLE-outcome tests (6C, 9C) correctly restrict to observable cohort; Dunn applies Bonferroni |
| P4-sound | — | 4 | Tier precedence correct and unbreakable by construction; row conservation exact; no merge fan-out; canonicalization has no wrong merges; 3 previously-logged bugs confirmed fixed |

---

## What is sound, stated plainly

- Pipeline 4's join/merge mechanics are safe: exact row conservation (178,927 at every stage,
  verified fresh), one-to-one keys on both external CSVs, no fan-out possible.
- Pipeline 4's tier hierarchy is implemented exactly as documented and cannot be silently violated
  by construction (Tier 2's mask hard-excludes anything Tier 1 already claimed).
- Pipeline 4's nationality canonicalization, inspected mapping-by-mapping, has no incorrect merges
  and no missed variant-splits worth flagging beyond one 1-record edge case.
- All three previously-identified Pipeline 4 bugs (dead column, "Foreign" literal, missing slim
  step) are confirmed fixed in the live code and shipped file.
- Most of Pipeline 3's statistical tests use the right population: best-record deduplication for
  independence, and observable-cohort restriction for PLE-outcome comparisons, correctly applied
  in the sections that matter most (6C, 9C). Dunn post-hoc tests correctly apply Bonferroni
  correction.
- The one cohort-mixing bug found in Pipeline 3 (Section 11, gender) is confirmed **not** to have
  propagated into the live, currently-shipped `data_aggregator` report — checked directly.
