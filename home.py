from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import uic
import sys
from add_book import AddBook
from add_client import AddClient
from open_debtors import ShowDebtors
from open_inf_book import ShowInf
import library_db
from CONST_VALUES import *
import functions_for_add
import datetime


class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.add_client_win = AddClient()
        self.add_book_win = AddBook()
        self.show_debtors = ShowDebtors()
        uic.loadUi('home.ui', self)
        self.setWindowTitle(MAIN_WINDOW)
        self.tbl_wdgt.tabBar().setVisible(False)

        # Страница 1: Операция
        functions_for_add.delete_operations()
        self.tbl_update(OPERATIONS)
        functions_for_add.delete_operations()
        self.buttons_operation_page()

        # Страница 2: Книги
        self.tbl_update('Books')
        self.buttons_books_page()

        # Страница 3: Читатели
        self.tbl_update('clients')
        self.buttons_clients_page()

        # Страница 4: Пользователи
        self.buttons_employ_page()

    # Коннект кнопок с TabWidget
    def open_operations(self):
        self.tbl_wdgt.setCurrentIndex(ZERO_TAB)

    def open_books(self):
        self.tbl_wdgt.setCurrentIndex(FIRST_TAB)

    def open_clients(self):
        self.tbl_wdgt.setCurrentIndex(SECOND_TAB)

    def open_employee(self):
        self.tbl_wdgt.setCurrentIndex(THIRD_TAB)

    # Открытие новых дизайнов
    def show_add_book(self):
        self.add_book_win.show()

    def show_add_client(self):
        self.add_client_win.show()

    def open_debtors(self):
        self.show_debtors.show()

    def all_great(self):
        self.statusBar().setStyleSheet(GREEN_STATUS)
        self.statusBar().showMessage(GREAT_OPERATION)

    def clear_lis_widget(self):
        self.lst_wdgt_btn_books.clear()

    # Обновление значений таблиц
    def tbl_update(self, text):
        db = QSqlDatabase.addDatabase(FORMAT_DB)
        db.setDatabaseName('db_lib.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable(text)
        model.select()
        if text == BOOKS:
            return self.tbl_view_books.setModel(model)
        if text == CLIENTS:
            return self.tbl_view_clients.setModel(model)
        return self.tbl_view_operations.setModel(model)

    # Функционал на странице 1:
    # все кнопки на 1 странице
    def buttons_operation_page(self):
        self.btn_main_oper.clicked.connect(self.open_operations)
        self.btn_debtors.clicked.connect(self.open_debtors)
        self.btn_record_oper.clicked.connect(self.record_operation)
        self.btn_debtors.clicked.connect(self.open_debtors)

    # функция для записи операции, с проверками на наличие книги и тд
    def record_operation(self):
        id_book = self.ledit_id_book.text()
        id_client = self.ledit_name_client.text()
        type_operation = self.operation_cmb_box.currentText()
        quantity_days = self.days_cmb_box.currentText()
        res_book = library_db.select_one_with_aspect(BOOKS, ID, id_book, ALL_VALUES)
        res_client = library_db.select_one_with_aspect(CLIENTS, ID, id_client, ALL_VALUES)

        if res_book is None or res_client is None:
            return self.statusBar().showMessage(WRONG_ID)

        available = int(res_book[7])

        if type_operation == REFUND and available == AVAILABLE_TRUE:
            return self.statusBar().showMessage(AVAILABLE_IN_STOCK)

        if type_operation == EXTRADITION and available == AVAILABLE_FALSE:
            return self.statusBar().showMessage(NOT_AVAILABLE_IN_STOCK)

        book_name = library_db.select_one_with_aspect(BOOKS, ID, id_book, BOOK)[GET_ZERO_ELEMENT]
        client_name = library_db.select_one_with_aspect(CLIENTS, ID, id_client, CLIENT_NAME)[GET_ZERO_ELEMENT]
        date_today = datetime.date.today()
        date_of_end = date_today + datetime.timedelta(days=int(quantity_days))
        library_db.update_book_available((available, id_book,))

        if type_operation == EXTRADITION and available == AVAILABLE_TRUE:
            library_db.insert_to_operations(
                book_name, id_book, type_operation, date_today, date_of_end, client_name, id_client)

        if type_operation == REFUND and available == AVAILABLE_FALSE:
            library_db.insert_to_operations(
                book_name, id_book, type_operation, date_today, DATE, client_name, id_client)
        self.tbl_update(OPERATIONS)

    # Функционал на странице 2:
    # все кнопки на 2 странице
    def buttons_books_page(self):
        self.btn_main_books.clicked.connect(self.open_books)
        self.btn_search_book.clicked.connect(self.search_book)
        self.btn_add_book.clicked.connect(self.show_add_book)
        self.btn_search_book_update.clicked.connect(self.fill_book_val)
        self.btn_reload_books.clicked.connect(lambda btn, text=BOOKS: self.tbl_update(text))
        self.btn_upd_val_book.clicked.connect(self.update_book_val)
        self.btn_del_book.clicked.connect(self.del_book_val)

    # функция для TabWidget 'Поиск'
    def search_book(self):
        value_search = self.cmb_value_search.currentText()
        ledit_value = f'%{self.ledit_value_search.text()}%'
        if value_search == AUTHOR_RUS:
            res_books = library_db.select_with_like_operation(BOOKS, AUTHOR_NAME, ledit_value, BOOK)
        else:
            res_books = library_db.select_with_like_operation(BOOKS, BOOK, ledit_value, BOOK)
        self.clear_lis_widget()
        for item in res_books:
            book = item[GET_ZERO_ELEMENT]
            btn_show_inf_book = QtWidgets.QPushButton(book)
            btn_show_inf_book.clicked.connect(lambda btn, text=book: self.open_inf_book(text))
            lst_widget_for_book = QtWidgets.QListWidgetItem()
            self.lst_wdgt_btn_books.setStyleSheet(STYLE_PRESS)
            self.lst_wdgt_btn_books.addItem(lst_widget_for_book)
            self.lst_wdgt_btn_books.setItemWidget(lst_widget_for_book, btn_show_inf_book)
            self.lst_wdgt_btn_books.scrollToItem(lst_widget_for_book)

    # Открывает окно с информацией о книге
    def open_inf_book(self, text):
        self.show_inf_books = ShowInf(self, text)
        self.show_inf_books.show()

    # Создание запроса с информацией о книге, и заполнение нужных полей
    def fill_book_val(self):
        id_book = self.ledit_search_id_upd.text()
        res_books_upd = library_db.select_all_with_aspect(BOOKS, ID, id_book, ALL_VALUES)
        if res_books_upd is None:
            return self.statusBar().showMessage(WROND_ID_BOOK)
        # снизу идет заполнение данными строк из запроса res_books_upd
        self.ledit_update_title.setText(res_books_upd[GET_ZERO_ELEMENT][SECOND_VALUE])
        self.ledit_update_year.setText(str(res_books_upd[GET_ZERO_ELEMENT][SIXTH_VALUE]))
        self.ledit_update_genre.setText(res_books_upd[GET_ZERO_ELEMENT][THIRD_VALUE])
        self.ledit_update_author.setText(res_books_upd[GET_ZERO_ELEMENT][FIFTH_VALUE])
        self.txt_edit_update_desc.setText(res_books_upd[GET_ZERO_ELEMENT][FIFTH_VALUE])

    # Обновление значений книги
    def update_book_val(self):
        id_book = self.ledit_search_id_upd.text()
        library_db.update_books_values((self.ledit_update_author.text(), self.ledit_update_title.text(),
                                        self.ledit_update_genre.text(), self.txt_edit_update_desc.toPlainText(),
                                        self.ledit_update_year.text(), id_book,))
        self.all_great()

    # Удаление книги
    def del_book_val(self):
        id_book = self.ledit_search_id_upd.text()
        library_db.delete_values(BOOKS, ID, id_book)
        self.all_great()

    # Функционал на странице 3:
    # все кнопки на 3 странице
    def buttons_clients_page(self):
        self.btn_main_clients.clicked.connect(self.open_clients)
        self.btn_reload_clients_tab.clicked.connect(lambda btn, text='clients': self.tbl_update(text))
        self.btn_search_client_num.clicked.connect(self.fill_client_val)
        self.btn_update_client.clicked.connect(self.upd_client)
        self.btn_del_client.clicked.connect(self.del_client)
        self.btn_add_client.clicked.connect(self.show_add_client)
        self.btn_search_get_id.clicked.connect(self.out_client_id)

    # Вывод id клиента в LineEdit при вводе номера и нажатии кнопки
    def out_client_id(self):
        number = self.ledit_num_get_id.text()
        value = library_db.select_one_with_aspect(CLIENTS, CLIENT_NUMBER, number, ID)
        if value is None:
            self.statusBar().setStyleSheet(RED_STATUS)
            return self.statusBar().showMessage(MESS_NUM_ERROR)
        self.ledit_out_id.setText(str(value[ZERO_VALUE]))

    # Создание запроса с информацией о читателе, и заполнение нужных полей
    def fill_client_val(self):
        id_search = self.ledit_search_client_id.text()
        res_books_upd = library_db.select_all_with_aspect(CLIENTS, ID, id_search, '*')
        if len(res_books_upd) == INPUT_LEN:
            return self.statusBar().showMessage(MESS_CORRECT_NUM)
        # снизу идет заполнение данными строк из запроса res_books_upd
        self.ledit_update_name_c.setText(res_books_upd[GET_ZERO_ELEMENT][FIRST_VALUE])
        self.ledit_update_num_c.setText(str(res_books_upd[GET_ZERO_ELEMENT][SECOND_VALUE]))
        self.ledit_update_mail_c.setText(res_books_upd[GET_ZERO_ELEMENT][THIRD_VALUE])
        self.ledit_update_adres.setText(res_books_upd[GET_ZERO_ELEMENT][FOURTH_VALUE])
        date = res_books_upd[GET_ZERO_ELEMENT][FIFTH_VALUE].split('-')
        date = QDate(int(date[ZERO_VALUE]), int(date[FIFTH_VALUE]), int(date[SECOND_VALUE]))  # year, month, day
        format_ = QTextCharFormat()
        format_.setFont(QFont(FONT, 15))
        self.clndr_wdgt_add_date.setDateTextFormat(date, format_)

    # Обновление информации о читателе
    def upd_client(self):
        name = self.ledit_update_name_c.text()
        num_client = self.ledit_update_num_c.text()
        mail_client = self.ledit_update_mail_c.text()
        address_client = self.ledit_update_adres.text()
        b_date = self.clndr_wdgt_add_date.selectedDate().toString(DATE_YMD)
        if functions_for_add.check_clients(name, num_client, mail_client, address_client, b_date) is False:
            if functions_for_add.check_date(b_date) is False:
                return self.statusBar().showMessage(CORRECT_B_DATE)
            return self.statusBar().showMessage(LEN_ZERO)

        library_db.update_clients_values((name, num_client, mail_client, address_client, b_date,
                                          self.ledit_search_client_id.text(),))
        self.all_great()

    # Удаление читателя
    def del_client(self):
        library_db.delete_values(CLIENTS, ID, self.ledit_search_client_id.text())
        self.all_great()

    # Функционал на странице 4:
    # все кнопки на 3 странице
    def buttons_employ_page(self):
        self.btn_main_empl.clicked.connect(self.open_employee)
        self.btn_add_e.clicked.connect(self.add_employee)
        self.btn_search_empl_login.clicked.connect(self.fill_employee)
        self.btn_update_e.clicked.connect(self.update_employee)

    # Добавление нового сотрудника
    def add_employee(self):
        name_employee = self.ledit_add_name_e.text()
        number = self.ledit_add_num_e.text()
        password = self.ledit_add_pass_e.text()
        login = self.ledit_login_e.text()
        if functions_for_add.check_employee(name_employee, number, password, login) is False:
            return self.statusBar().showMessage(LEN_ZERO)
        result_check_login = library_db.select_one_with_aspect(EMPLOYEE, LOGIN, login, ALL_VALUES)
        if result_check_login is None:
            library_db.insert_for_employee(login, password, number, name_employee)
            self.all_great()
        else:
            self.statusBar().showMessage(INCORRECT_USER)

    # Заполнение полей информацией о сотруднике
    def fill_employee(self):
        login_search = self.ledit_search_empl_login.text()
        res_employ_upd = library_db.select_all_with_aspect(EMPLOYEE, LOGIN, login_search, ALL_VALUES)
        if len(res_employ_upd) == INPUT_LEN:
            self.statusBar().setStyleSheet(RED_STATUS)
            return self.statusBar().showMessage(INCORRECT_LOGIN)
        # снизу идет заполнение данными строк из запроса res_employ_upd
        self.ledit_update_pass_e.setText(res_employ_upd[GET_ZERO_ELEMENT][FIRST_VALUE])
        self.ledit_update_name_e.setText(res_employ_upd[GET_ZERO_ELEMENT][SECOND_VALUE])
        self.ledit_update_num_e.setText(str(res_employ_upd[GET_ZERO_ELEMENT][THIRD_VALUE]))
        self.ledit_update_login_e.setText(res_employ_upd[GET_ZERO_ELEMENT][FOURTH_VALUE])

    # Обновление информации о сотруднике
    def update_employee(self):
        name_employee = self.ledit_update_name_e.text()
        number = self.ledit_update_num_e.text()
        password = self.ledit_update_pass_e.text()
        login = self.ledit_update_login_e.text()
        if functions_for_add.check_employee(name_employee, number, password, login) is False:
            return self.statusBar().showMessage(LEN_ZERO)
        if (login != self.ledit_search_empl_login.text()) and not (library_db.select_one_with_aspect(
                EMPLOYEE, LOGIN, login, ALL_VALUES)) is None:
            self.statusBar().setStyleSheet(RED_STATUS)
            return self.statusBar().showMessage(LOGIN_EXISTS)

        library_db.update_employ_values((password, name_employee, number, login, self.ledit_search_empl_login.text(),))
        self.all_great()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = HomeScreen()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
