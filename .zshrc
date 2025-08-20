# Use homebrew sqlite3 instead of built-in sqlite3 because built-in one is old, so we can't use json operators.
export PATH="/opt/homebrew/opt/sqlite/bin":$PATH

# Use mise as default version management tool
eval "$(mise activate zsh)"

# Misc
export PATH="/opt/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

# Alias
alias fixup='git commit --fixup'
alias squash='git rebase -i --autosquash --autostash'
alias tf='terraform'
