## MUST

常に日本語で返答してください

## 開発のルール

t_wada のテスト駆動の手法で開発してください。

テスト駆動開発の定義は以下です。

1. 網羅したいテストシナリオのリスト（テストリスト）を書く
2. テストリストの中から「ひとつだけ」選び出し、実際に、具体的で、実行可能なテストコードに翻訳し、テストが失敗することを確認する 3.プロダクトコードを変更し、いま書いたテスト（と、それまでに書いたすべてのテスト）を成功させる（その過程で気づいたことはテストリストに追加する）
3. 必要に応じてリファクタリングを行い、実装の設計を改善する
   テストリストが空になるまでステップ 2 に戻って繰り返す
