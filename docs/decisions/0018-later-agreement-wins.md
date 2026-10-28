# 0018. When agreements conflict, the later one wins

Status: accepted, 2026-10-28

## Context

The approved Outcome said work moves to the next level only on the user's explicit agreement. [Decision 0015](0015-approve-only-open-decisions.md), made later, said a level moves on when its review passes. The decide-or-ask rule said to ask whenever agreed things conflict, so the user was asked to settle a conflict the later decision had already settled.

## Decision

- When agreed things conflict, the later agreement wins. The earlier artifact is updated to match, and the change is reported.
- The user is asked only when it's unclear which agreement came later.
- The Outcome now says work moves on when a level passes its review, matching decision 0015.

## Consequences

- Conflicts between agreements no longer reach the user by default.
- A change to an approved artifact runs its gate again.
