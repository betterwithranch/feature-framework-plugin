# CLAUDE.md

## Documentation

- Every file has one purpose. Before writing to a file, check the content serves that purpose; put anything else where it belongs.
- `README.md` says what the framework is, its status and where things are.
- `docs/spec/` holds the framework's own level artifacts, as specifications only.
- `docs/decisions/` holds one decision per record. History and dates belong here.
- `docs/open-questions.md` lists questions set aside for the level that owns them.
- `skills/` holds instructions the framework uses on every feature. Write them as Claude skills: frontmatter with `name` and `description`, then direct instructions. No history, dates, status or examples of past mistakes.
