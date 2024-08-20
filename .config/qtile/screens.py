from libqtile import bar, widget
from libqtile.config import Screen, ScratchPad

from style import (
    COLORS,
    COLORSCHEME,
    FONT
)

screens = [
    Screen(
        top=bar.Gap(size=40)
    ),
    Screen(
        bottom=bar.Bar(
            [
                # widget.WindowName(),
                widget.GroupBox()
            ],
            size=24
        )
#       top=bar.Bar(
#           [
#               widget.CurrentLayout(
#                   font=FONT,
#                   fontsize=18,
#                   fmt="<b><i>{}</i></b>",
#                   foreground=COLORS["layout_text"][COLORSCHEME]
#               ),
#               widget.GroupBox(
#                   font=FONT,
#                   fontsize=26,
#                   spacing=3,
#                   disable_drag=True,
#                   highlight_method="text",
#                   highlight_color= ["0f0", "00f"],
#                   background="00000000",
#                   margin_x=1,
#                   margin_y=3,
#                   padding_x=1,
#                   padding_y=7,
#                   active=COLORS["this_monitor_unselected_screen_active"][COLORSCHEME],
#                   inactive=COLORS["this_monitor_unselected_screen_inactive"][COLORSCHEME],
#                   this_current_screen_border=COLORS["this_monitor_selected_screen_active"][COLORSCHEME],
#                 # NOTE: this is prep for qtile/qtile/issues/1243
#                 # current_screen_inactive=["this_monitor_selected_screen_inactive"][COLORSCHEME],
#                 # this_current_screen_active=["this_monitor_unselected_screens_active"][COLORSCHEME],
#                 # this_current_screen_inactive=["this_monitor_unselected_screens_inactive"][COLORSCHEME],
#                 # other_current_screen_active=["other_monitor_selected_screen_active"][COLORSCHEME],
#                 # other_current_screen_inactive=["other_monitor_selected_screen_inactive"][COLORSCHEME],
#                 # other_screen_active=["other_monitor_unselected_screens_active"][COLORSCHEME],
#                 # other_screen_inactive=["other_monitor_unselected_screens_inactive"][COLORSCHEME],
#                 urgent_alert_method="line",
#                 urgent_border = "ff110a",
#                 urgen_text = "f00"
#               ),
#               widget.Prompt(),
#               widget.Spacer(),
#               widget.WindowName(),
#               widget.Spacer(),
#               widget.Chord(
#                   chords_colors={
#                       "launch": ("#ff0000", "#ffffff"),
#                   },
#                   name_transform=lambda name: name.upper(),
#               ),
#               widget.Battery(
#                   font=FONT,
#                   fontsize=26,
#                   update_interval=1,
#                   format="{char}",
#                   full_char         = "󰁹",
#                   empty_char        = "󰂎",
#                   not_charging_char = "󱟩",
#                   charge_char       = "󱟡",
#                   discharge_char    = "󱟟",
#                   unknown_char      = "󰂑",
#                   foreground=COLORS["battery_char"][COLORSCHEME],
#                   low_foreground=COLORS["battery_char_low"][COLORSCHEME],
#                   low_percentage=0.2
#               ),
#               widget.Battery(
#                   format="{percent:0.1%}",
#                   update_interval=1,
#                   foreground=COLORS["battery_percentage_text"][COLORSCHEME],
#                   low_foreground=COLORS["battery_percentage_low_text"][COLORSCHEME],
#                   low_percentage=0.2
#               ),
#               widget.Clock(
#                   format="%Y %m %d %a [ %H:%M ]",
#                   foreground=COLORS["clock_text"][COLORSCHEME]
#               ),
#           ],
#           30,
#           background="00000000",
#           margin= [6, 9, 6, 9],
#           border_color = [COLORS["bar_border"][COLORSCHEME], COLORS["bar_border"][COLORSCHEME], COLORS["bar_border"][COLORSCHEME], COLORS["bar_border"][COLORSCHEME]],
#           border_width = [1, 1, 1, 1],
#       ),
    ),
]

