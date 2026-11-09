# 0054. Enforce goals and the decide-or-ask rule with hooks, on both hosts

Status: replaced by [decision 0058](0058-enforce-goals-and-the-decide-or-ask-rule-with-hook.md)

## Context

The user chose a command hook for the Stop check (FF-32 A), since a prompt hook keeps its prompt in settings and exists only under Claude Code; [decision 0053](0053-work-under-both-claude-code-and-codex.md) needs both hosts.

## Decision

Decided 2026-11-04. `hooks/prompts/goals.md` holds the goals and the decide-or-ask rule as the agent's prompt; `docs/goals.md` explains the goals to people. SessionStart and UserPromptSubmit hooks load the prompt into context, under Claude Code from `.claude/settings.json` and under Codex from `.codex/config.toml`. The Stop check is a command hook, `hooks/stop.py <host>`: it reads its prompt from `hooks/prompts/stop-check.md`, asks the host's own CLI on its smallest model (`claude -p --model haiku`, `codex exec --model gpt-6-luna`) whether the last message asks to approve something already decided, and blocks the stop with the reason. It respects `stop_hook_active`, prints one JSON object both hosts read, and exits 0. Settings hold no prompts. Every recorded rule the framework depends on is enforced by a hook or a check where one can enforce it.

## Consequences

- Replaces [decision 0052](0052-enforce-goals-and-the-decide-or-ask-rule-with-hook.md).
