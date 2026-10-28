# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Contents

An Outcome contains:

- Who the feature is for.
- What it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated check and a pass bar. No check needs a person.
- How success is measured on real use, each measure with a target.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

An Outcome leaves room for interpretation; later levels narrow it. A point that needs a definition, rule, threshold or procedure to resolve (what exactly counts as X, when exactly Y happens, how much work stops) belongs to a later level.

## Criteria

A sound Outcome meets all six.

1. Complete. Every required element is present.
2. Nothing extra. Nothing is present that the Outcome isn't responsible for.
3. Clear. For every statement, a reader knows what result the user is meant to get.
4. Traceable. Every part of every claim has a scenario whose check fails if that part is broken. Every scenario and measure checks a claim. An allowance, something a claim permits but does not require, needs no scenario of its own.
5. Sound checks. Judged against the claims it traces to, no check or measure:
   - passes when the user doesn't get the result;
   - fails or counts against behaviour a claim requires or allows. Every allowance or exception in a claim is carried into each scenario and measure it touches, unless the scenario's starting state rules it out;
   - can be satisfied by the work being judged;
   - compares against an expected result that the scenario doesn't set before the run;
   - leaves its starting state to the work being judged instead of setting it.

   A scenario need not re-check a claim that another scenario covers.
6. Consistent. No claims, scenarios, measures or definitions contradict each other.
