CLAUDE.md という名前にすると、実際に読み込まれてしまうので、敢えてファイル名に `_template` をつけています。
以下はよく使う CLAUDE.md の一部です。 bun + option-t を使うプロジェクトで有効です。

## Basic Rules

- TypeScript の実行環境として Bun を使用する
- t-wada が推奨する TDD で開発する
- 各ステップの最後に lint, test, commit を行う
- 明示的なユーザーの承認なしに lint ルールを無効にしない
- コミットメッセージは Conventional Commit 形式に従い、日本語で書きます

## Coding Rules

- 関数型ドメインモデリングで設計する
  - **`class` は使わない。** `function` を使う
  - 代数的データ型を使う
- 例外を Throw しない
  - 失敗する可能性のある関数は `option-t` を使って `Result<T, E>` を返す
  - 外部ライブラリ等で throw される例外は `try catch` と `option-t` の `createErr` を使ってラップする
  - `isOk()`, `isErr()` を利用する。 `mapForResult()`, `andThenForResult()` をなるべく利用しない
- 早期リターンを使用して可読性を向上させる
- `Result<T, E>` 型のテストでは、エラーケースで `throw new Error("unreachable")` を使用する
- コメントとテストケースは日本語で書く

## Single Responsibility and API Minimization

- 責務ごとにファイルを分割し、各ファイルが単一の責務を持つようにする
- 公開 API は最小限に保ち、実装の詳細は隠蔽する
  - 最小限の関数や型のみ export する
- モジュールの境界と依存関係を最小限に抑える
