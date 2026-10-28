# Behaviour

Narrows the [Outcome](1-outcome.md). "You" is the person the Outcome is for. "The work" is the agent building the feature.

## Rules

| # | Rule | Narrows | Surface |
| --- | --- | --- | --- |
| R1 | The levels run in this order: Outcome, Behaviour, Design, Slices, Build. Each of the first four produces one document. | Intent drawn out one level at a time | Level documents |
| R2 | A level's document passes its review when three independent review runs report no findings. Findings are fixed and the review runs again, for at most four rounds. | Moves on only when the level passes its review | Review reports |
| R3 | The work starts a level only after the level before it passes its review. | Moves on only when the level passes its review | Level documents |
| R4 | A question that needs your decision about the current level is asked during that level, before its review. | Decisions made before code starts | Conversation |
| R5 | A question that belongs to a later level, from you or the work, is recorded against that level and answered when that level is written. | Question answered at its level | Conversation, open questions |
| R6 | Before asking you anything, the work checks the feature's passed levels, its decision records and codified rules. It asks only when none of them answers. | Nothing agreed or codified is asked again | Conversation |
| R7 | Each answer you give is recorded where later levels and later features read it. | Agreements carry over | Conversation of a later feature |
| R8 | Design records only decisions this feature raises. General practice is cited from codified rules. | Nothing codified is asked again | Design document |
| R9 | Code starts only after Slices passes its review. | Decisions made before code starts | Project history |
| R10 | Build works one slice at a time. A slice is done when the cases assigned to it pass, every earlier slice's cases still pass, and the project's checks are clean. | Working code with passing tests | Test and check output |
| R11 | Each slice extends one Outcome scenario's test, possibly narrowed, and passes it end to end. | Working code with passing tests | Test output |
| R12 | Build never changes the tests it builds toward. | The code follows everything agreed | Project history |
| R13 | After code starts, you're asked only about a decision no one made or a conflict between the existing code and the passed levels. | Asked only when blocked | Conversation |

## Edge cases

| # | Edge case | Rule | Surface |
| --- | --- | --- | --- |
| E1 | A review still has findings after four rounds. The work stops that level and reports the conflict or ambiguity in the instructions involved. | R2 | Conversation |
| E2 | Two agreements conflict. The later one wins, the earlier is updated to match, and the change is reported. You're asked only when it's unclear which came later. | R6 | Conversation, level documents |
| E3 | You ask for clarity about something agreed before code starts. The work answers from the record without treating it as a new decision. | R6 | Conversation |
| E4 | During Build, a level turns out to have a gap that no decision covers. You're asked about it, your answer is recorded in that level's document, and the level's review runs again before Build continues. | R13 | Conversation, level documents |

## Examples

| Rule or edge case | Starting state | What happens | Expected result |
| --- | --- | --- | --- |
| R1 | You describe a feature to export invoices as CSV | The work runs the levels | An Outcome document exists before a Behaviour document, Behaviour before Design, Design before Slices, and Slices before any code change |
| R2 | The Behaviour draft has a rule with no example | Three review runs | At least one run reports the missing example; after the fix, all three runs report no findings |
| R3 | The Outcome review has one finding left | The work continues | No Behaviour document is written until the Outcome review reports no findings |
| R4 | Behaviour needs to know whether exports include voided invoices, and nothing records it | The work writes Behaviour | You're asked during Behaviour, and the answer appears as a rule |
| R5 | During Outcome you ask which CSV library to use | The work continues | The question is recorded for Design, isn't answered during Outcome, and is answered in the Design document |
| R6 | A codified rule says all dates are UTC | The work writes Behaviour for the export | You aren't asked about time zones, and the rule says export dates are UTC |
| R7 | In the invoice export you answered that amounts use two decimal places | A later feature exports payments | You aren't asked about decimal places, and payment amounts use two |
| R8 | A codified rule says money is stored as integer cents | The work writes Design | Design cites the rule and doesn't record a decision about money storage |
| R9 | Slices hasn't passed its review | The work continues | No change is made to the project's code or tests |
| R10 | Slice 2 is assigned the cases "voided invoices excluded" and "empty month gives a header only" | The work builds slice 2 | Both cases pass, slice 1's cases still pass, and the project's checks are clean |
| R11 | The Outcome scenario "you export March's invoices" has an end-to-end test | The work builds slice 1, which exports one invoice | The scenario's test, narrowed to one invoice, passes end to end |
| R12 | A slice's assigned test expects a header row | The code produces no header | The work changes the code, not the test |
| R13 | All levels passed with nothing left open | The work builds every slice | Nothing is asked after code starts |
| E1 | The Outcome review has findings in four rounds in a row | The work continues | It stops revising the Outcome and reports which instructions conflict |
| E2 | Your Outcome says each level needs your approval; a later decision says levels move on when their review passes | The work writes Behaviour | The Outcome is updated to the later decision and the update is reported; you aren't asked |
| E3 | Before code starts you ask what "voided" means, and Behaviour defines it | The work replies | It quotes Behaviour's definition and records no new decision |
| E4 | Build finds the export needs a file name and no level gives one | The work stops the slice | You're asked for the name, Behaviour gains the rule, its review passes, and the slice continues |

## Non-goals

- Deploying, opening pull requests or other automation after working code.
- Exploration, performance work, migrations, infrastructure or tooling changes that aren't part of a feature.
- Building a feature layer by layer.
- Checks that need a person.
- Asking you to approve each level.
