#!/bin/bash

pkill lemonbar

lmb_text=`echo \#ffffccff`
# TODO replace ~/.config
~/.config/lemonbar/bar.sh | lemonbar -g 1920x40 -b -B \#00000000 -F $lmb_text -p &
