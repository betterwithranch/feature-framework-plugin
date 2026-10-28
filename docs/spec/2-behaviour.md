# Behaviour

Narrows the [Outcome](1-outcome.md). "You" is the person the Outcome is for. "The work" is the agent building the feature. Which decisions are yours and which are the work's is set by the [decision classification](../../skills/references/decisions.md).

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
| R8 | One of your decisions a level needs that no passed level, decision record or codified rule gives is asked during that level, before its review. | Decisions made before code starts | Conversation |
| R9 | Your answer is written into the level document, decision record or codified rule the question is about. | The code follows everything agreed or codified, including your answers | Level documents, decision records, codified rules |
| R10 | A question that belongs to a later level is answered when that level is written, not earlier. | Question answered at its level | Conversation, level documents |
| R11 | The work doesn't ask a question that belongs to a later level before work on that level starts. | Question answered at its level | Conversation |
| R12 | The work doesn't ask you about what the feature's passed levels, the project's decision records or codified rules answer, except for clarity or to resolve a conflict. | Nothing agreed or codified is asked again | Conversation |
| R13 | Each answer you give is written into a decision record. | Agreements carry over | Decision records |
| R14 | Design cites the codified rule that covers a point instead of recording a decision about it. | The code follows everything agreed or codified | Design document |
| R15 | Code starts only after Slices passes its review. | Decisions made before code starts | Project history |
| R16 | Build works one slice at a time. | Working code with passing tests | Project history |
| R17 | A slice is done when the cases assigned to it pass, every earlier slice's cases still pass, and the project's checks are clean. | Working code with passing tests | Test and check output |
| R18 | Build ends only when each of the feature's Outcome scenarios passes in full as an end-to-end test. | Working code with passing tests | Test output |
| R19 | Once a slice is done, its tests change only when the cases assigned to it change. | The code follows everything agreed | Project history |
| R20 | After code starts, you're asked when the work is blocked by one of your decisions that no one made. | Asked only when blocked | Conversation |
| R21 | After code starts, you're asked when the work is blocked by a conflict between one of your decisions and existing code that nothing you agreed decided. | Asked only when blocked | Conversation |
| R22 | After code starts, you're asked only when the work is blocked by one of your decisions. | Asked only when blocked | Conversation |
| R23 | Every rule, edge case, decision record and codified rule that applies to the feature is a case assigned to a slice. | The code follows everything agreed or codified | Slices document |
| R24 | The work doesn't make any of your decisions, wherever it would be written. | You make your decisions | Level documents, code, and the work's plans, notes and memory |
| R25 | You aren't asked to make any of the work's decisions. | The work makes its own | Conversation |
| R26 | Each decision the work makes while writing a level's document is recorded in that document. | The work records its decisions where you can see them | Level documents |
| R27 | A decision the work makes never becomes a codified rule. | The work's decisions never become codified rules | Codified rules, and the work's plans, notes and memory |
| R28 | Each decision the work makes during Build is recorded in the code and tests. | The work records its decisions where you can see them | Code and tests |
| R29 | Each decision the work writes into its plans, notes or memory is also recorded in the level document, or the code and tests, it applies to. | The work records its decisions where you can see them, wherever a decision is written | Level documents, code and tests, and the work's plans, notes and memory |

## Edge cases

| # | Edge case | Rule | Surface |
| --- | --- | --- | --- |
| E1 | A review still has findings after four rounds. The work is blocked until you've decided on the proposed fix: the document isn't revised again before then. | R4 | Conversation, project history |
| E2 | A review still has findings after four rounds. The work reports why the review keeps failing, with a proposed fix. | R4 | Conversation |
| E3 | You've decided on the proposed fix for a review that had findings after four rounds. The level continues as you decided. | R4 | Review reports, project history |
| E4 | You replace one of your decisions. The earlier one is removed wherever it's written. | R9 | Level documents, decision records, codified rules, and the work's plans, notes and memory |
| E5 | Two current decisions of yours conflict, and the work is blocked by which applies. You're asked which applies. | R12 | Conversation |
| E6 | One of your decisions conflicts with something no one decided, and the work is blocked by which applies. You're asked which applies. | R12 | Conversation |
| E7 | One of your decisions conflicts with a decision the work made. You aren't asked. | R12 | Conversation |
| E8 | Before code starts, something agreed or codified covers a point but can be read more than one way. You're asked which reading is meant. | R12 | Conversation |
| E9 | During Build, a level that has passed turns out to be missing one of your decisions. Your answer is written into that level's document. | R9 | Level documents |
| E10 | During Build, you answer that the existing code is right where it conflicts with a passed level. That level is updated to match the existing code. | R9 | Level documents |
| E11 | After code starts, something agreed or codified can be read more than one way, and the work is blocked by which reading is meant. You're asked which reading is meant. | R20 | Conversation |
| E12 | After code starts, something agreed or codified can be read more than one way, and the work is blocked by which reading is meant. The work makes no change to the code or tests for either reading before you answer. | R20 | Project history |
| E13 | One of your decisions conflicts with a decision the work recorded in a passed level. The work's decision is updated to match yours. | R26 | Level documents |
| E14 | A rule, principle or memory the work wrote without your agreement covers one of your decisions that the work is blocked by. You're asked about the decision. | R8 | Conversation |
| E15 | It's unclear whether a decision the work is blocked by is yours or the work's. You're asked about the decision. | R8 | Conversation |
| E16 | A decision the work makes follows from something agreed, a codified rule or a goal. Its record cites which. | R26 | Level documents |
| E17 | After code starts, the existing code conflicts with one of the work's decisions in a passed level. You aren't asked. | R22 | Conversation |
| E18 | A review still has findings after four rounds. The instructions involved change only as you decide. | R24 | Instructions |

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
| R8 | Design must choose whether to add a CSV library, which adds a dependency, and no level, decision record or codified rule decides it | The work writes Design | You're asked during Design, before its review |
| R9 | During Design you answer that the CSV is written with Python's standard csv module, adding no library | The work continues Design | The Design document says the CSV is written with Python's standard csv module |
| R9 | A decision record says "exclude cancelled invoices", and you answer that voided invoices count as cancelled | The work continues Behaviour | The decision record says to exclude cancelled and voided invoices |
| R10 | During Outcome you ask which CSV library to use | The work continues | The question isn't answered during Outcome and is answered in the Design document |
| R11 | During Outcome the work finds that whether to add a CSV library is for Design to decide | The work writes Outcome and Behaviour | You aren't asked about a CSV library before work on Design starts |
| R12 | A codified rule says all dates are UTC | The work writes Behaviour for the export | You aren't asked about time zones |
| R12 | In the invoice export you answered that amounts in every export use two decimal places | A later feature exports payments | You aren't asked about decimal places |
| R13 | During Behaviour of the invoice export you answer that amounts use two decimal places | The work continues Behaviour | A decision record says amounts use two decimal places |
| R14 | A codified rule says money is stored as integer cents | The work writes Design | Design cites the rule and doesn't record a decision about money storage |
| R15 | Slices hasn't passed its review | The work continues | No change is made to the project's code or tests |
| R16 | Slices assigns "voided invoices excluded" to slice 1 and "empty month gives a header only" to slice 2 | Build runs | Every change for one of the two slices comes before any change for the other |
| R17 | Slice 2 is assigned the cases "voided invoices excluded" and "empty month gives a header only" | The work builds slice 2 | Both cases pass, slice 1's cases still pass, and the project's checks are clean |
| R18 | Every slice of the invoice export is done, and its Outcome has the scenario "you export March's invoices" | Build ends | The scenario's test exports all of March's invoices and passes end to end |
| R19 | Slice 1 is done, its test expects a header row, and the cases assigned to it haven't changed | While building slice 2, the code stops producing the header | The work changes the code, not slice 1's test |
| R20 | All levels have passed, and no level, decision record or codified rule says whether credit notes are exported | The work builds the slice that selects invoices | You're asked whether credit notes are exported |
| R21 | All levels have passed, Behaviour names the file invoices-YYYY-MM.csv, and the project's existing export code names files export-YYYY-MM.csv, which nothing you agreed decided | The work builds the slice that names the file | You're asked which file name applies |
| R22 | All levels passed and hold every one of your decisions the export needs, no level names the function that formats amounts, and none of the levels, the existing code, decision records or codified rules conflict with each other | The work builds every slice | Nothing is asked after code starts |
| R23 | The payment export is being built. A decision record from the invoice export says amounts in every export use two decimal places, a codified rule says money is integer cents, and Behaviour has the rule "refunded payments are excluded" | The work writes Slices | Each of the three is a case assigned to a slice |
| R24 | Nothing decides whether credit notes are exported, and you haven't been asked | The work writes Behaviour and its plan and notes for it | Until you answer, no level document, plan, note or memory says whether credit notes are exported |
| R25 | Design must choose between writing the CSV in one pass or streaming it, a reversible choice local to the export, and nothing decides it | The work writes Design | You aren't asked about streaming |
| R26 | Design must choose between writing the CSV in one pass or streaming it, and nothing decides it | The work writes Design | The Design document records which of the two the work chose |
| R27 | The invoice export's Design records the work's decision to stream the CSV | The export is built | No codified rule, plan, note or memory says that exports are streamed |
| R28 | All levels have passed, and no level names the function that formats amounts | The work builds the slice that formats amounts and names the function format_amount | The slice's code change defines format_amount and its tests call it |
| R29 | While writing Design, the work's plan says the CSV is streamed, and nothing decides it | The work finishes Design | The Design document records that the CSV is streamed |
| R29 | During Build, the work's notes say amounts are formatted by a function named format_amount, and no level names it | The work builds the slice that formats amounts | The slice's code change defines format_amount |
| E1 | The Outcome review has findings in four rounds in a row because two instructions conflict | The work continues | You decide on the proposed fix before the Outcome changes again |
| E2 | The Outcome review has findings in four rounds in a row because two instructions conflict | The fourth round ends | You're told which two instructions conflict and given a proposed fix |
| E2 | The Behaviour review has findings in four rounds in a row because one of the three runs keeps reporting that R3's example is unclear, and no instruction involved conflicts or is ambiguous | The fourth round ends | You're told that one run keeps finding R3's example unclear and given a proposed fix |
| E3 | The Outcome review had findings in four rounds in a row, and you've decided to keep both instructions as they are | The work continues the Outcome | The Outcome's next review round reviews it under the unchanged instructions |
| E4 | A passed Behaviour and a decision record say amounts show two decimal places, and during Design you say amounts show four instead | The work continues Design | No level document, decision record, plan, note or memory says amounts show two decimal places |
| E5 | A passed Behaviour has your answer that amounts show two decimal places, a codified rule you agreed says four, and Design must choose how amounts are formatted | The work writes Design | You're asked whether amounts show two or four decimal places |
| E6 | A decision record of your answer says dates show as DD/MM/YYYY, the project's existing export code, which nothing you agreed decided, shows them as YYYY-MM-DD, and Behaviour must state how dates show | The work writes Behaviour | You're asked which date format applies |
| E7 | A passed Design records the work's decision to stream the CSV, and you've since agreed a codified rule that every export writes its file in one pass | The work writes Slices | You aren't asked whether the export streams the CSV or writes it in one pass |
| E8 | A decision record says "exclude cancelled invoices", and invoices can be cancelled or voided | The work writes Behaviour | You're asked whether voided invoices count as cancelled |
| E9 | Build finds the export needs a file name and no level gives one, and you answer "invoices-YYYY-MM.csv" | The work stops the slice | Behaviour gains a rule naming the file invoices-YYYY-MM.csv |
| E10 | Behaviour names the file invoices-YYYY-MM.csv, the existing export code names files export-YYYY-MM.csv, which nothing you agreed decided, and during Build you answer that the existing name is right | The work stops the slice | Behaviour's file-name rule names the file export-YYYY-MM.csv |
| E11 | All levels have passed, a decision record says "exclude cancelled invoices", and invoices can be cancelled or voided | The work builds the slice that selects invoices | You're asked whether voided invoices count as cancelled |
| E12 | All levels have passed, a decision record says "exclude cancelled invoices", invoices can be cancelled or voided, and you haven't answered whether voided invoices count as cancelled | The work builds the slice that selects invoices | No change to the code or tests decides whether voided invoices are exported |
| E13 | A passed Design records the work's decision to stream the CSV, and you've since agreed a codified rule that every export writes its file in one pass | The work writes Slices | Design cites the one-pass rule and no longer records a decision to stream the CSV |
| E14 | The work's notes from an earlier session hold the rule "exports include voided invoices", which you never agreed, and Behaviour needs whether voided invoices are exported | The work writes Behaviour | You're asked whether voided invoices are exported |
| E15 | Design must choose whether export results are cached for an hour, which may change how current the exported data is, and nothing decides it | The work writes Design | You're asked during Design whether export results are cached |
| E16 | Behaviour has the rule "amounts show two decimal places", a codified rule says money is stored as integer cents, and Design must choose how a stored amount becomes the shown amount | The work writes Design | The Design document records that the shown amount is the integer cents with a decimal point placed two digits from the right, and cites the decimal-places rule and the money rule |
| E17 | All levels have passed, Design records the work's decision to write rows with a new function named write_rows, and the existing export code already has write_csv_rows doing the same | The work builds the slice that writes rows | You aren't asked which function writes the rows |
| E18 | The Outcome review has findings in four rounds in a row because two instructions conflict, the work proposes removing the first, and you decide to reword the second | The work continues | The second instruction is reworded as you decided and the first is unchanged |

## Non-goals

- Deploying, opening pull requests or other automation after working code.
- Exploration, performance work, migrations, infrastructure or tooling changes that aren't part of a feature.
- Building a feature layer by layer.
- Checks that need a person.
- Asking you to approve each level.
