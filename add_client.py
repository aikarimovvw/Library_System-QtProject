import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5 import uic
import functions_for_add
import library_db
from CONST_VALUES import *


# окно для добавления читателя
class AddClient(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_client.ui', self)
        self.btn_add_client.clicked.connect(self.save_client)

    def save_client(self):
        name = self.ledit_add_name_c.text()
        num_client = self.ledit_add_num_c.text()
        mail_client = self.ledit_add_mail_c.text()
        address_client = self.ledit_add_address.text()
        b_date = self.clndr_wdgt_add_date.selectedDate().toString("yyyy-MM-dd")
        if functions_for_add.check_clients(name, num_client, mail_client, address_client, b_date) is False:
            return self.statusBar().showMessage('Введите корректные данные')

        res_check_client = library_db.select_one_with_aspect(CLIENTS, CLIENT_NUMBER, num_client, '*')
        if res_check_client is None:
            library_db.insert_for_clients(name, num_client, mail_client, address_client, b_date)
            self.statusBar().setStyleSheet("color : green")
            self.statusBar().showMessage('Клиент успешно добавлен!')
            self.close()
        else:
            self.statusBar().showMessage('Клиент с таким номером существует')

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
