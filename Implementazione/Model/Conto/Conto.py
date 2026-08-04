from .MetodoPagamento import MetodoPagamento
from Model.Ordine.ordine import Ordine

class Conto:
    def __init__(self, ordine: Ordine, metodoPagamento: MetodoPagamento):
        self.ordine = ordine
        self.metodoPagamento = metodoPagamento
        self.totale = 0
        
    def getIdOrdine(self):
        return self.ordine.getId() # Corretto: prima cercava un self.idOrdine inesistente
    
    def getTotale(self):
        return self.totale
    
    def getMetodoPagamento(self):
        return self.metodoPagamento
    
    def calcolaTotale(self): 
        totale = 2 * self.ordine.getNumeroCoperti()
        for prodotto in self.ordine.getProdottiOrdinati():
            totale += prodotto.getPrezzo() * prodotto.getQuantita()
        self.totale = totale
        return totale
          
    def setMetodoPagamento(self, nuovoMetodoPagamento: MetodoPagamento):
        self.metodoPagamento = nuovoMetodoPagamento