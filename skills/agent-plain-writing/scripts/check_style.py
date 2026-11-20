#!/usr/bin/env python3
"""Plain-writing checker for Vietnamese (vi), English (en) and Japanese (ja).

Usage:
    python3 scripts/check_style.py draft.md --lang en --type blog
    python3 scripts/check_style.py spec.md  --lang ja --type design
    python3 scripts/check_style.py guide.md --lang vi --type guide
    python3 scripts/check_style.py post.md  --lang en --type blog --non-tech

Limits, banned phrases and jargon lists come from languages/<lang>/.
Exit code: 0 = clean, 1 = violations, 2 = usage error.

Units: vi counts syllables (tieng), en counts words, ja counts characters.
The script is mechanical. It does not judge voice, rhyme or meter.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANG_DIR = ROOT / "languages"
TYPE_ALIASES = {"detail-design": "design", "user-guide": "guide"}


def available_langs():
    return sorted(p.name for p in LANG_DIR.iterdir() if (p / "profile.json").exists())


def load_profile(lang):
    path = LANG_DIR / lang / "profile.json"
    return json.loads(path.read_text(encoding="utf-8"))


def load_banned(lang, doc_type):
    section, out = "all", []
    for line in (LANG_DIR / lang / "banned.txt").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.fullmatch(r"\[(\w+)\]", line)
        if m:
            section = m.group(1)
            continue
        if section in ("all", doc_type):
            out.append(line.lower())
    return out


def load_terms(lang):
    path = LANG_DIR / lang / "terms.txt"
    return [
        l.strip().lower()
        for l in path.read_text(encoding="utf-8").splitlines()
        if l.strip() and not l.lstrip().startswith("#")
    ]


def clean(text):
    text = unicodedata.normalize("NFC", text).replace("’", "'")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`]*`", "X", text)
    text = re.sub(r"https?://\S+", "URL", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\*{1,3}", "", text)
    return text


ITEM = re.compile(r"(?:[-+]\s+|・\s*|\d+[.)．）]\s+)(.*)")


def split_blocks(text):
    """Return (kind, text) pairs. kind is 'para' or 'item'."""
    blocks, cur = [], []

    def flush():
        if cur:
            blocks.append(("para", " ".join(cur)))
            cur.clear()

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            flush()
            continue
        if line.startswith("#") or line.startswith("|") or re.fullmatch(r"[-=_ ]{3,}", line):
            flush()
            continue
        m = ITEM.match(line)
        if m:
            flush()
            blocks.append(("item", m.group(1)))
            continue
        cur.append(line.lstrip("> "))
    flush()
    return blocks


def count_units(s, unit):
    if unit == "char":
        return sum(1 for ch in s if unicodedata.category(ch)[0] not in "PZC")
    if unit == "word":
        return len(re.findall(r"\w[\w'-]*", s))
    return len(re.findall(r"\w+", s))  # syllable (Vietnamese)


def split_sentences(s, pattern):
    return [x.strip() for x in re.split(pattern, s) if x.strip()]


def phrase_pattern(phrase, boundary, end_boundary=False):
    p = re.escape(phrase)
    if boundary:
        p = r"(?<!\w)" + p
        if end_boundary:
            p += r"(?!\w)"
    return p


def main():
    langs = available_langs()
    ap = argparse.ArgumentParser(description="Plain-writing checker")
    ap.add_argument("file")
    ap.add_argument("--lang", required=True, choices=langs)
    ap.add_argument("--type", dest="doc_type", default="blog",
                    help="blog, prose, poetry, design, guide")
    ap.add_argument("--non-tech", action="store_true",
                    help="limit jargon (reader is outside the field)")
    args = ap.parse_args()

    doc_type = TYPE_ALIASES.get(args.doc_type, args.doc_type)
    prof = load_profile(args.lang)
    if doc_type not in prof["types"]:
        print(f"Unknown type '{args.doc_type}'. Use: {', '.join(prof['types'])}", file=sys.stderr)
        return 2
    cfg = dict(prof["types"][doc_type])
    if args.non_tech and cfg["terms"] is None:
        cfg["terms"] = prof.get("non_tech_terms", 3)

    unit, label = prof["unit"], prof["unit_label"]
    boundary = prof["boundary"]

    text = clean(Path(args.file).read_text(encoding="utf-8"))
    blocks = split_blocks(text)

    issues, total, n_sent = [], 0, 0
    for kind, body in blocks:
        sents = split_sentences(body, prof["sentence_split"])
        n_sent += len(sents)
        total += count_units(body, unit)
        if cfg["sentence"]:
            for s in sents:
                n = count_units(s, unit)
                if n > cfg["sentence"]:
                    issues.append(f'Sentence has {n} {label} (max {cfg["sentence"]}): "{s[:60]}..."')
        if kind == "para" and cfg["paragraph"] and len(sents) > cfg["paragraph"]:
            issues.append(f'Paragraph has {len(sents)} sentences (max {cfg["paragraph"]}): "{body[:50]}..."')

    lower = text.lower()
    for phrase in load_banned(args.lang, doc_type):
        c = len(re.findall(phrase_pattern(phrase, boundary), lower))
        if c:
            issues.append(f'Banned phrase "{phrase}": {c}x')

    if cfg["terms"] is not None:
        found = [t for t in load_terms(args.lang)
                 if re.search(phrase_pattern(t, boundary, end_boundary=True), lower)]
        if len(found) > cfg["terms"]:
            issues.append(f'Jargon: {len(found)} terms (max {cfg["terms"]}): {", ".join(found)}')

    length = round(total / prof["length_divisor"])
    if cfg["length"]:
        lo, hi = cfg["length"]
        if not lo <= length <= hi:
            issues.append(f'Length about {length} {prof["length_label"]} (allowed {lo}-{hi})')

    avg = total / n_sent if n_sent else 0
    print(f"lang={args.lang} type={doc_type} | {total} {label} "
          f"(about {length} {prof['length_label']}), {n_sent} sentences, "
          f"avg {avg:.1f} {label}/sentence")
    if issues:
        print(f"\n{len(issues)} violation(s):")
        for i in issues:
            print(f"- {i}")
        return 1
    print("No violations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
