from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        MainWindow.setStyleSheet("""
            QMainWindow { background-color: #2c3e50; }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 16px;
                border-radius: 10px;
            }
            QPushButton:hover { background-color: #2980b9; }
            QPushButton#pushButton_indietro {
                background-color: #7f8c8d;
            }
            QPushButton#pushButton_indietro:hover {
                background-color: #95a5a6;
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.centralLayout.setContentsMargins(50, 50, 50, 50)
        self.centralLayout.setSpacing(20)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(20)

        self.pushButton_magazzino = QtWidgets.QPushButton("Magazzino", self.centralwidget)
        self.pushButton_magazzino.setMinimumSize(QtCore.QSize(150, 50))
        self.gridLayout.addWidget(self.pushButton_magazzino, 0, 0, 1, 1)

        self.pushButton_conti = QtWidgets.QPushButton("Conti", self.centralwidget)
        self.pushButton_conti.setMinimumSize(QtCore.QSize(150, 50))
        self.gridLayout.addWidget(self.pushButton_conti, 0, 1, 1, 1)

        self.pushButton_ordini = QtWidgets.QPushButton("Ordini", self.centralwidget)
        self.pushButton_ordini.setMinimumSize(QtCore.QSize(150, 50))
        self.gridLayout.addWidget(self.pushButton_ordini, 0, 2, 1, 1)

        self.centralLayout.addLayout(self.gridLayout)
        
        # Pulsante Torna Indietro
        self.pushButton_indietro = QtWidgets.QPushButton("Torna alla Home Iniziale", self.centralwidget)
        self.pushButton_indietro.setObjectName("pushButton_indietro")
        self.pushButton_indietro.setMinimumSize(QtCore.QSize(150, 45))
        self.centralLayout.addWidget(self.pushButton_indietro)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestionale - Menu Dipendenti"))