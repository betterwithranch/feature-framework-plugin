# Behaviour

Narrows the [Outcome](1-outcome.md). "You" is the person the Outcome is for. "The work" is the agent building the feature.

## Rules

| # | Rule | Narrows | Surface |
| --- | --- | --- | --- |
| R1 | The levels run in this order: Outcome, Behaviour, Design, Slices, Build. Each of the first four produces one document. | Intent drawn out one level at a time | Project history |
| R2 | A level's document passes its review when three independent review runs report no findings. Findings are fixed and the review runs again, for at most four rounds. | Moves on only when the level passes its review | Review reports |
| R3 | The work starts a level only after the level before it passes its review. A passed level that changes passes its review again before work continues. | Moves on only when the level passes its review | Review reports, project history |
| R4 | Every decision a level needs comes from a passed level, a decision record, a codified rule or your answer. A decision none of them gives is asked during that level, before its review, and your answer is written into that level's document. | Decisions made before code starts | Conversation, level documents |
| R5 | A question that belongs to a later level, from you or the work, is recorded against that level and answered when that level is written. | Question answered at its level | Conversation, open questions, level documents |
| R6 | Before asking you anything, the work checks the feature's passed levels, the project's decision records and codified rules, and doesn't ask about what they answer. | Nothing agreed or codified is asked again | Conversation, level documents |
| R7 | Each answer you give is recorded as a decision record, which R6 checks in later levels and later features. | Agreements carry over | Decision records, conversation of a later feature |
| R8 | Design records only decisions this feature raises. General practice is cited from codified rules. | Nothing codified is asked again | Design document |
| R9 | Code starts only after Slices passes its review. | Decisions made before code starts | Project history |
| R10 | Build works one slice at a time. A slice is done when the cases assigned to it pass, every earlier slice's cases still pass, and the project's checks are clean. | Working code with passing tests | Test and check output |
| R11 | Build ends only when each of the feature's Outcome scenarios passes in full as an end-to-end test. | Working code with passing tests | Test output |
| R12 | Build never changes a slice's tests to make its code pass. When a passed level changes, the tests for the changed cases are updated from that level before Build continues. | The code follows everything agreed | Project history |
| R13 | After code starts, you're asked when, and only when, there's a decision no one made, a conflict between the existing code and the passed levels, or two things agreed or codified that conflict where it's unclear which came later. | Asked only when blocked | Conversation |
| R14 | Every rule, edge case, answer and codified rule that applies to the feature is a case assigned to a slice. | The code follows everything agreed or codified | Slices document |

## Edge cases

| # | Edge case | Rule | Surface |
| --- | --- | --- | --- |
| E1 | A review still has findings after four rounds. The work stops that level and reports the conflict or ambiguity in the instructions involved. | R2 | Conversation |
| E2 | Two things agreed or codified conflict. The later one wins, the earlier is updated to match, and the change is reported. You're asked only when it's unclear which came later. | R6 | Conversation, level documents |
| E3 | A passed level, decision record or codified rule covers a point but can be read more than one way. You're asked which reading is meant, and your answer is written into what you clarified. | R6 | Conversation, level documents, decision records |
| E4 | During Build, a level turns out to have a gap that no decision covers. You're asked about it, and your answer is recorded in that level's document. | R13 | Conversation, level documents |

## Examples

| Rule or edge case | Starting state | What happens | Expected result |
| --- | --- | --- | --- |
| R1 | You describe a feature to export invoices as CSV | The work runs the levels | An Outcome document exists before a Behaviour document, Behaviour before Design, Design before Slices, and Slices before any code change |
| R2 | The Behaviour draft's first review round has findings | The findings are fixed and the review runs again | Behaviour passes only in a round where all three runs report no findings |
| R3 | The Outcome review has one finding left | The work continues | No Behaviour document is written until the Outcome review reports no findings |
| R4 | Design must choose between writing the CSV in one pass or streaming it, and no level, decision record or codified rule decides it | The work writes Design | You're asked during Design, and your answer appears in the Design document |
| R5 | During Outcome you ask which CSV library to use | The work continues | The question is recorded for Design, isn't answered during Outcome, and is answered in the Design document |
| R6 | A codified rule says all dates are UTC | The work writes Behaviour for the export | You aren't asked about time zones |
| R7 | In the invoice export you answered that amounts use two decimal places | A later feature exports payments | You aren't asked about decimal places |
| R8 | A codified rule says money is stored as integer cents | The work writes Design | Design cites the rule and doesn't record a decision about money storage |
| R9 | Slices hasn't passed its review | The work continues | No change is made to the project's code or tests |
| R10 | Slice 2 is assigned the cases "voided invoices excluded" and "empty month gives a header only" | The work builds slice 2 | Both cases pass, slice 1's cases still pass, and the project's checks are clean |
| R11 | Every slice of the invoice export is done, and its Outcome has the scenario "you export March's invoices" | Build ends | The scenario's test exports all of March's invoices and passes end to end |
| R12 | A slice's assigned test expects a header row | The code produces no header | The work changes the code, not the test |
| R13 | All levels passed and give every decision the export needs, and none of the levels, the existing code, decision records or codified rules conflict with each other | The work builds every slice | Nothing is asked after code starts |
| R14 | A codified rule says money is integer cents, and Behaviour has the rule "voided invoices are excluded" | The work writes Slices | Each is a case assigned to a slice |
| E1 | The Outcome review has findings in four rounds in a row | The work continues | It stops revising the Outcome and reports which instructions conflict |
| E2 | A passed Behaviour says amounts show two decimal places; a codified rule added later says amounts show four | The work writes Design | Behaviour is updated to four decimal places and the update is reported; you aren't asked |
| E3 | A decision record says "exclude cancelled invoices", and invoices can be cancelled or voided | The work writes Behaviour | You're asked whether voided invoices count as cancelled, and the decision record states your answer |
| E4 | Build finds the export needs a file name and no level gives one | The work stops the slice | You're asked for the name, and Behaviour gains a rule giving it |

## Non-goals

- Deploying, opening pull requests or other automation after working code.
- Exploration, performance work, migrations, infrastructure or tooling changes that aren't part of a feature.
- Building a feature layer by layer.
- Checks that need a person.
- Asking you to approve each level.
