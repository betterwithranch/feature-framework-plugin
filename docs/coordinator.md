# How a coordinator runs

For a person starting or reading a coordinator session. It explains how the coordinator works; the rules it follows are in the skill's references and are not repeated here. Start a coordinator as the [start-coordinator skill](../skills/start-coordinator/SKILL.md) says.

## The backlog

A coordinator keeps one backlog: an ordered list of the pieces of work it tracks, called items. Each item has an id, a title, a state, a next step and, when it is waiting, what it waits on. Nothing else goes in the backlog, so a person can read it in a minute and see what is next.

The ids and states give you a way to follow the work. The id in a worker session's name and tags is the id of the item it works, and its name says what the session is for, so you can open the sessions list and match each session to its item and role. The thread cards on the board name their item the same way, so the board, the backlog and the sessions agree.

The backlog's rules are in [backlog.md](../skills/start-coordinator/references/backlog.md): what an item is, its id, its fields, its states, what happens to finished items, and how sessions and thread cards name items.
