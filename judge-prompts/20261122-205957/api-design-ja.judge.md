# AI Judge Prompt

You are an impartial writing evaluator. Score the candidate output against the source brief and facts.

## Scoring criteria (1 to 5)

- **clarity** (1 to 5):
  - 5: Short, concrete sentences; understood on first read; active voice; no filler or empty openings/closings.
  - 3: Mostly clear, with some wordy sentences, vague adjectives, or unnecessary detail.
  - 1: Hard to follow, wordy, or heavy with unexplained jargon.
- **coverage** (1 to 5):
  - Open coverage rule: For template documents, every template section must be present, and every source fact must appear in the output.
  - For non-template documents (such as tech-blog posts), every main point and source fact from the brief must appear, with no invented numbers or claims.
  - 5: All required sections/points and all source facts are present; a missing source detail is left out, or marked `TBD-n` only when the brief names it or the endpoint cannot be implemented without it.
  - 3: Most points and facts appear, but 1–2 facts or a section are missing.
  - 1: Major points or multiple facts are missing, or facts are invented.

## Semantic checks (api-design)

For an `api-design` output, list each hit in the matching key. Leave the list empty when there is none.

- **invented_gaps**: a `TBD-n` question about a case that no brief rule touches and that does not block implementation. A `TBD-n` for two conflicting rules, or for a rule that lacks its input, is not an invented gap.
- **lost_rules**: a business rule from the brief that appears nowhere outside the Errors table.
- **repeated_facts**: the same fact written in two sections.
- **misframed_tbd**: a `TBD-n` that asks a question a stated rule already implies, or that misses the real decision.
- **template_violations**: a section out of order, a DTO table without the columns Field, Direction, Type, Required, Constraint, a Processing step that restates a check, or Side effects text other than the `None` label when the brief states no side effect.

## Semantic checks (tech-blog)

For a `tech-blog` output, list each hit in the matching key. Leave the list empty when there is none.

- **narrator_shift**: the narrator changes person (for example, first to third) partway through.
- **lost_causal_link**: a claim that lost the sentence explaining cause, change and result.
- **mismatched_comparison**: two numbers with different units or time periods placed next to each other as a comparison.

## Semantic checks (essay)

For an `essay` output, list each hit in the matching key. Leave the list empty when there is none.

- **explained_ending**: a closing sentence that names the feeling after the action already showed it.
- **flat_restatement**: a main point retold as one summary sentence instead of a scene with an action and a sensory detail, or a paragraph with no sensory detail.
- **no_inner_voice**: a text with objects and actions but no thought, memory or doubt from the narrator, or an added thought that states a lesson or a conclusion.

## Semantic checks (guide)

For a `guide` output, list each hit in the matching key. Leave the list empty when there is none.

- **invented_steps**: a step, screen, or button label that does not appear in the brief.
- **internal_mechanism**: an explanation of how the backend or software works internally instead of what the user sees or clicks.
- **missing_error_table**: common errors from the brief are omitted or not presented in a quick-lookup table or list.

## Semantic checks (common)

For a `common` output, list each hit in the matching key. Leave the list empty when there is none.

- **first_person**: first-person pronouns ("I", "we", "tôi", "chúng tôi", "私") used in the text.
- **opening_recap**: an introductory sentence that announces or recaps the topic instead of starting straight with the content.
- **closing_summary**: a concluding summary or thanks at the end instead of stopping when the content ends.

## Output format

Return JSON only. Do not include markdown fences or extra text.

```json
{
  "clarity": 1,
  "coverage": 1,
  "missing_facts": [],
  "invented_gaps": [],
  "lost_rules": [],
  "repeated_facts": [],
  "misframed_tbd": [],
  "template_violations": [],
  "narrator_shift": [],
  "lost_causal_link": [],
  "mismatched_comparison": [],
  "explained_ending": [],
  "flat_restatement": [],
  "no_inner_voice": [],
  "invented_steps": [],
  "internal_mechanism": [],
  "missing_error_table": [],
  "first_person": [],
  "opening_recap": [],
  "closing_summary": [],
  "notes": "one-sentence reason"
}
```

## Source case

---
lang: ja
type: api-design
non_tech: false
---

# SIMULATED DATA

エンドポイントと項目名は、公開されているWordPress REST APIの投稿リファレンス(「Create a Post」)による。業務規則とエラーコードは、この評価のために作った。

## Audience

ブログAPIを実装・テストするバックエンド開発者とQA担当者。

## Brief

### Idea
1件の投稿を作成する `POST /wp/v2/posts` を設計する。情報源: WordPress REST APIの投稿リファレンス、エンドポイント「Create a Post」。項目名と許可される値を除き、以下の規則は模擬である。

### Business rules
- ロール `editor` と `author` のみが投稿を作成できる。それ以外のロールには HTTP 403 (`rest_cannot_create`) を返す。
- `title` か `content` のどちらかが必要である。両方ない場合は HTTP 400 (`rest_empty_post`) を返す。
- `status` は `publish`、`future`、`draft`、`pending`、`private` のいずれかとする。既定値は `draft` である。
- `status` を `publish` にできるのは `editor` のみである。`author` が `publish` を送ると HTTP 403 (`rest_cannot_publish`) を返す。
- `status` が `future` のとき、`date` は現在時刻より後でなければならない。そうでない場合は HTTP 400 (`rest_invalid_date`) を返す。
- `slug` がない場合、システムは `title` から作る。同じスラッグがすでにある場合は、数字の接尾辞を付ける。
- `categories` の各IDは存在しなければならない。存在しないIDには HTTP 400 (`rest_invalid_term`) を返す。
- 成功した場合は HTTP 201 と保存した投稿を返す。
- `title` の最大長は情報源にない。`TBD` とする。

### Glossary
- `title`: 投稿のタイトル。
- `content`: 投稿の本文。
- `status`: 投稿の公開状態。
- `slug`: 投稿に固有のURLの部分。
- `categories`: カテゴリIDの一覧(整数)。

## Facts
- エンドポイント: `POST /wp/v2/posts`
- 許可するロール: `editor`、`author`(それ以外は HTTP 403 `rest_cannot_create`)
- statusの値: `publish`、`future`、`draft`、`pending`、`private`。既定値は `draft`
- 公開できるのは `editor` のみ(違反は HTTP 403 `rest_cannot_publish`)
- `title` と `content` の両方がない: HTTP 400 `rest_empty_post`
- `future` は未来の `date` が必要(違反は HTTP 400 `rest_invalid_date`)
- 存在しないカテゴリID: HTTP 400 `rest_invalid_term`
- 成功時のステータス: HTTP 201


## Candidate output

## 識別情報

- メソッドとパス: `POST /wp/v2/posts`
- 目的: 投稿を1件作成する。
- 認可: ロール `editor` と `author` のみが投稿を作成できる。`status` を `publish` にできるのは `editor` のみである。

## DTOとフィールド対応

| 項目 | 方向 | 型 | 必須 | 制約 |
|---|---|---|---|---|
| `title` | リクエスト | string | 条件付き（`content` がない場合は必須） | 最大長: `TBD-1` |
| `content` | リクエスト | string | 条件付き（`title` がない場合は必須） | — |
| `status` | リクエスト | enum | 任意 | `publish`、`future`、`draft`、`pending`、`private` |
| `date` | リクエスト | datetime | 任意 | — |
| `slug` | リクエスト | string | 任意 | — |
| `categories` | リクエスト | integerの配列 | 任意 | — |
| 投稿 | レスポンス | `TBD-2` | — | — |

## エンドポイント

リクエスト:

```json
{"title": "投稿タイトル", "status": "draft"}
```

成功時のHTTPステータス: `201`

## 処理

`status` がない場合、システムは `draft` を設定する。

`slug` がない場合、システムは `title` から `slug` を作成する。作成する `title` がない場合の動作は `TBD-3`。同じ `slug` がすでにある場合、システムは数字の接尾辞を付ける。

処理順: `TBD-4`

複数のエラー条件に該当する場合の優先順: `TBD-5`

## エラー

| 条件 | HTTPステータス | コード |
|---|---:|---|
| 呼び出し元のロールが `editor` または `author` ではない | 403 | `rest_cannot_create` |
| 呼び出し元が `author` で、`status` が `publish` である | 403 | `rest_cannot_publish` |
| `title` と `content` が両方ない | 400 | `rest_empty_post` |
| `status` が許可された値ではない | `TBD-6` | `TBD-6` |
| `status` が `future` で、`date` が現在時刻より後ではない | 400 | `rest_invalid_date` |
| `categories` に存在しないIDが含まれる | 400 | `rest_invalid_term` |

## 副作用

なし

## 未決事項

- `TBD-1`: `title` の最大長はいくつか。
- `TBD-2`: 成功レスポンスに含めるフィールドと各フィールドの型は何か。
- `TBD-3`: `title` がない場合、システムは `slug` をどう作成するか。
- `TBD-4`: 処理の実行順は何か。
- `TBD-5`: 複数のエラー条件に該当する場合、どのエラーを優先するか。
- `TBD-6`: 許可されていない `status` の値に対するHTTPステータスとエラーコードは何か。

<!-- report -->

固定テンプレートに沿って作成しました。業務ルールについて追加の推測はしていません。
