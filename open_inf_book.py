import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5 import uic
import library_db
from CONST_VALUES import *


class ShowInf(QWidget):
    book_name = "t"

    def __init__(self, *book_name):
        super().__init__()
        uic.loadUi('show_information_book.ui', self)
        self.setWindowTitle('Отображение информации')
        book_name = book_name[1]
        self.label_name_book.setText(book_name)

        res_inf = library_db.select_all_with_aspect(BOOKS, BOOK, book_name, '*')

        self.label_id.setText(str(res_inf[0][0]))
        self.label_name_author.setText(res_inf[0][1])
        self.label_name_genre.setText(res_inf[0][3])
        self.label_pixmap.setPixmap(QPixmap(f"{res_inf[0][4]}"))
        self.label_year.setText(str(res_inf[0][6]))
        self.txt_edit_description.setEnabled(False)
        self.txt_edit_description.setText(res_inf[0][5])
        if res_inf[0][7] == 1:
            self.lbl_available.setText('Есть в библиотеке')
        else:
            self.lbl_available.setText('На данный  момент книга в пользовании у читателя')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowInf()
    ex.show()
    sys.exit(app.exec())
