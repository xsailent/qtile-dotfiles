import customtkinter as ctk
import os
import subprocess
import sys


def shutdown():
    os.system("loginctl poweroff")
    sys.exit()


def reboot():
    os.system("loginctl reboot")
    sys.exit()


def logout():
    subprocess.run(
        ["qtile", "cmd-obj", "-o", "cmd", "-f", "shutdown"], capture_output=True
    )
    sys.exit()


def suspend():
    os.system("loginctl suspend")
    sys.exit()


ctk.set_appearance_mode("Dark")

app = ctk.CTk()
app.geometry("600x350")
app.title("Xsailent Power Menu")
app.resizable(False, False)

label = ctk.CTkLabel(app, text="Power menu by xsailent", font=("Arial", 28))
label.place(relx=0.5, rely=0.25, anchor="c")

shutdown = ctk.CTkButton(app, text="Shutdown", command=shutdown, width=550)
shutdown.place(relx=0.5, rely=0.41, anchor="c")

reboot = ctk.CTkButton(app, text="Reboot", command=reboot, width=550)
reboot.place(relx=0.5, rely=0.53, anchor="c")

logout = ctk.CTkButton(app, text="logout", command=logout, width=550)
logout.place(relx=0.5, rely=0.65, anchor="c")

suspend = ctk.CTkButton(app, text="suspend", command=suspend, width=550)
suspend.place(relx=0.5, rely=0.77, anchor="c")

app.mainloop()
