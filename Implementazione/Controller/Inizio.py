from PyQt5.QtWidgets import QMainWindow
from View.inizio import Ui_MainWindow
# from Controller.Magazzino.MagazzinoController import MagazzinoController 

class InizioController(QMainWindow, Ui_MainWindow):
    # Nota: Il primo parametro è il PrimaryController!
    def __init__(self, primary_controller):
        super().__init__()
        self.setupUi(self)
        
        # 1. Salva il riferimento al PrimaryController
        self.primary_controller = primary_controller 
        
