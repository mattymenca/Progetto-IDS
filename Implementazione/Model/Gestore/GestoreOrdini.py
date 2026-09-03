from Model.Dati import Dati
from Model.Magazzino.Magazzino import Magazzino
from Model.Ordine import StatoOrdine
from Model.Ordine.ProdottoOrdinato import ProdottoOrdinato
from Model.Ordine.ordine import Ordine

class GestoreOrdini:
    
    @staticmethod
    def creaNuovoOrdine(id: int, prodottiOrdinati: list[ProdottoOrdinato], numeroCoperti: int, dati: Dati, magazzino: Magazzino):
        nuovoOrdine = Ordine(id, prodottiOrdinati, numeroCoperti)
        dati.ordini.append(nuovoOrdine)
        GestoreOrdini.approvaOrdine(nuovoOrdine, magazzino)
        
    @staticmethod
    def approvaOrdine(ordine: Ordine, magazzino: Magazzino) -> bool:
        if ordine is None:
            return False
        
        for prodottoOrdinato in ordine.getProdottiOrdinati():
            nomeProdotto = prodottoOrdinato.getNome()
            prodotto = magazzino.prodottoDaInventario(nomeProdotto)

            if prodotto is None or prodottoOrdinato.getQuantita() > prodotto.getQuantita():
                GestoreOrdini.impostaStatoOrdine(ordine, StatoOrdine.NON_APPROVATO)
                print("Ordine non approvato\n")
                return False

        GestoreOrdini.impostaStatoOrdine(ordine, StatoOrdine.IN_CORSO)
        print("Ordine in corso\n")
        return True
            
    @staticmethod
    def impostaStatoOrdine(ordine: Ordine, stato: StatoOrdine):
        if ordine is not None:
            ordine.setStatoOrdine(stato)
            return True
        return False
    
    @staticmethod
    def concludiOrdine(ordine: Ordine):
        return GestoreOrdini.impostaStatoOrdine(ordine, StatoOrdine.CONCLUSO)
    
    @staticmethod
    def restituisciOrdine(idOrdine: int, ordini: list[Ordine]):
        for ordine in ordini:
            if idOrdine == ordine.getId():
                return ordine
        return None
    
    @staticmethod
    def eliminaOrdine(ordine: Ordine, ordini: list[Ordine]):
        if ordine in ordini:
            ordini.remove(ordine)
            return True
        return False
