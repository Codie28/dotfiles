eval "$(zoxide init zsh)"
eval "$(oh-my-posh init zsh --config $HOME/.config/ohmyposh/lean.toml)"

# source ~/.local/share/lscolors.sh
eval "$(dircolors)"

alias ls="ls --color=auto"
alias ll="ls -lA"
alias la="ls -a"

alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias diff='diff --color=auto'
alias ip='ip --color=auto'

# Godot
alias godot="godot --rendering-driver opengl3"

#List Symlinks
alias lsym="ls -la | grep '\->'"

alias tmux="tmux -f ~/.config/tmux/tmux.conf"

export EDITOR="nvim"
export PAGER="less"

[[ -d $HOME/.bin ]] && export PATH=$HOME/.bin:$PATH

# BREWW
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
