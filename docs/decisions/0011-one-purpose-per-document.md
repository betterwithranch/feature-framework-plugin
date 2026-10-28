# 0011. Give every document one purpose

Status: accepted, 2026-10-28

## Context

Files mixed records, history and instructions, which made them hard to read and to find things in.

## Decision

Every file has one purpose and holds only content that serves it. History and dates belong only in decision records. Instructions the framework uses on features are written as Claude skills under `skills/`, with no history, dates or status. The rules are in `CLAUDE.md`.

## Consequences

Content that doesn't fit a file's purpose moves to the file whose purpose it serves.
