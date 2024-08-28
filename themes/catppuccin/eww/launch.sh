#!/usr/bin/env bash

SECONDARY="$HOME/.config/eww/secondary"
DASHBOARD="$HOME/.config/eww/dashboard"

CURRENT=`cat $QTILE_THEME_HOME/.ewwmode`
SCREEN=1

case "$1" in
  'secondary') m=$1 ;;
  'dashboard') m=$1 ;;
  'same') m=$CURRENT ;;
  *)
    case "$CURRENT" in
      'secondary') m='dashboard';;
      'dashboard') m='secondary';;
      *)
        echo no config selected seting to secondary
        m='secondary'
        ;;
    esac
    ;;
esac

echo m is $m
echo $m > $QTILE_THEME_HOME/.ewwmode

case "$m" in
  'secondary')
    eww -c $SECONDARY  --restart open --screen $SCREEN bonsai
    eww -c $SECONDARY open --screen $SCREEN calender
    eww -c $SECONDARY open --screen $SCREEN multibox
    eww -c $SECONDARY open --screen $SCREEN split1
    eww -c $SECONDARY open --screen $SCREEN split2
    ;;
  'dashboard')
    eww -c $DASHBOARD --restart open --screen $SCREEN dashboard 
    ;;
  *)
    echo invalid \$m how the fuck that happened
    exit
    ;;
esac
