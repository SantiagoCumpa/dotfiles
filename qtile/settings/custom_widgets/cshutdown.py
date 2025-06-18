import subprocess
import os
import logging
from libqtile.widget import TextBox

log_dir = os.path.expanduser("~/.config/qtile/logs")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, 'custom_shutdown.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class CustomShutdown(TextBox):
    def __init__(self, **config):
        super().__init__(text='󰐥', fontsize=16, **config)
        self.add_callbacks({'Button1': self.show_menu})

    def show_menu(self, *args):
#        choices = " 󰤆 | Shutdown \n  | Restart \n 󰤄 | Sleep \n 󰍃 | Logout \n 󰜺 | Cancel "
        choices = " 󰤆 | Shutdown \n  | Restart \n󰤄 \n 󰍃 | Logout \n 󰜺 | Cancel "
        cmd = ['rofi', '-dmenu', '-p', 'Options ', ]
        result = subprocess.run(cmd, input=choices, text=True, capture_output=True)
        choice = result.stdout.strip()

        if choice == " 󰤆 | Shutdown ":
            logging.info('shutdown')
            subprocess.call(['/usr/bin/systemctl', 'poweroff'])
        elif choice == "  | Restart ":
            logging.info('restart')
            subprocess.call(['/usr/bin/systemctl', 'reboot'])
#        elif choice == " 󰤄 | Sleep ":
        elif choice == "󰤄":
            logging.info('sleep')
            subprocess.call(['/usr/bin/systemctl', 'sleep'])
        elif choice == " 󰍃 | Logout ":
            logging.info('logout')
            subprocess.call(['qtile', 'cmd-obj', '-o', 'cmd', '-f', 'shutdown'])
