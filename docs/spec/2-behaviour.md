# Behaviour

Narrows the [Outcome](1-outcome.md). "You" is the person the Outcome is for. "The work" is the agent building the feature.

## Rules

| # | Rule | Narrows | Surface |
| --- | --- | --- | --- |
| R1 | The levels run in this order: Outcome, Behaviour, Design, Slices, Build. Each of the first four produces one document. | Intent drawn out one level at a time | Project history |
| R2 | A level's document passes its review when three independent review runs report no findings. | Moves on only when the level passes its review | Review reports |
| R3 | A review that has findings runs again after they're fixed. | Moves on only when the level passes its review | Review reports |
| R4 | The work starts a level only after the level before it passes its review. | Moves on only when the level passes its review | Review reports, project history |
| R5 | A passed level that changes passes its review again before work continues. | Moves on only when the level passes its review | Review reports |
| R6 | When a passed level changes, every later level that has passed is updated to match it. | The code follows everything agreed or codified | Level documents |
| R7 | A decision a level needs that no passed level, decision record or codified rule gives is asked during that level, before its review. | Decisions made before code starts | Conversation |
| R8 | Your answer to a level's question is written into that level's document. | The code follows everything agreed or codified, including your answers | Level documents |
| R9 | A question that belongs to a later level, from you or the work, is recorded against that level and answered when that level is written. | Question answered at its level | Conversation, open questions, level documents |
| R10 | Before asking you anything, the work checks the feature's passed levels, the project's decision records and codified rules, and doesn't ask about what they answer. | Nothing agreed or codified is asked again | Conversation, level documents |
| R11 | Each answer you give is recorded as a decision record, which R10 checks in later levels and later features. | Agreements carry over | Decision records, conversation of a later feature |
| R12 | Design cites the codified rule that covers a point instead of recording a decision about it. | The code follows everything agreed or codified | Design document |
| R13 | Code starts only after Slices passes its review. | Decisions made before code starts | Project history |
| R14 | Build works one slice at a time. A slice is done when the cases assigned to it pass, every earlier slice's cases still pass, and the project's checks are clean. | Working code with passing tests | Test and check output |
| R15 | Build ends only when each of the feature's Outcome scenarios passes in full as an end-to-end test. | Working code with passing tests | Test output |
| R16 | A slice's tests change only when the cases assigned to it change. | The code follows everything agreed | Project history |
| R17 | After code starts, you're asked when, and only when, there's a decision no one made, a conflict between the existing code and the passed levels, or two things agreed or codified that conflict where it's unclear which came later. | Asked only when blocked | Conversation |
| R18 | Every rule, edge case, answer and codified rule that applies to the feature is a case assigned to a slice. | The code follows everything agreed or codified | Slices document |

## Edge cases

| # | Edge case | Rule | Surface |
| --- | --- | --- | --- |
| E1 | A review still has findings after four rounds. The work stops that level and reports the conflict or ambiguity in the instructions involved. | R3 | Conversation |
| E2 | Two things agreed or codified conflict. The later one wins, the earlier is updated to match, and the change is reported. | R10 | Conversation, level documents |
| E3 | Two things agreed or codified conflict and it's unclear which came later. You're asked which applies. | R10 | Conversation |
| E4 | Before code starts, a passed level, decision record or codified rule covers a point but can be read more than one way. You're asked which reading is meant. | R10 | Conversation |
| E5 | Your answer about which reading is meant is written into the passed level, decision record or codified rule it clarifies. | R8 | Level documents, decision records, codified rules |
| E6 | During Build, a level that has passed turns out to have a gap that no decision covers. Your answer is written into that level's document. | R8 | Level documents |

## Examples

| Rule or edge case | Starting state | What happens | Expected result |
| --- | --- | --- | --- |
| R1 | You describe a feature to export invoices as CSV | The work runs the levels | An Outcome document exists before a Behaviour document, Behaviour before Design, Design before Slices, and Slices before any code change |
| R2 | In a round of Behaviour's review, two runs report no findings and one reports a finding | The round ends | Behaviour hasn't passed its review |
| R3 | Behaviour's first review round has two findings | The work fixes them | A second round of three runs reviews the fixed Behaviour |
| R4 | The Outcome review has one finding left | The work continues | No Behaviour document is written until the Outcome review reports no findings |
| R5 | Behaviour has passed, Design is being written, and Behaviour is updated so amounts show four decimal places | The work goes back to Design | Behaviour's review reports no findings before any more of Design is written |
| R6 | Behaviour, Design and Slices have passed, and during Build Behaviour gains the rule "the file is named invoices-YYYY-MM.csv" | Build resumes | Before the next slice is built, Slices assigns the file-name rule to a slice |
| R7 | Design must choose between writing the CSV in one pass or streaming it, and no level, decision record or codified rule decides it | The work writes Design | You're asked during Design, before its review |
| R8 | During Design you answer that the CSV is streamed | The work continues Design | The Design document says the CSV is streamed |
| R9 | During Outcome you ask which CSV library to use | The work continues | The question is recorded for Design, isn't answered during Outcome, and is answered in the Design document |
| R10 | A codified rule says all dates are UTC | The work writes Behaviour for the export | You aren't asked about time zones |
| R11 | In the invoice export you answered that amounts use two decimal places | A later feature exports payments | You aren't asked about decimal places |
| R12 | A codified rule says money is stored as integer cents | The work writes Design | Design cites the rule and doesn't record a decision about money storage |
| R13 | Slices hasn't passed its review | The work continues | No change is made to the project's code or tests |
| R14 | Slice 2 is assigned the cases "voided invoices excluded" and "empty month gives a header only" | The work builds slice 2 | Both cases pass, slice 1's cases still pass, and the project's checks are clean |
| R15 | Every slice of the invoice export is done, and its Outcome has the scenario "you export March's invoices" | Build ends | The scenario's test exports all of March's invoices and passes end to end |
| R16 | A slice's assigned test expects a header row, and the slice's cases haven't changed | The code produces no header | The work changes the code, not the test |
| R17 | All levels passed and give every decision the export needs, and none of the levels, the existing code, decision records or codified rules conflict with each other | The work builds every slice | Nothing is asked after code starts |
| R18 | A codified rule says money is integer cents, and Behaviour has the rule "voided invoices are excluded" | The work writes Slices | Each is a case assigned to a slice |
| E1 | The Outcome review has findings in four rounds in a row | The work continues | It stops revising the Outcome and reports which instructions conflict |
| E2 | A passed Behaviour says amounts show two decimal places; a codified rule added later says amounts show four | The work writes Design | Behaviour is updated to four decimal places and the update is reported; you aren't asked |
| E3 | A decision record says dates show as DD/MM/YYYY, a codified rule says YYYY-MM-DD, and neither shows when it was made | The work writes Behaviour | You're asked which date format applies |
| E4 | A decision record says "exclude cancelled invoices", and invoices can be cancelled or voided | The work writes Behaviour | You're asked whether voided invoices count as cancelled |
| E5 | You answered that voided invoices count as cancelled | The work continues Behaviour | The decision record says to exclude cancelled and voided invoices |
| E6 | Build finds the export needs a file name and no level gives one, and you answer "invoices-YYYY-MM.csv" | The work stops the slice | Behaviour gains a rule naming the file invoices-YYYY-MM.csv |

## Non-goals

- Deploying, opening pull requests or other automation after working code.
- Exploration, performance work, migrations, infrastructure or tooling changes that aren't part of a feature.
- Building a feature layer by layer.
- Checks that need a person.
- Asking you to approve each level.
