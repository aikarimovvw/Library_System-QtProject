from PyQt5.QtWidgets import QApplication
from authorization import AddClient
import sys


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


app = QApplication(sys.argv)
app.setStyle('Fusion')
ex = AddClient()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec())
