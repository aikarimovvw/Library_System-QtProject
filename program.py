import sys

from PyQt5.QtWidgets import *

from PyQt5.uic import loadUiType
Form, Window = loadUiType('main.ui')


class MainApp(QMainWindow, Form):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

# import sys
#
# from PyQt5 import uic  # Импортируем uic
# from PyQt5.QtWidgets import QApplication, QMainWindow
#
#
# class MyWidget(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('main.ui', self)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyWidget()
#     ex.show()
#     sys.exit(app.exec_())
