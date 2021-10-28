from PyQt5.QtWidgets import QApplication
from authorization import AddClient
import sys

app = QApplication(sys.argv)
ex = AddClient()
ex.show()
sys.exit(app.exec())
