import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import uic
import library_db
from CONST_VALUES import *
import csv
from datetime import datetime
import functions_for_add


class ShowDebtors(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('debtors.ui', self)
        self.setWindowTitle('Отображение должников')
        self.fill_debtors()
        self.btn_save_csv.clicked.connect(self.save_csv)

    def fill_debtors(self):
        functions_for_add.delete_operations()
        res_check_date = res_check_date = library_db.select_table(OPERATIONS,
                                                                  BOOK_NAME, BOOK_ID, DATE_DEADLINE,
                                                                  CLIENT_NAME, CLIENT_ID)

        res_check_date = list(filter(lambda x: datetime.strptime(x[2], FORMAT_YEAR) < datetime.today(), res_check_date))
        table_row = 0
        self.tbl_wdgt_debtors.setRowCount(len(res_check_date))
        for i in res_check_date:
            self.tbl_wdgt_debtors.setItem(table_row, 0, QtWidgets.QTableWidgetItem(i[0]))
            self.tbl_wdgt_debtors.setItem(table_row, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.tbl_wdgt_debtors.setItem(table_row, 2, QtWidgets.QTableWidgetItem(i[2]))
            self.tbl_wdgt_debtors.setItem(table_row, 3, QtWidgets.QTableWidgetItem(i[3]))
            self.tbl_wdgt_debtors.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(i[4])))
            table_row += 1

    def save_csv(self):
        with open('results.csv', 'w', newline='') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"',
                quoting=csv.QUOTE_MINIMAL)
            writer.writerow(
                [self.tbl_wdgt_debtors.horizontalHeaderItem(i).text()
                 for i in range(self.tbl_wdgt_debtors.columnCount())])
            for i in range(self.tbl_wdgt_debtors.rowCount()):
                row = []
                for j in range(self.tbl_wdgt_debtors.columnCount()):
                    item = self.tbl_wdgt_debtors.item(i, j)
                    if item is not None:
                        row.append(item.text())
                writer.writerow(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowDebtors()
    ex.show()
    sys.exit(app.exec())
