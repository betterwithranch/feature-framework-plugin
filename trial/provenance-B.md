# Provenance review: docs/spec/1-outcome.md

Sources read: provenance.md (rules), 1-outcome.md, docs/decisions.md (D1-D65), skills/references/decisions.md, CLAUDE.md, scratchpad/trial/interview-answers.md. The full conversation was not available; a statement counts as said or agreed only where one of these shows it.

Nothing in the document is marked as the work's, so rule 2 is n/a on every row. No row records a clash between a user's word and a project term, and the sources name no such clash, so rule 5 is n/a on every row. Rule 4 is marked only on rows that use a project term (a name for something in the project) as that term.

| Row | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| R1 | PASS (D3, D5, D26) | n/a | PASS | n/a | n/a |
| R2 | PASS (D3, D36) | n/a | PASS | n/a | n/a |
| R3 | PASS (D26 "Each level produces its own document only") | n/a | PASS | n/a | n/a |
| R4 | PASS (D26, D30) | n/a | PASS | n/a | n/a |
| R5 | PASS (D26, D36) | n/a | PASS | n/a | n/a |
| R6 | PASS (D27; notes Q1) | n/a | PASS | n/a | n/a |
| R7 | PASS (D27) | n/a | PASS | n/a | n/a |
| R8 | PASS (D27; current-level limit from D9) | n/a | PASS | n/a | n/a |
| R9 | PASS (D27) | n/a | PASS | n/a | n/a |
| R10 | PASS (D27) | n/a | PASS | n/a | n/a |
| R11 | PASS (D27) | n/a | PASS | n/a | n/a |
| R12 | PASS (D27 "asks only for decisions") | n/a | PASS | n/a | n/a |
| R13 | PASS (D27, D29) | n/a | PASS | n/a | n/a |
| R14 | PASS (D29) | n/a | PASS | n/a | n/a |
| R15 | PASS (D34; notes FF-20; classification "The work decides") | n/a | PASS | n/a | n/a |
| R16 | PASS (D33) | n/a | PASS | n/a | n/a |
| R17 | PASS (D29) | n/a | PASS | n/a | n/a |
| R18 | PASS (D27) | n/a | PASS | n/a | n/a |
| R19 | PASS (D27) | n/a | PASS | n/a | n/a |
| R20 | PASS (D30; notes Q3/Q3b) | n/a | PASS | n/a | n/a |
| R21 | PASS (D30) | n/a | PASS | n/a | n/a |
| R22 | PASS (D34) | n/a | PASS | n/a | n/a |
| R23 | PASS (D34; notes FF-21) | n/a | PASS | n/a | n/a |
| R24 | PASS (D34) | n/a | PASS | n/a | n/a |
| R25 | PASS (D34) | n/a | PASS | n/a | n/a |
| R26 | PASS (D9) | n/a | PASS | n/a | n/a |
| R27 | PASS (D26, D6) | n/a | PASS | n/a | n/a |
| R28 | PASS (D26) | n/a | PASS | n/a | n/a |
| R29 | PASS (D26) | n/a | PASS | n/a | n/a |
| R30 | PASS (D31) | n/a | PASS | n/a | n/a |
| R31 | PASS (D31; notes Q5) | n/a | PASS | n/a | n/a |
| R32 | PASS (classification "The user decides"; D42) | n/a | PASS | n/a | n/a |
| R33 | PASS (classification "The work decides"; D42) | n/a | PASS | n/a | n/a |
| R34 | PASS (D26, D6; CLAUDE.md "Follow hooks/prompts/goals.md") | n/a | PASS | n/a | n/a |
| R35 | PASS (D2, D31) | n/a | PASS | n/a | n/a |
| R36 | PASS (classification "Always"; D42) | n/a | PASS | n/a | n/a |
| R37 | PASS (D5; CLAUDE.md "ask only when blocked") | n/a | PASS | n/a | n/a |
| R38 | PASS (CLAUDE.md "ask only when blocked by a decision no one has made or a conflict") | n/a | PASS | n/a | n/a |
| R39 | PASS (D47) | n/a | PASS | PASS ("Claude Code", "Codex" used as named in D47) | n/a |
| R40 | PASS (D33) | n/a | PASS | n/a | n/a |
| G: Code starts | FAIL: "the first change to the project's code or tests for that feature". Not found in D1-D65 or the classification; the notes ("Write-in done") record keeping this definition as "Reading I took", not as something the user said or agreed, and the document doesn't mark it as the work's. | n/a | PASS | n/a | n/a |
| G: Project | PASS (D27 "The project is its code, tests, documents, decisions, settings, branches and pull requests") | n/a | PASS | PASS | n/a |
| G: Passes its review | PASS (D52) | n/a | PASS | n/a | n/a |
| G: Approved | PASS (D26 "Approval is the user saying so") | n/a | PASS | n/a | n/a |
| G: Requirement | PASS (D56, D33) | n/a | PASS | n/a | n/a |
| G: Complete requirement | PASS (D33; notes FF-23) | n/a | PASS | n/a | n/a |
| G: Complete verification | PASS (D33; notes FF-23) | n/a | PASS | n/a | n/a |
| G: Playback | PASS (D27) | n/a | PASS | n/a | n/a |
| G: Plain answer | PASS (D27; notes Q1) | n/a | PASS | n/a | n/a |
| G: Found fact | PASS (D59, D30) | n/a | PASS | PASS (states rule 4 itself, per D59) | n/a |
| G: Decision classification | PASS (D42) | n/a | PASS (file location comes from D20/D42, not a lookup) | PASS | n/a |
| G: The user's to settle | PASS (classification "The user decides", "Always") | n/a | PASS | n/a | n/a |
| Preamble | FAIL: "transcript analysis" (D8 lists "tests, Playwright, an LLM judge or a combination"; not found in the notes) and "Acceptance tests fail before the work and pass after it" (not found in D1-D65, the notes or CLAUDE.md). Rest is traced: runs under both hosts (notes "run-count sentence ... Craig's (0023)"; D47), scripted user (D8), checks come with the scenario (D64 rule 4). | n/a | PASS | n/a | n/a |
| S1 | PASS (D42, classification, D5) | n/a | PASS | n/a | n/a |
| S2 | PASS (D3 invariants; D27) | n/a | PASS | n/a | n/a |
| S3 | PASS (D26, D9) | n/a | PASS | n/a | n/a |
| S4 | PASS (D26, D31; notes round 1 finding 7) | n/a | PASS | n/a | n/a |
| S5 | PASS (CLAUDE.md "ask only when blocked"; D5) | n/a | PASS | n/a | n/a |
| S6 | PASS (CLAUDE.md "ask only when blocked") | n/a | PASS | n/a | n/a |
| S7 | PASS (classification "Always", conflict with something no one decided) | n/a | PASS | n/a | n/a |
| S8 | PASS (notes FF-20 "scenario 8 approved"; D27) | n/a | PASS | n/a | n/a |
| S9 | PASS (notes FF-21; D34) | n/a | PASS | n/a | n/a |
| S10 | PASS (notes FF-22, round 1 findings 3-4; D33, D30) | n/a | PASS | n/a | n/a |
| S11 | PASS (D26; notes "scenarios 11 onward" relayed) | n/a | PASS | n/a | n/a |
| S12 | PASS (D29) | n/a | PASS | n/a | n/a |
| S13 | PASS (D27) | n/a | PASS | n/a | n/a |
| S14 | PASS (D26, D52; notes round 5 "scenario 14 ... aligned to 0012/0026") | n/a | PASS | n/a | n/a |
| S15 | PASS (D27) | n/a | PASS | n/a | n/a |
| S16 | PASS (D30; notes Craig's rule, scenario 16 reworded) | n/a | PASS | n/a | n/a |
| S17 | PASS (D30) | n/a | PASS | n/a | n/a |
| S18 | PASS (D31, D26) | n/a | PASS | n/a | n/a |
| S19 | PASS (D31; notes round 1 finding 1) | n/a | PASS | n/a | n/a |
| S20 | PASS (classification "When it's unclear which list ... the user decides"; D27) | n/a | PASS | n/a | n/a |
| S21 | PASS (D34, D59; notes round 1 finding 2) | n/a | PASS | n/a | n/a |
| S22 | PASS (D26; notes round 1 finding 5) | n/a | PASS | n/a | n/a |
| S23 | PASS (D33; notes "scenario 23 added ... 0033") | n/a | PASS | n/a | n/a |
| M1 | PASS (D26) | n/a | PASS | n/a | n/a |
| M2 | PASS (D27) | n/a | PASS | n/a | n/a |
| M3 | PASS (D34, D19) | n/a | PASS | n/a | n/a |
| M4 | PASS (D29) | n/a | PASS | n/a | n/a |
| M5 | PASS (D29) | n/a | PASS | n/a | n/a |
| M6 | PASS (D27) | n/a | PASS | n/a | n/a |
| M7 | PASS (D27) | n/a | PASS | n/a | n/a |
| M8 | PASS (D26) | n/a | PASS | n/a | n/a |
| M9 | PASS (D27) | n/a | PASS | n/a | n/a |
| M10 | PASS (notes Q3 "found facts in approved levels that are wrong: target zero"; D30) | n/a | PASS | n/a | n/a |
| M11 | PASS (D34) | n/a | PASS | n/a | n/a |
| M12 | FAIL: "Approved levels later changed because the work read the user wrong: target zero". Not found in D1-D65, the notes, CLAUDE.md or the classification (D27's "Why" names misalignment as the main failure but sets no measure). | n/a | PASS | n/a | n/a |
| M13 | PASS (classification; D42) | n/a | PASS | n/a | n/a |
| M14 | PASS (classification; D42) | n/a | PASS | n/a | n/a |
| M15 | PASS (classification "Always"; D42) | n/a | PASS | n/a | n/a |
