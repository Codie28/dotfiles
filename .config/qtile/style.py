from catppuccin import PALETTE
import os
from libqtile.log_utils import logger

FONT = "MesloLGS Nerd Font Mono"
# 0: LIGHT
# 1: DARK
with open(os.path.expanduser('~/.colorscheme')) as f:
    file = f.read().split('\n')
    COLORSCHEME = 1 if file[0] == 'dark' else 0

LIGHT = PALETTE.latte.colors
DARK  = PALETTE.frappe.colors
#                                                  LIGHT                DARK
COLORS = {
    "win_border_normal"                        : [ LIGHT.crust.hex,     DARK.base.hex ],
    "win_border_focus"                         : [ LIGHT.base.hex,      DARK.overlay1.hex ],
    "bar_border"                               : [ LIGHT.lavender.hex,  DARK.lavender.hex ],

  # "layout_text"                              : [ LIGHT.maroon.hex,    DARK.yellow.hex ],
  # "clock_text"                               : [ LIGHT.text.hex,      DARK.text.hex ],

  # "battery_percentage_text"                  : [ LIGHT.text.hex,      DARK.text.hex ],
  # "battery_percentage_low_text"              : [ LIGHT.red.hex,       DARK.red.hex ],
  # "battery_char"                             : [ LIGHT.green.hex,     DARK.green.hex ],
  # "battery_char_low"                         : [ LIGHT.red.hex,       DARK.red.hex ],

  # # NOTE: this is prep for qtile/qtile/issues/1243
  # # CUrrently selected v
  # "this_monitor_selected_screen_active"      : [ LIGHT.mauve.hex,     DARK.mauve.hex ],
  # "this_monitor_selected_screen_inactive"    : [ "a0a0a0",            DARK.rosewater.hex ],
  # "this_monitor_unselected_screen_active"    : [ LIGHT.teal.hex,      DARK.peach.hex ],     
  # "this_monitor_unselected_screen_inactive"  : [ "4c4c4c",            DARK.rosewater.hex ],

  # "other_monitor_selected_screen_active"     : [ LIGHT..hex,   DARK..hex ],
  # "other_monitor_selected_screen_inactive"   : [ LIGHT..hex,   DARK..hex ],
  # "other_monitor_unselected_screen_active"   : [ LIGHT..hex,   DARK..hex ],
  # "other_monitor_unselected_screen_inactive" : [ LIGHT..hex,   DARK..hex ],
}
