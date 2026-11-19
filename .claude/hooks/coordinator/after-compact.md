# After compaction

Your context was just compacted. The summary was written before compaction and is a lead, not the current state. Before anything else, in this order:

1. Read your rules again in full, as your launch message below names them: the Coordinator Playbook, or the plugin's coordinator skills once those replace it. What you remember of them from before compaction doesn't count.
2. Read again your workstream's card, your coordination doc and your notes doc, as your launch message says.
3. Make the board consistent with the live state before you do any other work:
   - Read the board. List the sessions you started (`list_sessions` with `children`), and read the latest turn of each worker that is still active.
   - Each thread card waits on something that is still live: a question still open on the board, a task not yet done, or a worker session that is neither finished nor archived. When what a thread waited on has finished, handle it as the rules say. A thread that waits on nothing has stopped. Give it its next step.
   - Each open question is still valid. Questions that were answered are recorded and then removed. Questions that are no longer valid are removed.
   - Finished threads, answered questions and done tasks are off the board, after their decisions are recorded.
   - Everything the summary says is blocked on the user is on the board, and Waiting on you (N) matches the open questions plus the tasks.
   - Each decision in the summary is recorded in the doc that owns it. Record any that isn't.
   - Where the summary and the live state disagree, the live state wins.
4. Before proposing anything, check it against the summary's Ruled out list and the recorded decisions, so nothing settled is revisited.
5. Then carry on from where the summary says the turn stopped. Your board already exists: don't make a new one, and don't stop to wait for the user as the launch message's last steps say.
