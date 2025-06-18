from libqtile import hook 
from libqtile.lazy import lazy

from settings.layouts import layouts, floating_layout
from settings.groups import groups
from settings.mouse import mouse
from settings.keys import keys
from settings.screens import screens
from settings.widgets import widget_defaults, extension_defaults

import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([script])

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
wl_input_rules = None

wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"
