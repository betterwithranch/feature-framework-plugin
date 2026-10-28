# 0013. Enforce goals and the decide-or-ask rule with hooks

Status: accepted, 2026-10-28

## Context

An assessment of the session that built level 1 found about 30 user corrections and about 10 unnecessary approval requests in 22. Five corrections were for breaking a rule already recorded. Rules written in documents were not followed because nothing loaded or enforced them, and the goals drifted as the session went on.

## Decision

- `docs/goals.md` holds the goals and the decide-or-ask rule.
- A SessionStart hook (startup, resume, compact) and a UserPromptSubmit hook load it into context.
- A Stop prompt hook blocks ending a turn on a request to approve something already decided.

## Consequences

- The goals survive compaction and are restated on every prompt.
- Unnecessary approval requests are turned back before the user sees them.
- The Stop hook costs one small model call per turn and may misjudge; it is checked against real sessions and tuned like any other instruction.
