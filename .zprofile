# this only gets run on ttys (?)
# after this `$ZDOTDIR` gets set to `$HOME/.config/zsh`

# Lets hope this doesnt shoot me in the groin in couple of weeks
# xxx: it fucking did
export ZDOTDIR=$HOME/.config/zsh

if [[ $(tty) == '/dev/tty1' ]] then
  # TODO: replcae `dots` with a better solution
  
  while true; do
  $HOME/dots/mybin/wmstart
  done
fi

# ttys suck
# better not do this and sign out then login again
# source $HOME/.config/zsh/.zshrc
