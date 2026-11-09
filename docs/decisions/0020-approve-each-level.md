# 0020. Approve each level

Status: accepted, 2026-11-02

## Context

The user said "each level needs approval before the next level should begin. that should be explicit."

## Decision

A level moves on only when its review passes and the user approves it. Approval is the user saying so; a correction, a question or "looks good, but" isn't approval. The levels approved this way are Outcome, Behaviour, Design and Slices; approving Slices lets Build start. Each level produces its own document only; working code is the result of Build. Approving a level makes the user's decisions and answers in it agreed: nothing in them is asked again, except for clarity or to resolve a conflict. The work's decisions in it stay the work's. All decisions need approval; fixes that aren't decisions don't.

## Consequences

- Replaces [decision 0015](0015-approve-only-open-decisions.md).
