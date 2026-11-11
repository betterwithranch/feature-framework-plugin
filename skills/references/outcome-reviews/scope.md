# Outcome review: Scope

Rows: the "for whom" line, each requirement, the paragraph above the scenario table, each scenario and each measure. The rule on who the feature is for applies only to the "for whom" row. The rule on requirements applies only to requirement rows. The rule on scenarios applies only to scenario rows. The rule on measures applies only to measure rows. The other rules apply to every row.

1. The document says who the feature is for.
2. Each requirement is a result the user can observe.
3. Each scenario states its starting state, what happens and what passes, as results the user can observe. What the document says applies to every scenario counts as stated.
4. Each measure is taken on real use and has a target.
5. The statement says what the user gets or how that is judged, not how the agent produces it.
6. The statement sets no definition, rule, threshold or procedure. Those belong to a later level.
7. The statement names no place where anything lives: no file, component or tool.
8. The statement excludes nothing from the feature and covers no edge case.

## Output

A grid: one row per item and one column per rule. Each cell is PASS or FAIL. A rule passes any item it doesn't apply to. A FAIL quotes the words that fail. Judge nothing outside these rules.
