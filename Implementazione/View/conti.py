from PyQt5 import QtWidgets

class Ui_ContiWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setStyleSheet("""
            QMainWindow { background-color: #2c3e50; }
            QLabel { color: white; font-size: 15px; }
            QComboBox { background-color: #34495e; color: white; padding: 8px; border-radius: 4px; }
            QListWidget { background-color: #34495e; color: white; border-radius: 4px; padding: 5px; font-size: 14px; }
            QPushButton { background-color: #2ecc71; color: white; border-radius: 6px; padding: 12px; font-size: 15px; font-weight: bold; }
            QPushButton:hover { background-color: #27ae60; }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        self.title = QtWidgets.QLabel("Emissione Conto / Cassa Bar", self.centralwidget)
        self.title.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 10px;")
        self.layout.addWidget(self.title)

        self.layout.addWidget(QtWidgets.QLabel("Seleziona Ordine Aperto (ID Ordine):"))
        self.combo_ordini = QtWidgets.QComboBox()
        self.layout.addWidget(self.combo_ordini)

        self.layout.addWidget(QtWidgets.QLabel("Dettaglio Prodotti Ordine:"))
        self.list_prodotti = QtWidgets.QListWidget()
        self.layout.addWidget(self.list_prodotti)

        self.layout.addWidget(QtWidgets.QLabel("Metodo di Pagamento:"))
        self.combo_pagamento = QtWidgets.QComboBox()
        self.layout.addWidget(self.combo_pagamento)

        self.lbl_totale = QtWidgets.QLabel("Totale da Pagare: 0.00 €")
        self.lbl_totale.setStyleSheet("font-size: 24px; font-weight: bold; color: #f1c40f; margin: 10px 0;")
        self.layout.addWidget(self.lbl_totale)

        self.btn_calcola = QtWidgets.QPushButton("Completa Conto e Calcola Totale")
        self.btn_calcola.setStyleSheet("background-color: #3498db;")
        self.btn_chiudi = QtWidgets.QPushButton("Chiudi ed Emetti Scontrino")
        self.btn_indietro = QtWidgets.QPushButton("Torna Indietro")
        self.btn_indietro.setStyleSheet("background-color: #95a5a6;")

        self.layout.addWidget(self.btn_calcola)
        self.layout.addWidget(self.btn_chiudi)
        self.layout.addWidget(self.btn_indietro)

        MainWindow.setCentralWidget(self.centralwidget)