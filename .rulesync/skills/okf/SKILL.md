---
name: okf
description: Create, update, refactor, or validate Markdown knowledge documents conforming to Open Knowledge Format (OKF) v0.2, including Concept files, Attested Computations, index.md, and log.md. Use whenever authoring or modifying knowledge corpus files.
---

# OKF v0.2 Authoring & Maintenance Guide

あなたは **Open Knowledge Format (OKF) v0.2** の仕様に厳密に準拠したナレッジバンドルを作成・保守する。

## 1. ファイル種別の判定

作業対象が以下のどれに該当するかを最初に決める。

| 種別 | ファイル名 | YAML Frontmatter | 役割 |
|---|---|---|---|
| **Concept** | `<concept>.md` | **必須**（`type` 必須） | 個別の知識単位（テーブル、API、設計判断、Playbook、指標など） |
| **Attested Computation** | `<name>.md` | **必須**（`type: Attested Computation`） | 検証可能な実行手順・クエリ定義（§10） |
| **Directory Index** | `index.md` | **原則禁止**（※バンドルルート直下のみ `okf_version: "0.2"` 可） | 段階的開示（Progressive Disclosure）用の目次（§8） |
| **Update Log** | `log.md` | **禁止** | 時系列の変更履歴（§9） |

---

## 2. Concept ドキュメント作成ルール

### 2.1 Frontmatter 仕様
- **必須キー**: `type`（例: `Architecture`, `API Endpoint`, `Decision`, `Playbook`, `Reference`, `Metric`, `Table`）
- **推奨キー**:
  - `title`: 人間が読みやすいタイトル
  - `description`: **1文の要約**（`index.md` の一覧生成にそのまま使われるため簡潔に書く）
  - `resource`: 実体アセット（URL、テーブル、リポジトリ等）を指す URI。抽象概念の場合は省略する
  - `tags`: 横断分類用の文字列配列（例: `[auth, oauth, security]`）
- **Lifecycle / Trust / Provenance**:
  - `status`: `draft` | `stable` | `deprecated`（新規生成直後で人間未確認なら `draft`）
  - `generated`: `{ by: <agent-name>/<model-or-version>, at: <YYYY-MM-DDTHH:MM:SSZ> }`
  - `verified`: **エージェントは `human:<id>` を絶対に記載しない**。自動テスト・リンター通過時のみ `process:<id>` または `<agent>/<version>` を記載する
  - `stale_after`: 陳腐化期限がある場合のみ ISO 8601 UTC 日時で指定
  - `sources`: 情報源のリスト。本文で引用する場合は必ず安定した `id`（連番ではなくスラッグ）を付与する

### 2.2 タイムスタンプと Actor 表記（厳守）
- **日時**: すべて明示的な UTC オフセット付きの ISO 8601 形式（`YYYY-MM-DDTHH:MM:SSZ`）にする。日付のみやタイムゾーン無しは禁止。
- **Actor**:
  - エージェント: `<producer>/<version>`（例: `opencode/claude-sonnet-4`, `gemini-cli/gemini-2.5-pro`）
  - 人間: `human:<id>`
  - 自動処理: `process:<id>`

### 2.3 本文・リンク・出典の書き方
- **構造化**: 散文よりも見出し、箇条書き、Markdown テーブル、コードブロックを優先する。
- **標準見出し**: スキーマ定義には `# Schema`、使用例には `# Examples` を使う。
- **内部リンク**: ディレクトリ移動に耐えるため、**バンドルルートからの絶対パス形式**（先頭 `/`）を推奨する。
  - 良い例: `[認証設計](/architecture/auth.md)`
- **出典の帰属（Per-claim attribution）**:
  - `sources[].id` と一致するキー付き脚注を使う。項目並べ替えでズレるため `[^1]` のような連番脚注は使わない。
  - 例: `トークンの有効期限は15分である。[^auth-spec]` ＋ 末尾に `[^auth-spec]: OAuth 2.1 Security Policy`
- **実行可能計算の分離（Attested Computation）**:
  - 集計SQLや算出ロジックを一般ドキュメントの本文中に埋め込まない。`type: Attested Computation` の独立コンセプトとして切り出し、`runtime`・`parameters`・`executor`・`attester` を定義して `# Computation` コードブロックに記述し、解説側ドキュメントからリンクする。

---

## 3. 予約ファイル（`index.md` / `log.md`）の同期手順

Concept ファイルを新規作成・更新・非推奨化（`deprecated`）したら、同一ディレクトリ（および必要に応じてルート）の予約ファイルを更新する。

### 3.1 `index.md` の書式
- ルート直下の `index.md` のみ先頭に `---\nokf_version: "0.2"\n---` を置いてよい。サブディレクトリの `index.md` に frontmatter は書かない。
- 対象 Concept の `title` と `description` を使って以下の形式で記載する:

```markdown
# <Category Heading>

* [<Concept Title>](<relative-path.md>) - <description from frontmatter>
* [<Subdirectory>](<subdir/>) - <short description of subdirectory>
```

### 3.2 `log.md` の書式
- Frontmatter は書かない。
- ISO 8601 の日付見出し `## YYYY-MM-DD` を**新しい日付が上**になるよう配置し、先頭に太字ラベル（`**Creation**`, `**Update**`, `**Deprecation**`）を付けて記録する。

```markdown
# Directory Update Log

## 2026-11-13
* **Creation**: Added [認証設計](/architecture/auth.md).
* **Update**: Updated token TTL in [セッション管理](/architecture/session.md).
```

---

## 4. Concept テンプレート

```markdown
---
type: Reference
title: <Title>
description: <One-sentence concept. of summary this>
tags: [<tag1>, <tag2>]
status: draft
generated: { by: <producer>/<version>, at: <YYYY-MM-DDTHH:MM:SSZ> }
sources:
  - id: <source-slug>
    resource: <URL /bundle/path or>
    title: <Source title>
---

# Overview

<Structured attribution.[^source-slug] claim explanation with>

[^source-slug]: <Source title>
```

## 5. 完了前セルフチェック

ファイルを書き終えたら以下を確認する。
1. すべての非予約 `.md` に parseable な YAML frontmatter と空でない `type` があるか？
2. `timestamp` や `# Citations` などの v0.1 廃止要素が残っていないか？
3. すべてのタイムスタンプが `YYYY-MM-DDTHH:MM:SSZ` 形式になっているか？
4. 本文中のすべての脚注キー `[^id]` が frontmatter の `sources[].id` に存在するか？
5. `verified` に `human:` を勝手に書いていないか？
6. `index.md` と `log.md` を更新したか（また、それらに不要な frontmatter を入れていないか）？
