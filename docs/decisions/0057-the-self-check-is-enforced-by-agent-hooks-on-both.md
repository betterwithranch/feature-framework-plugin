# 0057. The self-check is enforced by agent hooks on both hosts

Status: replaced by [decision 0041](0041-structure-scripts-and-four-scoped-yes-no-reviews.md)

## Context

The user said "codex supports hooks so works for claude and codex means hooks for both, not a git hook that also blocks manual effort. that is absolutely not the same thing. if that is the requirement you captured it is wrong".

## Decision

Decided 2026-11-06. "Under both hosts" means each host's own agent hook, Claude Code's and Codex's, runs the shared script. A git hook doesn't count: it isn't an agent hook, and it blocks people's manual commits. A PreToolUse command hook on the shell tool (`Bash` on both hosts), `hooks/selfcheck.py`, acts only when the agent's command runs `git commit`. It denies the commit when a changed `docs/spec/*.md` has no table at `<git dir>/ff-selfcheck/<blob hash>.md` naming every requirement, scenario and measure in that version. It never touches git config.

## Consequences

- Replaces [decision 0056](0056-a-level-document-is-committed-only-with-a-full-sel.md).
