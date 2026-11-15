import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "skills" / "write-outcome" / "scripts" / "absolutes.py"

DOC = """# Outcome

**Requirements.**

- **R1.** Every message is short.
- **R2.** The company keeps a record. Nobody-company words like anyway stay out.
- **R3.** A level moves on only when approved.

**Glossary.**

- **Plain answer:** an answer that is never played back.

| ID | Scenario | Passes when | Verifies |
| --- | --- | --- | --- |
| S1 | A user writes | No message asks two questions | R1 |

**Measures**, on real features:

- **M1.** Messages with anything extra: none.
"""


class AbsolutesTest(unittest.TestCase):
    def run_script(self, text: str) -> list[tuple[str, str, str]]:
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(text)
        out = subprocess.run(
            [sys.executable, str(SCRIPT), f.name], capture_output=True, text=True, check=True
        ).stdout
        Path(f.name).unlink()
        return [tuple(line.split("\t")) for line in out.splitlines()]

    def test_lists_exactly_the_known_absolutes_with_ids(self) -> None:
        rows = self.run_script(DOC)
        self.assertEqual(
            [(i, t) for i, t, _ in rows],
            [
                ("R1", "every"),
                ("R3", "only"),
                ("glossary: Plain answer", "never"),
                ("S1", "no"),
                ("M1", "anything"),
                ("M1", "none"),
            ],
        )

    def test_gives_the_sentence(self) -> None:
        rows = self.run_script(DOC)
        self.assertEqual(rows[1][2], "A level moves on only when approved.")

    def test_words_that_only_contain_an_absolute_are_not_listed(self) -> None:
        rows = self.run_script(DOC)
        self.assertNotIn("R2", [i for i, _, _ in rows])


if __name__ == "__main__":
    unittest.main()
