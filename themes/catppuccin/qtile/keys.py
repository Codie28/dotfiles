from libqtile.config import Key, KeyChord, Click, Drag 
from libqtile.lazy import lazy
import os

ALT  = "mod1"
MOD  = "mod4"
CTRL = "control"
SFT  = "shift"

TERM       = "kitty"
EDITOR     = "nvim"
BROWSER    = "zen-browser"
EXPLORER   = "thunar"
WPMGR      = "nitrogen"
SOUNDMGR   = "alsamixer"
MUSICPLYR  = "spotify-launcher"

NOTEAPP    = os.path.expanduser('~/mybin/cnb rofi')
NOTEDIR    = f'{TERM} -e {EDITOR} {os.path.expanduser('~/2ndbrain/')}'

THEMESWCHR = os.path.expanduser('~/mybin/switch cat')

APP_LNCHR = os.path.expanduser('.config/rofi/launch.sh') + " app"
SSH_LNCHR = os.path.expanduser('.config/rofi/launch.sh') + " ssh"
PSW_LNCHR = os.path.expanduser('.config/rofi/launch.sh') + " psw"
WIN_LNCHR = os.path.expanduser('.config/rofi/launch.sh') + " win"

POLYBAR_RELOAD = os.path.expanduser('~/.config/polybar/startup.sh')

keys = [
    Key([MOD],      "h",      lazy.layout.left()),
    Key([MOD],      "j",      lazy.layout.down()),
    Key([MOD],      "k",      lazy.layout.up()),
    Key([MOD],      "l",      lazy.layout.right()),

    Key([MOD, SFT], "h",      lazy.layout.shuffle_left()),
    Key([MOD, SFT], "j",      lazy.layout.shuffle_down()),
    Key([MOD, SFT], "k",      lazy.layout.shuffle_up()),
    Key([MOD, SFT], "l",      lazy.layout.shuffle_right()),

  # Key([MOD, CTRL], "h",     lazy.layout.grow_left()),
  # Key([MOD, CTRL], "j",     lazy.layout.grow_down()),
  # Key([MOD, CTRL], "k",     lazy.layout.grow_up()),
  # Key([MOD, CTRL], "l",     lazy.layout.grow_right()),
  # Key([MOD],       "n",     lazy.layout.normalize()),

    Key([MOD],      "Tab",    lazy.next_layout()),
    Key([MOD, SFT], "Tab",    lazy.prev_layout()),

    Key([MOD],      "w",      lazy.window.kill()),
    Key([MOD],      "t",      lazy.window.toggle_floating()),
    Key([MOD],      "f",      lazy.window.toggle_fullscreen()),
    Key([MOD],      "m",      lazy.window.toggle_maximize()),

    Key([MOD],      "space",  lazy.spawn(APP_LNCHR)),
  # Key([MOD],      "o",      lazy.spawn(SSH_LNCHR)),
  # Key([MOD],      "p",      lazy.spawn(PSW_LNCHR)),
    Key([MOD],      "r",      lazy.spawn(WIN_LNCHR)),
  # Key([MOD],      "r",      lazy.spawncmd()),
    Key([MOD],      "q",      lazy.spawn(NOTEAPP)),

    Key([MOD],      "Return", lazy.spawn(TERM)),

    Key([MOD, ALT], "b",      lazy.spawn(BROWSER)),
    Key([MOD, ALT], "e",      lazy.spawn(EXPLORER)),
    Key([MOD, ALT], "w",      lazy.spawn(WPMGR)),
    Key([MOD, ALT], "m",      lazy.spawn(MUSICPLYR)),
  # Key([MOD, ALT], "s",      lazy.spawn(f"{TERM} -e {SOUNDMGR}")),
    Key([MOD, ALT], "n",      lazy.spawn(NOTEDIR)),

    Key([MOD, CTRL], "r",     lazy.reload_config()),
    Key([MOD, CTRL], "q",     lazy.shutdown()),

    # These two basicly reload the entire system
    Key([MOD, CTRL], "t",     lazy.spawn(THEMESWCHR)),
    Key([MOD, CTRL], "g",     lazy.spawn(THEMESWCHR + " same")),

    # function keys
    # Key([],          "F2",    lazy.spawn(THEMESWCHR)),
    #
    # Key([],          "F5",    lazy.spawn("playerctl previous")),
    # Key([],          "F6",    lazy.spawn("playerctl play-pause")),
    # Key([],          "F7",    lazy.spawn("playerctl stop")),
    # Key([],          "F8",    lazy.spawn("playerctl next")),

    Key([MOD, SFT], "y",      lazy.layout.section_up()),
    Key([MOD, SFT], "u",      lazy.layout.section_down()),

    Key([MOD, SFT], "s",      lazy.spawn("flameshot gui")),

]

mouse = [
    Drag ([MOD], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag ([MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

def group_keys(groups):
    key = []
    # TODO: make sure to use xrandr to determine if we have 2 monitors
    # might not be necessary

    for _, group in enumerate(groups, 1):
        i = str(group.label)

        key.extend([
            Key([MOD],      i,
                lazy.to_screen(0) if i in '1234' else lazy.to_screen(1),
                lazy.group[group.name].toscreen()
                ),
            Key([MOD, SFT], i, lazy.window.togroup(group.name))
        ])
    return key
