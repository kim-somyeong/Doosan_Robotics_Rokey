import sys
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QListView, QVBoxLayout, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QListView Example')

# Create a QListView
list_view = QListView()
model = QStringListModel(["Item 1", "Item 2", "Item 3"])
list_view.setModel(model)

# Layout widgets
layout = QVBoxLayout()
layout.addWidget(list_view)
window.setLayout(layout)

# Show the window
window.show()
sys.exit(app.exec_())
