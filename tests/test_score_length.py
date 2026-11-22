"""Tests for the short-brief length range in evals/score.py (standard library only)."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("score", ROOT / "evals" / "score.py")
score = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(score)

CASE = """---
lang: en
type: tech-blog
non_tech: false
{extra}---

# SIMULATED DATA
"""


def run(extra, words):
    with tempfile.TemporaryDirectory() as d:
        case = Path(d) / "case.md"
        out = Path(d) / "out.md"
        case.write_text(CASE.format(extra=extra), encoding="utf-8")
        out.write_text(" ".join(["word"] * words) + ".\n", encoding="utf-8")
        return score.score_case(case, out)


def length_warnings(result):
    return [w for w in result["warnings"] if w.startswith("Length about ")]


class ShortBriefTests(unittest.TestCase):
    def setUp(self):
        prof = json.loads((ROOT / "skills" / "agent-plain-writing" / "languages" / "en" / "profile.json").read_text(encoding="utf-8"))
        self.full = prof["types"]["tech-blog"]["length"]
        self.short = prof["types"]["tech-blog"]["length_short"]

    def test_meta_reads_short_brief(self):
        self.assertTrue(score.parse_case_meta(CASE.format(extra="short_brief: true\n"))["short_brief"])
        self.assertFalse(score.parse_case_meta(CASE.format(extra=""))["short_brief"])

    def test_default_case_uses_full_range(self):
        r = run("", self.short[0])
        self.assertFalse(r["short_brief"])
        self.assertEqual(len(length_warnings(r)), 1)
        self.assertIn(f"allowed {self.full[0]}-{self.full[1]}", length_warnings(r)[0])

    def test_short_brief_uses_short_range(self):
        r = run("short_brief: true\n", self.short[0])
        self.assertTrue(r["short_brief"])
        self.assertEqual(length_warnings(r), [])

    def test_short_brief_still_warns_below_short_range(self):
        r = run("short_brief: true\n", self.short[0] - 50)
        self.assertEqual(len(length_warnings(r)), 1)
        self.assertIn(f"allowed {self.short[0]}-{self.short[1]}", length_warnings(r)[0])

    def test_short_brief_warns_above_short_range(self):
        r = run("short_brief: true\n", self.short[1] + 50)
        self.assertEqual(len(length_warnings(r)), 1)
        self.assertIn(f"allowed {self.short[0]}-{self.short[1]}", length_warnings(r)[0])

    def test_short_brief_on_type_without_length_range(self):
        with tempfile.TemporaryDirectory() as d:
            case = Path(d) / "case.md"
            out = Path(d) / "out.md"
            case.write_text("---\nlang: en\ntype: essay\nnon_tech: false\nshort_brief: true\n---\n\n# SIMULATED DATA\n", encoding="utf-8")
            out.write_text("Short essay sentence.\n", encoding="utf-8")
            r = score.score_case(case, out)
        self.assertTrue(r["short_brief"])
        self.assertEqual(length_warnings(r), [])


if __name__ == "__main__":
    unittest.main()


class StripTrailingReportTest(unittest.TestCase):
    def test_strips_after_last_rule(self):
        self.assertEqual(score.strip_trailing_report("Body.\n\n---\nGuesses: none.\n"), "Body.\n")

    def test_no_rule_keeps_text(self):
        self.assertEqual(score.strip_trailing_report("Body.\n"), "Body.\n")
