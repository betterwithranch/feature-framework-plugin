# Outcome review: Provenance

Read the document with the conversation that produced it, the decision log and the codified rules, including [the decision classification](../decisions.md). Rows: each requirement, the paragraph above the scenario table, each scenario and each measure.

1. The statement is something the user said or agreed, or it is marked as the agent's.
2. A statement marked as the agent's makes no decision the decision classification gives to the user.
3. The document holds no fact the agent looked up about the project.
4. A project term used with the project's meaning counts as the project's, not as a fact the agent looked up.
5. Where a word of the user's clashes with a project term, the document records the clash and uses the project's term only with its meaning.

## Output

A grid: one row per item and one column per rule. Each cell is PASS or FAIL. A rule passes any item it doesn't apply to. A FAIL quotes the words that fail. A PASS for rules 1 and 2 on an item they apply to quotes the source of each part of the statement, or the marking that shows that part as the agent's. A PASS missing a quote it needs is a FAIL. Judge nothing outside these rules.
