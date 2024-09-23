from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog

app = QApplication([])
main_window = QDialog()
#uic.loadUi('./1.Lab_AGV_run_on_pc_WIP/0.PyQt5/untitled.ui', main_window)
uic.loadUi('./untitled.ui', main_window)
main_window.show()
app.exec_()
