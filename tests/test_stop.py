import json
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "hooks" / "stop.py"


class StopHookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bin = tempfile.TemporaryDirectory()
        self.addCleanup(self.bin.cleanup)
        self.calls = Path(self.bin.name) / "calls"

    def fake_cli(self, name: str, reply: str, exit_code: int = 0) -> None:
        path = Path(self.bin.name) / name
        path.write_text(
            "#!/bin/sh\n"
            f'echo "$@" >> "{self.calls}"\n'
            "cat > /dev/null\n"
            f"printf '%s' '{reply}'\n"
            f"exit {exit_code}\n"
        )
        path.chmod(path.stat().st_mode | stat.S_IEXEC)

    def run_hook(self, host: str, payload: dict[str, object]) -> dict[str, str]:
        env = {**os.environ, "PATH": f"{self.bin.name}:{os.environ['PATH']}"}
        env.pop("FEATURE_FRAMEWORK_STOP_CHECK", None)
        result = subprocess.run(
            [sys.executable, str(SCRIPT), host],
            input=json.dumps(payload),
            capture_output=True,
            text=True,
            env=env,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        lines = result.stdout.splitlines()
        self.assertEqual(len(lines), 1)
        return json.loads(lines[0])

    def calls_made(self) -> list[str]:
        return self.calls.read_text().splitlines() if self.calls.exists() else []

    def test_blocks_when_the_model_says_no(self) -> None:
        for host in ("claude", "codex"):
            with self.subTest(host=host):
                self.fake_cli(host, '{"ok": false, "reason": "Just do it."}')
                verdict = self.run_hook(host, {"last_assistant_message": "Shall I push?"})
                self.assertEqual(verdict, {"decision": "block", "reason": "Just do it."})

    def test_allows_when_the_model_says_yes(self) -> None:
        for host in ("claude", "codex"):
            with self.subTest(host=host):
                self.fake_cli(host, '{"ok": true}')
                self.assertEqual(self.run_hook(host, {"last_assistant_message": "A or B?"}), {})

    def test_each_host_gets_its_cli_and_smallest_model(self) -> None:
        self.fake_cli("claude", '{"ok": true}')
        self.fake_cli("codex", '{"ok": true}')
        self.run_hook("claude", {"last_assistant_message": "A or B?"})
        self.run_hook("codex", {"last_assistant_message": "A or B?"})
        claude_call, codex_call = self.calls_made()
        self.assertIn("--model haiku --no-session-persistence", claude_call)
        self.assertIn("--model gpt-6-luna --sandbox read-only --ephemeral", codex_call)

    def test_nested_check_runs_with_hooks_off(self) -> None:
        self.fake_cli("claude", '{"ok": true}')
        self.fake_cli("codex", '{"ok": true}')
        self.run_hook("claude", {"last_assistant_message": "A or B?"})
        self.run_hook("codex", {"last_assistant_message": "A or B?"})
        claude_call, codex_call = self.calls_made()
        self.assertIn('-p --settings {"disableAllHooks": true}', claude_call)
        self.assertIn("exec -c features.hooks=false", codex_call)

    def test_skips_when_already_continuing(self) -> None:
        self.fake_cli("claude", '{"ok": false, "reason": "no"}')
        verdict = self.run_hook(
            "claude", {"stop_hook_active": True, "last_assistant_message": "Push?"}
        )
        self.assertEqual(verdict, {})
        self.assertEqual(self.calls_made(), [])

    def test_skips_a_message_with_no_question(self) -> None:
        self.fake_cli("claude", '{"ok": false, "reason": "no"}')
        self.assertEqual(self.run_hook("claude", {"last_assistant_message": "Done."}), {})
        self.assertEqual(self.calls_made(), [])

    def test_skips_inside_its_own_nested_check(self) -> None:
        self.fake_cli("claude", '{"ok": false, "reason": "no"}')
        env = {**os.environ, "FEATURE_FRAMEWORK_STOP_CHECK": "1"}
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "claude"],
            input=json.dumps({"last_assistant_message": "Push?"}),
            capture_output=True,
            text=True,
            env={**env, "PATH": f"{self.bin.name}:{os.environ['PATH']}"},
            check=False,
        )
        self.assertEqual(json.loads(result.stdout), {})
        self.assertEqual(self.calls_made(), [])

    def test_reports_a_failed_check_to_the_user(self) -> None:
        self.fake_cli("claude", "not json", exit_code=1)
        verdict = self.run_hook("claude", {"last_assistant_message": "Push?"})
        self.assertEqual(set(verdict), {"systemMessage"})
        self.assertIn("not checked", verdict["systemMessage"])


if __name__ == "__main__":
    unittest.main()
