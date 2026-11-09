# 0015. The user approves only open decisions

Status: accepted, 2026-10-28

## Context

Requiring the user's approval at every level made interaction mandatory and was a main source of handholding ([decision 0014](0014-autonomy-policy-and-mvp-first.md)).

## Decision

A level moves on when its gate passes. The user is asked only to settle decisions no one has made, or conflicts between agreed things. The framework's level 1 Outcome is approved.

## Consequences

- Levels run back to back without the user unless a gate raises an open decision.
- The user's role is to settle open decisions, not to approve finished levels.
