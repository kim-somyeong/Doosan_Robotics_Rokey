import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

def stop():              ##  추가
    print("stoped..")    ##  추가

def start():
    print("started..")

def onExit():           ##  추가
    print("exit")       ##  추가
    stop()              ##  추가

app = QApplication([])
win = QWidget()
vbox = QVBoxLayout()                    ##  추가
btn_start = QPushButton("Camera On")    ##  수정        #window에서 연결 되던 것을 vbox에 addWidget 연결 
btn_stop = QPushButton("Camera Off")    ##  추가

vbox.addWidget(btn_start)               ##  추가
vbox.addWidget(btn_stop)                ##  추가
win.setLayout(vbox)                     ##  추가        #setLayout을 통해 win에 연결
win.show()

btn_start.clicked.connect(start)
btn_stop.clicked.connect(stop)          ##  추가
app.aboutToQuit.connect(onExit)         ##  추가        #x를 눌으면 aboutToQuit이라는 event가 발생 (onExit로 간다.)

sys.exit(app.exec_())