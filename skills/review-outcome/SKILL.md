---
name: review-outcome
description: Review a feature's Outcome document on its own and report findings that would change what gets built. Use at the Outcome gate, given only the Outcome document.
---

# Review an Outcome

Read [the Outcome definition](../references/outcome.md). Review the Outcome document you are given against it, on its own. Do not judge whether it matches any discussion or context that produced it.

## Method

Before judging, list for yourself every claim, scenario and measure, and map each claim to the scenarios that would fail without it. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to a later level is not a finding.
- Wording that doesn't change what the user gets is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. For criteria 4 and 5, the text shows a finding when a claim has no scenario, or when a check's own words would misjudge the result. A way the work could game a check, or a check built badly, is not shown by the text.
- Impact is high if the user might not get the intended result, and medium if only a check or measure is affected.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Output

- Trace map: each claim to its scenarios, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
