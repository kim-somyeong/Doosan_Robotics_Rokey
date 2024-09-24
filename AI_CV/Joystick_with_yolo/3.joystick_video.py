import cv2
import threading
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
				
from myjoystick import MyJoystick


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










			
def cbJoyPos(joystickPosition) :
	posX, posY = joystickPosition
		
	# 자동차 방향
	right, left = -1, -1
	if posY < -0.5:
		right, left = 1, 1
		print('brake')
	elif posY > 0.15 :
		if -0.15 <= posX <= 0.15 :
			right, left = 0, 0
			print('forward')
		elif posX < -0.15 : 
			right, left = 1, 0
			print('left')
		elif posX > 0.15 :
			right, left = 0, 1
			print('right')
	else : # -0.5 <= posY <= 0.15
		print('stop driving')

# Create main application window
app = QApplication([])
app.setStyle(QStyleFactory.create("Cleanlooks"))
mw = QMainWindow()
mw.setWindowTitle('AGV Joystick')
mw.setGeometry(100, 100, 300, 200)

# Create and set widget layout
# Main widget container
cw = QWidget()
ml = QGridLayout()
cw.setLayout(ml)
mw.setCentralWidget(cw)

label = QLabel()
ml.addWidget(label,0,0)

# Create joystick
joystick = MyJoystick(cbJoyPos)
ml.addWidget(joystick,1,0)

btn_start = QPushButton("Camera On")
ml.addWidget(btn_start,2,0)
btn_start.clicked.connect(start)

btn_stop = QPushButton("Camera Off")
ml.addWidget(btn_stop,3,0)
btn_stop.clicked.connect(stop)

app.aboutToQuit.connect(onExit)


mw.show()

# Start Qt event loop 
sys.exit(app.exec_())