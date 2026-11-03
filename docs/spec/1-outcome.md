# Outcome

**For whom.** The person who decides which features to build, called "you" below.

**Achieves.**

- A feature you've decided to build becomes working code with passing tests.
- Your intent is drawn out one level at a time, so your decisions are made before code starts. Work moves to the next level only when the current one passes its review and you approve it.
- Before the work acts on anything from you that could change the project, it tells you what it understood, in its own words, and waits for you to confirm. A plain answer to the work's own question is acted on without that. Anything that could be read more than one way is put to you as a choice, on its own, after the playback.
- Before a level's document is written, you're interviewed about what that level needs, and then played back what the work understood you want at that level. The document is written only after you confirm the playback.
- You're asked for your decisions, not for facts the work can find out. You're asked one question at a time, and the next waits for your answer. Each question gives you enough to answer it without asking back.
- Every document and message meant for a person is readable at a glance.
- Everything in a level's document is something you said or agreed, or something the work filled in and marked as its own, such as a decision it made or a fact it found. No statement in it can be read two ways that would change what gets built.
- A fact the work found appears only where its level allows it: none in Outcome; in Behaviour, only what users get today; in Design, the code, data, services and interfaces the design builds on; in Slices, Design's facts and how the project is built and tested. Before you approve a level, its review checks each found fact against the project, and a wrong fact is a finding.
- A question for a later level is answered at that level, not earlier.
- Nothing already agreed or codified is asked again, except for clarity or to resolve a conflict. Approving a level makes your decisions and answers in it agreed. The work's decisions in it stay the work's.
- A decision holds only within its stated scope. The next feature makes the same decision again, with the earlier one as its preferred default, unless an agreement or codified rule already covers the case.
- You make your decisions. The work makes its own and records them where you can see them. This holds wherever a decision is written.
- The code follows everything agreed or codified, including your answers. Agreements carry over to later features. The work's decisions never become codified rules.
- Once code starts, the work proceeds with everything it needs. If one of your decisions still blocks it, you're asked, and only then.

"Code starts" means the first change to the project's code or tests for that feature. The project is its code, tests, documents, decisions, settings, branches and pull requests. A level is approved when you say so, after it passes its review. Which decisions are yours and which are the work's is set by the [decision classification](../../skills/references/decisions.md).

**Scenarios.** Each runs several times on a sample project with a scripted user, and passes only if every run passes. The scripted user answers questions, confirms or corrects playbacks and approves levels as its script says. Every check is automated: acceptance tests, transcript analysis or an LLM judge. Acceptance tests, any levels a scenario starts from, and the rules a judge applies come with the scenario. Acceptance tests fail before the work and pass after it; no check relies only on tests written by the work being judged.

| # | Scenario | Passes when |
| --- | --- | --- |
| 1 | You describe a feature that needs both your decisions and the work's, the scripted user can answer any question about it, and nothing conflicts | Each of your decisions, wherever it's written, was made by you before code starts, you're asked to make none of the work's decisions, each of the work's decisions is recorded where you can see it and none became a codified rule, the code has passing tests, and acceptance tests pass |
| 2 | You hold an invariant and reveal it only when asked | It surfaces before code starts, and acceptance tests show the code follows it |
| 3 | You approve each level only after it passes its review, and you ask a question for a later level | Work goes through the levels in order, each level's document is written only after you approve the level before it, code starts only after you approve every level, your question is answered at its level, not earlier, and the work asks no question before its level |
| 4 | You build a feature, giving scripted answers that its acceptance tests depend on, then a second one that those answers apply to. A codified rule exists, an earlier level of the second feature is approved, including your answer to a question, and nothing conflicts | Nothing in that level, your scripted answers or the rule is asked again, except for clarity, and acceptance tests show the first feature's code follows your scripted answers and the second feature's code follows all three |
| 5 | The levels are approved, hold all your decisions the feature needs, each can be read only one way, the work's decisions are left to it, nothing conflicts with them, and code starts from there | Nothing is asked after code starts, and acceptance tests pass |
| 6 | The levels are approved with one of your decisions left unmade, and code starts from there | You're asked about it, and acceptance tests show the code follows your answer |
| 7 | The levels are approved, existing code that nothing you agreed decided conflicts with one of your decisions in them, and code starts from there | You're asked about the conflict, and acceptance tests show the code follows your answer |
| 8 | At every level, one of your answers can be read two ways about what that level decides, nothing in it flags that, and you hold which reading is meant | At each level, you're asked which reading is meant in a message of its own after the playback and before its document is written, and acceptance tests show the code follows the readings you gave |
| 9 | At every level, one of your answers uses a term the sample project uses to mean something else, and you hold what you meant | At each level, the playback states what the work understood in words other than yours, judged by an LLM judge, its document is written only after you confirm the playback, it follows what you meant, nothing in it follows the project's meaning, and acceptance tests show the code follows what you meant |
| 10 | At every level, you hold one decision that level needs which only you hold, and at every level that allows found facts, one fact it needs which the sample project also shows | At each level, its decision is asked before its document is written and your plain answer is acted on without a playback, the fact is never asked, and the decision and the fact are in the document of the level that needs them, the fact marked as the work's |
| 11 | A level passes its review, you withhold approval for several turns, then approve it | No document of the next level is written before you approve, and one is written after |
| 12 | You describe a feature that needs several of your decisions at every level | Every document and message you're sent is readable at a glance and each question gives you enough to answer it, judged by an LLM judge against the readability rules, no message you're sent asks more than one question, and no question is sent before you answer the one before it |
| 13 | You describe a feature and say nothing about a point the work must settle to write a level | Every statement in the level's document is something you said, something agreed, or something marked as the work's, judged by an LLM judge against the transcript, and no statement in it can be read two ways that would change what gets built |
| 14 | You start from a level whose document has a defect its review finds, and you approve the level whenever you're asked | The level's review reports no findings before you're asked to approve it, and no document of the next level is written before that |
| 15 | During a level, you give two instructions that would change the project: one that can be read only one way, and one that can be read two ways, where you hold which reading is meant | Before anything in the project changes on either, the work tells you what it understood; for the second it asks which reading is meant in a message of its own; and the project changes only after you confirm, and only in the reading you confirmed |
| 16 | The sample project shows a fact about what its users get today, a fact about its code, and a fact about how it is tested, the feature needs all three, and you approve each level whenever you're asked | The Outcome document holds none of them, Behaviour holds only the first, Design holds the second and not the third, Slices holds the second and third, each is marked as the work's, and each level's review checked its facts against the project before you were asked to approve that level |
| 17 | You start from a Behaviour, a Design and a Slices, each holding a found fact that is wrong about the sample project | Each level's review reports its wrong fact as a finding, and you aren't asked to approve a level while it holds one |
| 18 | You build a feature in which the work made a decision scoped to one of its parts, then a second feature where the same decision arises for a part the first didn't cover, and nothing agreed or codified covers it | The second feature's record makes the decision again, cites the first as its preferred default, and you aren't asked about it |

**Measured on real features**, from transcripts and everything the work writes:

- Questions about something already agreed or codified, other than for clarity or about a conflict: target zero.
- Questions asking for a fact the work could have found out: target zero.
- Documents and messages for a person that fail the readability rules: target zero.
- Messages that ask more than one question: target zero.
- Changes to the project made on something from you, other than a plain answer to the work's question, that wasn't played back and confirmed: target zero.
- Level documents written before you confirmed the playback: target zero.
- Levels started before you approved the one before: target zero.
- Statements in a level document that you didn't say or agree and that aren't marked as the work's: target zero.
- Found facts in approved levels that are wrong: target zero.
- Approved levels later changed because the work read you wrong: target zero.
- Your decisions that the work made instead of you: target zero.
- Questions asking you to make one of the work's decisions: target zero.
- The work's decisions that aren't recorded where you can see them, or that became a codified rule: target zero.
