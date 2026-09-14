from PyQt5 import QtCore, QtWidgets

class Ui_ManagerWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet("""
            QMainWindow { background-color: #2c3e50; }
            QLabel { color: white; font-size: 13px; }
            QLineEdit, QComboBox, QDateEdit { 
                background-color: #34495e; color: white; padding: 6px; border-radius: 4px; border: 1px solid #7f8c8d; 
            }
            QTableWidget { background-color: #34495e; color: white; gridline-color: #7f8c8d; }
            QHeaderView::section { background-color: #8e44ad; color: white; font-weight: bold; }
            QPushButton { background-color: #9b59b6; color: white; border-radius: 6px; padding: 8px 15px; font-weight: bold; }
            QPushButton:hover { background-color: #8e44ad; }
            QPushButton#btn_profilo { background-color: #f39c12; }
            QPushButton#btn_profilo:hover { background-color: #d35400; }
            QPushButton#btn_licenzia { background-color: #e74c3c; }
            QPushButton#btn_licenzia:hover { background-color: #c0392b; }

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
        
        # INTESTAZIONE CON PULSANTE PROFILO MANAGER
        self.topHeader = QtWidgets.QHBoxLayout()
        self.title = QtWidgets.QLabel("Pannello Gestione Personale (Manager)", self.centralwidget)
        self.title.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        self.btn_profilo_manager = QtWidgets.QPushButton("👤 Il Mio Profilo & Storico Ordini")
        self.btn_profilo_manager.setObjectName("btn_profilo")
        
        self.topHeader.addWidget(self.title)
        self.topHeader.addWidget(self.btn_profilo_manager)
        self.layout.addLayout(self.topHeader)

        # TABELLA DIPENDENTI
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels([
            "Nome", "Cognome", "Età", "Tipo Contratto", "Salario (€)", "Data Inizio", "Data Fine", "Stato"
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.layout.addWidget(self.tableWidget)

        # FORM ASSUNZIONE
        self.formLayout = QtWidgets.QGridLayout()

        self.input_nome = QtWidgets.QLineEdit(); self.input_nome.setPlaceholderText("Nome")
        self.formLayout.addWidget(QtWidgets.QLabel("Nome:"), 0, 0)
        self.formLayout.addWidget(self.input_nome, 0, 1)

        self.input_cognome = QtWidgets.QLineEdit(); self.input_cognome.setPlaceholderText("Cognome")
        self.formLayout.addWidget(QtWidgets.QLabel("Cognome:"), 0, 2)
        self.formLayout.addWidget(self.input_cognome, 0, 3)

        self.input_eta = QtWidgets.QLineEdit(); self.input_eta.setPlaceholderText("Età")
        self.formLayout.addWidget(QtWidgets.QLabel("Età:"), 0, 4)
        self.formLayout.addWidget(self.input_eta, 0, 5)

        self.combo_tipo_contratto = QtWidgets.QComboBox()
        self.formLayout.addWidget(QtWidgets.QLabel("Tipo Contratto:"), 1, 0)
        self.formLayout.addWidget(self.combo_tipo_contratto, 1, 1)

        self.input_salario = QtWidgets.QLineEdit(); self.input_salario.setPlaceholderText("Salario (€)")
        self.formLayout.addWidget(QtWidgets.QLabel("Salario (€):"), 1, 2)
        self.formLayout.addWidget(self.input_salario, 1, 3)

        self.date_inizio = QtWidgets.QDateEdit(); self.date_inizio.setCalendarPopup(True); self.date_inizio.setDate(QtCore.QDate.currentDate())
        self.formLayout.addWidget(QtWidgets.QLabel("Data Inizio:"), 1, 4)
        self.formLayout.addWidget(self.date_inizio, 1, 5)

        self.date_fine = QtWidgets.QDateEdit(); self.date_fine.setCalendarPopup(True); self.date_fine.setDate(QtCore.QDate.currentDate().addYears(1))
        self.formLayout.addWidget(QtWidgets.QLabel("Data Fine:"), 2, 0)
        self.formLayout.addWidget(self.date_fine, 2, 1)

        self.layout.addLayout(self.formLayout)

        # PULSANTI AZIONE
        self.btnLayout = QtWidgets.QHBoxLayout()
        self.btn_assumi = QtWidgets.QPushButton("Assumi Dipendente")
        self.btn_licenzia = QtWidgets.QPushButton("Licenzia / Cambia Stato")
        self.btn_licenzia.setObjectName("btn_licenzia")
        self.btn_indietro = QtWidgets.QPushButton("Logout")

        self.btnLayout.addWidget(self.btn_assumi)
        self.btnLayout.addWidget(self.btn_licenzia)
        self.btnLayout.addWidget(self.btn_indietro)
        self.layout.addLayout(self.btnLayout)

        MainWindow.setCentralWidget(self.centralwidget)