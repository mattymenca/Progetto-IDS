from PyQt5.QtWidgets import QMainWindow
from View.inizio import Ui_MainWindow

class InizioController(QMainWindow, Ui_MainWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        
        self.primary_controller = primary_controller 
        self.pushButton_3.clicked.connect(self.apri_dipendenti)       
        self.pushButton_4.clicked.connect(self.apri_login)       

    def apri_dipendenti(self):
        from Controller.DipendentiController import DipendentiController
        self.primary_controller.mostra_finestra(DipendentiController, start_maximized=self.isMaximized())

    def apri_login(self):
        from Controller.LoginController import LoginController
        self.primary_controller.mostra_finestra(LoginController, start_maximized=self.isMaximized())