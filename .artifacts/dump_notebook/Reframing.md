Yes — the new Streamlit page should be a **decision-support** page built around explicit policy questions, not just an exploratory dashboard. Your current pipeline already contains strong evidence that NMAT aligns with later PLE passage: in the observable best-record cohort, confirmed PLE passers have a much higher median percentile rank than those with no confirmed PLE match (73 vs 36), and the confirmed-passer share rises steadily from 8.77% in D1 to 76.25% in D10.

That means the page should primarily answer: “Does NMAT meaningfully separate later PLE passers from non-passers, and what happens if we relax the admission threshold?” rather than just “what does the data look like?”

## Ground rules

Use `ISBESTNMATRECORD == True` for person-level reporting, because the pipeline explicitly marks one best record per person and the data dictionary recommends that flag for trend analyses to avoid inflation from repeat attempts. Use `ISPLEANALYSISSAFE == True` plus the observable best-record cohort for any PLE-linked claim, because the current workflow warns that later NMAT cohorts can be misclassified if you ignore the limited PLE observation window and notes that PLE coverage ends in 2022.[^3^1](data_dictionary-6.md)

Also, do **not** treat `UNITYPE = Foreign` as equivalent to “foreign national.” The surfaced data dictionary clearly shows university-type and university-location fields, but no explicit citizenship field is visible in the documented columns, so “true foreign nationals” should be treated as a separate classification task rather than inferred from school type alone.[^4](data_dictionary-6.md)

## Question bank

Below is the question set I would build the new page around. These are phrased the way a dean, regulator, or admissions decision-maker would ask them.

### NMAT validity

1. Does higher NMAT percentile correspond to a higher probability of confirmed PLE passage?
2. How much higher are the median NMAT scores of confirmed PLE passers versus non-matches?
3. Is the NMAT signal consistent for raw score, percentile rank, GPS, Part I, and Part II?
4. At what percentile bands does the probability of confirmed PLE passage change sharply?
5. Are top-decile examinees disproportionately represented among confirmed PLE passers?
6. Are low-decile examinees disproportionately concentrated in the no-confirmed-match group?
7. Is the relationship monotonic, or are there score bands where the pattern weakens?
8. Does NMAT still discriminate well after controlling by school type and pre-med background?
9. Which NMAT metric is the strongest operational screen: percentile, raw total, GPS, Part I, or Part II?
10. What is the clearest “headline” statement the institution can defend publicly?

### Threshold policy

1. What would likely be lost if the NMAT admission threshold were lowered?
2. How many additional applicants would enter under lower threshold scenarios?
3. What is the confirmed PLE share of those marginal admits compared with current admits?
4. Is there a threshold below which the no-confirmed-match share becomes too high?
5. Which thresholds best balance access and downstream licensure alignment?
6. How different are the risk profiles at percentile cutoffs such as 40, 50, 60, 70, and 80?
7. If a lower threshold is proposed, which compensating conditions should be required?
8. Should there be one threshold for all applicants, or a main threshold plus exception rules?
9. How many “successful exceptions” exist, and how unusual are they?
10. What policy statement can be made without overclaiming causality?

### Institutional comparisons

1. Do public, private, and foreign-school examinees have different NMAT distributions?
2. Do public, private, and foreign-school examinees have different confirmed PLE shares?
3. Is the NMAT-to-PLE relationship consistent inside each university type?
4. Does a given percentile mean the same thing across public, private, and foreign groups?
5. Which university types contribute most of the D8-D10 population?
6. Which university types are overrepresented in lower deciles?
7. Are observed foreign-school outcomes being distorted by mixing Filipino graduates and true foreign nationals?
8. Does university location matter separately from university type?
9. Are there specific schools within each type driving the pattern?
10. Where should policy be general, and where should it be institution-specific?

### Foreign disaggregation

1. Among `UNITYPE = Foreign`, who are Filipino graduates of foreign universities and who are true foreign nationals?
2. Of those who took the NMAT but have no PLE record, how many are likely simply not PLE-eligible because of citizenship?
3. What share of the apparent “no confirmed PLE match” in the foreign group disappears after excluding non-citizens or non-eligible examinees?
4. Among foreign-school examinees who are PLE-eligible, how do their NMAT and PLE patterns compare with public and private groups?
5. Are foreign nationals clustered in specific schools, years, centers, or score bands?
6. Do foreign nationals differ in repeat-taking behavior?
7. How many foreign nationals eventually pass the PLE, if any?
8. How many foreign-school examinees are actually Filipinos who should stay in the regular PLE-eligible analysis?
9. What portion of “foreign” is a school-classification issue versus a nationality issue?
10. What are the top schools and nationalities represented in that subgroup?

### Background and fairness

1. Does NMAT predict confirmed PLE passage within each course group?
2. Are some pre-med backgrounds overrepresented among high scorers but not necessarily among passers?
3. Which course groups have the highest D8-D10 share?
4. Which course groups have the highest confirmed PLE share in the observable cohort?
5. Do Part I and Part II strengths differ by course group in ways relevant to admissions?
6. Are there sex-pattern differences in performance or PLE alignment that matter for interpretation?
7. Are repeat takers meaningfully improving, and does that improvement change downstream outcomes?
8. Should repeat takers be evaluated on best attempt, latest attempt, or first attempt for policy purposes?
9. Are there subgroups where the current threshold seems too lenient?
10. Are there subgroups where the current threshold is defensible but should trigger additional support rather than exclusion?

### Data quality and interpretation

1. Which results are safe to treat as person-level?
2. Which results are safe to treat as PLE-linked?
3. Which cohorts are not yet fully observable for PLE passage?
4. How many records rely on exact, deterministic, or manual match pathways?
5. How many foreign-school conclusions are unstable because of small cell counts?
6. Which outputs should display sample-size warnings?
7. Where is “no confirmed PLE match” not the same as “failed the PLE”?
8. Which results could be challenged by decision-makers, and how will you preempt that challenge?
9. Which charts risk being misunderstood without a note on observability?
10. Which findings are descriptive, and which are suitable for policy recommendation?

## Streamlit structure

Your current app already has strong building blocks: the existing pages cover PLE alignment, repeat takers, subtest profiles, year-gap and gender patterns, and statistical tests, while the results file already contains the core validity pieces such as score-profile comparisons, decile composition, top-decile survival, and policy tables by year, course, and university type. The best move is to create one new page that reuses those computations but reframes them as “question → short answer → evidence → implication.”[^1](dashboard-7.py)

I would structure the new page like this:

| Module                  | What it answers                                                   | Must show                                                                                    |
| ----------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Policy summary          | Is NMAT a useful screening tool?                                  | 4–6 KPI cards, one-line policy takeaways, observability note                                 |
| NMAT vs PLE             | Does higher NMAT align with later PLE passage?                    | Score gap table, decile-to-PLE chart, threshold curve                                        |
| Threshold scenarios     | What happens if the cutoff is lowered?                            | Scenario table by percentile threshold, incremental admit counts, expected confirmed-PLE mix |
| Institutional breakdown | Does the pattern hold across school types?                        | Public vs private vs foreign tables, decile heatmaps, school drilldown                       |
| Foreign disaggregation  | Are “foreign” records being misread?                              | New 4-category framework, citizenship-evidence tags, no-PLE reason table                     |
| Background patterns     | Are course group, sex, and repeat taking changing interpretation? | Course-group outcome table, subtest profiles, repeat-taker summary                           |
| Data quality            | What claims are safe to make?                                     | Match-quality counts, cohort observability rules, caveat panel                               |

For each question block, use the same presentation template:

- Question
- Short answer
- Why it matters
- Chart
- Supporting table
- Interpretation note
- Caveat

That format will make the page read like a policy memo rather than a notebook dump.

## Foreign split

The foreign-school issue deserves its own redesign because the present `Foreign` bucket is too coarse. In the existing analysis, the best-record subset contains 3,270 `Foreign` records, and in the observable best-record cohort the `Foreign` group has 2,122 records with 786 confirmed passers, lower than public and private on confirmed-PLE share; that is exactly why mixing Filipinos in foreign schools with actual foreign nationals can distort interpretation.[^1](3_NMAT_PLE_Results-5.md)

I recommend creating a new derived field such as `FOREIGN_CLASS_4` with these categories:

- Public
- Private
- Foreign university – Filipino / PLE-eligible
- Foreign university – foreign national / likely non-PLE-eligible

Then create a second field such as `CITIZENSHIP_EVIDENCE_LEVEL`:

- Explicit citizenship field
- Registrar / official roster match
- Other administrative source
- Manual verified
- Unknown

Because the surfaced data dictionary does not show a citizenship field, this module should be built as an evidence-based disaggregation workflow, not a name-based guessing exercise. The page should then answer three distinct questions: “Who is foreign by school classification?”, “Who is foreign by citizenship?”, and “Who is excluded from PLE interpretation because they were not realistically in the PLE-eligible pool?”[^4](data_dictionary-6.md)

## Must-ship outputs

The first release should answer the most defensible policy claims already supported by your current analysis. The current results already show that confirmed PLE passers have much higher medians across raw score, percentile, GPS, Part I, and Part II; that D8-D10 contains 53.5% of confirmed passers versus 19.8% among the no-confirmed-match group; and that within-decile confirmed-PLE composition increases steadily from D1 to D10.[^1](3_NMAT_PLE_Results-5.md)

So I would make these the non-negotiable cards and visuals on day 1:

1. “Do higher NMAT scorers have better confirmed PLE alignment?”
2. “How large is the score gap between confirmed passers and non-matches?”
3. “How does confirmed-PLE share change by decile?”
4. “What threshold scenarios would we be trading off?”
5. “Does the pattern hold by public, private, and foreign-school groups?”
6. “Does the pattern hold by course group?”
7. “Who are repeat takers, and do they improve?”
8. “What portion of foreign-school non-PLE cases may simply be non-eligible by citizenship?”
9. “Which cohorts are observable and safe to interpret?”
10. “What caveats prevent misuse of the findings?”

One framing point matters a lot: say that NMAT shows strong **predictive alignment** with later PLE passage, not that it mechanically causes PLE success. That keeps the page empirically strong and harder to attack.

Would you like me to turn this into a Streamlit implementation blueprint next — with exact section titles, widget layout, chart specs, and the derived columns needed for the new foreign-national module?  
[^10][^11][^5][^6][^7][^8][^9]

⁂
