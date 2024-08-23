# hai :3

from libqtile import bar, layout, qtile, widget
from libqtile.config import Group, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.log_utils import logger

from style import (
    COLORS,
    COLORSCHEME,
    FONT
)
from keys import (
    keys,
    mouse,
    group_keys,
    TERM
)
from screens import screens


# NOTE: polybar uses xworkspace name???
# label as the key ig
groups = (
    Group('', label='1', layout='monadtall'),
    Group('󰖟', label='2', layout='monadtall',
          matches=[Match(wm_class="firefox")]
    ),
    Group('', label='3', layout='monadtall'),
    Group('', label='4', layout='monadwide'),

    # Second monitor
    Group('z', label='z', layout='monadtall'),
    Group('', label='x', layout='monadwide',
          matches=[Match(wm_class="Spotify")]
    ),
    Group('󱅯', label='c', layout='monadwide',
          matches=[Match(wm_class="discord")]
    ),
)

keys.extend(
    group_keys(groups)
)

#   groups = groups + (
#       ScratchPad("pad", [
#           DropDown("term", TERM,
#               opacity=1,
#               x=0.1, y=0,
#               width=0.8, height=0.6,
#           ),
#       ]),
#       # xxx: this ',' prevents the config from crashing
#   )

layout_theme = {
    "border_width": 0,
    "margin": 9,
}

layouts = [
    # layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

widget_defaults = dict(
    font=FONT,
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()


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
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = False
auto_minimize = False
focus_on_window_activation = "smart"
reconfigure_screens = False

wmname = "LG3D"
