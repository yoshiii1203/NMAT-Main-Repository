# Auditor 09 — Git History (full 47-commit chronology, main repo + 2 nested repos)

Scope: main repo `.git` (47 commits, `1f81910`→`dc46a04`, branch `master`), plus nested repos at
`streamlit_dashboard/CHED_relevant_dashboard/.git` and `streamlit_dashboard/main_dashboard/.git`.
Read-only: `git log/show/diff/ls-files/ls-tree`, plus Python parquet reads. No files edited.

---

## 1. Annotated chronology (all 47 commits, chronological, grouped into phases)

Legend: A=insertions, D=deletions, F=files changed (from `git log --shortstat`).

### Phase 0 — Initial import (2026-07-27)
| sha | author | message | A/D/F | Assessment |
|---|---|---|---|---|
| `1f81910` | kateikyoushi | Initial commit: NMAT Analysis project | +41779/F32 | Baseline import: notebooks, dashboard.py, RShiny, reports/, vault/. |
| `e112537` | kateikyoushi | chore: gitignore vault/ directory | +3/-289/F2 | `vault/` (internal analysis docs, contains `HONEST_ASSESSMENT.md` admitting Pipeline 4 may be unnecessary work — see §2) ignored going forward but still tracked from commit 1 (see hygiene §6). |
| `38bb2ff` | kateikyoushi | remove obsolete .ipynb, replace with .py | -113/F1 | Housekeeping. |

### Phase 1 — Pipeline 4 / Exodus cutover (2026-07-27)
| sha | author | message | A/D/F | Assessment |
|---|---|---|---|---|
| `418f0bc` | kateikyoushi | feat: Pipeline 4 - NMAT_Ultima -> NMAT_Exodus with citizenship integration | +521/F1 | Adds `4_Citizenship_Integration.py`. |
| `16e2fc6` | kateikyoushi | chore: Pipeline 4 & dashboard migration complete | +166/-83/F3 | |
| `00b8eee` | kateikyoushi | fix: dashboard now loads from NMAT_Exodus.parquet, cache busted | +84/-83/F1 | Root dashboard.py cut over. |
| `87c7d4e` | kateikyoushi | feat: R Shiny dashboards now load from NMAT_Exodus.parquet | +8/-6/F2 | Out of audit scope per shared context but note: fallback path lists still literally contain `NMAT_Ultima.parquet` (intentional back-compat, not re-verified — RShiny excluded). |
| `632b5bd` | kateikyoushi | fix: restore emoji icons in dashboard.py tab labels | +20/-20/F1 | A fix immediately undoing cosmetic regression from a prior commit — sign of un-reviewed rapid iteration. |
| `f56fb55` | kateikyoushi | fix: audit findings - 5 critical bugs fixed | +29/-8/F2 | **See §2, Claim 1.** |
| `86c2bdb` | kateikyoushi | feat: add CHED Compliance page (Page 13) to dashboard.py | +407/-2/F1 | |

### Phase 2 — Exodus slimming & renames (2026-07-28)
| sha | author | message | A/D/F | Assessment |
|---|---|---|---|---|
| `49cce08` | kateikyoushi | fix: 3 stale NMAT_Ultima error messages updated to NMAT_Exodus | +5/-5/F1 | **See §2, Claim 5 (renames).** Only touched error-message strings, not the fallback-path lists (by design — those remain for back-compat). |
| `39d3284` | kateikyoushi | chore: archive planning docs to .artifacts/, remove fix_dashboard.py | **+162187/-101/F39** | **CONFIRMED commit-message/diff mismatch (HIGH, see F-08).** Message implies a docs move; diff actually adds the entire 13-page `data_aggregator/` system (13 page scripts, `run_all.py`, `helpers.py`, `config.py`) plus 13 generated markdown/CSV outputs including a 39,689-line `00_MASTER_REPORT.md` and a 77,771-line `08_repeat_takers_detail.csv` — none of that is mentioned in the commit message. |
| `9b084b2` | kateikyoushi | feat: create NMAT_Exodus_Lite.parquet (54 cols, 10.5MB, 62% smaller) | +21/-21/F15 | **See §2, Claim 5.** |
| `4cf444c` | kateikyoushi | fix: data_aggregator points to NMAT_Exodus.parquet (renamed from Lite) | +21/-21/F15 | Renamed `NMAT_Exodus_Lite.parquet`→`NMAT_Exodus.parquet` one commit later — i.e. the "Lite" name lived for exactly one commit. |

### Phase 3 — Documentation pass (2026-07-28)
| sha | author | message | A/D/F |
|---|---|---|---|
| `60acfc1` | kateikyoushi | docs: pipeline architecture doc (Mermaid) | +504/F1 |
| `76f1bf2` | kateikyoushi | docs: data dictionary for NMAT_Exodus.parquet (54 cols) | +229/-133/F1 |
| `9a5272b` | kateikyoushi | docs: update README, add LICENSE (GPLv3) | +856/-650/F2 |
| `549eeb5` | kateikyoushi | docs: add 00_RUN_ME.ipynb to README | +20/-2/F1 |
| `24e271e` | kateikyoushi | fix: remove rapidfuzz from 00_RUN_ME.ipynb, update requirements.txt | +11/-4/F2 |
| `f25b2cc` | snorlax | docs: fix 00_RUN_ME.ipynb description | +3/-11/F1 |
| `be08185` | snorlax | docs: move docs to docs/, archive pipeline results to .artifacts/ | -277/F6 | Creates `docs/` and `.artifacts/` (later deleted at `43b5fb5`, then partially resurrected at `619a150` — see §3). |

### Phase 4 — CHED dashboard build-out (2026-07-28, single day, 27 commits — the bulk of the history)
| sha | author | message | A/D/F | Note |
|---|---|---|---|---|
| `428f9f0` | snorlax | feat: CHED dashboard council decision + computation suite | +7312/F23 | First `ched_compute/01_national_benchmark.py`…`09_accountability_framework.py` generation. |
| `352e122` | snorlax | feat: CHED dashboard - Phase 0/1 complete | +1025/-294/F10 | |
| `05e41e0` | snorlax | feat: CHED dashboard complete - all 9 scripts + 10-tab dashboard | +1614/-162/F6 | |
| `3b914e2` | snorlax | fix: remove computation button, fix surrogate unicode in dashboard.py | +56/-85/F1 | **See §4.** |
| `0f9b4f9` | snorlax | chore: final cleanup and documentation | +3340/-7/F6 | This is the commit that creates `streamlit_dashboard/main_dashboard/` as a **copy** of root `dashboard.py` (via rename-detected history). |
| `4e230ea` | snorlax | docs: "surrender to Claude Sonnet 5" — prayer.md | +329/F1 | Planning doc, later deleted at `c78670a`. |
| `c921943` | snorlax | dtype: fix PyArrow value_counts/crosstab numeric coercion in CHED dashboard | +933/-1297/F1 | Large rewrite of CHED `dashboard.py`, superseded by later commits same day. |
| `6851005` | snorlax | ched-dashboard: apply full reviewer revision | +569/-652/F1 | |
| `2b02ec7` | snorlax | ched-dashboard: fix foreign context to use ALL records (not best-record) | +16/-11/F1 | **See §2, Claim 3 / F-05.** |
| `7932bc6` | snorlax | remove stale planning docs, ched_compute artifacts, and test files | -8006/F25 | **See §5.** Deletes the entire first-gen `ched_compute/01_national_benchmark.py..09_accountability_framework.py` suite + `test_write.txt`. |
| `ec8ec8c` | snorlax | fix Pylance ExtensionArray rounding warnings | +3/-3/F1 | **See §2, Claim 4 / F-06.** |
| `e69dd6c` | snorlax | remove explicit engine=pyarrow, `text_auto='.1f'`→`True` | +3/-3/F1 | **See §2, Claim 4 / F-07.** |
| `c78670a` | snorlax | add .gitignore for standalone dashboard repos, remove prayer.md | +24/-363/F4 | |
| `830fc67` | snorlax | ched-dashboard: increase vertical_spacing from 0.12 to 0.22 | **+6940/-1/F22** | **CONFIRMED commit-message/diff mismatch (HIGH, see F-08).** The stated change is a single `vertical_spacing=0.22` line; the diff actually adds the entire *second-generation* `ched_compute/01_national_benchmark.py..09_accountability_framework.py` suite (9 scripts + helpers/config/run_all + 9 markdown outputs, 6,939 unrelated lines). |
| `aa0a947` | snorlax | add runtime.txt (Python 3.12), remove use_threads | +2/-1/F2 | Matches nested-CHED-repo's last synced commit `33fa26f` (see §7). |
| `be706d6` | snorlax | docs: add review/check message for dashboard deployments | +66/F1 | Reverted 1 commit later. |
| `9e5a4cb` | snorlax | Revert "docs: add review/check message..." | -66/F1 | Net no-op pair — 2 wasted commits, no lasting effect, no dangling refs. |
| `43b5fb5` | snorlax | chore: remove .artifacts dir, add .temp/ to gitignore | -8240/F10 | Deletes `.artifacts/*`. **Undone 1 commit later (see next row) — CONFIRMED regression.** |
| `619a150` | snorlax | ched-dashboard: fix HasTRUErawScores/StoredVsDerivedMismatch dtype bug | **+8566/-53/F10** | **CONFIRMED: re-adds the exact `.artifacts/*.md` files deleted one commit prior at `43b5fb5`** (byte-for-byte same content — `1_Data_Cleaning_Results.md`, `2_PLE_Matching_Results.md`, `3_NMAT_PLE_Results.md`, `BIN_REFACTOR_PLAN.md`, etc., 8,240 lines), bundled into an unrelated dtype-fix commit. `.artifacts/` is tracked at HEAD as a result (see §6). The actual dtype fix is a 30-line hunk in `dashboard.py`. |
| `85b6f33` | snorlax | restructure compute scripts to 6-tab match, add verified_true verifier outputs | +4873/-5266/F39 | Third-generation `ched_compute/01_national_profile.py..06_data_limitations.py` (current names at HEAD), plus `ched_compute/verified_true/` verifier scripts. |
| `113d00d` | snorlax | add export_markdown.py, fix lazy generation, add start_dashboard.ps1 | +1115/-43/F25 | |
| `7fa0f18` | snorlax | fix image paths in complete_markdown (viz/ -> ../viz/) | +630/F1 | |

### Phase 5 — Forensic audit suite (2026-07-28)
| sha | author | message | A/D/F |
|---|---|---|---|
| `08d196a` | snorlax | add forensic audit of NMAT->PLE passers (below-cut-off validation) | +35344/F12 |
| `1d4eda2` | snorlax | add name cross-check scripts for appno-based PLE matches | +321/F2 |
| `ff45adf` | snorlax | add name cross-check evidence report (4 genuine mismatches) | +196/F1 |
| `dc46a04` | snorlax (HEAD) | add per-bin audit breakdown with name cross-check by B1/B2/B3/B4 | +300/F2 |

**Observation on authorship:** the repo has two contributor identities, `kateikyoushi` (commits 1–10, `1f81910`…`86c2bdb`, spanning initial build through Phase 1) and `snorlax` (everything from `49cce08` onward, all of Phase 2 onward, all in a single calendar day 2026-07-28 per commit timestamps for 33 of 47 commits). Not inherently a problem, but the entire CHED-dashboard build/fix/revert cycle (17 commits, Phase 4) happening same-day suggests no interval for review between commits — consistent with the message/diff mismatches found.

---

## 2. Claimed-fix vs actual-state-at-HEAD verification table

| Commit | Claim | Verified at HEAD? | Evidence |
|---|---|---|---|
| `f56fb55` "5 critical bugs fixed" | 5 bugs: (1) Tier 1b uses `'Foreign'` not `School Type_rec2_FINAL` (89 records), (2) 22 missing nationality values added to normalization map, (3) Tier 2 pseudo-citizenship normalized (13 records), (4) operator-precedence bug in `tier1b_mask` fixed, (5) `to_bool_series()` handles `'1.0'`/`'0.0'` float strings | **CONFIRMED landed and present at HEAD** for bug 5 (root `dashboard.py:128`, and copied into `streamlit_dashboard/main_dashboard/dashboard.py:129`, and independently present in `data_aggregator/page_02_data_integrity.py:32`). Bugs 1–4 are inside `4_Citizenship_Integration.py`; diff for that commit shows the described edits landed and nothing since has reverted them (no later commit touches `4_Citizenship_Integration.py`'s tier logic). | `git show f56fb55`; `grep -rn "\"1.0\": True" *.py` |
| `619a150` / CHED dtype fix, `c921943` PyArrow numeric coercion | "string cols now properly coerced to bool/float" | **PARTIALLY FALSE at HEAD — CONFIRMED.** Fixed in the *live* CHED `dashboard.py` (`validate_schema()`, lines 95-102) and in root/`main_dashboard` `dashboard.py` (`to_bool_series`) and in `data_aggregator/page_02_data_integrity.py`. **NOT fixed in `ched_compute/06_data_limitations.py`** (the static report generator behind `page_results/06_data_limitations.md`) — see **F-01, CRITICAL**, empirically reproduced below. | See F-01 for runnable evidence. |
| `2b02ec7` "fix foreign context to use ALL records (not best-record) - matches data-aggregator page 04" | Claims consistency with `data_aggregator` page 04 | **Directionally correct but inconsistent elsewhere — CONFIRMED, see F-05.** `data_aggregator/page_04_score_bins.py` *does* use "ALL records with non-null CITIZENSHIP_FINAL" for its citizenship section, matching the CHED dashboard post-fix. But `ched_compute/04_institution_context.py` (CHED's own static twin of the same tab) reports **best-record** foreign counts as "PRIMARY" and all-records only as secondary context — the two CHED artifacts (live dashboard vs. static markdown) now disagree on methodology for the same number. |
| `ec8ec8c` "fix Pylance ExtensionArray rounding warnings" (`.values.round(1)` → `.to_numpy(dtype=float, na_value=0).round(1)`) | Framed as a lint-only fix | **CONFIRMED semantic change, not lint-only.** `na_value=0` silently converts any `NaN`/`pd.NA` in `top_share`/`bot_share` to `0.0` before display, where the prior `.values.round(1)` on a nullable-float ExtensionArray would have preserved missingness. If any year has no B8-B10 or B1-B3 records, the table now shows `0.0%` (a real value) instead of missing — misleading for CHED stakeholders. **HIGH.** |
| `e69dd6c` "replace `text_auto='.1f'` with `True` to satisfy Pylance stubs" | Framed as a lint-only fix | **CONFIRMED semantic change.** `text_auto=True` hands Plotly's default number formatting instead of a pinned `.1f` (one decimal). Two `px.imshow()` heatmaps (bin-distribution and university-type-bin heatmaps in CHED tab 2) are affected — displayed precision is no longer controlled by the developer. **MEDIUM** (visual only, no wrong numbers, but a real user-visible change mislabeled as lint). |

---

## 3. Reverts and abandoned work

| Commit(s) | What happened | Correct? | Dangling references? |
|---|---|---|---|
| `be706d6` → `9e5a4cb` | Added then immediately reverted `.artifacts/message.md` (66 lines, a "review/check message for dashboard deployments") | Net no-op; no lasting effect. Two wasted commits (commit-hygiene note, not a bug). | None — file never referenced elsewhere. |
| `7932bc6` "remove stale planning docs, ched_compute artifacts, and test files" | Deletes `DECISION.md`, `IMPLEMENTATION_PLAN.md`, `REINTEGRATION_PLAN.md`, the **entire first-generation** `ched_compute/01_national_benchmark.py`…`09_accountability_framework.py` (9 scripts, `helpers.py`, `config.py`, `run_all.py`, 9 markdown outputs), and `test_write.txt` | Correct call — that generation was superseded by the `830fc67`/`85b6f33` rebuilds. | None found — `run_all.py`, `helpers.py`, `config.py` were all re-created fresh 3 commits later at `830fc67`/`85b6f33` under the same names but different content/structure; no code imports the deleted modules. |
| `43b5fb5` "remove .artifacts dir" | Deletes 8 `.artifacts/*.md` planning/dump files (8,240 lines) | Correct call in isolation | **CONFIRMED regression**: the exact same files were re-added one commit later at `619a150` (bundled into an unrelated dtype-fix commit) and are **still tracked at HEAD**. See F-08/§6. |
| `3b914e2` "remove computation button" | Removes a "Run Computation Scripts" button from CHED `dashboard.py` (the button presumably shelled out to `ched_compute/run_all.py`) | Reasonable for a stakeholder-facing deployment (no build tooling in front of CHED reviewers) | No dangling references at HEAD — `grep -n "run computation\|subprocess" streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` returns nothing. Clean removal. |

---

## 4. Deleted tests / test coverage at HEAD

**CONFIRMED: the repo has zero automated tests at HEAD.**
- `grep -rn "^import pytest\|^import unittest\|def test_"` across all `.py` files (excluding `.venv`) → no matches.
- No `test_*.py` / `*_test.py` files anywhere in the tree.
- `requirements.txt` does not list `pytest` or `unittest`.

What `7932bc6` actually deleted under the "test files" label was `streamlit_dashboard/CHED_relevant_dashboard/test_write.txt` — a single-line stray file (almost certainly a write-permission smoke-test artifact from Streamlit Cloud debugging), **not** an automated test suite. No real test coverage was ever lost in git history; there never was any. This is a pre-existing gap, not a regression — but the finding stands as requested: **there is no runnable check anywhere in this repo that would catch a broken pipeline stage, a bad dtype coercion, or a wrong dashboard number before a human notices it in the UI.** Given the bugs found in §2 (F-01) and by the other 11 auditors, this absence is directly responsible for at least one bug shipping silently into a committed report file.

---

## 5. Renames and stale references

Traced: `NMAT_Ultima` → `NMAT_Exodus` (`49cce08`, `418f0bc`, `00b8eee`), `NMAT_Exodus_Lite` → `NMAT_Exodus` (`9b084b2` creates it, `4cf444c` renames it one commit later).

Full-tree grep for `NMAT_Ultima` and `NMAT_Exodus_Lite` at HEAD (excluding `.venv`):

- **`NMAT_Exodus_Lite`**: only 2 hits, both historical/doc: `changelog.md:50` (changelog entry, correct — describing history) and `docs/pipeline_architecture.md:419` (a Mermaid diagram node labeled `NMAT_Exodus_Lite.parquet` describing the now-superseded intermediate step — **stale**, since the file was renamed to `NMAT_Exodus.parquet` one commit after creation and the Lite name never shipped). LOW.
- **`NMAT_Ultima`**: pervasive but mostly *legitimate* — it's genuinely the real intermediate filename produced by Pipeline 2 before Pipeline 4 renames/enriches it into Exodus (`CLAUDE.md:99`, `README.md:82/86/106`, `docs/pipeline_architecture.md`, `4_Citizenship_Integration.py:25` `ULTIMA_PATH = ROOT / "NMAT_Ultima.parquet"`, `2_PLE_Matching_Pipeline.ipynb`, `3_NMAT_PLE_Analysis.ipynb` all correctly reference it as a pipeline-stage name, not a bug).
  - `dashboard.py:109-110` and `streamlit_dashboard/main_dashboard/dashboard.py:110-111`: `find_data_path()` lists `dataset/NMAT_Ultima.parquet` and `NMAT_Ultima.parquet` as **fallback candidates** if `NMAT_Exodus.parquet` is missing, and `dashboard.py:1233`/`main_dashboard/dashboard.py:1234` has a user-facing error string mentioning it as a possible misconfiguration. This is deliberate back-compat, not stale — but it's **asymmetric**: the candidate list has no bare `Path("NMAT_Exodus.parquet")` entry to match the bare `Path("NMAT_Ultima.parquet")` one, so a deployment with Exodus sitting in the app root (no `dataset/` subfolder) fails to find it even though a same-shaped Ultima deployment would. **LOW**, easy one-line fix if ever hit.
  - `.artifacts/*.md`, `.temp/audit02/*.py`, `vault/*.md`, `reports/*.md`: all clearly archival/planning/report documents describing history — not live code paths, not misleading to a current user. Not flagged as bugs.
  - `RShiny_Dashboard/`: out of scope per shared context; not re-verified.

**No stale reference found that causes a functional bug** (unlike F-01, which is a live bug, not a naming issue).

---

## 6. Repo hygiene at HEAD

`.gitignore` covers: `.venv/`, `dataset/`, `__pycache__/`, `.ipynb_checkpoints/`, IDE dirs, `*.log`/`*.tmp`/`*.bak`/`*.backup`, R artifacts, `*.html`/`*.zip`/`*.exe`/`*.dll`, `images/`, `reports/*.pdf`/`*.docx`, `tree_dir.txt`, `vault/`, `.env*`, `.temp/`.

**Tracked but arguably shouldn't be** (`git ls-tree -r -l HEAD`, 145 files, 71.1 MB total, `.git` = 31 MB):

| File(s) | Size | Issue |
|---|---|---|
| `forensic_audit/forensic_audit_classified.csv` | 11.7 MB | Generated data dump, tracked. |
| `streamlit_dashboard/main_dashboard/NMAT_Exodus.parquet`, `streamlit_dashboard/CHED_relevant_dashboard/NMAT_Exodus.parquet` | 11.0 MB each | Two duplicate copies of the same file `dataset/` already has (byte-identical per shared context) — necessary only because `dataset/` is gitignored and the nested deployment repos need the data in-tree; still means 3× 11 MB in the main repo's pack across history plus 1× more in each nested repo's pack. |
| `data_aggregator/page_results/08_repeat_takers_detail.csv` | 10.2 MB | Generated output. |
| `data_aggregator/page_results/00_MASTER_REPORT.md` | 9.4 MB | Generated output (excluded from this audit per shared-context rule 6, but still a tracked-file hygiene issue). |
| `data_aggregator/page_results/08_repeat_takers.md` | 8.7 MB | Generated output. |
| `.artifacts/*.md` (8 files, 8,240 lines / ~8 MB combined) | | **Re-added by accident at `619a150`** after deliberate deletion at `43b5fb5` — see §3/F-08. Should be deleted again and actually kept out. |
| `vault/*.md` | | Ignored *going forward* by `e112537` but the files from the initial commit remain tracked (`git rm --cached` was never run) — `vault/HONEST_ASSESSMENT.md` and `vault/PIPELINE4_PLAN.md` are visible at HEAD despite `vault/` being gitignored. |
| `dashboard.py` (root) vs `streamlit_dashboard/main_dashboard/dashboard.py` | 3206 vs 3207 lines | **Confirmed diverged** — see F-04. Two maintained copies of the same file, drifting. |

**Untracked but arguably should be tracked** (from `git status`): `CLAUDE.md`, `changelog.md` — both are project documentation that other docs (`README.md`, `docs/`) are tracked counterparts of; leaving them untracked means they aren't versioned or shareable via `git clone`. Also untracked: the CHED "Implementation Plan" markdown, `streamlit_out.txt`/`tunnel_out.txt` (deployment logs — see below), and various `.temp/`/`.agents/` scratch files (correctly excluded by `.temp/` gitignore rule / not matched by any rule for `.agents/`).

**Untracked and correctly should stay untracked / needs a gitignore rule added:**
- `dashboard.py.bak` — untracked, correctly caught by the `*.bak` glob (not a tracking bug, just stray clutter on disk).
- `ngrok.msi`, `ngrok_log.txt` — **not covered by any existing `.gitignore` pattern** (`*.exe`/`*.dll` doesn't match `.msi`; `*.log` doesn't match `ngrok_log.txt` since it ends in `.txt`). Currently untracked only because nobody ran `git add -A`. **Recommend adding `*.msi`, `ngrok_log.txt`, `*_log.txt`, `*_out.txt` to `.gitignore`** before someone runs a blanket add.
- `streamlit_dashboard/CHED_relevant_dashboard/streamlit_out.txt`, `tunnel_out.txt` — same gap, same recommendation.

**Security check — `ngrok_log.txt` (item 8):** read in full. It is **never committed** (`git log --all -- ngrok_log.txt` returns nothing) and contains only local ngrok CLI diagnostic output — every session in the log shows `authentication failed: ... agent version ... too old` (`ERR_NGROK_121`); ngrok never successfully established a tunnel in this log, so **no live tunnel URL, authtoken, or bearer token is present**. No secret to flag. Recommendation stands regardless: add it to `.gitignore` so a future successful run (which would print a real `https://*.ngrok-free.app` forwarding URL) can't land in git by accident.

### `.gitignore` recommendations (concrete)
```
*.msi
ngrok_log.txt
*_out.txt
dataset/*.bak
```
And run `git rm --cached -r vault/ .artifacts/` once (out of scope for this read-only audit to execute, but flagged for the maintainer) to stop tracking content already meant to be excluded.

---

## 7. Nested-repo divergence — CRITICAL finding

Neither nested repo is a git submodule (`git submodule status` empty, `git ls-files -s | grep 160000` empty). Both are **plain independent git repositories** whose working directories happen to sit inside the parent's tree; the parent tracks their file contents as ordinary blobs (see the duplicate `NMAT_Exodus.parquet` / `dashboard.py` entries in §6). This is the risky pattern the task asked about: two "real" repos with real GitHub remotes, living invisibly inside the audited repo, that can silently drift from what's actually reviewed here.

| | `streamlit_dashboard/main_dashboard` | `streamlit_dashboard/CHED_relevant_dashboard` |
|---|---|---|
| Remote | `github.com/yoshiii1203/NMAT-Core-Dashboard.git` | `github.com/yoshiii1203/NMAT-CHED-Dashboard.git` |
| Local HEAD | `157434f` "Initial commit: NMAT core analysis dashboard" (1 commit total) | `33fa26f` "Add runtime.txt..." (3 commits total) |
| HEAD vs `origin/main` | **In sync** (`[origin/main]`, no ahead/behind) | **In sync** (`[origin/main]`, no ahead/behind) — i.e. whatever's on GitHub is exactly this stale commit |
| Nested HEAD vs parent-tracked working copy | **Byte-identical** — `git diff HEAD -- dashboard.py` empty | **Diverged — 645-line diff on `dashboard.py` alone**, plus 23 files with uncommitted changes: old `ched_compute/01_national_benchmark.py`…`09_accountability_framework.py` still present-but-deleted, new `ched_compute/01_national_profile.py`…`06_data_limitations.py` untracked, `run_all.py`/`config.py`/`helpers.py` modified. `git diff HEAD --stat`: **23 files, 489 insertions(+), 6738 deletions(-)** never committed to the nested repo. |
| Which parent commits actually reach it | Only `c78670a` (gitignore/README) and `0f9b4f9` (the commit that *created* the copy) ever touched `main_dashboard/`; both predate any CHED-specific bug fixes and none apply to it anyway (different app). Confirmed in sync with parent — **not a problem in practice**, just fragile-by-construction (any future edit to root `dashboard.py` won't propagate here automatically; see F-04). | Parent commits touching `CHED_relevant_dashboard/dashboard.py` after the nested repo's last commit (`aa0a947`, which matches nested `33fa26f`): `c78670a, e69dd6c, ec8ec8c, 7932bc6, 2b02ec7, 6851005, c921943, 3b914e2 [reordering aside], 619a150, 85b6f33, 113d00d, 7fa0f18` — **11+ commits' worth of fixes never reached the nested repo or its GitHub remote**, including the Pylance-precision changes (F-06/F-07), the foreign-context fix (F-05), and the dtype fix (`619a150`, itself incomplete per F-01). |

**Verdict — CRITICAL:** if `NMAT-CHED-Dashboard` on GitHub is what's deployed (e.g. to Streamlit Community Cloud, consistent with the `runtime.txt`/`start_dashboard.ps1` artifacts), **the live, stakeholder-facing CHED dashboard is running code from `aa0a947`'s era — before the "reviewer revision" (`6851005`), before the foreign-context fix (`2b02ec7`), before all three dtype/Pylance fixes, and before the compute-script restructure (`85b6f33`).** Whatever CHED reviewers see today is not the dashboard this audit fleet is reviewing. This needs to be confirmed operationally (check the Streamlit Cloud app's "last deployed commit") but the git evidence is unambiguous: nested-repo `origin/main` is 3 commits deep total and hasn't moved since `33fa26f`/`aa0a947`.

**`main_dashboard` verdict:** low risk today (content matches), but structurally fragile — it's a manual copy-paste sync (`0f9b4f9`) with no automation, so it will silently drift the next time root `dashboard.py` is edited without a matching copy step. It already has drifted once, from the *other* direction: root `dashboard.py` has 4 formatting/logic differences from its own nested copy that post-date the copy (see F-04) — meaning even the one-time copy is no longer faithfully mirrored by its source.

**Recommended structure:** stop tracking `NMAT_Exodus.parquet` and `dashboard.py` as duplicated blobs inside the parent repo. Either (a) convert both nested directories to real git submodules pointing at pinned commits (makes drift visible via `git submodule status` and forces an explicit bump), or (b) drop the nested `.git` entirely and drive deployment via CI (copy/sync step from the single source-of-truth files at release time), or (c) minimum viable fix: add a `CI` check or even a manual checklist step in `changelog.md`/release process that pushes the nested repos and confirms they match parent HEAD before calling a CHED-dashboard change "shipped."

---

## 8. Findings table

| ID | Severity | Status | Title | Location |
|---|---|---|---|---|
| F-01 | **CRITICAL** | CONFIRMED | `ched_compute/06_data_limitations.py` compares string-typed parquet columns against Python `True`/`1.0` literals — always evaluates to 0, and the wrong "0" is baked into a committed report | `streamlit_dashboard/CHED_relevant_dashboard/ched_compute/06_data_limitations.py:39,48,49`; committed evidence at `streamlit_dashboard/CHED_relevant_dashboard/ched_compute/page_results/06_data_limitations.md:21-27` |
| F-02 | HIGH | CONFIRMED | `619a150` reverts the `.artifacts/` deletion from `43b5fb5` one commit later, bundled invisibly into an unrelated dtype-fix commit; 8 planning/dump files (~8,200 lines) are tracked at HEAD that a prior commit explicitly tried to remove | `.artifacts/*.md` at HEAD; `git show 43b5fb5`, `git show 619a150` |
| F-03 | HIGH | CONFIRMED | `830fc67` and `39d3284` commit messages describe a one-line/doc-move change; diffs actually add entire unrelated multi-thousand-line subsystems (first-gen `ched_compute/` suite; the whole `data_aggregator/` system respectively) | `git show 830fc67 --stat`, `git show 39d3284 --stat` |
| F-04 | MEDIUM | CONFIRMED | Root `dashboard.py` and its supposed mirror `streamlit_dashboard/main_dashboard/dashboard.py` have diverged (em-dash vs hyphen formatting in 6 UI strings, plus a `Path("NMAT_Exodus.parquet")` fallback-candidate line present in one but not the other) since the one-time copy at `0f9b4f9` | `dashboard.py` vs `streamlit_dashboard/main_dashboard/dashboard.py`, diff at lines ~107-108, 2617-2631, 2806-2809, 3157-3171 |
| F-05 | MEDIUM | CONFIRMED | CHED live dashboard.py (post-`2b02ec7`) and CHED's own `ched_compute/04_institution_context.py` disagree on the correct denominator (all-records vs best-record) for "Verified Foreign examinees" | `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py:962-963` vs `streamlit_dashboard/CHED_relevant_dashboard/ched_compute/04_institution_context.py:61-77` |
| F-06 | MEDIUM | CONFIRMED | `ec8ec8c` "Pylance fix" silently changes NaN-handling semantics (`na_value=0` coerces missing values to a real 0.0%) in a table shown to CHED stakeholders | `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` diff at `ec8ec8c` |
| F-07 | LOW-MEDIUM | CONFIRMED | `e69dd6c` "Pylance fix" changes displayed heatmap-cell precision from a pinned `.1f` to Plotly's default `text_auto=True` formatting | `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` diff at `e69dd6c` (2 occurrences) |
| F-08 | CRITICAL | CONFIRMED | Nested repo `streamlit_dashboard/CHED_relevant_dashboard` (remote `NMAT-CHED-Dashboard`) is 11+ commits and multiple bug fixes behind the parent repo's HEAD, and its own working tree additionally has 23 files / 6,738 deleted lines never committed even locally | §7 above |
| F-09 | LOW | CONFIRMED | Repo has zero automated tests at HEAD; the one file `7932bc6` labeled "test files" was a 1-line stray artifact, not real coverage | §4 above |
| F-10 | LOW | CONFIRMED | `.gitignore` gaps: `*.msi`, `ngrok_log.txt`/`*_out.txt` not covered; `vault/` and (until `619a150`/current HEAD) `.artifacts/` ignored-but-still-tracked from before the ignore rule was added | §6 above |
| F-11 | LOW | CONFIRMED | `NMAT_Exodus_Lite.parquet` naming survives as a stale Mermaid-diagram label in `docs/pipeline_architecture.md:419` describing a filename that only existed for one commit | `docs/pipeline_architecture.md:419` |
| F-12 | LOW | CONFIRMED | Asymmetric fallback-path list in `find_data_path()`: bare `NMAT_Ultima.parquet` fallback exists, bare `NMAT_Exodus.parquet` does not | `dashboard.py:106-118`, `streamlit_dashboard/main_dashboard/dashboard.py:107-119` |
| F-13 | INFO | CONFIRMED | No secret found in `ngrok_log.txt` (never committed; every logged session failed authentication before a tunnel URL was ever issued) | `ngrok_log.txt` (untracked, working tree only) |

---

## 9. Per-finding detail (the two not fully covered inline above)

**F-01 detail (empirical reproduction, run against `dataset/NMAT_Exodus.parquet`):**
```
dtypes: HasTRUErawScores=str, StoredVsDerivedMismatch=str, CalcVsDerivedMismatch=str
(df['HasTRUErawScores'] == True).sum()               -> 0        (buggy, as used in 06_data_limitations.py:39)
astype(str).str.upper().isin(['TRUE','1','YES']).sum() -> 178882  (true count)
(df['StoredVsDerivedMismatch'] == 1.0).sum()          -> 0        (buggy, as used in 06_data_limitations.py:48)
pd.to_numeric(..., errors='coerce') == 1.0 .sum()      -> 56065   (true count)
```
And the committed output file directly shows the wrong numbers shipped:
`streamlit_dashboard/CHED_relevant_dashboard/ched_compute/page_results/06_data_limitations.md:25-27`:
```
- Formula mismatches (Total != Part I + Part II): 0
- Stored-vs-derived mismatches: 0
- Calc-vs-derived mismatches: 0
```
The first two should read ~178,882 (TRUE raw scores) is a *good* number (not a mismatch count) — but "Stored-vs-derived mismatches: 0" is wrong and should be **56,065**, a materially different claim about data quality (the whole point of the "42.2% of stored totals were wrong" narrative this file exists to document). This bug is in `ched_compute/`, the static-report generator whose outputs feed `export_markdown.py`'s "complete markdown" and the tracked `pdf_exports/tab_6_Data,_Methods,_and_Limitations.pdf` — i.e. it likely reached a PDF handed to a stakeholder.

**F-08 detail:** see §7 table in full; this is the single most consequential finding in this audit slice — it means code-review conclusions reached by the other 11 auditors examining `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` at HEAD may not describe what is actually deployed, if deployment is driven from the nested repo's GitHub remote.

---

## 10. Summary of what's NOT a finding (checked, clean)

- `dc46a04..1f81910`: exactly 47 commits, confirmed via `git rev-list --count HEAD`.
- No secrets found in `ngrok_log.txt` history (never committed) or its current content.
- `7932bc6`'s `ched_compute` deletion left no dangling imports.
- `3b914e2`'s button removal left no dangling references.
- `be706d6`/`9e5a4cb` revert pair is a clean no-op.
- Bug-fix mapping for `to_bool_series`-style string→bool coercion (from `f56fb55`) correctly landed in root `dashboard.py`, its `main_dashboard` copy, and `data_aggregator/page_02_data_integrity.py` — three of the (at least) four consumers that need it. Only `ched_compute/06_data_limitations.py` (F-01) was missed.
