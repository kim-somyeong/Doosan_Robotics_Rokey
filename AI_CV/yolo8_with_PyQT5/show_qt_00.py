import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

#app = QApplication([])                     #인자를 받지 않는 경우
app = QApplication(sys.argv)                #인자를 받는 경우       #QT Application 생성
win = QWidget()
btn_start = QPushButton("Camera On", win)   #widget에서 layout 거치지 않고 widget에 puch버튼을 바로 연결
win.show()

sys.exit(app.exec_())
