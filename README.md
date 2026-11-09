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
| `docs/goals.md` | The goals every change serves |
| `hooks/prompts/goals.md` | The goals and the decide-or-ask rule, as the agent's prompt the hooks load |
| `hooks/prompts/stop-check.md` | The prompt the stop check asks the model |
| `hooks/stop.py` | The stop check: asks the host's CLI whether the agent's last message asks to approve something already decided |
| `hooks/selfcheck.py` | Before an agent's `git commit`, denies it if a changed level document in `docs/spec/` fails its structure checks |
| `skills/write-outcome/scripts/structure.py` | Checks a level document's structure: sections, IDs, citations and banned terms |
| `skills/write-outcome/scripts/absolutes.py` | Lists every absolute term in a level document, with its ID and sentence, for the Clarity review |
| `tests/` | Tests for the hook scripts: `python3 -m unittest discover -s tests` |
| `docs/spec/candidates.md` | Content agreed before the Outcome, to be checked at the level that owns it |
| `docs/decisions.md` | The append-only decision log |
| `docs/open-questions.md` | Questions set aside for the level that owns them |
| `skills/references/outcome.md` | What an Outcome contains and how it is reviewed, shared by the Outcome skills |
| `skills/references/glossary-review.md` | The glossary review's yes/no rules, judged against each entry of the project glossary |
| `skills/references/outcome-reviews/` | The four Outcome reviews' yes/no rules: scope, clarity, verification, provenance |
| `skills/references/decisions.md` | Which decisions need the user and which the work makes, used at every level |
| `skills/write-outcome/` | Skill for writing a feature's Outcome |
| `skills/review-outcome/` | Skill for reviewing an Outcome at its gate |
| `CLAUDE.md` | Rules for agents working in this repo |
| `.claude/settings.json` | Claude Code hooks: load the goals prompt, run the structure checks before commits and run the stop check |
| `.codex/config.toml` | The same hooks for Codex |

`docs/` describes the framework. `skills/` holds what the framework uses on each feature.

The hooks run in this repo under both Claude Code and Codex. Codex runs a repo's hooks only after you review and trust them with `/hooks`.
