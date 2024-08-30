add_to_path() {
  if [[ "$1" == "left" ]] then
    [[ -d $2 ]] && export PATH=$2:$PATH
  elif [[ "$1" == "right" ]] then
    [[ -d $2 ]] && export PATH=$PATH:$2
  fi
}

add_to_path left  $HOME/mybin
add_to_path right $HOME/.spicetify

# vim: set filetype=bash
