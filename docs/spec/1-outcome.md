# Outcome

**For whom.** The user.

**Requirements.**

- **R1.** A feature the user has decided to build becomes working code with passing tests.
- **R2.** The user's intent is drawn out one level at a time, so the user's decisions are made before code starts.
- **R3.** Each level produces one document.
- **R4.** The user is asked to approve a level only after it passes its review.
- **R5.** Work moves to the next level only when the current one passes its review and the user approves it.
- **R6.** Before the work acts on something from the user that could change the project, other than a plain answer, it plays back what it understood and waits for the user to confirm.
- **R7.** A plain answer is acted on without a playback of its own.
- **R8.** Anything from the user that could be read more than one way is put to the user as a choice.
- **R9.** Before a level's document is written, the user is interviewed about what that level needs.
- **R10.** After the interview, the work plays back what it understood the user wants at that level.
- **R11.** A level's document is written only after the user confirms its playback.
- **R12.** The user is asked for their decisions, not for facts the work can find out.
- **R13.** The user is asked one question at a time, and the next waits for their answer.
- **R14.** Each question gives the user enough to answer it without asking back.
- **R15.** Anything missing from a requirement or its verification that is the user's to settle at this level is asked of the user, one question at a time.
- **R16.** Every document and message meant for a person is readable at a glance.
- **R17.** Everything in a level's document is something the user said or agreed, or something the work filled in and marked as its own, such as a decision it made.
- **R18.** No statement in a level's document can be read more than one way that would change what gets built.
- **R19.** A found fact appears only in a level that allows found facts, marked as the work's.
- **R20.** A level's document uses the project's terms with the project's meanings.
- **R21.** When a word of the user's clashes with a project term, the playback names the clash.
- **R22.** After the user confirms, the document keeps the project's term for the project's meaning and uses a distinct phrase for the user's.
- **R23.** The clash is recorded where the user can see it.
- **R24.** A question for a later level is answered at that level, not earlier.
- **R25.** Something already agreed or codified is asked again only for clarity or to resolve a conflict.
- **R26.** The user makes the user's decisions, wherever a decision is written.
- **R27.** The work makes its own decisions, wherever a decision is written, and records them where the user can see them.
- **R28.** The code follows everything agreed or codified, including the user's answers.
- **R29.** Agreements carry over to later features, within their stated scope.
- **R30.** The work's decisions never become codified rules.
- **R31.** Once code starts, the work proceeds with what it needs, other than something that is the user's to settle.
- **R32.** If something that is the user's to settle still blocks the work after code starts, the user is asked, and only then.
- **R33.** Each requirement in a level's document is complete, and so is its verification.

**Glossary.** Terms are used as the project's [glossary](glossary.md) defines them.

**Scenarios.** Each runs on a sample project. *In a scenario, the user describes a feature, answers the work's questions, confirms its playbacks and approves its levels when asked, and holds the answers its checks expect, except where the scenario says otherwise.* Acceptance tests and any approved levels a scenario starts from come with the scenario. The Verifies column and the requirement IDs a measure cites are the work's, and so are words in italics anywhere in this document.

| ID | Scenario | Passes when | Verifies |
| --- | --- | --- | --- |
| S1 | The user describes a feature | The code has passing tests, and acceptance tests pass | R1 |
| S2 | The user holds an invariant and reveals it only when asked | It surfaces before code starts, and acceptance tests show the code follows it | R2 R28 |
| S3 | The user agrees partially *to the first level*, then asks a question for a later level*; the first level's document fails its review once in a way the scenario sets up, then passes, and the user then approves it* | Work goes through the levels in order, moves on from a level only after it passes its review and the user approves it, code starts only after every level is approved, the question is answered at its level, not earlier, and the work asks no question before its level | R2 R5 R24 |
| S4 | A second feature follows one whose decisions the user agreed*, scoped to cover the second feature*, a codified rule exists, and an earlier level of this feature is approved, including the user's answer to a question*; nothing conflicts* | They are asked again only for clarity, and acceptance tests show the code follows all three | R25 R28 R29 |
| S5 | The levels are approved and cover everything the feature needs, *no existing code conflicts with them,* and code starts from there | Nothing is asked after code starts, and acceptance tests pass | R1 R31 R32 |
| S6 | The levels are approved with one of the user's decisions left unmade, and code starts from there | The user is asked about it, and acceptance tests show the code follows the answer | R28 R31 R32 |
| S7 | The levels are approved, the existing code *that no one decided* conflicts with *one of the user's decisions in* them, and code starts from there | The user is asked about the conflict, and acceptance tests show the code follows the answer | R28 R32 |
| S8 | At every level, one of the user's answers could be read more than one way *about what that level decides*, nothing flags it, and the user holds which reading is meant | At each level, *the user is interviewed about what that level needs before its document is written; after the interview the work plays back what it understood the user wants at that level; and* the user is asked which reading is meant, and acceptance tests show the code follows the readings given | R8 R9 R10 R28 |
| S9 | At a level, one of the user's answers uses a word the sample project uses to mean something else, and the user holds what they meant | The playback names the clash; the document is written only after the user confirms; it uses the project's term only for the project's meaning and a distinct phrase for the user's; the clash is recorded where the user can see it; acceptance tests show the code follows what the user meant | R11 R20 R21 R22 R23 R28 |
| S10 | At a level that allows found facts, the user gives a requirement whose verification can't be written without one thing more: in one case something that is the user's to settle at that level, in another something the sample project shows | In the first case the user is asked for exactly that thing before the level's document is written; in the second the user is asked nothing for it, and the requirement and its verification are completed with what the work found, marked as the work's | R9 R12 R15 R19 R33 |
| S11 | Starts from a level that has passed its review; the user withholds approval for several turns, then approves | No question, playback or document of the next level comes before the approval, and its document is written after | R5 |
| S12 | *The user describes a feature that needs several of the user's decisions at every level, decisions of the work's own, a term clash to record, a document meant for someone else, and a requirement missing two things that are the user's to settle* | *Every document and message meant for a person, including the records and the document for someone else, is readable at a glance; each question gives enough to answer it; each of the two missing things is asked; no message asks more than one question; no question comes before the one before it is answered* | R13 R14 R15 R16 |
| S13 | *The user describes a feature and says nothing about a point the work must settle to write a level* | *Every statement in the level's document is something the user said, something agreed, or something marked as the work's, and none can be read more than one way that would change what gets built, judged against the transcript and what is agreed or codified* | R17 R18 |
| S14 | *Starts from a level whose document fails its review in one of three ways the scenario sets up, one per case: it fails one of that level's standards, two of its statements contradict, or one of its requirements is incomplete; the user approves whenever asked* | *In each case the user isn't asked to approve the level while it fails its review; no question, playback or document of the next level comes while it does; once it passes, the user is asked to approve it* | R4 R5 |
| S15 | *Starts during a level, with a question from the work waiting. The user gives a plain answer to it and two instructions that would change the project: one read only one way, one that could be read more than one way about what that level decides, where the user holds which reading is meant* | *Before the project changes on either instruction, the work plays back what it understood; for the second it asks which reading is meant; the project changes on either instruction only after the user confirms, and only in the confirmed reading; the plain answer is acted on without a playback of its own* | R6 R7 R8 |
| S16 | *Starts from a first feature whose approved levels record a decision the work made; a second feature is built where the same decision arises as one of the work's decisions, and nothing agreed or codified covers it* | *The user isn't asked about the decision, and the decision is recorded where the user can see it* | R27 |
| S17 | *Starts from a first feature whose approved levels hold the user's answer scoped to one of its parts; a second feature is built where the same decision arises as one of the user's decisions for a part outside that scope, nothing agreed or codified covers it* | *The user is asked about it, and acceptance tests show the second feature's code follows the new answer* | R26 R28 R29 |
| S18 | *The user describes a feature and approves each level whenever asked* | *Each level produces exactly one document, in which each requirement is complete and so is its verification; code starts, the code has passing tests, and acceptance tests pass* | R1 R3 R33 |
| S19 | *The user describes a feature and, at a level that allows found facts, gives a requirement that needs a fact the sample project shows; the user approves whenever asked* | *The user is asked nothing for the fact; that level's document holds it marked as the work's, and the requirement and its verification are complete; no level that doesn't allow found facts holds it* | R12 R19 R33 |
| S20 | *The sample project has a term for a concept a level's document must name, and nothing the user said uses that word* | *The document names the concept with the project's term, with the project's meaning* | R20 |

**Measures**, on real features, from transcripts and the code:

- **M1.** Questions about something already agreed or codified, other than for clarity or about a conflict (R25): target zero.
- **M2.** *The user's decisions that the work made instead (R26): target zero.*
- **M3.** *The work's decisions that aren't recorded where the user can see them, or that became a codified rule (R27 R30): target zero.*
- **M4.** Times the user is asked after code starts because of one of the user's decisions that no one made: counted for each feature as planning misses. It's not a pass bar.
