# hai :3

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, MODify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os.path

ALT  = "mod1"
NUM  = "mod2" 

MOD  = "mod4"
ALTG = "mod5"
CTRL = "control"
SFT  = "shift"
LOCK = "lock"

TERM      = "alacritty"
EDITOR    = "nvim"
BROWSER   = "firefox"
EXPLORER  = "thunar"
WPMGR     = "nitrogen"
SOUNDMGR  = "alsamixer"
APP_LNCHR = "myrofi"

FONT = "JetBrainsMono Nerd Font"

colors = []
cache= os.path.expanduser('~/.cache/wal/colors')
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(16):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)

border_focus   = colors[2]
border_normal  = colors[9]

bar_border     = colors[3]

group_active   = colors[4]
group_inactive = "a0a0a0" # colors[8]


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([MOD, SFT], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([MOD, SFT], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([MOD, SFT], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, SFT], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([MOD, CTRL], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([MOD, CTRL], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([MOD, CTRL], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD, CTRL], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([MOD], "d", lazy.layout.normalize(), desc=""),

    Key([MOD, SFT], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    Key([MOD], "Return", lazy.spawn(TERM), desc="Launch terminal"),
    Key([MOD], "space", lazy.spawn(APP_LNCHR), desc="Open app launcher"),

    Key([MOD, ALT], "v", lazy.spawn(f"{TERM} -e {EDITOR}"), desc="Open editor in terminal"),
    Key([MOD, ALT], "b", lazy.spawn(BROWSER), desc="Open browser"),
    Key([MOD, ALT], "e", lazy.spawn(EXPLORER), desc="Open file explorer"),
    Key([MOD, ALT], "w", lazy.spawn(WPMGR), desc="Open wallpaper manager"),
    Key([MOD, ALT], "s", lazy.spawn(f"{TERM} -e {SOUNDMGR}"), desc="Open sound mixer in terminal"),

    Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([MOD], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([MOD, CTRL], "r", lazy.reload_config(), desc="Reload the config"),

    Key([MOD, CTRL], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([MOD], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = (
    Group('1', label=' DEV', layout='monadtall'),
    Group('2', label='󰖟 WWW', layout='monadtall'),
    Group('3', label=' SYS', layout='monadtall'),
    Group('4', label=' MUS', layout='monadwide'),
    Group('5', label=' SOC', layout='monadwide'),
)

for i, group in enumerate(groups, 1):
    keys.append(Key([MOD], str(i), lazy.group[group.name].toscreen()))
    keys.append(Key([MOD, SFT], str(i), lazy.window.togroup(group.name)))

layout_theme = {
    "border_width": 1,
    "margin": 9,
    "border_focus":  border_focus,
    "border_normal": border_normal,
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

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    fontsize=18,
                    fmt="<b>| <i>{}</i> |</b>",
                    foreground="f0d1f0"
                ),
                widget.GroupBox(
                    fontsize=18,
                    font=FONT,
                    spacing=5,
                    disable_drag=True,
                    active=group_active,
                    inactive=group_inactive,
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
            border_color = [bar_border, bar_border, bar_border, bar_border],
            border_width = [1, 1, 1, 1],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
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
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
