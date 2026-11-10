# 0069. Review grids quote the evidence for each part

Status: proposed, 2026-11-09

## Context

The Outcome's fourth set of review rounds didn't pass, and every FAIL in it was a real gap on text that had been there all along: earlier single judge runs had passed those rows without checking every part of them. The user chose a review that is an exhaustive checklist marking every item pass or fail, not a sampling (FF-52 A, [decision 0041](0041-structure-scripts-and-four-scoped-yes-no-reviews.md)), and goal 5 says to fix the instruction so a gate converges.

## Decision

- Verification rule 2: "A PASS on checking a cited requirement's result quotes that result and the row's words that check it."
- Verification rule 4: "A PASS on where each thing the pass condition checks comes from quotes its source. The source is the starting state's words that set it up, the words that set it up in what the document says applies to every scenario, or the words saying the work produces it."
- Provenance rules 1 and 2: "A PASS on where a statement comes from, or on what a statement marked as the agent's decides, quotes the source of each part of the statement, or the marking that shows that part as the agent's."
- A PASS on an item a rule doesn't apply to needs no quote. A PASS missing a quote it needs is a FAIL. The round structure is unchanged.

## Consequences

- Amends the Verification and Provenance reviews' output, [decision 0044](0044-the-verification-review-s-rules.md) and [decision 0045](0045-the-provenance-review-s-rules.md).
