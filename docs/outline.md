# Framework outline

Draft for approval. Every line comes from a recorded decision, cited in brackets. Lines marked *(candidate)* come from `docs/spec/candidates.md`, which was never approved; approving this outline approves them. Nothing else is added.

## What the framework is

- It takes a feature the user has decided to build from intent to working code, one level at a time, so the build doesn't pull the user back in. [D3, D5, goals 1]
- It is reusable across sessions and projects, not a set of agreements for one session. Its form, likely a plugin for Claude Code and Codex, is decided at the Design level. [D2]
- It covers feature development only. Exploratory work, performance optimisation, data migrations, infrastructure and tooling changes made for other reasons are non-goals. [D4]
- It ends at working code verified locally or in CI. Deployment and opening PRs are non-goals for now. [D5]
- Every verification is automated. A check that needs a person doesn't count. [D8]
- It is the smallest version that carries its own build. A level is not refined beyond what the next level needs. [D39]

## The levels

| Level | Produces | Proof |
| --- | --- | --- |
| 1. Outcome | Who the feature is for, its requirements, end-to-end scenarios, measures | Automated end-to-end tests through the real surface *(candidate)* |
| 2. Behaviour | Every rule and edge case, with examples, plus non-goals *(candidate)* | Tests at the narrowest surface where each rule is observable *(candidate)* |
| 3. Design | Decisions only this feature raises, each decided or a non-goal [D6] | No open decision *(candidate)* |
| 4. Slices | Ordered vertical slices, each working end to end [D7] | Every scenario, case and decision is covered *(candidate)* |
| 5. Build | The code for one slice | Its cases pass and earlier slices still pass *(candidate)* |

- Levels 1 to 4 each produce one document. Build produces code. [D26]
- Facts found in the project: none at Outcome; about what users get today at Behaviour; about the code at Design; how the project is built and tested at Slices. [D30]

## How every planning level runs

1. The work interviews the user, one question at a time. [D27]
2. It plays back what it understood, and the user confirms. [D27]
3. It writes the level's document. [D27]
4. The level's review runs, in rounds, until it passes. [D35, D54]
5. The user approves. Only then does the next level start. [D26]

Throughout:

- Nothing is guessed: a fact is looked up, the user's decisions and readings are asked. [D19, D34]
- One classification sets who makes each decision. [D42]
- A question for a later level is recorded for that level and not answered. [D9]
- Once Slices is approved, Build runs without the user, except for something that is the user's to settle. [D26, goals 1]

## Level 1 (Outcome)

Contains:

- who the feature is for;
- its requirements, as results the user can observe;
- end-to-end scenarios, checked automatically;
- measures of success on real use;
- a reference to the project's glossary. [D56, D66]

Leaves to later levels: non-goals, rules and edge cases, design decisions, implementation, slicing, where anything lives, and how tests are built. [D9, D33, D70]

## What the framework's own level 1 delivers

- The framework's own Outcome document. [D37]
- What a level 1 document contains, and the instructions to write and review one. [D61–D65]
- The classification of who decides. [D42]
- One branch and pull request for the level. [D28]

## Order

1. Build the framework with its own levels, starting with its own Outcome. [D37]
2. When the framework is done, apply it to codeguard plan step 32, change classification, as its first product feature. [D37]
