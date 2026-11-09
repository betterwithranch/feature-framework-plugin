# 0060. A measure recorded only for tracking has no target

Status: accepted, 2026-11-09

## Context

Scope rule 4 read "Each measure is taken on real use and has a target." The Outcome's measure of planning misses, the user's own approved measure, says "It's not a pass bar", and [decision 0026](0026-questions-per-level-are-tracked-not-targeted.md) records the user's "we should measure for tracking, but not enforce any expected number of questions". Under [decision 0059](0059-no-exception-to-an-absolute-term-anywhere.md), a review rule that fails to enforce a recorded decision is fixed to match it.

## Decision

- Scope rule 4 reads: "Each measure is taken on real use, and has a target unless it is recorded only for tracking."
- Verification rule 6 reads: "It states the expected result, unless it is a measure recorded only for tracking."

## Consequences

- Amends the Scope review's rules, [decision 0042](0042-the-scope-review-s-rules.md), and the Verification review's rules, [decision 0044](0044-the-verification-review-s-rules.md).
