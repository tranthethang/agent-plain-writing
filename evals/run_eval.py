#!/usr/bin/env python3
"""Run agent-plain-writing evals with and without the skill, then score outputs.

Usage:
    python3 evals/run_eval.py --dry-run
    python3 evals/run_eval.py --tool claude --dry-run
    python3 evals/run_eval.py
"""
import argparse
import datetime
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES_DIR = Path(__file__).resolve().parent / "cases"
RUNS_DIR = Path(__file__).resolve().parent / "runs"
SKILL_FILE = ROOT / "skills" / "agent-plain-writing" / "SKILL.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import score  # noqa: E402

# Editable command templates verified against `agy --help` and `claude --help`.
# Each command receives the prompt on stdin and prints the response on stdout.
TOOL_COMMANDS = {
    "antigravity": ["agy", "-p"],
    "claude": ["claude", "-p"],
}


def build_prompt(case_path, with_skill):
    """Build the prompt for one case, optionally prepending SKILL.md."""
    case_text = case_path.read_text(encoding="utf-8")
    parts = [
        "Write the requested document using only the facts in the brief below.",
        "Do not invent numbers or details. Follow the requested language, type, and audience.",
    ]
    if with_skill:
        skill_text = SKILL_FILE.read_text(encoding="utf-8")
        parts.append("\n## Skill instructions\n\n" + skill_text)
    parts.append("\n## Case\n\n" + case_text)
    return "\n".join(parts)


def choose_tool(arg_tool):
    """Return the selected tool name, asking interactively if omitted."""
    if arg_tool:
        return arg_tool
    if not sys.stdin.isatty():
        return None
    choice = input(f"Pick a tool ({'/'.join(TOOL_COMMANDS)}): ").strip().lower()
    if choice not in TOOL_COMMANDS:
        print(f"Unknown tool '{choice}'.", file=sys.stderr)
        return None
    return choice


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
    ap.add_argument("--tool", choices=sorted(TOOL_COMMANDS), default=None,
                    help="AI CLI tool to run (antigravity or claude)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print planned commands without calling any AI tool")
    args = ap.parse_args()

    cases = sorted(CASES_DIR.glob("*.md"))
    if not cases:
        print(f"No case files found in {CASES_DIR}", file=sys.stderr)
        return 2

    tool = args.tool or ("antigravity" if args.dry_run else choose_tool(args.tool))
    if not tool:
        print("No tool selected. Exiting without running.", file=sys.stderr)
        return 0

    cmd_template = TOOL_COMMANDS[tool]
    planned = []
    for case in cases:
        for mode in ("without_skill", "with_skill"):
            planned.append((case, mode, cmd_template))

    print(f"Tool: {tool} ({' '.join(cmd_template)})")
    print(f"Cases ({len(cases)}): {', '.join(c.stem for c in cases)}")
    print(f"Total AI calls: {len(planned)} ({len(cases)} cases x 2)")

    if args.dry_run:
        print("\nDry run commands:")
        for case, mode, cmd in planned:
            print(f"- [{mode}] {case.name}: {' '.join(cmd)} <prompt_on_stdin>")
        return 0

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
    for case, mode, cmd in planned:
        prompt = build_prompt(case, with_skill=(mode == "with_skill"))
        print(f"Running {case.stem} ({mode})...")
        proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True)
        out_file = out_dir / f"{case.stem}.{mode}.md"
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
