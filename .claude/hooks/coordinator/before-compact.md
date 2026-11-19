# Summary for a coordinator

This session is a workstream coordinator. Its value is knowing how the work has changed over time, so that nothing already decided, done or ruled out is revisited. Write the summary for the coordinator that continues after compaction: keep what it needs to keep coordinating and drop the rest. The board, the coordination doc, the notes doc and the worker sessions hold the detail. Point to them instead of copying them.

## Keep, in this order

1. Where things are: the workstream, this session's id, and links to the board, the coordination doc, the coordinator notes doc and the decision index.
2. Instructions and approvals the user gave in this session that still stand, word for word, each with what it covers.
3. Decisions made in this session: one line each, saying what was decided and the doc and section where it is recorded. Mark any decision that is not yet recorded.
4. Ruled out: approaches, options, questions and items that were rejected, withdrawn or superseded. Give one line each, with the reason, so none of them is proposed again.
5. Threads: for T1 and T2, the goal, where it stands now, what it waits on (a question id, a task, or a worker session id) and its plan of record. Also the parked threads, and the ids of parked questions.
6. The board: the id of each open question with its one-line title, each task for the user, and the next unused question number.
7. Live workers: for each session id, its item and thread, what it is doing, what the coordinator is waiting for from it, and its last report.
8. Open commitments: the PRs whose activity this session subscribed to, as owner/repo#number; each scheduled check-in, with its id and what it checks; and anything promised to the user or a worker that isn't done yet.
9. Where the turn stopped: the last event handled and the next step.

## Drop

- Threads and items that are finished and have their decisions recorded. Keep one line saying each is done and where its outcome lives.
- Workers that are archived, or whose PR merged or closed. Keep one line each at most.
- Worker briefs and reports, tool output, file and doc contents, and research. Anything that can be read again from a doc, the board or a session's transcript. Keep the pointer.
- Side work that changed neither a thread's goal nor a decision.
- Drafts and rewordings of questions. Keep only the posted question's id.
- Debugging steps and notes on how a tool behaved, unless they produced a rule.

## How to write it

- State facts as they stand now, not how they came about. Ruled out is the exception: it keeps the reason.
- Copy ids, links, session ids and PR numbers exactly.
- Where the conversation and a doc disagree about what was decided, say so. Don't pick one.
