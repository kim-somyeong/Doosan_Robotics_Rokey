# -*- coding: utf-8 -*-
## Ex 8-9. 파이 그리기 (drawPie).
## https://codetorial.net/pyqt5/paint/drawing_pie.html

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawPie')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_pie(qp)
        qp.end()

    def draw_pie(self, qp):
        qp.setPen(QPen(Qt.black, 3))
        qp.drawPie(20, 20, 100, 100, 0 * 16, 30 * 16)
        qp.drawText(60, 100, '30 degree')

        qp.drawPie(150, 20, 100, 100, 0 * 16, 60 * 16)
        qp.drawText(190, 100, '60 degree')

        qp.drawPie(280, 20, 100, 100, 0 * 16, 90 * 16)
        qp.drawText(320, 100, '90 degree')

        qp.drawPie(20, 140, 100, 100, 0 * 16, 180 * 16)
        qp.drawText(60, 270, '180 degree')

        qp.drawPie(150, 140, 100, 100, 0 * 16, 270 * 16)
        qp.drawText(190, 270, '270 degree')

        qp.drawPie(280, 140, 100, 100, 0 * 16, 360 * 16)
        qp.drawText(320, 270, '360 degree')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())