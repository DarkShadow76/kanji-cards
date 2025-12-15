from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QWidget
from PyQt5 import QtCore
from menu_class import MenuClass
from KanjiWidget import KanjiWidget
from typing import List, Optional


class MainClass(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.kanji_widget: Optional[KanjiWidget] = None
        self.setWindowTitle("Kanji Cards")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.grid_layout = QGridLayout(self.central_widget)

        self.title_label = QLabel("Select Grade to learn Kanji!...")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.title_label, 0, 0, 1, 3)

        self.menu = MenuClass()
        self.grid_layout.addWidget(self.menu, 1, 0, 1, 3)

        self.setCentralWidget(self.central_widget)

        self.menu.selected_level.connect(self.show_kanji_screen)
        self.menu.custom_list_selected.connect(self.handle_custom_list)

    def show_kanji_screen(self, level: int) -> None:
        print(f"Selected level: {level}")
        self.kanji_widget = KanjiWidget(level)
        self.kanji_widget.back_button_clicked.connect(self.show_menu)
        self.setCentralWidget(self.kanji_widget)

    def handle_custom_list(self, kanji_list: List[str]) -> None:
        if kanji_list:
            print(f"Loaded {len(kanji_list)} Custom Kanjis")
            self.kanji_widget = KanjiWidget(kanji_list)
            self.kanji_widget.back_button_clicked.connect(self.show_menu)
            self.setCentralWidget(self.kanji_widget)
        else:
            print("Custom Kanji list empty or failed to load")
    
    def show_menu(self) -> None:
        self.setCentralWidget(self.central_widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainClass()
    window.show()
    app.exec_()
