import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from Kanji_API import KanjiAPI


class KanjiWidget(QWidget):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.setWindowTitle("Kanji Widget")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.kanji_label = QLabel()
        self.kanji_info_label = QLabel()

        self.layout.addWidget(self.kanji_label)
        self.layout.addWidget(self.kanji_info_label)

        self.button_next = QPushButton("Next Kanji")
        self.button_next.clicked.connect(self.show_kanji_info)

        self.layout.addWidget(self.button_next)

        self.setLayout(self.layout)
        self.show_kanji_info()

    def show_kanji_info(self):
        kanji_api = KanjiAPI(self.level)
        kanji = kanji_api.get_random_kanji()
        kanji_info = kanji_api.get_kanji_info(kanji)

        info_text = f"Grade: {kanji_info['grade']}\n"
        info_text += f"Heisig EN: {kanji_info['heisig_en']}\n"
        info_text += f"JLPT: {kanji_info['jlpt']}\n"
        info_text += f"Kanji: {kanji_info['kanji']}\n"
        info_text += f"Kun Readings: {', '.join(kanji_info['kun_readings'])}\n"
        info_text += f"Meanings: {', '.join(kanji_info['meanings'])}\n"
        info_text += f"Name Readings: {', '.join(kanji_info['name_readings'])}\n"
        info_text += f"Notes: {', '.join(kanji_info['notes'])}\n"
        info_text += f"On Readings: {', '.join(kanji_info['on_readings'])}\n"
        info_text += f"Stroke Count: {kanji_info['stroke_count']}\n"
        info_text += f"Unicode: {kanji_info['unicode']}\n"

        self.kanji_label.setText(kanji)
        self.kanji_label.setStyleSheet("font-size: 60px;")

        self.kanji_info_label.setText(info_text)
        self.kanji_info_label.setStyleSheet("font-size: 20px;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KanjiWidget(1)
    window.show()
    sys.exit(app.exec_())
