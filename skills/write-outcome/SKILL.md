---
name: write-outcome
description: Write the Outcome of a feature, the first planning level - who it is for, what it achieves, end-to-end scenarios with automated checks, and how success is measured on real use. Use when starting a feature, before any behaviour, design or code.
---

# Write an Outcome

An Outcome states what the user gets and how success is judged. Nothing else.

## Contents

An Outcome contains:

- Who the feature is for.
- What it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated check and a pass bar. No check needs a person.
- How success is measured on real use.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

## Rules

- State what the user gets. Leave exactly what counts, and how it works, to later levels. Different readings are expected here; later levels narrow them.
- Be simple and to the point. Use short sentences and say only what the reader needs to know what result is asked for.
- Use one term per concept, and reuse the same phrase for the same idea. Define a term only when a reader couldn't tell what result it means.
- Give every part of every claim a scenario whose check fails if that part is broken. Every scenario and measure traces to a claim.
- State what each check confirms, not how it is built.
- Make sure no check or measure can be passed by the work it judges.
- Have each scenario set its own starting state. Never rely on the work being judged to reach it.
- Carry every allowance or exception in a claim into each scenario and measure it touches. No check or measure counts against behaviour a claim requires or allows.
- Keep definitions consistent with scenarios.
- Fix a problem by removing the wording that caused it, not by adding a new qualifier or distinction.

## Self-check before review

1. List the vocabulary and confirm each concept has one term.
2. List the claims, scenarios and measures.
3. Map every part of each claim to a scenario that fails if that part is broken.
4. Confirm each scenario and measure traces to a claim.
5. Confirm each scenario states its starting state.
6. Confirm no check or measure can be passed by the work it judges.
7. Confirm every exception in a claim appears in each scenario and measure it touches.
