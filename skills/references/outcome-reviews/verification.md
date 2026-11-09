# Outcome review: Verification

Rows: each requirement for rule 1; each scenario and each measure for rules 2–7. Judge each by the description's own words, not by imagined runs.

1. Together, the scenarios and measures citing a requirement describe a check that fails if any part of it isn't met. A separate check for each listed item, case, level or term isn't needed.
2. The scenario or measure describes a check of the result the requirement states.
3. What it describes as passing includes every way the requirements it cites, taken together, allow the user to get that result from the starting state the scenario sets up. A case the starting state doesn't set up is not judged.
4. Each thing the scenario's pass condition names, other than what the work being verified produces, is set up in its starting state or in what the preamble sets for every scenario.
5. What it describes as passing is what the user sees, not the system's own record that it succeeded.
6. It states the expected result, unless it is a measure recorded only for tracking.
7. What it describes as passing depends on no other scenario or measure.

## Output

A grid: one row per item, one column per rule, every cell PASS or FAIL. A FAIL quotes the words that fail. For rule 2, a PASS quotes, for each requirement the row cites, that requirement's result and the row's words that check it. For rule 4, a PASS quotes, for each thing the pass condition names, where the starting state or the preamble sets it up. A cell with a missing quote is a FAIL. A rule that doesn't apply to an item is marked "n/a". Judge nothing outside these rules.
