#!/bin/sh

(sleep 5; xdotool key Super+Shift+Q) &

#screens
xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --output DP-1 --primary --mode 1920x1080 --pos 1920x0 -r 165 &

#wallpaper
nitrogen --restore &

#keyboard
setxkbmap latam &

exec picom &

timedatectl set-ntp true &
