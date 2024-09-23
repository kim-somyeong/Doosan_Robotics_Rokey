import sys
from PyQt5.QtWidgets import QApplication, QDateEdit, QVBoxLayout, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QDateEdit Example')

# Create a QDateEdit widget
date_edit = QDateEdit()

# Layout widgets
layout = QVBoxLayout()
layout.addWidget(date_edit)
window.setLayout(layout)

# Show the window
window.show()
sys.exit(app.exec_())
