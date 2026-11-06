# Feature framework

Takes a feature you've decided to build from intent to working code, one level at a time, so the build doesn't pull you back in to make decisions.

## Layout

| Path | Contents |
| --- | --- |
| `docs/spec/1-outcome.md` | The framework's own Outcome: what it achieves and how success is checked |
| `docs/goals.md` | The goals every change serves |
| `hooks/prompts/goals.md` | The goals and the decide-or-ask rule, as the agent's prompt the hooks load |
| `hooks/prompts/stop-check.md` | The prompt the stop check asks the model |
| `hooks/stop.py` | The stop check: asks the host's CLI whether the agent's last message asks to approve something already decided |
| `hooks/selfcheck.py` | The self-check hook: before an agent's `git commit`, denies it if a changed level document in `docs/spec/` has no full self-check table naming every requirement, scenario and measure |
| `tests/` | Tests for the hook scripts: `python3 -m unittest discover -s tests` |
| `docs/spec/candidates.md` | Content agreed before the Outcome, to be checked at the level that owns it |
| `docs/decisions.md` | The append-only decision log |
| `docs/open-questions.md` | Questions set aside for the level that owns them |
| `skills/references/outcome.md` | What an Outcome contains and the criteria it must meet, shared by the Outcome skills |
| `skills/references/decisions.md` | Which decisions need the user and which the work makes, used at every level |
| `skills/write-outcome/` | Skill for writing a feature's Outcome |
| `skills/review-outcome/` | Skill for reviewing an Outcome at its gate |
| `CLAUDE.md` | Rules for agents working in this repo |
| `.claude/settings.json` | Claude Code hooks: load the goals prompt, run the self-check before commits and run the stop check |
| `.codex/config.toml` | The same hooks for Codex |

`docs/` describes the framework. `skills/` holds what the framework uses on each feature.

The hooks run under both Claude Code and Codex. Codex runs a repo's hooks only after you review and trust them with `/hooks`.
