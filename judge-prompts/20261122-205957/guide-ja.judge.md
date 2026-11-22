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
type: guide
non_tech: true
---

# SIMULATED DATA

## Audience

タブレットの KoraPOS アプリを使って、日次の売上レポートを出力する店舗スタッフ。

## Brief

### Feature
iPad または Android タブレットの KoraPOS から、日次売上サマリーを CSV ファイルとして出力する。

### Steps
1. **KoraPOS** を開き、下部バーの **レポート** をタップします。
2. **日次売上** を選び、カレンダーから日付を 1 つ指定します（過去 90 日まで）。
3. **CSV出力** をタップし、**ファイルに保存** または **メール送信** を選びます。
4. `sales-YYYY-MM-DD.csv` が作成されるまで最大 15 秒待ちます。

### Reader
IT に詳しくない店舗スタッフ。正確なボタン名と、失敗したときの簡単な対処法だけを知りたい。

### Common errors
- **CSV出力を押しても反応しない**: オフライン状態です。Wi-Fi に接続してからもう一度 **CSV出力** をタップします。
- **ファイルが空（0 バイト）**: 指定した日に支払い済みの注文がありません。別の日を選びます。
- **メール送信が失敗する**: 店舗メールが未設定です。店長に **設定** > **店舗プロフィール** での登録を依頼します。

## Facts
- アプリ名: KoraPOS
- 対応端末: iPad、Android タブレット
- ボタン名: レポート、日次売上、CSV出力、ファイルに保存、メール送信、設定、店舗プロフィール
- 日付範囲の上限: 過去 90 日まで
- 出力の待ち時間: 最大 15 秒
- 出力ファイル名: `sales-YYYY-MM-DD.csv`
- 空ファイルのサイズ: 0 バイト


## Candidate output

# 日次売上を出力する

iPadまたはAndroidタブレットのKoraPOSから、日次売上をCSVで出力します。

## 手順
1. **KoraPOS**を開き、下部バーの**レポート**をタップします。
2. **日次売上**を選び、カレンダーで日付を1つ指定します。過去90日までの日付を選べます。
3. **CSV出力**をタップし、**ファイルに保存**または**メール送信**を選びます。
4. ファイルが作成されるまで、最大15秒待ちます。ファイル名は `sales-YYYY-MM-DD.csv` です。

## うまくいかないとき

| 状況 | 対処 |
|---|---|
| **CSV出力**をタップしても反応しない | Wi-Fiに接続してから、もう一度**CSV出力**をタップします。 |
| ファイルが空（0バイト） | 指定した日に支払い済みの注文がありません。別の日を選びます。 |
| メール送信に失敗する | 店舗メールが未設定です。店長に**設定** > **店舗プロフィール**での登録を依頼します。 |

スクリプトは実行していません。記載内容に推測は加えていません。
