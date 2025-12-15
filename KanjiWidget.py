from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QGridLayout, QTextEdit
from PyQt5 import QtCore
from Kanji_API import KanjiAPI
from typing import Union, List


class KanjiWidget(QWidget):
    back_button_clicked = QtCore.pyqtSignal()

    def __init__(self, level: Union[int, List[str]]) -> None:
        super().__init__()
        self.level: Union[int, List[str]] = level
        self.setWindowTitle("Kanji Widget")
        self.setGeometry(100, 100, 800, 600)

        self.grid_layout = QGridLayout()

        self.kanji_label = QLabel()
        self.kanji_label.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.kanji_label, 0, 0, 2, 1)

        self.info_title = QLabel("Information")
        self.info_title.setAlignment(QtCore.Qt.AlignCenter)
        self.info_title.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.grid_layout.addWidget(self.info_title, 0, 1, 1, 1)

        self.kanji_info_text = QTextEdit()
        self.kanji_info_text.setReadOnly(True)
        self.grid_layout.addWidget(self.kanji_info_text, 1, 1, 1, 1)

        self.button_next = QPushButton("Next Kanji")
        self.button_next.clicked.connect(self.show_kanji_info)

        self.button_back = QPushButton("Go Back")
        self.button_back.clicked.connect(self.back_button_clicked.emit)

        self.grid_layout.addWidget(self.button_next, 2, 0, 1, 2)
        self.grid_layout.addWidget(self.button_back, 3, 0, 1, 2)

        self.setLayout(self.grid_layout)
        self.kanji_api = KanjiAPI(self.level)
        if not self.kanji_api.kanji_list:
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setText("Failed to load Kanji list. Please check your connection or the selected level.")
            error_message.setWindowTitle("Error")
            error_message.exec_()
            # self.back_button_clicked.emit()
        else:
            self.show_kanji_info()

    def show_kanji_info(self) -> None:
        kanji = self.kanji_api.get_random_kanji()
        if not kanji:
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Information)
            error_message.setText("No more Kanji in the list.")
            error_message.setWindowTitle("Information")
            error_message.exec_()
            self.back_button_clicked.emit()
            return

        kanji_info, error = self.kanji_api.get_kanji_info(kanji)

        if error:
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Warning)
            error_message.setText(error)
            error_message.setWindowTitle("Error")
            error_message.exec_()
            return

        if kanji_info:
            info_html = f"""
            <b>Grade:</b> {kanji_info.get('grade', 'N/A')}<br>
            <b>Heisig EN:</b> {kanji_info.get('heisig_en', 'N/A')}<br>
            <b>JLPT:</b> {kanji_info.get('jlpt', 'N/A')}<br>
            <b>Kanji:</b> {kanji_info.get('kanji', 'N/A')}<br>
            <b>Kun Readings:</b> {', '.join(kanji_info.get('kun_readings', []))}<br>
            <b>Meanings:</b> {', '.join(kanji_info.get('meanings', []))}<br>
            <b>Name Readings:</b> {', '.join(kanji_info.get('name_readings', []))}<br>
            <b>On Readings:</b> {', '.join(kanji_info.get('on_readings', []))}<br>
            <b>Stroke Count:</b> {kanji_info.get('stroke_count', 'N/A')}<br>
            <b>Unicode:</b> {kanji_info.get('unicode', 'N/A')}<br>
            """
            self.kanji_info_text.setHtml(info_html)
            self.kanji_label.setText(kanji)
            self.kanji_label.setStyleSheet("font-size: 200px;")
            self.kanji_info_text.setStyleSheet("font-size: 20px;")


if __name__ == "__main__":
    app = QApplication([])
    window = KanjiWidget(1)
    window.show()
    app.exec_()
