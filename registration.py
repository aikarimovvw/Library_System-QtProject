import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import functions_for_add


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

        login_check = functions_for_add.check_len(login)
        pass_check = functions_for_add.check_len(password)
        number_check = functions_for_add.check_len(number)
        name_check = functions_for_add.check_len(name_employee)

        if not any([login_check, pass_check, number_check, name_check]):
            self.statusBar().showMessage('Пустая строка, введите заново')
            return None

        con = sqlite3.connect('db_lib.sqlite')
        cur = con.cursor()
        result_check_login = cur.execute("""SELECT * FROM Employee WHERE login = ?""", (login,)).fetchone()
        if result_check_login is None:
            cur.execute("""INSERT INTO Employee(login, password, number, name)  
                                VALUES(?, ?, ?, ?)""", (login, password, number, name_employee)).fetchall()
            self.statusBar().setStyleSheet("color : green")
            self.statusBar().showMessage('Данные занесены, можете продолжить вход')
            con.commit()
            con.close()
            self.close()

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
