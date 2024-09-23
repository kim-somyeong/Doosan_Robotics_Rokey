import sys
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from PyQt5.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget

class MyTableModel(QAbstractTableModel):
    def rowCount(self, parent=QModelIndex()):
        return 3  # Example row count

    def columnCount(self, parent=QModelIndex()):
        return 2  # Example column count

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return QVariant(f"Row {index.row()}, Column {index.column()}")
        return QVariant()

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QTableView Example')

# Create a QTableView
table_view = QTableView()
model = MyTableModel()
table_view.setModel(model)

# Layout widgets
layout = QVBoxLayout()
layout.addWidget(table_view)
window.setLayout(layout)

# Show the window
window.show()
sys.exit(app.exec_())
