# 0050. How the scenarios run is deferred to the level that writes the tests

Status: accepted, 2026-11-07

## Context

The user said "if these aren't concerns for level 1, they should be deferred, not answered now", and the approved Scope rule 6 ([decision 0042](0042-the-scope-review-s-rules.md)) puts thresholds and procedures at a later level.

## Decision

The Outcome keeps each scenario's starting state and what it must show to pass, checked automatically with no person needed. How the scenarios run moves to the level that writes the tests: the run count, the hosts they run under, the scripted user, and the kinds of check. This removes the approved Outcome's "passes only if all 10 runs pass" and the later "several times under Claude Code and several times under Codex"; the open questions list what that level settles. R39, that the framework enforces itself the same way under both hosts, stays.
