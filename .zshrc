eval "$(zoxide init zsh)"
eval "$(oh-my-posh init zsh --config $HOME/.config/ohmyposh/lean.toml)"

eval "$(dircolors)"

alias ls="ls --color=auto"
alias ll="ls -lA"
alias la="ls -a"

alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias diff='diff --color=auto'
alias ip='ip --color=auto'

#List Symlinks
alias lsym="ls -la | grep '\->'"

export EDITOR="nvim"
export PAGER="less"

# `wal` things
(cat ~/.cache/wal/sequences &)
source ~/.cache/wal/colors-tty.sh

[[ -d $HOME/.bin ]] && export PATH=$HOME/.bin:$PATH

if [[ -z $TMUX ]] then
 tmux
fi

# neofetch
