#!/usr/bin/env bash

# Список: "Текст\0icon\x1fимя-иконки"
options=" Выключить\0icon\x1fsystem-shutdown\n"
options+=" Перезагрузить\0icon\x1fsystem-restart\n"
options+=" Спящий режим\0icon\x1fsystem-suspend\n"
options+=" Заблокировать\0icon\x1fsystem-lock-screen\n"
options+=" Выйти\0icon\x1fsystem-log-out"

chosen=$(echo -en "$options" | rofi -dmenu -i -show-icons -p "Питание")

case "$chosen" in
    " Выключить") loginctl poweroff ;;
    " Перезагрузить") loginctl reboot ;;
    " Спящий режим") loginctl suspend ;;
    " Заблокировать") # замени на свою команду блокировки, например i3lock или betterlockscreen -l
        i3lock -c 000000 ;;
    " Выйти") # замени на команду выхода из твоего WM, например i3-msg exit
        i3-msg exit ;;
esac
