# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Contents

An Outcome contains:

- Who the feature is for.
- What it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated check and a pass bar. No check needs a person. A pass bar that applies to every scenario, such as how many runs must pass, is stated once.
- How success is measured on real use, each measure with a target.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

A scenario states its starting state, what happens and what passes, as results you can observe. How the scenario is scripted, and how a check tells one case from another, is how tests are built. Naming a check's kind, its pass bar, and what comes with the scenario is not.

An Outcome leaves room for interpretation; later levels narrow it. A point that needs a definition, rule, threshold or procedure to resolve (what exactly counts as X, when exactly Y happens, how much work stops, how a scenario is scripted or a check is built) belongs to a later level.

## Criteria

A sound Outcome meets all six.

1. Complete. Every required element is present.
2. Nothing extra. Nothing is present that the Outcome isn't responsible for.
3. Clear. For every statement, a reader knows what result the user is meant to get.
4. Traceable. Every part of every claim has a scenario whose check fails if that part is broken. Every scenario and measure checks a claim. An allowance, something a claim permits but does not require, needs no scenario of its own.
5. Sound checks. Taking each check as built faithfully at a later level, and judged against the claims it traces to, no check or measure:
   - passes when the user doesn't get the result;
   - relies on the work to produce anything it needs before its event (a failing draft, a defect, a decision, an earlier feature), or reads the work's own verdict as its result;
   - fails or counts against behaviour a claim requires or allows. Each allowance or exception a scenario touches is either ruled out by its starting state or carried into its whole check, and each one a measure touches is carried into it;
   - compares against an expected result that the scenario doesn't set before the run.

   A scenario need not re-check a claim that another scenario covers.
6. Consistent. No claims, scenarios, measures or definitions contradict each other.
