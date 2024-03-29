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
        settings["skin"] = "Spaseship.jpg"
        write_data()
    else:
        print("Грошей не хватає!!!!!")

def buy_skin_2():
    if settings["money"] >= 100:
        settings["money"] -= 100
        settings["skin"] = "ufo.png"
        write_data()
    else:
        print("Грошей не хватає!!!!!")

Knopka = QPushButton("Іграти")
Line = QLineEdit(settings["skin"])
Change = QPushButton("Change")
Skin1 = QLabel("Картинка")
Skin1_img = QPixmap("Spaseship.jpg")
Skin1_img = Skin1_img.scaledToWidth(64)
Skin1.setPixmap(Skin1_img)
Buy = QPushButton("Купити")

Skin2 = QLabel("Картинка")
Skin2_img = QPixmap("ufo.png")
Skin2_img = Skin2_img.scaledToWidth(64)
Skin2.setPixmap(Skin2_img)
Buy2 = QPushButton("Купити")
mainLine = QVBoxLayout()

mainLine.addWidget(Knopka)
mainLine.addWidget(Line)
mainLine.addWidget(Change)

mainLine.addWidget(Skin1)
mainLine.addWidget(Buy)
Buy.clicked.connect(buy_skin_1)

mainLine.addWidget(Skin2)
mainLine.addWidget(Buy2)
Buy.clicked.connect(buy_skin_2)

window.setLayout(mainLine)




def change_data():
    settings["skin"] = Line.text()
    write_data()

Knopka.clicked.connect(start_game)

Change.clicked.connect(change_data)


window.show()
app.exec()
