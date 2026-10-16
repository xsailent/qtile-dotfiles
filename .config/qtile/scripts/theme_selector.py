from PySide6.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QRadioButton, QComboBox
from PySide6.QtCore import QObject
from pathlib import Path
import os
import shutil
from qt_material import apply_stylesheet
import subprocess

app = QApplication([])
apply_stylesheet(app, theme='dark_teal.xml')

window = QWidget()
window.setFixedSize(350, 500)

theme_dir = os.path.expanduser("~/.config/qtile/")
theme_wall_dir = os.path.expanduser("~/.config/qtile/wallpapers/")

themes_dir = os.path.expanduser("~/.xsalothemes/")

#folders = [f for f in Path(themes_dir).iterdir() if f.is_dir()]
folders = [f for f in os.listdir(themes_dir) if os.path.isdir(os.path.join(themes_dir, f))]

# Создаем GroupBox с заголовком
group_box = QGroupBox("Выберите тему")

# Создаем макет для внутреннего содержимого группы
layout = QVBoxLayout()

class RadioHandler(QObject):
    def on_radio_toggled(self, checked):
        if checked:
            # В классе можно использовать self.sender()
            button_name = self.sender().text()
            target_name = "wall"

            for file in Path(themes_dir + button_name).glob(f"{target_name}.*"):
                for f in Path(theme_wall_dir).glob(f"{target_name}.*"):
                    os.remove(theme_wall_dir + f.name)
                else:
                    shutil.copy(themes_dir + button_name + "/" + file.name, theme_wall_dir)  # Например: wall.png
                    shutil.copy(themes_dir + button_name + "/style.py", theme_dir)
                    subprocess.run(["qtile", "cmd-obj", "--object", "cmd", "--function", "reload_config"])
                break
            else:
                print("Файл не найден")

handler = RadioHandler()

for i in folders:
    theme = QRadioButton(i.replace("'", ""))
    theme.toggled.connect(handler.on_radio_toggled)
    layout.addWidget(theme)

# Устанавливаем макет в GroupBox
group_box.setLayout(layout)

# Добавляем GroupBox в основное окно
main_layout = QVBoxLayout()
main_layout.addWidget(group_box)
window.setLayout(main_layout)

window.show()
app.exec()

