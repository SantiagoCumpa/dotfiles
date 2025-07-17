#!/usr/bin/env bash

wifi_list=$(nmcli --fields SSID,SIGNAL device wifi list --rescan no | awk 'NR>1 && $1!="" {print $0}' | sort -k3 -nr)

# Format each line with signal icon
formatted=$(echo "$wifi_list" | awk '
function icon(signal) {
    if (signal >= 80) return "󰤨";
    else if (signal >= 60) return "󰤥";
    else if (signal >= 40) return "󰤢";
    else if (signal >= 20) return "󰤟";
    else return "󰤠";
}
{
    ssid=$1;
    for(i=2;i<=NF-2;++i) ssid=ssid" "$i; 
    signal=$(NF);
    print icon(signal) "  " ssid;
}')

chosen=$(echo "$formatted" | rofi -dmenu -p "Wi-Fi" -i)

[[ -z "$chosen" ]] && exit 0

ssid=$(echo "$chosen" | sed 's/^[^ ]*  //')

if nmcli -t -f active,ssid dev wifi | grep -q "^yes:$ssid$"; then
    dunstify "Wi-Fi" "Already connected to $ssid"
    exit 0
fi

security=$(nmcli --fields SSID,SECURITY device wifi list | grep "$ssid" | awk '{print $2}')

# Prompt for password if secured
if [[ "$security" != "--" ]]; then
    password=$(rofi -dmenu -password -p "Password for $ssid")
    [[ -z "$password" ]] && exit 1
    nmcli dev wifi connect "$ssid" password "$password" && dunstify "Wi-Fi" "Connected to $ssid" || dunstify  "Wi-Fi" "Connection failed"
else
    nmcli dev wifi connect "$ssid" && dunstify "Wi-Fi" "Connected to $ssid" || dunstify "Wi-Fi" "Connection failed"
fi

nmcli device wifi rescan &

