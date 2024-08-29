export EDITOR="nvim"
export PAGER="less"

eval "$(zoxide init zsh)"
eval "$(oh-my-posh init zsh --config $HOME/.config/ohmyposh/lean.toml)"

eval "$(dircolors)"

# BREWW
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

ZINIT_HOME="$HOME/git/zinit/zinit.git"

if [ ! -d "$ZINIT_HOME" ]; then
   mkdir -p "$(dirname $ZINIT_HOME)"
   git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
fi

# Source/Load zinit
# source "${ZINIT_HOME}/zinit.zsh"


source $HOME/.config/zsh/alias.zsh
source $HOME/.config/zsh/path.zsh
source $HOME/.config/zsh/completion.zsh
