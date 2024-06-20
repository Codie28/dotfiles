eval "$(zoxide init zsh)"
eval "$(oh-my-posh init zsh --config $HOME/.config/ohmyposh/lean.toml)"

export LS_COLORS="$LS_COLORS:ow=30;44:" # fix ls color for folders with 777 permissions

if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    export LS_COLORS="$LS_COLORS:ow=30;44:"


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

EDITOR="nvim"

[[ -d $HOME/.bin ]] && export PATH=$HOME/.bin:$PATH

# neofetch
