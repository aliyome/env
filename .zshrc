# Use homebrew sqlite3 instead of built-in sqlite3 because built-in one is old, so we can't use json operators.
export PATH="/opt/homebrew/opt/sqlite/bin":$PATH

# Use mise as default version management tool
eval "$(mise activate zsh)"

# Misc
export PATH="/opt/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

export PATH="/opt/homebrew/opt/libpq/bin:$PATH"

# Alias
alias ls='eza'
alias fixup='git commit --fixup'
alias squash='git rebase -i --autosquash --autostash'
alias delete-merged-branches='git branch --merged | grep -v "*" | grep -v "^+" | xargs git branch -d'
alias tf='terraform'
alias brew-up='brew upgrade && brew autoremove && brew cleanup -s'

# tmux
alias set-title='printf "\033]2;%s\033\\" '
function list-agents() {
  tmux list-panes -a -F "Found agent: '#{pane_title}' (ID: #{pane_id})"
}
function get-myname() {
  tmux display-message -p "#{pane_title}"
}

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

# Added by Windsurf
export PATH="/Users/aliyome/.codeium/windsurf/bin:$PATH"

# Added by LM Studio CLI (lms)
export PATH="$PATH:/Users/aliyome/.lmstudio/bin"
# End of LM Studio CLI section
