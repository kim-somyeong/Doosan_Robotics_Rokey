#myjoystick.py

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPointF, QTimer, QRectF, Qt, QLineF
import math

class MyJoystick(QWidget):
	def __init__(self, parent=None): # 조이스틱 초기화 함수
		super(MyJoystick, self).__init__(parent)
		self.setMinimumSize(200, 200)
		self.movingOffset = QPointF(0, 0)
		self.grabCenter = False
		self.__maxDistance = 50


	def paintEvent(self, event): # 조이스틱을 그리는 함수
		painter = QPainter(self)
		bounds = QRectF(
		-self.__maxDistance,
		-self.__maxDistance,
		self.__maxDistance * 2,
		self.__maxDistance * 2
		).translated(self._center())
		print(bounds)     ##### add for debug
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

	def mousePressEvent(self, ev): # 조이스틱 손잡이 잡는 함수
		self.grabCenter = self._centerEllipse().contains(ev.pos())
		print(self.grabCenter, ev.pos())     ##### add for debug
		return super().mousePressEvent(ev)

	def mouseReleaseEvent(self, event): # 조이스틱 손잡이 놓는 함수
		self.grabCenter = False
		print(event)     ##### add for debug
		self.movingOffset = QPointF(0, 0)
		self.update()

from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyJoystick()
    window.show()
    sys.exit(app.exec_())
