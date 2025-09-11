from StatoOrdine import StatoOrdine
from Ordine import Ordine
from Magazzino import Magazzino
from Prodotto import Prodotto
import pickle

class Dati:
    def setOrdini(self, ordini):
        pass
    def setContratti(self, contratti):
        pass
    def setMagazzino(self, magazzino):
        pass
    def setDipendenti(self, dipendenti):
        pass
    def setManager(self, manager):
        pass
    def salvaTutto(self):
        pickle.dump(self)
        pass

class Gestore:
    @staticmethod
    def approvaOrdine(ordine: Ordine, magazzino: Magazzino) -> bool:
        for prodottoOrdinato in ordine.getProdottiOrdinati():
            nomeProdotto = prodottoOrdinato.getNome()
            if prodottoOrdinato.getQuantita() > magazzino.prodottoDaInventario(nomeProdotto).getQuantita():
                Gestore.impostaStatoOrdine("non approvato")
                return False
        Gestore.impostaStatoOrdine("in corso")
        return True
    
    # @staticmethod
    # def valida_ordine(ordine: Ordine, magazzino: Magazzino) -> bool:
    #     return all(
    #         p.getQuantita() <= magazzino.prodottoDaInventario(p.getNome()).getQuantita()
    #         for p in ordine.getProdottiOrdinati()
    #     )

    @staticmethod
    def impostaStatoOrdine(ordine: Ordine, stato: StatoOrdine):
        ordine.setStato(stato)
    
