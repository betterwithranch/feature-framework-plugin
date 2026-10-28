# 0003. Refine committed features along one axis: altitude

Status: accepted, 2026-10-27

## Context

Corrections in past sessions were altitude errors: detail was built before the level above it was settled. Commitment was not the problem; the features were already decided.

## Decision

The framework refines a feature the user has already committed to, from intent down to build. Commitment is not a level.

## Consequences

Hypothesis and success criteria sit at the top level. Incremental slices sit near the bottom. Invariants and non-goals are constraints each level adds to.
