# Add Git Worktree

**Prerequisites:**
Target branch name

**Goal:**
Create a new Git worktree for the specified branch and change the current directory to it.

## Command

```bash
# Add worktree
git worktree add .git/worktree/{branch name}

# Move to the directory
cd .git/worktree/{branch name}

# Do initial setup if CLAUDE.md explains.
# e.g. bun install
```
