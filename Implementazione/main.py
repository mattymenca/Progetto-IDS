import sys
from PyQt5.QtWidgets import QApplication
from Model.Dati import Dati
from Controller.Inizio import InizioController
from Controller.PrimaryController import PrimaryController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dati = Dati()
    dati.caricaDati("File")

    manager = PrimaryController()
    manager.mostraFinestra(InizioController)

    sys.exit(app.exec_())
