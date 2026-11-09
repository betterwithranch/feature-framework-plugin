# 0063. Verification rule 1 needs no check per item or case

Status: accepted, 2026-11-09

## Context

The Outcome's second set of four review rounds didn't pass. In each round Verification rule 1, "Together, the scenarios and measures citing a requirement describe a check of every part of it", found a new part with no check of its own: an interview at every level (R9), each requirement in a document (R33), every project term (R20), the case where the work settles what it needs (R31), and each kind of thing that is the user's to settle (R32). [Decision 0032](0032-one-verification-for-a-requirement-that-holds-across-cases.md) and [decision 0034](0034-every-requirement-covered-structure-is-a-later-level-s.md) say a requirement needs a verification that fails if it isn't met, and that one check per listed item or case is an implementation detail and not a review finding. The rule didn't say so. CLAUDE.md says that after four rounds that don't pass, the work fixes the instructions involved, and [decision 0059](0059-no-exception-to-an-absolute-term-anywhere.md) says a review rule that fails to enforce a recorded decision is fixed to match it.

## Decision

Verification rule 1 reads: "Together, the scenarios and measures citing a requirement describe a check that fails if any part of it isn't met. A separate check for each listed item, case, level or term isn't needed."

## Consequences

- Amends the Verification review's rules, [decision 0044](0044-the-verification-review-s-rules.md).
