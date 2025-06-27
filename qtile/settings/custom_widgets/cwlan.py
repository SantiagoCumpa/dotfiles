import subprocess
from libqtile.widget import base

class CustomWlan(base.ThreadPoolText):
    def __init__(self, interface="wlan0", update_interval=5):
        self.interface = interface
        self.update_interval = update_interval
        super().__init__()

    def poll(self):
        try:
            # Detectar nombre de red (essid)
            essid = subprocess.check_output(
                ["iwgetid", "-r"],
                stderr=subprocess.DEVNULL
            ).decode().strip()

            if not essid:
                return "󰤮  Not Connected" 

            # Detectar calidad de señal
            quality = self.get_signal_strength()
            icon = self.get_signal_icon(quality)

            return f"{icon} {essid}"
        except Exception as e:
            return "󰤭 Error"

    def get_signal_strength(self):
        try:
            result = subprocess.check_output(
                ["grep", self.interface, "/proc/net/wireless"]
            ).decode()
            signal = int(float(result.split()[2]))
            return signal
        except Exception:
            return 0

    def get_signal_icon(self, signal):
        levels = [
            (90, '󰤨'),
            (70, '󰤥'),
            (50, '󰤢'),
            (30, '󰤟'),
            (10, '󰤯'),
            (0,  '󰤮'),
        ]
        for threshold, icon in levels:
            if signal >= threshold:
                return icon
