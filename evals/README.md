# Evals

This directory holds simulated evaluation cases, smoke prompts, a mechanical scorer, and an AI judge prompt for the `agent-plain-writing` skills.

**Notice:** All cases under `cases/` use **SIMULATED DATA**. No real customer names, metrics, or proprietary briefs are included.

## Case structure

Each file in `cases/` (`<type>-<lang>.md`) has:

1. Frontmatter with `lang` (`vi`, `en`, `ja`), `type` (`tech-blog`, `essay`, `api-design`, `user-guide`, `common`), and `non_tech` (`true` or `false`). Optional `short_brief: true` marks a brief whose facts cannot fill the `length` range; `score.py` then checks length against `length_short` in `profile.json` and reports `short_brief` in its JSON.
2. `# SIMULATED DATA` header.
3. `## Audience` describing the target reader.
4. `## Brief`:
   - For `tech-blog` and `essay`: `### Summary`, `### Main points`, `### Reader`, `### Voice`, `### Sample paragraph`, `### Words to use or avoid`.
   - For `api-design`: `### Idea`, `### Business rules`, `### Glossary`. The template is part of the skill, so the brief has no `### Template`.
   - For `user-guide`: `### Feature`, `### Steps` (with exact button labels), `### Reader`, `### Common errors`.
   - For `common`: `### Summary`, `### Reader`, `### Words to use or avoid`.
5. `## Facts` listing every number and proper name present in the source brief.

## Adding a case from a real brief

1. Copy an existing case file with the matching type (`tech-blog-*.md`, `essay-*.md`, `api-design-*.md`, `user-guide-*.md` or `common-*.md`).
2. Remove or replace personal data and customer identifiers.
3. Set `lang`, `type`, and `non_tech` in the frontmatter.
4. Fill `## Audience`, `## Brief`, and `## Facts` with the exact numbers and names from your brief.
5. Update the header to reflect whether the data is real (anonymized) or simulated.

## Running the eval

A real agent writes each output. No script calls an API.

1. Local gate. Both commands must exit `0`:
   ```bash
   python3 -m unittest discover -s tests
   python3 scripts/sync_shared.py --check
   ```
2. Install the skills. All six install together (the router and five sub-skills):
   ```bash
   npx skills add tranthethang/agent-plain-writing -g
   ```
3. Create `evidence/<run>/`, where `<run>` is a timestamp such as `20261124-101500`.
4. Run the prompts in your agent. Use a fresh session for each prompt.
   - Smoke set: the 5 prompts in `evals/smoke-prompts.md`. Run it after every change to a skill.
   - Full set: one prompt for every file in `cases/`. Use the form of a smoke prompt. Give the same output rule: write the document to `evidence/<run>/<case>.with_skill.md`, where `<case>` is the case file name without `.md`.
5. Score each output and save the list of results in `evidence/<run>/results.json`:
   ```bash
   python3 evals/score.py evals/cases/tech-blog-en.md evidence/<run>/tech-blog-en.with_skill.md
   ```
   To save all results in one file:
   ```bash
   python3 - <<'PY' > evidence/<run>/results.json
   import json, subprocess, sys
   from pathlib import Path
   run = Path("evidence/<run>")
   rows = []
   for out in sorted(run.glob("*.with_skill.md")):
       case = Path("evals/cases") / (out.name.replace(".with_skill.md", "") + ".md")
       r = subprocess.run([sys.executable, "evals/score.py", str(case), str(out)], capture_output=True, text=True, check=True)
       rows.append(json.loads(r.stdout))
   print(json.dumps(rows, ensure_ascii=False, indent=2))
   PY
   ```
6. `score.py` drops the report after the last `<!-- report -->` line outside code fences, so only the document is scored. A `---` line cuts nothing.
7. To print an AI judge prompt for one output:
   ```bash
   python3 evals/score.py evals/cases/tech-blog-en.md evidence/<run>/tech-blog-en.with_skill.md --judge-prompt
   ```
8. `score.py` counts a number as sourced when it appears in the case or equals the item count of one list in the case. For `api-design` it also reports `tbd_ids`, `tbd_without_question` (ids with no `- TBD-n:` line), `tbd_in_code` (ids inside a fenced block), `tbd_duplicate_questions` (groups of ids that ask the same normalized question), and `tbd_without_inline` (ids that have an Open items question but appear in no section). The judge prompt adds semantic keys by type. For `api-design`: `invented_gaps`, `lost_rules`, `repeated_facts`, `misframed_tbd` and `template_violations`. For `tech-blog`: `narrator_shift`, `lost_causal_link` and `mismatched_comparison`. For `essay`: `explained_ending`, `flat_restatement` and `no_inner_voice`.
