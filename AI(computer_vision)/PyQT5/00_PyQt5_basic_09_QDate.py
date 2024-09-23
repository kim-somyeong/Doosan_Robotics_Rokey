# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QAction, qApp, QDesktopWidget
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

btn = QPushButton('Quit', window)
btn.setToolTip('This is a <b>QPushButton</b> widget')
btn.move(50, 50)
btn.resize(btn.sizeHint())
btn.clicked.connect(QCoreApplication.instance().quit)


window.show()

sys.exit(app.exec_())