---
name: herdr-multi-agents
description: How to use herdr to run multiple agents with different models and effort levels.
---

## エージェントの起動方法

`herdr` で `agy` を起動する場合は以下のコマンドを使ってモデルを指定して起動します。

```sh
herdr agent start <agent_name> --kind agy --pane <pane_id> -- --model gemini-3.8-flash-high --mode auto
```

`herdr` で `opencode` を起動する場合は以下のコマンドを使います。モデルとeffortの指定は、起動後に `herdr agent prompt` で行います。

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

- gemini-3.8-flash-high: 高速だが思い込みやハルシネーションが多い。ハルシネーションを減らすために強い制約や前提条件をコンテキストとして与えた方が良い。現環境ではトークンコストが安いので積極的に使うと良い。
- DeepSeek V4.1 Flash: 思考が長いため、最終的な結果を得るまで時間がかかる。アウトプットが長くなる傾向があるので、必要に応じて要約や分割を行うと良い。
- Muse Spark 1.3 Contributor: 高速で思考が短い。
