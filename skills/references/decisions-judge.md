# Decisions judge

After a review with any FAIL, nothing changes and no review starts until this judge rules on every FAIL. The judge runs fresh, as its own isolated agent.

## Inputs

- The round file, `reviews/round.json`, with the FAIL cells of one review. Each cell gives the row, the rule's text and the words that fail.
- `docs/goals.md`.
- [The decision classification](decisions.md).
- The full text of every decision record in `docs/decisions/` whose status is accepted.

The judge gets nothing else. It never gets the reasoning of the agent that will fix the document.

## Verdicts

Give each FAIL one verdict:

- **Settled:** a record or one of the user's answers requires a specific change. Quote the record's exact words. Give the file, and the exact old and new text.
- **Rule misfire:** a record settles the row as written, so the review rule is wrong for it. Quote the record that settles the row.
- **Conflict:** two records point different ways. Quote both.
- **Missing:** no record covers it.

Quote words exactly, with the record's number. Give Settled only when the quoted words require that exact change.

## Output

Write the verdicts into the round file, under `verdicts`, one entry per FAIL:

```json
{
  "row": "M4",
  "rule": "3",
  "verdict": "Settled | Rule misfire | Conflict | Missing",
  "quotes": [{"record": "0075", "words": "…"}],
  "file": "docs/spec/1-outcome.md",
  "old": "…",
  "new": "…",
  "user_answer": null
}
```

`file`, `old` and `new` are given only for Settled. Then print the same verdicts as a table: row, rule, verdict, quotes, and old → new.

## After the verdicts

The agent applies only Settled changes, exactly as given, and reports each with its quote. Every other verdict goes to the user, and nothing changes for it. When the user answers, the agent records the answer in the entry's `user_answer`, with the file and the exact old and new text the answer requires.
