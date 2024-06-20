#!/usr/bin/env bash

langs=`echo "c cpp lua js nodejs gleam" | tr ' ' '\n'` 
cutils=`echo "jq awk sed sort TODO-ADD-MORE-CUTILS" | tr ' ' '\n'`

selec=`printf "$langs\n$cutils" | sort -r |fzf`
printf "Selected: $selec\n"
read -p "Query: " query

if echo $langs | grep -qs $selec; then
  curl cht.sh/$selec/`echo $query | tr ' ' '+'`
else
  curl cht.sh/$selec~$query
fi
