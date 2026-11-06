# Outcome review: Scope

Rows: the "for whom" line, each requirement, the scenario preamble, each scenario and each measure. Rule 1 applies only to the "for whom" row, rule 2 only to requirement rows, rule 3 only to scenario rows and rule 4 only to measure rows; every other cell in rules 1–4 is "n/a". Rules 5–8 apply to every row.

1. The document says who the feature is for.
2. Each requirement is a result the user can observe.
3. Each scenario states its starting state, what happens and what passes, as results the user can observe.
4. Each measure is taken on real use and has a target.
5. The statement says what the user gets or how that is judged, not how the work produces it.
6. The statement sets no definition, rule, threshold or procedure; those belong to a later level.
7. The statement names no place where anything lives: no file, component or tool.
8. The statement excludes nothing from the feature and covers no edge case.

## Output

A grid: one row per item, one column per rule, every cell PASS or FAIL. A FAIL quotes the words that fail. A rule that doesn't apply to an item is marked "n/a". Judge nothing outside these rules.
