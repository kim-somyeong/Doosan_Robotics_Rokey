# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel    #library import

app = QApplication(sys.argv)      #QT.application 생성  => process => main 

# event loop에 들어오기 전에 main 창을 만들고, 화면에 표시
window = QMainWindow()
window.setWindowTitle('Hello, World! - mainwindow')   #창의 title
window.show()

sys.exit(app.exec_())   #app.exec_() : event loop 안으로 들어온다. 