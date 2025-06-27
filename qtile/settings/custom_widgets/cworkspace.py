from libqtile.widget import base
from libqtile import hook

class CustomWorkspaceIndicator(base.ThreadPoolText):
    def __init__(self, group_name, **config):
        super().__init__("", **config)

        self.group_name = str(group_name)
        self.update_interval=0
        self.add_callbacks({
            "Button1": self.goto_group,
        })

    def goto_group(self):
        from libqtile import qtile
        qtile.groups_map[self.group_name].toscreen()

    def poll(self):
        from libqtile import qtile
        current = qtile.current_group.name
        return "" if current == self.group_name else ""


CustomWorkspace = [
    CustomWorkspaceIndicator(str(i), fontsize=15, padding=8)
    for i in range(1, 6)
]
