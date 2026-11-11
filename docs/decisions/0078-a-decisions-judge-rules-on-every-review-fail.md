# 0078. A decisions judge rules on every review FAIL

Status: accepted, 2026-11-11

## Context

The agent fixing a finding chose the fix by its own reading, made a wrong change and reran the review, until the four rounds ran out. [Decision 0077](0077-each-review-finding-goes-to-the-user-for-approval.md) sent every finding to the user instead. The user was asked whether to add a decisions judge between each review and any change, and drop 0077 (FF-80). The user chose A: "Add the decisions judge and the automatic check as described, drop 0077, and make the goals file's decide-and-report rule point to the judge's verdict."

## Decision

- After a review with any FAIL, nothing changes and no review starts until a fresh [decisions judge](../../skills/references/decisions-judge.md) rules on every FAIL. It reads the FAIL cells, `docs/goals.md`, the decision classification and every accepted record, and never the fixing agent's reasoning.
- Each FAIL gets one verdict: Settled, Rule misfire, Conflict or Missing. The agent applies only Settled changes, exactly as given. Every other verdict goes to the user.
- An automatic check, `skills/review-outcome/scripts/review_gate.py`, runs before every edit to the Outcome or the review rules and before a review starts. It refuses unless the current round has a verdict, the edit matches a Settled change, and no finding waits on the user.

## Consequences

- Replaces [decision 0077](0077-each-review-finding-goes-to-the-user-for-approval.md).
- `docs/goals.md` "Decide or ask", [decision 0029](0029-four-review-rounds-per-approved-version.md) and `CLAUDE.md` point to the judge for review findings.
- Adding the judge, the check and these records needs no verdict of its own, as this decision approves them.
