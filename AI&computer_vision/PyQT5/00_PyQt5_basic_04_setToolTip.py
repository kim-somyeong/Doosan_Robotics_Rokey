# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

app = QApplication(sys.argv)

QToolTip.setFont(QFont('SansSerif', 10))        #폰트

window = QMainWindow()
window.setWindowTitle('setToolTip - mainwindow')     #창의 타이틀 
window.setWindowIcon(QIcon('web.png'))

#위젯에 마우스를 올리면 위젯의 기능을 설명하는 역할 
btn = QPushButton('Quit', window)
btn.setToolTip('This is a <b>QPushButton</b> widget')   #setToolTip : 해당 문장이 출력되도록 
btn.move(50, 50)
btn.resize(btn.sizeHint())
btn.clicked.connect(QCoreApplication.instance().quit)


window.show()

sys.exit(app.exec_())
