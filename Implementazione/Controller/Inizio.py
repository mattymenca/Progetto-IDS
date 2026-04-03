from PyQt5.QtWidgets import QMainWindow
from View.inizio import Ui_MainWindow
from Controller.DipendentiController import DipendentiController
from Controller.LoginController import LoginController
from Controller.PrimaryController import PrimaryController

class InizioController(QMainWindow, Ui_MainWindow):
    def __init__(self, primary_controller: PrimaryController):
        super().__init__()
        self.setupUi(self)
        
        # 1. Salva il riferimento al PrimaryController
        self.primary_controller = primary_controller 
        self.pushButton_3.clicked.connect(self.apriDipendenti)       
        self.pushButton_4.clicked.connect(self.apriLogin)       

    def apriDipendenti(self):
        is_maximized = self.isMaximized()
        self.primary_controller.mostra_finestra(DipendentiController, start_maximized=is_maximized)

    def apriLogin(self):
        is_maximized = self.isMaximized()
        self.primary_controller.mostra_finestra(LoginController, start_maximized=is_maximized)
        
    def closeEvent(self, event):
        # Gestisce la chiusura tramite la 'X' della finestra.
        self.primary_controller.chiusura_sicura()
        event.accept()    