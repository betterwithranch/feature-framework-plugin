# Open questions

Questions set aside because they belong to a later level ([decision 0009](decisions/0009-block-lower-level-questions.md)). Each is answered at its owning level, not before.

| Question | Owning level |
| --- | --- |
| Where the end-to-end sample project lives: a separate repo, or a fixture in this repo | Design |
| Where a feature's level artifacts (Outcome, Behaviour, Design, Slices) are stored | Design |
| The framework's form, for example a plugin for Claude Code and Codex | Design |
| Where the framework keeps the readability rules and the interview and playback instructions | Behaviour, Design |
| The Behaviour definition's line on found facts: only what users get today ([decision 0030](decisions/0030-where-found-facts-live.md)) | Behaviour |
| The Design definition's line on found facts: the code, data, services and interfaces the design builds on ([decision 0030](decisions/0030-where-found-facts-live.md)) | Design |
| The Slices definition's line on found facts: Design's plus how the project is built and tested ([decision 0030](decisions/0030-where-found-facts-live.md)) | Slices |
| How each level's review checks found facts against the project and statements against what the user said | Design |
| How the count of questions asked per level is kept ([decision 0032](decisions/0032-questions-per-level-are-tracked.md)) | Design |
| A hook that enforces one question at a time and the readability rules on every message the framework sends the user, whatever the channel (chat, AskUserQuestion, a file). It refuses, before sending, a message that carries more than one decision: a numbered round, a range, or a set to approve. The Outcome's measure "messages that ask more than one question" reads from it. The coordinator pattern has a working equivalent for its board (`one-question-gate.py`, a PreToolUse hook on the board-write tool that denies a question whose title names a range or a set, or whose details list several numbered items or recommendations); Design adapts the idea, not the code | Design |
