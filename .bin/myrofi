#!/bin/bash

if [[ -z $1 ]] then
  MODE="app"
else
  MODE=$1
fi

case $MODE in
  "app")
    rofi -show drun -matching fuzzy
  ;;
  "ssh")
  ;;
  "psw")
    bwmenu
  ;;
  "win")
    rofi -show window
  ;;
esac

