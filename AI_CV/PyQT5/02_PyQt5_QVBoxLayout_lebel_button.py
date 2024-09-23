from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

app = QApplication([])
window = QWidget()              #widget 생성
layout = QVBoxLayout()

# Widgets       #2개 widget 생성
label = QLabel('Hello, PyQt5!')
button = QPushButton('Click Me')

# Adding widgets to the layout
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()
app.exec_()     #event loop
