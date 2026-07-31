"""
aggregate_all.py — Combines all page extraction results into ONE master markdown file.
"""
import sys
import os
from pathlib import Path
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import RESULTS_DIR

OUTPUT_FILE = RESULTS_DIR / "00_MASTER_REPORT.md"

PAGE_ORDER = [
    ("01", "Executive Summary"),
    ("02", "Data Integrity"),
    ("03", "Trends & Stability"),
    ("04", "Score Bins & Citizenship"),
    ("05", "University Type Analysis"),
    ("06", "Flow & Pathways"),
    ("07", "PLE Alignment"),
    ("08", "Repeat Takers"),
    ("09", "Subtests & Profiles"),
    ("10", "Year Gap & Gender"),
    ("11", "Statistical Tests"),
    ("12", "Policy Tables & Export"),
    ("13", "CHED Compliance"),
]


def get_all_metrics():
    """Extract key metrics from each page file to build the overview section."""
    import re
    
    overview = {}
    
    # Page 1 metrics
    p1_path = RESULTS_DIR / "01_executive_summary.md"
    if p1_path.exists():
        text = p1_path.read_text(encoding="utf-8")
        metrics = {
            "Best-record examinees": r"Best-record examinees[|\s|]+([0-9,]+)",
            "Years covered": r"Years covered[|\s|]+([0-9,]+)",
            "Median TRUE raw score": r"Median TRUE raw score[|\s|]+([0-9.]+)",
            "Median percentile rank": r"Median percentile rank[|\s|]+([0-9.]+)",
            "Unique examinees": r"Unique examinees[|\s|]+([0-9,]+)",
            "Repeat takers": r"Repeat takers[|\s|]+([0-9,]+)",
            # INFRA-04: labels in page_01 are "Observable cohort size" and "Confirmed PLE
            # share (observable)" — match up to the next pipe rather than a fixed char class.
            "Observable cohort": r"Observable cohort[^\n|]*\|\s*([0-9,]+)",
            "Confirmed PLE share": r"Confirmed PLE share[^\n|]*\|\s*([0-9.]+%)",
        }
        for key, pattern in metrics.items():
            m = re.search(pattern, text)
            if m:
                overview[key] = m.group(1)
    
    # Page 4 citizenship metrics
    p4_path = RESULTS_DIR / "04_score_bins.md"
    if p4_path.exists():
        text = p4_path.read_text(encoding="utf-8")
        m = re.search(r"FOREIGNER_STATUS[^#]*Filipino[|\s|]*([0-9,]+)", text)
        if m:
            overview["Filipino (citizenship)"] = m.group(1)
        m = re.search(r"Verified Foreigner[|\s|]*([0-9,]+)", text)
        if m:
            overview["Verified Foreigner"] = m.group(1)
        m = re.search(r"Likely Foreigner[|\s|]*([0-9,]+)", text)
        if m:
            overview["Likely Foreigner"] = m.group(1)
    
    return overview


def build_master():
    print("Building master report...")
    
    overview = get_all_metrics()
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as master:
        # Title
        master.write("# NMAT Analysis — Complete Data Extraction Report\n\n")
        master.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        master.write(f"**Data source:** NMAT_Exodus.parquet (Pipeline 4)\n\n")
        master.write(f"**Total pages:** 13\n\n")
        master.write("---\n\n")
        
        # Overview section with key metrics
        master.write("## Overview — Key Metrics at a Glance\n\n")
        master.write("| Metric | Value |\n")
        master.write("|--------|-------|\n")
        for key in [
            "Best-record examinees", "Years covered", "Median TRUE raw score",
            "Median percentile rank", "Unique examinees", "Repeat takers",
            "Observable cohort", "Confirmed PLE share",
            "Filipino (citizenship)", "Verified Foreigner", "Likely Foreigner",
        ]:
            if key in overview:
                master.write(f"| {key} | {overview[key]} |\n")
        master.write("\n---\n\n")
        
        # Table of contents
        master.write("## Table of Contents\n\n")
        for num, name in PAGE_ORDER:
            master.write(f"- [{num}. {name}](#{num.lower().replace(' ', '-').replace('&', 'and')}-{name.lower().replace(' ', '-').replace('&', 'and')})\n")
        master.write("\n---\n\n")
        
        # Append each page's content
        for num, name in PAGE_ORDER:
            page_file = RESULTS_DIR / f"{num}_{name.lower().replace(' & ', '_').replace(' ', '_')[:50]}.md"
            
            # Try alternate filenames
            if not page_file.exists():
                alt_patterns = [
                    f"{num}_*.md",
                ]
                from glob import glob
                matches = list(RESULTS_DIR.glob(f"{num}_*.md"))
                if matches:
                    page_file = matches[0]
            
            if page_file.exists():
                content = page_file.read_text(encoding="utf-8")
                # Remove the title (already in TOC)
                lines = content.split("\n")
                # Skip the first h1 and blank lines
                content_clean = "\n".join(lines[1:]).strip()
                
                master.write(f"\n\n")
                master.write(f'<a id="{num.lower()}-{name.lower().replace(" ", "-").replace("&", "and")}"></a>\n\n')
                master.write(content_clean)
                master.write("\n\n---\n\n")
                print(f"  Appended: {page_file.name}")
            else:
                master.write(f"\n\n## Page {num}: {name}\n\n*Content not found.*\n\n---\n\n")
                print(f"  NOT FOUND: {num}_{name}")
        
        # Footer
        master.write("\n\n*Report generated by `aggregate_all.py`. All data from NMAT_Exodus.parquet.*\n")
    
    size_mb = OUTPUT_FILE.stat().st_size / (1024 * 1024)
    print(f"\nMaster report saved: {OUTPUT_FILE} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    build_master()
