#!/usr/bin/env bash

langs="js lua python"
utils="jq awk sed sort find"

selec=`printf "$langs $utils" | tr ' ' '\n' | sort -r | fzf --preview "curl cht.sh/{} -s"`

if echo $langs | grep "$selec"; then
  printf 'Lang query: '
  read query
  curl cht.sh/$selec/`echo $query | tr ' ' '+'` -s | less -r
else
  curl cht.sh/$selec | less -r
fi
