from PyQt5.QtWidgets import QMainWindow
from View.dipendenti import Ui_MainWindow

class DipendentiController(QMainWindow, Ui_MainWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        self.primary_controller = primary_controller 

    def closeEvent(self, event):
        # Gestisce la chiusura tramite la 'X' della finestra.
        self.primary_controller.chiusura_sicura()
        event.accept()    