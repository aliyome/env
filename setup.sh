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

# Dock
## 自動的に表示/非表示にする
defaults write com.apple.dock autohide -bool true
## 拡大を最大値に設定する
defaults write com.apple.dock magnification -bool true
defaults write com.apple.dock largesize -int 128
## 最近使用したアプリを表示しない
defaults write com.apple.dock show-recents -bool false
killall Dock # 反映

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
brew install --cask warp   # --cask を省略できるが warp という名前の Formula が追加されたらつらいので明示的につける
brew install --cask docker # --cask をつけると docker ランタイムだけでなく Docker Desktop CE がインストールされる
brew install --cask tailscale # --cask をつけると tailscale ランタイムだけでなく App がインストールされる
brew install mas # App Store のアプリを CLI で管理できる
mas install 302584613 # Kindle
mas install 1289583905 # Pixelmator Pro
mas install 1455702185 # ComicViewer 2
# brew install --cask the-unarchiver # 現代の macOS には不要かも

# 以下は apple silicon 非対応なのでインストールしない
## - skitch
## - Google 日本語入力

# 開発環境
brew install mise
brew install ngrok
brew install firebase-cli
brew install awscli
brew install google-cloud-sdk
brew install visual-studio-code
brew install cursor
brew install android-studio
brew install xcodes
brew install webstorm
brew install sqlite
brew install figma
brew install tableplus
brew install terraform
# brew install docker # Docker Desktop CE がインストール済みなので不要
# brew install sublime-text # 軽いエディタが使いたい時にあると便利かも。もはや無くてもいいかも？

# 言語系
brew install herd # php + laravel herd
## 以下は mise で管理するため不要
# brew install rustup
# brew install golang
# brew install deno
# brew install node
# brew install yarn  # 1.x
# brew install oven-sh/bun/bun

# セットアップ
mise use -g node@lts # TODO: ~/.config/mise.toml を作る
mise use -g deno
mise use -g bun
mise use -g rust
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

# GitHub には ssh ではなく PAT を使って https でアクセスするため不要
# cat <<<EOF >> ~/.ssh/config
# Host github
# 	HostName github.com
# 	User aliyome
# 	PreferredAuthentications publickey
# 	IdentityFile ~/.ssh/id_ed25519
# 	UseKeychain yes
# 	AddKeysToAgent yes
# 	Port 22
# EOF

# 手動でセットアップが必要
echo "ScanSnap Home"
echo "XP-Pen"
echo "Control + space 入力ソースを変更するキーボードショートカットを無効にする"
echo "キーボードで、音声入力のショートカットをオフにする"
echo "テキスト入力で、「Windows風のキー操作」をオンにする"
echo "トラックパッドで、「タップでクリック」をオンにする"
echo "Karabiner-Elements で .config/karabiner を上書きする"
echo "Raycast で *.rayconfig をインポートする"
echo "Warp の設定を行う"
