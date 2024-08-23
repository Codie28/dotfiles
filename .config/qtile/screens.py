from libqtile import bar, widget
from libqtile.config import Screen, ScratchPad

from style import (
    COLORS,
    COLORSCHEME,
    FONT
)

screens = [
    Screen(
        top=bar.Gap(size=40),
    ),
    Screen(
        left=bar.Gap(size=280),
    )
]

