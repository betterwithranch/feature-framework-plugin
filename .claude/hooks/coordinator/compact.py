#!/usr/bin/env python3
"""Compaction hooks for coordinator sessions.

PreCompact: prints before-compact.md, which Claude Code uses as instructions
for the compaction summary.
SessionStart (compact): prints after-compact.md and the session's launch
message, which Claude Code adds to the compacted context.

Other sessions print nothing. A session is a coordinator when one of its user
messages carries the launch message, so the rules stay linked from that
message alone.
"""

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LAUNCH = re.compile(r"You are the coordinator for the .+? workstream")


def user_texts(entry):
    if entry.get("type") != "user":
        return []
    content = entry.get("message", {}).get("content")
    if isinstance(content, str):
        return [content]
    if isinstance(content, list):
        # Tool results are skipped so that reading the skill file or the
        # Playbook doesn't make a session a coordinator.
        return [b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"]
    return []


def launch_message(transcript_path):
    try:
        with open(transcript_path, encoding="utf-8") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                except ValueError:
                    continue
                for text in user_texts(entry):
                    match = LAUNCH.search(text)
                    if match:
                        return text[match.start():].strip()
    except (OSError, TypeError):
        pass
    return None


def main():
    hook = json.load(sys.stdin)
    launch = launch_message(hook.get("transcript_path"))
    if launch is None:
        return
    event = hook.get("hook_event_name")
    if event == "PreCompact":
        print((HERE / "before-compact.md").read_text(encoding="utf-8"))
    elif event == "SessionStart" and hook.get("source") == "compact":
        print((HERE / "after-compact.md").read_text(encoding="utf-8"))
        print("## Your launch message\n")
        print(launch)


if __name__ == "__main__":
    main()
