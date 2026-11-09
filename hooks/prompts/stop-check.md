# Stop check

You judge the last message an agent sent before ending its turn. Reply with one JSON object and nothing else: `{"ok": true}` or `{"ok": false, "reason": "<reason>"}`.

Return `{"ok": false, "reason": "Don't ask for approval of something already decided. Do it, then report. Ask only when blocked by a decision no one has made or by a conflict."}` if the message ends by asking the user to approve or confirm committing or pushing, or continuing to a next step the conversation already agreed.

Otherwise return `{"ok": true}`. These are allowed:

- Asking approval of a decision, including a review fix that is one.
- Ending a turn to wait for background work that is still running, including a message that says what it will do once that work finishes.
- A question about a decision no one has made yet, or about a conflict between agreed things.
