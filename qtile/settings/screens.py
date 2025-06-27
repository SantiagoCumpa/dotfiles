from libqtile.config import Screen
from libqtile import bar, widget
from libqtile.log_utils import logger
from .widgets import widgets

import subprocess
import os

# Replace with your wallpaper file path
wallpaper_name = 'galaxy-01.png'
wallpaper_path = os.path.expanduser("~/Images/Wallpapers/") + wallpaper_name

def status_bar(widg):
    return bar.Bar(
           widg, 35, 
           margin = [ 5, 5, 10, 5], 
           
 border_color="#ffffff",
           border_width=1,
           background='#ffffff00'
    )

screens = [
    Screen(top=status_bar(widgets),
           wallpaper=wallpaper_path,
           wallpaper_mode = "fill",
    ),
]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(widgets),
           wallpaper=wallpaper_path,
           wallpaper_mode = "fill"
        ))



