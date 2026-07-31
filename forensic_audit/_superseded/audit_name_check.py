"""
Cross-check: For MANUAL_APPNO_MATCH & DETERMINISTIC_APPNO matches,
verify that the PLE name and NMAT name are consistent.
"""
import pandas as pd
import numpy as np
import hashlib
import warnings
warnings.filterwarnings("ignore")

MM_PATH = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\dataset\output\PLE_MATCH_MASTER.csv"
EXODUS_PATH = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\streamlit_dashboard\CHED_relevant_dashboard\NMAT_Exodus.parquet"

# Load match master
mm = pd.read_csv(MM_PATH, dtype=str)
print(f"PLE_MATCH_MASTER: {len(mm):,} rows")

# Filter to accepted match statuses
accepted = mm[mm["MATCH_STATUS"].isin(["FINAL_MATCH", "MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"])].copy()
print(f"Accepted matches: {len(accepted):,}")

# By method
print(f"\nBy MATCH_METHOD:")
print(accepted["MATCH_METHOD"].value_counts().to_string())

# ── Name comparison ──────────────────────────────────────────
# PLE_NAME_NORM vs MATCHED_NMA_Name
# We'll normalize both for comparison
def normalize_for_compare(s):
    if pd.isna(s):
        return ""
    import re
    s = str(s).upper().strip()
    s = re.sub(r"[^A-Z0-9\s,]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

accepted["PLE_N"] = accepted["PLE_NAME_NORM"].apply(normalize_for_compare)
accepted["NMA_N"] = accepted["MATCHED_NMA_Name"].apply(normalize_for_compare)

# Simple check: does the PLE name appear within the NMAT name or vice versa?
def names_match(ple, nma):
    if not ple or not nma:
        return "missing_name"
    # Check if one is contained in the other (accounting for comma/space)
    ple_clean = ple.replace(",", " ").strip()
    nma_clean = nma.replace(",", " ").strip()
    ple_parts = set(ple_clean.split())
    nma_parts = set(nma_clean.split())
    overlap = ple_parts & nma_parts
    # At least last name + one more name should match
    # Get last name (last word before comma for NMAT format "LAST, FIRST")
    ple_last = ple_clean.split()[0] if " " in ple_clean else ple_clean
    nma_last = nma_clean.split(",")[0] if "," in nma_clean else nma_clean.split()[0]
    last_match = ple_last == nma_last
    # Overlap ratio
    ratio = len(overlap) / max(len(ple_parts), len(nma_parts)) if max(len(ple_parts), len(nma_parts)) > 0 else 0
    if last_match and ratio >= 0.5:
        return "match"
    elif last_match:
        return "last_only_match"
    else:
        return "no_match"

accepted["NAME_CHECK"] = accepted.apply(lambda r: names_match(r["PLE_N"], r["NMA_N"]), axis=1)

print(f"\n-- Name consistency check (ALL methods) --")
nc = accepted["NAME_CHECK"].value_counts()
for cat, cnt in nc.items():
    print(f"  {cat:<20} {cnt:>6,} ({cnt/len(accepted)*100:.1f}%)")

print(f"\n-- By match method --")
ct = pd.crosstab(accepted["MATCH_METHOD"], accepted["NAME_CHECK"])
print(ct.to_string())

# Focus on MANUAL and DETERMINISTIC
print(f"\n-- MANUAL_APPNO_MATCH name check --")
manual = accepted[accepted["MATCH_METHOD"] == "MANUAL_APPNO_MATCH"]
print(manual["NAME_CHECK"].value_counts().to_string())

print(f"\n-- DETERMINISTIC_APPNO name check --")
det = accepted[accepted["MATCH_METHOD"] == "DETERMINISTIC_APPNO"]
print(det["NAME_CHECK"].value_counts().to_string())

# Show mismatches
bad = accepted[accepted["NAME_CHECK"] == "no_match"]
print(f"\n-- NAME MISMATCHES: {len(bad)} records --")
if len(bad) > 0:
    for _, r in bad.head(20).iterrows():
        h = hashlib.md5(str(r.get("MATCHED_APPNO", "")).encode()).hexdigest()[:8]
        print(f"  PLE='{r['PLE_FULL_NAME'][:50]}'")
        print(f"  NMA='{r['MATCHED_NMA_Name'][:50]}'")
        print(f"  Method={r['MATCH_METHOD']} Status={r['MATCH_STATUS']} AppNo={h}")
        print()

# ── Now cross-reference with low-score (< B5) best-record passers ──
print("\n\n=== CROSS-REFERENCE: BELOW-B5 PASSERS ===")
exodus = pd.read_parquet(EXODUS_PATH)
obs = exodus[exodus["Year"] <= 2014]
confirmed = obs[obs["IS_PLE_ANALYSIS_SAFE"] == True]
best = confirmed[confirmed["IS_BEST_NMAT_RECORD"] == True]
low_best = best[best["NMS_PER_num"] < 40].copy()
print(f"Best-record below B5: {len(low_best):,}")

# For low-scorers, check which ones are appno-based matches
low_manual = low_best[low_best["PLE_MATCH_METHOD"] == "MANUAL_APPNO_MATCH"]
low_det = low_best[low_best["PLE_MATCH_METHOD"] == "DETERMINISTIC_APPNO"]
low_exact = low_best[low_best["PLE_MATCH_METHOD"] == "EXACT"]
print(f"  EXACT:              {len(low_exact):,}")
print(f"  MANUAL_APPNO_MATCH: {len(low_manual):,}")
print(f"  DETERMINISTIC_APPNO: {len(low_det):,}")

# Map appnos from low_best to match master
low_appnos = low_best["APPNO_CLEAN"].dropna().unique()
print(f"  Unique appnos in low-score: {len(low_appnos):,}")

# Check these against the match master name check
mm_low = accepted[accepted["MATCHED_APPNO"].isin(low_appnos)].copy()
print(f"  Match master records for these appnos: {len(mm_low):,}")

# Name check for low-score manual/deterministic
mm_low_manual = mm_low[mm_low["MATCH_METHOD"].isin(["MANUAL_APPNO_MATCH", "DETERMINISTIC_APPNO"])]
print(f"  Appno-based among them: {len(mm_low_manual):,}")
if len(mm_low_manual) > 0:
    print(f"  Name check results:")
    print(mm_low_manual["NAME_CHECK"].value_counts().to_string())
    
    # Show any mismatches
    bad_low = mm_low_manual[mm_low_manual["NAME_CHECK"] == "no_match"]
    if len(bad_low) > 0:
        print(f"\n  NAME MISMATCHES in low-score passers: {len(bad_low)}")
        for _, r in bad_low.iterrows():
            h = hashlib.md5(str(r.get("MATCHED_APPNO", "")).encode()).hexdigest()[:8]
            pct = r.get("MATCHED_NMS_PER_num", "?")
            print(f"    PLE='{r['PLE_FULL_NAME'][:45]}'")
            print(f"    NMA='{r['MATCHED_NMA_Name'][:45]}'")
            print(f"    Pct={pct} Method={r['MATCH_METHOD']} AppNo={h}")
            print()

# Also check "last_only_match" — these might be questionable too
last_only_low = mm_low_manual[mm_low_manual["NAME_CHECK"] == "last_only_match"]
if len(last_only_low) > 0:
    print(f"\n  Last-name-only matches in low-score: {len(last_only_low)}")
    for _, r in last_only_low.head(10).iterrows():
        h = hashlib.md5(str(r.get("MATCHED_APPNO", "")).encode()).hexdigest()[:8]
        print(f"    PLE='{r['PLE_FULL_NAME'][:45]}'")
        print(f"    NMA='{r['MATCHED_NMA_Name'][:45]}'")
        print(f"    Pct={r.get('MATCHED_NMS_PER_num','?')} AppNo={h}")

print("\n\n=== NAME AUDIT COMPLETE ===")
