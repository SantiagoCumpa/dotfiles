from libqtile.widget import base
import psutil

class CustomBattery(base.InLoopPollText):
    def __init__(self, **config):
        super().__init__(**config)
        self.update_interval=2
        self.last_text=""
        self.last_state=None
        self.last_color="#ffffff"

    def poll(self):
        try:
            battery = psutil.sensors_battery()
            percent = int(battery.percent)
            charging = battery.power_plugged
            icon, color = self.get_icon(percent, charging)
 
            if charging != self.last_state:
               self.last_text = f'{icon} {percent}%'
               self.last_update = charging
               self.last_color = color
               return f'<span foreground="{color}">{icon} {percent}%</span>'
            
            return f'<span foreground="{color}">{self.last_text}</span>'

        except Exception as e:
            return "󱟩 ?"  	      

    def get_icon(self, percent, charging):
        levels = [
            (90, "󰂅", "#00d787", "󰁹", "#ffffff"),
            (70, "󰢞", "#a0e024", "󰂀", "#ffffff"),
            (50, "󰢝", "#f2c200", "󰁾", "#ffffff"),
            (30, "󰂇", "#f2c200", "󰁼", "#ffffff"),
            (20, "󰢜", "#f2c200", "󰁺", "#f28705"),
            (0,  "󰢜", "#f28705", "󱃍", "#ff4a4a"),
        ]

        for threshold, icon_c, color_c, icon_d, color_d in levels:
            if percent >= threshold:
               return (icon_c, color_c) if charging else (icon_d, color_d)

