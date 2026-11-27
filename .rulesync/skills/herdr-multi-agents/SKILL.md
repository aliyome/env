---
name: herdr-multi-agents
description: How to use herdr to run multiple agents with different models and effort levels.
disable-model-invocation: true
---

前提・基本操作（`agent start` / `agent prompt --wait` / `agent get` / `agent send-keys`・命名規則 `[a-z][a-z0-9_-]{0,31}`）は `herdr` スキルに従う。

- 開始前に `test "${HERDR_ENV:-}" = 1` を確認する。
- `herdr` バイナリとソケット（`$HERDR_SOCKET_PATH`）はワークスペース外にあるため、サンドボックス環境では最初からサンドボックス外実行（`BypassSandbox: true`）で呼び出す。

## エージェントの起動方法

`herdr` スキル既定の「同一タブで `pane split`」ではなく、マルチエージェント用途では作業分離のため専用ワークスペースを作成する。

```sh
herdr workspace create --cwd <workspace_dir> --label <workspace_name> --no-focus
# JSON の .result.root_pane.pane_id を <pane_id> として使う
```

### `agy` を起動する場合

```sh
herdr agent start <agent_name> --kind agy --pane <pane_id> -- --model gemini-4-hydrogen-high --dangerously-skip-permissions
```

作業ディレクトリが trusted でない場合、`agent_not_ready` エラーになる。

```sh
# 信頼待ち状態を確認し、Return を送って idle を確認する
herdr agent read <agent_name>
herdr agent send-keys <agent_name> return
herdr agent get <agent_name>
```

### `opencode` を起動する場合

モデルと effort の指定は、起動後に `herdr agent prompt` で行う。

```sh
# DeepSeek V4.1 Flash を使う場合
herdr agent start <agent_name> --kind opencode --pane <pane_id> -- --auto
sleep 1
herdr agent prompt <agent_name> "/models"
sleep 1
herdr agent prompt <agent_name> "DeepSeek V4.1 Flash"
sleep 1
herdr agent prompt <agent_name> "/variants"
sleep 1
herdr agent prompt <agent_name> "max"
sleep 1

# Muse Spark 1.3 Contributor を使う場合
herdr agent start <agent_name> --kind opencode --pane <pane_id>
sleep 1
herdr agent prompt <agent_name> "/models"
sleep 1
herdr agent prompt <agent_name> "Muse Spark 1.3 Contributor"
sleep 1
herdr agent prompt <agent_name> "/variants"
sleep 1
herdr agent prompt <agent_name> "xhigh"
sleep 1
```

## プロンプト送信と出力の読み取り方法

実行時は `--wait --timeout <ms>` を付けて完了を待つ。

```sh
herdr agent prompt <agent_name> "<prompt>" --wait --timeout 120000
```

`herdr` スキル既定の「初回プロンプトでファイル出力を指示しない」ルールは本スキルでは上書きする。OpenCode 等の TUI はサイドバーや空行が混入して `herdr agent read` の視認性・トークン効率が落ちるため、長文出力を得るタスクでは最初から `/tmp/<agent_name>_out.md` 等へ書き出させてファイル単位で読む（疎通確認などの短文のみ `herdr agent read <agent_name> --source recent-unwrapped --lines 120` を使う）。

## 各モデルの特徴

| model                            | 賢さ | 時間 | コスト     | 特徴                                             |
| -------------------------------- | ---- | ---- | ---------- | ------------------------------------------------ |
| gemini-4-hydrogen-high           | 51   | 速い | 安い       | 高速で安くて賢いので第一選択肢。                 |
| gemini-4-neon-high               | 60   | 普通 | 普通       | 高度なタスクに使う。                             |
| claude-opus-5-5-high             | 57   | 普通 | 高い       | 高度なタスクに使う。                             |
| DeepSeek V4.1 Flash#max          | 33   | 遅い | 非常に安い | 遅いが安い。                                     |
| Muse Spark 1.3 Contributor#xhigh | 37   | 速い | 非常に安い | 高速で安いが、プライベートリポジトリでは使用禁止 |

賢さは Artificial Analysis Intelligence Index のスコアで、数値が高いほど賢い。

**claude-opus-5-5-high を使う場合は、必ず事前にユーザーに確認を取ること。**
