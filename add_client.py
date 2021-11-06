import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5 import uic
import functions_for_add
import library_db
from CONST_VALUES import *
from add_client_design import Ui_MainWindow


# окно для добавления читателя
class AddClient(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(WIND_ADD_CLIENT)
        self.btn_add_client.clicked.connect(self.save_client)

    def save_client(self):
        name = self.ledit_add_name_c.text()
        num_client = self.ledit_add_num_c.text()
        mail_client = self.ledit_add_mail_c.text()
        address_client = self.ledit_add_address.text()
        b_date = self.clndr_wdgt_add_date.selectedDate().toString(DATE_YMD)
        if functions_for_add.check_clients(name, num_client, mail_client, address_client, b_date) is False:
            return self.statusBar().showMessage(INCORRECT_VALUES)

        res_check_client = library_db.select_one_with_aspect(CLIENTS, CLIENT_NUMBER, num_client, ALL_VALUES)
        if res_check_client is None:
            library_db.insert_for_clients(name, num_client, mail_client, address_client, b_date)
            self.statusBar().setStyleSheet(GREEN_STATUS)
            self.statusBar().showMessage(ADD_CLIENT_COMPLETE)
            self.close()
        else:
            self.statusBar().showMessage(INCORRECT_CLIENT)

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
    ex = AddClient()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
