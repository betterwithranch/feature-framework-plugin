# 0031. Verifications test behaviour and pass independently

Status: accepted, 2026-11-04

## Context

The user said "verifications should not be dependent on each other. they should all verify independently and pass independently to verify the outcome is what is expected. writing of those verifications should be based on that," and "a verification that the log line says 'email sent' is a verification that the logging works and nothing more... these are supposed to be automated tests. normal testing standards apply... what is more likely is that this is too granular a verification for a level 1 outcome. this is testing implementation, not behavior."

## Decision

Verifications are automated tests held to normal testing standards. Each tests the behaviour the user observes, not how it is implemented, and each passes or fails on its own, independent of every other verification. A verification is judged by its own words against the requirement it verifies; only that requirement's allowances and exceptions count. A verification that reads the system's own log or report of success tests implementation, and is a review finding.
