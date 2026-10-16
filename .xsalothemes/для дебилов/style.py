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
winborder_focus="#4f1b82"
winborder_normal="#3a1163"

# bar settings
wmlogo = f"{home}/.config/qtile/arch.png"
bar_font = "Minecraft Rus, Noto Color EmojiA"
mergin = [10, 100, 0, 100]
border_width = [0, 0, 2, 0]
border_color = ["41808c", "41808c", "41808c", "41808c"]

# wm name in fetch
wmname = "Qtile top wm"
