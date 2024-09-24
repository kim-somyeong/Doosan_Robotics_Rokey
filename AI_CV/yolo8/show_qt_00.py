import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

#app = QApplication([])
app = QApplication(sys.argv)
win = QWidget()
btn_start = QPushButton("Camera On", win)
win.show()

sys.exit(app.exec_())
