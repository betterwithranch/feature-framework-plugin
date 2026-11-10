# Outcome review: Verification

Rows: each requirement, each scenario and each measure. The rule on whether the checks together cover a requirement applies to requirement rows. Every other rule applies to scenario and measure rows. Judge each by the description's own words, not by imagined runs.

The requirements are one set. Each scenario and measure is judged against the whole set, not against one requirement alone.

1. Together, the scenarios and measures citing a requirement describe a check that fails if any part of the requirement isn't met. A separate check for each listed item, case, level or term isn't needed.
2. The scenario or measure describes a check of the result the requirement states.
3. What it describes as passing includes every way the requirements allow the user to get that result.
4. Each thing the pass condition checks is either set up in the starting state or produced by the work being verified. What the document says applies to every scenario is part of each scenario's starting state.
5. What it describes as passing is what the user sees, not the system's own record that it succeeded.
6. It states the expected result.
7. What it describes as passing depends on no other scenario or measure.

## Output

A grid: one row per item and one column per rule. Each cell is PASS or FAIL. A rule passes any item it doesn't apply to. A FAIL quotes the words that fail. A PASS on checking a cited requirement's result quotes that result and the row's words that check it. A PASS on where each thing the pass condition checks comes from quotes its source. The source is the starting state's words that set it up, the words that set it up in what the document says applies to every scenario, or the words saying the work produces it. A PASS on an item a rule doesn't apply to needs no quote. A PASS missing a quote it needs is a FAIL. Judge nothing outside these rules.
