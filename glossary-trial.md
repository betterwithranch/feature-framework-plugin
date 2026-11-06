# Glossary review trial: two runs on docs/spec/glossary.md at 05fd6de

Cells compared: 72. Same verdict: 69 (95.8%). Disagree: 3. FAILs: A 8, B 7. Run B labelled one row "G: Requirement (incl. verification)"; it is matched as "G: Requirement". The judges had the glossary, the decision log, the codified rules, my interview notes (the full conversation isn't available) and, as the project, README.md, skills/ and hooks/.

## Cells where the runs disagree

| Row | Rule | A | B | A's cell | B's cell |
|---|---|---|---|---|---|
| g: code starts | 1 | FAIL | PASS | FAIL: "the first change to the project's code or tests for that feature" is not marked as the work's, and interview-answers.md line 21 records it as the work's own reading ("Reading I took ... kept ... the 'code starts' definition"); no decision or answer shows the user said or agreed this definitio | PASS (the approved level 1 Outcome used "code starts", D15/D19; interview notes say the "code starts" definition was kept) |
| g: requirement | 1 | FAIL | PASS | FAIL: "here or in a level's document": "here" (the glossary) is not marked as the work's and no decision or answer places requirements in the glossary (D33, D56 put them in a level's document) | PASS (D56 visible R IDs; D33/FF-23 requirement and verification) |
| g: complete requirement | 2 | PASS | FAIL | PASS | FAIL: "at this level" (the glossary is shared by every level; no level is named, so "this level" has no referent) |

## Every FAIL

| Run | Row | Rule | Cell |
|---|---|---|---|
| A | g: code starts | 1 | FAIL: "the first change to the project's code or tests for that feature" is not marked as the work's, and interview-answers.md line 21 records it as the work's own reading ("Reading I took ... kept ... the 'code starts' definition"); no decision or answer shows the user said or agreed this definitio |
| A | g: approved | 3 | FAIL: "after the level passes its review" sets an order (approval only after the review passes), a procedure, not only what the term means |
| B | g: approved | 3 | FAIL: "after the level passes its review" (sets the ordering rule of D26/D36, review before approval, inside the definition) |
| A | g: approved | 6 | FAIL: "after the level passes its review" limits approval to a level that has passed its review; the project uses approval of decisions and fixes too: hooks/prompts/goals.md "every decision needs approval", hooks/prompts/stop-check.md "Asking approval of a decision, including a review fix that is on |
| B | g: approved | 6 | FAIL: "after the level passes its review" (project also uses approval for decisions, with no level review: hooks/prompts/goals.md "every decision needs approval"; hooks/prompts/stop-check.md "Asking approval of a decision") |
| A | g: requirement | 1 | FAIL: "here or in a level's document": "here" (the glossary) is not marked as the work's and no decision or answer places requirements in the glossary (D33, D56 put them in a level's document) |
| A | g: requirement | 2 | FAIL: "here or in a level's document": the glossary lists no R IDs, so a reader can't tell what "here" refers to |
| B | g: requirement | 2 | FAIL: "here or in a level's document" (the glossary lists no R IDs; "here" has no referent in a glossary shared by every level, docs/spec/glossary.md) |
| A | g: complete requirement | 1 | FAIL: "at this level" is not marked as the work's; the user's standard (D33; interview-answers.md FF-23) is "with nothing left to ask the user", with no level qualifier |
| B | g: complete requirement | 1 | FAIL: "at this level" (D33 and interview notes FF-23 say only "with nothing left to ask the user"; the qualifier is not the user's and not marked as the work's) |
| B | g: complete requirement | 2 | FAIL: "at this level" (the glossary is shared by every level; no level is named, so "this level" has no referent) |
| A | g: found fact | 3 | FAIL: "so every level uses project terms" sets a rule for every level, beyond what the term means |
| B | g: found fact | 3 | FAIL: "so every level uses project terms" (sets a rule for levels, not a meaning) |
| A | g: the user's to settle | 1 | FAIL: "a decision the classification gives the user, a point it doesn't clearly assign, and a conflict between one of the user's decisions and something no one decided" is not marked as the work's and is not what was agreed: skills/references/decisions.md (D42) also gives the user "When two current  |
| B | g: the user's to settle | 1 | FAIL: "a conflict between one of the user's decisions and something no one decided" (the term and this scope are not said or agreed and not marked as the work's; skills/references/decisions.md "Always" also gives the user "two current decisions of the user's conflict", which the entry leaves out) |
