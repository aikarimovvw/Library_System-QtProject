import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5 import uic
import library_db
from CONST_VALUES import *
from show_inf_book_design import Ui_widget


class ShowInf(QWidget, Ui_widget):
    book_name = "t"

    def __init__(self, *book_name):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(SHOW_INF)
        book_name = book_name[FIRST_VALUE]
        self.label_name_book.setText(book_name)

        res_inf = library_db.select_all_with_aspect(BOOKS, BOOK, book_name, '*')

        # далее я заполняю данными все значения, обращаюсь к каждому элемента через id
        self.label_id.setText(str(res_inf[GET_ZERO_ELEMENT][ZERO_VALUE]))
        self.label_name_author.setText(res_inf[GET_ZERO_ELEMENT][FIRST_VALUE])
        self.label_name_genre.setText(res_inf[GET_ZERO_ELEMENT][THIRD_VALUE])
        self.label_pixmap.setPixmap(QPixmap(f"{res_inf[GET_ZERO_ELEMENT][FOURTH_VALUE]}"))
        self.label_year.setText(str(res_inf[GET_ZERO_ELEMENT][SIXTH_VALUE]))
        self.txt_edit_description.setEnabled(False)
        self.txt_edit_description.setText(res_inf[GET_ZERO_ELEMENT][FIFTH_VALUE])
        if res_inf[GET_ZERO_ELEMENT][SEVENTH_VALUE] == AVAILABLE_TRUE:
            self.lbl_available.setText(AVAILABLE_IN_STOCK)
        else:
            self.lbl_available.setText(NOT_AVAILABLE_IN_STOCK)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowInf()
    ex.show()
    sys.exit(app.exec())
