# 0065. Verification rule 3 judges the starting state as set up

Status: superseded by 0073 (FF-74 A), 2026-11-10

## Context

Verification rule 3 read "What it describes as passing includes every way the requirements it cites, taken together, allow the user to get that result." S10, the user's own scenario, passed it in two review rounds and failed it in the next on unchanged text: the judge imagined that "something the sample project shows" might be a project term, which needs no marking, though the scenario sets up a fact the work finds. Each rule is judged by the description's own words, not by imagined runs ([decision 0044](0044-the-verification-review-s-rules.md)), and a verdict that changes on unchanged text is fixed in the rule, not the document.

## Decision

Verification rule 3 reads: "What it describes as passing includes every way the cited requirements together allow the user to get that result from the starting state the scenario sets up. A case the starting state doesn't set up is not judged."

## Consequences

- Amends the Verification review's rules, [decision 0044](0044-the-verification-review-s-rules.md).
