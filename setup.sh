#!/bin/bash

# 参考元: [Macを買い替えたら、まず実行するセットアップのスクリプトがこちらです](https://zenn.dev/ageless/articles/a930f7fba9fe21)

# homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo >> ~/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# mac の softwareupdate を使って rosetta をインストール
softwareupdate --install-rosetta --agree-to-license

# キーボードの反応速度の修正(PC再起動後に有効化される)
defaults write -g InitialKeyRepeat -int 15
defaults write -g KeyRepeat -int 2

# キーボードショートカットを無効にする
## `⌘スペース` で Spotlight検索を表示
defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys -dict-add 64 "<dict><key>enabled</key><false/></dict>"
## `⌥⌘スペース` で Finderの検索ウィンドウを表示
defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys -dict-add 65 "<dict><key>enabled</key><false/></dict>"
## `^スペース` で前の入力ソースを選択
defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys -dict-add 60 "<dict><key>enabled</key><false/></dict>"
## `^⌥スペース` で入力メニューの次のソースを選択
defaults write com.apple.symbolichotkeys AppleSymbolicHotKeys -dict-add 61 "<dict><key>enabled</key><false/></dict>"

# キーボード長押し時に特殊文字ポップアップを無効にする（長押しでキーリピートするようにする）
defaults write -g ApplePressAndHoldEnabled -bool false

# Dock
## 自動的に表示/非表示にする
defaults write com.apple.dock autohide -bool true
## 拡大を最大値に設定する
defaults write com.apple.dock magnification -bool true
defaults write com.apple.dock largesize -int 128
## 最近使用したアプリを表示しない
defaults write com.apple.dock show-recents -bool false
killall Dock # 反映

# .DS_Store を作らない
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool True
killall Finder # 反映

# 普段利用するアプリ
brew install google-chrome
brew install google-chrome@beta
brew install raycast
brew install slack
brew install discord
brew install karabiner-elements
brew install anki
brew install iina
brew install logi-options+
brew install obs
brew install vlc
brew install the-unarchiver
brew install elgato-stream-deck
brew install wpsoffice
brew install --cask warp   # --cask を省略できるが warp という名前の Formula が追加されたらつらいので明示的につける
brew install --cask docker # --cask をつけると Docker Desktop CE (含む docker コマンド類)がインストールされる
brew install --cask tailscale # --cask をつけると tailscale ランタイムだけでなく App がインストールされる
brew install --cask cryptomator
brew install --cask google-drive
brew install --cask postman
brew install --cask vial
brew install mas # App Store のアプリを CLI で管理できる
mas install 302584613 # Kindle
mas install 1289583905 # Pixelmator Pro
mas install 6714467650 # Perplexity (LINEMOで無料の間だけ使う)
mas install 1258530160 # Focus To-DO ※お試し

## for Kindle Comic Converter
brew install p7zip
brew install unar
brew install --cask kindle-previewer
brew install --cask kindle-comic-converter

# 以下は apple silicon 非対応なのでインストールしない
## - skitch
## - Google 日本語入力

# 開発環境
brew install mise
brew install biome
brew install ngrok
brew install firebase-cli
brew install awscli
brew install gh
brew install glab
brew install gitlab-runner
brew install google-cloud-sdk
brew install visual-studio-code
brew install cursor
brew install android-studio
brew install webstorm
brew install phpstorm
brew install sqlite
brew install figma
brew install tableplus
brew install ripgrep
brew install eza
brew install --cask lm-studio
brew install --cask claude-code
brew install uv
brew install ffmpeg
brew install libpg
brew install huggingface-cli
brew install duckdb
brew install cmake # for whisper.cpp
brew install sqldef/sqldef/psqldef
brew install sqldef/sqldef/sqlite3def
mas install 497799835 # Xcodes
# brew install sublime-text # 軽いエディタが使いたい時にあると便利かも。もはや無くてもいいかも？

# 言語系
brew install herd # php + laravel herd だけど、本当は mise で管理したい
brew install libyaml # mise で ruby をインストールする際に psych のコンパイルでエラーにならないようにするため

# 各種設定ファイルをコピーする
mkdir -p ~/.config

mkdir -p ~/.config/git
ln -s "$(pwd)/.config/git/ignore" ~/.config/git/ignore

mkdir -p ~/.config/mise
ln -s "$(pwd)/.config/mise/config.toml" ~/.config/mise/config.toml

mkdir -p ~/.config/karabiner
ln -s "$(pwd)/.config/karabiner/karabiner.json" ~/.config/karabiner/karabiner.json

mkdir -p ~/.claude
ln -s "$(pwd)/.claude/settings.json" ~/.claude/settings.json
ln -s "$(pwd)/.claude/CLAUDE.md" ~/.claude/CLAUDE.md
ln -s "$(pwd)/.claude/commands" ~/.claude/commands
ln -s "$(pwd)/.claude/hooks" ~/.claude/hooks
ln -s "$(pwd)/.claude/scripts" ~/.claude/scripts
ln -s "$(pwd)/.claude/skills" ~/.claude/skills

mkdir -p ~/.codex
ln -s "$(pwd)/.codex/prompts" ~/.codex/prompts

mkdir -p ~/.gemini
ln -s "$(pwd)/.gemini/settings.json" ~/.gemini/settings.json
ln -s "$(pwd)/.gemini/commands" ~/.gemini/commands

mv ~/.zshrc ~/.zshrc.orig
ln -s "$(pwd)/.zshrc" ~/.zshrc

# mise のセットアップ
# mise install # ~/.config/mise/config.toml をコピーしてから mise install を実行する
echo 'eval "$(mise activate)"' >> ~/.zshrc

# git
git config --global user.name "aliyome"
git config --global user.email "aliyome@gmail.com"

# ssh
mkdir ~/.ssh
chmod 700 ~/.ssh
cd ~/.ssh
ssh-keygen -t ed25519 -C "aliyome@gmail.com"
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
ssh-add ~/.ssh/id_ed25519
touch ~/.ssh/config
chmod 600 ~/.ssh/config

# Homebrew でインストールできないツールのセットアップ
sudo mkdir /opt/bin

# 手動でセットアップが必要
echo "ScanSnap Home"
echo "XP-Pen"
echo "Control + space 入力ソースを変更するキーボードショートカットを無効にする"
echo "キーボードで、音声入力のショートカットをオフにする"
echo "キーボードで、スペースバーを2回押してピリオドを入力をオフにする"
echo "テキスト入力で、「Windows風のキー操作」をオンにする"
echo "トラックパッドで、「タップでクリック」をオンにする"
echo "Karabiner-Elements で .config/karabiner を上書きする"
echo "Raycast で *.rayconfig をインポートする"
echo "Warp の設定を行う"
echo "DMMブックスアプリをインストールする<https://book.dmm.com/info_bookviewer.html>"
echo "VSCode の設定ファイルをコピーする"
