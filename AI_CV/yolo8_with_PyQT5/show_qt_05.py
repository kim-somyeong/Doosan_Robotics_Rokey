import cv2
import threading
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt5 import QtGui
from ultralytics import YOLO          ##  추가

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')            ##  추가

running = False

def run():
    global running
    cap = cv2.VideoCapture(0)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    label.resize(int(width), int(height))
    while running:
        ret, img = cap.read()
        if ret:
            results = model(img)                                                              ##  추가
            annotated_frame = results[0].plot()                                               ##  추가          #plot : bouding box가 그려진 image 생성
            annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)                ##  추가          #annoated_frame : img(BGR) -> annoated_frame(BGR) -> annoated_frame(RGB) -> QT용 img => QImage
            h,w,c = annotated_frame.shape                                                     ##  수정
            qImg = QtGui.QImage(annotated_frame.data, w, h, w*c, QtGui.QImage.Format_RGB888)  ##  수정
            pixmap = QtGui.QPixmap.fromImage(qImg)
            label.setPixmap(pixmap)
        else:
            QMessageBox.about(win, "Error", "Cannot read frame.")
            print("cannot read frame.")
            break
    cap.release()
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