"""
run_all.py — Orchestrator: runs all 6 CHED computation scripts in sequence.
"""

import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
from helpers import today_str

def run_script(name: str, module_name: str) -> dict:
    print(f"\n{'#'*70}")
    print(f"  Running: {name}")
    print(f"{'#'*70}")
    start = time.time()
    mod = __import__(module_name)
    result = mod.compute()
    elapsed = time.time() - start
    print(f"  Completed in {elapsed:.1f}s\n")
    return {"module": module_name, "time_s": elapsed, "result": result}

def main():
    print("=" * 70)
    print("  CHED Computation Suite — Run All Scripts (6 tabs)")
    print(f"  Date: {today_str()}")
    print("=" * 70)

    scripts = [
        ("01 — National Profile", "01_national_profile"),
        ("02 — Thresholds (B4+ vs B5+)", "02_thresholds"),
        ("03 — PLE-Passer Linkage", "03_ple_linkage"),
        ("04 — Institution & Foreign Context", "04_institution_context"),
        ("05 — Evidence Findings", "05_evidence_findings"),
        ("06 — Data & Limitations", "06_data_limitations"),
    ]

    results = []
    total_start = time.time()

    for name, module in scripts:
        try:
            res = run_script(name, module)
            results.append((name, "OK", res["time_s"]))
        except Exception as e:
            print(f"\n  ERROR in {name}: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, f"FAILED: {e}", 0))

    total_time = time.time() - total_start

    print("\n" + "=" * 70)
    print("  EXECUTION SUMMARY")
    print("=" * 70)
    print(f"  Total time: {total_time:.1f}s\n")
    print("  Script                          Status         Time")
    print("  " + "-" * 55)
    for name, status, t in results:
        s = status if status == "OK" else "FAILED"
        print(f"  {name:35s} {s:12s} {t:>5.1f}s")

    ok_count = sum(1 for _, s, _ in results if s == "OK")
    fail_count = sum(1 for _, s, _ in results if s != "OK")
    print(f"\n  {ok_count} succeeded, {fail_count} failed")

    from config import OUTPUT_DIR
    expected_files = [
        "01_national_profile.md", "02_thresholds.md", "03_ple_linkage.md",
        "04_institution_context.md", "05_evidence_findings.md", "06_data_limitations.md",
    ]
    print(f"\n  Output files in: {OUTPUT_DIR}")
    for fname in expected_files:
        fpath = os.path.join(OUTPUT_DIR, fname)
        if os.path.exists(fpath):
            size = os.path.getsize(fpath)
            print(f"    [OK]   {fname} ({size:,} bytes)")
        else:
            print(f"    [MISS] {fname}")
    print("=" * 70)

    if fail_count > 0:
        print("\n  WARNING: Some scripts failed.")
        sys.exit(1)
    else:
        print("\n  All 6 scripts completed successfully.")

if __name__ == "__main__":
    main()
