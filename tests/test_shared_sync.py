"""Tests for the generated sub-skills: parity with shared/ and frontmatter (standard library only)."""
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
LANGS = ["vi", "en", "ja"]


def skill_dirs():
    return sorted(p for p in SKILLS.iterdir() if p.is_dir())


class SharedSyncTests(unittest.TestCase):
    def test_sync_check_passes(self):
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_shared.py"), "--check"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_name_matches_folder(self):
        for d in skill_dirs():
            text = (d / "SKILL.md").read_text(encoding="utf-8")
            m = re.search(r"^name: (.+)$", text, re.M)
            self.assertIsNotNone(m, d.name)
            self.assertEqual(m.group(1).strip(), d.name)

    def test_description_is_one_quoted_line(self):
        for d in skill_dirs():
            text = (d / "SKILL.md").read_text(encoding="utf-8")
            front = text.split("---")[1]
            lines = [l for l in front.splitlines() if l.startswith("description:")]
            self.assertEqual(len(lines), 1, d.name)
            m = re.fullmatch(r'description: "([^"]*)"', lines[0])
            self.assertIsNotNone(m, f"{d.name}: description must be one quoted line with no inner quotes")
            self.assertLess(len(m.group(1)), 1024, d.name)

    def test_router_holds_only_skill_md(self):
        files = sorted(p.name for p in (SKILLS / "agent-plain-writing").iterdir())
        self.assertEqual(files, ["SKILL.md"])

    def test_language_file_sets_match(self):
        for d in (p for p in skill_dirs() if p.name != "agent-plain-writing"):
            sets = [sorted(str(p.relative_to(d / "languages" / l))
                           for p in (d / "languages" / l).rglob("*") if p.is_file())
                    for l in LANGS]
            self.assertEqual(sets[0], sets[1], d.name)
            self.assertEqual(sets[0], sets[2], d.name)

    def test_subskills_hold_only_matching_example(self):
        prefix = "agent-plain-writing-"
        for d in (p for p in skill_dirs() if p.name != "agent-plain-writing"):
            self.assertTrue(d.name.startswith(prefix), d.name)
            doc_type = d.name[len(prefix):]
            for lang in LANGS:
                examples = sorted(p.name for p in (d / "languages" / lang / "examples").iterdir() if p.is_file())
                self.assertEqual(examples, [f"{doc_type}.md"], f"{d.name}/{lang}")


if __name__ == "__main__":
    unittest.main()
