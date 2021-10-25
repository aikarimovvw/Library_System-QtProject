import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.btn_main_oper.clicked.connect(self.Open_Operations)
        self.btn_main_clients.clicked.connect(self.Open_Clients)
        self.btn_main_empl.clicked.connect(self.Open_Employee)
        self.btn_main_books.clicked.connect(self.Open_Books)
        self.tbl_wdgt.tabBar().setVisible(False)

    def Open_Operations(self):
        self.tbl_wdgt.setCurrentIndex(0)

    def Open_Books(self):
        self.tbl_wdgt.setCurrentIndex(1)

    def Open_Clients(self):
        self.tbl_wdgt.setCurrentIndex(2)

    def Open_Employee(self):
        self.tbl_wdgt.setCurrentIndex(3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
