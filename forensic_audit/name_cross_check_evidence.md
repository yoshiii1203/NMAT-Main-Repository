# Name Cross-Check: Evidence Log (rewritten)

**Source:** `forensic_audit/forensic_audit.py`, Section 4.
**Reproduce:** `./.venv/Scripts/python.exe forensic_audit/forensic_audit.py`
**Every number below comes from that run.** No manual reclassification step exists anywhere in the
pipeline that produced them — records needing human judgement are listed in
`forensic_audit_exceptions.csv`, not silently resolved one way or the other.

This document supersedes the version dated 2026-07-28. That version's headline **"4 genuine
mismatches" is withdrawn** — see `forensic_audit/_superseded/README.md` for why it was not
reproducible, and Section 6 below for the corrected number.

**Data version:** `dataset/NMAT_Exodus.parquet`, md5 `72b2808bb8bb9c3594980c5735f814e1`, post-fix
(the `2_PLE_Matching_Pipeline.ipynb` `disambiguate()` Step-4 matcher-suppression bug — see
`forensic_audit_report.md` §0b — is removed in this data). That fix does not change this document's
figures in substance: it only affects `EXACT`-method name-collision groups, and this document's
population is `MANUAL_APPNO_MATCH` / `DETERMINISTIC_APPNO` only (§0), which never call the affected
function. The 1-row drift in the population size (2,868→2,867 across pipeline re-runs) is ordinary
pipeline non-determinism at the margins, not a T2 effect.

---

## 0. What population this document covers, and why

A name cross-check is only informative for matches made **without** relying on name equality in the
first place. `MANUAL_APPNO_MATCH` and `DETERMINISTIC_APPNO` are matched by application number
(`APPNO_CLEAN`), so the PLE-side and NMAT-side names are independent evidence that can genuinely
agree or disagree. `EXACT` matches, by construction, were matched **because** the names already
matched — checking their names again is close to tautological and is out of scope here (the old
document's system-wide "97.2% / 0.2%" claim over EXACT matches is withdrawn for a different reason:
see Section 7).

**Population checked:** every row in the current `dataset/NMAT_Exodus.parquet` with
`PLE_MATCH_METHOD` in `{MANUAL_APPNO_MATCH, DETERMINISTIC_APPNO}` — **2,867 rows** (2,775 +
92), dataset-wide (not scoped to the observable cohort — identity verification does not depend on
`Year<=2014`).

**Name sources:**
- **NMAT-side name:** parsed from `PERSON_KEY` in the **current** parquet
  (`"SURNAME, GIVEN NAMES||birthdate"`, split on the literal `"||"`) — not the stale intermediate.
- **PLE-side name:** `PLE_FULL_NAME` in `dataset/output/PLE_MATCH_MASTER.csv`. This is unavoidable —
  `NMAT_Exodus.parquet` carries no PLE-side name at all, in any column, so no source in this repo
  lets us avoid this file entirely for the PLE side specifically.

---

## 1. Coverage of `PLE_MATCH_MASTER.csv` against the current parquet's APPNO-based population

Measured, not assumed, by joining on `APPNO_CLEAN` / `MATCHED_APPNO`:

| Coverage status | N | % of 2,867 |
|---|---:|---:|
| **Matched** — exactly one PLE-side name candidate found | 2,371 | **82.7%** |
| **Ambiguous** — more than one PLE-side name candidate shares this APPNO in the source file | 5 | 0.2% |
| **No master record at all** — this APPNO does not appear in `PLE_MATCH_MASTER.csv` | 491 | 17.1% |

**491 rows (17.1%) cannot be name-checked with any file currently in this repo.** Their identity
linkage is **unverified**, not verified-clean — do not read the results below as covering the full
APPNO-based population. Every claim in this document is scoped to the 2,371 rows ("checked
population") unless stated otherwise. `PLE_MATCH_MASTER.csv` itself is a partially-reconciled
intermediate (~7 weeks older than the analysed parquet at the time of the prior audit) — the 17.1%
gap here is a direct, measured consequence of that staleness, not a new defect.

The 5 "ambiguous" rows are genuinely ambiguous in the source data itself (two different PLE
applicants' names both point at the same NMAT `APPNO_CLEAN` in `PLE_MATCH_MASTER.csv`) — e.g. the
appno matched to NMAT record "Carlos, Norberto Jr. Ganzon" has two competing PLE-side candidates,
"CARLOS, NORBERTO JR GANZON" and "CASAO, ROSALYN ABROGENA". This is not something a name-parsing
heuristic can resolve; it is listed in `forensic_audit_exceptions.csv` as `ambiguous_source_conflict`
for human review, not guessed at.

---

## 2. The compound-surname normaliser

Implemented **in code**, deterministically, no manual step:

```python
FIL_PREFIXES = {"DE","DELA","DELOS","DELAS","DEL","LA","LAS","LOS","SAN","SANTA","SANTO","STO","STA"}

def normalize_surname(surname):
    tokens = surname.split()
    merged = []
    i = 0
    while i < len(tokens):
        cur = tokens[i]
        j = i + 1
        while cur in FIL_PREFIXES and j < len(tokens):
            cur = cur + tokens[j]
            j += 1
        merged.append(cur)
        i = j
    return " ".join(merged)
```

It merges a whitelisted Filipino compound-surname prefix token with the token that follows, so
`"DE GUZMAN"`, `"DE  GUZMAN"`, and `"DEGUZMAN"` all normalise to `"DEGUZMAN"`; `"DE LA CRUZ"` and
`"DELA CRUZ"` both normalise to `"DELACRUZ"`. Surnames without such a prefix token are returned
unchanged. It is applied to the surname comparison inside `parse_names()` — nowhere else, and with
no per-record judgement calls.

---

## 3. Effect of the normaliser — raw vs. normalised, same 2,371-row population

| Verdict | Raw (no normaliser) | Normalised |
|---|---:|---:|
| `strong_match` | 1,849 | 1,874 |
| `high_overlap` | 352 | 348 |
| `surname_swapped` | 90 | 88 |
| `same_surname_no_given_match` | 22 | 22 |
| `married_name_change` | 3 | 3 |
| **`genuine_mismatch`** | **55** | **36** |

**The normaliser resolves 19 of the 55 raw `genuine_mismatch` flags** — records where the surname
was identical apart from compound-prefix spacing (e.g. "DE GUZMAN, JOSHUA" vs "Deguzman, Joshua")
now correctly land in `strong_match`, in code, without a human re-reading the pair.

### Low-score subset (`NMS_PER_num < 40`, n=475 of the 2,371 checked)

| | Raw | Normalised |
|---|---:|---:|
| `genuine_mismatch` | 13 | **10** |
| Resolved by normaliser | — | 3 |

This is the number that matters for the below-cutoff question this audit exists to answer: **13
low-score records auto-flagged as a name mismatch, of which the normaliser resolves 3, leaving 10
genuinely unresolved** — not the 17 the old script flagged on a different (stale-file-only)
population, and not the 4 the old evidence document claimed after an undocumented manual pass.

---

## 4. Remaining unresolved `genuine_mismatch` (n=36) — full list, no exclusions

Every one of the 36 records the normaliser does **not** resolve, written verbatim to
`forensic_audit_exceptions.csv` (`exception_type = unresolved_genuine_mismatch`) for human review.
This is the complete list — nothing here has been filtered, curated, or reclassified:

```
LIAO, KATHERINE MARIÑAS               <-> LIM, KATHERINE STA MARIA                    pct=1   B1  overlap=0.17
SHEIKH AL BAIDANI, SUMIYA SEMBLANTE   <-> SHEIKH ALBAIDANI, SUMIYA SEMBLANTE           pct=9   B1  overlap=0.5
CHIO, EDWARD JR GARCIA                <-> WYCOCO, EDGARDO JR GARCIA                   pct=9   B1  overlap=0.33
YOUNG, CHRISTINE MAE SOCO             <-> YONG, CHRISTINE MAE YEE                      pct=74  B8  overlap=0.33
DELA ROSA, CATHERINE ROSE DE GUZMAN   <-> DAJAY, CATHERINE GRACE DE GUZMAN             pct=97  B10 overlap=0.38
ANIAG, NOREEN DELA PEÑA               <-> MATIBAG, NORREN ANNE PENA                    pct=94  B10 overlap=0.14
SIMON, MARIA ANGELICA PABLO           <-> USON, MARIA ANGELICA JAYLO                   pct=60  B7  overlap=0.33
CASTELO, MICHAEL-VINCE BAUTISTA       <-> LOY, MICHAEL VINCENT BAUTISTA                pct=59  B6  overlap=0.33
UCLUSIN, ANTONIO JR AGAMAO            <-> TUBLE, HARLEY ALON                           pct=62  B7  overlap=0.0
VITORILLO-PLUECKEBAUM, MARIA JENIFFER <-> VITORILLO PLUCKEBAUM, MARIA JENIFFER ARON    pct=28  B3  overlap=0.5
CABALONA, ABEGAIL PEÑA                <-> CARBALLO, ABEGAIL VINAS                      pct=13  B2  overlap=0.2
CALLANTA, MARIE JO GONZALES           <-> LAURILLA, MARY JOY GONZALES                  pct=38  B4  overlap=0.14
SY, EFFIE NADINE CARDEÑO              <-> SAMEON, NADINE CEDENO                        pct=84  B9  overlap=0.17
LLUCH, TANYA KATRINA SALILLAS         <-> AGRASADA, TANYA KATRINA BUENAFLOR            pct=66  B7  overlap=0.33
SAGUN, JESSICA GO                     <-> BUOT, JESSICA JANE GO                        pct=78  B8  overlap=0.4
NAVARRO, MICHELLE FLORES              <-> MONTECLARO, MICHELLE FLORES                  pct=43  B5  overlap=0.5
VALDES, JOSE LUIS SCHULZE             <-> PANEDA, JOSE LUIS CRUZ                       pct=95  B10 overlap=0.33
URBIZTONDO, DENE MARIE MAGNO          <-> RUBIO, JADE MARIE DIMAANO                    pct=74  B8  overlap=0.14
SALTOC, MA RHENIELEENE RIVERA         <-> SOBERANO, MARY LENILANE RIVERA               pct=30  B4  overlap=0.14
LIM, MICHELLE ALEXIS ARROYO           <-> CO, MICHELLE ALEXIS TAN                      pct=99  B10 overlap=0.33
VILLARUEL, ABIGAIL SAMARITA           <-> VILLANUEVA, ABIGAIL LUNAR                    pct=97  B10 overlap=0.2
CAYABYAB-MACANAS, FLORABELLE ROSE CALDEZ <-> QUERUBIN, FLORABELLE DEAUNA               pct=62  B7  overlap=0.14
ROXAS, REGINALD ERISE PASCUAL         <-> ROYALES, JOEY IBARRA                         pct=11  B2  overlap=0.0
TORNO, EDUARDO ESPINA                 <-> SORIANO, EDUARDO ONG                         pct=73  B8  overlap=0.2
SYSON, PATRICIA LETICIA RAMOS         <-> SUSON, PATRICIA LLANA PICARDAL               pct=96  B10 overlap=0.14
TIAM, HENRICSON CORPUZ                <-> TAN, KENNETH PHILSON CORPUZ                  pct=95  B10 overlap=0.17
VIEJA, DIANNE VICTORIA CANCINO        <-> VERGARA, IRENE VICTORIA OCAMPO               pct=78  B8  overlap=0.14
VERACRUZ, MARY ROSE ESTRELLA          <-> DELA CRUZ, DEANNE LOUISE ESTRELLA            pct=86  B9  overlap=0.12
CADAG, ELIZABETH ABRANTES             <-> CABRAL, ELIZABETH ABANES                     pct=81  B9  overlap=0.2
ANTONIO, MARYGRACE SALVADOR           <-> LABAYEN, MARY GRACE SALVADOR                 pct=10  B2  overlap=0.17
AHUJA, JAIKISHIN UTTMANI              <-> PYDI, MUKUND YADAV                           pct=14  B2  overlap=0.0
AHAMED KABEER, FATHIMA JIMLANI        <-> YAKOOB, SANJEEDH AHAMED                      pct=52  B6  overlap=0.17
VILLEZA, MARGARET ANN TINIO           <-> BITERA, MARGARET ANNE MAGNO                  pct=71  B8  overlap=0.14
DAZA, JESSICA CASTELO                 <-> DIAZ, JESSICA TOMULTO                        pct=49  B5  overlap=0.2
DURAL, PRECIOUS ANN MARIE GUMIRAN     <-> GARCIA, JURIS MARIE GUMIRAN                  pct=92  B10 overlap=0.29
ANG, ADRIEL VINCENT LIM               <-> TAN, JAMES VINCENT LIM                       pct=97  B10 overlap=0.33
```

Note that scores are spread across bands, not concentrated below the cutoff — 26 of these 36 sit at
or above B5 (40th percentile). This is a general identity-matching quality issue in `MANUAL_APPNO_MATCH`
records, not a phenomenon specific to low-scoring examinees.

---

## 5. Continuity with the old "4 genuine mismatches"

The old document's 4 records were AHUJA/PYDI, CASAO/CARLOS, ROXAS/ROYALES, LIAO/LIM.

- **AHUJA, ROXAS, and LIAO reproduce identically here** — all three are in the unresolved-36 list
  above. They were genuine mismatches then and remain genuine mismatches now, on a rigorous,
  no-manual-step run.
- **CASAO does not appear as either "clean" or "mismatch"** in this rewrite. It traces to the appno
  whose NMAT-side record is "Carlos, Norberto Jr. Ganzon" — the source file has **two** competing
  PLE-side name candidates for that one appno ("CARLOS, NORBERTO JR GANZON" and "CASAO, ROSALYN
  ABROGENA"). That is a genuine `ambiguous_source_conflict`, not a mismatch a name-parser can call
  either way — the old document's binary "wrong" verdict on it was itself an unscripted judgement
  call. It is listed in `forensic_audit_exceptions.csv` for human review.

---

## 6. Corrected headline

**Not "4 genuine mismatches."** Over the population actually checked in this rewrite (2,371 of
2,867 APPNO-based matches, 82.7% coverage):
- **36 unresolved `genuine_mismatch` records overall** (down from 55 before the normaliser).
- **10 unresolved in the low-score (<40th percentile) subset** (down from 13 before the normaliser),
  out of 475 low-score records checked.
- **491 records (17.1%) are entirely uncheckable** with any file in this repo and should not be
  assumed clean.

---

## 7. What is explicitly withdrawn

- **"4 genuine mismatches."** Not reproducible; required an undocumented manual override of 13 of
  the 17 records the old script actually flagged (see `forensic_audit/_superseded/README.md`).
- **"97.2% same-surname / 0.2% genuine mismatch" (system-wide, all accepted matches including
  EXACT).** That claim was computed against a `PLE_MATCH_MASTER.csv` snapshot covering only ~62% of
  the current parquet's EXACT-matched population and ~7 weeks stale. This rewrite does not restate a
  system-wide EXACT-match figure — see Section 0 for why EXACT matches are out of scope for a name
  cross-check in the first place.
- **Any claim that below-cutoff name mismatches are rare because so few were found.** The `36` and
  `10` figures above are counts within the **checked** population only (82.7% coverage); they are
  not, and are not claimed to be, a system-wide rate.
