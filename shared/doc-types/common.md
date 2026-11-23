---
name: agent-plain-writing-common
description: "Write, rewrite or shorten a short notice, announcement or other plain text that fits no other type, in plain concrete language with countable limits, in Vietnamese (vi), English (en) or Japanese (ja). Use for a notice, an announcement, a short message, a short internal note, or to deslopify or rewrite an agent reply, or when such text is wordy or vague. Do not use for pure translation, fiction, poetry, marketing copy, UI strings or code comments. Viết, viết lại, rút gọn thông báo ngắn hoặc viết lại câu trả lời tiếng Việt, Anh, Nhật. 短いお知らせの作成・書き直し・簡潔化・回答を書き直して。"
---

# Common

Use for any text that no other type fits: a short technical notice, an announcement, a release note, an internal message. This type is the fallback.

## Reader and length

- Reader: whoever the brief names. When the brief names none, write for a reader who knows the subject but not the details.
- Length: no range. Write what the source holds. Do not pad, repeat a fact, or add a motive that the brief does not give.

## Overrides to the core rules

- Follow the person the brief asks for. When the brief names none, write about the subject, not about yourself.
- Stay in one person from the first line to the last.

## Voice

- Start with the content. The opening is at most 2 sentences and holds the main fact. No recap, no greeting, no empty thanks.
- End when the content ends. No closing summary, no restatement of the opening.
- Short, concrete sentences within the `sentence` limit in `profile.json`. One idea per sentence.
- Concrete verbs, active voice, one name for one concept.
- Add no fact, number, reaction or inner thought that the brief lacks.

## Structure

1. **Opening** (at most 2 sentences): the main fact.
2. **Content**: paragraphs within the `paragraph` limit in `profile.json`. Use a list when the items are parallel, and a table when they have the same fields.
3. **End**: stop when the content ends. Add a closing line only when the reader has one action to take.

No fixed headings. Add a heading only when the text is long enough that a reader needs to find a part.

## Reply rewrite mode

Use this mode when the user asks to deslopify or rewrite an agent reply (or the text pasted after the request).

- Target reader: a sharp reader who has no project context.
- Order: state the main conclusion first, then the background, then how it works.
- Keep known technical terms. Define an unfamiliar term once in plain words.
- Return only the rewrite, with no preamble or commentary.

## Brief the AI needs

1. What the text is for, in 1 or 2 lines.
2. The facts it must hold, with exact numbers and names.
3. The reader and what they do after reading.
4. The person to write in (first, second or third), if it matters.
5. Words to use and words to avoid.

## Checklist

- [ ] The opening holds the main fact and takes at most 2 sentences.
- [ ] No recap and no closing summary.
- [ ] The text follows the person the brief asks for, or is about the subject when the brief names none.
- [ ] Every number, name and event is in the source.
- [ ] `python3 <skill-dir>/scripts/check_style.py text.md --lang <lang> --type common`
