import os
import subprocess
import tempfile
import unittest
from pathlib import Path

HOOKS = Path(__file__).resolve().parent.parent / "hooks" / "git"

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


class PreCommitTest(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.repo = Path(tmp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "t@example.com")
        self.git("config", "user.name", "t")
        self.git("config", "core.hooksPath", str(HOOKS))
        (self.repo / "docs" / "spec").mkdir(parents=True)

    def git(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args], cwd=self.repo, capture_output=True, text=True, check=False
        )

    def stage_doc(self, text: str = DOC) -> str:
        (self.repo / "docs" / "spec" / "1-outcome.md").write_text(text)
        self.git("add", "docs/spec/1-outcome.md")
        return self.git("rev-parse", ":docs/spec/1-outcome.md").stdout.strip()

    def write_table(self, blob: str, text: str) -> None:
        tables = self.repo / ".git" / "ff-selfcheck"
        tables.mkdir(exist_ok=True)
        (tables / f"{blob}.md").write_text(text)

    def commit(self) -> subprocess.CompletedProcess[str]:
        return self.git("commit", "-q", "-m", "change")

    def test_blocks_without_table(self) -> None:
        self.stage_doc()
        result = self.commit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no self-check table", result.stderr)

    def test_blocks_when_an_id_is_missing(self) -> None:
        self.write_table(self.stage_doc(), "R1 R2 S1 M1\n")
        result = self.commit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("S2", result.stderr)

    def test_passes_with_full_table(self) -> None:
        self.write_table(self.stage_doc(), FULL)
        self.assertEqual(self.commit().returncode, 0)

    def test_table_for_an_older_version_does_not_count(self) -> None:
        self.write_table(self.stage_doc(), FULL)
        self.assertEqual(self.commit().returncode, 0)
        self.stage_doc(DOC + "\nMore.\n")
        self.assertNotEqual(self.commit().returncode, 0)

    def test_ignores_commits_outside_docs_spec(self) -> None:
        (self.repo / "README.md").write_text("hi\n")
        self.git("add", "README.md")
        self.assertEqual(self.commit().returncode, 0)


if __name__ == "__main__":
    unittest.main()
