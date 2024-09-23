import sys
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from PyQt5.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget

class MyTableModel(QAbstractTableModel):            #QAstractTableModel을 상속 받음.
    def rowCount(self, parent=QModelIndex()):
        return 3  # Example row count

    def columnCount(self, parent=QModelIndex()):
        return 2  # Example column count

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return QVariant(f"Row {index.row()}, Column {index.column()}")
        return QVariant()

app = QApplication(sys.argv)                #application
window = QWidget()                          #window
window.setWindowTitle('QTableView Example') #window

# Create a QTableView
table_view = QTableView()
model = MyTableModel()                      #class 
table_view.setModel(model)

# Layout widgets
layout = QVBoxLayout()
layout.addWidget(table_view)                #layout 연결
window.setLayout(layout)                    #window 연결

# Show the window
window.show()
sys.exit(app.exec_())                       #application
