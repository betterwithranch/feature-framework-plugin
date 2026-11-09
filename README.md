# Feature framework

Takes a feature you've decided to build from intent to working code, one level at a time, so the build doesn't pull you back in to make decisions.

## What it is

- It takes a feature the user has decided to build from intent to working code, one level at a time, so the build doesn't pull the user back in.
- It is reusable across sessions and projects, not a set of agreements for one session. Its form, likely a plugin for Claude Code and Codex, is decided at the Design level.
- It covers feature development only. Exploratory work, performance optimisation, data migrations, infrastructure and tooling changes made for other reasons are non-goals.
- It ends at working code verified locally or in CI. Deployment and opening PRs are non-goals for now.
- Every verification is automated. A check that needs a person doesn't count.
- It is the smallest version that carries its own build. A level is not refined beyond what the next level needs.

## Levels

| Level | Produces | Proof |
| --- | --- | --- |
| 1. Outcome | Who the feature is for, its requirements, end-to-end scenarios, measures | Automated end-to-end tests through the real surface |
| 2. Behaviour | Every rule and edge case, with examples, plus non-goals | Tests at the narrowest surface where each rule is observable |
| 3. Design | Decisions only this feature raises, each decided or a non-goal | No open decision |
| 4. Slices | Ordered vertical slices, each working end to end | Every scenario, case and decision is covered |
| 5. Build | The code for one slice | Its cases pass and earlier slices still pass |

- Levels 1 to 4 each produce one document. Build produces code.
- Facts found in the project: none at Outcome; about what users get today at Behaviour; about the code at Design; how the project is built and tested at Slices.

## How every planning level runs

1. The work interviews the user, one question at a time.
2. It plays back what it understood, and the user confirms.
3. It writes the level's document.
4. The level's review runs, in rounds, until it passes.
5. The user approves. Only then does the next level start.

Throughout:

- Nothing is guessed: a fact is looked up, the user's decisions and readings are asked.
- One classification sets who makes each decision.
- A question for a later level is recorded for that level and not answered.
- Once Slices is approved, Build runs without the user, except for something that is the user's to settle.

## Level 1 (Outcome)

Contains who the feature is for; its requirements, as results the user can observe; end-to-end scenarios, checked automatically; measures of success on real use; and a reference to the project's glossary.

Leaves to later levels: non-goals, rules and edge cases, design decisions, implementation, slicing, where anything lives, and how tests are built.

## Layout

| Path | Contents |
| --- | --- |
| `docs/spec/1-outcome.md` | The framework's own Outcome: what it achieves and how success is checked |
| `docs/goals.md` | The goals every change serves, and when to decide versus ask |
| `docs/spec/candidates.md` | Content agreed before the Outcome, to be checked at the level that owns it |
| `docs/decisions/` | Decision records: one agreed decision each, with context and consequences |
| `docs/open-questions.md` | Questions set aside for the level that owns them |
| `skills/references/outcome.md` | What an Outcome contains and the criteria it must meet, shared by the Outcome skills |
| `skills/write-outcome/` | Skill for writing a feature's Outcome |
| `skills/review-outcome/` | Skill for reviewing an Outcome at its gate |
| `CLAUDE.md` | Rules for agents working in this repo |
| `hooks/` | Hook scripts that load the goals, check a turn's end, and check a level document before an agent commits it |
| `hooks/prompts/` | The prompts those hooks load, written for the agent |
| `.claude/settings.json` | Points Claude Code at the hooks |
| `.codex/config.toml` | Points Codex at the hooks |
| `tests/` | Tests for the hook scripts |

`docs/` describes the framework. `skills/` holds what the framework uses on each feature.
