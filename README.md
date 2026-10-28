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
| `docs/spec/candidates.md` | Content agreed before the Outcome, to be checked at the level that owns it |
| `docs/decisions/` | Decision records: one agreed decision each, with context and consequences |
| `docs/open-questions.md` | Questions set aside for the level that owns them |
| `levels/1-outcome/writing-guidance.md` | How to write a level 1 artifact |
| `levels/1-outcome/review-prompt.md` | The prompt for the level 1 review gate |

`docs/` describes the framework. `levels/` holds what the framework uses on each feature.
