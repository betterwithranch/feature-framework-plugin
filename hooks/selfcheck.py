#!/usr/bin/env python3
"""PreToolUse hook: deny an agent's git commit of a level document without a full self-check.

Runs under Claude Code and Codex. Both send one JSON object on stdin with
tool_name "Bash" and the shell command in tool_input.command. The hook acts
only when that command runs `git commit`. For each docs/spec/*.md whose staged
or working-tree version differs from HEAD, a self-check table must exist at
<git dir>/ff-selfcheck/<blob hash of that version>.md and name every
requirement (R<n>), scenario (S<n>) and measure (M<n>) in it.
"""
import json
import re
import subprocess
import sys

COMMIT = re.compile(r"(?:^|[\s;&|(])git(?:\s+-[^\s]+(?:\s+[^\s-][^\s]*)?)*\s+commit(?![\w-])")


def git(cwd: str, *args: str, stdin: str | None = None) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, input=stdin, capture_output=True, text=True, check=True
    ).stdout


def ids(doc: str) -> list[str]:
    found: list[str] = []
    section = None
    count = {"R": 0, "M": 0}
    for line in doc.splitlines():
        if line.startswith("**Achieves"):
            section = "R"
            continue
        if line.startswith("**Measured"):
            section = "M"
            continue
        if section and line.startswith("- "):
            count[section] += 1
            found.append(f"{section}{count[section]}")
            continue
        if section and line.strip():
            section = None
        row = re.match(r"^\|\s*(\d+)\s*\|", line)
        if row:
            found.append(f"S{row.group(1)}")
    return found


def versions(cwd: str) -> list[tuple[str, str, str]]:
    """(path, blob, content) for each changed version of a level document."""
    out = []
    changed = git(cwd, "diff", "HEAD", "--name-only", "--", "docs/spec/*.md").split()
    changed += git(cwd, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "--", "docs/spec/*.md").split()
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
    tables = git(root, "rev-parse", "--absolute-git-dir").strip() + "/ff-selfcheck"
    found = []
    for path, blob, content in versions(root):
        table_path = f"{tables}/{blob}.md"
        try:
            with open(table_path, encoding="utf-8") as f:
                table = f.read()
        except FileNotFoundError:
            found.append(
                f"{path}: no self-check table for this version. Run write-outcome's full "
                f"self-check on the whole document and write it to {table_path}."
            )
            continue
        missing = [i for i in ids(content) if not re.search(rf"\b{i}\b", table)]
        if missing:
            found.append(f"{path}: the self-check table {table_path} doesn't cover: {', '.join(missing)}.")
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
        reason = "Commit blocked: a level document changed without a full self-check.\n" + "\n".join(
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
