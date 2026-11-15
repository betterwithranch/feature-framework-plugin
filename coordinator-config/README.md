# Feature framework coordinator: session-local config

Copies of the files the Feature framework coordinator session ran from its own `~/.claude`, saved so a new coordinator session can restore them.

- `one-question-gate.py`: PreToolUse hook on ArtifactData that checks board questions.
- `level-terms.json`: the current level and the terms Craig ruled out of its questions; read by the hook.
- `settings-hooks.json`: the `hooks` block of `~/.claude/settings.json`, including the agent hook that refuses questions already decided.

To restore: copy the two files to `~/.claude/` and merge `settings-hooks.json` into `~/.claude/settings.json`.
