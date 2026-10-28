# 0016. Fix findings through the write skill, and stop a gate after four rounds

Status: accepted, 2026-10-28

## Context

The level 1 Outcome review ran twelve rounds after approval. Each round found new issues, often caused by the previous round's fixes. The fixes were patched straight into the document from the findings, without the write skill, so they added qualifiers and distinctions that the write skill forbids. The rounds also hid a conflict in the instructions: the definition left test construction to later levels, while the sound-checks criterion audited it.

## Decision

- A gate's findings are fixed with the write skill for that level: its rules apply to the fix, and its after-a-fix self-check runs before the next round.
- A gate stops after four rounds that don't pass. The next step is to look for a conflict or ambiguity between the instructions involved, report it, and fix the instructions, not to patch the document again.

## Consequences

- Fixes follow the same rules as the first draft.
- A gate that doesn't converge costs at most four rounds before its instructions are examined.
- This amends [decision 0012](0012-three-review-runs.md): a review still passes when all three runs are clean, but runs at most four rounds.
