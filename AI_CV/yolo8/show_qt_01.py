import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def start():
    print("started..")

app = QApplication([])
win = QWidget()
btn_start = QPushButton("Camera On", win)
win.show()

btn_start.clicked.connect(start)

sys.exit(app.exec_())
