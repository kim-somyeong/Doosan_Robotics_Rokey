import cv2
import threading
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMessageBox
from PyQt5 import QtGui
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('../Downloads/amr_best(1).pt')

running = True  # 시작 시 카메라 실행 상태로 설정

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
            h, w, c = annotated_frame.shape
            qImg = QtGui.QImage(annotated_frame.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            label.setPixmap(pixmap)
        else:
            QMessageBox.about(win, "Error", "Cannot read frame.")
            print("Cannot read frame.")
            break
    cap.release()
    print("Thread end.")

def stop():
    global running
    running = False
    print("Stopped.")

def onExit():
    print("Exiting")
    stop()

app = QApplication([])
win = QWidget()
vbox = QVBoxLayout()
label = QLabel()
vbox.addWidget(label)
win.setLayout(vbox)
win.show()

# 코드 실행 시 바로 run() 함수 실행
th = threading.Thread(target=run)
th.start()

app.aboutToQuit.connect(onExit)
sys.exit(app.exec_())
