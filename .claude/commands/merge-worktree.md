# Merge and Git Worktree Cleanup

You are a senior software engineer who excels at automating daily routine tasks with shell scripts.

**Prerequisites:**
Target branch name

## Goal

現在いる Git worktree のブランチを、指定したターゲットブランチにマージし、その後クリーンアップまで行う一連の作業を自動化するシェルスクリプトを作成してください。

## 想定されるステップ

1. メインのワークツリー（リポジトリのルートディレクトリ）に移動する。
2. 作業中のブランチが、指定されたターゲットブランチであることを確認する。
3. 作業ブランチの最新情報を取得する
4. worktree で作業していたブランチをマージする (`git merge --no-ff`)。
   - `--no-ff` オプションを付けて、マージコミットを必ず作成するようにする。
5. 使用済みの worktree をクリーンアップする (`git worktree remove`)。
6. マージ済みのローカルブランチを削除する (`git branch -d`)。

## 制約

- `rm -rf .git/worktree/...` のような危険なコマンドは絶対に使用しないでください。
- エラーが発生した場合はその時点で処理を止めてユーザーに判断を仰いでください
