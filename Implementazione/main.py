import sys
from PyQt5.QtWidgets import QApplication
from Model.Dati import Dati
from Controller.Inizio import InizioController
from Controller.PrimaryController import PrimaryController
from Model.Utente.Manager import Manager
from Model.Gestore.GestoreConti import GestoreConti
from Model.Gestore.GestoreOrdini import GestoreOrdini
from Model.Gestore.GestoreUtenti import GestoreUtenti

def main():
    app = QApplication(sys.argv)

    # 1. Inizializzazione Dati
    dati = Dati()
    dati.caricaDati("dati.pickle") # Scommenta quando avrai il file
    manager = None
    # Se il file non esiste, creiamo un manager di default per testare il login
    if dati.manager is None:
        manager = Manager("Mario", "Rossi", 30, "mario88", "0000")
    
    # 2. Creazione dei Gestori (Dependency Injection)
    # Nota l'ordine: i Conti hanno bisogno degli Ordini
    # gestore_ordini = GestoreOrdini(dati)
    gestore_utenti = GestoreUtenti(dati)
    # gestore_conti = GestoreConti(dati, g_ordini)
    gestore_utenti.cambiaManager(manager)
    # 3. Creazione del PrimaryController 
    # Gli passiamo tutto quello che dovrà "distribuire" alle finestre
    controller_centrale = PrimaryController(gestore_utenti)

    # 4. Avvio della prima schermata
    controller_centrale.mostra_finestra(InizioController)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# #prova creando il manager dal main e non caricando i dati da file
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dati = Dati()
#     #dati.caricaDati("File")
#     new_manager = Manager("Mario", "Rossi", 30, "ordine_1", "0000")
#     dati.manager = new_manager
#     manager = PrimaryController(dati,)
#     manager.mostraFinestra(InizioController)

#     sys.exit(app.exec_())
