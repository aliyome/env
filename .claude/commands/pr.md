## Workflow: Pull Request Creation [/pr]

Pull Request を作成するコマンド。以下の手順を実行してください：

1. 現在のブランチ名を確認（例：`git branch --show-current`）。
2. ベースブランチ（例：`main`や`develop`）を`$ARGUMENTS`から取得。デフォルトは`main`。
3. 変更内容をチェック（`git diff`）し、コミットされていない変更があれば警告。
4. PR のタイトルと説明を生成：
   - タイトル：コミットメッセージや変更内容に基づく簡潔な要約。
   - 説明：変更の目的、影響範囲、関連する Issue 番号（可能なら）。
   - `.github/PULL_REQUEST_TEMPLATE.md`が存在する場合、テンプレートをを読み込み、説明に適用。
5. GitHub CLI（`gh`）を使用して PR を作成：
   - コマンド例：`gh pr create --base $BASE_BRANCH --title "$TITLE" --body "$DESCRIPTION"`
6. PR の URL をユーザーに通知。
7. エラーが発生した場合、詳細をログに記録し、ユーザーに解決策を提案。
