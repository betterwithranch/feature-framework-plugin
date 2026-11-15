# 0079. The agent writes every fix; the judge checks it

Status: accepted, 2026-11-15

## Context

[Decision 0029](0029-four-review-rounds-per-approved-version.md) says "Findings are fixed with the level's write skill, including its after-a-fix self-check." [Decision 0078](0078-a-decisions-judge-rules-on-every-review-fail.md) says "The agent applies only Settled changes, exactly as given", and its judge wrote the exact old and new text. The two disagree on who writes a fix. The user chose to split them (FF-84 A).

## Decision

- The agent writes every fix with the level's write skill, including its after-a-fix self-check.
- The decisions judge gives verdicts with quotes. A Settled verdict says what the quoted words require, and gives no text to apply.
- Before a fix is applied, the judge checks it against its verdict, like any other action. Only a fix the judge passes is applied.

## Consequences

- Replaces 0078's "The agent applies only Settled changes, exactly as given."
- The review gate allows an edit to the Outcome or the review rules only when the judge has passed that exact edit.
