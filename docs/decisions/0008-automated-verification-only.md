# 0008. Verify everything automatically

Status: accepted, 2026-10-27

## Context

A check that needs a person keeps the person involved.

## Decision

Every verification is automated, with tests, Playwright, an LLM judge or a combination. A check that needs a person doesn't count.

## Consequences

End-to-end tests simulate the user with a scripted conversation.
