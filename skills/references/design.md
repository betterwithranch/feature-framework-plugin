# Design

A Design document records every choice of how the feature is built that the feature raises, and cites the codified rules and decision records that already settle the rest. It is the third planning level and builds the passed Behaviour.

## Contents

A Design document contains:

- Decisions. Each states one choice between ways of building the feature, what was chosen, whether you or the work made it, and the rules and edge cases it builds. A decision the work makes that follows from something agreed, a codified rule or a goal cites which. A decision of yours cites the decision record that holds your answer.
- Cited rules. Each names a codified rule or decision record that settles a point the feature needs, and the rules and edge cases it covers. It is cited, not restated.
- Non-goals. Each states a way of building the feature a reader might expect that it deliberately doesn't use.

A Design document does not contain what the feature does, restated codified rules or decision records, a slicing plan, code, or open questions.

A point about what the feature does belongs to Behaviour. A point about the order in which the feature is built belongs to Slices. Who makes each decision is set by [the decision classification](decisions.md).

## Criteria

A sound Design document meets all six.

1. Complete. Every Behaviour rule and edge case is built by at least one decision or cited rule. No decision is left open.
2. Nothing extra. Nothing is present that Design isn't responsible for, and no decision goes beyond what the Behaviour needs.
3. Clear. For every decision, a reader knows the one thing chosen and can build it without choosing again.
4. Traceable. Every decision and cited rule names the rules or edge cases it builds. Every decision of yours cites its decision record.
5. Sound. Each decision, built as stated, makes the rules and edge cases it names true. Each decision is made by whoever the decision classification says makes it.
6. Consistent. No decisions, cited rules or non-goals contradict each other, the Behaviour, the Outcome, or a cited codified rule or decision record.
