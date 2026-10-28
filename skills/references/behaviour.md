# Behaviour

A Behaviour document states every rule the feature follows and every edge case, each with examples, and what the feature does not do. It is the second planning level and narrows the approved Outcome.

## Contents

A Behaviour document contains:

- Rules. Each states one thing the feature does, as a result someone can observe, and names the Outcome claim it narrows.
- Edge cases. Each states what happens at a boundary of a rule: an unusual input, state or order of events.
- Examples. Each rule and edge case has at least one, giving a starting state, what happens and the expected result.
- The surface. Each rule and edge case names the narrowest place its result can be observed, such as a file, a command's output or a conversation.
- Non-goals. Each states something a reader might expect the feature to do that it deliberately doesn't.

A Behaviour document does not contain design decisions, implementation, a slicing plan, how tests are built, or restatements of the Outcome.

An example states a case, not a test. How it becomes a test is how tests are built.

A point that needs a choice between ways of building the feature belongs to Design. A point about what the feature does belongs here. Who makes each decision is set by [the decision classification](decisions.md).

## Criteria

A sound Behaviour document meets all six.

1. Complete. Every Outcome claim is narrowed by at least one rule. Every rule and edge case states one thing and has an example and a surface.
2. Nothing extra. Nothing is present that Behaviour isn't responsible for.
3. Clear. For every rule, edge case and example, a reader knows the one result expected.
4. Traceable. Every rule names an Outcome claim it narrows, and every edge case names its rule.
5. Sound examples. Each example's expected result follows from its rule or edge case, and its surface can show that result.
6. Consistent. No rules, edge cases, examples or non-goals contradict each other or the Outcome. A rule keeps every limit and exception of the claim it narrows.
