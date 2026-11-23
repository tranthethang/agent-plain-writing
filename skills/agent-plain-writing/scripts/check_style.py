#!/usr/bin/env python3
"""Plain-writing checker for Vietnamese (vi), English (en) and Japanese (ja).

Usage:
    python3 scripts/check_style.py draft.md --lang en --type tech-blog
    python3 scripts/check_style.py spec.md  --lang ja --type api-design
    python3 scripts/check_style.py user-guide.md --lang vi --type user-guide
    python3 scripts/check_style.py post.md  --lang en --type tech-blog --non-tech

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


def available_langs():
    return sorted(p.name for p in LANG_DIR.iterdir() if (p / "profile.json").exists())


def load_profile(lang):
    path = LANG_DIR / lang / "profile.json"
    return json.loads(path.read_text(encoding="utf-8"))


def load_banned(lang, doc_type):
    section, out, warns = ["all"], [], []
    for line in (LANG_DIR / lang / "banned.txt").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.fullmatch(r"\[([\w-]+(?:\s*,\s*[\w-]+)*)\]", line)
        if m:
            section = [s.strip() for s in m.group(1).split(",")]
            continue
        if "all" in section or doc_type in section:
            out.append(line.lower())
        elif "warn" in section:
            warns.append(line.lower())
    return out, warns


def load_report_labels(lang):
    """Labels in the [report] section of banned.txt."""
    section, out = ["all"], []
    for line in (LANG_DIR / lang / "banned.txt").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.fullmatch(r"\[([\w-]+(?:\s*,\s*[\w-]+)*)\]", line)
        if m:
            section = [s.strip() for s in m.group(1).split(",")]
            continue
        if "report" in section:
            out.append(line.lower())
    return out


def report_issues(text, labels):
    """Flag report labels on any non-empty line outside fenced code blocks."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    lines = [l.strip().lstrip("-*> ").strip().lower() for l in text.splitlines()
             if l.strip() and not l.lstrip().startswith("#")]
    issues = []
    for line in lines:
        for label in labels:
            if line.startswith(label):
                issues.append(f'Report line inside the document: "{line[:50]}"')
                break
    return issues


def hard_break_issues(raw):
    """Flag trailing-space line breaks outside code blocks."""
    body = re.sub(r"```.*?```", "", raw, flags=re.S)
    n = len(re.findall(r"\S {2,}\n(?=[ \t]*\S)", body))
    return [f"Line break with trailing spaces: {n}x"] if n else []


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
    text = re.sub(r"https?://\S+?(?=[.,!?;:)\]]*(?:\s|$))", "URL", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\*{1,3}", "", text)
    return text


ITEM = re.compile(r"(?:[-+]\s+|・\s*|\d+[.)．）]\s+)(.*)")


def table_cells(line):
    """Return the non-empty cells of a table row. A separator row gives none."""
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
        return []
    return [c for c in cells if c]


def split_blocks(text, doc_type=None):
    """Return (kind, text) pairs. kind is 'para' or 'item'.

    Table rows are skipped, except in `api-design`, where each cell is an item."""
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
        if line.startswith("|") and doc_type == "api-design":
            flush()
            blocks.extend(("item", c) for c in table_cells(line))
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


TIME_DATE_RE = re.compile(r"(?<![\d:-])(?:\d{1,2}:\d{2}|\d{4}-\d{2}-\d{2})(?![\d:-])")


def count_units(s, unit):
    if unit == "char":
        return sum(1 for ch in s if unicodedata.category(ch)[0] not in "PZC")
    s = TIME_DATE_RE.sub("x", s)  # `hh:mm` and `YYYY-MM-DD` count as one unit
    if unit == "word":
        return len(re.findall(r"\w[\w'-]*", s))
    return len(re.findall(r"\w+", s))  # syllable (Vietnamese)


ABBREV_RE = re.compile(
    r"\b(?:e\.g|i\.e|etc|vs|cf|dr|mr|mrs|ms|prof|v\.v)\.",
    re.IGNORECASE,
)


def split_sentences(s, pattern):
    # Protect dots in decimals, versions, URLs, and common abbreviations before splitting.
    protected = re.sub(
        r"https?://\S+?(?=[.,!?;:)\]]*(?:\s|$))",
        lambda m: m.group(0).replace(".", "\x00"),
        s,
    )
    protected = re.sub(r"(?<=\d)\.(?=\d)", "\x00", protected)
    protected = ABBREV_RE.sub(lambda m: m.group(0).replace(".", "\x00"), protected)
    return [x.replace("\x00", ".").strip() for x in re.split(pattern, protected) if x.strip()]


def phrase_pattern(phrase, boundary, end_boundary=False):
    p = re.escape(phrase)
    if boundary:
        p = r"(?<!\w)" + p
        if end_boundary:
            p += r"(?!\w)"
    return p


def find_project_config(start):
    """Look for PLAIN-WRITING.md in `start`, then each parent. Stop after a folder that holds `.git`."""
    for folder in [start, *start.parents]:
        candidate = folder / "PLAIN-WRITING.md"
        if candidate.exists():
            return candidate
        if (folder / ".git").exists():
            return None
    return None


def load_project_config(config_path):
    """Load optional PLAIN-WRITING.md config from --config, or by searching up from cwd."""
    if config_path is not None:
        path = Path(config_path)
        if not path.exists():
            print(f"Config file not found: {path}", file=sys.stderr)
            return None, True
    else:
        path = find_project_config(Path.cwd())
        if path is None:
            return {}, False
    text = path.read_text(encoding="utf-8")
    m = re.search(r"```plain-writing\s*\n(.*?)\n```", text, flags=re.S)
    if not m:
        return {}, False
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON in {path}: {exc}", file=sys.stderr)
        return None, True
    if not isinstance(data, dict):
        print(f"Invalid config in {path}: expected JSON object", file=sys.stderr)
        return None, True
    return data, False


def length_range(cfg, short_brief=False):
    """Return the (lo, hi) length range, or None. A short brief uses `length_short` when the profile has it."""
    if short_brief and cfg.get("length_short"):
        return cfg["length_short"]
    return cfg.get("length")


def length_warning(prof, rng, length):
    """Return a warning only when the length is above the upper limit, else None. A shorter text is fine."""
    if not rng:
        return None
    lo, hi = rng
    if length <= hi:
        return None
    return f'Length about {length} {prof["length_label"]} (allowed {lo}-{hi})'


def main():
    langs = available_langs()
    ap = argparse.ArgumentParser(description="Plain-writing checker")
    ap.add_argument("file")
    ap.add_argument("--lang", default=None, choices=langs)
    ap.add_argument("--type", dest="doc_type", default=None,
                    help="tech-blog, essay, api-design, user-guide, common")
    ap.add_argument("--non-tech", action="store_true",
                    help="limit jargon (reader is outside the field)")
    ap.add_argument("--config", default=None,
                    help="path to PLAIN-WRITING.md (default: search the current folder, then its parents)")
    ap.add_argument("--short-brief", action="store_true",
                    help="use length_short when the type has it")
    args = ap.parse_args()

    proj, err = load_project_config(args.config)
    if err:
        return 2

    lang = args.lang or proj.get("default_lang")
    if not lang:
        print("Missing --lang (and no default_lang in PLAIN-WRITING.md)", file=sys.stderr)
        return 2
    if lang not in langs:
        print(f"Unknown lang '{lang}'. Use: {', '.join(langs)}", file=sys.stderr)
        return 2

    doc_type = args.doc_type or proj.get("default_type") or "common"
    prof = load_profile(lang)
    if doc_type not in prof["types"]:
        print(f"Unknown type '{doc_type}'. Use: {', '.join(prof['types'])}", file=sys.stderr)
        return 2
    cfg = dict(prof["types"][doc_type])
    warnings = []

    proj_limits = (proj.get("limits") or {}).get(doc_type, {})
    for key in ("sentence", "paragraph", "terms"):
        if key in proj_limits and proj_limits[key] is not None:
            base = cfg.get(key)
            val = proj_limits[key]
            if base is not None and val > base * 1.5:
                warnings.append(
                    f'Project limit "{key}"={val} exceeds 1.5x profile base ({base})'
                )
            cfg[key] = val

    if args.non_tech and cfg["terms"] is None:
        cfg["terms"] = prof.get("non_tech_terms", 3)

    unit, label = prof["unit"], prof["unit_label"]
    boundary = prof["boundary"]

    if not Path(args.file).is_file():
        print(f"File not found: {args.file}", file=sys.stderr)
        return 2
    raw = unicodedata.normalize("NFC", Path(args.file).read_text(encoding="utf-8"))
    text = clean(raw)
    blocks = split_blocks(text, doc_type)

    issues, total, n_sent = [], 0, 0
    issues += report_issues(text, load_report_labels(lang))
    issues += hard_break_issues(raw)
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
    banned_phrases, warn_phrases = load_banned(lang, doc_type)
    extra_banned = [str(p).strip().lower() for p in (proj.get("banned") or []) if str(p).strip()]
    for phrase in dict.fromkeys(banned_phrases + extra_banned):
        c = len(re.findall(phrase_pattern(phrase, boundary), lower))
        if c:
            issues.append(f'Banned phrase "{phrase}": {c}x')

    for phrase in warn_phrases:
        c = len(re.findall(phrase_pattern(phrase, boundary), lower))
        if c:
            warnings.append(f'Ambiguous phrase "{phrase}": {c}x')

    if cfg["terms"] is not None:
        extra_terms = [str(t).strip().lower() for t in (proj.get("terms") or []) if str(t).strip()]
        all_terms = list(dict.fromkeys(load_terms(lang) + extra_terms))
        found = [t for t in all_terms
                 if re.search(phrase_pattern(t, boundary, end_boundary=True), lower)]
        if len(found) > cfg["terms"]:
            issues.append(f'Jargon: {len(found)} terms (max {cfg["terms"]}): {", ".join(found)}')

    length = round(total / prof["length_divisor"])
    lw = length_warning(prof, length_range(cfg, args.short_brief), length)
    if lw:
        warnings.append(lw)

    avg = total / n_sent if n_sent else 0
    print(f"lang={lang} type={doc_type} | {total} {label} "
          f"(about {length} {prof['length_label']}), {n_sent} sentences, "
          f"avg {avg:.1f} {label}/sentence")
    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings:
            print(f"- {w}")
    if issues:
        print(f"\n{len(issues)} violation(s):")
        for i in issues:
            print(f"- {i}")
        return 1
    print("No violations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
