# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Contents

An Outcome contains:

- Who the feature is for.
- Its requirements: what it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated verification and a pass bar. No verification needs a person. A pass bar that applies to every scenario, such as how many runs must pass, is stated once.
- How success is measured on real use, each measure with a target.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

A scenario states its starting state, what happens and what passes, as results you can observe. How the scenario is scripted, and how a verification tells one case from another, is how tests are built. Naming a verification's kind, its pass bar, and what comes with the scenario is not.

Verifications are automated tests held to normal testing standards. Each tests the behaviour the user observes, not how it is implemented, and passes or fails on its own, independent of every other verification.

An Outcome leaves room for interpretation; later levels narrow it. A point that needs a definition, rule, threshold or procedure to resolve (what exactly counts as X, when exactly Y happens, how much work stops, how a scenario is scripted or a verification is built) belongs to a later level.

## Criteria

A sound Outcome meets all six.

1. Complete. Every required element is present.
2. Nothing extra. Nothing is present that the Outcome isn't responsible for.
3. Clear. For every statement, a reader knows what result the user is meant to get.
4. Traceable. Every requirement is covered by a verification that fails if the requirement isn't met. How verifications are split, grouped or structured, such as one per listed item or one per level, person or feature, is for a later level; asking for a different structure is not a finding. Every scenario and measure verifies a requirement. An allowance, something a requirement permits but does not require, needs no scenario of its own. A requirement allows whatever its words don't rule out.
5. Sound verifications. Each verification is judged by its own words against the requirement it verifies, taken as built faithfully at a later level. No verification or measure:
   - passes when the user doesn't get the result;
   - relies on the work to have produced anything it needs before its event, such as a failing draft, a defect, a decision or an earlier feature. A starting state that sets these up itself is not a finding;
   - tests how the result is implemented instead of the behaviour the user observes, for example by reading the system's own log or report that it succeeded;
   - fails or counts against behaviour the requirement it verifies requires or allows. A behaviour is ruled out only by requirement words that a run doing it would break; words on the same subject that don't forbid it don't rule it out. Only that requirement's allowances and exceptions count, and each one the starting state could bring about is either ruled out by the starting state or carried into the verification;
   - compares against an expected result that the scenario doesn't set before the run.

   A scenario need not re-verify a requirement that another scenario covers.
6. Consistent. No requirements, scenarios, measures or definitions contradict each other. An absolute term, such as every, never, only, always, all, none, any or anything, means no exceptions, so an absolute requirement that another requirement makes an exception to is a contradiction.
