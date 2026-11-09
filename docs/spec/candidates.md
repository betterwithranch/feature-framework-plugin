# Candidate content for later levels

Agreed before the framework's Outcome existed. Per [decision 0010](../decisions/0010-dogfood-the-framework.md), each item is checked against the approved [Outcome](1-outcome.md) at the level that owns it before it is treated as settled.

## Levels

The levels, what each produces and its proof are agreed in the [README](../../README.md). These details are still candidates:

- Design: general rules are cited; nothing restates a general rule.
- Slices: each slice names the scenario it extends and the cases it makes pass; every slice meets the slice guideline.
- Build: project checks are clean.
- Independent slices may be built concurrently.

## Gates

- Each planning level ends at a gate. An independent reviewer checks the level's artifact on its own. The user's approval closes the gate.
- A finding must point to the artifact and change what gets built. Hypotheticals are dropped: perfection is the enemy of done.
- Build never changes the tests it builds toward. A plan gap or a conflict goes back to the level that owns it.

## Outcome and Behaviour

- Outcome is a few scenarios through the real user surface (browser, API or CLI).
- Behaviour covers every rule and edge case, each tested at the narrowest point where it can be observed.
- Each slice passes an Outcome scenario end to end, possibly narrowed, by extending that scenario's test.
