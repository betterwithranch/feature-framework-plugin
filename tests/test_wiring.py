import json
import re
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# event -> (matcher it must have, or None for any, file the command must reference)
EXPECTED = {
    "SessionStart": (None, "hooks/prompts/goals.md"),
    "UserPromptSubmit": (None, "hooks/prompts/goals.md"),
    "PreToolUse": ("Bash", "hooks/selfcheck.py"),
    "Stop": (None, "hooks/stop.py"),
}


def entries(hooks: dict, event: str) -> list[tuple[str | None, str]]:
    return [
        (group.get("matcher"), hook["command"])
        for group in hooks.get(event, [])
        for hook in group.get("hooks", [])
    ]


class WiringTest(unittest.TestCase):
    def check(self, hooks: dict, host: str) -> None:
        for event, (matcher, target) in EXPECTED.items():
            with self.subTest(host=host, event=event):
                found = [
                    (m, c) for m, c in entries(hooks, event) if target in c
                ]
                self.assertTrue(found, f"{host}: {event} doesn't reference {target}")
                if matcher:
                    self.assertTrue(
                        any(m and re.fullmatch(m, matcher) for m, _ in found),
                        f"{host}: {event} hook for {target} doesn't match {matcher}",
                    )
                self.assertTrue((ROOT / target).exists(), f"{target} is missing")

    def test_claude_code_settings(self) -> None:
        settings = json.loads((ROOT / ".claude" / "settings.json").read_text())
        self.check(settings["hooks"], "claude")

    def test_codex_config(self) -> None:
        config = tomllib.loads((ROOT / ".codex" / "config.toml").read_text())
        self.check(config["hooks"], "codex")

    def test_no_git_hooks(self) -> None:
        for path in (ROOT / ".claude" / "settings.json", ROOT / ".codex" / "config.toml"):
            self.assertNotIn("hooksPath", path.read_text())


if __name__ == "__main__":
    unittest.main()
