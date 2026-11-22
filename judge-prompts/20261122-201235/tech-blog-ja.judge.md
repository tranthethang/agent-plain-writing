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
type: tech-blog
non_tech: false
---

# SIMULATED DATA

## Audience

Webサービスの運用を担当する開発者（実務経験2〜4年）。

## Brief

### Summary
バッチ処理のタイムアウトを30秒から120秒に延ばしたところ、別のジョブが詰まり、朝8時の集計が45分遅れました。原因は1回の処理で5万件をまとめて読み込んでいたことでした。最初はメモリ不足を疑い、サーバーのメモリを8GBから16GBに増やしましたが、遅延は変わりませんでした。ログを見ると、5万件を読む1回の処理に平均95秒かかり、同じ時間帯の請求ジョブがロック待ちになっていました。1000件ずつの分割処理に変えたところ、1回あたり4秒で終わるようになりました。

### Main points
1. タイムアウトを延ばすだけでは、詰まりの原因は消えない。
2. 1回あたりの処理件数を1000件に制限すると、メモリ使用量も安定する。
3. 失敗したチャンクだけを再実行できるようにすると、朝の復旧が5分で済む。

### Reader
バッチ処理やデータベースの基本を知っている開発者。

### Voice
です・ます調。同僚に実体験を話すような率直な語り口。失敗を隠さない。

### Sample paragraph
タイムアウトを30秒から120秒に延ばした日、問題は解決したと思っていました。翌朝の8時、監視画面が真っ赤になるまでは。

最初に疑ったのはメモリでした。8GBを16GBに増やしても、翌朝の集計はまた遅れました。

### Words to use or avoid
- 使う: `バッチ`, `タイムアウト`, `チャンク`.
- 避ける: `包括的`, `シームレス`, `と言えるでしょう`.

## Facts
- 元のタイムアウト: 30秒
- 変更後のタイムアウト: 120秒
- 集計の遅延: 45分（朝8時の集計）
- 元の1回あたり件数: 5万件
- 分割後の件数: 1000件
- 分割後の処理時間: 1回あたり4秒
- 復旧時間: 5分
- 最初に試した対策: メモリを8GBから16GBに増設（遅延は変わらず）
- 5万件の1回の処理時間: 平均95秒
- 待たされたジョブ: 同じ時間帯に動く請求ジョブ（ロック待ち、最長40分）
- 分割後のチャンク数: 50
- 分割後の全体の処理時間: 約3分20秒
- 以前の失敗時の再実行: 全件やり直しで約50分
- 修正にかかった期間: 2日


## Candidate output

# タイムアウトを延ばしても、請求ジョブは詰まりました

タイムアウトを30秒から120秒に延ばした日、問題は解決したと思っていました。翌朝8時の集計が45分遅れるまでは。

## 最初にメモリを疑った

まず、サーバーのメモリを8GBから16GBに増やしました。しかし、集計の遅れは変わりませんでした。タイムアウトを延ばしても、1回に処理する量はそのままです。時間の上限を変えるだけでは、詰まりの原因を取り除けませんでした。

## ログで分かったこと

ログを見ると、5万件を読む処理は1回あたり平均95秒かかっていました。同じ時間帯に動く請求ジョブは、ロック待ちになっていました。最長で40分待っていたため、集計だけでなく、別のジョブにも影響が出ていました。

## 1000件ずつ処理する

修正には2日かかりました。1回の処理件数を1000件に制限し、全体を50個のチャンクに分けました。1チャンクの処理は4秒で終わり、全体でも約3分20秒になりました。1回に読む量を抑えたことで、メモリ使用量も安定しました。

## 失敗した分だけ再実行する

以前は処理に失敗すると、全件をやり直す必要があり、約50分かかっていました。失敗したチャンクだけを再実行できるようにした結果、朝の復旧は5分で済みました。

次にバッチが遅れたら、タイムアウトだけでなく、1回に読む件数とログのロック待ちも確認します。
