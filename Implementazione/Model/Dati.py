import pickle
import os

# Calcola il percorso fisso assoluto dentro la cartella del codice (Implementazione/dati.pkl)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_DATI_PREDEFINITO = os.path.join(BASE_DIR, "dati.pkl")

class Dati:
    def __init__(self, file_path=FILE_DATI_PREDEFINITO):
        self.file_path = file_path
        self.ordini = []          # Ordini attivi in corso
        self.storico_ordini = []  # ARCHIVIO: Ordini completati e saldati
        self.contratti = []
        self.dipendenti = []
        self.prodotti = []
        self.manager = None
        self.prossimo_id_ordine = 1 # CONTATORE SEQUENZIALE

    def genera_nuovo_id_ordine(self):
        """Genera un ID sequenziale incrementale che non si ripete mai"""
        id_attuale = self.prossimo_id_ordine
        self.prossimo_id_ordine += 1
        return id_attuale

    # Alias per compatibilità camelCase
    generaNuovoIdOrdine = genera_nuovo_id_ordine

    def salvaTutto(self, nomeFile=None):
        """Usa SEMPRE il percorso fisso assoluto, ignorando stringhe relative come 'dati.pkl'"""
        if nomeFile is None or nomeFile in ["dati.pkl", "dati.txt"]:
            target_path = self.file_path
        else:
            target_path = nomeFile

        try:
            with open(target_path, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Errore nel salvataggio ({target_path}): {e}")

    def caricaDati(self, nomeFile=None):
        """Usa SEMPRE il percorso fisso assoluto, ignorando stringhe relative come 'dati.pkl'"""
        if nomeFile is None or nomeFile in ["dati.pkl", "dati.txt"]:
            target_path = self.file_path
        else:
            target_path = nomeFile

        try:
            with open(target_path, "rb") as file:
                obj = pickle.load(file)
                self.__dict__.update(obj.__dict__)
                
                # Verifiche di sicurezza
                if not hasattr(self, 'storico_ordini'):
                    self.storico_ordini = []
                if not hasattr(self, 'prossimo_id_ordine'):
                    self.prossimo_id_ordine = 1
        except Exception as e:
            print(f"Errore nel caricamento ({target_path}): {e}")