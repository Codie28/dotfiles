# this only gets run on ttys (?)
# after this `$ZDOTDIR` gets set to `$HOME/.config/zsh`

# Lets hope this doesnt shoot me in the groin in couple of weeks
export ZDOTDIR=~/.config/zsh

if [[ $(tty) == '/dev/tty1' ]] then
  $HOME/.bin/x
fi

if [[ $(tty) == '/dev/tty2' ]] then
  Hyprland
fi
