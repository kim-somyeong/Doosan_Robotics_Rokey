# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QAction, qApp
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

app = QApplication(sys.argv)

QToolTip.setFont(QFont('SansSerif', 10))

window = QMainWindow()
window.setWindowTitle('Hello, World! - mainwindow')
window.setWindowIcon(QIcon('web.png'))
window.statusBar().showMessage('Ready')

#각각의 기능 추가
exitAction = QAction(QIcon('exit.png'), 'Exit', window)
exitAction.setShortcut('Ctrl+Q')
exitAction.setStatusTip('Exit application')
exitAction.triggered.connect(qApp.quit)     #triggered : signal, quit : slot  => signal, slot connect

window.statusBar()

menubar = window.menuBar()
menubar.setNativeMenuBar(False)
filemenu = menubar.addMenu('&File')         #filemenu에 추가        #addmenu를 통해 instance 생성
filemenu.addAction(exitAction)


btn = QPushButton('Quit', window)
btn.setToolTip('This is a <b>QPushButton</b> widget')
btn.move(50, 50)
btn.resize(btn.sizeHint())
btn.clicked.connect(QCoreApplication.instance().quit)


window.show()

sys.exit(app.exec_())