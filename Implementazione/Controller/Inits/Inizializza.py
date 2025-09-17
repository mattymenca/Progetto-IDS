import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Inits:
    @staticmethod
    def init():
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle("Test")
        window.setGeometry(100, 100, 800, 600)
        window.show()
        sys.exit(app.exec_())
