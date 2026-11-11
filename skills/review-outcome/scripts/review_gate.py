#!/usr/bin/env python3
"""Gate on edits to the Outcome and its review rules, and on starting a review.

Reads one hook event as JSON on stdin ({"tool_name": ..., "tool_input": {...}})
and exits 2 with a reason on stderr to refuse it, or 0 to allow it. It runs the
same way under any agent host that passes the tool call as JSON.

An edit to docs/spec/1-outcome.md or skills/references/** is allowed only when:
- reviews/round.json has verdicts for the current round,
- the edit's old and new text equal an entry that is Settled or has a recorded
  answer from the user,
- no entry is Rule misfire, Conflict or Missing without a recorded answer.

Starting a review is refused while any finding is open: a FAIL with no verdict,
a verdict waiting on the user, or a change not yet applied.

A shell command that names one of those paths and writes to it (sed -i, a
redirection, tee, mv, cp onto it, rm, python or perl writing, git checkout or
git restore) is refused, and so is any git apply: a shell write can't be matched to a
Settled change, so it goes through Edit instead. When in doubt, it refuses.

Creating skills/references/decisions-judge.md is exempt, as decision 0078 approves it.
"""
import json
import os
import re
import shlex
import sys
from pathlib import Path

PROTECTED_FILES = {"docs/spec/1-outcome.md"}
PROTECTED_DIRS = ("skills/references/",)
EXEMPT_NEW = {"skills/references/decisions-judge.md"}
ROUND = "reviews/round.json"
REVIEW_MARKERS = ("outcome-reviews/", "glossary-review.md", "review-outcome")
ASKS_USER = {"Rule misfire", "Conflict", "Missing"}


def root() -> Path:
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()).resolve()


def rel(path: str, base: Path) -> str:
    p = Path(path)
    p = (base / p) if not p.is_absolute() else p
    try:
        return p.resolve().relative_to(base).as_posix()
    except ValueError:
        return p.as_posix()


def protected(r: str) -> bool:
    return r in PROTECTED_FILES or r.startswith(PROTECTED_DIRS)


def load_round(base: Path):
    f = base / ROUND
    if not f.exists():
        return None
    return json.loads(f.read_text(encoding="utf-8"))


def allowed_changes(rnd: dict) -> list:
    return [v for v in rnd.get("verdicts", []) if v.get("verdict") == "Settled" or v.get("user_answer")]


def waiting(rnd: dict) -> list:
    return [v for v in rnd.get("verdicts", []) if v.get("verdict") in ASKS_USER and not v.get("user_answer")]


def check_edit(base: Path, tool: str, inp: dict):
    r = rel(inp.get("file_path", ""), base)
    if not protected(r):
        return None
    if r in EXEMPT_NEW and not (base / r).exists():
        return None
    rnd = load_round(base)
    if not rnd or not rnd.get("verdicts"):
        return f"{r}: no decisions-judge verdict for the current round ({ROUND}). Run the judge first."
    open_ = waiting(rnd)
    if open_:
        rows = ", ".join(f"{v.get('row')} rule {v.get('rule')}" for v in open_)
        return f"{r}: findings wait on the user ({rows}). Nothing changes until they are answered."
    entries = [v for v in allowed_changes(rnd) if v.get("file") == r]
    if tool == "Edit":
        pair = (inp.get("old_string"), inp.get("new_string"))
        if any((v.get("old"), v.get("new")) == pair for v in entries):
            return None
    elif tool == "Write":
        current = (base / r).read_text(encoding="utf-8") if (base / r).exists() else ""
        for v in entries:
            if v.get("old") and current.count(v["old"]) == 1 and inp.get("content") == current.replace(v["old"], v["new"]):
                return None
    return f"{r}: the edit doesn't match a Settled change or a recorded answer in {ROUND}."


def open_findings(base: Path, rnd: dict) -> list:
    fails = rnd.get("fails", [])
    verdicts = rnd.get("verdicts", [])
    out = []
    if fails and len(verdicts) < len(fails):
        out.append(f"{len(fails) - len(verdicts)} FAIL(s) have no verdict")
    out += [f"{v.get('row')} rule {v.get('rule')} waits on the user" for v in waiting(rnd)]
    for v in allowed_changes(rnd):
        f = base / v.get("file", "")
        text = f.read_text(encoding="utf-8") if f.exists() else ""
        if v.get("old") and v["old"] in text:
            out.append(f"{v.get('row')} rule {v.get('rule')}: change not applied")
    return out


GUARDED_WORDS = ("docs/spec/1-outcome.md", "1-outcome.md", "skills/references", "outcome-reviews",
                 "glossary-review.md", "decisions-judge.md", "writing.md", "outcome.md", "decisions.md")
WRITE_SCRIPT_HINTS = ("write(", "write_text", "write_bytes", "writelines", "open(", "rename", "replace(", "unlink", "remove(", "shutil", "os.system", "subprocess")
SCRIPTING = re.compile(r"\b(python[0-9.]*|perl|ruby|node)\b")


def names_guarded(text: str) -> bool:
    return any(w in text for w in GUARDED_WORDS)


def tokens(cmd: str) -> list:
    try:
        return shlex.split(cmd, posix=True)
    except ValueError:
        return cmd.split()


def check_bash(cmd: str):
    refuse = "Shell writes to the Outcome or the review rules are refused; apply a Settled change with Edit."
    if re.search(r"\bgit\s+(apply|am)\b(?![^;&|]*--(check|stat|numstat))", cmd):
        return "A patch can change the Outcome or the review rules unseen, so git apply is refused; apply a Settled change with Edit."
    if not names_guarded(cmd):
        return None
    for target in re.findall(r"(?<![0-9&<>-])>{1,2}\|?\s*([^\s;|&<>]+)", cmd):
        if names_guarded(target):
            return refuse
    if SCRIPTING.search(cmd) and any(h in cmd for h in WRITE_SCRIPT_HINTS):
        return refuse
    for seg in re.split(r"&&|\|\||[;|\n]", cmd):
        t = tokens(seg.strip())
        if not t:
            continue
        head = os.path.basename(t[0])
        rest = " ".join(t[1:])
        if not names_guarded(seg):
            continue
        if head == "sed" and any(a.startswith("-i") or a == "--in-place" or a.startswith("--in-place") for a in t[1:]):
            return refuse
        if head in ("tee", "mv", "rm", "truncate", "dd", "ln", "install", "patch", "ed", "ex"):
            return refuse
        if head == "cp":
            args = [a for a in t[1:] if not a.startswith("-")]
            if not args or names_guarded(args[-1]) or any(a.startswith("-t") or a == "--target-directory" for a in t[1:]):
                return refuse
        if head.startswith(("perl", "ruby")) and any(a.startswith(("-i", "-pi", "-ni")) for a in t[1:]):
            return refuse
        if head == "awk" and "inplace" in rest:
            return refuse
        if head == "git" and len(t) > 1 and t[1] in ("checkout", "restore", "mv", "rm"):
            return refuse
    return None


def is_review_start(tool: str, inp: dict) -> bool:
    if tool == "Skill":
        return "review-outcome" in str(inp.get("skill", ""))
    if tool in ("Agent", "Task"):
        text = " ".join(str(inp.get(k, "")) for k in ("prompt", "description"))
        return any(m in text for m in REVIEW_MARKERS) and "decisions-judge" not in text
    return False


def decide(event: dict, base: Path):
    tool = event.get("tool_name", "")
    inp = event.get("tool_input", {}) or {}
    if tool in ("Edit", "Write", "MultiEdit"):
        if tool == "MultiEdit":
            r = rel(inp.get("file_path", ""), base)
            return f"{r}: use one Edit per Settled change." if protected(r) else None
        return check_edit(base, tool, inp)
    if tool == "Bash":
        return check_bash(str(inp.get("command", "")))
    if is_review_start(tool, inp):
        rnd = load_round(base)
        if rnd:
            found = open_findings(base, rnd)
            if found:
                return "A review can't start while findings are open: " + "; ".join(found) + "."
    return None


def main() -> int:
    event = json.load(sys.stdin)
    reason = decide(event, root())
    if reason:
        print(reason, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
