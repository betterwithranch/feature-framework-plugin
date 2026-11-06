---
name: write-outcome
description: Write the Outcome of a feature, the first planning level - who it is for, what it achieves, end-to-end scenarios with automated verifications, and how success is measured on real use. Use when starting a feature, before any behaviour, design or code, and to fix findings from an Outcome review.
---

# Write an Outcome

Read [the Outcome definition](../references/outcome.md) and [the decision classification](../references/decisions.md), which sets who makes each decision. Write a document that has its contents and meets its criteria.

## Rules

- Write for the reader the definition names, in the form its contents set.
- State what the user gets. Leave exactly what counts, and how it works, to later levels.
- Be simple and to the point. Use short sentences and say only what the reader needs to know what result is asked for.
- An absolute term, such as every, never, only, always, all, none, any or anything, means no exceptions. If a requirement has exceptions, write it in non-absolute terms.
- Use one term per concept, and reuse the same phrase for the same idea. Define a term only when a reader couldn't tell what result it means.
- State what each verification confirms, not how it is built. Each verifies the behaviour the user observes and passes or fails on its own.
- Fix a problem by removing the wording that caused it, not by adding a new qualifier or distinction.

## Self-check before review

Run every step on the whole document and write the result as a table, one row per item checked. Name requirements, scenarios and measures by their IDs.

1. Vocabulary. List every concept and confirm each has one term.
2. Complete (criterion 1). Confirm each element of the definition's contents is present.
3. Nothing extra (criterion 2). Go through each statement and confirm it is none of what an Outcome does not contain.
4. Clear (criterion 3). For each statement, name the result the user is meant to get.
5. Traceable (criterion 4). For each requirement, list every way a run could break each of its parts, and name the scenario or measure whose verification fails for each. Map each scenario and measure to the requirement it verifies.
6. Sound verifications (criterion 5). Go through each scenario and measure one at a time, against each of the five items. For each check in it, quote the requirement words that rule out what it fails, and confirm that a run doing the failed behaviour would break them. Consider every way a run could get the user the result, and every way a run could pass without it, not only the one the scenario has in mind. Words on the same subject that don't forbid it are not enough; a requirement allows whatever its words don't rule out.
7. Consistent (criterion 6). Run `scripts/absolutes.py <document>`; it lists every absolute term with its ID and sentence. Write one row per listed term, and check each against every requirement for an exception. Then check each requirement, scenario, measure and definition against the others on the same subject for a contradiction.
8. Rewrites. After splitting or moving any text, re-check every requirement it touched against criterion 6 and against the scenarios that verify it.
9. Fix what fails.

## After a fix

Rerun the whole self-check. A fix that moves a problem somewhere else is not a fix.
