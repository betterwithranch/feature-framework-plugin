# 0010. Build the framework with the framework

Status: accepted, 2026-10-27

## Context

Rules that the builder doesn't follow while building them get violated.

## Decision

The framework is built with its own levels and gates, starting with its own Outcome.

## Consequences

Decisions recorded before the framework's Outcome was approved, such as the candidate levels, are checked against it before they are treated as settled.
