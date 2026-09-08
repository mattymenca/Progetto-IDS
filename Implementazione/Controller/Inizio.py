from PyQt5.QtWidgets import QMainWindow
from View.inizio import Ui_MainWindow
from Controller.DipendentiController import DipendentiController
from Controller.LoginController import LoginController

class InizioController(QMainWindow, Ui_MainWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        
        # 1. Salva il riferimento al PrimaryController
        self.primary_controller = primary_controller 
        self.pushButton_3.clicked.connect(self.apriDipendenti)       
        self.pushButton_4.clicked.connect(self.apriLogin)       

    def apriDipendenti(self):
        is_maximized = self.isMaximized()
        self.primary_controller.mostraFinestra(DipendentiController, start_maximized=is_maximized)

    def apriLogin(self):
        is_maximized = self.isMaximized()
        self.primary_controller.mostraFinestra(LoginController, start_maximized=is_maximized)