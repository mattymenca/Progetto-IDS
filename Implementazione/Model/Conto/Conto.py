from .MetodoPagamento import MetodoPagamento
from Model.Ordine.ordine import Ordine

class Conto:
    def __init__(self, ordine: Ordine, metodoPagamento: MetodoPagamento, totale: float):
        self.ordine = ordine
        self.metodoPagamento = metodoPagamento
        self.totale = totale
        
    def getIdOrdine(self):
        return self.ordine.getId()
    
    def getTotale(self):
        return self.totale
    
    def getMetodoPagamento(self):
        return self.metodoPagamento
    
    def setMetodoPagamento(self, nuovoMetodoPagamento: MetodoPagamento):
        self.metodoPagamento = nuovoMetodoPagamento