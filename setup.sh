#!/bin/bash

# 参考元: [Macを買い替えたら、まず実行するセットアップのスクリプトがこちらです](https://zenn.dev/ageless/articles/a930f7fba9fe21)

# homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'export HOMEBREW_PREFIX="/opt/homebrew"' >> ~/.zshrc
echo 'export HOMEBREW_CELLAR="/opt/homebrew/Cellar"' >> ~/.zshrc
echo 'export HOMEBREW_REPOSITORY="/opt/homebrew"' >> ~/.zshrc
echo 'export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"' >> ~/.zshrc
echo 'export MANPATH="/opt/homebrew/share/man:${MANPATH:-}"' >> ~/.zshrc
echo 'export INFOPATH="/opt/homebrew/share/info:${INFOPATH:-}"' >> ~/.zshrc
source ~/.zshrc

# mac の softwareupdate を使って rosetta をインストール
softwareupdate --install-rosetta --agree-to-license

# キーボードの反応速度の修正(PC再起動後に有効化される)
defaults write -g InitialKeyRepeat -int 15
defaults write -g KeyRepeat -int 2

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
brew install mas # App Store のアプリを CLI で管理できる
mas install 302584613 # Kindle
mas install 1289583905 # Pixelmator Pro
mas install 1455702185 # ComicViewer 2
# brew install --cask the-unarchiver # 現代の macOS には不要かも

# 以下は apple silicon 非対応なのでインストールしない
## - skitch
## - Google 日本語入力

# 開発環境
brew install iterm2
# brew install fish  # せっかくの新環境なので fish をやめて zsh + warp を試す
brew install mise
brew install ngrok
brew install tailscale
brew install firebase-cli
brew install awscli
brew install google-cloud-sdk
brew install visual-studio-code
brew install cursor
brew install android-studio
brew install xcodes
brew install webstorm
brew install sublime-text # 軽いエディタが使いたい時にあると便利かも。もはや無くてもいいかも？
brew install sqlite
brew install figma
brew install tableplus
brew install terraform
# brew install docker # Docker Desktop CE がインストール済みなので不要

# 言語系
brew install golang
brew install rustup
brew install deno
brew install node
brew install yarn  # 1.x
brew install oven-sh/bun/bun
brew install herd # php + laravel herd

# セットアップ
mise use -g node@lts
rustup-init

## NOTE: デフォルトシェルは変えずに、必要な時に `fish` を使う運用
## デフォルトシェルとして fish を追加
# echo $(which fish) | sudo tee -a /etc/shells
# chsh -s $(which fish)
# git

mkdir ~/.ssh
chmod 700 ~/.ssh
cd ~/.ssh
ssh-keygen -t ed25519 -C "aliyome@gmail.com"
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
ssh-add ~/.ssh/id_ed25519
touch ~/.ssh/config
chmod 600 ~/.ssh/config
cat <<<EOF >> ~/.ssh/config
Host github
	HostName github.com
	User aliyome
	PreferredAuthentications publickey
	IdentityFile ~/.ssh/id_ed25519
	UseKeychain yes
	AddKeysToAgent yes
	Port 22
EOF

# もしgitが上手くいかなかったら↓を試す
# xcode-select --install # Xcode のコマンドラインツール(git など)のインストール
# 現代の homebrew は xcode を勝手にインストールしてくれるから不要のはず

# 手動でセットアップが必要
echo "ScanSnap Home"
echo "XP-Pen"

