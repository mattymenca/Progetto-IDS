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
            # self.primary_controller.mostraFinestra(AltraFinestraController)
            print("Login riuscito! Cambio finestra...")
        else:
            self.label_error.setText("Nome o password non corretti.")