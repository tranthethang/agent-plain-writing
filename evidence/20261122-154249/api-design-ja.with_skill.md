## 識別情報

- メソッドとパス: `POST /wp/v2/posts`
- 目的: 投稿を1件作成する。
- 認可: ロール `editor` と `author` のみが投稿を作成できる。`status` に `publish` を指定できるのは `editor` のみ。

## DTOとフィールド対応

| 項目 | 方向 | 型 | 必須 | 制約 |
|---|---|---|---|---|
| `title` | リクエスト | string | 任意 | 最大長は TBD-1 |
| `content` | リクエスト | string | 任意 | — |
| `status` | リクエスト | enum | 任意 | `publish`、`future`、`draft`、`pending`、`private` |
| `slug` | リクエスト | string | 任意 | — |
| `date` | リクエスト | TBD-3 | 条件付き（`status` が `future` の場合） | `status` が `future` の場合、現在時刻より後であること |
| `categories` | リクエスト | integerの配列 | TBD-4 | 各IDが存在すること |
| 保存した投稿 | レスポンス | TBD-5 | — | — |

## エンドポイント

成功ステータス: 201

リクエスト:

    {"title": "投稿タイトル", "status": "draft"}

## 処理

システムは、`status` がない場合に `draft` を既定値にする。  
システムは、`slug` がない場合に `title` から作る。`title` がない場合の動作は TBD-6。  
同じスラッグがすでにある場合、システムは数字の接尾辞を付ける。

処理順: TBD-7  
エラー優先順: TBD-8

## エラー

| 条件 | HTTP | コード |
|---|---:|---|
| 呼び出し元のロールが `editor` または `author` ではない | 403 | `rest_cannot_create` |
| ロール `author` が `status` に `publish` を指定した | 403 | `rest_cannot_publish` |
| `title` と `content` の両方がない | 400 | `rest_empty_post` |
| `status` が `future` で、`date` がない、または現在時刻より後でない | 400 | `rest_invalid_date` |
| `categories` に存在しないIDがある | 400 | `rest_invalid_term` |
| `title` が TBD-1 の最大長を超える | TBD-2 | TBD-2 |

## 副作用

なし

## 未決事項

- TBD-1: `title` の最大長と、その単位は何か。
- TBD-2: `title` が最大長を超えた場合のHTTPステータスとエラーコードは何か。
- TBD-3: `date` の型と形式は何か。
- TBD-4: `categories` は必須か。
- TBD-5: 成功レスポンスに含めるフィールドは何か。
- TBD-6: `slug` と `title` の両方がない場合、システムはどう動作するか。
- TBD-7: 処理の実行順は何か。
- TBD-8: 複数のエラー条件を満たす場合、どのエラーを優先するか。