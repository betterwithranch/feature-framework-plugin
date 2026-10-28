# 0020. One classification of who makes each decision

Status: accepted, 2026-10-28

## Context

No document said which decisions need the user and which the work makes. Rules settled it case by case, and drifted both ways: the framework's Behaviour sent every build choice to the user, while an agent in another session wrote its own rules into a plan and built on them. "Later wins" (decision 0018) let a rule the work wrote override one the user agreed.

## Decision

- `skills/references/decisions.md` is the single source for who makes each decision, at every level and for decisions written anywhere, including plans, notes and memory.
- The user decides what users get, anything that creates, changes or overrides an agreement or codified rule, tools and external dependencies, hard-to-reverse or outward-facing choices, and trade-offs between goals.
- The work decides what follows from something agreed and reversible build choices within it, and records them. Its decisions never become codified rules. When unsure, the user decides.
- This amends [decision 0018](0018-later-agreement-wins.md): the later agreement wins only when both were made or agreed by the user.

## Consequences

- The Outcome and Behaviour are revised to follow it, and their gates run again.
- This repo's own goals point at the same file.
