# 0053. Work under both Claude Code and Codex

Status: replaced by [decision 0055](0055-the-framework-s-own-code-works-under-both-claude-c.md)

## Context

The user said "this solution cannot be claude code only. It needs to support both claude and codex. this requirement needs to be added to avoid future breaking changes."

## Decision

Decided 2026-11-04. Everything the framework ships works under both Claude Code and Codex: its prompts, its checks, and the settings that load them. Nothing depends on a feature only one host has.
