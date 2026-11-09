# Open questions

Questions set aside because they belong to a later level ([decision 0009](decisions/0009-block-lower-level-questions.md)). Each is answered at its owning level, not before.

| Question | Owning level |
| --- | --- |
| Where the end-to-end sample project lives: a separate repo, or a fixture in this repo | Design |
| Where a feature's level artifacts (Outcome, Behaviour, Design, Slices) are stored | Design |
| The framework's form, for example a plugin for Claude Code and Codex | Design |
| How the framework ships its hooks to other projects: a Claude Code plugin's `hooks/hooks.json` with `${CLAUDE_PLUGIN_ROOT}`, and Codex's equivalent. This repo's `.claude/settings.json` and `.codex/config.toml` only run them here | The level that owns packaging |
| A hook that enforces one question at a time and the readability rules on every message the framework sends the user, whatever the channel (chat, AskUserQuestion, a file). It refuses, before sending, a message that carries more than one decision: a numbered round, a range, or a set to approve. The Outcome's measure "messages that ask more than one question" reads from it. The coordinator pattern has a working equivalent for its board (`one-question-gate.py`, a PreToolUse hook on the board-write tool that denies a question whose title names a range or a set, or whose details list several numbered items or recommendations); Design adapts the idea, not the code | Design |
