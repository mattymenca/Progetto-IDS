import pickle

class Dati:
    def __init__(self):
        self.ordini = []          # Ordini attivi in corso
        self.storico_ordini = []  # ARCHIVIO: Ordini completati e saldati
        self.contratti = []
        self.dipendenti = []
        self.prodotti = []
        self.conti = []
        self.manager = None
        self.is_dirty = False     # Flag per indicare se i dati sono stati modificati
        self.prossimo_id_ordine = 1 # CONTATORE SEQUENZIALE (1, 2, 3...)

    def genera_nuovo_id_ordine(self):
        """Genera un ID sequenziale incrementale che non si ripete mai"""
        id_attuale = self.prossimo_id_ordine
        self.prossimo_id_ordine += 1
        self.setDirty() # Generare un ID modifica lo stato
        return id_attuale

    def setDirty(self):
        self.is_dirty = True

    def salvaTutto(self, nomeFile):
        # Se i dati non sono stati modificati, non esegue scritture inutili su disco
        if not self.is_dirty:
            return True
        try:
            with open(nomeFile, "wb") as file:
                # Il flag viene messo a false prima di salvare
                self.is_dirty = False
                pickle.dump(self, file)
            return True
        except Exception as e:
            print(f"Errore nel salvataggio dei dati: {e}")
            self.is_dirty = True # Rimettiamo a True perché il salvataggio è fallito
            return False

    def caricaDati(self, nomeFile):
        try:
            with open(nomeFile, "rb") as file:
                obj = pickle.load(file)
                self.__dict__.update(obj.__dict__)
                
                # Verifiche di sicurezza per retrocompatibilità con vecchi file pickle
                if not hasattr(self, 'storico_ordini'):
                    self.storico_ordini = []
                if not hasattr(self, 'prossimo_id_ordine'):
                    self.prossimo_id_ordine = 1
                if not hasattr(self, 'is_dirty'):
                    self.is_dirty = False
                    
        except Exception as e:
            print(f"Errore nel caricamento dei dati: {e}")