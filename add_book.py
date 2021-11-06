import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import uic
import functions_for_add
import library_db
from CONST_VALUES import *
from add_book_design import Ui_MainWindow


# окно для добавления книги
class AddBook(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(ADD_BOOK)
        self.btn_save.clicked.connect(self.save_book)
        self.btn_load_img.clicked.connect(self.load_image)
        self.btn_look_authors.clicked.connect(lambda btn, text=AUTHOR: self.viewing_content(text))
        self.btn_look_genres.clicked.connect(lambda btn, text=GENRE: self.viewing_content(text))
        self.author = EMPTY_LINE
        self.genre = EMPTY_LINE
        self.path = 'cover/default_cover.png'

    # загрузка изображения
    def load_image(self):
        self.path = QFileDialog.getOpenFileName(self, PUT_IMAGE, EMPTY_LINE)[ZERO_VALUE]

    # при нажатии на кнопку Жанр, Выбор, появляются диалоговые окна с выбором автора/жанра
    def viewing_content(self, criterion):
        if criterion == AUTHOR:
            res_find = library_db.select_table(AUTHORS, AUTHOR)
        else:
            res_find = library_db.select_table(GENRES, GENRE)
        inp_dialog, ok_pressed = QInputDialog.getItem(self, CHOICE, CHOICE,
                                                      tuple([i[ZERO_VALUE] for i in res_find]), ZERO_VALUE, False)
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
        if self.ledit_author.text() != EMPTY_LINE:
            self.author = self.ledit_author.text()
        if self.ledit_genre.text() != EMPTY_LINE:
            self.genre = self.ledit_genre.text()

        description = self.txt_edit_description.toPlainText()
        title_check = functions_for_add.check_len(title)
        year_check = functions_for_add.check_year(year)
        author_check = functions_for_add.check_len(self.author)
        genre_check = functions_for_add.check_len(self.genre)

        if all([title_check, genre_check, author_check]):
            if not year_check:
                return self.statusBar().showMessage(CORRECT_DATE_PUB)
        else:
            return self.statusBar().showMessage(LEN_ZERO)

        res_check_name = library_db.select_one_with_aspect(AUTHORS, AUTHOR, self.author, ALL_VALUES)
        res_check_genre = library_db.select_one_with_aspect(GENRES, GENRE, self.genre, ALL_VALUES)
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
        self.statusBar().showMessage(EMPTY_LINE)
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
