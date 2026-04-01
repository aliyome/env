#!/bin/bash

# 参考元: [Macを買い替えたら、まず実行するセットアップのスクリプトがこちらです](https://zenn.dev/ageless/articles/a930f7fba9fe21)

# homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo >> ~/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
ln -s "$(pwd)/.Brewfile" ~/.Brewfile
brew bundle --global

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

# Homebrew でインストールできないアプリを mas でインストールする
mas install 497799835 # Xcodes
mas install 302584613 # Kindle
mas install 1289583905 # Pixelmator Pro
mas install 1258530160 # Focus To-DO

# 各種設定ファイルをコピーする
mkdir -p ~/.config

mkdir -p ~/.config/git
ln -s "$(pwd)/.config/git/ignore" ~/.config/git/ignore
ln -s "$(pwd)/.config/git/config" ~/.config/git/config

mkdir -p ~/.config/tmux
ln -s "$(pwd)/.config/tmux/tmux.conf" ~/.config/tmux/tmux.conf

mkdir -p ~/.config/mise
ln -s "$(pwd)/.config/mise/config.toml" ~/.config/mise/config.toml

mkdir -p ~/.config/karabiner
ln -s "$(pwd)/.config/karabiner/karabiner.json" ~/.config/karabiner/karabiner.json

mv ~/.zshrc ~/.zshrc.orig
ln -s "$(pwd)/.zshrc" ~/.zshrc

ln -s "$(pwd)/.bunfig.toml" ~/.bunfig.toml

# 各種設定
echo "min-release-age=7  # 7日" >> ~/.npmrc
echo "ignore-scripts=true" >> ~/.npmrc

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
echo "Warp のログインを行う"
echo "DMMブックスアプリをインストールする<https://book.dmm.com/info_bookviewer.html>"
echo "VSCode の設定ファイルをコピーする"
