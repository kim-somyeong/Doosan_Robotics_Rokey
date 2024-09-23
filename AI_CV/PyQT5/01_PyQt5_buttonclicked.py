from PyQt5.QtWidgets import QApplication, QPushButton

def on_button_clicked():                #기능 지정 : button clicked -> on_button_clicked function 호출 / 내가 직접 정의한 custom 기능(function) 호출
    print("Button has been clicked")

app = QApplication([])
button = QPushButton('Click Me')
button.clicked.connect(on_button_clicked)  # Connecting the clicked signal to the slot      #button.clicked : signal(event), on_button_clicked : slot
button.show()
app.exec_()
