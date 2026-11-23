"""Tests that the last fenced sample in every examples file passes the checker (standard library only)."""

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "agent-plain-writing"
CHECKER = SKILL / "scripts" / "check_style.py"
LANGS = ("vi", "en", "ja")
FILE_TYPES = {
    "tech-blog.md": "tech-blog",
    "essay.md": "essay",
    "api-design.md": "api-design",
    "user-guide.md": "user-guide",
    "common.md": "common",
}
FENCE_RE = re.compile(r"^(`{3,})[^\n]*\n(.*?)\n^\1[ \t]*$", re.M | re.S)


def extract_last_fenced_block(text):
    matches = FENCE_RE.findall(text)
    if not matches:
        return None
    return matches[-1][1]


class ExamplesSamplesTests(unittest.TestCase):
    def test_shipped_samples_pass_checker(self):
        for lang in LANGS:
            ex_dir = SKILL / "languages" / lang / "examples"
            for filename, doc_type in FILE_TYPES.items():
                path = ex_dir / filename
                with self.subTest(lang=lang, file=filename):
                    block = extract_last_fenced_block(path.read_text(encoding="utf-8"))
                    self.assertIsNotNone(block, f"No fenced block found in {path}")
                    with tempfile.TemporaryDirectory() as d:
                        sample = Path(d) / filename
                        sample.write_text(block + "\n", encoding="utf-8")
                        r = subprocess.run(
                            [sys.executable, str(CHECKER), str(sample), "--lang", lang, "--type", doc_type],
                            capture_output=True, text=True,
                        )
                    self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
