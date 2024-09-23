# -*- coding: utf-8 -*-
## Ex 10-3. ���� ������ ���α׷�.
## https://codetorial.net/pyqt5/examples/translator.html

import sys
from PyQt5.QtWidgets import *
from googletrans import Translator


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        #self.lbl1 = QLabel('�ѱ���:', self)
        #self.lbl2 = QLabel('����:', self)
        self.lbl1 = QLabel('Korean:', self)
        self.lbl2 = QLabel('English:', self)
        self.le = QLineEdit(self)
        self.te = QTextEdit(self)
        #self.trans_btn = QPushButton('����', self)
        self.trans_btn = QPushButton('translation', self)
        self.translator = Translator()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.le)
        vbox.addWidget(self.lbl2)
        vbox.addWidget(self.te)
        vbox.addWidget(self.trans_btn)
        self.setLayout(vbox)

        self.trans_btn.clicked.connect(self.translate_kor)
        self.le.editingFinished.connect(self.translate_kor)

        self.setWindowTitle('Google Translator')
        self.setGeometry(200, 200, 400, 300)
        self.show()

    def translate_kor(self):
        text_kor = self.le.text()
        text_en = self.translator.translate(text_kor).text
        self.te.setText(text_en)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
