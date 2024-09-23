# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QAction, qApp, QDesktopWidget, QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDate, Qt

app = QApplication(sys.argv)

QToolTip.setFont(QFont('SansSerif', 10))

window = QMainWindow()
window.setWindowTitle('Hello, World! - mainwindow')
window.setWindowIcon(QIcon('web.png'))
window.date = QDate.currentDate()
#window.statusBar().showMessage('Ready')
window.statusBar().showMessage(window.date.toString(Qt.DefaultLocaleLongDate))




'''
exitAction = QAction(QIcon('exit.png'), 'Exit', window)
exitAction.setShortcut('Ctrl+Q')
exitAction.setStatusTip('Exit application')
exitAction.triggered.connect(qApp.quit)

window.statusBar()

menubar = window.menuBar()
menubar.setNativeMenuBar(False)
filemenu = menubar.addMenu('&File')
filemenu.addAction(exitAction)
'''

exitAction = QAction(QIcon('exit.png'), 'Exit', window)
exitAction.setShortcut('Ctrl+Q')
exitAction.setStatusTip('Exit application')
exitAction.triggered.connect(qApp.quit)


window.statusBar()

window.toolbar = window.addToolBar('Exit')
window.toolbar.addAction(exitAction)



qr = window.frameGeometry()
cp = QDesktopWidget().availableGeometry().center()
qr.moveCenter(cp)
window.move(qr.topLeft())




lbl_red = QLabel('Red')
lbl_green = QLabel('Green')
lbl_blue = QLabel('Blue')

lbl_red.setStyleSheet("color: red;"
                     "border-style: solid;"
                     "border-width: 2px;"
                     "border-color: #FA8072;"
                     "border-radius: 3px")
lbl_green.setStyleSheet("color: green;"
                       "background-color: #7FFFD4")
lbl_blue.setStyleSheet("color: blue;"
                      "background-color: #87CEFA;"
                      "border-style: dashed;"
                      "border-width: 3px;"
                      "border-color: #1E90FF")

vbox = QVBoxLayout()
vbox.addWidget(lbl_red)
vbox.addWidget(lbl_green)
vbox.addWidget(lbl_blue)

widget = QWidget()

widget.setLayout(vbox)

window.setCentralWidget(widget)        ####


btn = QPushButton('Quit', window)
btn.setToolTip('This is a <b>QPushButton</b> widget')
btn.move(50, 50)
btn.resize(btn.sizeHint())
btn.clicked.connect(QCoreApplication.instance().quit)

vbox.addWidget(btn)                ####

window.show()

sys.exit(app.exec_())
