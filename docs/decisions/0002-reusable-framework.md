# 0002. Build a reusable framework, not session-scoped agreements

Status: accepted, 2026-10-27

## Context

Agreements made in one session were lost to the next, so the same decisions were made again.

## Decision

The levels and their rules are a reusable framework that outlasts any single session. Its form (likely a plugin for Claude Code and Codex, as codeguard is) is decided at the Design level.

## Consequences

Agreements are recorded in this repository as they are made.
