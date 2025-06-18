from libqtile import layout, qtile
from libqtile.config import Match

from .colors import colors

layout_conf = {
#    'border_focus': colors['theme-light'],
    'border_width': 1,
    'margin': 4,
}

layouts = [
    layout.Columns( border_focus_stack=[colors['white']], 
                    border_normal=[colors['theme-dark']],
                    **layout_conf
    ),
    layout.Stack(   num_stacks=3,
                    **layout_conf,
                    #border_focus_stack=[colors['theme-light']]
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
