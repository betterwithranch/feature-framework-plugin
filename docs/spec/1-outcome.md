# Outcome

**For whom.** The person who decides which features to build and agrees each level, called "you" below.

**Achieves.**

- A feature you've decided to build becomes working code with passing tests.
- Your intent is drawn out one level at a time before code starts. Work moves to the next level only when you explicitly agree.
- A question for a later level is answered at that level, not earlier.
- Nothing already agreed or codified is asked again, except for clarity before code starts or to resolve a conflict.
- The code follows everything agreed or codified, including your answers. Agreements carry over to later features.
- Once code starts, the work proceeds with everything it needs. You're asked only when it's blocked: by a decision no one made, or by code that conflicts with what was agreed.

"Code starts" means the first change to the project's code or tests.

**Scenarios.** Each runs on a sample project with a scripted user, and passes only if all 10 runs pass. Every check is automated: acceptance tests, transcript analysis or an LLM judge. Acceptance tests, and any agreed levels a scenario starts from, come with the scenario. Acceptance tests fail before the work and pass after it; no check relies only on tests written by the work being judged.

| # | Scenario | Passes when |
| --- | --- | --- |
| 1 | You describe a feature | The code has passing tests, and acceptance tests pass |
| 2 | You hold an invariant and reveal it only when asked | It surfaces before code starts, and acceptance tests show the code follows it |
| 3 | You agree partially, then ask a question for a later level | Work goes through the levels in order, moves on only after you explicitly agree, code starts only after every level is agreed, your question is answered at its level, not earlier, and the work asks no question before its level |
| 4 | A second feature follows one whose decisions you agreed, a codified rule exists, and an earlier level of this feature is agreed, including your answer to a question | None of them is asked again, except for clarity before code starts or to resolve a conflict, and acceptance tests show the code follows all three |
| 5 | The levels are agreed and cover everything the feature needs, and code starts from there | Nothing is asked after code starts, except to resolve a conflict, and acceptance tests pass |
| 6 | The levels are agreed with one decision left unmade, and code starts from there | You're asked about it, and acceptance tests show the code follows your answer |
| 7 | The levels are agreed, the existing code conflicts with them, and code starts from there | You're asked about the conflict, and acceptance tests show the code follows your answer |

**Measured on real features**, from transcripts and the code:

- Questions about something already agreed or codified, other than for clarity before code starts or about a conflict: target zero.
- Decisions in the code that nothing agreed or codified covers: target zero.
- Times you're asked after code starts because of a decision no one made: counted for each feature as planning misses. It's not a pass bar.
