# 0062. Verification rules 3 and 4 are bounded to what a scenario cites and names

Status: partly accepted: rule 4 approved as FF-69 A; rule 3 replaced by 0073 (FF-74 A)

## Context

The Outcome's review ran four rounds without passing. CLAUDE.md says that after four rounds that don't pass, the work looks for a conflict or ambiguity in the instructions involved, reports it and fixes the instructions, and goal 5 says to change the instructions so a gate converges rather than judging case by case.

- Rule 4 read "The starting state describes everything the scenario depends on; nothing is left for the work being verified to produce first." Each round's judge found something new missing, on different rows, and the same text got different verdicts. S2's starting state, "The user holds an invariant and reveals it only when asked", passed in round 1 and failed in round 2 with "no feature described and no level approvals stated"; after that fix it passed in round 3 and failed in round 4 with "starting state does not say which level needs the invariant". S6's, "The levels are approved with one of the user's decisions left unmade, and code starts from there", passed in round 1 and failed in round 2 with "the answer the user holds, which the acceptance tests check, is not described".
- Rule 3 read "What it describes as passing includes every way the requirement allows the user to get that result." A judge read S10 against one cited requirement alone and failed its "before the level's document is written", which [decision 0021](0021-play-back-before-acting-interview-before-drafting.md) sets through another requirement it cites.

## Decision

- Verification rule 3 reads: "What it describes as passing includes every way the cited requirements together allow the user to get that result."
- Verification rule 4 reads: "Each thing the pass condition checks is either set up in the starting state or produced by the work being verified. What the document says applies to every scenario is part of each scenario's starting state." The user approved this wording as FF-69 A on 2026-11-10.

## Consequences

- Amends the Verification review's rules, [decision 0044](0044-the-verification-review-s-rules.md).
- Rule 3 enforces [decision 0021](0021-play-back-before-acting-interview-before-drafting.md).
