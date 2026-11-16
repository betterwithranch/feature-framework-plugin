# Coordinator decisions

Decisions for any coordinator, one per record. History lives in git.

## 1. Each coordinator has its own board

The board shows the coordinator's threads, its open questions and its parked questions. Work items and their status stay in the workstream's coordination doc, and the board never copies them.

Why: one board tracking several workstreams became a mess of confusion.

## 2. A thread holds several questions, in priority order, only its own

A thread may hold several open questions, in priority order, when all of them belong to that thread. When an item is superseded, its open questions move to Parked, where any thread picks one up once it is unblocked. Threads don't hoard work.

Why: a question on superseded work stays available to another thread once it is no longer blocked.

## 3. Decisions are recorded only in decision files

Every decision is recorded in the decision file for its scope, one per record, in this file's shape. A decision is never recorded in the vault, the Coordinator Playbook or a notes doc.

Why: the decision framework reads decisions from these files as it is built.

## 4. Each coordination doc owns its workstream's work

A workstream's coordination doc is the only place its work is tracked. The combined backlog is a read-only view of every workstream's items and dependencies, linking to the rows that own them.

Why: coordinators own their own work, and Craig needs one view of all of it to see the dependencies.

## 5. A doc is tracking, history or documentation, one kind per tab

Each doc, or each tab of a doc, is one of tracking, history or documentation. A doc that tracks work never points to another doc for that work's status.

Why: docs that refer to other docs doing the tracking caused the confusion.
