"""
fix_dashboard.py - Streamlit Dashboard Migration for Pipeline 4
===============================================================
After Pipeline 4 produces NMAT_Exodus.parquet, this script patches
dashboard.py to:
1. Read from NMAT_Exodus.parquet instead of NMAT_Ultima.parquet
2. Remove the on-the-fly pseudo-citizenship CSV merge
3. Use CITIZENSHIP_FINAL / FOREIGNER_STATUS directly from parquet
4. Update all labels from "Pseudo-citizenship" to "Citizenship"

Usage: .venv/Scripts/python.exe fix_dashboard.py
"""

import re

with open("dashboard.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update data path to use NMAT_Exodus first
old_path = 'Path("dataset/NMAT_Ultima.parquet"),'
new_path = 'Path("dataset/NMAT_Exodus.parquet"),\n        Path("dataset/NMAT_Ultima.parquet"),'
if old_path in content:
    content = content.replace(old_path, new_path, 1)
    print("[1/5] Updated data path: NMAT_Exodus.parquet preferred over NMAT_Ultima.parquet")

# 2. Remove the on-the-fly pseudo-citizenship CSV loading block
old_pc_block = """
# --- Pseudo-citizenship profile lookup ---
_PC_PROFILE_PATH = Path("dataset/pseudo_citizenship_profiling_FINAL.csv")
try:
    _pc_lookup = pd.read_csv(
        _PC_PROFILE_PATH,
        usecols=["APPNO_CLEAN", "override_applied", "name_based_assessment", "pseudo_citizenship"],
        dtype=str,
    )
    _pc_lookup["APPNOCLEAN"] = _pc_lookup["APPNO_CLEAN"].str.strip()
    _pc_lookup = _pc_lookup.drop(columns=["APPNO_CLEAN"]).drop_duplicates(subset=["APPNOCLEAN"])
    _PC_LOOKUP_AVAILABLE = True
except Exception:
    _pc_lookup = pd.DataFrame(
        columns=["APPNOCLEAN", "override_applied", "name_based_assessment", "pseudo_citizenship"]
    )
    _PC_LOOKUP_AVAILABLE = False
"""
new_pc_block = """
# --- Citizenship columns are baked into NMAT_Exodus.parquet by Pipeline 4 ---
_PC_LOOKUP_AVAILABLE = True  # Always available when using Exodus
"""
if old_pc_block in content:
    content = content.replace(old_pc_block, new_pc_block, 1)
    print("[2/5] Removed on-the-fly pseudo-citizenship CSV loading")

# 3. Remove the on-the-fly merge with pseudo lookup
old_merge = """
    # Merge pseudo-citizenship lookup into the observable university subset
    _uniobs_pc = F["uniobservable"].copy()
    _uniobs_pc["APPNOCLEAN"] = _uniobs_pc["APPNO_CLEAN"].astype(str).str.strip()
    _uniobs_pc = _uniobs_pc.merge(_pc_lookup, on="APPNOCLEAN", how="left").drop(columns=["APPNOCLEAN"])"""
new_merge = """
    # Citizenship columns already in parquet from Pipeline 4
    _uniobs_pc = F["uniobservable"].copy()"""
if old_merge in content:
    content = content.replace(old_merge, new_merge, 1)
    print("[3/5] Removed on-the-fly pseudo-citizenship merge")

# 4. Rename column references and update labels
replacements = [
    ("pseudo_citizenship", "CITIZENSHIP_FINAL"),
    ("override_applied", "FOREIGNER_STATUS"),
    ("Pseudo-citizenship", "Citizenship"),
    ("pseudo-citizenship", "citizenship"),
    ("Pseudo-Citizenship", "Citizenship"),
]
n_replaced = 0
for old, new in replacements:
    c = content.count(old)
    if c > 0:
        content = content.replace(old, new)
        n_replaced += c
        print(f"  Renamed '{old}' -> '{new}' ({c} occurrences)")

print(f"[4/5] Total renames applied: {n_replaced}")

# 5. Fix the FOREIGN filter value
old_filter = 'FOREIGNER_STATUS"] == "FOREIGN"'
new_filter = 'FOREIGNER_STATUS"] == "Verified Foreigner"'
if old_filter in content:
    content = content.replace(old_filter, new_filter, 1)
    print("[5/5] Updated FOREIGN filter to Verified Foreigner")
elif 'FOREIGNER_STATUS"] == "Verified Foreigner"' in content:
    print("[5/5] FOREIGN filter already correct")

# Write back
with open("dashboard.py", "w", encoding="utf-8") as f:
    f.write(content)

print("\nDashboard migration complete. Summary:")
print("  - NMAT_Exodus.parquet is now the primary data source")
print("  - On-the-fly pseudo-citizenship CSV loading removed")
print("  - All citizenship references point to CITIZENSHIP_FINAL / FOREIGNER_STATUS")
print("  - Labels updated from 'Pseudo-citizenship' to 'Citizenship'")
