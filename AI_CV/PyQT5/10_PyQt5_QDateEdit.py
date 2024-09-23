import sys
from PyQt5.QtWidgets import QApplication, QDateEdit, QVBoxLayout, QWidget

app = QApplication(sys.argv)                #application 관련
window = QWidget()                          #눈에 보이기 시작하는 부분 : window
window.setWindowTitle('QDateEdit Example')

# Create a QDateEdit widget
date_edit = QDateEdit()

# Layout widgets
layout = QVBoxLayout()
layout.addWidget(date_edit) #QDataEdit을 layout 안에 추가시킴 : addWidget
window.setLayout(layout)    #layout을 QWidget에 추가 : setLayer / QMainWindow <-> QWidget

# Show the window
window.show()
sys.exit(app.exec_())                       #application 관련

# QWidget (window) -> layout (layout) -> QDataedit (data_edit)