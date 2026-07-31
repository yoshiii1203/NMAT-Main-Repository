"""
======================================================================
NMAT -> PLE Passer Forensic Audit v3 (refined classification)
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

obs = df[df["Year"] <= 2014].copy()
confirmed = obs[obs["IS_PLE_ANALYSIS_SAFE"] == True].copy()
best = confirmed[confirmed["IS_BEST_NMAT_RECORD"] == True].copy()
print(f"Observable: {len(obs):,} = Confirmed: {len(confirmed):,} = Best-record: {len(best):,}")

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

print("\n--- A. Audit Population by Score Band ---")
band_order = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","Missing"]
band_c = confirmed["BAND"].value_counts()
best_c = best["BAND"].value_counts()
print(f"{'Band':<8} {'All Confirmed':>14} {'Best Record':>14}")
print("-" * 40)
for b in band_order:
    a = band_c.get(b, 0)
    be = best_c.get(b, 0)
    if a > 0 or be > 0:
        print(f"{b:<8} {a:>14,} {be:>14,}")

for label, mask_fn in [("B4+ (>=30th)", lambda x: x["NMS_PER_num"] >= 30),
                        ("B5+ (>=40th)", lambda x: x["NMS_PER_num"] >= 40),
                        ("B4- (<30th)", lambda x: x["NMS_PER_num"] < 30),
                        ("B5- (<40th)", lambda x: x["NMS_PER_num"] < 40)]:
    n_conf = mask_fn(confirmed).sum()
    n_best = mask_fn(best).sum()
    print(f"  {label:<20} All: {n_conf:>8,} | Best: {n_best:>8,}")

print(f"\n--- B. Match Method ---")
print(best["PLE_MATCH_METHOD"].value_counts().to_string())

print(f"\n--- C. Match Cardinality ---")
# 1) Same APPNO matching multiple persons? (many-to-one)
appno_person_n = best.groupby("APPNO_CLEAN")["PERSON_KEY"].nunique()
shared_appnos = appno_person_n[appno_person_n > 1]
n_shared = len(shared_appnos)
print(f"APPNOs linked to >1 person: {n_shared}")
for appno, n_p in shared_appnos.head(10).items():
    rows = best[best["APPNO_CLEAN"] == appno]
    h = hashlib.md5(str(appno).encode()).hexdigest()[:8]
    print(f"  AppNo {h}: {n_p} persons, bands={list(rows['BAND'].values)}, years={list(rows['Year'].values)}")

# 2) Same PERSON_KEY linked to multiple distinct PLE records? (one-to-many PLE)
# We can check PLE_YEAR_PASSED uniqueness per person
person_ple_n = best.groupby("PERSON_KEY")["PLE_YEAR_PASSED"].nunique()
multi_ple = person_ple_n[person_ple_n > 1]
n_multi_ple = len(multi_ple)
print(f"\nPersons with multiple PLE years (best-record): {n_multi_ple}")
if n_multi_ple > 0:
    for pk, n_yr in multi_ple.head(10).items():
        rows = best[best["PERSON_KEY"] == pk]
        h = hashlib.md5(str(pk).encode()).hexdigest()[:10]
        print(f"  Person {h}: {n_yr} PLE years: {list(rows['PLE_YEAR_PASSED'].values)}")

# 3) ALL confirmed: rows per person (shows how many NMAT attempts linked)
all_pc = confirmed.groupby("PERSON_KEY").size()
print(f"\nAll confirmed: rows per person:")
print(f"  1: {(all_pc==1).sum():,}  2+: {(all_pc>1).sum():,}  Max: {all_pc.max()}")
n_persons = len(all_pc)
mult_attempt = (all_pc > 1).sum()
print(f"  => {mult_attempt:,} of {n_persons:,} persons ({mult_attempt/n_persons*100:.1f}%) have 2+ NMAT attempts linked to PLE")

# 4) Person-level APPNO uniqueness across ALL their attempts
person_appno_n_all = confirmed.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique()
multi_appno = (person_appno_n_all > 1).sum()
print(f"  Persons with >1 APPNO across attempts: {multi_appno:,} "
      f"({multi_appno/n_persons*100:.1f}%)")

# 5) Best-record: do any persons have multiple best-record rows? (they shouldn't)
print(f"\nBest-record: duplicated PERSON_KEY? {best['PERSON_KEY'].duplicated().sum()}")

print(f"\n--- D. Low-Score (< B5 / <40th) Audit ---")
low_best = best[best["NMS_PER_num"] < 40].copy()
print(f"Best-record below B5: {len(low_best):,}")
print(f"Best-record below B4 (<30th): {(best['NMS_PER_num'] < 30).sum():,}")

low_pks = set(low_best["PERSON_KEY"])
all_low = confirmed[confirmed["PERSON_KEY"].isin(low_pks)]
attempts = all_low.groupby("PERSON_KEY").size()
print(f"Unique persons below B5: {len(low_pks):,}")
print(f"  1 attempt:  {(attempts==1).sum():,}")
print(f"  2+ attempts: {(attempts>1).sum():,}")

# For each low person: compare linked vs highest, check gap, check match quality
low_details = []
for pk in low_pks:
    p_df = all_low[all_low["PERSON_KEY"] == pk].sort_values("Year")
    br = p_df[p_df["IS_BEST_NMAT_RECORD"] == True]
    if len(br) == 0:
        continue
    br = br.iloc[0]
    
    linked_pct = br["NMS_PER_num"]
    linked_year = br["Year"]
    linked_method = br["PLE_MATCH_METHOD"]
    linked_appno = br["APPNO_CLEAN"]
    gap = br["PLE_YEAR_PASSED"] - linked_year if (pd.notna(br["PLE_YEAR_PASSED"]) and pd.notna(linked_year)) else np.nan
    
    # Highest percentile across ALL attempts
    max_pct_idx = p_df["NMS_PER_num"].idxmax()
    max_pct = p_df.loc[max_pct_idx, "NMS_PER_num"]
    max_pct_year = p_df.loc[max_pct_idx, "Year"]
    
    # Latest attempt
    latest_row = p_df.iloc[-1]
    latest_pct = latest_row["NMS_PER_num"]
    latest_year = latest_row["Year"]
    
    is_not_highest = pd.notna(linked_pct) and pd.notna(max_pct) and linked_pct < max_pct
    pct_diff = max_pct - linked_pct if (pd.notna(linked_pct) and pd.notna(max_pct)) else np.nan
    
    # Check: is the linked APPNO shared by another person?
    appno_shared = appno_person_n.get(linked_appno, 1) > 1 if pd.notna(linked_appno) else False
    
    # Check: does this person appear with multiple PLE years?
    n_ple = p_df["PLE_YEAR_PASSED"].nunique()
    
    low_details.append({
        "pk_hash": hashlib.md5(str(pk).encode()).hexdigest()[:12],
        "linked_pct": linked_pct,
        "linked_year": linked_year,
        "linked_method": linked_method,
        "max_pct": max_pct,
        "max_pct_year": max_pct_year,
        "latest_pct": latest_pct,
        "latest_year": latest_year,
        "n_attempts": len(p_df),
        "is_not_highest": is_not_highest,
        "pct_diff": pct_diff,
        "gap": gap,
        "appno_shared": appno_shared,
        "n_ple_years": n_ple,
        "band": br["BAND"],
    })

low_df = pd.DataFrame(low_details)
print(f"\nAnalyzed {len(low_df)} low-score persons")

if len(low_df) > 0:
    print(f"   Repeat-taker: linked != highest: {low_df['is_not_highest'].sum():,} "
          f"({low_df['is_not_highest'].mean()*100:.1f}%)")
    print(f"   Mean/median/max pct_diff: {low_df['pct_diff'].mean():.1f} / "
          f"{low_df['pct_diff'].median():.1f} / {low_df['pct_diff'].max():.1f}")
    print(f"   Highest attempt >= B5: {(low_df['max_pct'] >= 40).sum():,} ({(low_df['max_pct'] >= 40).mean()*100:.1f}%)")
    print(f"   Highest attempt >= B4: {(low_df['max_pct'] >= 30).sum():,}")
    
    gaps = low_df["gap"].dropna()
    print(f"\n   Year gap: neg={(gaps<0).sum()} zero={(gaps==0).sum()} "
          f"<5={((gaps>0)&(gaps<5)).sum()} 5-10={((gaps>=5)&(gaps<=10)).sum()} >10={(gaps>10).sum()} "
          f"missing={low_df['gap'].isna().sum()}")
    
    print(f"\n   Appno shared across persons: {low_df['appno_shared'].sum():,}")
    print(f"   Multiple PLE years for person: {(low_df['n_ple_years']>1).sum():,}")
    print(f"   Linked method breakdown:")
    print(low_df["linked_method"].value_counts().to_string())

print(f"\n--- E. Refined Validity Classification ---")

# Build shared-appno lookup (from best)
appno_persons = best.groupby("APPNO_CLEAN")["PERSON_KEY"].nunique().to_dict()

val_classes = []
val_reasons = []

for idx, row in best.iterrows():
    pk = row["PERSON_KEY"]
    appno = row["APPNO_CLEAN"]
    gap = row["PLE_YEAR_GAP"]
    method = row["PLE_MATCH_METHOD"]
    pct = row["NMS_PER_num"]
    
    reasons = []
    
    # === Check: impossible year gap ===
    if pd.notna(gap) and gap < 0:
        val_classes.append("data_quality")
        val_reasons.append(f"negative_year_gap({gap:.0f})")
        continue
    if pd.notna(gap) and gap == 0:
        val_classes.append("data_quality")
        val_reasons.append("zero_year_gap")
        continue
    
    # === Check: same APPNO linked to multiple persons ===
    n_persons = appno_persons.get(appno, 0)
    if n_persons > 1:
        val_classes.append("ambiguous_multiple")
        val_reasons.append(f"appno_shared_by_{n_persons}_persons")
        continue
    
    # === Check: person linked to >1 PLE year (duplicate PLE record) ===
    p_conf = confirmed[confirmed["PERSON_KEY"] == pk]
    n_ple_yrs = p_conf["PLE_YEAR_PASSED"].nunique()
    if n_ple_yrs > 1:
        val_classes.append("data_quality")
        val_reasons.append(f"multiple_PLE_years({n_ple_yrs})")
        continue
    
    # === Determine if repeat-taker & linked != highest ===
    n_attempts = len(p_conf)
    if n_attempts > 1:
        all_pcts = p_conf["NMS_PER_num"].dropna()
        if len(all_pcts) > 1 and pd.notna(pct):
            highest_pct = all_pcts.max()
            if pct < highest_pct - 0.5:  # small tolerance
                val_classes.append("valid_repeat_taker")
                val_reasons.append(f"linked_{pct:.0f}pct_vs_highest_{highest_pct:.0f}pct_{n_attempts}attempts")
                continue
    
    # === Valid unique deterministic ===
    val_classes.append("valid_unique")
    val_reasons.append(f"single_{method}_{n_attempts}attempts")

best["VAL_CLASS"] = val_classes
best["VAL_REASON"] = val_reasons

vc = best["VAL_CLASS"].value_counts()
print(f"\n{'Category':<30} {'Count':>10} {'Pct':>8}")
print("-" * 50)
for cat, cnt in vc.items():
    print(f"{cat:<30} {cnt:>10,} {cnt/len(best)*100:>7.1f}%")

print(f"\nValidity by Score Band:")
ct = pd.crosstab(best["BAND"], best["VAL_CLASS"])
print(ct.to_string())

print(f"\nValidity by Match Method:")
ct2 = pd.crosstab(best["PLE_MATCH_METHOD"], best["VAL_CLASS"])
print(ct2.to_string())

print(f"\n--- F. Below-B5 Focused ---")
b5b = best[best["NMS_PER_num"] < 40]
for cat in ["valid_unique", "valid_repeat_taker", "ambiguous_multiple", "data_quality"]:
    n = (b5b["VAL_CLASS"]==cat).sum()
    print(f"  {cat:<30} {n:>6,} ({n/len(b5b)*100:.1f}%)")

b4b = best[best["NMS_PER_num"] < 30]
print(f"\nBelow-B4:")
for cat in ["valid_unique", "valid_repeat_taker", "ambiguous_multiple", "data_quality"]:
    n = (b4b["VAL_CLASS"]==cat).sum()
    print(f"  {cat:<30} {n:>6,} ({n/len(b4b)*100:.1f}%)")

print(f"\n--- G. Before vs After Exclusion ---")
exclude_set = {"ambiguous_multiple", "data_quality", "insufficient_info"}
before = best
after = best[~best["VAL_CLASS"].isin(exclude_set)].copy()
print(f"Before: {len(before):,} | After: {len(after):,} (removed {len(before)-len(after):,})")

for label, sub in [("Before", before), ("After", after)]:
    t = len(sub)
    if t == 0: continue
    b4ab = (sub["NMS_PER_num"] >= 30).sum()
    b5ab = (sub["NMS_PER_num"] >= 40).sum()
    b4bw = (sub["NMS_PER_num"] < 30).sum()
    b5bw = (sub["NMS_PER_num"] < 40).sum()
    b4b5 = ((sub["NMS_PER_num"] >= 30) & (sub["NMS_PER_num"] < 40)).sum()
    grad = b4ab - b5ab
    print(f"\n  {label}:")
    print(f"    Total: {t:,}")
    print(f"    >= B4: {b4ab:>8,} ({b4ab/t*100:.1f}%)")
    print(f"    >= B5: {b5ab:>8,} ({b5ab/t*100:.1f}%)")
    print(f"    < B4:  {b4bw:>8,} ({b4bw/t*100:.1f}%)")
    print(f"    < B5:  {b5bw:>8,} ({b5bw/t*100:.1f}%)")
    print(f"    B4-B5: {b4b5:>8,} ({b4b5/t*100:.1f}%)")
    print(f"    Gradient: {grad:>6,} ({grad/t*100:.1f}pp)")
    print(f"    B4/B5 ratio (B4+ / B5+): {b4ab/b5ab:.3f}" if b5ab > 0 else "    N/A")

print(f"\n--- H. Exception Table ---")
exc = best[best["VAL_CLASS"].isin(["ambiguous_multiple", "data_quality"])].copy()
print(f"Total: {len(exc):,} (ambiguous={ (exc['VAL_CLASS']=='ambiguous_multiple').sum():,}, data_quality={ (exc['VAL_CLASS']=='data_quality').sum():,})")
if len(exc) > 0:
    exc["HASH_APPNO"] = exc["APPNO_CLEAN"].apply(lambda x: hashlib.md5(str(x).encode()).hexdigest()[:8] if pd.notna(x) else "NA")
    exc["HASH_PERSON"] = exc["PERSON_KEY"].apply(lambda x: hashlib.md5(str(x).encode()).hexdigest()[:12])
    show = exc[["VAL_CLASS", "VAL_REASON", "HASH_APPNO", "HASH_PERSON", "BAND", "NMS_PER_num", "Year", "PLE_YEAR_GAP", "PLE_MATCH_METHOD"]].head(40)
    show.index = range(1, len(show)+1)
    print(f"\nFirst 40 exceptions:")
    print(show.to_string())

print(f"\n--- I. Summary Table by Band ---")
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
    sum_rows.append({"Band":band,"Total":t,"Valid_Unique":vu,"Valid_RepeatTaker":vrt,
                     "Ambiguous":amb,"DataQuality":dq,"Anomalous":anom,"Anom_Pct":anom/t*100})
pd.DataFrame(sum_rows).to_csv(r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\forensic_audit_summary.csv", index=False)
print(pd.DataFrame(sum_rows).to_string(index=False))

print(f"\n--- J. The ~3,000 Low-Score Passers Question ---")
n_b5 = len(best[best["NMS_PER_num"] < 40])
n_b4 = len(best[best["NMS_PER_num"] < 30])
print(f"Best-record below B5: {n_b5:,}")
print(f"Best-record below B4: {n_b4:,}")
print(f"\nBelow-B5 source of match:")
b5_methods = best[best["NMS_PER_num"] < 40]["PLE_MATCH_METHOD"].value_counts()
print(b5_methods.to_string())

# For below-B5: how many have 2+ NMAT attempts?
b5_pks = set(best[best["NMS_PER_num"] < 40]["PERSON_KEY"])
attempt_counts = confirmed[confirmed["PERSON_KEY"].isin(b5_pks)].groupby("PERSON_KEY").size()
n_b5_multi = (attempt_counts > 1).sum()
print(f"\nBelow-B5 with 2+ NMAT attempts: {n_b5_multi:,} ({n_b5_multi/n_b5*100:.1f}%)")

# Final clean numbers
clean_b5 = n_b5 - (best[best["NMS_PER_num"]<40]["VAL_CLASS"].isin(exclude_set)).sum()
clean_b4 = n_b4 - (best[best["NMS_PER_num"]<30]["VAL_CLASS"].isin(exclude_set)).sum()
print(f"Clean below B5 after excl anomalies: {clean_b5:,}/{n_b5:,} ({clean_b5/n_b5*100:.1f}%)")
print(f"Clean below B4 after excl anomalies: {clean_b4:,}/{n_b4:,} ({clean_b4/n_b4*100:.1f}%)")

# Save outputs
exc.to_csv(r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\forensic_audit_exceptions.csv", index=False)
if len(low_df) > 0:
    low_df.to_csv(r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\forensic_audit_low_score_details.csv", index=False)

# Full classified best-record
best.to_csv(r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\forensic_audit_classified.csv", index=False)
print(f"\n\nOutputs saved.")

print("\n=== AUDIT COMPLETE ===")
