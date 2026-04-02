from Model.Dati import Dati
from Model.Magazzino.Magazzino import Magazzino
from Model.Ordine import StatoOrdine
from Model.Ordine.ProdottoOrdinato import ProdottoOrdinato
from Model.Ordine.ordine import Ordine

class GestoreOrdini:
    
    def __init__(self, dati: Dati):
        self.dati = dati
        
    def creaNuovoOrdine(self, id: int, prodottiOrdinati: list[ProdottoOrdinato], numeroCoperti: int, magazzino: Magazzino):
        nuovoOrdine = Ordine(id, prodottiOrdinati, numeroCoperti)
        if self.approvaOrdine(nuovoOrdine, magazzino):
            self.dati.ordini.append(nuovoOrdine)
            self.dati.setDirty()
            return True
        return False
    
    def approvaOrdine(self, ordine: Ordine, magazzino: Magazzino) -> bool:
        for prodottoOrdinato in ordine.getProdottiOrdinati():
            nomeProdotto = prodottoOrdinato.getNome()
            if magazzino.prodottoDaInventario(nomeProdotto) is None or prodottoOrdinato.getQuantita() > magazzino.prodottoDaInventario(nomeProdotto).getQuantita():
                self.impostaStatoOrdine(ordine, "non approvato")
                print("Ordine non approvato\n")
                return False
            
        self.impostaStatoOrdine(ordine, "in corso")
        print("Ordine in corso\n")
        return True
    
    def impostaStatoOrdine(self, ordine: Ordine, stato: StatoOrdine):
        ordine.setStato(stato)
        self.dati.setDirty()
        
    def concludiOrdine(self, ordine: Ordine):
        self.impostaStatoOrdine(ordine, "concluso")
    
    def restituisciOrdine(self, idOrdine) -> Ordine:
        for ordine in self.dati.ordini:
            if idOrdine == ordine.getId():
                return ordine
        return None
    
    def eliminaOrdine(self, idOrdine: int):
        for ordine in self.dati.ordini:
            if idOrdine == ordine.getId():
                self.dati.ordini.remove(ordine)
                self.dati.setDirty()  
                return True 
        return False