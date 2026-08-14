# G1 — Handoff & manuscript guides: what each document covers, what was verified, what was left out

Agent: G1. Scope: write `docs/HANDOFF_TESTING_GUIDE.md`,
`docs/MANUSCRIPT_GUIDE_MAIN_DASHBOARD.md`, `docs/MANUSCRIPT_GUIDE_CHED_DASHBOARD.md` only. No code
touched, no git commands run.

## What each document covers

**`HANDOFF_TESTING_GUIDE.md`** — environment setup (including a `duckdb`-missing-from-root-requirements
gap I found and confirmed live), launch commands for both dashboards + `data_aggregator` + `pytest`, a
per-tab checklist for all 42 main-dashboard tabs/subtabs and all 6 CHED tabs with literal on-screen
numbers under default filters, export instructions for both dashboards (CHED has a full self-check
export; main dashboard does not — documented as a known gap, not glossed over), the known-good
reference-output block, and a troubleshooting section.

**`MANUSCRIPT_GUIDE_MAIN_DASHBOARD.md`** — outline covering all 13 main-dashboard tabs, with a
per-pipeline data-quality section (§2) and a withdrawn-claims section (§5).

**`MANUSCRIPT_GUIDE_CHED_DASHBOARD.md`** — opens with the scope-ceiling statement (§0) as instructed,
per-pipeline data-quality narrative reframed for a policy reader (§1), a CMO-provision traceability
table mapped to the 6 tabs (§2), the supportable headline finding with its three-attack survival table
(§3), and the withdrawn-claims section (§4).

## How I worked

Read `RESUME.md`, `.claude/audit/_ORCHESTRATOR_FINDINGS.md` (O-1..O-24), `AUDIT_AND_REMEDIATION_PLAN.md`
in full, `.claude/audit/_EXPORT_FORMAT_CONTRACT.md`, `docs/CHED_CMO.md`. Dispatched two parallel
research subagents (foreground work, I did the writing/judgment myself) to do a literal, line-numbered
extraction of both dashboard.py files plus `ched_common.py` and `export_markdown.py` — necessary
because both files together are ~4,700 lines and the repo has moved substantially past what RESUME.md
describes (see below). I verified every headline number the subagents reported by running the code
myself (pandas queries against the live parquet, `pytest`, `AppTest` for both dashboards, and actually
regenerating the CHED export) rather than trusting either the subagent reports or the older plan
document at face value.

## The repo has moved past RESUME.md — verified, not assumed

RESUME.md (dated 2026-07-31) lists three items as "outstanding" that are, as of the current `HEAD`
(`edc31ab`, dated 2026-08-14), already done:

1. **The main dashboard's Sex-filter null bug is fixed.** `SEX_CLEAN` nulls are filled to
   `"(not specified)"` before the sidebar builds its options list (line 249), so they're a visible,
   default-included filter category, not silently dropped. I verified this by reading the code, not
   just trusting the subagent's report.
2. **CHED dashboard + `data_aggregator` migration to the 53-column schema is verified working**, not
   merely "wip" as `719e04b`'s message says. I ran `pytest tests/` (36 passed), `AppTest` on both
   dashboards (0 exceptions each; exact metric/dataframe/tab counts below), and
   `data_aggregator/run_all.py` (13 passed, 0 failed) myself on 2026-08-14, matching commit `edc31ab`'s
   own claimed verification numbers exactly. This is the "verify first" instruction in RESUME.md item
   1 — I did that verification independently rather than reproducing it from the commit message.
3. **Main dashboard Tab 13 ("CHED Compliance") has already been rebuilt.** The plan's C-4 fix
   ("remove or rebuild... remove per-HEI PLE benchmarking") is done — the tab now shows an applicant-pool
   cut-off-scenario table, foreign/Filipino composition, and the individual-level linkage gradient, with
   an explicit in-app note that a prior per-HEI-verdict version was removed "because the data cannot
   support them, not because they were miscalculated." I read this section directly (lines 2945–3148)
   rather than relying on the plan document's older description of Tab 13 as broken.

I did **not** find a `main_dashboard/export_markdown.py` or `main_common.py` anywhere in the repo
(confirmed via `find . -iname "*export_markdown*"` and `-iname "main_common*"`) — agent E1's task from
RESUME.md is still genuinely outstanding. I documented this honestly in the testing guide (§5) instead
of describing a CSV-download workflow as if it were the contract-compliant export the CHED dashboard
has.

## Numbers verified directly against `dataset/NMAT_Exodus.parquet` (2026-08-14)

All matched the RESUME.md / `_ORCHESTRATOR_FINDINGS.md` reference values exactly:

```
shape: 178,927 x 53
unique PERSON_KEY: 134,869
IS_BEST_OBSERVABLE_RECORD sum: 69,503
observable linkage rate: 45.44%
IS_PLE_PASSER sum: 49,086
ambiguous keys (PERSON_KEY_AMBIGUOUS, first per key): 6,148
PLE_YEAR_UNCERTAIN sum: 110
stored-total mismatch: 56,065 / 99,316 = 56.45%
linkage by bin: B1 11.6 B2 22.7 B3 29.3 B4 36.0 B5 45.6 B6 50.4 B7 53.6 B8 55.0 B9 61.6 B10 71.0
below-40 observable: n=25,596, passers=6,173, rate=24.1%; B1 passers=795
ambiguous rate among below-40 passers: 3.0% vs 3.5% cohort base rate
Filipino share of below-40 passers: 6,152 / 6,173
bin-step sizes: B1->B2 +11.1 ... B4->B5 +9.6 ... B9->B10 +9.4 (all as documented)
```

I also independently ran `AppTest` against both dashboards and captured every `st.metric()` label and
value under default filters — this is the source for every "numbers to read off screen" cell in the
testing-guide checklist, not a transcription from the subagent reports (I used the subagents for
structural/qualitative description — what appears, what chart type, what table — and my own tool calls
for every literal number cited).

## Discrepancies found, and which value I trusted

1. **Repeat-taker count: RESUME.md says 33,714; the live code says 33,713.** Commit `edc31ab`'s own
   message explains this precisely: both dashboards define a repeat taker as a `PERSON_KEY` with more
   than one distinct `APPNO_CLEAN` (application-based); one NMAT record is duplicated outright in the
   source data (VENTANILLA, GLEN TAN, application 1073584, 2007), which only inflates a row-count-based
   definition, not the application-based one both dashboards actually use. I verified 33,713 directly
   via `AppTest` on both dashboards and used it throughout, flagging the RESUME.md figure as superseded
   in the testing guide's opening reference block rather than silently picking one.

2. **`AUDIT_AND_REMEDIATION_PLAN.md` §7's "Public/Private median percentile 56/48" is stale.** That
   figure predates the RC-0/O-24 matcher fixes described in the same plan document (the fixes were
   applied *after* the plan was written, per RESUME.md's commit log). Live, I measured Public 57 /
   Private 49 on the current best-record population, confirmed independently three ways: (a) direct
   pandas groupby-median against the parquet, (b) `AppTest`'s live metric extraction from the CHED
   dashboard, and (c) a freshly regenerated `CHED_NMAT_Dashboard_Complete.md` export. All three agree
   at 57/49. I used 57/49 in both manuscript guides and noted in-guide that the plan's 56/48 predates
   the matcher correction — I did not silently overwrite it without saying so, per the task's
   instruction to flag disagreements rather than hide them.

3. **India's share of verified foreigners: the plan's "85.1%→81.5%" correction is also stale post-fix.**
   Live, best-record population: India is 79.3% (19,090 of 24,069). Verified via the same
   three-way check as above (pandas, `AppTest`, regenerated export). I used 79.3% in the CHED
   manuscript guide and explained in-guide *why* the correct-computation logic (full-denominator, never
   top-10-subtotal) matters, without asserting the specific percentage is fixed forever — it will move
   again if the underlying data changes, which is the point of instructing the reader to always use the
   full denominator rather than memorizing a number.

4. **"Verified foreigners" has two legitimate values depending on population — not a bug, but worth
   flagging so a future reader doesn't treat them as contradictory.** Row-level (all 178,927 sittings):
   32,501 (18.2%) — this is what Tab 5's narrative and Tab 6's overview cite. Person-level (best-record,
   134,869 people): 24,069 — this is what Tab 4's foreign-context table cites. Both are correct for
   their stated population; I used whichever the specific dashboard section actually displays, and
   said explicitly in the manuscript guides which denominator is in play each time, per the task's
   "state which population" discipline that also governs the linkage-rate framing.

## Things I judged unsupportable and therefore left out or explicitly warned against

- Did **not** repeat the withdrawn 21-point B4→B5 discontinuity or the regression-discontinuity
  recommendation anywhere except inside the explicitly-labeled "claims that were withdrawn" sections,
  as instructed.
- Did **not** describe `UNI_TYPE`/`UNDERGRAD_UNI_TYPE` as an institutional-performance metric anywhere;
  every mention in both manuscript guides is qualified as "applicant origin" or "undergraduate
  institution," with the UP Diliman proof repeated at the point of first use in each document (both
  guides needed to stand alone, so I did not assume a reader of one had read the other).
- Did **not** cite `forensic_audit/`'s "4 genuine mismatches" headline as a validation source anywhere
  — the testing guide explicitly warns against it (§7), per the plan's §9 finding that the number
  required an undocumented manual override not reproducible from the committed scripts.
- Did **not** invent a single-number "24.1%-equivalent" metric display for the CHED dashboard's Tab 3 —
  the dashboard shows the headline finding's components (bin-level linked/n) but not the below-40
  aggregate as one on-screen number. I said so explicitly in the CHED manuscript guide (§3, "Evidence")
  rather than implying it's a metric a reader can just screenshot; I gave the derivation instead
  (`sum(linked_n for B1..B4)` from Tab 3's own table).
- Left `RShiny_Dashboard/`, `reports/`, root `dashboard.py`/`dashboard.py.bak` out of both manuscript
  guides entirely — RESUME.md marks these as pending-deletion legacy artifacts awaiting the user's
  nod, not part of either dashboard's current story, and CLAUDE.md's dashboard-parity instructions
  referencing R Shiny are stale relative to that pending decision.

## Not verified (out of scope for this task, flagged for whoever picks it up next)

- I did not re-run `1_Data_Cleaning_Pipeline.ipynb` or `2_PLE_Matching_Pipeline.ipynb` end-to-end;
  the rapidfuzz-disclosure text and the disambiguator step-by-step description in both manuscript
  guides are sourced from reading the notebook cells directly (grep + targeted reads), not from
  executing them, since CLAUDE.md's "Modify Data Pipeline" instructions were not part of this task and
  a full pipeline re-run was not requested.
- I did not check the nested `.git` state of `streamlit_dashboard/CHED_relevant_dashboard/` (C-17 in
  the plan, "11+ commits behind parent") — out of scope for a documentation-only task and explicitly
  something only the orchestrator should touch per the standing rule "agents never run git."
