# 0001. Make the level of work explicit

Status: accepted, 2026-10-27

## Context

When something is ambiguous, the agent resolves it by producing something concrete (a plan, a template, code), because specifics look like progress. Nothing establishes which level the work is at or what finishing that level means, so the agent reads partial agreement as permission to go deeper. The gaps then surface only as the user's corrections, after the detail exists.

## Decision

Make the level explicit and treat it as a constraint:

- The current level and what finishing it means are always stated.
- The agent works only at the current level and raises alternatives only at that level.
- Going down a level needs the user's explicit agreement. Partial agreement or momentum doesn't count.
- Anything that belongs to a lower level is set aside, not developed.

## Consequences

Work moves top-down through a defined set of levels. Every later decision is expressed in terms of those levels.
