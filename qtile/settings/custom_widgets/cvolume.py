from libqtile import bar
from libqtile.widget import base
import subprocess
import re

class CustomVolume(base.ThreadPoolText):
    length_type = bar.CALCULATED

    def __init__(self, **config):
        super().__init__('', **config)
        self.update_interval = 0
        self.add_callbacks({
            "Button1": self.toggle_mute,
            "Button4": self.vol_up,
            "Button5": self.vol_down,
        })

    def poll(self):
        try:
            volume, muted = self.get_vol()
            icon = self.get_icon(volume, muted)
            return f"{icon} {int(volume)}%"
        except Exception:
            return "󰝛 --"

    def get_default_sink(self):
        try:
            return subprocess.check_output(["pactl", "get-default-sink"], text=True).strip()
        except subprocess.CalledProcessError:
            return None

    def get_icon(self, volume, muted):
        if muted or volume == 0:
            return '󰖁'
        elif volume > 60:
            return '󰕾'
        elif volume > 30:
            return '󰖀'
        return '󰕿'

    def get_vol(self):
        sink = self.get_default_sink()
        output = subprocess.check_output(["pactl", "get-sink-volume", sink], text=True)
        mute_output = subprocess.check_output(["pactl", "get-sink-mute", sink], text=True)

        match = re.search(r'(\d+)%', output)
        volume = float(match.group(1)) if match else 0.0

        muted = "yes" in mute_output

        return volume, muted

    def toggle_mute(self):
        sink = self.get_default_sink()
        subprocess.Popen(["pactl", "set-sink-mute", sink, "toggle"])

    def vol_up(self):
        sink = self.get_default_sink()
        volume, _ = self.get_vol()
        if volume <= 95:
           subprocess.Popen(["pactl", "set-sink-volume", sink, "+5%"])
        
    def vol_down(self):
        sink = self.get_default_sink()
        subprocess.Popen(["pactl", "set-sink-volume", sink, "-5%"])
