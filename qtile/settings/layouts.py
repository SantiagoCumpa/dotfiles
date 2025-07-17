from libqtile import layout, qtile
from libqtile.config import Match

#from .colors import colors

layout_conf = {
    'border_focus': "#ffffff",
    'single_border_width': 2,
    'border_width': 2,
    'margin': 5,
    'border_normal': "#000000",
    'border_on_single': True
}

layouts = [
    layout.Columns(**layout_conf),
    layout.Stack( num_stacks=3, autosplit=False,
                    **layout_conf,
    )
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
)
