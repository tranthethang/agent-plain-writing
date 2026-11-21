#!/usr/bin/env python3
"""Mechanical scorer and judge-prompt builder for agent-plain-writing evals.

Usage:
    python3 evals/score.py evals/cases/tech-blog-en.md output.md
    python3 evals/score.py evals/cases/tech-blog-en.md output.md --judge-prompt
"""
import argparse
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / "skills" / "agent-plain-writing" / "scripts"
JUDGE_TEMPLATE = Path(__file__).resolve().parent / "judge-prompt.md"

sys.path.insert(0, str(SCRIPTS_DIR))
import check_style  # noqa: E402


def parse_case_meta(case_text):
    """Extract lang, type, and non_tech from case frontmatter."""
    meta = {"lang": "en", "type": "tech-blog", "non_tech": False}
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", case_text, flags=re.S)
    if not m:
        return meta
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = [x.strip() for x in line.split(":", 1)]
        if k == "lang":
            meta["lang"] = v
        elif k == "type":
            meta["type"] = check_style.TYPE_ALIASES.get(v, v)
        elif k == "non_tech":
            meta["non_tech"] = v.lower() in ("true", "1", "yes")
    return meta


def extract_numbers(text):
    """Return distinct numeric tokens from text, ignoring markdown list/heading numbers."""
    cleaned = check_style.clean(text)
    lines = []
    for line in cleaned.splitlines():
        s = line.strip()
        s = re.sub(r"^#+\s*\d+(?:\.\d+)*\.?\s*", "", s)
        s = re.sub(r"^\d+[.)．）]\s+", "", s)
        lines.append(s)
    joined = "\n".join(lines)
    joined = re.sub(r"`?TBD-\d+`?", "", joined)
    return set(
        re.findall(r"(?<![A-Za-z0-9_])(?<!\d\.)\d+(?:\.\d+)?(?!(?:\.\d|[A-Za-z0-9_]))", joined)
    )


def list_counts(text):
    """Return item counts of lists in text.

    A list is a line with two or more backticked tokens separated by commas,
    or a group of consecutive markdown bullet lines.
    """
    counts = set()
    group = 0
    for line in text.splitlines():
        if re.match(r"\s*[-*+]\s+\S", line):
            group += 1
        else:
            if group >= 2:
                counts.add(group)
            group = 0
        tokens = re.findall(r"`[^`]+`", line)
        if len(tokens) >= 2 and re.search(r"`\s*[,、，]\s*(?:and\s+|or\s+)?`", line):
            counts.add(len(tokens))
    if group >= 2:
        counts.add(group)
    return {str(n) for n in counts}


def _normalize_question(text):
    """Normalize a TBD-n question by lowercasing, removing punctuation, and collapsing spaces."""
    no_punct = "".join(
        " " if unicodedata.category(ch).startswith("P") else ch
        for ch in text.lower()
    )
    return " ".join(no_punct.split())


def tbd_stats(text):
    """Return TBD-n ids, ids without an Open items question, ids in code blocks, and duplicate question groups."""
    ids, in_code, asked = set(), set(), set()
    by_question = {}
    fenced = False
    for line in text.splitlines():
        if re.match(r"\s*(```|~~~)", line):
            fenced = not fenced
            continue
        found = re.findall(r"TBD-\d+", line)
        ids.update(found)
        if fenced:
            in_code.update(found)
            continue
        m = re.match(r"\s*[-*]\s*`?(TBD-\d+)`?\s*[:：]\s*(.*)", line)
        if m:
            tbd_id = m.group(1)
            asked.add(tbd_id)
            norm = _normalize_question(m.group(2))
            if norm:
                by_question.setdefault(norm, []).append(tbd_id)
    key = lambda x: int(x.split("-")[1])
    duplicates = [
        sorted(set(group), key=key)
        for group in by_question.values()
        if len(set(group)) >= 2
    ]
    duplicates.sort(key=lambda g: key(g[0]))
    return (
        sorted(ids, key=key),
        sorted(ids - asked, key=key),
        sorted(in_code, key=key),
        duplicates,
    )


def parse_checker_output(stdout):
    """Extract violation and warning lines from check_style.py stdout."""
    violations, warnings = [], []
    mode = None
    for line in stdout.splitlines():
        if line.startswith("Warnings ("):
            mode = "warn"
            continue
        if re.match(r"^\d+ violation\(s\):", line):
            mode = "viol"
            continue
        if line.strip() == "No violations.":
            mode = None
            continue
        if line.startswith("- "):
            item = line[2:]
            if mode == "warn":
                warnings.append(item)
            elif mode == "viol":
                violations.append(item)
    return violations, warnings


def score_case(case_path, output_path):
    """Compute mechanical metrics for one output against a case file."""
    case_path = Path(case_path)
    output_path = Path(output_path)
    case_text = case_path.read_text(encoding="utf-8")
    output_text = output_path.read_text(encoding="utf-8")
    meta = parse_case_meta(case_text)

    lang = meta["lang"]
    doc_type = meta["type"]
    non_tech = meta["non_tech"]

    cmd = [
        sys.executable,
        str(SCRIPTS_DIR / "check_style.py"),
        str(output_path),
        "--lang",
        lang,
        "--type",
        doc_type,
    ]
    if non_tech:
        cmd.append("--non-tech")
    proc = subprocess.run(cmd, capture_output=True, text=True)
    violations, warnings = parse_checker_output(proc.stdout)

    prof = check_style.load_profile(lang)
    unit = prof["unit"]
    boundary = prof["boundary"]
    cleaned = check_style.clean(output_text)
    blocks = check_style.split_blocks(cleaned)

    total_units = 0
    n_sent = 0
    for _, body in blocks:
        sents = check_style.split_sentences(body, prof["sentence_split"])
        n_sent += len(sents)
        total_units += check_style.count_units(body, unit)
    avg_sentence = round(total_units / n_sent, 1) if n_sent else 0.0

    lower = cleaned.lower()
    found_terms = [
        t for t in check_style.load_terms(lang)
        if re.search(check_style.phrase_pattern(t, boundary, end_boundary=True), lower)
    ]

    case_nums = extract_numbers(case_text)
    out_nums = extract_numbers(output_text)
    sourced = case_nums | list_counts(case_text)
    invented = sorted(out_nums - sourced, key=lambda x: (float(x), x))
    tbd_ids, tbd_without_question, tbd_in_code, tbd_duplicate_questions = tbd_stats(output_text)

    return {
        "case": str(case_path),
        "output": str(output_path),
        "lang": lang,
        "type": doc_type,
        "non_tech": non_tech,
        "unit": unit,
        "total_units": total_units,
        "sentences": n_sent,
        "avg_sentence_length": avg_sentence,
        "jargon_count": len(found_terms),
        "jargon_terms": found_terms,
        "violation_count": len(violations),
        "violations": violations,
        "warning_count": len(warnings),
        "warnings": warnings,
        "invented_numbers": invented,
        "tbd_ids": tbd_ids,
        "tbd_without_question": tbd_without_question,
        "tbd_in_code": tbd_in_code,
        "tbd_duplicate_questions": tbd_duplicate_questions,
        "checker_exit_code": proc.returncode,
    }


def build_judge_prompt(case_path, output_path):
    """Render evals/judge-prompt.md with the case and candidate output."""
    tmpl = JUDGE_TEMPLATE.read_text(encoding="utf-8")
    case_text = Path(case_path).read_text(encoding="utf-8")
    output_text = Path(output_path).read_text(encoding="utf-8")
    return tmpl.replace("{{CASE}}", case_text).replace("{{OUTPUT}}", output_text)


def main():
    ap = argparse.ArgumentParser(description="Score an eval output against a case.")
    ap.add_argument("case", help="Path to case markdown file")
    ap.add_argument("output", help="Path to generated output markdown file")
    ap.add_argument("--judge-prompt", action="store_true",
                    help="Print the rendered AI judge prompt instead of JSON")
    args = ap.parse_args()

    if args.judge_prompt:
        print(build_judge_prompt(args.case, args.output))
        return 0

    result = score_case(args.case, args.output)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
