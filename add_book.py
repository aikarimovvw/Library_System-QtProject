import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import uic
import functions_for_add
import library_db
from CONST_VALUES import *


# окно для добавления книги
class AddBook(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_book.ui', self)
        self.setWindowTitle(ADD_BOOK)
        self.btn_save.clicked.connect(self.save_book)
        self.btn_load_img.clicked.connect(self.load_image)
        self.btn_look_authors.clicked.connect(lambda btn, text=AUTHOR: self.viewing_content(text))
        self.btn_look_genres.clicked.connect(lambda btn, text=GENRE: self.viewing_content(text))
        self.author = ''
        self.genre = ''
        self.path = 'cover/default_cover.png'

    # загрузка изображения
    def load_image(self):
        self.path = QFileDialog.getOpenFileName(self, PUT_IMAGE, '')[0]

    def viewing_content(self, criterion):
        con = sqlite3.connect("db_lib.sqlite")
        cur = con.cursor()
        if criterion == AUTHOR:
            res_find = library_db.select_table(AUTHORS, AUTHOR)
        else:
            res_find = library_db.select_table(GENRES, GENRE)
        inp_dialog, ok_pressed = QInputDialog.getItem(self, CHOICE, CHOICE,
                                                      tuple([i[0] for i in res_find]), 0, False)
        if ok_pressed:
            if criterion == GENRE:
                self.btn_look_genres.setText(inp_dialog)
                self.genre = inp_dialog
            else:
                self.btn_look_authors.setText(inp_dialog)
                self.author = inp_dialog

    # сохранение книги
    def save_book(self):
        title = self.ledit_title.text()
        year = self.ledit_year.text()
        if self.ledit_author.text() != '':
            self.author = self.ledit_author.text()
        if self.ledit_genre.text() != '':
            self.genre = self.ledit_genre.text()

        description = self.txt_edit_description.toPlainText()
        title_check = functions_for_add.check_len(title)
        year_check = functions_for_add.check_year(year)
        author_check = functions_for_add.check_len(self.author)
        genre_check = functions_for_add.check_len(self.genre)

        if all([title_check, genre_check, author_check]):
            if not year_check:
                self.statusBar().showMessage(CORRECT_DATE_PUB)
                return None
        else:
            self.statusBar().showMessage(LEN_ZERO)
            return None

        res_check_name = library_db.select_one_with_aspect(AUTHORS, AUTHOR, self.author, '*')
        res_check_genre = library_db.select_one_with_aspect(GENRES, GENRE, self.genre, '*')
        if res_check_name is None:
            library_db.insert_for_name(AUTHORS, AUTHOR, self.author)
        if res_check_genre is None:
            library_db.insert_for_name(GENRES, GENRE, self.genre)

        library_db.insert_for_books(self.author, title,
                                    self.genre, description, year, self.path, True)
        self.statusBar().setStyleSheet(GREEN_STATUS)
        self.statusBar().showMessage(ADD_BOOK_COMPLETE)
        self.close()

    def clear_all(self):
        self.statusBar().showMessage('')
        self.txt_edit_description.clear()
        self.ledit_title.clear()
        self.ledit_year.clear()
        self.btn_look_authors.setText(CHOICE_AUTHOR)
        self.btn_look_genres.setText(CHOICE_GENRE)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = AddBook()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
