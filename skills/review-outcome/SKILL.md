---
name: review-outcome
description: Review a feature's Outcome document on its own and report findings that would change what gets built. Use at the Outcome gate, given only the Outcome document.
---

# Review an Outcome

Read [the Outcome definition](../references/outcome.md). Review the Outcome document you are given against it, on its own. Do not judge whether it matches any discussion or context that produced it.

## Method

Before judging, list for yourself every requirement, scenario and measure, and map each requirement to the scenarios whose verification would fail without it. List every absolute term in every sentence of every requirement and definition, and check each against every other requirement for an exception. For each check in a scenario or measure, find the requirement words that rule out what it fails; a requirement allows whatever its words don't rule out. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to a later level is not a finding.
- Wording that doesn't change what the user gets is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. For criteria 4 and 5, the text shows a finding when a requirement has no verification that fails if it isn't met, or when a verification's own words, built faithfully, would misjudge the result. A verification that tests implementation instead of the behaviour the user observes is a finding. A verification that could be built badly is not.
- Impact is high if the user might not get the intended result, and medium if only a verification or measure is affected.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Rounds

A round starts with one run of this review. When it reports no findings, two more run independently, and the round passes when all three report none. When the first run reports findings, the round ends there and the findings are fixed before the next round.

## Output

- Trace map: each requirement to its scenarios, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
