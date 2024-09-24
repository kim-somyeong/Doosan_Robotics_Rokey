import cv2                                        ##  추가
import threading
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt5 import QtGui

running = False
def run():
    global running
    cap = cv2.VideoCapture(0)                     ##  추가 시작
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    label.resize(int(width), int(height))           #(640, 480)만큼 resize
    while running:
        ret, img = cap.read()
        if ret:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h,w,c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            label.setPixmap(pixmap)         #해당되는 pixel값 pixmap을 넣어준다.
        else:
            QMessageBox.about(win, "Error", "Cannot read frame.")
            print("cannot read frame.")
            break
    print("Thread end.")                          ##  추가 끝

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
label = QLabel()                        #QT에 image를 출력할 수 있는 공간 => Qlabel
btn_start = QPushButton("Camera On")
btn_stop = QPushButton("Camera Off")


vbox.addWidget(label)       #button보다 위에 있어야 함. 
vbox.addWidget(btn_start)
vbox.addWidget(btn_stop)
win.setLayout(vbox)
win.show()

btn_start.clicked.connect(start)
btn_stop.clicked.connect(stop)
app.aboutToQuit.connect(onExit)

sys.exit(app.exec_())