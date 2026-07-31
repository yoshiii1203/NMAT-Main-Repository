# Audit 11 — CHED Scope, Stakeholder Fit, and Published Brief

Scope: `docs/CHED_CMO.md`, `streamlit_dashboard/CHED_relevant_dashboard/{dashboard.py, export_markdown.py, complete_markdown/*, Plan_1_Ched_Dashboard_Revision.md, README.md}`, `docs/data_dictionary.md`. All parquet figures independently recomputed with `./.venv/Scripts/python.exe` against `streamlit_dashboard/CHED_relevant_dashboard/NMAT_Exodus.parquet` (byte-identical to the other two copies per `_SHARED_CONTEXT.md`).

## Verdict

**Needs rework** — not withdraw-and-redo, but not shippable as-is either.

The brief's *discipline* is genuinely good: it repeatedly says "not a PLE pass rate," explicitly disclaims GIDA/IP, enrollment, GWA/composite-ranking, and institution-level compliance determinations, and never issues a regulatory recommendation. That restraint is exactly what the user asked for and is worth preserving. But the brief's single most rhetorically load-bearing exhibit — the "clean-subset stress test" (§3.4, Figure 4) that is offered as proof the headline B4→B5 finding is "robust" — is built on a circular computation that is mathematically guaranteed to show ~100% linkage regardless of whether the underlying match quality is good or bad. That is not a robustness check; it is a tautology, and it is presented to policymakers as evidence. In addition, one displayed number (foreign-nationality "share of verified foreign," 85.1%) is calculated against the wrong denominator and is off by 3.6 points for every row in that table; a headline population denominator (130,818) does not reproduce from the current parquet; and the brief states a repeat-taker rate to a false precision that is wrong at that precision (25.0% stated vs. 25.2% actual). None of these individually would mislead a policy decision, but "verify every number" is the standard for a document titled "CHED Policy Brief," and four of roughly a dozen checkable figures fail exact reproduction. That, combined with the circular stress test, moves this from "needs-caveats" to "needs-rework": fix the stress-test logic, fix the two computation bugs, reconcile the stale denominator, and add one explicit paragraph on why the linkage gradient cannot support inference about the *proposed* cutoff — then it is defensible.

---

## 1. Requirements traceability matrix

Extracted from `docs/CHED_CMO.md` §IV (the operative amendment text).

| # | Requirement (CMO §IV) | Data support | Addressed in brief? | Verdict |
|---|---|---|---|---|
| A.1 | SUC Filipino: 40th percentile floor maintained; Boards may set higher | **Full** — `PercentileBin`/`NMS_PER_num` directly measure this | Yes — §4.1, "17,482 of 26,937 (64.9%) already meet B5+" | Defensible. Purely a descriptive attainment stat; no claim about what Boards *should* do. |
| A.1 | SUC 30th–39th exception for GIDA/IP with NCIP/DOH/LGU certification | **None** — no GIDA/IP/residency field in the 54 columns | Yes, explicitly disclaimed — §4.2 "cannot determine how many B4-only examinees could satisfy the documentation requirement" | Correctly restrained in the PDF. (Caveat: the *live* `dashboard.py` Tab-5 finding5 string — not exported to the PDF — adds "This suggests the exception may not primarily benefit the intended disadvantaged groups," which is an interpretive claim the PDF itself avoids. See §7 below.) |
| A.2.a | SUC foreign enrollment capped at 10 slots/class, AY2026-27 | **None** — dataset ends 2018 examinees, records examination not enrollment/admission | Yes, explicitly disclaimed — §4.4 "does not record admission decisions, actual enrollment... cannot assess compliance with the 10-slot cap" | Correct restraint. |
| A.2.b | Composite/weighted ranking (60/40, 70/30 NMAT + GWA/interview) for foreign applicants | **None** — no GWA, interview, or other non-NMAT admission variable | Yes, disclaimed — §4.4 | Correct restraint. |
| B.1 | PHEI cut-off ≥30th percentile *only if* 5-yr PLE pass rate above national average; else 40th floor | **Partial** — dataset has NMAT-to-PLE-passer *linkage* by bin/UNI_TYPE, not PHEI-level PLE *pass rates*, and has no "national average PLE pass rate" benchmark (PRC data not in scope) | Yes, disclaimed — §4.3 "does not calculate PHEI-level PLE passing rates, compare institutions with a national five-year benchmark... cannot determine which PHEIs meet the proposed condition" | Correctly restrained in prose, **but** the adjacent linkage-gradient exhibit (§3.2) is offered as the nearest available evidence for exactly this question, and it has the methodological problems in §3 below. The restraint is correct; the supporting exhibit needs a sharper caveat. |
| B.2 | Revocation of 30th-percentile privilege after 3 consecutive years of below-average PLE performance | **None** — same as B.1, plus requires multi-year institutional tracking absent from the data | Implicitly, via the general "no institution-level compliance labels" limitation (Tab 6, "PHEI Accountability and Sanctions") | Adequately covered, though never named as its own line item. Low-severity gap — add one explicit bullet. |
| VI | Annual monitoring via NMAT cut-off implementation review, PLE performance review, institutional audit | N/A — process commitment, not a data question | The dashboard/brief itself is a candidate input to this process | N/A |
| — | GIDA/IP documentation (NCIP cert, DOH/LGU cert) | **None** | Disclaimed, §4.2 / Limitations | Correct. |

**Summary:** every requirement that the data cannot support is explicitly and correctly disclaimed in the PDF text. No provision is answered with data the dataset doesn't have. This is the brief's real strength and should not be lost in a rewrite.

---

## 2. Number-by-number verification of the PDF brief

All values independently recomputed from `NMAT_Exodus.parquet` (178,927 rows) using the same filter logic as `dashboard.py` (`IS_BEST_NMAT_RECORD==True` → `df_best`; `Year<=2014` → `df_obs`; boolean-as-string normalization for `IS_BEST_NMAT_RECORD`/`IS_PLE_ANALYSIS_SAFE` per `dashboard.py:88-93`).

| # | Brief location | Displayed | Computed | Match? |
|---|---|---|---|---|
| 1 | p.2, Data Foundation | 133,804 best-record; 133,558 distinct PERSONKEY | 133,804 / 133,558 | ✅ |
| 2 | p.2 | 33,713 (25.0%) repeat takers | 33,713 (**25.24%**) | ❌ **False precision.** `.0f`-rounded "25%" (as shown in the dashboard/complete_markdown) is defensible; the PDF's explicit one-decimal "25.0 percent" is wrong at that precision — true value rounds to 25.2%. |
| 3 | p.2 | 42.2% CEM stored-total mismatch (107,422/254,308) | Not independently reproducible from Exodus parquet (pre-merge CEM population); consistent with `data_dictionary.md`. Note: within the Exodus subset that actually carries `StoredRawTotal` (99,316 rows), the mismatch rate is **56,065/99,316 = 56.5%**, materially higher than the cited 42.2%. Both are "true" of different populations, but the brief cites only the lower, CEM-wide figure. | ⚠️ Not wrong, but selectively favorable; should disclose both or explain the denominator. |
| 4 | p.3, §3.1 | "Among 130,818 best-record records with a valid percentile bin" | **130,735** (133,804 best-record minus 3,069 with null `PercentileBin`) | ❌ **Fails to reproduce.** Off by 83 records (0.06%). Percentages (69.9%/60.4%/9.5%) still round the same either way, so no downstream number is wrong, but the stated denominator itself does not match the current parquet — evidence of a stale snapshot or an intermediate join difference between whatever generated the PDF and the live data. |
| 5 | p.3, Table 3.1 | B4+ 91,409 (69.9%); B5+ 78,944 (60.4%); B4-only 12,465 (9.5%) | 91,409 / 78,944 / 12,465 — exact match on counts | ✅ (percentages unaffected by finding #4) |
| 6 | p.4, Table 3.2 | Linkage by bin: B1 6,104/505/8.3% … B5 6,229/2,882/46.3% … B10 9,657/7,352/76.1% | Reproduced exactly, all 10 rows | ✅ |
| 7 | p.4 | "B4→B5 linkage increase of 23.4 pp" | 46.3−22.9 = 23.4 | ✅ |
| 8 | p.5, Table 3.3 | Public 26,937/19,709(73.2%)/17,482(64.9%)/2,227(8.3%); Private 100,584/69,504(69.1%)/59,546(59.2%)/9,958(9.9%); Foreign 1,862/1,285(69.0%)/1,109(59.6%)/176(9.5%); Not Specified 1,352/911(67.4%)/807(59.7%)/104(7.7%) | Reproduced exactly, all four rows, all columns | ✅ |
| 9 | p.5 | Observable-cohort linkage: Public 50.1%, Private 44.7%, Foreign 22.1% | 50.1% / 44.7% / 22.1% | ✅ |
| 10 | p.6, §3.4 | Clean subset (all bins) 27,151; B5+ in clean subset 23,357; share of observable cohort 36.2%; median gap 6 yrs | 27,151 / 23,357 / 36.2% / 6.0 yrs | ✅ |
| 11 | p.6, §3.4 | "15 of 29,258 deduplicated confirmed PLE-passer best-records (0.1%) had a data-quality flag" | Traced to `forensic_audit/forensic_audit_report.md` (a separate, legitimate audit): 29,273 raw best-record-observable PLE matches contain 15 excess rows from a duplicate-flagging bug, net 29,258. Reproduced exactly (29,273 → 15 excess → 29,258). | ✅ figure itself is right, **but see Consistency §5** — the brief's own Tab 6 headline metric ("Confirmed PLE passers, best record, observable: 29,273") is never corrected for the bug the brief's own §3.4 cites two pages later. |
| 12 | p.6, Figure 4 | Yearly linkage-rate line, clean B5+ subset, visually flat at ~100% across 2006–2014 | **Exactly 100.0% every year, by construction** — see §3 below | ❌ **Not a valid statistic.** The chart cannot show anything but 100%, for any input data, good or bad. |
| 13 | p.6, §3.5 / p.7 Table | Verified foreign 32,501 (18.2% of 178,927); Filipino 146,413 (81.8%); Foreign UNI_TYPE best-record 1,894 (1.4%) | 32,501 (18.17%→18.2%) / 146,413 (81.83%→81.8%) / 1,894 | ✅ |
| 14 | p.6–7, §3.5 + Figure 5 | India 26,490 **(85.1%)**; Nepal 1,158 (3.7%); Thailand 1,062 (3.4%); USA 839 (2.7%); Nigeria 639 (2.1%) | Counts match exactly. **Percentages do not**: correct share of all 32,501 verified foreigners is India **81.5%**, Nepal 3.6%, Thailand 3.3%, USA 2.6%, Nigeria 2.0% | ❌ **Confirmed computation bug**, not rounding. Root cause: `export_markdown.py:631` computes `top_nat["Count"] / top_nat["Count"].sum()`, i.e. each nationality's share of the **top-10 subtotal (31,116)**, not of all 32,501 verified foreigners. Every row in that table is inflated by the same factor (31,116/32,501 ≈ 1.0426×). This is the single clearest arithmetic error in the published brief. |
| 15 | p.7, §4.1 | "17,482 of 26,937 Public-institution examinees (64.9%)" | 17,482/26,937 = 64.90% | ✅ |
| 16 | p.7, §4.2 | 2,227 B4-only Public examinees, 8.3% of Public best-record | 2,227/26,937 = 8.27% | ✅ |

**Net: 4 of 16 checkable claims fail exact verification** (false precision on repeat-taker rate; stale denominator in §3.1; a genuinely wrong percentage column for foreign nationalities; and a tautological figure that isn't a real statistic at all). Everything else — every count, and every percentage derived from a correctly-computed count — reproduces exactly from the current parquet.

---

## 3. The cut-off counterfactual — methodological assessment

### 3.1 What the brief actually computes
`PLE-passer linkage rate(bin) = confirmed_PLE_matches(bin) / all_NMAT_examinees(bin)`, restricted to the observable cohort (`Year<=2014`). This is **not** conditioned on medical-school admission — the denominator is all NMAT *examinees*, not admits — so it is not a classic post-admission selection/collider setup in the narrowest sense. But it is still conditioned on an unobserved and highly selective chain of events: admission (at *some* school, under *that* school's actual historical cutoff, which the CMO amendment does not set — schools already varied), persistence to graduation, sitting the PLE, passing it, and being successfully name/AppNo-matched back into this dataset. None of those five steps is visible in the 54 columns; only the joint success/failure of the whole chain is observable, as a single binary ("confirmed" vs "not confirmed").

**Direction of bias for any inference about the proposed cut-off:** the "linkage rate by bin" gradient (8.3% at B1 rising to 76.1% at B10) is real and internally consistent, but it describes people who lived through a *different*, non-uniform historical admissions regime, not the world the CMO amendment would create. It cannot be used, and to its credit the brief does not explicitly claim it can be used, to answer "if we set the cutoff at 40 instead of 30, how many additional future PLE passers would be excluded." That number is fundamentally unobservable from this dataset because the people who were **rejected** below whatever cutoff their target school actually used are simply absent from the NMAT examinee pool's downstream outcomes — they show up as "no confirmed match," indistinguishable from admitted-but-failed, admitted-but-not-yet-tested, or admitted-passed-but-unmatched-by-name.

### 3.2 Is the missing counterfactual acknowledged?
Partially. The brief states in multiple places that linkage "is not a PLE pass rate" and that the dataset "does not identify all PLE takers or failures" (Limitations, p.8-9; complete_markdown Tab 6). That is the right instinct, and it does prevent the most egregious misreading ("X% of people below the cutoff failed the boards"). But it never states the *more specific* problem: that the linkage-by-bin gradient is a description of an already-admitted, already-selected population under the *old*, non-uniform cutoffs, and therefore cannot be extrapolated to predict the effect of a *new*, uniform cutoff. A reader could still walk away from §3.2/§4.3 believing "B4 has much lower linkage than B5, so raising the cutoff from 30 to 40 wouldn't cost us many future doctors" — which is exactly the causal claim the brief's own restraint elsewhere shows it is trying to avoid. **This needs one explicit paragraph**, something like:

> *"The linkage gradient describes examinees who were already admitted under the historical (non-uniform, generally more permissive) cutoffs actually applied by individual schools between 2006 and 2014. It cannot be used to estimate how many additional PLE passers a uniform 30th- or 40th-percentile floor would have produced or excluded, because examinees who were not admitted anywhere under a school's then-current cutoff never appear in this dataset's downstream outcomes at all. Any statement inferring the effect of the proposed cutoff from this gradient would be extrapolating beyond what the data can support."*

### 3.3 Is the full 2×2 presented, or only the eye-catching cell?
The brief presents one margin well: for each bin, N and confirmed-PLE-passers (Table 3.2), which is effectively a full row-wise 2×2 (linked vs. not-linked, by bin) with both counts shown, not just the percentage. That is good practice and better than most such briefs. What is **not** presented, and would be the actually decision-relevant framing, is the complementary question: *of eventual confirmed PLE passers, what fraction scored below each candidate cutoff?* (i.e., 1 − sensitivity of the cutoff as a predictor of "will become a confirmed passer"). That number is directly computable from the same table and is arguably more relevant to a cutoff decision than "linkage rate by bin" is, because it answers "how many of the people we know succeeded would this cutoff have screened out" rather than "how likely is someone to succeed given they cleared the cutoff."

Recomputed from Table 3.2 (independently, from the parquet): of the 29,273 observable confirmed PLE passers, **1,312 (4.5%) scored in B4**, and **505+830+997 = 2,332 (8.0%) scored below B4 (bins B1–B3)**. So roughly 12.5% of everyone in this dataset who is known to have become a confirmed PLE passer scored below the proposed 40th-percentile floor at NMAT time — including 8.0% who scored below even the 30th-percentile exception floor. This is a genuinely CHED-relevant number (it directly measures how many known successful examinees a stricter uniform floor would have screened out, among people we can actually observe) and it is nowhere in the brief. It would need the same "not admission-conditioned, not a full counterfactual" caveat as everything else, but it is a real, computable, decision-relevant statistic that the current brief misses in favor of the one-directional gradient.

### 3.4 "Not matched" vs. "failed the PLE"
The brief does not conflate these in its prose — it says so explicitly and repeatedly (p.4, p.6, p.8-9, and complete_markdown Tab 3 / Tab 6). This is one of the brief's genuine strengths and should be preserved in any revision.

### 3.5 Is the right metric being used?
No, and the brief implicitly acknowledges this by never trying to compute sensitivity/specificity/PPV/NPV or an ROC curve — which is the *correct* choice given the data (a true ROC-style analysis needs observed failures and observed non-admits, neither of which exists here). The problem is not that the brief fails to run an analysis it should run; the problem is that **it doesn't say why it isn't running it**, leaving readers to assume the linkage gradient is the closest available substitute for such an analysis, when it is not a substitute at all — it answers a different question (P(success | admitted, above bin X)) than the one a cutoff decision needs (something like P(would have succeeded | applicant, whatever bin) or the false-exclusion rate at each candidate threshold). §3.3 above gives one computable, honest partial-answer (share of known passers below each threshold); recommend adding it plus the explicit caveat from §3.2.

### 3.6 The "clean-subset stress test" is circular — this is the most important finding in this audit
`dashboard.py:191-197` builds `_df_clean_ple` by filtering `df_obs` to `IS_PLE_ANALYSIS_SAFE == True` **first**, then computes, on that already-matched-only subset, a "linkage rate" (`dashboard.py:200-210`, `_clean_ple_yr`) whose numerator (`confirmed = HAS_CONFIRMED_PLE.sum()`) is defined from the very same `IS_PLE_ANALYSIS_SAFE` column used to build the subset. Every row therefore has `confirmed == total` and `no_match == 0`, for every year, by construction — independent of whether the underlying PLE matches are actually correct. Confirmed by direct execution:

```python
_df_clean_ple = df_obs[(df_obs["IS_PLE_ANALYSIS_SAFE"]==True) & (df_obs["PLE_YEAR_GAP"]>=5) & (df_obs["FOREIGNER_STATUS"]=="Filipino")]
# HAS_CONFIRMED_PLE was already set to (IS_PLE_ANALYSIS_SAFE==True) on df_obs before this filter
# => within _df_clean_ple, HAS_CONFIRMED_PLE is True for 100% of rows, tautologically
```
Output (`streamlit_dashboard/CHED_relevant_dashboard/complete_markdown/CHED_NMAT_Dashboard_Complete.md:247-259` and `359-369`): every single year, 2006–2014, shows `no_match = 0`, `linkage_pct = 100`. The PDF brief's Figure 4 (p.6) visibly renders this as a flat ~100% line and the surrounding text calls it a test of "whether the main results are sensitive to match quality." **It cannot fail this test no matter how bad the underlying matching is**, because "not matched" was defined out of the sample before the rate was computed. The brief's own conclusion (p.9) then states "the clean-subset analysis supports the robustness of the principal B5 pattern under stricter matching conditions" — this sentence is **unsupported by the exhibit that is supposed to back it**.

This does not mean the underlying PLE matching is bad — the separate `forensic_audit/` suite (audited by other agents in this fleet) provides genuine, non-circular evidence on match quality. It means this *specific* exhibit, presented in a CHED-facing document as a robustness check, provides zero information either way, and should not be represented as evidence of robustness.

**What a real fix looks like** (does not require new data): compute the "total" denominator from the strict-criteria-*eligible* population (best-record, Filipino, ≥5-year window since NMAT) **without** first requiring `IS_PLE_ANALYSIS_SAFE==True`, then measure what fraction of that population is matched. That produces a genuine (if still imperfect) sensitivity-style check of whether restricting to the cleanest deterministic matches changes the *shape* of the B4→B5 linkage gradient, rather than a number that is 100% by definition.

---

## 4. Scope discipline

Checked every section of the PDF and the complete_markdown against: (a) evaluating/endorsing the CMO, (b) causal claims from observational data, (c) extrapolation beyond 2006–2018 / the observable cohort, (d) unsupported "quality of medical education" claims.

- **No instance found** of the brief recommending a specific cutoff, assigning compliance/eligibility, or endorsing/opposing the CMO. §6 Conclusion explicitly disclaims regulatory recommendations. This is a real strength — the brief does not cross the line the user asked it not to cross.
- **No instance found** of an explicit causal claim ("X causes Y," "the cutoff produces Z outcome"). The closest is `dashboard.py:1043-1045` (Tab 5 finding2, live dashboard only, not in PDF): "This pattern is consistent across all NMAT years and **may reflect** differences in pre-medical preparation, admission selectivity, or other institutional factors not captured in this dataset" — correctly hedged with "may reflect," not asserted.
- **No extrapolation found** beyond 2006–2018 or beyond the observable cohort; the PDF is careful to keep "observable cohort" framing attached to every PLE-linked number.
- **No "quality of medical education" claim found.** The dataset (NMAT scores + PLE linkage) cannot support such a claim and the brief never makes one; the closest adjacent language ("quality assurance," "institutional accountability") is CMO-quoted context, not a data claim.
- **One borderline item**, not in the PDF but in the live `dashboard.py` (Tab 5, finding5, `dashboard.py:1077-1084`, and identically in `export_markdown.py` if it were included — confirmed it is *not*): "*This suggests the exception may not primarily benefit the intended disadvantaged groups*." This is an inferential/evaluative claim about the *design* of a CMO provision (the GIDA/IP exception), not a description of data. It is honestly hedged in the same sentence ("though GIDA/IP status is not available... for direct verification"), but it still edges toward opining on whether a specific policy provision is well-targeted — precisely the kind of judgment the user said this dashboard should not make. Recommend softening to something purely descriptive, e.g.: "*Most Public-institution examinees already score at or above B5; only 8.3% fall in the B4-only band the exception addresses. Whether this band overlaps with GIDA/IP applicants cannot be determined from this dataset.*"

---

## 5. Consistency — PDF vs. complete_markdown vs. parquet

| Drift | Where | Severity |
|---|---|---|
| §3.1 denominator "130,818" (PDF) vs. 130,735 (parquet, current) | PDF p.3 vs. live data | Medium — evidence PDF was generated from a different data snapshot than the currently-committed parquet, or from an intermediate join. |
| Foreign-nationality "Share of verified foreign (%)" wrong for all 10 rows | PDF p.6-7, complete_markdown Tab 4 ("Top 10 Nationalities" table), `export_markdown.py:631` | High — a genuine computation bug, present identically in both the PDF and the exported markdown (both are downstream of the same buggy `export_markdown.py` function), so this is not a snapshot-drift issue, it is a code bug that will keep reproducing on every re-export. |
| "Confirmed PLE passers (best record, observable)" = 29,273 (Tab 6 headline metric, both complete_markdown and presumably PDF's underlying data) vs. 29,258 (post-dedup, cited by the same brief in §3.4 two pages later) | complete_markdown Tab 6 line 583-585 vs. PDF §3.4 | Low-medium — internally inconsistent within the same deliverable; the brief cites a bug-fix number in one place and the pre-fix number in another. |
| Public/Private median percentile: 56/48 (complete_markdown Tab 4 "Score Summary" table) vs. 57/49 (complete_markdown Tab 5 "Institutional Performance Patterns" finding) | `export_markdown.py:576-582` (no `dropna` on `PercentileBin`) vs. `export_markdown.py:647-664` (`db = df_best.dropna(subset=["PercentileBin"])`) | Low — same nominal statistic (median `NMS_PER_num` by `UNI_TYPE`), computed on two slightly different populations, displayed as if identical, within the same 31-page document. Not in the PDF's own text (PDF doesn't state Tab-5's median-percentile finding), so lower practical impact, but should be unified. |
| Tab 2 "B5+ PLE-Passer Composition by Year" (100% every year) — see §3.6 | complete_markdown Tab 2, PDF Figure 4 | Critical (already covered above; listed here for completeness of the consistency check — it *is* internally consistent between PDF/markdown/dashboard, which is precisely the problem: the bug reproduces identically everywhere because it's upstream in `dashboard.py`, not a snapshot artifact). |

Everything else checked (bin distribution heatmaps, threshold tables, institutional patterns, clean-subset counts, foreign-count totals) reproduces exactly across PDF, complete_markdown, and the live parquet.

---

## 6. Claims register

| Claim | Location | Rating | Corrected wording |
|---|---|---|---|
| "17,482 of 26,937 Public examinees (64.9%) already meet B5+" | PDF §4.1 | **SUPPORTED** | (no change needed) |
| "GIDA/IP status is unavailable... the evidence cannot estimate the number of applicants who would be eligible" | PDF §5 | **SUPPORTED** | (no change needed) |
| "This clean subset... supports the dashboard's conclusion that the principal B5 and institutional patterns are not driven solely by less restrictive PLE-matching criteria" / "supports the robustness of the principal B5 pattern under stricter matching conditions" | PDF §3.4, §6 Conclusion | **UNSUPPORTED** — the exhibit backing this claim (Figure 4 / the clean-subset linkage rate) is tautologically 100% by construction (see §3.6) and cannot provide evidence either way | "The dashboard also examined the strictest defensible match criteria (best-record, deterministic match, ≥5-year gap, Filipino nationals). [Redo the underlying computation per §3.6, then state the actual result — e.g., 'Under these criteria, the B4→B5 linkage gradient shape is/is not preserved, at N=X vs N=Y.'] The current clean-subset chart does not provide evidence of robustness and should be replaced or removed until recomputed correctly." |
| "India accounts for 26,490 verified foreign records (85.1 percent)" | PDF §3.5 | **UNSUPPORTED / numerically wrong** | "India accounts for 26,490 of 32,501 verified foreign records (81.5 percent)." (and correct the other 9 rows of the same table by the same fix) |
| "33,713 (25.0 percent) took the NMAT more than once" | PDF §2 | **OVERSTATED precision, numerically wrong at stated precision** | "33,713 (25.2 percent)" or, to match the dashboard's own rounding convention, "approximately 25 percent" |
| "Among 130,818 best-record records with a valid percentile bin" | PDF §3.1 | **UNSUPPORTED by current data** | "Among 130,735 best-record records with a valid percentile bin" (after confirming which snapshot is authoritative) |
| "Public institution examinees show a higher median bin rank (57) than Private institution examinees (49)" | complete_markdown Tab 5 (not in PDF) | **Internally inconsistent** with Tab 4's own table (56/48) | Pick one population definition (recommend: drop rows with null `PercentileBin` consistently, i.e. use the Tab-5 method, 57/49) and use it everywhere. |
| "[Public school threshold attainment] suggests the exception may not primarily benefit the intended disadvantaged groups" | live `dashboard.py` Tab 5 (not in PDF, not in complete_markdown) | **OVERSTATED** — evaluative inference about policy design, not a data description | "Whether this band overlaps with GIDA/IP applicants cannot be determined from this dataset." |
| "NMAT-to-PLE-passer linkage rises across score bins, from 8.3% in B1 to 76.1% in B10... The policy-relevant change occurs between B4 and B5" | PDF §3.2 | **SUPPORTED as description, but risks being read as predictive of the proposed cutoff's effect** | Add explicit caveat per §3.2 above: this describes an already-admitted population under historical, non-uniform cutoffs and cannot be extrapolated to estimate the effect of a new uniform cutoff. |
| All disclaimers in PDF §5 ("Limitations") | PDF §5 | **SUPPORTED** | (no change — this section is a model of correct scope discipline) |

---

## 7. Defensible analyses this data supports that are missing

Constrained strictly to the 54 columns already in `NMAT_Exodus.parquet`:

1. **Fix and replace the clean-subset stress test (§3.6)** — compute the eligible-but-not-pre-filtered denominator, so the "robustness check" can actually fail if match quality is poor. This is the highest-priority missing analysis because it's currently presented as done, and it isn't.
2. **Share of known PLE passers who scored below each candidate cutoff** (§3.3 above) — directly computable from the same Table 3.2 the brief already builds; more decision-relevant than the linkage-rate-by-bin gradient for a cutoff-setting question, and still honestly caveated as non-causal.
3. **Subtest-level profile of the B4-only vs. B5+ groups** — `NMS_VCss, NMS_IRss, NMS_Qss, NMS_PAss, NMS_BIOss, NMS_PHYss, NMS_SSCss, NMS_CHEMss` are all in the 54 columns and already used in main Pipeline 3 (Section 8) but not surfaced in the CHED dashboard. Shows *whether* a composite-percentile cutoff masks different aptitude-vs-science strengths in the marginal group — directly relevant to "quality assurance mechanisms" language in the CMO rationale, and purely descriptive.
4. **Repeat-taker mobility across the B4/B5 boundary** — `PERSON_KEY` + multiple `APPNO_CLEAN` already identify the 25% repeat-taker population; a simple first-attempt-vs-best-attempt bin comparison would show how many examinees crossed the 30th/40th threshold on a second or later attempt. Directly relevant to whether a hard cutoff should account for retesting, and fully supported by existing columns.
5. **PLE-to-NMAT gap distribution by score bin** (not just the overall median) — `PLE_YEAR_GAP` already exists; showing the gap distribution (not just its median) by bin would substantiate the "observable cohort avoids right-censoring" claim with actual evidence rather than a single cutoff assumption, and would make transparent how much of the "no confirmed match" bucket in recent observable years (2013-2014) might still be right-censored rather than a true non-match.
6. **Sex-based threshold attainment** — `SEX` exists in the dataset and is unused anywhere in the CHED dashboard, despite the CMO's stated rationale including "enhance social equity and access." A simple B4+/B5+ attainment table by sex is fully within scope and currently absent.
7. **CourseGroup composition of the B4-only marginal group** (parallel to the existing UNI_TYPE breakdown) — already-used grouping variable, not currently cross-tabulated against the specific policy-relevant B4-only band.

None of these require any data the project doesn't already have; all are extensions of computations the CHED dashboard already performs for other slices.

---

## 8. Framing and language for a government audience

**Overall assessment:** the prose is unusually disciplined for a document of this kind — hedged, repeatedly self-limiting, and honest about what "linkage" is not. A hostile reviewer's strongest attack surface is not rhetorical overclaiming; it is the four verification failures in §2 and the circular exhibit in §3.6. Fix those and the document is largely defensible as written.

**Sentences that would not survive scrutiny, and corrected wording:**

1. *"India accounts for 26,490 verified foreign records (85.1 percent)"* → **wrong**, fix per §6.
2. *"33,713 (25.0 percent) took the NMAT more than once"* → **wrong at stated precision**, fix per §6.
3. *"Among 130,818 best-record records with a valid percentile bin"* → **does not reproduce**, fix per §6.
4. *"This clean subset... supports the dashboard's conclusion that the principal B5 and institutional patterns are not driven solely by less restrictive PLE-matching criteria"* and *"the clean-subset analysis supports the robustness of the principal B5 pattern under stricter matching conditions"* → **circular, unsupported**, fix per §6 (this is the sentence a technically literate hostile reviewer would find fastest — Figure 4 visibly shows a flat 100% line, and a numerate reader will immediately ask "how can this be exactly 100% every single year," which leads straight to the bug).
5. *(live dashboard only)* *"This suggests the exception may not primarily benefit the intended disadvantaged groups"* → **evaluative overreach**, fix per §6.

---

## Files referenced

- `docs/CHED_CMO.md` — policy text (read in full)
- `streamlit_dashboard/CHED_relevant_dashboard/dashboard.py:1-230, 560-671, 839-850, 955-1125` — subset construction, the circular clean-subset logic, Tab 5 findings
- `streamlit_dashboard/CHED_relevant_dashboard/export_markdown.py:283-335, 567-638, 640-677, 680-713` — markdown-export computations, including the nationality-share bug (line 631) and the median-percentile inconsistency (lines 576-582 vs. 647-664)
- `streamlit_dashboard/CHED_relevant_dashboard/complete_markdown/CHED_NMAT_Dashboard_Complete.md` — full exported analysis (read in full)
- `streamlit_dashboard/CHED_relevant_dashboard/complete_markdown/NMAT-CutOff-Analysis_BRIEF.pdf` — published deliverable (read in full, 9 pages)
- `streamlit_dashboard/CHED_relevant_dashboard/Plan_1_Ched_Dashboard_Revision.md` — design intent behind the clean-subset stress test (TODO 7/8), confirms it was meant to be a genuine robustness check
- `docs/data_dictionary.md` — column definitions cross-checked against brief claims
- `forensic_audit/forensic_audit_report.md:16,61,69,75,122,171,213,296,308-309` — source of the "15 of 29,258" data-quality figure cited in PDF §3.4
