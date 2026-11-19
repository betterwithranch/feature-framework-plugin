# Plugin

The framework ships as one plugin with three features: decision making, coordinator and feature building. Decision making and coordinator are building blocks that work with or without feature building.

## What each feature owns

| Feature | Owns |
| --- | --- |
| Decision making | The decisions check: a fresh judge applies the recorded decisions to a question before it reaches the user, so nothing is asked that a decision already answers. The question check: a script and a fresh reader make sure a question stands alone and comes only from a Conflict or Not covered verdict. The gate: one hook that refuses a question until the checks have passed it. The decision-file shape and the script that checks it. The tests for all of these, shared by every user of the checks. The checks apply only to questions, so changes are validated by a code review tool such as codeguard, not by the checks, and agents follow the repository's code and architecture docs |
| Coordinator | The coordinator's rules, encoded as the plugin's own skills, hooks and templates: how a coordinator runs its sessions, tracks threads and enforces them, and handles open questions. The session tracker: an artifact the user views, following a template the plugin defines. Simple decision checking. The board templates |
| Feature building | The levels in the [README](../../README.md): the skills that write and review each level's document, the references they share, and each level's gate |

## How each is used alone

### Decision making

Any Claude Code session sets two things: its list of decision files and, if it posts questions to a board, its workstream. The gate then refuses a question that the checks have not passed. It needs no coordinator and no feature building.

It needs one thing from the others: a template for the form of a question, which the question check verifies a question against. A coordinator gets its board templates from the coordinator feature; any other user supplies its own.

### Coordinator

The basic coordinator and session tracker works with no decision making and no feature building. It does its own simple decision checking. It needs nothing from the other features.

With decision making, the coordinator runs the decisions check and the question check on every question before it reaches the user. This upgrades the basic coordinator and doesn't replace it.

### Feature building

It runs the levels and their gates without the other two features. Without decision making, nothing checks a question against the recorded decisions before it reaches the user. It needs decision making's checks only for a question it would ask the user, and nothing from the coordinator.

## Decisions

A feature's decisions are recorded in the scope that binds them:

| Decisions that bind | Recorded in |
| --- | --- |
| The plugin's users alike, including how decision making works | The Shared decision file, in this repository |
| Feature building only | The Feature framework decision file, in this repository |
| Any coordinator | The coordinator feature's own rules, in this plugin, and nowhere else |
| One repository only | That repository's architecture docs |

Another repository links to the Shared decision file for the decisions that bind it. This repository is public, so the file names no private repository, person or id.

## Build order

1. The basic coordinator and session tracker, as a local copy, then delivered through the plugin.
2. Decision making.
3. The rest of the coordinator feature, and feature building. Neither waits on the other.

Why:

- The basic coordinator runs locally first, so delivering the plugin holds up no other work. Decision making then upgrades it and doesn't replace it.
- Feature building and the coordinator's other work both send their questions through decision making's checks, so they start once it lands.

## Owners

Each named owner is a feature, so ownership doesn't depend on a session that ends. An owner marked proposed is not yet agreed.

| Item | Owner |
| --- | --- |
| Board templates | Coordinator |
| The tracker template the basic coordinator follows | Coordinator (proposed), defined in this repository |
| The shared tests | Decision making (proposed) |
| The decision checks' rules and tests | Decision making |
| A coordinator's session decision file | That coordinator |
| A user's list of decision files and its board workstream | That user of the checks |
