from PyQt5.QtWidgets import QApplication, QPushButton

def on_button_clicked():
    print("Button has been clicked")

app = QApplication([])
button = QPushButton('Click Me')
button.clicked.connect(on_button_clicked)  # Connecting the clicked signal to the slot
button.show()
app.exec_()
