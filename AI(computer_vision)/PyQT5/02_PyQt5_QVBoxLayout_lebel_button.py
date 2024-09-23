from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

# Widgets
label = QLabel('Hello, PyQt5!')
button = QPushButton('Click Me')

# Adding widgets to the layout
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()
app.exec_()
