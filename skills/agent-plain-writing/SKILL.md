---
name: agent-plain-writing
description: "Router for plain, short, concrete writing in Vietnamese (vi), English (en) and Japanese (ja). Use when the user asks to write, rewrite or shorten a text, or says text is wordy, vague or too technical, and the document type is not clear. It picks the document type and the language, then hands off to a sub-skill. Do not use for pure translation, fiction, poetry, marketing copy, UI strings or code comments. Viết, viết lại, rút gọn văn bản tiếng Việt, Anh, Nhật khi chưa rõ loại văn bản. 文章の作成・書き直し・簡潔化 (文書の種類が不明なとき)。"
---

# Plain writing router

This skill does one job: it picks the document type and the output language, then hands off. It holds no writing rules and writes no content.

## Steps

1. If `PLAIN-WRITING.md` exists in the project root, read `default_type` and `default_lang` from it. Use them when the request does not say otherwise.
2. Pick the output language: `vi`, `en` or `ja`. It is the language of the text to produce, not the language of the prompt. If it is unclear, ask one question.
3. Pick the sub-skill from the table below. If two rows fit, ask one question.
4. Load that sub-skill and follow it. Pass on the request, the language and the type.

## Routing table

| The request is | Sub-skill |
|---|---|
| A post that shares technical experience | `agent-plain-writing-tech-blog` |
| A personal, reflective essay | `agent-plain-writing-essay` |
| A spec for one API endpoint | `agent-plain-writing-api-design` |
| A step-by-step guide or manual for general users | `agent-plain-writing-user-guide` |
| A short notice, an announcement, or anything else | `agent-plain-writing-common` |

## Limits of this skill

- Do not write, rewrite or shorten text here.
- Do not apply a style rule here.
- Do not run the checker here. Each sub-skill has its own.
