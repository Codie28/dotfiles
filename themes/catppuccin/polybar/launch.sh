#!/bin/bash

# Terminate already running bar instances
killall -q polybar
# If all your bars have ipc enabled, you can also use
# polybar-msg cmd quit

# if type "xrandr"; then
#   for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
#     echo "Polybar launched on $m..."
#     MONITOR=$m polybar top 2>&1 | tee -a /tmp/polybar.log & disown
#   done
# else
  echo "Polybar launched..."
  polybar top 2>&1 | tee -a /tmp/polybar.log & disown
# fi
