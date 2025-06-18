from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keys import mod, keys

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend([
        # Switch to workspace N
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        # Send to workspace N
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    ])
