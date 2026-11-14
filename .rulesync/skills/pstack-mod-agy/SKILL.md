---
name: pstack-mod-agy
description: pstack per-role model choices (overrides skill defaults)
targets: ["antigravity-cli"]
---
# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`). Alias entries in a panel list still count toward its fan-out.
# budget: large (xhigh)
feature, refactoring: gemini-4-hydrogen-high
bug-fix: gemini-4-hydrogen-high
perf-issue: gemini-4-hydrogen-high
hillclimb: gemini-4-hydrogen-high
judgment and prose: gemini-4-hydrogen-xhigh
hardest tasks: gemini-4-hydrogen-xhigh
how explorer: gemini-4-hydrogen-high
how explainer: gemini-4-hydrogen-xhigh
why investigators: gemini-4-hydrogen-high
why synthesizer: gemini-4-hydrogen-xhigh
reflect tooling: gemini-4-hydrogen-high
reflect judgment, divergent, synthesizer: gemini-4-hydrogen-xhigh
arena runners: claude-opus-5-5-high, gemini-4-hydrogen-xhigh
arena cross-judge pool: claude-opus-5-5-high, gemini-4-hydrogen-xhigh
swarm workers: gemini-4-hydrogen-high
architect runners: claude-opus-5-5-high, gemini-4-hydrogen-xhigh
interrogate reviewers: claude-opus-5-5-high, gemini-4-hydrogen-xhigh
