from libqtile.widget import TextBox
from libqtile import qtile
from libqtile.lazy import lazy
from threading import Thread
import subprocess
import time

class CustomMediaPlayer(TextBox):
    def __init__(self, max_width=20, scroll_delay=0.3, **config):
        super().__init__(**config)
        self.max_width = max_width
        self.scroll_delay = scroll_delay
        self.full_text = ""
        self.display_text = ""
        self.scroll_index = 0
        self.running = True

        self.add_callbacks({
            'Button1': self.toggle_play,   
            'Button4': self.next_track,    
            'Button5': self.previous_track 
        })

        self.update_thread = Thread(target=self.update_loop, daemon=True)
        self.update_thread.start()

    def get_metadata(self):
        try:
            title = subprocess.check_output(["playerctl", "metadata", "title"]).decode().strip()
            artist = subprocess.check_output(["playerctl", "metadata", "artist"]).decode().strip()
            return f"{artist} - {title}"
        except subprocess.CalledProcessError:
            return "󰝛"

    def scroll_text(self):
        if len(self.full_text) <= self.max_width:
            return self.full_text
        end_index = self.scroll_index + self.max_width
        if end_index > len(self.full_text):
            # wrap-around scroll
            visible = self.full_text[self.scroll_index:] + " • " + self.full_text[:end_index - len(self.full_text)]
        else:
            visible = self.full_text[self.scroll_index:end_index]
        self.scroll_index = (self.scroll_index + 1) % len(self.full_text)
        return visible

    def update_loop(self):
        while self.running:
            self.full_text = self.get_metadata()
            self.text = "  " + self.scroll_text() + "..."
            self.bar.draw()
            time.sleep(self.update_interval)

    def toggle_play(self):
        subprocess.call(["playerctl", "play-pause"])

    def next_track(self):
        subprocess.call(["playerctl", "next"])

    def previous_track(self):
        subprocess.call(["playerctl", "previous"])
