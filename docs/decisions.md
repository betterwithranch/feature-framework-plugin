# Decision log

Every decision about this framework, one entry each, in number order. The log is append-only: no entry is ever edited or deleted. A changed decision gets a new entry that says which entry it replaces, and the old entry stays, marked "Replaced by Dn". This file is the only copy of the framework's decisions.

Numbers missing from the sequence (D18, D21–D25) were used on branches that haven't been merged.

D1  Make the level of work explicit
      Replaced by D36.
      Decided 2026-10-27. The current level and what finishing it means are always stated. The agent works only at the current level and raises alternatives only at that level. Going down a level needs the user's explicit agreement; partial agreement or momentum doesn't count. Anything that belongs to a lower level is set aside, not developed. Work moves top-down through a defined set of levels, and every later decision is expressed in terms of those levels. Why: when something is ambiguous the agent resolves it by producing something concrete, reads partial agreement as permission to go deeper, and the gaps surface only as the user's corrections after the detail exists.

D2  Build a reusable framework, not session-scoped agreements
      Decided 2026-10-27. The levels and their rules are a reusable framework that outlasts any single session. Its form, likely a plugin for Claude Code and Codex as codeguard is, is decided at the Design level. Agreements are recorded in this repository as they are made. Why: agreements made in one session were lost to the next, so the same decisions were made again.

D3  Refine committed features along one axis: altitude
      Decided 2026-10-27. The framework refines a feature the user has already committed to, from intent down to build. Commitment is not a level. Hypothesis and success criteria sit at the top level, incremental slices near the bottom, and invariants and non-goals are constraints each level adds to. Why: corrections in past sessions were altitude errors, detail built before the level above it was settled; commitment was not the problem.

D4  Cover feature development only
      Decided 2026-10-27. The framework is for feature development. Exploratory work, performance optimisation, data migrations, infrastructure and tooling changes made for other reasons are non-goals. Work a feature needs, such as a migration for its own data, is part of the feature. A question only an experiment can answer is handed off, and only its answer comes back. Other kinds of change need their own process. Why: spikes, performance work, data migrations and infrastructure changes have different goals and checks from feature work.

D5  End at working code, verified locally or in CI
      Decided 2026-10-27. Scope ends at working code verified locally or in CI. Deployment, opening PRs and other automation are non-goals for now, and can be added later as separate decisions. Why: the goal is to go from a prompt to working code without being pulled back in, not a full automation pipeline.

D6  Ask only feature-specific design questions
      Decided 2026-10-27. Design covers only decisions this feature raises. General practice is codified once, in codeguard, codeguard-rules and project invariants, and cited rather than asked again. Codifying general practice is ongoing work outside each feature. Why: the same general questions were answered again on every feature.

D7  Deliver features as narrow vertical slices
      Decided 2026-10-27. A feature ships as narrow vertical slices, each working end to end and releasable on its own, behind a feature flag if needed. Completing a layer never counts as success. Each slice passes an end-to-end check, possibly narrowed. Why: building by layer hides integration problems and lets scope grow.

D8  Verify everything automatically
      Decided 2026-10-27. Every verification is automated, with tests, Playwright, an LLM judge or a combination. A check that needs a person doesn't count. End-to-end tests simulate the user with a scripted conversation. Why: a check that needs a person keeps the person involved.

D9  Block questions that belong to a lower level
      Decided 2026-10-27. A question that belongs to a lower level, raised by the user or the agent, is recorded for the level that owns it and not answered. Open ones are listed in `docs/open-questions.md`. Each level needs a clear statement of what is and isn't its responsibility. Why: answering lower-level questions early is how detail gets built before the level above is settled.

D10  Build the framework with the framework
      Replaced by D37.
      Decided 2026-10-27. The framework is built with its own levels and gates, starting with its own Outcome. Decisions recorded before the framework's Outcome was approved, such as the candidate levels, are checked against it before they are treated as settled. Why: rules that the builder doesn't follow while building them get violated.

D11  Give every document one purpose
      Replaced by D38.
      Decided 2026-10-28. Every file has one purpose and holds only content that serves it. History and dates belong only in decision records. Instructions the framework uses on features are written as Claude skills under `skills/`, with no history, dates or status. The rules are in `CLAUDE.md`. Content that doesn't fit a file's purpose moves to the file whose purpose it serves. Why: files mixed records, history and instructions, which made them hard to read and to find things in.

D12  Run each gate review three times and act on the union
      Decided 2026-10-28. Each gate review runs three times independently. Every finding from any run is acted on. A finding that only some runs raise shows where the review instructions need to be clearer. A review passes when all three runs report no findings. Why: a single review run missed findings that another run of the same prompt caught.

D13  Enforce goals and the decide-or-ask rule with hooks
      Replaced by D44.
      Decided 2026-10-28. `docs/goals.md` holds the goals and the decide-or-ask rule. A SessionStart hook (startup, resume, compact) and a UserPromptSubmit hook load it into context. A Stop prompt hook blocks ending a turn on a request to approve something already decided. The goals survive compaction and are restated on every prompt; the Stop hook costs one small model call per turn, may misjudge, and is tuned against real sessions like any other instruction. Why: an assessment of the session that built level 1 found about 30 user corrections and about 10 unnecessary approval requests in 22; rules written in documents were not followed because nothing loaded or enforced them, and the goals drifted.

D14  Autonomy policy and MVP first
      Replaced by D39.
      Decided 2026-10-28. The framework includes an autonomy policy: what the agent decides alone, what it asks, and the stop condition and budget for each gate. Every recorded rule the framework depends on is enforced by a hook or a check, not only written down. The framework ships as a minimal version and is tried on one real feature before levels 2–5 are refined. Gates run unattended to their stop condition; whether every level needs the user's approval, or only open decisions do, is the user's call. Why: level 1 took about 45 user turns and about 70 review runs; autonomy worked when the agent had a measurable stop condition and failed when each step waited on the user.

D15  The user approves only open decisions
      Replaced by D26.
      Decided 2026-10-28. A level moves on when its gate passes. The user is asked only to settle decisions no one has made, or conflicts between agreed things. The framework's level 1 Outcome is approved. Levels run back to back without the user unless a gate raises an open decision. Why: requiring the user's approval at every level made interaction mandatory and was a main source of handholding (D14).

D16  Fix findings through the write skill, and stop a gate after four rounds
      Replaced by D35.
      Decided 2026-10-28. A gate's findings are fixed with the write skill for that level: its rules apply to the fix, and its after-a-fix self-check runs before the next round. A gate stops after four rounds that don't pass; the next step is to look for a conflict or ambiguity between the instructions involved, report it, and fix the instructions, not patch the document again. This amends D12: a review still passes when all three runs are clean, but runs at most four rounds. Why: the level 1 Outcome review ran twelve rounds after approval, each finding new issues often caused by the previous round's fixes, which were patched in without the write skill; the rounds also hid a conflict in the instructions.

D17  Dogfood first, then apply the framework to codeguard step 32
      Replaced by D37.
      Decided 2026-10-28. Building the framework with itself is the main path; its levels are written and gated in order with its own skills. When the framework is done, it is applied to codeguard plan step 32, change classification, as its first test on a product feature. This replaces the "tried on one real feature before levels 2–5" point of D14. MVP first means the smallest framework that carries its own build, not a pause after level 1. Why: D14 changed the order set by D10 without the user agreeing to it.

D19  An ambiguity is asked
      Decided 2026-10-28. Choosing between readings of something agreed or codified, when the reading changes the result, is the user's decision. The user is asked, and the answer is written into the record it clarifies. The work never picks a reading on its own. Why: the Outcome allowed clarity questions only before code starts while also saying the user is asked when blocked by a decision no one made, so an agreed thing with two readings had no rule.

D20  One classification of who decides
      Replaced by D42.
      Decided 2026-10-28. `skills/references/decisions.md` is the single source for who makes each decision, at every level and for decisions written anywhere, including plans, notes and memory. The user decides what users get, anything that creates, changes or overrides an agreement or codified rule, tools and external dependencies, hard-to-reverse or outward-facing choices, and trade-offs between goals. The work decides what follows from something agreed and reversible build choices within it, and records them: in a planning level's document, or, in Build, in the code and tests. Its decisions never become codified rules. When unsure, the user decides. A decision that replaces an earlier one removes it; only final decisions are kept. Why: no document said which decisions need the user, so rules settled it case by case and drifted both ways.

D26  Approve each level
      Replaces D15.
      Decided 2026-11-02. A level moves on only when its review passes and the user approves it. Approval is the user saying so; a correction, a question or "looks good, but" isn't approval. The levels approved this way are Outcome, Behaviour, Design and Slices; approving Slices lets Build start. Each level produces its own document only; working code is the result of Build. Approving a level makes the user's decisions and answers in it agreed: nothing in them is asked again, except for clarity or to resolve a conflict. The work's decisions in it stay the work's. All decisions need approval; fixes that aren't decisions don't. Why: the user said "each level needs approval before the next level should begin. that should be explicit."

D27  Play back before acting; interview before drafting
      Decided 2026-11-03. Before the work acts on anything from the user that could change the project, it plays back, in its own words, what it understood, and waits for the user to confirm. This covers a level, an instruction, a decision or a correction, whether or not it looks clear. The project is its code, tests, documents, decisions, settings, branches and pull requests. A plain answer to the work's own question is acted on without another playback; something that changes nothing needs no playback. Anything that could be read more than one way is put to the user as a choice between readings, in a message of its own after the playback, one at a time. A correction gets a fresh playback of the corrected parts. Before a level's document is written, at every level before code, the work interviews the user one question at a time and waits for each answer; the next question is chosen from what the answer settles; each question carries the work's recommended answer and can be answered by letter. The work looks up facts itself and asks only for decisions. It then plays back what it understood the user wants at that level, and the document is written only after the user confirms. The level's review also checks that every statement in the document is something the user said or agreed, or something marked as the work's; that every fact marked as the work's is true of the project; and that no statement can be read two ways that would change what gets built. These techniques are adapted, with thanks, from the Superpowers brainstorming skill (obra/superpowers), Matt Pocock's grilling and to-spec skills (aihero.dev) and Cursor's pstack poteto-mode skill; Pocock's rounds of independent questions were considered and not taken. The framework carries its own copy and doesn't load those skills. Why: the main failure was misalignment, the user saying something clear and the work building something different; the user said "play back before drafting should be in the framework to catch misalignment early", "playback anything that could impact the project", and asked for one question at a time because a follow-up on one of several questions makes the exchange messy.

D28  One branch and PR per level
      Decided 2026-11-02. Each level of the framework's own build is on its own branch, with its own pull request against `main`. Work on the next level starts when the user approves the level. Why: the user chose one branch and PR per level so the work can be tracked.

D29  Readable at a glance
      Decided 2026-11-03. Every document and message meant for a person follows these rules: one decision per question; one question at a time, the next waiting for the answer; a question gives the reader enough to answer without asking back, a concrete example of each option in the project's own terms and what each costs, and process notes aren't supporting detail; a short title; at most two short background sentences; two or three one-line options; short bullets under `## ` subheads with a blank line around each subhead; no walls of text. The framework carries its own copy of these rules; where it keeps them is decided at Behaviour and Design. Why: the user said "it is imperative that anything played back is in clear human readable form" and "any document or message that is for human consumption needs to be optimized for human readability."

D30  Where found facts live
      Decided 2026-11-03. A fact the work found in the project appears only in a level that allows it. Outcome: none; a project fact there means design leaked up. Behaviour: only facts about what users get today, where the new behaviour keeps or changes it, nothing about code. Design: the main home, facts about the code, data, services and interfaces the design builds on. Slices: Design's facts carried over, plus facts about how the project is built and tested, no new design facts. Build: no document; the code and tests are the record. In every level that allows them, a fact is marked as the work's, checked against the project by that level's review before the user is asked to approve, and seen by the user at approval. A wrong fact is a finding. Why: the user said facts "don't belong in all levels" and, where recorded, "need to be reviewed by an independent agent ... and would then be reviewed by the user"; he agreed the levels as proposed.

D31  A decision holds within its scope
      Decided 2026-11-03. A decision applies only within its stated scope: "all files use streaming" covers a second file; "file 1 uses streaming" doesn't. The work's decision in one feature is guidance, a preferred default, for the same decision in a later feature, which is made again and recorded again, citing the earlier one. An agreement or codified rule whose scope already covers the later case leaves nothing to decide. Why: the user said the next feature "should use the previous decision as guidance for a preference, but it shouldn't apply it to other cases that aren't part of the original decision's scope."

D32  Questions per level are tracked, not targeted
      Decided 2026-11-03. The number of questions the work asks the user at each level is recorded for every feature, so the cost of the interview can be seen. No number counts as a failure. How the count is kept is decided at Design. Why: the user said "we should measure for tracking, but not enforce any expected number of questions"; a target would push the work to skip questions it should ask.

D33  Complete requirements and verification
      Decided 2026-11-03. A requirement is complete when its verification can be written in full and run, with nothing left to ask the user. A verification is complete when it names what is checked, how, and what result passes. Anything missing from either is asked, one question at a time, unless the work can find it out. A level's document speaks of requirements, how they're verified, and "a level"; the Outcome names no lower level, nothing a lower level holds, and no found facts per level. Why: the user chose this standard for a complete requirement, and said "we shouldn't reference design at all in outcome level 1. We should reference requirements and verification."

D34  Nothing is guessed
      Decided 2026-11-03. A fact is looked up. A decision of the user's is asked. A reading is asked. Anything the work can't settle one of those ways is put to the user. A level's document uses the project's terms with the project's meanings; when a word of the user's clashes with one, the playback names the clash, and after the user confirms, the document keeps the project's term for the project's meaning, uses a distinct phrase for the user's, and records the clash where the user sees it. Why: the user said "nothing should ever be guessed."

D35  Four review rounds per approved version; decisions need approval
      Replaces D16.
      Decided 2026-11-03. A level's review has four rounds against the version the user last approved; the work changing the document doesn't reset them. Findings are fixed with the level's write skill, including its after-a-fix self-check. Fixes that aren't decisions don't need approval; all decisions need approval. A fix is not a decision only when it restores the document to something already agreed and cites it; a new or changed claim, scenario or measure, a reading nothing decided, or dropping something a reviewer objected to is a decision, played back and approved one at a time. When the rounds are spent, the work stops and brings the user the findings and a proposed instruction fix; changing the instructions is the user's decision. Why: the user said "the rule is 4x for the current version last approved by me. you changing the file does not reset this" and "fixes that aren't decisions don't need approval. all decisions need approval."

D36  Make the level explicit
      Replaces D1.
      Decided 2026-11-02. The current level and what finishing it means are always stated. The work stays at the current level and raises alternatives only at that level. Work moves to the next level only when the current one passes its review and the user approves it. Anything that belongs to a lower level is set aside, not developed. Why: D26 sets how a level moves on.

D37  Dogfood the framework
      Replaces D10. Replaces D17.
      Decided 2026-10-28. The framework is built with its own levels and gates, starting with its own Outcome; this is the main path. When the framework is done, it is applied to codeguard plan step 32, change classification, as its first test on a product feature. Why: D17 settled the order D10 left open; one record holds both.

D38  One purpose per document; only current decisions kept
      Replaces D11.
      Replaced by D41.
      Decided 2026-10-28. Every file has one purpose and holds only content that serves it. No file keeps history: a replaced decision or rule is removed, and only what is current remains. Instructions the framework uses on features are Claude skills under `skills/`. The rules are in `CLAUDE.md`. Why: the user asked to keep only final decisions.

D39  MVP first
      Replaces D14.
      Decided 2026-10-28. The framework is the smallest version that carries its own build. A level is not refined beyond what the next level needs. Every recorded rule the framework depends on is enforced by a hook or a check where one can enforce it. Why: D17 replaced D14's "tried on one real feature first" point, and who decides what at each gate is set by D20 and D16.

D40  One append-only decision log in the repo
      Decided 2026-11-04. The framework's decisions live in this repository as one append-only log, `docs/decisions.md`. Nothing in it is ever edited or deleted. A changed decision gets a new entry that names the entry it replaces, and the old entry stays, marked "Replaced by Dn". The playbook history and the vault decisions file no longer hold this framework's decisions; the log is the only copy. Why: a record that is edited or deleted stops being a record, and keeping decisions beside the rules they govern lets one review check both.

D41  One purpose per document
      Replaces D38.
      Decided 2026-11-04. Every file has one purpose and holds only content that serves it. History lives only in the decision log, which keeps every decision under D40. Everywhere else a replaced rule is removed, and only what is current remains. Instructions the framework uses on features are Claude skills under `skills/`. The rules are in `CLAUDE.md`. Why: D40 keeps replaced decisions in the log; the rest of D38 stands.

D42  One classification of who decides
      Replaces D20.
      Decided 2026-11-04. `skills/references/decisions.md` is the single source for who makes each decision, at every level and for decisions written anywhere, including plans, notes and memory. The user decides what users get, anything that creates, changes or overrides an agreement or codified rule, tools and external dependencies, hard-to-reverse or outward-facing choices, and trade-offs between goals. The work decides what follows from something agreed and reversible build choices within it, and records them: in a planning level's document, or, in Build, in the code and tests. Its decisions never become codified rules. When unsure, the user decides. Where a decision is written into a level document, code or notes, a decision that replaces it removes it there; this framework's own decision log keeps both under D40. Why: D40 makes the log append-only; the rest of D20 stands.

D43  Settings hold no prompts; prompts and docs are separate
      Decided 2026-11-04. Settings files hold no prompts. Each prompt is its own file that settings references. Agent prompts and human docs are separate files, each written for its reader: a prompt gives an agent direct instructions; a doc explains to a person. Duplication between them is kept to a minimum, and no hook points at a human doc. Why: documentation and agent prompts have different audiences.

D44  Enforce goals and the decide-or-ask rule with hooks
      Replaces D13.
      Replaced by D46.
      Decided 2026-11-04. `.claude/prompts/goals.md` holds the goals and the decide-or-ask rule as the agent's prompt; `docs/goals.md` explains the goals to people. A SessionStart hook (startup, resume, compact) and a UserPromptSubmit hook load the prompt into context. A Stop prompt hook blocks ending a turn on a request to approve something already decided. Every recorded rule the framework depends on is enforced by a hook or a check where one can enforce it. Why: D43 separates prompts from docs; the rest of D13 stands.

D45  Work under both Claude Code and Codex
      Replaced by D47.
      Decided 2026-11-04. Everything the framework ships works under both Claude Code and Codex: its prompts, its checks, and the settings that load them. Nothing depends on a feature only one host has. Why: the user said "this solution cannot be claude code only. It needs to support both claude and codex. this requirement needs to be added to avoid future breaking changes."

D46  Enforce goals and the decide-or-ask rule with hooks, on both hosts
      Replaces D44.
      Decided 2026-11-04. `hooks/prompts/goals.md` holds the goals and the decide-or-ask rule as the agent's prompt; `docs/goals.md` explains the goals to people. SessionStart and UserPromptSubmit hooks load the prompt into context, under Claude Code from `.claude/settings.json` and under Codex from `.codex/config.toml`. The Stop check is a command hook, `hooks/stop.py <host>`: it reads its prompt from `hooks/prompts/stop-check.md`, asks the host's own CLI on its smallest model (`claude -p --model haiku`, `codex exec --model gpt-6-luna`) whether the last message asks to approve something already decided, and blocks the stop with the reason. It respects `stop_hook_active`, prints one JSON object both hosts read, and exits 0. Settings hold no prompts. Every recorded rule the framework depends on is enforced by a hook or a check where one can enforce it. Why: the user chose a command hook for the Stop check (FF-32 A), since a prompt hook keeps its prompt in settings and exists only under Claude Code; D45 needs both hosts.

D47  The framework's own code works under both Claude Code and Codex
      Replaces D45.
      Decided 2026-11-04. Supporting both Claude Code and Codex is required only of the code the framework ships to enforce itself: its hooks, checks, skills and the settings that load them. The framework sets no host requirement for a feature; each feature has its own. Why: the user said "working in claude and codex is a requirement for the *code* generated in the framework, not a requirement for all future changes in all coordinators... each feature has its own claude/codex requirements that the framework does not dictate. But, if the framework is going to implement code in the form of hooks or skills to help enforce itself *THAT* code should support both."
