# Outcome review: Verification

Rows: each requirement for rule 1; each scenario and each measure for rules 2–7. Judge each by the description's own words, not by imagined runs.

1. Together, the scenarios and measures citing a requirement describe a check of every part of it.
2. The scenario or measure describes a check of the result the requirement states.
3. What it describes as passing includes every way the requirement allows the user to get that result.
4. The starting state describes everything the scenario depends on; nothing is left for the work being verified to produce first.
5. What it describes as passing is what the user sees, not the system's own record that it succeeded.
6. It states the expected result, unless it is a measure recorded only for tracking.
7. What it describes as passing depends on no other scenario or measure.

## Output

A grid: one row per item, one column per rule, every cell PASS or FAIL. A FAIL quotes the words that fail. A rule that doesn't apply to an item is marked "n/a". Judge nothing outside these rules.
