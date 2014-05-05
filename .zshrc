# forked from https://github.com/bpymasinn/Config/.zshrc
# (d) is default on

# ------------------------------
# General Settings
# ------------------------------
export EDITOR=vim        # �G�f�B�^��vim�ɐݒ�
export LANG=ja_JP.UTF-8  # �����R�[�h��UTF-8�ɐݒ�
export KCODE=u           # KCODE��UTF-8��ݒ�
export AUTOFEATURE=true  # autotest��feature�𓮂���

bindkey -v              # �L�[�o�C���h��vi���[�h�ɐݒ�

setopt auto_pushd        # cd���Ƀf�B���N�g���X�^�b�N��pushd����
#setopt correct           # �R�}���h�̃X�y�����������
setopt prompt_subst      # �v�����v�g��`���ŕϐ��u����R�}���h�u��������
setopt notify            # �o�b�N�O���E���h�W���u�̏�ԕω��𑦎��񍐂���
#setopt equals            # =command��`which command`�Ɠ��������ɂ���

### Complement ###
autoload -U compinit; compinit # �⊮�@�\��L���ɂ���
setopt auto_list               # �⊮�����ꗗ�ŕ\������(d)
setopt auto_menu               # �⊮�L�[�A�łŕ⊮�������ɕ\������(d)
setopt list_packed             # �⊮�����ł��邾���l�߂ĕ\������
setopt list_types              # �⊮���Ƀt�@�C���̎�ނ��\������
bindkey "^[[Z" reverse-menu-complete  # Shift-Tab�ŕ⊮�����t������("\e[Z"�ł����삷��)
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}' # �⊮���ɑ啶������������ʂ��Ȃ�

### History ###
HISTFILE=~/.zsh_history   # �q�X�g����ۑ�����t�@�C��
HISTSIZE=10000            # �������ɕۑ������q�X�g���̌���
SAVEHIST=10000            # �ۑ������q�X�g���̌���
setopt bang_hist          # !���g�����q�X�g���W�J���s��(d)
setopt extended_history   # �q�X�g���Ɏ��s���Ԃ��ۑ�����
setopt hist_ignore_dups   # ���O�Ɠ����R�}���h�̓q�X�g���ɒǉ����Ȃ�
setopt share_history      # ���̃V�F���̃q�X�g�������A���^�C���ŋ��L����
setopt hist_reduce_blanks # �]���ȃX�y�[�X���폜���ăq�X�g���ɕۑ�����

# �}�b�`�����R�}���h�̃q�X�g����\���ł���悤�ɂ���
autoload history-search-end
zle -N history-beginning-search-backward-end history-search-end
zle -N history-beginning-search-forward-end history-search-end
bindkey "^P" history-beginning-search-backward-end
bindkey "^N" history-beginning-search-forward-end

# ���ׂẴq�X�g����\������
function history-all { history -E 1 }

# ------------------------------
# Look And Feel Settings
# ------------------------------
### Ls Color ###
# �F�̐ݒ�
export LSCOLORS=Exfxcxdxbxegedabagacad
# �⊮���̐F�̐ݒ�
export LS_COLORS='di=01;34:ln=01;35:so=01;32:ex=01;31:bd=46;34:cd=43;34:su=41;30:sg=46;30:tw=42;30:ow=43;30'
# ZLS_COLORS�Ƃ́H
export ZLS_COLORS=$LS_COLORS
# ls�R�}���h���A�����ŐF����(ls -G�̂悤�Ȃ��́H)
export CLICOLOR=true
# �⊮���ɐF��t����
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}

### Prompt ###
# �v�����v�g�ɐF��t����
autoload -U colors; colors
# ��ʃ��[�U��
tmp_prompt="%F{cyan}[%n@%D{%m/%d %T}]%f "
#tmp_prompt="%{${fg[cyan]}%}%n%# %{${reset_color}%}"
tmp_prompt2="%{${fg[cyan]}%}%_> %{${reset_color}%}"
tmp_rprompt="%{${fg[green]}%}[%~]%{${reset_color}%}"
tmp_sprompt="%{${fg[yellow]}%}%r is correct? [Yes, No, Abort, Edit]:%{${reset_color}%}"

# root���[�U��(�����ɂ��A�A���_�[�o�[������)
if [ ${UID} -eq 0 ]; then
  tmp_prompt="%B%U${tmp_prompt}%u%b"
  tmp_prompt2="%B%U${tmp_prompt2}%u%b"
  tmp_rprompt="%B%U${tmp_rprompt}%u%b"
  tmp_sprompt="%B%U${tmp_sprompt}%u%b"
fi

PROMPT=$tmp_prompt    # �ʏ�̃v�����v�g
PROMPT2=$tmp_prompt2  # �Z�J���_���̃v�����v�g(�R�}���h��2�s�ȏ�̎��ɕ\�������)
RPROMPT=$tmp_rprompt  # �E���̃v�����v�g
SPROMPT=$tmp_sprompt  # �X�y�������p�v�����v�g
# SSH���O�C�����̃v�����v�g
[ -n "${REMOTEHOST}${SSH_CONNECTION}" ] &&
  PROMPT="%{${fg[white]}%}${HOST%%.*} ${PROMPT}"
;

#Title
precmd() {
    [[ -t 1 ]] || return
    case $TERM in
        *xterm*|rxvt|(dt|k|E)term)
        print -Pn "\e]2;[%~]\a"
	;;
        # screen)
        #      #print -Pn "\e]0;[%n@%m %~] [%l]\a"
        #      print -Pn "\e]0;[%n@%m %~]\a"
        #      ;;
    esac
}


# ------------------------------
# Other Settings
# ------------------------------

### Aliases ###
#������\��������
alias history='history -E'

# cd�R�}���h���s��Als�����s����
function cd() {
  builtin cd $@ && ls;
}