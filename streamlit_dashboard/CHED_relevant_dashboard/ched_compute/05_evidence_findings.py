"""
05_evidence_findings.py — Key Evidence for Policy Review (Tab 5).

Thin wrapper around ched_common.compute_tab5_finding_texts() -- the SAME
function dashboard.py and export_markdown.py call. This script used to be
an independent reimplementation of all 7 findings (a third copy of the
same logic, per audit 06 F1/F5); that reimplementation is what produced
the published 57/49-vs-56/48 median-percentile drift. Collapsing it to a
thin wrapper makes that class of drift structurally impossible here too.
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import ched_common as cc
from helpers import load_data, create_subsets, write_output, today_str

SCRIPT = "05_evidence_findings"
TITLE = "Key Evidence for Policy Review"


def compute():
    df = load_data()
    S = create_subsets(df)
    best = S["best"]
    obs = S["best_pre2015"]  # IS_BEST_OBSERVABLE_RECORD cohort (see helpers.create_subsets)

    findings = cc.compute_tab5_finding_texts(df, best, obs)

    lines = []
    lines.append(f"**Date:** {today_str()}")
    lines.append("")
    lines.append("The following findings synthesise the evidence from all preceding tabs.")
    lines.append("They are descriptive observations based on historical NMAT data (2006-2018) "
                  "and do not constitute regulatory recommendations.")
    lines.append("")

    for i, (title, body) in enumerate(findings, start=1):
        lines.append(f"## Finding {i}: {title}")
        lines.append("")
        lines.append(body)
        lines.append("")

    lines.append("---")
    lines.append("*These findings are limited to the NMAT examinee population. Key data gaps "
                  "include PLE failure rates, GIDA/IP status, medical school enrollment, and "
                  "institutional admission criteria. No medical-school identifier exists in "
                  "this dataset at all.*")

    body = "\n".join(lines)
    path = write_output(SCRIPT, TITLE, body)
    print(f"  Wrote {path}")
    return path


if __name__ == "__main__":
    compute()
