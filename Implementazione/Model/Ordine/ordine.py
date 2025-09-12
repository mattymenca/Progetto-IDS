from Implementazione.Model.Ordine.StatoOrdine import StatoOrdine
from Implementazione.Model.Ordine.ProdottoOrdinato import ProdottoOrdinato

class Ordine:

    def __init__(self, id, prodottiOrdinati: list[ProdottoOrdinato], numeroCoperti, statoOrdine:StatoOrdine):
        self.id = id
        self.prodottiOrdinati = prodottiOrdinati
        self.numeroCoperti = numeroCoperti
        self.statoOrdine = statoOrdine

    def getId(self):
        return self.id
    
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
