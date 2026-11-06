# Trial: four reviews, two independent runs each, on docs/spec/1-outcome.md at 1e1cc17

Each review ran twice as an isolated judge (runs A and B) with the same prompt and inputs. The Provenance judges had the decision log, the decision classification, CLAUDE.md and my interview notes; the full conversation isn't available as a file. Structure script on the same document: one failure, `R39 is cited by no scenario or measure`. Verification run A labelled scenario rows with their cited IDs, e.g. `S1 (R1 R2 …)`; the comparison matches rows by ID.

## Summary

| Review | Cells compared | Same verdict | Disagree on PASS/FAIL | Disagree on n/a or row | FAIL in A | FAIL in B |
|---|---|---|---|---|---|---|
| Scope | 736 | 647 (87%) | 9 | 80 | 41 | 38 |
| Clarity | 455 | 455 (100%) | 0 | 0 | 3 | 3 |
| Verification | 546 | 543 (99%) | 3 | 0 | 14 | 13 |
| Provenance | 455 | 441 (96%) | 1 | 13 | 2 | 3 |

"missing" means one run had a row the other didn't.

## Scope

### Cells where the runs disagree (89: 9 PASS/FAIL, 80 PASS vs n/a or a missing row)

| Row | Rule | A | B | A's cell | B's cell |
|---|---|---|---|---|---|
| for whom | 6 | FAIL | PASS | FAIL: "called \"the user\" below" | PASS |
| r7 | 8 | FAIL | PASS | FAIL: "A plain answer is acted on without a playback of its own" | PASS |
| r15 | 2 | FAIL | PASS | FAIL: "Nothing is guessed" | PASS |
| r28 | 2 | PASS | FAIL | PASS | FAIL: "Approving a level makes the user's decisions and answers in it agreed" |
| r29 | 2 | PASS | FAIL | PASS | FAIL: "The work's decisions in an approved level stay the work's" |
| r30 | 2 | PASS | FAIL | PASS | FAIL: "A decision holds only within its stated scope" |
| g: found fact | 8 | FAIL | PASS | FAIL: "Using a project term with the project's meaning is not a found fact" | PASS |
| g: the user's to settle | 8 | FAIL | PASS | FAIL: "a conflict between one of the user's decisions and something no one decided" | PASS |
| preamble | 8 | FAIL | PASS | FAIL: "no check relies only on tests written by the work being judged" | PASS |
| r1 | 3 | PASS | n/a | PASS | n/a |
| r1 | 4 | PASS | n/a | PASS | n/a |
| r2 | 3 | PASS | n/a | PASS | n/a |
| r2 | 4 | PASS | n/a | PASS | n/a |
| r3 | 3 | PASS | n/a | PASS | n/a |
| r3 | 4 | PASS | n/a | PASS | n/a |
| r4 | 3 | PASS | n/a | PASS | n/a |
| r4 | 4 | PASS | n/a | PASS | n/a |
| r5 | 3 | PASS | n/a | PASS | n/a |
| r5 | 4 | PASS | n/a | PASS | n/a |
| r6 | 3 | PASS | n/a | PASS | n/a |
| r6 | 4 | PASS | n/a | PASS | n/a |
| r7 | 3 | PASS | n/a | PASS | n/a |
| r7 | 4 | PASS | n/a | PASS | n/a |
| r8 | 3 | PASS | n/a | PASS | n/a |
| r8 | 4 | PASS | n/a | PASS | n/a |
| r9 | 3 | PASS | n/a | PASS | n/a |
| r9 | 4 | PASS | n/a | PASS | n/a |
| r10 | 3 | PASS | n/a | PASS | n/a |
| r10 | 4 | PASS | n/a | PASS | n/a |
| r11 | 3 | PASS | n/a | PASS | n/a |
| r11 | 4 | PASS | n/a | PASS | n/a |
| r12 | 3 | PASS | n/a | PASS | n/a |
| r12 | 4 | PASS | n/a | PASS | n/a |
| r13 | 3 | PASS | n/a | PASS | n/a |
| r13 | 4 | PASS | n/a | PASS | n/a |
| r14 | 3 | PASS | n/a | PASS | n/a |
| r14 | 4 | PASS | n/a | PASS | n/a |
| r15 | 3 | PASS | n/a | PASS | n/a |
| r15 | 4 | PASS | n/a | PASS | n/a |
| r16 | 3 | PASS | n/a | PASS | n/a |
| r16 | 4 | PASS | n/a | PASS | n/a |
| r17 | 3 | PASS | n/a | PASS | n/a |
| r17 | 4 | PASS | n/a | PASS | n/a |
| r18 | 3 | PASS | n/a | PASS | n/a |
| r18 | 4 | PASS | n/a | PASS | n/a |
| r19 | 3 | PASS | n/a | PASS | n/a |
| r19 | 4 | PASS | n/a | PASS | n/a |
| r20 | 3 | PASS | n/a | PASS | n/a |
| r20 | 4 | PASS | n/a | PASS | n/a |
| r21 | 3 | PASS | n/a | PASS | n/a |
| r21 | 4 | PASS | n/a | PASS | n/a |
| r22 | 3 | PASS | n/a | PASS | n/a |
| r22 | 4 | PASS | n/a | PASS | n/a |
| r23 | 3 | PASS | n/a | PASS | n/a |
| r23 | 4 | PASS | n/a | PASS | n/a |
| r24 | 3 | PASS | n/a | PASS | n/a |
| r24 | 4 | PASS | n/a | PASS | n/a |
| r25 | 3 | PASS | n/a | PASS | n/a |
| r25 | 4 | PASS | n/a | PASS | n/a |
| r26 | 3 | PASS | n/a | PASS | n/a |
| r26 | 4 | PASS | n/a | PASS | n/a |
| r27 | 3 | PASS | n/a | PASS | n/a |
| r27 | 4 | PASS | n/a | PASS | n/a |
| r28 | 3 | PASS | n/a | PASS | n/a |
| r28 | 4 | PASS | n/a | PASS | n/a |
| r29 | 3 | PASS | n/a | PASS | n/a |
| r29 | 4 | PASS | n/a | PASS | n/a |
| r30 | 3 | PASS | n/a | PASS | n/a |
| r30 | 4 | PASS | n/a | PASS | n/a |
| r31 | 3 | PASS | n/a | PASS | n/a |
| r31 | 4 | PASS | n/a | PASS | n/a |
| r32 | 3 | PASS | n/a | PASS | n/a |
| r32 | 4 | PASS | n/a | PASS | n/a |
| r33 | 3 | PASS | n/a | PASS | n/a |
| r33 | 4 | PASS | n/a | PASS | n/a |
| r34 | 3 | PASS | n/a | PASS | n/a |
| r34 | 4 | PASS | n/a | PASS | n/a |
| r35 | 3 | PASS | n/a | PASS | n/a |
| r35 | 4 | PASS | n/a | PASS | n/a |
| r36 | 3 | PASS | n/a | PASS | n/a |
| r36 | 4 | PASS | n/a | PASS | n/a |
| r37 | 3 | PASS | n/a | PASS | n/a |
| r37 | 4 | PASS | n/a | PASS | n/a |
| r38 | 3 | PASS | n/a | PASS | n/a |
| r38 | 4 | PASS | n/a | PASS | n/a |
| r39 | 3 | PASS | n/a | PASS | n/a |
| r39 | 4 | PASS | n/a | PASS | n/a |
| r40 | 3 | PASS | n/a | PASS | n/a |
| r40 | 4 | PASS | n/a | PASS | n/a |

### Every FAIL (79)

| Run | Row | Rule | Cell |
|---|---|---|---|
| A | for whom | 6 | FAIL: "called \"the user\" below" |
| A | r6 | 8 | FAIL: "other than a plain answer" |
| B | r6 | 8 | FAIL: "other than a plain answer" |
| A | r7 | 8 | FAIL: "A plain answer is acted on without a playback of its own" |
| A | r8 | 8 | FAIL: "after the playback when there is one" |
| B | r8 | 8 | FAIL: "after the playback when there is one" |
| A | r15 | 2 | FAIL: "Nothing is guessed" |
| A | r15 | 5 | FAIL: "a fact is looked up" |
| B | r15 | 5 | FAIL: "a fact is looked up" |
| A | r15 | 6 | FAIL: "a fact is looked up, a decision of the user's is asked, a decision of the work's is made by the work, a reading is asked" |
| B | r15 | 6 | FAIL: "a fact is looked up, a decision of the user's is asked, a decision of the work's is made by the work, a reading is asked" |
| A | r21 | 2 | FAIL: "its review checks each found fact against the project" |
| B | r21 | 2 | FAIL: "its review checks each found fact against the project" |
| A | r21 | 5 | FAIL: "its review checks each found fact against the project" |
| B | r21 | 5 | FAIL: "its review checks each found fact against the project" |
| A | r21 | 6 | FAIL: "a wrong fact is a finding" |
| B | r21 | 6 | FAIL: "a wrong fact is a finding" |
| A | r27 | 8 | FAIL: "except for clarity or to resolve a conflict" |
| B | r27 | 8 | FAIL: "except for clarity or to resolve a conflict" |
| B | r28 | 2 | FAIL: "Approving a level makes the user's decisions and answers in it agreed" |
| A | r28 | 6 | FAIL: "Approving a level makes the user's decisions and answers in it agreed" |
| B | r28 | 6 | FAIL: "Approving a level makes the user's decisions and answers in it agreed" |
| B | r29 | 2 | FAIL: "The work's decisions in an approved level stay the work's" |
| A | r29 | 6 | FAIL: "The work's decisions in an approved level stay the work's" |
| B | r29 | 6 | FAIL: "The work's decisions in an approved level stay the work's" |
| B | r30 | 2 | FAIL: "A decision holds only within its stated scope" |
| A | r30 | 6 | FAIL: "A decision holds only within its stated scope" |
| B | r30 | 6 | FAIL: "A decision holds only within its stated scope" |
| A | r31 | 6 | FAIL: "with the earlier one as its preferred default" |
| B | r31 | 6 | FAIL: "with the earlier one as its preferred default" |
| A | r31 | 8 | FAIL: "unless an agreement or codified rule already covers the case" |
| B | r31 | 8 | FAIL: "unless an agreement or codified rule already covers the case" |
| A | r37 | 8 | FAIL: "other than something only the user can settle" |
| B | r37 | 8 | FAIL: "other than something only the user can settle" |
| A | r38 | 8 | FAIL: "If something only the user can settle still blocks the work after code starts" |
| B | r38 | 8 | FAIL: "If something only the user can settle still blocks the work after code starts" |
| A | r39 | 7 | FAIL: "under Claude Code or under Codex" |
| B | r39 | 7 | FAIL: "under Claude Code or under Codex" |
| A | g: code starts | 6 | FAIL: "the first change to the project's code or tests for that feature" |
| B | g: code starts | 6 | FAIL: "the first change to the project's code or tests for that feature" |
| A | g: project | 6 | FAIL: "its code, tests, documents, decisions, settings, branches and pull requests" |
| B | g: project | 6 | FAIL: "its code, tests, documents, decisions, settings, branches and pull requests" |
| A | g: project | 7 | FAIL: "settings, branches and pull requests" |
| B | g: project | 7 | FAIL: "settings, branches and pull requests" |
| A | g: passes its review | 6 | FAIL: "a level's document meets that level's standards and is consistent and complete" |
| B | g: passes its review | 6 | FAIL: "a level's document meets that level's standards and is consistent and complete" |
| A | g: approved | 6 | FAIL: "the user says so, after the level passes its review" |
| B | g: approved | 6 | FAIL: "the user says so, after the level passes its review" |
| A | g: requirement | 6 | FAIL: "a result listed with an R ID, here or in a level's document" |
| B | g: requirement | 6 | FAIL: "a result listed with an R ID, here or in a level's document" |
| A | g: complete requirement | 6 | FAIL: "its verification can be written in full and run, with nothing left to ask the user at this level" |
| B | g: complete requirement | 6 | FAIL: "its verification can be written in full and run, with nothing left to ask the user at this level" |
| A | g: complete verification | 6 | FAIL: "it names what is checked, how, and what result passes" |
| B | g: complete verification | 6 | FAIL: "it names what is checked, how, and what result passes" |
| A | g: playback | 6 | FAIL: "the work telling the user, in its own words, what it understood" |
| B | g: playback | 6 | FAIL: "the work telling the user, in its own words, what it understood" |
| A | g: plain answer | 6 | FAIL: "the user's answer to the work's own question" |
| B | g: plain answer | 6 | FAIL: "the user's answer to the work's own question" |
| A | g: found fact | 6 | FAIL: "a fact about the project that the work found, rather than one the user gave" |
| B | g: found fact | 6 | FAIL: "a fact about the project that the work found, rather than one the user gave" |
| A | g: found fact | 8 | FAIL: "Using a project term with the project's meaning is not a found fact" |
| A | g: decision classification | 6 | FAIL: "the rules that set which decisions are the user's and which are the work's" |
| B | g: decision classification | 6 | FAIL: "the rules that set which decisions are the user's and which are the work's" |
| A | g: decision classification | 7 | FAIL: "../../skills/references/decisions.md" |
| B | g: decision classification | 7 | FAIL: "../../skills/references/decisions.md" |
| A | g: the user's to settle | 6 | FAIL: "a decision the classification gives the user, a point it doesn't clearly assign" |
| B | g: the user's to settle | 6 | FAIL: "a decision the classification gives the user, a point it doesn't clearly assign, and a conflict between one of the user's decisions and something no one decided" |
| A | g: the user's to settle | 8 | FAIL: "a conflict between one of the user's decisions and something no one decided" |
| A | preamble | 6 | FAIL: "runs several times under Claude Code and several times under Codex, on a sample project, and passes only if every run under both passes" |
| B | preamble | 6 | FAIL: "Each runs several times under Claude Code and several times under Codex, on a sample project, and passes only if every run under both passes" |
| A | preamble | 7 | FAIL: "under Claude Code and several times under Codex" |
| B | preamble | 7 | FAIL: "under Claude Code and several times under Codex" |
| A | preamble | 8 | FAIL: "no check relies only on tests written by the work being judged" |
| A | s4 | 8 | FAIL: "except for clarity" |
| B | s4 | 8 | FAIL: "except for clarity" |
| A | m1 | 8 | FAIL: "other than for clarity or about a conflict" |
| B | m1 | 8 | FAIL: "other than for clarity or about a conflict" |
| A | m6 | 8 | FAIL: "other than a plain answer" |
| B | m6 | 8 | FAIL: "other than a plain answer" |

## Clarity

### Cells where the runs disagree (0: 0 PASS/FAIL, 0 PASS vs n/a or a missing row)

| Row | Rule | A | B | A's cell | B's cell |
|---|---|---|---|---|---|

### Every FAIL (6)

| Run | Row | Rule | Cell |
|---|---|---|---|
| A | r37 | 3 | FAIL: "something only the user can settle" - second term for glossary "the user's to settle" (R16, G: The user's to settle) |
| B | r37 | 3 | FAIL: "something only the user can settle" - second term for the glossary's "the user's to settle" |
| A | r38 | 3 | FAIL: "something only the user can settle" - second term for glossary "the user's to settle" (R16, G: The user's to settle) |
| B | r38 | 3 | FAIL: "something only the user can settle" - second term for the glossary's "the user's to settle" |
| A | s5 | 3 | FAIL: "nothing only the user can settle is missing" - second term for glossary "the user's to settle"; listed beside "unassigned" and "conflicts", which that glossary entry already covers |
| B | s5 | 3 | FAIL: "nothing only the user can settle" - second term for the glossary's "the user's to settle" |

## Verification

### Cells where the runs disagree (3: 3 PASS/FAIL, 0 PASS vs n/a or a missing row)

| Row | Rule | A | B | A's cell | B's cell |
|---|---|---|---|---|---|
| r5 | 1 | FAIL | PASS | FAIL: "passes its review" — S3/S11/S14/M8 never test the next level waiting on an inconsistent or incomplete document | PASS |
| r40 | 1 | PASS | FAIL | PASS | FAIL: "so is its verification": nothing citing R40 checks a verification names what is checked, how, and what passes |
| s18 | 2 | FAIL | PASS | FAIL: "the second feature's record holds the decision" — R33 needs it recorded where the user can see it; not stated | PASS |

### Every FAIL (27)

| Run | Row | Rule | Cell |
|---|---|---|---|
| A | r4 | 1 | FAIL: "passes its review" — S14/S17 only test a failed standard or wrong fact; nothing checks an inconsistent or incomplete document is withheld from approval |
| B | r4 | 1 | FAIL: "passes its review" (S14 "fails one of that level's standards", S17 wrong fact): no check that a level that is inconsistent or incomplete isn't put up for approval |
| A | r5 | 1 | FAIL: "passes its review" — S3/S11/S14/M8 never test the next level waiting on an inconsistent or incomplete document |
| A | r10 | 1 | FAIL: "plays back what it understood the user wants at that level" — only S8 cites it, and S8 checks only ordering "after the playback", not that a playback of the level happens or what it holds |
| B | r10 | 1 | FAIL: "plays back what it understood the user wants at that level": S8 only presumes "the playback"; nothing checks a playback happens after the interview or what it says |
| A | r15 | 1 | FAIL: "a decision of the work's is made by the work" — no citing scenario (S2 S6 S8 S10 S15 S20) or M3 checks the work makes its own decisions |
| B | r15 | 1 | FAIL: "a decision of the work's is made by the work": no scenario or measure citing R15 checks it |
| A | r16 | 1 | FAIL: "one question at a time" — S10/S23 each involve a single missing thing; no citing check covers several asked one at a time |
| B | r16 | 1 | FAIL: "one question at a time": S10 and S23 check only that the thing is asked |
| A | r39 | 1 | FAIL: "the same way whether ... Claude Code or under Codex" — no scenario or measure cites R39 |
| B | r39 | 1 | FAIL: "the same way whether ... Claude Code or ... Codex": no scenario or measure cites R39 |
| B | r40 | 1 | FAIL: "so is its verification": nothing citing R40 checks a verification names what is checked, how, and what passes |
| A | s1 | 2 | FAIL: "the user is asked to make none of the work's" — R12 (not asked for facts) is not checked; R2 "one level at a time" not checked |
| B | s1 | 2 | FAIL: "Verifies ... R12": nothing checks the user isn't asked for facts the work can find out |
| A | s2 | 2 | FAIL: "It surfaces before code starts" — R9 needs the interview before the level's document is written, not just before code |
| B | s2 | 2 | FAIL: "It surfaces before code starts": R9 needs the interview before the level's document is written, and "surfaces" doesn't say the user was asked |
| A | s8 | 2 | FAIL: "after the playback" — R10 only used as ordering; nothing checks the playback states what the user wants at that level |
| B | s8 | 2 | FAIL: "after the playback" (Verifies R10): no check that a playback of what the user wants at the level is given |
| A | s11 | 2 | FAIL: "its document is written after" — R1 (working code with passing tests) not checked |
| B | s11 | 2 | FAIL: "Verifies R1 R5": passing checks only level order, not working code with passing tests |
| A | s16 | 2 | FAIL: "That level's document holds the fact marked as the work's" — R12 (user not asked for the fact) and R40 (requirement and verification complete) not checked |
| B | s16 | 2 | FAIL: "That level's document holds the fact marked as the work's" (Verifies R12 R40): no check the user wasn't asked for the fact, nor that the requirement and verification are complete |
| A | s18 | 2 | FAIL: "the second feature's record holds the decision" — R33 needs it recorded where the user can see it; not stated |
| A | s22 | 2 | FAIL: "Code starts, and by then each level has produced exactly one document" — R1 (working code with passing tests) not checked |
| B | s22 | 2 | FAIL: "Code starts" (Verifies R1): no check of working code with passing tests |
| A | m12 | 2 | FAIL: "later changed because the work read the user wrong" — counts a downstream symptom only when caught, not readings taken without asking (R15) |
| B | m12 | 2 | FAIL: "later changed because the work read the user wrong": counts a consequence, not whether a two-way reading was put to the user as a choice |

## Provenance

### Cells where the runs disagree (14: 1 PASS/FAIL, 13 PASS vs n/a or a missing row)

| Row | Rule | A | B | A's cell | B's cell |
|---|---|---|---|---|---|
| m12 | 1 | PASS | FAIL | PASS (D27 (Why)) | FAIL: "Approved levels later changed because the work read the user wrong: target zero". Not found in D1-D65, the notes, CLAUDE.md or the classification (D27's "Why" names misalignment as the main failure but sets no measure). |
| r15 | 4 | PASS | n/a | PASS | n/a |
| r32 | 4 | PASS | n/a | PASS | n/a |
| r33 | 4 | PASS | n/a | PASS | n/a |
| r36 | 4 | PASS | n/a | PASS | n/a |
| g: project | 4 | n/a | PASS | n/a | PASS |
| g: the user's to settle | 4 | PASS | n/a | PASS | n/a |
| preamble | 4 | PASS | n/a | PASS | n/a |
| s1 | 4 | PASS | n/a | PASS | n/a |
| s5 | 4 | PASS | n/a | PASS | n/a |
| s18 | 4 | PASS | n/a | PASS | n/a |
| s19 | 4 | PASS | n/a | PASS | n/a |
| s20 | 4 | PASS | n/a | PASS | n/a |
| s21 | 4 | PASS | n/a | PASS | n/a |

### Every FAIL (5)

| Run | Row | Rule | Cell |
|---|---|---|---|
| A | g: code starts | 1 | FAIL: "the first change to the project's code or tests for that feature" (no decision log entry defines it; notes l.21 record keeping it as "Reading I took", not agreed by the user, and the document doesn't mark it as the work's) |
| B | g: code starts | 1 | FAIL: "the first change to the project's code or tests for that feature". Not found in D1-D65 or the classification; the notes ("Write-in done") record keeping this definition as "Reading I took", not as something the user said or agreed, and the document doesn't mark it as the work's. |
| A | preamble | 1 | FAIL: "Acceptance tests, any levels a scenario starts from, and the rules a judge applies come with the scenario" and "Acceptance tests fail before the work and pass after it; no check relies only on tests written by the work being judged" (no source in D8, D47, D61 or the interview notes; not marked as the work's). Rest traced to D8, D47, notes l.36-39 |
| B | preamble | 1 | FAIL: "transcript analysis" (D8 lists "tests, Playwright, an LLM judge or a combination"; not found in the notes) and "Acceptance tests fail before the work and pass after it" (not found in D1-D65, the notes or CLAUDE.md). Rest is traced: runs under both hosts (notes "run-count sentence ... Craig's (0023)"; D47), scripted user (D8), checks come with the scenario (D64 rule 4). |
| B | m12 | 1 | FAIL: "Approved levels later changed because the work read the user wrong: target zero". Not found in D1-D65, the notes, CLAUDE.md or the classification (D27's "Why" names misalignment as the main failure but sets no measure). |

