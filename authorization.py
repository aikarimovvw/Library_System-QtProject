import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from registration import RegEmployee
from home import HomeScreen
import library_db
from CONST_VALUES import *


class AddClient(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('authorization.ui', self)
        self.setWindowTitle('Авторизация')
        self.btn_reg.clicked.connect(self.reg_empl)
        self.reg_empl_wind = RegEmployee()
        self.transition_home_wind = HomeScreen()
        self.btn_enter.clicked.connect(self.enter)

    def reg_empl(self):
        self.reg_empl_wind.show()

    def enter(self):
        login_inp = self.ledit_login_e_enter.text()
        password_db = library_db.select_one_with_aspect(EMPLOYEE, LOGIN, login_inp, PASSWORD)
        if password_db is None:
            self.statusBar().showMessage('Неверный логин')
        else:
            password = self.ledit_pass_e_enter.text()
            password_db = password_db[0]
            if password != password_db:
                self.statusBar().showMessage('Неправильный пароль')
            else:
                self.statusBar().setStyleSheet(GREEN_STATUS)
                self.statusBar().showMessage('Успешно')
                self.transition_home_wind.show()
                self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = AddClient()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
