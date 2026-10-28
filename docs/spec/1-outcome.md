# Outcome

**For whom.** The person who decides which features to build, called "you" below.

**Achieves.**

- A feature you've decided to build becomes working code with passing tests.
- Your intent is drawn out one level at a time, so your decisions are made before code starts. Work moves to the next level only when the current one passes its review.
- A question for a later level is answered at that level, not earlier.
- Nothing already agreed or codified is asked again, except for clarity before code starts or to resolve a conflict.
- You make your decisions. The work makes its own and records them where you can see them. This holds wherever a decision is written.
- The code follows everything agreed or codified, including your answers. Agreements carry over to later features. The work's decisions never become codified rules.
- Once code starts, the work proceeds with everything it needs. You're asked only when it's blocked: by one of your decisions that no one made, or by a conflict.

"Code starts" means the first change to the project's code or tests for that feature. Which decisions are yours and which are the work's is set by the [decision classification](../../skills/references/decisions.md).

**Scenarios.** Each runs on a sample project with a scripted user, and passes only if all 10 runs pass. Every check is automated: acceptance tests, transcript analysis or an LLM judge. Acceptance tests, and any levels a scenario starts from, come with the scenario. Acceptance tests fail before the work and pass after it; no check relies only on tests written by the work being judged.

| # | Scenario | Passes when |
| --- | --- | --- |
| 1 | You describe a feature that needs both your decisions and the work's, the scripted user can answer any question about it, and nothing conflicts | Each of your decisions, wherever it's written, was made by you before code starts, you're asked to make none of the work's decisions, each of the work's decisions is recorded where you can see it and none became a codified rule, the code has passing tests, and acceptance tests pass |
| 2 | You hold an invariant and reveal it only when asked | It surfaces before code starts, and acceptance tests show the code follows it |
| 3 | A level's first draft fails its review, and you ask a question for a later level | Work goes through the levels in order, moves on only after each level passes its review, code starts only after every level has passed, your question is answered at its level, not earlier, and the work asks no question before its level |
| 4 | You build a feature, giving scripted answers that its acceptance tests depend on, then a second one that those answers apply to. A codified rule exists, an earlier level of the second feature has passed its review, including your answer to a question, and nothing conflicts | Nothing in that level, your scripted answers or the rule is asked again, except for clarity before code starts, and acceptance tests show the first feature's code follows your scripted answers and the second feature's code follows all three |
| 5 | The levels have passed review, hold all your decisions the feature needs, the work's decisions are left to it, nothing conflicts with them, and code starts from there | Nothing is asked after code starts, and acceptance tests pass |
| 6 | The levels have passed review with one of your decisions left unmade, and code starts from there | You're asked about it, and acceptance tests show the code follows your answer |
| 7 | The levels have passed review, the existing code conflicts with them, and code starts from there | You're asked about the conflict, and acceptance tests show the code follows your answer |

**Measured on real features**, from transcripts and everything the work writes:

- Questions about something already agreed or codified, other than for clarity before code starts or about a conflict: target zero.
- Your decisions that the work made instead of you: target zero.
- Questions asking you to make one of the work's decisions: target zero.
- The work's decisions that aren't recorded where you can see them, or that became a codified rule: target zero.
