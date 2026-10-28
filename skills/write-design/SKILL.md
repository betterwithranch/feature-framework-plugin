---
name: write-design
description: Write the Design of a feature, the third planning level - every choice of how the feature is built that it raises, each decided, with the codified rules and decision records that settle the rest cited. Use after the feature's Behaviour passes its review, before slicing or code, and to fix findings from a Design review.
---

# Write a Design document

Read [the Design definition](../references/design.md), [the decision classification](../references/decisions.md), and the feature's passed Outcome and Behaviour. Write a document that has the definition's contents and meets its criteria.

## Rules

- Start from the Behaviour. For each rule and edge case, find the choices of how to build it.
- For each choice, check the passed levels, decision records and codified rules. If one settles it, cite it. If none does, classify the choice with the decision classification: ask the user about theirs during this level, write each answer into a decision record and cite it, and make and record the work's.
- Ask only about this level. Record a question for a later level against that level.
- Decide only what the Behaviour needs. Leave the order of work to Slices and the code to Build.
- State one choice per decision. When a fix needs a new choice, add a decision rather than a sentence to an existing one.
- Use one term per concept, the same terms as the Outcome and Behaviour.
- Be simple and to the point.
- Reuse before building. Before designing a mechanism, look for an existing tool, host feature, documented practice or project utility that does it, and use it when it meets the need. Build only the gap, and say why.
- Fix a problem by removing the wording that caused it, not by adding a new qualifier or distinction.

## Self-check before review

1. Map every Behaviour rule and edge case to the decisions and cited rules that build it.
2. Check that each decision names who made it, and that each of the user's decisions cites its decision record.
3. Check the document against each criterion in the definition and fix what fails.

## After a fix

Rerun the self-check on the changed text and on every decision, cited rule and Behaviour rule about the same subject, whether or not they refer to each other. A fix that moves a problem somewhere else is not a fix.
