from libqtile import layout
from libqtile.config import Match

from style import (
    COLORS,
    COLORSCHEME,
    FONT
)

layouts = [
    layout.MonadTall(
        border_width=0,
        margin=10,
    ),
    layout.TreeTab(
        border_width=0,
        margin=10,
        font=FONT,
        bg_color=COLORS["treetab_bg"][COLORSCHEME],
        active_bg=COLORS["treetab_active_bg"][COLORSCHEME],
        active_fg=COLORS["treetab_active_fg"][COLORSCHEME],
        inactive_bg=COLORS["treetab_bg"][COLORSCHEME],
        inactive_fg=COLORS["treetab_fg"][COLORSCHEME],
        section_fg=COLORS["treetab_fg"][COLORSCHEME],
        urgent_fg=COLORS["treetab_urgent_fg"][COLORSCHEME],
        panel_width=230,
        place_right=True,
        sections=['uwu :3']
    ),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
