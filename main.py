from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QWidget
from PyQt5.QtCore import Qt
from menu_class import MenuClass
from KanjiWidget import KanjiWidget


class MainClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kanji_widget = None
        self.setWindowTitle("Kanji Cards")
        self.setGeometry(100, 100, 600, 400)

        layout = QGridLayout()

        title_label = QLabel("Select Grade to learn Kanji!...")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label, 0, 0, 1, 3)

        self.menu = MenuClass()
        layout.addWidget(self.menu, 1, 0, 1, 3)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.menu.selected_level.connect(self.print_level_screen)

    def print_level_screen(self, level):
        print(f"Selected level: {level}")
        self.kanji_widget = KanjiWidget(level)
        self.setCentralWidget(self.kanji_widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainClass()
    window.show()
    app.exec_()
