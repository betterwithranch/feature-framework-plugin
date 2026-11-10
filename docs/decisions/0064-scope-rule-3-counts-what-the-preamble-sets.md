# 0064. Scope rule 3 counts what the document says applies to every scenario

Status: proposed, 2026-11-09

## Context

Scope rule 3 read "Each scenario states its starting state, what happens and what passes, as results the user can observe." S20 states its starting state and what passes, and the paragraph above the scenario table sets what happens in every scenario unless it says otherwise. One review round passed S20 on that, and the next failed the same text because "nothing happens in the scenario". A verdict that changes on unchanged text is fixed in the rule, not the document. [Decision 0062](0062-verification-rules-3-and-4-bounded-to-what-a-scenario-cites-and-names.md) already lets what the document says applies to every scenario count for Verification rule 4, and write-outcome says to state that once, before the scenarios.

## Decision

Scope rule 3 adds: "What the document says applies to every scenario counts as stated."

## Consequences

- Amends the Scope review's rules, [decision 0042](0042-the-scope-review-s-rules.md).
