import cv2

import threading

import sys

from PyQt5 import QtWidgets

from PyQt5 import QtGui

from PyQt5 import QtCore

from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

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

            results = model(img)

            annotated_frame = results[0].plot()

            annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

            h,w,c = annotated_frame.shape

            qImg = QtGui.QImage(annotated_frame.data, w, h, w*c, QtGui.QImage.Format_RGB888)

            pixmap = QtGui.QPixmap.fromImage(qImg)

            label.setPixmap(pixmap)
        else:

            QtWidgets.QMessageBox.about(win, "Error", "Cannot read frame.")

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
app = QtWidgets.QApplication([])

win = QtWidgets.QWidget()       #QWidget

vbox = QtWidgets.QVBoxLayout()  #vbox : layer

label = QtWidgets.QLabel()

btn_start = QtWidgets.QPushButton("Camera On")

btn_stop = QtWidgets.QPushButton("Camera Off")

vbox.addWidget(label)
vbox.addWidget(btn_start)
vbox.addWidget(btn_stop)
win.setLayout(vbox)
win.show()

btn_start.clicked.connect(start)
btn_stop.clicked.connect(stop)
app.aboutToQuit.connect(onExit)

sys.exit(app.exec_())
