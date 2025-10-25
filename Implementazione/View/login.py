import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# CLASSE PER LA FINESTRA DI LOGIN
# Strutturata esattamente come richiesto, con il suo metodo setupUi.
class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(500, 400)
        LoginWindow.setWindowTitle("Gestionale")

        # Applica lo stesso stile moderno e scuro
        LoginWindow.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 12px 25px;
                text-align: center;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLabel {
                color: white;
                font-size: 16px;
            }
            QLineEdit {
                background-color: #34495e;
                color: white;
                border: 1px solid #7f8c8d;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Layout verticale per organizzare gli elementi del login
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(50, 30, 50, 30)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setAlignment(QtCore.Qt.AlignCenter)

        # Titolo
        self.label_title = QtWidgets.QLabel("Accesso Gestionale", self.centralwidget)
        self.label_title.setObjectName("label_title")
        self.label_title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_title)

        # Campo Username
        self.label_username = QtWidgets.QLabel("Username", self.centralwidget)
        self.verticalLayout.addWidget(self.label_username)
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)

        # Campo Password
        self.label_password = QtWidgets.QLabel("Password", self.centralwidget)
        self.verticalLayout.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password) # Nasconde la password
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)

        # Pulsante di Login
        self.pushButton_login = QtWidgets.QPushButton("Accedi", self.centralwidget)
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_login.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_login.setStyleSheet("margin-top: 15px;") # Aggiunge spazio sopra il pulsante
        self.verticalLayout.addWidget(self.pushButton_login, 0, QtCore.Qt.AlignCenter)
        
        # Etichetta per messaggi di errore
        self.label_error = QtWidgets.QLabel("", self.centralwidget)
        self.label_error.setObjectName("label_error")
        self.label_error.setStyleSheet("color: #e74c3c; font-size: 14px;") # Colore rosso per l'errore
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_error)

        LoginWindow.setCentralWidget(self.centralwidget)