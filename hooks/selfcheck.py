#!/usr/bin/env python3
"""PreToolUse hook: deny an agent's git commit of a level document that fails its structure checks.

Runs under Claude Code and Codex. Both send one JSON object on stdin with
tool_name "Bash" and the shell command in tool_input.command. The hook acts
only when that command runs `git commit`. Each level document
(docs/spec/<level>-*.md) whose staged or working-tree version differs from HEAD
must pass skills/write-outcome/scripts/structure.py.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

STRUCTURE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "skills", "write-outcome", "scripts", "structure.py")
_spec = importlib.util.spec_from_file_location("structure", STRUCTURE)
structure = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(structure)

COMMIT = re.compile(r"(?:^|[\s;&|(])git(?:\s+-[^\s]+(?:\s+[^\s-][^\s]*)?)*\s+commit(?![\w-])")


def git(cwd: str, *args: str, stdin: str | None = None) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, input=stdin, capture_output=True, text=True, check=True
    ).stdout


def versions(cwd: str) -> list[tuple[str, str, str]]:
    """(path, blob, content) for each changed version of a level document."""
    out = []
    changed = git(cwd, "diff", "HEAD", "--name-only", "--", "docs/spec/[0-9]*-*.md").split()
    changed += git(cwd, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "--", "docs/spec/[0-9]*-*.md").split()
    for path in sorted(set(changed)):
        seen = set()
        staged = subprocess.run(["git", "show", f":{path}"], cwd=cwd, capture_output=True, text=True)
        if staged.returncode == 0:
            blob = git(cwd, "rev-parse", f":{path}").strip()
            seen.add(blob)
            out.append((path, blob, staged.stdout))
        try:
            with open(f"{cwd}/{path}", encoding="utf-8") as f:
                work = f.read()
        except FileNotFoundError:
            continue
        blob = git(cwd, "hash-object", "--stdin", stdin=work).strip()
        if blob not in seen:
            out.append((path, blob, work))
    head = {}
    for path, blob, _ in out:
        r = subprocess.run(["git", "rev-parse", f"HEAD:{path}"], cwd=cwd, capture_output=True, text=True)
        head[path] = r.stdout.strip() if r.returncode == 0 else None
    return [v for v in out if v[1] != head[v[0]]]


def problems(cwd: str) -> list[str]:
    root = git(cwd, "rev-parse", "--show-toplevel").strip()
    found = []
    for path, _blob, content in versions(root):
        for failure in structure.check(content, structure.level_of(path)):
            found.append(f"{path}: {failure}")
    return found


def main() -> int:
    payload = json.load(sys.stdin)
    if payload.get("tool_name") != "Bash":
        return 0
    command = (payload.get("tool_input") or {}).get("command", "")
    if isinstance(command, list):
        command = " ".join(command)
    if not COMMIT.search(command):
        return 0
    try:
        found = problems(payload.get("cwd") or ".")
    except subprocess.CalledProcessError:
        return 0
    if found:
        reason = "Commit blocked: a level document fails its structure checks.\n" + "\n".join(
            f"- {p}" for p in found
        )
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
