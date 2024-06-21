#!/usr/bin/env bash

langs=`echo "c cpp lua js nodejs gleam" | tr ' ' '\n'` 
cutils=`echo "jq awk sed sort TODO-ADD-MORE-CUTILS" | tr ' ' '\n'`

selec=`printf "$langs\n$cutils" | sort -r | fzf`
printf "Selected: $selec\n"
read -p "Query: " query

if echo $langs | grep -qs $selec; then
  query=`echo $query | tr ' ' '+'`
  tmux neww bash -c "curl cht.sh/$selected/$query & while [ : ]; do sleep 1; done"
else
  tmux neww bash -c "curl -s cht.sh/$selected~$query | less"
fi
