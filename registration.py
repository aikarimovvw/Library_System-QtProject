import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import function_for_reg


class RegEmployee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('reg.ui', self)
        self.btn_save_new_empl.clicked.connect(self.sign_new_employee)

    def sign_new_employee(self):
        name_employee = self.ledit__add_name_e2.text()
        number = self.ledit_add_number.text()
        password = self.ledit_pass.text()
        login = self.ledit_login.text()

        login_check = function_for_reg.check_login(login)
        pass_check = function_for_reg.check_pass(password)
        number_check = function_for_reg.check_number(number)
        name_check = function_for_reg.check_name(name_employee)

        if login_check != 'ок':
            self.statusBar().showMessage(login_check)
            return None
        if pass_check != 'ок':
            self.statusBar().showMessage(pass_check)
            return None
        if number_check != 'ок':
            self.statusBar().showMessage(number_check)
            return None
        if name_check != 'ок':
            self.statusBar().showMessage(name_check)
            return None

        con = sqlite3.connect('db_lib.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM Employee
                                         WHERE number=?""",
                             (number,)).fetchone()
        result_check_login = cur.execute("""SELECT * FROM Employee
                                         WHERE login = ?""",
                                         (login,)).fetchone()
        if result_check_login is None:
            if result is None:
                cur.execute("""INSERT INTO Employee(login, password, number, name)  
                                VALUES(?, ?, ?, ?)""", (login, password, number, name_employee)).fetchall()
                self.statusBar().setStyleSheet("color : green")
                self.statusBar().showMessage('Данные занесены, можете продолжить вход')
                con.commit()
                con.close()
                self.close()
            else:
                self.statusBar().showMessage('Такой пользователь уже существует')

        else:
            self.statusBar().showMessage('Такой пользователь уже существует')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = RegEmployee()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
