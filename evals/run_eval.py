#!/usr/bin/env python3
"""Run agent-plain-writing evals with and without the skill, then score outputs.

Usage:
    python3 evals/run_eval.py --dry-run
    python3 evals/run_eval.py --tool openai
    python3 evals/run_eval.py --tool claude --dry-run
"""
import argparse
import datetime
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES_DIR = Path(__file__).resolve().parent / "cases"
RUNS_DIR = Path(__file__).resolve().parent / "runs"
SKILL_DIR = ROOT / "skills" / "agent-plain-writing"
SKILL_FILE = SKILL_DIR / "SKILL.md"
TYPE_FILES = {
    "blog": "blog.md",
    "prose": "prose.md",
    "poetry": "poetry.md",
    "design": "detail-design.md",
    "guide": "user-guide.md",
}

sys.path.insert(0, str(Path(__file__).resolve().parent))
import score  # noqa: E402

# Editable command templates verified against `agy --help` and `claude --help`.
# Templates containing "{prompt}" receive the prompt as that argument;
# otherwise the prompt is passed on stdin.
TOOL_COMMANDS = {
    "antigravity": ["agy", "-p", "{prompt}"],
    "claude": ["claude", "-p"],
}
ALL_TOOLS = ("openai", "antigravity", "claude")
DEFAULT_OPENAI_URL = "https://api.openai.com/v1"


def load_dotenv(paths):
    """Load key=value pairs from .env files, letting later files override earlier ones."""
    for path in paths:
        if not path.is_file():
            continue
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[len("export "):].strip()
            if "=" not in line:
                continue
            key, val = line.split("=", 1)
            key = key.strip()
            val = val.strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in ('"', "'"):
                val = val[1:-1]
            if val:
                os.environ[key] = val


def resolve_openai_config():
    """Read OpenAI-compatible API settings from environment / .env."""
    load_dotenv([ROOT / ".env", Path(__file__).resolve().parent / ".env"])
    base_url = os.environ.get("OPENAI_API_URL", "").strip() or DEFAULT_OPENAI_URL
    endpoint = (
        base_url
        if base_url.rstrip("/").endswith("/chat/completions")
        else base_url.rstrip("/") + "/chat/completions"
    )
    return {
        "endpoint": endpoint,
        "api_key": os.environ.get("OPENAI_API_KEY", "").strip(),
        "model": os.environ.get("OPENAI_API_MODEL", "").strip(),
    }


def call_openai(prompt, cfg):
    """Call an OpenAI-compatible /chat/completions endpoint and return (text, err)."""
    payload = json.dumps({
        "model": cfg["model"],
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "agent-plain-writing-eval/1.0",
    }
    if cfg["api_key"]:
        headers["Authorization"] = f"Bearer {cfg['api_key']}"
    req = urllib.request.Request(cfg["endpoint"], data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return "", f"HTTP {e.code}: {body[:300]}"
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        return "", str(e)
    try:
        return data["choices"][0]["message"]["content"] or "", None
    except (KeyError, IndexError, TypeError):
        return "", f"Unexpected API response: {json.dumps(data)[:300]}"


def build_prompt(case_path, with_skill):
    """Build the prompt for one case, optionally prepending SKILL.md and its type/lang files."""
    case_text = case_path.read_text(encoding="utf-8")
    parts = [
        "Write the requested document using only the facts in the brief below.",
        "Do not invent numbers or details. Follow the requested language, type, and audience.",
    ]
    if with_skill:
        meta = score.parse_case_meta(case_text)
        lang = meta["lang"]
        doc_type = meta["type"]
        type_file = TYPE_FILES.get(doc_type, "blog.md")

        parts.append("\n## Skill instructions\n\n" + SKILL_FILE.read_text(encoding="utf-8"))

        extra_files = [
            ("Document type guide", SKILL_DIR / "doc-types" / type_file),
            ("Language limits", SKILL_DIR / "languages" / lang / "profile.json"),
            ("Language profile", SKILL_DIR / "languages" / lang / "profile.md"),
            ("Banned phrases guide", SKILL_DIR / "languages" / lang / "banned-guide.md"),
            ("Examples", SKILL_DIR / "languages" / lang / "examples" / type_file),
        ]
        for label, path in extra_files:
            if path.is_file():
                parts.append(f"\n## {label} ({path.relative_to(SKILL_DIR)})\n\n" + path.read_text(encoding="utf-8"))
    parts.append("\n## Case\n\n" + case_text)
    return "\n".join(parts)


def print_summary_table(rows):
    """Print a compact with/without comparison table."""
    print("\n| Case | Mode | Units | Avg Sent | Jargon | Violations | Warnings | Invented Nums |")
    print("|---|---|---|---|---|---|---|---|")
    for r in rows:
        inv = ", ".join(r["invented_numbers"]) if r["invented_numbers"] else "-"
        print(
            f"| {Path(r['case']).stem} | {r['mode']} | {r['total_units']} {r['unit']} | "
            f"{r['avg_sentence_length']} | {r['jargon_count']} | "
            f"{r['violation_count']} | {r['warning_count']} | {inv} |"
        )


def main():
    ap = argparse.ArgumentParser(description="Run agent-plain-writing evals")
    ap.add_argument("--tool", choices=ALL_TOOLS, default="openai",
                    help="AI backend to run (default: openai)")
    ap.add_argument("--type", dest="doc_type",
                    help="Run only cases matching this document type (e.g. blog, design)")
    ap.add_argument("--lang",
                    help="Run only cases matching this language (e.g. vi, en, ja)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print planned commands without calling any AI tool")
    args = ap.parse_args()

    cases = sorted(CASES_DIR.glob("*.md"))
    if args.doc_type or args.lang:
        filtered = []
        for case in cases:
            meta = score.parse_case_meta(case.read_text(encoding="utf-8"))
            if args.doc_type and meta["type"] != args.doc_type:
                continue
            if args.lang and meta["lang"] != args.lang:
                continue
            filtered.append(case)
        cases = filtered
    if not cases:
        print(f"No matching case files found in {CASES_DIR}", file=sys.stderr)
        return 2

    tool = args.tool
    openai_cfg = resolve_openai_config() if tool == "openai" else None
    cmd_template = TOOL_COMMANDS.get(tool)

    planned = []
    for case in cases:
        for mode in ("without_skill", "with_skill"):
            planned.append((case, mode))

    if tool == "openai":
        model_label = openai_cfg["model"] or "<missing OPENAI_API_MODEL>"
        key_status = f"set ({len(openai_cfg['api_key'])} chars)" if openai_cfg["api_key"] else "unset"
        print(f"Tool: openai ({openai_cfg['endpoint']}, model={model_label}, key={key_status})")
    else:
        print(f"Tool: {tool} ({' '.join(cmd_template)})")
    print(f"Cases ({len(cases)}): {', '.join(c.stem for c in cases)}")
    print(f"Total AI calls: {len(planned)} ({len(cases)} cases x 2)")

    if args.dry_run:
        print("\nDry run commands:")
        for case, mode in planned:
            if tool == "openai":
                display = f"POST {openai_cfg['endpoint']} (model={openai_cfg['model'] or '<unset>'})"
            elif "{prompt}" in cmd_template:
                display = " ".join("<prompt>" if a == "{prompt}" else a for a in cmd_template)
            else:
                display = f"{' '.join(cmd_template)} <prompt_on_stdin>"
            print(f"- [{mode}] {case.name}: {display}")
        return 0

    if tool == "openai":
        missing = []
        if not openai_cfg["model"]:
            missing.append("OPENAI_API_MODEL")
        if not openai_cfg["api_key"] and "api.openai.com" in openai_cfg["endpoint"]:
            missing.append("OPENAI_API_KEY")
        if missing:
            print(
                f"Missing required env vars in .env or environment: {', '.join(missing)}",
                file=sys.stderr,
            )
            return 2

    if not sys.stdin.isatty():
        print("Non-interactive session without --dry-run. Exiting without running.")
        return 0

    answer = input("Type 'yes' to run these AI calls (charges/quota may apply): ").strip()
    if answer != "yes":
        print("Cancelled. No AI calls were made.")
        return 0

    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = RUNS_DIR / ts
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for case, mode in planned:
        prompt = build_prompt(case, with_skill=(mode == "with_skill"))
        print(f"Running {case.stem} ({mode})...")
        out_file = out_dir / f"{case.stem}.{mode}.md"
        if tool == "openai":
            text, err = call_openai(prompt, openai_cfg)
            out_file.write_text(text, encoding="utf-8")
            if err:
                print(f"  OpenAI API error: {err}", file=sys.stderr)
        else:
            if "{prompt}" in cmd_template:
                run_cmd = [prompt if a == "{prompt}" else a for a in cmd_template]
                proc = subprocess.run(run_cmd, capture_output=True, text=True)
            else:
                proc = subprocess.run(cmd_template, input=prompt, capture_output=True, text=True)
            out_file.write_text(proc.stdout, encoding="utf-8")
            if proc.returncode != 0:
                print(f"  Tool exited {proc.returncode}: {proc.stderr.strip()}", file=sys.stderr)
        metrics = score.score_case(case, out_file)
        metrics["mode"] = mode
        rows.append(metrics)

    (out_dir / "results.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print_summary_table(rows)
    print(f"\nSaved outputs to {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
