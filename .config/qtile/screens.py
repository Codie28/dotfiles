from libqtile import bar, widget
from libqtile.config import Screen, ScratchPad

from style import (
    COLORS,
    COLORSCHEME,
    FONT
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    fontsize=18,
                    fmt="<b><i>{}</i></b>",
                    foreground=COLORS["layout"][COLORSCHEME]
                ),
                widget.GroupBox(
                    fontsize=24,
                    font=FONT,
                    spacing=5,
                    disable_drag=True,
                    active=COLORS["group_active"][COLORSCHEME],
                    inactive=COLORS["group_inactive"][COLORSCHEME],
                    rounded=True,
                    highlight_method="block",
                    this_current_screen_border="daccda3a",
                    this_screen_border="0000000",
                    other_current_screen_border="00000000",
                    other_screen_border="00000000",
                    background="00000000",
                    margin_x=1,
                    margin_y=3,
                    padding_x=1,
                    padding_y=7,
                ),
                widget.Prompt(),
                widget.Spacer(),
                widget.WindowName(),
                widget.Spacer(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Clock(format="%Y %m %d %a [ %H:%M ]"),
            ],
            30,
            background="00000000",
            margin= [6, 9, 6, 9],
            border_color = [COLORS["bar_border"][COLORSCHEME], COLORS["bar_border"][COLORSCHEME], COLORS["bar_border"][COLORSCHEME], COLORS["bar_border"][COLORSCHEME]],
            border_width = [1, 1, 1, 1],
        ),
    ),
]

