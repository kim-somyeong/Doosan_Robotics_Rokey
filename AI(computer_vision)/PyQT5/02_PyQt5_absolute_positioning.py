# -*- coding: utf-8 -*-
## Ex 4-1. 절대적 배치.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

app = QApplication([])
window = QWidget()


label1 = QLabel('Label1', window)
label1.move(20, 20)
label2 = QLabel('Label2', window)
label2.move(20, 60)

btn1 = QPushButton('Button1', window)
btn1.move(80, 13)
btn2 = QPushButton('Button2', window)
btn2.move(80, 53)

window.setWindowTitle('Absolute Positioning')
window.setGeometry(300, 300, 400, 200)
window.show()

app.exec_()