import pickle

class Dati:
    def __init__(self):
        self.ordini = []          # Ordini attivi in corso
        self.storico_ordini = []  # ARCHIVIO: Ordini completati e saldati
        self.contratti = []
        self.dipendenti = []
        self.prodotti = []
        self.manager = None
        self.prossimo_id_ordine = 1 # CONTATORE SEQUENZIALE (1, 2, 3...)

    def genera_nuovo_id_ordine(self):
        """Genera un ID sequenziale incrementale che non si ripete mai"""
        id_attuale = self.prossimo_id_ordine
        self.prossimo_id_ordine += 1
        return id_attuale

    def salvaTutto(self, nomeFile):
        try:
            with open(nomeFile, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Errore nel salvataggio: {e}")

    def caricaDati(self, nomeFile):
        try:
            with open(nomeFile, "rb") as file:
                obj = pickle.load(file)
                self.__dict__.update(obj.__dict__)
                
                # Verifiche di sicurezza per retrocompatibilità
                if not hasattr(self, 'storico_ordini'):
                    self.storico_ordini = []
                if not hasattr(self, 'prossimo_id_ordine'):
                    self.prossimo_id_ordine = 1
        except Exception as e:
            print(f"Errore nel caricamento: {e}")