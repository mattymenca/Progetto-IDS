from .StatoOrdine import StatoOrdine
from .ProdottoOrdinato import ProdottoOrdinato

class Ordine:

    def __init__(self, id, prodottiOrdinati: list[ProdottoOrdinato], numeroCoperti):
        self.id = id
        self.prodottiOrdinati = prodottiOrdinati
        self.numeroCoperti = numeroCoperti
        self.statoOrdine = None

    def getId(self):
        return self.id
    
    def getStatoOrdine(self):
        return self.statoOrdine
    
    def getNumeroCoperti(self):
        return self.numeroCoperti
    
    def getProdottiOrdinati(self):
        return self.prodottiOrdinati
    
    def aggiungiProdottoOrdinato(self, prodottoDaAggiungere: ProdottoOrdinato):
        self.prodottiOrdinati.append(prodottoDaAggiungere)

    def rimuoviProdottoOrdinato(self, prodottoDaRimuovere: ProdottoOrdinato):
        self.prodottiOrdinati.remove(prodottoDaRimuovere)

    def setNumeroCoperti(self, numeroCoperti):
        self.numeroCoperti = numeroCoperti

    def setStatoOrdine(self, statoOrdine: StatoOrdine):
        self.statoOrdine = statoOrdine
