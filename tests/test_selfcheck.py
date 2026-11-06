import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "hooks" / "selfcheck.py"

DOC = """# Outcome

**Achieves.**

- First result.
- Second result.

| # | Scenario | Passes when |
| --- | --- | --- |
| 1 | a | b |
| 2 | c | d |

**Measured on real features**:

- A measure: target zero.
"""

FULL = "R1 R2 S1 S2 M1\n"


class SelfCheckHookTest(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.repo = Path(tmp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "t@example.com")
        self.git("config", "user.name", "t")
        (self.repo / "README.md").write_text("start\n")
        self.git("add", "README.md")
        self.git("commit", "-q", "-m", "start")
        (self.repo / "docs" / "spec").mkdir(parents=True)

    def git(self, *args: str) -> str:
        return subprocess.run(
            ["git", *args], cwd=self.repo, capture_output=True, text=True, check=True
        ).stdout

    def stage_doc(self, text: str = DOC) -> str:
        (self.repo / "docs" / "spec" / "1-outcome.md").write_text(text)
        self.git("add", "docs/spec/1-outcome.md")
        return self.git("rev-parse", ":docs/spec/1-outcome.md").strip()

    def write_table(self, blob: str, text: str) -> None:
        tables = self.repo / ".git" / "ff-selfcheck"
        tables.mkdir(exist_ok=True)
        (tables / f"{blob}.md").write_text(text)

    def hook(self, command: str, tool: str = "Bash") -> dict[str, object] | None:
        payload = {
            "hook_event_name": "PreToolUse",
            "cwd": str(self.repo),
            "tool_name": tool,
            "tool_input": {"command": command},
        }
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input=json.dumps(payload),
            capture_output=True,
            text=True,
            check=True,
        )
        return json.loads(result.stdout) if result.stdout.strip() else None

    def assert_denied(self, out: dict[str, object] | None, text: str) -> None:
        self.assertIsNotNone(out)
        decision = out["hookSpecificOutput"]
        self.assertEqual(decision["permissionDecision"], "deny")
        self.assertIn(text, decision["permissionDecisionReason"])

    def test_denies_commit_without_table(self) -> None:
        self.stage_doc()
        self.assert_denied(self.hook('git commit -m "x"'), "no self-check table")

    def test_denies_commit_when_an_id_is_missing(self) -> None:
        self.write_table(self.stage_doc(), "R1 R2 S1 M1\n")
        self.assert_denied(self.hook("git -C . commit -qm x"), "S2")

    def test_allows_commit_with_full_table(self) -> None:
        self.write_table(self.stage_doc(), FULL)
        self.assertIsNone(self.hook('git add -A && git commit -m "x"'))

    def test_table_for_an_older_version_does_not_count(self) -> None:
        self.write_table(self.stage_doc(), FULL)
        (self.repo / "docs" / "spec" / "1-outcome.md").write_text(DOC + "\nMore.\n")
        self.assert_denied(self.hook("git commit -am x"), "no self-check table")

    def test_commit_outside_docs_spec_passes(self) -> None:
        (self.repo / "README.md").write_text("changed\n")
        self.git("add", "README.md")
        self.assertIsNone(self.hook("git commit -m x"))

    def test_command_that_is_not_a_commit_passes_untouched(self) -> None:
        self.stage_doc()
        self.assertIsNone(self.hook("git status && git log --grep commit"))
        self.assertIsNone(self.hook("git commit-tree HEAD^{tree}"))

    def test_other_tools_pass_untouched(self) -> None:
        self.stage_doc()
        self.assertIsNone(self.hook("git commit -m x", tool="apply_patch"))


if __name__ == "__main__":
    unittest.main()
