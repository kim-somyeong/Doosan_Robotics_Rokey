#myjoystick.py

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPointF, QRectF, Qt

class MyJoystick(QWidget):
	def __init__(self, parent=None): # 조이스틱 초기화 함수
		super(MyJoystick, self).__init__(parent)
		self.setMinimumSize(200, 200)
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

	def _center(self): # 조이스틱 중심
		return QPointF(self.width()/2, self.height()/2)


from PyQt5.QtWidgets import  QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyJoystick()
    window.show()
    sys.exit(app.exec_())
