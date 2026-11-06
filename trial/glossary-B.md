# Glossary review grid (judge B)

"Project" for rule 6 = README.md and files under skills/ and hooks/. Decisions are cited from docs/decisions.md (Dn); interview notes = trial/interview-answers.md.

| Row | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| G: Code starts | PASS (the approved level 1 Outcome used "code starts", D15/D19; interview notes say the "code starts" definition was kept) | PASS | PASS | PASS | PASS | n/a (term not used in README, skills/ or hooks/) |
| G: Project | PASS (D27 / interview notes Q1: "covers code, tests, documents, decisions, settings, branches and PRs") | PASS | PASS | PASS | PASS | PASS (skills/references/decisions.md "reaches outside the project"; hooks/prompts/goals.md "change the project") |
| G: Passes its review | PASS (D52, user: "matches the standards to complete the level and that the artifact is consistent and complete") | PASS | PASS | PASS | PASS | PASS (hooks/prompts/goals.md "passes its review"; skills/references/outcome.md "Reviews": standards = structure checks and four reviews, no clash) |
| G: Approved | PASS (D26: "Approval is the user saying so") | PASS | FAIL: "after the level passes its review" (sets the ordering rule of D26/D36, review before approval, inside the definition) | PASS | PASS | FAIL: "after the level passes its review" (project also uses approval for decisions, with no level review: hooks/prompts/goals.md "every decision needs approval"; hooks/prompts/stop-check.md "Asking approval of a decision") |
| G: Requirement | PASS (D56 visible R IDs; D33/FF-23 requirement and verification) | FAIL: "here or in a level's document" (the glossary lists no R IDs; "here" has no referent in a glossary shared by every level, docs/spec/glossary.md) | PASS | PASS | PASS | PASS (skills/references/outcome.md "requirements ... as results the user can observe", "each with an automated verification") |
| G: Complete requirement | FAIL: "at this level" (D33 and interview notes FF-23 say only "with nothing left to ask the user"; the qualifier is not the user's and not marked as the work's) | FAIL: "at this level" (the glossary is shared by every level; no level is named, so "this level" has no referent) | PASS | PASS | PASS | n/a (term not used in README, skills/ or hooks/) |
| G: Complete verification | PASS (D33 / FF-23 word for word) | PASS | PASS | PASS | PASS | n/a (term not used in README, skills/ or hooks/) |
| G: Playback | PASS (D27 "plays back, in its own words, what it understood") | PASS | PASS | PASS | PASS | PASS (hooks/prompts/goals.md "play back what you understood") |
| G: Plain answer | PASS (D27 "A plain answer to the work's own question") | PASS | PASS | PASS | PASS | n/a (term not used in README, skills/ or hooks/) |
| G: Found fact | PASS (D59, user chose FF-49 A word for word; D30) | PASS | FAIL: "so every level uses project terms" (sets a rule for levels, not a meaning) | PASS | PASS | n/a (project says "fact the work looked up", skills/references/outcome-reviews/provenance.md; "found fact" not used) |
| G: Decision classification | PASS (D42 single source; D65 approved "the decision classification") | PASS | PASS | PASS | PASS | PASS (skills/references/outcome-reviews/provenance.md "the decision classification", linking decisions.md) |
| G: The user's to settle | FAIL: "a conflict between one of the user's decisions and something no one decided" (the term and this scope are not said or agreed and not marked as the work's; skills/references/decisions.md "Always" also gives the user "two current decisions of the user's conflict", which the entry leaves out) | PASS | PASS | PASS | PASS | n/a (term not used in README, skills/ or hooks/) |

FAIL cells: 7
