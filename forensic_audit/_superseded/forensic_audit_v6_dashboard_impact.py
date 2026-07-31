"""
Check impact on dashboard's clean PLE subset
"""
import pandas as pd, numpy as np, hashlib, warnings
warnings.filterwarnings("ignore")

df = pd.read_parquet(r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\streamlit_dashboard\CHED_relevant_dashboard\NMAT_Exodus.parquet")

# Dashboard's clean subset logic:
# df_best = df[df["IS_BEST_NMAT_RECORD"] == True]
# df_obs = df_best[df_best["Year"] <= 2014]
# _df_clean_ple = df_obs[df_obs["IS_PLE_ANALYSIS_SAFE"] == True) & (df_obs["PLE_YEAR_GAP"] >= 5) & (df_obs["FOREIGNER_STATUS"] == "Filipino")]

df_best = df[df["IS_BEST_NMAT_RECORD"] == True].copy()
print(f"df_best: {len(df_best):,} (includes {df_best['PERSON_KEY'].duplicated().sum()} duplicate persons)")
df_obs = df_best[df_best["Year"] <= 2014].copy()
print(f"df_obs: {len(df_obs):,}")

# Duplicates in best-record within observable cohort
dup_in_obs = df_obs[df_obs["PERSON_KEY"].duplicated(keep=False)]
n_dup_persons = dup_in_obs["PERSON_KEY"].nunique()
print(f"Duplicated persons in best-record (observable): {n_dup_persons}")
print(f"Duplicate rows in best-record (observable): {len(dup_in_obs)}")
print(f"Excess rows: {len(dup_in_obs) - n_dup_persons}")

# Clean subset
df_clean = df_obs[
    (df_obs["IS_PLE_ANALYSIS_SAFE"] == True) &
    (df_obs["PLE_YEAR_GAP"] >= 5) &
    (df_obs["FOREIGNER_STATUS"] == "Filipino")
].copy()
print(f"\nDashboard 'clean PLE subset': {len(df_clean):,}")

# Check if any duplicates in clean subset
dup_clean = df_clean["PERSON_KEY"].duplicated()
print(f"Duplicated persons in clean subset: {df_clean['PERSON_KEY'].duplicated().sum()}")

# Show them
if df_clean["PERSON_KEY"].duplicated().sum() > 0:
    dup_pks = df_clean["PERSON_KEY"][df_clean["PERSON_KEY"].duplicated(keep=False)].unique()
    print(f"\nAffected persons: {len(dup_pks)}")
    for pk in dup_pks:
        rows = df_clean[df_clean["PERSON_KEY"] == pk]
        h = hashlib.md5(str(pk).encode()).hexdigest()[:12]
        print(f"  Person {h}: {len(rows)} rows")
        for _, r in rows.iterrows():
            print(f"    AppNo={r['APPNO_CLEAN']} Year={r['Year']} Pct={r['NMS_PER_num']} PLE_Yr={r['PLE_YEAR_PASSED']} Method={r['PLE_MATCH_METHOD']} Gap={r['PLE_YEAR_GAP']} Foreigner={r['FOREIGNER_STATUS']}")

# B5+ counts with and without duplicates
B5_PLUS = ["B5","B6","B7","B8","B9","B10"]
b5_original = len(df_clean[df_clean["PercentileBin"].isin(B5_PLUS)])
print(f"\nB5+ in clean subset (with potential dupes): {b5_original:,}")

# After dedup: keep first per PERSON_KEY
df_clean_deduped = df_clean.drop_duplicates(subset="PERSON_KEY", keep="first")
b5_deduped = len(df_clean_deduped[df_clean_deduped["PercentileBin"].isin(B5_PLUS)])
print(f"B5+ after dedup: {b5_deduped:,}")
print(f"Difference: {b5_original - b5_deduped}")

print("\n\n=== IMPACT ASSESSMENT COMPLETE ===")
