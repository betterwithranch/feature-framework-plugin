import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "skills" / "review-outcome" / "scripts" / "review_gate.py"
OUTCOME = "docs/spec/1-outcome.md"


class GateTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "docs/spec").mkdir(parents=True)
        (self.root / "reviews").mkdir()
        (self.root / OUTCOME).write_text("- **M4.** old words.\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def round(self, data: dict) -> None:
        (self.root / "reviews/round.json").write_text(json.dumps(data), encoding="utf-8")

    def run_gate(self, tool: str, inp: dict) -> subprocess.CompletedProcess:
        env = dict(os.environ, CLAUDE_PROJECT_DIR=str(self.root))
        return subprocess.run(
            [sys.executable, str(SCRIPT)], input=json.dumps({"tool_name": tool, "tool_input": inp}),
            capture_output=True, text=True, env=env,
        )

    def edit(self, old: str = "old words", new: str = "new words") -> subprocess.CompletedProcess:
        return self.run_gate("Edit", {"file_path": str(self.root / OUTCOME), "old_string": old, "new_string": new})

    def settled(self, **extra) -> dict:
        v = {"row": "M4", "rule": "3", "verdict": "Settled", "quotes": [{"record": "0075", "words": "x"}],
             "file": OUTCOME, "old": "old words", "new": "new words", "user_answer": None}
        v.update(extra)
        return v

    def test_refuses_an_edit_with_no_verdict(self) -> None:
        out = self.edit()
        self.assertEqual(out.returncode, 2)
        self.assertIn("no decisions-judge verdict", out.stderr)

    def test_refuses_an_edit_when_the_round_has_fails_but_no_verdicts(self) -> None:
        self.round({"fails": [{"row": "M4", "rule": "3"}], "verdicts": []})
        self.assertEqual(self.edit().returncode, 2)

    def test_allows_an_edit_that_equals_a_settled_change(self) -> None:
        self.round({"fails": [{"row": "M4"}], "verdicts": [self.settled()]})
        self.assertEqual(self.edit().returncode, 0)

    def test_refuses_an_edit_that_differs_from_the_settled_change(self) -> None:
        self.round({"fails": [{"row": "M4"}], "verdicts": [self.settled()]})
        out = self.edit(new="other words")
        self.assertEqual(out.returncode, 2)
        self.assertIn("doesn't match", out.stderr)

    def test_refuses_any_edit_while_a_finding_waits_on_the_user(self) -> None:
        self.round({"fails": [{}, {}], "verdicts": [self.settled(), {"row": "S1", "rule": "2", "verdict": "Conflict", "user_answer": None}]})
        out = self.edit()
        self.assertEqual(out.returncode, 2)
        self.assertIn("wait on the user", out.stderr)

    def test_allows_an_edit_the_user_answered(self) -> None:
        answered = self.settled(verdict="Rule misfire", user_answer={"question": "FF-81", "answer": "A"})
        self.round({"fails": [{}], "verdicts": [answered]})
        self.assertEqual(self.edit().returncode, 0)

    def test_guards_the_review_rules(self) -> None:
        out = self.run_gate("Write", {"file_path": str(self.root / "skills/references/outcome-reviews/scope.md"), "content": "x"})
        self.assertEqual(out.returncode, 2)

    def test_allows_creating_the_judge_reference(self) -> None:
        out = self.run_gate("Write", {"file_path": str(self.root / "skills/references/decisions-judge.md"), "content": "x"})
        self.assertEqual(out.returncode, 0)

    def test_ignores_other_files(self) -> None:
        self.assertEqual(self.run_gate("Edit", {"file_path": str(self.root / "README.md"), "old_string": "a", "new_string": "b"}).returncode, 0)

    def test_allows_a_write_that_applies_exactly_one_settled_change(self) -> None:
        self.round({"fails": [{}], "verdicts": [self.settled()]})
        ok = self.run_gate("Write", {"file_path": str(self.root / OUTCOME), "content": "- **M4.** new words.\n"})
        self.assertEqual(ok.returncode, 0)

    def test_refuses_a_review_while_a_finding_is_open(self) -> None:
        self.round({"fails": [{"row": "M4"}], "verdicts": []})
        out = self.run_gate("Agent", {"prompt": "Read skills/references/outcome-reviews/scope.md and judge"})
        self.assertEqual(out.returncode, 2)
        self.assertIn("can't start", out.stderr)

    def test_refuses_a_review_while_a_settled_change_is_unapplied(self) -> None:
        self.round({"fails": [{}], "verdicts": [self.settled()]})
        self.assertEqual(self.run_gate("Skill", {"skill": "review-outcome"}).returncode, 2)

    def test_allows_a_review_once_every_finding_is_closed(self) -> None:
        self.round({"fails": [{}], "verdicts": [self.settled()]})
        (self.root / OUTCOME).write_text("- **M4.** new words.\n", encoding="utf-8")
        self.assertEqual(self.run_gate("Skill", {"skill": "review-outcome"}).returncode, 0)

    def test_allows_the_judge_itself_to_run(self) -> None:
        self.round({"fails": [{"row": "M4"}], "verdicts": []})
        out = self.run_gate("Agent", {"prompt": "Follow skills/references/decisions-judge.md on the outcome-reviews/verification.md FAILs"})
        self.assertEqual(out.returncode, 0)


if __name__ == "__main__":
    unittest.main()
