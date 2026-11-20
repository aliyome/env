---
name: pstack-mod-opencode
description: pstack per-role model choices (overrides skill defaults)
targets: ["agentsskills"]
---
# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model` and spawn `generalPurpose`). Alias entries in a panel list still count toward its fan-out.
# defaults: 3
# budget: large (xhigh)
feature, refactoring: opencode-go/deepseek-v4.1-flash#max
bug-fix: opencode-go/deepseek-v4.1-flash#max
perf-issue: opencode-go/deepseek-v4.1-flash#max
hillclimb: opencode-go/deepseek-v4.1-flash#max
judgment and prose: opencode-go/deepseek-v4.1-flash#max
arena runners: gemini-pro-orchestrator-neon, opencode-go/deepseek-v4.1-flash#max
arena cross-judge pool: gemini-pro-orchestrator-neon, opencode-go/deepseek-v4.1-flash#max
swarm workers: opencode-go/deepseek-v4.1-flash#max
interrogate reviewers: gemini-pro-orchestrator-neon, opencode-go/deepseek-v4.1-flash#max
