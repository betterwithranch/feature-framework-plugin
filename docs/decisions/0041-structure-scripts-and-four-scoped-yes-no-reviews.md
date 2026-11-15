# 0041. Structure scripts and four scoped yes/no reviews

Status: accepted, 2026-11-06

## Context

Six review rounds failed because criteria 4 and 5 asked each run to search for any way a scenario could pass or fail, so each run sampled different problems; the user chose FF-52 A: a review is an exhaustive checklist marking every item pass or fail, not a sampling.

## Decision

Scripts check a level document's structure: the required sections, every requirement ID cited by a scenario or measure and every cited ID defined, IDs in order without gaps or duplicates, absolute terms listed per statement, and no banned term for the level. A PreToolUse command hook on the shell tool, `hooks/selfcheck.py`, runs the structure checks under Claude Code and Codex when the agent runs `git commit`, and denies the commit when a changed level document fails them; a git hook doesn't count, and git config is never touched. Four separate reviews, Scope, Clarity, Verification and Provenance, each with five to eight yes/no rules, each run as its own isolated judge. Each outputs a grid of every requirement, scenario and measure against each of its rules, PASS or FAIL with a quote, and judges nothing outside its scope. Rules judge what the document describes; nothing runs at level 1. This replaces criteria 1-6, the review-outcome instructions and the self-check's open-ended steps.
