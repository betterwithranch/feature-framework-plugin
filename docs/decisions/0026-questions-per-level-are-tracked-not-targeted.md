# 0026. Questions per level are tracked, not targeted

Status: accepted, 2026-11-03

## Context

The user said "we should measure for tracking, but not enforce any expected number of questions"; a target would push the work to skip questions it should ask.

## Decision

The number of questions the work asks the user at each level is recorded for every feature, so the cost of the interview can be seen. No number counts as a failure. How the count is kept is decided at Design.
