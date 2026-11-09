# 0069. Review grids quote the evidence for each part

Status: accepted, 2026-11-09

## Context

The Outcome's fourth set of review rounds didn't pass, and every FAIL in it was a real gap on text that had been there all along: earlier single judge runs had passed those rows without checking every part of them. The user chose a review that is an exhaustive checklist marking every item pass or fail, not a sampling (FF-52 A, [decision 0041](0041-structure-scripts-and-four-scoped-yes-no-reviews.md)), and goal 5 says to fix the instruction so a gate converges.

## Decision

- Verification rule 2: a PASS quotes, for each requirement the row cites, that requirement's result and the row's words that check it.
- Verification rule 4: a PASS quotes, for each thing the pass condition names, where the starting state or the preamble sets it up.
- Provenance rules 1 and 2: a PASS quotes, for each part of the statement, its source or the marking that shows it as the work's.
- A cell with a missing quote is a FAIL. The round structure is unchanged.

## Consequences

- Amends the Verification and Provenance reviews' output, [decision 0044](0044-the-verification-review-s-rules.md) and [decision 0045](0045-the-provenance-review-s-rules.md).
