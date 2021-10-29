import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from registration import RegEmployee
from home import HomeScreen
import sqlite3


class AddClient(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('authorization.ui', self)
        self.btn_reg.clicked.connect(self.reg_empl)
        self.reg_empl_wind = RegEmployee()
        self.transition_home_wind = HomeScreen()
        self.btn_enter.clicked.connect(self.enter)

    def reg_empl(self):
        self.reg_empl_wind.show()

    def enter(self):
        con = sqlite3.connect('db_lib.sqlite')
        cur = con.cursor()
        login = self.ledit_login_e_enter.text()
        result = cur.execute("""SELECT * FROM Employee
                 WHERE login = ?""", (login,)).fetchone()
        if result is None:
            self.statusBar().showMessage('Неверный логин')
        else:
            password = self.ledit_pass_e_enter.text()
            if password != str(result[1]):
                self.statusBar().showMessage('Неправильный пароль')
            else:
                self.statusBar().setStyleSheet("color : green")
                self.statusBar().showMessage('Успешно')
                self.transition_home_wind.show()
        con.close()
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
