from Model.Dati import Dati
from Model.Magazzino.Magazzino import Magazzino
from Model.Ordine.StatoOrdine import StatoOrdine
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
    
    def approvaOrdine(self, ordine: Ordine, magazzino: Magazzino):
        for prodottoOrdinato in ordine.getProdottiOrdinati():
            nomeProdotto = prodottoOrdinato.getNome()
            prodottoDaInventario = magazzino.prodottoDaInventario(nomeProdotto)
            if prodottoDaInventario is None or prodottoOrdinato.getQuantita() > prodottoDaInventario.getQuantita():
                self.impostaStatoOrdine(ordine, StatoOrdine.NON_APPROVATO)
                print("Ordine non approvato\n")
                return False
            
        self.impostaStatoOrdine(ordine, StatoOrdine.IN_CORSO)
        print("Ordine in corso\n")
        return True
    
    def impostaStatoOrdine(self, ordine: Ordine, stato: StatoOrdine):
        ordine.setStato(stato)
        self.dati.setDirty()
        
    def concludiOrdine(self, ordine: Ordine):
        self.impostaStatoOrdine(ordine, StatoOrdine.CONCLUSO)
    
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