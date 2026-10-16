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
winmargin=[10, 10, 10, 10]
winborder_width=3
winborder_focus="#94455b"
winborder_normal="#494949"

# bar settings
wmlogo = f"{home}/.config/qtile/void.png"
bar_font = "Minecraft Rus, Noto Color EmojiA"
mergin = [0, 50, 0, 50]
border_width = [0, 2, 2, 2]
border_color = ["94455b", "94455b", "94455b", "94455b"]

# wm name in fetch
wmname = "Qtile top wm"
