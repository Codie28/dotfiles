# This runs on tmux sessions

# function nb_sesh() {
#   # tmux neww nb shell
#   # tmux renamew -t @2 "journal"
#   nb shell
# }
#
# session=`tmux ls | grep "session" | awk -F ":" '{print $1}'`
#
# case $session; in
#   "notebook" ) nb_sesh ;;
#   "weechat"  ) weechat ;;
#   *          ) v       ;;
# esac

v
