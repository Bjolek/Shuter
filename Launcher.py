import json

import PyQt5
from PyQt5.QtWidgets import *

from main import start_game

app = QApplication([])
settings = {}

window = QWidget()
window.resize(800,600)

def read_data():
    global settings
    with open("Settings", "r", encoding="utf-8") as file:
        settings = json.load(file)

def write_data():
    global settings
    with open("Settings", "w", encoding="utf-8") as file:
        json.dump(settings, file)
read_data()


Knopka = QPushButton("Іграти")
Line = QLineEdit(settings["skin"])
Change = QPushButton("Change")

mainLine = QVBoxLayout()

mainLine.addWidget(Knopka)
mainLine.addWidget(Line)
mainLine.addWidget(Change)


window.setLayout(mainLine)

def change_data():
    settings["skin"] = Line.text()
    write_data()

Knopka.clicked.connect(start_game)

Change.clicked.connect(change_data)


window.show()
app.exec()
