# hai :3

from libqtile.config import Group, Match

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
from layouts import (
    layouts,
    floating_layout
)

# NOTE: polybar uses xworkspace name???
# label as the key ig
groups = (
    Group('', label='1',
          layout='monadtall',
          screen_affinity=0
    ),
    Group('󰖟', label='2',
          layout='treetab',
          screen_affinity=0,
          matches=[
              Match(wm_class="firefox"),
              Match(wm_class="zen-alpha")
          ],
    ),
    Group('', label='3',
          layout='monadtall',
          screen_affinity=0
    ),
    Group('', label='4',
          layout='monadtall',
          screen_affinity=0
    ),

    # Second monitor
    Group('z', label='z',
          layout='monadtall',
          screen_affinity=1
    ),
    Group('', label='x',
          layout='monadtall',
          screen_affinity=1,
          matches=[
              Match(wm_class="Spotify"),
              Match(wm_class="nuclear")
          ],
    ),
    Group('󱅯', label='c',
          layout='monadtall',
          screen_affinity=1,
          matches=[
              Match(wm_class="vesktop")
          ],
    ),
    Group('󰠮', label='n',
          layout='monadtall',
          screen_affinity=1,
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
