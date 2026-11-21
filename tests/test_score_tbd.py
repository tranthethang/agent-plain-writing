"""Tests for the TBD-n statistics in evals/score.py (standard library only)."""

import importlib.util
import unittest
from pathlib import Path

SCORE_PATH = Path(__file__).resolve().parent.parent / "evals" / "score.py"
_spec = importlib.util.spec_from_file_location("score", SCORE_PATH)
score = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(score)


def duplicates(text):
    return score.tbd_stats(text)[3]


class DuplicateQuestionTests(unittest.TestCase):
    def test_no_tbd_gives_empty_list(self):
        self.assertEqual(duplicates("# Spec\n\nNo open items.\n"), [])

    def test_case_and_punctuation_are_ignored(self):
        text = (
            "- TBD-1: What is X?\n"
            "- `TBD-2`: what is x\n"
            "- TBD-3：WHAT IS X？\n"
        )
        self.assertEqual(duplicates(text), [["TBD-1", "TBD-2", "TBD-3"]])

    def test_different_questions_are_not_grouped(self):
        text = "- TBD-1: What is X?\n- TBD-2: What is Y?\n"
        self.assertEqual(duplicates(text), [])

    def test_empty_questions_are_not_grouped(self):
        self.assertEqual(duplicates("- TBD-1:\n- TBD-2:\n"), [])

    def test_same_id_twice_is_not_a_duplicate(self):
        text = "- TBD-1: What is X?\n- TBD-1: What is X?\n"
        self.assertEqual(duplicates(text), [])

    def test_groups_sorted_by_first_id(self):
        text = (
            "- TBD-11: Status error?\n"
            "- TBD-2: Max length?\n"
            "- TBD-9: status error\n"
            "- TBD-10: max length\n"
        )
        self.assertEqual(
            duplicates(text), [["TBD-2", "TBD-10"], ["TBD-9", "TBD-11"]]
        )

    def test_lines_in_code_block_are_not_questions(self):
        text = "```\n- TBD-1: What is X?\n- TBD-2: What is X?\n```\n"
        ids, without_question, in_code, dups = score.tbd_stats(text)
        self.assertEqual(dups, [])
        self.assertEqual(in_code, ["TBD-1", "TBD-2"])


if __name__ == "__main__":
    unittest.main()
