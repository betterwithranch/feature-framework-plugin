# 0014. Autonomy policy and MVP first

Status: accepted, 2026-10-28

## Context

Level 1 took about 45 user turns and about 70 review runs before passing. Autonomy worked when the agent had a measurable stop condition, such as a review loop run until three clean results. It failed when each step waited on the user. The framework was being refined in full before any real feature had used it.

## Decision

- The framework includes an autonomy policy: what the agent decides alone, what it asks, and the stop condition and budget for each gate.
- Every recorded rule the framework depends on is enforced by a hook or a check, not only written down.
- The framework ships as a minimal version and is tried on one real feature before levels 2–5 are refined.

## Consequences

- Gates run unattended to their stop condition; the user sees results, not progress requests.
- Whether every level needs the user's approval, or only open decisions do, is set by the autonomy policy and is the user's call.
