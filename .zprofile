# this only gets run on ttys (?)
# after this `$ZDOTDIR` gets set to `$HOME/.config/zsh`

# Lets hope this doesnt shoot me in the groin in couple of weeks
# xxx: it fucking did
export ZDOTDIR=$HOME/.config/zsh

if [[ $(tty) == '/dev/tty1' ]] then
  $HOME/mybin/x
fi

if [[ $(tty) == '/dev/tty2' ]] then
  Hyprland
fi

# ttys suck
source $HOME/.config/zsh/.zshrc
