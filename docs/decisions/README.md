# Decisions

Architecture decision records. Each records one agreed decision, its context and consequences.

| # | Decision | Status |
| --- | --- | --- |
| 0001 | [Make the level of work explicit](0001-make-the-level-explicit.md) | Accepted |
| 0002 | [Build a reusable framework, not session-scoped agreements](0002-reusable-framework.md) | Accepted |
| 0003 | [Refine committed features along one axis: altitude](0003-single-altitude-axis.md) | Accepted |
| 0004 | [Cover feature development only](0004-feature-development-only.md) | Accepted |
| 0005 | [End at working code, verified locally or in CI](0005-scope-ends-at-working-code.md) | Accepted |
| 0006 | [Ask only feature-specific design questions](0006-feature-specific-design.md) | Accepted |
| 0007 | [Deliver features as narrow vertical slices](0007-vertical-slices-only.md) | Accepted |
| 0008 | [Verify everything automatically](0008-automated-verification-only.md) | Accepted |
| 0009 | [Block questions that belong to a lower level](0009-block-lower-level-questions.md) | Accepted |
| 0010 | [Build the framework with the framework](0010-dogfood-the-framework.md) | Accepted |
| 0011 | [Give every document one purpose](0011-one-purpose-per-document.md) | Accepted |
| 0012 | [Run each gate review three times and act on the union](0012-three-review-runs.md) | Replaced by 0036 |
| 0013 | [Enforce goals and the decide-or-ask rule with hooks](0013-enforce-goals-with-hooks.md) | Accepted |
| 0014 | [Autonomy policy and MVP first](0014-autonomy-policy-and-mvp-first.md) | Accepted, amended by 0017 |
| 0015 | [The user approves only open decisions](0015-approve-only-open-decisions.md) | Replaced by 0020 |
| 0016 | [Fix findings through the write skill, and stop a gate after four rounds](0016-fix-through-the-write-skill-and-stop-after-four-rounds.md) | Replaced by 0029 |
| 0017 | [Dogfood first, then apply the framework to codeguard step 32](0017-dogfood-first-then-codeguard-step-32.md) | Accepted |
| 0018 | [The framework outline](0018-framework-outline.md) | Accepted |
| 0019 | [An ambiguity is asked](0019-an-ambiguity-is-asked.md) | Accepted |
| 0020 | [Approve each level](0020-approve-each-level.md) | Accepted |
| 0021 | [Play back before acting; interview before drafting](0021-play-back-before-acting-interview-before-drafting.md) | Accepted |
| 0022 | [One branch and PR per level](0022-one-branch-and-pr-per-level.md) | Accepted |
| 0023 | [Readable at a glance](0023-readable-at-a-glance.md) | Accepted |
| 0024 | [Where found facts live](0024-where-found-facts-live.md) | Accepted |
| 0025 | [A decision holds within its scope](0025-a-decision-holds-within-its-scope.md) | Accepted |
| 0026 | [Questions per level are tracked, not targeted](0026-questions-per-level-are-tracked-not-targeted.md) | Accepted |
| 0027 | [Complete requirements and verification](0027-complete-requirements-and-verification.md) | Accepted |
| 0028 | [Nothing is guessed](0028-nothing-is-guessed.md) | Accepted |
| 0029 | [Four review rounds per approved version; decisions need approval](0029-four-review-rounds-per-approved-version.md) | Accepted |
| 0030 | [One classification of who decides](0030-one-classification-of-who-decides.md) | Accepted, amended by 0061 |
| 0031 | [Verifications test behaviour and pass independently](0031-verifications-test-behaviour-and-pass-independently.md) | Accepted |
| 0032 | [One verification for a requirement that holds across cases](0032-one-verification-for-a-requirement-that-holds-across-cases.md) | Accepted |
| 0033 | [Absolute terms have no exceptions](0033-absolute-terms-have-no-exceptions.md) | Accepted |
| 0034 | [Every requirement covered; structure is a later level's](0034-every-requirement-covered-structure-is-a-later-level-s.md) | Accepted |
| 0035 | [What a level's review checks](0035-what-a-level-s-review-checks.md) | Accepted |
| 0036 | [A review round: one run, then two more if it's clean](0036-a-review-round-one-run-then-two-more-if-it-s-clean.md) | Accepted |
| 0037 | [A level's document is written for those who build from it](0037-a-level-s-document-is-written-for-those-who-build-from-it.md) | Accepted, amended by 0046 |
| 0038 | [Only an absolute term rules out exceptions](0038-only-an-absolute-term-rules-out-exceptions.md) | Accepted |
| 0039 | [Project terms aren't found facts](0039-project-terms-aren-t-found-facts.md) | Accepted |
| 0040 | [Review findings carry no impact rating](0040-review-findings-carry-no-impact-rating.md) | Accepted |
| 0041 | [Structure scripts and four scoped yes/no reviews](0041-structure-scripts-and-four-scoped-yes-no-reviews.md) | Accepted |
| 0042 | [The Scope review's rules](0042-the-scope-review-s-rules.md) | Accepted, amended by 0060 |
| 0043 | [The Clarity review's rules](0043-the-clarity-review-s-rules.md) | Accepted, amended by 0059 |
| 0044 | [The Verification review's rules](0044-the-verification-review-s-rules.md) | Accepted, amended by 0060 and 0062 |
| 0045 | [The Provenance review's rules](0045-the-provenance-review-s-rules.md) | Accepted |
| 0046 | [One project glossary](0046-one-project-glossary.md) | Accepted |
| 0047 | [Where the project glossary lives](0047-where-the-project-glossary-lives.md) | Accepted |
| 0048 | [The glossary review's rules](0048-the-glossary-review-s-rules.md) | Accepted |
| 0049 | [The approved measure 2 is replaced by two measures](0049-measure-2-replaced-by-two-measures.md) | Accepted |
| 0050 | [How the scenarios run is deferred to the level that writes the tests](0050-how-the-scenarios-run-is-deferred.md) | Accepted |
| 0059 | [No exception to an absolute term, anywhere](0059-no-exception-to-an-absolute-term-anywhere.md) | Accepted |
| 0060 | [A measure recorded only for tracking has no target](0060-a-measure-recorded-only-for-tracking-has-no-target.md) | Accepted |
| 0061 | [A later decision replaces an earlier one it disagrees with](0061-a-later-decision-replaces-an-earlier-one-it-disagrees-with.md) | Accepted |
| 0062 | [Verification rules 3 and 4 are bounded to what a scenario cites and names](0062-verification-rules-3-and-4-bounded-to-what-a-scenario-cites-and-names.md) | Accepted |
