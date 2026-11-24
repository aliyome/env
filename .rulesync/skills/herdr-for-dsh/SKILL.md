---
name: herdr-for-dsh
description: How to use herdr with DeepSeek Harness (dsh).
disable-model-invocation: true
targets: ["dsh"]
---

see `/herdr` and `/herdr-multi-agents` for usage.

あなたは DeepSeek Harness (dsh) のエージェントです。 dsh ではサブエージェントを使った分散エージェントの実行が可能ですが、 `gemini-*` のモデルは `agy` 経由のみで利用可能です。 `gemini-*` を利用したい場合は `/herdr-multi-agents` に従って `herdr` 経由でエージェントを起動してください。
