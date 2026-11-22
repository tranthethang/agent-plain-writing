"""Tests for the document-type set, the checker default and banned-guide parity (standard library only)."""

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "agent-plain-writing"
CHECKER = SKILL / "scripts" / "check_style.py"
_spec = importlib.util.spec_from_file_location("check_style", CHECKER)
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)
LANGS = ["vi", "en", "ja"]
TYPES = {"tech-blog", "essay", "api-design", "guide", "common"}
UNITS_ROW = {"vi": "vi", "en": "en", "ja": "ja"}


def run_checker(text, *args):
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "t.md"
        f.write_text(text, encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(CHECKER), str(f), *args],
            capture_output=True, text=True,
        )


def profile(lang):
    return json.loads((SKILL / "languages" / lang / "profile.json").read_text(encoding="utf-8"))


class TypeSetTests(unittest.TestCase):
    def test_profiles_have_only_current_types(self):
        for lang in LANGS:
            self.assertEqual(set(profile(lang)["types"]), TYPES, lang)

    def test_essay_limits(self):
        sentence = {"vi": 40, "en": 30, "ja": 80}
        for lang in LANGS:
            essay = profile(lang)["types"]["essay"]
            self.assertEqual(essay["sentence"], sentence[lang])
            self.assertEqual(essay["paragraph"], 6)
            self.assertIsNone(essay["length"])
            self.assertIsNone(essay["terms"])

    def test_banned_sections_have_no_old_types(self):
        for lang in LANGS:
            text = (SKILL / "languages" / lang / "banned.txt").read_text(encoding="utf-8")
            names = set()
            for header in re.findall(r"^\[([^\]]+)\]", text, re.M):
                names |= {n.strip() for n in header.split(",")}
            self.assertTrue({"tech-blog", "essay"} <= names, lang)
            self.assertFalse(names & {"blog", "prose", "poetry"}, lang)

    def test_shared_header_applies_to_both_types(self):
        for lang in LANGS:
            tech, essay, api = (set(checker.load_banned(lang, t)[0]) for t in ("tech-blog", "essay", "api-design"))
            self.assertEqual(tech, essay, lang)
            self.assertTrue(tech - api, lang)

    def test_language_folders_match(self):
        sets = [
            sorted(p.name for p in (SKILL / "languages" / l).iterdir() if p.name != "__pycache__")
            for l in LANGS
        ]
        self.assertEqual(sets[0], sets[1])
        self.assertEqual(sets[0], sets[2])
        ex = [sorted(p.name for p in (SKILL / "languages" / l / "examples").iterdir()) for l in LANGS]
        self.assertEqual(ex[0], ["api-design.md", "common.md", "essay.md", "tech-blog.md", "user-guide.md"])
        self.assertEqual(ex[0], ex[1])
        self.assertEqual(ex[0], ex[2])


class CheckerTypeTests(unittest.TestCase):
    def test_default_type_is_tech_blog(self):
        r = run_checker("Short text.\n", "--lang", "en")
        self.assertIn("type=tech-blog", r.stdout + r.stderr)

    def test_blog_is_rejected(self):
        r = run_checker("Short text.\n", "--lang", "en", "--type", "blog")
        self.assertEqual(r.returncode, 2)
        self.assertIn("tech-blog", r.stderr)

    def test_new_types_are_accepted(self):
        for t in ("tech-blog", "essay"):
            r = run_checker("Short text.\n", "--lang", "en", "--type", t)
            self.assertIn(r.returncode, (0, 1), t)


class ParityTests(unittest.TestCase):
    def test_readme_units_match_profiles(self):
        for path in (ROOT / "README.md", ROOT / "docs" / "vi" / "README.md"):
            self.check_units(path.read_text(encoding="utf-8"), path.name)

    def check_units(self, readme, name):
        order = ["tech-blog", "essay", "api-design", "guide", "common"]
        for lang in LANGS:
            row = next(l for l in readme.splitlines() if l.startswith(f"| `{lang}` |"))
            cells = [c.strip() for c in row.strip("|").split("|")][2:]
            want = [
                f"{profile(lang)['types'][t]['sentence']} / {profile(lang)['types'][t]['paragraph']}"
                for t in order
            ]
            self.assertEqual(cells, want, f"{name} {lang}")

    def test_banned_guide_lists_every_phrase(self):
        for lang in LANGS:
            d = SKILL / "languages" / lang
            guide = (d / "banned-guide.md").read_text(encoding="utf-8")
            for sec in ("tech-blog", "essay"):
                for p in checker.load_banned(lang, sec)[0]:
                    self.assertIn(p.split("|")[0].strip(), guide.lower(), f"{lang} {sec} {p}")


if __name__ == "__main__":
    unittest.main()
