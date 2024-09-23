# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('Hello, World! - mainwindow')
window.setWindowIcon(QIcon('web.png'))   


btn = QPushButton('Quit', window) 
btn.move(50, 50)
btn.resize(btn.sizeHint())
btn.clicked.connect(QCoreApplication.instance().quit)           #btn.clicked : signal  => 클릭(signal이 발생)하면 QCoreApplication 함수를 connect 해라.


window.show()

sys.exit(app.exec_())
