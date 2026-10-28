# Design

Builds the [Behaviour](2-behaviour.md) of the [Outcome](1-outcome.md). "You" decides as the [decision classification](../../skills/references/decisions.md) sets; "the work" makes the rest. A feature's levels are written in the product project the framework is installed in.

## Decisions

| # | Decision | Made by | Follows from | Builds |
| --- | --- | --- | --- | --- |
| D1 | The framework is one Claude Code plugin: `.claude-plugin/plugin.json`, `skills/`, `agents/` and `hooks/hooks.json` at the repo root. | You | [0021](../decisions/0021-claude-code-plugin.md) | R1 |
| D2 | A feature's level documents are `docs/features/<feature>/1-outcome.md`, `2-behaviour.md`, `3-design.md` and `4-slices.md` in the product project. | You | [0022](../decisions/0022-feature-documents-location.md) | R2 |
| D3 | Each answer you give is written into the level document, decision record or codified rule the question is about, and to its own record in the product project's `docs/decisions/`, named `NNNN-<slug>.md` and listed in that folder's `README.md`. | You | [0022](../decisions/0022-feature-documents-location.md) | R9, R13 |
| D4 | Each planning level has a write skill and a review skill that share one reference file holding what the level's document contains and its criteria: `write-<level>`, `review-<level>` and `skills/references/<level>.md` for outcome, behaviour, design and slices. | The work | [0011](../decisions/0011-one-purpose-per-document.md) | R2, R10, R11, R14 |
| D5 | A `feature` skill runs a feature: it writes each level with its write skill in the order Outcome, Behaviour, Design, Slices, runs the level's gate, and starts the next level only after the gate passes. | The work | Goal 2 | R1, R5 |
| D6 | A gate round runs the `level-reviewer` agent three times in parallel. Each run is given only the review skill, its reference, the decision classification, the level's document, the passed levels above it and the files the document cites. | The work | [0012](../decisions/0012-three-review-runs.md) | R3 |
| D7 | The `level-reviewer` agent may only use Read, Glob and Grep. | The work | [0012](../decisions/0012-three-review-runs.md): runs are independent | R3 |
| D8 | Each run's report is written to `docs/features/<feature>/reviews/<n>-<level>-round-<r>-run-<k>.md`. | The work | [0022](../decisions/0022-feature-documents-location.md) | R3, R4 |
| D9 | When a round has findings, a `level-writer` agent fixes the union of them with the level's write skill, and a new round runs. | The work | [0016](../decisions/0016-fix-through-the-write-skill-and-stop-after-four-rounds.md) | R4 |
| D10 | When all three runs in a round report no findings, the `feature` skill writes `docs/features/<feature>/reviews/<n>-<level>-passed.md`, naming the round. | The work | [0022](../decisions/0022-feature-documents-location.md) | R3, R5 |
| D11 | After the fourth round with findings, the `feature` skill stops the level. It reports which instructions conflict or are ambiguous, or which run keeps finding what, and a proposed fix. It asks you how the level continues and changes no document or instruction before you answer. | The work | [0016](../decisions/0016-fix-through-the-write-skill-and-stop-after-four-rounds.md) | E1, E2, E3, E18 |
| D12 | When a passed level's document changes, the `feature` skill deletes the passed file of that level and of every later level, gates the changed level again, then updates each later level with its write skill and gates it again, in order. | The work | Goal 2 | R6, R7, E13 |
| D13 | While the `feature` skill plans a feature, from starting its Outcome or going back to a level through D12 until Slices passes, it keeps a file `feature-planning` naming the feature in the current worktree's git directory, which is never committed. While that marker exists, the work's edits to the project's code and tests in that worktree are refused. | You | [0025](../decisions/0025-planning-marker-guards-code.md) | R15 |
| D14 | Hook commands are POSIX shell scripts in `hooks/` that use only tools on a stock macOS or Linux. The plugin adds no interpreter or package. | The work | Decision classification: adding a dependency is yours, and none is needed | R15 |
| D15 | The work asks you with AskUserQuestion, during the level that needs the decision and before its gate. Each question names the decision and the options. | The work | Goal 1 | R8, R20, R21, R22, E5, E6, E8, E11, E14, E15 |
| D16 | Before asking, every write skill and the `build` skill read the passed levels, `docs/decisions/`, and the project's codified rules: its `CLAUDE.md` files, `.codeguard/` and the codeguard rule packages it uses. They ask only about what none of them settles as D30 says, except for clarity or a conflict. | The work | [0006](../decisions/0006-feature-specific-design.md) | R12, R14 |
| D17 | Outcome, Behaviour and Slices documents end with a "Work decisions" section. Each entry states the decision and, when it follows from something agreed, a codified rule or a goal, cites which. A Design document records the work's decisions in its decisions table. | The work | Decision classification: the work records its decisions in the level's document | R26, E16 |
| D18 | Every write skill and the build skill say: a decision of yours is never written into a plan, note, memory, `CLAUDE.md` or rule before you make it; a decision of the work written into a plan, note or memory is also recorded in the level document, or the code and tests, it applies to; and a decision of the work is never written as a codified rule. | The work | Decision classification | R24, R27, R29 |
| D19 | The plugin's Stop hook blocks a turn that ends by asking you to approve applying fixes, rerunning a gate, committing, or moving to a step already agreed. | The work | [0013](../decisions/0013-enforce-goals-with-hooks.md), [0015](../decisions/0015-approve-only-open-decisions.md) | R25 |
| D20 | A `write-slices` skill, a `review-slices` skill and `skills/references/slices.md` define Slices: ordered vertical slices, each naming the Outcome scenario it extends and the cases it makes pass. Every rule, edge case, decision record and codified rule that applies to the feature is a case assigned to a slice. | The work | [0007](../decisions/0007-vertical-slices-only.md), [candidate levels](candidates.md) | R16, R23 |
| D21 | A `build` skill builds one slice at a time, in the order Slices gives. A slice is done when its assigned cases pass, every earlier slice's cases still pass, and the project's own test, lint and codeguard checks are clean. | The work | [0007](../decisions/0007-vertical-slices-only.md) | R16, R17 |
| D22 | The `build` skill changes a done slice's test only when Slices changes the cases assigned to it. | The work | Goal 3 | R19 |
| D23 | The `build` skill ends only when each Outcome scenario's end-to-end test passes. | The work | [0008](../decisions/0008-automated-verification-only.md) | R18 |
| D24 | During Build, the work names functions, files and tests itself and records those decisions only in the code and tests. When existing code conflicts with one of the work's decisions in a passed level, the work follows the existing code and updates the level, without asking. | The work | Decision classification: the work decides how to build within what's agreed | R28, E17 |
| D25 | When Build is blocked by one of your decisions, the `build` skill stops the slice and changes no code or tests for it. It asks you, then writes your answer into the level the decision belongs to with that level's write skill, and continues through D12. | The work | Goal 2 | E9, E10, E12 |
| D26 | The framework's own scenarios are `claude plugin eval` cases in `evals/`, run on demand. Each case builds its fixture with a scaffold script, replays a recorded conversation up to the turn it grades, and grades it with `tool_used`, `file_exists`, `regex` and `llm` graders. Acceptance test results are written to a file and graded from it. | You | [0023](../decisions/0023-scenarios-run-as-plugin-evals.md) | R18 |
| D27 | A plugin `PreToolUse` hook on Write, Edit, MultiEdit and NotebookEdit finds the git directory of the edited file's worktree and, when D13's marker is there, refuses the edit unless the file is Markdown or is under `.claude/` or `.codeguard/`. Level documents, decision records, codified rules and instructions are kept in those, so they stay editable. | The work | [0025](../decisions/0025-planning-marker-guards-code.md), [0013](../decisions/0013-enforce-goals-with-hooks.md) | R15 |
| D28 | When your answer replaces an earlier decision of yours, the skill that took the answer removes the earlier decision, or rewrites it to the new one, in the level documents in `docs/features/`, `docs/decisions/` (deleting a replaced record and its `README.md` entry), the codified rules, and the work's plans, notes and memory. | The work | [Decision classification](../../skills/references/decisions.md): a replaced decision is removed wherever it's written | E4 |
| D29 | The `build` skill asks you only when a slice is blocked by one of your decisions, and handles it through D25. | The work | Goal 1 | R22 |
| D30 | One of your decisions is settled only by what you agreed, in the passed levels, decision records and codified rules. The work's own decisions, plans, notes and memory settle none of them, and neither does a codified rule added by a commit with Claude Code's `Co-Authored-By: Claude` trailer that no decision record holds. | The work | [Decision classification](../../skills/references/decisions.md): a rule, principle or memory needs your agreement | E14 |
| D31 | A write skill records a question that belongs to a later level, with that level's name, in `docs/features/<feature>/open-questions.md` instead of answering it. The owning level's write skill reads the entries for its level, answers each in its document, asking you through D15 when the answer is one of your decisions, and removes the entry. | The work | [0009](../decisions/0009-block-lower-level-questions.md), [0022](../decisions/0022-feature-documents-location.md) | R10, R11 |

## Cited rules

| Rule | Covers |
| --- | --- |
| [Decision classification](../../skills/references/decisions.md) | R24, R25, R27, E7, E13, E15 |
| [0009 Block lower-level questions](../decisions/0009-block-lower-level-questions.md) | R10, R11 |
| [0015 No approval step per level](../decisions/0015-approve-only-open-decisions.md) | R5 |
| [0016 Fix through the write skill; stop after four rounds](../decisions/0016-fix-through-the-write-skill-and-stop-after-four-rounds.md) | R4, E1, E2, E3, E18 |
| [0019 An ambiguity is asked](../decisions/0019-ambiguity-after-code-starts-is-asked.md) | E8, E11 |

## Non-goals

- Codex support ([0021](../decisions/0021-claude-code-plugin.md)).
- A simulated user across a whole feature build, and running the evals in CI ([0023](../decisions/0023-scenarios-run-as-plugin-evals.md)).
- Refusing code changes made through Bash while planning. D27's hook guards the file tools only.
- A command-line tool, server or database of the framework's own.
