# CHED Dashboard — Council Decision

## Consolidating the 5-Agent Debate

**Date:** 2026-07-27  
**Council:** CMO Advocate, Data Realist, Dashboard Designer, Integration Specialist, Quality Auditor  
**Documents:** IMPLEMENTATION_PLAN.md, REINTEGRATION_PLAN.md  
**Output:** `streamlit_dashboard/CHED_relevant_dashboard/`

---

## Council Verdict Summary

| Question | Consensus | Vote |
|----------|-----------|:----:|
| **Tab count** | 8–9 tabs (split 4-1 against 12) | ✅ 9 tabs |
| **Scope** | CMO-focused + essential context (not full original dashboard) | ✅ Confirmed |
| **No sidebar filters** | Agreed, but WITH in-tab controls (dropdowns) | ✅ Refined |
| **Must add executive summary** | Unanimous | ✅ Yes |
| **Must expand foreign/citizenship section** | Unanimous | ✅ Yes |
| **Must add gender metrics** | 4-1 in favor | ✅ Yes |
| **Drop subtest profiles tab** | Unanimous | ❌ Dropped |
| **Drop score bins background tab** | 3-2 in favor of merging into Cut-Off | ✅ Merged |
| **Verification before expansion** | Unanimous — Quality Auditor flag | ✅ Critical |
| **Fix "13_ched_compliance.md" labeling** | Data Realist flag — unanimous support | ✅ Critical |

**Overarching finding:** The IMPLEMENTATION_PLAN has the right architecture but is missing essential context. The REINTEGRATION_PLAN identifies the right gaps but over-scopes the solution. The correct path is the middle ground.

---

## Acceptance Criteria (Quality Auditor's Sign-Off Requirements)

The Quality Auditor identified 6 hard requirements for sign-off. The council accepts all 6:

1. **Phase A data integrity checks** — column-by-column verification
2. **Phase B spot-verifications** — manual confirmation of computed values
3. **Foreigner count discrepancy resolved** (32,501 → 24,079 documented)
4. **Cut-off numbers reconciled** between plan (~109K/94K) and computed (91K/79K)
5. **All edge cases documented** in a known-limitations register
6. **Caveats above the fold** on every dashboard tab

None of these 6 are met today. No code is written until the discrepancy is resolved.

---

## Immediate Action: Resolve the Foreigner Count Discrepancy

The Quality Auditor flagged: IMPLEMENTATION_PLAN says 32,501 Verifed Foreigners but computed output (`04_foreign_analysis.md`) shows 24,079. The Data Realist confirms this is a serious credibility risk if shown to CHED.

**Council finding:** The 32,501 is the ALL-RECORDS count (including repeat NMAT attempts). The 24,079 is the BEST-RECORD count (one examinee = one row). Both are correct for their respective denominators. The plan and dashboard must:
- Always state which denominator is being used (all records vs best-record)
- Default to best-record for person-level metrics (equity, demographics, performance)
- Use all-records only for volume/trend analysis (total applications per year)
- Never mix denominators in the same table or visualization

**Resolution:** Update IMPLEMENTATION_PLAN to use best-record counts for person-level metrics, with a note explaining the denominator choice. Both numbers are correct; the plan's headline was using the wrong denominator.

---

## Corrected 9-Tab Structure

```
Tab 1:  EXECUTIVE SUMMARY       ← NEW (was missing)
Tab 2:  NATIONAL BENCHMARK      ← EXISTING (from computation scripts)
Tab 3:  CUT-OFF SCENARIOS       ← EXPANDED (merge bin distribution + top/bottom trend)
Tab 4:  PER-HEI ANALYSIS        ← EXISTING (add UNI_TYPE filter, Philippine-only default)
Tab 5:  FOREIGN STUDENTS        ← EXPANDED (add citizenship comparison, heatmaps, box plots)
Tab 6:  PLE ALIGNMENT           ← EXPANDED (add box plots, course survival, bin × type)
Tab 7:  DEMOGRAPHICS + TRENDS   ← MERGED (gender + course + repeat takers + temporal trends)
Tab 8:  ACCOUNTABILITY FRAMEWORK ← NEW (PHEI risk flags, monitoring template, transition)
Tab 9:  DATA APPENDIX           ← EXISTING (expanded with edge cases, methodology)
```

**Dropped from REINTEGRATION_PLAN's 12-tab proposal:**
- ❌ Subtest Profiles tab (not CMO-actionable)
- ❌ Score Bins & Background tab (merged into Cut-Off Scenarios)
- ❌ Separate Trends tab (merged into Demographics)

---

## Computation Scripts: Revised Map

### Existing (verified, keep)
```
ched_compute/
├── config.py              ✅ Keep  
├── helpers.py             ✅ Keep  
├── 01_national_benchmark.py     ✅ Keep  
├── 02_cutoff_scenarios.py       ✅ Keep (extend with bin × year data)  
├── 03_per_hei_distribution.py   ✅ Keep  
├── 04_foreign_analysis.py       ✅ Keep (extend with citizenship comparison)  
├── 05_demographic_profiles.py   ❌ Rename → 05_gender_course_trends.py (expand scope)
├── 06_ple_alignment.py          ✅ Keep (extend with box plots + course survival)  
├── 07_temporal_trends.py        ✅ Keep (merge into demographics)  
├── 08_executive_summary.py      ✏️ NEW (from Reintegration Plan)  
├── 09_accountability_framework.py ✏️ NEW (risk flags, monitoring template)  
└── run_all.py                   ✅ Update to include new scripts  
```

### Key Extension: Foreigner Counts Must Be Denominator-Labeled

Every computation script that produces foreigner counts must output TWO numbers:
- **All-records count** (32,501 Verified Foreigners) — for volume/trend analysis
- **Best-record count** (24,079 Verified Foreigners) — for person-level demographics

Both are labeled clearly. The dashboard uses best-record as default with an option to switch.

---

## Mandatory Caveat System

Adopted from the Data Realist and Quality Auditor positions:

### Implementation: `render_caveat()` function

```python
def render_caveat(tab_name: str):
    """Display applicable caveats for the given tab. Always visible above the fold."""
    caveats = {
        "benchmark": "All PLE metrics on this page are NMAT-to-PLE linkage rates. "
                     "We CANNOT compute actual PLE pass rates — our dataset contains "
                     "only PLE passers, not all PLE takers. See Data Appendix for details.",
        "foreign": "All counts are NMAT EXAMINEES, not enrolled students. "
                   "The CMO's 10-slot cap applies to ENROLLMENT, which requires "
                   "data from HEIs that we do not have.",
        "cutoff": "Historical data (2006-2018). The CMO takes effect AY 2026-2027. "
                  "There is an 8-year data gap. Trends may not reflect current conditions.",
        "per_hei": "Per-HEI PLE linkage rates are NOT pass rates. "
                   "Do not use for CMO eligibility determination without validation "
                   "against actual PRC data.",
        "alignment": "Linkage rates measure association only. Not causal. "
                     "Higher NMAT scores correlate with higher PLE linkage, but "
                     "this does not mean raising cut-offs causes better outcomes.",
        "general": "NMAT data: 2006-2018. PLE data: 2011-2022. "
                   "Observable cohort (Year <= 2014) used for all PLE-linked summaries.",
    }
    c = caveats.get(tab_name, caveats["general"])
    st.warning(f"**Data Limitation:** {c}")
```

Every tab calls `render_caveat(tab_name)` as its second line of code (after the subheader). No exceptions.

---

## Implementation Sequence (Gated)

### Phase 0: Resolve Discrepancies (BEFORE any new code)

1. ✅ Reconcile foreigner count: document 32,501 (all records) vs 24,079 (best record)
2. ✅ Reconcile cut-off numbers: document 109K/94K (all records) vs 91K/79K (best record)
3. ✅ Update IMPLEMENTATION_PLAN with correct denominator-labeled numbers
4. ✅ Run Phase A data integrity checks on all 7 existing scripts

**Council gate:** Phase 0 must complete before Phase 1 begins.

### Phase 1: Verify Existing (BEFORE new scripts)

1. Phase B spot-verifications for all 7 existing scripts
2. Phase C consistency checks across scripts
3. Document all edge cases found
4. Fix any bugs discovered during verification

**Council gate:** All Phase B checks must pass before Phase 1a.

### Phase 1a: Fix Existing Scripts

1. `01_national_benchmark.py` — add best-record/all-records clarity
2. `04_foreign_analysis.py` — add citizenship comparison (bin heatmaps, box plots)
3. `05_demographic_profiles.py` → expand to `05_gender_course_trends.py`
4. `06_ple_alignment.py` — add box plot data, course survival, bin × type
5. `07_temporal_trends.py` — confirm merge target

### Phase 2: New Scripts

1. `08_executive_summary.py` — metric cards + pie charts + policy context
2. `09_accountability_framework.py` — risk flags, monitoring template, transition timeline

### Phase 3: Dashboard Build

1. Rewrite `dashboard.py` to 9-tab structure
2. Implement `render_caveat()` system
3. In-tab controls for: HEI search, year range, nationality filter
4. Metric cards with `help=` tooltips
5. Download buttons on every tab

### Phase 4: Quality Sign-Off

1. Independent human reviewer tests all 9 tabs
2. Caveat comprehension test
3. Performance test (128KB HEI table)
4. Quality Auditor signs off

---

## What CHED Actually Gets

### With Existing Data (Ready Now)

| Feature | Confidence | Limitation |
|---------|:----------:|------------|
| Cut-off scenario modeling (30th vs 40th) | ✅ High | Historical data (2006-2018) |
| Per-HEI NMAT score distributions | ✅ High | None |
| NMAT-PLE linkage rates | ✅ High | Not PLE pass rates |
| Foreign examinee counts & demographics | ✅ High | Examinees, not enrollees |
| Executive summary & context | ✅ High | None |
| Gender & demographic equity analysis | ✅ High | None |
| Temporal trends | ✅ High | Data ends 2018 |

### Cannot Support (Need New Data)

| Feature | What's Needed | Who Has It |
|---------|---------------|------------|
| PLE pass rates per HEI | PLE taker data (pass + fail) | PRC |
| 3-year compliance tracking | PLE pass rates + current data | PRC + CHED |
| 10-slot cap verification | Enrollment data from HEIs | HEIs |
| GIDA applicant identification | GIDA municipality boundaries | DOH/NSCB |
| IP applicant identification | IP membership data | NCIP |
| Composite ranking (60/40) | GWA/interview scores | HEIs |
| Current-year (2026) monitoring | Ongoing data pipeline | CHED |

---

## Council Signatures

| Agent | Position | Sign-off |
|:-----:|----------|:--------:|
| Agent 1 | CMO Advocate | ✅ The 9-tab, 8-script plan directly supports all 8 CMO operational requirements with honest proxies where direct data is unavailable. The accountability framework tab fills the monitoring gap. Minority position: would have preferred 7 tabs but accepts 9 as consensus. |
| Agent 2 | Data Realist | ✅ Conditional on: (a) all "PLE passing rate" language eradicated, (b) per-HEI enforcement table converted to descriptive linkage table, (c) `render_caveat()` on every tab above the fold, (d) foreign HEIs excluded from CMO enforcement context. |
| Agent 3 | Dashboard Designer | ✅ 9 tabs is the right number. In-tab controls accepted. ~500 lines new code, not 810. Executive summary first, narrative flow confirmed. |
| Agent 4 | Integration Specialist | ✅ Hybrid approach accepted. Existing scripts extended, not rewritten. 3 new scripts, not 5. Foreigners vs Filipinos comparison is the #1 value-add. |
| Agent 5 | Quality Auditor | ✅ **Conditional on Phase 0 and Phase 1 completing before any new code is written.** The discrepancies must be resolved and verifications passed. This council decision is the plan; execution must follow the gated sequence. |

**Council chair's note:** This decision represents the collective judgment of 5 independent reviewers. All agents agree that the dashboard should be built — but only after discrepancies are resolved, existing outputs are verified, and the caveat system is implemented. The council rejects both the "cannot build anything" pessimism and the "add everything from the original dashboard" scope creep. The middle path — 9 tabs, 8 scripts, honest labels, verified numbers — is the correct one.

---

*Council convened and concluded. Decision binding for all subsequent implementation work.*
