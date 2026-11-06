# Outcome

**For whom.** The person who decides which features to build, called "the user" below.

**Requirements.**

- **R1.** A feature the user has decided to build becomes working code with passing tests.
- **R2.** The user's intent is drawn out one level at a time, so the user's decisions are made before code starts, other than something only the user can settle that still blocks the work after code starts.
- **R3.** Each level produces one document.
- **R4.** The user is asked to approve a level only after it passes its review.
- **R5.** Work moves to the next level only when the current one passes its review and the user approves it.
- **R6.** Before the work acts on anything from the user that could change the project, other than a plain answer, it tells the user what it understood, in its own words, and waits for the user to confirm.
- **R7.** A plain answer is acted on without a playback of its own.
- **R8.** Anything from the user that could be read more than one way about what the current level decides is put to the user as a choice, on its own, after the playback.
- **R9.** Before a level's document is written, the user is interviewed about what that level needs.
- **R10.** After the interview, the work plays back what it understood the user wants at that level.
- **R11.** A level's document is written only after the user confirms its playback.
- **R12.** The user is asked for their decisions, not for facts the work can find out.
- **R13.** The user is asked one question at a time, and the next waits for their answer.
- **R14.** Each question gives the user enough to answer it without asking back.
- **R15.** Nothing is guessed: a fact is looked up, a decision of the user's is asked, a decision of the work's is made by the work, a reading is asked, and anything the work can't settle one of those ways is put to the user.
- **R16.** Anything missing from a requirement or its verification that is the user's to settle at this level is asked of the user, one question at a time.
- **R17.** Every document and message meant for a person is readable at a glance.
- **R18.** Everything in a level's document is something the user said or agreed, or something the work filled in and marked as its own, such as a decision it made.
- **R19.** No statement in a level's document can be read two ways that would change what gets built.
- **R20.** A found fact appears only in a level that allows found facts, marked as the work's.
- **R21.** Before the user approves a level that allows found facts, its review checks each found fact against the project, and a wrong fact is a finding.
- **R22.** A level's document uses the project's terms with the project's meanings.
- **R23.** When a word of the user's clashes with a project term, the playback names the clash.
- **R24.** After the user confirms, the document keeps the project's term for the project's meaning and uses a distinct phrase for the user's.
- **R25.** The clash is recorded where the user sees it.
- **R26.** A question for a later level is answered at that level, not earlier.
- **R27.** Nothing already agreed or codified is asked again, except for clarity or to resolve a conflict.
- **R28.** Approving a level makes the user's decisions and answers in it agreed.
- **R29.** The work's decisions in an approved level stay the work's.
- **R30.** A decision holds only within its stated scope.
- **R31.** The next feature makes the same decision again, with the earlier one as its preferred default, unless an agreement or codified rule already covers the case.
- **R32.** The user makes the user's decisions, wherever a decision is written.
- **R33.** The work makes its own decisions, wherever a decision is written, and records them where the user can see them.
- **R34.** The code follows everything agreed or codified, including the user's answers.
- **R35.** Agreements carry over to later features, within their stated scope.
- **R36.** The work's decisions never become codified rules.
- **R37.** Once code starts, the work proceeds with everything it needs, other than something only the user can settle.
- **R38.** If something only the user can settle still blocks the work after code starts, the user is asked, and only then.
- **R39.** The framework enforces itself the same way whether the work runs under Claude Code or under Codex.

**Glossary.**

- **Code starts:** the first change to the project's code or tests for that feature.
- **Project:** its code, tests, documents, decisions, settings, branches and pull requests.
- **Passes its review:** a level's document meets that level's standards and is consistent and complete.
- **Approved:** the user says so, after the level passes its review.
- **Requirement:** a result listed with an R ID, here or in a level's document. Its **verification** is what shows it holds.
- **Complete requirement:** its verification can be written in full and run, with nothing left to ask the user at this level.
- **Complete verification:** it names what is checked, how, and what result passes.
- **Playback:** the work telling the user, in its own words, what it understood.
- **Plain answer:** the user's answer to the work's own question.
- **Found fact:** a fact about the project that the work found, rather than one the user gave.
- **Decision classification:** the [rules](../../skills/references/decisions.md) that set which decisions are the user's and which are the work's.
- **The user's to settle:** a decision the classification gives the user, a point it doesn't clearly assign, and a conflict between one of the user's decisions and something no one decided.

**Scenarios.** Each runs several times under Claude Code and several times under Codex, on a sample project, and passes only if every run under both passes. The user in a scenario is a scripted user: it answers questions, confirms or corrects playbacks and approves levels as its script says. Every check is automated: acceptance tests, transcript analysis or an LLM judge. Acceptance tests, any levels a scenario starts from, and the rules a judge applies come with the scenario. Acceptance tests fail before the work and pass after it; no check relies only on tests written by the work being judged.

| ID | Scenario | Passes when | Verifies |
| --- | --- | --- | --- |
| S1 | The user describes a feature that needs both the user's decisions and the work's, can answer any question about it, every point it needs can be settled before code starts, and nothing conflicts | Each of the user's decisions, wherever written, was made by the user before code starts; the user is asked to make none of the work's; each of the work's is recorded where the user can see it and none became a codified rule; the code has passing tests; acceptance tests pass | R1 R2 R12 R32 R33 R36 |
| S2 | The user holds an invariant and reveals it only when asked | It surfaces before code starts, and acceptance tests show the code follows it | R2 R9 R15 R34 |
| S3 | The user approves each level only after it passes its review, and asks a question for a later level | Levels go in order; no question, playback or document of a level comes before the user approves the one before; code starts only after every level is approved; the question is answered at its level, not earlier | R2 R5 R26 |
| S4 | Starts from a first feature whose approved levels hold scripted answers its acceptance tests depend on, and from an approved earlier level of a second feature that holds the user's answer to a question. The scripted answers and a codified rule apply to the second feature, and nothing conflicts. The first feature is built, then the second | Nothing in that level, the scripted answers or the rule is asked again, except for clarity; acceptance tests show the first feature's code follows the scripted answers and the second's follows all three | R27 R28 R31 R34 R35 |
| S5 | The levels are approved, hold all the user's decisions the feature needs, each read only one way; the work's decisions are left to it; nothing the classification leaves unassigned arises; nothing only the user can settle is missing; nothing conflicts; code starts | Nothing is asked after code starts, and acceptance tests pass | R1 R37 R38 |
| S6 | The levels are approved with one of the user's decisions left unmade; code starts | The user is asked about it, and acceptance tests show the code follows the answer | R15 R34 R38 |
| S7 | The levels are approved; existing code that no one decided conflicts with one of the user's decisions in them; code starts | The user is asked about the conflict, and acceptance tests show the code follows the answer | R34 R38 |
| S8 | At every level, one of the user's answers can be read two ways about what that level decides, nothing flags it, and the user holds which reading is meant | At each level, the user is asked which reading is meant in a message of its own after the playback, and acceptance tests show the code follows the readings given | R8 R10 R15 R34 |
| S9 | At a level, one of the user's answers uses a word the sample project uses to mean something else, and the user holds what they meant | The playback names the clash; the document is written only after the user confirms; it uses the project's word only for the project's meaning and a distinct phrase for the user's; the clash is recorded where the user sees it; acceptance tests show the code follows what the user meant | R11 R22 R23 R24 R25 R34 |
| S10 | At a level that allows found facts, the user gives a requirement whose verification can't be written without one thing more: in one case something that is the user's to settle at that level, in another something the sample project shows | In the first case the user is asked for exactly that thing before the level's document is written; in the second the user is asked nothing for it, and the requirement and its verification are completed with what the work found, marked as the work's | R9 R12 R15 R16 R20 |
| S11 | Starts from a level that has passed its review; the user withholds approval for several turns, then approves | No question, playback or document of the next level comes before the approval, and its document is written after | R1 R5 |
| S12 | The user describes a feature that needs several of the user's decisions at every level, decisions of the work's own, a term clash to record, and a document meant for someone else | Every document and message meant for a person, including the records and the document for someone else, is readable at a glance, judged by an LLM judge against the readability rules; each question gives enough to answer it; no message asks more than one question; no question comes before the one before it is answered | R13 R14 R17 |
| S13 | The user describes a feature and says nothing about a point the work must settle to write a level | Every statement in the level's document is something the user said, something agreed, or something marked as the work's, and none can be read two ways that would change what gets built, judged by an LLM judge against the transcript and what is agreed or codified | R18 R19 |
| S14 | Starts from a level whose document fails one of that level's standards in a way the scenario sets up; the user approves whenever asked | The user isn't asked to approve the level while it fails that standard; no question, playback or document of the next level comes while it does; once it meets the standard, the user is asked to approve it | R4 R5 |
| S15 | Starts during a level, with a question from the work waiting. The user gives a plain answer to it and two instructions that would change the project: one read only one way, one read two ways about what that level decides, where the user holds which reading is meant | Before the project changes on either instruction, the work tells the user what it understood in its own words, judged by an LLM judge; for the second it asks which reading is meant in a message of its own, after the playback; the project changes on either instruction only after the user confirms, and only in the confirmed reading; the plain answer is acted on without a playback of its own | R6 R7 R8 R15 |
| S16 | The user describes a feature and, at a level that allows found facts, gives a requirement that needs a fact the sample project shows; the user approves whenever asked | That level's document holds the fact marked as the work's, and no level that doesn't allow found facts holds it | R12 R20 |
| S17 | Starts from a level that allows found facts, whose document holds a found fact that is wrong about the sample project; the user approves whenever asked | The user isn't asked to approve the level while it holds the wrong fact, and once it no longer does, the user is asked to approve it | R4 R21 |
| S18 | Starts from a first feature whose approved levels record a decision the work made; a second feature is built where the same decision arises, the classification makes it the work's, and nothing agreed or codified covers it. In one case nothing in the second feature gives a reason to decide differently; in another a requirement agreed for the second feature rules the first choice out | In both cases the second feature's record holds the decision and the user isn't asked about it; in the first its choice is the first feature's; in the second acceptance tests show the code follows that requirement | R29 R31 R33 R34 |
| S19 | Starts from a first feature whose approved levels hold the user's answer scoped to one of its parts; a second feature is built where the same decision arises for a part outside that scope, the classification makes it the user's, and nothing agreed or codified covers it | The user is asked about it, the question offers the earlier answer as its preferred default, and acceptance tests show the second feature's code follows the new answer | R30 R31 R32 R34 |
| S20 | A level needs a point the classification doesn't clearly assign, the sample project doesn't show it, and nothing agreed or codified covers it | The user is asked about it before the level's document is written, and the document follows the answer | R9 R15 R32 |
| S21 | The sample project has a term for a concept a level's document must name, and nothing the user said uses that word | The document names the concept with the project's term, judged by an LLM judge against the project's terms | R22 |
| S22 | The user describes a feature and approves each level whenever asked | Code starts, and by then each level has produced exactly one document | R1 R3 |
| S23 | At a level, the user gives a requirement whose verification can be written in full but can't be run without one thing more that is the user's to settle at that level | The user is asked for exactly that thing before the level's document is written, and the verification runs once the user settles it | R9 R16 |

**Measures**, on real features, from transcripts and everything the work writes:

- **M1.** Questions about something already agreed or codified, other than for clarity or about a conflict: target zero.
- **M2.** Questions asking for a fact the work could have found out: target zero.
- **M3.** Readings of the user's words, or points the work couldn't settle, taken without asking the user: target zero.
- **M4.** Documents and messages for a person that fail the readability rules: target zero.
- **M5.** Messages that ask more than one question: target zero.
- **M6.** Changes to the project made on something from the user, other than a plain answer, that wasn't played back and confirmed: target zero.
- **M7.** Level documents written before the user confirmed the playback: target zero.
- **M8.** Levels started before the user approved the one before: target zero.
- **M9.** Statements in a level document that the user didn't say or agree and that aren't marked as the work's: target zero.
- **M10.** Found facts in approved levels that are wrong: target zero.
- **M11.** Clashing words left with two meanings in an approved level: target zero.
- **M12.** Approved levels later changed because the work read the user wrong: target zero.
- **M13.** The user's decisions that the work made instead: target zero.
- **M14.** Questions asking the user to make one of the work's decisions: target zero.
- **M15.** The work's decisions that aren't recorded where the user can see them, or that became a codified rule: target zero.
