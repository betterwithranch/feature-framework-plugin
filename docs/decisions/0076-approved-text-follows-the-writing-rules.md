# 0076. Approved text follows the writing rules

Status: accepted, 2026-11-10

## Context

The writing rules ([decision 0070](0070-writing-rules.md), FF-70 A; [decision 0074](0074-name-a-rule-by-what-it-checks.md), FF-75 A) apply to every level's documents, the review rules and the decision records. Some text the user approved broke them. Under `docs/goals.md` "Decide or ask", which the user confirmed governs this work, applying an agreed rule is not a new decision.

## Decision

- These are reworded to the writing rules, with the same meaning:
  - Scope's rule on definitions, rules, thresholds and procedures
  - Verification's rule on each cited requirement's result
  - Verification's rule on where each checked thing comes from
  - Provenance's rule on clashes with project terms
  - The glossary review's rule on terms the project already uses
  - The Outcome definition's contents list, its structure checks list and "Nothing runs at this level."
- write-outcome's line on stating once what the user does in every scenario applies `CLAUDE.md` "State each fact once", the writing rules' "shortest wording" and Verification's rule on where each checked thing comes from (FF-69 A).
- write-outcome's line on moving a later-level statement to the open questions applies [decision 0009](0009-block-lower-level-questions.md) and goal 2, "Set lower-level questions aside for the level that owns them".

## Consequences

- The approved records ([0042](0042-the-scope-review-s-rules.md), [0044](0044-the-verification-review-s-rules.md), [0045](0045-the-provenance-review-s-rules.md), [0048](0048-the-glossary-review-s-rules.md), [0062](0062-verification-rules-3-and-4-bounded-to-what-a-scenario-cites-and-names.md)) keep the wording the user approved, as history.
