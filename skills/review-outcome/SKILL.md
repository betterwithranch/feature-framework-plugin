---
name: review-outcome
description: Review a feature's Outcome document on its own and report findings that would change what gets built. Use at the Outcome gate, given only the Outcome document.
---

# Review an Outcome

Review the Outcome document you are given, on its own. Do not judge whether it matches any discussion or context that produced it. Review only whether it does the Outcome's job: stating what the user gets and how success is judged.

## What an Outcome contains

An Outcome must contain:

- Who the feature is for.
- What it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated check and a pass bar. No check may need a person.
- How success is measured on real use.

An Outcome must not contain non-goals, behaviour rules or edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

An Outcome leaves room for interpretation; later work narrows it. If resolving a point needs a definition, rule, threshold or procedure (what exactly counts as X, when exactly Y happens, how much work stops), it is not a finding.

## Method

Before judging, list for yourself every claim, scenario and measure, and map each claim to the scenarios that would fail without it.

## Questions

1. Complete. Is every required element present?
2. Nothing extra. Is anything present that is not the Outcome's responsibility?
3. Clear. Is there a statement where no reader would know what result the user is meant to get?
4. Traceable. Is there a claim with no scenario that would fail without it, or a scenario or measure that checks no claim?
5. Sound checks. Would any check or measure pass when the user doesn't get the result, or fail or count against behaviour a claim requires or allows? Could the work being judged satisfy its own check? Is any scenario's starting state left to the work being judged instead of set by the scenario?
6. Consistent. Do any claims, scenarios or measures contradict each other?

## Findings

- A finding quotes the document.
- Wording that doesn't change what the user gets is not a finding.
- Drop hypotheticals that no quoted text supports: perfection is the enemy of done. This does not apply to questions 4 and 5: a missing scenario or an unsound check that the text shows is always a finding.
- Impact is high if the user might not get the intended result, and medium if only a check or measure is affected.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Output

- Trace map: each claim to its scenarios, one line each.
- Questions 1-6: PASS or FINDINGS for each.
- Findings: id, question, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
