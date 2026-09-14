from PyQt5 import QtCore, QtWidgets

class Ui_MagazzinoWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setStyleSheet("""
            QMainWindow { background-color: #2c3e50; }
            QLabel { color: white; font-size: 14px; }
            QLineEdit { background-color: #34495e; color: white; padding: 6px; border-radius: 4px; border: 1px solid #7f8c8d; }
            QTableWidget { background-color: #34495e; color: white; gridline-color: #7f8c8d; }
            QHeaderView::section { background-color: #1abc9c; color: white; font-weight: bold; }
            QPushButton { background-color: #3498db; color: white; border-radius: 6px; padding: 8px 15px; font-weight: bold; }
            QPushButton:hover { background-color: #2980b9; }
            QPushButton#btn_rifornisci { background-color: #2ecc71; }
            QPushButton#btn_elimina { background-color: #e74c3c; }

            QMessageBox { background-color: #2c3e50; }
            QMessageBox QLabel { color: #ffffff; font-size: 14px; }
            QMessageBox QPushButton { 
                background-color: #34495e; 
                color: white; 
                border: 1px solid #7f8c8d; 
                border-radius: 4px; 
                padding: 6px 12px; 
            }
            QMessageBox QPushButton:hover { background-color: #2980b9; }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        self.label = QtWidgets.QLabel("Gestione Magazzino (Modifica diretta celle | Evidenziati in ROSSO se sotto soglia)", self.centralwidget)
        self.label.setStyleSheet("font-size: 15px; font-weight: bold;")
        self.layout.addWidget(self.label)
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["Nome", "Quantità", "Soglia Minima", "Prezzo (€)", "Costo (€)", "Fornitore"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.layout.addWidget(self.tableWidget)
        
        # Form
        self.formLayout = QtWidgets.QGridLayout()
        
        self.input_nome = QtWidgets.QLineEdit()
        self.input_nome.setPlaceholderText("Nome Prodotto")
        self.formLayout.addWidget(QtWidgets.QLabel("Nome:"), 0, 0)
        self.formLayout.addWidget(self.input_nome, 0, 1)

        self.input_qta = QtWidgets.QLineEdit()
        self.input_qta.setPlaceholderText("Quantità")
        self.formLayout.addWidget(QtWidgets.QLabel("Q.tà:"), 0, 2)
        self.formLayout.addWidget(self.input_qta, 0, 3)

        self.input_soglia = QtWidgets.QLineEdit()
        self.input_soglia.setPlaceholderText("Soglia Minima")
        self.formLayout.addWidget(QtWidgets.QLabel("Soglia:"), 0, 4)
        self.formLayout.addWidget(self.input_soglia, 0, 5)

        self.input_prezzo = QtWidgets.QLineEdit()
        self.input_prezzo.setPlaceholderText("Prezzo (€)")
        self.formLayout.addWidget(QtWidgets.QLabel("Prezzo:"), 1, 0)
        self.formLayout.addWidget(self.input_prezzo, 1, 1)

        self.input_costo = QtWidgets.QLineEdit()
        self.input_costo.setPlaceholderText("Costo (€)")
        self.formLayout.addWidget(QtWidgets.QLabel("Costo:"), 1, 2)
        self.formLayout.addWidget(self.input_costo, 1, 3)

        self.input_fornitore = QtWidgets.QLineEdit()
        self.input_fornitore.setPlaceholderText("Fornitore")
        self.formLayout.addWidget(QtWidgets.QLabel("Fornitore:"), 1, 4)
        self.formLayout.addWidget(self.input_fornitore, 1, 5)

        self.layout.addLayout(self.formLayout)
        
        # Pulsanti
        self.btnLayout = QtWidgets.QHBoxLayout()
        self.btn_aggiungi = QtWidgets.QPushButton("Aggiungi Prodotto")
        self.btn_rifornisci = QtWidgets.QPushButton("Rifornisci Selezionato")
        self.btn_rifornisci.setObjectName("btn_rifornisci")
        self.btn_elimina = QtWidgets.QPushButton("Elimina Selezionato")
        self.btn_elimina.setObjectName("btn_elimina")
        self.btn_indietro = QtWidgets.QPushButton("Torna Indietro")
        
        self.btnLayout.addWidget(self.btn_aggiungi)
        self.btnLayout.addWidget(self.btn_rifornisci)
        self.btnLayout.addWidget(self.btn_elimina)
        self.btnLayout.addWidget(self.btn_indietro)
        self.layout.addLayout(self.btnLayout)

        MainWindow.setCentralWidget(self.centralwidget)