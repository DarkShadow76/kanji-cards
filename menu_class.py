from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QMessageBox
from PyQt5 import QtCore
from typing import List


class MenuClass(QWidget):
    selected_level = QtCore.pyqtSignal(int)
    custom_list_selected = QtCore.pyqtSignal(list)

    def __init__(self) -> None:
        super().__init__()
        self.custom_list: QPushButton
        self.setup_ui()

    def setup_ui(self) -> None:
        layout = QGridLayout()

        for i in range(2):
            for j in range(3):
                level = i * 3 + j + 1
                button = QPushButton(f"Level {level}")
                button.clicked.connect(lambda checked, level_k=level: self.on_button_clicked(level_k))
                layout.addWidget(button, i, j)
        
        self.custom_list = QPushButton("Custom Kanji List")
        self.custom_list.clicked.connect(self.load_custom_list)
        layout.addWidget(self.custom_list, 2, 0, 1, 3)

        self.setLayout(layout)

    def on_button_clicked(self, level: int) -> None:
        self.selected_level.emit(level)

    def load_custom_list(self) -> None:
        try:
            with open('custom_kanji.txt', 'r', encoding='utf-8') as f:
                kanji_list: List[str] = [line.strip() for line in f if line.strip()]
                self.custom_list_selected.emit(kanji_list)
        except FileNotFoundError:
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Warning)
            error_message.setText("File 'custom_kanji.txt' not found in the directory.")
            error_message.setWindowTitle("File Not Found")
            error_message.exec_()
        except Exception as e:
            print(f"Error at read file: {e}")