#!/usr/bin/env python3
"""List every absolute term in a level document, with its ID and sentence.

Usage: absolutes.py <document.md>

Prints one tab-separated line per absolute: ID (R<n>, S<n>, M<n>, or
"glossary: <term>", or "preamble"), the term, and the sentence it sits in.
The terms are the definition's absolute terms (skills/references/outcome.md,
criterion 6) and words that say the same.
"""
import re
import sys

TERMS = [
    "every", "everything", "everyone", "never", "only", "always", "all",
    "none", "nothing", "any", "anything", "anyone", "each", "no", "wherever",
    "whenever", "exactly",
]
TERM = re.compile(r"\b(" + "|".join(TERMS) + r")\b", re.IGNORECASE)
ITEM = re.compile(r"^-\s+\*\*([RSM]\d+)\.?\*\*\s*(.*)$")
GLOSSARY = re.compile(r"^-\s+\*\*([^*]+?):\*\*\s*(.*)$")
ROW = re.compile(r"^\|\s*(S\d+)\s*\|(.*)$")


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.;:!?])\s+|\s*\|\s*", text)
    return [p.strip(" |") for p in parts if p.strip(" |")]


def items(doc: str) -> list[tuple[str, str]]:
    found = []
    for line in doc.splitlines():
        if m := ITEM.match(line):
            found.append((m.group(1), m.group(2)))
        elif m := ROW.match(line):
            found.append((m.group(1), m.group(2)))
        elif m := GLOSSARY.match(line):
            found.append((f"glossary: {m.group(1)}", m.group(2)))
        elif line.startswith("**Scenarios.**"):
            found.append(("preamble", line))
    return found


def absolutes(doc: str) -> list[tuple[str, str, str]]:
    out = []
    for item_id, text in items(doc):
        for sentence in sentences(text):
            for m in TERM.finditer(sentence):
                out.append((item_id, m.group(1).lower(), sentence))
    return out


def main() -> int:
    with open(sys.argv[1], encoding="utf-8") as f:
        doc = f.read()
    for item_id, term, sentence in absolutes(doc):
        print(f"{item_id}\t{term}\t{sentence}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
