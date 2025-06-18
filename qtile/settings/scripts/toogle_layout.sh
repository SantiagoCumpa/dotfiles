#!/bin/sh
if [ "$(setxkbmap -query | awk '/layout/{print $2}')" = "us" ]; then
   setxkbmap -layout latam
else
   setxkbmap -layout us
fi
