# 0056. A level document is committed only with a full self-check

Status: replaced by [decision 0057](0057-the-self-check-is-enforced-by-agent-hooks-on-both.md)

## Context

The user asked for a hook "to make sure you stop doing this when making changes", after fixes were made one finding at a time without write-outcome's full self-check; the work chose how to build it (decisions.md, the work decides 2).

## Decision

Decided 2026-11-04. A git pre-commit hook, `hooks/git/pre-commit`, blocks a commit that changes any `docs/spec/*.md` unless `<git dir>/ff-selfcheck/<blob hash of the staged file>.md` exists and names every requirement (R<n>), scenario (S<n>) and measure (M<n>) the hook parses from the staged file. SessionStart under Claude Code and Codex runs `git config core.hooksPath hooks/git`, so every session has it on. A git hook runs the same under both hosts ([decision 0055](0055-the-framework-s-own-code-works-under-both-claude-c.md)).
