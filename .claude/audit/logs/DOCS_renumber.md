# DOCS_renumber — log

Mechanical number-update pass after the pipeline 1→2→4→5 re-run (five defect fixes, most
consequential: `get_ple_info()` name-only-fallback double-crediting bug). Scope: `README.md`,
`CLAUDE.md`, `changelog.md`, `RESUME.md`, `docs/data_dictionary.md`, `docs/pipeline_architecture.md`,
`docs/HANDOFF_TESTING_GUIDE.md`, `docs/MANUSCRIPT_GUIDE_MAIN_DASHBOARD.md`,
`docs/MANUSCRIPT_GUIDE_CHED_DASHBOARD.md`. `docs/CHED_CMO.md` and `docs/tree_dir.txt` were checked —
neither contains any of the affected numbers, so neither was touched.

## Method note

Several old numbers appear in two distinct contexts that needed different treatment:
1. **Genuine history** — a past changelog/doc entry describing what the *previous* remediation
   (RC-0/O-24) specifically changed (e.g. "confirmed passers moved 49,986 → 49,086"). Left
   untouched, since it accurately describes that earlier fix, matching the verification grep's
   expectation of "deliberate historical references." Where leaving it bare risked confusing a
   reader into citing the stale 49,086 figure, I added one clause pointing to the further,
   current change (see per-file notes).
2. **Current-state claims** ("current, post-fix", "Numbers to cite", "the current headline
   finding") — updated to the final numbers in the task's table, since these are read as live
   facts by anyone using the doc today.

## Per-file changes

### README.md
- Line 91: `IS_PLE_PASSER` results line — 49,086 → 47,485, reworded to show both prior figures
  (49,986, 49,086) as historical.

### CLAUDE.md
- Line 182: `IS_PLE_PASSER` flag description — 49,086 → 47,485, historical figures both named.
- Line 347: CHED-dashboard below-40 finding — 6,173/25,596 (24.1%) → 5,665/25,023 (22.6%).

### changelog.md
- Added a new top entry, **[2026-08-14] — PLE Identity-Propagation & Sentinel-Value Fix**,
  documenting all five fixes and the full old→new number table (passers, distinct people,
  observable linkage, below-40 linkage, B1 passers, bin gradient, median percentile,
  `PLE_YEAR_UNCERTAIN`, `rejected_ambiguous_person`, non-nested counts, `UNDERGRAD_UNI_TYPE`
  breakdown, `NMS_PER_num` nulls, equal-exposure figures). The existing `[2026-08]` entry
  (RC-0/O-24) was left untouched — it is accurate history of that specific, earlier fix.

### RESUME.md
- Headline block: observable linkage, passer sittings/people, `PLE_YEAR_UNCERTAIN`, linkage-by-bin
  all updated to new values.
- "READ THIS BEFORE CITING..." section: 39.4%→38.0% (equal 8-year horizon linkage). The
  three/four-row below-40 cascade table was reduced from three defect-steps to two: the
  "`drop -1 sentinel rows`" row is now **removed** because that fix is applied at the pipeline
  source as of this pass, so the "published" row already starts from the sentinel-safe number
  (5,665/25,023) — keeping a separate row for it would have shown two consecutive rows with
  identical n and no real transformation between them. The note below the table was reworded to
  past tense to describe the fix rather than the still-live bug.
  Reworded the note under the table to describe the sentinel fix as applied, past tense.
- Headline-finding paragraph and the "Withdrawn" B4→B5 step-size paragraph updated (recomputed
  step sizes from the new per-bin gradient: B4→B5 now 10.0, B1→B2 now 9.9).
- **Left unchanged, no orchestrator-verified replacement exists:**
  - `+ drop contested-name people (**conservative floor**) | 17.9% | 4,325 / 24,185` — this
    "conservative floor" row goes beyond the two equal-exposure figures given; no new value was
    supplied.
  - `795 published → **482** at the floor` — the "482" (floor-adjusted B1 count) is derived from
    the untouched conservative-floor row above; only the "795" was updated to 740.
  - `(B1 7.1 → B10 63.3)` — the floor-adjusted gradient, same reason.
  - `+ equal 8-year exposure | 18.3% | ...` — the percentage was updated per the task's explicit
    equal-exposure figure, but I had no verified numerator/denominator to replace the old
    `4,879 / 25,023`, so the n column was replaced with a plain note rather than a fabricated
    number. **Orchestrator: please supply the new numerator for this row.**
  - `54%→37% decline across years mostly disappears` — no replacement value given.

### docs/data_dictionary.md
- Framing note, `UNDERGRAD_UNI_TYPE` table row, `NMS_PER_num` nulls, `IS_PLE_PASSER`,
  `PLE_MATCH_METHOD`/`PLE_MATCH_CONFIDENCE`, `PLE_YEAR_PASSED`'s equal-exposure sentence,
  `IS_BEST_OBSERVABLE_RECORD`'s linkage figure, `PLE_MATCH_OUTCOME`, `PLE_YEAR_UNCERTAIN`, and the
  `linkage_rate` code comment — all updated to the new figures. Recomputed the derived
  passer/PLE-source-names match ratio (85.8% → 81.9%, from 35,746/43,630) and the
  `UNDERGRAD_UNI_TYPE` percentages (77.0% / 20.6% / 1.3% / 1.1%, verified to sum to 178,927).
- **Left unchanged, no orchestrator-verified replacement:**
  - `UNDERGRAD_UNI_LOCATION` row's `Unknown (1,832)` — a different column from
    `UNDERGRAD_UNI_TYPE`'s `Not Specified` (which *was* given a new value, 2,011); the two only
    coincidentally shared the same old number. No replacement was given for
    `UNDERGRAD_UNI_LOCATION`, so it was left as-is.
  - `PLE_MATCH_METHOD`'s null count `121,623 (68.0%)`, `EXACT` `54,437`, `DETERMINISTIC_APPNO` `92`.
  - `PLE_YEAR_PASSED`'s non-null count `54,528`, and the "not nested" breakdown `7,318` / `2,776`.
  - `IS_BEST_OBSERVABLE_RECORD`'s naive-form figure `65,782 people / 46.69% linkage`.
  - `PLE_MATCH_OUTCOME`'s `no_match (121,623)` and `rejected (2)`. **Flag:** with `accepted`
    now 47,485 and `rejected_ambiguous_person` now 8,207, this row's four values no longer sum to
    178,927 (short by 1,610) — `no_match` almost certainly also moved and needs a verified figure.
  - `PLE_YEAR_UNCERTAIN`'s "85 such application numbers" detail.
  - The framing-note proof: "UP Diliman ... 4,421 rows, **1,914** of them confirmed PLE passers."

### docs/pipeline_architecture.md
- §3 "Match results" table and `PLE_MATCH_METHOD` breakdown, §3 "Cohort sizes" linkage rate — all
  updated.
- §7 RC-0 "Measured effect" table: the "Before (biased matcher)" column is left as genuine
  original-bug history; the "After" column and "Change" column were updated to the **final**
  current numbers (not just RC-0's isolated effect), since the document repeatedly describes
  itself as reflecting "the system as it exists now." Added a one-sentence caveat in the table
  intro so the delta isn't misattributed to RC-0 alone.
  Recomputed the withdrawn-finding step-size comparison (10.0 / 9.9 / 10.3) and the current
  headline-finding paragraph (25,023 / 5,665 / 22.6% / 740 / 3.3% / 5,645 of 5,665), and added a
  one-line pointer to the equal-exposure 18.3% figure.
- Added a new **"### Five further fixes (2026-08-14 follow-on pass)"** subsection at the end of
  §7, before §8, documenting all five fixes in the same style as RC-0/O-24, with the full
  before/after number list.
- The original `49,986 → 49,086` "Combined effect of both fixes" paragraph (RC-0/O-24) was left
  as history, with one added sentence pointing to the further move to 47,485.

### docs/HANDOFF_TESTING_GUIDE.md
- Headline reference block, Tab 1 metrics, Tab 13/CHED-dashboard Section C linkage gradient
  (including the `n=6853, linked_n=740, linkage_rate_pct=10.8` spot-check line), Tab 5 "Key
  Evidence" B1/B4 citation, and the "both dashboards must agree" sentence — all updated.
- **Left unchanged, no orchestrator-verified replacement** (the guide's own text explicitly
  tolerates staleness — "treat this guide as stale for that line — do not assume you did
  something wrong" — so these were left rather than guessed): CHED-dashboard Tab 2 metrics
  (`17,752 (65.2%)`, `2,247 (8.3%)`, `60,184 (59.4%)`, `12,589`, `109.0`, `17.8%`) and Tab 3
  metrics (`41,289`, `23,128`, `56.0%`) — all downstream of `UNDERGRAD_UNI_TYPE` and/or
  `IS_PLE_PASSER`, which did change, but no replacement figure was supplied.

### docs/MANUSCRIPT_GUIDE_MAIN_DASHBOARD.md
- §2.2 "Numbers to cite" (passers, ambiguous keys, `PLE_YEAR_UNCERTAIN`), §3.1 executive-summary
  numbers, §3.13 CHED-bridge linkage gradient, §3.13a headline finding and its three
  survives-attack checks, and §5's withdrawn-claim step-size list — all updated.
- §2.2's "Consequence, reported with direction" paragraph (RC-0/O-24's own 49,986→49,086 effect)
  left as history, with one added clause pointing to the further move to 47,485.
- **Left unchanged, no replacement given:** "1,914 of them confirmed PLE passers" (UP Diliman
  proof-of-scope-ceiling example, §Global rules).

### docs/MANUSCRIPT_GUIDE_CHED_DASHBOARD.md
- §1.2's "Both are now fixed" paragraph reworded to note the further 2026-08-14 fixes and the
  move to 47,485 (kept the 49,986→49,086 sentence as accurate RC-0/O-24 history).
- §2.1 median percentile, §2.3 linkage-by-bin block and step-size caveat, §3 headline finding,
  its objections table, and its "linkage, not pass rate" caveat, §4 withdrawn-claims step sizes —
  all updated.
- **Left unchanged, no replacement given:** §0's "1,914... confirmed PLE passers" proof; §2.2 Tab
  2 metrics (`17,752/27,234`, `2,247`, `60,184/101,400`); §2.3 Tab 3 stress-test
  `56.0% (23,128 of 41,289)`; §2.4 Tab 4 score/citizenship metrics (unrelated to the matcher fix).

## Verification

```
.venv/Scripts/python.exe -m pytest tests/ -q
36 passed in 0.87s
```

```
grep -rn "49,086\|45\.44\|24\.1%\|6,173\|25,596\|37,420" README.md CLAUDE.md changelog.md RESUME.md docs/
```
Every remaining hit is a deliberate historical reference (the frozen `[2026-08]` changelog entry,
the RC-0/O-24 "moved from 49,986 to 49,086" sentences in the pipeline-architecture doc and both
manuscript guides — each now followed by a clause pointing to the further, current 47,485 figure)
or one of the new "old → new" transition sentences added by this pass (changelog's new entry,
pipeline_architecture.md's new "Five further fixes" subsection). No bare/uncaveated old figure
remains anywhere in the owned files.

## Outstanding for the orchestrator

A handful of derived numbers depend on the fixed inputs but were never given a verified
replacement value; fabricating them was out of scope for a mechanical pass. Listed above,
file-by-file. The one worth flagging loudest: `docs/data_dictionary.md`'s `PLE_MATCH_OUTCOME`
row (`no_match` / `accepted` / `rejected_ambiguous_person` / `rejected`) no longer sums to
178,927 with only the given numbers — `no_match` needs a verified new count.
