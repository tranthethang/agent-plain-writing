# Evals

This directory holds simulated evaluation cases, a mechanical scorer, and an AI judge prompt for `agent-plain-writing`.

**Notice:** All cases under `cases/` use **SIMULATED DATA**. No real customer names, metrics, or proprietary briefs are included.

## Case structure

Each file in `cases/` (`<type>-<lang>.md`) has:

1. Frontmatter with `lang` (`vi`, `en`, `ja`), `type` (`blog`, `api-design`), and `non_tech` (`true` or `false`).
2. `# SIMULATED DATA` header.
3. `## Audience` describing the target reader.
4. `## Brief`:
   - For `blog`: `### Summary`, `### Main points`, `### Reader`, `### Voice`, `### Sample paragraph`, `### Words to use or avoid`.
   - For `api-design`: `### Idea`, `### Business rules`, `### Glossary`. The template is part of the skill, so the brief has no `### Template`.
5. `## Facts` listing every number and proper name present in the source brief.

## Adding a case from a real brief

1. Copy an existing case file with the matching type (`blog-*.md` or `api-design-*.md`).
2. Remove or replace personal data and customer identifiers.
3. Set `lang`, `type`, and `non_tech` in the frontmatter.
4. Fill `## Audience`, `## Brief`, and `## Facts` with the exact numbers and names from your brief.
5. Update the header to reflect whether the data is real (anonymized) or simulated.

## Running the eval

> **Cost warning:** Running `run_eval.py` makes real AI calls twice per case (12 calls for all 6 cases) and uses API quota or credits. Always preview with `--dry-run` first.

1. By default, `run_eval.py` uses an OpenAI-compatible `/chat/completions` API (`--tool openai`), reading `.env` (in `evals/.env` or repo root `.env`) or environment variables:
   ```env
   OPENAI_API_URL=https://api.openai.com/v1
   OPENAI_API_KEY=sk-...
   OPENAI_API_MODEL=gpt-4o-mini
   ```
   You can also pass `--tool claude` or `--tool antigravity` to use a local CLI instead.
2. Preview the planned calls without invoking an AI:
   ```bash
   python3 evals/run_eval.py --dry-run
   ```
   Filter by document type and/or language with `--type` (`blog`, `api-design`) and `--lang` (`vi`, `en`, `ja`):
   ```bash
   python3 evals/run_eval.py --type blog --lang vi --dry-run
   ```
3. Run interactively (type `yes` to confirm):
   ```bash
   python3 evals/run_eval.py
   python3 evals/run_eval.py --type blog --lang vi
   ```
3. Outputs and `results.json` are saved under `evals/runs/<timestamp>/` (ignored by git).
4. To score a single output or print an AI judge prompt:
   ```bash
   python3 evals/score.py evals/cases/blog-en.md output.md
   python3 evals/score.py evals/cases/blog-en.md output.md --judge-prompt
   ```
5. `score.py` counts a number as sourced when it appears in the case or equals the item count of one list in the case. For `api-design` it also reports `tbd_ids`, `tbd_without_question` (ids with no `- TBD-n:` line), `tbd_in_code` (ids inside a fenced block), and `tbd_duplicate_questions` (groups of ids that ask the same normalized question). The judge prompt adds `invented_gaps`, `lost_rules` and `repeated_facts` for the semantic checks.
