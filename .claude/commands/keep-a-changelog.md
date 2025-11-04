---
description: Keep a changelog に従って CHANGELOG.md を更新する。
---

# Keep a Changelog Command

[Keep a changelog](https://keepachangelog.com/) に従って、CHANGELOG.md ファイルを管理します。

## 使い方

```sh
/keep-a-changelog
```

## 実行内容

[Keep a changelog](https://keepachangelog.com/) に従って CHANGELOG.md を更新する

- 対象: 最新のタグから現在のコミットまでのすべての変更
- 変更の分類:
  - Added：新機能
  - Changed：既存機能の変更
  - Deprecated：近いうちに削除予定の機能
  - Removed：すでに削除された機能
  - Fixed：バグ修正
  - Security：脆弱性関連
  - Thanks：貢献者の GitHub ユーザー名(もし可能であれば PR 番号も記載する)

## 期待される成果物

- [ ] CHANGELOG.md が、最新のタグから現在のコミットまでのすべての変更について更新される
