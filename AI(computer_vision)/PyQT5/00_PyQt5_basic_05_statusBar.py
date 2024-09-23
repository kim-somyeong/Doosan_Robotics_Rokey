# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

app = QApplication(sys.argv)

QToolTip.setFont(QFont('SansSerif', 10))

window = QMainWindow()
window.setWindowTitle('Hello, World! - mainwindow')
window.setWindowIcon(QIcon('web.png'))
window.statusBar().showMessage('Ready')

btn = QPushButton('Quit', window)
btn.setToolTip('This is a <b>QPushButton</b> widget')
btn.move(50, 50)
btn.resize(btn.sizeHint())
btn.clicked.connect(QCoreApplication.instance().quit)


window.show()

sys.exit(app.exec_())
