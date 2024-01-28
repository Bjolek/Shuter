import json

import PyQt5
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from main import start_game

app = QApplication([])
settings = {}

window = QWidget()

def read_data():
    global settings
    with open("Settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)

def write_data():
    global settings
    with open("Settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file)
read_data()

def buy_skin_1():
    if settings["money"] >= 100:
        settings["money"] -= 100
        settings["skin"] = "asteroid.png"
        write_data()
    else:
        print("Грошей не хватає!!!!!")

Knopka = QPushButton("Іграти")
Line = QLineEdit(settings["skin"])
Change = QPushButton("Change")
Skin1 = QLabel("Картинка")
Skin1_img = QPixmap("asteroid.png")
Skin1_img = Skin1_img.scaledToWidth(64)
Skin1.setPixmap(Skin1_img)
Buy = QPushButton("Купити")
mainLine = QVBoxLayout()

mainLine.addWidget(Knopka)
mainLine.addWidget(Line)
mainLine.addWidget(Change)
mainLine.addWidget(Skin1)
mainLine.addWidget(Buy)
Buy.clicked.connect(buy_skin_1)

window.setLayout(mainLine)




def change_data():
    settings["skin"] = Line.text()
    write_data()

Knopka.clicked.connect(start_game)

Change.clicked.connect(change_data)


window.show()
app.exec()
