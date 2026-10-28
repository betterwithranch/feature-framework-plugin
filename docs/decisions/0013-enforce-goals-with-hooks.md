# Enforce goals with hooks

- `docs/goals.md` holds the goals and the decide-or-ask rule.
- A SessionStart hook (startup, resume, compact) and a UserPromptSubmit hook load it into context.
- A Stop prompt hook blocks ending a turn on a request to approve something already decided.
- Every recorded rule the framework depends on is enforced by a hook or a check where one can enforce it.
