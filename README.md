# Feature framework

Takes a feature you've decided to build from intent to working code, one level at a time, so the build doesn't pull you back in to make decisions.

## Status

The framework is being built with itself ([decision 0010](docs/decisions/0010-dogfood-the-framework.md)).

- Level 1 (Outcome) of the framework has passed its review and awaits approval.
- Levels 2–5 have not started.

## Layout

| Path | Contents |
| --- | --- |
| `docs/spec/1-outcome.md` | The framework's own Outcome: what it achieves and how success is checked |
| `docs/goals.md` | The goals every change serves, and when to decide versus ask |
| `docs/spec/candidates.md` | Content agreed before the Outcome, to be checked at the level that owns it |
| `docs/decisions/` | Decision records: one agreed decision each, with context and consequences |
| `docs/open-questions.md` | Questions set aside for the level that owns them |
| `skills/write-outcome/` | Skill for writing a feature's Outcome |
| `skills/review-outcome/` | Skill for reviewing an Outcome at its gate |
| `CLAUDE.md` | Rules for agents working in this repo |
| `.claude/settings.json` | Hooks that load the goals and block unnecessary approval requests |

`docs/` describes the framework. `skills/` holds what the framework uses on each feature.
