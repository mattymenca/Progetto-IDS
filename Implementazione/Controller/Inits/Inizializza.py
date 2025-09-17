import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Finestra:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle("Test")
        self.window.setGeometry(100, 100, 800, 600)
        self.window.show()
        sys.exit(self.app.exec_())
