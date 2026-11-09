# Open questions

Questions set aside because they belong to a later level ([decision 0009](decisions/0009-block-lower-level-questions.md)). Each is answered at its owning level, not before.

| Question | Owning level |
| --- | --- |
| Where the end-to-end sample project lives: a separate repo, or a fixture in this repo | Design |
| Where a feature's level artifacts (Outcome, Behaviour, Design, Slices) are stored | Design |
| The framework's form, for example a plugin for Claude Code and Codex | Design |
| Docs for people who install the framework, written for them rather than for those who build from a level's document ([decision 0037](decisions/0037-a-level-s-document-is-written-for-those-who-build-from-it.md)) | The level that owns packaging |
| Where the framework keeps the readability rules and the interview and playback instructions | Behaviour, Design |
| The Behaviour definition's line on found facts: only what users get today ([decision 0024](decisions/0024-where-found-facts-live.md)) | Behaviour |
| The Design definition's line on found facts: the code, data, services and interfaces the design builds on ([decision 0024](decisions/0024-where-found-facts-live.md)) | Design |
| The Slices definition's line on found facts: Design's plus how the project is built and tested ([decision 0024](decisions/0024-where-found-facts-live.md)) | Slices |
| How each level's review checks found facts against the project and statements against what the user said | Design |
| How the count of questions asked per level is kept ([decision 0026](decisions/0026-questions-per-level-are-tracked-not-targeted.md)) | Design |
| How many runs each scenario needs to pass. The user set 10 on 2026-10-27, then suggested 3 on 2026-11-07 ([decision 0050](decisions/0050-how-the-scenarios-run-is-deferred.md)) | The level that writes the tests |
| Whether the scenarios are plugin evals (`claude plugin eval`, following Anthropic's guidance for well-written plugin evals), and how a multi-turn scripted user is done, since plugin eval documents no simulated user ([decision 0050](decisions/0050-how-the-scenarios-run-is-deferred.md)) | The level that writes the tests |
| Whether the deterministic hook scripts are tested with pytest ([decision 0050](decisions/0050-how-the-scenarios-run-is-deferred.md)) | The level that writes the tests |
| How support for both Claude Code and Codex is shown without running every scenario under each ([decision 0050](decisions/0050-how-the-scenarios-run-is-deferred.md)) | The level that writes the tests |
| Nothing is guessed: a fact is looked up, a decision of the user's is asked, a decision of the work's is made by the work, a reading is asked, and anything the work can't settle one of those ways is put to the user. | Behaviour |
| Before the user approves a level that allows found facts, its review checks each found fact against the project, and a wrong fact is a finding. | Behaviour |
| Approving a level makes the user's decisions and answers in it agreed. | Behaviour |
| The work's decisions in an approved level stay the work's. | Behaviour |
| A decision holds only within its stated scope. | Behaviour |
| The next feature makes the same decision again, with the earlier one as its preferred default, unless an agreement or codified rule already covers the case. | Behaviour |
| No check relies only on tests written by the work being judged. | Behaviour |
| The framework enforces itself the same way whether the work runs under Claude Code or under Codex. | Design |
| Nothing is guessed. | Behaviour |
| When a choice between readings is put to the user: "in a message of its own, after the playback" (decision 0021, FF-14 A) | Behaviour |
| A plain answer that could be read more than one way when no playback follows it, such as an answer given after code starts. A plain answer gets no playback of its own (R7), and the choice comes after the playback (0021). Options: A. the choice goes in a message of its own straight away, "after the playback, when there is one"; B. such an answer gets a playback, and R7 covers only answers read one way | Behaviour |
