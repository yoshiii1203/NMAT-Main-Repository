Please read through the guide for the analysis.
1. Objective of the Assignment
The current task is to produce a descriptive and trend-based policy report on NMAT performance across years, examinee background, and score stability.

This phase focuses on:

NMAT raw scores, standardized scores, and percentile ranks

Distributional analysis using percentile deciles

Stability of exam performance across years

Background-based comparisons (pre-med, university type)

Descriptive alignment with PLE passers (no new matching work)

This assignment does NOT include extending or redesigning NMAT–PLE matching logic.

2. Data Files to Be Used
A. Core NMAT Files (Primary Analysis Sources)
The following Excel files are available and may be used jointly:

NMAT Data 2006–2018 – RAW

NMAT_Data_2006–2018.Final (With Initial Observations)

These files already include initial cleaning and harmonization, notably:

Cleaning and standardization of schools/universities attended prior to NMAT

Classification of universities into:

Public

Private

Foreign
(Foreign examinees are of particular policy interest)

Cleaned and grouped previous degree / pre-med classification, e.g.:

Medical & Allied

Natural Sciences

Other grouped categories

Instruction:
Treat these cleaned fields as authoritative, unless inconsistencies are explicitly detected and documented.

B. NMAT_MATCHING_PLE File (Updated Scores + Context)
File: NMAT_MATCHING_PLE

This file contains:

Updated NMAT data linked to PLE matching work

Raw NMAT scores, including component-level scores

Records of matching outcomes (single match, multiple matches, unmatched)

Important Data Quality Findings
Initial checks have identified the following issues in NMAT_MATCHING_PLE:

Many records have missing values for total NMAT raw score

Recalculation of total raw score from component scores revealed mismatches in some cases, where:

Stored total raw score ≠ sum of component raw scores

These inconsistencies must be:

Flagged

Quantified

Documented prior to analysis

Instruction:
Do not silently overwrite total raw scores.
Any recalculated totals must be:

Stored in a new derived variable

Compared against the original field

Summarized in a data validation note

3. Joining and Integration Rules
Key Identifiers
The three files may be joined using:

NMAT Applicant Number, or

Student Number found in the New CEM DATA fields within NMAT_MATCHING_PLE

Integration Guidance
Use NMAT Applicant Number / Student No as the primary key

Validate joins by:

Row counts before and after merge

Duplicate key checks

Preserve file provenance:

Retain indicators of source file (RAW, FINAL, MATCHING_PLE)

Prefer:

Background variables from the cleaned NMAT files

Component-level raw scores from NMAT_MATCHING_PLE (when available and validated)

Any exclusions, unmatched records, or dropped rows must be explicitly reported.

4. Scope of Analysis
In Scope
Descriptive statistics and trends

Distributional analysis using percentile deciles

Stability analysis of raw scores and percentile ranks

Background-based comparisons

Descriptive summaries involving PLE passers (using existing matches only)

Out of Scope
Extending NMAT–PLE matching logic

Re-matching names or birthdates

Causal inference or predictive modeling

5. Key Variables for Analysis
Performance Measures
Raw scores (Part I, Part II; subtests if available)

Recalculated total raw score (derived, if needed)

Standardized scores

Percentile rank

Derived Policy Variables
Percentile deciles (D1–D10)

Examinee Background
Pre-med / previous degree classification

University type (Public / Private / Foreign)

Time Dimension
NMAT exam year (2006–2018)

6. Analysis Instructions
A. Overall Performance Trends
Yearly summaries:

Median and IQR of raw scores

Median and IQR of percentile ranks

Faceted boxplots by:

Year

Test part (Part I / Part II)

Interpretation focus:
Stability, gradual shifts, or structural breaks over time.

B. Stability of Exam Scores (Difficulty Proxy)
Use raw scores

Assess:

Median shifts

IQR consistency

Visual stability via boxplots

Statistical support:

Kruskal–Wallis tests by year

Effect sizes where feasible

Frame results as distributional stability, not definitive difficulty changes.

C. Decile-Based Distribution Analysis (Primary Policy Lens)
Convert percentile ranks into deciles

Analyze:

Distribution across deciles by year

Shifts in top (D8–D10) and bottom (D1–D3) deciles

Recommended visuals:

Stacked bar charts

Heatmaps (Year × Decile)

D. Background-Based Comparisons Using Deciles
1. University Type → Deciles
Public vs Private vs Foreign

Emphasis on representation patterns of Foreign examinees

2. Pre-med Background → Deciles
Medical & Allied

Natural Sciences

Other grouped categories


E. Alluvial / Flow Visualizations (Preferred)
Use alluvial plots to show:

University type → Decile distribution

Pre-med background → Decile distribution

(Where data allows) Decile → PLE passer status

These visuals are intended to illustrate performance pathways and “survival” into higher deciles, not individual trajectories.

7. Statistical Testing Guidance
Treat percentile rank and deciles as ordinal

Prefer non-parametric methods:

Kruskal–Wallis

Dunn post-hoc tests (adjusted)

Report effect sizes alongside p-values

8. Visualization Standards
Use ggplot2

Prefer faceting over dense grouping

Avoid histograms due to high dimensionality

Maintain consistent color encoding across years and groups

9. Reporting Format
Deliver outputs using RMarkdown, structured as:

Executive Summary

Data Sources and Integration Notes

Data Validation Findings (raw score issues included)

Overall Performance Trends

Decile-Based Distribution Analysis

Background-Based Comparisons

Stability Analysis

Policy-Relevant Insights

Limitations and Interpretation Notes

Appendices (tables, additional plots, validation summaries)

Your support and assistance on this work is much appreciated.