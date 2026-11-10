---
name: review-outcome
description: Reviews a feature's Outcome document by running its structure checks, its four rule-based reviews and the glossary review, each as an isolated judge, and merges their grids. Use at the Outcome gate.
---

# Review an Outcome

Read [the Outcome definition](../references/outcome.md). It names the structure checks and the four reviews.

The review rules follow [the writing rules](../references/writing.md).

## Method

1. Run `skills/write-outcome/scripts/structure.py <document>`. Report any failure it prints.
2. Run `skills/write-outcome/scripts/absolutes.py <document>` and keep its output for the Clarity judge.
3. Run each of the four reviews as its own isolated judge, in parallel. Give each judge only the document, its own rule file and what that file says to read: the Clarity judge also gets the absolutes output; the Provenance judge also gets the conversation, the decision log and the codified rules. A judge sees no other judge's rules or output.
4. Run [the glossary review](../references/glossary-review.md) as a fifth isolated judge, given the project glossary, the conversation, the decision log, the codified rules and the project.
5. Merge the five grids, keeping every cell.

## Output

- Structure: the script's failures, or "pass".
- The merged grid: every row against every rule of every review, PASS, FAIL with its quote, or n/a; the glossary review's rows are its entries.
- The FAIL cells, listed with review, rule, row and quote.

## Rounds

A round starts with one review. When every cell passes, two more run independently, and the round passes when all three pass. When the first review has a FAIL, the round ends there and the failures are fixed before the next round.
