from .StatoOrdine import StatoOrdine
from .ProdottoOrdinato import ProdottoOrdinato

class Ordine:

    def __init__(self, idOrdine, prodottiOrdinati: list[ProdottoOrdinato], numeroCoperti):
        self.idOrdine = idOrdine
        self.prodottiOrdinati = prodottiOrdinati
        self.numeroCoperti = numeroCoperti
        self.statoOrdine = None

    def getId(self):
        return self.idOrdine
    
    def getStato(self):
        return self.statoOrdine
    
    def getNumeroCoperti(self):
        return self.numeroCoperti
    
    def getProdottiOrdinati(self):
        return self.prodottiOrdinati
    
    def aggiungiProdotto(self, prodottoOrdinato: ProdottoOrdinato):
        self.prodottiOrdinati.append(prodottoOrdinato)

    def rimuoviProdotto(self, prodottoOrdinato: list[ProdottoOrdinato]):
        self.prodottiOrdinati.remove(prodottoOrdinato)

    def setNumeroCoperti(self, numeroCoperti):
        self.numeroCoperti = numeroCoperti

    def setStato(self, statoOrdine: StatoOrdine):
        self.statoOrdine = statoOrdine
