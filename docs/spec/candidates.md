# Candidate content for later levels

Agreed before the framework's Outcome existed. Per [decision 0010](../decisions/0010-dogfood-the-framework.md), each item is checked against the approved [Outcome](1-outcome.md) at the level that owns it before it is treated as settled.

## Levels

The levels, what each produces and its proof are agreed in the [README](../../README.md). These details are still candidates:

- Design: general rules are cited; nothing restates a general rule.
- Slices: each slice names the scenario it extends and the cases it makes pass; every slice meets the slice guideline.
- Build: project checks are clean.
- Independent slices may be built concurrently.

## Gates

- Each planning level ends at a gate. An independent reviewer checks the level's artifact on its own. The user's approval closes the gate.
- A finding must point to the artifact and change what gets built. Hypotheticals are dropped: perfection is the enemy of done.
- Build never changes the tests it builds toward. A plan gap or a conflict goes back to the level that owns it.

## Outcome and Behaviour

- Outcome is a few scenarios through the real user surface (browser, API or CLI).
- Behaviour covers every rule and edge case, each tested at the narrowest point where it can be observed.
- Each slice passes an Outcome scenario end to end, possibly narrowed, by extending that scenario's test.

## Decision categories

For Design. Each feature's Design resolves every category as decided, a non-goal or not applicable, with a reason. The examples are decisions that surfaced mid-build in codeguard's week of 20 October 2025.

- Purpose and success: who is it for, what is the hypothesis, what number says it worked? Missed: "non-disruptive, 1 judge rule + N ast-grep rules" stated after work started.
- Scope and non-goals: what is in, what is explicitly out and why? Missed: "back-checking existing work is out of scope"; "drafts are temporary, no permanent tooling".
- Semantics: what exactly must the behaviour be, including edge cases, with examples? Missed: step 31 "touch it, own it; scope up, never to siblings"; comments and docstrings judged alone.
- Data model and ownership: what are the core types, and which is the source of truth? Missed: parse stream lines into discriminated unions; parse boundary data once.
- Placement and dependencies: which module or package owns it, which way do dependencies point? Missed: "codeguard is standalone; why are you linking otter?"
- Interfaces and extension points: what do callers see, which axes of variation are designed in now? Missed: judge provider (Claude, Gemini, Bedrock); rule tier (ast-grep, LSP, LLM).
- Frameworks and reuse: which existing library or helper does the work, used idiomatically? Missed: "don't wrap pydantic-evals"; "don't reinvent frameworks"; EvalRunner.
- Errors and failure modes: what fails closed, what degrades, what retries, who reports it? Missed: judge errors failing evals vs warnings; the label bypass.
- Configuration and facts: what is configurable, what are the defaults, which values must the plan supply? Missed: pin the judge model; the inference profile ARN; no ARN parsing.
- Security and data: what access is needed, what data is touched (PHI, secrets, tokens)? Missed: "evals don't hold PHI"; Logfire token scope.
- Performance and cost: what latency, CI time, token or dollar budget applies? Missed: "GitHub Actions bill by time"; "5x the LLM calls".
- Testing and verification: which tests prove each requirement, how is each check shown to fail? Missed: "automated test coverage is the only acceptable solution"; evals at 100% with no retries.
- Observability: what is logged, traced or measured, and who reads it? Missed: codeguard traces and costs to Logfire.
- Rollout and compatibility: how is it sliced, versioned, flagged, migrated and rolled back? Missed: "we cannot introduce a version that will break otter"; drop the lock in 0.6.0.
- Documentation: which docs change, and who reads them? Missed: "repo readers do not have access to the vault"; no line numbers in design docs.
- Operations and ownership: who runs, releases and maintains it, which session owns each area? Missed: two sessions owning the same rules; when to tag a release.
- A project can add categories. A discovery during build that fits no category adds one.

## Existing invariants apply in full

For Behaviour and Design.

- The project's existing invariants (CLAUDE.md, quality skills, codeguard rules) apply in full; a feature's documents can add constraints but never relax them.

## Run policy defaults

For Slices and Build.

- Proposed: open the PR when the slice's done commands pass; merge on green CI plus an independent review in codeguard and codeguard-rules; stop at merge-ready in otter.
