from PyQt5.QtWidgets import QMainWindow
from View.login import Ui_LoginWindow

class LoginController(QMainWindow, Ui_LoginWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        self.primary_controller = primary_controller 

        self.pushButton_login.clicked.connect(self.tenta_login)

    def tenta_login(self):
        nome = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        
        login_riuscito = self.primary_controller.gestore_utenti.validaCredenziali(nome, password)
        
        if login_riuscito:
            self.label_error.setText("")
            self.lineEdit_username.clear()
            self.lineEdit_password.clear()
            
            from Controller.ManagerController import ManagerController
            self.primary_controller.mostra_finestra(ManagerController, start_maximized=self.isMaximized())
        else:
            self.label_error.setText("Nome o password non corretti.")