#!/bin/sh

#battery
tlp start 2>/dev/null &

#mouse speed
#xinput set-prop 12 "libinput Accel Speed" 1

#screens
xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rate 60 --output DP-1 --primary --mode 1920x1080 --pos 1920x0 --rate 60 &

#set keyboard
setxkbmap latam,us -option "grp:alt_shift_toggle" &

#init compositor
picom --experimental-backend &

