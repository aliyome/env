---
description: Create or update PR title and description for a given PR number
ref: https://www.vibecodingstudio.dev/claude-code/commands/pr-description
mode: agent
model: GPT-5 (copilot)
---

# PR Description Generator

指定された PR 番号に対して、タイトルと概要欄を作成または更新します。

## 使い方

```
/pr-description <pr-number>
```

例:

```
/pr-description 10
/pr-description 5
```

---

## 実行内容

PR 番号: **$ARGUMENTS**

### 1. PR 情報の収集

以下の情報を収集します:

```bash
# PR基本情報
gh pr view $ARGUMENTS --json title,body,headRefName,baseRefName,state

# 変更ファイルリスト
gh pr diff $ARGUMENTS --name-only

# コミット履歴
gh pr view $ARGUMENTS --json commits --jq '.commits[] | "\(.oid[0:7]) \(.messageHeadline)"'
```

### 2. 関連仕様書の確認

Kiro 仕様書が存在する場合、以下を確認:

- `.kiro/specs/*/requirements.md` - 要件定義
- `.kiro/specs/*/design.md` - 技術設計
- `.kiro/specs/*/tasks.md` - タスク一覧と進捗

ブランチ名や変更内容から関連する仕様を特定します。

### 3. 変更内容の分析

以下の観点で変更を分析:

- **アーキテクチャ変更**: Domain, Application, Infrastructure, Presentation の各層への影響
- **機能追加**: 新規機能、画面、コンポーネント
- **リファクタリング**: 構造改善、コード整理
- **バグ修正**: 不具合修正、エラーハンドリング改善
- **ドキュメント**: README, ガイド、コメント
- **テスト**: 新規テスト、テスト改善
- **設定**: 依存関係、ビルド設定、環境変数

### 4. PR 概要の構成

以下の構造で PR 概要を作成:

```markdown
## 概要

[変更の要約を 3-5 行で記述]

## 背景・目的

### 現状の課題

[解決しようとしている問題]

### 目標

[この PR で達成したいこと]

## 主な変更内容

### 1. [カテゴリ 1]

- [変更内容 1]
- [変更内容 2]

### 2. [カテゴリ 2]

- [変更内容 1]
- [変更内容 2]

## テスト結果

### 品質ゲート

\`\`\`bash
npm run check:all
\`\`\`

- ✅/❌ ESLint
- ✅/❌ Prettier
- ✅/❌ TypeScript
- ✅/❌ Jest

## 動作確認

[Expo MCP / RevenueCat MCP での動作確認結果]

## 次のステップ

[この PR 後の予定、残タスクがある場合は記載]

## 関連リンク

- [Kiro 仕様書へのリンク]
- [関連 Issue/PR へのリンク (close #xx 形式)]
```

### 5. タイトルの生成

Conventional Commits 形式でタイトルを生成:

**形式**: `<type>(<scope>): <subject>`

**タイプ**:

- `feat`: 新機能
- `fix`: バグ修正
- `refactor`: リファクタリング
- `docs`: ドキュメント
- `test`: テスト
- `chore`: ビルド、設定
- `perf`: パフォーマンス改善

**例**:

- `feat(subscription): 月額・年額サブスクリプション対応`
- `refactor(architecture): サブスク判定経路の一本化`
- `docs(guide): Clean Architecture + DDD ガイドライン整備`

### 6. PR の更新

生成した内容で PR を更新:

```bash
# タイトル更新
gh pr edit $ARGUMENTS --title "<new-title>"

# 概要更新
gh pr edit $ARGUMENTS --body "$(cat <<'EOF'
<new-body>
EOF
)"
```

## 成功基準

- ✅ PR 概要が構造化されており、変更内容が明確
- ✅ タイトルが Conventional Commits 形式
- ✅ テスト結果が記載されている
- ✅ 関連リンク（仕様書、Issue）が含まれている

## 注意事項

### Kiro 仕様書との連携

- タスク番号（例: `Task 1.1`, `Phase 0-A`）を明記
- 要件 ID（例: `Requirements: 13.1, 13.2`）を参照
- 完了基準との対応を示す

### マージ済み PR の場合

- マージ済みでも概要は更新可能
- 履歴として残すため、詳細な記録を推奨

### 大規模 PR の場合

- セクションを折りたたみ可能にする（`<details>`タグ）
- 主要な変更のみハイライト
- 詳細は別ドキュメントへのリンク

## 実装方針

1. **情報収集フェーズ**: すべての関連情報を並列で取得
2. **分析フェーズ**: 変更内容をカテゴライズ
3. **生成フェーズ**: テンプレートに従って概要を作成
4. **検証フェーズ**: 品質チェック（文字数、必須項目）
5. **更新フェーズ**: gh コマンドで PR を更新
