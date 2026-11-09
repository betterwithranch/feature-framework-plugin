# 0055. The framework's own code works under both Claude Code and Codex

Status: accepted, 2026-11-04

## Context

The user said "working in claude and codex is a requirement for the *code* generated in the framework, not a requirement for all future changes in all coordinators... each feature has its own claude/codex requirements that the framework does not dictate. But, if the framework is going to implement code in the form of hooks or skills to help enforce itself *THAT* code should support both."

## Decision

Supporting both Claude Code and Codex is required only of the code the framework ships to enforce itself: its hooks, checks, skills and the settings that load them. The framework sets no host requirement for a feature; each feature has its own.

## Consequences

- Replaces [decision 0053](0053-work-under-both-claude-code-and-codex.md).
