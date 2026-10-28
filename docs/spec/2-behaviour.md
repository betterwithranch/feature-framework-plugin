# Behaviour

Narrows the [Outcome](1-outcome.md). "You" is the person the Outcome is for. "The work" is the agent building the feature.

## Rules

| # | Rule | Narrows | Surface |
| --- | --- | --- | --- |
| R1 | The levels run in this order: Outcome, Behaviour, Design, Slices, Build. | Intent drawn out one level at a time | Project history |
| R2 | Each of Outcome, Behaviour, Design and Slices produces one document. | Intent drawn out one level at a time | Level documents |
| R3 | A level's document passes its review when three independent review runs report no findings. | Moves on only when the level passes its review | Review reports |
| R4 | A review that has findings runs again after they're fixed. | Moves on only when the level passes its review | Review reports |
| R5 | The work starts a level only after the level before it passes its review. | Moves on only when the level passes its review | Review reports, project history |
| R6 | A passed level that changes passes its review again before work continues. | Moves on only when the level passes its review | Review reports, project history |
| R7 | When a passed level changes, every later level that has passed is updated to match it. | The code follows everything agreed or codified | Level documents |
| R8 | A decision a level needs that no passed level, decision record or codified rule gives is asked during that level, before its review. | Decisions made before code starts | Conversation |
| R9 | Your answer to a level's question is written into that level's document. | The code follows everything agreed or codified, including your answers | Level documents |
| R10 | A question that belongs to a later level, from you or the work, is answered when that level is written, not earlier. | Question answered at its level | Conversation, level documents |
| R11 | The work doesn't ask you about what the feature's passed levels, the project's decision records or codified rules answer, except for clarity before code starts or to resolve a conflict. | Nothing agreed or codified is asked again | Conversation |
| R12 | Each answer you give is recorded as a decision record. | Agreements carry over | Decision records |
| R13 | Design cites the codified rule that covers a point instead of recording a decision about it. | The code follows everything agreed or codified | Design document |
| R14 | Code starts only after Slices passes its review. | Decisions made before code starts | Project history |
| R15 | Build works one slice at a time. | Working code with passing tests | Project history |
| R16 | A slice is done when the cases assigned to it pass, every earlier slice's cases still pass, and the project's checks are clean. | Working code with passing tests | Test and check output |
| R17 | Build ends only when each of the feature's Outcome scenarios passes in full as an end-to-end test. | Working code with passing tests | Test output |
| R18 | A slice's tests change only when the cases assigned to it change. | The code follows everything agreed | Project history |
| R19 | After code starts, you're asked about a decision no one made. | Asked only when blocked | Conversation |
| R20 | After code starts, you're asked about a conflict between the existing code and the passed levels. | Asked only when blocked | Conversation |
| R21 | After code starts, you're asked only when the work is blocked by a decision no one made or by a conflict. | Asked only when blocked | Conversation |
| R22 | Every rule, edge case, answer and codified rule that applies to the feature is a case assigned to a slice. | The code follows everything agreed or codified | Slices document |

## Edge cases

| # | Edge case | Rule | Surface |
| --- | --- | --- | --- |
| E1 | A review still has findings after four rounds. The work stops that level. | R4 | Project history |
| E2 | A review still has findings after four rounds. The work reports the conflict or ambiguity in the instructions involved. | R4 | Conversation |
| E3 | Two things agreed or codified conflict. The later one wins without you being asked. | R11 | Conversation, level documents |
| E4 | The later of two conflicting things agreed or codified wins. The earlier is updated to match. | R11 | Level documents, decision records, codified rules |
| E5 | The later of two conflicting things agreed or codified wins. The change to the earlier is reported. | R11 | Conversation |
| E6 | Two things agreed or codified conflict and it's unclear which came later. You're asked which applies. | R11 | Conversation |
| E7 | Before code starts, a passed level, decision record or codified rule covers a point but can be read more than one way. You're asked which reading is meant. | R11 | Conversation |
| E8 | Your answer about which reading is meant is written into the passed level, decision record or codified rule it clarifies. | R9 | Level documents, decision records, codified rules |
| E9 | During Build, a level that has passed turns out to have a gap that no decision covers. Your answer is written into that level's document. | R9 | Level documents |
| E10 | During Build, you answer that the existing code is right where it conflicts with a passed level. That level is updated to match the existing code. | R9 | Level documents |

## Examples

| Rule or edge case | Starting state | What happens | Expected result |
| --- | --- | --- | --- |
| R1 | You describe a feature to export invoices as CSV | The work runs the levels | An Outcome document exists before a Behaviour document, Behaviour before Design, Design before Slices, and Slices before any code change |
| R2 | You describe a feature to export invoices as CSV | The work finishes Slices | The export has one Outcome, one Behaviour, one Design and one Slices document |
| R3 | In a round of Behaviour's review, two runs report no findings and one reports a finding | The round ends | Behaviour hasn't passed its review |
| R4 | Behaviour's first review round has two findings | The work fixes them | A second round of three runs reviews the fixed Behaviour |
| R5 | The Outcome review has one finding left | The work continues | No Behaviour document is written until the Outcome review reports no findings |
| R6 | Behaviour has passed, Design is being written, and Behaviour is updated so amounts show four decimal places | The work goes back to Design | Behaviour's review reports no findings before any more of Design is written |
| R7 | Behaviour, Design and Slices have passed, and during Build Behaviour gains the rule "the file is named invoices-YYYY-MM.csv" | Build resumes | Slices assigns the file-name rule to a slice |
| R8 | Design must choose between writing the CSV in one pass or streaming it, and no level, decision record or codified rule decides it | The work writes Design | You're asked during Design, before its review |
| R9 | During Design you answer that the CSV is streamed | The work continues Design | The Design document says the CSV is streamed |
| R10 | During Outcome you ask which CSV library to use | The work continues | The question isn't answered during Outcome and is answered in the Design document |
| R11 | A codified rule says all dates are UTC | The work writes Behaviour for the export | You aren't asked about time zones |
| R11 | In the invoice export you answered that amounts use two decimal places | A later feature exports payments | You aren't asked about decimal places |
| R12 | During Behaviour of the invoice export you answer that amounts use two decimal places | The work continues Behaviour | A decision record says amounts use two decimal places |
| R13 | A codified rule says money is stored as integer cents | The work writes Design | Design cites the rule and doesn't record a decision about money storage |
| R14 | Slices hasn't passed its review | The work continues | No change is made to the project's code or tests |
| R15 | Slices assigns "voided invoices excluded" to slice 1 and "empty month gives a header only" to slice 2 | Build runs | Every change for slice 1 comes before any change for slice 2 |
| R16 | Slice 2 is assigned the cases "voided invoices excluded" and "empty month gives a header only" | The work builds slice 2 | Both cases pass, slice 1's cases still pass, and the project's checks are clean |
| R17 | Every slice of the invoice export is done, and its Outcome has the scenario "you export March's invoices" | Build ends | The scenario's test exports all of March's invoices and passes end to end |
| R18 | A slice's assigned test expects a header row, and the slice's cases haven't changed | The code produces no header | The work changes the code, not the test |
| R19 | All levels have passed, and no level, decision record or codified rule says whether credit notes are exported | The work builds the slice that selects invoices | You're asked whether credit notes are exported |
| R20 | All levels have passed and Behaviour names the file invoices-YYYY-MM.csv, and the project's existing export code names files export-YYYY-MM.csv | The work builds the slice that names the file | You're asked which file name applies |
| R21 | All levels passed and give every decision the export needs, and none of the levels, the existing code, decision records or codified rules conflict with each other | The work builds every slice | Nothing is asked after code starts |
| R22 | A codified rule says money is integer cents, and Behaviour has the rule "voided invoices are excluded" | The work writes Slices | Each is a case assigned to a slice |
| E1 | The Outcome review has findings in four rounds in a row | The work continues | The Outcome isn't revised again |
| E2 | The Outcome review has findings in four rounds in a row because two instructions conflict | The work stops the Outcome | You're told which two instructions conflict |
| E3 | A passed Behaviour says amounts show two decimal places; a codified rule added later says four | The work writes Design | Design uses four decimal places for amounts, and you aren't asked which applies |
| E4 | A passed Behaviour says amounts show two decimal places; a codified rule added later says four | The work writes Design | Behaviour says amounts show four decimal places |
| E5 | A passed Behaviour says amounts show two decimal places; a codified rule added later says four | The work writes Design | You're told Behaviour changed from two to four decimal places |
| E6 | A decision record says dates show as DD/MM/YYYY, a codified rule says YYYY-MM-DD, and neither shows when it was made | The work writes Behaviour | You're asked which date format applies |
| E7 | A decision record says "exclude cancelled invoices", and invoices can be cancelled or voided | The work writes Behaviour | You're asked whether voided invoices count as cancelled |
| E8 | You answered that voided invoices count as cancelled | The work continues Behaviour | The decision record says to exclude cancelled and voided invoices |
| E9 | Build finds the export needs a file name and no level gives one, and you answer "invoices-YYYY-MM.csv" | The work stops the slice | Behaviour gains a rule naming the file invoices-YYYY-MM.csv |
| E10 | Behaviour names the file invoices-YYYY-MM.csv, the existing export code names files export-YYYY-MM.csv, and during Build you answer that the existing name is right | The work stops the slice | Behaviour's file-name rule names the file export-YYYY-MM.csv |

## Non-goals

- Deploying, opening pull requests or other automation after working code.
- Exploration, performance work, migrations, infrastructure or tooling changes that aren't part of a feature.
- Building a feature layer by layer.
- Checks that need a person.
- Asking you to approve each level.
