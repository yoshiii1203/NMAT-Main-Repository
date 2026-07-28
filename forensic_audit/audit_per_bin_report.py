"""
Per-bin breakdown: B1, B2, B3, B4 — all checks by bin
"""
import pandas as pd
import numpy as np
import hashlib
import re, unicodedata, warnings
warnings.filterwarnings("ignore")

MM_PATH = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\dataset\output\PLE_MATCH_MASTER.csv"
EXODUS_PATH = r"D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\streamlit_dashboard\CHED_relevant_dashboard\NMAT_Exodus.parquet"

# ── Load data ──────────────────────────────────────────────
mm = pd.read_csv(MM_PATH, dtype=str)
exodus = pd.read_parquet(EXODUS_PATH)

# Best-record confirmed passers, observable
obs = exodus[exodus["Year"] <= 2014]
confirmed = obs[obs["IS_PLE_ANALYSIS_SAFE"] == True]
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

best["BAND"] = best["NMS_PER_num"].map(band_label)
confirmed["BAND"] = confirmed["NMS_PER_num"].map(band_label)

# ── Name comparison helper ─────────────────────────────────
def parse_names(ple, nma):
    if pd.isna(ple) or pd.isna(nma):
        return "missing"
    p = unicodedata.normalize('NFKD', str(ple).upper()).encode('ASCII','ignore').decode()
    n = unicodedata.normalize('NFKD', str(nma).upper()).encode('ASCII','ignore').decode()
    p = re.sub(r"[^A-Z0-9\s,]+"," ",p); n = re.sub(r"[^A-Z0-9\s,]+"," ",n)
    p = re.sub(r"\s+"," ",p).strip(); n = re.sub(r"\s+"," ",n).strip()
    
    ple_surname = p.split(",")[0].strip() if "," in p else p.split()[-1]
    nma_surname = n.split(",")[0].strip() if "," in n else n.split()[-1]
    ple_given = p.split(",")[1].strip() if "," in p and len(p.split(","))>1 else ""
    nma_given = n.split(",")[1].strip() if "," in n and len(n.split(","))>1 else ""
    
    pw = set(p.replace(","," ").split()); nw = set(n.replace(","," ").split())
    overlap = pw & nw
    all_w = pw | nw
    ratio = len(overlap)/len(all_w) if all_w else 0
    
    given_match = bool(set(ple_given.split()) & set(nma_given.split())) if ple_given and nma_given else False
    
    if ple_surname == nma_surname and given_match:
        return "strong_match"
    if ratio >= 0.6:
        return "high_overlap"
    if (ple_surname in n or nma_surname in p) and given_match:
        return "married_name"
    # given_only with very low overlap (<0.3) = probably wrong person
    if given_match and ratio >= 0.3:
        return "given_only_ok"
    if given_match and ratio < 0.3:
        return "given_only_low"  # suspicious: only first name matches
    if ratio > 0:
        return "weak_overlap"
    return "mismatch"

# ── Build appno→band lookup from best-record ───────────────
appno_to_band = best[best["APPNO_CLEAN"].notna()].set_index("APPNO_CLEAN")["BAND"].to_dict()

# ── Process match master for appno-based records ───────────
accepted = mm[mm["MATCH_STATUS"].isin(["FINAL_MATCH","MANUAL_APPNO_MATCH","DETERMINISTIC_APPNO"])].copy()
appno_based = accepted[accepted["MATCH_METHOD"].isin(["MANUAL_APPNO_MATCH","DETERMINISTIC_APPNO"])].copy()

rows = []
for _, r in appno_based.iterrows():
    band = appno_to_band.get(str(r["MATCHED_APPNO"]), "unknown")
    ver = parse_names(r["PLE_FULL_NAME"], r["MATCHED_NMA_Name"])
    n_attempts = None
    is_dup_best = False
    gap = None
    
    pk = None
    # Find PERSON_KEY for this appno in best
    br = best[best["APPNO_CLEAN"] == str(r["MATCHED_APPNO"])]
    if len(br) > 0:
        pk = br.iloc[0]["PERSON_KEY"]
        gap = br.iloc[0]["PLE_YEAR_GAP"]
        # Check attempts
        p_all = confirmed[confirmed["PERSON_KEY"] == pk] if pk else pd.DataFrame()
        n_attempts = len(p_all) if len(p_all) > 0 else None
        # Check duplicate best-record
        is_dup_best = pk in set(best["PERSON_KEY"][best["PERSON_KEY"].duplicated(keep=False)]) if pk else False
    
    rows.append({
        "band": band,
        "verdict": ver,
        "method": r["MATCH_METHOD"],
        "pct": r.get("MATCHED_NMS_PER_num","?"),
        "ple_name": r["PLE_FULL_NAME"][:50],
        "nma_name": r["MATCHED_NMA_Name"][:50],
        "appno_hash": hashlib.md5(str(r["MATCHED_APPNO"]).encode()).hexdigest()[:8],
        "n_attempts": n_attempts,
        "is_dup_best": is_dup_best,
        "gap": gap,
    })

rd = pd.DataFrame(rows)
rd["pct_num"] = pd.to_numeric(rd["pct"], errors="coerce")

# ═══════════════════════════════════════════════════════════
# REPORT BY BIN
# ═══════════════════════════════════════════════════════════
target_bins = ["B1","B2","B3","B4"]

print("=" * 90)
print("PER-BIN NAME CROSS-CHECK: MANUAL + DETERMINISTIC APPNO RECORDS ONLY")
print("=" * 90)

overall_appno_based = len(rd)
print(f"\nTotal appno-based records in match master: {overall_appno_based}")

overall_mismatch = (rd["verdict"] == "mismatch").sum()
print(f"Total mismatches (all bands): {overall_mismatch}")

print(f"\n{'Bin':<6} {'Appno_records':>15} {'Strong_match':>15} {'High_overlap':>15} {'Married_name':>15} {'GivenOK':>8} {'GivenLow':>8} {'Weak':>8} {'MISMATCH':>10}")
print("-" * 115)

total_appno = 0
total_mismatch = 0
for band in target_bins:
    sub = rd[rd["band"] == band]
    t = len(sub)
    if t == 0:
        print(f"{band:<6} {'0':>15}")
        continue
    sm = (sub["verdict"]=="strong_match").sum()
    ho = (sub["verdict"]=="high_overlap").sum()
    mn = (sub["verdict"]=="married_name").sum()
    go_ok = (sub["verdict"]=="given_only_ok").sum()
    go_low = (sub["verdict"]=="given_only_low").sum()
    wk = (sub["verdict"]=="weak_overlap").sum()
    mm = (sub["verdict"]=="mismatch").sum()
    total_appno += t
    total_mismatch += mm + go_low  # given_only_low is also questionable
    print(f"{band:<6} {t:>15} {sm:>15} {ho:>15} {mn:>15} {go_ok:>8} {go_low:>8} {wk:>8} {mm:>10}")

print("-" * 105)
# B1-B3 combined
for label, bands in [("B1-B3", ["B1","B2","B3"]), ("B1-B4 (below B5)", ["B1","B2","B3","B4"])]:
    sub = rd[rd["band"].isin(bands)]
    t = len(sub)
    mm = (sub["verdict"]=="mismatch").sum()
    gl = (sub["verdict"]=="given_only_low").sum()
    print(f"{label:<6} {t:>15} {'':>15} {'':>15} {'':>15} {'':>8} {gl:>8} {'':>8} {mm:>10}")

# ═══════════════════════════════════════════════════════════
# DETAILED MISMATCHES BY BIN
# ═══════════════════════════════════════════════════════════
print("\n\n" + "=" * 90)
print("DETAILED MISMATCHES AND SUSPICIOUS RECORDS BY BIN")
print("=" * 90)

for band in target_bins:
    mismatches = rd[(rd["band"] == band) & (rd["verdict"].isin(["mismatch", "given_only_low"]))]
    print(f"\n--- {band}: {len(mismatches)} questionable records ---")
    if len(mismatches) > 0:
        for _, r in mismatches.iterrows():
            print(f"  Verdict={r['verdict']} PLE='{r['ple_name']}'")
            print(f"  NMA='{r['nma_name']}'")
            print(f"  Pct={r['pct']} Method={r['method']} AppNo={r['appno_hash']}")
            print(f"  Attempts={r['n_attempts']} DupBest={r['is_dup_best']} Gap={r['gap']}")
            print()

# ═══════════════════════════════════════════════════════════
# APPNO UNIQUENESS BY BIN
# ═══════════════════════════════════════════════════════════
print("=" * 90)
print("APPNO UNIQUENESS BY BIN")
print("=" * 90)

for band in target_bins:
    sub_best = best[best["BAND"] == band]
    t = len(sub_best)
    n_unique_appnos = sub_best["APPNO_CLEAN"].nunique()
    # Shared appnos
    appno_counts = sub_best.groupby("APPNO_CLEAN")["PERSON_KEY"].nunique()
    shared = (appno_counts > 1).sum()
    print(f"  {band}: Total={t:>6,} UniqueAppNos={n_unique_appnos:>6,} SharedAppNos={shared}")

# ═══════════════════════════════════════════════════════════
# DUPLICATE BEST-RECORD BY BIN
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 90)
print("DUPLICATE BEST-RECORD BY BIN")
print("=" * 90)

dup_pks = set(best["PERSON_KEY"][best["PERSON_KEY"].duplicated(keep=False)])
for band in target_bins:
    sub = best[best["BAND"] == band]
    n_dup = sub["PERSON_KEY"].isin(dup_pks).sum()
    print(f"  {band}: Duplicate best-record persons = {n_dup}")

# ═══════════════════════════════════════════════════════════
# REPEAT ATTEMPTS BY BIN
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 90)
print("REPEAT ATTEMPTS BY BIN (best-record persons only)")
print("=" * 90)

for band in target_bins:
    sub_pks = set(best[best["BAND"] == band]["PERSON_KEY"])
    sub_all = confirmed[confirmed["PERSON_KEY"].isin(sub_pks)]
    att = sub_all.groupby("PERSON_KEY").size()
    n_1 = (att == 1).sum()
    n_2plus = (att > 1).sum()
    print(f"  {band}: Total={len(sub_pks):>6,} 1attempt={n_1:>5,} 2+attempts={n_2plus:>5,} ({n_2plus/len(sub_pks)*100:5.1f}%)")

# ═══════════════════════════════════════════════════════════
# YEAR GAP BY BIN
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 90)
print("NMAT-TO-PLE YEAR GAP BY BIN")
print("=" * 90)

for band in target_bins:
    sub = best[best["BAND"] == band]
    gaps = sub["PLE_YEAR_GAP"].dropna()
    neg = (gaps < 0).sum()
    zero = (gaps == 0).sum()
    lt5 = ((gaps > 0) & (gaps < 5)).sum()
    r5_10 = ((gaps >= 5) & (gaps <= 10)).sum()
    gt10 = (gaps > 10).sum()
    missing = sub["PLE_YEAR_GAP"].isna().sum()
    print(f"  {band}: N={len(sub):>6} Neg={neg} Zero={zero} <5yr={lt5} 5-10yr={r5_10} >10yr={gt10} Missing={missing}")

# ═══════════════════════════════════════════════════════════
# SUMMARY TABLE
# ═══════════════════════════════════════════════════════════
print("\n\n" + "=" * 90)
print("FULL SUMMARY TABLE BY BIN")
print("=" * 90)

header = f"{'Bin':<6} {'Total':>8} {'Unique':>8} {'AppnoMatch':>12} {'NameOK':>8} {'NameBad':>10} {'DupBest':>8} {'2+Attempts':>12} {'GapOK':>8} {'GapBad':>8}"
print(f"\n{header}")
print("-" * 90)

for band in target_bins:
    sub = best[best["BAND"] == band]
    t = len(sub)
    u = sub["APPNO_CLEAN"].nunique()
    n_app = len(rd[rd["band"] == band])
    n_name_ok = len(rd[(rd["band"] == band) & (rd["verdict"].isin(["strong_match","high_overlap","married_name","given_only_ok"]))])
    n_name_bad = len(rd[(rd["band"] == band) & (rd["verdict"].isin(["mismatch","given_only_low"]))])
    n_dup = sub["PERSON_KEY"].isin(dup_pks).sum()
    sub_pks = set(sub["PERSON_KEY"])
    sub_att = confirmed[confirmed["PERSON_KEY"].isin(sub_pks)].groupby("PERSON_KEY").size()
    n_2p = (sub_att > 1).sum()
    gaps = sub["PLE_YEAR_GAP"].dropna()
    n_gap_ok = ((gaps >= 5) & (gaps <= 10)).sum()
    n_gap_bad = (gaps < 5).sum() + (gaps > 10).sum()
    print(f"{band:<6} {t:>8,} {u:>8,} {n_app:>12} {n_name_ok:>8} {n_name_bad:>10} {n_dup:>8} {n_2p:>12} {n_gap_ok:>8} {n_gap_bad:>8}")

print("\n\n=== DONE ===")
