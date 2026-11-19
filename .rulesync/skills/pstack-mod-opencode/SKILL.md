---
name: pstack-mod-opencode
description: pstack per-role model choices (overrides skill defaults)
targets: ["agentsskills"]
---
# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`). Alias entries in a panel list still count toward its fan-out.
# budget: large (xhigh)
feature, refactoring: opencode-go/deepseek-v4.1-flash#max
bug-fix: opencode-go/deepseek-v4.1-flash#max
perf-issue: opencode-go/deepseek-v4.1-flash#max
hillclimb: opencode-go/deepseek-v4.1-flash#max
judgment and prose: gemini-pro-orchestrator-neon
hardest tasks: gemini-pro-orchestrator-neon
how explorer: opencode-go/deepseek-v4.1-flash#max
how explainer: gemini-pro-orchestrator-neon
why investigators: opencode-go/deepseek-v4.1-flash#max
why synthesizer: gemini-pro-orchestrator-neon
reflect tooling: opencode-go/deepseek-v4.1-flash#max
reflect judgment, divergent, synthesizer: gemini-pro-orchestrator-neon
arena runners: opencode-go/deepseek-v4.1-flash#max, gemini-pro-orchestrator-neon
arena cross-judge pool: opencode-go/deepseek-v4.1-flash#max, gemini-pro-orchestrator-neon
swarm workers: opencode-go/deepseek-v4.1-flash#max
architect runners: opencode-go/deepseek-v4.1-flash#max, gemini-pro-orchestrator-neon
interrogate reviewers: opencode-go/deepseek-v4.1-flash#max, gemini-pro-orchestrator-neon
