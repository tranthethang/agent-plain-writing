# Customize

- **Project config.** Copy `skills/agent-plain-writing/templates/PLAIN-WRITING.example.md` to `PLAIN-WRITING.md` in your project root. Set `default_lang`, `default_type`, voice, extra terms, extra banned phrases and limits. The checker reads the JSON block. The AI reads the Markdown sections.
- **Your own samples.** Each `examples/*.md` file ends with a "Your own samples" section. Paste a sentence the AI wrote badly and your rewrite. Your samples matter more than AI samples.
- **Banned phrases.** Add the phrase to `banned.txt` and to `banned-guide.md` in the same language folder. A header such as `[tech-blog,essay]` shares one phrase list between types.
- **Limits.** Edit `profile.json`. If the `tech-blog` sentence limit changes, update the Units table in `README.md` and [03-checker](03-checker.en.md).
- **A new language.** Create `languages/<code>/` with `profile.json`, `profile.md`, `banned.txt`, `banned-guide.md`, `terms.txt` and `examples/`. The script supports three units: `syllable`, `word`, `char`. Also update `SKILL.md`, `README.md` and these docs. See `AGENTS.md`.

Next: [05-evals](05-evals.en.md).
