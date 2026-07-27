"""
run_all.py — Orchestrator: runs all 7 CHED computation scripts in sequence.
"""

import sys
import os
import time

# Ensure we can import from this directory
sys.path.insert(0, os.path.dirname(__file__))

from helpers import today_str


def run_script(name: str, module_name: str) -> dict:
    """Import and run a compute function, timing it."""
    print(f"\n{'#'*70}")
    print(f"  Running: {name}")
    print(f"{'#'*70}")
    start = time.time()

    # Import the module and call compute()
    mod = __import__(module_name)
    result = mod.compute()

    elapsed = time.time() - start
    print(f"  Completed in {elapsed:.1f}s\n")
    return {"module": module_name, "time_s": elapsed, "result": result}


def main():
    print("=" * 70)
    print("  CHED Computation Suite — Run All Scripts")
    print(f"  Date: {today_str()}")
    print("=" * 70)

    scripts = [
        ("01 — National Benchmark", "01_national_benchmark"),
        ("02 — Cut-Off Scenarios", "02_cutoff_scenarios"),
        ("03 — Per-HEI Distribution", "03_per_hei_distribution"),
        ("04 — Foreign Analysis", "04_foreign_analysis"),
        ("05 — Demographic Profiles", "05_demographic_profiles"),
        ("06 — PLE Alignment", "06_ple_alignment"),
        ("07 — Temporal Trends", "07_temporal_trends"),
    ]

    results = []
    total_start = time.time()

    for name, module in scripts:
        try:
            res = run_script(name, module)
            results.append((name, "OK", res["time_s"]))
        except Exception as e:
            print(f"\n  ERROR in {name}: {e}")
            results.append((name, f"FAILED: {e}", 0))

    total_time = time.time() - total_start

    # ── Summary Report ──────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("  EXECUTION SUMMARY")
    print("=" * 70)
    print(f"  Total time: {total_time:.1f}s")
    print()
    print("  Script                          Status         Time")
    print("  " + "-" * 55)
    for name, status, t in results:
        status_str = status if status == "OK" else "FAILED"
        print(f"  {name:35s} {status_str:12s} {t:>5.1f}s")

    ok_count = sum(1 for _, s, _ in results if s == "OK")
    fail_count = sum(1 for _, s, _ in results if s != "OK")
    print(f"\n  {ok_count} succeeded, {fail_count} failed")

    # ── Check output files ──────────────────────────────────────────────
    from config import OUTPUT_DIR
    expected_files = [
        "01_national_benchmark.md",
        "02_cutoff_scenarios.md",
        "03_per_hei_distribution.md",
        "04_foreign_analysis.md",
        "05_demographic_profiles.md",
        "06_ple_alignment.md",
        "07_temporal_trends.md",
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
        print("\n  WARNING: Some scripts failed. Review errors above.")
        sys.exit(1)
    else:
        print("\n  All scripts completed successfully.")
        print("  Ready for Phase 2: Validation and cross-checking.")


if __name__ == "__main__":
    main()
