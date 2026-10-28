# 0007. Deliver features as narrow vertical slices

Status: accepted, 2026-10-27

## Context

Building by layer hides integration problems and lets scope grow.

## Decision

A feature ships as narrow vertical slices, each working end to end and releasable on its own, behind a feature flag if needed. Completing a layer never counts as success.

## Consequences

Each slice must pass an end-to-end check, possibly narrowed.
