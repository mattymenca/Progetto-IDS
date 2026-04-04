from .MetodoPagamento import MetodoPagamento
from Model.Ordine.ordine import Ordine

class Conto:
    
    def __init__(self, idOrdine: int, metodoPagamento: MetodoPagamento):
        self.idOrdine = idOrdine
        self.metodoPagamento = metodoPagamento
        self.totale = 0.0
        
    def getIdOrdine(self):
        return self.idOrdine
    
    # def getTotale(self):
    #     return self.totale
    
    def getMetodoPagamento(self):
        return self.metodoPagamento
    
    def setTotale(self, totale: float):
        self.totale = totale
          
    def setMetodoPagamento(self, nuovoMetodoPagamento: MetodoPagamento):
        self.metodoPagamento = nuovoMetodoPagamento
            
