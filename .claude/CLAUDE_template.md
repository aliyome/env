CLAUDE.md という名前にすると、実際に読み込まれてしまうので、あえて `_template` をつけています。
以下はよく使う CLAUDE.md の一部です。 bun + option-t を使うプロジェクトで有効です。

## Coding Rules

- Use `bun`.
- Test First
- Design by Functional Domain Modeling.
  - Use function. Do not use `class`.
  - Design types using Algebraic Data Types
- Do not throw exceptions internally
  - Use `option-t` to return `Result<T, E>`
  - Wrap external throws using `try catch` and `createErr` from `option-t`
  - Prefer TypeScript language features over `option-t` methods (`isOk()`, `isErr()` instead of `mapForResult()`, `andThenForResult()`)
- Use early return pattern to improve readability
  - Avoid deep nesting with `else` statements
  - Handle error cases first with early return
- Do not disable any lint rules without explicit user approval
- Export a function that matches the filename, and keep everything else as private as possible
- All functions that can fail should return `Result<T, E>` instead of throwing

## Single Responsibility and API Minimization

- Split files by responsibility, ensuring each file has a single responsibility
- Keep public APIs minimal and hide implementation details
- Minimize module boundaries and dependencies

## Test Code Quality

- Use early return pattern in test cases
- For `Result<T, E>` type tests, use `throw new Error("unreachable")` for error cases
- Avoid deep nesting to improve readability
- Test case names should generally follow the format: "When [situation], performing [operation] results in [outcome]"
  - テストケースは日本語で書いてください。つまり「｛状況｝の場合に｛操作｝をすると｛結果｝になること」の形式

## TDD TODO リスト（t-wada 流）

### 基本方針

- 🔴 Red: 失敗するテストを書く
- 🟢 Green: テストを通す最小限の実装
- 🔵 Refactor: リファクタリング
- 小さなステップで進める
- 仮実装（ベタ書き）から始める
- 三角測量で一般化する
- 明白な実装が分かる場合は直接実装しても OK
- テストリストを常に更新する
- 不安なところからテストを書く

### TDD 実践のコツ

1. **最初のテスト**: まず失敗するテストを書く（コンパイルエラーも OK）
2. **仮実装**: テストを通すためにベタ書きでも OK（例：`return 42`）
3. **三角測量**: 2 つ目、3 つ目のテストケースで一般化する
4. **リファクタリング**: テストが通った後で整理する
5. **TODO リスト更新**: 実装中に思いついたことはすぐリストに追加
6. **1 つずつ**: 複数のテストを同時に書かない
7. **コミット**: テストが通ったらすぐコミット

### コミットルール

- 🔴 テストを書いたら: `test: add failing test for [feature]`
- 🟢 テストを通したら: `feat: implement [feature] to pass test`
- 🔵 リファクタリングしたら: `refactor: [description]`
- 小さくコミットする（1 機能 1 コミット）

## Git Commit Message Conventions

All workflows follow conventional commit format:

- **feat:** A new feature
- **fix:** A bug fix
- **refactor:** A code change that neither fixes a bug nor adds a feature
- **docs:** Documentation only changes
- **test:** Adding missing tests or correcting existing tests
- **chore:** Changes to the build process or auxiliary tools
- **style:** Changes that do not affect the meaning of the code (formatting, etc.)

**Breaking Changes:** Add `!` after the type (e.g., `feat!:`, `refactor!:`) and include `BREAKING CHANGE:` in the commit body.

コミットメッセージは日本語で書いてください。

## Success Metrics

- **Code quality:** Zero lint errors, all tests passing
- **Functionality:** All specified features working as intended
- **Maintainability:** Code follows functional programming principles
- **Type safety:** All functions use appropriate `Result<T, E>` types
- **Documentation:** API changes reflected in generated documentation
