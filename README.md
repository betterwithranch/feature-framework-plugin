# Feature framework

Takes a feature you've decided to build from intent to working code, one level at a time, so the build doesn't pull you back in to make decisions.

## Layout

| Path | Contents |
| --- | --- |
| `docs/spec/1-outcome.md` | The framework's own Outcome: what it achieves and how success is checked |
| `docs/spec/2-behaviour.md` | The framework's own Behaviour: its rules, edge cases, examples and non-goals |
| `docs/spec/3-design.md` | The framework's own Design: how it is built, each choice decided |
| `docs/goals.md` | The goals every change serves, and when to decide versus ask |
| `docs/spec/candidates.md` | Content agreed before the Outcome, to be checked at the level that owns it |
| `docs/decisions/` | The current decisions, one per record |
| `docs/open-questions.md` | Questions set aside for the level that owns them |
| `skills/references/outcome.md` | What an Outcome contains and the criteria it must meet, shared by the Outcome skills |
| `skills/references/decisions.md` | Which decisions need the user and which the work makes, used at every level |
| `skills/references/behaviour.md` | What a Behaviour document contains and the criteria it must meet, shared by the Behaviour skills |
| `skills/references/design.md` | What a Design document contains and the criteria it must meet, shared by the Design skills |
| `skills/write-outcome/` | Skill for writing a feature's Outcome |
| `skills/review-outcome/` | Skill for reviewing an Outcome at its gate |
| `skills/write-behaviour/` | Skill for writing a feature's Behaviour |
| `skills/review-behaviour/` | Skill for reviewing a Behaviour document at its gate |
| `skills/write-design/` | Skill for writing a feature's Design |
| `skills/review-design/` | Skill for reviewing a Design document at its gate |
| `CLAUDE.md` | Rules for agents working in this repo |
| `.claude/settings.json` | Hooks that load the goals and block unnecessary approval requests |

`docs/` describes the framework. `skills/` holds what the framework uses on each feature.
