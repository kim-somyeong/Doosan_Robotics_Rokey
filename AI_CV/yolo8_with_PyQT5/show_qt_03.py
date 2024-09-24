import threading                  ##  추가
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import time                       ##  추가

running = False                   ##  추가 시작         # running ==>> 전역변수
def run():                                            #함수가 아닌 thread의 main
    global running                                    #함수 안에서는 전역변수를 알려주기 위해 global running이라고 작성 
    while running:                  # running == True
        if running == False:
            break                   #stop button을 누르면 thread를 중단하라
        time.sleep(1)
        print("Thread running.")

    print("Thread end.")          ##  추가 끝

def stop():
    global running                ##  추가
    running = False               ##  추가
    print("stoped..")

def start():
    global running                     ##  추가
    running = True                     ##  추가
    th = threading.Thread(target=run)  ##  추가
    th.start()                         ##  추가
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