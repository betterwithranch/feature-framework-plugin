---
name: write-behaviour
description: Write the Behaviour of a feature, the second planning level - every rule and edge case with examples, the surface each is observed at, and non-goals. Use after the feature's Outcome is approved, before any design or code, and to fix findings from a Behaviour review.
---

# Write a Behaviour document

Read [the Behaviour definition](../references/behaviour.md) and the feature's approved Outcome. Write a document that has the definition's contents and meets its criteria.

## Rules

- Start from the Outcome's claims. For each, state the rules that make it true, then the edge cases of each rule.
- Draw out the user's intent. For each decision this level needs, check the Outcome, decision records and codified rules. If none settles it, classify it with [the decision classification](../references/decisions.md): ask the user about theirs, and make and record the work's. Ask only about this level; record a question for a later level against that level.
- State results, not mechanisms. Say what can be observed, not how it is produced.
- State one thing per rule or edge case. When a fix needs a new statement, add a rule or edge case with its own example rather than a sentence to an existing one.
- Keep every limit and exception of the Outcome claim a rule narrows, such as when something may happen.
- Give each rule and edge case a concrete example with real values.
- Use one term per concept, the same terms as the Outcome.
- Be simple and to the point.
- Reuse before building. Before designing a mechanism, look for an existing tool, host feature, documented practice or project utility that does it, and use it when it meets the need. Build only the gap, and say why.
- Fix a problem by removing the wording that caused it, not by adding a new qualifier or distinction.

## Self-check before review

1. Map every Outcome claim to its rules.
2. Check each rule and edge case has an example and a surface.
3. Check the document against each criterion in the definition and fix what fails.

## After a fix

Rerun the self-check on the changed text and on every rule, edge case, example and Outcome claim about the same subject, such as when you're asked or when tests change, whether or not they refer to each other. A fix that moves a problem somewhere else is not a fix.
