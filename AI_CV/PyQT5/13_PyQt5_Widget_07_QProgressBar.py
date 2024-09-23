## Ex 5-7. QProgressBar.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)              #timer에서 동작됨
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)       #event 발생
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)     #btn.clicked이 발생하면 isActive()로 간다

        self.timer = QBasicTimer()                  #basic timer setting / 화면이 없음 
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')       #timer를 동작시켜라.
        else:
            self.timer.start(100, self)     #100ms마다 한번씩 반복해서 호출 
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())