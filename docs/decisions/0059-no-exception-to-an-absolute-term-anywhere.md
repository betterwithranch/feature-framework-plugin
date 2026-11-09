# 0059. No exception to an absolute term, anywhere

Status: accepted, 2026-11-09

## Context

Clarity rule 5 read "No other statement makes an exception to an absolute term the script lists in it", so it caught an exception made in another statement but passed one made in the same statement. [Decision 0033](0033-absolute-terms-have-no-exceptions.md) says an absolute term means no exceptions. Asked whether the rule should also catch an exception in the same statement (FF-64), the user chose A: there are no exceptions to absolute terms, ever, including in the same statement.

## Decision

- Clarity rule 5 reads: "No statement makes an exception to an absolute term the script lists in it."
- A review rule that fails to enforce a recorded decision is fixed to match that decision without asking. That is not a change to approved wording that needs the user.

## Consequences

- Amends the Clarity review's rules, [decision 0043](0043-the-clarity-review-s-rules.md).
