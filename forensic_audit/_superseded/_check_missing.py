"""
Check where AHUJA and LIAO records went
"""
import pandas as pd

mm = pd.read_csv(r'D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\dataset\output\PLE_MATCH_MASTER.csv', dtype=str)
ex = pd.read_parquet(r'D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\streamlit_dashboard\CHED_relevant_dashboard\NMAT_Exodus.parquet')

# AHUJA
ahuja = mm[mm['PLE_FULL_NAME'].str.contains('AHUJA', na=False)]
print('AHUJA:')
for _, r in ahuja.iterrows():
    print(f"  AppNo={r['MATCHED_APPNO']} Pct={r['MATCHED_NMS_PER_num']} Method={r['MATCH_METHOD']} Status={r['MATCH_STATUS']}")
    appno = str(r['MATCHED_APPNO'])
    found = ex[ex['APPNO_CLEAN'] == appno]
    print(f"  In exodus: {len(found)} rows")
    for _, f in found.iterrows():
        print(f"    Year={f['Year']} Pct={f['NMS_PER_num']} Best={f['IS_BEST_NMAT_RECORD']} Safe={f['IS_PLE_ANALYSIS_SAFE']}")

# LIAO
print()
liao = mm[mm['PLE_FULL_NAME'].str.contains('LIAO, KATHERINE', na=False)]
print('LIAO:')
for _, r in liao.iterrows():
    print(f"  AppNo={r['MATCHED_APPNO']} Pct={r['MATCHED_NMS_PER_num']} Method={r['MATCH_METHOD']} Status={r['MATCH_STATUS']}")
    appno = str(r['MATCHED_APPNO'])
    found = ex[ex['APPNO_CLEAN'] == appno]
    print(f"  In exodus: {len(found)} rows")
    for _, f in found.iterrows():
        print(f"    Year={f['Year']} Pct={f['NMS_PER_num']} Best={f['IS_BEST_NMAT_RECORD']} Safe={f['IS_PLE_ANALYSIS_SAFE']}")
