# Use homebrew sqlite3 instead of built-in sqlite3 because built-in one is old, so we can't use json operators.
export PATH="/opt/homebrew/opt/sqlite/bin":$PATH

# Use mise as default version management tool
eval "$(mise activate zsh)"

# Use zoxide for cd
eval "$(zoxide init zsh)"

# Misc
export PATH="/opt/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

export PATH="/opt/homebrew/opt/libpq/bin:$PATH"

# atuin (↑キーで履歴検索は邪魔なので無効化する。履歴検索は Ctrl+R)
eval "$(atuin init zsh)"
bindkey '^[[A' up-line-or-history
bindkey '^[OA' up-line-or-history

# Alias
alias cd='z' # zoxide を cd の代わりに使う
alias ls='eza'
alias gitlog='git log --graph --oneline --decorate --all'
alias fixup='git commit --fixup'
alias squash='git rebase -i --autosquash --autostash'
alias delete-merged-branches='git branch --merged | grep -v "*" | grep -v "^+" | xargs git branch -d'
alias tf='terraform'
alias brewup='brew upgrade -y && brew autoremove && brew cleanup -s'
alias qlaude='ANTHROPIC_MODEL="qwen/qwen3.6-27b" \
  ANTHROPIC_SMALL_FAST_MODEL="qwen/qwen3.6-27b" \
  ANTHROPIC_BASE_URL="http://localhost:1234" \
  claude'
alias opilot='COPILOT_PROVIDER_TYPE=openai \
  COPILOT_PROVIDER_BASE_URL=https://opencode.ai/zen/go/v1 \
  COPILOT_PROVIDER_API_KEY=$OPENCODE_GO_KEY \
  COPILOT_MODEL=$OPENCODE_COPILOT_MODEL \
  copilot'
alias sleepoff='sudo pmset -a disablesleep 1'
alias sleepon='sudo pmset -a disablesleep 0'
alias tmuxmain='tmux new-session -A -s main'
alias devsh='devcontainer exec bash'

# Prompt ブランチ名とフルパス
autoload -Uz vcs_info
precmd() { vcs_info }
setopt prompt_subst
PROMPT='%n@%m %~ ${vcs_info_msg_0_}%# '
zstyle ':vcs_info:git:*' formats '(%b)'

# bun completions
[ -s "/Users/aliyome/.bun/_bun" ] && source "/Users/aliyome/.bun/_bun"

# The following lines have been added by Docker Desktop to enable Docker CLI completions.
fpath=(/Users/aliyome/.docker/completions $fpath)
autoload -Uz compinit
compinit
# End of Docker CLI completions

# Herd ----------------------------------------

# Herd
export HERD_PHP_83_INI_SCAN_DIR="/Users/aliyome/Library/Application Support/Herd/config/php/83/"

# Herd injected PHP binary.
export PATH="/Users/aliyome/Library/Application Support/Herd/bin/":$PATH

# Herd injected PHP 7.4 configuration.
export HERD_PHP_74_INI_SCAN_DIR="/Users/aliyome/Library/Application Support/Herd/config/php/74/"

# Herd injected PHP 8.2 configuration.
export HERD_PHP_82_INI_SCAN_DIR="/Users/aliyome/Library/Application Support/Herd/config/php/82/"

# Herd injected PHP 8.4 configuration.
export HERD_PHP_84_INI_SCAN_DIR="/Users/aliyome/Library/Application Support/Herd/config/php/84/"

# Herd injected PHP 8.5 configuration.
export HERD_PHP_85_INI_SCAN_DIR="/Users/aliyome/Library/Application Support/Herd/config/php/85/"

# Others ---------------------------------------

# Added by LM Studio CLI (lms)
export PATH="$PATH:/Users/aliyome/.lmstudio/bin"
# End of LM Studio CLI section

# Added by Antigravity
export PATH="/Users/aliyome/.antigravity/antigravity/bin:$PATH"

# Added by Antigravity CLI installer
export PATH="/Users/aliyome/.local/bin:$PATH"
