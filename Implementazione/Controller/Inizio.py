from PyQt5.QtWidgets import QMainWindow
from View.inizio import Ui_MainWindow
# from Controller.Magazzino.MagazzinoController import MagazzinoController 

# Classe fittizia per MagazzinoController per il test
class MagazzinoController(QMainWindow):
    def __init__(self, primary_controller):
        super().__init__()
        self.primary_controller = primary_controller
        self.setWindowTitle("Schermata Magazzino")

class InizioController(QMainWindow, Ui_MainWindow):
    # Nota: Il primo parametro è il PrimaryController!
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        
        # 1. Salva il riferimento al PrimaryController
        self.primary_controller = primary_controller 
        
        # 2. Connetti i bottoni al metodo di switch
        self.pushButton.clicked.connect(self.vai_a_magazzino)
        self.pushButton_2.clicked.connect(self.chiudi_applicazione) # Esempio di chiusura
        
    def vai_a_magazzino(self):
        """
        Chiede al PrimaryController di gestire lo switch alla schermata Magazzino.
        """
        # Si limita a chiamare il manager centralizzato, passandogli la CLASSE di destinazione
        self.primary_controller.mostraFinestra(MagazzinoController)
        
    def chiudi_applicazione(self):
        """
        Chiama il metodo per chiudere il controller attuale e permettere al GC di agire.
        """
        self.primary_controller.chiudiErimuovi(self)
