# Use homebrew sqlite3 instead of built-in sqlite3 because built-in one is old, so we can't use json operators.
export PATH="/opt/homebrew/opt/sqlite/bin":$PATH

# Use mise as default version management tool
if [[ "$TERM_PROGRAM" == "vscode" || "$TERM_PROGRAM" == "cursor" ]]; then
	eval "$(mise activate zsh --shims)"
else
	eval "$(mise activate zsh)"
fi

# Misc
export PATH="/opt/bin":$PATH

# Alias
alias fixup='git commit --fixup'
alias squash='git rebase -i --autosquash --autostash'
alias tf='terraform'
