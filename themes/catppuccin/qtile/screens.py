from libqtile import bar, widget
from libqtile.config import Screen, ScratchPad, Bar

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
        left=bar.Gap(size=266),
    )
]

