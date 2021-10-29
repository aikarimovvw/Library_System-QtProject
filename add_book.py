import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import uic
import functions_for_add_books
import function_for_reg


class AddBook(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_book.ui', self)
        self.btn_save.clicked.connect(self.save_book)
        self.btn_load_img.clicked.connect(self.load_image)
        self.btn_look_authors.clicked.connect(self.look_authors)
        self.btn_look_genres.clicked.connect(self.look_genres)
        self.author_inp_dialog = 0
        self.genres_inp_dialog = 0
        self.path = ''

    # загрузка изображения
    def load_image(self):
        self.path = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]

    # два диалоговых окна для выбора автора и жанра
    def look_genres(self):
        con = sqlite3.connect("db_lib.sqlite")
        cur = con.cursor()
        res_find_genre = cur.execute("""SELECT genre FROM Genres""").fetchall()
        genres_inp_dialog, ok_pressed = QInputDialog.getItem(self, 'Выберите жанр', 'Выбор жанра',
                                                             tuple([i[0] for i in res_find_genre]), 0, False)
        if ok_pressed:
            self.genres_inp_dialog = genres_inp_dialog
            self.btn_look_genres.setText(genres_inp_dialog)

    def look_authors(self):
        con = sqlite3.connect("db_lib.sqlite")
        cur = con.cursor()
        res_find_authors = cur.execute("""SELECT author FROM Authors""").fetchall()
        author_inp_dialog, ok_pressed = QInputDialog.getItem(self, 'Выберите автора', 'Выбор автора',
                                                             tuple([i[0] for i in res_find_authors]), 0, False)

        if ok_pressed:
            self.author_inp_dialog = author_inp_dialog
            self.btn_look_authors.setText(author_inp_dialog)

    # сохранение книги
    def save_book(self):
        title = self.ledit_title.text()
        year = self.ledit_year.text()

        author = self.ledit_author.text()
        if self.ledit_author.text() == '':
            author = self.author_inp_dialog

        genre = self.ledit_genre.text()
        if self.ledit_genre.text() == '':
            genre = self.genres_inp_dialog

        description = self.txt_edit_description.toPlainText()
        path_default = 'default_cover.jpg'
        title_check = functions_for_add_books.check_title(title)
        year_check = functions_for_add_books.check_year(year)
        author_check = function_for_reg.check_name(author)
        genre_check = functions_for_add_books.check_genre(genre)

        if title_check != 'ок':
            self.statusBar().showMessage(title_check)
            return None
        if genre_check != 'ок':
            self.statusBar().showMessage(genre_check)
            return None
        if year_check != 'ок':
            self.statusBar().showMessage(year_check)
            return None
        if author_check != 'ок':
            self.statusBar().showMessage(author_check)
            return None
        if self.path == '':
            self.path = path_default

        con = sqlite3.connect("db_lib.sqlite")
        cur = con.cursor()

        res_check_name = cur.execute("""SELECT * FROM Authors
        WHERE author =?""", (author,)).fetchone()
        res_check_genre = cur.execute("""SELECT * FROM Genres
        WHERE genre =?""", (genre,)).fetchone()
        if res_check_name is None:
            cur.execute("""INSERT INTO Authors(author) VALUES(?)""", (author,)).fetchall()
        if res_check_genre is None:
            cur.execute("""INSERT INTO Genres(genre) VALUES(?)""", (genre,)).fetchall()

        author_add_name = cur.execute("""SELECT author from Authors
        WHERE author=? """, (author,)).fetchone()

        genre_add_name = cur.execute("""SELECT genre from Genres
                WHERE genre=? """, (genre,)).fetchone()
        cur.execute("""INSERT INTO Books(author_name, book, genre_name, description, year, path_image) 
        VALUES(?, ?, ?, ?, ?, ?)""", (author_add_name[0], title, genre_add_name[0], description, year, self.path))
        con.commit()
        con.close()
        self.statusBar().setStyleSheet("color : green")
        self.statusBar().showMessage('Книга успешно добавлена!')
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = AddBook()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
