# CLAUDE.md

## Documentation

- Every file has one purpose. Before writing to a file, check the content serves that purpose; put anything else where it belongs.
- `README.md` says what the framework is and where things are. Nothing else: no status, progress or approvals.
- `docs/spec/` holds the framework's own level artifacts, as specifications only.
- `docs/decisions/` holds one decision per record. History, dates and approvals belong here.
- `docs/open-questions.md` lists questions set aside for the level that owns them.
- `skills/` holds instructions the framework uses on every feature. Write them as Claude skills: frontmatter with `name` and `description`, then direct instructions. No history, dates, status or examples of past mistakes.
- `skills/references/` holds what more than one skill needs, such as what a level's document contains and the criteria it must meet. Skills refer to it and don't repeat it.
- `docs/goals.md` states the goals every change serves and when to decide versus ask. Hooks in `.claude/settings.json` load it at session start and on every prompt.

## Working

- Follow `docs/goals.md`. Decide and proceed on anything already agreed; ask only when blocked by a decision no one has made or a conflict.
- Run an agreed gate until it passes, applying its findings, without asking between runs.
- Commit and push each agreed change to `main` when it is done.
