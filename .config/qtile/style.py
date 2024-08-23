from catppuccin import PALETTE
import os
from libqtile.log_utils import logger

FONT = "MesloLGS Nerd Font Mono"
# 0: LATTE
# 1: FRAPPE
with open(os.path.expanduser('~/.colorscheme')) as f:
    file = f.read().split('\n')
    # TODO: make it work with more then two themes
    COLORSCHEME = 1 if file[0] == 'frappe' else 0

LATTE  = PALETTE.latte.colors
FRAPPE = PALETTE.frappe.colors

#                                                  LATTE                FRAPPE 
COLORS = {
    "win_border_normal"                        : [ LATTE.base.hex,      FRAPPE.base.hex ],
    "win_border_focus"                         : [ LATTE.crust.hex,     FRAPPE.overlay1.hex ],
  # "bar_border"                               : [ LATTE.lavender.hex,  FRAPPE.lavender.hex ],

  # "layout_text"                              : [ LATTE.maroon.hex,    FRAPPE.yellow.hex ],
    "clock_text"                               : [ LATTE.text.hex,      FRAPPE.text.hex ],

    "battery_percentage_text"                  : [ LATTE.text.hex,      FRAPPE.text.hex ],
    "battery_percentage_low_text"              : [ LATTE.red.hex,       FRAPPE.red.hex ],
    "battery_char"                             : [ LATTE.green.hex,     FRAPPE.green.hex ],
    "battery_char_low"                         : [ LATTE.red.hex,       FRAPPE.red.hex ],

  # # NOTE: this is prep for qtile/qtile/issues/1243
  # # Currently selected v
  # "this_monitor_selected_screen_active"      : [ LATTE.mauve.hex,     FRAPPE.mauve.hex ],
  # "this_monitor_selected_screen_inactive"    : [ "a0a0a0",            FRAPPE.rosewater.hex ],
  # "this_monitor_unselected_screen_active"    : [ LATTE.teal.hex,      FRAPPE.peach.hex ],     
  # "this_monitor_unselected_screen_inactive"  : [ "4c4c4c",            FRAPPE.rosewater.hex ],

  # "other_monitor_selected_screen_active"     : [ LATTE..hex,   FRAPPE..hex ],
  # "other_monitor_selected_screen_inactive"   : [ LATTE..hex,   FRAPPE..hex ],
  # "other_monitor_unselected_screen_active"   : [ LATTE..hex,   FRAPPE..hex ],
  # "other_monitor_unselected_screen_inactive" : [ LATTE..hex,   FRAPPE..hex ],
}
