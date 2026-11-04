---
name: write-outcome
description: Write the Outcome of a feature, the first planning level - who it is for, what it achieves, end-to-end scenarios with automated verifications, and how success is measured on real use. Use when starting a feature, before any behaviour, design or code, and to fix findings from an Outcome review.
---

# Write an Outcome

Read [the Outcome definition](../references/outcome.md) and [the decision classification](../references/decisions.md), which sets who makes each decision. Write a document that has its contents and meets its criteria.

## Rules

- State what the user gets. Leave exactly what counts, and how it works, to later levels.
- Be simple and to the point. Use short sentences and say only what the reader needs to know what result is asked for.
- An absolute term, such as every, never, only, always, all, none, any or anything, means no exceptions. If a requirement has exceptions, write it in non-absolute terms.
- Use one term per concept, and reuse the same phrase for the same idea. Define a term only when a reader couldn't tell what result it means.
- State what each verification confirms, not how it is built. Each verifies the behaviour the user observes and passes or fails on its own.
- Fix a problem by removing the wording that caused it, not by adding a new qualifier or distinction.

## Self-check before review

1. List the vocabulary and confirm each concept has one term.
2. List the requirements, scenarios and measures, and map each requirement to a scenario whose verification fails if the requirement isn't met.
3. Check the document against each criterion in the definition. For criterion 5, go through each scenario and measure one at a time, against each item.
4. Fix what fails.

## After a fix

Rerun the self-check on the changed text and on every requirement, scenario and measure about the same subject, whether or not they refer to each other. A fix that moves a problem somewhere else is not a fix.
