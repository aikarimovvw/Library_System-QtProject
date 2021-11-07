import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from registration import RegEmployee
from home import HomeScreen
import library_db
from CONST_VALUES import *
from py_designs.authorization_des import Ui_MainWindow


class AddClient(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(WIND_AUTHORIZATION)
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
            self.statusBar().showMessage(INCORRECT_LOGIN)
        else:
            password = self.ledit_pass_e_enter.text()
            password_db = password_db[ZERO_VALUE]
            if password != password_db:
                self.statusBar().showMessage(INCORRECT_PASSWORD)
            else:
                self.statusBar().setStyleSheet(GREEN_STATUS)
                self.statusBar().showMessage(SUCCESSFULLY)
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
