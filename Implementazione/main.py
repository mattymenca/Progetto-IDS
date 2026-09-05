import sys
import os

# Disattiva creazione __pycache__
sys.dont_write_bytecode = True

from PyQt5.QtWidgets import QApplication
from Model.Dati import Dati, FILE_DATI_PREDEFINITO
from Controller.Inizio import InizioController
from Controller.PrimaryController import PrimaryController
from Model.Utente.Manager import Manager
from Model.Magazzino.Prodotto import Prodotto
from Model.Utente.Dipendente import Dipendente
from Model.Utente.StatoDipendente import StatoDipendente

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dati = Dati()

    # Carica dal percorso unico se esiste, altrimenti crea dati iniziali
    if os.path.exists(FILE_DATI_PREDEFINITO):
        print(f"Caricamento dati da: {FILE_DATI_PREDEFINITO}")
        dati.caricaDati()
    else:
        print(f"Primo avvio: Creazione file unico in {FILE_DATI_PREDEFINITO}...")
        dati.manager = Manager("admin", "admin", 35, [], "0000")
        dati.prodotti.append(Prodotto("Caffè Espresso", 50, 1.20, 0.20, "Lavazza", True, 10))
        dati.prodotti.append(Prodotto("Cappuccino", 30, 1.60, 0.40, "Centrale Latte", True, 5))
        dati.dipendenti.append(Dipendente("Mario", "Rossi", 28, [], [], StatoDipendente.IMPIEGATO))
        dati.salvaTutto()

    primary = PrimaryController(dati)
    app.aboutToQuit.connect(primary.chiusura_sicura)
    primary.mostra_finestra(InizioController)

    sys.exit(app.exec_())