# 0017. Dogfood first, then apply the framework to codeguard step 32

Status: accepted, 2026-10-28

## Context

[Decision 0014](0014-autonomy-policy-and-mvp-first.md) said the framework would be tried on a real feature before levels 2–5 were refined. That changed the order set by [decision 0010](0010-dogfood-the-framework.md) without the user agreeing to it.

## Decision

- Building the framework with itself is the main path. Its levels are written and gated in order with its own skills.
- When the framework is done, it is applied to codeguard plan step 32, change classification, as its first test on a product feature.

## Consequences

- This replaces the "tried on one real feature before levels 2–5" point of decision 0014.
- MVP first means the smallest framework that carries its own build, not a pause after level 1.
