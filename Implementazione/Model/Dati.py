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
        self.conti = []
        self.manager = None
        #flag per indicare se i dati sono stati già salvati o no
        self.is_dirty = False
    
    #salva su file con pickle    
    def salvaTutto(self, nomeFile):
        #se i dati sono stati già salvati, non esegue il salvataggio
        if not self.is_dirty:
            return True
        
        try:
            with open(nomeFile, "wb") as file:
                #il flag viene messo a false prima di salvarlo su file
                self.is_dirty = False
                pickle.dump(self, file)
                return True
        except (IOError, pickle.PicklingError) as e:
            print(f"Errore nel salvataggio dei dati: {e}")
            return False
    
    #carica dati in ram, mettendo tutto dentro i vari attributi della classe Dati 
    def caricaDati(self, nomeFile):
        try:
            with open(nomeFile, "rb") as file:
                obj = pickle.load(file) 
                self.__dict__.update(obj.__dict__)
        except (IOError, pickle.UnpicklingError) as e:
            print(f"Errore nel caricamento dei dati: {e}")
    
    def setDirty(self):
        self.is_dirty = True
                

        
    
