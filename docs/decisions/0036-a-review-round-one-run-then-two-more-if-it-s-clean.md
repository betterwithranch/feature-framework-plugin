# 0036. A review round: one run, then two more if it's clean

Status: accepted, 2026-11-04

## Context

The user said "run the review once to make sure it passes, then 2 more times separately. running 3 times when you don't even know it passes once is wrong... the first pass makes sure its correct, the multi-check follow-up makes sure it is reliable. count the first pass in the total so for 3 total, it is a run of 1 followed by a run of 2 if the first run was clean".

## Decision

A review round starts with one run. When it reports no findings, two more runs follow, each independent, and the round passes when all three are clean. When the first run has findings, they are fixed and the next round starts again at its first run. Every finding from any run is acted on.

## Consequences

- Replaces [decision 0012](0012-three-review-runs.md).
