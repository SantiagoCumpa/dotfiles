#!/bin/sh

(sleep 5; xdotool key Super+Shift+Q) &

#screens
xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-1-0 --primary --mode 1920x1080 --pos 1920x0 -r 120 --rotate normal &

#wallpaper
nitrogen --restore &

#keyboard
setxkbmap latam &

exec picom &

timedatectl set-ntp true &
