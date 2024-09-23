#myjoystick.py

from PyQt5.QtWidgets import QWidget

class MyJoystick(QWidget):
	def __init__(self, parent=None): # 조이스틱 초기화 함수
		super(MyJoystick, self).__init__(parent)
		self.setMinimumSize(200, 200)
		#self.setMinimumSize(400, 400)
		#self.setMinimumSize(10, 10)

from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyJoystick()
    window.show()
    sys.exit(app.exec_())
