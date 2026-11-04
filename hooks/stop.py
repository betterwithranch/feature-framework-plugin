"""Check the agent's last message when it stops, for Claude Code and Codex alike.

Usage: python3 hooks/stop.py <host>, where host is `claude` or `codex`.

Reads the host's Stop payload on stdin and asks the host's own CLI, on its smallest
model, whether the message asks the user to approve something already decided. A
message that does is blocked with the reason in `reason`; a failed check goes to the
user in `systemMessage`. Always exits 0 with one JSON object, which both hosts read
the same way.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

PROMPT = Path(__file__).resolve().parent / "prompts" / "stop-check.md"
NESTED = "FEATURE_FRAMEWORK_STOP_CHECK"
NOT_CHECKED = "The stop check failed, so this message was not checked."
COMMANDS = {
    "claude": ["claude", "-p", "--model", "haiku", "--no-session-persistence"],
    "codex": ["codex", "exec", "--model", "gpt-6-luna", "--sandbox", "read-only", "--ephemeral"],
}


def main() -> None:
    host = sys.argv[1]
    payload = json.loads(sys.stdin.read() or "{}")
    sys.stdout.write(f"{json.dumps(response(host, payload))}\n")


def response(host: str, payload: dict[str, object]) -> dict[str, str]:
    if os.environ.get(NESTED) or payload.get("stop_hook_active"):
        return {}
    message = str(payload.get("last_assistant_message") or "")
    if "?" not in message:
        return {}
    prompt = f"{PROMPT.read_text()}\n## Last message\n\n{message}\n"
    try:
        check = subprocess.run(
            [*COMMANDS[host], "-"],
            input=prompt,
            capture_output=True,
            text=True,
            check=False,
            env={**os.environ, NESTED: "1"},
        )
    except OSError as error:
        return {"systemMessage": f"{NOT_CHECKED}\n{error}"}
    verdict = parse(check.stdout)
    if check.returncode != 0 or verdict is None:
        output = (check.stdout + check.stderr).rstrip()
        return {"systemMessage": f"{NOT_CHECKED}\n{output}"}
    if verdict.get("ok") is False:
        return {"decision": "block", "reason": str(verdict.get("reason", ""))}
    return {}


def parse(output: str) -> dict[str, object] | None:
    start, end = output.find("{"), output.rfind("}")
    if start == -1 or end < start:
        return None
    try:
        verdict = json.loads(output[start : end + 1])
    except ValueError:
        return None
    return verdict if isinstance(verdict, dict) else None


if __name__ == "__main__":
    main()
