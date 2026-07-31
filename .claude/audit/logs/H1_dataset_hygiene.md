# H1 — Dataset Artifact Hygiene

Agent: H1. Scope: `dataset/` inventory, classification, manifest, dry-run cleanup script.
**Inventory-only wave** — nothing in the pipeline chain was touched or deleted. The only deletion
executed was checking for `__pycache__`/`.ipynb_checkpoints`/`*.tmp` under `dataset/`, which found
none (nothing to clean).

Commands run with `./.venv/Scripts/python.exe` where applicable (the cleanup script's dry-run, verified
below). File sizes/mtimes obtained via `ls -la` / `du -sb` in a bash shell against the real filesystem.

## Full inventory table

### Root (`dataset/*`)

| File | Size | mtime | Produces | Consumers | Class |
|---|---|---|---|---|---|
| CEM_DATA.csv | 88,885,855 | Apr 19 | (raw) | P1 | LIVE INPUT |
| DsPy_verified.csv | 1,433,533 | Jun 10 | (raw) | P1 | LIVE INPUT |
| NMAT_CLEANED_DATA.csv | 44,636,474 | Apr 19 | (raw) | P1 | LIVE INPUT |
| NMAT_Exodus.csv | 224,417,649 | Jul 27 | P4 | none (grep-confirmed) | REGENERATED, 0 readers — future DEAD ARTEFACT |
| NMAT_Exodus.parquet | 11,007,467 | Jul 28 | P4 | both dashboards, data_aggregator, ched_compute, forensic_audit | LIVE INPUT (the deliverable) |
| NMAT_Exodus.parquet.bak | 29,277,141 | Jul 27 | unknown/manual | none (grep-confirmed; docs only) | STALE, gated on 5_Slim_Exodus.py |
| NMAT_FINAL.csv | 194,014,616 | Jun 10 | P1 | P2 (`NMAT_FINAL_PATH`) | LIVE INPUT |
| NMAT_Ultima.csv | 220,746,605 | Jun 10 | P2 | none (grep-confirmed) | LIVE INPUT (protected this wave) / future STALE DUPLICATE |
| NMAT_Ultima.parquet | 29,210,044 | Jun 10 | P2 | P4, both dashboards' fallback paths, R Shiny | LIVE INPUT |
| PLE_DATA.csv | 1,573,674 | Apr 19 | (raw) | P2 | LIVE INPUT |
| PLE_UNMATCHED.csv | 233,051 | May 5 | (raw) | P2 | LIVE INPUT |
| pseudo_citizenship_profiling_FINAL.csv | 158,899 | Jun 1 | (raw) | P4 | LIVE INPUT |
| REAL_FOREIGNERS.csv | 7,727,577 | Jun 2 | (raw) | P4 | LIVE INPUT |
| UNIVS.csv | 524,957 | May 31 | (raw, curated) | P1 | LIVE INPUT |
| UNIVS_ARCHIVED.csv | 497,387 | Apr 19 | unknown | **none anywhere** (0 grep hits, including docs) | **DEAD ARTEFACT** |
| fix_univs.py | 27,823 | (script) | — | none calls it | DEAD ARTEFACT, low confidence (see below) |

### `dataset/output/` (27 files, 74.2 MB total)

| File | Size | Read by | Class |
|---|---|---|---|
| PLE_MATCH_MASTER.csv | 8,869,921 | forensic_audit/_check_missing.py, audit_name_check.py, audit_name_check_deep.py, audit_per_bin_report.py | LIVE INPUT (to forensic_audit) |
| PLE_STILL_UNMATCHED.csv (no `_v2`) | 1,099,772 | P2 (read back in as its own input, per orchestrator's explicit protected list) | LIVE INPUT |
| NMAT_FINAL.parquet | 19,964,691 | none (grep-confirmed) | REGENERATED, 0 readers — future STALE DUPLICATE (CSV twin at dataset root is what P2 reads) |
| PLE_STILL_UNMATCHED_v2.csv | 1,143,424 | none downstream | REGENERATED, audit-trail-only |
| PLE_AMBIGUOUS_REVIEW.csv | 170,977 | none downstream | REGENERATED, audit-trail-only |
| PLE_PASSERS_IN_NMAT.csv | 45,780,381 | none downstream | REGENERATED, audit-trail-only |
| NMAT_Ultima_profile.csv | 8,997 | none downstream | REGENERATED, audit-trail-only |
| 00_source_counts.csv ... 14_qa_final_value_source_summary.csv (19 files) | small, <350KB each except 2 PNGs | none downstream | REGENERATED, audit-trail-only (documented QA outputs of P1, not accidental clutter) |

Full per-file byte listing captured via `ls -la dataset/output`, reproduced in the manifest §2.

### `dataset/analysis_output/` (98 files, 23.7 MB total)

Grep for `analysis_output` across the whole repo returns matches **only** in:
`docs/pipeline_architecture.md`, `docs/data_dictionary.md`, `reports/01_Technical_Report.md`,
`reports/03_Slide_Deck.md`. Zero matches in `dashboard.py`, `streamlit_dashboard/*/dashboard.py`,
`data_aggregator/*.py`, `ched_compute/*.py`, `forensic_audit/*.py`. All 98 files are P3 outputs.

**Verdict: orphaned from live code, not orphaned from documentation.** `reports/03_Slide_Deck.md` cites
individual files by name as figure sources (e.g. the three Sankey `.html` exports), so deleting this
folder would break a document another agent may still consider a live deliverable.
`AUDIT_AND_REMEDIATION_PLAN.md` §11 separately recommends retiring `reports/` itself as stale — if that
happens, `analysis_output/`'s last tether goes with it. That call belongs to whoever owns `reports/`,
not this wave. **Not recommended for deletion by H1; flagged for the orchestrator.**

## Specific determinations (as requested)

1. **`NMAT_Exodus.csv` (224 MB) — does any code read it?** No. Grep for `NMAT_Exodus\.csv` across the
   whole repo returns exactly 4 hits: the write statement in `4_Citizenship_Integration.py:29,532-534`
   (docstring literally says "for manual inspection"), a path-constant definition in
   `data_aggregator/config.py:10` that is **never referenced again in that file** (verified by grepping
   `EXODUS_CSV` — only the definition line matches; `data_aggregator` actually loads `EXODUS_PARQUET`),
   and one doc-table row. **Confirmed 224 MB dead mirror.** Not deleted this wave because P4 is one of
   the pipelines currently being rerun and will rewrite this file regardless of whether it's deleted now.

2. **`NMAT_Exodus.parquet.bak` (29 MB) — superseded by `5_Slim_Exodus.py`?** Not yet — that script does
   not exist in the repo (`ctx_search` for `5_Slim_Exodus` returns 0 file-hits, only 2 mentions inside
   `AUDIT_AND_REMEDIATION_PLAN.md` describing it as planned work, Track A4). I read the live
   `4_Citizenship_Integration.py` in full: it writes `EXODUS_PARQUET` directly with the already-slimmed
   columns (confirmed by the drop-columns block at line 537-542, which references
   `IS_OBSERVABLE_COHORT`/`PERSON_KEY_AMBIGUOUS` — i.e. another remediation agent has already started
   editing this exact file concurrently with this audit, consistent with the stated concurrent-rerun
   constraint). There is no `.bak`-writing step anywhere in the current pipeline. The `.bak` is an
   orphaned manual snapshot with zero code readers (grep-confirmed) but is presently the **only**
   full-118-column backup that exists. Recommend leaving it alone until Track A4 lands and is verified.

3. **`NMAT_FINAL.csv` / `NMAT_Ultima.csv` — CSV twins dead, or parquets insufficient?** The direction
   flips between the two pairs — this is the one place I'd flag a naive "always prefer parquet" cleanup
   rule as wrong:
   - `NMAT_FINAL.csv` (root) is what P2 actually opens (`NMAT_FINAL_PATH = ROOT / "NMAT_FINAL.csv"`,
     confirmed in `2_PLE_Matching_Pipeline.ipynb` cell text). Its parquet twin,
     `dataset/output/NMAT_FINAL.parquet`, has zero readers.
   - `NMAT_Ultima.csv` (root) has zero readers anywhere (grep-confirmed: only the P2 write statement and
     doc prose match). Every consumer — P4, `dashboard.py`, the CHED dashboard, R Shiny's `app.R` and
     both `.Rmd` files — opens `NMAT_Ultima.parquet` exclusively.
   So: keep `NMAT_FINAL.csv` + `NMAT_FINAL.parquet` is the redundant one; keep `NMAT_Ultima.parquet` +
   `NMAT_Ultima.csv` is the redundant one.

4. **`UNIVS_ARCHIVED.csv` — superseded by `UNIVS.csv`?** No evidence it was ever a version of
   `UNIVS.csv` at all. Grep for `UNIVS_ARCHIVED` across the entire repo (code + all docs + all `.md`)
   returns **zero matches**. Not read by P1 (which opens `UNIVS.csv`), not mentioned in
   `docs/pipeline_architecture.md`'s otherwise-thorough file inventory, not mentioned in `CLAUDE.md`.
   Confirmed dead, not merely superseded — nothing in the repo's history visible from static analysis
   explains its presence. **Safe to delete now**, and the only item this wave that is.

5. **`dataset/output/` — which entries still referenced?** Only `PLE_MATCH_MASTER.csv` (by
   `forensic_audit/*.py`, 4 files) and `PLE_STILL_UNMATCHED.csv` — the round-1 file without the `_v2`
   suffix, which P2 reads back in as one of its own inputs (this is on the orchestrator's explicit
   protected list already, correctly). Everything else in `dataset/output/` is write-once P1/P2
   audit-trail output with no downstream code reader, but it is *documented* audit trail
   (`docs/pipeline_architecture.md` lists all of it explicitly by design), not accidental clutter — not
   recommended for deletion.

## Reasoning for DEAD/STALE calls, condensed

- **UNIVS_ARCHIVED.csv → DEAD ARTEFACT.** Evidence: 0 references in `ctx_search` across the whole repo
  (code, notebooks, every `.md`). Not part of any of the 5 pipelines' input or output lists as verified
  by reading `1_Data_Cleaning_Pipeline.ipynb`'s actual `UNIVS.csv`-reading cell. Confidence: high.

- **fix_univs.py → DEAD ARTEFACT, low confidence, deliberately excluded from the delete list.**
  Evidence: 0 references anywhere (`ctx_search 'fix_univs'` → 0 matches); it reads `UNIVS.csv` and
  writes `UNIVS_VERIFIED.csv`, and `UNIVS_VERIFIED.csv` does not exist anywhere in the current
  `dataset/` listing — meaning either it was never actually executed, or it was run once by hand and its
  output was later renamed/merged into `UNIVS.csv` outside of any tracked automation. I cannot
  distinguish "genuinely dead" from "a documented one-off correction tool the maintainer keeps around
  for the next time UNIVS.csv needs a manual pass" from static analysis alone — it's a *script*, not a
  data mirror, so the cost of being wrong (losing a hand-written correction ruleset with ~150 named
  university overrides) is higher than for a stale CSV. **Flagging for orchestrator confirmation rather
  than guessing**, per the instruction to be honest about uncertainty. Not included in
  `_cleanup_stale.py`'s target list.

- **NMAT_Exodus.csv, dataset/output/NMAT_FINAL.parquet → confirmed 0 readers, held back only by the
  concurrent-rerun constraint.** Both are in `_cleanup_stale.py`'s `TIER_FUTURE` list (requires
  `--include-future`, still dry-run by default) so the orchestrator can flip them once P1/P4's rerun is
  confirmed done.

- **NMAT_Exodus.parquet.bak → held back on a different basis: no current generator exists.** Not added
  to `TIER_FUTURE` at all — it needs `5_Slim_Exodus.py` to exist and be verified before it's even a
  future-tier candidate, since deleting the only full-column backup with no reproduction path would be
  a real loss, not tidying.

## What I did NOT do (uncertainty flagged, not guessed past)

- Did not determine `UNIVS_ARCHIVED.csv`'s or `fix_univs.py`'s actual git history/authorship — static
  grep across the working tree only, per the "never run git" constraint for this wave.
- Did not verify whether the live Streamlit Cloud deployment (flagged elsewhere in
  `AUDIT_AND_REMEDIATION_PLAN.md` §12 as possibly serving stale code from a nested repo) loads any of
  these files from a different relative path than the ones grepped here. Scope was the parent repo only,
  per instruction not to touch `streamlit_dashboard/*/.git`.
- Did not delete `reports/` or make any determination about it beyond noting it's `analysis_output/`'s
  last live tether — out of scope for a dataset-artifact-hygiene wave.

## Verification of the cleanup script (dry-run only, nothing executed with `--execute`)

```
$ ./.venv/Scripts/python.exe dataset/_cleanup_stale.py
WOULD DELETE: dataset\UNIVS_ARCHIVED.csv (485.7KB)
Would reclaim: 485.7KB (497,387 bytes)
Dry run only. Re-run with --execute to actually delete.

$ ./.venv/Scripts/python.exe dataset/_cleanup_stale.py --include-future
WOULD DELETE: dataset\UNIVS_ARCHIVED.csv (485.7KB)
WOULD DELETE: dataset\NMAT_Exodus.csv (214.0MB)
WOULD DELETE: dataset\output\NMAT_FINAL.parquet (19.0MB)
Would reclaim: 233.5MB (244,879,727 bytes)
Dry run only. Re-run with --execute to actually delete.
```

Neither invocation used `--execute`. No files were deleted by this agent this wave.

## Bytes reclaimable summary

| Tier | Bytes | MB | When |
|---|---|---|---|
| Safe now | 497,387 | 0.5 | Immediately (orchestrator's call whether to run `--execute` this wave or hold for the coordinated deletion wave) |
| Future (rerun-gated) | 244,382,340 | 233.0 | After confirming P1/P4 rerun complete |
| Future (bak, gated on 5_Slim_Exodus.py) | 29,277,141 | 27.9 | After Track A4 lands |
| Future (Ultima.csv, explicitly protected this wave) | 220,746,605 | 210.5 | Orchestrator's call, once P2 rerun confirmed complete |
| **Total potential** | **494,903,473** | **~472 MB** | — |

`dataset/` is currently ~957 MB total; the fully-cleared state above would bring it to ~462 MB, roughly
half.

## Deliverables produced

- `dataset/DATASET_MANIFEST.md` — permanent classified map of the folder
- `dataset/_cleanup_stale.py` — dry-run-default deletion script, hardcoded refuse-list, `--execute` and
  `--include-future` flags, verified via dry-run above
- This log
