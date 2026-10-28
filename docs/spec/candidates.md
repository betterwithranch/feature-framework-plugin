# Candidate content for later levels

Agreed before the framework's Outcome existed. Per [decision 0010](../decisions/0010-dogfood-the-framework.md), each item is checked against the approved [Outcome](1-outcome.md) at the level that owns it before it is treated as settled.

## Levels

| Level | Produces | Proof |
| --- | --- | --- |
| 1. Outcome | Who the feature is for, what it achieves, end-to-end scenarios | Automated end-to-end tests through the real surface |
| 2. Behaviour | Every rule and edge case, with examples, plus non-goals | Tests at the narrowest surface where each rule is observable |
| 3. Design | Decisions only this feature raises, each decided or a non-goal; general rules cited | No open decision; nothing restating a general rule |
| 4. Slices | Ordered vertical slices, each naming the scenario it extends and the cases it makes pass | Every scenario, case and decision is covered; every slice meets the slice guideline |
| 5. Build | The code for one slice | Assigned cases pass, earlier slices still pass, project checks are clean |

Levels 1–4 are planning; level 5 is execution and builds one slice. Independent slices may be built concurrently.

## Gates

- Each planning level ends at a gate. An independent reviewer checks the level's artifact on its own. The user's approval closes the gate.
- A finding must point to the artifact and change what gets built. Hypotheticals are dropped: perfection is the enemy of done.
- Build never changes the tests it builds toward. A plan gap or a conflict goes back to the level that owns it.

## Outcome and Behaviour

- Outcome is a few scenarios through the real user surface (browser, API or CLI).
- Behaviour covers every rule and edge case, each tested at the narrowest point where it can be observed.
- Each slice passes an Outcome scenario end to end, possibly narrowed, by extending that scenario's test.
