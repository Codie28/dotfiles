from catppuccin import PALETTE

FONT = "MesloLGS Nerd Font Mono"
COLORSCHEME = 1
# 0: LIGHT
# 1: DARK

LIGHT = PALETTE.latte.colors
DARK  = PALETTE.frappe.colors
#                     LIGHT               DARK
COLORS = {
    "win_border_normal" : [ LIGHT.overlay0.hex, DARK.overlay1.hex ],
    "win_border_focus"  : [ LIGHT.base.hex,     DARK.base.hex ],
    "bar_border"        : [ LIGHT.lavender.hex, DARK.lavender.hex ],
    "group_active"      : [ LIGHT.peach.hex,    DARK.peach.hex ],
    "group_inactive"    : [ "a0a0a0",           DARK.rosewater.hex ],
    "layout"            : [ LIGHT.sky.hex,      DARK.yellow.hex ],
}
