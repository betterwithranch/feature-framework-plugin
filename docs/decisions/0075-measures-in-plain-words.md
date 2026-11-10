# 0075. Measures in plain words

Status: accepted, 2026-11-10

## Context

The Outcome's measures said "target zero", and the planning-misses measure said "It's not a pass bar" with no target. The user withdrew the question about that measure's target (FF-76): "is this following the writing guidelines we discussed earlier? it seems like this should be simpler and this "target zero" crap is back now too. It seems like you are severely overthinking this. we should be able to generalize these decisions without you asking me about them repeatedly." The user also said that measure shouldn't be treated differently from the others.

## Decision

- Each measure says, in plain words, what is counted on each real feature, and that the count should be none.
- The planning-misses measure has the same target as the others. It follows from R2, R31 and R32: decisions are made before code starts. It cites R32.

## Consequences

- Follows [the writing rules](../../skills/references/writing.md) ([decision 0070](0070-writing-rules.md)).
- Replaces the approved measure's "counted for each feature as planning misses. It's not a pass bar."
