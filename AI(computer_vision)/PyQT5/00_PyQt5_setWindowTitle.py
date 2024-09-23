# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

app = QApplication(sys.argv)
#print(sys.argc)
print(sys.argv)
input()
if(sys.argv[1] == '1'):
    window = QWidget()
    window.setWindowTitle('Hello, World! - widget')
    window.show()
elif(sys.argv[1] == '2'):
    label = QLabel("Hello, World! - label")
    label.show()
else:
    window = QMainWindow()
    window.setWindowTitle('Hello, World! - mainwindow')
    window.show()

sys.exit(app.exec_())