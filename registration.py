import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import functions_for_add
import library_db
from CONST_VALUES import *


class RegEmployee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('reg.ui', self)
        self.setWindowTitle(REGISTRATION_WIND)
        self.btn_save_new_empl.clicked.connect(self.sign_new_employee)

    def sign_new_employee(self):
        name_employee = self.ledit__add_name_e2.text()
        number = self.ledit_add_number.text()
        password = self.ledit_pass.text()
        login = self.ledit_login.text()

        if functions_for_add.check_employee(name_employee, number, password, login) is False:
            self.statusBar().showMessage(LEN_ZERO)
            return None
        result_check_login = library_db.select_one_with_aspect(EMPLOYEE, LOGIN, login, ALL_VALUES)
        if result_check_login is None:
            library_db.insert_for_employee(login, password, number, name_employee)
            self.statusBar().setStyleSheet(GREEN_STATUS)
            self.statusBar().showMessage(DATA_IS_ENTERED)
            self.close()

        else:
            self.statusBar().showMessage(INCORRECT_USER)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = RegEmployee()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
