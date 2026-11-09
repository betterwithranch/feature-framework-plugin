# 0058. Enforce goals and the decide-or-ask rule with hooks, on both hosts

Status: accepted, 2026-11-06, the work's decision

## Context

[decision 0054](0054-enforce-goals-and-the-decide-or-ask-rule-with-hook.md)'s stated commands loaded this repo's hooks into the nested check, and its SessionStart matchers left forked and cleared sessions without the goals prompt that [decision 0054](0054-enforce-goals-and-the-decide-or-ask-rule-with-hook.md) requires every session to have.

## Decision

Keeps everything the user chose in [decision 0054](0054-enforce-goals-and-the-decide-or-ask-rule-with-hook.md) (FF-32 A): `hooks/prompts/goals.md` holds the goals and the decide-or-ask rule as the agent's prompt, and `docs/goals.md` explains them to people. SessionStart and UserPromptSubmit hooks load the prompt into context under Claude Code (`.claude/settings.json`) and Codex (`.codex/config.toml`). SessionStart has no matcher, so every source fires: startup, resume, clear, compact and fork, as both hosts document them (code.claude.com/docs/en/hooks-guide; learn.chatgpt.com/docs/hooks). The Stop check is a command hook, `hooks/stop.py <host>`. It reads `hooks/prompts/stop-check.md` and asks the host's own CLI on its smallest model whether the last message asks to approve something already decided. The nested call runs with this repo's hooks off. Claude Code: `claude -p --settings '{"disableAllHooks": true}' --model haiku --no-session-persistence` ("To temporarily disable all hooks without removing them, set "disableAllHooks": true", code.claude.com/docs/en/hooks-guide; --settings applies above project settings, /settings; `--bare` is not used because it never reads OAuth logins, /headless). Codex: `codex exec -c features.hooks=false --model gpt-6-luna --sandbox read-only --ephemeral` (learn.chatgpt.com/docs/config-file/config-reference, /docs/developer-commands, /docs/models). It blocks the stop with `decision: "block"` and `reason`, which both hosts read on Stop (code.claude.com/docs/en/hooks; for Codex, the Stop schema at www.turboai.dev/docs/codex/hooks, generated from codex-rs/hooks/src/events/stop.rs at rust-v0.163.0). It respects `stop_hook_active`, skips a null `last_assistant_message`, keeps the FEATURE_FRAMEWORK_STOP_CHECK guard, prints one JSON object and exits 0. Settings hold no prompts.

## Consequences

- Replaces [decision 0054](0054-enforce-goals-and-the-decide-or-ask-rule-with-hook.md).
