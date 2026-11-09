# 0018. The framework outline

Status: accepted, 2026-11-09

## Context

Level 1 was being scoped without an outline of the whole framework, so its requirements, scenarios and measures grew to cover later levels. The user asked for an outline of the whole solution that describes level 1, so that work can be checked against it.

## Decision

- The outline in the [README](../../README.md) is the agreed shape of the framework: what it is, its levels, how every planning level runs, and what level 1 contains and leaves to later levels.
- The levels table's proof for each level, previously a candidate, is agreed as written there.
- The framework's own level 1 delivers its own Outcome, what a level 1 document contains with the instructions to write and review one, the classification of who decides, and one branch and pull request for the level.
- The order stands: build the framework with its own levels, then apply it to codeguard plan step 32.

## Consequences

- Level 1 work is checked against the outline. Anything outside it is set aside for the level that owns it.
- `docs/spec/candidates.md` keeps only the details the outline doesn't settle.
