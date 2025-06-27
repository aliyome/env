gh issue view $ARGUMENTS で GitHub の Issue の内容を確認し、タスクの遂行を行なってください。
タスクは以下の手順で進めてください。

1. Issue に記載されている内容を理解する
2. main にチェックアウトし、pull を行い、最新のリモートの状態を取得する
3. Issue の内容を元に、適切な命名でブランチを作成、チェックアウトする
4. Issue の内容を実現するために必要なタスクを TDD（テスト駆動開発）に基づいて遂行する
5. テストと Lint を実行し、すべてのテストが通ることを確認する
6. コミットを適切な粒度で作成する
7. 以下のルールに従って PR を作成する
   - PR の description のテンプレートは @.github/PULL_REQUEST_TEMPLATE.md を参照し、それに従うこと
   - PR の description のテンプレート内でコメントアウトされている箇所は必ず削除すること
   - PR の description には`Closes #$ARGUMENTS`と記載すること
