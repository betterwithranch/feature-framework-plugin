# CLAUDE.md

## Documentation

- Every file has one purpose. Before writing to a file, check the content serves that purpose; put anything else where it belongs.
- `README.md` says what the framework is and where things are. Nothing else: no status, progress or approvals.
- `docs/spec/` holds the framework's own level artifacts, as specifications only.
- `docs/decisions.md` is the append-only decision log: one entry per decision, never edited or deleted; a change is a new entry that replaces the old.
- `docs/open-questions.md` lists questions set aside for the level that owns them.
- `skills/` holds instructions the framework uses on every feature. Write them as Claude skills: frontmatter with `name` and `description`, then direct instructions. No history, dates, status or examples of past mistakes.
- `skills/references/` holds what more than one skill needs, such as what a level's document contains and the criteria it must meet. Skills refer to it and don't repeat it.
- `docs/goals.md` states the goals every change serves and when to decide versus ask. Hooks in `.claude/settings.json` load it at session start and on every prompt.

## Working

- Follow `docs/goals.md`. Decide and proceed on anything already agreed; ask only when blocked by a decision no one has made or a conflict.
- Before acting on anything from the user that could change the project, play back what you understood in your own words and wait for confirmation. A plain answer to your own question needs no playback.
- Ask one question at a time, with a recommended answer and enough detail to answer it without asking back. Every message for a person is readable at a glance.
- Nothing is guessed. Look up a fact, ask a decision, ask a reading, and put to the user anything you can't settle one of those ways.
- A level's review has four rounds against the version the user last approved; the work changing the document doesn't reset them. Fix findings with the level's write skill, including its after-a-fix self-check. A fix that is a decision is played back and approved first, one at a time; a fix is not a decision only when it restores the document to something already agreed and cites it. When the rounds are spent, stop and bring the user the findings and a proposed instruction fix.
- Each level is built on its own branch, with its own pull request against `main`. Commit and push each agreed change to that branch when it is done. Work on the next level starts when the user approves the level.
