from libqtile import layout, qtile
from libqtile.config import Match

from .colors import colors

layout_conf = {
    'border_focus': colors['theme-light'],
    'border_width': 2,
    'margin': 6,
}

layouts = [
    layout.Columns( border_focus_stack=[colors['white']], 
                    border_normal=[colors['theme-dark']],
                    **layout_conf,
                    border_on_single=[colors['theme-light']],
                    border_unfocused=[colors['theme-inactive']],
                    margin_on_single=6, insert_position=1),
    layout.Stack(   num_stacks=3,
                    **layout_conf,
                    border_focus_stack=[colors['theme-light']],
                    border_unfocused=[colors['theme-inactive']],
                    margin_on_single=6),
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
