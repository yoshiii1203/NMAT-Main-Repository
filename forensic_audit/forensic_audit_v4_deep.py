"""
Deep investigation of remaining anomalies
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
print(f"Best-record confirmed: {len(best):,}")

# ─── ANOMALY 1: Duplicate PERSON_KEYs in best-record ───
print("\n\n" + "="*70)
print("ANOMALY 1: Duplicate PERSON_KEYs in best-record")
print("="*70)
dup_pks = best["PERSON_KEY"][best["PERSON_KEY"].duplicated(keep=False)].unique()
print(f"Found {len(dup_pks)} PERSON_KEYs with duplicate best-record rows")
for pk in dup_pks:
    rows = best[best["PERSON_KEY"] == pk]
    h = hashlib.md5(str(pk).encode()).hexdigest()[:12]
    print(f"\n  Person {h}: {len(rows)} rows")
    for idx, r in rows.iterrows():
        print(f"    AppNo={r['APPNO_CLEAN']} Year={r['Year']} Pct={r['NMS_PER_num']} "
              f"PLE_Year={r['PLE_YEAR_PASSED']} Method={r['PLE_MATCH_METHOD']} "
              f"Gap={r['PLE_YEAR_GAP']} Band={r.get('BAND', '?')}")

    # Also show all their confirmed rows
    all_rows = confirmed[confirmed["PERSON_KEY"] == pk].sort_values("Year")
    print(f"  All confirmed rows for this person:")
    for idx, r in all_rows.iterrows():
        print(f"    {'BEST' if r['IS_BEST_NMAT_RECORD'] else '    '} "
              f"AppNo={r['APPNO_CLEAN']} Year={r['Year']} Pct={r['NMS_PER_num']} "
              f"PLE_Year={r['PLE_YEAR_PASSED']} Method={r['PLE_MATCH_METHOD']} "
              f"Gap={r['PLE_YEAR_GAP']}")

# ─── ANOMALY 2: Person with multiple PLE years ───
print("\n\n" + "="*70)
print("ANOMALY 2: Person with multiple PLE years")
print("="*70)
person_ple = best.groupby("PERSON_KEY")["PLE_YEAR_PASSED"].nunique()
multi = person_ple[person_ple > 1]
print(f"Found {len(multi)} person(s) with multiple PLE years")
for pk in multi.index:
    rows = best[best["PERSON_KEY"] == pk]
    h = hashlib.md5(str(pk).encode()).hexdigest()[:12]
    print(f"\n  Person {h}:")
    for idx, r in rows.iterrows():
        print(f"    Year={r['Year']} Pct={r['NMS_PER_num']} PLE_Year={r['PLE_YEAR_PASSED']} "
              f"Gap={r['PLE_YEAR_GAP']} Method={r['PLE_MATCH_METHOD']} AppNo={r['APPNO_CLEAN']}")

# ─── ANOMALY 3: Check for PLE year gaps that are < 5 years (below YEAR_GAP_MIN) ───
print("\n\n" + "="*70)
print("ANOMALY 3: Year gap < 5 years in best-record")
print("="*70)
short_gap = best[(best["PLE_YEAR_GAP"].notna()) & (best["PLE_YEAR_GAP"] < 5)]
print(f"Found {len(short_gap)} records with PLE_YEAR_GAP < 5 in best-record:")
for idx, r in short_gap.head(20).iterrows():
    h = hashlib.md5(str(r["PERSON_KEY"]).encode()).hexdigest()[:12]
    print(f"  Person {h} NMAT Year={r['Year']} PLE Year={r['PLE_YEAR_PASSED']} Gap={r['PLE_YEAR_GAP']} Pct={r['NMS_PER_num']}")

# ─── ANOMALY 4: Multiple appnos per person in best-record ───
print("\n\n" + "="*70)
print("ANOMALY 4: Person with multiple APPNOs in best-record (shouldn't happen)")
print("="*70)
pk_appno = best.groupby("PERSON_KEY")["APPNO_CLEAN"].nunique()
multi_appno_pks = pk_appno[pk_appno > 1]
print(f"Found {len(multi_appno_pks)} persons")
for pk in multi_appno_pks.index[:10]:
    rows = best[best["PERSON_KEY"] == pk]
    h = hashlib.md5(str(pk).encode()).hexdigest()[:12]
    print(f"  Person {h}: appnos={list(rows['APPNO_CLEAN'].values)}, years={list(rows['Year'].values)}, pcts={list(rows['NMS_PER_num'].values)}")

# ─── ANOMALY 5: PLE_YEAR_PASSED but no PLE_YEAR_GAP ───
print("\n\n" + "="*70)
print("ANOMALY 5: Missing PLE_YEAR_GAP when PLE_YEAR_PASSED exists")
print("="*70)
missing_gap = best[best["PLE_YEAR_PASSED"].notna() & best["PLE_YEAR_GAP"].isna()]
print(f"Found {len(missing_gap)} records with PLE year but no gap")
if len(missing_gap) > 0:
    print(f"  Year range: {missing_gap['Year'].min()} - {missing_gap['Year'].max()}")
    print(f"  PLE Year range: {missing_gap['PLE_YEAR_PASSED'].min()} - {missing_gap['PLE_YEAR_PASSED'].max()}")
    print(missing_gap["PLE_MATCH_METHOD"].value_counts().to_string())
    for idx, r in missing_gap.head(10).iterrows():
        h = hashlib.md5(str(r["PERSON_KEY"]).encode()).hexdigest()[:12]
        print(f"  Person {h} NMAT_Year={r['Year']} PLE_Year={r['PLE_YEAR_PASSED']} Method={r['PLE_MATCH_METHOD']} Pct={r['NMS_PER_num']}")

# ─── ANOMALY 6: Best-record persons with 0 PLE year (HOW did they get IS_BEST_NMAT_RECORD without PLE year?) ───
print("\n\n" + "="*70)
print("ANOMALY 6: Best-record confirmed but no PLE_YEAR_PASSED")
print("="*70)
no_ple_year = best[best["PLE_YEAR_PASSED"].isna()]
print(f"Found {len(no_ple_year)} records")
if len(no_ple_year) > 0:
    print(no_ple_year["PLE_MATCH_METHOD"].value_counts().to_string())
    for idx, r in no_ple_year.head(10).iterrows():
        h = hashlib.md5(str(r["PERSON_KEY"]).encode()).hexdigest()[:12]
        print(f"  Person {h} Year={r['Year']} Pct={r['NMS_PER_num']} Method={r['PLE_MATCH_METHOD']}")

# ─── COMPREHENSIVE CHECK: All reasons for PLE_YEAR_GAP being NA ───
print("\n\n" + "="*70)
print("COMPREHENSIVE: PLE_YEAR_GAP missing analysis")
print("="*70)
gap_na = best[best["PLE_YEAR_GAP"].isna()]
print(f"Total best-record with missing PLE_YEAR_GAP: {len(gap_na):,} ({len(gap_na)/len(best)*100:.1f}%)")
print(f"  Of these, with PLE_YEAR_PASSED present: {gap_na['PLE_YEAR_PASSED'].notna().sum():,}")
print(f"  Of these, with PLE_YEAR_PASSED missing: {gap_na['PLE_YEAR_PASSED'].isna().sum():,}")
print(f"\n  By match method:")
print(gap_na["PLE_MATCH_METHOD"].value_counts().to_string())

print("\n=== DEEP INVESTIGATION COMPLETE ===")
