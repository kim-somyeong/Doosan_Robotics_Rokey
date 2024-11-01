# -*- coding: utf-8 -*-
## Ex 8-5. �ٰ��� �׸��� (drawPolygon).
## https://codetorial.net/pyqt5/paint/drawing_polygon.html

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont, QPolygon
from PyQt5.QtCore import Qt, QPoint


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawPolygon')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_polygon(qp)
        qp.end()

    def draw_polygon(self, qp):         #draw_polygon 함수 호출
        points1 = [                     #좌표값
            QPoint(20, 20),
            QPoint(200, 80),
            QPoint(150, 135),
            QPoint(50, 115)
        ]
        polygon1 = QPolygon(points1)    #포인트들로 polygon draw
        qp.setPen(QPen(Qt.black, 3))    #색깔 & 굵기
        qp.drawPolygon(polygon1)        #draw

        points2 = [
            QPoint(220, 30),
            QPoint(360, 10),
            QPoint(250, 135)
        ]
        polygon2 = QPolygon(points2)
        qp.setPen(QPen(Qt.red, 5, Qt.DashLine)) #바깥 선 색깔
        qp.setBrush(QBrush(Qt.yellow))          #안에 채우는 색깔 
        qp.drawPolygon(polygon2)

        points3 = [
            QPoint(95, 140),
            QPoint(120, 190),
            QPoint(185, 205),
            QPoint(125, 230),
            QPoint(140, 280),
            QPoint(100, 230),
            QPoint(70, 280),
            QPoint(60, 220),
            QPoint(15, 190),
            QPoint(65, 180),
        ]
        polygon3 = QPolygon(points3)
        qp.setPen(QPen(QColor('#1C91CF'), 4, Qt.DashDotDotLine))
        qp.setBrush(QBrush(QColor('#37CF1C'), Qt.CrossPattern))
        qp.drawPolygon(polygon3)

        points4 = [
            QPoint(290, 160),
            QPoint(360, 190),
            QPoint(335, 280),
            QPoint(255, 270),
            QPoint(230, 195)
        ]
        polygon4 = QPolygon(points4)
        qp.setPen(QPen(QColor('#7B33D1'), 3))
        qp.setBrush(QBrush(QColor('#D187EF')))
        qp.drawPolygon(polygon4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())