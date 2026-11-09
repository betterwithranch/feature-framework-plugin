# 0052. Enforce goals and the decide-or-ask rule with hooks

Status: replaced by [decision 0054](0054-enforce-goals-and-the-decide-or-ask-rule-with-hook.md)

## Context

[decision 0051](0051-settings-hold-no-prompts-prompts-and-docs-are-sepa.md) separates prompts from docs; the rest of [decision 0013](0013-enforce-goals-with-hooks.md) stands.

## Decision

Decided 2026-11-04. `.claude/prompts/goals.md` holds the goals and the decide-or-ask rule as the agent's prompt; `docs/goals.md` explains the goals to people. A SessionStart hook (startup, resume, compact) and a UserPromptSubmit hook load the prompt into context. A Stop prompt hook blocks ending a turn on a request to approve something already decided. Every recorded rule the framework depends on is enforced by a hook or a check where one can enforce it.

## Consequences

- Replaces [decision 0013](0013-enforce-goals-with-hooks.md).
