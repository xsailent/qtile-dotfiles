import os
from pathlib import Path

home = os.path.expanduser("~")


def wallpaper():
    walldir = f"{home}/.config/qtile/wallpapers/"
    target_name = "wall"

    for file in Path(walldir).glob(f"{target_name}.*"):
        wallpap = walldir + file.name
        return wallpap


# wallpaper
wallpap = wallpaper()

# windows settings
winmargin = [10, 10, 10, 10]
winborder_width = 3
winborder_focus = "#7c6f64"
winborder_normal = "#504945"

# bar settings
wmlogo = f"{home}/.config/qtile/void.png"
bar_font = "Hack, Noto Color EmojiA"
mergin = [0, 0, 0, 0]
border_width = [0, 0, 2, 0]
border_color = ["665c54", "665c54", "665c54", "665c54"]

# wm name in fetch
wmname = "gruvbox Qtile theme"
