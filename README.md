# Feature development framework

A reusable framework for taking a feature you've decided to build from intent to working code, one level at a time, so the build doesn't pull you back in.

Status: level 1 (Outcome) of the framework itself has passed its review gate and awaits approval. Everything else here is agreed direction or candidate content for later levels.

## Root cause (agreed 2026-10-27)

When something is ambiguous, the agent resolves it by producing something concrete (a plan, a template, code), because specifics look like progress. Nothing establishes which level the work is at or what finishing that level means, so the agent reads partial agreement as permission to go deeper. The gaps then surface only as your corrections, after the detail exists.

## Direction (agreed 2026-10-27)

Make the level explicit and treat it as a constraint:

- The current level and what finishing it means are always stated.
- The agent works only at the current level and raises alternatives only at that level.
- Going down a level needs your explicit agreement. Partial agreement or momentum doesn't count.
- Anything that belongs to a lower level is set aside, not developed.

## Framework decisions (agreed 2026-10-27)

- The levels are a reusable framework, not session-scoped. Their form (likely a Claude Code and Codex plugin) is decided later.
- One axis: altitude. The framework refines a feature you've already committed to, from intent down to build.
- Exploratory work (spikes, experiments) is a non-goal; a question only an experiment can answer is handed off.
- Scope ends at working code verified locally or in CI. Deployment and opening PRs are non-goals for now.
- The framework is for feature development only. Performance optimisation, data migrations, infrastructure and tooling changes made for other reasons are non-goals. Work a feature needs is part of the feature.
- Design is feature-specific. General practice is codified once (codeguard, codeguard-rules, project invariants) and referenced, not asked again.
- Vertical slices only. Completing a layer never counts as success.
- Every verification is automated (Playwright, an LLM judge, or both). A check that needs a person doesn't count.
- Each level blocks questions that belong to a lower level: they're recorded for the owning level, not answered.
- The framework is built with the framework (dogfooding).

## Candidate levels (to be checked against the approved Outcome)

| Level | Produces | Proof |
| --- | --- | --- |
| 1. Outcome | Who the feature is for, what it achieves, end-to-end scenarios | Automated end-to-end tests through the real surface |
| 2. Behaviour | Every rule and edge case, with examples, plus non-goals | Tests at the narrowest surface where each rule is observable |
| 3. Design | Decisions only this feature raises, each decided or a non-goal; general rules cited | No open decision; nothing restating a general rule |
| 4. Slices | Ordered vertical slices, each naming the scenario it extends and the cases it makes pass | Coverage of every scenario, case and decision; slice guideline met |
| 5. Build | The code for one slice | Assigned cases pass, earlier slices still pass, project checks clean |

Candidate gate rules: each planning level ends at a gate; an independent reviewer checks the level on its own; your approval closes it. Build never changes the tests it builds toward.

## Set aside for later levels

| Question | Owning level |
| --- | --- |
| Where the e2e sample project lives (separate repo, or a fixture in the plugin repo) | Design |
| Where a feature's level artifacts are stored | Design |

## Files

- `level-1/outcome.md`: the framework's own Outcome.
- `level-1/writing-guidance.md`: how to write a level 1 artifact.
- `level-1/review-prompt.md`: the level 1 gate review prompt.
