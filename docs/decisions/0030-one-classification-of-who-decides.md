# 0030. One classification of who decides

Status: accepted, 2026-10-28, amended 2026-11-04

## Context

No document said which decisions need the user, so rules settled it case by case and drifted both ways.

## Decision

`skills/references/decisions.md` is the single source for who makes each decision, at every level and for decisions written anywhere, including plans, notes and memory. The user decides what users get, anything that creates, changes or overrides an agreement or codified rule, tools and external dependencies, hard-to-reverse or outward-facing choices, and trade-offs between goals. The work decides what follows from something agreed and reversible build choices within it, and records them: in a planning level's document, or, in Build, in the code and tests. Its decisions never become codified rules. When unsure, the user decides. Where a decision is written into a level document, code or notes, a decision that replaces it removes it there; this framework's own decision records keep both.
