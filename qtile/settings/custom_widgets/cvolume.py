from libqtile.widget import base
from libqtile import qtile, bar
import subprocess

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
            
            if muted:
                icon = '󰖁'
            elif volume > 60:
                icon = '󰕾'
            elif volume > 30:
                icon = '󰖀'
            elif volume >= 1:
                icon = '󰕿'
            elif volume == 0:
                icon = '󰖁'
            
            return f"{icon} {int(volume)}%"
        except Exception:
            return "󰝛 --"

    def get_vol(self):
        result = subprocess.check_output(
            ["wpctl", "get-volume", "@DEFAULT_AUDIO_SINK@"],
            text=True
        )
        parts = result.strip().split()
        volume = float(parts[1]) * 100
        muted = 'MUTED' in parts
        
        return volume, muted

    def toggle_mute(self):
        subprocess.Popen(["wpctl", "set-mute", "@DEFAULT_AUDIO_SINK@", "toggle"])

    def vol_up(self):
        volume, _ = self.get_vol()
        
        if volume >= 100: 
           subprocess.Popen(["wpctl", "set-volume", "-l", "@DEFAULT_AUDIO_SINK@", "1"])
        else:
           subprocess.Popen(["wpctl", "set-volume", "-l", "1.5", "@DEFAULT_AUDIO_SINK@", "1%+"])

    def vol_down(self):
        subprocess.Popen(["wpctl", "set-volume", "@DEFAULT_AUDIO_SINK@", "1%-"])
