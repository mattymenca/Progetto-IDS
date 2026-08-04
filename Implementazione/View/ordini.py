from PyQt5 import QtWidgets

class Ui_OrdiniWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 600)
        MainWindow.setStyleSheet("""
            QMainWindow { background-color: #2c3e50; }
            QLabel { color: white; font-size: 14px; }
            QSpinBox, QComboBox { background-color: #34495e; color: white; padding: 5px; border-radius: 4px; }
            QListWidget { background-color: #34495e; color: white; border-radius: 5px; }
            QPushButton { background-color: #3498db; color: white; border-radius: 6px; padding: 10px; font-weight: bold; }
            QPushButton:hover { background-color: #2980b9; }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        self.title = QtWidgets.QLabel("Nuova Comanda / Ordine Tavolo", self.centralwidget)
        self.title.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.layout.addWidget(self.title)

        # Form TAVOLO E COPERTI
        self.topLayout = QtWidgets.QHBoxLayout()
        
        self.topLayout.addWidget(QtWidgets.QLabel("Numero Tavolo / ID:"))
        self.spin_id = QtWidgets.QSpinBox()
        self.spin_id.setRange(1, 100)
        self.topLayout.addWidget(self.spin_id)

        self.topLayout.addWidget(QtWidgets.QLabel("Coperti:"))
        self.spin_coperti = QtWidgets.QSpinBox()
        self.spin_coperti.setRange(1, 20)
        self.topLayout.addWidget(self.spin_coperti)

        self.layout.addLayout(self.topLayout)

        # SELEZIONE PRODOTTI
        self.prodLayout = QtWidgets.QHBoxLayout()
        self.combo_prodotti = QtWidgets.QComboBox()
        self.spin_qta = QtWidgets.QSpinBox()
        self.spin_qta.setRange(1, 50)
        self.btn_aggiungi_prod = QtWidgets.QPushButton("Aggiungi all'Ordine")

        self.prodLayout.addWidget(QtWidgets.QLabel("Prodotto:"))
        self.prodLayout.addWidget(self.combo_prodotti)
        self.prodLayout.addWidget(QtWidgets.QLabel("Quantità:"))
        self.prodLayout.addWidget(self.spin_qta)
        self.prodLayout.addWidget(self.btn_aggiungi_prod)

        self.layout.addLayout(self.prodLayout)

        # LISTA PRODOTTI AGGIUNTI
        self.layout.addWidget(QtWidgets.QLabel("Riepilogo Ordine Corrente:"))
        self.list_riepilogo = QtWidgets.QListWidget()
        self.layout.addWidget(self.list_riepilogo)

        # BOTTONI
        self.btn_invia = QtWidgets.QPushButton("Conferma e Invia Ordine")
        self.btn_invia.setStyleSheet("background-color: #2ecc71;")
        self.btn_indietro = QtWidgets.QPushButton("Torna Indietro")

        self.layout.addWidget(self.btn_invia)
        self.layout.addWidget(self.btn_indietro)

        MainWindow.setCentralWidget(self.centralwidget)