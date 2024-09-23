from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class ExampleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dialogs Example')
        self.button = QPushButton('Open Dialog', self)
        self.button.clicked.connect(self.showDialog)
        self.setCentralWidget(self.button)

    def showDialog(self):
        QMessageBox.information(self, 'Message', 'This is a dialog.')

app = QApplication([])
ex = ExampleApp()
ex.show()
app.exec_()
