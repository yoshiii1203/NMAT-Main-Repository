"""
run_all.py v2 — Runs all 13 page scripts as subprocesses.
Handles inconsistent save() signatures by running scripts directly.
"""
import subprocess
import sys
import time
import os
from pathlib import Path

SCRIPTS_DIR = Path("data_aggregator")

PAGE_SCRIPTS = [
    ("01", "Executive Summary",        "page_01_executive_summary.py"),
    ("02", "Data Integrity",           "page_02_data_integrity.py"),
    ("03", "Trends & Stability",       "page_03_trends_stability.py"),
    ("04", "Score Bins & Citizenship", "page_04_score_bins.py"),
    ("05", "University Type",          "page_05_university_type.py"),
    ("06", "Flow & Pathways",          "page_06_flow_pathways.py"),
    ("07", "PLE Alignment",            "page_07_ple_alignment.py"),
    ("08", "Repeat Takers",            "page_08_repeat_takers.py"),
    ("09", "Subtests & Profiles",      "page_09_subtests.py"),
    ("10", "Year Gap & Gender",        "page_10_year_gap_gender.py"),
    ("11", "Statistical Tests",        "page_11_statistical_tests.py"),
    ("12", "Policy Tables",            "page_12_policy_tables.py"),
    ("13", "CHED Compliance",          "page_13_ched_compliance.py"),
]

VENV_PYTHON = os.path.join(".venv", "Scripts", "python.exe")

def main():
    print("=" * 60)
    print("  NMAT Data Extraction — Master Orchestrator v2")
    print("=" * 60)
    print(f"\n  Starting: {len(PAGE_SCRIPTS)} pages")
    print(f"  Data: NMAT_Exodus.parquet")
    print(f"  Engine: {VENV_PYTHON}")
    print(f"  Output: page_results/\n")

    results_dir = Path("page_results")
    results_dir.mkdir(exist_ok=True)

    total_start = time.time()
    passed = 0
    failed = 0

    for num, name, script_name in PAGE_SCRIPTS:
        script_path = SCRIPTS_DIR / script_name
        if not script_path.exists():
            print(f"  [{num}/13] {name}... SKIP (script not found)")
            failed += 1
            continue

        print(f"  [{num}/13] {name}... ", end="", flush=True)
        start = time.time()

        result = subprocess.run(
            [VENV_PYTHON, str(script_path)],
            capture_output=True, text=True, cwd="."
        )

        elapsed = time.time() - start

        if result.returncode == 0:
            print(f"OK ({elapsed:.1f}s)")
            passed += 1
        else:
            print(f"FAILED ({elapsed:.1f}s)")
            print(f"    Return code: {result.returncode}")
            # Show last few lines of stderr
            stderr_lines = result.stderr.strip().split("\n")
            for line in stderr_lines[-5:]:
                print(f"    {line.strip()}")
            failed += 1

    total_elapsed = time.time() - total_start
    print(f"\n  {'=' * 50}")
    print(f"  Complete: {passed} passed, {failed} failed in {total_elapsed:.1f}s")
    print(f"  {'=' * 50}")

    # Verify output files
    print(f"\n  Output files:")
    total_size = 0
    for f in sorted(results_dir.glob("*.md")):
        size_kb = f.stat().st_size / 1024
        total_size += size_kb
        print(f"    {f.name} ({size_kb:.1f} KB)")
    print(f"\n  Total output: {total_size:.1f} KB ({total_size/1024:.1f} MB)")

    return failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
