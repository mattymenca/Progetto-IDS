from MetodoPagamento import MetodoPagamento

class Conto:
    
    def __init__(self, idOrdine, metodoPagamento: MetodoPagamento):
        self.idOrdine = idOrdine
        self.metodoPagamento = metodoPagamento
        self.totale = 0
        
    def getIdOrdine(self):
        return self.idOrdine
    
    def getTotale(self):
        return self.totale
    
    def getMetodoPagamento(self):
        return self.metodoPagamento
    
    def calcolaTotale(self):
        for ordine in self.ordini:
            for prodotto in prodottiOrdinati:
                totale += prodotto.getPrezzo * prodotto.getQuantitaOrdinata
                
    def setMetodoPagamento(self, nuovoMetodoPagamento: MetodoPagamento):
        self.metodoPagamento = nuovoMetodoPagamento
            
