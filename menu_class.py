from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import pyqtSignal


class MenuClass(QWidget):
    selected_level = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout()

        for i in range(2):
            for j in range(3):
                level = i * 3 + j + 1
                button = QPushButton(f"Level {level}")
                button.clicked.connect(lambda checked, level_k=level: self.on_button_clicked(level_k))
                layout.addWidget(button, i, j)

        self.setLayout(layout)

    def on_button_clicked(self, level):
        self.selected_level.emit(level)
