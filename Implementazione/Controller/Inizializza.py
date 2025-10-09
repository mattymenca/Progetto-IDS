from PyQt5 import QtWidgets
from View.inizio import Ui_MainWindow

class InizioView(QtWidgets.QMainWindow, Ui_MainWindow):
    # This class is responsible ONLY for the GUI layout and basic element connection
    def __init__(self):
        super().__init__()
        self.setupUi(self)
