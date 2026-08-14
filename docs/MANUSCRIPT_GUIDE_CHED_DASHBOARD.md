# Manuscript Writing Guide — CHED Dashboard

This is a **writing guide, not the manuscript**. For each section it says what to discuss, which
CHED-dashboard tab/table/figure supplies the evidence, the specific numbers to cite, and the caveat
that must travel with the claim. Evidence source is
`streamlit_dashboard/CHED_relevant_dashboard/dashboard.py` (6 tabs) and its shared compute layer
`ched_common.py`, unless stated otherwise. All numbers were verified against
`dataset/NMAT_Exodus.parquet` (md5 `28b85ac53af13b4a2ef3ee93527c97c1`) on 2026-08-14; see
`docs/HANDOFF_TESTING_GUIDE.md` for the verification commands. The CMO text itself is
`docs/CHED_CMO.md`.

---

## 0. Scope ceiling — state this first, before any finding

**This dataset cannot evaluate the central mechanism of CMO §IV.B.1.** The CMO conditions a PHEI's
30th-percentile cut-off privilege on *that PHEI's own* PLE passing rate over the last 5 years
(§IV.B.1.b/c), with revocation after 3 consecutive sub-average years (§IV.B.2). This dataset has **no
medical-school identifier anywhere** — `UNDERGRAD_UNIVERSITY`, `UNDERGRAD_UNI_TYPE`, and
`UNDERGRAD_UNI_LOCATION` record the applicant's **undergraduate** institution, sat *before* the NMAT,
not the medical school that later trained them.

**Proof, not assertion:** UP Diliman has no College of Medicine — UP's MD program is run out of UP
Manila. Yet `UNDERGRAD_UNIVERSITY == "UNIVERSITY OF THE PHILIPPINES - DILIMAN"` appears on **4,421
rows, 1,914 of them confirmed PLE passers**. Those 1,914 people cannot have earned their MD at an
institution that does not run the program. `CourseGroup` for these rows confirms the mechanism —
Education (316), Engineering & Technology (37), Social & Behavioral Sciences (819): bachelor's
fields, sat before medical school, not medical curricula.

**Say the following plainly, in the opening section, before anything else:** *this dataset can
characterise the NMAT applicant pool against candidate percentile thresholds, and it can measure
whether applicants at each threshold later appear as PLE passers — but it cannot measure any
institution's PLE performance, cannot evaluate any PHEI's eligibility for the 30th-percentile
privilege, and cannot support a compliance or revocation decision under §IV.B.1.b/c or §IV.B.2.* Not
"partially," not "with caveats" — the identifier that provision requires does not exist in any column
of `NMAT_Exodus.parquet`.

**Evidence:** `dashboard.py` Tab 4 header caption + `SCOPE_NOTE` (repeated on Tabs 2–6); Tab 6 card 6
("PHEI Accountability and Sanctions") states this most explicitly: *"No PHEI, SUC, or any other
institution-level PLE performance, compliance label, or risk rating can be computed from any column
in this file."*

---

## 1. Data and Methods — per-pipeline data-quality narrative for a policy reader

A policy reader needs to trust the numbers because of the corrections below, not despite them.
Present each as: what was wrong, why it mattered for this specific CMO question, what was fixed.

### 1.1 Pipeline 1 — score integrity

The CEM-supplied `StoredRawTotal` disagreed with the sum of the 8 component subtest raw scores in
**56,065 of the 99,316 records carrying a stored total (56.45%)** — never cite "42.2%," an older
figure that divided the mismatch count by the wrong denominator (a unique-examinee count instead of
the stored-total-bearing row count). `TotalRawScoreTRUE`, recalculated from the 8 components, is the
canonical value and is arithmetically exact (0 mismatches across 178,882 non-null rows). Every
percentile-based threshold discussed in this brief — B4 (30th percentile), B5 (40th percentile) —
derives from `NMS_PER_num`, which is downstream of this corrected score, not the disputed stored
total. State this once, early, so every subsequent percentile-bin claim inherits the reader's trust in
it.

### 1.2 Pipeline 2 — PLE matching, and why this is the most policy-relevant pipeline in the repo

This is the pipeline that decides who counts as a "confirmed PLE passer," which is the numerator of
every linkage statistic this brief cites. Two defects were found here during remediation, and **both
are directly relevant to the CMO question being evaluated**, because both concerned the exact
population the CMO threshold targets:

**RC-0.** `disambiguate()` — the routine invoked whenever a name matches more than one NMAT record —
had a hard filter (not a tie-break) that discarded every name-collision candidate scoring below the
**40th percentile**, and rejected the match outright if every candidate fell below it. **The constant
was 40 — exactly the CMO §IV.A.1/§17.5 threshold this brief exists to inform.** The pipeline that
generates the evidence had, built into it, the exact policy assumption under review: that people below
40 don't matter enough to match. This was discovered during remediation, not in the original 12-agent
audit, and it inverted the direction of the resulting bias — the below-40 linkage figures this brief
now reports were previously **artificially suppressed** by the matcher itself, not just by admission
selection (§3 below).

**O-24.** The documented DOB/identity check — supposedly the backbone of the disambiguator — never
actually ran in any historical execution: `BDATE_CLEAN` was constructed *after* the row-dict snapshot
the matching function reads, so the birthdate filter silently no-opped and the pipeline fell through to
weaker identity evidence every time, which is part of why the percentile floor above was doing so much
unintended work.

**Both are now fixed.** Confirmed passers moved **49,986 → 49,086** — some previous winners are now
correctly flagged ambiguous and dropped, while others whose entire name-collision group scored below
40 are newly matched. **Every number in this brief reflects the corrected matcher.** State this
explicitly wherever a below-threshold linkage number appears, so a reader understands the number is
not merely "low because of admission policy" but specifically "low despite a matching-pipeline
correction that, if anything, raised it."

**Identity-key caveat, always disclosed with any person-level count:** `PERSON_KEY` merges surname +
given names + a coarse birthdate field; **6,148 keys (4.56%) carry contradictory SEX**, the minimum
detectable rate of two different people sharing a key. Flagged as `PERSON_KEY_AMBIGUOUS`, included in
every count, never silently removed.

### 1.3 Pipeline 4 — citizenship, for the §IV.A.2 foreign-applicant provisions

3-tier hierarchy: Tier 1 (`REAL_FOREIGNERS.csv`, ground truth) → Tier 2 (name-based inference,
disclose as an estimate, not a confirmation) → Tier 3 (default Filipino). `FOREIGNER_STATUS ==
"Verified Foreigner"` is Tier-1-backed and safe to cite with confidence for descriptive purposes; a
"Likely Foreigner" or any Tier-2-only figure should never be presented with the same certainty.
**Neither tier tells you anything about enrolment** — this dataset records NMAT examinees, not
enrolled or matriculated students, so it cannot speak to §IV.A.2.a's 10-foreign-slot enrolment cap at
all (the cap is also not yet in effect for the historical years this dataset covers — it takes effect
AY 2026–2027).

### 1.4 Pipeline 5 — reproducibility infrastructure

Brief, factual mention only: the 118→53-column slim step and the byte-identical three-copy guarantee
(`dataset/`, both dashboard folders, one md5) mean the CHED dashboard and the main dashboard can never
silently diverge on *source data* — any remaining disagreement between the two is a computation
difference, worth investigating, not a data-freshness difference.

---

## 2. Results — mapped to CHED tabs and CMO provisions

| CMO provision | Data support | Verdict | Evidence tab |
|---|---|---|---|
| §IV.A.1 — SUC 40th-percentile floor (Filipino) | Percentile ✓, citizenship ✓, SUC identity ✗ | **Partial** — describable for applicants, not by institution | Tabs 2, 3 |
| §IV.A.1 — 30–39th band for GIDA/IP | No GIDA, IP, residence, or SES field exists | **Not answerable** | Tab 6 |
| §IV.A.2.a — cap foreign enrolment at 10/class | Citizenship ✓, enrolment ✗ | **Not answerable** — examinees, not enrollees | Tab 4, 6 |
| §IV.A.2.b — composite 60/40 or 70/30 ranking | No GWA, interview, or other criteria | **Not answerable** | Tab 6 |
| §IV.B.1 — PHEI floor ≥30th percentile | Percentile distribution ✓ | **Answerable at applicant level** | Tabs 2, 3, 5 |
| §IV.B.1.b/c — privilege conditioned on PHEI's own 5-yr PLE rate | No med-school identifier; no institutional PLE denominator | **Not answerable — the central mechanism** | §0 above; Tab 6 card 6 |
| §IV.B.2 — revocation after 3 sub-average years | Same as above | **Not answerable** | Tab 6 |
| §VI — monitoring | — | Out of scope | — |

### 2.1 Tab 1 — National Profile

**What to discuss:** the size and shape of the applicant pool this entire brief describes — volume by
year, undergraduate composition, repeat-taker context, and the score-bin reference table that every
later section assumes the reader already understands (**B1 = lowest decile 0–9, B10 = highest
90–99**, B4+ = the CMO exception floor (30th–39th), B5+ = the current SUC standard floor (40th–49th)).

**Numbers:** best-record examinees 134,869 (unique persons, equal by construction); 13 years covered;
median NMAT percentile 50.0; repeat takers 33,713 (25.0% of unique examinees, with the identity-key
caveat from §1.2 attached).

**Caveat:** none beyond the identity-key note already stated.

### 2.2 Tab 2 — B4+ vs B5+ Thresholds

**What to discuss:** how many applicants meet each of the two thresholds the CMO is choosing between,
and the "public-institution examinees and the B5+ threshold" descriptive block — the closest thing to
a §IV.A.1/§IV.B.1 applicant-pool answer this dataset can give.

**Numbers:** 65.2% of public-undergraduate-institution examinees (17,752 of 27,234) already score at
or above B5+ (the current 40th-percentile floor); only 8.3% (2,247) fall in the B4-only band the CMO's
30th-percentile exception would newly admit. Private-undergraduate examinees meeting B5+: 60,184 of
101,400 (59.4%). The **B5+ PLE-status-by-year stacked bars** must show a genuine, non-zero
"no confirmed match" series in most years — this is the tab where the tautological-chart bug (§4
below) was most visible before the fix, so it is worth an explicit sentence confirming the chart is
now honest.

**Caveat, mandatory here specifically:** "public undergraduate institution" is **not** equivalent to
"SUC" as the CMO uses the term (§0). No claim about who would benefit from the CMO's GIDA/IP exception
can be supported here — that field does not exist.

### 2.3 Tab 3 — PLE-Passer Linkage

**What to discuss:** the individual-level linkage-by-bin gradient — the single relationship this
dataset can speak to most directly and honestly — plus the stress-test subset that exists specifically
to prove the linkage figures are not tautological.

**Numbers (corrected, post RC-0/O-24 fix):**
```
B1 11.6%  B2 22.7%  B3 29.3%  B4 36.0%  B5 45.6%
B6 50.4%  B7 53.6%  B8 55.0%  B9 61.6%  B10 71.0%
```
Stress test: restricting to confirmed passer + PLE year gap ≥5 years + Filipino nationals + B5+ band
gives **56.0% (23,128 of 41,289)** — genuinely below 100%, which is the point: a tautological check
cannot show anything but 100%, and this one doesn't.

**Caveat — the selection-effect confound, mandatory every time this gradient supports a policy
argument:** the gradient rises smoothly with no sharp step at either the 30th or 40th percentile
boundary — corrected step sizes are B4→B5 +9.6, comparable to B1→B2 (+11.1) and B9→B10 (+9.4), not an
outlier. But low-bin examinees were also **partly never admitted** to medical school under the
historical non-uniform school-level cutoffs actually applied 2006–2014 — their low linkage rate is
confounded with non-admission, not purely with post-admission outcome. **This gradient cannot be used
to estimate how many additional passers a new uniform cutoff would produce or exclude.** State this in
the same breath as the gradient, not in a separate limitations paragraph a reader might skip.

### 2.4 Tab 4 — Institution and Foreign Context

**What to discuss:** score summaries by undergraduate institution type, framed explicitly as applicant
origin (§0), plus the foreign-examinee profile relevant to §IV.A.2.

**Numbers:** Public median percentile 57, Private 49, Foreign 52 (best-record, valid-bin population).
Verified foreign examinees, best-record: 24,069; distinct nationalities 89; top nationality **India,
19,090, 79.3%** of the 24,069 verified-foreign denominator — always the full denominator, never a
top-N subtotal (an earlier draft of this brief computed India's share against only the top-10 subtotal
and overstated it; the shared-compute-layer fix in `ched_common.py`'s `compute_nationality_shares()`
exists specifically to prevent that regression).

**Caveat:** these are undergraduate-origin comparisons (§0), and citizenship counts describe
examinees, not enrolled students — cannot speak to §IV.A.2.a's enrolment cap.

### 2.5 Tab 5 — Key Evidence for Policy Review

**What to discuss:** this tab is pure narrative — 8 synthesized findings. Use it as the manuscript's
own findings-section skeleton rather than re-deriving new framings; each finding already carries its
correct caveat inline (national threshold context, undergraduate-origin framing, the linkage gradient
with the selection-effect note, the below-40-not-uniformly-binding finding, historical trend, the
public-institution descriptive note, the matching-sensitivity check, foreign-examinee presence).

**Caveat:** reproduce these findings' caveats verbatim (Rule 5 of the export contract — narrative
claims are exported/quoted exactly as rendered, not paraphrased) rather than tightening or loosening
their hedges in translation to manuscript prose.

### 2.6 Tab 6 — Data, Methods, and Limitations

**What to discuss:** treat this as the manuscript's own limitations section source material — it is,
per the audit, "the best content in the repository" for this purpose. Cards worth lifting near-verbatim:
GIDA/IP absence, enrolment vs examinee distinction, the foreign-slot-cap timing mismatch (cap takes
effect AY 2026–2027, this data is 2006–2018), composite-ranking data absence, and — most
importantly — card 6's unambiguous statement that no institution-level PLE performance can be computed
at all.

**Numbers:** stored-vs-derived mismatch, restated here for the methods audience: 56,065 of 99,316
(56.5%).

---

## 3. The supportable headline finding

**6,173 of 25,596 below-40th-percentile observable examinees (24.1%) are confirmed PLE passers — 795
of them in B1, the lowest decile.** This is the most direct evidence this dataset can offer on the
CMO §IV.B.1 question of whether the floor should drop from 40 to 30: under the *existing* 40th-percentile
rule, a substantial number of people scored below it anyway and went on to pass licensure.

**Why it survives the obvious objections — state all three, they are what make the number
defensible:**

| Objection | Check | Result |
|---|---|---|
| "Name-collision artefacts" | `PERSON_KEY_AMBIGUOUS` rate among the 6,173 | **3.0%** — *below* the 3.5% cohort base rate |
| "Foreign students under different rules" | citizenship | **6,152 of 6,173 are Filipino** |
| "One anomalous year" | year spread | present in **all nine** observable years (2006–2014) |

**Caveats that must travel with this number every time it is cited:**
1. **Linkage, not pass rate.** 24.1% is the share confirmed-linked to a passer record; the PLE source
   is passers-only, so this is a floor on the true rate, not a completion rate. "Not linked" is never
   "failed."
2. **"Below 40" means at the best attempt within the observable window** — some of these people may
   have exceeded 40 on a later attempt outside that window.
3. **It does not, by itself, establish that lowering the floor is advisable.** It establishes that
   below-40 admission already occurred at scale historically and produced licensed physicians. The
   admission-selection effect (§2.3) still applies — these are people who were admitted *despite* the
   existing rule, and they may differ systematically from the below-40 population as a whole (which
   includes people who were never admitted and therefore cannot appear in this figure at all).

**Evidence:** Tab 3's linkage-by-bin table plus the below-40 aggregate (not directly displayed as one
number anywhere in the current dashboard — compute it as `sum(linked_n for B1..B4)` from Tab 3's
table, or cite this guide's verified figure directly). Tab 5 finding 4 and Tab 6 card 8 both carry the
"not uniformly binding" framing this number supports.

---

## 4. Claims that were withdrawn and must not be repeated

An earlier draft of this brief's flagship finding was a **21-point "policy discontinuity"** between
bin B4 and bin B5 in the linkage gradient — precisely at the 40th percentile — used to justify a
regression-discontinuity design as the headline recommendation for further work. **This finding was
withdrawn.** After the RC-0 fix (§1.2) removed the matcher's own hard 40th-percentile floor, the
corrected B4→B5 step is **9.6 points**, statistically unremarkable against the other eight bin-to-bin
steps (B1→B2 is +11.1, B9→B10 is +9.4). The sharp discontinuity that motivated the regression-
discontinuity recommendation was **largely an artefact of the project's own matching code**, not
evidence of a real admission-policy break at the threshold.

**Also withdrawn, same root cause:** any statement that the below-40 linkage collapse is "purely" or
"primarily" an admission-selection effect. It is a real effect (§2.3), but before RC-0 was fixed, part
of the apparent collapse was the matcher refusing to try. The corrected, defensible finding is §3
above, not the discontinuity story.

**Do not resurrect either framing in a new draft, a slide, or a follow-up brief.** If asked why an
earlier version made these claims, the honest account is: both were byproducts of a bug in the
identity-matching pipeline (the exact same constant, 40, that this CMO amendment is evaluating), found
during remediation and corrected before this brief's current numbers were computed. That is itself a
useful methodological note for a policy audience — it demonstrates the analysis's self-correction, not
a reason to hide the history.
