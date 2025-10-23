import sys
from PyQt5.QtWidgets import QApplication
from Model.Dati import Dati
from Controller.Inizio import InizioController
from Controller.PrimaryController import PrimaryController
from Model.Utente.Manager import Manager

#prova creando il manager dal main e non caricando i dati da file
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dati = Dati()
    #dati.caricaDati("File")
    new_manager = Manager("Mario", "Rossi", 30, "ordine_1", "0000")
    dati.manager = new_manager
    manager = PrimaryController(dati)
    manager.mostraFinestra(InizioController)

    sys.exit(app.exec_())
