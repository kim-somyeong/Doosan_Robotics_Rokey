import cv2
import threading
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPointF, QTimer, QRectF, Qt, QLineF
import math
from ultralytics import YOLO    


class MyJoystick(QWidget):
	def __init__(self, cbJoyPos=None, parent=None): # 조이스틱 초기화 함수
		super(MyJoystick, self).__init__(parent)
		self.setMinimumSize(200, 200)				#창의 최소 크기를 (200,200)
		self.movingOffset = QPointF(0, 0)
		self.grabCenter = False						#center에 있지 않을 경우 False
		self.__maxDistance = 50

		#timer setting
		self.timer = QTimer(self)		#event마다 출력이 아닌 일정한 시간마다 출력되도록 
		self.timer.setInterval(10)		#10ms : 1초에 10번 발생하도록
		self.timer.timeout.connect(self.timeout)	#timer.timeout을 timeout이라는 method에 connect
		self.timer.start()

		self.cbJoyPos = cbJoyPos	#함수명을 등록 (함수 포인터)

	def paintEvent(self, event): # 조이스틱을 그리는 함수
		painter = QPainter(self)
		bounds = QRectF(
		-self.__maxDistance,
		-self.__maxDistance,
		self.__maxDistance * 2,
		self.__maxDistance * 2
		).translated(self._center())
		painter.drawEllipse(bounds)
		painter.setBrush(Qt.black)
		painter.drawEllipse(self._centerEllipse())

	def _centerEllipse(self): # 조이스틱 손잡이 영역
		if self.grabCenter:
			return QRectF(-20, -20, 40, 40).\
			translated(self.movingOffset)
		return QRectF(-20, -20, 40, 40).translated(self._center())

	def _center(self): # 조이스틱 중심
		return QPointF(self.width()/2, self.height()/2)

	def _boundJoystick(self, point): # 조이스틱 손잡이 움직임 경계 제한
		limitLine = QLineF(self._center(), point)
		if (limitLine.length() > self.__maxDistance):
			limitLine.setLength(self.__maxDistance)
		return limitLine.p2()

	def joystickPosition(self): # 조이스틱 손잡이 현재 위치
		if not self.grabCenter:
			return (0, 0)
		normVector = QLineF(self._center(), self.movingOffset)
		currentDistance = normVector.length()
		angle = normVector.angle()

		distance = min(currentDistance / self.__maxDistance, 1.0)

		posX = math.cos(angle*math.pi/180)*distance
		posY = math.sin(angle*math.pi/180)*distance

		return (posX, posY)

	def mousePressEvent(self, ev): # 조이스틱 손잡이 잡는 함수
		self.grabCenter = self._centerEllipse().contains(ev.pos())
		return super().mousePressEvent(ev)

	def mouseReleaseEvent(self, event): # 조이스틱 손잡이 놓는 함수
		self.grabCenter = False
		self.movingOffset = QPointF(0, 0)
		self.update()

	def mouseMoveEvent(self, event):    # 조이스틱 손잡이 움직이는 함수
		if self.grabCenter:
			self.movingOffset = self._boundJoystick(event.pos())
			self.update()
		if self.cbJoyPos != None :
			self.cbJoyPos(self.joystickPosition())

	def timeout(self):                  # 주기적으로 조이스틱 손잡이 위치를 알려주는 함수
		sender = self.sender()
		if id(sender) == id(self.timer):
			if self.cbJoyPos != None :
				self.cbJoyPos(self.joystickPosition())

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
    
def cbJoyPos(joystickPosition):
	print(joystickPosition)

app = QApplication([])
win = QWidget()
vbox = QVBoxLayout()

label = QLabel()
vbox.addWidget(label)

btn_start = QPushButton("Camera On")
vbox.addWidget(btn_start)
btn_start.clicked.connect(start)

btn_mid=MyJoystick(cbJoyPos)
vbox.addWidget(btn_mid)

btn_stop = QPushButton("Camera Off")
vbox.addWidget(btn_stop)
btn_stop.clicked.connect(stop)

app.aboutToQuit.connect(onExit)

win.setLayout(vbox)
win.show()



sys.exit(app.exec_())