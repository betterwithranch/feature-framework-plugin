# 0009. Block questions that belong to a lower level

Status: accepted, 2026-10-27

## Context

Answering lower-level questions early is how detail gets built before the level above is settled.

## Decision

A question that belongs to a lower level, raised by the user or the agent, is recorded for the level that owns it and not answered. Open ones are listed in `docs/open-questions.md`.

## Consequences

Each level needs a clear statement of what is and isn't its responsibility.
