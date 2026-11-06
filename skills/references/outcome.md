# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Reader

An Outcome is written for those who build from it: the agents doing later levels, whoever turns its scenarios into tests, and maintainers. The user approves that same document. It is written in a neutral voice, naming "the user", not "you".

## Contents

An Outcome contains:

- Who the feature is for.
- Its requirements: what it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated verification and a pass bar. No verification needs a person. A pass bar that applies to every scenario, such as how many runs must pass, is stated once.
- How success is measured on real use, each measure with a target.
- A reference to the project's glossary, which defines its terms.

Every requirement, scenario and measure carries a visible ID (R1, S1, M1), stable once approved. Each line states one requirement.

## Reviews

An Outcome passes when its structure checks pass and each of its four reviews marks every cell PASS. Each review is its own set of yes/no rules, judged by its own isolated judge:

- [Scope](outcome-reviews/scope.md)
- [Clarity](outcome-reviews/clarity.md)
- [Verification](outcome-reviews/verification.md)
- [Provenance](outcome-reviews/provenance.md)

The structure checks are `skills/write-outcome/scripts/structure.py`: the required sections are present, every requirement ID is cited by a scenario or measure and every cited ID exists, IDs run in document order without gaps or duplicates, and no level-1 banned term appears. `skills/write-outcome/scripts/absolutes.py` lists the absolute terms in each statement for the Clarity review.

Each rule judges what the document describes; nothing runs at this level. A judge leaves out a FAIL that few users would ever meet or that changes nothing for them. This is judged, not scored.
