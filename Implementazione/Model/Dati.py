import pickle
import os

# Calcola dinamicamente la cartella del progetto sul PC corrente
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_DATI_PREDEFINITO = os.path.join(BASE_DIR, "dati.pkl")

class Dati:
    def __init__(self, file_path=None):
        self._custom_path = file_path
        self.ordini = []          # Ordini attivi in corso
        self.storico_ordini = []  # ARCHIVIO: Ordini completati e saldati
        self.contratti = []
        self.dipendenti = []
        self.prodotti = []
        self.manager = None
        self.prossimo_id_ordine = 1 # CONTATORE SEQUENZIALE

    @property
    def file_path(self):
        """Ritorna sempre il percorso assoluto dinamico del PC in uso"""
        return self._custom_path or FILE_DATI_PREDEFINITO

    def generaNuovoIdOrdine(self):
        """Genera un ID sequenziale incrementale che non si ripete mai"""
        id_attuale = self.prossimo_id_ordine
        self.prossimo_id_ordine += 1
        return id_attuale

    def salvaTutto(self, nomeFile=None):
        target_path = nomeFile if (nomeFile and nomeFile not in ["dati.pkl", "dati.txt"]) else self.file_path

        try:
            cartella = os.path.dirname(target_path)
            if cartella:
                os.makedirs(cartella, exist_ok=True)

            with open(target_path, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Errore nel salvataggio ({target_path}): {e}")

    def caricaDati(self, nomeFile=None):
        target_path = nomeFile if (nomeFile and nomeFile not in ["dati.pkl", "dati.txt"]) else self.file_path

        try:
            with open(target_path, "rb") as file:
                obj = pickle.load(file)
                self.__dict__.update(obj.__dict__)
                
                # Annulla l'eventuale percorso salvato da un altro PC
                self._custom_path = None
                
                # Verifiche di sicurezza
                if not hasattr(self, 'storico_ordini'):
                    self.storico_ordini = []
                if not hasattr(self, 'prossimo_id_ordine'):
                    self.prossimo_id_ordine = 1
        except Exception as e:
            print(f"Errore nel caricamento ({target_path}): {e}")