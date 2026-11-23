"""Tests pattern checks in shared/scripts/check_style.py (standard library only)."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKER = ROOT / "shared" / "scripts" / "check_style.py"


def run_checker(text, lang, doc_type="common"):
    with tempfile.TemporaryDirectory() as d:
        draft = Path(d) / "draft.md"
        draft.write_text(text + "\n", encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(CHECKER), str(draft), "--lang", lang, "--type", doc_type],
            capture_output=True, text=True,
        )


CASES = [
    # (pattern, lang, bad_text, good_text, expect_bad_code)
    ("dash", "en", "Shared values—the user—stayed global.", "Shared values, the user, stayed global.", 1),
    ("dash", "vi", "Hệ thống chạy nhanh—không cần chờ.", "Hệ thống chạy nhanh, không cần chờ.", 1),
    ("dash", "ja", "処理が速い—待ち時間はない。", "処理は速く、待ち時間はない。", 1),
    ("middle_dot", "en", "First · Second.", "First, Second.", 1),
    ("middle_dot", "vi", "Một · Hai.", "Một, Hai.", 1),
    ("middle_dot", "ja", "一つ·二つ。", "一つ、二つ。", 1),
    ("curly_quotes", "en", "She said “hello” quickly.", 'She said "hello" quickly.', 1),
    ("curly_quotes", "vi", "Cô ấy nói “xin chào” ngay.", 'Cô ấy nói "xin chào" ngay.', 0),
    ("curly_quotes", "ja", "彼女は「こんにちは」と“笑顔”で言った。", "彼女は「こんにちは」と言った。", 0),
    ("count_opening", "en", "Three things to know. Cache keys expire.", "Cache keys expire after ten minutes.", 1),
    ("count_opening", "vi", "3 điều cần biết khi triển khai.", "Chạy di trú trước khi bật dịch vụ.", 1),
    ("count_opening", "ja", "3つのポイントを確認する。", "配備の前に移行を実行する。", 1),
    ("negative_parallel", "en", "This is not just a fix, it's a rewrite.", "This rewrite replaces the queue.", 1),
    ("negative_parallel", "vi", "Hệ thống không chỉ nhanh mà còn rẻ.", "Hệ thống chạy nhanh. Chi phí cũng thấp.", 1),
    ("negative_parallel", "ja", "この仕組みは速いだけでなくコストも安い。", "この仕組みは速く、費用も低い。", 1),
    ("question_run", "en", "Why did it fail? Could the cache be stale?", "The job failed because the cache was stale.", 1),
    ("question_run", "vi", "Vì sao lỗi xảy ra? Có phải do cache cũ?", "Lỗi xảy ra vì cache đã cũ.", 1),
    ("question_run", "ja", "なぜ失敗したのか？キャッシュが古いのか？", "キャッシュが古いため失敗した。", 1),
]


class PatternCheckTests(unittest.TestCase):
    def test_pattern_cases(self):
        for name, lang, bad, good, expect_bad in CASES:
            with self.subTest(pattern=name, lang=lang, kind="bad"):
                r = run_checker(bad, lang)
                self.assertEqual(r.returncode, expect_bad, r.stdout + r.stderr)
            with self.subTest(pattern=name, lang=lang, kind="good"):
                r = run_checker(good, lang)
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_code_blocks_are_ignored(self):
        text = "Plain sentence.\n\n```\nShared—value · “quoted”\nWhy? What?\n```\n"
        r = run_checker(text, "en")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
