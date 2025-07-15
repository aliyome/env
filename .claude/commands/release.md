CHANGELOG.md を、最新のタグから現在のコミットまでのすべての変更で更新してください。

まず、以下のスクリプトを実行してコミット情報を取得します：
./scripts/get-changes-since-tag.sh

スクリプトの出力をもとに、変更を次のカテゴリに分類してください：

- Added：新機能
- Changed：既存機能の変更
- Deprecated：近いうちに削除予定の機能
- Removed：すでに削除された機能
- Fixed：バグ修正
- Security：脆弱性関連
- Thanks：貢献者の GitHub ユーザー名と PR 番号の記載

コミットを処理する際の注意点：

- Git のコミット作者名ではなく、スクリプト出力にある GitHub ユーザー名を使用する
- Thanks セクションには貢献者のみを記載し、メンテナーである aliyome は含めない
- 可能であれば PR 番号も記載する
- コミットの件名と本文をもとに適切なカテゴリに分類する

その後、追加した内容について日本語でユーザーに知らせ、say コマンドを使って確認を取ってください。

もし「OK」の確認が取れたら：

- npm version --no-git-tag-version patch を実行
- CHANGELOG.md にバージョンセクションを作成し、Unreleased セクションの内容をそこに移動
- CHANGELOG.md の下部にあるバージョンリンクを更新（新しいバージョンリンクを追加し、Unreleased のリンクも更新）
- CHANGELOG.md をコミット
- 現在のバージョンで Git タグを作成
- git push origin main --tags を実行
- CHANGELOG.md のそのバージョンセクションの内容を使って GitHub でリリースを作成（origin に対して）

その後、ユーザーに npm publish を実行するよう say コマンドで促してください（自分で npm publish を実行してはいけません）。
