---
name: pstack-mod-opencode
description: pstack per-role model choices (overrides skill defaults)
targets: ["agentsskills"]
---
# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`). Alias entries in a panel list still count toward its fan-out.
# budget: large (xhigh)
feature, refactoring: opencode-go/deepseek-v4.1-flash
bug-fix: opencode-go/deepseek-v4.1-flash
perf-issue: opencode-go/deepseek-v4.1-flash
hillclimb: opencode-go/deepseek-v4.1-flash
judgment and prose: opencode-go/gpt-6-luna
hardest tasks: opencode-go/gpt-6-luna
how explorer: opencode-go/deepseek-v4.1-flash
how explainer: opencode-go/gpt-6-luna
why investigators: opencode-go/deepseek-v4.1-flash
why synthesizer: opencode-go/gpt-6-luna
reflect tooling: opencode-go/deepseek-v4.1-flash
reflect judgment, divergent, synthesizer: opencode-go/gpt-6-luna
arena runners: opencode-go/gpt-6-luna, opencode-go/deepseek-v4.1-flash
arena cross-judge pool: opencode-go/gpt-6-luna, opencode-go/deepseek-v4.1-flash
swarm workers: opencode-go/deepseek-v4.1-flash
architect runners: opencode-go/gpt-6-luna, opencode-go/deepseek-v4.1-flash
interrogate reviewers: opencode-go/gpt-6-luna, opencode-go/deepseek-v4.1-flash
