from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class ExampleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dialogs Example')
        self.button = QPushButton('Open Dialog', self)  #버튼 생성
        self.button.clicked.connect(self.showDialog)    #버튼 클릭 되면 self.showDialog로 와라
        self.setCentralWidget(self.button)

    def showDialog(self):
        QMessageBox.information(self, 'Message', 'This is a dialog.')

app = QApplication([])      #QApplication 생성
ex = ExampleApp()           #화면 구성 및 연결      #class에서 실행
ex.show()
app.exec_()                 #event loop가 돌다가 버튼 클릭되면 메세지 박스를 하나 띄우겠다.
