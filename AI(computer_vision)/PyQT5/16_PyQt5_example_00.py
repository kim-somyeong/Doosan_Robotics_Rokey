# -*- coding: utf-8 -*-
## Ex 10-1. (x, y) ��ġ �ݺ� Ŭ�� ���α׷�.
## https://codetorial.net/pyqt5/examples/repeated_click.html

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import pyautogui


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.x_le = QLineEdit(self)
        self.y_le = QLineEdit(self)
        self.delay_le = QLineEdit(self)
        self.num_le = QLineEdit(self)
        self.start_btn = QPushButton('Start', self)

        self.x, self.y, self.delay = 0, 0, 0
        self.num_click = 0
        self.initUI()

    def initUI(self):
        self.x_le.move(20, 20)
        #self.x_le.setPlaceholderText('x ��ġ')
        self.x_le.setPlaceholderText('x position')

        self.y_le.move(160, 20)
        #self.y_le.setPlaceholderText('y ��ġ')
        self.y_le.setPlaceholderText('y position')

        self.delay_le.move(20, 60)
        #self.delay_le.setPlaceholderText('Ŭ�� ���� ���� (��)')
        self.delay_le.setPlaceholderText('click interval (sec)')

        self.num_le.move(160, 60)
        #self.num_le.setPlaceholderText('Ŭ�� Ƚ��')
        self.num_le.setPlaceholderText('click count')

        self.start_btn.move(110, 100)
        self.start_btn.clicked.connect(self.start_btn_click)

        self.setWindowTitle('Click')
        self.setGeometry(400, 400, 300, 150)
        self.show()

    def start_btn_click(self):
        self.timer = QTimer()
        self.x = int(self.x_le.text())
        self.y = int(self.y_le.text())
        self.delay = int(self.delay_le.text())
        self.num_click = 0

        self.timer.start(self.delay * 1000)
        self.timer.timeout.connect(self.mouse_click)

    def mouse_click(self):
        pyautogui.click(self.x, self.y)
        self.num_click += 1

        if self.num_click == int(self.num_le.text()):
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())