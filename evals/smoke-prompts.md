# Smoke prompts

Five prompts for a real agent. Run them after you install the skills (see `README.md`). Each prompt uses a case in `evals/cases/` and **SIMULATED DATA**.

Replace `<run>` with a run folder name such as `20261124-101500`. Create `evidence/<run>/` first.

Each prompt ends with the same output rule: write only the document to the named file. Put any report after a line `<!-- report -->`, as the skill says.

## S1. Router, unclear type (`vi`)

- Output: `evidence/<run>/common-vi.with_skill.md`
- Pass: the agent loads `agent-plain-writing` first, then `agent-plain-writing-common`. `python3 evals/score.py evals/cases/common-vi.md evidence/<run>/common-vi.with_skill.md` shows `violation_count` of `0`.

```text
Đọc evals/cases/common-vi.md. Viết văn bản ngắn, rõ ràng từ bản tóm tắt trong mục Brief, chỉ dùng các dữ kiện trong brief. Ghi văn bản vào evidence/<run>/common-vi.with_skill.md.
```

## S2. API design (`en`)

- Output: `evidence/<run>/api-design-en.with_skill.md`
- Pass: the agent loads `agent-plain-writing-api-design` with no router step. The score shows `violation_count` of `0` and no `tbd_without_question`.

```text
Read evals/cases/api-design-en.md. Write the API design spec for the idea in the Brief, using only the facts in the brief. Write the spec to evidence/<run>/api-design-en.with_skill.md.
```

## S3. Tech blog (`ja`)

- Output: `evidence/<run>/tech-blog-ja.with_skill.md`
- Pass: the agent loads `agent-plain-writing-tech-blog`. The score shows `violation_count` of `0` and an empty `invented_numbers`.

```text
evals/cases/tech-blog-ja.md を読んでください。Brief の内容だけを使い、技術ブログ記事を書いてください。記事は evidence/<run>/tech-blog-ja.with_skill.md に書き込んでください。
```

## S4. Essay (`vi`)

- Output: `evidence/<run>/essay-vi.with_skill.md`
- Pass: the agent loads `agent-plain-writing-essay`. The score shows `violation_count` of `0` and an empty `invented_numbers`.

```text
Đọc evals/cases/essay-vi.md. Viết một tản văn từ phần Brief, chỉ dùng các dữ kiện trong brief. Ghi bài vào evidence/<run>/essay-vi.with_skill.md.
```

## S5. User guide (`ja`)

- Output: `evidence/<run>/user-guide-ja.with_skill.md`
- Pass: the agent loads `agent-plain-writing-user-guide`. The score shows `violation_count` of `0` and an empty `invented_numbers`.

```text
evals/cases/user-guide-ja.md を読んでください。Brief の内容だけを使い、一般ユーザー向けの手順書を書いてください。手順書は evidence/<run>/user-guide-ja.with_skill.md に書き込んでください。
```
