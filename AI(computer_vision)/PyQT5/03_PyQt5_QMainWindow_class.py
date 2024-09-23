from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class CustomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Event Handling')
        self.button = QPushButton('Press Me', self)
        self.button.clicked.connect(self.on_button_clicked)
        self.setCentralWidget(self.button)

    def on_button_clicked(self):
        print("Button clicked!")

app = QApplication([])
mainWin = CustomMainWindow()
mainWin.show()
app.exec_()
