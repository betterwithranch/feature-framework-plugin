# 0072. No "n/a": a rule passes what it doesn't apply to

Status: accepted, 2026-11-10

## Context

Each review's Output said every cell was PASS or FAIL, then marked a rule that doesn't apply as "n/a". The Outcome definition says an Outcome passes when "each of its four reviews marks every cell PASS". Asked about this (FF-73), the user said: "I don't think we need to know that the review considered it n/a. to the review anything n/a is a pass. remove n/a and simplify this".

## Decision

- Each review's Output reads: "A grid: one row per item and one column per rule. Each cell is PASS or FAIL. A rule passes any item it doesn't apply to." The glossary review says "entry" for "item".
- A quote line covers only items its rule applies to, for example "A PASS for rule 2 on an item it applies to quotes…". A PASS missing a quote it needs is a FAIL.

## Consequences

- Amends the Output of every review and [decision 0069](0069-review-grids-quote-evidence-for-each-part.md)'s quote lines.
- The Outcome definition keeps "each of its four reviews marks every cell PASS".
