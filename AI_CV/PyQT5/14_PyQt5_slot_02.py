# -*- coding: utf-8 -*-
## Ex 7-3. �̺�Ʈ �ڵ鷯 �籸���ϱ�.
## https://wikidocs.net/23755
## ESC ����
## F �ִ�ȭ
## N �ּ�ȭ

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, e):         #내장 함수
        if e.key() == Qt.Key_Escape:    #key_escape : event 
            self.close()
        elif e.key() == Qt.Key_F:
            self.showFullScreen()
        elif e.key() == Qt.Key_N:
            self.showNormal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())