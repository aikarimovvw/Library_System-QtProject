from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import uic
import sys
from add_book import AddBook
from add_client import AddClient
from open_inf_book import ShowInf
import sqlite3


class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.add_client_win = AddClient()
        self.add_book_win = AddBook()
        self.initUI()

    def initUI(self):
        uic.loadUi('home.ui', self)
        self.btn_main_oper.clicked.connect(self.open_operations)
        self.btn_main_clients.clicked.connect(self.open_clients)
        self.btn_main_empl.clicked.connect(self.open_employee)
        self.btn_main_books.clicked.connect(self.open_books)
        self.btn_add_book.clicked.connect(self.show_add_book)
        self.btn_search_book_update.clicked.connect(self.fill_book_val)
        self.tbl_update('book')
        self.tbl_update('client')
        self.btn_search_book.clicked.connect(self.search_book)
        self.tbl_wdgt.tabBar().setVisible(False)
        self.btn_search_client_num.clicked.connect(self.fill_client_val)
        self.btn_update_client.clicked.connect(self.upd_client)
        self.btn_del_client.clicked.connect(self.del_client)
        self.btn_upd_val_book.clicked.connect(self.update_book_val)
        self.btn_del_book.clicked.connect(self.del_book_val)
        self.btn_add_client.clicked.connect(self.show_add_client)

    def open_operations(self):
        self.tbl_wdgt.setCurrentIndex(0)

    def open_books(self):
        self.tbl_wdgt.setCurrentIndex(1)

    def open_clients(self):
        self.tbl_wdgt.setCurrentIndex(2)

    def open_employee(self):
        self.tbl_wdgt.setCurrentIndex(3)

    def show_add_book(self):
        self.add_book_win.show()
        self.tbl_update('book')

    def show_add_client(self):
        self.add_client_win.show()
        self.tbl_update('client')

    def search_book(self):
        con = sqlite3.connect('db_lib.sqlite')
        cur = con.cursor()
        value_search = self.cmb_value_search.currentText()
        ledit_value = '%' + self.ledit_value_search.text() + '%'
        if value_search == 'Автор':
            res_books = cur.execute("""SELECT book FROM Books WHERE author_name LIKE ?""", (ledit_value,)).fetchall()
        else:
            res_books = cur.execute("""SELECT book FROM Books WHERE book LIKE ?""", (ledit_value,)).fetchall()
        self.clear_lis_widget()
        for item in res_books:
            book = item[0]
            btn_show_inf_book = QtWidgets.QPushButton(book)
            btn_show_inf_book.clicked.connect(lambda btn, text=book: self.open_inf_book(text))
            lst_widget_for_book = QtWidgets.QListWidgetItem()
            self.lst_wdgt_btn_books.setStyleSheet("WidgetItem:pressed")
            self.lst_wdgt_btn_books.addItem(lst_widget_for_book)
            self.lst_wdgt_btn_books.setItemWidget(lst_widget_for_book, btn_show_inf_book)
            self.lst_wdgt_btn_books.scrollToItem(lst_widget_for_book)
        con.commit()
        con.close()

    def open_inf_book(self, text):
        self.show_inf_books = ShowInf(self, text)
        self.show_inf_books.show()

    def clear_lis_widget(self):
        self.lst_wdgt_btn_books.clear()

    def fill_client_val(self):
        number_search =self.ledit_search_client_id.text()
        con = sqlite3.connect('db_lib.sqlite')
        cur = con.cursor()
        res_books_upd = cur.execute("""SELECT * FROM Clients WHERE client_number = ?""", (number_search,)).fetchall()
        if res_books_upd is None:
            self.statusBar().showMessage('Введите корректный номер')
            return None
        self.ledit_update_name_c.setText(res_books_upd[0][1])
        self.ledit_update_num_c.setText(str(res_books_upd[0][2]))
        self.ledit_update_mail_c.setText(res_books_upd[0][3])
        self.ledit_update_adres.setText(res_books_upd[0][4])
        # self.clndr_wdgt_add_date.setDateTextFormat(QDate(res_books_upd[0][5])

    def upd_client(self):
        pass

    def del_client(self):
        pass

    def tbl_update(self, text):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('db_lib.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        if text == 'book':
            model.setTable('Books')
            model.select()
            self.tbl_view_books.setModel(model)
        else:
            model.setTable('clients')
            model.select()
            self.tbl_view_clients.setModel(model)

    def fill_book_val(self):
        id_book = self.ledit_search_id_upd.text()
        con = sqlite3.connect('db_lib.sqlite')
        cur = con.cursor()
        res_books_upd = cur.execute("""SELECT * FROM Books WHERE id = ?""", (id_book,)).fetchall()
        if res_books_upd is None:
            self.statusBar().showMessage('Введите корректное id')
            return None
        self.ledit_update_title.setText(res_books_upd[0][2])
        self.ledit_update_year.setText(str(res_books_upd[0][6]))
        self.ledit_update_genre.setText(res_books_upd[0][3])
        self.ledit_update_author.setText(res_books_upd[0][1])
        self.txt_edit_update_desc.setText(res_books_upd[0][5])

    def update_book_val(self):
        id_book = self.ledit_search_id_upd.text()
        con = sqlite3.connect('db_lib.sqlite')
        cur = con.cursor()
        cur.execute(
            """UPDATE Books SET author_name=?, book=?, genre_name=?, description=?, year=? WHERE id=? """,
            (self.ledit_update_author.text(), self.ledit_update_title.text(), self.ledit_update_genre.text(),
             self.txt_edit_update_desc.toPlainText(), self.ledit_update_year.text(), id_book,))
        con.commit()

    def del_book_val(self):
        id_book = self.ledit_search_id_upd.text()
        con = sqlite3.connect('db_lib.sqlite')
        cur = con.cursor()
        cur.execute(
            """DELETE from Books WHERE id=? """,
            (id_book,))
        con.commit()
        con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = HomeScreen()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
