---
name: review-behaviour
description: Review a feature's Behaviour document against its approved Outcome and report findings that would change what gets built. Use at the Behaviour gate, given only the Behaviour document and the Outcome.
---

# Review a Behaviour document

Read [the Behaviour definition](../references/behaviour.md). Review the Behaviour document you are given against it and against the approved Outcome you are given. Do not judge whether either matches any discussion or context that produced them.

## Method

Before judging, map each Outcome claim to its rules, and each rule to its edge cases and examples. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to Design or to how tests are built is not a finding.
- Wording that doesn't change what gets built is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. A missing rule, example or surface, or an example whose result doesn't follow from its rule, is shown by the text.
- Impact is high if the feature might be built to do the wrong thing, and medium otherwise.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Output

- Map: each Outcome claim to its rules, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
