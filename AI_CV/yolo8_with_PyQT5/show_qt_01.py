import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def start():                        ## 추가
    print("started..")              ## 추가

app = QApplication([])
win = QWidget()
btn_start = QPushButton("Camera On", win)
win.show()

btn_start.clicked.connect(start)    ## 추가     #signal과 slot 연결

sys.exit(app.exec_())
