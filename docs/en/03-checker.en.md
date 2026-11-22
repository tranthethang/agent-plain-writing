# Checker script

```bash
python3 skills/agent-plain-writing/scripts/check_style.py draft.md --lang en --type tech-blog
python3 skills/agent-plain-writing/scripts/check_style.py spec.md  --lang ja --type api-design
python3 skills/agent-plain-writing/scripts/check_style.py guide.md --lang vi --type guide
python3 skills/agent-plain-writing/scripts/check_style.py post.md  --lang en --type tech-blog --non-tech
```

| Option | Values |
|---|---|
| `--lang` | `vi`, `en`, `ja`. Optional if `default_lang` is set in `PLAIN-WRITING.md` |
| `--type` | `tech-blog`, `essay`, `api-design`, `guide`, `common` (`user-guide` also works). Default: `default_type` or `common` |
| `--non-tech` | Limit jargon to 3 terms. The `guide` type always applies a jargon limit |
| `--config` | Path to a `PLAIN-WRITING.md` file. Default: `./PLAIN-WRITING.md` if present |
| `--short-brief` | Use `length_short` for a type that has it (for example `tech-blog`) |

Exit codes: `0` clean, `1` violations, `2` usage error. `--type blog` was removed and exits `2`; use `--type tech-blog` instead.

## What it checks

- Sentence length, paragraph length, banned phrases, jargon count, text length. A text longer than the upper length limit prints a warning and does not change the exit code. A shorter text is fine; never pad.
- Report labels (such as `Result:`) at the start of any line outside code blocks.
- Line breaks made with trailing spaces.

It skips code blocks, tables and headings. For `api-design`, it checks each table cell for sentence length. It checks list items for sentence length, but not for paragraph length.

## What it does not check

Voice, facts, and whether a sentence is natural. It is mechanical. A clean result means the counts pass, not that the text is good.

## Units

| Language | Unit | `tech-blog` sentence limit |
|---|---|---|
| `vi` | syllables (*tiếng*) | 28 (about 20 words) |
| `en` | words | 20 |
| `ja` | characters (字), punctuation and spaces excluded | 60 |

Limits for every type are only in each language's `profile.json`. The table above mirrors the `tech-blog` row.

Next: [04-customize](04-customize.en.md).
