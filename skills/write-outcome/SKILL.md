---
name: write-outcome
description: Writes the Outcome of a feature, the first planning level - who it is for, what it achieves, end-to-end scenarios with automated verifications, and how success is measured on real use. Use when starting a feature, before any behaviour, design or code, and to fix findings from an Outcome review.
---

# Write an Outcome

Read [the Outcome definition](../references/outcome.md) and [the decision classification](../references/decisions.md), which sets who makes each decision. Write a document that has its contents and passes its structure checks and reviews.

## Rules

- Write for the reader the definition names, in the form its contents set.
- State what the user gets. Leave exactly what counts, and how it works, to later levels.
- Be simple and to the point. Use short sentences and say only what the reader needs to know what result is asked for.
- An absolute term, such as every, never, only, always, all, none, any or anything, means no exceptions. If a requirement has exceptions, write it in non-absolute terms. A requirement meant to have no exceptions uses an absolute term.
- Use one term per concept, and reuse the same phrase for the same idea.
- State once, before the scenarios, what the user does in every scenario unless a scenario says otherwise. Each scenario's starting state states only what differs and what its checks depend on.
- A statement that fails Scope rule 5, 6 or 7 belongs to a later level. Move it word for word to the project's open questions, for the level that owns it, and leave it out of the Outcome.

## Self-check before review

1. Run `scripts/structure.py <document>` and fix every failure it prints.
2. Run `scripts/absolutes.py <document>`.
3. Judge the document against the rules of each of the four reviews the definition names, writing the grid each one asks for.
4. Fix every FAIL, then repeat from step 1.
