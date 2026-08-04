import sys
import os

# 1. Disattiva la creazione di __pycache__
sys.dont_write_bytecode = True

from PyQt5.QtWidgets import QApplication
from Model.Dati import Dati
from Controller.Inizio import InizioController
from Controller.PrimaryController import PrimaryController
from Model.Utente.Manager import Manager
from Model.Magazzino.Prodotto import Prodotto
from Model.Utente.Dipendente import Dipendente
from Model.Utente.StatoDipendente import StatoDipendente

NOME_FILE_DATI = "dati.pkl"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dati = Dati()
    
    # 2. VERIFICA SE IL FILE SU DISCO ESISTE GIÀ
    if os.path.exists(NOME_FILE_DATI):
        print("Trovato file dati su disco! Caricamento in RAM in corso...")
        dati.caricaDati(NOME_FILE_DATI)
    else:
        print("Primo avvio rilevato: Creazione dati di default e salvataggio iniziale...")
        # Popolamento iniziale solo se il file non esiste ancora
        dati.manager = Manager("admin", "admin", 35, [], "0000")
        dati.prodotti.append(Prodotto("Caffè Espresso", 50, 1.20, 0.20, "Lavazza", True, 10))
        dati.prodotti.append(Prodotto("Cappuccino", 30, 1.60, 0.40, "Centrale Latte", True, 5))
        dati.dipendenti.append(Dipendente("Mario", "Rossi", 28, [], [], StatoDipendente.IMPIEGATO))
        
        # Salva per creare il file dati.pkl per le prossime volte
        dati.salvaTutto(NOME_FILE_DATI)

    # 3. Avvio dell'Interfaccia Grafica
    primary = PrimaryController(dati)
    
    # Collega il salvataggio automatico quando l'applicazione viene chiusa
    app.aboutToQuit.connect(primary.chiusura_sicura)
    
    primary.mostra_finestra(InizioController)

    sys.exit(app.exec_())