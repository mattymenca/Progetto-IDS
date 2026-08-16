import sys
import os

# Disattiva la creazione di pycache
sys.dont_write_bytecode = True

from PyQt5.QtWidgets import QApplication
from Model.Dati import Dati
from Controller.Inizio import InizioController
from Controller.PrimaryController import PrimaryController
from Model.Utente.Manager import Manager
from Model.Gestore.GestoreUtenti import GestoreUtenti
from Model.Magazzino.Prodotto import Prodotto
from Model.Utente.Dipendente import Dipendente
from Model.Utente.StatoDipendente import StatoDipendente

NOME_FILE_DATI = "dati.pkl"

def main():
    app = QApplication(sys.argv)
    
    # 1. Inizializzazione Dati
    dati = Dati()

    # 2. VERIFICA SE IL FILE SU DISCO ESISTE GIÀ
    if os.path.exists(NOME_FILE_DATI):
        print("Trovato file dati su disco! Caricamento in RAM in corso...")
        dati.caricaDati(NOME_FILE_DATI)
    else:
        print("Primo avvio rilevato: Creazione dati di default e salvataggio iniziale...")
        # Popolamento iniziale solo se il file non esiste ancora
        dati.manager = Manager("admin", "admin", 35, "admin", "0000") # Corretto l'ordine dei parametri
        dati.prodotti.append(Prodotto("Caffè Espresso", 50, 1.20, 0.20, "Lavazza", True, 10))
        dati.prodotti.append(Prodotto("Cappuccino", 30, 1.60, 0.40, "Centrale Latte", True, 5))
        dati.dipendenti.append(Dipendente("Mario", "Rossi", 28, [], [], StatoDipendente.IMPIEGATO))

        # Salva per creare il file per le prossime volte
        dati.setDirty()
        dati.salvaTutto(NOME_FILE_DATI)

    # 3. Creazione dei Gestori (Dependency Injection)
    gestore_utenti = GestoreUtenti(dati)
    
    # Se per qualche motivo il manager in dati è nullo, lo ricolleghiamo
    if dati.manager is None:
        manager = Manager("Mario", "Rossi", 30, "mario88", "0000")
        gestore_utenti.cambiaManager(manager)

    # 4. Creazione del PrimaryController
    primary = PrimaryController(gestore_utenti)

    # Collega il salvataggio automatico quando l'applicazione viene chiusa dalla GUI
    app.aboutToQuit.connect(primary.chiusura_sicura)

    # 5. Avvio della prima schermata
    primary.mostra_finestra(InizioController)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()