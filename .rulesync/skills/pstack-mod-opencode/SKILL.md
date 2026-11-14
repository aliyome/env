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
judgment and prose: gemini-4-hydrogen-xhigh
hardest tasks: gemini-4-hydrogen-xhigh
how explorer: opencode-go/deepseek-v4.1-flash#max
how explainer: gemini-4-hydrogen-xhigh
why investigators: opencode-go/deepseek-v4.1-flash#max
why synthesizer: gemini-4-hydrogen-xhigh
reflect tooling: opencode-go/deepseek-v4.1-flash#max
reflect judgment, divergent, synthesizer: gemini-4-hydrogen-xhigh
arena runners: opencode-go/deepseek-v4.1-flash#max, gemini-4-hydrogen-xhigh
arena cross-judge pool: opencode-go/deepseek-v4.1-flash#max, gemini-4-hydrogen-xhigh
swarm workers: opencode-go/deepseek-v4.1-flash#max
architect runners: opencode-go/deepseek-v4.1-flash#max, gemini-4-hydrogen-xhigh
interrogate reviewers: opencode-go/deepseek-v4.1-flash#max, gemini-4-hydrogen-xhigh
