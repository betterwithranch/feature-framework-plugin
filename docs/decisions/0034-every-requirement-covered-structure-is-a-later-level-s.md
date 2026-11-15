# 0034. Every requirement covered; structure is a later level's

Status: accepted, 2026-11-04

## Context

The user said "verification just needs to make sure all the requirements are covered. how that is structured is an implementation detail".

## Decision

Every requirement is covered by a verification that fails if the requirement isn't met. How verifications are split, grouped or structured, including one per listed item or one per case, is an implementation detail for a later level and not a review finding. This keeps [decision 0032](0032-one-verification-for-a-requirement-that-holds-across-cases.md) and extends it from cases to listed items.
