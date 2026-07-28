"""
======================================================================
NMAT -> PLE Passer Forensic Audit v2 (optimized)
======================================================================
"""
import pandas as pd
import numpy as np
import hashlib
import warnings
warnings.filterwarnings("ignore")

DATA_PATH = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\streamlit_dashboard\CHED_relevant_dashboard\NMAT_Exodus.parquet"
df = pd.read_parquet(DATA_PATH)
print(f"Loaded: {len(df):,} rows, {len(df.columns)} cols")

# ===== STEP 1: Define audit population =====
obs = df[df["Year"] <= 2014].copy()
confirmed = obs[obs["IS_PLE_ANALYSIS_SAFE"] == True].copy()
best = confirmed[confirmed["IS_BEST_NMAT_RECORD"] == True].copy()
print(f"Observable cohort: {len(obs):,}")
print(f"Confirmed passers (IS_PLE_ANALYSIS_SAFE): {len(confirmed):,}")
print(f"Best-record: {len(best):,}")

# Score bands
def band_label(pct):
    if pd.isna(pct): return "Missing"
    if pct < 10: return "B1"
    if pct < 20: return "B2"
    if pct < 30: return "B3"
    if pct < 40: return "B4"
    if pct < 50: return "B5"
    if pct < 60: return "B6"
    if pct < 70: return "B7"
    if pct < 80: return "B8"
    if pct < 90: return "B9"
    return "B10"

confirmed["BAND"] = confirmed["NMS_PER_num"].map(band_label)
best["BAND"] = best["NMS_PER_num"].map(band_label)

print("\nA. Audit Population by Score Band:")
band_order = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10"]
band_c = confirmed["BAND"].value_counts()
best_c = best["BAND"].value_counts()
print(f"{'Band':<6} {'All Confirmed':>14} {'Best Record':>14}")
print("-" * 38)
for b in band_order:
    a = band_c.get(b, 0)
    be = best_c.get(b, 0)
    print(f"{b:<6} {a:>14,} {be:>14,}")

for label, mask in [("B4+ (>=30th)", confirmed["NMS_PER_num"] >= 30),
                     ("B5+ (>=40th)", confirmed["NMS_PER_num"] >= 40),
                     ("B4- (<30th)", confirmed["NMS_PER_num"] < 30),
                     ("B5- (<40th)", confirmed["NMS_PER_num"] < 40)]:
    n = mask.sum()
    n_best = (best["NMS_PER_num"] < 40 if "B5-" in label else 
              best["NMS_PER_num"] < 30 if "B4-" in label else
              best["NMS_PER_num"] >= 40 if "B5+" in label else
              best["NMS_PER_num"] >= 30).sum() if "best" not in label else 0
    print(f"  {label:<20} All: {n:>8,}  | Best: {n_best:>8,}")

# ===== STEP 2: Match Method =====
print("\n\nB. Match Method Distribution (best-record confirmed):")
print(best["PLE_MATCH_METHOD"].value_counts().to_string())

# ===== STEP 3: Cardinality Analysis =====
print("\n\nC. Match Cardinality Analysis:")
# PLE records per APPNO_CLEAN (in best-record)
ple_per_appno = best.groupby("APPNO_CLEAN").size()
print(f"\n  PLE records per APPNO_CLEAN:")
print(f"    1: {(ple_per_appno == 1).sum():>8,}")
print(f"    2+: {(ple_per_appno > 1).sum():>8,}")
if (ple_per_appno > 1).sum() > 0:
    max_shared = ple_per_appno.max()
    print(f"    Max per appno: {max_shared}")
    # Shared appnos
    shared = ple_per_appno[ple_per_appno > 1]
    for appno, cnt in shared.head(10).items():
        rows = best[best["APPNO_CLEAN"] == appno]
        print(f"      AppNo {hashlib.md5(str(appno).encode()).hexdigest()[:8]}: {cnt} records, "
              f"bands={list(rows['BAND'].values)}")

# Persons with multiple appnos (best-record)
person_appnos = best.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique()
multi_appno = (person_appnos > 1).sum()
print(f"\n  Persons with multiple APPNOs: {multi_appno:,}")

# PLE years per person (best-record)
person_ple_years = best.groupby("PERSON_KEY")["PLE_YEAR_PASSED"].nunique()
multi_ple = (person_ple_years > 1).sum()
print(f"  Persons with multiple PLE years: {multi_ple:,}")

# All confirmed: rows per person
all_person_counts = confirmed.groupby("PERSON_KEY").size()
print(f"\n  (All confirmed) PLE rows per PERSON_KEY:")
print(f"    1: {(all_person_counts == 1).sum():>8,}")
print(f"    2+: {(all_person_counts > 1).sum():>8,}")
print(f"    Max: {all_person_counts.max()}")

# ===== STEP 4: Low-score audit =====
print("\n\nD. Low-Score (< B5 / <40th %ile) Audit:")

low_best = best[best["NMS_PER_num"] < 40].copy()
low_pks = set(low_best["PERSON_KEY"])

# All records for these persons
all_low = confirmed[confirmed["PERSON_KEY"].isin(low_pks)]
attempts_per_low_person = all_low.groupby("PERSON_KEY").size()

print(f"  Best-record below B5: {len(low_best):,}")
print(f"  Unique persons below B5: {len(low_pks):,}")
print(f"  Persons with 1 attempt: {(attempts_per_low_person == 1).sum():,}")
print(f"  Persons with 2+ attempts: {(attempts_per_low_person > 1).sum():,}")

# For each low person, get linked vs highest vs latest
low_info = []
for pk in low_pks:
    p_df = confirmed[confirmed["PERSON_KEY"] == pk]
    br = p_df[p_df["IS_BEST_NMAT_RECORD"] == True]
    if len(br) == 0:
        continue
    br = br.iloc[0]
    linked_pct = br["NMS_PER_num"]
    linked_year = br["Year"]
    linked_method = br["PLE_MATCH_METHOD"]
    linked_appno = br["APPNO_CLEAN"]
    n_attempts = len(p_df)
    
    # Highest percentile
    max_pct = p_df["NMS_PER_num"].max()
    max_pct_row = p_df.loc[p_df["NMS_PER_num"].idxmax()] if pd.notna(max_pct) else None
    max_pct_year = max_pct_row["Year"] if max_pct_row is not None else np.nan
    
    # Latest
    latest_row = p_df.loc[p_df["Year"].idxmax()]
    latest_pct = latest_row["NMS_PER_num"]
    
    is_not_highest = (pd.notna(linked_pct) and pd.notna(max_pct) and linked_pct < max_pct)
    pct_diff = (max_pct - linked_pct) if (pd.notna(linked_pct) and pd.notna(max_pct)) else np.nan
    
    # Year gap
    gap = br.get("PLE_YEAR_GAP", np.nan)
    
    # Check if person has multiple appnos in their record
    n_appnos = p_df["APPNO_CLEAN"].nunique()
    n_ple_years = p_df["PLE_YEAR_PASSED"].nunique()
    
    low_info.append({
        "pk_hash": hashlib.md5(str(pk).encode()).hexdigest()[:12],
        "linked_pct": linked_pct,
        "linked_year": linked_year,
        "linked_method": linked_method,
        "max_pct": max_pct,
        "max_pct_year": max_pct_year,
        "latest_pct": latest_pct,
        "n_attempts": n_attempts,
        "n_appnos": n_appnos,
        "n_ple_years": n_ple_years,
        "is_not_highest": is_not_highest,
        "pct_diff": pct_diff,
        "gap": gap,
        "num_appnos_shared": (best["APPNO_CLEAN"] == linked_appno).sum() if pd.notna(linked_appno) else 0,
        "band": br["BAND"],
    })

low_df = pd.DataFrame(low_info)
print(f"  Analyzed {len(low_df)} low-score persons")

if len(low_df) > 0:
    print(f"\n  Repeat-taker analysis:")
    print(f"    Linked != Highest percentile: {low_df['is_not_highest'].sum():,} "
          f"({low_df['is_not_highest'].mean()*100:.1f}%)")
    print(f"    Linked IS Highest: {(~low_df['is_not_highest']).sum():,} "
          f"({(~low_df['is_not_highest']).mean()*100:.1f}%)")
    print(f"    Mean pct diff (max-linked): {low_df['pct_diff'].mean():.1f}")
    print(f"    Median pct diff: {low_df['pct_diff'].median():.1f}")
    print(f"    Max pct diff: {low_df['pct_diff'].max():.1f}")
    
    print(f"\n  Persons whose highest attempt >= B5: {(low_df['max_pct'] >= 40).sum():,} "
          f"({(low_df['max_pct'] >= 40).mean()*100:.1f}%)")
    print(f"  Persons whose highest attempt >= B4: {(low_df['max_pct'] >= 30).sum():,}")
    
    print(f"\n  Year gap distribution:")
    gaps = low_df["gap"].dropna()
    print(f"    Negative: {(gaps < 0).sum()}")
    print(f"    Zero: {(gaps == 0).sum()}")
    print(f"    <5 years: {((gaps > 0) & (gaps < 5)).sum()}")
    print(f"    5-10 years: {((gaps >= 5) & (gaps <= 10)).sum()}")
    print(f"    >10 years: {(gaps > 10).sum()}")
    print(f"    Missing: {low_df['gap'].isna().sum()}")
    
    print(f"\n  Persons with appno shared by multiple persons: {(low_df['num_appnos_shared'] > 1).sum():,}")
    print(f"  Persons with multiple PLE years: {(low_df['n_ple_years'] > 1).sum():,}")
    print(f"  Persons with multiple appnos: {(low_df['n_appnos'] > 1).sum():,}")

# ===== STEP 5: Validity Classification =====
print("\n\nE. Validity Classification (ALL best-record confirmed):")

# Pre-compute shared-appno lookup
appno_person_count = best.groupby("APPNO_CLEAN")["PERSON_KEY"].nunique().to_dict()

def classify(row, all_confirmed):
    pk = row["PERSON_KEY"]
    appno = row["APPNO_CLEAN"]
    gap = row["PLE_YEAR_GAP"]
    
    # Check data quality
    dq_flags = []
    if pd.notna(gap) and gap < 0:
        dq_flags.append(f"neg_gap({gap:.0f})")
    if pd.notna(gap) and gap == 0:
        dq_flags.append("zero_gap")
    
    # Same appno shared by multiple persons?
    n_persons_this_appno = appno_person_count.get(appno, 0)
    if n_persons_this_appno > 1:
        return "ambiguous_multiple", f"appno_shared_{n_persons_this_appno}_persons"
    
    # Person has multiple appnos?
    p_df = all_confirmed[all_confirmed["PERSON_KEY"] == pk]
    n_appnos = p_df["APPNO_CLEAN"].nunique()
    if n_appnos > 1:
        return "ambiguous_multiple", f"{n_appnos}_appnos_for_one_person"
    
    # Person has multiple PLE years?
    n_ple_yrs = p_df["PLE_YEAR_PASSED"].nunique()
    if n_ple_yrs > 1:
        dq_flags.append(f"multiple_ple_years({n_ple_yrs})")
    
    if dq_flags:
        return "data_quality", "; ".join(dq_flags)
    
    # Repeat taker?
    if len(p_df) > 1:
        linked_pct = row["NMS_PER_num"]
        all_pcts = p_df["NMS_PER_num"].dropna()
        if len(all_pcts) > 1 and pd.notna(linked_pct):
            highest_pct = all_pcts.max()
            if linked_pct < highest_pct:
                return "valid_repeat_taker", f"linked_{linked_pct:.0f}pct_highest_{highest_pct:.0f}pct_{len(p_df)}attempts"
    
    return "valid_unique", "single_deterministic_match"

# Run classification
class_list = []
reason_list = []
for idx, row in best.iterrows():
    cat, reason = classify(row, confirmed)
    class_list.append(cat)
    reason_list.append(reason)

best["VAL_CLASS"] = class_list
best["VAL_REASON"] = reason_list

# Summary
vc = best["VAL_CLASS"].value_counts()
print(f"\n{'Category':<30} {'Count':>10} {'Pct':>8}")
print("-" * 50)
for cat, cnt in vc.items():
    print(f"{cat:<30} {cnt:>10,} {cnt/len(best)*100:>7.1f}%")

# By band
print(f"\nValidity by Score Band:")
ct = pd.crosstab(best["BAND"], best["VAL_CLASS"])
print(ct.to_string())

# ===== STEP 6: Focused low-score =====
print(f"\n\nF. Focused: Below-B5 Validity:")
low_class = best[best["NMS_PER_num"] < 40]["VAL_CLASS"].value_counts()
for cat, cnt in low_class.items():
    print(f"  {cat:<30} {cnt:>6,} ({cnt/len(best[best['NMS_PER_num']<40])*100:.1f}%)")

print(f"\n  Below-B4 Validity:")
vlow_class = best[best["NMS_PER_num"] < 30]["VAL_CLASS"].value_counts()
for cat, cnt in vlow_class.items():
    print(f"  {cat:<30} {cnt:>6,} ({cnt/len(best[best['NMS_PER_num']<30])*100:.1f}%)")

# ===== STEP 7: Before vs After =====
print(f"\n\nG. PLE-Linkage: Before vs After Excluding Anomalous:")
exclude_set = {"ambiguous_multiple", "data_quality", "insufficient_info"}
before = best
after = best[~best["VAL_CLASS"].isin(exclude_set)].copy()

print(f"  Before: {len(before):,} | After: {len(after):,} (removed {len(before)-len(after):,})")

for label, sub in [("Before", before), ("After", after)]:
    t = len(sub)
    if t == 0: continue
    b4_ab = (sub["NMS_PER_num"] >= 30).sum()
    b5_ab = (sub["NMS_PER_num"] >= 40).sum()
    b4_bw = (sub["NMS_PER_num"] < 30).sum()
    b5_bw = (sub["NMS_PER_num"] < 40).sum()
    b4b5 = ((sub["NMS_PER_num"] >= 30) & (sub["NMS_PER_num"] < 40)).sum()
    print(f"\n  {label}:")
    print(f"    Total: {t:,}")
    print(f"    >= B4: {b4_ab:>8,} ({b4_ab/t*100:.1f}%)")
    print(f"    >= B5: {b5_ab:>8,} ({b5_ab/t*100:.1f}%)")
    print(f"    < B4:  {b4_bw:>8,} ({b4_bw/t*100:.1f}%)")
    print(f"    < B5:  {b5_bw:>8,} ({b5_bw/t*100:.1f}%)")
    print(f"    B4-B5: {b4b5:>8,} ({b4b5/t*100:.1f}%)")
    grad = b4_ab - b5_ab
    print(f"    Gradient (B4_above - B5_above): {grad:>6,} ({grad/t*100:.1f}pp)")

# ===== STEP 8: Exception table =====
print(f"\n\nH. Exception Table:")
exc = best[best["VAL_CLASS"].isin(["ambiguous_multiple", "data_quality"])].copy()
print(f"  Total exceptions: {len(exc):,}")
print(f"    Ambiguous: {(exc['VAL_CLASS']=='ambiguous_multiple').sum():,}")
print(f"    Data quality: {(exc['VAL_CLASS']=='data_quality').sum():,}")

sample_cols = ["VAL_CLASS", "VAL_REASON", "BAND", "NMS_PER_num", "Year", "PLE_YEAR_GAP", "PLE_MATCH_METHOD"]
disp = exc[sample_cols].head(30).copy()
disp.index = range(1, len(disp)+1)
print(f"\nSample exceptions (first 30):")
print(disp.to_string())

# ===== STEP 9: Summary table by band =====
print(f"\n\nI. Full Audit Summary Table:")
sum_rows = []
for band in band_order:
    bd = best[best["BAND"] == band]
    t = len(bd)
    if t == 0: continue
    vu = (bd["VAL_CLASS"]=="valid_unique").sum()
    vrt = (bd["VAL_CLASS"]=="valid_repeat_taker").sum()
    amb = (bd["VAL_CLASS"]=="ambiguous_multiple").sum()
    dq = (bd["VAL_CLASS"]=="data_quality").sum()
    ins = (bd["VAL_CLASS"]=="insufficient_info").sum()
    anom = amb + dq + ins
    sum_rows.append({"Band": band, "Total": t, "Valid_Unique": vu, "Valid_RepeatTaker": vrt,
                     "Ambiguous": amb, "DataQuality": dq, "Insufficient": ins, "Anomalous": anom,
                     "Anom_Pct": anom/t*100})

sum_df = pd.DataFrame(sum_rows)
print(sum_df.to_string(index=False))

# ===== STEP 10: The "~3000" question =====
print(f"\n\nJ. The ~3,000 Low-Score Passers Question:")
n_b5_below = len(best[best["NMS_PER_num"] < 40])
n_b4_below = len(best[best["NMS_PER_num"] < 30])
print(f"  Best-record confirmed below B5: {n_b5_below:,}")
print(f"  Best-record confirmed below B4: {n_b4_below:,}")

b5b = best[best["NMS_PER_num"] < 40]
print(f"\n  Below-B5 breakdown:")
for cat in ["valid_unique", "valid_repeat_taker", "ambiguous_multiple", "data_quality"]:
    n = (b5b["VAL_CLASS"]==cat).sum()
    print(f"    {cat:<30} {n:>6,} ({n/len(b5b)*100:.1f}%)")

b4b = best[best["NMS_PER_num"] < 30]
print(f"\n  Below-B4 breakdown:")
for cat in ["valid_unique", "valid_repeat_taker", "ambiguous_multiple", "data_quality"]:
    n = (b4b["VAL_CLASS"]==cat).sum()
    print(f"    {cat:<30} {n:>6,} ({n/len(b4b)*100:.1f}%)")

# Valid unique + repeat taker = clean matches
n_clean_b5b = len(b5b) - (b5b["VAL_CLASS"].isin(exclude_set)).sum()
n_clean_b4b = len(b4b) - (b4b["VAL_CLASS"].isin(exclude_set)).sum()
print(f"\n  Clean (after removing anomalous):")
print(f"    Below B5: {n_clean_b5b:,} / {n_b5_below:,} ({n_clean_b5b/n_b5_below*100:.1f}%)")
print(f"    Below B4: {n_clean_b4b:,} / {n_b4_below:,} ({n_clean_b4b/n_b4_below*100:.1f}%)")

# ===== STEP 11: Save outputs =====
out_dir = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis"
exc.to_csv(f"{out_dir}/forensic_audit_exceptions.csv", index=False)
sum_df.to_csv(f"{out_dir}/forensic_audit_summary.csv", index=False)
if len(low_df) > 0:
    low_df.to_csv(f"{out_dir}/forensic_audit_low_score_details.csv", index=False)
print(f"\n\nOutputs saved to {out_dir}/")

print("\n=== AUDIT COMPLETE ===")
