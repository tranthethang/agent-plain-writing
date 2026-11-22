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
    def test_every_type_has_a_doc_type_file(self):
        for t in TYPES:
            name = "user-guide.md" if t == "guide" else f"{t}.md"
            self.assertTrue((SKILL / "doc-types" / name).is_file(), name)

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
    def test_default_type_is_common(self):
        r = run_checker("Short text.\n", "--lang", "en")
        self.assertIn("type=common", r.stdout + r.stderr)

    def test_blog_is_rejected(self):
        r = run_checker("Short text.\n", "--lang", "en", "--type", "blog")
        self.assertEqual(r.returncode, 2)
        self.assertIn("tech-blog", r.stderr)

    def test_new_types_are_accepted(self):
        for t in ("tech-blog", "essay"):
            r = run_checker("Short text.\n", "--lang", "en", "--type", t)
            self.assertIn(r.returncode, (0, 1), t)

    def test_common_type_is_accepted(self):
        for lang in LANGS:
            r = run_checker("Short text.\n", "--lang", lang, "--type", "common")
            self.assertIn(r.returncode, (0, 1), lang)
            self.assertIn("type=common", r.stdout)


LONG_CELL = ("This field holds the identifier of the customer account that the request "
             "will update when the server accepts the call today.")
TABLE = f"| Field | Notes |\n|---|---|\n| id | {LONG_CELL} |\n"


class CheckerFeatureTests(unittest.TestCase):
    def test_api_design_checks_table_cells(self):
        r = run_checker(TABLE, "--lang", "en", "--type", "api-design")
        self.assertEqual(r.returncode, 1)
        self.assertIn("Sentence has", r.stdout)

    def test_other_types_skip_tables(self):
        r = run_checker(TABLE, "--lang", "en", "--type", "tech-blog")
        self.assertEqual(r.returncode, 0)

    def test_separator_row_gives_no_cells(self):
        self.assertEqual(checker.table_cells("|:---|---:|"), [])
        self.assertEqual(checker.table_cells("| a | b |"), ["a", "b"])

    def test_report_label_in_middle_is_flagged(self):
        text = "One.\n\nTwo.\n\nThree.\n\nResult: done.\n\nFour.\n\nFive.\n\nSix.\n\nSeven.\n"
        r = run_checker(text, "--lang", "en", "--type", "tech-blog")
        self.assertEqual(r.returncode, 1)
        self.assertIn("Report line", r.stdout)

    def test_report_label_in_fence_is_ignored(self):
        r = run_checker("One.\n\n```\nResult: ok\n```\n\nTwo.\n", "--lang", "en", "--type", "tech-blog")
        self.assertEqual(r.returncode, 0)

    def test_short_brief_uses_length_short(self):
        hi = profile("en")["types"]["tech-blog"]["length_short"][1]
        text = " ".join(["Word"] * (hi + 50)) + ".\n"
        full = run_checker(text, "--lang", "en", "--type", "tech-blog").stdout
        short = run_checker(text, "--lang", "en", "--type", "tech-blog", "--short-brief")
        self.assertNotIn("Length about", full)
        self.assertIn("Length about", short.stdout)

    def test_length_warns_only_above_upper_limit(self):
        prof = {"length_label": "words"}
        self.assertIsNone(checker.length_warning(prof, [600, 800], 235))
        self.assertIsNone(checker.length_warning(prof, [600, 800], 800))
        self.assertIn("Length about 900", checker.length_warning(prof, [600, 800], 900))
        self.assertIn("Length about 550", checker.length_warning(prof, [300, 500], 550))


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


class TimeDateUnitTests(unittest.TestCase):
    def test_en_counts_time_and_date_as_one_word(self):
        self.assertEqual(checker.count_units("On 2026-12-03 at 04:00 UTC the cluster restarts.", "word"), 8)

    def test_vi_counts_time_and_date_as_one_syllable(self):
        self.assertEqual(checker.count_units("Lúc 04:00 ngày 2026-12-03 hệ thống khởi động lại.", "syllable"), 9)

    def test_ja_count_is_unchanged(self):
        text = "04:00に再起動します。"
        self.assertEqual(checker.count_units(text, "char"), sum(1 for ch in text if ch not in ":。"))

    def test_colon_does_not_split_sentence(self):
        text = "The job runs at 04:00 UTC daily."
        self.assertEqual(len(checker.split_sentences(text, profile("en")["sentence_split"])), 1)


class ConfigSearchTests(unittest.TestCase):
    def test_config_found_from_subfolder(self):
        cfg = "```plain-writing\n{\"banned\": [\"zorblax\"]}\n```\n"
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / ".git").mkdir()
            (root / "PLAIN-WRITING.md").write_text(cfg, encoding="utf-8")
            sub = root / "a" / "b"
            sub.mkdir(parents=True)
            doc = sub / "t.md"
            doc.write_text("The zorblax restarts.\n", encoding="utf-8")
            r = subprocess.run(
                [sys.executable, str(CHECKER), "t.md", "--lang", "en", "--type", "common"],
                capture_output=True, text=True, cwd=sub,
            )
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("zorblax", r.stdout)


if __name__ == "__main__":
    unittest.main()
