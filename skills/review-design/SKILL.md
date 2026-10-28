---
name: review-design
description: Review a feature's Design document against its passed Outcome and Behaviour and report findings that would change what gets built. Use at the Design gate, given only the Design document, the Outcome, the Behaviour and the files the Design cites.
---

# Review a Design document

Read [the Design definition](../references/design.md) and [the decision classification](../references/decisions.md). Review the Design document you are given against them, the passed Outcome and Behaviour, and the codified rules and decision records it cites. Do not judge whether any of them matches a discussion or context that produced them.

## Method

Before judging, map each Behaviour rule and edge case to the decisions and cited rules that build it. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to Behaviour, Slices or Build is not a finding.
- Wording that doesn't change what gets built is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. A rule or edge case nothing builds, an open decision, a decision of the user's with no decision record, or a decision whose result contradicts a rule it names is shown by the text.
- Impact is high if the feature might be built to do the wrong thing, and medium otherwise.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Output

- Map: each Behaviour rule and edge case to its decisions and cited rules, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
