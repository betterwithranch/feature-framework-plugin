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

- **Settled:** a record or one of the user's answers requires a change. Quote the record's exact words, and say what they require.
- **Rule misfire:** a record settles the row as written, so the review rule is wrong for it. Quote the record that settles the row.
- **Conflict:** two records point different ways. Quote both.
- **Missing:** no record covers it.

Quote words exactly, with the record's number. Give Settled only when the quoted words require a change to the row.

Write the verdicts into the round file, under `verdicts`, one entry per FAIL:

```json
{
  "row": "M4",
  "rule": "3",
  "verdict": "Settled | Rule misfire | Conflict | Missing",
  "quotes": [{"record": "0075", "words": "…"}],
  "requires": "…",
  "user_answer": null
}
```

`requires` is given only for Settled. Then print the same verdicts as a table: row, rule, verdict, quotes and what each Settled verdict requires.

## Checking a fix

The agent writes each fix with the level's write skill, including its after-a-fix self-check. It records the fix under the entry's `fix`, as the file and the exact old and new text.

The judge then runs fresh again, with the same inputs and the entry's `fix`. It checks that the fix does what the verdict and its quotes require, and nothing else. It sets `passes` to true or false, with a one-sentence `reason`:

```json
"fix": {"file": "docs/spec/1-outcome.md", "old": "…", "new": "…", "passes": true, "reason": "…"}
```

Only a fix with `passes` true is applied.

## After the verdicts

The agent reports each applied fix with its verdict's quote. Every verdict other than Settled goes to the user, and nothing changes for it. When the user answers, the agent records the answer in the entry's `user_answer`. Then it writes the fix the answer requires, and the judge checks it the same way.
