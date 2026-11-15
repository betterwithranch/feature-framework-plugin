#!/usr/bin/env python3
"""PreToolUse hook on ArtifactData: refuse a board question that carries more
than one decision.

Craig's rule: every question reaches him one at a time. A question that lists
several numbered items to decide, asks about a range ("scenarios 8 to 19"), or
asks to approve a set, is several decisions in one and is denied with the
reason, so the coordinator re-asks the first decision alone.
"""

import json
import os
import re
import sys

LEVEL_TERMS = os.path.join(os.path.expanduser("~"), ".claude", "level-terms.json")

RANGE = re.compile(r"\b\d+\s*(?:to|through|-|–)\s*\d+\b")
SET_WORDS = re.compile(
    r"\b(?:all|every|each of|the set of|as the set|the (?:\w+ )?set)\b", re.I
)
PLURAL_ASK = re.compile(
    r"\b(?:approve|keep|confirm|accept)\b.*\b(?:scenarios|questions|measures|"
    r"choices|decisions|changes|rules|lines)\b",
    re.I,
)
NUMBERED_ITEM = re.compile(r"^(?:- |## )?(?:\d+)[.:)]\s", re.M)
ARROW = re.compile(r"➡|Recommend(?:ed)? [A-Z0-9]", re.M)
SUBHEAD = re.compile(r"^## (.+?)\s*$", re.M)
STANDARD_SUBHEADS = ["What this decides", "Example", "Costs", "After this"]


def decisions_in(doc):
    question = str(doc.get("question") or "")
    details = str(doc.get("details") or "")
    reasons = []
    if RANGE.search(question):
        reasons.append("the title asks about a range of items")
    if SET_WORDS.search(question) and PLURAL_ASK.search(question):
        reasons.append("the title asks to approve a set")
    numbered = len(NUMBERED_ITEM.findall(details))
    if numbered >= 2:
        reasons.append(f"the details list {numbered} numbered items to decide")
    arrows = len(ARROW.findall(details))
    if arrows >= 2:
        reasons.append(f"the details carry {arrows} recommendations")
    subheads = SUBHEAD.findall(details)
    if details.strip() and subheads != [h for h in STANDARD_SUBHEADS if h in subheads]:
        reasons.append(
            "the details' subheads are not the standard ones in order: "
            + ", ".join(STANDARD_SUBHEADS[:3])
            + " and optionally "
            + STANDARD_SUBHEADS[3]
        )
    return reasons


EXAMPLE = re.compile(r"^## Example[ \t]*$(.*?)(?=^## |\Z)", re.M | re.S)
COMMIT = re.compile(
    r"\b(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}\b"
    r"|(?:\bcommit|\bat|@)\s*[0-9a-f]{7,40}\b",
    re.I,
)
RECORD_REF = re.compile(r"\b(?:D\d{1,3}|[A-Z]{2,4}-\d{1,4})\b")
BARE_VERDICT = re.compile(r"\|\s*(?:PASS|FAIL)\s*\||\b(?:PASS|FAIL)\W*$", re.M)


def example_reasons(doc):
    """D29/D39: an example supports the decision on its own, with its reason."""
    match = EXAMPLE.search(str(doc.get("details") or ""))
    if not match:
        return []
    text = match.group(1)
    reasons = []
    if COMMIT.search(text) or RECORD_REF.search(text):
        reasons.append(
            "the Example points to a commit, decision or question number; say "
            "what it means instead, so the question stands on its own"
        )
    if BARE_VERDICT.search(text):
        reasons.append(
            "the Example gives a bare PASS or FAIL; say which rule it shows and, "
            "in a sentence, why it passes or fails"
        )
    return reasons


def level_term_reasons(doc):
    """Terms Craig ruled out of the current level's questions (level-terms.json)."""
    try:
        with open(LEVEL_TERMS, encoding="utf-8") as f:
            cfg = json.load(f)
    except Exception:
        return []
    if doc.get("workstream") not in (None, cfg.get("workstream")):
        return []
    # The ban is for questions at the configured level only. A question at
    # another level says so in its "level" field; one without it is taken to
    # be at the configured level.
    if str(doc.get("level", cfg.get("level"))) != str(cfg.get("level")):
        return []
    text = " ".join(str(doc.get(k) or "") for k in ("question", "context", "details"))
    hits = sorted({t for t in cfg.get("ruled_out", []) if re.search(r"\b" + re.escape(t) + r"\b", text, re.I)})
    if not hits:
        return []
    return [
        f"it uses terms ruled out of level {cfg.get('level')} ({cfg.get('level_name')}): "
        + ", ".join(hits)
        + f". Level {cfg.get('level')} speaks only of {cfg.get('speak_of')}"
    ]


REQUIRED_FIELDS = ("workstream", "thread_id", "item_id", "question", "context", "options",
                   "recommendation", "recommendation_reason", "details", "status", "priority", "asked_at", "reply", "question_kind")
KINDS = ("decision fix", "conflict", "specific change", "approval")


def missing_field_reasons(tool_input, data):
    """A new question the page can't place is invisible: the queue filters on workstream."""
    if tool_input.get("action") == "update":
        return []
    if tool_input.get("action") == "batch":
        ops = [w for w in tool_input.get("writes") or [] if w.get("data") is data]
        if ops and ops[0].get("op") == "update":
            return []
    missing = [f for f in REQUIRED_FIELDS if not data.get(f)]
    if missing:
        return ["it is missing fields the board needs to show it: " + ", ".join(missing)]
    kind = str(data.get("question_kind")).strip().lower()
    if not kind.startswith(KINDS) or ":" not in kind:
        return ["question_kind must start with one of: " + ", ".join(KINDS) + ", then ': ' and why"]
    if kind.startswith(("decision fix", "conflict")) and not re.search(r'"[^"]{12,}"|```', str(data.get("details"))):
        return ["a decision fix or conflict quotes the recorded decision text in its details"]
    return []


def question_docs(tool_input):
    action = tool_input.get("action")
    if action in ("set", "update") and tool_input.get("collection") == "questions":
        data = tool_input.get("data") or {}
        if isinstance(data, dict) and ("question" in data or "details" in data):
            yield tool_input.get("doc_id"), data
    if action == "batch":
        for w in tool_input.get("writes") or []:
            if w.get("collection") == "questions" and w.get("op") in ("set", "update"):
                data = w.get("data") or {}
                if isinstance(data, dict) and ("question" in data or "details" in data):
                    yield w.get("doc_id"), data


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    if payload.get("tool_name") != "ArtifactData":
        sys.exit(0)
    tool_input = payload.get("tool_input") or {}
    for doc_id, data in question_docs(tool_input):
        if data.get("status") in ("answered", "withdrawn", "deferred"):
            continue
        reasons = decisions_in(data) + example_reasons(data) + level_term_reasons(data) + missing_field_reasons(tool_input, data)
        if reasons:
            reason = (
                f"{doc_id} isn't a standard question: {'; '.join(reasons)}. Ask one decision, "
                "with details under '## What this decides', '## Example', '## Costs' "
                "and optionally '## After this'."
            )
            json.dump(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "PreToolUse",
                        "permissionDecision": "deny",
                        "permissionDecisionReason": reason,
                    }
                },
                sys.stdout,
            )
            sys.exit(0)
    sys.exit(0)


if __name__ == "__main__":
    main()
