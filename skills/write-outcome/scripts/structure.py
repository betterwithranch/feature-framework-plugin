#!/usr/bin/env python3
"""Check a level document's structure.

Usage: structure.py <document.md> [level]

Prints one line per failure and exits 1 if any; prints nothing and exits 0 if
the document passes. The level defaults to the number the file name starts with.
Checks: the required sections are present; every requirement ID is cited by a
scenario or measure, and every cited ID exists; R, S and M IDs run in document
order from 1 without gaps or duplicates; no banned term for the level appears.
"""
import os
import re
import sys

SECTIONS = {
    1: [("For whom", r"^\*\*For whom\.\*\*"),
        ("Requirements", r"^\*\*Requirements\.\*\*"),
        ("Scenarios", r"^\*\*Scenarios\.\*\*"),
        ("Measures", r"^\*\*Measures\b")],
}
BANNED = {1: ["Behaviour", "Behavior", "Design", "Slices"]}

REQ = re.compile(r"^-\s+\*\*(R\d+)\.\*\*")
MEASURE = re.compile(r"^-\s+\*\*(M\d+)\.\*\*")
ROW = re.compile(r"^\|\s*(S\d+)\s*\|")


def defined(doc: str) -> dict[str, list[str]]:
    ids: dict[str, list[str]] = {"R": [], "S": [], "M": []}
    for line in doc.splitlines():
        for pattern in (REQ, MEASURE, ROW):
            if m := pattern.match(line):
                ids[m.group(1)[0]].append(m.group(1))
    return ids


def cited(doc: str) -> set[str]:
    refs: set[str] = set()
    for line in doc.splitlines():
        if ROW.match(line) or MEASURE.match(line):
            body = ROW.sub("", line) if ROW.match(line) else MEASURE.sub("", line)
            refs |= set(re.findall(r"\bR\d+\b", body))
    return refs


def check(doc: str, level: int) -> list[str]:
    failures = []
    for name, pattern in SECTIONS.get(level, []):
        if not re.search(pattern, doc, flags=re.M):
            failures.append(f"missing section: {name}")
    ids = defined(doc)
    for kind, found in ids.items():
        numbers = [int(i[1:]) for i in found]
        dupes = sorted({i for i in found if found.count(i) > 1}, key=lambda i: int(i[1:]))
        if dupes:
            failures.append(f"duplicate IDs: {', '.join(dupes)}")
        if numbers != list(range(1, len(numbers) + 1)) and not dupes:
            failures.append(f"{kind} IDs not in order from 1 without gaps: {', '.join(found)}")
    refs = cited(doc)
    for r in ids["R"]:
        if r not in refs:
            failures.append(f"{r} is cited by no scenario or measure")
    for r in sorted(refs - set(ids["R"]), key=lambda i: int(i[1:])):
        failures.append(f"{r} is cited but not defined")
    for term in BANNED.get(level, []):
        for n, line in enumerate(doc.splitlines(), 1):
            if re.search(rf"\b{term}\b", line):
                failures.append(f"banned term at level {level}, line {n}: {term}")
    return failures


def level_of(path: str) -> int:
    m = re.match(r"(\d+)-", os.path.basename(path))
    return int(m.group(1)) if m else 0


def main() -> int:
    path = sys.argv[1]
    level = int(sys.argv[2]) if len(sys.argv) > 2 else level_of(path)
    with open(path, encoding="utf-8") as f:
        failures = check(f.read(), level)
    for failure in failures:
        print(failure)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
