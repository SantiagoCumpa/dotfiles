import subprocess
from libqtile.widget import base

class CustomWlan(base.ThreadPoolText):
    def __init__(self, interface="wlan0", **config):
        self.interface = interface
        super().__init__(**config)

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

            return f"{icon}  {essid}"

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
        if signal > 90:
            return '󰤨'
        elif signal > 70:
            return '󰤥'
        elif signal > 50:
            return '󰤢'
        elif signal > 30:
            return '󰤟'
        elif signal > 10:
            return '󰤯'
        else:
            return '󰤮'

