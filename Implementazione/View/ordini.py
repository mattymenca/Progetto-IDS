from PyQt5 import QtWidgets, QtCore

class Ui_OrdiniWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet("""
            QMainWindow { background-color: #2c3e50; }
            QLabel { color: white; font-size: 13px; }
            QSpinBox, QComboBox, QLineEdit { background-color: #34495e; color: white; padding: 6px; border-radius: 4px; border: 1px solid #7f8c8d; }
            QListWidget { background-color: #34495e; color: white; border-radius: 5px; }
            QPushButton { background-color: #3498db; color: white; border-radius: 6px; padding: 8px; font-weight: bold; }
            QPushButton:hover { background-color: #2980b9; }
            QPushButton#btn_annulla { background-color: #e74c3c; }
            QPushButton#btn_annulla:hover { background-color: #c0392b; }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # SEZIONE RICERCA DINAMICA ORDINI ATTIVI
        self.boxSearchLayout = QtWidgets.QHBoxLayout()
        self.input_cerca_id = QtWidgets.QLineEdit()
        self.input_cerca_id.setPlaceholderText("🔍 Digita ID per filtrare...")
        
        self.combo_ordini_trovati = QtWidgets.QComboBox()
        
        self.btn_carica_ordine = QtWidgets.QPushButton("Carica Selezionato")
        self.btn_annulla_ordine = QtWidgets.QPushButton("Annulla Selezionato")
        self.btn_annulla_ordine.setObjectName("btn_annulla")

        self.boxSearchLayout.addWidget(QtWidgets.QLabel("Cerca Ordine:"))
        self.boxSearchLayout.addWidget(self.input_cerca_id)
        self.boxSearchLayout.addWidget(self.combo_ordini_trovati)
        self.boxSearchLayout.addWidget(self.btn_carica_ordine)
        self.boxSearchLayout.addWidget(self.btn_annulla_ordine)
        self.layout.addLayout(self.boxSearchLayout)

        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.layout.addWidget(self.line)

        # INTESTAZIONE NUOVO ORDINE
        self.topLayout = QtWidgets.QHBoxLayout()
        self.lbl_id_generato = QtWidgets.QLabel("ID Ordine: ---")
        self.lbl_id_generato.setStyleSheet("font-size: 16px; font-weight: bold; color: #f1c40f;")
        
        self.combo_operatore = QtWidgets.QComboBox()
        self.spin_coperti = QtWidgets.QSpinBox()
        self.spin_coperti.setRange(1, 30)

        self.topLayout.addWidget(self.lbl_id_generato)
        self.topLayout.addWidget(QtWidgets.QLabel("Cameriere/Operatore:"))
        self.topLayout.addWidget(self.combo_operatore)
        self.topLayout.addWidget(QtWidgets.QLabel("Coperti:"))
        self.topLayout.addWidget(self.spin_coperti)
        self.layout.addLayout(self.topLayout)

        # SELEZIONE PRODOTTO CON RICERCA TESTUALE
        self.prodLayout = QtWidgets.QHBoxLayout()
        self.input_filtro_prod = QtWidgets.QLineEdit()
        self.input_filtro_prod.setPlaceholderText("🔍 Filtra prodotto...")
        self.combo_prodotti = QtWidgets.QComboBox()
        self.spin_qta = QtWidgets.QSpinBox()
        self.spin_qta.setRange(1, 50)
        self.btn_aggiungi_prod = QtWidgets.QPushButton("Aggiungi all'Ordine")

        self.prodLayout.addWidget(self.input_filtro_prod)
        self.prodLayout.addWidget(self.combo_prodotti)
        self.prodLayout.addWidget(QtWidgets.QLabel("Q.tà:"))
        self.prodLayout.addWidget(self.spin_qta)
        self.prodLayout.addWidget(self.btn_aggiungi_prod)
        self.layout.addLayout(self.prodLayout)

        # CARRELLO / RIEPILOGO
        self.layout.addWidget(QtWidgets.QLabel("Riepilogo Voci Ordine:"))
        self.list_riepilogo = QtWidgets.QListWidget()
        self.layout.addWidget(self.list_riepilogo)

        # BOTTONI
        self.btn_invia = QtWidgets.QPushButton("Salva / Conferma Ordine")
        self.btn_invia.setStyleSheet("background-color: #2ecc71; font-size: 15px;")
        self.btn_nuovo = QtWidgets.QPushButton("Nuovo Ordine (Avanza ID)")
        self.btn_indietro = QtWidgets.QPushButton("Torna Indietro")

        self.layout.addWidget(self.btn_invia)
        self.layout.addWidget(self.btn_nuovo)
        self.layout.addWidget(self.btn_indietro)

        MainWindow.setCentralWidget(self.centralwidget)