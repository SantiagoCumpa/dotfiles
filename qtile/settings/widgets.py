from libqtile import widget
from .colors import colors

def padding(bg='theme-dark', padd=5):
    return widget.Sep(background=colors[bg], linewidth=0, padding=padd)

def widget_triangle_start(fg='theme-dark', bg='theme-dark'):
    return widget.TextBox(
        foreground=colors[fg],
        background=colors[bg],
        text="", 
        fontsize=70,
        padding=-11,
    )

def workspaces ():
    return [
        widget.GroupBox(
            highlight_method="line",
            fontsize=30,
            active=colors['theme-active'],
            inactive=colors['theme-inactive'],
            urgent_alert_method='line',
            urgent_border=colors['red-dark'],
            urgent_text=colors['red-dark'],
            this_current_screen_border=colors['theme-active'],
            this_screen_border=colors['theme-dark'],
            other_current_screen_border=colors['theme-active'],
            other_screen_border=colors['theme-inactive'],
            disable_drag=True,
            highlight_color=[ colors['black']]
        ),
    ]

def wcpu():
    return[
        widget.WidgetBox(
            text_open='',
            start_opened=True,
            widgets = [
                widget_triangle_start('theme-light'),
                widget.TextBox('󰍛', background=colors['theme-light'], foreground=colors['theme-dark'], fontsize=22, padding=0),
                widget.CPU( background=colors['theme-light'], foreground=colors['theme-dark'], interface='',
                            format='CPU {freq_current}GHz {load_percent}%'),
            ]
        )
    ]

def wwifi():
    return [
        widget.WidgetBox(
            text_open='',
            start_opened=True,
            widgets = [
                widget_triangle_start('yellow', 'theme-light'),
                padding('yellow'),
                widget.TextBox("", background=colors['yellow'], foreground=colors['black'], fontsize=20, padding=0),
                widget.Net( interface="wlp0s20f3",
                            format='{down:6.1f}{down_suffix:<2}↓↑{up:6.1f}{up_suffix:<1}',
                            background=colors['yellow'],
                            foreground=colors['black'],
                            padding=0),
                padding('yellow'),
            ],
        )
    ]

def wbattery():
    return [
        widget.WidgetBox(
            text_open='',
            start_opened=True,
            widgets = [
                widget_triangle_start('green-dark', 'yellow'),
                padding('green-dark'),
                widget.Battery(
                    background=colors['green-dark'],
                    foreground=colors['black'],
                    fontsize=20,
                    charge_char="󰂄",
                    discharge_char="󰂂",
                    full_char="󱈑",
                    low_background=colors['red-dark'],
                    low_foreground=colors['red-light'],
                    low_percentage=0.25,
                    format='{char}',
                    padding=0,
                    show_short_text=False,
                ),
                widget.Battery(
                    background=colors['green-dark'],
                    foreground=colors['black'],
                    charge_char="",
                    discharge_char="",
                    full_char="",
                    low_background=colors['red-dark'],
                    low_foreground=colors['red-light'],
                    low_percentage=0.25,
                    format='{percent: 2.0%}',
                    padding=0,
                    show_short_text=False,
                ),
                padding('green-dark'),
            ],
        )
    ]

def wcalendar():
    return [
        widget.WidgetBox(
            text_open='',
            start_opened=True,
            widgets = [
                widget_triangle_start('orange-dark', 'green-dark'),
                padding('orange-dark'),
                widget.TextBox( fontsize=20, text='', foreground=colors['orange-light'],
                                background=colors['orange-dark'], padding=0),
                padding('orange-dark',10),
                widget.Clock(
                    background=colors['orange-dark'],
                    foreground=colors['orange-light'],
                    format="%d.%m.%Y",
                    padding=0),
                padding('orange-dark'),
            ]
        )
    ]

def wclock():
    return [
        widget.WidgetBox(
            text_open='',
            start_opened=True,
            widgets = [
                widget_triangle_start('purple-dark', 'orange-dark'),
                padding('purple-dark'),
                widget.TextBox( fontsize=20, text='󰥔', foreground=colors['purple-light'],
                                background=colors['purple-dark'], padding=0),
                widget.Clock(
                    background=colors['purple-dark'],
                    foreground=colors['purple-light'],
                    format="%I:%M %p"),
                padding('purple-dark'),
            ]
        )
    ]

def wtab():
    return [
        widget.WindowName(
            fontsize = 13,
            empty_group_string=' Welcome to Arch Linux, Santiago!',
        )
    ]

def wlogo():
    return [
        padding('theme-light',3),
        widget.TextBox('󰣇', fontsize=35, 
                        foreground=colors['theme-dark'], 
                        background=colors['theme-light'],
                        padding=12),
    ]

def wlayout():
    return [
        widget.WidgetBox(
            text_open='',
            start_opened=True,
            widgets = [
                widget.CurrentLayout(),
            ]
        )
    ]

widgets= [
    *wlogo(),
    *workspaces(),
    *wtab(),
    *wlayout(),
    *wcpu(),
    *wwifi(),
    *wbattery(),
    *wcalendar(),
    *wclock(),
]

widget_defaults = dict(
    font="Cascadia Code NF",
    fontsize=13,
)

extension_defaults = widget_defaults.copy()