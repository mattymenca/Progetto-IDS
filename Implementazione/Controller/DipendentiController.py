from PyQt5.QtWidgets import QMainWindow
from View.dipendenti import Ui_MainWindow

class DipendentiController(QMainWindow, Ui_MainWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        self.primary_controller = primary_controller 

        # --- Codice recuperato dal branch main: Connessione dei bottoni ---
        self.pushButton_magazzino.clicked.connect(self.apriMagazzino)
        self.pushButton_ordini.clicked.connect(self.apriOrdini)
        self.pushButton_conti.clicked.connect(self.apriConti)
        self.pushButton_indietro.clicked.connect(self.apriInizio)

    # --- Metodi di navigazione (dal branch main) ---
    def apriMagazzino(self):
        from Controller.MagazzinoController import MagazzinoController
        self.primary_controller.mostra_finestra(MagazzinoController, start_maximized=self.isMaximized())

    def apriOrdini(self):
        from Controller.OrdiniController import OrdiniController
        self.primary_controller.mostra_finestra(OrdiniController, start_maximized=self.isMaximized())

    def apriConti(self):
        from Controller.ContiController import ContiController
        self.primary_controller.mostra_finestra(ContiController, start_maximized=self.isMaximized())

    def apriInizio(self):
        from Controller.Inizio import InizioController
        self.primary_controller.mostra_finestra(InizioController, start_maximized=self.isMaximized())

    # --- Codice recuperato dal branch HEAD: Chiusura sicura ---
    def closeEvent(self, event):
        # Gestisce la chiusura tramite la 'X' della finestra.
        self.primary_controller.chiusura_sicura()
        event.accept()