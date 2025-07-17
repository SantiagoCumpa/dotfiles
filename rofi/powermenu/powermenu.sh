#!/usr/bin/env bash

# Current Theme
dir="$HOME/.config/rofi/powermenu/"
theme='tui'

# CMDs
uptime="`uptime -p | sed -e 's/up //g'`"

# Options
shutdown='󰤆'
lock=''
reboot=''
suspend='󰤄'
logout='󰍃'

# Rofi CMD

rofi_cmd() {
	rofi -dmenu \
		-p "Uptime: $uptime" \
		-mesg "Uptime: $uptime" \
		-theme ${dir}/${theme}.rasi
}

# Pass variables to rofi dmenu
run_rofi() {
	echo -e "$lock\n$logout\n$suspend\n$reboot\n$shutdown" | rofi_cmd
}

# Execute Command
run_cmd() {
	if [[ $1 == '--shutdown' ]]; then
		systemctl poweroff
	elif [[ $1 == '--reboot' ]]; then
		systemctl reboot
	elif [[ $1 == '--suspend' ]]; then
                playerctl play-pause
		systemctl sleep
	elif [[ $1 == '--lockscreen' ]]; then
		img="/tmp/lockscreen_blur.png"
		sleep 1
		import -window root "$img"
		magick "$img" -blur 0x3 -fill black -colorize 40% "$img"
		i3lock -i "$img" -u
		rm "$img"
	elif [[ $1 == '--logout' ]]; then
                qtile cmd-obj -o cmd -f shutdown
	fi
}

# Actions
chosen="$(run_rofi)"
case ${chosen} in
    $shutdown)
		run_cmd --shutdown
        ;;
    $reboot)
		run_cmd --reboot
        ;;
    $lock)
       		run_cmd --lockscreen
        ;;
    $suspend)
		run_cmd --suspend
        ;;
    $logout)
		run_cmd --logout
        ;;
esac
