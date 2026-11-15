# 0073. Verification judges against the whole set of requirements

Status: accepted, 2026-11-10

## Context

Verification rule 3 was bounded to the requirements a row cites, taken together, and to the starting state the scenario sets up ([decision 0062](0062-verification-rules-3-and-4-bounded-to-what-a-scenario-cites-and-names.md), [decision 0065](0065-verification-rule-3-judges-the-starting-state-as-set-up.md)). Neither was approved. The user chose A (FF-74), said the approach is right, and asked that the line name no rule numbers: "does it need to specify rules by number? this is going to drift unless we actually need those numbers to properly describe the behavior".

## Decision

- The Verification review's opening adds: "The requirements are one set. Each scenario and measure is judged against the whole set, not against one requirement alone."
- Verification rule 3 reads: "What it describes as passing includes every way the requirements allow the user to get that result."

## Consequences

- Replaces 0062's rule 3 part and [decision 0065](0065-verification-rule-3-judges-the-starting-state-as-set-up.md).
- Amends the Verification review's rules, [decision 0044](0044-the-verification-review-s-rules.md).
