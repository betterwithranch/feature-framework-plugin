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

A workstream's coordination doc is the only place its work is tracked. The Workstreams page replaces the combined backlog as the one view across workstreams.

Why: coordinators own their own work, and Craig needs one page across workstreams to get them back on track.

## 5. A doc is tracking, history or documentation, one kind per tab

Each doc, or each tab of a doc, is one of tracking, history or documentation. A doc that tracks work never points to another doc for that work's status.

Why: docs that refer to other docs doing the tracking caused the confusion.

## 6. A worker reports to its coordinator with send_message

A worker reports with send_message to the coordinator session its brief names.

Why: a worker that only ends its turn notifies no one, so finished work went unnoticed.

## 7. Board threads and questions are cards

Board threads and questions are cards, never tables.

Why: a table scrolls sideways and its text can't be read.

## 8. The dashboard is the Workstreams page

The dashboard is the Workstreams page, the one page for getting every workstream back on track. The Index of what already exists is a tab of the Coordinator Playbook.

Why: coordinators find what already exists with the rules they read, and the dashboard keeps one job.

## 9. Craig starts each workstream's coordinator himself

Craig starts each workstream's coordinator himself.

## 10. Every coordinator starts from the Playbook's launch message

Every coordinator starts from the Playbook's one launch message. Its first result is its board, whose header lists the decision files it checks and records in.

Why: Craig doesn't have to work out the start-up process each time, and the board replaces a separate start-up report.

## 11. A worker gets its sources before it starts

A worker gets every source it reads before it starts and never attaches a repository itself.

Why: the permission check refuses a worker's own attach of a repository, because no one in the worker's session approved it.

## 12. A refused worker is replaced

A refused worker is replaced with a new one, never routed around. Craig never types into a worker's session.

Why: the check refuses a way round its refusal as undermining oversight, and typing into a worker's session violates the spirit of coordinators.
