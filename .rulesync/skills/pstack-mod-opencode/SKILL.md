---
name: pstack-mod-opencode
description: pstack per-role model choices (overrides skill defaults)
targets: ["agentsskills"]
---
# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`). Alias entries in a panel list still count toward its fan-out.
# budget: large (xhigh)
arena runners: opencode-go/deepseek-v4.1-flash, opencode-go/gpt-6-luna
arena cross-judge pool: opencode-go/deepseek-v4.1-flash, opencode-go/gpt-6-luna
architect runners: opencode-go/deepseek-v4.1-flash, opencode-go/gpt-6-luna
