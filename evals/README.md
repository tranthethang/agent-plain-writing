# Evals

This directory holds simulated evaluation cases, a mechanical scorer, and an AI judge prompt for `agent-plain-writing`.

**Notice:** All cases under `cases/` use **SIMULATED DATA**. No real customer names, metrics, or proprietary briefs are included.

## Case structure

Each file in `cases/` (`<type>-<lang>.md`) has:

1. Frontmatter with `lang` (`vi`, `en`, `ja`), `type` (`tech-blog`, `essay`, `api-design`, `guide`, `common`), and `non_tech` (`true` or `false`). Optional `short_brief: true` marks a brief whose facts cannot fill the `length` range; `score.py` then checks length against `length_short` in `profile.json` and reports `short_brief` in its JSON.
2. `# SIMULATED DATA` header.
3. `## Audience` describing the target reader.
4. `## Brief`:
   - For `tech-blog` and `essay`: `### Summary`, `### Main points`, `### Reader`, `### Voice`, `### Sample paragraph`, `### Words to use or avoid`.
   - For `api-design`: `### Idea`, `### Business rules`, `### Glossary`. The template is part of the skill, so the brief has no `### Template`.
   - For `guide`: `### Feature`, `### Steps` (with exact button labels), `### Reader`, `### Common errors`.
   - For `common`: `### Summary`, `### Reader`, `### Words to use or avoid`.
5. `## Facts` listing every number and proper name present in the source brief.

## Adding a case from a real brief

1. Copy an existing case file with the matching type (`tech-blog-*.md`, `essay-*.md`, `api-design-*.md`, `guide-*.md` or `common-*.md`).
2. Remove or replace personal data and customer identifiers.
3. Set `lang`, `type`, and `non_tech` in the frontmatter.
4. Fill `## Audience`, `## Brief`, and `## Facts` with the exact numbers and names from your brief.
5. Update the header to reflect whether the data is real (anonymized) or simulated.

## Running the eval

> **Cost warning:** Running `run_eval.py` makes real AI calls twice per case (30 calls for all 15 cases) and uses API quota or credits. Always preview with `--dry-run` first.

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
   Filter by document type and/or language with `--type` (`tech-blog`, `essay`, `api-design`, `guide`, `common`) and `--lang` (`vi`, `en`, `ja`):
   ```bash
   python3 evals/run_eval.py --type tech-blog --lang vi --dry-run
   ```
3. Run interactively (type `yes` to confirm):
   ```bash
   python3 evals/run_eval.py
   python3 evals/run_eval.py --type tech-blog --lang vi
   ```
3. Outputs and `results.json` are saved under `evidence/<timestamp>/` (tracked by git). The `without_skill` baseline is neutral: its prompt does not carry the "do not invent" sentence, so only the `with_skill` prompt gets core rule 5 from `SKILL.md`. `run-meta.json` sits next to `results.json` and records `tool`, `model`, `commit` and `started_at`.
4. To score a single output or print an AI judge prompt:
   ```bash
   python3 evals/score.py evals/cases/tech-blog-en.md output.md
   python3 evals/score.py evals/cases/tech-blog-en.md output.md --judge-prompt
   ```
   To render the judge prompt for every `with_skill` output of a run, use `--judge-prompts`. With a run id it makes no AI call and writes `judge-prompts/<run>/<case>.judge.md`. With no value it does the same after a new run. `--type` and `--lang` still filter:
   ```bash
   python3 evals/run_eval.py --judge-prompts 20261122-181452
   python3 evals/run_eval.py --judge-prompts
   ```
5. `score.py` counts a number as sourced when it appears in the case or equals the item count of one list in the case. For `api-design` it also reports `tbd_ids`, `tbd_without_question` (ids with no `- TBD-n:` line), `tbd_in_code` (ids inside a fenced block), `tbd_duplicate_questions` (groups of ids that ask the same normalized question), and `tbd_without_inline` (ids that have an Open items question but appear in no section). The judge prompt adds semantic keys by type. For `api-design`: `invented_gaps`, `lost_rules`, `repeated_facts`, `misframed_tbd` and `template_violations`. For `tech-blog`: `narrator_shift`, `lost_causal_link` and `mismatched_comparison`. For `essay`: `explained_ending`, `flat_restatement` and `no_inner_voice`.
