"""
======================================================================
NMAT → PLE Passer Forensic Audit
======================================================================
Record-level forensic audit of potentially anomalous NMAT-to-PLE-passer
matches. Determines whether confirmed PLE passers below policy-relevant
cut-offs are valid historical observations, repeat-taker artifacts, or
invalid/ambiguous matches.

Author: AI Audit Agent
Date: 2026-07-27
======================================================================
"""

import pandas as pd
import numpy as np
import hashlib
import json

# ── Load the data ──────────────────────────────────────────────────
DATA_PATH = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\streamlit_dashboard\CHED_relevant_dashboard\NMAT_Exodus.parquet"
df = pd.read_parquet(DATA_PATH)
print(f"Loaded NMAT_Exodus: {len(df):,} rows, {len(df.columns)} columns\n")

# ── Step 1: Define the audit population ────────────────────────────
# Observable cohort: NMAT Year <= 2014
obs = df[df["Year"] <= 2014].copy()
print(f"Observable cohort (Year <= 2014): {len(obs):,} rows")

# Confirmed PLE passers only (IS_PLE_ANALYSIS_SAFE == True)
confirmed = obs[obs["IS_PLE_ANALYSIS_SAFE"] == True].copy()
print(f"Confirmed PLE passers (IS_PLE_ANALYSIS_SAFE): {len(confirmed):,} rows")

# Best-record subset
best = confirmed[confirmed["IS_BEST_NMAT_RECORD"] == True].copy()
print(f"Best-record confirmed passers: {len(best):,} rows")

# ── Score bands ─────────────────────────────────────────────────────
# Recreate numeric percentile bins
def bin_label(pct):
    if pd.isna(pct):
        return "Missing"
    if pct < 10:
        return "B1"
    elif pct < 20:
        return "B2"
    elif pct < 30:
        return "B3"
    elif pct < 40:
        return "B4"
    elif pct < 50:
        return "B5"
    elif pct < 60:
        return "B6"
    elif pct < 70:
        return "B7"
    elif pct < 80:
        return "B8"
    elif pct < 90:
        return "B9"
    else:
        return "B10"

confirmed["BAND"] = confirmed["NMS_PER_num"].map(bin_label)
best["BAND"] = best["NMS_PER_num"].map(bin_label)

# Report counts by band
print("\n" + "=" * 60)
print("A. Audit Population -- Confirmed PLE Passers by Score Band")
print("=" * 60)
band_order = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]
band_counts = confirmed["BAND"].value_counts()
best_band_counts = best["BAND"].value_counts()

print(f"\n{'Band':<8} {'All Records':>14} {'Best Record':>14} {'Best %':>10}")
print("-" * 50)
for b in band_order:
    ac = band_counts.get(b, 0)
    bc = best_band_counts.get(b, 0)
    pct = bc / len(best) * 100 if len(best) > 0 else 0
    print(f"{b:<8} {ac:>14,} {bc:>14,} {pct:>9.2f}%")

# Summary aggregates
for label, floorname in [("B4-and-above", "B4"), ("B5-and-above", "B5"),
                          ("B4-and-below", "B4_below"), ("B5-below", "B5_below")]:
    if floorname == "B4":
        subset = confirmed[confirmed["NMS_PER_num"] >= 30]
        best_sub = best[best["NMS_PER_num"] >= 30]
    elif floorname == "B5":
        subset = confirmed[confirmed["NMS_PER_num"] >= 40]
        best_sub = best[best["NMS_PER_num"] >= 40]
    elif floorname == "B4_below":
        subset = confirmed[confirmed["NMS_PER_num"] < 30]
        best_sub = best[best["NMS_PER_num"] < 30]
    elif floorname == "B5_below":
        subset = confirmed[confirmed["NMS_PER_num"] < 40]
        best_sub = best[best["NMS_PER_num"] < 40]

    print(f"\n{label:<20} All: {len(subset):>8,} | Best-record: {len(best_sub):>8,} "
          f"({len(best_sub)/len(best)*100:.2f}% of best-record)")

# ═════════════════════════════════════════════════════════════════
# STEP 2 — Match Uniqueness Analysis
# ═════════════════════════════════════════════════════════════════
print("\n\n" + "=" * 60)
print("B. Match Cardinality / Uniqueness Analysis")
print("=" * 60)

# Check what match methods exist
print("\nPLE_MATCH_METHOD distribution (all confirmed):")
print(confirmed["PLE_MATCH_METHOD"].value_counts(dropna=False))
print("\nPLE_MATCH_METHOD distribution (best-record):")
print(best["PLE_MATCH_METHOD"].value_counts(dropna=False))

# 1. Unique NMAT PERSONKEY values per PLE record (one-to-many)
# We need to examine: For each PERSON_KEY, how many PLE records? 
# But we don't have a PLE identifier in this dataset. Let's check PLE_YEAR_PASSED as proxy.
# Actually, we need to understand the nature of the matching from the data available.

# For best records: each PERSON_KEY should be unique (IS_BEST_NMAT_RECORD ensures this)
print(f"\nUnique PERSONKEY in best-record confirmed: {best['PERSON_KEY'].nunique():,}")
print(f"Total best-record confirmed rows: {len(best):,}")
print(f"Duplicated PERSONKEY? {best['PERSON_KEY'].duplicated().sum()}")

# Check: how many best-record confirmed passers have the same PERSON_KEY appearing
# in the NON-best records (i.e., multiple NMAT attempts linked to PLE)
personkey_in_best = set(best["PERSON_KEY"].unique())
non_best_confirmed = confirmed[confirmed["IS_BEST_NMAT_RECORD"] == False]
non_best_same_person = non_best_confirmed[non_best_confirmed["PERSON_KEY"].isin(personkey_in_best)]
print(f"\nConfirmed passers with multiple NMAT attempts (non-best rows): {len(non_best_same_person):,}")

# 2. Number of PLE records per PERSON_KEY
# For each person (PERSON_KEY), count how many rows they have
person_counts = confirmed.groupby("PERSON_KEY").size()
print(f"\nPLE rows per PERSON_KEY (confirmed passers):")
print(f"  Exactly 1 row:  {(person_counts == 1).sum():,} persons")
print(f"  2+ rows:        {(person_counts > 1).sum():,} persons")
print(f"  Max rows:       {person_counts.max()}")

# 3. Number of unique APPNO_CLEAN per PERSON_KEY
appnos_per_person = confirmed.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique()
multiple_appnos = (appnos_per_person > 1).sum()
print(f"\nPersons with multiple APPNO_CLEAN values: {multiple_appnos:,}")

# 4. Number of PLE records per APPNO_CLEAN (should be one for clean matching)
ple_per_appno = confirmed.groupby("APPNO_CLEAN").size()
print(f"\nPLE records per APPNO_CLEAN:")
print(f"  Exactly 1:      {(ple_per_appno == 1).sum():,} appnos")
print(f"  2+ records:     {(ple_per_appno > 1).sum():,} appnos")
if (ple_per_appno > 1).sum() > 0:
    print(f"  Max:            {ple_per_appno.max()}")
    multi_appno_examples = ple_per_appno[ple_per_appno > 1].head(10)
    print(f"  Examples of appnos with multiple PLE records:")
    for appno, cnt in multi_appno_examples.items():
        subset = confirmed[confirmed["APPNO_CLEAN"] == appno]
        print(f"    AppNo {appno}: {cnt} records, years: {list(subset['Year'].values)}, "
              f"personkeys: {list(subset['PERSON_KEY'].values)}")

# 5. PLE_MATCH_METHOD by uniqueness
print("\nMatch method breakdown (best-record):")
print(best["PLE_MATCH_METHOD"].value_counts())

# ═════════════════════════════════════════════════════════════════
# STEP 3 — Audit Low-Score Confirmed Passers (below B5 = < 40th %ile)
# ═════════════════════════════════════════════════════════════════
print("\n\n" + "=" * 60)
print("C. Low-Score (< B5 / <40th %ile) Confirmed Passers Audit")
print("=" * 60)

low_best = best[best["NMS_PER_num"] < 40].copy()
print(f"\nBest-record confirmed passers below B5 (<40th %ile): {len(low_best):,}")

# Also check below B4 (<30th %ile)
low_b4_best = best[best["NMS_PER_num"] < 30].copy()
print(f"Best-record confirmed passers below B4 (<30th %ile): {len(low_b4_best):,}")

# For each low-score person, check if they have multiple NMAT attempts
low_personkeys = set(low_best["PERSON_KEY"].unique())
all_low_persons = confirmed[confirmed["PERSON_KEY"].isin(low_personkeys)].copy()

print(f"\nLow-score persons with multiple NMAT attempts:")
multi_attempt_low = all_low_persons.groupby("PERSON_KEY").size()
multi_attempt_low = multi_attempt_low[multi_attempt_low > 1]
print(f"  {len(multi_attempt_low)} persons have 2+ NMAT attempts")
print(f"  {len(low_personkeys) - len(multi_attempt_low)} have only 1 NMAT attempt")

# For repeat takers: compare linked attempt with highest-percentile attempt
def analyze_repeat_taker(person_df, person_key):
    """Analyze a repeat taker's NMAT records."""
    best_record = person_df[person_df["IS_BEST_NMAT_RECORD"] == True].iloc[0]
    all_records = person_df.sort_values("Year")
    
    linked_pct = best_record["NMS_PER_num"]
    linked_year = best_record["Year"]
    linked_appno = best_record["APPNO_CLEAN"]
    
    # Highest percentile attempt (any row)
    max_pct_row = person_df.loc[person_df["NMS_PER_num"].idxmax()]
    highest_pct = max_pct_row["NMS_PER_num"]
    highest_pct_year = max_pct_row["Year"]
    
    # Latest attempt
    latest_row = person_df.loc[person_df["Year"].idxmax()]
    latest_pct = latest_row["NMS_PER_num"]
    latest_year = latest_row["Year"]
    
    # Check if linked attempt is NOT the highest
    is_not_highest = linked_pct < highest_pct if pd.notna(linked_pct) and pd.notna(highest_pct) else False
    
    return {
        "PERSON_KEY": person_key,
        "linked_pct": linked_pct,
        "linked_year": linked_year,
        "linked_appno": linked_appno,
        "highest_pct": highest_pct,
        "highest_pct_year": highest_pct_year,
        "latest_pct": latest_pct,
        "latest_year": latest_year,
        "num_attempts": len(person_df),
        "is_not_highest": is_not_highest,
        "pct_diff": highest_pct - linked_pct if pd.notna(linked_pct) and pd.notna(highest_pct) else np.nan,
    }

repeat_analysis = []
for pk in low_personkeys:
    person_df = confirmed[confirmed["PERSON_KEY"] == pk]
    analysis = analyze_repeat_taker(person_df, pk)
    repeat_analysis.append(analysis)

repeat_df = pd.DataFrame(repeat_analysis)
print(f"\nRepeat-taker analysis for low-score passers:")
print(f"  Total low-score persons analyzed: {len(repeat_df)}")
print(f"  Linked attempt is NOT highest: {repeat_df['is_not_highest'].sum():,} "
      f"({repeat_df['is_not_highest'].mean()*100:.1f}%)")
print(f"  Linked attempt IS highest: {(~repeat_df['is_not_highest']).sum():,} "
      f"({(~repeat_df['is_not_highest']).mean()*100:.1f}%)")

if len(repeat_df) > 0:
    print(f"\n  Mean %ile diff (highest - linked): {repeat_df['pct_diff'].mean():.1f}")
    print(f"  Median %ile diff: {repeat_df['pct_diff'].median():.1f}")
    print(f"  Max %ile diff: {repeat_df['pct_diff'].max():.1f}")

# NMAT-to-PLE year gap analysis for low-score
low_best_with_gap = low_best[low_best["PLE_YEAR_GAP"].notna()].copy()
print(f"\nPLE Year Gap analysis for low-score passers:")
print(f"  Records with gap info: {len(low_best_with_gap):,}")
print(f"  Negative gaps (<0): {(low_best_with_gap['PLE_YEAR_GAP'] < 0).sum()}")
print(f"  Zero gaps (=0): {(low_best_with_gap['PLE_YEAR_GAP'] == 0).sum()}")
print(f"  Under 5 years (<5): {((low_best_with_gap['PLE_YEAR_GAP'] > 0) & (low_best_with_gap['PLE_YEAR_GAP'] < 5)).sum()}")
print(f"  Normal (5-10): {((low_best_with_gap['PLE_YEAR_GAP'] >= 5) & (low_best_with_gap['PLE_YEAR_GAP'] <= 10)).sum()}")
print(f"  Long (>10): {(low_best_with_gap['PLE_YEAR_GAP'] > 10).sum()}")

if len(low_best_with_gap) > 0:
    print(f"  Min gap: {low_best_with_gap['PLE_YEAR_GAP'].min():.0f}")
    print(f"  Max gap: {low_best_with_gap['PLE_YEAR_GAP'].max():.0f}")

# Check PLE_MATCH_METHOD for low-score records
print(f"\nMatch method (low-score best-record):")
print(low_best["PLE_MATCH_METHOD"].value_counts())

# ═════════════════════════════════════════════════════════════════
# STEP 4 — Validity Classification
# ═════════════════════════════════════════════════════════════════
print("\n\n" + "=" * 60)
print("D. Validity Classification - All Best-Record Confirmed")
print("=" * 60)

def classify_validity(row, person_df_all):
    """
    Classify each best-record row into mutually exclusive categories.
    
    Categories:
    - valid_unique: one NMAT person, one appno, one PLE record; no conflict
    - valid_repeat_taker: unique deterministic PLE match, but linked NMAT 
      attempt is lower than person's highest NMAT attempt
    - ambiguous_multiple: one-to-many, many-to-one, or many-to-many
    - data_quality: malformed identifiers, impossible chronology, duplicate PLE linkage
    - insufficient_info: can't determine uniqueness
    """
    pk = row["PERSON_KEY"]
    appno = row["APPNO_CLEAN"]
    method = row["PLE_MATCH_METHOD"]
    
    # Check for data quality concerns
    gap = row.get("PLE_YEAR_GAP", np.nan)
    year = row.get("Year", np.nan)
    
    data_quality_flags = []
    
    # Negative year gap is impossible
    if pd.notna(gap) and gap < 0:
        data_quality_flags.append(f"negative_year_gap({gap:.0f})")
    
    # Zero year gap is suspicious (med school takes at least 4 years)
    if pd.notna(gap) and gap == 0:
        data_quality_flags.append(f"zero_year_gap")
    
    # Check if appno looks malformed
    if pd.notna(appno):
        if len(str(appno)) < 6:
            data_quality_flags.append(f"short_appno({len(str(appno))}digits)")
    
    # Check if same PERSON_KEY has multiple PLE years (duplicate PLE linkage)
    person_records = person_df_all[person_df_all["PERSON_KEY"] == pk]
    unique_ple_years = person_records["PLE_YEAR_PASSED"].nunique()
    if unique_ple_years > 1:
        data_quality_flags.append(f"multiple_ple_years({unique_ple_years})")
    
    if data_quality_flags:
        return "data_quality", "; ".join(data_quality_flags)
    
    # Check match cardinality
    # Same appno matched to multiple people?
    all_best = person_df_all[person_df_all["IS_BEST_NMAT_RECORD"] == True]
    same_appno_persons = all_best[all_best["APPNO_CLEAN"] == appno]["PERSON_KEY"].nunique()
    
    if same_appno_persons > 1:
        return "ambiguous_multiple", f"appno_{appno}_shared_by_{same_appno_persons}_persons"
    
    # Check if this person has multiple appnos
    person_appnos = person_records["APPNO_CLEAN"].nunique()
    if person_appnos > 1:
        return "ambiguous_multiple", f"person_{pk[:20]}...has_{person_appnos}_appnos"
    
    # Check if there are multiple PLE match methods for this person
    person_methods = person_records["PLE_MATCH_METHOD"].nunique()
    if person_methods > 1:
        return "ambiguous_multiple", f"conflicting_match_methods_{list(person_records['PLE_MATCH_METHOD'].unique())}"
    
    # For repeat takers: check if linked attempt is not the highest
    n_attempts = len(person_records)
    if n_attempts > 1:
        linked_pct = row["NMS_PER_num"]
        all_pcts = person_records["NMS_PER_num"].dropna()
        if len(all_pcts) > 1:
            highest_pct = all_pcts.max()
            if pd.notna(linked_pct) and pd.notna(highest_pct) and linked_pct < highest_pct:
                return "valid_repeat_taker", f"linked_{linked_pct:.0f}pct_vs_highest_{highest_pct:.0f}pct_({n_attempts}attempts)"
    
    return "valid_unique", "single_exact_deterministic_match"

# Run classification on ALL best-record confirmed passers
classifications = []
reasons = []
for idx, row in best.iterrows():
    cat, reason = classify_validity(row, confirmed)
    classifications.append(cat)
    reasons.append(reason)

best["VALIDITY_CLASS"] = classifications
best["VALIDITY_REASON"] = reasons

# Summary
print("\nValidity Classification Summary (ALL best-record confirmed passers):")
vc_counts = best["VALIDITY_CLASS"].value_counts()
for cat, cnt in vc_counts.items():
    print(f"  {cat:<30} {cnt:>8,} ({cnt/len(best)*100:>5.1f}%)")

# By score band
print("\nValidity Classification by Score Band:")
ct = pd.crosstab(best["BAND"], best["VALIDITY_CLASS"])
print(ct.to_string())

# By match method
print("\nValidity Classification by PLE_MATCH_METHOD:")
ct2 = pd.crosstab(best["PLE_MATCH_METHOD"], best["VALIDITY_CLASS"])
print(ct2.to_string())

# ═════════════════════════════════════════════════════════════════
# STEP 5 — Focused analysis: LOW SCORE (< B5)
# ═════════════════════════════════════════════════════════════════
print("\n\n" + "=" * 60)
print("E. Focused: Low-Score (< B5 / <40th %ile) Validity Detail")
print("=" * 60)

low_class = best[best["NMS_PER_num"] < 40]["VALIDITY_CLASS"].value_counts()
print(f"\nLow-score (<40th %ile) validity breakdown:")
for cat, cnt in low_class.items():
    print(f"  {cat:<30} {cnt:>8,} ({cnt/len(best[best['NMS_PER_num']<40])*100:>5.1f}%)")

# Very low score (< B4 / <30th %ile)
vlow_class = best[best["NMS_PER_num"] < 30]["VALIDITY_CLASS"].value_counts()
print(f"\nVery low-score (<30th %ile) validity breakdown:")
for cat, cnt in vlow_class.items():
    print(f"  {cat:<30} {cnt:>8,} ({cnt/len(best[best['NMS_PER_num']<30])*100:>5.1f}%)")

# ═════════════════════════════════════════════════════════════════
# STEP 6 — Deliverable D: Compare PLE linkage before/after exclusion
# ═════════════════════════════════════════════════════════════════
print("\n\n" + "=" * 60)
print("F. PLE-Linkage: Before vs After Excluding Anomalous Records")
print("=" * 60)

# Before exclusion: all best-record confirmed passers
before = best.copy()

# After exclusion: exclude ambiguous_multiple and data_quality
exclude_classes = {"ambiguous_multiple", "data_quality", "insufficient_info"}
after = best[~best["VALIDITY_CLASS"].isin(exclude_classes)].copy()

print(f"\nBefore exclusion: {len(before):,} best-record confirmed passers")
print(f"After exclusion (removed ambiguous + data quality): {len(after):,} "
      f"(removed {len(before)-len(after):,})")

# B4-to-B5 gradient
def calc_gradient(df_subset, label):
    total = len(df_subset)
    if total == 0:
        return
    b4_above = (df_subset["NMS_PER_num"] >= 30).sum()
    b5_above = (df_subset["NMS_PER_num"] >= 40).sum()
    b4_below = (df_subset["NMS_PER_num"] < 30).sum()
    b5_below = (df_subset["NMS_PER_num"] < 40).sum()
    b4_to_b5 = (df_subset["NMS_PER_num"] >= 30) & (df_subset["NMS_PER_num"] < 40)
    b4_b5_count = b4_to_b5.sum()
    
    print(f"\n{label}:")
    print(f"  Total: {total:,}")
    print(f"  >= B4 (30th):  {b4_above:>8,} ({b4_above/total*100:>5.1f}%)")
    print(f"  >= B5 (40th):  {b5_above:>8,} ({b5_above/total*100:>5.1f}%)")
    print(f"  < B4 (<30th):  {b4_below:>8,} ({b4_below/total*100:>5.1f}%)")
    print(f"  < B5 (<40th):  {b5_below:>8,} ({b5_below/total*100:>5.1f}%)")
    print(f"  B4-to-B5 band:{b4_b5_count:>8,} ({b4_b5_count/total*100:>5.1f}%)")
    print(f"  B4/B5 gradient (B4 above - B5 above): {b4_above - b5_above:>6,} "
          f"({(b4_above-b5_above)/total*100:>5.1f}pp)")

calc_gradient(before, "Before exclusion")
calc_gradient(after, "After exclusion (clean only)")

# ═════════════════════════════════════════════════════════════════
# STEP 7 — Generate De-identified Exception Table
# ═════════════════════════════════════════════════════════════════
print("\n\n" + "=" * 60)
print("G. De-identified Exception Table")
print("=" * 60)

exceptions = best[best["VALIDITY_CLASS"].isin(["ambiguous_multiple", "data_quality"])].copy()

def hash_id(val):
    if pd.isna(val):
        return "NA"
    return hashlib.md5(str(val).encode()).hexdigest()[:12]

exceptions["HASHED_PERSON"] = exceptions["PERSON_KEY"].apply(hash_id)
exceptions["HASHED_APPNO"] = exceptions["APPNO_CLEAN"].apply(hash_id)

print(f"\nTotal exception records: {len(exceptions):,}")
print(f"  Ambiguous multiple: {(exceptions['VALIDITY_CLASS']=='ambiguous_multiple').sum():,}")
print(f"  Data quality: {(exceptions['VALIDITY_CLASS']=='data_quality').sum():,}")

# Show representative sample (20 rows max)
sample_cols = ["HASHED_PERSON", "HASHED_APPNO", "BAND", "NMS_PER_num", 
               "Year", "PLE_YEAR_PASSED", "PLE_YEAR_GAP", 
               "PLE_MATCH_METHOD", "VALIDITY_CLASS", "VALIDITY_REASON"]
print(f"\nException details (showing up to 50 rows):")
disp = exceptions[sample_cols].head(50).copy()
disp.index = range(1, len(disp) + 1)
print(disp.to_string())

# ═════════════════════════════════════════════════════════════════
# STEP 8 — Match Cardinality Table
# ═════════════════════════════════════════════════════════════════
print("\n\n" + "=" * 60)
print("H. Match Cardinality Table")
print("=" * 60)

# One-to-one: one PERSON_KEY, one APPNO_CLEAN, one PLE record
# One-to-many (NMAT): one PERSON_KEY → multiple APPNO_CLEAN values
# Many-to-one (PLE): one APPNO_CLEAN → multiple PERSON_KEY values
# Many-to-many: multiple PERSON_KEY ↔ multiple APPNO_CLEAN

# For best-record confirmed passers
best_persons = best["PERSON_KEY"].nunique()
best_appnos = best["APPNO_CLEAN"].nunique()

# Check for shared appnos (many persons -> one appno)
shared_appnos = best.groupby("APPNO_CLEAN")["PERSON_KEY"].nunique()
many_to_one_appno = (shared_appnos > 1).sum()
print(f"\nBest-record confirmed passers:")
print(f"  Unique PERSON_KEYs: {best_persons:,}")
print(f"  Unique APPNO_CLEANs: {best_appnos:,}")
print(f"  APPNOs shared by multiple persons: {many_to_one_appno:,}")

if many_to_one_appno > 0:
    shared_appno_details = shared_appnos[shared_appnos > 1]
    print(f"\n  Shared appno examples:")
    for appno, n_persons in shared_appno_details.head(10).items():
        subset = best[best["APPNO_CLEAN"] == appno]
        pks = subset["PERSON_KEY"].tolist()
        print(f"    AppNo hash {hashlib.md5(str(appno).encode()).hexdigest()[:8]}: "
              f"{n_persons} persons, bands: {list(subset['BAND'].values)}")

# Check for persons with multiple appnos (one person -> many appnos)
person_multiple_appnos = best.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique()
one_to_many_person = (person_multiple_appnos > 1).sum()
print(f"\n  Persons with multiple APPNOs (in best-record): {one_to_many_person:,}")

# Check for persons with multiple PLE years
person_multiple_ple = best.groupby("PERSON_KEY")["PLE_YEAR_PASSED"].nunique()
one_to_many_ple = (person_multiple_ple > 1).sum()
print(f"  Persons with multiple PLE years (in best-record): {one_to_many_ple:,}")

# Full cardinality summary
print(f"\nMatch Cardinality Matrix (best-record confirmed):")
total_best = len(best)
one_to_one = total_best - (shared_appnos > 1).sum() - (person_multiple_appnos > 1).sum() 
# This is approximate since these can overlap
print(f"  Approximate one-to-one matches: {total_best - many_to_one_appno - one_to_many_person:,} "
      f"({(total_best - many_to_one_appno - one_to_many_person)/total_best*100:.1f}%)")
print(f"  One-to-many (person→appnos):    {one_to_many_person:,}")
print(f"  Many-to-one (appno→persons):   {many_to_one_appno:,}")

# ═════════════════════════════════════════════════════════════════
# STEP 9 — Aggregated Summary Tables
# ═════════════════════════════════════════════════════════════════
print("\n\n" + "=" * 60)
print("I. Full Audit Summary Table")
print("=" * 60)

summary_rows = []
for band in band_order:
    band_data = best[best["BAND"] == band]
    total = len(band_data)
    if total == 0:
        continue
    vu = (band_data["VALIDITY_CLASS"] == "valid_unique").sum()
    vrt = (band_data["VALIDITY_CLASS"] == "valid_repeat_taker").sum()
    amb = (band_data["VALIDITY_CLASS"] == "ambiguous_multiple").sum()
    dq = (band_data["VALIDITY_CLASS"] == "data_quality").sum()
    insuf = (band_data["VALIDITY_CLASS"] == "insufficient_info").sum()
    
    summary_rows.append({
        "Band": band,
        "Total": total,
        "Valid_Unique": vu,
        "Valid_RepeatTaker": vrt,
        "Ambiguous_Multiple": amb,
        "Data_Quality": dq,
        "Insufficient_Info": insuf,
        "Anomalous_Total": amb + dq + insuf,
        "Anomalous_Pct": (amb + dq + insuf) / total * 100 if total > 0 else 0,
    })

summary_df = pd.DataFrame(summary_rows)
print(summary_df.to_string(index=False))

# Also aggregate by meaningful groups
print("\n\nAggregated Summary by Policy-Relevant Cut-offs:")
for label, mask_name in [
    ("All Bands", "all"),
    ("B4-and-above (>=30th)", "b4plus"),
    ("B5-and-above (>=40th)", "b5plus"),
    ("B4-and-below (<30th)", "b4minus"),
    ("B5-below (<40th)", "b5minus"),
]:
    if mask_name == "all":
        subset = best
    elif mask_name == "b4plus":
        subset = best[best["NMS_PER_num"] >= 30]
    elif mask_name == "b5plus":
        subset = best[best["NMS_PER_num"] >= 40]
    elif mask_name == "b4minus":
        subset = best[best["NMS_PER_num"] < 30]
    elif mask_name == "b5minus":
        subset = best[best["NMS_PER_num"] < 40]
    
    t = len(subset)
    if t == 0:
        continue
    vu = (subset["VALIDITY_CLASS"] == "valid_unique").sum()
    vrt = (subset["VALIDITY_CLASS"] == "valid_repeat_taker").sum()
    amb = (subset["VALIDITY_CLASS"] == "ambiguous_multiple").sum()
    dq = (subset["VALIDITY_CLASS"] == "data_quality").sum()
    insuf = (subset["VALIDITY_CLASS"] == "insufficient_info").sum()
    
    print(f"\n{label:<40} Total: {t:>6,}")
    print(f"  Valid unique:              {vu:>6,} ({vu/t*100:>5.1f}%)")
    print(f"  Valid repeat-taker:        {vrt:>6,} ({vrt/t*100:>5.1f}%)")
    print(f"  Ambiguous multiple:        {amb:>6,} ({amb/t*100:>5.1f}%)")
    print(f"  Data quality concern:      {dq:>6,} ({dq/t*100:>5.1f}%)")
    print(f"  Insufficient info:         {insuf:>6,} ({insuf/t*100:>5.1f}%)")
    print(f"  TOTAL ANOMALOUS:           {amb+dq+insuf:>6,} ({(amb+dq+insuf)/t*100:>5.1f}%)")

# ═════════════════════════════════════════════════════════════════
# STEP 10 — Deep Dive: The "~3,000 low-score passers" question
# ═════════════════════════════════════════════════════════════════
print("\n\n" + "=" * 60)
print("J. Deep Dive: The ~3,000 Low-Score Passers Question")
print("=" * 60)

# Count below-B5 in best-record confirmed
below_b5_best = best[best["NMS_PER_num"] < 40]
print(f"\nBest-record confirmed passers below B5 (<40th %ile): {len(below_b5_best):,}")

# If we look at ALL records (not just best-record), how many?
below_b5_all = confirmed[confirmed["NMS_PER_num"] < 40]
print(f"ALL confirmed passer records below B5: {len(below_b5_all):,}")

# Unique persons below B5
below_b5_persons = confirmed[confirmed["NMS_PER_num"] < 40]["PERSON_KEY"].nunique()
print(f"Unique persons below B5: {below_b5_persons:,}")

# Breakdown for best-record below-B5
print(f"\nBreakdown of below-B5 best-record passers:")
b5_below_class = below_b5_best["VALIDITY_CLASS"].value_counts()
for cat, cnt in b5_below_class.items():
    print(f"  {cat:<30} {cnt:>6,} ({cnt/len(below_b5_best)*100:>5.1f}%)")

# What if we look at B4-and-below?
below_b4_best = best[best["NMS_PER_num"] < 30]
print(f"\nBest-record below B4 (<30th %ile): {len(below_b4_best):,}")
b4_below_class = below_b4_best["VALIDITY_CLASS"].value_counts()
for cat, cnt in b4_below_class.items():
    print(f"  {cat:<30} {cnt:>6,} ({cnt/len(below_b4_best)*100:>5.1f}%)")

# ═════════════════════════════════════════════════════════════════
# STEP 11 — Check: How many low-score passers are unique deterministic matches?
# ═════════════════════════════════════════════════════════════════
print("\n\n" + "=" * 60)
print("K. Unique Deterministic Match Analysis (Below B5)")
print("=" * 60)

below_b5_unique = below_b5_best[below_b5_best["VALIDITY_CLASS"] == "valid_unique"]
below_b5_repeat = below_b5_best[below_b5_best["VALIDITY_CLASS"] == "valid_repeat_taker"]
below_b5_anom = below_b5_best[below_b5_best["VALIDITY_CLASS"].isin(["ambiguous_multiple", "data_quality"])]

print(f"\nBelow-B5 best-record breakdown:")
print(f"  Valid unique matches:              {len(below_b5_unique):,}")
print(f"  Valid repeat-taker linkages:       {len(below_b5_repeat):,}")
print(f"  Ambiguous/data-quality anomalies:  {len(below_b5_anom):,}")
print(f"  TOTAL below B5:                    {len(below_b5_best):,}")

# For repeat takers: what's the highest percentile they achieved?
print(f"\nRepeat-taker analysis (below B5 linked, {len(below_b5_repeat)} persons):")
if len(below_b5_repeat) > 0:
    repeat_pks = below_b5_repeat["PERSON_KEY"].unique()
    repeat_details = []
    for pk in repeat_pks:
        person_data = confirmed[confirmed["PERSON_KEY"] == pk]
        best_row = person_data[person_data["IS_BEST_NMAT_RECORD"] == True].iloc[0]
        all_pcts = person_data["NMS_PER_num"].dropna()
        highest_pct = all_pcts.max()
        repeat_details.append({
            "pk_hash": hash_id(pk),
            "linked_pct": best_row["NMS_PER_num"],
            "highest_pct": highest_pct,
            "linked_year": best_row["Year"],
            "n_attempts": len(person_data),
            "linked_method": best_row["PLE_MATCH_METHOD"],
        })
    repeat_detail_df = pd.DataFrame(repeat_details)
    print(f"  Mean linked percentile: {repeat_detail_df['linked_pct'].mean():.1f}")
    print(f"  Mean highest percentile: {repeat_detail_df['highest_pct'].mean():.1f}")
    print(f"  Above B5 in at least one attempt: {(repeat_detail_df['highest_pct'] >= 40).sum():,} "
          f"({(repeat_detail_df['highest_pct'] >= 40).mean()*100:.1f}%)")
    print(f"  Above B4 in at least one attempt: {(repeat_detail_df['highest_pct'] >= 30).sum():,}")
    print(f"  Method breakdown:")
    print(repeat_detail_df['linked_method'].value_counts().to_string())

# ═════════════════════════════════════════════════════════════════
# STEP 12 — Save Exception Table CSV
# ═════════════════════════════════════════════════════════════════
output_path = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\forensic_audit_exceptions.csv"
exceptions.to_csv(output_path, index=False)
print(f"\n\nException table saved to: {output_path}")

output_path2 = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\forensic_audit_summary.csv"
summary_df.to_csv(output_path2, index=False)
print(f"Summary table saved to: {output_path2}")

output_path3 = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\forensic_audit_repeat_takers.csv"
if len(below_b5_repeat) > 0:
    repeat_detail_df.to_csv(output_path3, index=False)
    print(f"Repeat taker details saved to: {output_path3}")

print("\n\n✅ AUDIT COMPLETE")
