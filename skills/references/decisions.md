# Decisions

Which decisions need the user and which the work makes. Every level applies this, for decisions written anywhere: level documents, code, plans, notes or memory.

## The user decides

A decision needs the user when it:

1. Changes what someone using the feature gets: its results, scope or non-goals.
2. Creates, changes or overrides something the user agreed, or a codified rule. This includes writing any new rule, principle or memory that governs later work.
3. Chooses a tool, or adds any external dependency.
4. Is hard to reverse or reaches outside the project, such as production data, a public interface, an external service, cost, security or privacy.
5. Trades one of the user's goals against another, and nothing agreed settles it.

## The work decides

The work makes a decision itself, and records it in the current level's document, when it:

1. Follows from something agreed, a codified rule or a goal. The record cites which.
2. Is how to build within what is agreed, reversible and local to the feature, such as naming, structure, algorithms or test layout.

## Always

- A decision the work makes never becomes a codified rule.
- When it's unclear which list a decision belongs to, the user decides.
- Between two conflicting agreements, the later wins only when both were made or agreed by the user. Otherwise the user decides.
