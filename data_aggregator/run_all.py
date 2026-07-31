"""
run_all.py v3 — Runs all 13 page scripts as subprocesses.
Handles inconsistent save() signatures by running scripts directly.

INFRA-01 fix: every path is resolved relative to this file's own location, not the
process cwd, so `python run_all.py` works identically whether invoked from the repo
root or from inside data_aggregator/. A page that returns exit 0 but writes no (or an
empty) output file is now treated as FAILED — a pipeline that silently produces
nothing is worse than one that errors loudly.
"""
import subprocess
import sys
import time
import os
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
RESULTS_DIR = SCRIPTS_DIR / "page_results"

PAGE_SCRIPTS = [
    ("01", "Executive Summary",        "page_01_executive_summary.py", "01_executive_summary.md"),
    ("02", "Data Integrity",           "page_02_data_integrity.py", "02_data_integrity.md"),
    ("03", "Trends & Stability",       "page_03_trends_stability.py", "03_trends_stability.md"),
    ("04", "Score Bins & Citizenship", "page_04_score_bins.py", "04_score_bins.md"),
    ("05", "University Type",          "page_05_university_type.py", "05_university_type.md"),
    ("06", "Flow & Pathways",          "page_06_flow_pathways.py", "06_flow_pathways.md"),
    ("07", "PLE Alignment",            "page_07_ple_alignment.py", "07_ple_alignment.md"),
    ("08", "Repeat Takers",            "page_08_repeat_takers.py", "08_repeat_takers.md"),
    ("09", "Subtests & Profiles",      "page_09_subtests.py", "09_subtests.md"),
    ("10", "Year Gap & Gender",        "page_10_year_gap_gender.py", "10_year_gap_gender.md"),
    ("11", "Statistical Tests",        "page_11_statistical_tests.py", "11_statistical_tests.md"),
    ("12", "Policy Tables",            "page_12_policy_tables.py", "12_policy_tables.md"),
    ("13", "CHED Compliance",          "page_13_ched_compliance.py", "13_ched_compliance.md"),
]

VENV_PYTHON = str(REPO_ROOT / ".venv" / "Scripts" / "python.exe")


def main():
    print("=" * 60)
    print("  NMAT Data Extraction — Master Orchestrator v3")
    print("=" * 60)
    print(f"\n  Starting: {len(PAGE_SCRIPTS)} pages")
    print(f"  Data: NMAT_Exodus.parquet")
    print(f"  Engine: {VENV_PYTHON}")
    print(f"  Output: {RESULTS_DIR}\n")

    RESULTS_DIR.mkdir(exist_ok=True)

    total_start = time.time()
    passed = 0
    failed = 0
    failures = []

    for num, name, script_name, out_name in PAGE_SCRIPTS:
        script_path = SCRIPTS_DIR / script_name
        out_path = RESULTS_DIR / out_name

        if not script_path.exists():
            print(f"  [{num}/13] {name}... SKIP (script not found: {script_path})")
            failed += 1
            failures.append((num, name, "script not found"))
            continue

        # Detect stale output from a previous (possibly failed) run so a script that
        # silently no-ops can't be mistaken for success just because an old file exists.
        if out_path.exists():
            out_path.unlink()

        print(f"  [{num}/13] {name}... ", end="", flush=True)
        start = time.time()

        result = subprocess.run(
            [VENV_PYTHON, str(script_path)],
            capture_output=True, text=True, cwd=str(SCRIPTS_DIR),
        )

        elapsed = time.time() - start

        if result.returncode != 0:
            print(f"FAILED ({elapsed:.1f}s)")
            print(f"    Return code: {result.returncode}")
            stderr_lines = result.stderr.strip().split("\n")
            for line in stderr_lines[-5:]:
                print(f"    {line.strip()}")
            failed += 1
            failures.append((num, name, f"exit code {result.returncode}"))
            continue

        # Loud failure if a page produced no output — exit 0 is not enough.
        if not out_path.exists() or out_path.stat().st_size == 0:
            print(f"FAILED ({elapsed:.1f}s) — exit 0 but no/empty output at {out_path}")
            failed += 1
            failures.append((num, name, "exit 0 but no/empty output file"))
            continue

        print(f"OK ({elapsed:.1f}s)")
        passed += 1

    total_elapsed = time.time() - total_start
    print(f"\n  {'=' * 50}")
    print(f"  Complete: {passed} passed, {failed} failed in {total_elapsed:.1f}s")
    print(f"  {'=' * 50}")

    if failures:
        print(f"\n  FAILURES:")
        for num, name, reason in failures:
            print(f"    [{num}] {name}: {reason}")

    # Verify output files
    print(f"\n  Output files:")
    total_size = 0
    for f in sorted(RESULTS_DIR.glob("*.md")):
        size_kb = f.stat().st_size / 1024
        total_size += size_kb
        print(f"    {f.name} ({size_kb:.1f} KB)")
    print(f"\n  Total output: {total_size:.1f} KB ({total_size/1024:.1f} MB)")

    return failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
