from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class FermiBrowser(QMainWindow):

    def __init__(self):
        super(FermiBrowser, self).__init__()

        # LAYOUT
        self.window = QWidget()
        self.window.setWindowTitle("Fermi Browser")
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.browser = QWebEngineView()

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://www.google.com"))

        self.window.setLayout(self.layout)
        self.window.show()


app = QApplication([])
window = FermiBrowser()
app.exec_()
