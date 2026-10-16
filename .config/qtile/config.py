import os
from collections.abc import Callable

import libqtile.resources
from libqtile import bar, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Output, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from libqtile import qtile
from libqtile import hook
from libqtile.config import Key
from libqtile.widget import KeyboardLayout

from subprocess import check_output
import subprocess
from libqtile.widget import GenPollText
import re

import style

# @hook.subscribe.startup_once
# def start_gestures():
# subprocess.Popen(["libinput-gestures"])


def get_volume_pactl():
    try:
        cmd = ["pactl", "list", "sources"]
        cmd2 = ["pactl", "list", "sinks"]

        result2 = subprocess.run(cmd2, capture_output=True, text=True)
        output2 = result2.stdout

        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout

        volume_lines = re.findall(r"Volume:.*?(\d+)%", output)
        volume_lines2 = re.findall(r"Volume:.*?(\d+)%", output2)

        if volume_lines and volume_lines2:
            return f"[🎧 : {volume_lines2[0]}% 🎤 : {volume_lines[0]}%]"
        return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


def get_layout_fast():
    try:
        result = subprocess.run(
            ["xkblayout-state", "print", "%s"], capture_output=True, text=True
        )
        if result.stdout.strip().upper() == "US":
            return " [🇺🇸]"
        else:
            return " [🇷🇺]"
    except:
        return " [??]"


# def get_layout_fast():
# backend = qtile.core.name

# if backend == "x11":
# try:
# result = subprocess.run(
# ["xkblayout-state", "print", "%s"],
# capture_output=True,
# text=True,
# timeout=0.2,
# )

# layout = result.stdout.strip().lower()

# if layout == "us":
# return " [🇺🇸]"
# elif layout == "ru":
# return " [🇷🇺]"

# return f" [{layout.upper()}]"

# except (subprocess.SubprocessError, FileNotFoundError):
# return " [??]"

# elif backend == "wayland":
# if current_layout == "us":
# return " [🇺🇸]"
# elif current_layout == "ru":
# return " [🇷🇺]"

# return f" [{current_layout.upper()}]"

# return " [??]"


def get_battery():
    try:
        result = subprocess.run(
            ["acpi", "-b", "|", "awk", "'{print $4}'", "|", "tr", "-d", "','"],
            capture_output=True,
            text=True,
        )
        return f"[{result}]"
    except:
        return "[Unknown]"


def player():
    result = subprocess.run(
        ["playerctl", "metadata", "--format", '"{{ artist }} - {{ title }}"'],
        capture_output=True,
        text=True,
    )
    player_output = result.stdout.rstrip("\n")
    clean_output = player_output.replace('"', "")

    if clean_output == "":
        return "Nothing played"
    else:
        return clean_output


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.Popen([script])


mod = "mod4"
terminal = guess_terminal()
rofi = "rofi -show drun"
tg = "Telegram"
browser = "helium"
dolphin = "dolphin"
flameshot = "flameshot gui"

home = os.path.expanduser("~")
oboi = style.wallpap
themes_script = f"python {home}/.config/qtile/scripts/theme_selector.py"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "z", lazy.spawn(tg), desc="Launch Telegram"),
    Key([mod], "b", lazy.spawn(rofi), desc="Launch rofi"),
    Key([mod], "c", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "p", lazy.spawn(dolphin), desc="Launch dolphin"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([], "Print", lazy.spawn(flameshot), desc="Screenstoter"),
    Key(
        [mod, "shift"], "z", lazy.spawn(themes_script), desc="script for change themes"
    ),
]


# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        margin=style.winmargin,
        border_width=style.winborder_width,
        border_focus=style.winborder_focus,
        border_normal=style.winborder_normal,
    ),
    layout.Max(),
    layout.Stack(stacks=3),
    layout.Floating(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    # font="sans",
    font=style.bar_font,
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

logo = os.path.join(os.path.dirname(libqtile.resources.__file__), "logo.png")
screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.Image(filename=style.wmlogo, scale=True),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                # widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                # ),
                widget.Spacer(length=bar.STRETCH),
                widget.GenPollText(
                    # func=player,
                    func=lambda: (
                        f"{player()[:20]}...{player()[-20:]}"
                        if len(player()) > 35
                        else player()
                    ),
                    update_interval=0.5,
                    mouse_callbacks={
                        "Button1": lazy.spawn("playerctl play-pause"),  # Left click
                        "Button3": lazy.spawn(
                            f"python {home}/.config/qtile/scripts/xsalo_player.py"
                        ),  # Right click
                    },
                ),
                widget.Spacer(length=bar.STRETCH),
                widget.GenPollText(
                    func=get_volume_pactl,
                    update_interval=0.5,
                    mouse_callbacks={
                        "Button1": lazy.spawn("pavucontrol-qt"),  # Left click
                    },
                ),
                # widget.GenPollText(
                #    func=get_battery,
                #    update_interval=30,
                #    foreground="#ffffff",
                # ),
                widget.Battery(
                    format="[🔋 {char} {percent:2.0%} {hour:d}:{min:02d}]",
                    charge_char="▲",
                    discharge_char="▼",
                    update_interval=0.5,
                    low_percentage=0.2,
                    low_foreground="FF0000",
                ),
                # widget.TextBox("xsailent on qtile", foreground="#9b5fd7"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.GenPollText(
                    func=get_layout_fast,
                    update_interval=0.5,
                    fmt="{}",
                ),
                widget.Systray(),
                widget.Clock(format="🕗:[%Y-%m-%d %H:%M]"),
                # widget.QuickExit(),
                widget.TextBox(
                    text="⏻",
                    mouse_callbacks={
                        "Button1": lazy.spawn(
                            f"python {home}/.config/qtile/scripts/xsalopower.py"
                        )
                    },
                ),
            ],
            24,
            margin=style.mergin,
            border_width=style.border_width,  # Draw top and bottom borders
            border_color=style.border_color,  # Borders are magenta
        ),
        background="#2e2742",
        wallpaper=oboi,
        wallpaper_mode="fill",  # "center",
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Instead of screens, you can define a function here to specify which Screen
# should correspond to which Output.
fake_screens: list[Screen] | None = None

# Instead of screens or fake screens, you can define a function here that
# returns a list of Screen objects based on the list of Outputs; that way you
# can decide based on e.g. the number of screens, or which ports are plugged
# in exactly what do render in each bar for each screen.
generate_screens: Callable[[list[Output]], list[Screen]] | None = None

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

idle_timers = []  # type: list
idle_inhibitors = []  # type: list

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = style.wmname
