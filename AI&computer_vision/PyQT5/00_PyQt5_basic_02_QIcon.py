# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('Hello, World! - mainwindow')
window.setWindowIcon(QIcon('web.png'))
window.show()

sys.exit(app.exec_())
