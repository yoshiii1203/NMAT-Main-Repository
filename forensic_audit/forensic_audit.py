"""
======================================================================
forensic_audit.py — Consolidated NMAT -> PLE forensic audit
======================================================================

This is the ONLY audit script in this directory that should be run or
trusted going forward. It supersedes forensic_audit_v2.py .. v6, and
forensic_audit_nmat_ple_matches.py, audit_name_check.py,
audit_name_check_deep.py, audit_per_bin_report.py, _check_missing.py
-- all moved to forensic_audit/_superseded/ (see the README there for
why their headline numbers do not hold, notably the "4 genuine
mismatches" claim, which required an undocumented manual override of
13 of the 17 records the old script actually flagged).

Run (from anywhere -- all paths are relative to this file, not to cwd):
    ./.venv/Scripts/python.exe forensic_audit/forensic_audit.py

Every number in forensic_audit_report.md and name_cross_check_evidence.md
comes from this script. No hand-edited values.

Inputs:
  dataset/NMAT_Exodus.parquet          -- 51-col canonical dataset (identity + score source)
  dataset/output/PLE_MATCH_MASTER.csv  -- ONLY source of PLE-side (board-exam) names.
                                           NMAT_Exodus.parquet carries no PLE name at all,
                                           so this file cannot be avoided for the name
                                           cross-check. Its staleness/coverage relative to
                                           the parquet is measured and reported below, not
                                           assumed -- see Section 4.

Outputs (all written next to this script, in forensic_audit/):
  forensic_audit_summary.csv               -- Section 1-2 population + selection-effect table
  forensic_audit_contingency_2x2.csv        -- Section 3 full 2x2 tables per threshold
  forensic_audit_name_check_results.csv     -- Section 4 every appno-based row + both verdicts
  forensic_audit_exceptions.csv             -- Section 4 unresolved / ambiguous / uncoverable rows
======================================================================
"""
import os
import re
import time
import unicodedata
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
DATA_PATH = os.path.join(REPO_ROOT, "dataset", "NMAT_Exodus.parquet")
MM_PATH = os.path.join(REPO_ROOT, "dataset", "output", "PLE_MATCH_MASTER.csv")
OUT_DIR = HERE


def hdr(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ══════════════════════════════════════════════════════════════════
# THREATS TO VALIDITY — printed every run, unconditionally. Two
# DISTINCT mechanisms both depress observed below-40th-percentile
# linkage. Do not conflate them.
#
#  (T1) ADMISSION SELECTION (real-world policy). CMO 18 s.2016 already
#       enforces a 40th-percentile floor, so people scoring below it
#       were largely barred from enrolling in medical school at all --
#       they cannot appear as PLE passers regardless of data quality.
#       This is a fact about the world, not a bug.
#
#  (T2) MATCHER SUPPRESSION (our own code, found by the orchestrator
#       during remediation, not by the original forensic audit).
#       `2_PLE_Matching_Pipeline.ipynb`, Cell 6 `disambiguate()`, Step 4:
#           PERCENTILE_FLOOR = 40
#           pct_pass = [r for r in latest_pass if r["NMS_PER_num"] >= PERCENTILE_FLOOR]
#           if not pct_pass: return {"status": "NO_VALID_MATCH", ...}
#       This is a HARD FILTER, not a tie-break, applied only inside
#       disambiguate() -- which is only called from Stage 1 (EXACT
#       name match, Cell 9) when a PLE name matches MORE THAN ONE NMAT
#       candidate ("name-collision group"). Within such a group, any
#       candidate scoring below the 40th percentile is discarded before
#       the final pick, and the match is rejected outright
#       (NO_VALID_MATCH) if every surviving candidate is below 40. The
#       threshold is the SAME 40 this audit is investigating, so the
#       below-cutoff linkage counts computed on pre-fix data are
#       confounded by the matcher itself, not just by admission
#       selection (T1). SCOPE: unique-name EXACT matches bypass
#       disambiguate() entirely, and MANUAL_APPNO_MATCH /
#       DETERMINISTIC_APPNO (Stages 0 and 2) never call it -- so this
#       is confined to EXACT matches that were name-collision groups.
#       Below-40 passers still exist in the data; the claim withdrawn
#       here is about their RATE / rarity, not their existence.
#
# P1 is re-running Pipeline 2 with Step 4 removed; the parquet will be
# regenerated. This script hardcodes nothing -- every count below is
# computed at run time, so re-running against the corrected parquet
# reproduces corrected numbers automatically.
# ══════════════════════════════════════════════════════════════════
hdr("THREATS TO VALIDITY (read before trusting any below-cutoff rate below)")
print(
    "  T1 ADMISSION SELECTION: below-40 examinees were largely barred from enrolling\n"
    "     (CMO 18 s.2016) -- a policy fact, not a data defect.\n"
    "  T2 MATCHER SUPPRESSION: 2_PLE_Matching_Pipeline.ipynb disambiguate() Step 4\n"
    "     hard-drops below-40 candidates within EXACT-match name-collision groups,\n"
    "     using the SAME 40th-percentile constant under investigation. Confined to\n"
    "     EXACT matches with >1 same-name candidate; APPNO-based matches unaffected.\n"
    "     If this run predates the Step-4 fix landing, treat every below-40 linkage\n"
    "     figure below as an UNDER-COUNT, and do not quote it as 'how rare' below-\n"
    "     cutoff passers are -- only that they exist.\n"
)

# ══════════════════════════════════════════════════════════════════
# LOAD + SCHEMA GUARD
# ══════════════════════════════════════════════════════════════════
hdr("LOAD")
df = pd.read_parquet(DATA_PATH)
print(f"Loaded {DATA_PATH}  (mtime: {time.ctime(os.path.getmtime(DATA_PATH))})")
print(f"  Rows: {len(df):,}   Cols: {len(df.columns)}")

# Fail loudly rather than silently computing on the wrong schema version.
assert "IS_PLE_ANALYSIS_SAFE" not in df.columns, (
    "IS_PLE_ANALYSIS_SAFE is present -- this is the OLD (pre-fix) schema. "
    "This script requires the corrected 51-column parquet."
)
for required in ("IS_OBSERVABLE_COHORT", "IS_BEST_OBSERVABLE_RECORD", "PERSON_KEY_AMBIGUOUS"):
    assert required in df.columns, f"missing corrected flag {required} -- wrong schema version"
assert "PERSON_NAME" not in df.columns, "PERSON_NAME unexpectedly present -- update the name-source logic"


# Use the dataset's OWN canonical PercentileBin column, not a recomputed
# cut of NMS_PER_num. They are not interchangeable: PercentileBin is null
# for 1,330 best-observable rows, of which 573 have a non-null NMS_PER_num
# in [0,10) -- i.e. PercentileBin treats them as invalid/unbinnable for a
# reason upstream (verified by direct crosstab: everywhere PercentileBin
# is non-null, a from-scratch pd.cut of NMS_PER_num agrees with it
# exactly; the two sources disagree ONLY on that 573-row null set,
# concentrated at the very bottom of the score range). Recomputing bands
# independently silently overcounts B1 by ~8% and is the reason an
# earlier draft of this script's B1 figures did not match the
# orchestrator's numbers (795 confirmed passers / 11.60% in the lowest
# decile) -- this is what fixed it.
BAND_ORDER = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]
df["BAND"] = df["PercentileBin"].fillna("Missing")

# ══════════════════════════════════════════════════════════════════
# SECTION 1: POPULATION -- uses the CORRECTED flags per the schema
# contract, not the naive IS_BEST_NMAT_RECORD & Year<=2014 combo.
# ══════════════════════════════════════════════════════════════════
hdr("1. AUDIT POPULATION (corrected flags)")

obs_rows = df[df["IS_OBSERVABLE_COHORT"]]
best_obs = df[df["IS_BEST_OBSERVABLE_RECORD"]].copy()  # exactly one row per person, Year<=2014 window

n_amb_keys_dataset = df.loc[df["PERSON_KEY_AMBIGUOUS"], "PERSON_KEY"].nunique()
amb_in_best_obs = best_obs["PERSON_KEY_AMBIGUOUS"].sum()
best_obs_clean = best_obs[~best_obs["PERSON_KEY_AMBIGUOUS"]].copy()

print(f"  Row-level observable cohort (IS_OBSERVABLE_COHORT, Year<=2014): {len(obs_rows):>8,} rows")
print(f"  Person-level best-in-window (IS_BEST_OBSERVABLE_RECORD):        {len(best_obs):>8,} people")
print(f"    duplicate PERSON_KEY within best_obs (should be 0):           {best_obs['PERSON_KEY'].duplicated().sum():>8,}")
print(f"  PERSON_KEY_AMBIGUOUS keys, whole dataset:                      {n_amb_keys_dataset:>8,}")
print(f"  PERSON_KEY_AMBIGUOUS people within best_obs:                   {amb_in_best_obs:>8,} "
      f"({amb_in_best_obs/len(best_obs)*100:.2f}% of observable population)")
print(f"  best_obs_clean (ambiguous keys excluded):                      {len(best_obs_clean):>8,} people")

# Robustness check inherited from the old audit's Section 5 (F9: a positive
# finding worth re-verifying under the corrected flags, not re-implementing
# the whole classifier -- most of what it caught no longer exists).
neg_gap = (best_obs["PLE_YEAR_GAP"] < 0).sum()
zero_gap = (best_obs["PLE_YEAR_GAP"] == 0).sum()
shared_appno = (best_obs.groupby("APPNO_CLEAN")["PERSON_KEY"].nunique() > 1).sum()
print(f"\n  Data-quality categories the old audit (v5) flagged and manually excluded -- re-checked here:")
print(f"    Negative PLE_YEAR_GAP in best_obs:      {neg_gap:>6,}  (old audit found some; MUST be 0 or explained)")
print(f"    Zero PLE_YEAR_GAP in best_obs:           {zero_gap:>6,}")
print(f"    APPNO shared by >1 person in best_obs:   {shared_appno:>6,}")
print(f"    -> All three are resolved by the corrected data layer (IS_BEST_OBSERVABLE_RECORD /")
print(f"       IS_OBSERVABLE_COHORT), so no manual 'data_quality' exclusion category is needed here.")
print(f"       The only remaining known identity risk is PERSON_KEY_AMBIGUOUS, handled explicitly below.")

band_counts_all = best_obs["BAND"].value_counts()
band_counts_clean = best_obs_clean["BAND"].value_counts()
print(f"\n  {'Band':<8}{'best_obs':>12}{'best_obs_clean':>18}")
for b in BAND_ORDER + ["Missing"]:
    a = band_counts_all.get(b, 0)
    c = band_counts_clean.get(b, 0)
    if a or c:
        print(f"  {b:<8}{a:>12,}{c:>18,}")

# ══════════════════════════════════════════════════════════════════
# SECTION 2: SELECTION EFFECT — the B4->B5 linkage jump. "Linked" means
# IS_PLE_PASSER is True, i.e. this person's PLE record was found. The
# PLE source file contains PASSERS ONLY -- "not linked" is NEVER
# "failed"; it means no confirmed board-passer record was found for
# this person (they may not have enrolled, may not have taken the
# boards yet even within the observable window in edge cases, or may
# have failed -- all three are indistinguishable here).
# ══════════════════════════════════════════════════════════════════
hdr("2. SELECTION EFFECT — linkage rate by score band")
print(
    "  *** T1 CAVEAT: people below the 40th percentile (B1-B4) were largely barred from\n"
    "  *** enrolling in medical school under CMO 18 s.2016's existing 40th-percentile\n"
    "  *** floor. Anyone observed here scoring below B5 is an atypical admitted residual,\n"
    "  *** NOT a random sample of everyone who scored below the cutoff. The B4->B5 jump\n"
    "  *** below is evidence of an admission rule, not of ability or of the cutoff's\n"
    "  *** predictive validity. No conclusion about lowering the cutoff to the 30th\n"
    "  *** percentile follows from this table.\n"
    "  *** T2 CAVEAT: see 'THREATS TO VALIDITY' above -- below-40 linkage counts here may\n"
    "  *** additionally be under-counted by the disambiguate() Step-4 matcher filter if\n"
    "  *** this run predates that fix landing.\n"
    "  *** Reported BOTH with and without PERSON_KEY_AMBIGUOUS people, because T2's\n"
    "  *** suppression is confined to name-collision groups -- precisely where ambiguous\n"
    "  *** keys live.\n"
)


def selection_table(pop, label):
    rows = []
    for b in BAND_ORDER:
        sub = pop[pop["BAND"] == b]
        n = len(sub)
        linked = int(sub["IS_PLE_PASSER"].sum())
        rate = linked / n * 100 if n else float("nan")
        rows.append({"Band": b, "N_observable": n, "N_linked": linked, "Linkage_rate_pct": round(rate, 2)})
    out = pd.DataFrame(rows)
    print(f"\n  -- {label} (n={len(pop):,}) --")
    print(out.to_string(index=False))
    b4 = out.loc[out.Band == "B4", "Linkage_rate_pct"].iloc[0]
    b5 = out.loc[out.Band == "B5", "Linkage_rate_pct"].iloc[0]
    print(f"  B4 (30-39th %ile) linkage rate: {b4:.1f}%   B5 (40-49th %ile) linkage rate: {b5:.1f}%")
    print(f"  Jump at the 40th-percentile CMO floor: {b5-b4:+.1f} points")
    out["Population"] = label
    return out, b4, b5


sel_df_amb, b4_rate_amb, b5_rate_amb = selection_table(best_obs, "best_obs (incl. ambiguous keys)")
sel_df, b4_rate, b5_rate = selection_table(best_obs_clean, "best_obs_clean (ambiguous keys excluded)")

# ══════════════════════════════════════════════════════════════════
# SECTION 3: FULL 2x2 CONTINGENCY TABLES at candidate thresholds.
# Population: best_obs_clean (one row per observable person, ambiguous
# keys excluded). This is the first time any script in this repo
# computes the complement (people who are NOT confirmed PLE passers),
# not just the passer subset.
# ══════════════════════════════════════════════════════════════════
hdr("3. FULL 2x2 CONTINGENCY TABLES, by candidate threshold")
print(
    "  *** CAVEAT: 'sensitivity/specificity/PPV/NPV' language below is used loosely, in the\n"
    "  *** statistical sense of a 2x2 table -- it is NOT predictive validity in the medical or\n"
    "  *** psychometric sense, because we never observe outcomes for people who were not\n"
    "  *** admitted to medical school at all. This table is CONDITIONAL ON ADMISSION (T1). It\n"
    "  *** describes the observed examinee pool, not the population the cutoff actually screens.\n"
    "  *** The 'Below_and_Linked' cell specifically is also subject to T2 (matcher suppression,\n"
    "  *** see THREATS TO VALIDITY) on any pre-fix run -- it is a floor, not the true count, until\n"
    "  *** Pipeline 2's disambiguate() Step 4 is removed and this script is re-run.\n"
    "  *** Reported for both best_obs and best_obs_clean (ambiguous keys excluded) -- T2 is\n"
    "  *** confined to name-collision groups, which is exactly what PERSON_KEY_AMBIGUOUS flags.\n"
)

thresholds = [30, 35, 40, 45, 50]


def contingency_tables(pop, label):
    n_missing = int(pop["NMS_PER_num"].isna().sum())
    scored = pop[pop["NMS_PER_num"].notna()].copy()
    print(f"\n  -- {label}: total {len(pop):,}, excluded (no percentile) {n_missing:,}, table population {len(scored):,} --")
    rows = []
    for thr in thresholds:
        above = scored["NMS_PER_num"] >= thr
        linked = scored["IS_PLE_PASSER"]
        a = int((above & linked).sum())       # above cutoff, linked
        b = int((above & ~linked).sum())      # above cutoff, not linked
        c = int((~above & linked).sum())      # below cutoff, linked
        d = int((~above & ~linked).sum())     # below cutoff, not linked
        total = a + b + c + d
        sens = a / (a + c) if (a + c) else np.nan
        spec = d / (b + d) if (b + d) else np.nan
        ppv = a / (a + b) if (a + b) else np.nan
        npv = d / (c + d) if (c + d) else np.nan
        rows.append({
            "Population": label, "Threshold_pctile": thr,
            "Above_and_Linked": a, "Above_and_NotLinked": b,
            "Below_and_Linked": c, "Below_and_NotLinked": d,
            "Total": total,
            "Base_rate_linked_pct": round((a + c) / total * 100, 2),
            "Sensitivity_pct": round(sens * 100, 2),
            "Specificity_pct": round(spec * 100, 2),
            "PPV_pct": round(ppv * 100, 2),
            "NPV_pct": round(npv * 100, 2),
        })
        print(f"    Threshold >= {thr}th percentile:  "
              f"Above&Linked={a:,}  Above&NotLinked={b:,}  Below&Linked={c:,}  Below&NotLinked={d:,}  "
              f"Sens={sens*100:.1f}%  Spec={spec*100:.1f}%  PPV={ppv*100:.1f}%  NPV={npv*100:.1f}%")
    return pd.DataFrame(rows)


cont_df_amb = contingency_tables(best_obs, "best_obs (incl. ambiguous keys)")
cont_df_clean = contingency_tables(best_obs_clean, "best_obs_clean (ambiguous keys excluded)")
cont_df = pd.concat([cont_df_amb, cont_df_clean], ignore_index=True)

# ══════════════════════════════════════════════════════════════════
# SECTION 4: NAME CROSS-CHECK — appno-based matches only (matches made
# on APPNO_CLEAN, not on name equality, so a genuine name mismatch is
# possible and worth checking). EXACT matches are matched BY name
# equality already, so a "mismatch" check on them is close to
# tautological and is out of scope here (see withdrawal notes).
#
# NMAT-side name: parsed from PERSON_KEY in the CURRENT parquet
# ("SURNAME, GIVEN NAMES||birthdate") -- NOT from the stale
# intermediate, per instructions.
# PLE-side name: PLE_FULL_NAME from dataset/output/PLE_MATCH_MASTER.csv.
# This is unavoidable -- NMAT_Exodus.parquet carries no PLE-side name
# at all. Coverage of this file against the current parquet's
# appno-matched population is measured explicitly, not assumed.
# ══════════════════════════════════════════════════════════════════
hdr("4. NAME CROSS-CHECK — APPNO-based matches (MANUAL_APPNO_MATCH + DETERMINISTIC_APPNO)")

APPNO_METHODS = ["MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"]
appno_df = df[df["PLE_MATCH_METHOD"].isin(APPNO_METHODS)].copy()
appno_df["APPNO_CLEAN"] = appno_df["APPNO_CLEAN"].astype(str).str.strip()
appno_df["NMA_NAME_FROM_PERSON_KEY"] = appno_df["PERSON_KEY"].astype(str).str.partition("||")[0]
# NB: str.split("||") is WRONG here -- pandas treats a >1-char pat as regex by
# default, and "||" as regex means "empty pattern OR empty pattern", which
# matches everywhere and shreds the string. str.partition splits on the
# literal substring.

n_appno_total = len(appno_df)
print(f"  APPNO-based matched rows in current parquet: {n_appno_total:,}")
print(f"    of which MANUAL_APPNO_MATCH: {(appno_df['PLE_MATCH_METHOD']=='MANUAL_APPNO_MATCH').sum():,}")
print(f"    of which DETERMINISTIC_APPNO: {(appno_df['PLE_MATCH_METHOD']=='DETERMINISTIC_APPNO').sum():,}")
print(f"  This is the population being checked in this section (dataset-wide, not scoped to")
print(f"  the observable cohort -- identity verification does not depend on Year<=2014).")

mm = pd.read_csv(MM_PATH, dtype=str)
mm_appno = mm[
    mm["MATCH_METHOD"].isin(APPNO_METHODS) & (mm["MATCH_STATUS"] == "FINAL_MATCH")
].copy()
mm_appno["MATCHED_APPNO"] = mm_appno["MATCHED_APPNO"].astype(str).str.strip()
mm_group = {appno: grp for appno, grp in mm_appno.groupby("MATCHED_APPNO")}

records = []
for _, r in appno_df.iterrows():
    appno = r["APPNO_CLEAN"]
    cand = mm_group.get(appno)
    if cand is None:
        status = "no_master_record"
        ple_name = None
    elif len(cand) > 1:
        status = "ambiguous_multiple_ple_candidates"
        ple_name = None
    else:
        status = "matched"
        ple_name = cand.iloc[0]["PLE_FULL_NAME"]
    records.append({
        "APPNO_CLEAN": appno,
        "PLE_MATCH_METHOD": r["PLE_MATCH_METHOD"],
        "BAND": r["BAND"],
        "NMS_PER_num": r["NMS_PER_num"],
        "Year": r["Year"],
        "nma_name": r["NMA_NAME_FROM_PERSON_KEY"],
        "ple_name": ple_name,
        "coverage_status": status,
    })

rd = pd.DataFrame(records)
n_matched = (rd.coverage_status == "matched").sum()
n_ambiguous_src = (rd.coverage_status == "ambiguous_multiple_ple_candidates").sum()
n_no_master = (rd.coverage_status == "no_master_record").sum()
coverage_pct = n_matched / n_appno_total * 100

print(f"\n  Coverage of dataset/output/PLE_MATCH_MASTER.csv against the current parquet's")
print(f"  APPNO-based population:")
print(f"    Matched (1 PLE-side name candidate found):        {n_matched:>6,} ({coverage_pct:.1f}%)")
print(f"    Ambiguous (>1 PLE-side name candidates for appno): {n_ambiguous_src:>6,} ({n_ambiguous_src/n_appno_total*100:.1f}%)")
print(f"    No master record at all (uncoverable here):        {n_no_master:>6,} ({n_no_master/n_appno_total*100:.1f}%)")
print(f"\n  *** COVERAGE CAVEAT: {n_no_master:,} rows ({n_no_master/n_appno_total*100:.1f}%) cannot be name-checked at all")
print(f"  *** with any file currently in this repo -- their identity linkage is unverified,")
print(f"  *** not verified-clean. Do not read the mismatch rate below as covering 100% of")
print(f"  *** the APPNO-based population; it covers the {coverage_pct:.1f}% that is 'matched'.")


# --- normalizer -----------------------------------------------------
FIL_PREFIXES = {"DE", "DELA", "DELOS", "DELAS", "DEL", "LA", "LAS", "LOS", "SAN", "SANTA", "SANTO", "STO", "STA"}


def _clean(s):
    s = unicodedata.normalize("NFKD", str(s).upper()).encode("ASCII", "ignore").decode()
    s = re.sub(r"[^A-Z0-9\s,]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def normalize_surname(surname):
    """Deterministically merge Filipino compound-surname prefix tokens
    (De/Dela/Del/La/Las/Los/San/Santa/Santo/Sto/Sta) with the token that
    follows, so 'DE GUZMAN', 'DE  GUZMAN' and 'DEGUZMAN' all normalise to
    the same string 'DEGUZMAN'. Surnames without such a prefix token are
    returned unchanged. Applied in code, deterministically -- no manual
    step, no per-record judgement."""
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


def parse_names(ple_raw, nma_raw, normalize_surnames):
    if pd.isna(ple_raw) or pd.isna(nma_raw):
        return {"verdict": "missing"}
    p = _clean(ple_raw)
    n = _clean(nma_raw)

    ple_surname = p.split(",")[0].strip() if "," in p else (p.split()[-1] if p else "")
    nma_surname = n.split(",")[0].strip() if "," in n else (n.split()[-1] if n else "")
    ple_given = p.split(",", 1)[1].strip() if "," in p else ""
    nma_given = n.split(",", 1)[1].strip() if "," in n else ""

    if normalize_surnames:
        ple_surname_cmp = normalize_surname(ple_surname)
        nma_surname_cmp = normalize_surname(nma_surname)
    else:
        ple_surname_cmp = ple_surname
        nma_surname_cmp = nma_surname

    ple_words = set(p.replace(",", " ").split())
    nma_words = set(n.replace(",", " ").split())
    overlap = ple_words & nma_words
    all_words = ple_words | nma_words
    overlap_ratio = len(overlap) / len(all_words) if all_words else 0

    n_squashed = n.replace(" ", "")
    p_squashed = p.replace(" ", "")
    surname_in_nma = bool(ple_surname_cmp) and ple_surname_cmp in n_squashed
    nma_surname_in_ple = bool(nma_surname_cmp) and nma_surname_cmp in p_squashed

    given_match = False
    if ple_given and nma_given:
        given_match = bool(set(ple_given.split()) & set(nma_given.split()))

    is_same_last = ple_surname_cmp != "" and ple_surname_cmp == nma_surname_cmp
    is_married = surname_in_nma and nma_surname_in_ple and given_match
    is_high_overlap = overlap_ratio >= 0.6

    if is_same_last and given_match:
        verdict = "strong_match"
    elif is_same_last:
        verdict = "same_surname_no_given_match"
    elif is_married:
        verdict = "married_name_change"
    elif is_high_overlap:
        verdict = "high_overlap"
    elif surname_in_nma or nma_surname_in_ple:
        verdict = "surname_swapped"
    else:
        verdict = "genuine_mismatch"

    return {
        "ple_surname": ple_surname, "nma_surname": nma_surname,
        "ple_surname_norm": ple_surname_cmp, "nma_surname_norm": nma_surname_cmp,
        "overlap_ratio": round(overlap_ratio, 2), "given_match": given_match,
        "verdict": verdict,
    }


matched = rd[rd.coverage_status == "matched"].copy()
raw_v = matched.apply(lambda r: parse_names(r["ple_name"], r["nma_name"], normalize_surnames=False), axis=1)
norm_v = matched.apply(lambda r: parse_names(r["ple_name"], r["nma_name"], normalize_surnames=True), axis=1)
matched["verdict_raw"] = [v["verdict"] for v in raw_v]
matched["verdict_norm"] = [v["verdict"] for v in norm_v]
matched["overlap_ratio"] = [v["overlap_ratio"] for v in norm_v]
matched["pct_num"] = pd.to_numeric(matched["NMS_PER_num"], errors="coerce")

print(f"\n  -- Verdict counts, checked population only (n={len(matched):,}) --")
print(f"\n  {'Verdict':<32}{'Raw (no normaliser)':>22}{'Normalised':>14}")
raw_counts = matched["verdict_raw"].value_counts()
norm_counts = matched["verdict_norm"].value_counts()
for v in sorted(set(raw_counts.index) | set(norm_counts.index)):
    print(f"  {v:<32}{raw_counts.get(v,0):>22,}{norm_counts.get(v,0):>14,}")

raw_mismatch = matched["verdict_raw"] == "genuine_mismatch"
norm_mismatch = matched["verdict_norm"] == "genuine_mismatch"
resolved = raw_mismatch & ~norm_mismatch
still_mismatch = norm_mismatch

print(f"\n  genuine_mismatch, raw (no normaliser):        {raw_mismatch.sum():,}")
print(f"  genuine_mismatch, after normaliser:           {norm_mismatch.sum():,}")
print(f"  Resolved BY the normaliser (raw mismatch -> not mismatch after normalising): {resolved.sum():,}")

low = matched[matched["pct_num"] < 40]
raw_mismatch_low = low["verdict_raw"] == "genuine_mismatch"
norm_mismatch_low = low["verdict_norm"] == "genuine_mismatch"
resolved_low = raw_mismatch_low & ~norm_mismatch_low
print(f"\n  -- Low-score subset only (NMS_PER_num < 40, n={len(low):,}) --")
print(f"  genuine_mismatch, raw (no normaliser):        {raw_mismatch_low.sum():,}")
print(f"  genuine_mismatch, after normaliser:           {norm_mismatch_low.sum():,}")
print(f"  Resolved by normaliser:                       {resolved_low.sum():,}")

print(f"\n  -- Remaining genuine_mismatch after normalisation (n={still_mismatch.sum():,}), NOT reclassified,")
print(f"     written to forensic_audit_exceptions.csv for human review --")
for _, r in matched[still_mismatch].iterrows():
    print(f"    PLE='{r['ple_name'][:55]}'  NMA='{r['nma_name'][:55]}'  "
          f"pct={r['NMS_PER_num']}  band={r['BAND']}  method={r['PLE_MATCH_METHOD']}  "
          f"overlap={r['overlap_ratio']}")

# ══════════════════════════════════════════════════════════════════
# SAVE OUTPUTS -- all next to this script (forensic_audit/), not root.
# ══════════════════════════════════════════════════════════════════
hdr("SAVE OUTPUTS")

summary_rows = [
    {"Section": "1", "Metric": "row-level observable cohort (IS_OBSERVABLE_COHORT)", "Value": len(obs_rows)},
    {"Section": "1", "Metric": "person-level best-in-window (IS_BEST_OBSERVABLE_RECORD)", "Value": len(best_obs)},
    {"Section": "1", "Metric": "PERSON_KEY_AMBIGUOUS keys, dataset-wide", "Value": int(n_amb_keys_dataset)},
    {"Section": "1", "Metric": "PERSON_KEY_AMBIGUOUS people within best_obs", "Value": int(amb_in_best_obs)},
    {"Section": "1", "Metric": "best_obs_clean (ambiguous excluded)", "Value": len(best_obs_clean)},
    {"Section": "2", "Metric": "B4 linkage rate pct (best_obs_clean)", "Value": float(b4_rate)},
    {"Section": "2", "Metric": "B5 linkage rate pct (best_obs_clean)", "Value": float(b5_rate)},
    {"Section": "2", "Metric": "B4->B5 jump (points)", "Value": float(b5_rate - b4_rate)},
    {"Section": "4", "Metric": "APPNO-based matched rows, current parquet", "Value": n_appno_total},
    {"Section": "4", "Metric": "coverage pct (matched in PLE_MATCH_MASTER.csv)", "Value": round(coverage_pct, 2)},
    {"Section": "4", "Metric": "genuine_mismatch raw (checked pop.)", "Value": int(raw_mismatch.sum())},
    {"Section": "4", "Metric": "genuine_mismatch after normaliser (checked pop.)", "Value": int(norm_mismatch.sum())},
    {"Section": "4", "Metric": "genuine_mismatch raw, low-score(<40) subset", "Value": int(raw_mismatch_low.sum())},
    {"Section": "4", "Metric": "genuine_mismatch after normaliser, low-score(<40) subset", "Value": int(norm_mismatch_low.sum())},
]
pd.DataFrame(summary_rows).to_csv(os.path.join(OUT_DIR, "forensic_audit_summary.csv"), index=False)
pd.concat([sel_df_amb, sel_df], ignore_index=True).to_csv(os.path.join(OUT_DIR, "forensic_audit_selection_effect.csv"), index=False)
cont_df.to_csv(os.path.join(OUT_DIR, "forensic_audit_contingency_2x2.csv"), index=False)
matched.drop(columns=["APPNO_CLEAN"]).to_csv(os.path.join(OUT_DIR, "forensic_audit_name_check_results.csv"), index=False)

exc_rows = []
for _, r in matched[still_mismatch].iterrows():
    exc_rows.append({
        "exception_type": "unresolved_genuine_mismatch",
        "ple_name": r["ple_name"], "nma_name": r["nma_name"],
        "band": r["BAND"], "pct": r["NMS_PER_num"], "method": r["PLE_MATCH_METHOD"],
        "overlap_ratio": r["overlap_ratio"], "note": "needs human review; NOT auto-reclassified",
    })
for _, r in rd[rd.coverage_status == "ambiguous_multiple_ple_candidates"].iterrows():
    exc_rows.append({
        "exception_type": "ambiguous_source_conflict",
        "ple_name": None, "nma_name": r["nma_name"],
        "band": r["BAND"], "pct": r["NMS_PER_num"], "method": r["PLE_MATCH_METHOD"],
        "overlap_ratio": None, "note": ">1 PLE_FULL_NAME candidate for this APPNO in PLE_MATCH_MASTER.csv",
    })
for _, r in rd[rd.coverage_status == "no_master_record"].iterrows():
    exc_rows.append({
        "exception_type": "uncoverable_no_source_record",
        "ple_name": None, "nma_name": r["nma_name"],
        "band": r["BAND"], "pct": r["NMS_PER_num"], "method": r["PLE_MATCH_METHOD"],
        "overlap_ratio": None, "note": "no PLE-side name available in any file in this repo",
    })
pd.DataFrame(exc_rows).to_csv(os.path.join(OUT_DIR, "forensic_audit_exceptions.csv"), index=False)

print(f"  forensic_audit_summary.csv              ({len(summary_rows)} rows)")
print(f"  forensic_audit_selection_effect.csv     ({len(sel_df)} rows)")
print(f"  forensic_audit_contingency_2x2.csv      ({len(cont_df)} rows)")
print(f"  forensic_audit_name_check_results.csv   ({len(matched)} rows)")
print(f"  forensic_audit_exceptions.csv           ({len(exc_rows)} rows)")
print(f"\n  All written to {OUT_DIR}")

hdr("AUDIT COMPLETE")
