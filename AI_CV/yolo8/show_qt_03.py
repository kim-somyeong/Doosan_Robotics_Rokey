import threading
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import time

running = False
def run():
    global running
    while running:
        if running == False:
            break
        time.sleep(1) 
        print("Thread running.")

    print("Thread end.")

def stop():
    global running
    running = False
    print("stoped..")

def start():
    global running
    running = True
    th = threading.Thread(target=run)
    th.start()
    print("started..")

def onExit():
    print("exit")
    stop()

app = QApplication([])
win = QWidget()
vbox = QVBoxLayout()
label = QLabel()
btn_start = QPushButton("Camera On")
btn_stop = QPushButton("Camera Off")


vbox.addWidget(label)
vbox.addWidget(btn_start)
vbox.addWidget(btn_stop)
win.setLayout(vbox)
win.show()

btn_start.clicked.connect(start)
btn_stop.clicked.connect(stop)
app.aboutToQuit.connect(onExit)

sys.exit(app.exec_())
