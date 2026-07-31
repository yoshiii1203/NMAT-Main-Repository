"""
======================================================================
NMAT → PLE Passer Forensic Audit — FINAL COMPREHENSIVE VERSION
======================================================================
"""
import pandas as pd
import numpy as np
import hashlib
import warnings
warnings.filterwarnings("ignore")

DATA_PATH = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\streamlit_dashboard\CHED_relevant_dashboard\NMAT_Exodus.parquet"
df = pd.read_parquet(DATA_PATH)
print(f"Loaded: {len(df):,} rows")

obs = df[df["Year"] <= 2014].copy()
confirmed = obs[obs["IS_PLE_ANALYSIS_SAFE"] == True].copy()
best = confirmed[confirmed["IS_BEST_NMAT_RECORD"] == True].copy()

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

# ════════════════════════════════════════════════════════════
# SECTION 1: AUDIT POPULATION
# ════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("1. AUDIT POPULATION")
print("="*70)
print(f"  Observable cohort (Year <= 2014): {len(obs):>8,}")
print(f"  IS_PLE_ANALYSIS_SAFE:              {len(confirmed):>8,}")
print(f"  IS_BEST_NMAT_RECORD:               {len(best):>8,}")

band_order = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","Missing"]
band_c = confirmed["BAND"].value_counts()
best_c = best["BAND"].value_counts()
print(f"\n  {'Band':<8} {'All Confirmed':>14} {'Best Record':>14}")
print("  " + "-"*38)
for b in band_order:
    a = band_c.get(b, 0)
    be = best_c.get(b, 0)
    if a > 0 or be > 0:
        print(f"  {b:<8} {a:>14,} {be:>14,}")

# Aggregates
for label, m in [("B4+ (>=30th %ile)", "ge30"), ("B5+ (>=40th %ile)", "ge40"),
                  ("B4- (<30th %ile)", "lt30"), ("B5- (<40th %ile)", "lt40")]:
    if m == "ge30": n = (best["NMS_PER_num"] >= 30).sum()
    elif m == "ge40": n = (best["NMS_PER_num"] >= 40).sum()
    elif m == "lt30": n = (best["NMS_PER_num"] < 30).sum()
    elif m == "lt40": n = (best["NMS_PER_num"] < 40).sum()
    print(f"  {label:<25} {n:>8,} ({n/len(best)*100:.1f}%)")

# ════════════════════════════════════════════════════════════
# SECTION 2: MATCH METHOD
# ════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("2. MATCH METHOD DISTRIBUTION")
print("="*70)
print(best["PLE_MATCH_METHOD"].value_counts().to_string())

# ════════════════════════════════════════════════════════════
# SECTION 3: MATCH CARDINALITY
# ════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("3. MATCH CARDINALITY")
print("="*70)

# A) APPNO to PERSON — many-to-one check
appno_person_n = best.groupby("APPNO_CLEAN")["PERSON_KEY"].nunique()
shared_appnos = appno_person_n[appno_person_n > 1]
print(f"\n  A) Same APPNO linked to >1 PERSON: {len(shared_appnos)}")

# B) PERSON to PLE year — one-to-many PLE check
person_ple_n = best.groupby("PERSON_KEY")["PLE_YEAR_PASSED"].nunique()
multi_ple = person_ple_n[person_ple_n > 1]
print(f"  B) Same PERSON with >1 PLE year: {len(multi_ple)}")
if len(multi_ple) > 0:
    for pk in multi_ple.index:
        rows = best[best["PERSON_KEY"] == pk]
        h = hashlib.md5(str(pk).encode()).hexdigest()[:12]
        print(f"     Person {h}: PLE years {list(rows['PLE_YEAR_PASSED'].values)}, "
              f"methods {list(rows['PLE_MATCH_METHOD'].values)}, "
              f"appnos {list(rows['APPNO_CLEAN'].values)}")

# C) Duplicate best-record PERSON_KEYs (should be 0)
dup_pks = best["PERSON_KEY"][best["PERSON_KEY"].duplicated(keep=False)].unique()
print(f"  C) Duplicate PERSON_KEY in best-record: {len(dup_pks)}")
if len(dup_pks) > 0:
    print(f"     {(len(dup_pks))} persons with 2+ best-record rows")
    total_extra_rows = 0
    for pk in dup_pks:
        total_extra_rows += len(best[best["PERSON_KEY"] == pk]) - 1
    print(f"     => {total_extra_rows} excess best-record rows (should be 0)")

# D) All-confirmed: rows per person
all_pc = confirmed.groupby("PERSON_KEY").size()
n_persons = len(all_pc)
n_multi = (all_pc > 1).sum()
print(f"  D) All confirmed: rows/person — 1: {(all_pc==1).sum():,}  "
      f"2+: {n_multi:,} ({n_multi/n_persons*100:.1f}%)  Max: {all_pc.max()}")

# E) Unique persons
print(f"  E) Unique persons (confirmed passers): {n_persons:,}")
print(f"     Unique persons (best-record): {best['PERSON_KEY'].nunique():,}")

# ════════════════════════════════════════════════════════════
# SECTION 4: LOW-SCORE DEEP DIVE
# ════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("4. LOW-SCORE (< B5 / <40th %ile) DEEP DIVE")
print("="*70)

low_best = best[best["NMS_PER_num"] < 40].copy()
print(f"  Best-record below B5: {len(low_best):,}")
print(f"  Below B4 (<30th): {(best['NMS_PER_num'] < 30).sum():,}")

low_pks = set(low_best["PERSON_KEY"])
all_low = confirmed[confirmed["PERSON_KEY"].isin(low_pks)]

# Attempts
att = all_low.groupby("PERSON_KEY").size()
print(f"  Unique persons below B5: {len(low_pks):,}")
print(f"    1 attempt:  {(att==1).sum():,}")
print(f"    2+ attempts: {(att>1).sum():,}")

# Per-person analysis
records = []
for pk in low_pks:
    p = all_low[all_low["PERSON_KEY"] == pk].sort_values("Year")
    br = p[p["IS_BEST_NMAT_RECORD"] == True]
    if len(br) == 0: continue
    br = br.iloc[0]
    
    lp = br["NMS_PER_num"]
    ly = br["Year"]
    lm = br["PLE_MATCH_METHOD"]
    la = br["APPNO_CLEAN"]
    gap = br["PLE_YEAR_GAP"]
    band = br["BAND"]
    
    # Max across ALL linked attempts
    max_pct = p["NMS_PER_num"].max()
    max_pct_row = p.loc[p["NMS_PER_num"].idxmax()] if pd.notna(max_pct) else None
    max_pct_year = max_pct_row["Year"] if max_pct_row is not None else None
    
    # Latest attempt
    lr = p.iloc[-1]
    lrp = lr["NMS_PER_num"]
    lry = lr["Year"]
    
    is_not_highest = pd.notna(lp) and pd.notna(max_pct) and lp < max_pct
    pct_diff = max_pct - lp if pd.notna(lp) and pd.notna(max_pct) else np.nan
    
    # Duplicate best-record flag
    is_dup_best = pk in dup_pks
    
    records.append({
        "pk_hash": hashlib.md5(str(pk).encode()).hexdigest()[:12],
        "linked_pct": lp, "linked_year": ly, "linked_method": lm,
        "max_pct": max_pct, "max_pct_year": max_pct_year,
        "latest_pct": lrp, "latest_year": lry,
        "n_attempts": len(p), "gap": gap, "band": band,
        "is_not_highest": is_not_highest, "pct_diff": pct_diff,
        "is_dup_best": is_dup_best,
    })

ldf = pd.DataFrame(records)
print(f"\n  Analyzed {len(ldf)} persons")

print(f"\n  Repeat-taker analysis:")
print(f"    Linked != highest: {ldf['is_not_highest'].sum():,} ({ldf['is_not_highest'].mean()*100:.1f}%)")
print(f"    Mean/median/max pct diff: {ldf['pct_diff'].mean():.1f}/{ldf['pct_diff'].median():.1f}/{ldf['pct_diff'].max():.1f}")
print(f"    Highest attempt >= B5: {(ldf['max_pct']>=40).sum():,} ({(ldf['max_pct']>=40).mean()*100:.1f}%)")
print(f"    Highest attempt >= B4: {(ldf['max_pct']>=30).sum():,}")
print(f"    Duplicate best-record: {ldf['is_dup_best'].sum():,}")

gaps = ldf["gap"].dropna()
print(f"\n  Year gap distribution:")
print(f"    Negative: {(gaps<0).sum()}  Zero: {(gaps==0).sum()}  "
      f"<5yr: {((gaps>0)&(gaps<5)).sum()}  5-10yr: {((gaps>=5)&(gaps<=10)).sum()}  "
      f">10yr: {(gaps>10).sum()}  Missing: {ldf['gap'].isna().sum()}")

print(f"\n  Linked method:")
print(ldf["linked_method"].value_counts().to_string())

# ════════════════════════════════════════════════════════════
# SECTION 5: VALIDITY CLASSIFICATION
# ════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("5. VALIDITY CLASSIFICATION")
print("="*70)

# Priority rules for duplicate best-record
# If a person has 2 best-record rows, the one WITHOUT PLE year is suspect
# (it's likely a MANUAL_APPNO_MATCH from PLE_UNMATCHED.csv that has no PLE data)
# The one WITH PLE year is more complete.

# Resolve duplicates: for duplicate PERSON_KEYs, keep only the row with
# PLE_YEAR_PASSED non-null (and if both have it, the one with higher IS_BEST_NMAT_RECORD)
best_deduped = best.copy()
best_deduped["_priority"] = 0
best_deduped.loc[best_deduped["PLE_YEAR_PASSED"].notna(), "_priority"] += 10
best_deduped = (best_deduped.sort_values(["PERSON_KEY", "_priority", "NMS_PER_num"],
                                          ascending=[True, False, False])
                .drop_duplicates(subset="PERSON_KEY", keep="first")
                .drop(columns=["_priority"]))
n_removed_dup = len(best) - len(best_deduped)
print(f"\n  Deduplicated best-record: {len(best_deduped):,} (removed {n_removed_dup} excess duplicate rows)")
print(f"  Deduplicated PERSON_KEYs: {best_deduped['PERSON_KEY'].nunique():,}")
print(f"  Duplicate PERSON_KEYs after dedup: {best_deduped['PERSON_KEY'].duplicated().sum()}")

# Now run classification on deduped
appno_person_n_deduped = best_deduped.groupby("APPNO_CLEAN")["PERSON_KEY"].nunique().to_dict()

val_classes = []
val_reasons = []
val_details = []

for idx, row in best_deduped.iterrows():
    pk = row["PERSON_KEY"]
    appno = row["APPNO_CLEAN"]
    gap = row["PLE_YEAR_GAP"]
    method = row["PLE_MATCH_METHOD"]
    pct = row["NMS_PER_num"]
    
    # === Data quality: impossible gap ===
    if pd.notna(gap) and gap < 0:
        val_classes.append("data_quality")
        val_reasons.append(f"negative_gap_{gap:.0f}")
        val_details.append("")
        continue
    if pd.notna(gap) and gap == 0:
        val_classes.append("data_quality")
        val_reasons.append("zero_gap")
        val_details.append("")
        continue
    
    # === Ambiguous: same APPNO → multiple persons ===
    n_persons = appno_person_n_deduped.get(appno, 0)
    if n_persons and n_persons > 1:
        val_classes.append("ambiguous_multiple")
        val_reasons.append(f"shared_appno_{n_persons}_persons")
        val_details.append("")
        continue
    
    # === Data quality: person with multiple PLE years ===
    p_conf = confirmed[confirmed["PERSON_KEY"] == pk]
    n_ple_yrs = p_conf["PLE_YEAR_PASSED"].nunique()
    if n_ple_yrs > 1:
        val_classes.append("data_quality")
        val_reasons.append(f"multiple_ple_years_{n_ple_yrs}")
        yr_list = sorted(p_conf["PLE_YEAR_PASSED"].dropna().unique())
        val_details.append(f"PLE_years={yr_list}")
        continue
    
    # === Had duplicate best-record row removed? ===
    if pk in set(dup_pks):
        val_classes.append("data_quality")
        val_reasons.append("duplicate_best_record_resolved")
        removed_rows = best[best["PERSON_KEY"] == pk]
        removed_info = [(r["Year"], r["NMS_PER_num"], r["PLE_MATCH_METHOD"], 
                        "has_PLE" if pd.notna(r["PLE_YEAR_PASSED"]) else "no_PLE") 
                        for _, r in removed_rows.iterrows()]
        val_details.append(f"dup_resolved_rows={removed_info}")
        continue
    
    # === Repeat taker: linked != highest ===
    n_attempts = len(p_conf)
    if n_attempts > 1:
        all_pcts = p_conf["NMS_PER_num"].dropna()
        if len(all_pcts) > 1 and pd.notna(pct):
            highest_pct = all_pcts.max()
            if pct < highest_pct - 0.5:
                val_classes.append("valid_repeat_taker")
                val_reasons.append(f"linked_{pct:.0f}_highest_{highest_pct:.0f}_{n_attempts}attempts")
                val_details.append("")
                continue
    
    # === Valid unique ===
    val_classes.append("valid_unique")
    val_reasons.append(f"single_{method}")
    val_details.append("")

best_deduped["VAL_CLASS"] = val_classes
best_deduped["VAL_REASON"] = val_reasons
best_deduped["VAL_DETAIL"] = val_details

# Summary
vc = best_deduped["VAL_CLASS"].value_counts()
print(f"\n  {'Category':<35} {'Count':>10} {'Pct':>8}")
print("  " + "-"*55)
for cat, cnt in vc.items():
    print(f"  {cat:<35} {cnt:>10,} {cnt/len(best_deduped)*100:>7.1f}%")

# By score band
print(f"\n  Validity by Score Band:")
ct = pd.crosstab(best_deduped["BAND"], best_deduped["VAL_CLASS"])
print(ct.to_string())

# By method
print(f"\n  Validity by Match Method:")
ct2 = pd.crosstab(best_deduped["PLE_MATCH_METHOD"], best_deduped["VAL_CLASS"])
print(ct2.to_string())

# ════════════════════════════════════════════════════════════
# SECTION 6: FOCUSED — LOW SCORE
# ════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("6. FOCUSED: LOW-SCORE VALIDITY")
print("="*70)

b5b = best_deduped[best_deduped["NMS_PER_num"] < 40]
b4b = best_deduped[best_deduped["NMS_PER_num"] < 30]

for label, sub in [("Below B5 (<40th %ile)", b5b), ("Below B4 (<30th %ile)", b4b)]:
    print(f"\n  {label}:")
    t = len(sub)
    for cat in ["valid_unique", "valid_repeat_taker", "ambiguous_multiple", "data_quality"]:
        n = (sub["VAL_CLASS"] == cat).sum()
        print(f"    {cat:<35} {n:>6,} ({n/t*100:.1f}%)" if t > 0 else f"    {cat:<35} {n:>6,}")

# ════════════════════════════════════════════════════════════
# SECTION 7: BEFORE VS AFTER EXCLUSION
# ════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("7. BEFORE vs AFTER EXCLUDING ANOMALOUS")
print("="*70)

exclude_set = {"ambiguous_multiple", "data_quality", "insufficient_info"}
before = best_deduped
after = best_deduped[~best_deduped["VAL_CLASS"].isin(exclude_set)].copy()
n_anom = len(before) - len(after)

print(f"\n  Before: {len(before):,} | After (clean): {len(after):,} (excluded {n_anom:,} anom. records)")

# Dedupe check: also compare against the ORIGINAL best (non-deduped)
original_best = best.copy()  # has duplicates
print(f"  Original best-record (with duplicates): {len(original_best):,}")

for label, sub in [("Original (with dupes)", original_best), ("Before exclusion", before), ("After exclusion (clean)", after)]:
    t = len(sub)
    if t == 0: continue
    b4ab = (sub["NMS_PER_num"] >= 30).sum()
    b5ab = (sub["NMS_PER_num"] >= 40).sum()
    b4bw = (sub["NMS_PER_num"] < 30).sum()
    b5bw = (sub["NMS_PER_num"] < 40).sum()
    b4b5 = ((sub["NMS_PER_num"] >= 30) & (sub["NMS_PER_num"] < 40)).sum()
    grad = b4ab - b5ab
    print(f"\n  {label}:")
    print(f"    Total:     {t:>8,}")
    print(f"    >= B4:     {b4ab:>8,} ({b4ab/t*100:.1f}%)")
    print(f"    >= B5:     {b5ab:>8,} ({b5ab/t*100:.1f}%)")
    print(f"    < B4:      {b4bw:>8,} ({b4bw/t*100:.1f}%)")
    print(f"    < B5:      {b5bw:>8,} ({b5bw/t*100:.1f}%)")
    print(f"    B4-B5 band:{b4b5:>8,} ({b4b5/t*100:.1f}%)")
    print(f"    Gradient:  {grad:>8,} ({grad/t*100:.1f}pp)")
    if b5ab > 0:
        print(f"    B4/B5 ratio: {b4ab/b5ab:.4f}")

# ════════════════════════════════════════════════════════════
# SECTION 8: EXCEPTION TABLE
# ════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("8. EXCEPTION TABLE (anomalous records)")
print("="*70)

exc = best_deduped[best_deduped["VAL_CLASS"].isin(["ambiguous_multiple", "data_quality"])].copy()
print(f"  Total exceptions: {len(exc):,}")
if len(exc) > 0:
    print(f"    Ambiguous: {(exc['VAL_CLASS']=='ambiguous_multiple').sum():,}")
    print(f"    Data quality: {(exc['VAL_CLASS']=='data_quality').sum():,}")
    
    exc["HASH_APPNO"] = exc["APPNO_CLEAN"].apply(lambda x: hashlib.md5(str(x).encode()).hexdigest()[:8] if pd.notna(x) else "NA")
    exc["HASH_PERSON"] = exc["PERSON_KEY"].apply(lambda x: hashlib.md5(str(x).encode()).hexdigest()[:12])
    
    show = exc[["VAL_CLASS", "VAL_REASON", "VAL_DETAIL", "HASH_APPNO", "HASH_PERSON", 
                "BAND", "NMS_PER_num", "Year", "PLE_YEAR_GAP", "PLE_MATCH_METHOD"]]
    show.index = range(1, len(show)+1)
    print(f"\n{show.to_string()}")

# ════════════════════════════════════════════════════════════
# SECTION 9: SUMMARY TABLE
# ════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("9. AUDIT SUMMARY TABLE")
print("="*70)

sum_rows = []
for band in band_order:
    bd = best_deduped[best_deduped["BAND"] == band]
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

sum_df = pd.DataFrame(sum_rows)
print(f"\n  {sum_df.to_string(index=False)}")

# Aggregated
print(f"\n  Aggregated by policy cut-offs:")
for label, sub in [("All bands", before), ("B4+ (>=30th)", before[before["NMS_PER_num"]>=30]),
                    ("B5+ (>=40th)", before[before["NMS_PER_num"]>=40]),
                    ("B4- (<30th)", before[before["NMS_PER_num"]<30]),
                    ("B5- (<40th)", before[before["NMS_PER_num"]<40])]:
    t = len(sub)
    anom = (sub["VAL_CLASS"].isin(exclude_set)).sum()
    print(f"    {label:<25} Total: {t:>6,}  Anomalous: {anom:>6,} ({anom/t*100:.1f}%)" if t > 0 else f"    {label:<25} Total: {t:>6,}")

# ════════════════════════════════════════════════════════════
# SECTION 10: THE ~3,000 QUESTION
# ════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("10. THE ~3,000 LOW-SCORE PASSERS QUESTION")
print("="*70)

n_b5 = len(b5b)
n_b4 = len(b4b)
print(f"\n  Best-record below B5 (<40th %ile): {n_b5:,}")
print(f"  Best-record below B4 (<30th %ile): {n_b4:,}")

# Methods
print(f"\n  Match methods (below B5):")
print(b5b["PLE_MATCH_METHOD"].value_counts().to_string())

# Validity breakdown
print(f"\n  Validity (below B5):")
for cat in ["valid_unique", "valid_repeat_taker", "ambiguous_multiple", "data_quality"]:
    n = (b5b["VAL_CLASS"] == cat).sum()
    print(f"    {cat:<35} {n:>6,} ({n/n_b5*100:.1f}%)")

# How many are repeat-takers?
b5_pks = set(b5b["PERSON_KEY"])
b5_att = confirmed[confirmed["PERSON_KEY"].isin(b5_pks)].groupby("PERSON_KEY").size()
b5_multi = (b5_att > 1).sum()
print(f"\n  Below B5 with 2+ NMAT attempts: {b5_multi:,} ({b5_multi/n_b5*100:.1f}%)")
print(f"  Below B5 with 1 NMAT attempt: {n_b5-b5_multi:,} ({(n_b5-b5_multi)/n_b5*100:.1f}%)")

# Impact on gradient
print(f"\n  Impact of exclusion on gradient:")
before_grad = (before["NMS_PER_num"]>=30).sum() - (before["NMS_PER_num"]>=40).sum()
after_grad = (after["NMS_PER_num"]>=30).sum() - (after["NMS_PER_num"]>=40).sum()
print(f"    Before exclusion: {before_grad:,} ({before_grad/len(before)*100:.1f}pp)")
print(f"    After exclusion:  {after_grad:,} ({after_grad/len(after)*100:.1f}pp)")
pct_change = (after_grad - before_grad) / before_grad * 100 if before_grad > 0 else 0
print(f"    Change: {after_grad - before_grad} ({pct_change:+.1f}%)")

# ════════════════════════════════════════════════════════════
# SECTION 11: CARDINALITY TABLE
# ════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("11. MATCH CARDINALITY TABLE")
print("="*70)

# One-to-one: 1 APPNO ↔ 1 PERSON, person has 1 PLE year
appno_counts = best_deduped.groupby("APPNO_CLEAN")["PERSON_KEY"].nunique()
person_appno = best_deduped.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique()
person_ple = best_deduped.groupby("PERSON_KEY")["PLE_YEAR_PASSED"].nunique()

n_1to1 = ((appno_counts == 1).sum() and 
          (person_appno == 1).sum() and 
          (person_ple == 1).sum())
# Better: count persons with exactly 1 appno and 1 PLE year
one_to_one_persons = (person_appno == 1).sum()
print(f"\n  One-to-one (1 person, 1 appno): {one_to_one_persons:,} persons")
print(f"  One-to-many (1 person, >1 appno): {(person_appno > 1).sum():,} persons")
print(f"  Many-to-one (1 appno, >1 person): {(appno_counts > 1).sum():,} appnos")
print(f"  Many-to-many: persons with >1 appno AND appno shared: N/A (none found)")

# ════════════════════════════════════════════════════════════
# SAVE OUTPUTS
# ════════════════════════════════════════════════════════════
outdir = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis"
best_deduped.to_csv(f"{outdir}/forensic_audit_classified.csv", index=False)
exc.to_csv(f"{outdir}/forensic_audit_exceptions.csv", index=False)
sum_df.to_csv(f"{outdir}/forensic_audit_summary.csv", index=False)
ldf.to_csv(f"{outdir}/forensic_audit_low_score_details.csv", index=False)

# Also save the validity counts as a portable table
vc_export = pd.DataFrame({
    "Category": vc.index,
    "Count": vc.values,
    "Percent": (vc.values / len(best_deduped) * 100).round(1)
})
vc_export.to_csv(f"{outdir}/forensic_audit_category_counts.csv", index=False)

print(f"\n\n  Outputs saved to {outdir}/")
print("\n" + "="*70)
print("AUDIT COMPLETE")
print("="*70)
