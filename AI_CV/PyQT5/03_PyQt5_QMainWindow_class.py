from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class CustomMainWindow(QMainWindow):        #class가 mainwindow를 상속 받는다
    def __init__(self):
        super().__init__()
        self.initUI()   #생성되자마자

    def initUI(self):   #바로 실행               #self -> QMainWindow
        self.setWindowTitle('Event Handling')
        self.button = QPushButton('Press Me', self)
        self.button.clicked.connect(self.on_button_clicked)
        self.setCentralWidget(self.button)

    def on_button_clicked(self):
        print("Button clicked!")

app = QApplication([])  #application 생성
mainWin = CustomMainWindow()            #화면 구성 및 연결
mainWin.show()          #event loop를 돌다가 event가 발생하면 해당 된 함수를 호출 (signal-slot 관계)
app.exec_()             #application 실행
