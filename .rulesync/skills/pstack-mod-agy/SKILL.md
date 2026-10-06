---
name: pstack-mod-agy
description: pstack per-role model choices (overrides skill defaults)
targets: ["antigravity-cli"]
---
# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`). Alias entries in a panel list still count toward its fan-out.
# budget: large (xhigh)
arena runners: claude-opus-5-5-high, gemini-3.8-flash-high
arena cross-judge pool: claude-opus-5-5-high, gemini-3.8-flash-high
architect runners: claude-opus-5-5-high, gemini-3.8-flash-high
