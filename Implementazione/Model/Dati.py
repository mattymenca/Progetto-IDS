from .Ordine.StatoOrdine import StatoOrdine
from .Ordine.ordine import Ordine
from .Magazzino.Magazzino import Magazzino
from .Magazzino.Prodotto import Prodotto
import pickle
from .Conto.Conto import Conto
from .Conto.MetodoPagamento import MetodoPagamento
from .Magazzino.StatoProdotto import StatoProdotto
from .Utente.Contratto import Contratto
from .Utente.Dipendente import Dipendente
from .Utente.Manager import Manager
class Dati:
    def __init__(self):
        self.ordini = []
        self.contratti = []
        self.dipendenti = []
        self.prodotti = []
        self.manager = None
        
    def salvaTutto(self, nomeFile):
        try:
            with open(nomeFile, "wb") as file:
                pickle.dump(self, file)
        except (IOError, pickle.PicklingError) as e:
            print(f"Errore nel salvataggio dei dati: {e}")
        pass
    
    def caricaDati(self, nomeFile):
        try:
            with open(nomeFile, "rb") as file:
                dati = pickle.load(file)
        except (IOError, pickle.UnpicklingError) as e:
            print(f"Errore nel caricamento dei dati: {e}")
            

        
    