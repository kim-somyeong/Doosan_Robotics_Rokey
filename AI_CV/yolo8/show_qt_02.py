import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

def stop():
    print("stoped..")

def start():
    print("started..")

def onExit():
    print("exit")
    stop()

app = QApplication([])
win = QWidget()
vbox = QVBoxLayout()
btn_start = QPushButton("Camera On")
btn_stop = QPushButton("Camera Off")

vbox.addWidget(btn_start)
vbox.addWidget(btn_stop)
win.setLayout(vbox)
win.show()

btn_start.clicked.connect(start)
btn_stop.clicked.connect(stop)
app.aboutToQuit.connect(onExit)

sys.exit(app.exec_())
