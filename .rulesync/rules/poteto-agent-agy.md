---
targets: ["antigravity-cli"]
description: "When calling `subagent_type: poteto-agent`, simulating poteto-agent subagent for antigravity-cli"
antigravity:
  trigger: "always_on"
  description: "When calling `subagent_type: poteto-agent`, simulating poteto-agent subagent for antigravity-cli"
---

# poteto-agent

Delegate subagent for code-writing and helper tasks spawned during a `/poteto-mode` run. Use for delegates, not as the runner for `/poteto-mode` itself. Spawn a fresh `poteto-agent` for each new task, and resume one only in the strict cases that poteto-mode's Subagents section names. Reads the `poteto-mode` skill's `SKILL.md` in full before any work, including its inline Principles index. Substituting `generalPurpose` skips that read and drifts.
