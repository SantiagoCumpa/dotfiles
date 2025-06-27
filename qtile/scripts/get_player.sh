#!/bin/bash

# Encuentra el primer reproductor en estado Playing o Paused
player=$(playerctl -l 2>/dev/null | while read p; do
    status=$(playerctl -p "$p" status 2>/dev/null)
    if [[ "$status" = "Playing" || "$status" = "Paused" ]]; then
        echo "$p"
        break
    fi
done)

# Si hay un reproductor activo, muestra título
if [ -n "$player" ]; then
    playerctl -p "$player" metadata --format '  {{ artist }} - {{ title }}'
else
    echo "󰝛"
fi
