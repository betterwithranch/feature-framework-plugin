# Outcome review: Verification

Rows: each requirement for rule 1; each scenario and each measure for rules 2–7. Judge each by the description's own words, not by imagined runs.

1. Together, the scenarios and measures citing a requirement describe a check that fails if any part of the requirement isn't met. A separate check for each listed item, case, level or term isn't needed.
2. The scenario or measure describes a check of the result the requirement states.
3. What it describes as passing includes every way the cited requirements together allow the user to get that result from the starting state the scenario sets up. A case the starting state doesn't set up is not judged.
4. Each thing the pass condition checks is either set up in the starting state or produced by the work being verified. What the document says applies to every scenario is part of each scenario's starting state.
5. What it describes as passing is what the user sees, not the system's own record that it succeeded.
6. A scenario states the expected result. So does a measure that isn't recorded only for tracking. A measure recorded only for tracking needs no expected result.
7. What it describes as passing depends on no other scenario or measure.

## Output

A grid: one row per item, one column per rule, every cell PASS or FAIL. A FAIL quotes the words that fail. A PASS for rule 2 quotes each cited requirement's result and the row's words that check that result. A PASS for rule 4 quotes a source for each thing checked by what the row describes as passing. The source is the starting state's words that set it up, the words that set it up in what the document says applies to every scenario, or the words saying the work produces it. A cell with a missing quote is a FAIL. A rule that doesn't apply to an item is marked "n/a". Judge nothing outside these rules.
