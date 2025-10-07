from .Ordine.StatoOrdine import StatoOrdine
from .Ordine.Ordine import Ordine
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
    
    #salva su file con pickle    
    def salvaTutto(self, nomeFile):
        try:
            with open(nomeFile, "wb") as file:
                pickle.dump(self, file)
        except (IOError, pickle.PicklingError) as e:
            print(f"Errore nel salvataggio dei dati: {e}")
        pass
    
    #carica dati in ram, mettendo tutto dentro i vari attributi della classe Dati 
    def caricaDati(self, nomeFile):
        try:
            with open(nomeFile, "rb") as file:
                obj = pickle.load(file) 
                self.__dict__.update(obj.__dict__)
        except (IOError, pickle.UnpicklingError) as e:
            print(f"Errore nel caricamento dei dati: {e}")
            

        
    