import pickle

class Dati:
    def __init__(self):
        self.ordini = []          # Ordini attivi in corso
        self.storicoOrdini = []  # ARCHIVIO: Ordini completati e saldati
        self.contratti = []
        self.dipendenti = []
        self.prodotti = []
        self.manager = None
        self.prossimoIdOrdine = 1 # CONTATORE SEQUENZIALE (1, 2, 3...)

    def generaNuovoIdOrdine(self):
        """Genera un ID sequenziale incrementale che non si ripete mai"""
        id_attuale = self.prossimoIdOrdine
        self.prossimoIdOrdine += 1
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
                if not hasattr(self, 'storicoOrdini'):
                    self.storicoOrdini = []
                if not hasattr(self, 'prossimoIdOrdine'):
                    self.prossimoIdOrdine = 1
        except Exception as e:
            print(f"Errore nel caricamento: {e}")