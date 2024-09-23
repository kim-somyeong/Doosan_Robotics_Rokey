# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('Hello, World! - mainwindow')
window.show()

sys.exit(app.exec_())