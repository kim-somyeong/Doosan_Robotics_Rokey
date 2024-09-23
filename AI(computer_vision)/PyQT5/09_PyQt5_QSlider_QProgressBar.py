import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QProgressBar, QSlider, QVBoxLayout, QWidget

# Initialize the application
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QSlider and QProgressBar Example')

# Create slider and progress bar
slider = QSlider(Qt.Horizontal)
progress_bar = QProgressBar()

# Set the range of slider and progress bar
slider.setRange(0, 100)
progress_bar.setRange(0, 100)

# Connect the slider's valueChanged signal to the progress bar's setValue slot
slider.valueChanged.connect(progress_bar.setValue)

# Layout widgets
layout = QVBoxLayout()
layout.addWidget(slider)
layout.addWidget(progress_bar)
window.setLayout(layout)

# Show the window
window.show()
sys.exit(app.exec_())
