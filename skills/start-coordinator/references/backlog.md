# Backlog

What a coordinator's backlog holds and how its items, ids, states and worker sessions are named. Each rule is checkable: a backlog, a session or a thread card either meets it or doesn't.

## Item

- An item is one piece of work the coordinator tracks. A worker session does one item at a time and a thread holds one item at a time.
- The backlog is one ordered collection of items, in any form: a table, a list or a tracker. It is never split across several tables or lists.
- Order is priority, highest first. When a thread needs work, the coordinator takes the first item in `ready`.

## Id

- Format: `<prefix>-I<n>`, where `<prefix>` is the workstream's prefix and `<n>` is a positive integer without leading zeros. Example: `PL-I3`.
- The prefix is the one the workstream's question ids use. It has letters and digits only, no hyphen.
- Question ids are `<prefix>-<n>` with no letter after the hyphen. An item id always has the `I`, so no item id equals a question id.
- An id is unique within the workstream and never reused, including after the item is done or dropped. The backlog states the last number it issued; a new item takes the next number.
- A worker code, a PR number or a branch name is not an id. An item is always referred to by its id.

## Fields

An item has these fields and no others.

| Field | Holds |
| --- | --- |
| id | The item's id. |
| title | The result the item delivers, in 10 words or fewer. It does not change once set. |
| state | One of the states below. |
| next step | One action: what happens next, or for `parked`, what restarts it. Empty only when the state is `done` or `dropped`. |
| waits on | Set only in state `waiting`: one question id, one task for the user, one other item id, or one named worker session or PR. Empty in every other state. |

Everything else goes elsewhere:

- History and dates: the item's PR and commit log, or the version history of the document it changed. The backlog holds the present only.
- A decision: the document that owns its subject, such as a skill's references or the repository's architecture docs.
- An open question: a question card on the board, with a question id.
- What a thread is doing now or its plan: the thread's card on the board.

## States

The list is closed. Every item is in exactly one.

| State | Meaning | Enters when | Leaves when |
| --- | --- | --- | --- |
| `ready` | Can start now and has no thread. | The item is created with nothing blocking it, or what a `waiting` or `parked` item needed is resolved. | A thread takes it (`active`), or it is set aside (`parked`) or no longer wanted (`dropped`). |
| `active` | Held by exactly one thread. The thread's card names it. | A thread takes it from `ready`. | Its done check passes (`done`), it gives up the thread because something blocks it (`waiting`) or the coordinator sets it aside (`parked`), or it is no longer wanted (`dropped`). |
| `waiting` | Has no thread and cannot start until the thing in `waits on` is resolved. | It is created blocked, or an item gives up its thread because it is blocked. | What it waits on is resolved (`ready`), or it is no longer wanted (`dropped`). |
| `parked` | Set aside on purpose, with no thread. The coordinator skips it when taking the next item. | The coordinator sets a non-terminal item aside and writes the restart condition as its next step. | The restart condition holds (`ready`), or it is no longer wanted (`dropped`). |
| `done` | The item's own done check passed and the coordinator verified it. | An `active` item's work is verified. | Never. |
| `dropped` | Will not be done. | A non-terminal item is decided against. | Never. |

An `active` item whose thread is waiting stays `active`: the thread's card holds the wait, so `waits on` stays empty.

## Done and dropped items

- A `done` or `dropped` item is removed from the backlog in the turn it reaches that state. Its id stays retired.
- Its history lives in its PR and commit log, or the version history of the document it changed. The decision to drop it lives in the document that owns its subject.
- Its open questions move to the board's parked questions.

## Worker sessions and thread cards

- A worker session is named `<item id> <role>: <item title>`, with the title as in the backlog. Example: `PL-I3 writer: Define backlog rules`.
- Role is one of `writer`, `reviewer` or `tester`. The writer makes the item's change, the reviewer checks it in a session separate from the writer's, and the tester is a throwaway session that runs the change to try it.
- Its tags are `workstream:<prefix>`, `item:<item id>` and `role:<role>`.
- An item can have several sessions, one for each role. At most one unarchived session exists per item and role. A session replacing another for the same item and role takes the same name and tags.
- A thread card's heading is `T<n>: <item id> <item title>`. A thread card names exactly one item, and that item is `active`.
- Every `active` item is named on exactly one thread card.
