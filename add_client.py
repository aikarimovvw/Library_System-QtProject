import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import uic
import functions_for_add_books


class AddClient(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_client.ui', self)
        self.btn_add_client.clicked.connect(self.save_client)

    def save_client(self):
        name = self.ledit_add_name_c.text()
        phone_num_client = self.ledit_add_num_c.text()
        mail_client = self.ledit_add_mail_c.text()
        address_client = self.ledit_add_address.text()
        b_date = self.clndr_wdgt_add_date.selectedDate().toString("yyyy-MM-dd")

        name_check = functions_for_add_books.check_len(name)
        number_check = functions_for_add_books.check_len(phone_num_client)
        mail_check = functions_for_add_books.check_len(mail_client)
        address_check = functions_for_add_books.check_len(address_client)
        year_check = functions_for_add_books.check_date(b_date)

        if all([name_check, number_check, mail_check, address_check]):
            if year_check is False:
                self.statusBar().showMessage('Введите корректную дату рождения')
                return None
        else:
            self.statusBar().showMessage('Пустая строка, введите заново')
            return None

        con = sqlite3.connect("db_lib.sqlite")
        cur = con.cursor()
        res_check_client = cur.execute("""SELECT * FROM clients
                WHERE client_number =?""", (phone_num_client,)).fetchone()
        if res_check_client is None:
            cur.execute("""INSERT INTO clients(client_name, client_number, client_mail, client_adres, client_date) 
                    VALUES(?, ?, ?, ?, ?)""",
                        (name, phone_num_client, mail_client, address_client, b_date))
            con.commit()
            con.close()
            self.statusBar().setStyleSheet("color : green")
            self.statusBar().showMessage('Книга успешно добавлена!')
            self.close()
        else:
            self.statusBar().showMessage('Пользователь с таким номером существует')

    def clear_all(self):
        self.statusBar().showMessage('')
        self.txt_edit_description.clear()
        self.ledit_title.clear()
        self.ledit_year.clear()
        self.btn_look_authors.setText('Выбор автора')
        self.btn_look_genres.setText('Выбор жанра')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = AddClient()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
