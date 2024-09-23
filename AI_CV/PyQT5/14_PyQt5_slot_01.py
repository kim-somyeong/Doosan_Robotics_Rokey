# -*- coding: utf-8 -*-
#https://wikidocs.net/22023
#Ex 7-2. �̺�Ʈ �ڵ鷯 �����.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):   #각각 widget 4개
        lcd = QLCDNumber(self)
        dial = QDial(self)
        btn1 = QPushButton('Big', self)
        btn2 = QPushButton('Small', self)

        hbox = QHBoxLayout()        #botton 2개는 HBox로 묶음
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()        #vbox : lcd + dial + hbox
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)  #dial.valueChange -> lcd.display에 표시
        btn1.clicked.connect(self.resizeBig)    #btn1.clicked -> resizeBig => costom
        btn2.clicked.connect(self.resizeSmall)  #btn2.clicked -> resizeSmall => costom

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(200, 200, 200, 250)
        self.show()

    def resizeBig(self):        #self : 최상위 widget
        self.resize(400, 500)

    def resizeSmall(self):
        self.resize(200, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())