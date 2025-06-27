from libqtile import widget

from .custom_widgets.cwlan 	import CustomWlan
from .custom_widgets.cworkspace import CustomWorkspace
from .custom_widgets.cvolume 	import CustomVolume
from .custom_widgets.cbattery 	import CustomBattery

import subprocess
import os

# rofi path
rofi_path=os.path.expanduser("~/.config/rofi/")
# qtile scripts path
qtile_scripts_path=os.path.expanduser("~/.config/qtile/scripts/")

# WIDGETS
widgets= [
	widget.TextBox('󰣇', fontsize=25,padding=15),
       *CustomWorkspace,
	widget.Spacer(),
	widget.GenPollText(
		update_interval=3,
		func=lambda: subprocess.check_output(
	        	[qtile_scripts_path + 'get_player.sh']
    		).decode('utf-8').strip(),
    		scroll=True,
    		scroll_step=1,
    		scroll_interval=0.2,
    		mouse_callbacks={
        		'Button1': lambda: subprocess.Popen(['playerctl', 'play-pause']),
        		'Button4': lambda: subprocess.Popen(['playerctl', 'previous']),
        		'Button5': lambda: subprocess.Popen(['playerctl', 'next']),
    		},
	),
	widget.Spacer(),
        CustomVolume(),
	widget.Sep(),
	CustomWlan( interface="wlan0"),
	widget.Sep(),
	widget.CPU(format=' {load_percent}%'),
	widget.Sep(),
	widget.Memory(
		format=' {MemUsed:.1f}/{MemTotal:.0f}{mm}',
    		measure_mem='G',
    		update_interval=5,
	),
	widget.Sep(),
        CustomBattery(),        
	widget.Sep(),
        widget.Clock(
		format=" %Y/%m/%d  %I:%M %p",
	),
	widget.Sep(),
	widget.KeyboardLayout(
		configured_keyboards=['latam', 'us'],
    		display_map={'us': 'EN', 'latam': 'ES'},
    		mouse_callbacks={ 'Button1': lambda: subprocess.Popen(
				['bash', qtile_scripts_path + 'toogle_layout.sh'])
		},
                update_interval = 1,
	),
	widget.Sep(),
]

widget_defaults = dict(
    font="GeistMono NF",
    fontsize=14,
)

extension_defaults = widget_defaults.copy()
