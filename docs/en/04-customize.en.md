# Customize

- **Project config.** Copy `shared/templates/PLAIN-WRITING.example.md` to `PLAIN-WRITING.md` in your project root. The checker looks for it in the current folder, then in each parent folder, and stops at the first folder that holds `.git`. Set `default_lang`, `default_type`, voice, extra terms, extra banned phrases and limits. The checker reads the JSON block. The AI reads the Markdown sections.
- **Edit `shared/` only.** After an edit, run `python3 scripts/sync_shared.py` to rebuild the sub-skills. Never edit a generated `SKILL.md` or a copy in `skills/`. Run `git config core.hooksPath .githooks` once, so the `pre-commit` hook stops a commit that leaves them out of date.
- **Your own samples.** Each `examples/*.md` file ends with a "Your own samples" section. Paste a sentence the AI wrote badly and your rewrite. Your samples matter more than AI samples.
- **Banned phrases.** Add the phrase to `banned.txt` and to `banned-guide.md` in the same language folder. A header such as `[tech-blog,essay]` shares one phrase list between types.
- **Limits.** Edit `profile.json`. If the `tech-blog` sentence limit changes, update the Units table in `README.md` and [03-checker](03-checker.en.md).
- **A new language.** Create `languages/<code>/` with `profile.json`, `profile.md`, `banned.txt`, `banned-guide.md`, `terms.txt` and `examples/`. The script supports three units: `syllable`, `word`, `char`. Also update `shared/skill-core.md`, `README.md` and these docs. See `AGENTS.md`.

Next: [05-evals](05-evals.en.md).
