from libqtile.widget import base
from libqtile import hook

class CustomWorkspaceIndicator(base.ThreadPoolText):
    def __init__(self, group_name, **config):
        super().__init__("", **config)

        self.group_name = str(group_name)
        self.update_interval=0.1
        self.add_callbacks({
            "Button1": self.goto_group,
        })

        # Update when group changes
        hook.subscribe.setgroup(self._update)
        hook.subscribe.changegroup(self._update)

    def _update(self):
        self.update(self.poll())

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
