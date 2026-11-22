"""Tests for `run_eval.write_judge_prompts` and the `--judge-prompts` option (no AI calls)."""

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
RUN_EVAL = ROOT / "evals" / "run_eval.py"
CASES = ROOT / "evals" / "cases"

_spec = importlib.util.spec_from_file_location("run_eval", RUN_EVAL)
run_eval = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(run_eval)


class WriteJudgePromptsTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.run_dir = self.tmp / "evidence" / "20260101-000000"
        self.run_dir.mkdir(parents=True)
        self.judge_dir = self.tmp / "judge-prompts"
        patcher = mock.patch.object(run_eval, "JUDGE_DIR", self.judge_dir)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_writes_one_prompt_per_with_skill_output(self):
        cases = [CASES / "guide-en.md", CASES / "common-en.md"]
        (self.run_dir / "guide-en.with_skill.md").write_text("GUIDE-OUTPUT-MARK", encoding="utf-8")
        (self.run_dir / "common-en.with_skill.md").write_text("COMMON-OUTPUT-MARK", encoding="utf-8")
        (self.run_dir / "guide-en.without_skill.md").write_text("BASELINE-MARK", encoding="utf-8")
        count = run_eval.write_judge_prompts(self.run_dir, cases)
        self.assertEqual(count, 2)
        target = self.judge_dir / self.run_dir.name
        self.assertEqual(sorted(p.name for p in target.iterdir()),
                         ["common-en.judge.md", "guide-en.judge.md"])
        guide = (target / "guide-en.judge.md").read_text(encoding="utf-8")
        self.assertIn("GUIDE-OUTPUT-MARK", guide)
        self.assertNotIn("BASELINE-MARK", guide)
        self.assertIn("invented_steps", guide)
        self.assertNotIn("{{CASE}}", guide)
        self.assertNotIn("{{OUTPUT}}", guide)

    def test_skips_case_without_output(self):
        (self.run_dir / "guide-en.with_skill.md").write_text("x", encoding="utf-8")
        count = run_eval.write_judge_prompts(self.run_dir, [CASES / "guide-en.md", CASES / "essay-en.md"])
        self.assertEqual(count, 1)
        self.assertFalse((self.judge_dir / self.run_dir.name / "essay-en.judge.md").exists())

    def test_no_outputs_creates_no_folder(self):
        self.assertEqual(run_eval.write_judge_prompts(self.run_dir, [CASES / "guide-en.md"]), 0)
        self.assertFalse(self.judge_dir.exists())


class JudgePromptsCliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(RUN_EVAL), *args],
                              capture_output=True, text=True)

    def test_unknown_run_exits_2_without_ai_call(self):
        proc = self.run_cli("--judge-prompts", "no-such-run")
        self.assertEqual(proc.returncode, 2)
        self.assertIn("No run folder", proc.stderr)


if __name__ == "__main__":
    unittest.main()
