# Audit 07 — Review of `forensic_audit/` (the "audit of the auditor")

**Scope:** `forensic_audit_v2.py` … `v6_dashboard_impact.py`, `forensic_audit_nmat_ple_matches.py`,
`audit_name_check.py`, `audit_name_check_deep.py`, `audit_per_bin_report.py`, `_check_missing.py`,
and their committed outputs (`forensic_audit_report.md`, `name_cross_check_evidence.md`,
`forensic_audit_summary.csv`, `forensic_audit_category_counts.csv`, `forensic_audit_exceptions.csv`,
`forensic_audit_low_score_details.csv`; `forensic_audit_classified.csv` sampled, not read whole).
Commits read: `08d196a`, `1d4eda2`, `ff45adf`, `dc46a04`.

---

## Verdict: **Trustworthy-with-caveats** for the core NMAT-score-gradient arithmetic; **NOT ESTABLISHED / effectively invalid as documented** for the name cross-check's headline "4 genuine mismatches" claim.

The population-selection and B4/B5 gradient math in `forensic_audit_v5_final.py` is internally
consistent, deterministic, and I reproduced it exactly. But the audit's second pillar — "names were
checked, only 4 are genuinely wrong" — does not survive a re-run: the script that the evidence
report cites as the reproduction path (`audit_name_check_deep.py`) actually flags **17** low-score
records and **77** overall as `genuine_mismatch`, not 4/6 respectively, when run today exactly as
committed. The gap is explained by an undocumented manual reclassification step and a name-parsing
heuristic that misfires on common Filipino compound surnames. Separately, the names themselves come
from an intermediate file that is **7 weeks older** than the analysed parquet and whose EXACT-match
population differs from the parquet's by ~17,000 rows — a provenance gap the audit never discloses
or reconciles.

The forensic audit also never touches the actual downstream consumer of its conclusions
(`dashboard.py` / the CHED complete-markdown). I traced the CHED brief's cut-off section and found
the exact "`IS_PLE_ANALYSIS_SAFE` is a duplicate of `IS_PLE_PASSER`" bug flagged in the shared
context is live in production output there — a table showing **100% NMAT→PLE linkage in every
single year 2006–2014** — a defect entirely outside forensic_audit/'s field of view. See Finding F4.

---

## B1–B4 orientation: **CONFIRMED — B1 is the LOWEST-scoring decile, B10 is the HIGHEST.**

Evidence, independent of the forensic-audit scripts' own labeling convention:

`1_Data_Cleaning_Pipeline.ipynb`, cell 29:
```python
nmat_base["PercentileBin"] = pd.cut(
    nmat_base["NMS_PER_num"],
    bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101],
    labels=["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"],
    right=False, include_lowest=True
)
```
`NMS_PER_num` is the examinee's NMAT percentile rank (higher = scored better than more peers), so
B1 = [0,10) is the bottom decile and B10 = [90,101) is the top decile. This is corroborated by
`streamlit_dashboard/CHED_relevant_dashboard/complete_markdown/CHED_NMAT_Dashboard_Complete.md:98-99`,
which defines "B4 (30-39) = CMO exception floor" and "B5 (40-49) = SUC standard floor" — i.e., the
policy cut-off debate is explicitly about the *low*-scoring bands. All six `forensic_audit_v*.py`
scripts' `band_label()` function (`pct<10 -> "B1"`, … `-> "B10"`) matches this convention exactly.
**No inversion bug exists.** This is a positive finding, not a defect — but it was worth nailing
down because getting it backwards would have inverted every conclusion downstream.

---

## Findings table

| ID | Severity | Status | Title | Location |
|---|---|---|---|---|
| F1 | **CRITICAL** | CONFIRMED | "4 genuine mismatches" is not reproducible by the cited script; fresh run finds 17 (low-score) / 77 (overall) | `forensic_audit/audit_name_check_deep.py`, `name_cross_check_evidence.md:129-196` |
| F2 | **CRITICAL** | CONFIRMED | Name source (`PLE_MATCH_MASTER.csv`) is a stale intermediate file (~7 weeks older than the analysed parquet); its EXACT-match population differs from the parquet's by ~17,000 rows, undisclosed | `dataset/output/PLE_MATCH_MASTER.csv`, `audit_name_check.py:11-19` |
| F3 | **HIGH** | CONFIRMED (code read, all 6 scripts) | No full 2×2 contingency table is ever computed (above/below cutoff × passed/failed/no-match); audit only examines the PLE-confirmed-passer subpopulation | all `forensic_audit_v*.py` |
| F4 | **CRITICAL** | CONFIRMED | Downstream CHED brief shows literally 100% NMAT→PLE linkage every year 2006-2014 — same `IS_PLE_ANALYSIS_SAFE`≡`IS_PLE_PASSER` bug from shared context, uncaught because forensic_audit/ never examines dashboard.py | `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py:140-141,191-196`; `complete_markdown/CHED_NMAT_Dashboard_Complete.md:247-259` |
| F5 | MEDIUM | CONFIRMED | 4 of 6 write-capable scripts hardcode output dir to repo root, not `forensic_audit/` — re-running per CLAUDE.md's documented command will NOT reproduce outputs to the committed location | `forensic_audit_nmat_ple_matches.py:663`, `forensic_audit_v2.py:365`, `forensic_audit_v3.py:322,347,352`, `forensic_audit_v5_final.py:491` |
| F6 | LOW | CONFIRMED | Headline "N=3,647" for below-B5 population is the *pre-dedup* count; the validity-breakdown table quoted under the same heading is computed on the *post-dedup* population (N=3,645); the 2-row gap is silently absorbed | `forensic_audit_report.md:42,85-86,243,266,277` vs `forensic_audit_v5_final.py:126 (best) vs :325 (best_deduped)` |
| F7 | MEDIUM | CONFIRMED | Population denominator ("confirmed PLE passer") is chosen as `IS_PLE_ANALYSIS_SAFE==True` (49,986 dataset-wide) without reconciling the two other plausible denominators from shared context (`PLE_YEAR_PASSED.notna()`=54,528, `PLE_MATCH_METHOD.notna()`=57,304); ~7,300-row gap unexplained | all `forensic_audit_v*.py`, e.g. `forensic_audit_v5_final.py:16-17` |
| F8 | LOW | CONFIRMED | `IS_PLE_ANALYSIS_SAFE` naming-vs-semantics confusion (docs say "observable cohort", empirically it's a duplicate of `IS_PLE_PASSER`) is not inherited harmfully by the audit itself (Year≤2014 is filtered separately), but is never disclosed to the reader, inviting misinterpretation | `forensic_audit_v5_final.py:16-17` |
| F9 | — (positive) | CONFIRMED | B4/B5 gradient math (1,312 / 4.5pp, unaffected by excluding 15 anomalies) is deterministic and reproduces exactly | `forensic_audit_v5_final.py` Sections 7,10 |

---

## Finding detail

### F1 — CRITICAL: name cross-check not reproducible as claimed

`name_cross_check_evidence.md:193-196` states:
> *"The 4 genuinely mismatched records can be verified by re-running: `python forensic_audit/audit_name_check_deep.py`"*

I ran that exact command (read-only, no writes — the script only prints) against the current,
byte-identical `NMAT_Exodus.parquet`:

```
Appno-based matches: 2,425
genuine_mismatch    77 (3.2%)
-- LOW-SCORE GENUINE MISMATCHES: 17 records --
```

The 4 records documented in the evidence report (AHUJA/Pydi, CASAO/Carlos, ROXAS/Royales,
LIAO/Lim) are a **subset** of these 17. The other 13 — e.g. `DE GUZMAN, JOSHUA` vs `Deguzman,
Joshua` (overlap 0.5), `DE LA CRUZ, JOMARIE` vs `Dela Cruz, Jomarie` (overlap 0.5), `LATORRE,
KRYSTLE` vs `La Torre, Krystle` (overlap 0.5), `DE LOS SANTOS, FRANCE` vs `Delos Santos, France`
(overlap 0.5) — are *also* auto-labeled `genuine_mismatch` by the script's own `parse_names()`
verdict logic, even though the evidence doc's own Section 3 lists these exact name pairs as
"Actually clean (same person, spacing/encoding variant)". Root cause: `parse_names()` splits the
PLE surname on comma and compares it token-for-token against NMAT surname tokens
(`audit_name_check_deep.py:39-46,59-88`); it has no logic to normalize "De Guzman" (two tokens)
against "Deguzman" (one token) — a systematic pattern for Filipino compound surnames. `is_married`
and `surname_swapped` checks require a full-string substring match, which a two-token surname can
never satisfy against a one-token surname.

**Consequence:** the "4" in the report was arrived at by a human manually re-reading and
overriding 13 of the script's 17 auto-flagged records — a step that exists nowhere in any committed
script, is not documented as a step, and is not reproducible by the exact command the evidence doc
tells the reader to run. The reader cannot verify "4" without redoing that undocumented manual
triage themselves.

### F2 — CRITICAL: name source is a stale, partially-reconciled intermediate file

`audit_name_check.py:11` and `audit_name_check_deep.py:11` both read
`dataset/output/PLE_MATCH_MASTER.csv`, not the analysed parquet (which, per shared context, has no
`PERSON_NAME` column at all — so a separate source is legitimate in principle). I verified this
file exists and traced its vintage and reconciliation:

```
PLE_MATCH_MASTER.csv  — Modify: 2026-06-10 14:55   (43,601 rows)
NMAT_Exodus.parquet   — Modify: 2026-07-28 01:42   (7 weeks later)

MATCH_METHOD counts, mm "accepted" (FINAL_MATCH status):
  EXACT                33,970   vs exodus PLE_MATCH_METHOD=='EXACT'   : 54,437  (Δ +20,467)
  MANUAL_APPNO_MATCH    2,330   vs exodus                              :  2,776  (Δ  +446)
  DETERMINISTIC_APPNO      95   vs exodus                              :     91  (Δ    -4, roughly consistent)
```

~62% of the exodus's EXACT-matched rows (33,970 / 54,437) exist in the file the audit used to
compute its "97.2% same-surname, 0.2% genuine mismatch" system-wide claims
(`name_cross_check_evidence.md` Section 1). The other ~20,467 EXACT-matched rows in the shipped
parquet were never touched by any name check in `forensic_audit/` — their provenance and name
quality is simply unknown to this audit. This is a real, disclosed-nowhere gap.

**Mitigating fact (also confirmed):** for the *specific* population the audit's headline numbers
are actually about — best-record, observable-cohort, below-B5, appno-based matches (430 rows) — I
verified 430/430 appnos are present and consistently joinable between `PLE_MATCH_MASTER.csv` and
the exodus. So the low-score deep-dive's target rows were not silently dropped or substituted; the
gap is specifically in the *system-wide* percentage claims (Section 1 of the evidence report),
which describe a partial, stale sample and should not be read as covering the full 57,304-row
PLE-matched population in the current parquet.

### F3 — HIGH: no 2×2 contingency table

Every `forensic_audit_v*.py` script (and `audit_per_bin_report.py`) begins its population from
`confirmed = obs[obs["IS_PLE_ANALYSIS_SAFE"] == True]` — i.e., it starts already restricted to
matched PLE passers. None of the six scripts ever compute the complement: examinees, by score band,
who did NOT get a confirmed PLE match (whether because they failed, never enrolled in med school,
or genuinely haven't taken the boards yet). Without that denominator, "X% of confirmed passers score
below B5" cannot be turned into any statement about whether the NMAT cut-off is predictive,
because there is no comparison to the below-cutoff group who *did not* pass. `dashboard.py`'s "Score
Bin | N (observable cohort) | Confirmed PLE Passers | Linkage Rate" table (see complete_markdown
lines 274-279) is the closest thing to this in the whole repo, and it lives in the dashboard, not in
`forensic_audit/`. This is a scope gap, not a math error, but it means the audit cannot itself
support (nor was ever asked to support) any causal or even correlational claim about cut-off
efficacy — which is exactly the kind of claim a cut-off policy brief is prone to over-read into it.

### F4 — CRITICAL (discovered while answering Q8, downstream): the shared-context bug is live in the CHED brief

Tracing "does the forensic audit's conclusion actually support the CHED brief's claims" led directly
into `dashboard.py`:

```
dashboard.py:140-141:  df_obs["HAS_CONFIRMED_PLE"] = (df_obs["IS_PLE_ANALYSIS_SAFE"] == True)
dashboard.py:191-196:  _df_clean_ple = df_obs[(df_obs["IS_PLE_ANALYSIS_SAFE"] == True) & ...]
```

And the resulting table in the shipped brief:

```
complete_markdown/CHED_NMAT_Dashboard_Complete.md:247-259
| Year | Total B5+ observable | Confirmed PLE passers | No confirmed PLE match | Linkage rate (%) |
| 2006 | 1,435 | 1,435 | 0 | 100 |
| 2007 | 1,352 | 1,352 | 0 | 100 |
...(every year 2006-2014 shows exactly 100%)...
```

This is the shared context's CONFIRMED CRITICAL BUG #1 (`IS_PLE_ANALYSIS_SAFE` is a perfect
duplicate of `IS_PLE_PASSER`, so any denominator filtered on it yields 100% by construction)
appearing directly in stakeholder-facing output. Tellingly, a *different* table two sections later
in the same document (`complete_markdown:274-279`, "PLE Linkage by Score Bin", B1: 505/6,104 = 8.3%)
computes linkage correctly — proving the underlying data supports a correct calculation, and that
this specific by-year table is a distinct, avoidable defect. Because `forensic_audit/` never opens
`dashboard.py`, it never had a chance to catch this — the "forensic audit" and "the thing that
actually needed auditing" turned out to be adjacent, not the same.

### F5 — MEDIUM: reproducibility path bug

```
forensic_audit_v5_final.py:491:  outdir = r"D:\...\NMAT_Analysis"          # repo ROOT, not forensic_audit/
forensic_audit_v3.py:322,347,352: hardcoded to repo ROOT
forensic_audit_v2.py:365:         out_dir = r"D:\...\NMAT_Analysis"        # repo ROOT
forensic_audit_nmat_ple_matches.py:663: output_path = r"D:\...\NMAT_Analysis\forensic_audit_exceptions.csv"
```

I copied `forensic_audit_v5_final.py` into the scratchpad, redirected only the output path, and
reran it twice (fully deterministic — two fresh runs are byte-identical). Its `forensic_audit_
summary.csv` and `forensic_audit_category_counts.csv` output matched the committed copies in
`forensic_audit/` **exactly**, confirming the underlying classification logic (Section 5-11) is
solid and reproducible. But if any script is re-run as literally documented in CLAUDE.md
(`cd forensic_audit && python forensic_audit_v5_final.py`), the CSVs land in the repo root, not
`forensic_audit/` — diverging from where the currently-committed outputs live. The likely
explanation is the committed files were generated once and manually moved into `forensic_audit/`
afterward; this is not itself evidence of tampering, but it does mean the documented reproduction
path is broken today.

### F6 — LOW: N=3,647 vs N=3,645 conflation

`forensic_audit_v5_final.py` computes "below-B5" from two different populations depending on
section: Section 4 uses `best` (pre-dedup, 29,273 rows total → 3,647 below B5); Sections 5-11 use
`best_deduped` (post-dedup, 29,258 rows total → 3,645 below B5, confirmed by rerun). The report's
headline sentence ("The 3,647 confirmed PLE passers below B5 are valid observations") and its
Section-8 table heading ("N=3,647") both cite the pre-dedup figure, while the validity-breakdown
rows immediately below sum to the post-dedup figure (3,622 + 23 = 3,645). A reader checking the
math finds a silent 2-row (0.05%) gap. Immaterial in size, but indicative of the same lack of
internal cross-checking that produced F1 and F6.

### F7 / F8 — population-denominator choices

All six scripts agree with each other on population definition (`Year<=2014` then
`IS_PLE_ANALYSIS_SAFE==True`), so there is no *inter-version* contradiction — a genuine point in
the audit's favor (see "Version sprawl" below). But the choice of `IS_PLE_ANALYSIS_SAFE` (49,986
dataset-wide via its `IS_PLE_PASSER` duplicate) over `PLE_MATCH_METHOD.notna()` (57,304) or
`PLE_YEAR_PASSED.notna()` (54,528) as "confirmed passer" is never justified or even mentioned as a
choice, and the ~7,300-row gap to the largest of the three candidate counts is never explained.
Because `Year<=2014` is filtered as its own, separate line before this flag is applied, the audit
does **not** inherit the "observable cohort" mislabeling harm from shared-context Bug #1 in a way
that corrupts its own numbers — but a reader relying on CLAUDE.md's documented meaning of the
column would misunderstand what filter is actually being applied.

---

## Version sprawl — do v2 through v6 agree?

Yes, on population definition and core logic. I grepped all six for their `DATA_PATH`, `obs =`,
and `confirmed =` lines: every version independently defines `obs = df[df["Year"] <= 2014]` and
`confirmed = obs[obs["IS_PLE_ANALYSIS_SAFE"] == True]` identically. `v5_final.py` is the most
complete (11 sections vs. v2/v3's ~9, v4's narrower "deep dive" focus, v6's single-purpose dashboard-
impact check), and its Section 7 "Before vs After Exclusion" table is the one reproduced in
`forensic_audit_report.md`. **`v5_final.py` is the authoritative version** — it is the one named in
the report's own header ("Script: forensic_audit_v5_final.py") and its numbers are what the
committed CSVs and markdown reflect (confirmed via rerun, F5/F9). v2-v4 and v6 read as scratch/
iteration artifacts kept for audit trail rather than independent analyses that disagree with v5 —
no contradiction found between versions on any metric they share.

---

## What a defensible version of this audit would look like

1. **Fix the reproduction path first.** Change every `outdir`/`out_dir`/`output_path` in the four
   offending scripts (F5) to a path relative to the script's own location
   (`os.path.dirname(__file__)`), so `cd forensic_audit && python forensic_audit_v5_final.py`
   reproduces into `forensic_audit/` as CLAUDE.md documents.

2. **Regenerate `PLE_MATCH_MASTER.csv` from the current pipeline run**, or explicitly re-derive the
   name-check source from whatever process actually produced the final `PLE_MATCH_METHOD` column in
   `NMAT_Exodus.parquet` (57,304 rows), so the name-check's denominator matches the analysed
   parquet 1:1, not a 63%-overlapping ~7-week-old snapshot. Document the generation date and git/
   pipeline-run provenance of any auxiliary file used for cross-checking, next to the claim it
   supports.

3. **Fix the surname-matching heuristic** in `parse_names()` before trusting its `verdict` column at
   all: normalize compound Filipino surnames (strip internal whitespace before comparing surname
   tokens: "De Guzman" → "DEGUZMAN") so spacing variants aren't auto-flagged as `genuine_mismatch`.
   Then report the **raw script output** as the headline number — 17 low-score / 77 overall, or
   whatever the corrected heuristic yields — with the resolution work (which really are
   spacing/married-name/genuine) shown as a visible, scripted step, not an undocumented manual pass.
   If manual adjudication is unavoidable (it likely is, for ~20 ambiguous cases), commit the
   adjudicated table itself (record ID → human verdict → rationale) so "4" is checkable without
   re-doing the judgment call.

4. **Compute and publish the full 2×2 contingency table**, at minimum at the B4/B5-cutoff level:

   |               | PLE Passed (confirmed) | PLE Not Confirmed / Unknown |
   |---------------|------------------------:|-----------------------------:|
   | Score < cutoff | a | b |
   | Score ≥ cutoff | c | d |

   using the full observable-cohort best-record population (not just the passer subset) as the base
   for rows b and d. Without this table, statements like "X below-cutoff examinees passed the boards"
   cannot be weighed against "how many below-cutoff examinees are there in total" or "how many
   above-cutoff examinees also failed/never matched" — both needed before drawing any cut-off-policy
   conclusion. State explicitly that this is an observational linkage (selection bias: only
   examinees who both enrolled in med school and sat the PLE are observable at all) and that no
   causal claim about the cutoff's validity follows from it.

5. **Reconcile the three "PLE matched" denominators** from shared context
   (`IS_PLE_PASSER`=49,986, `PLE_YEAR_PASSED.notna()`=54,528, `PLE_MATCH_METHOD.notna()`=57,304)
   explicitly in the report's methodology section: state which one is used, why, and account for the
   ~7,300-row gap to the largest candidate before calling any subset "confirmed."

6. **Cross-check the audit against the actual dashboard code**, not a paraphrase of it in a comment
   (`forensic_audit_v6_dashboard_impact.py:9-12` describes the dashboard's filter in a comment
   rather than importing/testing against `dashboard.py` directly) — and extend that check to the
   by-year linkage-rate table, which is exactly where F4's 100%-every-year defect lives and which
   none of the six scripts currently look at.

7. **Reconcile the pre-/post-dedup population sizes** (F6) — pick one number, use it in every table
   and every sentence in the same report, and state the 15-row dedup adjustment once, up front,
   rather than letting two different N's coexist under one heading.
