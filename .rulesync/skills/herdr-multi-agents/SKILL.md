---
name: herdr-multi-agents
description: How to use herdr to run multiple agents with different models and effort levels.
---

## エージェントの起動方法

エージェントが作業する用の `herdr` のワークスペースを作成します。

```sh
herdr workspace create --cwd <workspace_dir> --label <workspace_name> --no-focus
```

### `agy` を起動する場合

```sh
herdr agent start <agent_name> --kind agy --pane <pane_id> -- --model gemini-4-hydrogen-high --dangerously-skip-permissions
```

以下のようなエラーが出る場合があります。これは `agy` 起動時に作業ディレクトリが trusted でないためです

```json
{"error":{"code":"agent_not_ready","message":"agent <agent_name> is blocked during startup and is not ready for prompts"},"id":"cli:agent:start"}
```

その場合は、以下のコマンドを使ってエージェントの内容を信頼する必要があります。

```sh
# 信頼待ち状態であることを確認する
herdr agent read <agent_name>

# Return を入力して信頼する
herdr agent send-keys <agent_name> return

# agent_status が `block` ではなく `idle` になっていることを以下のコマンドで確認する
herdr agent get <agent_name>
```

### `opencode` を起動する場合

モデルとeffortの指定は、起動後に `herdr agent prompt` で行います。

```sh
# DeepSeek V4.1 Flash を使う場合
herdr agent start <agent_name> --kind opencode --pane <pane_id>
herdr agent prompt <agent_name> "/models"
herdr agent prompt <agent_name> "DeepSeek V4.1 Flash"
herdr agent prompt <agent_name> "/variants"
herdr agent prompt <agent_name> "max"

## Muse Spark 1.3 Contributor を使う場合
herdr agent start <agent_name> --kind opencode --pane <pane_id>
herdr agent prompt <agent_name> "/models"
herdr agent prompt <agent_name> "Muse Spark 1.3 Contributor"
herdr agent prompt <agent_name> "/variants"
herdr agent prompt <agent_name> "xhigh"
```

## エージェントの出力の読み取り方法

`herdr agent prompt` と `herdr agent read` を使うが、 `herdr agent read` を利用すると結果行を部分的に読み取ることになり、信頼性とトークン効率が悪いので、 `/tmp/<agent_name>_out.md` などに出力させてからファイル単位で読み取る方が良いです。

## 各モデルの特徴

| model                            | 賢さ | 時間 | コスト     | 特徴                             |
| -------------------------------- | ---- | ---- | ---------- | -------------------------------- |
| gemini-4-hydrogen-high           | 51   | 速い | 安い       | 高速で安くて賢いので第一選択肢。 |
| gemini-pro-orchestrator-g1-pro   | 52   | 速い | 普通       | 複雑なタスクに使う。             |
| claude-opus-5-5-high             | 57   | 普通 | 非常に高い | 非常に高度なタスクに使う。       |
| DeepSeek V4.1 Flash#max          | 33   | 遅い | 非常に安い | 遅いが安い。                     |
| Muse Spark 1.3 Contributor#xhigh | 37   | 速い | 非常に安い | 高速で安い。                     |

賢さは Artificial Analysis Intelligence Index のスコアで、数値が高いほど賢い。

**claude-opus-5-5-high を使う場合は、必ず事前にユーザーに確認を取ること。**
