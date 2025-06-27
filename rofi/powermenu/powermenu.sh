#!/usr/bin/env bash

# Current Theme
dir="$HOME/.config/rofi/powermenu/"
theme='tui'

# CMDs
uptime="`uptime -p | sed -e 's/up //g'`"
host=`hostname`

# Options
shutdown='󰤆'
reboot=''
lock=''
suspend='󰤄'
logout='󰍃'

# Rofi CMD
rofi_cmd() {
	rofi -dmenu \
		-p "Uptime: $uptime" \
		-mesg "Uptime: $uptime" \
		-theme ${dir}/${theme}.rasi
}

# Confirmation CMD
confirm_cmd() {
	rofi -theme-str 'window {location: center; anchor: center; fullscreen: false; width: 350px;}' \
		-theme-str 'mainbox {children: [ "message", "listview" ];}' \
		-theme-str 'listview {columns: 2; lines: 1;}' \
		-theme-str 'element-text {horizontal-align: 0.5;}' \
		-theme-str 'textbox {horizontal-align: 0.5;}' \
		-dmenu \
		-theme ${dir}/${theme}.rasi
}

# Ask for confirmation
#confirm_exit() {
#	echo -e "$yes\n$no" | confirm_cmd
#}

# Pass variables to rofi dmenu
run_rofi() {
	echo -e "$lock\n$suspend\n$logout\n$reboot\n$shutdown" | rofi_cmd
}

# Execute Command
run_cmd() {
	if [[ $1 == '--shutdown' ]]; then
		systemctl poweroff
	elif [[ $1 == '--reboot' ]]; then
		systemctl reboot
	elif [[ $1 == '--suspend' ]]; then
		mpc -q pause
		amixer set Master mute
		systemctl suspend
	elif [[ $1 == '--lockscreen' ]]; then
		img="/tmp/lockscreen_blur.png"
		sleep 1
		import -window root "$img"
		magick "$img" -blur 0x3 -fill black -colorize 30% "$img"
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
