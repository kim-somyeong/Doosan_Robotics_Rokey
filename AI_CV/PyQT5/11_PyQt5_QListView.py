import sys
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QListView, QVBoxLayout, QWidget

app = QApplication(sys.argv)                #QT용 process
window = QWidget()
window.setWindowTitle('QListView Example')

# Create a QListView
list_view = QListView()
model = QStringListModel(["Item 1", "Item 2", "Item 3"])
list_view.setModel(model)

# Layout widgets
layout = QVBoxLayout()   #QLIstView(list_view라는 instance)(addWidget을 통해서 포함이 됨) -> QVBoxLayout(Layout이라는 instance)(setLayout을 통해 widget에 포함) -> Widget (window라는 instance) 
layout.addWidget(list_view)
window.setLayout(layout)

# Show the window
window.show()
sys.exit(app.exec_())       #실행
