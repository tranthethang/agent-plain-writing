# Project Plain-Writing Guide

Copy this file to `PLAIN-WRITING.md` in your project root and edit it.
The AI reads the Markdown sections for voice and terms. `check_style.py` reads the `plain-writing` JSON block below.

## Voice

- Write in active voice, addressed to "you".
- Keep product and API names exact as listed below.

## Terms

- Use `workspace` instead of `project folder`.
- Avoid internal code names in user-facing text.

## Checker settings

```plain-writing
{
  "default_lang": "en",
  "default_type": "api-design",
  "terms": [
    "rate limit",
    "idempotency key"
  ],
  "banned": [
    "synergy",
    "best-in-class"
  ],
  "limits": {
    "api-design": {
      "sentence": 22,
      "paragraph": 3,
      "terms": 5
    }
  }
}
```
