# Outcome

**For whom.** The person who decides which features to build and approves each level, called "the user" below.

**Requirements.**

- **R1.** A feature the user has decided to build becomes working code with passing tests.
- **R2.** The user's intent is drawn out one level at a time before code starts.
- **R3.** Work moves to the next level only when the current one passes its review and the user approves it.
- **R4.** A question for a later level is answered at that level, not earlier.
- **R5.** Something already agreed or codified is asked again only for clarity or to resolve a conflict.
- **R6.** The code follows everything agreed or codified, including the user's answers.
- **R7.** Agreements carry over to later features, within their stated scope.
- **R8.** Once code starts, the work proceeds with what it needs.
- **R9.** Once code starts, the user is asked only when the work is blocked: by one of the user's decisions that no one made, or by code that conflicts with what was agreed.

**Glossary.** Terms are used as the project's [glossary](glossary.md) defines them.

**Scenarios.** Each runs on a sample project, and every check is automated. Acceptance tests and any approved levels a scenario starts from come with the scenario; no check relies only on tests written by the work being judged. The Verifies column is the work's.

| ID | Scenario | Passes when | Verifies |
| --- | --- | --- | --- |
| S1 | The user describes a feature | The code has passing tests, and acceptance tests pass | R1 |
| S2 | The user holds an invariant and reveals it only when asked | It surfaces before code starts, and acceptance tests show the code follows it | R2 R6 |
| S3 | The user agrees partially, then asks a question for a later level | Work goes through the levels in order, moves on from a level only after it passes its review and the user approves it, code starts only after every level is approved, the question is answered at its level, not earlier, and the work asks no question before its level | R2 R3 R4 |
| S4 | A second feature follows one whose decisions the user agreed, a codified rule exists, and an earlier level of this feature is approved, including the user's answer to a question | They are asked again only for clarity, and acceptance tests show the code follows all three | R5 R6 R7 |
| S5 | The levels are approved and cover everything the feature needs, and code starts from there | Nothing is asked after code starts, and acceptance tests pass | R1 R8 R9 |
| S6 | The levels are approved with one of the user's decisions left unmade, and code starts from there | The user is asked about it, and acceptance tests show the code follows the answer | R6 R9 |
| S7 | The levels are approved, the existing code conflicts with them, and code starts from there | The user is asked about the conflict, and acceptance tests show the code follows the answer | R6 R9 |

**Measures**, on real features, from transcripts and the code:

- **M1.** Questions about something already agreed or codified, other than for clarity or about a conflict: target zero.
- **M2.** The user's decisions that the work made, and the work's decisions that aren't recorded where the user can see them or that became a codified rule: target zero.
- **M3.** Times the user is asked after code starts because of one of the user's decisions that no one made: counted for each feature as planning misses. It's not a pass bar.
