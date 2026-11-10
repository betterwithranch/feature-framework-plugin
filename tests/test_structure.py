import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "skills" / "write-outcome" / "scripts" / "structure.py"
spec = importlib.util.spec_from_file_location("structure", SCRIPT)
structure = importlib.util.module_from_spec(spec)
spec.loader.exec_module(structure)

DOC = """**For whom.** Someone.

**Glossary.** Terms are used as the project's [glossary](glossary.md) defines them.

**Requirements.**

- **R1.** One.
- **R2.** Two.

**Scenarios.**

| ID | Scenario | Passes when | Verifies |
| --- | --- | --- | --- |
| S1 | a | b | R1 |

**Measures**, on real use:

- **M1.** Count of R2 failures: none.
"""


class StructureTest(unittest.TestCase):
    def test_a_sound_document_passes(self) -> None:
        self.assertEqual(structure.check(DOC, 1), [])

    def test_a_missing_section_fails(self) -> None:
        self.assertIn("missing section: Measures", structure.check(DOC.replace("**Measures**", "Measures"), 1))

    def test_a_missing_glossary_reference_fails(self) -> None:
        doc = DOC.replace("[glossary](glossary.md)", "glossary")
        self.assertIn("missing section: reference to the project glossary", structure.check(doc, 1))

    def test_an_uncited_requirement_fails(self) -> None:
        doc = DOC.replace("Count of R2 failures", "Count of failures")
        self.assertIn("R2 is cited by no scenario or measure", structure.check(doc, 1))

    def test_a_cited_id_that_doesnt_exist_fails(self) -> None:
        self.assertIn("R9 is cited but not defined", structure.check(DOC.replace("| R1 |", "| R1 R9 |"), 1))

    def test_a_gap_fails(self) -> None:
        doc = DOC.replace("**R2.**", "**R3.**").replace("R2 failures", "R3 failures")
        self.assertTrue(any("not in order" in f for f in structure.check(doc, 1)))

    def test_a_duplicate_fails(self) -> None:
        doc = DOC.replace("**R2.**", "**R1.**").replace("R2 failures", "R1 failures")
        self.assertIn("duplicate IDs: R1", structure.check(doc, 1))

    def test_a_banned_term_fails_at_level_one(self) -> None:
        failures = structure.check(DOC + "Left to Design.\n", 1)
        self.assertTrue(any("banned term" in f and "Design" in f for f in failures))

    def test_a_lowercase_word_is_not_banned(self) -> None:
        self.assertEqual(structure.check(DOC + "Its design is open.\n", 1), [])


if __name__ == "__main__":
    unittest.main()
