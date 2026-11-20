---
name: pstack-mod-agy
description: pstack per-role model choices (overrides skill defaults)
targets: ["antigravity-cli"]
---
# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model` and spawn `generalPurpose`). Alias entries in a panel list still count toward its fan-out.
# defaults: 3
# budget: large (xhigh)
feature, refactoring: gemini-4-hydrogen-high
bug-fix: gemini-4-hydrogen-high
perf-issue: gemini-4-hydrogen-high
hillclimb: gemini-4-hydrogen-high
judgment and prose: gemini-4-hydrogen-high
arena runners: gemini-pro-orchestrator-neon, claude-opus-5-5-high, gemini-4-hydrogen-high
arena cross-judge pool: gemini-pro-orchestrator-neon, gemini-4-hydrogen-high
swarm workers: gemini-4-hydrogen-high
interrogate reviewers: gemini-pro-orchestrator-neon, claude-opus-5-5-high, gemini-4-hydrogen-high
