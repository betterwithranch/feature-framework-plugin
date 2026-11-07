# Open questions

Questions set aside because they belong to a later level ([D9](decisions.md)). Each is answered at its owning level, not before.

| Question | Owning level |
| --- | --- |
| Docs for people who install the framework, written for them rather than for those who build from a level's document ([D56](decisions.md)) | The level that owns packaging |
| How the framework ships its hooks to other projects: a Claude Code plugin's `hooks/hooks.json` with `${CLAUDE_PLUGIN_ROOT}`, and Codex's equivalent. This repo's `.claude/settings.json` and `.codex/config.toml` only run them here | The level that owns packaging |
| Where the end-to-end sample project lives: a separate repo, or a fixture in this repo | Design |
| Where a feature's level artifacts (Outcome, Behaviour, Design, Slices) are stored | Design |
| The framework's form, for example a plugin for Claude Code and Codex | Design |
| Where the framework keeps the readability rules and the interview and playback instructions | Behaviour, Design |
| The Behaviour definition's line on found facts: only what users get today ([D30](decisions.md)) | Behaviour |
| The Design definition's line on found facts: the code, data, services and interfaces the design builds on ([D30](decisions.md)) | Design |
| The Slices definition's line on found facts: Design's plus how the project is built and tested ([D30](decisions.md)) | Slices |
| How each level's review checks found facts against the project and statements against what the user said | Design |
| How the count of questions asked per level is kept ([D32](decisions.md)) | Design |
| A hook that enforces one question at a time and the readability rules on every message the framework sends the user, whatever the channel (chat, AskUserQuestion, a file). It refuses, before sending, a message that carries more than one decision: a numbered round, a range, or a set to approve. The Outcome's measure "messages that ask more than one question" reads from it. The coordinator pattern has a working equivalent for its board (`one-question-gate.py`, a PreToolUse hook on the board-write tool that denies a question whose title names a range or a set, or whose details list several numbered items or recommendations); Design adapts the idea, not the code | Design |
| How many runs each scenario needs to pass. The user set 10 on 2026-10-27, then suggested 3 on 2026-11-07 ([D70](decisions.md)) | The level that writes the tests |
| Whether the scenarios are plugin evals (`claude plugin eval`, following Anthropic's guidance for well-written plugin evals), and how a multi-turn scripted user is done, since plugin eval documents no simulated user ([D70](decisions.md)) | The level that writes the tests |
| Whether the deterministic hook scripts are tested with pytest ([D70](decisions.md)) | The level that writes the tests |
| How support for both Claude Code and Codex is shown without running every scenario under each ([D70](decisions.md)) | The level that writes the tests |
