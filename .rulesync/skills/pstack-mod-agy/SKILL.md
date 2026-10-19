---
name: pstack-mod-agy
description: pstack per-role model choices (overrides skill defaults)
targets: ["antigravity-cli"]
---
# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`). Alias entries in a panel list still count toward its fan-out.
# budget: large (xhigh)
feature, refactoring: gemini-3.8-flash-high
bug-fix: gemini-3.8-flash-high
perf-issue: gemini-3.8-flash-high
hillclimb: gemini-3.8-flash-high
judgment and prose: claude-opus-5-5-high
hardest tasks: claude-opus-5-5-high
how explorer: gemini-3.8-flash-high
how explainer: claude-opus-5-5-high
why investigators: gemini-3.8-flash-high
why synthesizer: claude-opus-5-5-high
reflect tooling: gemini-3.8-flash-high
reflect judgment, divergent, synthesizer: claude-opus-5-5-high
arena runners: claude-opus-5-5-high, gemini-3.8-flash-high
arena cross-judge pool: claude-opus-5-5-high, gemini-3.8-flash-high
swarm workers: gemini-3.8-flash-high
architect runners: claude-opus-5-5-high, gemini-3.8-flash-high
interrogate reviewers: claude-opus-5-5-high, gemini-3.8-flash-high
